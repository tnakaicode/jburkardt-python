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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose import r8vec_transpose_print
from r8lib.r8mat_transpose import r8mat_transpose_print, r8mat_transpose_print_some

obj = plot2d()


def humps_antideriv(x):

    # *****************************************************************************80
    #
    # humps_antideriv evaluates the antiderivative of the humps function.
    #
    #  Discussion:
    #
    #    y = 1.0 ./ ( ( x - 0.3 )**2 + 0.01 ) \
    #      + 1.0 ./ ( ( x - 0.9 )**2 + 0.04 ) \
    #      - 6.0
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the argument.
    #
    #  Output:
    #
    #    real ya(): the value of the antiderivative at x.
    #

    ya = (1.0 / 0.1) * np.arctan((x - 0.3) / 0.1) \
        + (1.0 / 0.2) * np.arctan((x - 0.9) / 0.2) \
        - 6.0 * x

    return ya


def humps_antideriv_test():

    # *****************************************************************************80
    #
    # humps_antideriv_test tests humps_antideriv.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('humps_antideriv_test')
    print('  Python version')
    print('  Test humps_antideriv.')

    a = 0.0
    b = 2.0
    x = np.linspace(0.0, 2.0, 101)
    y = humps_antideriv(x)

    filename = 'humps_antideriv.png'

    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, y, 'g-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        obj.axs.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        obj.axs.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    obj.axs.set_xlabel('<--- X --->')
    obj.axs.set_ylabel('<--- Y --->')
    obj.axs.set_title('The y = antideriv humps(x)')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))
    print('')
    print('humps_antideriv_test:')
    print('  Normal end of execution.')


def humps_deriv2(x):

    # *****************************************************************************80
    #
    # humps_deriv2 evaluates the second derivative of the humps function.
    #
    #  Discussion:
    #
    #    y = 1.0 ./ ( ( x - 0.3 )**2 + 0.01 ) \
    #      + 1.0 ./ ( ( x - 0.9 )**2 + 0.04 ) \
    #      - 6.0
    #
    #    yp = - 2.0 .* ( x - 0.3 ) ./ ( ( x - 0.3 )**2 + 0.01 )**2 \
    #         - 2.0 .* ( x - 0.9 ) ./ ( ( x - 0.9 )**2 + 0.04 )**2
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the arguments.
    #
    #  Output:
    #
    #    real ypp(): the value of the second derivative at x.
    #
    u1 = - 2.0 * (x - 0.3)
    v1 = ((x - 0.3)**2 + 0.01)**2
    u2 = - 2.0 * (x - 0.9)
    v2 = ((x - 0.9)**2 + 0.04)**2

    u1p = - 2.0
    v1p = 2.0 * ((x - 0.3)**2 + 0.01) * 2.0 * (x - 0.3)
    u2p = - 2.0
    v2p = 2.0 * ((x - 0.9)**2 + 0.04) * 2.0 * (x - 0.9)

    ypp = (u1p * v1 - u1 * v1p) / v1**2 \
        + (u2p * v2 - u2 * v2p) / v2**2

    return ypp


def humps_deriv2_test():

    # *****************************************************************************80
    #
    # humps_deriv2_test tests humps_deriv2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('humps_deriv2_test')
    print('  Python version')
    print('  Test humps_deriv2.')

    a = 0.0
    b = 2.0
    x = np.linspace(a, b, 101)
    y = humps_deriv2(x)

    filename = 'humps_deriv2.png'

    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, y, 'r-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        obj.axs.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        obj.axs.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    obj.axs.set_xlabel('<--- X --->')
    obj.axs.set_ylabel('<--- Y --->')
    obj.axs.set_title('y = humps"(x)')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))
    print('')
    print('humps_deriv_test:')
    print('  Normal end of execution.')


def humps_deriv(x):

    # *****************************************************************************80
    #
    # humps_deriv evaluates the derivative of the humps function.
    #
    #  Discussion:
    #
    #    y = 1.0 ./ ( ( x - 0.3 )**2 + 0.01 ) \
    #      + 1.0 ./ ( ( x - 0.9 )**2 + 0.04 ) \
    #      - 6.0
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the arguments.
    #
    #  Output:
    #
    #    real yp(): the value of the derivative at x.
    #
    yp = - 2.0 * (x - 0.3) / ((x - 0.3)**2 + 0.01)**2 \
         - 2.0 * (x - 0.9) / ((x - 0.9)**2 + 0.04)**2

    return yp


def humps_deriv_test():

    # *****************************************************************************80
    #
    # humps_deriv_test tests humps_deriv.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('humps_deriv_test')
    print('  Python version')
    print('  Test humps_deriv.')

    a = 0.0
    b = 2.0
    x = np.linspace(a, b, 101)
    y = humps_deriv(x)

    filename = 'humps_deriv.png'

    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, y, 'r-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        obj.axs.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        obj.axs.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    obj.axs.set_xlabel('<--- X --->')
    obj.axs.set_ylabel('<--- Y --->')
    obj.axs.set_title('y = humps"(x)')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))
    print('')
    print('humps_deriv_test:')
    print('  Normal end of execution.')


def humps_fun(x):

    # *****************************************************************************80
    #
    # humps_fun evaluates the humps function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the evaluation points.
    #
    #  Output:
    #
    #    real y(): the def values.
    #

    y = 1.0 / ((x - 0.3)**2 + 0.01) \
        + 1.0 / ((x - 0.9)**2 + 0.04) \
        - 6.0
    return y


def humps_fun_test():

    # *****************************************************************************80
    #
    # humps_fun_test tests humps_fun.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('humps_fun_test')
    print('  Python version')
    print('  Test humps_fun.')

    a = 0.0
    b = 2.0
    x = np.linspace(a, b, 101)
    y = humps_fun(x)

    filename = 'humps_fun.png'

    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(x, y, 'b-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        obj.axs.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        obj.axs.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    obj.axs.set_xlabel('<--- X --->')
    obj.axs.set_ylabel('<--- Y --->')
    obj.axs.set_title('y = humps"(x)')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))
    print('')
    print('humps_fun_test:')
    print('  Normal end of execution.')


def humps_ode(x, y):

    # *****************************************************************************80
    #
    # humps_ode evaluates the derivative of the humps def for an ODE solver.
    #
    #  Discussion:
    #
    #    This verion of "humps_deriv" appends the input argument "y", as expected
    #    by most ODE solving software.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the arguments.
    #
    #    real y(): the value of the humps function.
    #
    #  Output:
    #
    #    real yp(): the value of the derivative of the humps function.
    #
    yp = - 1.0 / ((x - 0.3)**2 + 0.01)**2 \
        * 2.0 * (x - 0.3) \
        - 1.0 / ((x - 0.9)**2 + 0.04)**2 \
        * 2.0 * (x - 0.9)

    return yp


def humps_test():

    # *****************************************************************************80
    #
    # humps_test tests humps.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('humps_test')
    print('  Python version')
    print('  Test humps.')

    humps_antideriv_test()
    humps_fun_test()
    humps_deriv_test()
    humps_deriv2_test()

    print('')
    print('humps_test:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    humps_test()
    timestamp()
