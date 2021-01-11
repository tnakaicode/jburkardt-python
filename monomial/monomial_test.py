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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from monomial.mono_between_enum import mono_between_enum_test
from monomial.mono_between_next_grevlex import mono_between_next_grevlex_test
from monomial.mono_between_next_grlex import mono_between_next_grlex_test
from monomial.mono_between_random import mono_between_random_test
from monomial.mono_next_grevlex import mono_next_grevlex_test
from monomial.mono_next_grlex import mono_next_grlex_test
from monomial.mono_print import mono_print_test
from monomial.mono_rank_grlex import mono_rank_grlex_test
from monomial.mono_total_enum import mono_total_enum_test
from monomial.mono_total_next_grevlex import mono_total_next_grevlex_test
from monomial.mono_total_next_grlex import mono_total_next_grlex_test
from monomial.mono_total_random import mono_total_random_test
from monomial.mono_unrank_grlex import mono_unrank_grlex_test
from monomial.mono_upto_enum import mono_upto_enum_test
from monomial.mono_upto_next_grevlex import mono_upto_next_grevlex_test
from monomial.mono_upto_next_grlex import mono_upto_next_grlex_test
from monomial.mono_upto_random import mono_upto_random_test
from monomial.mono_value import mono_value_test


def monomial_test():

    # *****************************************************************************80
    #
    # MONOMIAL_TEST tests the MONOMIAL library.
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

    print('')
    print('MONOMIAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the MONOMIAL library.')

    mono_between_enum_test()
    mono_total_enum_test()
    mono_upto_enum_test()
    mono_next_grevlex_test()
    mono_next_grlex_test()
    mono_between_next_grevlex_test()
    mono_between_next_grlex_test()
    mono_total_next_grevlex_test()
    mono_total_next_grlex_test()
    mono_upto_next_grevlex_test()
    mono_upto_next_grlex_test()
    mono_rank_grlex_test()
    mono_unrank_grlex_test()
    mono_between_random_test()
    mono_total_random_test()
    mono_upto_random_test()
    mono_value_test()
    mono_print_test()

    print('')
    print('MONOMIAL_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    monomial_test()
    timestamp()
