from __future__ import division

import dolfin as df
import numpy as np
import logging

from pySDC.core.Problem import ptype
from pySDC.core.Errors import ParameterError


# noinspection PyUnusedLocal
class fenics_heat(ptype):
    """
    Example implementing the forced 1D heat equation with Dirichlet-0 BC in [0,1]

    Attributes:
        V: function space
        M: mass matrix for FEM
        K: stiffness matrix incl. diffusion coefficient (and correct sign)
        g: forcing term
        bc: boundary conditions
    """

    def __init__(self, problem_params, dtype_u, dtype_f):
        """
        Initialization routine

        Args:
            problem_params (dict): custom parameters for the example
            dtype_u: particle data type (will be passed parent class)
            dtype_f: acceleration data type (will be passed parent class)
        """

        # define the Dirichlet boundary
        def Boundary(x, on_boundary):
            return on_boundary

        # these parameters will be used later, so assert their existence
        essential_keys = ['c_nvars', 't0', 'family', 'order', 'refinements', 'nu']
        for key in essential_keys:
            if key not in problem_params:
                msg = 'need %s to instantiate problem, only got %s' % (key, str(problem_params.keys()))
                raise ParameterError(msg)

        # set logger level for FFC and dolfin
        df.set_log_level(df.WARNING)
        logging.getLogger('FFC').setLevel(logging.WARNING)

        # set solver and form parameters
        df.parameters["form_compiler"]["optimize"] = True
        df.parameters["form_compiler"]["cpp_optimize"] = True

        # set mesh and refinement (for multilevel)
        mesh = df.UnitIntervalMesh(problem_params['c_nvars'])
        for i in range(problem_params['refinements']):
            mesh = df.refine(mesh)

        # define function space for future reference
        self.V = df.FunctionSpace(mesh, problem_params['family'], problem_params['order'])
        tmp = df.Function(self.V)
        print('DoFs on this level:', len(tmp.vector().array()))

        # invoke super init, passing number of dofs, dtype_u and dtype_f
        super(fenics_heat, self).__init__(self.V, dtype_u, dtype_f, problem_params)

        self.g = df.Expression('-sin(a*x[0]) * (sin(t) - b*a*a*cos(t))', a=np.pi, b=self.params.nu, t=self.params.t0,
                               degree=self.params.order)

        # Stiffness term (Laplace)
        u = df.TrialFunction(self.V)
        v = df.TestFunction(self.V)
        a_K = -1.0 * df.inner(df.nabla_grad(u), self.params.nu * df.nabla_grad(v)) * df.dx

        # Mass term
        a_M = u * v * df.dx

        self.M = df.assemble(a_M)
        self.K = df.assemble(a_K)

        # set forcing term as expression
        self.g = df.Expression('-sin(a*x[0]) * (sin(t) - b*a*a*cos(t))', a=np.pi, b=self.params.nu, t=self.params.t0,
                               degree=self.params.order)
        # set boundary values
        self.bc = df.DirichletBC(self.V, df.Constant(0.0), Boundary)

    def solve_system(self, rhs, factor, u0, t):
        """
        Dolfin's linear solver for (M-dtA)u = rhs

        Args:
            rhs (dtype_f): right-hand side for the nonlinear system
            factor (float): abbrev. for the node-to-node stepsize (or any other factor required)
            u0 (dtype_u_: initial guess for the iterative solver (not used here so far)
            t (float): current time

        Returns:
            dtype_u: solution as mesh
        """

        A = self.M - factor * self.K
        b = self.__apply_mass_matrix(rhs)

        self.bc.apply(A, b.values.vector())

        u = self.dtype_u(u0)
        df.solve(A, u.values.vector(), b.values.vector())

        return u

    def __eval_fexpl(self, u, t):
        """
        Helper routine to evaluate the explicit part of the RHS

        Args:
            u (dtype_u): current values (not used here)
            t (fliat): current time

        Returns:
            explicit part of RHS
        """

        self.g.t = t
        fexpl = self.dtype_u(self.V)
        fexpl.values = df.Function(self.V, df.interpolate(self.g, self.V).vector())

        return fexpl

    def __eval_fimpl(self, u, t):
        """
        Helper routine to evaluate the implicit part of the RHS

        Args:
            u (dtype_u): current values
            t (float): current time (not used here)

        Returns:
            implicit part of RHS
        """

        tmp = self.dtype_u(self.V)
        tmp.values = df.Function(self.V, self.K * u.values.vector())
        fimpl = self.__invert_mass_matrix(tmp)

        return fimpl

    def eval_f(self, u, t):
        """
        Routine to evaluate both parts of the RHS

        Args:
            u (dtype_u): current values
            t (float): current time

        Returns:
            dtype_f: the RHS divided into two parts
        """

        f = self.dtype_f(self.V)
        f.impl = self.__eval_fimpl(u, t)
        f.expl = self.__eval_fexpl(u, t)
        return f

    def __apply_mass_matrix(self, u):
        """
        Routine to apply mass matrix

        Args:
            u (dtype_u): current values

        Returns:
            dtype_u: M*u
        """

        me = self.dtype_u(self.V)
        me.values = df.Function(self.V, self.M * u.values.vector())

        return me

    def __invert_mass_matrix(self, u):
        """
        Helper routine to invert mass matrix

        Args:
            u (dtype_u): current values

        Returns:
            dtype_u: inv(M)*u
        """

        me = self.dtype_u(self.V)

        A = 1.0 * self.M
        b = self.dtype_u(u)

        self.bc.apply(A, b.values.vector())

        df.solve(A, me.values.vector(), b.values.vector())

        return me

    def u_exact(self, t):
        """
        Routine to compute the exact solution at time t

        Args:
            t (float): current time

        Returns:
            dtype_u: exact solution
        """

        u0 = df.Expression('sin(a*x[0]) * cos(t)', a=np.pi, t=t, degree=self.params.order)

        me = self.dtype_u(self.V)
        me.values = df.interpolate(u0, self.V)

        return me
