#! /usr/bin/env python3
#
def c8_le_l2(c1, c2):

    # *****************************************************************************80
    #
    # C8_LE_L2 := C1 <= C1 for C8's, and the L2 norm.
    #
    #  Discussion:
    #
    #    The L2 norm can be defined here as:
    #
    #      C8_NORM_L2(C) = sqrt ( ( real (C) ) ^ 2 + abs ( imag (C) ) ^ 2 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, complex C1, C2, the values to be compared.
    #
    #    Output, boolean VALUE, is TRUE if C1 <= C2.
    #
    if (c1.real ** 2 + c1.imag ** 2 <= c2.real ** 2 + c2.imag ** 2):
        value = True
    else:
        value = False

    return value


def c8_le_l2_test():

    # *****************************************************************************80
    #
    # C8_LE_L2_TEST tests C8_LE_L2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8_LE_L2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8_LE_L2 evalues (C1 <= C2) using the L2 norm.')
    print('')
    print('       C1=C8_UNIFORM_01          C2=C8_UNIFORM_01          L3=C8_LE_L2(C1,C2)')
    print('     ---------------------     ---------------------     ---------------------')
    print('')

    seed = 123456789

    for i in range(0, 10):
        c1, seed = c8_uniform_01(seed)
        c2, seed = c8_uniform_01(seed)
        l3 = c8_le_l2(c1, c2)
        print('  (%12f,%12f)  (%12f,%12f)  %s'
              % (c1.real, c1.imag, c2.real, c2.imag, l3))
#
#  Terminate.
#
    print('')
    print('C8_LE_L2_TEST:')
    print('  Normal end of execution.')
    return


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
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('       %7d              ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m - 1)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%12g  %12gi ' % (a.real[i, j], a.imag[i, j]), end='')

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


def c8_norm_l2(c):

    # *****************************************************************************80
    #
    # C8_NORM_L2 evaluates the L2 norm of a C8.
    #
    #  Discussion:
    #
    #    Numbers of equal norm lie along diamonds centered at (0,0).
    #
    #    The L2 norm can be defined here as:
    #
    #      C8_NORM_L2(X) = aqrt ( ( real (X) ) ^ 2 + abs ( imag (X) ) ^ 2 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, complex C, the value whose norm is desired.
    #
    #    Output, real VALUE, the L2 norm of C.
    #
    import numpy as np

    value = np.sqrt((c.real) ** 2 + (c.imag) ** 2)

    return value


def c8_norm_l2_test():

    # *****************************************************************************80
    #
    # C8_NORM_L2_TEST tests C8_NORM_L2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8_NORM_L2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8_NORM_L2 computes the L2 norm of a C8.')
    print('')
    print('       C1=C8_UNIFORM_01          R2=C8_NORM_L21(C1)')
    print('     ---------------------     ---------------------')
    print('')

    seed = 123456789

    for i in range(0, 10):
        c1, seed = c8_uniform_01(seed)
        r2 = c8_norm_l2(c1)
        print('  (%12f,%12f)  %12f' % (c1.real, c1.imag, r2))
#
#  Terminate.
#
    print('')
    print('C8_NORM_L2_TEST:')
    print('  Normal end of execution.')
    return


def c8_uniform_01(seed):

    # *****************************************************************************80
    #
    # C8_UNIFORM_01 returns a unit pseudorandom C8.
    #
    #  Discussion:
    #
    #    The angle should be uniformly distributed between 0 and 2 * PI,
    #    the square root of the radius uniformly distributed between 0 and 1.
    #
    #    This results in a uniform distribution of values in the unit circle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, complex C, the pseudorandom complex value.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = np.floor(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('C8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('C8_UNIFORM_01 - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = np.sqrt(seed * 4.656612875E-10)

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    theta = 2.0 * np.pi * seed * 4.656612875E-10

    c = r * complex(np.cos(theta), np.sin(theta))

    return c, seed


def c8_uniform_01_test():

    # *****************************************************************************80
    #
    # C8_UNIFORM_01_TEST tests C8_UNIFORM_01.
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
    import platform

    seed = 123456789

    print('')
    print('C8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8_UNIFORM_01 computes pseudorandom complex values')
    print('  in the unit circle.')

    print('')
    print('  The initial seed is %d' % (seed))
    print('')

    for i in range(0, 10):
        x, seed = c8_uniform_01(seed)
        print('  %6d  ( %g, %g )' % (i, x.real, x.imag))
#
#  Terminate.
#
    print('')
    print('C8_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def c8vec_indicator(n):

    # *****************************************************************************80
    #
    # C8VEC_INDICATOR sets a C8VEC to the indicator vector.
    #
    #  Discussion:
    #
    #    X(1:N) = ( 1-1i, 2-2i, 3-3i, 4-4i, ... )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of elements.
    #
    #    Output, complex A(N), the array.
    #
    import numpy as np

    a = np.zeros(n, 'complex')

    for i in range(0, n):
        a[i] = float(i + 1) - float(i + 1) * 1j

    return a


def c8vec_indicator_test():

    # *****************************************************************************80
    #
    # C8VEC_INDICATOR_TEST tests C8VEC_INDICATOR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8VEC_INDICATOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8VEC_INDICATOR returns the indicator vector.')

    n = 10

    x = c8vec_indicator(n)

    c8vec_print(n, x, '  The indicator vector:')
#
#  Terminate.
#
    print('')
    print('C8VEC_INDICATOR_TEST:')
    print('  Normal end of execution.')
    return


def c8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # C8VEC_PRINT prints a C8VEC.
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
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, complex A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %12g  %12g' % (i, a.real[i], a.imag[i]))

    return


def c8vec_print_test():

    # *****************************************************************************80
    #
    # C8VEC_PRINT_TEST tests C8VEC_PRINT.
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
    print('C8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8VEC_PRINT prints an C8VEC.')

    n = 4
    v = np.array([complex(1.0, 2.0),
                  complex(3.0, 4.0),
                  complex(5.0, 6.0),
                  complex(7.0, 8.0)], dtype=np.complex128)
    c8vec_print(n, v, '  Here is a C8VEC:')
#
#  Terminate.
#
    print('')
    print('C8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def c8vec_sort_a_l2(n, x):

    # *****************************************************************************80
    #
    # C8VEC_SORT_A_L2 ascending sorts a C8VEC by L2 norm.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the array.
    #
    #    Input, complex X(N), an unsorted array.
    #
    #    Output, complex X(N), the sorted array.
    #
    if (1 < n):

        i = 0
        indx = 0
        isgn = 0
        j = 0
        i_save = 0
        j_save = 0
        k_save = 0
        l_save = 0
        n_save = 0

        while (True):

            [indx, i, j, i_save, j_save, k_save, l_save, n_save] = sort_safe_rc(
                n, indx, isgn, i_save, j_save, k_save, l_save, n_save)

            if (0 < indx):

                temp = x[i - 1]
                x[i - 1] = x[j - 1]
                x[j - 1] = temp

            elif (indx < 0):

                if (c8_le_l2(x[i - 1], x[j - 1])):
                    isgn = -1
                else:
                    isgn = +1

            elif (indx == 0):

                break

    return x


def c8vec_sort_a_l2_test():

    # *****************************************************************************80
    #
    # C8VEC_SORT_A_L2_TEST tests C8VEC_SORT_A_L2;
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8VEC_SORT_A_L2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8VEC_SORT_A_L2 sorts a C8VEC by L2 norm.')

    n = 10
    seed = 123456789
    a, seed = c8vec_uniform_01(n, seed)

    c8vec_print(n, a, '  The unsorted vector:')

    a = c8vec_sort_a_l2(n, a)

    print('')
    print('   I                  A(I)                   ||A(I)||')
    print('')

    for i in range(0, n):
        print('  %2d  (%14.6g,%14.6g)  %14.6g'
              % (i, a.real[i], a.imag[i], c8_norm_l2(a[i])))
#
#  Terminate.
#
    print('')
    print('C8VEC_SORT_A_L2_TEST:')
    print('  Normal end of execution.')
    return


def c8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # C8VEC_UNIFORM_01 returns a unit pseudorandom C8VEC.
    #
    #  Discussion:
    #
    #    The angles should be uniformly distributed between 0 and 2 * PI,
    #    the square roots of the radius uniformly distributed between 0 and 1.
    #
    #    This results in a uniform distribution of values in the unit circle.
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
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of values to compute.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, complex C(N), the pseudorandom complex vector.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = np.floor(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('C8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('C8VEC_UNIFORM_01 - Fatal error!')

    c = np.zeros(n, 'complex')

    for j in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        r = np.sqrt(seed * 4.656612875E-10)

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        theta = 2.0 * np.pi * seed * 4.656612875E-10

        c[j] = r * complex(np.cos(theta), np.sin(theta))

    return c, seed


def c8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # C8VEC_UNIFORM_01_TEST tests C8VEC_UNIFORM_01.
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
    import platform

    seed = 123456789

    print('')
    print('C8VEC_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8VEC_UNIFORM_01 computes pseudorandom complex values')
    print('  in the unit circle.')

    print('')
    print('  The initial seed is %d' % (seed))
    print('')

    n = 10

    [x, seed] = c8vec_uniform_01(n, seed)

    for i in range(0, n):
        print('  %6d  ( %f, %f )' % (i, x[i].real, x[i].imag))
#
#  Terminate.
#
    print('')
    print('C8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def c8vec_unity(n):

    # *****************************************************************************80
    #
    # C8VEC_UNITY returns the N roots of unity.
    #
    #  Discussion:
    #
    #    X(1:N) = exp ( 2 * PI * (0:N-1) / N )
    #
    #    X(1:N)^N = ( (1,0), (1,0), ..., (1,0) ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of elements.
    #
    #    Output, complex A(N), the array.
    #
    import numpy as np

    a = np.zeros(n, 'complex')

    for i in range(0, n):
        t = 2.0 * np.pi * float(i) / float(n)
        a[i] = np.cos(t) + 1j * np.sin(t)

    return a


def c8vec_unity_test():

    # *****************************************************************************80
    #
    # C8VEC_UNITY_TEST tests C8VEC_UNITY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8VEC_UNITY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8VEC_UNITY returns the N roots of unity.')

    n = 12

    x = c8vec_unity(n)

    c8vec_print(n, x, '  The N roots of unity:')
#
#  Terminate.
#
    print('')
    print('C8VEC_UNITY_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_PRINT prints an I4VEC.
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
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i4vec_print_test():

    # *****************************************************************************80
    #
    # I4VEC_PRINT_TEST tests I4VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_PRINT prints an I4VEC.')

    n = 4
    v = np.array([91, 92, 93, 94], dtype=np.int32)
    i4vec_print(n, v, '  Here is an I4VEC:')
#
#  Terminate.
#
    print('')
    print('I4VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C(N), the randomly chosen integer vector.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = np.floor(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4VEC_UNIFORM_AB - Fatal error!')

    seed = np.floor(seed)
    a = round(a)
    b = round(b)

    c = np.zeros(n, dtype=np.int32)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        seed = (seed % i4_huge)

        if (seed < 0):
            seed = seed + i4_huge

        r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
        r = (1.0 - r) * (min(a, b) - 0.5) \
            + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
        value = round(r)

        value = max(value, min(a, b))
        value = min(value, max(a, b))

        c[i] = value

    return c, seed


def i4vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
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
    import platform

    n = 20
    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    v, seed = i4vec_uniform_ab(n, a, b, seed)

    i4vec_print(n, v, '  The random vector:')
#
#  Terminate.
#
    print('')
    print('I4VEC_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


def linplus_c8_test():

    # *****************************************************************************80
    #
    # LINPLUS_C8_TEST tests the LINPLUS_C8 library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 October 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LINPLUS_C8_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the LINPLUS_C8 library.')
    print('')

    c8_le_l2_test()
    c8_norm_l2_test()
    c8_uniform_01_test()

    c8mat_print_test()
    c8mat_print_some_test()

    c8vec_indicator_test()
    c8vec_print_test()
    c8vec_sort_a_l2_test()
    c8vec_uniform_01_test()
    c8vec_unity_test()

    i4vec_print_test()
    i4vec_uniform_ab_test()

    sort_safe_rc_test()
#
#  Terminate.
#
    print('')
    print('LINPLUS_C8_TEST:')
    print('  Normal end of execution.')
    return


def sort_safe_rc(n, indx, isgn, i_save, j_save, k_save, l_save, n_save):

    # *****************************************************************************80
    #
    # SORT_SAFE_RC externally sorts a list of items into ascending order.
    #
    #  Discussion:
    #
    #    This is a version of SORT_RC which does not rely on
    #    storing certain work variables internally to the function.  This makes
    #    the function somewhat more awkward to call, but easier to program
    #    in a variety of languages, and safe to use in a parallel programming
    #    environment, or in cases where the sorting of several vectors is to
    #    be carried out at more or less the same time.
    #
    #    The actual list of data is not passed to the routine.  Hence this
    #    routine may be used to sort integers, reals, numbers, names,
    #    dates, shoe sizes, and so on.  After each call, the routine asks
    #    the user to compare or interchange two items, until a special
    #    return value signals that the sorting is completed.
    #
    #  Example:
    #
    #    n = 100
    #    indx = 0
    #    isgn = 0
    #    i_save = 0
    #    j_save = 0
    #    k_save = 0
    #    l_save = 0
    #    n_save = 0
    #
    #    while ( 1 )
    #
    #      indx, i, j, i_save, j_save, k_save, l_save, n_save =
    #        sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save )
    #
    #      if ( indx < 0 )
    #
    #        isgn = 1
    #        if ( a(i) <= a(j) )
    #          isgn = -1
    #        end
    #
    #      elseif ( 0 < indx )
    #
    #        k    = a(i)
    #        a(i) = a(j)
    #        a(j) = k
    #
    #      else
    #
    #        break
    #
    #      end
    #
    #    end
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 March 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Albert Nijenhuis, Herbert Wilf.
    #    MATLAB version by John Burkardt
    #
    #  Reference:
    #
    #    Albert Nijenhuis, Herbert Wilf.
    #    Combinatorial Algorithms,
    #    Academic Press, 1978, second edition,
    #    ISBN 0-12-519260-6.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items to be sorted.
    #
    #    Input, integer INDX, the main communication signal.
    #    The user must set INDX to 0 before the first call.
    #    Thereafter, the user should set the input value of INDX
    #    to the output value from the previous call.
    #
    #    Input, integer ISGN, results of comparison of elements I and J.
    #    (Used only when the previous call returned INDX less than 0).
    #    ISGN <= 0 means I is less than or equal to J
    #    0 <= ISGN means I is greater than or equal to J.
    #
    #    Output, integer INDX, the main communication signal.
    #    If INDX is
    #    * greater than 0, the user should:
    #      interchange items I and J
    #      call again.
    #    * less than 0, the user should:
    #      compare items I and J
    #      set ISGN = -1 if I < J, ISGN = +1 if J < I
    #      call again.
    #    * equal to 0, the sorting is done.
    #
    #    Output, integer I, J, the indices of two items.
    #    On return with INDX positive, elements I and J should be interchanged.
    #    On return with INDX negative, elements I and J should be compared, and
    #    the result reported in ISGN on the next call.
    #
    #    Input/output, integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, workspace
    #    needed by the routine.  Before calling the function,
    #    the user should declare variables to hold these values, but should
    #    not change them, and need not ever examine them.
    #

    #
    #  INDX = 0: This is the first call.
    #
    if (indx == 0):

        k_save = (n // 2)
        l_save = k_save
        n_save = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
    elif (indx < 0):

        if (indx == -2):

            if (isgn < 0):
                i_save = i_save + 1

            j_save = l_save
            l_save = i_save
            indx = -1
            i = i_save
            j = j_save
            return indx, i, j, i_save, j_save, k_save, l_save, n_save

        if (0 < isgn):
            indx = 2
            i = i_save
            j = j_save
            return indx, i, j, i_save, j_save, k_save, l_save, n_save

        if (k_save <= 1):

            if (n_save == 1):
                i_save = 0
                j_save = 0
                indx = 0
            else:
                i_save = n_save
                n_save = n_save - 1
                j_save = 1
                indx = 1

            i = i_save
            j = j_save
            return indx, i, j, i_save, j_save, k_save, l_save, n_save

        k_save = k_save - 1
        l_save = k_save
#
#  0 < INDX, the user was asked to make an interchange.
#
    elif (indx == 1):

        l_save = k_save

    while (True):

        i_save = 2 * l_save

        if (i_save == n_save):
            j_save = l_save
            l_save = i_save
            indx = -1
            i = i_save
            j = j_save
            return indx, i, j, i_save, j_save, k_save, l_save, n_save
        elif (i_save <= n_save):
            j_save = i_save + 1
            indx = -2
            i = i_save
            j = j_save
            return indx, i, j, i_save, j_save, k_save, l_save, n_save

        if (k_save <= 1):
            break

        k_save = k_save - 1
        l_save = k_save

    if (n_save == 1):
        i_save = 0
        j_save = 0
        indx = 0
        i = i_save
        j = j_save
    else:
        i_save = n_save
        n_save = n_save - 1
        j_save = 1
        indx = 1
        i = i_save
        j = j_save

    return indx, i, j, i_save, j_save, k_save, l_save, n_save


def sort_safe_rc_test():

    # *****************************************************************************80
    #
    # SORT_SAFE_RC_TEST tests SORT_SAFE_RC on an integer vector.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 20

    print('')
    print('SORT_SAFE_RC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SORT_SAFE_RC sorts objects externally.')
    print('  This function does not use persistent memory.')
#
#  Generate some data to sort.
#
    i4_lo = 1
    i4_hi = n
    seed = 123456789

    a, seed = i4vec_uniform_ab(n, i4_lo, i4_hi, seed)

    i4vec_print(n, a, '  Unsorted array:')
#
#  Sort the data.
#
    indx = 0
    isgn = 0
    i_save = 0
    j_save = 0
    k_save = 0
    l_save = 0
    n_save = 0

    while (True):

        indx, i, j, i_save, j_save, k_save, l_save, n_save = \
            sort_safe_rc(n, indx, isgn, i_save, j_save, k_save, l_save, n_save)

        if (indx < 0):
            isgn = 1
            if (a[i - 1] <= a[j - 1]):
                isgn = -1
        elif (0 < indx):
            k = a[i - 1]
            a[i - 1] = a[j - 1]
            a[j - 1] = k
        else:
            break
#
#  Display the sorted data.
#
    i4vec_print(n, a, '  Sorted array:')
#
#  Terminate.
#
    print('')
    print('SORT_SAFE_RC_TEST:')
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
    linplus_c8_test()
    timestamp()
