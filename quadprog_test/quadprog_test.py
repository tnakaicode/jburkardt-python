#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import platform
from optparse import OptionParser

sys.path.append(os.path.join("../"))
from base import plot2d
from timestamp.timestamp import timestamp
from quadprog.quadprog import solve_qp


def quadprog_test():

    # *****************************************************************************80
    #
    # quadprog_test tests quadprog.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('quadprog_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test quadprog()')
    print('  which solves quadratic programming problems.')
    print('')
    print('  minimize    1/2 x'' H x - f'' x')
    print('  subject to: A'' x >= b')
    print('')
    print('  H should be positive definite symmetric.')

    quadprog_test01()
    quadprog_test02()

    print('')
    print('quadprog_test')
    print('  Normal end of execution.')


def quadprog_test01():

    # *****************************************************************************80
    #
    # quadprog_test01 runs a simple test case.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('quadprog_test01')
    print('  minimize    1/2 x1^2 + x2^2 - x1x2 - 2x1 - 6x2')
    print('  subject to:  x1 +  x2 <= 2')
    print('              -x1 + 2x2 <= 2')
    print('              2x1 +  x2 <= 3')

    H = np.array([
        [1.0, -1.0],
        [-1.0, 2.0]])

    f = np.array([2.0, 6.0])

    A = np.array([
        [-1.0, +1.0, -2.0],
        [-1.0, -2.0, -1.0]])

    b = np.array([-2.0, -2.0, -3.0])

    sol = solve_qp(H, f, A, b)

    print('')
    print('  Solution vector x = [ %g, %g ]:' % (sol[0], sol[1]))
    print('  Function value at x is %g' % (sol[1]))


def quadprog_test02():

    # *****************************************************************************80
    #
    # quadprog_test02 runs a simple test case.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('quadprog_test02')
    print('  minimize    65/2 x^2 - 22xy + 7y^2 - 16xz + 7yz + 5/2z^2')
    print('              - 13x + 15y + 7z')
    print('  subject to:  x + 2y + z <=  3')
    print('              2x      + z <=  2')
    print('              -x + 2y - z <= -2')

    H = np.array([
        [65.0, -22.0, -16.0],
        [-22.0, 14.0, 7.0],
        [-16.0, 7.0, 5.0]])

    f = np.array([13.0, - 15.0, - 7.0])

    A = np.array([
        [-1.0, -2.0, 1.0],
        [-2.0, 0.0, -2.0],
        [-1.0, -1.0, 1.0]])

    b = np.array([-3.0, -2.0, 2.0])

    sol = solve_qp(H, f, A, b)

    print('')
    print('  Solution vector x = [ %g, %g, %g ]:' %
          (sol[0], sol[1], sol[2]))
    print('  Function value at x is %g' % (sol[1]))


if (__name__ == '__main__'):
    timestamp()
    quadprog_test()
    timestamp()
