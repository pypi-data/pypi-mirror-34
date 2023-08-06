Attempts to parallelize SDC
===========================

In this project, we test different strategies to parallelize SDC beyond PFASST.
More precisely, the goal is to find a robust parallelization strategy *within* each iteration, i.e. parallelization across the collocation nodes.
This code is used for the publication "Parallelizing SDC across the method".

Different preconditioners for SDC
---------------------------------

The easiest approach for a parallel SDC run is to parallelize the preconditioner, i.e. to find a diagonal Q-delta matrix.
So far, this matrix is a lower triangular matrix, containing e.g. the Euler scheme or parts of the LU-decomposition of Q.
Here, we study different ideas to work with a diagonal matrix and compare them to the standard schemes:

- ``IE`` and ``LU``: the standard scheme using implicit Euler or the LU trick
- ``PIC``: the most simple diagonal matrix, i.e. no preconditioner (which is the Picard iteration)
- ``IEpar``: one Euler step from t0 to the current node
- ``Qpar``: Jacobi-like diagonal part of Q

This part also contains ``minimization.py``, producing the heat maps for the spectral radius of the stiff limit matrix.

.. include:: doc_parallelSDC_preconditioner.rst

Simplified Newton for nonlinear problems
----------------------------------------

The main idea here is to work with a diagonalization of the Q matrix.
While this works well for non-equidistant and non-symmetri nodes like Gauss-Radau, this can only be applied for linear problem, where space and time is separated via Kronecker products.
In order to apply this also for nonlinear problems, we apply an outer Newton iteration to the nonlinear collocation problem and use the diagonalized SDC approach for the linear problem.
Yet, the naive implementation still does not decouple space and time, so that we need to fix the Jacobian at e.g. node 0.
This example compares the iteration counts and errors for this idea (incl. a modified Newton where the Jacobian is not fixed but the approach is applied nonetheless).
Three new sweepers are used here: ``linearized_implicit_parallel``, ``linearized_implicit_fixed_parallel`` and ``linearized_implicit_fixed_parallel_prec``.
This part also contains the code ``newton_vs_sdc.py`` where simplified and inexact Newton are compared to standard SDC for the generalized Fisher's equation.

.. include:: doc_parallelSDC_nonlinear.rst

