#! /usr/bin/env python3
#


def f00_f0(fi, n, x, y):

    # *****************************************************************************80
    #
    # F00_F0 returns the value of any function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FI, the index of the function.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    from sys import exit

    if (fi == 1):
        f = f01_f0(n, x, y)
    elif (fi == 2):
        f = f02_f0(n, x, y)
    elif (fi == 3):
        f = f03_f0(n, x, y)
    elif (fi == 4):
        f = f04_f0(n, x, y)
    elif (fi == 5):
        f = f05_f0(n, x, y)
    elif (fi == 6):
        f = f06_f0(n, x, y)
    elif (fi == 7):
        f = f07_f0(n, x, y)
    elif (fi == 8):
        f = f08_f0(n, x, y)
    elif (fi == 9):
        f = f09_f0(n, x, y)
    elif (fi == 10):
        f = f10_f0(n, x, y)
    elif (fi == 11):
        f = f11_f0(n, x, y)
    elif (fi == 12):
        f = f12_f0(n, x, y)
    elif (fi == 13):
        f = f13_f0(n, x, y)
    else:
        print('')
        print('F00_F0 - Fatal error!')
        print('  Illegal function index FI = %d' % (fi))
        exit('F00_F0 - Fatal error!')

    return f


def f00_f1(fi, n, x, y):

    # *****************************************************************************80
    #
    # F00_F1 returns first derivatives of any function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FI, the index of the function.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the first derivative values.
    #
    from sys import exit

    if (fi == 1):
        fx, fy = f01_f1(n, x, y)
    elif (fi == 2):
        fx, fy = f02_f1(n, x, y)
    elif (fi == 3):
        fx, fy = f03_f1(n, x, y)
    elif (fi == 4):
        fx, fy = f04_f1(n, x, y)
    elif (fi == 5):
        fx, fy = f05_f1(n, x, y)
    elif (fi == 6):
        fx, fy = f06_f1(n, x, y)
    elif (fi == 7):
        fx, fy = f07_f1(n, x, y)
    elif (fi == 8):
        fx, fy = f08_f1(n, x, y)
    elif (fi == 9):
        fx, fy = f09_f1(n, x, y)
    elif (fi == 10):
        fx, fy = f10_f1(n, x, y)
    elif (fi == 11):
        fx, fy = f11_f1(n, x, y)
    elif (fi == 12):
        fx, fy = f12_f1(n, x, y)
    elif (fi == 13):
        fx, fy = f13_f1(n, x, y)
    else:
        print('')
        print('F00_F1 - Fatal error!')
        print('  Illegal function index FI = %d' % (fi))
        exit('F00_F1 - Fatal error!')

    return fx, fy


def f00_f2(fi, n, x, y):

    # *****************************************************************************80
    #
    # F00_F2 returns second derivatives of any function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FI, the index of the function.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), the second derivatives.
    #
    from sys import exit

    if (fi == 1):
        fxx, fxy, fyy = f01_f2(n, x, y)
    elif (fi == 2):
        fxx, fxy, fyy = f02_f2(n, x, y)
    elif (fi == 3):
        fxx, fxy, fyy = f03_f2(n, x, y)
    elif (fi == 4):
        fxx, fxy, fyy = f04_f2(n, x, y)
    elif (fi == 5):
        fxx, fxy, fyy = f05_f2(n, x, y)
    elif (fi == 6):
        fxx, fxy, fyy = f06_f2(n, x, y)
    elif (fi == 7):
        fxx, fxy, fyy = f07_f2(n, x, y)
    elif (fi == 8):
        fxx, fxy, fyy = f08_f2(n, x, y)
    elif (fi == 9):
        fxx, fxy, fyy = f09_f2(n, x, y)
    elif (fi == 10):
        fxx, fxy, fyy = f10_f2(n, x, y)
    elif (fi == 11):
        fxx, fxy, fyy = f11_f2(n, x, y)
    elif (fi == 12):
        fxx, fxy, fyy = f12_f2(n, x, y)
    elif (fi == 13):
        fxx, fxy, fyy = f13_f2(n, x, y)
    else:
        print('')
        print('F00_F2 - Fatal error!')
        print('  Illegal function index FI = %d' % (fi))
        exit('F00_F2 - Fatal error!')

    return fxx, fxy, fyy


def f00_num():

    # *****************************************************************************80
    #
    # F00_NUM returns the number of test functions available.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #   Output, integer FUN_NUM, the number of test functions.
    #
    fun_num = 13

    return fun_num


def f00_title(fi):

    # *****************************************************************************80
    #
    # F00_TITLE returns the title for any function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FI, the index of the function.
    #
    #    Output, string TITLE, the function title.
    #
    from sys import exit

    if (fi == 1):
        title = f01_title()
    elif (fi == 2):
        title = f02_title()
    elif (fi == 3):
        title = f03_title()
    elif (fi == 4):
        title = f04_title()
    elif (fi == 5):
        title = f05_title()
    elif (fi == 6):
        title = f06_title()
    elif (fi == 7):
        title = f07_title()
    elif (fi == 8):
        title = f08_title()
    elif (fi == 9):
        title = f09_title()
    elif (fi == 10):
        title = f10_title()
    elif (fi == 11):
        title = f11_title()
    elif (fi == 12):
        title = f12_title()
    elif (fi == 13):
        title = f13_title()
    else:
        print('')
        print('F00_TITLE - Fatal error!')
        print('  Illegal function index FI = %d' % (fi))
        exit('F00_TITLE - Fatal error!')

    return title


def f01_f0(n, x, y):

    # *****************************************************************************80
    #
    # F01_F0 returns the value of function 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = \
        0.75 * np.exp(- ((9.0 * x[0:n] - 2.0) ** 2
                         + (9.0 * y[0:n] - 2.0) ** 2) / 4.0)  \
        + 0.75 * np.exp(- ((9.0 * x[0:n] + 1.0) ** 2) / 49.0
                        - (9.0 * y[0:n] + 1.0) / 10.0)        \
        + 0.5 * np.exp(- ((9.0 * x[0:n] - 7.0) ** 2
                          + (9.0 * y[0:n] - 3.0) ** 2) / 4.0)  \
        - 0.2 * np.exp(- (9.0 * x[0:n] - 4.0) ** 2
                       - (9.0 * y[0:n] - 7.0) ** 2)

    return f


def f01_f1(n, x, y):

    # *****************************************************************************80
    #
    # F01_F1 returns first derivatives of function 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    for i in range(0, n):

        t1 = np.exp(- ((9.0 * x[i] - 2.0) ** 2
                       + (9.0 * y[i] - 2.0) ** 2) / 4.0)
        t2 = np.exp(- ((9.0 * x[i] + 1.0) ** 2) / 49.0
                    - (9.0 * y[i] + 1.0) / 10.0)
        t3 = np.exp(- ((9.0 * x[i] - 7.0) ** 2
                       + (9.0 * y[i] - 3.0) ** 2) / 4.0)
        t4 = np.exp(- (9.0 * x[i] - 4.0) ** 2
                    - (9.0 * y[i] - 7.0) ** 2)

        fx[i] = \
            - 3.375 * (9.0 * x[i] - 2.0) * t1 \
            - (27.0 / 98.0) * (9.0 * x[i] + 1.0) * t2 \
            - 2.25 * (9.0 * x[i] - 7.0) * t3 \
            + 3.6 * (9.0 * x[i] - 4.0) * t4

        fy[i] = \
            - 3.375 * (9.0 * y[i] - 2.0) * t1 \
            - 0.675 * t2 \
            - 2.25 * (9.0 * y[i] - 3.0) * t3 \
            + 3.6 * (9.0 * y[i] - 7.0) * t4

    return fx, fy


def f01_f2(n, x, y):

    # *****************************************************************************80
    #
    # F01_F2 returns second derivatives of function 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)

    for i in range(0, n):

        t1 = np.exp(- ((9.0 * x[i] - 2.0) ** 2
                       + (9.0 * y[i] - 2.0) ** 2) / 4.0)
        t2 = np.exp(- ((9.0 * x[i] + 1.0) ** 2) / 49.0
                    - (9.0 * y[i] + 1.0) / 10.0)
        t3 = np.exp(- ((9.0 * x[i] - 7.0) ** 2
                       + (9.0 * y[i] - 3.0) ** 2) / 4.0)
        t4 = np.exp(- (9.0 * x[i] - 4.0) ** 2
                    - (9.0 * y[i] - 7.0) ** 2)

        fxx[i] = \
            15.1875 * ((9.0 * x[i] - 2.0) ** 2 - 2.0) * t1 \
            + 60.75 * ((9.0 * x[i] + 1.0) ** 2 - 24.5) * t2 \
            + 10.125 * ((9.0 * x[i] - 7.0) ** 2 - 2.0) * t3 \
            - 64.8 * ((9.0 * x[i] - 4.0) ** 2 - 0.5) * t4

        fxy[i] = \
            15.1875 * (9.0 * x[i] - 2.0) * (9.0 * y[i] - 2.0) * t1 \
            + (243.0 / 980.0) * (9.0 * x[i] + 1.0) * t2 \
            + 10.125 * (9.0 * x[i] - 7.0) * (9.0 * y[i] - 3.0) * t3 \
            - 64.8 * (9.0 * x[i] - 4.0) * (9.0 * y[i] - 7.0) * t4

    fyy[0:n] = \
        15.1875 * ((9.0 * y[0:n] - 2.0) ** 2 - 2.0) * t1[0:n] \
        + 0.6075 * t2[0:n] \
        + 10.125 * ((9.0 * y[0:n] - 3.0) ** 2 - 2.0) * t3[0:n] \
        - 64.8 * ((9.0 * y[0:n] - 7.0) ** 2 - 0.5) * t4[0:n]

    return fxx, fxy, fyy


def f01_title():

    # *****************************************************************************80
    #
    # F01_TITLE returns the title for function 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Exponential'

    return title


def f02_f0(n, x, y):

    # *****************************************************************************80
    #
    # F02_F0 returns the value of function 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = (np.tanh(9.0 * (y[0:n] - x[0:n])) + 1.0) / 9.0

    return f


def f02_f1(n, x, y):

    # *****************************************************************************80
    #
    # F02_F1 returns first derivatives of function 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    for i in range(0, n):
        t1[i] = 18.0 * (y[i] - x[i])
        fx[i] = - 4.0 / (np.exp(t1) + 2.0 + np.exp(- t1))
        fy[i] = - fx[i]

    return fx, fy


def f02_f2(n, x, y):

    # *****************************************************************************80
    #
    # F02_F2 returns second derivatives of function 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)

    t1[0:n] = 18.0 * (y[0:n] - x[0:n])

    fxx[0:n] = 18.0 * np.tanh(0.5 * t1[0:n]) \
        * (np.tanh(9.0 * (y[0:n] - x[0:n])) + 1.0) / 9.0
    fxy[0:n] = - fxx[0:n]
    fyy[0:n] = fxx[0:n]

    return fxx, fxy, fyy


def f02_title():

    # *****************************************************************************80
    #
    # F02_TITLE returns the title for function 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Cliff'

    return title


def f03_f0(n, x, y):

    # *****************************************************************************80
    #
    # F03_F0 returns the value of function 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = (1.25 + np.cos(5.4 * y[0:n])) \
        / (6.0 + 6.0 * (3.0 * x[0:n] - 1.0) ** 2)

    return f


def f03_f1(n, x, y):

    # *****************************************************************************80
    #
    # F03_F1 returns first derivatives of function 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    for i in range(0, n):
        t1 = 5.4 * y[i]
        t2 = 1.0 + (3.0 * x[i] - 1.0) ** 2
        fx[i] = - (3.0 * x[i] - 1.0) \
            * (1.25 + np.cos(t1)) / (t2 * t2)
        fy[i] = - 0.9 * np.sin(t1) / t2

    return fx, fy


def f03_f2(n, x, y):

    # *****************************************************************************80
    #
    # F03_F2 returns second derivatives of function 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)

    t1[0:n] = 5.4 * y[0:n]
    t2[0:n] = 1.0 + (3.0 * x[0:n] - 1.0) ** 2

    fxx[0:n] = 3.0 * (1.25 + np.cos(t1[0:n])) * (3.0 * t2[0:n] - 4.0) \
        / (t2[0:n] ** 3)
    fxy[0:n] = 5.4 * (3.0 * x[0:n] - 1.0) * np.sin(t1[0:n]) \
        / (t2[0:n] * t2[0:n])
    fyy[0:n] = - 4.86 * np.cos(t1[0:n]) / t2[0:n]

    return fxx, fxy, fyy


def f03_title():

    # *****************************************************************************80
    #
    # F03_TITLE returns the title for function 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Saddle'

    return title


def f04_f0(n, x, y):

    # *****************************************************************************80
    #
    # F04_F0 returns the value of function 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = np.exp(- 5.0625 * ((x[0:n] - 0.5) ** 2
                                + (y[0:n] - 0.5) ** 2)) / 3.0

    return f


def f04_f1(n, x, y):

    # *****************************************************************************80
    #
    # F04_F1 returns first derivatives of function 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)

    t1[0:n] = x[0:n] - 0.5
    t2[0:n] = y[0:n] - 0.5
    t3[0:n] = - 3.375 \
        * np.exp(- 5.0625 * (t1[0:n] * t1[0:n] + t2[0:n] * t2[0:n]))
    fx[0:n] = t1[0:n] * t3[0:n]
    fy[0:n] = t2[0:n] * t3[0:n]

    return fx, fy


def f04_f2(n, x, y):

    # *****************************************************************************80
    #
    # F04_F2 returns second derivatives of function 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)

    t1[0:n] = x[0:n] - 0.5
    t2[0:n] = y[0:n] - 0.5
    t3[0:n] = - 3.375 \
        * np.exp(- 5.0625 * (t1[0:n] * t1[0:n] + t2[0:n] * t2[0:n]))

    fxx[0:n] = (1.0 - 10.125 * t1[0:n] * t1[0:n]) * t3[0:n]
    fxy[0:n] = - 10.125 * t1[0:n] * t2[0:n] * t3[0:n]
    fyy[0:n] = (1.0 - 10.125 * t2[0:n] * t2[0:n]) * t3[0:n]

    return fxx, fxy, fyy


def f04_title():

    # *****************************************************************************80
    #
    # F04_TITLE returns the title for function 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Gentle'

    return title


def f05_f0(n, x, y):

    # *****************************************************************************80
    #
    # F05_F0 returns the value of function 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = np.exp(- 20.25 * ((x[0:n] - 0.5) ** 2
                               + (y[0:n] - 0.5) ** 2)) / 3.0

    return f


def f05_f1(n, x, y):

    # *****************************************************************************80
    #
    # F05_F1 returns first derivatives of function 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)

    t1[0:n] = x[0:n] - 0.5
    t2[0:n] = y[0:n] - 0.5
    t3[0:n] = - 13.5 * \
        np.exp(- 20.25 * (t1[0:n] * t1[0:n] + t2[0:n] * t2[0:n]))
    fx[0:n] = t1[0:n] * t3[0:n]
    fy[0:n] = t2[0:n] * t3[0:n]

    return fx, fy


def f05_f2(n, x, y):

    # *****************************************************************************80
    #
    # F05_F2 returns second derivatives of function 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)

    t1[0:n] = x[0:n] - 0.5
    t2[0:n] = y[0:n] - 0.5
    t3[0:n] = - 13.5 * \
        np.exp(- 20.25 * (t1[0:n] * t1[0:n] + t2[0:n] * t2[0:n]))

    fxx[0:n] = (1.0 - 40.5 * t1[0:n] * t1[0:n]) * t3[0:n]
    fxy[0:n] = - 40.5 * t1[0:n] * t2[0:n] * t3[0:n]
    fyy[0:n] = (1.0 - 40.5 * t2[0:n] * t2[0:n]) * t3[0:n]

    return fxx, fxy, fyy


def f05_title():

    # *****************************************************************************80
    #
    # F05_TITLE returns the title for function 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Steep'

    return title


def f06_f0(n, x, y):

    # *****************************************************************************80
    #
    # F06_F0 returns the value of function 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    for i in range(0, n):
        t4 = 64.0 - 81.0 * ((x[i] - 0.5) ** 2 + (y[i] - 0.5) ** 2)
        if (0.0 <= t4):
            f[i] = np.sqrt(t4) / 9.0 - 0.5

    return f


def f06_f1(n, x, y):

    # *****************************************************************************80
    #
    # F06_F1 returns first derivatives of function 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    for i in range(0, n):

        t4 = 64.0 - 81.0 * ((x[i] - 0.5) ** 2 + (y[i] - 0.5) ** 2)

        if (0.0 < t4):
            fx[i] = - 9.0 * (x(i) - 0.5) / np.sqrt(t4)
            fy[i] = - 9.0 * (y(i) - 0.5) / np.sqrt(t4)

    return fx, fy


def f06_f2(n, x, y):

    # *****************************************************************************80
    #
    # F06_F2 returns second derivatives of function 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)

    for i in range(0, n):

        t4 = 64.0 - 81.0 * ((x[i] - 0.5) ** 2 + (y[i] - 0.5) ** 2)

        if (0 < t4):
            t1 = x[i] - 0.5
            t2 = y[i] - 0.5
            t3 = - 9.0 / np.sqrt(t4)
            fxx[i] = (1.0 + t1 * t3 * t1 * t3) * t3
            fxy[i] = t1 * t3 * t2 * t3
            fyy[i] = (1.0 + t2 * t3 * t2 * t3) * t3

    return fxx, fxy, fyy


def f06_title():

    # *****************************************************************************80
    #
    # F06_TITLE returns the title for function 6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Sphere'

    return title


def f07_f0(n, x, y):

    # *****************************************************************************80
    #
    # F07_F0 returns the value of function 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = 2.0 * np.cos(10.0 * x[0:n]) * np.sin(10.0 * y[0:n]) \
        + np.sin(10.0 * x[0:n] * y[0:n])

    return f


def f07_f1(n, x, y):

    # *****************************************************************************80
    #
    # F07_F1 returns first derivatives of function 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)

    t1[0:n] = 10.0 * x[0:n]
    t2[0:n] = 10.0 * y[0:n]
    t3[0:n] = 10.0 * np.cos(10.0 * x[0:n] * y[0:n])
    fx[0:n] = - 20.0 * np.sin(t1[0:n]) * np.sin(t2[0:n]) + t3[0:n] * y[0:n]
    fy[0:n] = 20.0 * np.cos(t1[0:n]) * np.cos(t2[0:n]) + t3[0:n] * x[0:n]

    return fx, fy


def f07_f2(n, x, y):

    # *****************************************************************************80
    #
    # F07_F2 returns second derivatives of function 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)
    t4 = np.zeros(n)

    t1[0:n] = 10.0 * x[0:n]
    t2[0:n] = 10.0 * y[0:n]
    t3[0:n] = 10.0 * np.cos(10.0 * x[0:n] * y[0:n])
    t4[0:n] = 100.0 * np.sin(10.0 * x[0:n] * y[0:n])

    fxx[0:n] = - 200.0 * np.cos(t1[0:n]) * np.sin(t2[0:n]) \
        - t4[0:n] * y[0:n] * y[0:n]
    fxy[0:n] = - 200.0 * np.sin(t1[0:n]) * np.cos(t2[0:n]) \
        + t3[0:n] - t4[0:n] * x[0:n] * y[0:n]
    fyy[0:n] = - 200.0 * np.cos(t1[0:n]) * np.sin(t2[0:n]) \
        - t4[0:n] * x[0:n] * x[0:n]

    return fxx, fxy, fyy


def f07_title():

    # *****************************************************************************80
    #
    # F07_TITLE returns the title for function 7.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Trig'

    return title


def f08_f0(n, x, y):

    # *****************************************************************************80
    #
    # F08_F0 returns the value of function 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    for i in range(0, n):
        t1 = 5.0 - 10.0 * x[i]
        t2 = 5.0 - 10.0 * y[i]
        t3 = np.exp(- 0.5 * t1 * t1)
        t4 = np.exp(- 0.5 * t2 * t2)
        f[i] = t3 + 0.75 * t4 * (1.0 + t3)

    return f


def f08_f1(n, x, y):

    # *****************************************************************************80
    #
    # F08_F1 returns first derivatives of function 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)
    t4 = np.zeros(n)

    t1[0:n] = 5.0 - 10.0 * x[0:n]
    t2[0:n] = 5.0 - 10.0 * y[0:n]
    t3[0:n] = np.exp(- 0.5 * t1[0:n] * t1[0:n])
    t4[0:n] = np.exp(- 0.5 * t2[0:n] * t2[0:n])

    fx[0:n] = t1[0:n] * t3[0:n] * (10.0 + 7.5 * t4[0:n])
    fy[0:n] = t2[0:n] * t4[0:n] * (7.5 + 7.5 * t3[0:n])

    return fx, fy


def f08_f2(n, x, y):

    # *****************************************************************************80
    #
    # F08_F2 returns second derivatives of function 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)
    t4 = np.zeros(n)

    t1[0:n] = 5.0 - 10.0 * x[0:n]
    t2[0:n] = 5.0 - 10.0 * y[0:n]
    t3[0:n] = np.exp(- 0.5 * t1[0:n] * t1[0:n])
    t4[0:n] = np.exp(- 0.5 * t2[0:n] * t2[0:n])

    fxx[0:n] = t3[0:n] * (t1[0:n] * t1[0:n] - 1.0) * (100.0 + 75.0 * t4[0:n])
    fxy[0:n] = 75.0 * t1[0:n] * t2[0:n] * t3[0:n] * t4[0:n]
    fyy[0:n] = t4[0:n] * (t2[0:n] * t2[0:n] - 1.0) * (75.0 + 75.0 * t3[0:n])

    return fxx, fxy, fyy


def f08_title():

    # *****************************************************************************80
    #
    # F08_TITLE returns the title for function 8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Synergistic Gaussian'

    return title


def f09_f0(n, x, y):

    # *****************************************************************************80
    #
    # F09_F0 returns the value of function 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    for i in range(0, n):
        t1 = np.exp((10.0 - 20.0 * x[i]) / 3.0)
        t2 = np.exp((10.0 - 20.0 * y[i]) / 3.0)
        t3 = 1.0 / (1.0 + t1)
        t4 = 1.0 / (1.0 + t2)
        f[i] = ((20.0 / 3.0) ** 3 * t1 * t2) ** 2 \
            * (t3 * t4) ** 5 \
            * (t1 - 2.0 * t3) * (t2 - 2.0 * t4)

    return f


def f09_f1(n, x, y):

    # *****************************************************************************80
    #
    # F09_F1 returns first derivatives of function 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)
    t4 = np.zeros(n)

    t1[0:n] = np.exp((10.0 - 20.0 * x[0:n]) / 3.0)
    t2[0:n] = np.exp((10.0 - 20.0 * y[0:n]) / 3.0)
    t3[0:n] = 1.0 / (1.0 + t1[0:n])
    t4[0:n] = 1.0 / (1.0 + t2[0:n])

    fx[0:n] = ((20.0 / 3.0) * t1[0:n]) ** 2 * ((20.0 / 3.0) * t3[0:n]) ** 5 \
        * (2.0 * t1[0:n] - 3.0 * t3[0:n] - 5.0 + 12.0 * t3[0:n] * t3[0:n]) \
        * t2[0:n] * t2[0:n] * t4[0:n] ** 5 \
        * (t2[0:n] - 2.0 * t4[0:n])

    fy[0:n] = ((20.0 / 3.0) * t1[0:n]) ** 2 * ((20.0 / 3.0) * t3[0:n]) ** 5 \
        * (2.0 * t2[0:n] - 3.0 * t4[0:n] - 5.0 + 12.0 * t4[0:n] * t4[0:n]) \
        * t2[0:n] * t2[0:n] * t4[0:n] ** 5 \
        * (t1[0:n] - 2.0 * t3[0:n])

    return fx, fy


def f09_f2(n, x, y):

    # *****************************************************************************80
    #
    # F09_F2 returns second derivatives of function 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)
    t1 = np.zeros(n)
    t2 = np.zeros(n)
    t3 = np.zeros(n)
    t4 = np.zeros(n)
    t6 = np.zeros(n)

    t1[0:n] = np.exp((10.0 - 20.0 * x[0:n]) / 3.0)
    t2[0:n] = np.exp((10.0 - 20.0 * y[0:n]) / 3.0)
    t3[0:n] = 1.0 / (1.0 + t1[0:n])
    t4[0:n] = 1.0 / (1.0 + t2[0:n])
    t5 = 20.0 / 3.0
    t6[0:n] = (t5 * t1[0:n] * t2[0:n]) ** 2 * (t5 * t3[0:n] * t4[0:n]) ** 5

    fxx[0:n] = t5 * t6[0:n] * (t2[0:n] - 2.0 * t4[0:n]) \
        * (((- 84.0 * t3[0:n] + 78.0) * t3[0:n] + 23.0) * t3[0:n]
           + 4.0 * t1[0:n] - 25.0)

    fxy[0:n] = t5 * t6[0:n] \
        * ((12.0 * t4[0:n] - 3.0) * t4[0:n] + 2.0 * t2[0:n] - 5.0) \
        * ((12.0 * t3[0:n] - 3.0) * t3[0:n] + 2.0 * t1[0:n] - 5.0)

    fyy[0:n] = t5 * t6[0:n] * (t1[0:n] - 2.0 * t3[0:n]) \
        * (((- 84.0 * t4[0:n] + 78.0) * t4[0:n] + 23.0) * t4[0:n]
           + 4.0 * t2[0:n] - 25.0)

    return fxx, fxy, fyy


def f09_title():

    # *****************************************************************************80
    #
    # F09_TITLE returns the title for function 9.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Cloverleaf Asymmetric Peak/Valley'

    return title


def f10_f0(n, x, y):

    # *****************************************************************************80
    #
    # F10_F0 returns the value of function 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    for i in range(0, n):
        t1 = np.sqrt((80.0 * x[i] - 40.0) ** 2 + (90.0 * y[i] - 45.0) ** 2)
        t2 = np.exp(- 0.04 * t1)
        t3 = np.cos(0.15 * t1)
        f[i] = t2 * t3

    return f


def f10_f1(n, x, y):

    # *****************************************************************************80
    #
    # F10_F1 returns first derivatives of function 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    for i in range(0, n):

        t1 = np.sqrt((80.0 * x[i] - 40.0) ** 2 + (90.0 * y[i] - 45.0) ** 2)
        t2 = np.exp(- 0.04 * t1)
        t3 = np.cos(0.15 * t1)
        t4 = np.sin(0.15 * t1)

        if (t1 != 0.0):
            fx[i] = - t2 * (12.0 * t4 + 3.2 * t3) * (80.0 * x[i] - 40.0) / t1
            fy[i] = - t2 * (13.5 * t4 + 3.6 * t3) * (90.0 * y[i] - 45.0) / t1

    return fx, fy


def f10_f2(n, x, y):

    # *****************************************************************************80
    #
    # F10_F2 returns second derivatives of function 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)

    for i in range(0, n):

        t1 = np.sqrt((80.0 * x[i] - 40.0) ** 2 + (90.0 * y[i] - 45.0) ** 2)

        if (t1 != 0.0):
            t2 = np.exp(- 0.04 * t1)
            t3 = np.cos(0.15 * t1)
            t4 = np.sin(0.15 * t1)
            t5 = t2[i] / t1 ** 3

            fxx[i] = t5 * (t1 * (76.8 * t4 - 133.76 * t3)
                           * (80.0 * x[i] - 40.0) ** 2
                           - (960.0 * t4 + 256.0 * t3) * (90.0 * y[i] - 45.0) ** 2)

            fxy[i] = t5 * (t1 * (86.4 * t4 - 150.48 * t3)
                           + 1080.0 * t4 + 288.0 * t3) * (80.0 * x[i] - 40.0) \
                * (90.0 * y[i] - 45.0)

            fyy[i] = t5 * (t1 * (97.2 * t4 - 169.29 * t3)
                           * (90.0 * y[i] - 45.0) ** 2
                           - (1215.0 * t4 + 324.0 * t3) * (80.0 * x[i] - 40.0) ** 2)

    return fxx, fxy, fyy


def f10_title():

    # *****************************************************************************80
    #
    # F10_TITLE returns the title for function 10.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Cosine Peak'

    return title


def f11_f0(n, x, y):

    # *****************************************************************************80
    #
    # F11_F0 returns the value of function 11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = x[0:n] * (y[0:n] + 1.0)

    return f


def f11_f1(n, x, y):

    # *****************************************************************************80
    #
    # F11_F1 returns first derivatives of function f11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    fx[0:n] = y[0:n] + 1.0
    fy[0:n] = x[0:n]

    return fx, fy


def f11_f2(n, x, y):

    # *****************************************************************************80
    #
    # F11_F2 returns second derivatives of function f11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.ones(n)
    fyy = np.zeros(n)

    return fxx, fxy, fyy


def f11_title():

    # *****************************************************************************80
    #
    # F11_TITLE returns the title for function f11.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Bilinear function'

    return title


def f12_f0(n, x, y):

    # *****************************************************************************80
    #
    # F12_F0 returns the value of function 12.
    #
    #  Discussion:
    #
    #    This is an example from Vicente Romero.
    #
    #      R = np.sqrt ( X^2 + Y^2 )
    #      T = atan ( Y / X )
    #      F(X,Y) = ( 0.8 * R + 0.35 * np.sin ( 2.4 * pi * R / np.sqrt ( 2 )  ) )
    #               * 1.5 * np.sin ( 1.3 * T )
    #
    #    The mean and standard deviation of the function over the interval
    #    are approximately:
    #
    #      mu    = 0.581608
    #      sigma = 0.343208
    #
    #    Since the interpolation interval is the unit square, this means the
    #    integral of the function over the interval can also be estimated as
    #
    #      I = 0.581608
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Vicente Romero, John Burkardt, Max Gunzburger, Janet Peterson,
    #    Initial Evaluation of Centroidal Voronoi Tessellation for
    #    Statistical Sampling and Function Integration,
    #    Fourth International Symposium on Uncertainty Modeling and Analysis,
    #    (ISUMA) 2003.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    for i in range(0, n):

        r = np.sqrt(x[i] ** 2 + y[i] ** 2)
        t = np.arctan2(y[i], x[i])

        f[i] = 1.5 * (0.8 * r
                      + 0.35 * np.sin(2.4 * np.pi * r / np.sqrt(2.0))) \
            * np.sin(1.3 * t)

    return f


def f12_f1(n, x, y):

    # *****************************************************************************80
    #
    # F12_F1 returns first derivatives of function f12.
    #
    #  Discussion:
    #
    #    Currently, the derivative information is of no interest to me.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    return fx, fy


def f12_f2(n, x, y):

    # *****************************************************************************80
    #
    # F12_F2 returns second derivatives of function f12.
    #
    #  Discussion:
    #
    #    Currently, the derivative information is of no interest to me.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)

    return fxx, fxy, fyy


def f12_title():

    # *****************************************************************************80
    #
    # F12_TITLE returns the title for function f12.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Vicente Romero function'

    return title


def f13_f0(n, x, y):

    # *****************************************************************************80
    #
    # F13_F0 returns the value of function 13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real F(N), the function values.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = 1.0 / ((10.0 * x[0:n] - 5.0) ** 2 +
                    (10.0 * y[0:n] - 5.0) ** 2 + 1.0)

    return f


def f13_f1(n, x, y):

    # *****************************************************************************80
    #
    # F13_F1 returns first derivatives of function f13.
    #
    #  Discussion:
    #
    #    Currently, the derivative information is of no interest to me.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FX(N), FY(N), the derivative values.
    #
    import numpy as np

    fx = np.zeros(n)
    fy = np.zeros(n)

    return fx, fy


def f13_f2(n, x, y):

    # *****************************************************************************80
    #
    # F13_F2 returns second derivatives of function f13.
    #
    #  Discussion:
    #
    #    Currently, the derivative information is of no interest to me.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the evalution points.
    #
    #    Output, real FXX(N), FXY(N), FYY(N), second derivatives.
    #
    import numpy as np

    fxx = np.zeros(n)
    fxy = np.zeros(n)
    fyy = np.zeros(n)

    return fxx, fxy, fyy


def f13_title():

    # *****************************************************************************80
    #
    # F13_TITLE returns the title for function f13.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the function title.
    #
    title = 'Rescaled Runge function'

    return title


def file_name_sequence(file_name):

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE generates the next file name in a series.
    #
    #  Discussion:
    #
    #    It is assumed that the digits in the name, whether scattered or
    #    connected, represent a number that is to be increased by 1 on
    #    each call.  If this number is all 9's on input, the output number
    #    is all 0's.  Non-numeric letters of the name are unaffected..
    #
    #    If the name is empty, then the routine stops.
    #
    #    If the name contains no digits, the empty string is returned.
    #
    #  Example:
    #
    #      Input            Output
    #      -----            ------
    #      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
    #      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
    #      'a9to99.txt'     'a0to00.txt'  (wrap around)
    #      'cat.txt'        ' '           (no digits in input name.)
    #      ' '              STOP!         (error.)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILE_NAME, the string to be incremented.
    #
    #    Output, string FILE_NAME_NEXT, the incremented string.
    #
    #
    #  Because of Python's particular treatment of strings, (look up the
    #  word "immutable"!) we IMMEDIATELY copy a string into a list, treating
    #  the list like a normal data item, and then at the end, turning it back
    #  into a string.
    #
    file_name_list = list(file_name)

    flen = len(file_name_list)

    if (flen <= 0):
        print('')
        print('FILE_NAME_SEQUENCE - Fatal error!')
        print('  The input file name is empty.')
        exit('FILE_NAME_SEQUENCE - Fatal error!')

    change = 0

    for i in range(flen - 1, -1, -1):

        c = file_name_list[i]

        if ('0' <= c and c <= '8'):

            change = change + 1

            c = chr(ord(c) + 1)

            file_name_list[i] = c

            break

        elif (c == '9'):

            change = change + 1

            c = '0'

            file_name_list[i] = c

    if (change == 0):
        print('')
        print('FILE_NAME_SEQUENCE - Fatal error!')
        print('  The input file name contains no digits to increment.')
        exit('FILE_NAME_SEQUENCE - Fatal error!')

    file_name_next = "".join(file_name_list)

    return file_name_next


def file_name_sequence_test():

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE_TEST tests FILE_NAME_SEQUENCE.
    #
    #  Discussion:
    #
    #    There are situations such as animations or parallel processing in which
    #    it is necessary to generate a sequence of file names which include
    #    an embedded index that increases.  A simple example might be
    #
    #      'fred0.txt', 'fred1.txt', 'fred2.txt'
    #
    #    A side issue arises when the number of files is large enough that the
    #    number of digits in the index will vary.  Thus, if we are going to have
    #    15 files, do we want to number them as
    #
    #      'fred00.txt' through 'fred14.txt'
    #
    #    which means, for one thing, that they will alphabetize properly, or
    #    will we be satisfied with
    #
    #      'fred0.txt' through 'fred14.txt' ?
    #
    #    Schemes for generating such a sequence in MATLAB can involve the
    #    NUM2STR function, the SPRINTF function, or a more elaborate function
    #    called FILE_NAME_INC which searches a string for embedded numeric
    #    data and increments it.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FILE_NAME_SEQUENCE_TEST:')
    print('  Python version')
    print('  FILE_NAME_SEQUENCE generates a numeric sequence of file names.')

    file_name_sequence_test01('frado_', '_lives.txt', 0, 12)
    file_name_sequence_test02('fredo_', '_lives.txt', 0, 12)
    file_name_sequence_test03('frido_', '_lives.txt', 0, 12)
    file_name_sequence_test04('frodo_000_lives.txt', 12)
#
#  Terminate.
#
    print('')
    print('FILE_NAME_SEQUENCE:')
    print('  Normal end of execution.')
    return


def file_name_sequence_test01(prefix, suffix, first, last):

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE_TEST01 uses concatenation and the str() function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('FILE_NAME_SEQUENCE_TEST01:')
    print('  FILE_NAME = PREFIX + STR(I) + SUFFIX')
    print('  PREFIX = "%s"' % (prefix))
    print('  SUFFIX = "%s"' % (suffix))
    print('  %d <= I <= %d' % (first, last))
    print('  Numbers do NOT include leading zeros.')
    print('')

    for i in range(first, last + 1):
        file_name = prefix + str(i) + suffix
        print('  %4d:  "%s"' % (i, file_name))
#
#  Terminate.
#
    print('')
    print('FILE_NAME_SEQUENCE_TEST01:')
    print('  Normal end of execution.')
    return


def file_name_sequence_test02(prefix, suffix, first, last):

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE_TEST02 uses output formats.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('FILE_NAME_SEQUENCE_TEST02:')
    print('  FILE_NAME(I) = \'%s%d%s\' % ( PREFIX, I, SUFFIX )')
    print('  PREFIX = "%s"' % (prefix))
    print('  SUFFIX = "%s"' % (suffix))
    print('  %d <= I <= %d' % (first, last))
    print('  Numbers do NOT include leading zeros.')
    print('')

    for i in range(first, last + 1):
        file_name = '%s%d%s' % (prefix, i, suffix)
        print('  %4d:  "%s"' % (i, file_name))
#
#  Terminate.
#
    print('')
    print('FILE_NAME_SEQUENCE_TEST02:')
    print('  Normal end of execution.')
    return


def file_name_sequence_test03(prefix, suffix, first, last):

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE_TEST03 uses output formats.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('FILE_NAME_SEQUENCE_TEST03:')
    print('  FILE_NAME(I) = \'%s%02d%s\' % ( PREFIX, I, SUFFIX )')
    print('  PREFIX = "%s"' % (prefix))
    print('  SUFFIX = "%s"' % (suffix))
    print('  %d <= I <= %d' % (first, last))
    print('  Numbers include leading zeros.')
    print('')

    for i in range(first, last + 1):
        file_name = '%s%02d%s' % (prefix, i, suffix)
        print('  %4d:  "%s"' % (i, file_name))
#
#  Terminate.
#
    print('')
    print('FILE_NAME_SEQUENCE_TEST03:')
    print('  Normal end of execution.')
    return


def file_name_sequence_test04(file_name, file_name_num):

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE_TEST04 uses FILE_NAME_SEQUENCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('FILE_NAME_SEQUENCE_TEST04')
    print('  FILE_NAME = FILE_NAME_INC ( FILE_NAME )')
    print('  First FILE_NAME = "%s"' % (file_name))
    print('  Number of file names = %d' % (file_name_num))
    print('  Numbers may include leading zeros.')
    print('')
    i = 0
    print('  %4d:  "%s"' % (i, file_name))

    for i in range(1, file_name_num + 1):
        file_name = file_name_sequence(file_name)
        print('  %4d:  "%s"' % (i, file_name))
#
#  Terminate.
#
    print('')
    print('FILE_NAME_SEQUENCE_TEST04:')
    print('  Normal end of execution.')
    return


def g00_num():

    # *****************************************************************************80
    #
    # G00_NUM returns the number of grids available.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #   Output, integer GRID_NUM, the number of grids.
    #
    grid_num = 5

    return grid_num


def g00_size(gi):

    # *****************************************************************************80
    #
    # G00_SIZE returns the size for any grid.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GI, the index of the grid.
    #
    #    Output, integer GN, the grid size.
    #
    from sys import exit

    if (gi == 1):
        gn = g01_size()
    elif (gi == 2):
        gn = g02_size()
    elif (gi == 3):
        gn = g03_size()
    elif (gi == 4):
        gn = g04_size()
    elif (gi == 5):
        gn = g05_size()
    else:
        print('')
        print('G00_SIZE - Fatal error!')
        print('  Illegal grid index GI = %d' % (gi))
        exit('G00_SIZE - Fatal error!')

    return gn


def g00_title(gi):

    # *****************************************************************************80
    #
    # G00_TITLE returns the title for any grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GI, the index of the grid.
    #
    #    Output, string GT, the grid title.
    #
    from sys import exit

    if (gi == 1):
        gt = g01_title()
    elif (gi == 2):
        gt = g02_title()
    elif (gi == 3):
        gt = g03_title()
    elif (gi == 4):
        gt = g04_title()
    elif (gi == 5):
        gt = g05_title()
    else:
        print('')
        print('G00_TITLE - Fatal error!')
        print('  Illegal grid index GI = %d' % (gi))
        #exit('G00_TITLE - Fatal error!')

    return gt


def g00_xy(gi, gn):

    # *****************************************************************************80
    #
    # G00_XY returns the grid points for any grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GI, the index of the grid.
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    from sys import exit

    if (gi == 1):
        gx, gy = g01_xy(gn)
    elif (gi == 2):
        gx, gy = g02_xy(gn)
    elif (gi == 3):
        gx, gy = g03_xy(gn)
    elif (gi == 4):
        gx, gy = g04_xy(gn)
    elif (gi == 5):
        gx, gy = g05_xy(gn)
    else:
        print('')
        print('G00_XY - Fatal error!')
        print('  Illegal grid index GI = %d' % (gi))
        exit('G00_XY - Fatal error!')

    return gx, gy


def g01_size():

    # *****************************************************************************80
    #
    # G01_SIZE returns the size for grid 1.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 100

    return gn


def g01_title():

    # *****************************************************************************80
    #
    # G01_TITLE returns the title for grid 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Franke\'s 100 node set'

    return gt


def g01_xy(gn):

    # *****************************************************************************80
    #
    # G01_XY returns the grid points for grid 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.0227035, 0.0539888, 0.0217008, 0.0175129, 0.0019029,
        -0.0509685, 0.0395408, -0.0487061, 0.0315828, -0.0418785,
        0.1324189, 0.1090271, 0.1254439, 0.0934540, 0.0767578,
        0.1451874, 0.0626494, 0.1452734, 0.0958668, 0.0695559,
        0.2645602, 0.2391645, 0.2088990, 0.2767329, 0.1714726,
        0.2266781, 0.1909212, 0.1867647, 0.2304634, 0.2426219,
        0.3663168, 0.3857662, 0.3832392, 0.3179087, 0.3466321,
        0.3776591, 0.3873159, 0.3812917, 0.3795364, 0.2803515,
        0.4149771, 0.4277679, 0.4200010, 0.4663631, 0.4855658,
        0.4092026, 0.4792578, 0.4812279, 0.3977761, 0.4027321,
        0.5848691, 0.5730076, 0.6063893, 0.5013894, 0.5741311,
        0.6106955, 0.5990105, 0.5380621, 0.6096967, 0.5026188,
        0.6616928, 0.6427836, 0.6396475, 0.6703963, 0.7001181,
        0.6333590, 0.6908947, 0.6895638, 0.6718889, 0.6837675,
        0.7736939, 0.7635332, 0.7410424, 0.8258981, 0.7306034,
        0.8086609, 0.8214531, 0.7290640, 0.8076643, 0.8170951,
        0.8424572, 0.8684053, 0.8366923, 0.9418461, 0.8478122,
        0.8599583, 0.9175700, 0.8596328, 0.9279871, 0.8512805,
        1.0449820, 0.9670631, 0.9857884, 0.9676313, 1.0129299,
        0.9657040, 1.0019855, 1.0359297, 1.0414677, 0.9471506])

    gy = np.array([
        -0.0310206, 0.1586742, 0.2576924, 0.3414014, 0.4943596,
        0.5782854, 0.6993418, 0.7470194, 0.9107649, 0.9962890,
        0.0501330, 0.0918555, 0.2592973, 0.3381592, 0.4171125,
        0.5615563, 0.6552235, 0.7524066, 0.9146523, 0.9632421,
        0.0292939, 0.0602303, 0.2668783, 0.3696044, 0.4801738,
        0.5940595, 0.6878797, 0.8185576, 0.9046507, 0.9805412,
        0.0396955, 0.0684484, 0.2389548, 0.3124129, 0.4902989,
        0.5199303, 0.6445227, 0.8203789, 0.8938079, 0.9711719,
        -0.0284618, 0.1560965, 0.2262471, 0.3175094, 0.3891417,
        0.5084949, 0.6324247, 0.7511007, 0.8489712, 0.9978728,
        -0.0271948, 0.1272430, 0.2709269, 0.3477728, 0.4259422,
        0.6084711, 0.6733781, 0.7235242, 0.9242411, 1.0308762,
        0.0255959, 0.0707835, 0.2008336, 0.3259843, 0.4890704,
        0.5096324, 0.6697880, 0.7759569, 0.9366096, 1.0064516,
        0.0285374, 0.1021403, 0.1936581, 0.3235775, 0.4714228,
        0.6091595, 0.6685053, 0.8022808, 0.8476790, 1.0512371,
        0.0380499, 0.0902048, 0.2083092, 0.3318491, 0.4335632,
        0.5910139, 0.6307383, 0.8144841, 0.9042310, 0.9696030,
        -0.0120900, 0.1334114, 0.2695844, 0.3795281, 0.4396054,
        0.5044425, 0.6941519, 0.7459923, 0.8682081, 0.9801409])

    return gx, gy


def g02_size():

    # *****************************************************************************80
    #
    # G02_SIZE returns the size for grid 2.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 33

    return gn


def g02_title():

    # *****************************************************************************80
    #
    # G02_TITLE returns the title for grid 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Franke\'s 33 node set'

    return gt


def g02_xy(gn):

    # *****************************************************************************80
    #
    # G02_XY returns the grid points for grid 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.05, 0.00, 0.00, 0.00, 0.10,
        0.10, 0.15, 0.20, 0.25, 0.30,
        0.35, 0.50, 0.50, 0.55, 0.60,
        0.60, 0.60, 0.65, 0.70, 0.70,
        0.70, 0.75, 0.75, 0.75, 0.80,
        0.80, 0.85, 0.90, 0.90, 0.95,
        1.00, 1.00, 1.00])

    gy = np.array([
        0.45, 0.50, 1.00, 0.00, 0.15,
        0.75, 0.30, 0.10, 0.20, 0.35,
        0.85, 0.00, 1.00, 0.95, 0.25,
        0.65, 0.85, 0.70, 0.20, 0.65,
        0.90, 0.10, 0.35, 0.85, 0.40,
        0.65, 0.25, 0.35, 0.80, 0.90,
        0.00, 0.50, 1.00])

    return gx, gy


def g03_size():

    # *****************************************************************************80
    #
    # G03_SIZE returns the size for grid 3.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 25

    return gn


def g03_title():

    # *****************************************************************************80
    #
    # G03_TITLE returns the title for grid 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Lawson\'s 25 node set'

    return gt


def g03_xy(gn):

    # *****************************************************************************80
    #
    # G03_XY returns the grid points for grid 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.13750, 0.91250, 0.71250, 0.22500, -0.05000,
        0.47500, 0.05000, 0.45000, 1.08750, 0.53750,
        -0.03750, 0.18750, 0.71250, 0.85000, 0.70000,
        0.27500, 0.45000, 0.81250, 0.45000, 1.00000,
        0.50000, 0.18750, 0.58750, 1.05000, 0.10000])

    gy = np.array([
        0.97500, 0.98750, 0.76250, 0.83750, 0.41250,
        0.63750, -0.05000, 1.03750, 0.55000, 0.80000,
        0.75000, 0.57500, 0.55000, 0.43750, 0.31250,
        0.42500, 0.28750, 0.18750, -0.03750, 0.26250,
        0.46250, 0.26250, 0.12500, -0.06125, 0.11250])

    return gx, gy


def g04_size():

    # *****************************************************************************80
    #
    # G04_SIZE returns the size for grid 4.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 100

    return gn


def g04_title():

    # *****************************************************************************80
    #
    # G04_TITLE returns the title for grid 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Random 100 node set'

    return gt


def g04_xy(gn):

    # *****************************************************************************80
    #
    # G04_XY returns the grid points for grid 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.0096326, 0.0216348, 0.0298360, 0.0417447, 0.0470462,
        0.0562965, 0.0646857, 0.0740377, 0.0873907, 0.0934832,
        0.1032216, 0.1110176, 0.1181193, 0.1251704, 0.1327330,
        0.1439536, 0.1564861, 0.1651043, 0.1786039, 0.1886405,
        0.2016706, 0.2099886, 0.2147003, 0.2204141, 0.2343715,
        0.2409660, 0.2527740, 0.2570839, 0.2733365, 0.2853833,
        0.2901755, 0.2964854, 0.3019725, 0.3125695, 0.3307163,
        0.3378504, 0.3439061, 0.3529922, 0.3635507, 0.3766172,
        0.3822429, 0.3869838, 0.3973137, 0.4170708, 0.4255588,
        0.4299218, 0.4372839, 0.4705033, 0.4736655, 0.4879299,
        0.4940260, 0.5055324, 0.5162593, 0.5219219, 0.5348529,
        0.5483213, 0.5569571, 0.5638611, 0.5784908, 0.5863950,
        0.5929148, 0.5987839, 0.6117561, 0.6252296, 0.6331381,
        0.6399048, 0.6488972, 0.6558537, 0.6677405, 0.6814074,
        0.6887812, 0.6940896, 0.7061687, 0.7160957, 0.7317445,
        0.7370798, 0.7462030, 0.7566957, 0.7699998, 0.7879347,
        0.7944014, 0.8164468, 0.8192794, 0.8368405, 0.8500993,
        0.8588255, 0.8646496, 0.8792329, 0.8837536, 0.8900077,
        0.8969894, 0.9044917, 0.9083947, 0.9203972, 0.9347906,
        0.9434519, 0.9490328, 0.9569571, 0.9772067, 0.9983493])

    gy = np.array([
        0.3083158, 0.2450434, 0.8613847, 0.0977864, 0.3648355,
        0.7156339, 0.5311312, 0.9755672, 0.1781117, 0.5452797,
        0.1603881, 0.7837139, 0.9982015, 0.6910589, 0.1049580,
        0.8184662, 0.7086405, 0.4456593, 0.1178342, 0.3189021,
        0.9668446, 0.7571834, 0.2016598, 0.3232444, 0.4368583,
        0.8907869, 0.0647260, 0.5692618, 0.2947027, 0.4332426,
        0.3347464, 0.7436284, 0.1066265, 0.8845357, 0.5158730,
        0.9425637, 0.4799701, 0.1783069, 0.1146760, 0.8225797,
        0.2270688, 0.4073598, 0.8875080, 0.7631616, 0.9972804,
        0.4959884, 0.3410421, 0.2498120, 0.6409007, 0.1058690,
        0.5411969, 0.0089792, 0.8784268, 0.5515874, 0.4038952,
        0.1654023, 0.2965158, 0.3660356, 0.0366554, 0.9502420,
        0.2638101, 0.9277386, 0.5377694, 0.7374676, 0.4674627,
        0.9186109, 0.0416884, 0.1291029, 0.6763676, 0.8444238,
        0.3273328, 0.1893879, 0.0645923, 0.0180147, 0.8904992,
        0.4160648, 0.4688995, 0.2174508, 0.5734231, 0.8853319,
        0.8018436, 0.6388941, 0.8931002, 0.1000558, 0.2789506,
        0.9082948, 0.3259159, 0.8318747, 0.0508513, 0.9708450,
        0.5120548, 0.2859716, 0.9581641, 0.6183429, 0.3779934,
        0.4010423, 0.9478657, 0.7425486, 0.8883287, 0.5496750])

    return gx, gy


def g05_size():

    # *****************************************************************************80
    #
    # G05_SIZE returns the size for grid 5.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 81

    return gn


def g05_title():

    # *****************************************************************************80
    #
    # G05_TITLE returns the title for grid 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Gridded 81 node set'

    return gt


def g05_xy(gn):

    # *****************************************************************************80
    #
    # G05_XY returns the grid points for grid 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000,
        0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
        0.250, 0.250, 0.250, 0.250, 0.250, 0.250, 0.250, 0.250, 0.250,
        0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375,
        0.500, 0.500, 0.500, 0.500, 0.500, 0.500, 0.500, 0.500, 0.500,
        0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625,
        0.750, 0.750, 0.750, 0.750, 0.750, 0.750, 0.750, 0.750, 0.750,
        0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875,
        1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000])

    gy = np.array([
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000])

    return gx, gy


def test_interp_2d_test01():

    # *****************************************************************************80
    #
    # TEST_INTERP_2D_TEST01 simply prints the title of each grid and function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('TEST_INTERP_2D_TEST01')
    print('  For each grid and function, print the title.')

    print('')
    print('  GRIDS:')
    print('  Index  Title')
    print('')

    for gi in range(1, 6):
        gt = g00_title(gi)
        print('  %2d  "%s"' % (gi, gt))

    print('')
    print('  FUNCTIONS:')
    print('  Index  Title')
    print('')

    for fi in range(1, 14):
        ft = f00_title(fi)
        print('  %2d  "%s"' % (fi, ft))


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


if (__name__ == '__main__'):
    timestamp()

    # *****************************************************************************80
    #
    # TEST_INTERP_2D_TEST tests the TEST_INTERP_2D library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('TEST_INTERP_2D_TEST')
    print('  MATLAB version')
    print('  Test the TEST_INTERP_2D library.')

    test_interp_2d_test01()

    print('')
    print('TEST_INTERP_2D_TEST')
    print('  Normal end of execution.')

    timestamp()
