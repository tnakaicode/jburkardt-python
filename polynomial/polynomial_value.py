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

from i4lib.i4_choose import i4_choose
from i4lib.i4_fall import i4_fall
from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_concatenate import i4vec_concatenate
from i4lib.i4vec_permute import i4vec_permute
from i4lib.i4vec_print import i4vec_print
from i4lib.i4vec_sort_heap_index_a import i4vec_sort_heap_index_a
from i4lib.i4vec_sum import i4vec_sum
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from r8lib.r8vec_concatenate import r8vec_concatenate
from r8lib.r8vec_permute import r8vec_permute
from r8lib.r8vec_print import r8vec_print
from polynomial.mono_value import mono_value
from polynomial.mono_rank_grlex import mono_rank_grlex, mono_unrank_grlex
from polynomial.polynomial_print import polynomial_print
from polynomial.polynomial_sort import polynomial_sort
from polynomial.polynomial_compress import polynomial_compress


def polynomial_value(m, o, c, e, nx, x):

    # *****************************************************************************80
    #
    # POLYNOMIAL_VALUE evaluates a polynomial.
    #
    #  Discussion:
    #
    #    The polynomial is evaluated term by term, and no attempt is made to
    #    use an approach such as Horner's method to speed up the process.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int M, the spatial dimension.
    #
    #    Input, integer O, the "order" of the polynomial.
    #
    #    Input, real C[O], the coefficients of the scaled polynomial.
    #
    #    Input, integer E[O], the indices of the exponents of
    #    the scaled polynomial.
    #
    #    Input, integer NX, the number of evaluation points.
    #
    #    Input, real X[M*NX], the coordinates of the evaluation points.
    #
    #    Output, real V[NX], the value of the polynomial at X.
    #

    p = np.zeros(nx, dtype=np.float64)
    for j in range(0, o):
        f = mono_unrank_grlex(m, e[j])
        v = mono_value(m, nx, f, x)
        for k in range(0, nx):
            p[k] = p[k] + c[j] * v[k]

    return p


def polynomial_value_test():

    # *****************************************************************************80
    #
    # POLYNOMIAL_VALUE_TEST tests POLYNOMIAL_VALUE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    o = 6
    c = np.array([7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0], dtype=np.float64)
    e = np.array([1, 2, 4, 5, 12, 33], dtype=np.int32)
    nx = 2
    x = np.array([1.0, 2.0, 3.0,
                  -2.0, 4.0, 1.0], dtype=np.float64)

    print('')
    print('POLYNOMIAL_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYNOMIAL_VALUE evaluates a polynomial.')

    print('')
    title = '  P(X) = '
    polynomial_print(m, o, c, e, title)

    p = polynomial_value(m, o, c, e, nx, x)

    print('')
    for j in range(0, nx):
        print('  P(%f,%f,%f) = %g' %
              (x[0 + j * m], x[1 + j * m], x[2 + j * m], p[j]))

    print('')
    print('POLYNOMIAL_VALUE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polynomial_value_test()
    timestamp()
