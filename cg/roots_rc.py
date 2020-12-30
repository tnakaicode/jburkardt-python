#! /usr/bin/env python3
#


def roots_rc(n, x, fx, q):

    # *****************************************************************************80
    #
    # ROOTS_RC solves a system of nonlinear equations using reverse communication.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 November 2016
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Gaston Gonnet.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Gaston Gonnet,
    #    On the Structure of Zero Finders,
    #    BIT Numerical Mathematics,
    #    Volume 17, Number 2, June 1977, pages 170-183.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of equations.
    #
    #    Input, real X(N).  Before the first call, the user should
    #    set X to an initial guess or estimate for the root.  Thereafter, the input
    #    value of X should be the output value of XNEW from the previous call.
    #
    #    Input, real FX(N), the value of the function at XNEW.
    #
    #    Workspace, real ( kind = 8 ) Q(2*N+2,N+2).  Before the first call
    #    for a given problem, the user must set Q(2*N+1,1) to 0.0.
    #
    #    Output, real ( kind = 8 ) XNEW(N), a new point at which a function
    #    value is requested.
    #
    #    Output, real ( kind = 8 ) FERR, the function error, that is, the sum of
    #    the absolute values of the most recently computed function vector.
    #
    #    Workspace, real ( kind = 8 ) Q(2*N+2,N+2).
    #
    import numpy as np
    from sys import exit

    ferr = np.sum(abs(fx[0:n]))
#
#  Initialization if Q(2*N+1,1) = 0.0.
#
    if (q[2 * n, 0] == 0.0):

        for i in range(0, n):
            for j in range(0, n + 1):
                q[i, j] = 0.0
                q[i + 1, j] = 0.0
            q[i, i] = 100.0
            q[i + n, i] = 1.0

        q[2 * n, 0:n] = 1.0E+30
        q[2 * n + 1, 0:n] = float(n)

        for i in range(0, n):
            q[i + n, n] = x[i]

        q[0:n, n] = fx[0:n]

        q[2 * n, n] = ferr
        q[2 * n + 1, n] = 0.0
        damp = 0.99

    else:

        jsus = 0

        for i in range(1, n + 1):

            if (2 * n <= q[2 * n + 1, i]):
                q[2 * n, i] = 1.0E+30

            if (q[2 * n + 1, jsus] < ((n + 3) // 2)):
                jsus = i

            if ((n + 3) // 2 <= q[2 * n + 1, i] and q[2 * n, jsus] < q[2 * n, i]):
                jsus = i

        for i in range(0, n):
            q[i + n, jsus] = x[i]
            q[i, jsus] = fx[i]

        q[2 * n, jsus] = ferr
        q[2 * n + 1, jsus] = 0
        jsma = 1
        damp = 0.0

        for j in range(0, n + 1):

            if (1.0E+30 / 10.0 < q[2 * n, j]):
                damp = 0.99

            if (q[2 * n, j] < q[2 * n, jsma]):
                jsma = j

        if (jsma != n):
            for i in range(0, 2 * n + 2):
                t = q[i, jsma]
                q[i, jsma] = q[i, n]
                q[i, n] = t

    q[0:n, n + 1] = q[0:n, n]
#
#  Call the linear equation solver, which should not destroy the matrix
#  in Q(1:N,1:N), and should overwrite the solution into Q(1:N,N+2).
#
# q[0:n,n+1] = np.linalg.solve ( q[0:n,0:n], q[0:n,n+1] )
    q[0:n, n +
        1], res, rank, s = np.linalg.lstsq(q[0:n, 0:n], q[0:n, n + 1], rcond=None)

    sump = np.sum(q[0:n, n + 1])

    if (abs(1.0 - sump) <= 1.0E-10):
        print('')
        print('ROOT - Fatal error!')
        print('  SUMP almost exactly 1.')
        print('  SUMP = %g' % (sump))
        exit('ROOTS_RC - Fatal error!')

    xnew = np.zeros(n)

    for i in range(0, n):
        xnew[i] = q[i + n, n]
        for j in range(0, n):
            xnew[i] = xnew[i] - q[i + n, j] * q[j, n + 1]
#
#  If system not complete, damp the solution.
#
        xnew[i] = xnew[i] / (1.0 - sump) * (1.0 - damp) + q[i + n, n] * damp

    for j in range(0, n + 1):
        q[2 * n + 1, j] = q[2 * n + 1, j] + 1.0

    return xnew, ferr, q


def roots_rc_test():

    # *****************************************************************************80
    #
    # ROOTS_RC_TEST tests ROOTS_RC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 4
    it_max = 30
    x = np.zeros(n)
    xnew = np.zeros(n)
    fx = np.zeros(n)

    print('')
    print('ROOTS_RC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ROOTS_RC seeks a solution of')
    print('  the N-dimensional nonlinear system F(X) = 0.')
    print('')
    print('       FERR          X')
    print('')
#
#  Initialization.
#
    q = np.zeros([2 * n + 2, n + 2])

    xnew[0] = 1.2
    xnew[1:n] = 1.0

    it = 0

    while (True):

        x = xnew.copy()

        fx[0] = 1.0 - x[0]
        for i in range(1, n):
            fx[i] = 10.0 * (x[i] - x[i - 1] ** 2)

        if (it == 0):
            print('                '),
        else:
            print('  %14.6g' % (ferr)),

        for i in range(0, n):
            print('  %14.6g' % (x[i])),
        print('')

        xnew, ferr, q = roots_rc(n, x, fx, q)

        if (ferr < 1.0E-07):
            print('')
            print('  Sum of |f(x)| less than tolerance.')
            break

        if (it_max < it):
            print('')
            print('  Too many iterations!')
            break

        it = it + 1
#
#  Terminate.
#
    print('')
    print('ROOTS_RC_TEST:')
    print('  Normal end of execution.')
    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


if (__name__ == '__main__'):
    timestamp()
    roots_rc_test()
    timestamp()
