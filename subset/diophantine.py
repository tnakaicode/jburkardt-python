#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4_gcd import i4_gcd
from i4lib.i4_sign import i4_sign


def diophantine(a, b, c):

    # *****************************************************************************80
    #
    # DIOPHANTINE solves a Diophantine equation A * X + B * Y = C.
    #
    #  Discussion:
    #
    #    Given integers A, B and C, produce X and Y so that
    #
    #      A * X + B * Y = C.
    #
    #    In general, the equation is solvable if and only if the
    #    greatest common divisor of A and B also divides C.
    #
    #    A solution (X,Y) of the Diophantine equation also gives the solution
    #    X to the congruence equation:
    #
    #      A * X = C mod ( B ).
    #
    #    Generally, if there is one nontrivial solution, there are an infinite
    #    number of solutions to a Diophantine problem.
    #    If (X0,Y0) is a solution, then so is ( X0+T*B/D, Y0-T*A/D ) where
    #    T is any integer, and D is the greatest common divisor of A and B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Eric Weisstein, editor,
    #    CRC Concise Encylopedia of Mathematics,
    #    CRC Press, 1998, page 446.
    #
    #  Parameters:
    #
    #    Input, integer A, B, C, the coefficients of the Diophantine equation.
    #
    #    Output, integer X, Y, the solution of the Diophantine equation.
    #    Note that the algorithm will attempt to return a solution with
    #    smallest Euclidean norm.
    #
    #    Output, integer IERROR, error flag.
    #    0, no error, X and Y were computed.
    #    1, A = B = 0, C is nonzero.
    #    2, A = 0, B and C nonzero, but C is not a multiple of B.
    #    3, A nonzero, B zero, C nonzero, but C is not a multiple of A.
    #    4, A, B, C nonzero, but GCD of A and B does not divide C.
    #    5, the algorithm ran out of internal space.
    #

    nmax = 100

    ierror = 0
    x = 0
    y = 0

    #
    #  Special cases.
    #
    if (a == 0 and b == 0 and c == 0):
        x = 0
        y = 0
        return x, y, ierror
    elif (a == 0 and b == 0 and c != 0):
        ierror = 1
        x = 0
        y = 0
        return x, y, ierror
    elif (a == 0 and b != 0 and c == 0):
        x = 0
        y = 0
        return x, y, ierror
    elif (a == 0 and b != 0 and c != 0):
        x = 0
        y = c // b
        if ((c % b) != 0):
            ierror = 2
        return x, y, ierror
    elif (a != 0 and b == 0 and c == 0):
        x = 0
        y = 0
        return x, y, ierror
    elif (a != 0 and b == 0 and c != 0):
        x = c / a
        y = 0
        if ((c % a) != 0):
            ierror = 3
        return x, y, ierror
    elif (a != 0 and b != 0 and c == 0):
        g = i4_gcd(a, b)
        x = b // g
        y = - a // g
        return x, y, ierror

    #
    #  Now handle the "general" case: A, B and C are nonzero.
    #
    #  Step 1: Compute the GCD of A and B, which must also divide C.
    #
    g = i4_gcd(a, b)

    if ((c % g) != 0):
        ierror = 4
        return x, y, ierror

    a_copy = a // g
    b_copy = b // g
    c_copy = c // g

    #
    #  Step 2: Split A and B into sign and magnitude.
    #
    a_mag = abs(a_copy)
    a_sign = i4_sign(a_copy)
    b_mag = abs(b_copy)
    b_sign = i4_sign(b_copy)

    #
    #  Another special case, A_MAG = 1 or B_MAG = 1.
    #
    if (a_mag == 1):
        x = a_sign * c_copy
        y = 0
        return x, y, ierror
    elif (b_mag == 1):
        x = 0
        y = b_sign * c_copy
        return x, y, ierror

    #
    #  Step 3: Produce the Euclidean remainder sequence.
    #
    q = np.zeros(nmax, dtype=np.int32)

    if (b_mag <= a_mag):

        swap = False
        q[0] = a_mag
        q[1] = b_mag

    else:

        swap = True
        q[0] = b_mag
        q[1] = a_mag

    n = 2

    while (True):

        q[n] = (q[n - 2] % q[n - 1])

        if (q[n] == 1):
            break

        n = n + 1

        if (nmax <= n):
            ierror = 5
            print('')
            print('DIOPHANTINE - Fatal error!')
            print('  Exceeded number of iterations.')
            exit('DIOPHANTINE - Fatal error!')

    #
    #  Step 4: Now go backwards to solve X * A_MAG + Y * B_MAG = 1.
    #
    y = 0
    for k in range(n, 0, -1):
        x = y
        y = (1 - x * q[k - 1]) // q[k]

    #
    #  Step 5: Undo the swapping.
    #
    if (swap):
        z = x
        x = y
        y = z

    #
    #  Step 6: Now apply signs to X and Y so that X * A + Y * B = 1.
    #
    x = x * a_sign
    y = y * b_sign

    #
    #  Step 7: Multiply by C, so that X * A + Y * B = C.
    #
    x = x * c_copy
    y = y * c_copy

    #
    #  Step 8: Given a solution (X,Y), try to find the solution of
    #  minimal magnitude.
    #
    x, y = diophantine_solution_minimize(a_copy, b_copy, x, y)

    return x, y, ierror


def diophantine_test():

    # *****************************************************************************80
    #
    # DIOPHANTINE_TEST tests DIOPHANTINE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    test_num = 20

    a_test = np.array([
        1027, 1027, 1027, 1027, -1027, -1027, -1027, -1027, 6, 0,
        0, 0, 1, 1, 1, 1024, 0, 0, 5, 2])
    b_test = np.array([
        712, 712, -712, -712, 712, 712, -712, -712, 8, 0,
        1, 1, 0, 0, 1, -15625, 0, 3, 0, 4])
    c_test = np.array([
        7, -7, 7, -7, 7, -7, 7, -7, 50, 0,
        0, 1, 0, 1, 0, 11529, 1, 11, 19, 7])

    print('')
    print('DIOPHANTINE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DIOPHANTINE solves a Diophantine equation:')
    print('    A * X + B * Y = C')
    print('')
    print('        A         B         C         X     Y     Error')
    print('')

    for test_i in range(0, test_num):

        a = a_test[test_i]
        b = b_test[test_i]
        c = c_test[test_i]

        x, y, ierror = diophantine(a, b, c)

        if (ierror != 0):
            print('  %8d  %8d  %8d  Error code = %d' % (a, b, c, ierror))
        else:
            error = a * x + b * y - c
            print('  %8d  %8d  %8d  %8d  %8d  %8d' % (a, b, c, x, y, error))

    print('')
    print('DIOPHANTINE_TEST')
    print('  Normal end of execution.')
    return


def diophantine_solution_minimize(a, b, x, y):

    # *****************************************************************************80
    #
    # DIOPHANTINE_SOLUTION_MINIMIZE: minimal solution of a Diophantine equation.
    #
    #  Discussion:
    #
    #    Given a solution (X,Y) of a Diophantine equation:
    #
    #      A * X + B * Y = C.
    #
    #    then there are an infinite family of solutions of the form
    #
    #      ( X(i), Y(i) ) = ( X + i * B, Y - i * A )
    #
    #    An integral solution of minimal Euclidean norm can be found by
    #    tentatively moving along the vectors (B,-A) and (-B,A) one step
    #    at a time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Eric Weisstein, editor,
    #    CRC Concise Encylopedia of Mathematics,
    #    CRC Press, 1998, page 446.
    #
    #  Parameters:
    #
    #    Input, integer A, B, the coefficients of the Diophantine equation.
    #    A and B are assumed to be relatively prime.
    #
    #    Input, integer X, Y, on input, a solution of the Diophantine equation.
    #
    #    Output, integer X, Y, a solution of minimal Euclidean norm.
    #

    #
    #  Compute the minimum for T real, and then look nearby.
    #
    t = float(- b * x + a * y) / float(a * a + b * b)

    x = x + int(round(t)) * b
    y = y - int(round(t)) * a

    #
    #  Look nearby.
    #
    norm = x * x + y * y

    while (True):

        x2 = x + b
        y2 = y - a

        norm2 = x2 * x2 + y2 * y2

        if (norm <= norm2):
            break

        x = x2
        y = y2
        norm = norm2

    while (True):

        x2 = x - b
        y2 = y + a

        norm2 = x2 * x2 + y2 * y2

        if (norm <= norm2):
            break

        x = x2
        y = y2
        norm = norm2

    return x, y


def diophantine_solution_minimize_test():

    # *****************************************************************************80
    #
    # DIOPHANTINE_SOLUTION_MINIMIZE_TEST tests DIOPHANTINE_SOLUTION_MINIMIZE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('DIOPHANTINE_SOLUTION_MINIMIZE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DIOPHANTINE_SOLUTION_MINIMIZE computes a minimal')
    print('  Euclidean norm solution of a Diophantine equation:')
    print('    A * X + B * Y = C')

    a = 4096
    b = -15625
    c = 46116
    x = 665499996
    y = 174456828

    r = a * x + b * y - c

    print('')
    print('  Coefficients:')
    print('    A = %12d' % (a))
    print('    B = %12d' % (b))
    print('    C = %12d' % (c))
    print('  Solution:')
    print('    X = %12d' % (x))
    print('    Y = %12d' % (y))
    print('  Residual R = A * X + B * Y - C:')
    print('    R = %12d' % (r))

    x, y = diophantine_solution_minimize(a, b, x, y)

    r = a * x + b * y - c

    print('')
    print('  The minimized solution:')
    print('    X = %12d' % (x))
    print('    Y = %12d' % (y))
    print('  Residual R = A * X + B * Y - C:')
    print('    R = %12d' % (r))

    x = 15621
    y = 4092

    r = a * x + b * y - c

    print('')
    print('  The minimal positive solution:')
    print('    X = %12d' % (x))
    print('    Y = %12d' % (y))
    print('  Residual R = A * X + B * Y - C:')
    print('    R = %12d' % (r))
    print('')
    print('DIOPHANTINE_SOLUTION_MINIMIZE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    diophantine_test()
    diophantine_solution_minimize_test()
    timestamp()
