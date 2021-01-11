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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8_uniform_01 import r8_uniform_01
from r8lib.r8_normal_01 import r8_normal_01
from r8lib.r8vec_uniform_01 import r8vec_uniform_01

obj = plot2d()


def colored_noise_test():

    # *****************************************************************************80
    #
    # COLORED_NOISE_TEST tests the COLORED_NOISE library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('COLORED_NOISE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the COLORED_NOISE library.')

    r8vec_sftf_test()

    n = 128
    q_d = 1.0
    alpha = 0.00
    seed_init = 123456789

    for i in range(0, 9):
        alpha = 0.25 * float(i)
        colored_noise_test01(n, q_d, alpha, seed_init)

    alpha = 0.0
    colored_noise_test02(alpha, 'alpha_0.00_paths.png')

    alpha = 0.5
    colored_noise_test02(alpha, 'alpha_0.50_paths.png')

    alpha = 1.0
    colored_noise_test02(alpha, 'alpha_1.00_paths.png')

    alpha = 1.5
    colored_noise_test02(alpha, 'alpha_1.50_paths.png')

    alpha = 2.0
    colored_noise_test02(alpha, 'alpha_2.00_paths.png')

    print('')
    print('COLORED_NOISE_TEST:')
    print('  Normal end of execution.')


def colored_noise_test01(n, q_d, alpha, seed_init):

    # *****************************************************************************80
    #
    # COLORED_NOISE_TEST01 calls F_ALPHA with particular parameters.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of elements of the sequence
    #    to generate.
    #
    #    Input, real Q_D, the variance of the sequence.
    #
    #    Input, real ALPHA, the exponent of the power law.
    #
    #    Input, integer SEED_INIT, the initial seed for the
    #    random number generator.
    #

    output_filename = 'alpha_%4.2f.txt' % (alpha)

    #
    #  Report parameters.
    #
    print('')
    print('COLORED_NOISE_TEST01:')
    print('  Generating %d sample points.' % (n))
    print('  1/F^ALPHA noise has ALPHA = %f' % (alpha))
    print('  Variance is %f' % (q_d))
    print('  Initial random number seed = %d' % (seed_init))

    seed = seed_init
    x, seed = f_alpha(n, q_d, alpha, seed)

    #
    #  Print no more than 10 entries of the data.
    #
    r8vec_print_some(n, x, 10, '  Noise sample:')

    #
    #  Write the data to a file.
    #
    output = open(output_filename, 'w')
    for i in range(0, n):
        s = '  %g\n' % (x[i])
        output.write(s)
    output.close()
    print('  Data written to file "%s".' % (output_filename))


def colored_noise_test02(alpha, filename):

    # *****************************************************************************80
    #
    # COLORED_NOISE_TEST02 calls F_ALPHA with different random seeds.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real ALPHA, the exponent of the power law.
    #
    #    Input, string FILENAME, the output filename.
    #
    #  Local parameters:
    #
    #    Local, integer N, the number of elements of the sequence
    #    to generate.
    #
    #    Local, real Q_D, the variance of the sequence.
    #
    #    Local, integer SEED, the seed for the random number generator.
    #
    #    Local, real X(N), the sequence.
    #

    n_reals = 200
    n = 128
    q_d = 1.0
    seed_init = 123456789
    seed = seed_init

    #
    #  Report parameters.
    #
    print('')
    print('COLORED_NOISE_TEST02:')
    print('  Generating %d realizations' % (n_reals))
    print('  Generating %d sample points.' % (n))
    print('  1/F^ALPHA noise has ALPHA = %f' % (alpha))
    print('  Variance is %f' % (q_d))
    print('  Initial random number seed = %d' % (seed))

    #
    #  To get 1, 2, ..., N, Python makes you follow their atrocious
    #  off by one convention.
    #
    x = np.arange(1, n + 1)
    yave = np.zeros(n)

    for i in range(0, n_reals):
        y, seed = f_alpha(n, q_d, alpha, seed)
        yave = yave + y
        if (i < 5):
            plt.plot(x, y, linewidth=1, color='b')
    yave = yave / float(n_reals)

    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, yave, linewidth=2, color='k')
    s = 'ALPHA = %g,    5 realizations (blue), 200 averaged realizations (black)' % (
        alpha)
    obj.axs.set_title(s)
    obj.SavePng(filename)

    print('')
    print('  Plot saved as "%s"' % (filename))


def f_alpha(n, q_d, alpha, seed):

    # *****************************************************************************80
    #
    # F_ALPHA generates a 1/F^ALPHA noise sequence.
    #
    #  Discussion:
    #
    #    Thanks to Miro Stoyanov for pointing out that the second half of
    #    the data returned by the inverse Fourier transform should be
    #    discarded, 24 August 2010.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    Original C version by Todd Walter.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Jeremy Kasdin,
    #    Discrete Simulation of Colored Noise and Stochastic Processes
    #    and 1/f^a Power Law Noise Generation,
    #    Proceedings of the IEEE,
    #    Volume 83, Number 5, 1995, pages 802-827.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of samples to generate.
    #
    #    Input, real Q_D, the variance of the noise.
    #
    #    Input, real ALPHA, the exponent for the noise.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), a sequence sampled with the given power law.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #

    #
    #  Set the deviation of the noise.
    #
    q_d = np.sqrt(q_d)

    #
    #  Generate the coefficients Hk.
    #
    hfa = np.zeros(2 * n)

    hfa[0] = 1.0
    for i in range(1, n):
        hfa[i] = hfa[i - 1] * (0.5 * alpha + float(i - 1)) / float(i)

    #
    #  Fill Wk with white noise.
    #
    wfa = np.zeros(2 * n)
    for i in range(0, n):
        wfa[i], seed = r8_normal_01(seed)
        wfa[i] = wfa[i] * q_d

    #
    #  Perform the discrete Fourier transforms of Hk and Wk.
    #
    h_azero, h_a, h_b = r8vec_sftf(2 * n, hfa)
    w_azero, w_a, w_b = r8vec_sftf(2 * n, wfa)

    #
    #  Multiply the two complex vectors.
    #
    w_azero = w_azero * h_azero
    for i in range(0, n):
        wr = w_a[i]
        wi = w_b[i]
        w_a[i] = wr * h_a[i] - wi * h_b[i]
        w_b[i] = wi * h_a[i] + wr * h_b[i]

    #
    #  This scaling is introduced only to match the behavior
    #  of the Numerical Recipes code...
    #
    w_azero = w_azero * 2 * n
    for i in range(0, n - 1):
        w_a[i] = w_a[i] * float(n)
        w_b[i] = w_b[i] * float(n)

    w_a[n - 1] = w_a[n - 1] * float(2 * n)
    w_b[n - 1] = w_b[n - 1] * float(2 * n)

    #
    #  Take the inverse Fourier transform of the result.
    #
    xlong = r8vec_sftb(2 * n, w_azero, w_a, w_b)

    #
    #  Discard the second half of the inverse Fourier transform.
    #
    x = xlong[0:n]

    return x, seed


def r8vec_sftb(n, azero, a, b):

    # *****************************************************************************80
    #
    # R8VEC_SFTB computes a "slow" backward Fourier transform of real data.
    #
    #  Discussion:
    #
    #    SFTB and SFTF are inverses of each other.  If we begin with data
    #    AZERO, A, and B, and apply SFTB to it, and then apply SFTF to the
    #    resulting R vector, we should get back the original AZERO, A and B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data values.
    #
    #    Input, real AZERO, the constant Fourier coefficient.
    #
    #    Input, real A(N/2), B(N/2), the Fourier coefficients.
    #
    #    Output, real R(N), the reconstructed data sequence.
    #

    r = np.zeros(n)
    r[0:n] = azero

    for i in range(0, n):
        k_hi = int(n / 2)
        for k in range(0, k_hi):
            theta = float(k * i * 2) * np.pi / float(n)
            r[i] = r[i] + a[k] * np.cos(theta) + b[k] * np.sin(theta)

    return r


def r8vec_sftf(n, r):

    # *****************************************************************************80
    #
    # R8VEC_SFTF computes a "slow" forward Fourier transform of real data.
    #
    #  Discussion:
    #
    #    SFTF and SFTB are inverses of each other.  If we begin with data
    #    R and apply SFTB to it, and then apply SFTB to the resulting AZERO,
    #    A, and B, we should get back the original R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data values.
    #
    #    Input, real R(N), the data to be transformed.
    #
    #    Output, real AZERO, = sum ( 1 <= I <= N ) R(I) / N.
    #
    #    Output, real A(N/2), B(N/2), the Fourier coefficients.
    #

    azero = np.sum(r) / float(n)
    nhalf = int(n / 2)
    a = np.zeros(nhalf)
    b = np.zeros(nhalf)

    for i in range(0, nhalf):
        for j in range(0, n):
            theta = float(2 * (i + 1) * j) * np.pi / float(n)
            a[i] = a[i] + r[j] * np.cos(theta)
            b[i] = b[i] + r[j] * np.sin(theta)

        a[i] = a[i] / float(n)
        b[i] = b[i] / float(n)

        if ((n % 2) == 1 or i < nhalf - 1):
            a[i] = 2.0 * a[i]
            b[i] = 2.0 * b[i]

    return azero, a, b


def r8vec_sftf_test():

    # *****************************************************************************80
    #
    # R8VEC_SFTF_TEST tests R8VEC_SFTF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_SFTF_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_SFTF computes the "slow" Fourier transform (forward)')
    print('  of a vector of real data.')
    print('  The original data can be recovered using R8VEC_SFTB.')

    n = 15
    seed = 123456789
    r, seed = r8vec_uniform_01(n, seed)

    azero, a, b = r8vec_sftf(n, r)
    nhalf = int(n / 2)
    r2 = r8vec_sftb(n, azero, a, b)

    print('')
    print('  Fourier coefficients:')
    print('')
    print('  %10f' % (azero))
    for i in range(0, nhalf):
        print('  %10f  %10f' % (a[i], b[i]))

    print('')
    print('  Compare data R and recovered data R2:')
    print('')
    for i in range(0, n):
        print('  %10f  %10f' % (r[i], r2[i]))

    print('')
    print('R8VEC_SFTF_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    colored_noise_test()
    timestamp()
