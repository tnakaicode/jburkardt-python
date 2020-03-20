#! /usr/bin/env python3
#


def p00_bisection_test():

    # *****************************************************************************80
    #
    # p00_bisection_test tests p00_bisection.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    max_step = 10
    print('')
    print('p00_bisection_test')
    print('  For each problem, take a few steps of')
    print('  the bisection method.')
#
#  Get the number of problems.
#
    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        title = p00_title(problem)

        print('')
        print('  Problem %d' % (problem))
        print('  %s' % (title))

        a, c = p00_interval(problem)
        b = 0.5 * (a + c)
        fa = p00_f(problem, a)
        fb = p00_f(problem, c)
        fc = p00_f(problem, b)

        i = 0
        print('')
        print('  %d' % (i))
        print('  X:  %12e  %12e  %12e' % (a, b, c))
        print('  F:  %12e  %12e  %12e' % (fa, fb, fc))

        for i in range(1, max_step + 1):

            d = 0.5 * (a + b)
            fd = p00_f(problem, d)

            e = 0.5 * (b + c)
            fe = p00_f(problem, e)

            if (fd <= fb):
                c = b
                fc = fb
                b = d
                fb = fd
            elif (fe <= fb):
                a = b
                fa = fb
                b = e
                fb = fe
            else:
                a = d
                fa = fd
                c = e
                fc = fe

            print('  %d' % (i))
            print('  X:  %12e  %12e  %12e' % (a, b, c))
            print('  F:  %12e  %12e  %12e' % (fa, fb, fc))

    return


def p00_f(problem, x):

    # *****************************************************************************80
    #
    # p00_f evaluates the function for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem number.
    #
    #    real x, the argument of the objective function.
    #
    #  Output:
    #
    #    real f, the value of the objective function.
    #
    from sys import exit

    if (problem == 1):
        f = p01_f(x)
    elif (problem == 2):
        f = p02_f(x)
    elif (problem == 3):
        f = p03_f(x)
    elif (problem == 4):
        f = p04_f(x)
    elif (problem == 5):
        f = p05_f(x)
    elif (problem == 6):
        f = p06_f(x)
    elif (problem == 7):
        f = p07_f(x)
    elif (problem == 8):
        f = p08_f(x)
    elif (problem == 9):
        f = p09_f(x)
    elif (problem == 10):
        f = p10_f(x)
    elif (problem == 11):
        f = p11_f(x)
    elif (problem == 12):
        f = p12_f(x)
    elif (problem == 13):
        f = p13_f(x)
    elif (problem == 14):
        f = p14_f(x)
    else:
        print('')
        print('p00_f - Fatal error!')
        print('  Illegal problem number = %d', problem)
        exit('p00_f - Fatal error!')

    return f


def p00_f_test():

    # *****************************************************************************80
    #
    # p00_f_test tests p00_f
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_f_test')
    print('  p00_f evaluates the optimization function f(x)')
    print('  at any point x, and for any problem.')
    print('')
    print('  Problem               X            F(X)')
    print('')

    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x_start = p00_start(problem)

        f_start = p00_f(problem, x_start)

        print('  %7d  %14.6g  %14.6g' % (problem, x_start, f_start))

    return


def p00_f1(problem, x):

    # *****************************************************************************80
    #
    # p00_f1 evaluates the first derivative for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem number.
    #
    #    real x, the value of the variable.
    #
    #  Output:
    #
    #    real f1, the first derivative of the objective function.
    #
    from sys import exit

    if (problem == 1):
        f1 = p01_f1(x)
    elif (problem == 2):
        f1 = p02_f1(x)
    elif (problem == 3):
        f1 = p03_f1(x)
    elif (problem == 4):
        f1 = p04_f1(x)
    elif (problem == 5):
        f1 = p05_f1(x)
    elif (problem == 6):
        f1 = p06_f1(x)
    elif (problem == 7):
        f1 = p07_f1(x)
    elif (problem == 8):
        f1 = p08_f1(x)
    elif (problem == 9):
        f1 = p09_f1(x)
    elif (problem == 10):
        f1 = p10_f1(x)
    elif (problem == 11):
        f1 = p11_f1(x)
    elif (problem == 12):
        f1 = p12_f1(x)
    elif (problem == 13):
        f1 = p13_f1(x)
    elif (problem == 14):
        f1 = p14_f1(x)
    else:
        print('')
        print('p00_f1 - Fatal error!')
        print('  Illegal problem number = %d', problem)
        exit('p00_f1 - Fatal error!')

    return f1


def p00_f1_test():

    # *****************************************************************************80
    #
    # p00_f1_test tests p00_f1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_f1_test')
    print('  p00_f1 evaluates the derivative of the optimization ')
    print('  function f(x) at any point x, and for any problem.')
    print('')
    print('  Problem               X            F\'(X)')
    print('')

    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x_start = p00_start(problem)

        f1_start = p00_f1(problem, x_start)

        print('  %7d  %14.6g  %14.6g' % (problem, x_start, f1_start))

    return


def p00_f1_dif(problem, x):

    # *****************************************************************************80
    #
    # p00_f1_dif approximates the first derivative via finite differences.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem number.
    #
    #    real x, the point where the gradient is to be approximated.
    #
    #  Output:
    #
    #    real f1_dif, the approximated gradient vector.
    #
    import numpy as np

    r8_epsilon = 2.220446049250313E-016

    xrel = np.sqrt(r8_epsilon)

    if (0.0 <= x):
        dx = xrel * (x + 1.0)
    else:
        dx = xrel * (x - 1.0)

    xi = x
    x = xi + dx
    fplus = p00_f(problem, x)

    x = xi - dx
    fminus = p00_f(problem, x)

    f1_dif = (fplus - fminus) / (2.0 * dx)

    x = xi

    return f1_dif


def p00_f1_dif_test():

    # *****************************************************************************80
    #
    # p00_f1_dir_test compares the exact and approximate first derivatives.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_f1_dif_test')
    print('  p00_f1_dif approximates the first derivative f1')
    print('  by a finite difference f1_dif.')
    print('')
    print('  Problem               X           F1(X)       F1_DIF(X)')
    print('')
#
#  Get the number of problems.
#
    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x = p00_start(problem)

        f1 = p00_f1(problem, x)

        f1_dif = p00_f1_dif(problem, x)

        print('  %7d  %14.6g  %14.6g  %14.6g' % (problem, x, f1, f1_dif))

    return


def p00_f2(problem, x):

    # *****************************************************************************80
    #
    # p00_f2 evaluates the second derivative for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the values of the variables.
    #
    #  Output:
    #
    #    real f2, the second derivative.
    #
    from sys import exit

    if (problem == 1):
        f2 = p01_f2(x)
    elif (problem == 2):
        f2 = p02_f2(x)
    elif (problem == 3):
        f2 = p03_f2(x)
    elif (problem == 4):
        f2 = p04_f2(x)
    elif (problem == 5):
        f2 = p05_f2(x)
    elif (problem == 6):
        f2 = p06_f2(x)
    elif (problem == 7):
        f2 = p07_f2(x)
    elif (problem == 8):
        f2 = p08_f2(x)
    elif (problem == 9):
        f2 = p09_f2(x)
    elif (problem == 10):
        f2 = p10_f2(x)
    elif (problem == 11):
        f2 = p11_f2(x)
    elif (problem == 12):
        f2 = p12_f2(x)
    elif (problem == 13):
        f2 = p13_f2(x)
    elif (problem == 14):
        f2 = p14_f2(x)
    else:
        print('')
        print('p00_f2 - Fatal error!')
        print('  Illegal problem number = %d' % (problem))
        exit('p00_f2 - Fatal error!')

    return f2


def p00_f2_test():

    # *****************************************************************************80
    #
    # p00_f2_test tests p00_f2
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_f2_test')
    print('  p00_f2 evaluates the second derivative of the optimization ')
    print('  function f(x) at any point x, and for any problem.')
    print('')
    print('  Problem               X            F"(X)')
    print('')

    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x_start = p00_start(problem)

        f2_start = p00_f2(problem, x_start)

        print('  %7d  %14.6g  %14.6g' % (problem, x_start, f2_start))

    return


def p00_f2_dif(problem, x):

    # *****************************************************************************80
    #
    # p00_f2_dif approximates the second derivative via finite differences.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem number.
    #
    #    real x, the value of the variable.
    #
    #  Output:
    #
    #    real f2_dif, the approximate second derivative.
    #
    r8_epsilon = 2.220446049250313E-016
#
#  Choose the stepsize.
#
    epsilon = r8_epsilon ** 0.33

    s = epsilon * (abs(x) + 1.0)

    xi = x

    f00 = p00_f(problem, x)

    x = xi + s
    fpp = p00_f(problem, x)

    x = xi - s
    fmm = p00_f(problem, x)

    f2_dif = ((fpp - f00) + (fmm - f00)) / s / s

    x = xi

    return f2_dif


def p00_f2_dif_test():

    # *****************************************************************************80
    #
    # p00_f2_dif_test compares the exact and approximate second derivatives.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_f2_dif_test')
    print('  p00_f2_dif approximates the second derivative F2')
    print('  by a finite difference F2_DIF.')
    print('')
    print('  Problem               X           F2(X)       F2_DIF(X)')
    print('')
#
#  Get the number of problems.
#
    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x = p00_start(problem)

        f2 = p00_f2(problem, x)

        f2_dif = p00_f2_dif(problem, x)

        print('  %7d  %14.6g  %14.6g  %14.6g' % (problem, x, f2, f2_dif))

    return


def p00_fmin(a, b, problem, tol):

    # *****************************************************************************80
    #
    # p00_fmin seeks a minimizer of a scalar function of a scalar variable.
    #
    #  Discussion:
    #
    #    FMIN seeks an approximation to the point where F attains a minimum on
    #    the interval (A,B).
    #
    #    The method used is a combination of golden section search and
    #    successive parabolic interpolation.  Convergence is never much
    #    slower than that for a Fibonacci search.  If F has a continuous
    #    second derivative which is positive at the minimum (which is not
    #    at A or B), then convergence is superlinear, and usually of the
    #    order of about 1.324\.
    #
    #    The function F is never evaluated at two points closer together
    #    than EPS * ABS ( FMIN ) + (TOL/3), where EPS is approximately the
    #    square root of the relative machine precision.  If F is a unimodal
    #    function and the computed values of F are always unimodal when
    #    separated by at least EPS * ABS ( XSTAR ) + (TOL/3), then FMIN
    #    approximates the abcissa of the global minimum of F on the
    #    interval [A, B] with an error less than 3 * EPS * ABS ( FMIN ) + TOL.
    #    If F is not unimodal, then FMIN may approximate a local, but
    #    perhaps non-global, minimum to the same accuracy.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Richard Brent,
    #    Algorithms for Minimization without Derivatives,
    #    Prentice Hall, 1973.
    #
    #    David Kahaner, Cleve Moler, Steven Nash,
    #    Numerical Methods and Software,
    #    Prentice Hall, 1988.
    #
    #  Input:
    #
    #    real A, B, the left and right endpoints of the initial interval.
    #
    #    integer problem, the index of a problem.
    #
    #    real TOL, the desired length of the interval of
    #    uncertainty of the final result.  TOL must not be negative.
    #
    #  Output:
    #
    #    real fmin, the abcissa approximating the minimizer of f.
    #
    #    real A, B, the lower and upper bounds for the minimizer.
    #
    import numpy as np

    c = 0.5 * (3.0 - np.sqrt(5.0))
#
#  C is the squared inverse of the golden ratio.
#
#  EPSILON is the square root of the relative machine precision.
#
    r8_epsilon = r8_epsilon = 2.220446049250313E-016

    epsilon = np.sqrt(r8_epsilon)
#
#  Initialization.
#
    v = a + c * (b - a)
    w = v
    x = v
    e = 0.0
    fx = p00_f(problem, x)
    fv = fx
    fw = fx
#
#  The main loop starts here.
#
    while (True):

        midpoint = 0.5 * (a + b)
        tol1 = epsilon * abs(x) + tol / 3.0
        tol2 = 2.0 * tol1
#
#  Check the stopping criterion.
#
        if (abs(x - midpoint) <= (tol2 - 0.5 * (b - a))):
            break
#
#  Is golden-section necessary?
#
        if (abs(e) <= tol1):
            if (midpoint <= x):
                e = a - x
            else:
                e = b - x

            d = c * e
#
#  Consider fitting a parabola.
#
        else:

            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2.0 * (q - r)
            if (0.0 < q):
                p = -p
            q = abs(q)
            r = e
            e = d
#
#  Choose a golden-section step if the parabola is not advised.
#
            if (
                (abs(0.5 * q * r) <= abs(p)) or
                (p <= q * (a - x)) or
                    (q * (b - x) <= p)):

                if (midpoint <= x):
                    e = a - x
                else:
                    e = b - x

                d = c * e
#
#  Choose a parabolic interpolation step.
#
            else:

                d = p / q
                u = x + d

                if ((u - a) < tol2):
                    d = abs(tol1) * r8_sign(midpoint - x)

                if ((b - u) < tol2):
                    d = abs(tol1) * r8_sign(midpoint - x)
#
#  F must not be evaluated too close to X.
#
        if (tol1 <= abs(d)):
            u = x + d

        if (abs(d) < tol1):
            u = x + abs(tol1) * r8_sign(d)

        fu = p00_f(problem, u)
#
#  Update the data.
#
        if (fu <= fx):

            if (x <= u):
                a = x
            else:
                b = x

            v = w
            fv = fw
            w = x
            fw = fx
            x = u
            fx = fu
            continue

        if (u < x):
            a = u
        else:
            b = u

        if (fu <= fw or w == x):
            v = w
            fv = fw
            w = u
            fw = fu
        elif (fu <= fv or v == x or v == w):
            v = u
            fv = fu

    fmin = x

    return fmin, a, b


def p00_fmin_test():

    # *****************************************************************************80
    #
    # p00_fmin_test carries out a version of Brent's derivative-free minimizer.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    tol = 0.00000001

    print('')
    print('p00_fmin_test')
    print('  p00_fmin use Brent''s method to seek a minimizer.')
#
#  Get the number of problems.
#
    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        title = p00_title(problem)

        print('')
        print('  Problem %d' % (problem))
        print('  %s' % (title))

        a, b = p00_interval(problem)

        fa = p00_f(problem, a)
        fb = p00_f(problem, b)

        print('')
        print('  Initial interval [A,B]:')
        print('')
        print('   A,       B:  %24.16e            %24.16e' % (a, b))
        print('  FA,      FB:  %24.16e            %24.16e' % (fa, fb))

        x, a, b = p00_fmin(a, b, problem, tol)

        fa = p00_f(problem, a)
        fb = p00_f(problem, b)
        fx = p00_f(problem, x)

        print('')
        print('  Final interval [A,X*,B]:')
        print('')
        print('   A,  X*,  B:  %24.16e  %24.16e  %24.16e' % (a, x, b))
        print('  FA, FX*, FB:  %24.16e  %24.16e  %24.16e' % (fa, fx, fb))

    return


def p00_interval(problem):

    # *****************************************************************************80
    #
    # p00_interval returns a bracketing interval for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem index.
    #
    #  Output:
    #
    #    real a, b, two points, between which a local
    #    minimizer should be sought.
    #
    from sys import exit

    if (problem == 1):
        a, b = p01_interval()
    elif (problem == 2):
        a, b = p02_interval()
    elif (problem == 3):
        a, b = p03_interval()
    elif (problem == 4):
        a, b = p04_interval()
    elif (problem == 5):
        a, b = p05_interval()
    elif (problem == 6):
        a, b = p06_interval()
    elif (problem == 7):
        a, b = p07_interval()
    elif (problem == 8):
        a, b = p08_interval()
    elif (problem == 9):
        a, b = p09_interval()
    elif (problem == 10):
        a, b = p10_interval()
    elif (problem == 11):
        a, b = p11_interval()
    elif (problem == 12):
        a, b = p12_interval()
    elif (problem == 13):
        a, b = p13_interval()
    elif (problem == 14):
        a, b = p14_interval()
    else:
        print('')
        print('p00_interval - Fatal error!')
        print('  Illegal problem number = %d' % (problem))
        exit('p00_interval - Fatal error!')

    return a, b


def p00_interval_test():

    # *****************************************************************************80
    #
    # p00_interval_test tests p00_interval.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_interval_test')
    print('  p00_interval returns the finite interval [A,B] over which')
    print('  the optimization procedure is to be carried out.')
    print('')
    print('  Problem               A            F(A)               B            F(B)')
    print('')

    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        a, b = p00_interval(problem)

        fa = p00_f(problem, a)
        fb = p00_f(problem, b)

        print('  %7d  %14.6g  %14.6g  %14.6g  %14.6g' %
              (problem, a, fa, b, fb))

    return


def p00_problem_num():

    # *****************************************************************************80
    #
    # p00_problem_num returns the number of problems available.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    integer problem_num, the number of problems.
    #
    problem_num = 14

    return problem_num


def p00_sol(problem):

    # *****************************************************************************80
    #
    # p00_sol returns the solution for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem number.
    #
    #  Output:
    #
    #    real x, the solution.
    #
    from sys import exit

    if (problem == 1):
        x = p01_sol()
    elif (problem == 2):
        x = p02_sol()
    elif (problem == 3):
        x = p03_sol()
    elif (problem == 4):
        x = p04_sol()
    elif (problem == 5):
        x = p05_sol()
    elif (problem == 6):
        x = p06_sol()
    elif (problem == 7):
        x = p07_sol()
    elif (problem == 8):
        x = p08_sol()
    elif (problem == 9):
        x = p09_sol()
    elif (problem == 10):
        x = p10_sol()
    elif (problem == 11):
        x = p11_sol()
    elif (problem == 12):
        x = p12_sol()
    elif (problem == 13):
        x = p13_sol()
    elif (problem == 14):
        x = p14_sol()
    else:
        print('')
        print('p00_sol - Fatal error!')
        print('  Illegal problem number = %d' % (problem))
        exit('p00_sol - Fatal error!')

    return x


def p00_sol_test():

    # *****************************************************************************80
    #
    # p00_sol_test tests p00_sol.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_sol_test')
    print('  p00_sol returns a minimizer for the optimization function f(x)')
    print('  for any problem.')
    print('')
    print('  Problem               X            F(X)          F''(X)          F"(X)')
    print('')

    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x_sol = p00_sol(problem)

        f_sol = p00_f(problem, x_sol)

        f1_sol = p00_f1(problem, x_sol)

        f2_sol = p00_f2(problem, x_sol)

        print('  %7d  %14.6g  %14.6g  %14.6g  %14.6g'
              % (problem, x_sol, f_sol, f1_sol, f2_sol))

    return


def p00_start(problem):

    # *****************************************************************************80
    #
    # p00_start returns a starting point for optimization for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem index.
    #
    #  Output:
    #
    #    real x, a starting point for the optimization.
    #
    from sys import exit

    if (problem == 1):
        x = p01_start()
    elif (problem == 2):
        x = p02_start()
    elif (problem == 3):
        x = p03_start()
    elif (problem == 4):
        x = p04_start()
    elif (problem == 5):
        x = p05_start()
    elif (problem == 6):
        x = p06_start()
    elif (problem == 7):
        x = p07_start()
    elif (problem == 8):
        x = p08_start()
    elif (problem == 9):
        x = p09_start()
    elif (problem == 10):
        x = p10_start()
    elif (problem == 11):
        x = p11_start()
    elif (problem == 12):
        x = p12_start()
    elif (problem == 13):
        x = p13_start()
    elif (problem == 14):
        x = p14_start()
    else:
        print('')
        print('p00_start - Fatal error!')
        print('  Illegal problem number = %d' % (problem))
        exit('p00_start - Fatal error!')

    return x


def p00_start_test():

    # *****************************************************************************80
    #
    # p00_start_test tests p00_start
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_start_test')
    print('  p00_start returns a suggested starting point for an')
    print('  optimization procedure, for any problem.')
    print('')
    print('  Problem          Xstart       F(Xstart)')
    print('')

    problem_num = p00_problem_num()

    for problem in range(1, problem_num + 1):

        x_start = p00_start(problem)

        f_start = p00_f(problem, x_start)

        print('  %7d  %14.6g  %14.6g' % (problem, x_start, f_start))

    return


def p00_title(problem):

    # *****************************************************************************80
    #
    # p00_title returns a title for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    integer problem, the problem index.
    #
    #  Output:
    #
    #    string title, a title for the problem.
    #
    from sys import exit

    if (problem == 1):
        title = p01_title()
    elif (problem == 2):
        title = p02_title()
    elif (problem == 3):
        title = p03_title()
    elif (problem == 4):
        title = p04_title()
    elif (problem == 5):
        title = p05_title()
    elif (problem == 6):
        title = p06_title()
    elif (problem == 7):
        title = p07_title()
    elif (problem == 8):
        title = p08_title()
    elif (problem == 9):
        title = p09_title()
    elif (problem == 10):
        title = p10_title()
    elif (problem == 11):
        title = p11_title()
    elif (problem == 12):
        title = p12_title()
    elif (problem == 13):
        title = p13_title()
    elif (problem == 14):
        title = p14_title()
    else:
        print('')
        print('p00_title - Fatal error!')
        print('  Illegal problem number = %d' % (problem))
        exit('p00_title - Fatal error!')

    return title


def p00_title_test():

    # *****************************************************************************80
    #
    # p00_title_test prints the title of each problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('p00_title_test')
    print('  p00_title prints the title for each problem.')
#
#  Get the number of problems.
#
    problem_num = p00_problem_num()

    print('')
    print('   Problem title')
    print('')

    for problem in range(1, problem_num + 1):

        title = p00_title(problem)

        print('        %2d:  "%s"' % (problem, title))
#
#  Terminate.
#
    print('')
    print('p00_title_test')
    print('  Normal end of execution.')
    return


def p01_f(x):

    # *****************************************************************************80
    #
    # p01_f evaluates the objective function for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the argument of the objective function.
    #
    #  Output:
    #
    #    real f, the value of the objective function.
    #
    f = (x - 2.0) * (x - 2.0) + 1.0

    return f


def p01_f1(x):

    # *****************************************************************************80
    #
    # p01_f1 evaluates the first derivative for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the value of the variable.
    #
    #  Output:
    #
    #    real f1, the first derivative of the objective function.
    #
    f1 = 2.0 * (x - 2.0)

    return f1


def p01_f2(x):

    # *****************************************************************************80
    #
    # p01_f2 evaluates the second derivative for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the values of the variables.
    #
    #  Output:
    #
    #    real f2, the second derivative.
    #
    f2 = 2.0

    return f2


def p01_interval():

    # *****************************************************************************80
    #
    # P01_interval returns a starting interval for optimization for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    import numpy as np

    a = 0.0
    b = np.pi

    return a, b


def p01_sol():

    # *****************************************************************************80
    #
    # P01_sol returns the solution for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 2.0

    return x


def p01_start():

    # *****************************************************************************80
    #
    # P01_start returns a starting point for optimization for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    import numpy as np

    x = np.pi

    return x


def p01_title():

    # *****************************************************************************80
    #
    # P01_title returns a title for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'Simple quadratic, (x-2)^2+1.'

    return title


def p02_f(x):

    # *****************************************************************************80
    #
    # P02_F evaluates the objective function for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    f = x * x + np.exp(- x)

    return f


def p02_f1(x):

    # *****************************************************************************80
    #
    # P02_F1 evaluates the first derivative for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    f1 = 2.0 * x - np.exp(-x)

    return f1


def p02_f2(x):

    # *****************************************************************************80
    #
    # P02_F2 evaluates the second derivative for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    f2 = 2.0 + np.exp(-x)

    return f2


def p02_interval():

    # *****************************************************************************80
    #
    # P02_interval returns a starting interval for optimization for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 0.0
    b = 1.0

    return a, b


def p02_sol():

    # *****************************************************************************80
    #
    # P02_sol returns the solution for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 0.351734

    return x


def p02_start():

    # *****************************************************************************80
    #
    # P02_start returns a starting point for optimization for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 0.8

    return x


def p02_title():

    # *****************************************************************************80
    #
    # P02_title returns a title for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'Quadratic plus exponential, x^2 + e^(-x).'

    return title


def p03_f(x):

    # *****************************************************************************80
    #
    # P03_F evaluates the objective function for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    f = ((x * x + 2.0) * x + 1.0) * x + 3.0

    return f


def p03_f1(x):

    # *****************************************************************************80
    #
    # P03_F1 evaluates the first derivative for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    f1 = (4.0 * x * x + 4.0) * x + 1.0

    return f1


def p03_f2(x):

    # *****************************************************************************80
    #
    # P03_F2 evaluates the second derivative for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    f2 = 12.0 * x * x + 4.0

    return f2


def p03_interval():

    # *****************************************************************************80
    #
    # P03_interval returns a starting interval for optimization for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = -2.0
    b = +2.0

    return a, b


def p03_sol():

    # *****************************************************************************80
    #
    # P03_sol returns the solution for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = -0.236733

    return x


def p03_start():

    # *****************************************************************************80
    #
    # P03_start returns a starting point for optimization for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 1.5

    return x


def p03_title():

    # *****************************************************************************80
    #
    # P03_title returns a title for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'Quartic, x^4 + 2x^2 + x + 3.'

    return title


def p04_f(x):

    # *****************************************************************************80
    #
    # P04_F evaluates the objective function for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    f = np.exp(x) + 0.01 / x

    return f


def p04_f1(x):

    # *****************************************************************************80
    #
    # P04_F1 evaluates the first derivative for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    f1 = np.exp(x) - 0.01 / x / x

    return f1


def p04_f2(x):

    # *****************************************************************************80
    #
    # P04_F2 evaluates the second derivative for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    f2 = np.exp(x) + 0.02 / x / x / x

    return f2


def p04_interval():

    # *****************************************************************************80
    #
    # P04_interval returns a starting interval for optimization for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 0.0001
    b = 1.0

    return a, b


def p04_sol():

    # *****************************************************************************80
    #
    # P04_sol returns the solution for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 0.0953446

    return x


def p04_start():

    # *****************************************************************************80
    #
    # P04_start returns a starting point for optimization for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 0.95

    return x


def p04_title():

    # *****************************************************************************80
    #
    # P04_title returns a title for problem 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'Steep valley, e^x + 1/(100x).'

    return title


def p05_f(x):

    # *****************************************************************************80
    #
    # P05_F evaluates the objective function for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    f = np.exp(x) - 2.0 * x + 0.01 / x - 0.000001 / x / x

    return f


def p05_f1(x):

    # *****************************************************************************80
    #
    # P05_F1 evaluates the first derivative for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    f1 = np.exp(x) - 2.0 - 0.01 / x / x + 0.000002 / x / x / x

    return f1


def p05_f2(x):

    # *****************************************************************************80
    #
    # P05_F2 evaluates the second derivative for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    f2 = np.exp(x) + 0.02 / x / x / x - 0.000006 / x / x / x / x

    return f2


def p05_interval():

    # *****************************************************************************80
    #
    # P05_interval returns a starting interval for optimization for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 0.0002
    b = 2.0

    return a, b


def p05_sol():

    # *****************************************************************************80
    #
    # P05_sol returns the solution for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 0.703206

    return x


def p05_start():

    # *****************************************************************************80
    #
    # P05_start returns a starting point for optimization for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 1.5

    return x


def p05_title():

    # *****************************************************************************80
    #
    # P05_title returns a title for problem 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'Steep valley, e^x - 2x + 1/(100x) - 1/(1000000x^2).'

    return title


def p06_f(x):

    # *****************************************************************************80
    #
    # P06_F evaluates the objective function for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Richard Brent,
    #    Algorithms for Minimization Without Derivatives,
    #    Prentice Hall 1973,
    #    Reprinted Dover, 2002
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    f = 2.0 - x

    return f


def p06_f1(x):

    # *****************************************************************************80
    #
    # P06_F1 evaluates the first derivative for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    f1 = -1.0

    return f1


def p06_f2(x):

    # *****************************************************************************80
    #
    # P06_F2 evaluates the second derivative for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    LE Scales,
    #    Introduction to Non-Linear Optimization,
    #    Springer, 1985.
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    f2 = 0.0

    return f2


def p06_interval():

    # *****************************************************************************80
    #
    # P06_interval returns a starting interval for optimization for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 7.0
    b = 9.0

    return a, b


def p06_sol():

    # *****************************************************************************80
    #
    # P06_sol returns the solution for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 9.0

    return x


def p06_start():

    # *****************************************************************************80
    #
    # P06_start returns a starting point for optimization for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 7.2

    return x


def p06_title():

    # *****************************************************************************80
    #
    # P06_title returns a title for problem 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'line, 2 - x.'

    return title


def p07_f(x):

    # *****************************************************************************80
    #
    # P07_F evaluates the objective function for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Richard Brent,
    #    Algorithms for Minimization Without Derivatives,
    #    Prentice Hall 1973,
    #    Reprinted Dover, 2002
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    f = (x + np.sin(x)) * np.exp(- x * x)

    return f


def p07_f1(x):

    # *****************************************************************************80
    #
    # P07_F1 evaluates the first derivative for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    f1 = (1.0 - 2.0 * x * x + np.cos(x)
          - 2.0 * x * np.sin(x)) * np.exp(- x * x)

    return f1


def p07_f2(x):

    # *****************************************************************************80
    #
    # P07_F2 evaluates the second derivative for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    f2 = (- 4.0 - 2.0 * x - 4.0 * x * x * x
          - 3.0 * np.sin(x) - 4.0 * x * np.cos(x)
          + 4.0 * x * x * np.sin(x)) * np.exp(- x * x)

    return f2


def p07_interval():

    # *****************************************************************************80
    #
    # P07_interval returns a starting interval for optimization for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = -10.0
    b = +10.0

    return a, b


def p07_sol():

    # *****************************************************************************80
    #
    # P07_sol returns the solution for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = -0.6795786599525

    return x


def p07_start():

    # *****************************************************************************80
    #
    # P07_start returns a starting point for optimization for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = -5.0

    return x


def p07_title():

    # *****************************************************************************80
    #
    # P07_title returns a title for problem 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'The dying snake, ( x + sin(x) ) * e^(-x^2).'

    return title


def p08_f(x):

    # *****************************************************************************80
    #
    # P08_F evaluates the objective function for problem 8.
    #
    #  Discussion:
    #
    #    This function looks positive, but has a pole at x = pi,
    #    near which f -> negative infinity, and has two zeroes nearby.
    #    None of this will show up computationally.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Arnold Krommer, Christoph Ueberhuber,
    #    Numerical Integration on Advanced Systems,
    #    Springer, 1994, pages 185-186.
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    if (x == np.pi):
        f = - 10000.0
    else:
        f = 3.0 * x * x + 1.0 \
            + (np.log((x - np.pi) * (x - np.pi))) / np.pi ** 4

    return f


def p08_f1(x):

    # *****************************************************************************80
    #
    # P08_F1 evaluates the first derivative for problem 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    if (x == np.pi):
        f1 = 0.0
    else:
        f1 = 6.0 * x + (2.0 / (x - np.pi)) / np.pi ** 4

    return f1


def p08_f2(x):

    # *****************************************************************************80
    #
    # P08_F2 evaluates the second derivative for problem 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    if (x == np.pi):
        f2 = 1.0
    else:
        f2 = 6.0 + (- 2.0 / (x - np.pi) / (x - np.pi)) / np.pi ** 4

    return f2


def p08_interval():

    # *****************************************************************************80
    #
    # P08_interval returns a starting interval for optimization for problem 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 2.0
    b = 4.0

    return a, b


def p08_sol():

    # *****************************************************************************80
    #
    # P08_sol returns the solution for problem 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    import numpy as np

    x = np.pi

    return x


def p08_start():

    # *****************************************************************************80
    #
    # P08_start returns a starting point for optimization for problem 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 3.1

    return x


def p08_title():

    # *****************************************************************************80
    #
    # P08_title returns a title for problem 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'The "Thin Pole", x^2+1+log((pi-x)^2)/pi^4'

    return title


def p09_f(x):

    # *****************************************************************************80
    #
    # P09_F evaluates the objective function for problem 9.
    #
    #  Discussion:
    #
    #    This function is oscillatory, with many local minima.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    f = x * x - 10.0 * np.sin(x * x - 3.0 * x + 2.0)

    return f


def p09_f1(x):

    # *****************************************************************************80
    #
    # P09_F1 evaluates the first derivative for problem 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    f1 = 2.0 * x \
        - 10.0 * np.cos(x * x - 3.0 * x + 2.0) \
        * (2.0 * x - 3.0)

    return f1


def p09_f2(x):

    # *****************************************************************************80
    #
    # P09_F2 evaluates the second derivative for problem 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    f2 = 2.0  \
        + 10.0 * np.sin(x * x - 3.0 * x + 2.0) \
        * (2.0 * x - 3.0) * (2.0 * x - 3.0) \
        - 20.0 * np.cos(x * x - 3.0 * x + 2.0)

    return f2


def p09_interval():

    # *****************************************************************************80
    #
    # P09_interval returns a starting interval for optimization for problem 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = -5.0
    b = +5.0

    return a, b


def p09_sol():

    # *****************************************************************************80
    #
    # P09_sol returns the solution for problem 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 0.146621498932095

    return x


def p09_start():

    # *****************************************************************************80
    #
    # P09_start returns a starting point for optimization for problem 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = -2.0

    return x


def p09_title():

    # *****************************************************************************80
    #
    # P09_title returns a title for problem 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'The oscillatory parabola'

    return title


def p10_f(x):

    # *****************************************************************************80
    #
    # P10_F evaluates the objective function for problem 10.
    #
    #  Discussion:
    #
    #    This function is oscillatory.
    #
    #    The function has a local minimum at 1.7922 whose function value is
    #    very close to the minimum value.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Isabel Beichl, Dianne O'Leary, Francis Sullivan,
    #    Monte Carlo Minimization and Counting: One, Two, Too Many,
    #    Computing in Science and Engineering,
    #    Volume 9, Number 1, January/February 2007.
    #
    #    Dianne O'Leary,
    #    Scientific Computing with Case Studies,
    #    SIAM, 2008,
    #    ISBN13: 978-0-898716-66-5,
    #    LC: QA401.O44.
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    import numpy as np

    f = np.cos(x) \
        + 5.0 * np.cos(1.6 * x) \
        - 2.0 * np.cos(2.0 * x) \
        + 5.0 * np.cos(4.5 * x) \
        + 7.0 * np.cos(9.0 * x)

    return f


def p10_f1(x):

    # *****************************************************************************80
    #
    # P10_F1 evaluates the first derivative for problem 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    import numpy as np

    f1 = -             np.sin(x) \
         - 5.0 * 1.6 * np.sin(1.6 * x) \
        + 2.0 * 2.0 * np.sin(2.0 * x) \
         - 5.0 * 4.5 * np.sin(4.5 * x) \
         - 7.0 * 9.0 * np.sin(9.0 * x)

    return f1


def p10_f2(x):

    # *****************************************************************************80
    #
    # P10_F2 evaluates the second derivative for problem 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    import numpy as np

    f2 = -                   np.cos(x) \
         - 5.0 * 1.6 * 1.6 * np.cos(1.6 * x) \
        + 2.0 * 2.0 * 2.0 * np.cos(2.0 * x) \
         - 5.0 * 4.5 * 4.5 * np.cos(4.5 * x) \
         - 7.0 * 9.0 * 9.0 * np.cos(9.0 * x)

    return f2


def p10_interval():

    # *****************************************************************************80
    #
    # P10_interval returns a starting interval for optimization for problem 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 0.0
    b = 7.0

    return a, b


def p10_sol():

    # *****************************************************************************80
    #
    # P10_sol returns the solution for problem 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 5.975691087433868

    return x


def p10_start():

    # *****************************************************************************80
    #
    # P10_start returns a starting point for optimization for problem 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 0.5

    return x


def p10_title():

    # *****************************************************************************80
    #
    # P10_title returns a title for problem 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = 'The cosine combo'

    return title


def p11_f(x):

    # *****************************************************************************80
    #
    # P11_F evaluates the objective function for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the argument of the objective function.
    #
    #    Output, real F, the value of the objective function.
    #
    f = 1.0 + abs(3.0 * x - 1.0)

    return f


def p11_f1(x):

    # *****************************************************************************80
    #
    # P11_F1 evaluates the first derivative for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the value of the variable.
    #
    #    Output, real F1, the first derivative of the
    #    objective function.
    #
    if (3.0 * x - 1.0 < 0.0):
        f1 = - 3.0
    else:
        f1 = + 3.0

    return f1


def p11_f2(x):

    # *****************************************************************************80
    #
    # P11_F2 evaluates the second derivative for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the values of the variables.
    #
    #    Output, real F2, the second derivative.
    #
    f2 = 0.0

    return f2


def p11_interval():

    # *****************************************************************************80
    #
    # P11_interval returns a starting interval for optimization for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real A, B, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 0.0
    b = 1.0

    return a, b


def p11_sol():

    # *****************************************************************************80
    #
    # P11_sol returns the solution for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 1.0 / 3.0

    return x


def p11_start():

    # *****************************************************************************80
    #
    # P11_start returns a starting point for optimization for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real x, a starting point for the optimization.
    #
    x = 0.75

    return x


def p11_title():

    # *****************************************************************************80
    #
    # p11_title returns a title for problem 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string title, a title for the problem.
    #
    title = '1 + |3x-1|'

    return title


def p12_f(x):

    # *****************************************************************************80
    #
    # p12_f evaluates the objective function for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the argument of the objective function.
    #
    #  Output:
    #
    #    real f, the value of the objective function.
    #
    import numpy as np

    f = x * x + np.sin(53.0 * x)

    return f


def p12_f1(x):

    # *****************************************************************************80
    #
    # p12_f1 evaluates the first derivative for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the value of the variable.
    #
    #  Output:
    #
    #    real f1, the first derivative of the objective function.
    #
    import numpy as np

    f1 = 2.0 * x + 53.0 * np.cos(53.0 * x)

    return f1


def p12_f2(x):

    # *****************************************************************************80
    #
    # p12_f2 evaluates the second derivative for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the values of the variables.
    #
    #  Output:
    #
    #    real f2, the second derivative.
    #
    import numpy as np

    f2 = 2.0 - 53.0 * 53.0 * np.sin(53.0 * x)

    return f2


def p12_interval():

    # *****************************************************************************80
    #
    # p12_interval returns a starting interval for optimization for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real a, b, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = -2.0
    b = +2.0

    return a, b


def p12_sol():

    # *****************************************************************************80
    #
    # p12_sol returns the solution for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 0.088858774312511

    return x


def p12_start():

    # *****************************************************************************80
    #
    # p12_start returns a starting point for optimization for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, a starting point for the optimization.
    #
    x = 1.0

    return x


def p12_title():

    # *****************************************************************************80
    #
    # p12_title returns a title for problem 12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    string title, a title for the problem.
    #
    title = 'The fuzzy parabola'

    return title


def p13_f(x):

    # *****************************************************************************80
    #
    # p13_f evaluates the objective function for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the argument of the objective function.
    #
    #  Output:
    #
    #    real f, the value of the objective function.
    #
    f = f = 2.0 * x**4 - 7.0 * x**2 + 3.0 * x + 5.0

    return f


def p13_f1(x):

    # *****************************************************************************80
    #
    # p13_f1 evaluates the first derivative for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the value of the variable.
    #
    #  Output:
    #
    #    real f1, the first derivative of the objective function.
    #
    f1 = 8.0 * x**3 - 14.0 * x + 3.0

    return f1


def p13_f2(x):

    # *****************************************************************************80
    #
    # p13_f2 evaluates the second derivative for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the values of the variables.
    #
    #  Output:
    #
    #    real f2, the second derivative.
    #
    import numpy as np

    f2 = 24.0 * x**2 - 14.0

    return f2


def p13_interval():

    # *****************************************************************************80
    #
    # p13_interval returns a starting interval for optimization for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real a, b, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = -2.0
    b = +2.0

    return a, b


def p13_sol():

    # *****************************************************************************80
    #
    # p13_sol returns the solution for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = -1.419229002336325

    return x


def p13_start():

    # *****************************************************************************80
    #
    # p13_start returns a starting point for optimization for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, a starting point for the optimization.
    #
    x = -0.1

    return x


def p13_title():

    # *****************************************************************************80
    #
    # p13_title returns a title for problem 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    string title, a title for the problem.
    #
    title = 'The lazy W'

    return title


def p14_f(x):

    # *****************************************************************************80
    #
    # p14_f evaluates the objective function for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the argument of the objective function.
    #
    #  Output:
    #
    #    real f, the value of the objective function.
    #
    f = 1.0 / ((x - 0.3)**2 + 0.01) \
        + 1.0 / ((x - 0.9)**2 + 0.04) \
        - 6.0

    return f


def p14_f1(x):

    # *****************************************************************************80
    #
    # p14_f1 evaluates the first derivative for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the value of the variable.
    #
    #  Output:
    #
    #    real f1, the first derivative of the objective function.
    #
    f1 = - 2.0 * (x - 0.3) / ((x - 0.3)**2 + 0.01)**2 \
         - 2.0 * (x - 0.9) / ((x - 0.9)**2 + 0.04)**2

    return f1


def p14_f2(x):

    # *****************************************************************************80
    #
    # p14_f2 evaluates the second derivative for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x, the values of the variables.
    #
    #  Output:
    #
    #    real f2, the second derivative.
    #
    u1 = - 2.0 * (x - 0.3)
    v1 = ((x - 0.3)**2 + 0.01)**2
    u2 = - 2.0 * (x - 0.9)
    v2 = ((x - 0.9)**2 + 0.04)**2

    u1p = - 2.0
    v1p = 2.0 * ((x - 0.3)**2 + 0.01) * 2.0 * (x - 0.3)
    u2p = - 2.0
    v2p = 2.0 * ((x - 0.9)**2 + 0.04) * 2.0 * (x - 0.9)

    f2 = (u1p * v1 - u1 * v1p) / v1 / v1 \
        + (u2p * v2 - u2 * v2p) / v2 / v2

    return f2


def p14_interval():

    # *****************************************************************************80
    #
    # p14_interval returns a starting interval for optimization for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real a, b, two points defining an interval in which
    #    the local minimizer should be sought.
    #
    a = 0.3
    b = 0.8

    return a, b


def p14_sol():

    # *****************************************************************************80
    #
    # p14_sol returns the solution for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, the solution.
    #
    x = 0.6370089963

    return x


def p14_start():

    # *****************************************************************************80
    #
    # p14_start returns a starting point for optimization for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    real x, a starting point for the optimization.
    #
    x = 0.4

    return x


def p14_title():

    # *****************************************************************************80
    #
    # p14_title returns a title for problem 14.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Output:
    #
    #    string title, a title for the problem.
    #
    title = 'Humps'

    return title


def r8_sign(x):

    # *****************************************************************************80
    #
    # R8_SIGN returns the sign of an R8.
    #
    #  Discussion:
    #
    #    The value is +1 if the number is positive or zero, and it is -1 otherwise.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 June 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real x, the number whose sign is desired.
    #
    #    Output, real VALUE, the sign of X.
    #
    if (x < 0.0):
        value = -1.0
    else:
        value = +1.0

    return value


def r8_sign_test():

    # *****************************************************************************80
    #
    # R8_SIGN_test tests R8_SIGN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    test_num = 5

    r8_test = np.array([-1.25, -0.25, 0.0, +0.5, +9.0])

    print('')
    print('R8_SIGN_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_SIGN returns the sign of an R8.')
    print('')
    print('     R8     R8_SIGN(R8)')
    print('')

    for test in range(0, test_num):
        r8 = r8_test[test]
        s = r8_sign(r8)
        print('  %8.4f  %8.0f' % (r8, s))
#
#  Terminate.
#
    print('')
    print('R8_SIGN_test')
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
    # TIMESTAMP_test tests TIMESTAMP.
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
    print('TIMESTAMP_test:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_test:')
    print('  Normal end of execution.')
    return


def test_min_test():

    # *****************************************************************************80
    #
    # TEST_MIN_test tests the TEST_MIN library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('TEST_MIN_test')
    print('  Python version')
    print('  Test the TEST_MIN library.')

    p00_title_test()
    p00_interval_test()
    p00_start_test()
    p00_sol_test()
    p00_f_test()
    p00_f1_test()
    p00_f1_dif_test()
    p00_f2_test()
    p00_f2_dif_test()

    p00_bisection_test()
    p00_fmin_test()
#
#  Terminate.
#
    print('')
    print('TEST_MIN_test')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    test_min_test()
    timestamp()
