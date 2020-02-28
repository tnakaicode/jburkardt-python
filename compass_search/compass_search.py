#! /usr/bin/env python3
#


def beale(m, x):

    # *****************************************************************************80
    #
    # BEALE computes the Beale function.
    #
    #  Discussion:
    #
    #    This function has a global minimizer:
    #
    #      X = ( 3.0, 0.5 )
    #
    #    for which
    #
    #      F(X) = 0.
    #
    #    For a relatively easy computation, start the search at
    #
    #      X = ( 1.0, 1.0 )
    #
    #    A harder computation starts at
    #
    #      X = ( 1.0, 4.0 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Evelyn Beale,
    #    On an Iterative Method for Finding a Local Minimum of a Function
    #    of More than One Variable,
    #    Technical Report 25,
    #    Statistical Techniques Research Group,
    #    Princeton University, 1958.
    #
    #    Richard Brent,
    #    Algorithms for Minimization with Derivatives,
    #    Dover, 2002,
    #    ISBN: 0-486-41998-3,
    #    LC: QA402.5.B74.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    f1 = 1.5 - x[0] * (1.0 - x[1])
    f2 = 2.25 - x[0] * (1.0 - x[1] ** 2)
    f3 = 2.625 - x[0] * (1.0 - x[1] ** 3)

    f = f1 ** 2 + f2 ** 2 + f3 ** 2

    return f


def beale_test():

    # *****************************************************************************80
    #
    # % BEALE_TEST works with the Beale function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('BEALE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Beale function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.1
    k_max = 20000

    x = np.array([1.0, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (beale(m, x)))

    x, fx, k = compass_search(beale, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Repeat with more difficult start.
#
    x = np.array([1.0, 4.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (beale(m, x)))

    x, fx, k = compass_search(beale, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([3.0, 0.5])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (beale(m, x)))
#
#  Terminate.
#
    print('')
    print('BEALE_TEST')
    print('  Normal end of execution.')
    return


def bohach1(m, x):

    # *****************************************************************************80
    #
    # BOHACH1 evaluates the Bohachevsky function #1.
    #
    #  Discussion:
    #
    #    The minimizer is
    #
    #      X* = [ 0.0, 0.0 ]
    #      F(X*) = 0.0
    #
    #    Suggested starting point:
    #
    #      X = [ 0.5, 1.0 ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Zbigniew Michalewicz,
    #    Genetic Algorithms + Data Structures = Evolution Programs,
    #    Third Edition,
    #    Springer Verlag, 1996,
    #    ISBN: 3-540-60676-9,
    #    LC: QA76.618.M53.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    import numpy as np

    f = x[0] * x[0] - 0.3 * np.cos(3.0 * np.pi * x[0]) \
        + 2.0 * x[1] * x[1] - 0.4 * np.cos(4.0 * np.pi * x[1]) \
        + 0.7

    return f


def bohach1_test():

    # *****************************************************************************80
    #
    # BOHACH1_TEST works with the Bohachevsky function #1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('BOHACH1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Bohachevsky function #1')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([0.5, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (bohach1(m, x)))

    x, fx, k = compass_search(bohach1, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X[1]:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([0.0, 0.0])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (bohach1(m, x)))
#
#  Terminate.
#
    print('')
    print('BOHACH1_TEST')
    print('  Normal end of execution.')
    return


def bohach2(m, x):

    # *****************************************************************************80
    #
    # BOHACH2 evaluates the Bohachevsky function #2.
    #
    #  Discussion:
    #
    #    The minimizer is
    #
    #      X* = [ 0.0, 0.0 ]
    #      F(X*) = 0.0
    #
    #    Suggested starting point:
    #
    #      X = [ 0.6, 1.3 ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Zbigniew Michalewicz,
    #    Genetic Algorithms + Data Structures = Evolution Programs,
    #    Third Edition,
    #    Springer Verlag, 1996,
    #    ISBN: 3-540-60676-9,
    #    LC: QA76.618.M53.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    import numpy as np

    f = x[0] * x[0] \
        + 2.0 * x[1] * x[1] \
        - 0.3 * np.cos(3.0 * np.pi * x[0]) * np.cos(4.0 * np.pi * x[1]) \
        + 0.3

    return f


def bohach2_test():

    # *****************************************************************************80
    #
    # BOHACH2_TEST works with the Bohachevsky function #2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('BOHACH2_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Bohachevsky function #2.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([0.6, 1.3])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    f = bohach2(m, x)
    print('  F(X0) = %g' % (f))

    x, fx, k = compass_search(bohach2, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([0.0, 0.0])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    f = bohach2(m, x)
    print('  F(X*) = %g' % (f))
#
#  Terminate.
#
    print('')
    print('BOHACH2_TEST')
    print('  Normal end of execution.')
    return


def broyden(m, x):

    # *****************************************************************************80
    #
    # BROYDEN computes the two dimensional modified Broyden function.
    #
    #  Discussion:
    #
    #    This function has a global minimizer:
    #
    #      X = ( -0.511547141775014, -0.398160951772036 )
    #
    #    for which
    #
    #      F(X) = 1.44E-04
    #
    #    Start the search at
    #
    #      X = ( -0.9, -1.0 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Charles Broyden,
    #    A class of methods for solving nonlinear simultaneous equations,
    #    Mathematics of Computation,
    #    Volume 19, 1965, pages 577-593.
    #
    #    Jorge More, Burton Garbow, Kenneth Hillstrom,
    #    Testing unconstrained optimization software,
    #    ACM Transactions on Mathematical Software,
    #    Volume 7, Number 1, March 1981, pages 17-41.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    f1 = abs((3.0 - x[0]) * x[0] - 2.0 * x[1] + 1.0)
    f2 = abs((3.0 - 2.0 * x[1]) * x[1] - x[0] + 1.0)

    p = 3.0 / 7.0

    f = f1 ** p + f2 ** p

    return f


def broyden_test():

    # *****************************************************************************80
    #
    # BROYDEN_TEST works with the Broyden function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('BROYDEN_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Broyden function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([-0.9, -1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (broyden(m, x)))

    x, fx, k = compass_search(broyden, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([-0.511547141775014, -0.398160951772036])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (broyden(m, x)))
#
#  Terminate.
#
    print('')
    print('BROYDEN_TEST')
    print('  Normal end of execution.')
    return


def compass_search(function_handle, m, x, delta_tol, delta, k_max):

    # *****************************************************************************80
    #
    # COMPASS_SEARCH carries out a direct search minimization algorithm.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Tamara Kolda, Robert Michael Lewis, Virginia Torczon,
    #    Optimization by Direct Search: New Perspectives on Some Classical and Modern Methods,
    #    SIAM Review,
    #    Volume 45, Number 3, 2003, pages 385-482.
    #
    #  Parameters:
    #
    #    Input, function handle FUNCTION_HANDLE ( M, X ), a handle for the function
    #    to be minimized.
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), a starting estimate for the minimizer.
    #
    #    Input, real DELTA_TOL, the smallest step size that is allowed.
    #
    #    Input, real DELTA, the starting stepsize.
    #
    #    Input, integer K_MAX, the maximum number of steps allowed.
    #
    #    Output, real X(M), the estimated minimizer.
    #
    #    Output, real FX, the function value at X.
    #
    #    Output, integer K, the number of steps taken.
    #
    import numpy as np
    from sys import exit

    k = 0
    fx = function_handle(m, x)

    if (delta_tol <= 0):
        print('')
        print('COMPASS_SEARCH - Fatal error!')
        print('  DELTA_TOL <= 0.0.')
        exit('COMPASS_SEARCH - Fatal error!')

    if (delta <= delta_tol):
        print('')
        print('COMPASS_SEARCH - Fatal error!')
        print('  DELTA < DELTA_TOL.')
        exit('COMPASS_SEARCH - Fatal error!')

    while (k < k_max):

        k = k + 1
#
#  For each coordinate direction I, seek a lower function value
#  by increasing or decreasing X(I) by DELTA.
#
        decrease = False
        s = + 1.0
        i = 0

        for ii in range(0, 2 * m):

            xd = x.copy()
            xd[i] = xd[i] + s * delta
            fxd = function_handle(m, xd)
#
#  As soon as a decrease is noticed, accept the new point.
#
            if (fxd < fx):
                x = xd.copy()
                fx = fxd
                decrease = True
                break

            s = - s
            if (s == + 1.0):
                i = i + 1
#
#  If no decrease occurred, reduce DELTA.
#
        if (not decrease):
            delta = delta / 2.0
            if (delta < delta_tol):
                break

    return x, fx, k


def compass_search_test():

    # *****************************************************************************80
    #
    # COMPASS_SEARCH_TEST tests the COMPASS_SEARCH library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('COMPASS_SEARCH_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the COMPASS_SEARCH library.')

    beale_test()
    bohach1_test()
    bohach2_test()
    broyden_test()
    extended_rosenbrock_test()
    goldstein_price_test()
    himmelblau_test()
    local_test()
    mckinnon_test()
    powell_test()
    rosenbrock_test()
#
#  Terminate.
#
    print('')
    print('COMPASS_SEARCH_TEST:')
    print('  Normal end of execution.')
    return


def extended_rosenbrock(m, x):

    # *****************************************************************************80
    #
    # EXTENDED_ROSENBROCK computes the extended Rosenbrock function.
    #
    #  Discussion:
    #
    #    The number of dimensions is arbitrary, except that it must be even.
    #
    #    There is a global minimum at X* = (1,1,...), F(X*) = 0.
    #
    #    The contours are sharply twisted.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Howard Rosenbrock,
    #    An Automatic Method for Finding the Greatest or Least Value of a Function,
    #    Computer Journal,
    #    Volume 3, 1960, pages 175-184.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    import numpy as np

    r = np.zeros(m)

    for i in range(0, m, 2):
        r[i] = 1.0 - x[i]
        r[i + 1] = 10.0 * (x[i + 1] - x[i] ** 2)

    f = np.dot(r, r)

    return f


def extended_rosenbrock_test():

    # *****************************************************************************80
    #
    # EXTENDED_ROSENBROCK_TEST works with the extended Rosenbrock function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('EXTENDED_ROSENBROCK_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the extended Rosenbrock function.')
    m = 4
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([- 1.2, 1.0, -1.5, 1.2])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (extended_rosenbrock(m, x)))

    x, fx, k = compass_search(extended_rosenbrock, m,
                              x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([1.0, 1.0, 1.0, 1.0])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (extended_rosenbrock(m, x)))
#
#  Terminate.
#
    print('')
    print('EXTENDED_ROSENBROCK_TEST')
    print('  Normal end of execution.')
    return


def goldstein_price(m, x):

    # *****************************************************************************80
    #
    # GOLDSTEIN_PRICE evaluates the Goldstein-Price polynomial.
    #
    #  Discussion:
    #
    #    The minimizer is
    #
    #      X* = [ 0.0, -1.0 ]
    #      F(X*) = 3.0
    #
    #    Suggested starting point:
    #
    #      X = [ -0.5, 0.25 ] (easy convergence)
    #      X = [ -4.0, 5.00 ] (harder convergence)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Zbigniew Michalewicz,
    #    Genetic Algorithms + Data Structures = Evolution Programs,
    #    Third Edition,
    #    Springer Verlag, 1996,
    #    ISBN: 3-540-60676-9,
    #    LC: QA76.618.M53.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    a = x[0] + x[1] + 1.0

    b = 19.0 - 14.0 * x[0] + 3.0 * x[0] * x[0] - 14.0 * x[1] \
        + 6.0 * x[0] * x[1] + 3.0 * x[1] * x[1]

    c = 2.0 * x[0] - 3.0 * x[1]

    d = 18.0 - 32.0 * x[0] + 12.0 * x[0] * x[0] + 48.0 * x[1] \
        - 36.0 * x[0] * x[1] + 27.0 * x[1] * x[1]

    f = (1.0 + a * a * b) * (30.0 + c * c * d)

    return f


def goldstein_price_test():

    # *****************************************************************************80
    #
    # GOLDSTEIN_PRICE_TEST works with the Goldstein-Price function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('GOLDSTEIN_PRICE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Goldstein-Price function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([-0.5, 0.25])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (goldstein_price(m, x)))

    x, fx, k = compass_search(goldstein_price, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Repeat with more difficult start.
#
    x = np.array([-4.0, 5.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (goldstein_price(m, x)))

    x, fx, k = compass_search(goldstein_price, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([0.0, -1.0])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (goldstein_price(m, x)))
#
#  Terminate.
#
    print('')
    print('GOLDSTEIN_PRICE_TEST')
    print('  Normal end of execution.')
    return


def himmelblau(m, x):

    # *****************************************************************************80
    #
    # HIMMELBLAU computes the Himmelblau function.
    #
    #  Discussion:
    #
    #    This function has 4 global minima:
    #
    #      X* = (  3,        2       ), F(X*) = 0.
    #      X* = (  3.58439, -1.84813 ), F(X*) = 0.
    #      X* = ( -3.77934, -3.28317 ), F(X*) = 0.
    #      X* = ( -2.80512,  3.13134 ), F(X*) = 0.
    #
    #    Suggested starting points are
    #
    #      (+1,+1),
    #      (-1,+1),
    #      (-1,-1),
    #      (+1,-1),
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    David Himmelblau,
    #    Applied Nonlinear Programming,
    #    McGraw Hill, 1972,
    #    ISBN13: 978-0070289215,
    #    LC: T57.8.H55.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    f = (x[0] ** 2 + x[1] - 11.0) ** 2 \
        + (x[0] + x[1] ** 2 - 7.0) ** 2

    return f


def himmelblau_test():

    # *****************************************************************************80
    #
    # HIMMELBLAU_TEST works with the Himmelblau function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('HIMMELBLAU_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Himmelblau function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([1.0, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (himmelblau(m, x)))

    x, fx, k = compass_search(himmelblau, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))

    x = np.array([-1.0, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (himmelblau(m, x)))

    x, fx, k = compass_search(himmelblau, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))

    x = np.array([-1.0, -1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (himmelblau(m, x)))

    x, fx, k = compass_search(himmelblau, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))

    x = np.array([1.0, -1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (himmelblau(m, x)))

    x, fx, k = compass_search(himmelblau, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate Himmelblau minimizers.
#
    x = np.array([3.0, 2.0])
    r8vec_print(m, x, '  Correct Himmelblau minimizer X1*:')
    print('')
    print('  F(X*) = %g' % (himmelblau(m, x)))

    x = np.array([3.58439, -1.84813])
    r8vec_print(m, x, '  Correct Himmelblau minimizer X2*:')
    print('')
    print('  F(X*) = %g' % (himmelblau(m, x)))

    x = np.array([-3.77934, -3.28317])
    r8vec_print(m, x, '  Correct Himmelblau minimizer X3*:')
    print('')
    print('  F(X*) = %g' % (himmelblau(m, x)))

    x = np.array([-2.80512, 3.13134])
    r8vec_print(m, x, '  Correct Himmelblau minimizer X4*:')
    print('')
    print('  F(X*) = %g' % (himmelblau(m, x)))
#
#  Terminate.
#
    print('')
    print('HIMMELBLAU_TEST')
    print('  Normal end of execution.')
    return


def local(m, x):

    # *****************************************************************************80
    #
    # LOCAL computes the local function.
    #
    #  Discussion:
    #
    #    This function has a local minimizer:
    #
    #      X* = ( 0.2858054412..., 0.2793263206...), F(X*) = 5.9225...
    #
    #    and a global minimizer:
    #
    #      X* = ( -21.02667179..., -36.75997872...), F(X*) = 0.
    #
    #    Suggested starting point for local minimizer:
    #
    #      X = ( 1, 1 ), F(X) = 3.33 * 10^6.
    #
    #    Suggested starting point for global minimizer:
    #
    #      X = ( -15, -35), F(X) = 1.49 * 10^8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    David Himmelblau,
    #    Applied Nonlinear Programming,
    #    McGraw Hill, 1972,
    #    ISBN13: 978-0070289215,
    #    LC: T57.8.H55.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    f = (x[0] ** 2 + 12.0 * x[1] - 1.0) ** 2 \
        + (49.0 * x[0] ** 2 + 49.0 * x[1] ** 2 + 84.0 * x[0]
           + 2324.0 * x[1] - 681.0) ** 2

    return f


def local_test():

    # *****************************************************************************80
    #
    # LOCAL_TEST works with the Local function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('LOCAL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Local function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([1.0, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (local(m, x)))

    x, fx, k = compass_search(local, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate local minimizer.
#
    x = np.array([0.2858054412, 0.2793263206])
    r8vec_print(m, x, '  Correct local minimizer X*:')
    print('')
    print('  F(X*) = %g' % (local(m, x)))
#
#  Try for global minimizer.
#
    x = np.array([-15.0, -35.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (local(m, x)))

    x, fx, k = compass_search(local, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate global minimizer.
#
    x = np.array([-21.02667179, -36.75997872])
    r8vec_print(m, x, '  Correct global minimizer X*:')
    print('')
    print('  F(X*) = %g' % (local(m, x)))
#
#  Terminate.
#
    print('')
    print('LOCAL_TEST')
    print('  Normal end of execution.')
    return


def mckinnon(m, x):

    # *****************************************************************************80
    #
    # MCKINNON computes the McKinnon function.
    #
    #  Discussion:
    #
    #    This function has a global minimizer:
    #
    #      X* = ( 0.0, -0.5 ), F(X*) = -0.25.
    #
    #    There are three parameters, TAU, THETA and PHI.
    #
    #    1 < TAU, then F is strictly convex.
    #             and F has continuous first derivatives.
    #    2 < TAU, then F has continuous second derivatives.
    #    3 < TAU, then F has continuous third derivatives.
    #
    #    However, this function can cause the Nelder-Mead optimization
    #    algorithm to "converge" to a point which is not the minimizer
    #    of the function F.
    #
    #    Sample parameter values which cause problems for Nelder-Mead
    #    include:
    #
    #      PHI = 10,  TAU = 1, THETA = 15
    #      PHI = 60,  TAU = 2, THETA =  6
    #      PHI = 400, TAU = 3, THETA =  6
    #
    #    To get the bad behavior, we also assume the initial simplex has the form
    #
    #      X1 = (0,0),
    #      X2 = (1,1),
    #      X3 = (A,B),
    #
    #    where
    #
    #      A = (1+sqrt(33))/8 =  0.84307...
    #      B = (1-sqrt(33))/8 = -0.59307...
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Ken McKinnon,
    #    Convergence of the Nelder-Mead simplex method to a nonstationary point,
    #    SIAM Journal on Optimization,
    #    Volume 9, Number 1, 1998, pages 148-158.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    global phi
    global tau
    global theta

    if (x[0] <= 0.0):
        f = theta * phi * abs(x[0]) ** tau + x[1] * (1.0 + x[1])
    else:
        f = theta * x[0] ** tau + x[1] * (1.0 + x[1])

    return f


def mckinnon_test():

    # *****************************************************************************80
    #
    # MCKINNON_TEST works with the McKinnon function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    global phi
    global tau
    global theta

    print('')
    print('MCKINNON_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the McKinnon function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000
#
#  Test 1
#
    a = (1.0 + np.sqrt(33.0)) / 8.0
    b = (1.0 - np.sqrt(33.0)) / 8.0

    phi = 10.0
    tau = 1.0
    theta = 15.0

    x = np.array([a, b])
    r8vec_print(m, x, '  Initial point X0:')
    print('  PHI = %g, TAU = %g, THETA = %g' % (phi, tau, theta))
    print('')
    print('  F(X0) = %g' % (mckinnon(m, x)))

    x, fx, k = compass_search(mckinnon, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))

    x = np.array([0.0, -0.5])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (mckinnon(m, x)))
#
#  Test 2
#
    a = (1.0 + np.sqrt(33.0)) / 8.0
    b = (1.0 - np.sqrt(33.0)) / 8.0

    phi = 60.0
    tau = 2.0
    theta = 6.0

    x = np.array([a, b])
    r8vec_print(m, x, '  Initial point X0:')
    print('  PHI = %g, TAU = %g, THETA = %g' % (phi, tau, theta))
    print('')
    print('  F(X0) = %g' % (mckinnon(m, x)))

    x, fx, k = compass_search(mckinnon, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))

    x = np.array([0.0, -0.5])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (mckinnon(m, x)))
#
#  Test 3
#
    a = (1.0 + np.sqrt(33.0)) / 8.0
    b = (1.0 - np.sqrt(33.0)) / 8.0

    phi = 4000.0
    tau = 3.0
    theta = 6.0

    x = np.array([a, b])
    r8vec_print(m, x, '  Initial point X0:')
    print('  PHI = %g, TAU = %g, THETA = %g' % (phi, tau, theta))
    print('')
    print('  F(X0) = %g' % (mckinnon(m, x)))

    x, fx, k = compass_search(mckinnon, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))

    x = np.array([0.0, -0.5])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (mckinnon(m, x)))
#
#  Terminate.
#
    print('')
    print('MCKINNON_TEST')
    print('  Normal end of execution.')
    return


def powell(m, x):

    # *****************************************************************************80
    #
    # POWELL computes the Powell singular quartic function.
    #
    #  Discussion:
    #
    #    This function has a global minimizer:
    #
    #      X* = ( 0.0, 0.0, 0.0, 0.0 ), F(X*) = 0.
    #
    #    Start the search at
    #
    #      X = ( 3.0, -1.0, 0.0, 1.0 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Michael Powell,
    #    An Iterative Method for Finding Stationary Values of a Function
    #    of Several Variables,
    #    Computer Journal,
    #    Volume 5, 1962, pages 147-151.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    f1 = x[0] + 10.0 * x[1]
    f2 = x[2] - x[3]
    f3 = x[1] - 2.0 * x[2]
    f4 = x[0] - x[3]

    f = f1 * f1 + f2 * f2 + f3 * f3 + f4 * f4

    return f


def powell_test():

    # *****************************************************************************80
    #
    # POWELL_TEST works with the Powell function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('POWELL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Powell function.')
    m = 4
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([3.0, -1.0, 0.0, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (powell(m, x)))

    x, fx, k = compass_search(powell, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([0.0, 0.0, 0.0, 0.0])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (powell(m, x)))
#
#  Terminate.
#
    print('')
    print('POWELL_TEST')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def rosenbrock(m, x):

    # *****************************************************************************80
    #
    # ROSENBROCK computes the Rosenbrock function.
    #
    #  Discussion:
    #
    #    There is a global minimum at X* = (1,1), F(X*) = 0.
    #
    #    The starting point X = [ -1.2, 1.0 ] is suggested.
    #
    #    The contours are sharply twisted.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Howard Rosenbrock,
    #    An Automatic Method for Finding the Greatest or Least Value of a Function,
    #    Computer Journal,
    #    Volume 3, 1960, pages 175-184.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, real X(M), the argument of the function.
    #
    #    Output, real F, the value of the function at X.
    #
    f = (1.0 - x[0]) ** 2 + \
        100.0 * (x[1] - x[0] * x[0]) ** 2

    return f


def rosenbrock_test():

    # *****************************************************************************80
    #
    # ROSENBROCK_TEST works with the Rosenbrock function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ROSENBROCK_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test COMPASS_SEARCH with the Rosenbrock function.')
    m = 2
    delta_tol = 0.00001
    delta = 0.3
    k_max = 20000

    x = np.array([- 1.2, 1.0])
    r8vec_print(m, x, '  Initial point X0:')
    print('')
    print('  F(X0) = %g' % (rosenbrock(m, x)))

    x, fx, k = compass_search(rosenbrock, m, x, delta_tol, delta, k_max)
    r8vec_print(m, x, '  Estimated minimizer X1:')
    print('')
    print('  F(X1) = %g, number of steps = %d' % (fx, k))
#
#  Demonstrate correct minimizer.
#
    x = np.array([1.0, 1.0])
    r8vec_print(m, x, '  Correct minimizer X*:')
    print('')
    print('  F(X*) = %g' % (rosenbrock(m, x)))
#
#  Terminate.
#
    print('')
    print('ROSENBROCK_TEST')
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
    compass_search_test()
    timestamp()
