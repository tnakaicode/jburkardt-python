#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import platform
import scipy.sparse.linalg as la_sparse


def dg1d_poisson(nel, ss, penal, f):

    # *****************************************************************************80
    #
    # DG1D_POISSON applies Discontinuous Galerkin method to 1D Poisson equation.
    #
    #  Discussion:
    #
    #    A 1D version of the Poisson equation has the form
    #
    #      - ( K(x) u'(x) )' = f(x)  for 0 < x < 1
    #
    #      u(0) = 1
    #      u(1) = 0
    #
    #    Here, we will assume that K(x) = 1.
    #
    #    This function computes an approximate discrete solution to the problem,
    #    using a version of the Discontinuous Galerkin method.  The interval
    #    [0,1] is divided into NEL equal subintervals, over each of which a set
    #    of LOCDIM=3 basis monomials are defined, centered at the midpoint of
    #    the subinterval, and normalized to have unit value at the subinterval
    #    endpoints.
    #
    #    The discontinous Galerkin equations are then set up as the linear
    #    system A*c=b, where c represents coefficients of the basis functions.
    #    The result of solving this system can then be used to tabulate, evaluate,
    #    or plot the approximate DG solution function.
    #
    #  Modified:
    #
    #    17 September 2018
    #
    #  Author:
    #
    #    Original MATLAB version by Beatrice Riviere,
    #    Python version by Alex Lindsay: https://github.com/lindsayad
    #
    #  Reference:
    #
    #    Beatrice Riviere,
    #    Discontinuous Galerkin Methods for Solving Elliptic and Parabolic Equations,
    #    SIAM, 2008,
    #    ISBN: 978-0-898716-56-6
    #
    #  Parameters:
    #
    #   Input, integer NEL, the number of subintervals.
    #
    #    Input, real SS, the symmetrization parameter.
    #    Three values are meaningful:
    #    1.0: NIPG, nonsymmetric interior penalty Galerkin method.
    #    0.0: IIPG, incomplete interior penalty Galerkin method.
    #   -1.0: SIPG, symmetric interior penalty Galerkin method.
    #
    #    Input, real PENAL, the penalty parameter.
    #
    #    Input, F(x), the name of the function which evaluates the
    #    right hand side of the Poisson equation.
    #
    #    Output, real C(3*NEL), the DG coefficients.  The dimension of 3
    #    is due to the use of piecewise quadratics in the interpolation scheme.
    #

    #
    #  Dimension of local matrices.
    #  This number should correspond to the number of monomials used in each
    #  subinterval.  Because it is set to 3, we are using piecewise quadratics.
    #

    #
    #  Local matrices.
    #  These matrices have order locdimxlocdim.
    #  If we want to use higher order methods, then these local matrices would
    #  need to be enlarged, and the appropriate additional values inserted.
    #

    locdim = 3
    Amat = nel * np.array([
        [0.0, 0.0, 0.0],
        [0.0, 4.0, 0.0],
        [0.0, 0.0, 16.0 / 3.0]])

    Bmat = nel * np.array([
        [penal, 1.0 - penal, - 2.0 + penal],
        [- ss - penal, - 1.0 + ss - penal, 2.0 - ss - penal],
        [2.0 * ss + penal, 1.0 - 2.0 * ss - penal, - 2.0 + 2.0 * ss + penal]])

    Cmat = nel * np.array([
        [penal, - 1.0 + penal, - 2.0 + penal],
        [ss + penal, - 1.0 + ss + penal, - 2.0 + ss + penal],
        [2.0 * ss + penal, - 1.0 + 2.0 * ss + penal, - 2.0 + 2.0 * ss + penal]])

    Dmat = nel * np.array([
        [- penal, - 1.0 + penal, 2.0 - penal],
        [- ss - penal, - 1.0 + ss + penal, 2.0 - ss - penal],
        [- 2.0 * ss - penal, - 1.0 + 2.0 * ss + penal, 2.0 - 2.0 * ss - penal]])

    Emat = nel * np.array([
        [- penal, 1.0 - penal, 2.0 - penal],
        [ss + penal, - 1.0 + ss + penal, - 2.0 + ss + penal],
        [- 2.0 * ss - penal, 1.0 - 2.0 * ss - penal, 2.0 - 2.0 * ss - penal]])

    F0mat = nel * np.array([
        [penal, 2.0 - penal, - 4.0 + penal],
        [- 2.0 * ss - penal, - 2.0 + 2.0 * ss + penal, 4.0 - 2.0 * ss - penal],
        [4.0 * ss + penal, 2.0 - 4.0 * ss - penal, - 4.0 + 4.0 * ss + penal]])

    FNmat = nel * np.array([
        [penal, - 2.0 + penal, - 4.0 + penal],
        [2.0 * ss + penal, - 2.0 + 2.0 * ss + penal, - 4.0 + 2.0 * ss + penal],
        [4.0 * ss + penal, - 2.0 + 4.0 * ss + penal, - 4.0 + 4.0 * ss + penal]])
    #
    #  Dimension of global matrix.
    #
    glodim = nel * locdim

    #
    #  Initialize the global data.
    #
    A = np.zeros((glodim, glodim))
    b = np.zeros(glodim)

    #
    #  Gauss quadrature weights and points of order 2, which should be sufficient
    #  for integrals of products of piecewise quadratic functions.
    #
    ng = 2
    wg = np.array([1.0, 1.0])
    sg = np.array([-0.577350269189, 0.577350269189])

    #
    #  Assemble global matrix and RHS.
    #

    #
    #  First subinterval.
    #
    for ii in range(0, locdim):
        for jj in range(0, locdim):
            A[ii][jj] = A[ii][jj] + Amat[ii][jj] + F0mat[ii][jj] + Cmat[ii][jj]
            je = locdim + jj
            A[ii][je] = A[ii][je] + Dmat[ii][jj]

    b[0] = nel * penal
    b[1] = nel * penal * (-1.0) - ss * 2.0 * nel
    b[2] = nel * penal + ss * 4.0 * nel

    for ig in range(0, ng):
        xval = (sg[ig] + 1.0) / (2.0 * nel)
        b[0] = b[0] + wg[ig] * f(xval) / (2.0 * nel) * 1.0
        b[1] = b[1] + wg[ig] * f(xval) / (2.0 * nel) * sg[ig]
        b[2] = b[2] + wg[ig] * f(xval) / (2.0 * nel) * sg[ig] * sg[ig]

    #
    #  Intermediate subintervals.
    #
    for i in range(2, nel):
        for ii in range(0, locdim):
            ie = ii + (i - 1) * locdim
            for jj in range(0, locdim):
                je = jj + (i - 1) * locdim
                A[ie][je] = A[ie][je] + Amat[ii][jj] + \
                    Bmat[ii][jj] + Cmat[ii][jj]
                je = jj + (i - 2) * locdim
                A[ie][je] = A[ie][je] + Emat[ii][jj]
                je = jj + i * locdim
                A[ie][je] = A[ie][je] + Dmat[ii][jj]

            for ig in range(0, ng):
                xval = (sg[ig] + 2.0 * (i - 1) + 1.0) / (2.0 * nel)
                b[ie] = b[ie] + wg[ig] * f(xval) / (2.0 * nel) * (sg[ig] ** ii)

    #
    #  Last subinterval.
    #
    for ii in range(0, locdim):
        ie = ii + (nel - 1) * locdim
        for jj in range(0, locdim):
            je = jj + (nel - 1) * locdim
            A[ie][je] = A[ie][je] + Amat[ii][jj] + FNmat[ii][jj] + Bmat[ii][jj]
            je = jj + (nel - 2) * locdim
            A[ie][je] = A[ie][je] + Emat[ii][jj]

        for ig in range(0, ng):
            xval = (sg[ig] + 2.0 * (nel - 1) + 1.0) / (2.0 * nel)
            b[ie] = b[ie] + wg[ig] * f(xval) / (2.0 * nel) * (sg[ig] ** ii)
    #
    #  Solve the linear system.
    #
    c = np.linalg.solve(A, b)
    return c


def dg1d_poisson_interp(x, i, nel, order, c):

    # *****************************************************************************80
    #
    # DG1D_POISSON_INTERP evaluates a DG interpolant at a point in a subinterval.
    #
    #  Modified:
    #
    #    17 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the location of the point.
    #
    #    Input, integer I, the subinterval containing X.
    #    0 <= I < NE.
    #
    #    Input, integer NE, the number of subintervals.
    #
    #    Input, integer ORDER, the number of monomials used.
    #
    #    Input, real C(ORDER*NE), the interpolant coefficients.
    #
    #    Output, real VALUE, the value of the interpolant at X.
    #
    value = 0.0
    for k in range(0, order):
        value = value + c[k + i * order] * dg1d_poisson_monomial(x, i, nel, k)
    return value


def dg1d_poisson_monomial(x, i, nel, order):

    # *****************************************************************************80
    #
    # DG1D_POISSON_MONOMIAL evaluates a monomial for the Poisson problem.
    #
    #  Discussion:
    #
    #    Assume the I-th interval has width H and midpoint XM.
    #    Then the monomial of order ORDER is:
    #
    #      m(x;i,order) = ( 2 * ( x - xm ) / h ) ^ order
    #
    #  Modified:
    #
    #    15 September 2018
    #
    #  Parameters:
    #
    #    Input, real X, the argument.
    #
    #    Input, integer I, the index of the interval.
    #    0 <= I < NE.
    #
    #    Input, integer NEL, the number of intervals.
    #
    #    Input, integer ORDER, the order of the monomial.
    #
    #    Output, real VALUE, the value of the monomial at X.
    #
    h = 1.0 / nel
    xl = i * h
    xr = (i + 1) * h
    xm = 0.5 * (xl + xr)
    value = (2.0 * (x - xm) / h) ** order
    return value


def dg1d_poisson_test():

    # *****************************************************************************80
    #
    # DG1D_POISSON_TEST tests DG1D_POISSON.
    #
    #  Discussion:
    #
    #   The formula for the value of the computed solution at the point
    #   x in subinterval i, using quadratic polyonomials, is:
    #
    #     uh(x) = c[1+(i-1)*locdim] * dg1d_poisson_monomial(x,i,ne,0)
    #           + c[2+(i-1)*locdim] * dg1d_poisson_monomial(x,i,ne,1)
    #           + c[3+(i-1)*locdim] * dg1d_poisson_monomial(x,i,ne,2)
    #
    #  Modified:
    #
    #    17 September 2018
    #

    print('')
    print('DG1D_POISSON_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DG1D_POISSON solves a 1D Poisson problem using the')
    print('  discontinuous Galerkin method.')

    nel = 4
    h = 1.0 / nel
    ss = 1
    penal = 1.0
    #
    #  LOCDIM is actually the number of monomials used in each subinterval.
    #
    locdim = 3
    #
    #  Report parameters.
    #
    print('')
    print('  0.0 < x < 1.0')
    print('  Number of subintervals = %d' % (nel))
    print('  Number of monomials in expansion = %d' % (locdim))
    print('  Penalty parameter = %g' % (penal))
    print('  DG choice = %g' % (ss))
    #
    #  Compute C, which represents the solution as a set of coefficients
    #  of monomials, indexed by polynomial degree and by subinterval.
    #
    c = dg1d_poisson(nel, ss, penal, dg1d_poisson_test_source)
    #
    #  Evaluate the computed solution at 5 points in each subinterval.
    #
    m = 5

    xh = np.zeros(m * nel)
    uh = np.zeros(m * nel)

    order = locdim
    k = 0
    for i in range(0, nel):
        xl = float(i) / float(nel)
        xr = float(i + 1) / float(nel)
        for j in range(0, m):
            xh[k] = ((m - 1 - j) * xl + j * xr) / float(m - 1)
            uh[k] = dg1d_poisson_interp(xh[k], i, nel, order, c)
            k = k + 1

    #
    #  Tabulate the exact and computed solutions.
    #
    print('')
    print('  I     X(I)      U(X(I))     Uh(X(I))')
    print('')
    for k in range(0, m * nel):
        exact = dg1d_poisson_test_exact(xh[k])
        print('%2d  %8f  %8f  %8f' % (k, xh[k], exact, uh[k]))

    #
    #  Evaluate the true solution at lots of points.
    #
    x = np.linspace(0.0, 1.0, 101)
    u = dg1d_poisson_test_exact(x)

    #
    #  Make a plot comparing the exact and computed solutions.
    #
    plt.plot(xh, uh, label='approximate')
    plt.plot(x, u, label='exact')
    plt.legend(loc=0)
    plt.grid(True)
    plt.xlabel('<---X--->')
    plt.ylabel('<---U(X)--->')
    plt.title('Compare computed and exact solutions')
    filename = 'dg1d_poisson.png'
    plt.savefig(filename)
    print('')
    print('  Graphics saved as "%s"' % (filename))
    plt.clf()

    print('')
    print('DG1D_POISSON_TEST')
    print('  Normal end of execution.')


def dg1d_poisson_test_exact(x):

    # *****************************************************************************80
    #
    # DG1D_POISSON_TEST_EXACT returns the exact solution for the test problem.
    #
    #  Modified:
    #
    #    15 September 2018
    #
    #  Parameters:
    #
    #    Input, real X, the argument.
    #
    #    Output, real VALUE, the value of the exact solution at X.
    #

    value = (1.0 - x) * np.exp(- x ** 2)

    return value


def dg1d_poisson_test_source(x):

    # *****************************************************************************80
    #
    # DG1D_POISSON_TEST_SOURCE evaluates the source term for the test problem.
    #
    #  Modified:
    #
    #    15 September 2018
    #
    #  Parameters:
    #
    #    Input, real X, the argument.
    #
    #    Output, real VALUE, the value of the source term at X.
    #

    value = - (2.0 * x - 2.0 * (1.0 - 2.0 * x)
               + 4.0 * x * (x - x ** 2)) * np.exp(- x * x)

    return value


if __name__ == '__main__':
    timestamp()
    dg1d_poisson_test()
    timestamp()
