""" Unit tests for the SqliteCaseReader. """
from __future__ import print_function

import errno
import os
import unittest
import warnings
from shutil import rmtree
from tempfile import mkdtemp, mkstemp

import numpy as np
from six import iteritems, assertRaisesRegex


from openmdao.api import Problem, Group, IndepVarComp, ExecComp, NonlinearRunOnce, \
    NonlinearBlockGS, LinearBlockGS, ScipyOptimizeDriver, NewtonSolver
from openmdao.recorders.sqlite_recorder import SqliteRecorder, format_version
from openmdao.recorders.case_reader import CaseReader
from openmdao.recorders.sqlite_reader import SqliteCaseReader
from openmdao.recorders.recording_iteration_stack import recording_iteration
from openmdao.core.tests.test_units import SpeedComp
from openmdao.test_suite.components.paraboloid import Paraboloid
from openmdao.test_suite.components.sellar import SellarDerivativesGrouped, \
    SellarDis1withDerivatives, SellarDis2withDerivatives, SellarProblem
from openmdao.utils.assert_utils import assert_rel_error
from openmdao.utils.general_utils import set_pyoptsparse_opt

# check that pyoptsparse is installed
OPT, OPTIMIZER = set_pyoptsparse_opt('SLSQP')
if OPTIMIZER:
    from openmdao.drivers.pyoptsparse_driver import pyOptSparseDriver


class TestSqliteCaseReader(unittest.TestCase):

    def setUp(self):
        recording_iteration.stack = []  # reset to avoid problems from earlier tests

        self.orig_dir = os.getcwd()
        self.temp_dir = mkdtemp()
        os.chdir(self.temp_dir)

        self.filename = os.path.join(self.temp_dir, "sqlite_test")
        self.recorder = SqliteRecorder(self.filename)

    def tearDown(self):
        os.chdir(self.orig_dir)
        try:
            rmtree(self.temp_dir)
        except OSError as e:
            # If directory already deleted, keep going
            if e.errno not in (errno.ENOENT, errno.EACCES, errno.EPERM):
                raise e

    def test_bad_filetype(self):
        # Pass it a plain text file.
        fd, filepath = mkstemp()
        with os.fdopen(fd, 'w') as tmp:
            tmp.write("Lorem ipsum")
            tmp.close()

        with self.assertRaises(IOError) as cm:
            _ = CaseReader(filepath)

        self.assertTrue(str(cm.exception).startswith('File does not contain a valid sqlite database'))

    def test_bad_filename(self):

        with self.assertRaises(IOError) as cm:
            _ = CaseReader('junk.sql')

        self.assertTrue(str(cm.exception).startswith('File does not exist'))

    def test_format_version(self):
        prob = SellarProblem()
        prob.model.add_recorder(self.recorder)
        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        self.assertEqual(cr.format_version, format_version,
                         msg='format version not read correctly')

    def test_reader_instantiates(self):
        """ Test that CaseReader returns an SqliteCaseReader. """
        prob = SellarProblem()
        prob.model.add_recorder(self.recorder)
        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        self.assertTrue(isinstance(cr, SqliteCaseReader),
                        msg='CaseReader not returning the correct subclass.')

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_reading_driver_cases(self):
        """ Tests that the reader returns params correctly. """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9
        driver.recording_options['record_desvars'] = True
        driver.recording_options['record_responses'] = True
        driver.recording_options['record_objectives'] = True
        driver.recording_options['record_constraints'] = True
        driver.recording_options['record_derivatives'] = True
        driver.add_recorder(self.recorder)

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 7)
        self.assertEqual(cr.driver_derivative_cases.num_cases, 6)
        self.assertEqual(cr.system_cases.num_cases, 0)
        self.assertEqual(cr.solver_cases.num_cases, 0)

        # Test to see if the access by case keys works:
        seventh_slsqp_iteration_case = cr.driver_cases.get_case('rank0:SLSQP|5')
        np.testing.assert_almost_equal(seventh_slsqp_iteration_case.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        deriv_case = cr.driver_derivative_cases.get_case('rank0:SLSQP|3')
        np.testing.assert_almost_equal(deriv_case.totals['obj', 'pz.z'],
                                       [[3.8178954 , 1.73971323]],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # While thinking about derivatives, let's get them all.
        derivs = deriv_case.get_derivatives()

        self.assertEqual(set(derivs.keys),
                         set([('obj', 'z'), ('con2', 'z'), ('con1', 'x'), ('obj', 'x'), ('con2', 'x'), ('con1', 'z')]))

        # Test values from one case, the last case
        last_case = cr.driver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.driver_cases.list_cases()
        print (case_keys)
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}'.format(i))

    def test_feature_reading_derivatives(self):
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = ScipyOptimizeDriver(optimizer='SLSQP')
        driver.recording_options['record_derivatives'] = True
        driver.add_recorder(self.recorder)

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        # Get derivatives associated with the first iteration.
        deriv_case = cr.driver_derivative_cases.get_case('rank0:SLSQP|1')

        # Get all derivatives from that case.
        derivs = deriv_case.get_derivatives()

        # See what derivatives have been recorded.
        self.assertEqual(set(derivs.keys),
                         set([('obj', 'z'), ('con2', 'z'), ('con1', 'x'), ('obj', 'x'), ('con2', 'x'), ('con1', 'z')]))

        # Get specific derivative.
        assert_rel_error(self, derivs['obj', 'z'], [[9.61001056, 1.78448534]], 1e-4)

    def test_reading_system_cases(self):
        prob = SellarProblem()
        model = prob.model

        model.recording_options['record_inputs'] = True
        model.recording_options['record_outputs'] = True
        model.recording_options['record_residuals'] = True
        model.recording_options['record_metadata'] = False

        model.add_recorder(self.recorder)

        prob.setup()

        model.d1.add_recorder(self.recorder)  # SellarDis1withDerivatives (an ExplicitComp)
        model.obj_cmp.add_recorder(self.recorder)  # an ExecComp

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 0)
        self.assertEqual(cr.system_cases.num_cases, 15)
        self.assertEqual(cr.solver_cases.num_cases, 0)

        # Test values from cases
        second_last_case = cr.system_cases.get_case(-2)
        np.testing.assert_almost_equal(second_last_case.inputs['y2'], [12.05848815, ],
                                       err_msg='Case reader gives '
                                       'incorrect input value for {0}'.format('obj_cmp.y2'))
        np.testing.assert_almost_equal(second_last_case.outputs['obj'], [28.58830817, ],
                                       err_msg='Case reader gives '
                                       'incorrect output value for {0}'.format('obj_cmp.obj'))
        np.testing.assert_almost_equal(second_last_case.residuals['obj'], [0.0, ],
                                       err_msg='Case reader gives '
                                       'incorrect residual value for {0}'.format('obj_cmp.obj'))

        # Test to see if the case keys ( iteration coords ) come back correctly
        case_keys = cr.system_cases.list_cases()[:-1]  # Skip the last one
        for i, iter_coord in enumerate(case_keys):
            if i % 2 == 0:
                last_solver = 'd1._solve_nonlinear'
            else:
                last_solver = 'obj_cmp._solve_nonlinear'
            solver_iter_count = i // 2
            self.assertEqual(iter_coord,
                             'rank0:Driver|0|root._solve_nonlinear|0|NonlinearBlockGS|{iter}|'
                             '{solver}|{iter}'.format(iter=solver_iter_count, solver=last_solver))

    def test_reading_solver_cases(self):
        prob = SellarProblem()
        prob.setup()

        solver = prob.model.nonlinear_solver
        solver.add_recorder(self.recorder)

        solver.recording_options['record_abs_error'] = True
        solver.recording_options['record_rel_error'] = True
        solver.recording_options['record_solver_residuals'] = True

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 0)
        self.assertEqual(cr.system_cases.num_cases, 0)
        self.assertEqual(cr.solver_cases.num_cases, 7)

        # Test values from cases
        last_case = cr.solver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.abs_err, [0.0, ],
                                       err_msg='Case reader gives incorrect value for abs_err')
        np.testing.assert_almost_equal(last_case.rel_err, [0.0, ],
                                       err_msg='Case reader gives incorrect value for rel_err')
        np.testing.assert_almost_equal(last_case.outputs['x'], [1.0, ],
                                       err_msg='Case reader gives '
                                       'incorrect output value for {0}'.format('x'))
        np.testing.assert_almost_equal(last_case.residuals['con2'], [0.0, ],
                                       err_msg='Case reader gives '
                                       'incorrect residual value for {0}'.format('con_cmp2.con2'))

        # Test to see if the case keys ( iteration coords ) come back correctly
        case_keys = cr.system_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord,
                             'rank0:Driver|0|root._solve_nonlinear|0|NonlinearBlockGS|{}'
                             .format(i))

    def test_reading_metadata(self):
        prob = Problem()
        model = prob.model

        # the Sellar problem but with units
        model.add_subsystem('px', IndepVarComp('x', 1.0, units='m', lower=-1000, upper=1000), promotes=['x'])
        model.add_subsystem('pz', IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])
        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])
        model.add_subsystem('obj_cmp', ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                            z=np.array([0.0, 0.0]), x={'value': 0.0, 'units': 'm'},
                            y1={'units': 'm'}, y2={'units': 'cm'}),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        model.nonlinear_solver = NonlinearBlockGS()
        model.linear_solver = LinearBlockGS()

        model.add_design_var('z', lower=np.array([-10.0, 0.0]), upper=np.array([10.0, 10.0]))
        model.add_design_var('x', lower=0.0, upper=10.0)
        model.add_objective('obj')
        model.add_constraint('con1', upper=0.0)
        model.add_constraint('con2', upper=0.0)

        prob.driver.add_recorder(self.recorder)

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        self.assertEqual(cr.output2meta['x']['units'], 'm')
        self.assertEqual(cr.input2meta['obj_cmp.y1']['units'], 'm')
        self.assertEqual(cr.input2meta['obj_cmp.y2']['units'], 'cm')
        self.assertEqual(cr.input2meta['d1.x']['units'], None)
        self.assertEqual(cr.input2meta['d1.y1']['units'], None)
        self.assertEqual(cr.input2meta['d1.y2']['units'], None)
        self.assertEqual(cr.output2meta['x']['explicit'], True)
        self.assertEqual(cr.output2meta['x']['type'], ['output', 'desvar'])
        self.assertEqual(cr.input2meta['obj_cmp.y1']['explicit'], True)
        self.assertEqual(cr.input2meta['obj_cmp.y2']['explicit'], True)
        self.assertEqual(cr.output2meta['x']['lower'], -1000)
        self.assertEqual(cr.output2meta['x']['upper'], 1000)
        self.assertEqual(cr.output2meta['y2']['upper'], None)
        self.assertEqual(cr.output2meta['y2']['lower'], None)

    def test_reading_solver_metadata(self):
        prob = SellarProblem(linear_solver=LinearBlockGS())
        prob.setup()

        prob.model.nonlinear_solver.add_recorder(self.recorder)
        prob.model.linear_solver.add_recorder(self.recorder)

        d1 = prob.model.d1  # SellarDis1withDerivatives (an ExplicitComponent)
        d1.nonlinear_solver = NonlinearBlockGS(maxiter=5)
        d1.nonlinear_solver.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        self.assertEqual(
            sorted(cr.solver_metadata.keys()),
            sorted(['root.LinearBlockGS', 'root.NonlinearBlockGS', 'd1.NonlinearBlockGS'])
        )
        self.assertEqual(cr.solver_metadata['d1.NonlinearBlockGS']['solver_options']['maxiter'], 5)
        self.assertEqual(cr.solver_metadata['root.NonlinearBlockGS']['solver_options']['maxiter'],10)
        self.assertEqual(cr.solver_metadata['root.LinearBlockGS']['solver_class'],'LinearBlockGS')

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_reading_driver_recording_with_system_vars(self):
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9
        driver.recording_options['record_desvars'] = True
        driver.recording_options['record_responses'] = True
        driver.recording_options['record_objectives'] = True
        driver.recording_options['record_constraints'] = True
        driver.recording_options['includes'] = ['mda.d2.y2',]
        driver.add_recorder(self.recorder)

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        # Test values from one case, the last case
        last_case = cr.driver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['pz.z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], prob['px.x'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))
        np.testing.assert_almost_equal(last_case.outputs['y2'], prob['mda.d2.y2'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('mda.d2.y2'))

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_get_child_cases(self):
        prob = SellarProblem(SellarDerivativesGrouped, nonlinear_solver=NonlinearRunOnce)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9
        driver.recording_options['record_desvars'] = True
        driver.recording_options['record_responses'] = True
        driver.recording_options['record_objectives'] = True
        driver.recording_options['record_constraints'] = True
        driver.add_recorder(self.recorder)

        prob.setup()

        model = prob.model
        model.add_recorder(self.recorder)
        model.nonlinear_solver.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        expected_coords = [
            'rank0:SLSQP|0',
            'rank0:SLSQP|1',
            'rank0:SLSQP|2',
            'rank0:SLSQP|3',
            'rank0:SLSQP|4',
            'rank0:SLSQP|5',
            'rank0:SLSQP|6',
        ]
        ind = 0
        for c in cr.get_cases():
            self.assertEqual(c.iteration_coordinate, expected_coords[ind])
            ind += 1
        self.assertEqual(ind, len(expected_coords))

        coords_2 = [
            'rank0:SLSQP|0',
            'rank0:SLSQP|0|root._solve_nonlinear|0|NLRunOnce|0',
            'rank0:SLSQP|1',
            'rank0:SLSQP|1|root._solve_nonlinear|1|NLRunOnce|0',
            'rank0:SLSQP|2',
            'rank0:SLSQP|2|root._solve_nonlinear|2|NLRunOnce|0',
            'rank0:SLSQP|3',
            'rank0:SLSQP|3|root._solve_nonlinear|3|NLRunOnce|0',
            'rank0:SLSQP|4',
            'rank0:SLSQP|4|root._solve_nonlinear|4|NLRunOnce|0',
            'rank0:SLSQP|5',
            'rank0:SLSQP|5|root._solve_nonlinear|5|NLRunOnce|0',
            'rank0:SLSQP|6',
            'rank0:SLSQP|6|root._solve_nonlinear|6|NLRunOnce|0'
        ]
        ind = 0
        for c in cr.get_cases(recursive=True):
            self.assertEqual(c.iteration_coordinate, coords_2[ind])
            ind += 1
        self.assertEqual(ind, len(coords_2))

        coord_children = [
            'rank0:SLSQP|0|root._solve_nonlinear|0|NLRunOnce|0'
        ]
        for c in cr.get_cases('rank0:SLSQP|0', True):
            self.assertEqual(c.iteration_coordinate, coord_children[0])

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_get_child_cases_system(self):
        prob = SellarProblem(SellarDerivativesGrouped, nonlinear_solver=NonlinearRunOnce)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9
        prob.setup()

        model = prob.model
        model.add_recorder(self.recorder)
        model.nonlinear_solver.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        coords = [
            'rank0:SLSQP|0|root._solve_nonlinear|0|NLRunOnce|0',
            'rank0:SLSQP|1|root._solve_nonlinear|1|NLRunOnce|0',
            'rank0:SLSQP|2|root._solve_nonlinear|2|NLRunOnce|0',
            'rank0:SLSQP|3|root._solve_nonlinear|3|NLRunOnce|0',
            'rank0:SLSQP|4|root._solve_nonlinear|4|NLRunOnce|0',
            'rank0:SLSQP|5|root._solve_nonlinear|5|NLRunOnce|0',
            'rank0:SLSQP|6|root._solve_nonlinear|6|NLRunOnce|0'
        ]
        ind = 0
        for c in cr.get_cases(recursive=True):
            self.assertEqual(c.iteration_coordinate, coords[ind])
            ind += 1
        self.assertEqual(ind, len(coords))

    def test_list_outputs(self):
        prob = SellarProblem()

        prob.model.add_recorder(self.recorder)
        prob.model.recording_options['record_residuals'] = True

        prob.setup()

        d1 = prob.model.d1  # SellarDis1withDerivatives (an ExplicitComp)
        d1.nonlinear_solver = NonlinearBlockGS(maxiter=5)
        d1.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        outputs = cr.list_outputs(None, True, True, True, True, None, True, True, True,
                                  True, True, True)

        expected_outputs = {
            'd2.y2': {'lower': None, 'ref': 1.0, 'resids': [0.], 'shape': (1,), 'values': [12.0584882]},
            'con_cmp1.con1': {'lower': None, 'ref': 1.0, 'resids': [0.], 'shape': (1,), 'values': [-22.4283024]},
            'pz.z': {'lower': None, 'ref': 1.0, 'resids': [0., 0.], 'shape': (2,), 'values': [5., 2.]},
            'obj_cmp.obj': {'lower': None, 'ref': 1.0, 'resids': [0.], 'shape': (1,), 'values': [28.5883082]},
            'px.x': {'lower': None, 'ref': 1.0, 'resids': [0.], 'shape': (1,), 'values': [1.]},
            'con_cmp2.con2': {'lower': None, 'ref': 1.0, 'resids': [0.], 'shape': (1,), 'values': [-11.9415118]},
            'd1.y1': {'lower': None, 'ref': 1.0, 'resids': [1.318e-10], 'shape': (1,), 'values': [25.5883024]}
        }

        self.assertEqual(len(outputs), 7)
        for o in outputs:
            vals = o[1]
            name = o[0]
            expected = expected_outputs[name]
            self.assertEqual(vals['lower'], expected['lower'])
            self.assertEqual(vals['ref'], expected['ref'])
            self.assertEqual(vals['shape'], expected['shape'])
            np.testing.assert_almost_equal(vals['resids'], expected['resids'])
            np.testing.assert_almost_equal(vals['value'], expected['values'])

        expected_outputs_case = {
            'd1.y1': {'lower': None, 'ref': 1.0, 'resids': [1.318e-10], 'shape': (1,), 'values': [25.5454859]}
        }

        sys_case = cr.system_cases.get_case(1)
        outputs_case = cr.list_outputs(sys_case, True, True, True, True, None, True, True, True,
                                       True, True, True)

        for o in outputs_case:
            vals = o[1]
            name = o[0]
            expected = expected_outputs_case[name]
            self.assertEqual(vals['lower'], expected['lower'])
            self.assertEqual(vals['ref'], expected['ref'])
            self.assertEqual(vals['shape'], expected['shape'])
            np.testing.assert_almost_equal(vals['resids'], expected['resids'])
            np.testing.assert_almost_equal(vals['value'], expected['values'])

        for o in outputs_case:
            vals = o[1]
            name = o[0]
            expected = expected_outputs_case[name]
            self.assertEqual(vals['lower'], expected['lower'])
            self.assertEqual(vals['ref'], expected['ref'])
            self.assertEqual(vals['shape'], expected['shape'])
            np.testing.assert_almost_equal(vals['resids'], expected['resids'])
            np.testing.assert_almost_equal(vals['value'], expected['values'])

        impl_outputs_case = cr.list_outputs(sys_case, False, True)
        self.assertEqual(len(impl_outputs_case), 0)

    def test_list_inputs(self):
        prob = SellarProblem()

        prob.model.add_recorder(self.recorder)
        prob.model.recording_options['record_residuals'] = True

        prob.setup()

        d1 = prob.model.d1  # SellarDis1withDerivatives (an ExplicitComp)
        d1.nonlinear_solver = NonlinearBlockGS(maxiter=5)
        d1.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)

        inputs = cr.list_inputs(None, True, True, True)

        expected_inputs = {
            'obj_cmp.x': {'value': [1.]},
            'd2.z': {'value': [5., 2.]},
            'con_cmp2.y2': {'value': [12.05848815]},
            'obj_cmp.y2': {'value': [12.05848815]},
            'obj_cmp.z': {'value': [5., 2.]},
            'd1.x': {'value': [1.]},
            'd1.z': {'value': [5., 2.]},
            'd1.y2': {'value': [12.05848815]},
            'con_cmp1.y1': {'value': [25.58830237]},
            'obj_cmp.y1': {'value': [25.58830237]},
            'd2.y1': {'value': [25.58830237]}
        }

        self.assertEqual(len(inputs), 11)
        for o in inputs:
            vals = o[1]
            name = o[0]
            expected = expected_inputs[name]
            np.testing.assert_almost_equal(vals['value'], expected['value'])

        expected_inputs_case = {
            'd1.z': {'value': [5., 2.]},
            'd1.x': {'value': [1.]},
            'd1.y2': {'value': [12.27257053]}
        }

        sys_case = cr.system_cases.get_case(1)
        inputs_case = cr.list_inputs(sys_case, True, True, True, None)

        for o in inputs_case:
            vals = o[1]
            name = o[0]
            expected = expected_inputs_case[name]
            np.testing.assert_almost_equal(vals['value'], expected['value'])

    def test_get_vars(self):
        prob = SellarProblem()
        prob.setup()

        prob.model.add_recorder(self.recorder)
        prob.model.recording_options['record_residuals'] = True

        prob.driver.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        driver_case = cr.driver_cases.get_case(0)
        desvars = driver_case.get_desvars()
        objectives = driver_case.get_objectives()
        constraints = driver_case.get_constraints()
        responses = driver_case.get_responses()

        expected_desvars = {"x": 1., "z": [5., 2.]}
        expected_objectives = {"obj": 28.58830817, }
        expected_constraints = {"con1": -22.42830237, "con2": -11.94151185}

        expected_responses = expected_objectives.copy()
        expected_responses.update(expected_constraints)

        for expected_set, actual_set in ((expected_desvars, desvars),
                                         (expected_objectives, objectives),
                                         (expected_constraints, constraints),
                                         (expected_responses, responses)):

            self.assertEqual(len(expected_set), len(actual_set.keys))
            for k in actual_set:
                np.testing.assert_almost_equal(expected_set[k], actual_set[k])

    def test_simple_load_system_cases(self):
        prob = SellarProblem()

        model = prob.model
        model.recording_options['record_inputs'] = True
        model.recording_options['record_outputs'] = True
        model.recording_options['record_residuals'] = True
        model.add_recorder(self.recorder)

        prob.setup()

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        case = cr.system_cases.get_case(0)

        # Add one to all the inputs and outputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in model._inputs:
            model._inputs[name] += 1.0
        for name in model._outputs:
            model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(case)

        _assert_model_matches_case(case, model)

    def test_load_bad_system_case(self):
        prob = SellarProblem(SellarDerivativesGrouped)

        prob.model.add_recorder(self.recorder)

        driver = prob.driver = ScipyOptimizeDriver()
        driver.options['optimizer'] = 'SLSQP'
        driver.options['tol'] = 1e-9
        driver.options['disp'] = False
        driver.recording_options['record_desvars'] = True
        driver.recording_options['record_responses'] = True
        driver.recording_options['record_objectives'] = True
        driver.recording_options['record_constraints'] = True

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        case = cr.system_cases.get_case(0)

        # try to load it into a completely different model
        prob = SellarProblem()
        prob.setup()

        error_msg = "Input variable, '[^']+', recorded in the case is not found in the model"
        with assertRaisesRegex(self, KeyError, error_msg):
            prob.load_case(case)

    def test_subsystem_load_system_cases(self):
        prob = SellarProblem()
        prob.setup()

        model = prob.model
        model.recording_options['record_inputs'] = True
        model.recording_options['record_outputs'] = True
        model.recording_options['record_residuals'] = True

        # Only record a subsystem
        model.d2.add_recorder(self.recorder)

        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        case = cr.system_cases.get_case(0)

        # Add one to all the inputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            model._inputs[name] += 1.0
        for name in prob.model._outputs:
            model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(case)

        _assert_model_matches_case(case, model.d2)

    def test_load_system_cases_with_units(self):
        comp = IndepVarComp()
        comp.add_output('distance', val=1., units='m')
        comp.add_output('time', val=1., units='s')

        prob = Problem()
        model = prob.model
        model.add_subsystem('c1', comp)
        model.add_subsystem('c2', SpeedComp())
        model.add_subsystem('c3', ExecComp('f=speed',speed={'units': 'm/s'}))
        model.connect('c1.distance', 'c2.distance')
        model.connect('c1.time', 'c2.time')
        model.connect('c2.speed', 'c3.speed')

        model.add_recorder(self.recorder)

        prob.setup()
        prob.run_model()

        cr = CaseReader(self.filename)
        case = cr.system_cases.get_case(0)

        # Add one to all the inputs just to change the model
        # so we can see if loading the case values really changes the model
        for name in model._inputs:
            model._inputs[name] += 1.0
        for name in model._outputs:
            model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(case)

        _assert_model_matches_case(case, model)

    def test_optimization_load_system_cases(self):
        prob = SellarProblem(SellarDerivativesGrouped)

        prob.model.add_recorder(self.recorder)

        driver = prob.driver = ScipyOptimizeDriver()
        driver.options['optimizer'] = 'SLSQP'
        driver.options['tol'] = 1e-9
        driver.options['disp'] = False
        driver.recording_options['record_desvars'] = True
        driver.recording_options['record_responses'] = True
        driver.recording_options['record_objectives'] = True
        driver.recording_options['record_constraints'] = True

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        inputs_before = prob.model.list_inputs(values=True, units=True)
        outputs_before = prob.model.list_outputs(values=True, units=True)

        cr = CaseReader(self.filename)
        # get third case
        third_case = cr.system_cases.get_case(2)

        iter_count_before = driver.iter_count

        # run the model again with a fresh model
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = ScipyOptimizeDriver()
        driver.options['optimizer'] = 'SLSQP'
        driver.options['tol'] = 1e-9
        driver.options['disp'] = False

        prob.setup()
        prob.load_case(third_case)
        prob.run_driver()
        prob.cleanup()

        inputs_after = prob.model.list_inputs(values=True, units=True)
        outputs_after = prob.model.list_outputs(values=True, units=True)
        iter_count_after = driver.iter_count

        for before, after in zip(inputs_before, inputs_after):
            np.testing.assert_almost_equal(before[1]['value'], after[1]['value'])

        for before, after in zip(outputs_before, outputs_after):
            np.testing.assert_almost_equal(before[1]['value'], after[1]['value'])

        # Should take one less iteration since we gave it a head start in the second run
        self.assertEqual(iter_count_before, iter_count_after + 1)

    def test_load_solver_cases(self):
        prob = SellarProblem()
        prob.setup()

        model = prob.model
        model.nonlinear_solver = NewtonSolver()
        model.linear_solver = LinearBlockGS()
        model.linear_solver.add_recorder(self.recorder)

        prob.run_model()
        prob.cleanup()

        cr = CaseReader(self.filename)
        case = cr.solver_cases.get_case(0)

        # Add one to all the inputs just to change the model
        # so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            model._inputs[name] += 1.0
        for name in prob.model._outputs:
            model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(case)

        _assert_model_matches_case(case, model)

    def test_load_driver_cases(self):
        prob = Problem()
        model = prob.model

        model.add_subsystem('p1', IndepVarComp('x', 50.0), promotes=['*'])
        model.add_subsystem('p2', IndepVarComp('y', 50.0), promotes=['*'])
        model.add_subsystem('comp', Paraboloid(), promotes=['*'])
        model.add_subsystem('con', ExecComp('c = x - y'), promotes=['*'])

        prob.set_solver_print(level=0)

        prob.driver = ScipyOptimizeDriver()
        prob.driver.options['optimizer'] = 'SLSQP'
        prob.driver.options['tol'] = 1e-9
        prob.driver.options['disp'] = False

        model.add_design_var('x', lower=-50.0, upper=50.0)
        model.add_design_var('y', lower=-50.0, upper=50.0)

        model.add_objective('f_xy')
        model.add_constraint('c', lower=15.0)

        prob.driver.add_recorder(self.recorder)

        prob.set_solver_print(0)

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        cr = CaseReader(self.filename)
        case = cr.driver_cases.get_case(0)

        # Add one to all the inputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            prob.model._inputs[name] += 1.0
        for name in prob.model._outputs:
            prob.model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(case)

        _assert_model_matches_case(case, model)

    def test_system_options_pickle_fail(self):
        # simple paraboloid model
        model = Group()
        ivc = IndepVarComp()
        ivc.add_output('x', 3.0)
        model.add_subsystem('subs', ivc)
        subs = model.subs

        # declare two options
        subs.options.declare('options value 1', 1)
        # Given object which can't be pickled
        subs.options.declare('options value to fail', (i for i in []))
        subs.add_recorder(self.recorder)

        prob = Problem(model)
        prob.setup()

        with warnings.catch_warnings(record=True) as w:
            prob.run_model()

        prob.cleanup()
        cr = CaseReader(self.filename)
        subs_options = cr.system_metadata['subs']['component_options']

        # no options should have been recorded for d1
        self.assertEqual(len(subs_options._dict), 0)

        # make sure we got the warning we expected
        self.assertEqual(len(w), 1)
        self.assertTrue(issubclass(w[0].category, RuntimeWarning))

    def test_loading_cases(self):
        prob = SellarProblem()
        prob.setup()

        prob.add_recorder(self.recorder)
        prob.driver.add_recorder(self.recorder)
        prob.model.add_recorder(self.recorder)
        prob.model.nonlinear_solver.add_recorder(self.recorder)

        prob.run_driver()
        prob.record_iteration('c_1')
        prob.record_iteration('c_2')
        prob.cleanup()

        cr = CaseReader(self.filename)

        self.assertEqual(len(cr.driver_cases._cases), 0)
        self.assertEqual(len(cr.solver_cases._cases), 0)
        self.assertEqual(len(cr.system_cases._cases), 0)
        self.assertEqual(len(cr.problem_cases._cases), 0)

        cr.load_cases()

        # assert that we have now stored each of the cases
        self.assertEqual(len(cr.driver_cases._cases), cr.driver_cases.num_cases)
        self.assertEqual(len(cr.solver_cases._cases), cr.solver_cases.num_cases)
        self.assertEqual(len(cr.system_cases._cases), cr.system_cases.num_cases)
        self.assertEqual(len(cr.problem_cases._cases), cr.problem_cases.num_cases)

        for case_type in (cr.driver_cases, cr.solver_cases,
                          cr.system_cases, cr.problem_cases):
            for case in case_type.list_cases():
                self.assertTrue(case in case_type._cases)
                self.assertEqual(case, case_type._cases[case].iteration_coordinate)

    def test_caching_cases(self):
        prob = SellarProblem()
        prob.setup()

        prob.add_recorder(self.recorder)
        prob.driver.add_recorder(self.recorder)
        prob.model.add_recorder(self.recorder)
        prob.model.nonlinear_solver.add_recorder(self.recorder)

        prob.run_driver()
        prob.record_iteration('c_1')
        prob.record_iteration('c_2')
        prob.cleanup()

        cr = CaseReader(self.filename)

        self.assertEqual(len(cr.driver_cases._cases), 0)
        self.assertEqual(len(cr.solver_cases._cases), 0)
        self.assertEqual(len(cr.system_cases._cases), 0)
        self.assertEqual(len(cr.problem_cases._cases), 0)

        # get cases so they're all cached
        for case_type in (cr.driver_cases, cr.solver_cases,
                          cr.system_cases, cr.problem_cases):
            for case in case_type.list_cases():
                case_type.get_case(case)

        # assert that we have now stored each of the cases
        self.assertEqual(len(cr.driver_cases._cases), cr.driver_cases.num_cases)
        self.assertEqual(len(cr.solver_cases._cases), cr.solver_cases.num_cases)
        self.assertEqual(len(cr.system_cases._cases), cr.system_cases.num_cases)
        self.assertEqual(len(cr.problem_cases._cases), cr.problem_cases.num_cases)

        for case_type in (cr.driver_cases, cr.solver_cases,
                          cr.system_cases, cr.problem_cases):
            for case in case_type.list_cases():
                self.assertTrue(case in case_type._cases)
                self.assertEqual(case, case_type._cases[case].iteration_coordinate)

def _assert_model_matches_case(case, system):
    '''
    Check to see if the values in the case match those in the model.

    Parameters
    ----------
    case : Case object
        Case to be used for the comparison.
    system : System object
        System to be used for the comparison.
    '''
    case_inputs = case.inputs._values
    model_inputs = system._inputs
    for name, model_input in iteritems(model_inputs._views):
        np.testing.assert_almost_equal(case_inputs[name],model_input)

    case_outputs = case.outputs._values
    model_outputs = system._outputs
    for name, model_output in iteritems(model_outputs._views):
        np.testing.assert_almost_equal(case_outputs[name],model_output)


class TestSqliteCaseReaderLegacy(unittest.TestCase):

    def setUp(self):
        recording_iteration.stack = []  # reset to avoid problems from earlier tests

    def test_driver_v3(self):
        """
        Backwards compatibility version 3.
        Legacy case recording file generated using code from test_record_driver_system_solver
        test in test_sqlite_recorder.py
        """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = ScipyOptimizeDriver()
        prob.driver.options['optimizer'] = 'SLSQP'
        prob.driver.options['tol'] = 1e-9
        prob.driver.options['disp'] = False

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        filename = os.path.join(os.path.dirname(__file__), 'legacy_sql')
        filename = os.path.join(filename, 'case_driver_solver_system_03.sql')
        cr = CaseReader(filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 6)

        # Test to see if the access by case keys works:
        seventh_slsqp_iteration_case = cr.driver_cases.get_case('rank0:SLSQP|5')
        np.testing.assert_almost_equal(seventh_slsqp_iteration_case.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # Test values from one case, the last case
        last_case = cr.driver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.driver_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}'.format(i))

        # Test driver metadata
        self.assertIsNotNone(cr.driver_metadata)
        self.assertTrue('tree' in cr.driver_metadata)
        self.assertTrue('connections_list' in cr.driver_metadata)

        # While we are here, make sure we can load this case.

        # Add one to all the inputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            prob.model._inputs[name] += 1.0
        for name in prob.model._outputs:
            prob.model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(seventh_slsqp_iteration_case)

        _assert_model_matches_case(seventh_slsqp_iteration_case, prob.model)

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_driver_v2(self):
        """ Backwards compatibility version 2. """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        filename = os.path.join(os.path.dirname(__file__), 'legacy_sql')
        filename = os.path.join(filename, 'case_driver_solver_system_02.sql')
        cr = CaseReader(filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 7)

        # Test to see if the access by case keys works:
        seventh_slsqp_iteration_case = cr.driver_cases.get_case('rank0:SLSQP|5')
        np.testing.assert_almost_equal(seventh_slsqp_iteration_case.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # Test values from one case, the last case
        last_case = cr.driver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.driver_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}'.format(i))

        # Test driver metadata
        self.assertIsNotNone(cr.driver_metadata)
        self.assertTrue('tree' in cr.driver_metadata)
        self.assertTrue('connections_list' in cr.driver_metadata)

        # While we are here, make sure we can load this case.

        # Add one to all the inputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            prob.model._inputs[name] += 1.0
        for name in prob.model._outputs:
            prob.model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(seventh_slsqp_iteration_case)

        _assert_model_matches_case(seventh_slsqp_iteration_case, prob.model)

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_solver_v2(self):
        """ Backwards compatibility version 2. """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        filename = os.path.join(os.path.dirname(__file__), 'legacy_sql')
        filename = os.path.join(filename, 'case_driver_solver_system_02.sql')
        cr = CaseReader(filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.solver_cases.num_cases, 7)

        # Test to see if the access by case keys works:
        sixth_solver_iteration = cr.solver_cases.get_case('rank0:SLSQP|5|root._solve_nonlinear|5|NLRunOnce|0')
        np.testing.assert_almost_equal(sixth_solver_iteration.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # Test values from one case, the last case
        last_case = cr.solver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.solver_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}|root._solve_nonlinear|{}|NLRunOnce|0'.format(i, i))

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_system_v2(self):
        """ Backwards compatibility version 2. """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        filename = os.path.join(os.path.dirname(__file__), 'legacy_sql')
        filename = os.path.join(filename, 'case_driver_solver_system_02.sql')
        cr = CaseReader(filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.system_cases.num_cases, 7)

        # Test to see if the access by case keys works:
        sixth_system_case = cr.system_cases.get_case('rank0:SLSQP|5|root._solve_nonlinear|5')
        np.testing.assert_almost_equal(sixth_system_case.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # Test values from one case, the last case
        last_case = cr.system_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.system_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}|root._solve_nonlinear|{}'.format(i, i))

        # Test metadata read correctly
        self.assertEqual(cr.output2meta['mda.d2.y2']['type'], {'output'})
        self.assertEqual(cr.output2meta['mda.d2.y2']['size'], 1)
        self.assertTrue(cr.output2meta['mda.d2.y2']['explicit'], {'output'})
        self.assertEqual(cr.input2meta['mda.d1.z']['type'], {'input'})
        self.assertEqual(cr.input2meta['mda.d1.z']['size'], 2)
        self.assertIsNone(cr.input2meta['mda.d1.z']['units'])
        self.assertTrue(cr.output2meta['mda.d2.y2']['explicit'], {'output'})

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_driver_v1(self):
        """ Backwards compatibility oldest version. """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        filename = os.path.join(os.path.dirname(__file__), 'legacy_sql')
        filename = os.path.join(filename, 'case_driver_01.sql')
        cr = CaseReader(filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 7)
        self.assertEqual(cr.system_cases.num_cases, 0)
        self.assertEqual(cr.solver_cases.num_cases, 0)

        # Test to see if the access by case keys works:
        seventh_slsqp_iteration_case = cr.driver_cases.get_case('rank0:SLSQP|5')
        np.testing.assert_almost_equal(seventh_slsqp_iteration_case.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # Test values from one case, the last case
        last_case = cr.driver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.driver_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}'.format(i))

        # While we are here, make sure we can load this case.

        # Add one to all the inputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            prob.model._inputs[name] += 1.0
        for name in prob.model._outputs:
            prob.model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(seventh_slsqp_iteration_case)

        _assert_model_matches_case(seventh_slsqp_iteration_case, prob.model)

    @unittest.skipIf(OPT is None, "pyoptsparse is not installed")
    @unittest.skipIf(OPTIMIZER is None, "pyoptsparse is not providing SNOPT or SLSQP")
    def test_driver_v1_pre_problem(self):
        """ Backwards compatibility oldest version. """
        prob = SellarProblem(SellarDerivativesGrouped)

        driver = prob.driver = pyOptSparseDriver(optimizer='SLSQP')
        driver.options['print_results'] = False
        driver.opt_settings['ACC'] = 1e-9

        prob.setup()
        prob.run_driver()
        prob.cleanup()

        filename = os.path.join(os.path.dirname(__file__), 'legacy_sql')
        filename = os.path.join(filename, 'case_driver_pre01.sql')
        cr = CaseReader(filename)

        # Test to see if we got the correct number of cases
        self.assertEqual(cr.driver_cases.num_cases, 7)
        self.assertEqual(cr.system_cases.num_cases, 0)
        self.assertEqual(cr.solver_cases.num_cases, 0)

        # Test to see if the access by case keys works:
        seventh_slsqp_iteration_case = cr.driver_cases.get_case('rank0:SLSQP|5')
        np.testing.assert_almost_equal(seventh_slsqp_iteration_case.outputs['z'],
                                       [1.97846296,  -2.21388305e-13],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))

        # Test values from one case, the last case
        last_case = cr.driver_cases.get_case(-1)
        np.testing.assert_almost_equal(last_case.outputs['z'], prob['z'],
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('pz.z'))
        np.testing.assert_almost_equal(last_case.outputs['x'], [-0.00309521],
                                       decimal=2,
                                       err_msg='Case reader gives '
                                       'incorrect Parameter value'
                                       ' for {0}'.format('px.x'))

        # Test to see if the case keys (iteration coords) come back correctly
        case_keys = cr.driver_cases.list_cases()
        for i, iter_coord in enumerate(case_keys):
            self.assertEqual(iter_coord, 'rank0:SLSQP|{}'.format(i))

        # While we are here, make sure we can load this case.

        # Add one to all the inputs just to change the model
        #   so we can see if loading the case values really changes the model
        for name in prob.model._inputs:
            prob.model._inputs[name] += 1.0
        for name in prob.model._outputs:
            prob.model._outputs[name] += 1.0

        # Now load in the case we recorded
        prob.load_case(seventh_slsqp_iteration_case)

        _assert_model_matches_case(seventh_slsqp_iteration_case, prob.model)


if __name__ == "__main__":
    unittest.main()
