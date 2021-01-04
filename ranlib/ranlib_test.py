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


def ranlib_test():

    # *****************************************************************************80
    #
    # RANLIB_TEST tests the RANLIB library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    from ranlib.genbet import genbet_test
    from ranlib.genchi import genchi_test
    from ranlib.genexp import genexp_test
    from ranlib.genf import genf_test
    from ranlib.gengam import gengam_test
    from ranlib.genmn import genmn_test
    from ranlib.genmul import genmul_test
    from ranlib.gennch import gennch_test
    from ranlib.gennf import gennf_test
    from ranlib.gennor import gennor_test
    from ranlib.genprm import genprm_test
    from ranlib.genunf import genunf_test
    from ranlib.ignbin import ignbin_test
    from ranlib.ignnbn import ignnbn_test
    from ranlib.ignpoi import ignpoi_test
    from ranlib.ignuin import ignuin_test
    #from ranlib.initialize import initialize
    from ranlib.lennob import lennob_test
    from ranlib.low_level_test import low_level_test
    from ranlib.phrtsd import phrtsd_test
    from ranlib.prcomp import prcomp_test
    from ranlib.r4_exp import r4_exp_test
    from ranlib.r4_exponential_sample import r4_exponential_sample_test
    from ranlib.r4vec_covariance import r4vec_covariance_test
    from ranlib.r8_exponential_sample import r8_exponential_sample_test
    from ranlib.r8vec_covariance import r8vec_covariance_test
    from ranlib.setcov import setcov_test
    from ranlib.sexpo import sexpo_test
    from ranlib.sgamma import sgamma_test
    from ranlib.snorm import snorm_test
    from ranlib.spofa import spofa_test
    from ranlib.stats import stats_test
    from ranlib.trstat import trstat_test

    phrase = 'Randomizer'

    # initialize()

    print('')
    print('RANLIB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the RANLIB library.')

    genbet_test(phrase)
    genchi_test(phrase)
    genexp_test(phrase)
    genf_test(phrase)
    gengam_test(phrase)
    genmn_test(phrase)
    genmul_test(phrase)
    gennch_test(phrase)
    gennf_test(phrase)
    gennor_test(phrase)
    genprm_test(phrase)
    genunf_test(phrase)
    ignbin_test(phrase)
    ignnbn_test(phrase)
    ignpoi_test(phrase)
    ignuin_test(phrase)
    lennob_test()
    low_level_test()
    phrtsd_test()
    prcomp_test()
    r4_exp_test()
    r4_exponential_sample_test()
    r4vec_covariance_test()
    r8_exponential_sample_test()
    r8vec_covariance_test()
    setcov_test()
    sexpo_test()
    sgamma_test()
    snorm_test()
    spofa_test()
    stats_test()
    trstat_test()

    print('')
    print('RANLIB_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    ranlib_test()
    timestamp()
