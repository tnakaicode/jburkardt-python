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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4vec_sum import i4vec_sum
from i4lib.ui4_to_ubvec import ui4_to_ubvec


def morse_thue(i):

    # *****************************************************************************80
    #
    # MORSE_THUE generates a Morse_Thue number.
    #
    #  Discussion:
    #
    #    The Morse_Thue sequence can be defined in a number of ways.
    #
    #    A) Start with the string containing the single letter '0' then
    #       repeatedly apply the replacement rules '0' -> '01' and
    #       '1' -> '10' to the letters of the string.  The Morse_Thue sequence
    #       is the resulting letter sequence.
    #
    #    B) Starting with the string containing the single letter '0',
    #       repeatedly append the binary complement of the string to itself.
    #       Thus, '0' becomes '0' + '1' or '01', then '01' becomes
    #       '01' + '10', which becomes '0110' + '1001', and so on.
    #
    #    C) Starting with I = 0, the I-th Morse-Thue number is determined
    #       by taking the binary representation of I, adding the digits,
    #       and computing the remainder modulo 2.
    #
    #  Example:
    #
    #     I  binary   S
    #    --  ------  --
    #     0       0   0
    #     1       1   1
    #     2      10   1
    #     3      11   0
    #     4     100   1
    #     5     101   0
    #     6     110   0
    #     7     111   1
    #     8    1000   1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, the index of the Morse-Thue number.
    #    Normally, I is 0 or greater, but any value is allowed.
    #
    #    Output, integer S, the Morse-Thue number of index I.
    #

    nbits = 32

    i_copy = abs(i)
#
#  Expand I into binary form.
#
    b = ui4_to_ubvec(i_copy, nbits)
#
#  Sum the 1's in the binary representation.
#
    s = i4vec_sum(nbits, b)
#
#  Take the value modulo 2.
#
    s = (s % 2)

    return s


def morse_thue_test():

    # *****************************************************************************80
    #
    # MORSE_THUE_TEST tests MORSE_THUE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 100

    print('')
    print('MORSE_THUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MORSE_THUE computes the Morse-Thue numbers.')
    print('')

    for i in range(0, n + 1):
        s = morse_thue(i)
        print('  %4d  %d' % (i, s))
#
#  Terminate.
#
    print('')
    print('MORSE_THUE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    morse_thue_test()
    timestamp()
