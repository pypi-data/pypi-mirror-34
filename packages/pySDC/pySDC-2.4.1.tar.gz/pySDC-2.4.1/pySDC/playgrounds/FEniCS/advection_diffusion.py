from pySDC.implementations.sweeper_classes.generic_LU import generic_LU
from pySDC.implementations.problem_classes.AdvectionDiffusion_1D_FEniCS_matrix_periodic import fenics_adv_diff_1d
from pySDC.implementations.datatype_classes.fenics_mesh import fenics_mesh, rhs_fenics_mesh
from pySDC.implementations.collocation_classes.gauss_radau_right import CollGaussRadau_Right
from pySDC.implementations.transfer_classes.TransferFenicsMesh import mesh_to_mesh_fenics
from pySDC.implementations.controller_classes.allinclusive_classic_nonMPI import allinclusive_classic_nonMPI

if __name__ == "__main__":
    num_procs = 1

    t0 = 0
    dt = 0.2
    Tend = 1.6

    # initialize level parameters
    level_params = dict()
    level_params['restol'] = 5E-09
    level_params['dt'] = dt

    # initialize step parameters
    step_params = dict()
    step_params['maxiter'] = 50

    # initialize space transfer parameters
    space_transfer_params = dict()
    space_transfer_params['finter'] = True

    # initialize sweeper parameters
    sweeper_params = dict()
    sweeper_params['collocation_class'] = CollGaussRadau_Right
    sweeper_params['num_nodes'] = [3]

    problem_params = dict()
    problem_params['nu'] = 0.05
    problem_params['mu'] = 1.0
    problem_params['t0'] = t0  # ugly, but necessary to set up ProblemClass
    problem_params['c_nvars'] = [128]
    problem_params['family'] = 'CG'
    problem_params['order'] = [4]
    problem_params['refinements'] = [1, 0]

    # initialize controller parameters
    controller_params = dict()
    controller_params['logger_level'] = 20

    # Fill description dictionary for easy hierarchy creation
    description = dict()
    description['problem_class'] = fenics_adv_diff_1d
    description['problem_params'] = problem_params
    description['dtype_u'] = fenics_mesh
    description['dtype_f'] = rhs_fenics_mesh
    description['sweeper_class'] = generic_LU  # pass sweeper (see part B)
    description['sweeper_params'] = sweeper_params  # pass sweeper parameters
    description['level_params'] = level_params  # pass level parameters
    description['step_params'] = step_params  # pass step parameters
    description['space_transfer_class'] = mesh_to_mesh_fenics  # pass spatial transfer class
    description['space_transfer_params'] = space_transfer_params  # pass paramters for spatial transfer

    # quickly generate block of steps
    controller = allinclusive_classic_nonMPI(num_procs=num_procs, controller_params=controller_params,
                                             description=description)

    # get initial values on finest level
    P = controller.MS[0].levels[0].prob
    uinit = P.u_exact(t0)

    # call main function to get things done...
    uend, stats = controller.run(u0=uinit, t0=t0, Tend=Tend)

    # compute exact solution and compare
    uex = P.u_exact(Tend)

    print('(classical) error at time %s: %s' % (Tend, abs(uex - uend) / abs(uex)))
