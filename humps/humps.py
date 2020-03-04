#! /usr/bin/env python3
#


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
    import numpy as np

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
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('humps_antideriv_test')
    print('  Python version')
    print('  Test humps_antideriv.')

    a = 0.0
    b = 2.0
    x = np.linspace(0.0, 2.0, 101)
    y = humps_antideriv(x)

    plt.clf()

    plt.plot(x, y, 'g-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        plt.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        plt.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    plt.grid(True)
    plt.xlabel('<--- X --->')
    plt.ylabel('<--- Y --->')
    plt.title('The y = antideriv humps(x)')
    filename = 'humps_antideriv.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('humps_antideriv_test:')
    print('  Normal end of execution.')

    return


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

    plt.clf()

    plt.plot(x, y, 'r-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        plt.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        plt.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    plt.grid(True)
    plt.xlabel('<--- X --->')
    plt.ylabel('<--- Y --->')
    plt.title('y = humps"(x)')
    filename = 'humps_deriv2.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('humps_deriv_test:')
    print('  Normal end of execution.')

    return


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
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('humps_deriv_test')
    print('  Python version')
    print('  Test humps_deriv.')

    a = 0.0
    b = 2.0
    x = np.linspace(a, b, 101)
    y = humps_deriv(x)

    plt.clf()

    plt.plot(x, y, 'r-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        plt.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        plt.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    plt.grid(True)
    plt.xlabel('<--- X --->')
    plt.ylabel('<--- Y --->')
    plt.title('y = humps\'(x)')
    filename = 'humps_deriv.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('humps_deriv_test:')
    print('  Normal end of execution.')

    return


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
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('humps_fun_test')
    print('  Python version')
    print('  Test humps_fun.')

    a = 0.0
    b = 2.0
    x = np.linspace(a, b, 101)
    y = humps_fun(x)

    plt.clf()

    plt.plot(x, y, 'b-', linewidth=2)

    if (a <= 0.0 and 0.0 <= b):
        plt.plot([a, b], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        plt.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    plt.grid(True)
    plt.xlabel('<--- X --->')
    plt.ylabel('<--- Y --->')
    plt.title('y = humps(x)')
    filename = 'humps_fun.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('humps_fun_test:')
    print('  Normal end of execution.')

    return


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
#
#  Terminate.
#
    print('')
    print('humps_test:')
    print('  Normal end of execution.')

    return


def timestamp():

    # *****************************************************************************80
    #
    # timestamp prints the date as a timestamp.
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


if (__name__ == '__main__'):
    timestamp()
    humps_test()
    timestamp()
