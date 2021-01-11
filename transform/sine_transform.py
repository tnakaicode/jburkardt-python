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

from r8lib.r8vec3_print import r8vec3_print
from r8lib.r8vec2_print import r8vec2_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8vec_linspace2 import r8vec_linspace2
from r8lib.r8vec_linspace import r8vec_linspace
from r8lib.r8vec_uniform_01 import r8vec_uniform_01

obj = plot2d()

def cosine_sum(x):

    # *****************************************************************************80
    #
    # COSINE_SUM evaluates a function which is a cosine sum.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument.
    #
    #    Output, real VALUE, the value.
    #

    value = np.cos(x) \
        + 5.0 * np.cos(1.6 * x) \
        - 2.0 * np.cos(2.0 * x) \
        + 5.0 * np.cos(4.5 * x) \
        + 7.0 * np.cos(9.0 * x)

    return value


def poly5(x):

    # *****************************************************************************80
    #
    # POLY5 evaluates a particular fifth-degree polynomial.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument.
    #
    #    Output, real VALUE, the value of the polynomial at X.
    #
    value = (x - 0.1) * \
            (x - 0.2) * \
            (x - 0.4) * \
            (x - 2.1) * \
            (x - 3.0)

    return value


def sine_transform_data(n, d):

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_DATA does a sine transform on a vector of data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data points.
    #
    #    Input, real D(N), the vector of data.
    #
    #    Output, real S(N), the sine transform coefficients.
    #

    s = np.zeros(n)

    for i in range(0, n):
        for j in range(0, n):
            s[i] = s[i] + np.sin(np.pi * float((i + 1) *
                                               (j + 1)) / float(n + 1)) * d[j]
        s[i] = s[i] * np.sqrt(float(2) / float(n + 1))

    return s


def sine_transform_data_test():

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_DATA_TEST tests SINE_TRANSFORM_DATA.
    #
    #  Discussion:
    #
    #    This program demonstrates that the transform is its own inverse.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2012
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('SINE_TRANSFORM_DATA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SINE_TRANSFORM_DATA does a sine transform of data')
    print('  defined by a vector.')
    print('')
    print('  Demonstrate that the transform is its own inverse.')
    print('  Let R be a random N vector.')
    print('  Let S be the transform of D.')
    print('  Let T be the transform of E.')
    print('  Then R and T will be equal.')

    seed = 123456789
    r, seed = r8vec_uniform_01(n, seed)
    s = sine_transform_data(n, r)
    t = sine_transform_data(n, s)

    r8vec3_print(n, r, s, t, '       I          R             S             T')

    print('')
    print('SINE_TRANSFORM_DATA_TEST')
    print('  Normal end of execution.')


def sine_transform_function(n, a, b, f):

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_FUNCTION does a sine transform on functional data.
    #
    #  Discussion:
    #
    #    The interval [A,B] is divided into N+1 intervals using N+2 points,
    #    which are indexed by 0 through N+1.
    #
    #    The original function F(X) is regarded as the sum of a linear function
    #    F1 that passes through (A,F(A)) and (B,F(B)), and a function F2
    #    which is 0 at A and B.
    #
    #    The sine transform coefficients for F2 are then computed.
    #
    #    To recover the interpolant of F(X), it is necessary to combine the
    #    linear part F1 with the sine transform interpolant:
    #
    #      Interp(F)(X) = F1(X) + F2(X)
    #
    #    This can be done by calling SINE_TRANSFORM_INTERPOLANT().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data points.
    #
    #    Input, real A, B, the interval endpoints.
    #
    #    Input, function value = F ( x ), a pointer to the function.
    #
    #    Output, real S(N), the sine transform coefficients.
    #

    x = r8vec_linspace2(n, a, b)
    #
    #  Subtract F1(X) from F(X) to get F2(X).
    #
    fa = f(a)
    fb = f(b)

    f2 = np.zeros(n)

    for i in range(0, n):
        f2[i] = f(x[i]) - ((b - x[i]) * fa
                           + (x[i] - a) * fb) \
            / (b - a)
    #
    #  Compute the sine transform of F2(X).
    #
    s = sine_transform_data(n, f2)

    return s


def sine_transform_function_test():

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_FUNCTION_TEST tests SINE_TRANSFORM_FUNCTION.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 9
    a = 1.0
    b = 3.0
    x = r8vec_linspace2(n, a, b)

    print('')
    print('SINE_TRANSFORM_FUNCTION_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SINE_TRANSFORM_FUNCTION does a sine transform of data')
    print('  defined by a function F(X) evaluated at equally spaced')
    print('  points in an interval [A,B].')
    print('')
    print('  Demonstrate that the transform is its own inverse.')
    print('  Let X(0:N+1) be N+2 equally spaced points in [A,B].')
    print('  Let S be the transform of F(X(1:N)).')
    print('  Let F1 be the linear interpolant of (A,F(A)), (B,F(B)).')
    print('  Let F2 be the transform of S.')
    print('  Then F(X(1:N)) = F1(X(1:N)) + F2(1:N).')

    s = sine_transform_function(n, a, b, poly5)

    fa = poly5(a)
    fb = poly5(b)

    f1 = np.zeros(n + 2)

    f1[0] = fa
    for i in range(1, n + 1):
        f1[i] = ((b - x[i - 1]) * fa
                 + (x[i - 1] - a) * fb) \
            / (b - a)
    f1[n + 1] = fb

    f2 = sine_transform_data(n, s)

    print('')
    print('     I      X(I)      F(X(I))       S           F1          F2          F1+F2')
    print('')

    print('  %4d  %10f  %10f  %10f  %10f  %10f  %10f'
          % (0, a, poly5(a), 0.0, f1[0], 0.0, f1[0]))

    for i in range(1, n + 1):
        print('  %4d  %10f  %10f  %10f  %10f  %10f  %10f'
              % (i, x[i - 1], poly5(x[i - 1]), s[i - 1], f1[i], f2[i - 1], f1[i] + f2[i - 1]))

    print('  %4d  %10f  %10f  %10f  %10f  %10f  %10f'
          % (n + 1, b, poly5(b), 0.0, f1[n + 1], 0.0, f1[n + 1]))
    print('')
    print('SINE_TRANSFORM_FUNCTION_TEST')
    print('  Normal end of execution.')


def sine_transform_interpolant(n, a, b, fa, fb, s, nx, x):

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_INTERPOLANT evaluates the sine transform interpolant.
    #
    #  Discussion:
    #
    #    The interval [A,B] is divided into N+1 intervals using N+2 points,
    #    which are indexed by 0 through N+1.
    #
    #    The original function F(X) is regarded as the sum of a linear function
    #    F1 that passes through (A,F(A)) and (B,F(B)), and a function F2
    #    which is 0 at A and B.
    #
    #    The function F2 has been approximated using the sine transform,
    #    and the interpolant is then evaluated as:
    #
    #      Interp(F)(X) = F1(X) + F2(X)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of terms in the approximation.
    #
    #    Input, real A, B, the interval over which the approximant was defined.
    #
    #    Input, real FA, FB, the function values at A and B.
    #
    #    Input, real S(N), the approximant coefficients.
    #
    #    Input, integer NX, the number of evaluation points.
    #
    #    Input, real X(NX), the evaluation points.
    #
    #    Output, real VALUE(NX), the value of the interpolant.
    #

    #  Compute linear function F1(X).
    f1 = np.zeros(nx)

    for i in range(0, nx):
        f1[i] = ((b - x[i]) * fa
                 + (x[i] - a) * fb) \
            / (b - a)

    #  Compute sine interpolant F2(X).
    f2 = np.zeros(nx)

    for i in range(0, nx):
        for j in range(0, n):
            f2[i] = f2[i] + s[j] \
                * np.sin(np.pi * float(j + 1) * (x[i] - a) / (b - a))
        f2[i] = f2[i] * np.sqrt(2.0 / float(n + 1))

    #  Interpolant = F1 + F2.
    value = np.zeros(nx)
    for i in range(0, nx):
        value[i] = f1[i] + f2[i]

    return value


def sine_transform_interpolant_test1():

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_INTERPOLANT_TEST tests SINE_TRANSFORM_INTERPOLANT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SINE_TRANSFORM_INTERPOLANT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SINE_TRANSFORM_FUNCTION does a sine transform of data')
    print('  defined by a function F(X) evaluated at N equally spaced')
    print('  points in an interval [A,B].')
    print('  SINE_TRANSFORM_INTERPOLANT evaluates the interpolant.')
    print('')
    print('  The interpolant will be 0 at the 0th and (N+1)-th points.')
    print('  It equals the function at points 1 through N.')
    print('  In between, it can approximate smooth functions,')
    print('  and the approximation improves with N.')
    
    #
    #  N determines the number of data points, indexed by 1 to N.
    #  However, we essentially have N+2 data points, indexed 0 to N+1,
    #  with the data value being 0 at the first and last auxilliary points.
    #
    
    n = 9
    a = 1.0
    b = 4.0
    x = r8vec_linspace2(n, a, b)
    
    #
    #  Determine the interpolant coefficients.
    #
    s = sine_transform_function(n, a, b, poly5)

    px = np.zeros(n)
    for i in range(0, n):
        px[i] = poly5(x[i])

    r8vec3_print(n, x, px, s, '     I      X(I)      F(X(I))        S(I)')
    
    #
    #  Evaluate the interpolant.
    #
    fa = poly5(a)
    fb = poly5(b)
    n2 = 1 + 2 * (n + 1)
    x2 = np.linspace(a, b, n2)
    f2 = sine_transform_interpolant(n, a, b, fa, fb, s, n2, x2)

    px2 = np.zeros(n2)
    for i in range(0, n2):
        px2[i] = poly5(x2[i])

    r8vec3_print(n2, x2, px2, f2,
                 '     I      X            F(X)        FHAT(X)')

    n3 = 501
    x3 = np.linspace(a, b, n3)
    px3 = np.zeros(n3)
    for i in range(0, n3):
        px3[i] = poly5(x3[i])
    
    #
    #  Plot the sample points as blue dots,
    #  the interpolant as a red line,
    #  the exact function as a black line.
    #
    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, px, 'b*', markersize=20)
    obj.axs.plot(x2, f2, 'r-', linewidth=8.0)
    obj.axs.plot(x3, px3, 'k-', linewidth=2.0)
    obj.axs.set_title('Data (stars), interpolant (red), exact (black)')
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.legend()
    obj.SavePng('sine_interpolant1.png')
    
    print('')
    print('  Created plot file "sine_interpolant.png"')
    print('')
    print('SINE_TRANSFORM_INTERPOLANT_TEST')
    print('  Normal end of execution.')


def sine_transform_interpolant_test2():

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_INTERPOLANT_TEST2 evaluates the sine transform interpolant.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SINE_TRANSFORM_INTERPOLANT_TEST2:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SINE_TRANSFORM_FUNCTION does a sine transform of data')
    print('  defined by a function F(X) evaluated at N equally spaced')
    print('  points in an interval [A,B].')
    print('  SINE_TRANSFORM_INTERPOLANT evaluates the interpolant.')
    print('')
    print('  The interpolant will be 0 at the 0th and (N+1)-th points.')
    print('  It equals the function at points 1 through N.')
    print('  In between, it can approximate smooth functions,')
    print('  and the approximation improves with N.')
    
    #
    #  N determines the number of data points, indexed by 1 to N.
    #  However, we essentially have N+2 data points, indexed 0 to N+1,
    #  with the data value being 0 at the first and last auxilliary points.
    #
    n = 15
    a = 0.0
    b = 7.0
    x = r8vec_linspace2(n, a, b)
    f = np.zeros(n)
    for i in range(0, n):
        f[i] = cosine_sum(x[i])
    
    #
    #  Determine the interpolant coefficients.
    #
    s = sine_transform_function(n, a, b, cosine_sum)
    
    #
    #  Evaluate the interpolant.
    #
    fa = cosine_sum(a)
    fb = cosine_sum(b)
    n2 = 1 + 5 * (n + 1)
    x2 = np.linspace(a, b, n2)
    f2 = sine_transform_interpolant(n, a, b, fa, fb, s, n2, x2)
    
    #
    #  Plot the sample points as blue dots,
    #  the approximant as a red line,
    #  the exact function as a black line.
    #
    n3 = 501
    x3 = np.linspace(a, b, n3)
    f3 = np.zeros(n3)
    for i in range(0, n3):
        f3[i] = cosine_sum(x3[i])
        
    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, f, 'b*', markersize=20)
    obj.axs.plot(x2, f2, 'r-', linewidth=8)
    obj.axs.plot(x3, f3, 'k-', linewidth=2)
    obj.axs.set_title('Data (stars), interpolant (red), exact (black)')
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.legend()
    obj.SavePng('sine_interpolant2.png')

    print('')
    print('  Created plot file "sine_interpolant2.png"')
    print('')
    print('SINE_TRANSFORM_INTERPOLANT2_TEST')
    print('  Normal end of execution.')


def sine_transform_test():

    # *****************************************************************************80
    #
    # SINE_TRANSFORM_TEST tests the SINE_TRANSFORM library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SINE_TRANSFORM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SINE_TRANSFORM library.')

    sine_transform_data_test()
    sine_transform_function_test()
    sine_transform_interpolant_test1()
    sine_transform_interpolant_test2()

    print('')
    print('SINE_TRANSFORM_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    sine_transform_test()
    timestamp()
