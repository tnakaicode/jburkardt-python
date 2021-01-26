#! /usr/bin/env python3
#


def c8mat_exp_a(test, n):

    # *****************************************************************************80
    #
    # C8MAT_EXP_A returns the matrix for a given test.
    #
    #  Discussion:
    #
    #    1) Diagonal, real
    #    2) Diagonal, pure imaginary.
    #    3) Diagonal, complex.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Output, real A(N,N), the matrix.
    #
    import numpy as np
    from sys import exit

    if (test == 1):

        a = np.array([
            [1.0, 0.0],
            [0.0, 2.0]],
            dtype=np.complex128)

    elif (test == 2):

        a = np.array([
            [3.0j, 0.0],
            [0.0, - 4.0j]],
            dtype=np.complex128)

    elif (test == 3):

        a = np.array([
            [5.0 + 6.0j, 0.0],
            [0.0, 7.0 - 8.0j]],
            dtype=np.complex128)

    else:

        print('')
        print('C8MAT_EXP_A - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('C8MAT_EXP_A - Fatal error!')

    return a


def c8mat_exp_expa(test, n):

    # *****************************************************************************80
    #
    # C8MAT_EXP_EXPA returns the "exact" exponential matrix for a given test.
    #
    #  Discussion:
    #
    #    1) Diagonal, real.
    #    2) Diagonal, pure imaginary.
    #    3) Diagonal, complex.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Output, complex EXPA(N,N), the exponential of the test matrix.
    #
    import numpy as np
    from sys import exit

    expa = []

    if (test == 1):

        expa = np.array([
            [2.718281828459046, 0.0],
            [0.0, 7.389056098930650]],
            dtype=np.complex128)

    elif (test == 2):

        expa = np.array([
            [-0.989992496600446 + 0.141120008059j, 0.0],
            [0.0, -0.653643620863612 + 0.756802495307928j]],
            dtype=np.complex128)

    elif (test == 3):

        expa = np.array([
            [142.501905518208 - 41.468936789923j, 0.0],
            [0.0, -159.560161626987 - 1084.963058811836j]],
            dtype=np.complex128)

    else:

        print('')
        print('C8MAT_EXP_EXPA - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('C8MAT_EXP_EXPA - Fatal error!')

    return expa


def c8mat_exp_n(test):

    # *****************************************************************************80
    #
    # C8MAT_EXP_N returns the matrix order for a given test.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    #    Output, integer N, the order of the matrix.
    #
    from sys import exit

    if (test == 1):
        n = 2
    elif (test == 2):
        n = 2
    elif (test == 3):
        n = 2
    else:
        print('')
        print('C8MAT_EXP_N - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('C8MAT_EXP_N - Fatal error!')

    return n


def c8mat_exp_story(test):

    # *****************************************************************************80
    #
    # C8MAT_EXP_STORY prints explanatory text for each problem.
    #
    #  Discussion:
    #
    #    1) Diagonal, real
    #    2) Diagonal, pure imaginary.
    #    3) Diagonal, complex.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    from sys import exit

    if (test == 1):
        print('')
        print('  This matrix is diagonal.')
        print('  The diagonal entries are real.')
    elif (test == 2):
        print('')
        print('  This matrix is diagonal.')
        print('  The diagonal entries are pure imaginary.')
    elif (test == 3):
        print('')
        print('  This matrix is diagonal.')
        print('  The diagonal entries are complex.')
    else:
        print('')
        print('C8MAT_EXP_STORY - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('C8MAT_EXP_STORY - Fatal error!')

    return


def c8mat_exp_test_num():

    # *****************************************************************************80
    #
    # C8MAT_EXP_TEST_NUM returns the number of matrix exponential tests.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer TEST_NUM, the number of tests.
    #
    test_num = 3

    return test_num


def c8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # C8MAT_PRINT prints a C8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, complex A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    c8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def c8mat_print_test():

    # *****************************************************************************80
    #
    # C8MAT_PRINT_TEST tests C8MAT_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('C8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8MAT_PRINT prints an C8MAT.')

    m = 4
    n = 3
    v = np.array([
        [complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0)],
        [complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0)],
        [complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0)],
        [complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0)]],
        dtype=np.complex128)

    c8mat_print(m, n, v, '  Here is a C8MAT:')
#
#  Terminate.
#
    print('')
    print('C8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def c8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # C8MAT_PRINT_SOME prints out a portion of an C8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, complex A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 4

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for j2lo in range(max(jlo, 0), min(jhi, n - 1), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n - 1)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: '),

        for j in range(j2lo, j2hi + 1):
            print('       %7d              ' % (j)),

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m - 1)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i)),

            for j in range(j2lo, j2hi + 1):
                print('%12g  %12gi ' % (a.real[i, j], a.imag[i, j])),

            print('')

    return


def c8mat_print_some_test():

    # *****************************************************************************80
    #
    # C8MAT_PRINT_SOME_TEST tests C8MAT_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('C8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8MAT_PRINT_SOME prints some of an C8MAT.')

    m = 4
    n = 6
    v = np.array([
        [complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0),
         complex(10.0, 4.0), complex(10.0, 5.0), complex(10.0, 6.0)],
        [complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0),
            complex(20.0, 4.0), complex(20.0, 5.0), complex(20.0, 6.0)],
        [complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0),
            complex(30.0, 4.0), complex(30.0, 5.0), complex(30.0, 6.0)],
        [complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0),
            complex(40.0, 4.0), complex(40.0, 5.0), complex(40.0, 6.0)]],
        dtype=np.complex128)

    c8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is a C8MAT:')
#
#  Terminate.
#
    print('')
    print('C8MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution. ')
    return


def r8mat_exp_a(test, n):

    # *****************************************************************************80
    #
    # R8MAT_EXP_A returns the matrix for a given test.
    #
    #  Discussion:
    #
    #     1) Diagonal example
    #     2) Symmetric example
    #     3) Laub
    #     4) Moler and Van Loan
    #     5) Moler and Van Loan
    #     6) Moler and Van Loan
    #     7) Moler and Van Loan
    #     8) Wikipedia example
    #     9) NAG F01ECF
    #    10) Ward #1
    #    11) Ward #2
    #    12) Ward #3
    #    13) Ward #4
    #    14) Moler example
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Alan Laub,
    #    Review of "Linear System Theory" by Joao Hespanha,
    #    SIAM Review,
    #    Volume 52, Number 4, December 2010, page 779-781.
    #
    #    Cleve Moler, Charles VanLoan,
    #    Nineteen Dubious Ways to Compute the Exponential of a Matrix,
    #    Twenty-Five Years Later,
    #    SIAM Review,
    #    Volume 45, Number 1, March 2003, pages 3-49.
    #
    #    Cleve Moler,
    #    Cleve's Corner: A Balancing Act for the Matrix Exponential,
    #    July 23rd, 2012.
    #
    #    Robert Ward,
    #    Numerical computation of the matrix exponential with accuracy estimate,
    #    SIAM Journal on Numerical Analysis,
    #    Volume 14, Number 4, September 1977, pages 600-610.
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Output, real A(N,N), the matrix.
    #
    import numpy as np
    from sys import exit

    if (test == 1):

        a = np.array([
            [1.0, 0.0],
            [0.0, 2.0]])

    elif (test == 2):

        a = np.array([
            [1.0, 3.0],
            [3.0, 2.0]])

    elif (test == 3):

        a = np.array([
            [0.0, -39.0],
            [1.0, -40.0]])

    elif (test == 4):

        a = np.array([
            [-49.0, -64.0],
            [24.0, 31.0]])

    elif (test == 5):

        a = np.array([
            [0.0, 0.0, 0.0, 0.0],
            [6.0, 0.0, 0.0, 0.0],
            [0.0, 6.0, 0.0, 0.0],
            [0.0, 0.0, 6.0, 0.0]])

    elif (test == 6):

        a = np.array([
            [1.0, 0.0],
            [1.0, 1.0]])

    elif (test == 7):

        eps = 2.220446049250313E-016
        a = np.array([
            [1.0 + eps, 0.0],
            [1.0, 1.0 - eps]])

    elif (test == 8):

        a = np.array([
            [21.0, -5.0, 4.0],
            [17.0, -1.0, 4.0],
            [6.0, -6.0, 16.0]])

    elif (test == 9):

        a = np.array([
            [1.0, 3.0, 3.0, 3.0],
            [2.0, 1.0, 2.0, 3.0],
            [2.0, 1.0, 1.0, 3.0],
            [2.0, 2.0, 2.0, 1.0]])

    elif (test == 10):

        a = np.array([
            [4.0, 1.0, 1.0],
            [2.0, 4.0, 1.0],
            [0.0, 1.0, 4.0]])

    elif (test == 11):

        a = np.array([
            [29.87942128909879, 0.7815750847907159, -2.289519314033932],
            [0.7815750847907159, 25.72656945571064, 8.680737820540137],
            [-2.289519314033932, 8.680737820540137, 34.39400925519054]])

    elif (test == 12):

        a = np.array([
            [-131.0, -390.0, -387.0],
            [19.0, 56.0, 57.0],
            [18.0, 54.0, 52.0]])

    elif (test == 13):

        a = np.zeros([n, n])

        for i in range(0, n - 1):
            a[i, i + 1] = 1.0
        a[n - 1, 0] = 1.0E-10

    elif (test == 14):

        a = np.zeros([3, 3])

        a[0, 0] = 0.0
        a[1, 0] = 1.0E-08
        a[2, 0] = 0.0
        a[0, 1] = - 2.0E+10 - 2.0E+08 / 3.0
        a[1, 1] = - 3.0
        a[2, 1] = 2.0E+10
        a[0, 2] = 200.0 / 3.0
        a[1, 2] = 0.0
        a[2, 2] = - 200.0 / 3.0

    else:

        print('')
        print('R8MAT_EXP_A - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('R8MAT_EXP_A - Fatal error!')

    return a


def r8mat_exp_expa(test, n):

    # *****************************************************************************80
    #
    # R8MAT_EXP_EXPA returns the "exact" exponential matrix for a given test.
    #
    #  Discussion:
    #
    #    In some cases, the "exact" value is given to six significant digits.
    #
    #     1) Diagonal example
    #     2) Symmetric example
    #     3) Laub
    #     4) Moler and Van Loan
    #     5) Moler and Van Loan
    #     6) Moler and Van Loan
    #     7) Moler and Van Loan
    #     8) Wikipedia example
    #     9) NAG F01ECF
    #    10) Ward #1
    #    11) Ward #2
    #    12) Ward #3
    #    13) Ward #4
    #    14) Moler example
    #
    #    Thanks to Alex Griffing for correcting the value of matrix 3,
    #    17 October 2012.
    #
    #    Thanks again to Alex Griffing for providing improved values for
    #    matrices 4, 7 and 13, 03 September 2013.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Alan Laub,
    #    Review of "Linear System Theory" by Joao Hespanha,
    #    SIAM Review,
    #    Volume 52, Number 4, December 2010, page 779-781.
    #
    #    Cleve Moler, Charles VanLoan,
    #    Nineteen Dubious Ways to Compute the Exponential of a Matrix,
    #    Twenty-Five Years Later,
    #    SIAM Review,
    #    Volume 45, Number 1, March 2003, pages 3-49.
    #
    #    Cleve Moler,
    #    Cleve's Corner: A Balancing Act for the Matrix Exponential,
    #    July 23rd, 2012.
    #
    #    Robert Ward,
    #    Numerical computation of the matrix exponential with accuracy estimate,
    #    SIAM Journal on Numerical Analysis,
    #    Volume 14, Number 4, September 1977, pages 600-610.
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Output, real EXPA(N,N), the exponential of the test matrix.
    #
    import numpy as np
    from sys import exit

    if (test == 1):

        expa = np.array([
            [2.718281828459046, 0.0],
            [0.0, 7.389056098930650]])

    elif (test == 2):

        expa = np.array([
            [39.322809708033859, 46.166301438885753],
            [46.166301438885768, 54.711576854329110]])

    elif (test == 3):

        expa = np.array([
            [0.37756048, -0.37756048],
            [0.00968104, -0.00968104]])

    elif (test == 4):

        expa = np.array([
            [-0.7357587581447531, -1.4715175990882605],
            [0.5518190996580977, 1.1036382407155727]])

    elif (test == 5):

        expa = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [6.0, 1.0, 0.0, 0.0],
            [18.0, 6.0, 1.0, 0.0],
            [36.0, 18.0, 6.0, 1.0]])

    elif (test == 6):

        expa = np.array([
            [2.718281828459046, 0.0],
            [2.718281828459046, 2.718281828459046]])

    elif (test == 7):

        expa = np.array([
            [2.718281828459045235360287, 0.0],
            [2.718281828459045235360287, 2.718281828459045235360287]])

    elif (test == 8):

        exp16 = np.exp(16.0)
        exp4 = np.exp(4.0)

        expa = 0.25 * np.array([
            [13.0 * exp16 - exp4, -9.0 * exp16 + exp4, 16.0 * exp16],
            [13.0 * exp16 - 5.0 * exp4, -9.0 * exp16 + 5.0 * exp4, 16.0 * exp16],
            [2.0 * exp16 - 2.0 * exp4, -2.0 * exp16 + 2.0 * exp4, 4.0 * exp16]])

    elif (test == 9):

        expa = np.array([
            [740.7038, 731.2510, 823.7630, 998.4355],
            [610.8500, 603.5524, 679.4257, 823.7630],
            [542.2743, 535.0884, 603.5524, 731.2510],
            [549.1753, 542.2743, 610.8500, 740.7038]])

    elif (test == 10):

        expa = np.array([
            [147.8666224463699, 127.7810855231823, 127.7810855231824],
            [183.7651386463682, 183.7651386463682, 163.6796017231806],
            [71.79703239999647, 91.88256932318415, 111.9681062463718]])

    elif (test == 11):

        expa = np.array([
            [5.496313853692378E+15, -1.823188097200898E+16, -3.047577080858001E+16],
            [-1.823188097200899E+16, 6.060522870222108E+16, 1.012918429302482E+17],
            [-3.047577080858001E+16, 1.012918429302482E+17, 1.692944112408493E+17]])

    elif (test == 12):

        expa = np.array([
            [-1.509644158793135, -5.632570799891469, -4.934938326088363],
            [0.3678794391096522, 1.471517758499875, 1.103638317328798],
            [0.1353352811751005, 0.4060058435250609, 0.5413411267617766]])

    elif (test == 13):

        expa = np.zeros([n, n])

        k = 0
        for i in range(0, n):
            expa[i, i] = 1.0

        value = 1.0
        for k in range(1, n):
            value = value / float(k)
            for i in range(0, n - k):
                expa[i, i + k] = value

        value = 1.0 / 10.0 ** n
        for k in range(1, n):
            value = value / float(k)
            for j in range(0, k):
                expa[n + j - k, j] = value

    elif (test == 14):

        expa = np.array([
            [4.468494682831735E-01, -5.743067779479621E+06, 4.477229778494929E-01],
            [1.540441573839520E-09, -1.528300386868247E-02, 1.542704845195912E-09],
            [4.628114535587735E-01, -4.526542712784168E+06, 4.634806488376499E-01]])

    else:

        print('')
        print('R8MAT_EXP_EXPA - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('R8MAT_EXP_EXPA - Fatal error!')

    return expa


def r8mat_exp_n(test):

    # *****************************************************************************80
    #
    # R8MAT_EXP_N returns the matrix order for a given test.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    #    Output, integer N, the order of the matrix.
    #
    if (test == 1):
        n = 2
    elif (test == 2):
        n = 2
    elif (test == 3):
        n = 2
    elif (test == 4):
        n = 2
    elif (test == 5):
        n = 4
    elif (test == 6):
        n = 2
    elif (test == 7):
        n = 2
    elif (test == 8):
        n = 3
    elif (test == 9):
        n = 4
    elif (test == 10):
        n = 3
    elif (test == 11):
        n = 3
    elif (test == 12):
        n = 3
    elif (test == 13):
        n = 10
    elif (test == 14):
        n = 3
    else:
        print('')
        print('R8MAT_EXP_N - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('R8MAT_EXP_N - Fatal error!')

    return n


def r8mat_exp_story(test):

    # *****************************************************************************80
    #
    # R8MAT_EXP_STORY prints explanatory text for each problem.
    #
    #  Discussion:
    #
    #     1) Diagonal example
    #     2) Symmetric example
    #     3) Laub
    #     4) Moler and Van Loan
    #     5) Moler and Van Loan
    #     6) Moler and Van Loan
    #     7) Moler and Van Loan
    #     8) Wikipedia example
    #     9) NAG F01ECF
    #    10) Ward #1
    #    11) Ward #2
    #    12) Ward #3
    #    13) Ward #4
    #    14) Moler example
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Alan Laub,
    #    Review of "Linear System Theory" by Joao Hespanha,
    #    SIAM Review,
    #    Volume 52, Number 4, December 2010, page 779-781.
    #
    #    Cleve Moler, Charles VanLoan,
    #    Nineteen Dubious Ways to Compute the Exponential of a Matrix,
    #    Twenty-Five Years Later,
    #    SIAM Review,
    #    Volume 45, Number 1, March 2003, pages 3-49.
    #
    #    Cleve Moler,
    #    Cleve's Corner: A Balancing Act for the Matrix Exponential,
    #    July 23rd, 2012.
    #
    #    Robert Ward,
    #    Numerical computation of the matrix exponential with accuracy estimate,
    #    SIAM Journal on Numerical Analysis,
    #    Volume 14, Number 4, September 1977, pages 600-610.
    #
    #  Parameters:
    #
    #    Input, integer TEST, the index of the test case.
    #
    from sys import exit

    if (test == 1):
        print('')
        print('  This matrix is diagonal.')
        print('  The calculation of the matrix exponential is simple.')
    elif (test == 2):
        print('')
        print('  This matrix is symmetric.')
        print('  The calculation of the matrix exponential is straightforward.')
    elif (test == 3):
        print('')
        print('  This example is due to Laub.')
        print('  This matrix is ill-suited for the Taylor series approach.')
        print('  As powers of A are computed, the entries blow up too quickly.')
    elif (test == 4):
        print('')
        print('  This example is due to Moler and Van Loan.')
        print('  The example will cause problems for the series summation approach,')
        print('  as well as for diagonal Pade approximations.')
    elif (test == 5):
        print('')
        print('  This example is due to Moler and Van Loan.')
        print('  This matrix is strictly upper triangular')
        print('  All powers of A are zero beyond some (low) limit.')
        print('  This example will cause problems for Pade approximations.')
    elif (test == 6):
        print('')
        print('  This example is due to Moler and Van Loan.')
        print('  This matrix does not have a complete set of eigenvectors.')
        print('  That means the eigenvector approach will fail.')
    elif (test == 7):
        print('')
        print('  This example is due to Moler and Van Loan.')
        print('  This matrix is very close to example 5.')
        print('  Mathematically, it has a complete set of eigenvectors.')
        print('  Numerically, however, the calculation will be suspect.')
    elif (test == 8):
        print('')
        print('  This matrix was an example in Wikipedia.')
    elif (test == 9):
        print('')
        print('  This example is due to the NAG Library.')
        print('  It is an example for function F01ECF.')
    elif (test == 10):
        print('')
        print('  This is Ward\'s example #1.')
        print('  It is defective and nonderogatory.')
        print('  The eigenvalues are 3, 3 and 6.')
    elif (test == 11):
        print('')
        print('  This is Ward\'s example #2.')
        print('  It is a symmetric matrix.')
        print('  The eigenvalues are 20, 30, 40.')
    elif (test == 12):
        print('')
        print('  This is Ward\'s example #3.')
        print('  Ward\'s algorithm has difficulty estimating the accuracy')
        print('  of its results.  The eigenvalues are -1, -2, -20.')
    elif (test == 13):
        print('')
        print('  This is Ward\'s example #4.')
        print('  This is a version of the Forsythe matrix.')
        print('  The eigenvector problem is badly conditioned.')
        print('  Ward\'s algorithm has difficulty estimating the accuracy')
        print('  of its results for this problem.')
    elif (test == 14):
        print('')
        print('  This is Moler\'s example.')
        print('  This badly scaled matrix caused problems for MATLAB''s expm().')
    else:
        print('')
        print('R8MAT_EXP_STORY - Fatal error!')
        print('  Illegal value of TEST = %d' % (test))
        exit('R8MAT_EXP_STORY - Fatal error!')

    return


def r8mat_exp_test_num():

    # *****************************************************************************80
    #
    # R8MAT_EXP_TEST_NUM returns the number of matrix exponential tests.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer TEST_NUM, the number of tests.
    #
    test_num = 14

    return test_num


def r8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT prints an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    r8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_print_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_TEST tests R8MAT_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT prints an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print(m, n, v, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME prints out a portion of an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, real A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: '),

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j)),

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i)),

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j])),

            print('')

    return


def r8mat_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT_SOME prints some of an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def test_matrix_exponential_test01():

    # *****************************************************************************80
    #
    # TEST_MATRIX_EXPONENTIAL_TEST01 retrieves the test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('TEST_MATRIX_EXPONENTIAL_TEST01:')
    print('  Retrieve the data for each matrix exponential test.')

    test_num = r8mat_exp_test_num()

    for test in range(1, test_num + 1):

        print('')
        print('  Test #%d' % (test))

        n = r8mat_exp_n(test)

        r8mat_exp_story(test)

        print('')
        print('  Matrix order N = %d' % (n))

        a = r8mat_exp_a(test, n)

        r8mat_print(n, n, a, '  Matrix A:')

        a_exp = r8mat_exp_expa(test, n)
        r8mat_print(n, n, a_exp, '  Exact Exponential exp(A):')

    return


def test_matrix_exponential_test02():

    # *****************************************************************************80
    #
    # TEST_MATRIX_EXPONENTIAL_TEST02 retrieves the complex test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('TEST_MATRIX_EXPONENTIAL_TEST02:')
    print('  Retrieve the data for each matrix exponential test.')

    test_num = c8mat_exp_test_num()

    for test in range(1, test_num + 1):

        print('')
        print('  Test #%d' % (test))

        n = c8mat_exp_n(test)

        c8mat_exp_story(test)

        print('')
        print('  Matrix order N = %d\n' % (n))

        a = c8mat_exp_a(test, n)

        c8mat_print(n, n, a, '  Matrix A:')

        a_exp = c8mat_exp_expa(test, n)
        c8mat_print(n, n, a_exp, '  Exact Exponential exp(A):')

    return


def test_matrix_exponential_test():

    # *****************************************************************************80
    #
    # TEST_MATRIX_EXPONENTIAL_TEST tests the TEST_MATRIX_EXPONENTIAL library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TEST_MATRIX_EXPONENTIAL_TEST:\n')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the TEST_MATRIX_EXPONENTIAL library.')

    test_matrix_exponential_test01()
    test_matrix_exponential_test02()
#
#  Terminate.
#
    print('')
    print('TEST_MATRIX_EXPONENTIAL_TEST:')
    print('  Normal end of execution.')
    return


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


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    test_matrix_exponential_test()
    timestamp()
