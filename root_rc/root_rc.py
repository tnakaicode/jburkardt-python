#! /usr/bin/env python3
#


def root_rc(x, fx, q):

    # *****************************************************************************80
    #
    # ROOT_RC solves a single nonlinear equation using reverse communication.
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
    #    Input, real X, an estimate for the root.  On the first
    #    call, this must be a value chosen by the user.  Thereafter, it may
    #    be a value chosen by the user, or the value of ROOT returned on the
    #    previous call to the function.
    #
    #    Input, real FX, the value of the function at X.
    #
    #    Input, real Q(9), storage needed by the function.
    #    Before the first call, the user must set q[0] to 0.
    #
    #    Output, real XNEW, an improved estimate for the root.
    #
    #    Output, real FERR, the smallest value of F encountered.
    #
    #    Output, real XERR, the width of the change-in-sign interval,
    #    if one was encountered.
    #
    #    Output, real Q(9), storage needed by the function.
    #
    import numpy as np
    from sys import exit
#
#  If we found an exact zero, there is nothing more to do.
#
    if (fx == 0.0):
        xnew = x
        ferr = 0.0
        xerr = 0.0
        return xnew, ferr, xerr, q

    ferr = abs(fx)
#
#  If this is the first time, initialize, estimate the first root, and exit.
#
    if (q[0] == 0.0):
        q[0] = fx
        q[1] = x
        q[2:9] = 0.0
        xnew = x + fx
        xerr = np.Inf
        return xnew, ferr, xerr, q
#
#  This is not the first call.
#
    q[8] = q[8] + 1.0
#
#  Check for too many iterations.
#
    if (80.0 < q[8]):
        print('')
        print('ROOT_RC - Fatal error!')
        print('  Number of iterations = %d' % int(q[8]))
        exit('ROOT_RC - Fatal error!')
#
#  Check for a repeated X value.
#
    if ((2.0 <= q[8] and x == q[3]) or x == q[1]):
        print('')
        print('ROOT_RC - Fatal error!')
        print('  Value of X has been input before.')
        exit('ROOT_RC - Fatal error!')
#
#  Push X -> A -> B -> C
#
    q[5] = q[3]
    q[4] = q[2]
    q[3] = q[1]
    q[2] = q[0]
    q[1] = x
    q[0] = fx
#
#  If we have a change-in-sign interval, store the opposite value.
#
    if (np.sign(q[0]) != np.sign(q[2])):
        q[6] = q[2]
        q[7] = q[3]
#
#  Calculate XERR.
#
    if (q[6] != 0.0):
        xerr = abs(q[7] - q[1])
    else:
        xerr = np.Inf
#
#  If more than 30 iterations, and we have change-in-sign interval, bisect.
#
    if (30.0 < q[8] and q[6] != 0.0):
        xnew = q[1] + (q[7] - q[1]) / 2.0
        return xnew, ferr, xerr, q

    v = (q[2] - q[0]) / (q[3] - q[1])
#
#  If 3 or more points, try Muller.
#
    if (q[4] != 0.0):
        u = (q[4] - q[2]) / (q[5] - q[3])
        w = q[3] - q[1]
        z = (q[5] - q[1]) / w
        r = (z + 1.0) * v - u

        if (r != 0.0):
            p = 2.0 * z * q[0] / r
            d = 2.0 * p / (w * r) * (v - u)
            if (-1.0 <= d):
                xnew = q[1] - p / (1.0 + np.sqrt(1.0 + d))
                if (q[6] == 0.0 or
                    (q[1] < xnew and xnew < q[7]) or
                        (q[7] < xnew and xnew < q[1])):
                    return xnew, ferr, xerr, q
#
#  Try the secant step.
#
    if (q[0] != q[2] or q[6] == 0.0):

        if (q[0] == q[2]):
            print('')
            print('ROOT_RC - Fatal error!')
            print('  Cannot apply any method.')
            exit('ROOT_RC - Fatal error!')

        decr = q[0] / v
        if (abs(decr) * 4.6E+18 < abs(q[1])):
            decr = 1.74E-18 * abs(q[1]) * np.sign(decr)

        xnew = q[1] - decr
        if (q[6] == 0.0 or
            (q[1] < xnew and xnew < q[7]) or
                (q[7] < xnew and xnew < q[1])):
            return xnew, ferr, xerr, q
#
#  Apply bisection.
#
    xnew = q[1] + (q[7] - q[1]) / 2.0

    return xnew, ferr, xerr, q


def root_rc_test():

    # *****************************************************************************80
    #
    # ROOT_RC_TEST tests ROOT_RC.
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

    print('')
    print('ROOT_RC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ROOT_RC searches for an approximate solution of F(X) = 0.')
    print('')
    print('       X              XERR            FX              FERR')
    print('')
#
#  Initialization.
#
    it = 0
    it_max = 30
    q = np.zeros(9)
    x = - 2.1
#
#  Each call takes one more step of improvement.
#
    while (True):

        fx = np.cos(x) - x

        if (it == 0):
            print('  %14.6g                  %14.6g' % (x, fx))
        else:
            print('  %14.6g  %14.6g  %14.6g  %14.6g' % (x, xerr, fx, ferr))

        x, ferr, xerr, q = root_rc(x, fx, q)

        if (ferr < 1.0E-08):
            print('')
            print('  Uncertainty in F(X) less than tolerance.')
            break

        if (xerr < 1.0E-08):
            print('')
            print('  Width of X interal less than tolerance.')
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
    print('ROOT_RC_TEST:')
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


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    root_rc_test()
    timestamp()
