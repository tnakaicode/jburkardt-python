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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def t_cholesky_lower(n, t):

    # *****************************************************************************80
    #
    # T_CHOLESKY_LOWER: lower Cholesky factor of a compressed Toeplitz matrix.
    #
    #  Discussion:
    #
    #    The first row of the Toeplitz matrix A is supplied in T.
    #
    #    The Toeplitz matrix must be positive semi-definite.
    #
    #    After factorization, A = L * L'.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Michael Stewart,
    #    Cholesky factorization of semi-definite Toeplitz matrices.
    #    Linear Algebra and its Applications,
    #    Volume 254, pages 497-525, 1997.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real T(N), the first row of the Toeplitz matrix.
    #
    #    Output, real L(N,N), the lower Cholesky factor.
    #
    import numpy as np

    g = np.zeros([2, n])

    for j in range(0, n):
        g[0, j] = t[j]
    for j in range(1, n):
        g[1, j] = t[j]

    l = np.zeros([n, n])

    for j in range(0, n):
        l[j, 0] = g[0, j]

    for j in range(n - 1, 0, -1):
        g[0, j] = g[0, j - 1]
    g[0, 0] = 0.0

    for i in range(1, n):
        rho = - g[1, i] / g[0, i]
        gam = np.sqrt((1.0 - rho) * (1.0 + rho))
        for j in range(i, n):
            alf = g[0, j]
            bet = g[1, j]
            g[0, j] = (alf + rho * bet) / gam
            g[1, j] = (rho * alf + bet) / gam
        for j in range(i, n):
            l[j, i] = g[0, j]
        for j in range(n - 1, i, -1):
            g[0, j] = g[0, j - 1]
        g[0, i] = 0.0

    return l


def t_cholesky_lower_test():

    # *****************************************************************************80
    #
    # T_CHOLESKY_LOWER_TEST tests T_CHOLESKY_LOWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('T_CHOLESKY_LOWER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  T_CHOLESKY_LOWER computes the lower Cholesky')
    print('  factor of a positive semi-definite Toeplitz matrix.')
    print('  The Toeplitz matrix is defined by its first row.')

    n = 3
    t = np.array([1.0, 0.5, -0.375])

    r8vec_print(n, t, '  First row of Toeplitz matrix T:')

    l = t_cholesky_lower(n, t)
    r8mat_print(n, n, l, '  Computed lower Cholesky factor L:')

    b = np.dot(l, l.transpose())
    r8mat_print(n, n, b, '  Product L*L\':')

    return


def t_cholesky_upper(n, t):

    # *****************************************************************************80
    #
    # T_CHOLESKY_UPPER: upper Cholesky factor of a compressed Toeplitz matrix.
    #
    #  Discussion:
    #
    #    The Toeplitz matrix A is supplied by its first row.
    #
    #    The Toeplitz matrix must be positive semi-definite.
    #
    #    After factorization, A = R' * R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Michael Stewart,
    #    Cholesky factorization of semi-definite Toeplitz matrices.
    #    Linear Algebra and its Applications,
    #    Volume 254, pages 497-525, 1997.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real T(N), the compressed Toeplitz matrix.
    #
    #    Output, real R(N,N), the upper Cholesky factor.
    #
    import numpy as np

    g = np.zeros([2, n])

    for j in range(0, n):
        g[0, j] = t[j]
    for j in range(1, n):
        g[1, j] = t[j]

    r = np.zeros([n, n])

    for j in range(0, n):
        r[0, j] = g[0, j]

    for j in range(n - 1, 0, -1):
        g[0, j] = g[0, j - 1]
    g[0, 0] = 0.0

    for i in range(1, n):
        rho = - g[1, i] / g[0, i]
        gam = np.sqrt((1.0 - rho) * (1.0 + rho))
        for j in range(i, n):
            alf = g[0, j]
            bet = g[1, j]
            g[0, j] = (alf + rho * bet) / gam
            g[1, j] = (rho * alf + bet) / gam
        for j in range(i, n):
            r[i, j] = g[0, j]
        for j in range(n - 1, i, -1):
            g[0, j] = g[0, j - 1]
        g[0, i] = 0.0

    return r


def t_cholesky_upper_test():

    # *****************************************************************************80
    #
    # T_CHOLESKY_UPPER_TEST tests T_CHOLESKY_UPPER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('T_CHOLESKY_UPPER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  T_CHOLESKY_UPPER computes the upper Cholesky')
    print('  factor of a positive semi-definite Toeplitz matrix.')
    print('  The Toeplitz matrix is defined by its first row.')

    n = 3
    t = np.array([1.0, 0.5, -0.375])

    r8vec_print(n, t, '  First row of Toeplitz matrix T:')

    r = t_cholesky_upper(n, t)
    r8mat_print(n, n, r, '  Computed upper Cholesky factor R:')

    b = np.dot(r.transpose(), r)
    r8mat_print(n, n, b, '  Product R\'R:')

    return


def toep_cholesky_lower(n, g):

    # *****************************************************************************80
    #
    # TOEP_CHOLESKY_LOWER: lower Cholesky factor of a compressed Toeplitz matrix.
    #
    #  Discussion:
    #
    #    The Toeplitz matrix A is supplied in a compressed form G.
    #
    #    The Toeplitz matrix must be positive semi-definite.
    #
    #    After factorization, A = L * L'.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Michael Stewart,
    #    Cholesky factorization of semi-definite Toeplitz matrices.
    #    Linear Algebra and its Applications,
    #    Volume 254, pages 497-525, 1997.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real G(2,N), the compressed Toeplitz matrix.
    #    G(1,1:N) contains the first row.
    #    G(2,2:N) contains the first column.
    #
    #    Output, real L(N,N), the lower Cholesky factor.
    #
    import numpy as np

    l = np.zeros([n, n])

    for j in range(0, n):
        l[j, 0] = g[0, j]

    for j in range(n - 1, 0, -1):
        g[0, j] = g[0, j - 1]
    g[0, 0] = 0.0

    for i in range(1, n):
        rho = - g[1, i] / g[0, i]
        gam = np.sqrt((1.0 - rho) * (1.0 + rho))
        for j in range(i, n):
            alf = g[0, j]
            bet = g[1, j]
            g[0, j] = (alf + rho * bet) / gam
            g[1, j] = (rho * alf + bet) / gam
        for j in range(i, n):
            l[j, i] = g[0, j]
        for j in range(n - 1, i, -1):
            g[0, j] = g[0, j - 1]
        g[0, i] = 0.0

    return l


def toep_cholesky_lower_test():

    # *****************************************************************************80
    #
    # TOEP_CHOLESKY_LOWER_TEST tests TOEP_CHOLESKY_LOWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('TOEP_CHOLESKY_LOWER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TOEP_CHOLESKY_LOWER computes the lower Cholesky')
    print('  factor of a positive semi-definite Toeplitz matrix.')
    print('  The Toeplitz matrix is supplied as a (2,N) array.')

    n = 3
    g = np.array([
        [1.0, 0.5, -0.375],
        [0.0, 0.5, -0.375]])

    r8mat_print(2, n, g, '  Compressed Toeplitz matrix G:')

    l = toep_cholesky_lower(n, g)
    r8mat_print(n, n, l, '  Computed lower Cholesky factor L:')

    b = np.dot(l, l.transpose())
    r8mat_print(n, n, b, '  Product L*L\':')

    return


def toep_cholesky_upper(n, g):

    # *****************************************************************************80
    #
    # TOEP_CHOLESKY_UPPER: upper Cholesky factor of a compressed Toeplitz matrix.
    #
    #  Discussion:
    #
    #    The Toeplitz matrix A is supplied in a compressed form G.
    #
    #    The Toeplitz matrix must be positive semi-definite.
    #
    #    After factorization, A = R' * R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Michael Stewart,
    #    Cholesky factorization of semi-definite Toeplitz matrices.
    #    Linear Algebra and its Applications,
    #    Volume 254, pages 497-525, 1997.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real G(2,N), the compressed Toeplitz matrix.
    #    G(1,1:N) contains the first row.
    #    G(2,2:N) contains the first column.
    #
    #    Output, real R(N,N), the upper Cholesky factor.
    #
    import numpy as np

    r = np.zeros([n, n])

    for j in range(0, n):
        r[0, j] = g[0, j]

    for j in range(n - 1, 0, -1):
        g[0, j] = g[0, j - 1]
    g[0, 0] = 0.0

    for i in range(1, n):
        rho = - g[1, i] / g[0, i]
        gam = np.sqrt((1.0 - rho) * (1.0 + rho))
        for j in range(i, n):
            alf = g[0, j]
            bet = g[1, j]
            g[0, j] = (alf + rho * bet) / gam
            g[1, j] = (rho * alf + bet) / gam
        for j in range(i, n):
            r[i, j] = g[0, j]
        for j in range(n - 1, i, -1):
            g[0, j] = g[0, j - 1]
        g[0, i] = 0.0

    return r


def toep_cholesky_upper_test():

    # *****************************************************************************80
    #
    # TOEP_CHOLESKY_UPPER_TEST tests TOEP_CHOLESKY_UPPER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('TOEP_CHOLESKY_UPPER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TOEP_CHOLESKY_UPPER computes the upper Cholesky')
    print('  factor of a positive semi-definite Toeplitz matrix.')
    print('  The Toeplitz matrix is supplied as a (2,N) array.')

    n = 3
    g = np.array([
        [1.0, 0.5, -0.375],
        [0.0, 0.5, -0.375]])

    r8mat_print(2, n, g, '  Compressed Toeplitz matrix G:')

    r = toep_cholesky_upper(n, g)
    r8mat_print(n, n, r, '  Computed upper Cholesky factor R:')

    b = np.dot(r.transpose(), r)
    r8mat_print(n, n, b, '  Product R\'R:')

    return


def toeplitz_cholesky_lower(n, a):

    # *****************************************************************************80
    #
    # TOEPLITZ_CHOLESKY_LOWER computes the lower Cholesky factor of a Toeplitz matrix.
    #
    #  Discussion:
    #
    #    The Toeplitz matrix must be positive semi-definite.
    #
    #    After factorization, A = L * L'.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Michael Stewart,
    #    Cholesky factorization of semi-definite Toeplitz matrices.
    #    Linear Algebra and its Applications,
    #    Volume 254, pages 497-525, 1997.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the Toeplitz matrix.
    #
    #    Output, real L(N,N), the lower Cholesky factor.
    #
    import numpy as np

    g = np.zeros([2, n])

    for j in range(0, n):
        g[0, j] = a[j, 0]
    for j in range(1, n):
        g[1, j] = a[j, 0]

    l = np.zeros([n, n])

    for j in range(0, n):
        l[j, 0] = g[0, j]

    for j in range(n - 1, 0, -1):
        g[0, j] = g[0, j - 1]
    g[0, 0] = 0.0

    for i in range(1, n):
        rho = - g[1, i] / g[0, i]
        gam = np.sqrt((1.0 - rho) * (1.0 + rho))
        for j in range(i, n):
            alf = g[0, j]
            bet = g[1, j]
            g[0, j] = (alf + rho * bet) / gam
            g[1, j] = (rho * alf + bet) / gam
        for j in range(i, n):
            l[j, i] = g[0, j]
        for j in range(n - 1, i, -1):
            g[0, j] = g[0, j - 1]
        g[0, i] = 0.0

    return l


def toeplitz_cholesky_lower_test():

    # *****************************************************************************80
    #
    # TOEPLITZ_CHOLESKY_LOWER_TEST tests TOEPLITZ_CHOLESKY_LOWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('TOEPLITZ_CHOLESKY_LOWER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TOEPLITZ_CHOLESKY_LOWER computes the lower Cholesky')
    print('  factorization of a positive semi-definite Toeplitz matrix.')
    print('  The matrix is supplied as an NxN array.')

    n = 3
    a = np.array([
        [1.0, 0.5, -0.375],
        [0.5, 1.0, 0.5],
        [-0.375, 0.5, 1.0]])

    r8mat_print(n, n, a, '  Toeplitz matrix A:')

    l = toeplitz_cholesky_lower(n, a)
    r8mat_print(n, n, l, '  Computed lower Cholesky factor L:')

    b = np.dot(l, l.transpose())
    r8mat_print(n, n, b, '  Product LL\':')

    return


def toeplitz_cholesky_upper(n, a):

    # *****************************************************************************80
    #
    # TOEPLITZ_CHOLESKY_UPPER computes the upper Cholesky factor of a Toeplitz matrix.
    #
    #  Discussion:
    #
    #    The Toeplitz matrix must be positive semi-definite.
    #
    #    After factorization, A = R' * R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2017
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Michael Stewart,
    #    Cholesky factorization of semi-definite Toeplitz matrices.
    #    Linear Algebra and its Applications,
    #    Volume 254, pages 497-525, 1997.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the Toeplitz matrix.
    #
    #    Output, real R(N,N), the upper Cholesky factor.
    #
    import numpy as np

    g = np.zeros([2, n])

    for j in range(0, n):
        g[0, j] = a[0, j]
    for j in range(1, n):
        g[1, j] = a[j, 0]

    r = np.zeros([n, n])

    for j in range(0, n):
        r[0, j] = g[0, j]

    for j in range(n - 1, 0, -1):
        g[0, j] = g[0, j - 1]
    g[0, 0] = 0.0

    for i in range(1, n):
        rho = - g[1, i] / g[0, i]
        gam = np.sqrt((1.0 - rho) * (1.0 + rho))
        for j in range(i, n):
            alf = g[0, j]
            bet = g[1, j]
            g[0, j] = (alf + rho * bet) / gam
            g[1, j] = (rho * alf + bet) / gam
        for j in range(i, n):
            r[i, j] = g[0, j]
        for j in range(n - 1, i, -1):
            g[0, j] = g[0, j - 1]
        g[0, i] = 0.0

    return r


def toeplitz_cholesky_upper_test():

    # *****************************************************************************80
    #
    # TOEPLITZ_CHOLESKY_UPPER_TEST tests TOEPLITZ_CHOLESKY_UPPER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('TOEPLITZ_CHOLESKY_UPPER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TOEPLITZ_CHOLESKY_UPPER computes the upper Cholesky')
    print('  factorization of a positive semi-definite Toeplitz matrix.')
    print('  The matrix is supplied as an NxN array.')

    n = 3
    a = np.array([
        [1.0, 0.5, -0.375],
        [0.5, 1.0, 0.5],
        [-0.375, 0.5, 1.0]])

    r8mat_print(n, n, a, '  Toeplitz matrix A:')

    r = toeplitz_cholesky_upper(n, a)
    r8mat_print(n, n, r, '  Computed upper Cholesky factor R:')

    b = np.dot(r.transpose(), r)
    r8mat_print(n, n, b, '  Product R\'R:')

    return


def toeplitz_cholesky_test():

    # *****************************************************************************80
    #
    # TOEPLITZ_CHOLESKY_TEST tests the TOEPLITZ_CHOLESKY library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('TOEPLITZ_CHOLESKY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the TOEPLITZ_CHOLESKY library.')

    t_cholesky_lower_test()
    toep_cholesky_lower_test()
    toeplitz_cholesky_lower_test()

    t_cholesky_upper_test()
    toep_cholesky_upper_test()
    toeplitz_cholesky_upper_test()

    print('')
    print('TOEPLITZ_CHOLESKY_TEST:')
    print('  Normal end of execution.')
    print('')
    return


if (__name__ == '__main__'):
    timestamp()
    toeplitz_cholesky_test()
    timestamp()
