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

from sftpack.c8mat_sft import c8mat_sft_test
from sftpack.c8vec_sft import c8vec_sft_test
from sftpack.r8vec_sct import r8vec_sct_test
from sftpack.r8vec_sft import r8vec_sft_test
from sftpack.r8vec_sht import r8vec_sht_test
from sftpack.r8vec_sqct import r8vec_sqct_test
from sftpack.r8vec_sqst import r8vec_sqst_test
from sftpack.r8vec_sst import r8vec_sst_test
from sftpack.r8vec_swt import r8vec_swt_test


def sftpack_test():

    # *****************************************************************************80
    #
    # SFTPACK_TEST tests the SFTPACK library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SFTPACK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SFTPACK library.')

    c8mat_sft_test()
    c8vec_sft_test()

    r8vec_sct_test()
    r8vec_sft_test()
    r8vec_sht_test()
    r8vec_sqct_test()
    r8vec_sqst_test()
    r8vec_sst_test()
    r8vec_swt_test()

    print('')
    print('SFTPACK_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    sftpack_test()
    timestamp()
