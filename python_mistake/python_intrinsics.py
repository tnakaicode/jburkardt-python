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


def python_intrinsics_test():

    # *****************************************************************************80
    #
    # python_intrinsics_test tests python_intrinsics.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('python_intrinsics_test:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test python_intrinsics.')

    abs_test()
    all_test()
    any_test()
    bin_test()
    bool_test()
    bytearray_test()
    chr_test()
    # complex_test ( )
    dir_test()
    divmod_test()
    eval_test()
    float_test()
    globals_test()
    hash_test()
    hex_test()
    id_test()
    int_test()
    len_test()
    locals_test()
    max_test()
    min_test()
    oct_test()
    ord_test()
    pow_test()
    range_test()
    reversed_test()
    round_test()
    slice_test()
    sorted_test()
    sum_test()

    print('')
    print('python_intrinsics_test:')
    print('  Normal end of execution.')


def abs_test():

    # *****************************************************************************80
    #
    # abs_test tests abs().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('abs_test')
    print('  abs() returns the absolute value of a number.')
    print('')
    print('      x         abs(x)')
    print('')

    for test in range(0, 10):
        r8 = 100.0 * np.random.randn()
        r8_absolute = abs(r8)
        print('  %10.6f  %10.6f' % (r8, r8_absolute))

    print('')

    for test in range(0, 10):
        i4 = np.random.randint(-100000000, +100000000)
        i4_absolute = abs(i4)
        print('  %10d  %10d' % (i4, i4_absolute))

    return


def all_test():

    # *****************************************************************************80
    #
    # all_test tests all().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('all_test')
    print('  all() returns True if all elements are True.')
    print('')

    a = np.array([-2, 4, 12])
    print('  a = [', a[0], ',', a[1], ',', a[2], ']')
    print('')
    print('  all(a<10)', all(a < 10))
    print('  all(a!=0)', all(a != 0))
    print('  (all(-5<a)) and all(a<20))', (all(-5 < a) and all(a < 20)))

    return


def any_test():

    # *****************************************************************************80
    #
    # any_test tests any().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('any_test')
    print('  any() returns True if any elements is True.')
    print('')

    a = np.array([-2, 4, 12])
    print('  a = [', a[0], ',', a[1], ',', a[2], ']')
    print('')
    print('  any(a<1)', any(a < 1))
    print('  any(a==0)', any(a == 0))
    print('  (any(-5<a)) and any(a<-4))', (any(-5 < a) and any(a < -4)))
    print('  (any(-5<a)) or  any(a<-4))', (any(-5 < a) or any(a < -4)))

    return


def bin_test():

    # *****************************************************************************80
    #
    # bin_test tests bin().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('bin_test')
    print('  bin() returns a string that is the binary representation of an integer.')
    print('')
    print('      i         bin(i)')
    print('')

    data = np.array([0, 1, 2, 3, 4, 5, 10, 20, 30, 2019, -11])

    for i in data:
        s = bin(i)
        print('  %4d  %s' % (i, s))

    return


def bool_test():

    # *****************************************************************************80
    #
    # bool_test tests bool().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('bool_test')
    print('  bool() converts a value to a Boolean value.')
    print('')
    print('  value         bool(value)')
    print('')

    b = bool()
    print('  (empty)  ', b)

    value = True
    b = bool(value)
    print('  True  ', b)

    value = -1
    b = bool(value)
    print('  -1  ', b)

    value = 0
    b = bool(value)
    print('  0  ', b)

    value = 1000
    b = bool(value)
    print('  1000  ', b)

    value = np.pi
    b = bool(value)
    print('  3.14159...  ', b)

    value = ''
    b = bool(value)
    print('  \'\'  ', b)

    value = 'January'
    b = bool(value)
    print('  \'January\'  ', b)

    return


def bytearray_test():

    # *****************************************************************************80
    #
    # bytearray_test tests bytearray().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('bytearray_test')
    print('  bytearray() converts a string to an array of bytes.')
    print('')

    s = 'Hello!'
    encoding = 'utf-8'
    print('  bytearray(\'', s, '\',\'', encoding, '\') =', bytearray(s, encoding))

    s = 'Hello!'
    encoding = 'utf-16'
    print('  bytearray(\'', s, '\',\'', encoding, '\') =', bytearray(s, encoding))

    return


def chr_test():

    # *****************************************************************************80
    #
    # chr_test tests chr().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import string

    print('')
    print('chr_test')
    print('  chr(i) returns the i-th character.')
    print('')

    for i in range(0, 128):
        if ((i % 16) == 0):
            print('    ', end='')
        c = chr(i)
        if (c in string.digits or c in string.ascii_letters or c in string.punctuation):
            print(c, end='')
        else:
            print('X', end='')

        if ((i % 16) == 15):
            print('')

    return


def dir_test():

    # *****************************************************************************80
    #
    # dir_test tests dir().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    from pprint import pprint
    import string

    print('')
    print('dir_test')
    print('  dir() lists objects.')
    print('  dir(x) lists methods and properties of object x')
    print('')
    print('  The dir() command actually only prints information')
    print('  during interactive use, so the following dir()')
    print('  commands will not print out anything, since we')
    print('  are running noninteractively.')

    a = 1
    b = 2.3
    c = 'I love Java!'
    d = [4, 5, 6]

    print('  After defining a, b, c, and d, issue "dir()"')
    x = dir()
    pprint(x)

    print('')
    print('  Issue "dir(b)"')
    x = dir(b)
    pprint(x)

    return


def divmod_test():

    # *****************************************************************************80
    #
    # divmod_test tests divmod().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('divmod_test')
    print('  divmod(a,b) returns the rounded quotient and remainder of a/b.')
    print('')
    print('     a     b     q   r')
    print('')

    for test in range(0, 10):
        a = np.random.randint(-1000, +1000)
        b = np.random.randint(-100, +100)
        if (b != 0):
            q, r = divmod(a, b)
            print('  %6d  %6d  %6d  %6d' % (a, b, q, r))
    print('')

    for test in range(0, 10):
        a = 100.0 * np.random.randn()
        b = 10.0 * np.random.randn()
        q, r = divmod(a, b)
        print('  %10.6f  %10.6f  %10.6f  %10.6f' % (a, b, q, r))

    return


def eval_test():

    # *****************************************************************************80
    #
    # eval_test tests eval().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('eval_test')
    print('  eval() takes a string, which might represent a formula,')
    print('  and evaluates it.')
    print('')

    x = 1
    s = 'x + 9'
    v = eval(s)

    print('  x = ', x, ' s = \'', s, '\', eval(s) = ', v)

    x = 101
    s = 'x + 9'
    v = eval(s)

    print('  x = ', x, ' s = \'', s, '\', eval(s) = ', v)

    a = 1.2
    b = 8.0
    s = 'a * b + 1'
    v = eval(s)

    print('  a = ', a, ' b = ', b, ' s = \'', s, '\', eval(s) = ', v)

    return


def float_test():

    # *****************************************************************************80
    #
    # float_test tests float().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('float_test')
    print('  float returns the float version of a value.')
    print('')

    a = 123456
    float_a = float(a)
    print('  a =', a, ', float(a)=', float_a)

    a = np.pi
    float_a = float(a)
    print('  a =', a, ', float(a)=', float_a)

    a = '123.456'
    float_a = float(a)
    print('  a = \'', a, '\', float(a)=', float_a)

    return


def globals_test():

    # *****************************************************************************80
    #
    # globals_test tests globals().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    from pprint import pprint

    print('')
    print('globals_test')
    print('  globals() lists the global variables.')

    a = 1
    b = 2.3
    c = 'Who is that?'
    data = np.array([-1, -2, -3])
    e = (4, 5, 6)

    pprint(globals())


def hash_test():

    # *****************************************************************************80
    #
    # hash_test tests hash().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('hash_test')
    print('  hash() returns a hash value.')
    print('')
    print('      x         hash(x)')
    print('')

    data = np.array([-1, -2, -3, 0, 1, 2, 12345,
                     2019, -11, 691752902764109836])

    for i in data:
        j = hash(i)
        print('  %18d  %18d' % (i, j))

    x = 0.0
    j = hash(x)
    print('  %18.12g  %18d' % (x, j))
    x = 1.0
    j = hash(x)
    print('  %18.12g  %18d' % (x, j))
    x = np.pi
    j = hash(x)
    print('  %18.12g  %18d' % (x, j))
    x = 12345.6789
    j = hash(x)
    print('  %18.12g  %18d' % (x, j))
    x = 12345.6789

    s = 'a'
    j = hash(s)
    print('  \'%18s\'  %18d' % (s, j))
    s = 'abcde'
    j = hash(s)
    print('  \'%18s\'  %18d' % (s, j))
    s = '12345'
    j = hash(s)
    print('  \'%18s\'  %18d' % (s, j))


def hex_test():

    # *****************************************************************************80
    #
    # hex_test tests hex().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('hex_test')
    print('  hex() returns a string that is the hexadecimal representation')
    print('  of an integer.')
    print('')
    print('      i         hex(i)')
    print('')

    data = np.array([0, 1, 2, 3, 4, 5, 10, 20, 30, 2019, -11])

    for i in data:
        s = hex(i)
        print('  %4d  %s' % (i, s))

    return


def id_test():

    # *****************************************************************************80
    #
    # id_test tests id().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('id_test')
    print('  id returns the unique identifing number of an object.')
    print('')
    a = np.pi
    print('  a = ', a, ' id(a)=', id(a))
    b = 3
    print('  b = ', b, ' id(b)=', id(b))
    c = 'Hallelujah!'
    print('  c = ', c, ' id(c)=', id(c))
    d = np.array([1, 2, 3])
    print('  d = ', d, ' id(d)=', id(d))
    e = id_test
    print('  e = id_test, id(e) = ', id(e))

    return


def int_test():

    # *****************************************************************************80
    #
    # int_test tests int().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('int_test')
    print('  int returns the integer version of a value.')
    print('  You cannot convert a complex value.')
    print('  You cannot convert a string which includes a decimal point.')
    print('')
    a = np.pi
    int_a = int(a)
    print('  a =', a, ', int(a)=', int_a)
#
#  What about rounding?
#
    a = 4.5
    int_a = int(a)
    print('  a =', a, ', int(a)=', int_a)
    a = 5.5
    int_a = int(a)
    print('  a =', a, ', int(a)=', int_a)

    a = '904'
    int_a = int(a)
    print('  a = \'', a, '\', int(a)=', int_a)
#
#  Can include a numeric base.
#
    a = '101'
    int_a = int(a, 2)
    print('  a = \'', a, '\', int(a,2)=', int_a)
    a = '101'
    int_a = int(a, 5)
    print('  a = \'', a, '\', int(a,5)=', int_a)
    a = '101'
    int_a = int(a, 10)
    print('  a = \'', a, '\', int(a,10)=', int_a)

    a = '101'
    int_a = int(a, 16)
    print('  a = \'', a, '\', int(a,16)=', int_a)

    return


def len_test():

    # *****************************************************************************80
    #
    # len_test tests len().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('len_test')
    print('  len() returns the length of a string, tuple, or list.')

    print('')
    x = range(5, 10)
    print('  x=range(5,10)')
    print('  len(x) = ', len(x))

    print('')
    x = 'Matlab'
    print('  x=\'Matlab\'')
    print('  len(x) = ', len(x))

    print('')
    x = [10, 11, 12]
    print('  x = [ 10, 11, 12 ]')
    print('  len(x) = ', len(x))

    print('')
    x = (10, 11, 12)
    print('  x = ( 10, 11, 12 )')
    print('  len(x) = ', len(x))

    return


def locals_test():

    # *****************************************************************************80
    #
    # locals_test tests locals().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    from pprint import pprint

    print('')
    print('locals_test')
    print('  locals() lists the local variables.')

    a = 1
    b = 2.3
    c = 'Who is that?'
    data = np.array([-1, -2, -3])
    e = (4, 5, 6)

    pprint(locals())


def max_test():

    # *****************************************************************************80
    #
    # max_test tests max().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('max_test')
    print('  max returns the maximum of a pair of arguments, or an array.')
    print('')
    print('  max(a,b) returns the maximum of a and b.')
    print('     a     b     max(a,b)')
    print('')

    for test in range(0, 10):
        i1 = np.random.randint(-1000, +1000)
        i2 = np.random.randint(-1000, +1000)
        i3 = max(i1, i2)
        print('  %6d  %6d  %6d' % (i1, i2, i3))

    print('')
    print('  max(a) returns the maximum element of a.')
    print('     a1    a2   a3     max(a)')
    print('')

    for test in range(0, 10):
        a = np.random.randint(-1000, +1000, [3, 1])
        a_max = max(a)
        print('  %6d  %6d  %6d  %6d' % (a[0], a[1], a[2], a_max))

    return


def min_test():

    # *****************************************************************************80
    #
    # min_test tests min().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('min_test')
    print('  min returns the minimum of a pair of arguments, or an array.')
    print('')
    print('  min(a,b) returns the minimum of a and b.')
    print('     a     b     min(a,b)')
    print('')

    for test in range(0, 10):
        r1 = 100.0 * np.random.randn()
        r2 = 100.0 * np.random.randn()
        r3 = min(r1, r2)
        print('  %10.2f  %10.2f  %10.2f' % (r1, r2, r3))

    print('')
    print('  min(a) returns the minimum element of a.')
    print('     a1    a2   a3     min(a)')
    print('')

    for test in range(0, 10):
        a = 100.0 * np.random.randn(3)
        a_min = min(a)
        print('  %10.2f  %10.2f  %10.2f  %10.2f' % (a[0], a[1], a[2], a_min))

    return


def oct_test():

    # *****************************************************************************80
    #
    # oct_test tests oct().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('oct_test')
    print('  oct() returns a string that is the octal representation of an integer.')
    print('')
    print('      i         oct(i)')
    print('')

    data = np.array([0, 1, 2, 3, 4, 5, 10, 20, 30, 2019, -11])

    for i in data:
        s = oct(i)
        print('  %4d  %s' % (i, s))

    return


def ord_test():

    # *****************************************************************************80
    #
    # ord_test tests ord().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import string

    print('')
    print('ord_test')
    print('  ord(c) returns the index of character c.')
    print('')
    s = "Isn't this wonderful?"
    print('  String of characters: "', s, '".')
    print('')

    for c in s:
        print('  \'', c, '\' has character index', ord(c))

    return


def pow_test():

    # *****************************************************************************80
    #
    # pow_test tests pow().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('pow_test')
    print('')
    print('  pow(a,b) returns a to the power b.')
    print('     a     b     pow(a,b)')
    print('')
    print('  %g  %g  %g' % (2, 3, pow(2, 3)))
    print('  %g  %g  %g' % (2, -3, pow(2, -3)))
    print('  %g  %g  %g' % (-2, 3, pow(-2, 3)))
    print('  %g  %g  %g' % (-2, -3, pow(-2, -3)))
    x = np.pi
    print('  %g  %g  %g' % (x, 3, pow(x, 3)))
    print('  %g  %g  %g' % (x, -3, pow(x, -3)))
    print('  %g  %g  %g' % (2, x, pow(2, x)))
    print('')
    print('  pow(a,b,z) returns a to the power b, mod z.')
    print('     a     b    c     pow(a,b,z)')
    print('')
    print('  %g  %g  %g  %g' % (10, 3, 3, pow(10, 3, 3)))
    print('  %g  %g  %g  %g' % (10, 3, 5, pow(10, 3, 5)))
    print('  %g  %g  %g  %g' % (10, 3, 7, pow(10, 3, 7)))

    return


def range_test():

    # *****************************************************************************80
    #
    # range_test tests range().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('range_test')
    print('')
    print('  range(a,b) creates a range of integers from a to b-1.')
    print('  range(a,b,c) creates a range of integers from a to b-1 by increments of c.')

    print('')
    x = range(5, 10)
    print('  x=range(5,10)', x)
    print('  ', end='')
    for i in x:
        print(i, end=',')

    print('')
    x = range(1, 11, 2)
    print('  x=range(1,11,2)', x)
    print('  ', end='')
    for i in x:
        print(i, end=',')

    print('')
    x = range(11, 1, -2)
    print('  x=range(11,1,-2)', x)
    print('  ', end='')
    for i in x:
        print(i, end=',')

    print('  ')
    x = range(10, 20)
    print('  x=range(10,20) =', x)

    y = (8 in x)
    print('  y = (8 in x) is', y)
    z = len(x)
    print('  len(x) =', z)

    return


def reversed_test():

    # *****************************************************************************80
    #
    # reversed_test tests reversed().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('reversed_test')
    print('  reversed(object) returns a "reversed" version of the object.')

    print('')
    x = range(5, 10)
    print('  x=range(5,10)')
    for i in x:
        print(' ', i, end='')
    print('')

    xr = reversed(x)
    print('  xr = reversed(x)')
    for i in xr:
        print(' ', i, end='')
    print('')

    print('')
    s = 'Matlab'
    print('  s=\'Matlab\'')
    for i in s:
        print(' ', i, end='')
    print('')

    sr = reversed(s)
    print('  sr = reversed(s)')
    for i in sr:
        print(' ', i, end='')
    print('')

    print('')
    x = [10, 11, 12]
    print('  x = [ 10, 11, 12 ]')
    for i in x:
        print(' ', i, end='')
    print('')

    xr = reversed(x)
    print('  xr = reversed(x)')
    for i in xr:
        print(' ', i, end='')
    print('')

    print('')
    x = (10, 11, 12)
    print('  x = ( 10, 11, 12 )')
    for i in x:
        print(' ', i, end='')
    print('')

    xr = reversed(x)
    print('  xr = reversed(x)')
    for i in xr:
        print(' ', i, end='')
    print('')

    return


def round_test():

    # *****************************************************************************80
    #
    # round_test tests round().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('round_test')
    print('  round(x) rounds x to the nearest integral value.')
    print('')
    print('      x         round(x)')
    print('')

    for test in range(0, 10):
        r8 = 100.0 * np.random.randn()
        r8_round = round(r8)
        print('  %10.6f  %10.6f' % (r8, r8_round))

    print('')
    print('  round(x,ndigits) rounds x to n digits.')
    print('')
    print('      x     ndigits         round(x,ndigits)')
    print('')
    x = np.pi * 100.0
    for ndigits in range(0, 11):
        r8_round = round(x, ndigits)
        print('  %14.10f  %2d  %14.10f' % (x, ndigits, r8_round))

    return


def slice_test():

    # *****************************************************************************80
    #
    # slice_test tests slice().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('slice_test')
    print('  The slice() function creates an object represented')
    print('  by range(start:stop:increment)')

    s = 'Abcdefghijklmnopqrstuvwxyz'
    print('')
    print('  s: \'', s, '\'')

    print('')
    x = slice(0, 10, 2)
    print('  s[slice(0,10,2)]:', s[x])

    print('')
    x = slice(26, 0, -3)
    print('  s[slice(26,0,-3)]:', s[x])

    print('')
    x = slice(6)
    print('  s[slice(6)]:', s[x])

    return


def sorted_test():

    # *****************************************************************************80
    #
    # sorted_test tests sorted().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('sorted_test')
    print('  Demonstrate the sorted function.')
    print('')
    print('  sorted(x) returns a sorted list')
    print('')
    x = [3, 1, 4, 6, 2]
    print('  x =', x)
    y = sorted(x)
    print('  sorted(x) =(', y)
    z = sorted(x, reverse=True)
    print('  sorted(x,reverse=True) =(', z)

    print('')
    x = [1.23, 231.0, 31.2, 0.35]
    print('  x =', x)
    y = sorted(x)
    print('  sorted(x) =(', y)
    z = sorted(x, reverse=True)
    print('  sorted(x,reverse=True) =(', z)

    print('')
    x = ['a', 'c', 'z', 'b', 'D']
    print('  x =', x)
    y = sorted(x)
    print('  sorted(x) =(', y)
    z = sorted(x, reverse=True)
    print('  sorted(x,reverse=True) =(', z)

    print('')
    x = 'Anaconda'
    print('  x =', x)
    y = sorted(x)
    print('  sorted(x) =(', y)
    z = sorted(x, reverse=True)
    print('  sorted(x,reverse=True) =(', z)

    return


def sum_test():

    # *****************************************************************************80
    #
    # sum_test tests sum().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('sum_test')
    print('  Demonstrate the sum function.')

    print('')
    print('  sum(x) computes the sum of entries')
    print('')
    x = [5.0, 10.1, 15.2, 20.3]
    s = sum(x)
    print('  sum(', x, ') = ', s)

    print('')
    print('  sum(x) can count Boolean True values')
    print('')
    x = [False, True, True, False]
    s = sum(x)
    print('  sum(', x, ') = ', s)

    print('')
    print('  sum(x,init) computes the sum of the entries plus init.')
    print('')
    x = [5.0, 10.1, 15.2, 20.3]
    s = sum(x, 100)
    print('  sum(', x, ',100) = ', s)

    return


if (__name__ == '__main__'):
    timestamp()
    python_intrinsics_test()
    timestamp()
