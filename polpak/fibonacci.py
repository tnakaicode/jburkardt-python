#! /usr/bin/env python
#
def fibonacci_direct(n):

    # *****************************************************************************80
    #
    # FIBONACCI_DIRECT computes the N-th Fibonacci number directly.
    #
    #  Formula:
    #
    #      F(N) = ( PHIP^N - PHIM^N ) / sqrt(5)
    #
    #    where
    #
    #      PHIP = ( 1 + sqrt(5) ) / 2,
    #      PHIM = ( 1 - sqrt(5) ) / 2.
    #
    #  Example:
    #
    #     N   F
    #    --  --
    #     0   0
    #     1   1
    #     2   1
    #     3   2
    #     4   3
    #     5   5
    #     6   8
    #     7  13
    #     8  21
    #     9  34
    #    10  55
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the index of the Fibonacci number to compute.
    #    N should be nonnegative.
    #
    #    Output, integer VALUE, the value of the N-th Fibonacci number.
    #
    r8_sqrt5 = 2.236067977499790

    r8_phim = -0.618033988749895
    r8_phip = 1.618033988749895

    value = round((r8_phip ** n - r8_phim ** n) / r8_sqrt5)

    return value


def fibonacci_direct_test():

    # *****************************************************************************80
    #
    # FIBONACCI_DIRECT_TEST tests FIBONACCI_DIRECT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FIBONACCI_DIRECT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FIBONACCI_DIRECT computes a Fibonacci number directly;')
    print('')
    print('   I      F(I)')
    print('')

    for i in range(0, 21):
        value = fibonacci_direct(i)
        print('  %2d  %14d' % (i, value))
#
#  Terminate.
#
    print('')
    print('FIBONACCI_DIRECT_TEST')
    print('  Normal end of execution.')


def fibonacci_recursive(n):

    # *****************************************************************************80
    #
    # FIBONACCI_RECURSIVE computes the first N Fibonacci numbers.
    #
    #  Algebraic equation:
    #
    #    The 'golden ratio' PHI = (1+sqrt(5))/2 satisfies the equation
    #
    #      X*X-X-1=0
    #
    #    which is often written as:
    #
    #       X        1
    #      --- =  ------
    #       1      X - 1
    #
    #    expressing the fact that a rectangle, whose sides are in proportion X:1,
    #    is similar to the rotated rectangle after a square of side 1 is removed.
    #
    #      <----X---->
    #
    #      +-----*---*
    #      :     :   :  1
    #      :     :   :
    #      +-----*---+
    #      <--1-><X-1>
    #
    #  Formula:
    #
    #    Let
    #
    #      PHIP = ( 1 + sqrt(5) ) / 2
    #      PHIM = ( 1 - sqrt(5) ) / 2
    #
    #    Then
    #
    #      F(N) = ( PHIP^N + PHIM^N ) / sqrt(5)
    #
    #    Moreover, F(N) can be computed by computing PHIP**N / sqrt(5) and rounding
    #    to the nearest whole number.
    #
    #  First terms:
    #
    #      1
    #      1
    #      2
    #      3
    #      5
    #      8
    #     13
    #     21
    #     34
    #     55
    #     89
    #    144
    #
    #    The 40th number is                  102,334,155.
    #    The 50th number is               12,586,269,025.
    #    The 100th number is 354,224,848,179,261,915,075.
    #
    #  Recursion:
    #
    #    F(1) = 1
    #    F(2) = 1
    #
    #    F(N) = F(N-1) + F(N-2)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the highest Fibonacci number to compute.
    #
    #    Output, integer F(N+1), the first N Fibonacci numbers.
    #
    import numpy as np

    f = np.zeros(n + 1)

    f[0] = 0

    if (0 < n):

        f[1] = 1

        if (1 < n):

            f[2] = 1

            for i in range(3, n + 1):
                f[i] = f[i - 1] + f[i - 2]

    return f


def fibonacci_recursive_test():

    # *****************************************************************************80
    #
    # FIBONACCI_RECURSIVE_TEST tests FIBONACCI_RECURSIVE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from i4vec_print import i4vec_print

    n = 20

    print('')
    print('FIBONACCI_RECURSIVE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FIBONACCI_RECURSIVE computes Fibonacci numbers recursively;')

    f = fibonacci_recursive(n)

    i4vec_print(n + 1, f, '  The Fibonacci numbers:')
#
#  Terminate.
#
    print('')
    print('FIBONACCI_RECURSIVE_TEST')
    print('  Normal end of execution.')


def fibonacci_floor(n):

    # *****************************************************************************80
    #
    # FIBONACCI_FLOOR returns the largest Fibonacci number less than or equal to N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the positive integer whose Fibonacci "floor" is desired.
    #
    #    Output, integer F, the largest Fibonacci number less than or equal to N.
    #
    #    Output, integer I, the index of the F.
    #
    import numpy as np
    from fibonacci_direct import fibonacci_direct

    i = 0
    f = 0

    if (0 < n):

        i = int(np.log(0.5 * float(2 * n + 1) * np.sqrt(5.0))
                / np.log(0.5 * (1.0 + np.sqrt(5.0))))

        f = fibonacci_direct(i)

        if (n < f):
            i = i - 1
            f = fibonacci_direct(i)

    return f, i


def fibonacci_floor_test():

    # *****************************************************************************80
    #
    # FIBONACCI_FLOOR_TEST tests FIBONACCI_FLOOR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FIBONACCI_FLOOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FIBONACCI_FLOOR computes the largest Fibonacci number')
    print('  less than or equal to N.')
    print('')
    print('     N  Fibonacci  Index')
    print('')

    for n in range(0, 21):
        f, i = fibonacci_floor(n)
        print('  %4d  %4d  %4d' % (n, f, i))
#
#  Terminate.
#
    print('')
    print('FIBONACCI_FLOOR_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    fibonacci_floor_test()
    fibonacci_direct_test()
    fibonacci_recursive_test()
    timestamp()
