#! /usr/bin/env python3
#
def complex_numbers_test():
    
    # *****************************************************************************80
    #
    # complex_numbers_test is a program which demonstrates the use of complex numbers.
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
    import platform

    print('')
    print('complex_numbers_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  Demonstrate complex number usage.')
#
#  Single precision complex numbers: "complex64".
#
    complex_numbers_test01()
    complex_numbers_test02()
    complex_numbers_test03()
#
#  Double precision complex numbers: "complex128".
#
    complex_numbers_test04()
    complex_numbers_test05()
    complex_numbers_test06()
#
#  Terminate.
#
    print('')
    print('complex_numbers_test')
    print('  Normal end of execution.')
    return


def complex_numbers_test01():

    # *****************************************************************************80
    #
    #  COMPLEX_NUMBERS_TEST01 demonstrates declaration and assignment.
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
    import numpy as np
#
#  Declare a complex number A.
#  Declare a complex vector B.
#  Declare a complex array C.
#
    print('')
    print('COMPLEX_NUMBERS_TEST01')
    print('  Declare single precision complex variables.')
    print('  Assign value with an = statement.')
#
#  Assign values to A, B, and C.
#
    a = np.complex64(1.0 + 2.0j)
    print('')
    print('  Scalar a:')
    print('    (%+g%+gj)' % (a.real, a.imag))

    b = np.zeros(3, dtype=np.complex64)
    b[0] = 1.0 - 2.0j
    b[1] = - 3.0 + 4.0j
    b[2] = - 5.0 - 6.0j
    print('')
    print('  Vector b:')
    for i in range(0, 3):
        print('    (%+g%+gj)' % (b[i].real, b[i].imag))

    c = np.zeros([2, 2], dtype=np.complex64)
    c[0, 0] = 1.0 + 0.1j
    c[0, 1] = 1.0 + 0.2j
    c[1, 0] = 2.0 + 0.1j
    c[1, 1] = 2.0 + 0.2j
    print('')
    print('  Matrix c:')
    for i in range(0, 2):
        for j in range(0, 2):
            print('  (%+g%+gj)' % (c[i, j].real, c[i, j].imag), end='')
        print('')

    return


def complex_numbers_test02():

    # *****************************************************************************80
    #
    # COMPLEX_NUMBERS_TEST02 demonstrate declaration and initialization for complex variables.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('COMPLEX_NUMBERS_TEST02')
    print('  Declare single precision complex variables.')
    print('  Initialize value as part of the declaration.')

    a = np.complex64(1.0 + 2.0j)
    print('')
    print('  Scalar a:')
    print('    (%+g%+gj)' % (a.real, a.imag))

    b = np.array([1.0 + 2.0j, 3.0 + 4.0j, 5.0 + 6.0j], dtype=np.complex64)
    print('')
    print('  Vector b:')
    for i in range(0, 3):
        print('    (%+g%+gj)' % (b[i].real, b[i].imag))

    c = np.array([[1.0 + 0.1j, 1.0 + 0.2j],
                  [2.0 + 0.1j, 2.0 + 0.2j]], dtype=np.complex64)
    print('')
    print('  Matrix c:')
    for i in range(0, 2):
        for j in range(0, 2):
            print('  (%+g%+gj)' % (c[i, j].real, c[i, j].imag), end='')
        print('')
#
#  Stupidly, Python won't let you say d = complex ( dr, di )...
#
    dr = np.array([1.0, 2.0, 3.0], dtype=np.float32)
    di = np.array([4.0, 5.0, 6.0], dtype=np.float32)
    d = dr + di * 1j
    print('')
    print('  Vector d = dr + di * 1j:')
    for i in range(0, 3):
        print('    (%+g%+gj)' % (d[i].real, d[i].imag))

    return


def complex_numbers_test03():

    # *****************************************************************************80
    #
    #  Purpose:
    #
    #    COMPLEX_NUMBERS_TEST03: intrinsic functions for complex variables.
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
    import numpy as np

    a = np.complex64(1.0 + 2.0j)

    print('')
    print('COMPLEX_NUMBERS_TEST03')
    print('  Apply intrinsic functions to single precision complex variables')
    print('')
    print('  1j =                 (%+g%+g)' % (1j.real, 1j.imag))
    print('  a =                  (%+g%+g)' % (a.real, a.imag))
    print('  - a =                (%+g%+g)' % (- a.real, -a.imag))
    print('  a + 3 =              (%+g%+g)' % ((a + 3).real, (a + 3).imag))
    print('  a + 5j =             (%+g%+g)' % ((a + 5j).real, (a + 5j).imag))
    print('  4 * a =              (%+g%+g)' % ((4 * a).real, (4 * a).imag))
    print('  a / 8 =              (%+g%+g)' % ((a / 8).real, (a / 8).imag))
    print('  a * a =              (%+g%+g)' % ((a * a).real, (a * a).imag))
    print('  a ** 2 =             (%+g%+g)' % ((a ** 2).real, (a ** 2).imag))
    print('  2 ** a =             (%+g%+g)' % ((2 ** a).real, (2 ** a).imag))
    print('  a ** a =             (%+g%+g)' % ((a ** a).real, (a ** a).imag))
    print('  1/a =                (%+g%+g)' % ((1.0 / a).real, (1.0 / a).imag))
    print('')
    print('  abs(a) =             (%+g)' % (abs(a)))
    print('  arccos(a) =          (%+g%+g)' %
          ((np.arccos(a)).real, (np.arccos(a)).imag))
    print('  arccosh(a) =         (%+g%+g)' %
          ((np.arccosh(a)).real, (np.arccosh(a)).imag))
    print('  angle(a) =           %+g' % np.angle(a))
    print('  arcsin(a) =          (%+g%+g)' %
          ((np.arcsin(a)).real, (np.arcsin(a)).imag))
    print('  arcsinh(a) =         (%+g%+g)' %
          ((np.arcsinh(a)).real, (np.arcsinh(a)).imag))
    print('  arctan(a) =          (%+g%+g)' %
          ((np.arctan(a)).real, (np.arctan(a)).imag))
    print('  arctanh(a) =         (%+g%+g)' %
          ((np.arctanh(a)).real, (np.arctanh(a)).imag))
    print('  complex(1) =         (%+g%+g)' %
          ((complex(1)).real, (complex(1)).imag))
    print('  conjugate(a) =       (%+g%+g)' %
          (np.conjugate(a).real, np.conjugate(a).imag))
    print('  cos(a) =             (%+g%+g)' %
          ((np.cos(a)).real, (np.cos(a)).imag))
    print('  cosh(a) =            (%+g%+g)' %
          ((np.cosh(a)).real, (np.cosh(a)).imag))
    print('  exp(a) =             (%+g%+g)' %
          ((np.exp(a)).real, (np.exp(a)).imag))
    print('  a.imag =              %+g' % (a.imag))
    print('  isinf(a) =            %+s' % (np.isinf(a)))
    print('  isnan(a) =            %+s' % (np.isnan(a)))
    print('  log(a) =             (%+g%+g)' %
          ((np.log(a)).real, (np.log(a)).imag))
    print('  log10(a) =           (%+g%+g)' %
          ((np.log10(a)).real, (np.log10(a)).imag))
    print('  a.real =              %+g' % (a.real))
    print('  sin(a) =             (%+g%+g)' %
          ((np.sin(a)).real, (np.sin(a)).imag))
    print('  sinh(a) =            (%+g%+g)' %
          ((np.sinh(a)).real, (np.sinh(a)).imag))
    print('  sqrt(a) =            (%+g%+g)' %
          ((np.sqrt(a)).real, (np.sqrt(a)).imag))
    print('  tan(a) =             (%+g%+g)' %
          ((np.tan(a)).real, (np.tan(a)).imag))
    print('  tanh(a) =            (%+24.16g%+24.16g)' %
          ((np.tanh(a)).real, (np.tanh(a)).imag))

    return


def complex_numbers_test04():

    # *****************************************************************************80
    #
    #  COMPLEX_NUMBERS_TEST04 demonstrates declaration and assignment.
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
    import numpy as np
#
#  Declare a complex number A.
#  Declare a complex vector B.
#  Declare a complex array C.
#
    print('')
    print('COMPLEX_NUMBERS_TEST04')
    print('  Declare double precision complex variables.')
    print('  Assign value with an = statement.')
#
#  Assign values to A, B, and C.
#
    a = np.complex128(1.0 + 2.0j)
    print('')
    print('  Scalar a:')
    print('    (%+g%+gj)' % (a.real, a.imag))

    b = np.zeros(3, dtype=np.complex128)
    b[0] = 1.0 - 2.0j
    b[1] = - 3.0 + 4.0j
    b[2] = - 5.0 - 6.0j
    print('')
    print('  Vector b:')
    for i in range(0, 3):
        print('    (%+g%+gj)' % (b[i].real, b[i].imag))

    c = np.zeros([2, 2], dtype=np.complex128)
    c[0, 0] = 1.0 + 0.1j
    c[0, 1] = 1.0 + 0.2j
    c[1, 0] = 2.0 + 0.1j
    c[1, 1] = 2.0 + 0.2j
    print('')
    print('  Matrix c:')
    for i in range(0, 2):
        for j in range(0, 2):
            print('  (%+g%+gj)' % (c[i, j].real, c[i, j].imag), end='')
        print('')

    return


def complex_numbers_test05():

    # *****************************************************************************80
    #
    # COMPLEX_NUMBERS_TEST05 demonstrate declaration and initialization for complex variables.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('COMPLEX_NUMBERS_TEST05')
    print('  Declare a double precision complex variable.')
    print('  Initialize value as part of the declaration.')

    a = np.complex128(1.0 + 2.0j)
    print('')
    print('  Scalar a:')
    print('    (%+g%+gj)' % (a.real, a.imag))

    b = np.array([1.0 + 2.0j, 3.0 + 4.0j, 5.0 + 6.0j], dtype=np.complex128)
    print('')
    print('  Vector b:')
    for i in range(0, 3):
        print('    (%+g%+gj)' % (b[i].real, b[i].imag))

    c = np.array([[1.0 + 0.1j, 1.0 + 0.2j],
                  [2.0 + 0.1j, 2.0 + 0.2j]], dtype=np.complex128)
    print('')
    print('  Matrix c:')
    for i in range(0, 2):
        for j in range(0, 2):
            print('  (%+g%+gj)' % (c[i, j].real, c[i, j].imag), end='')
        print('')
#
#  Stupidly, Python won't let you say d = complex ( dr, di )...
#
    dr = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    di = np.array([4.0, 5.0, 6.0], dtype=np.float64)
    d = dr + di * 1j
    print('')
    print('  Vector d = dr + di * 1j:')
    for i in range(0, 3):
        print('    (%+g%+gj)' % (d[i].real, d[i].imag))

    return


def complex_numbers_test06():

    # *****************************************************************************80
    #
    #  Purpose:
    #
    #    COMPLEX_NUMBERS_TEST06: intrinsic functions for complex variables.
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
    import numpy as np

    a = np.complex128(1.0 + 2.0j)

    print('')
    print('COMPLEX_NUMBERS_TEST06')
    print('  Apply intrinsic functions to double precision complex variables')
    print('')
    print('  1j =                 (%+g%+g)' % (1j.real, 1j.imag))
    print('  a =                  (%+g%+g)' % (a.real, a.imag))
    print('  - a =                (%+g%+g)' % (- a.real, -a.imag))
    print('  a + 3 =              (%+g%+g)' % ((a + 3).real, (a + 3).imag))
    print('  a + 5j =             (%+g%+g)' % ((a + 5j).real, (a + 5j).imag))
    print('  4 * a =              (%+g%+g)' % ((4 * a).real, (4 * a).imag))
    print('  a / 8 =              (%+g%+g)' % ((a / 8).real, (a / 8).imag))
    print('  a * a =              (%+g%+g)' % ((a * a).real, (a * a).imag))
    print('  a ** 2 =             (%+g%+g)' % ((a ** 2).real, (a ** 2).imag))
    print('  2 ** a =             (%+g%+g)' % ((2 ** a).real, (2 ** a).imag))
    print('  a ** a =             (%+g%+g)' % ((a ** a).real, (a ** a).imag))
    print('  1/a =                (%+g%+g)' % ((1.0 / a).real, (1.0 / a).imag))
    print('')
    print('  abs(a) =             (%+g)' % (abs(a)))
    print('  arccos(a) =          (%+g%+g)' %
          ((np.arccos(a)).real, (np.arccos(a)).imag))
    print('  arccosh(a) =         (%+g%+g)' %
          ((np.arccosh(a)).real, (np.arccosh(a)).imag))
    print('  angle(a) =           %+g' % np.angle(a))
    print('  arcsin(a) =          (%+g%+g)' %
          ((np.arcsin(a)).real, (np.arcsin(a)).imag))
    print('  arcsinh(a) =         (%+g%+g)' %
          ((np.arcsinh(a)).real, (np.arcsinh(a)).imag))
    print('  arctan(a) =          (%+g%+g)' %
          ((np.arctan(a)).real, (np.arctan(a)).imag))
    print('  arctanh(a) =         (%+g%+g)' %
          ((np.arctanh(a)).real, (np.arctanh(a)).imag))
    print('  complex(1) =         (%+g%+g)' %
          ((complex(1)).real, (complex(1)).imag))
    print('  conjugate(a) =       (%+g%+g)' %
          (np.conjugate(a).real, np.conjugate(a).imag))
    print('  cos(a) =             (%+g%+g)' %
          ((np.cos(a)).real, (np.cos(a)).imag))
    print('  cosh(a) =            (%+g%+g)' %
          ((np.cosh(a)).real, (np.cosh(a)).imag))
    print('  exp(a) =             (%+g%+g)' %
          ((np.exp(a)).real, (np.exp(a)).imag))
    print('  a.imag =              %+g' % (a.imag))
    print('  isinf(a) =            %+s' % (np.isinf(a)))
    print('  isnan(a) =            %+s' % (np.isnan(a)))
    print('  log(a) =             (%+g%+g)' %
          ((np.log(a)).real, (np.log(a)).imag))
    print('  log10(a) =           (%+g%+g)' %
          ((np.log10(a)).real, (np.log10(a)).imag))
    print('  a.real =              %+g' % (a.real))
    print('  sin(a) =             (%+g%+g)' %
          ((np.sin(a)).real, (np.sin(a)).imag))
    print('  sinh(a) =            (%+g%+g)' %
          ((np.sinh(a)).real, (np.sinh(a)).imag))
    print('  sqrt(a) =            (%+g%+g)' %
          ((np.sqrt(a)).real, (np.sqrt(a)).imag))
    print('  tan(a) =             (%+g%+g)' %
          ((np.tan(a)).real, (np.tan(a)).imag))
    print('  tanh(a) =            (%+g%+g)' %
          ((np.tanh(a)).real, (np.tanh(a)).imag))

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
    complex_numbers_test()
    timestamp()
