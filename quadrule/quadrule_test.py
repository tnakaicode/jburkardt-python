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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose_print import r8vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from quadrule.bashforth_set import bashforth_set_test
from quadrule.chebyshev_set import chebyshev_set_test
from quadrule.chebyshev1_compute import chebyshev1_compute_test
from quadrule.chebyshev1_integral import chebyshev1_integral_test
from quadrule.chebyshev1_set import chebyshev1_set_test
from quadrule.chebyshev2_compute import chebyshev2_compute_test
from quadrule.chebyshev2_integral import chebyshev2_integral_test
from quadrule.chebyshev2_set import chebyshev2_set_test
from quadrule.chebyshev3_compute import chebyshev3_compute_test
from quadrule.chebyshev3_integral import chebyshev3_integral_test
from quadrule.chebyshev3_set import chebyshev3_set_test
from quadrule.clenshaw_curtis_compute import clenshaw_curtis_compute_test
from quadrule.clenshaw_curtis_set import clenshaw_curtis_set_test
from quadrule.fejer1_compute import fejer1_compute_test
from quadrule.fejer1_set import fejer1_set_test
from quadrule.fejer2_compute import fejer2_compute_test
from quadrule.fejer2_set import fejer2_set_test
from quadrule.gegenbauer_integral import gegenbauer_integral_test
from quadrule.gegenbauer_ss_compute import gegenbauer_ss_compute_test
from quadrule.gen_hermite_ek_compute import gen_hermite_ek_compute_test
from quadrule.gen_hermite_integral import gen_hermite_integral_test
from quadrule.gen_laguerre_ek_compute import gen_laguerre_ek_compute_test
from quadrule.gen_laguerre_integral import gen_laguerre_integral_test
from quadrule.hermite_ek_compute import hermite_ek_compute_test
from quadrule.hermite_integral import hermite_integral_test
from quadrule.hermite_set import hermite_set_test
from quadrule.hermite_gk16_set import hermite_gk16_set_test
from quadrule.hermite_gk18_set import hermite_gk18_set_test
from quadrule.hermite_gk22_set import hermite_gk22_set_test
from quadrule.hermite_gk24_set import hermite_gk24_set_test
from quadrule.hermite_1_set import hermite_1_set_test
from quadrule.hermite_probabilist_set import hermite_probabilist_set_test
from quadrule.hyper_2f1_values import hyper_2f1_values_test
from quadrule.imtqlx import imtqlx_test
from quadrule.jacobi_ek_compute import jacobi_ek_compute_test
from quadrule.jacobi_integral import jacobi_integral_test
from quadrule.kronrod_set import kronrod_set_test
from quadrule.laguerre_ek_compute import laguerre_ek_compute_test
from quadrule.laguerre_integral import laguerre_integral_test
from quadrule.laguerre_set import laguerre_set_test
from quadrule.laguerre_1_set import laguerre_1_set_test
from quadrule.legendre_dr_compute import legendre_dr_compute_test
from quadrule.legendre_ek_compute import legendre_ek_compute_test
from quadrule.legendre_integral import legendre_integral_test
from quadrule.legendre_set import legendre_set_test
from quadrule.lobatto_compute import lobatto_compute_test
from quadrule.lobatto_set import lobatto_set_test
from quadrule.moulton_set import moulton_set_test
from quadrule.nc_compute_weights import nc_compute_weights_test
from quadrule.ncc_compute import ncc_compute_test
from quadrule.ncc_set import ncc_set_test
from quadrule.nco_compute import nco_compute_test
from quadrule.nco_set import nco_set_test
from quadrule.ncoh_compute import ncoh_compute_test
from quadrule.ncoh_set import ncoh_set_test
from quadrule.patterson_set import patterson_set_test
from quadrule.psi_values import psi_values_test
from quadrule.radau_set import radau_set_test


def quadrule_test():

    # *****************************************************************************80
    #
    # QUADRULE_TEST tests the QUADRULE library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('QUADRULE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the QUADRULE library.')

    hyper_2f1_values_test()
    psi_values_test()

    bashforth_set_test()

    chebyshev_set_test()

    chebyshev1_compute_test()
    chebyshev1_integral_test()
    chebyshev1_set_test()

    chebyshev2_compute_test()
    chebyshev2_integral_test()
    chebyshev2_set_test()

    chebyshev3_compute_test()
    chebyshev3_integral_test()
    chebyshev3_set_test()

    clenshaw_curtis_compute_test()
    clenshaw_curtis_set_test()

    fejer1_compute_test()
    fejer1_set_test()

    fejer2_compute_test()
    fejer2_set_test()

    gegenbauer_integral_test()
    gegenbauer_ss_compute_test()

    gen_hermite_ek_compute_test()
    gen_hermite_integral_test()

    gen_laguerre_ek_compute_test()
    gen_laguerre_integral_test()

    hermite_ek_compute_test()
    hermite_integral_test()
    hermite_set_test()
    hermite_gk16_set_test()
    hermite_gk18_set_test()
    hermite_gk22_set_test()
    hermite_gk24_set_test()
    hermite_1_set_test()
    hermite_probabilist_set_test()

    imtqlx_test()

    jacobi_ek_compute_test()
    jacobi_integral_test()

    kronrod_set_test()

    laguerre_ek_compute_test()
    laguerre_integral_test()
    laguerre_set_test()
    laguerre_1_set_test()

    legendre_dr_compute_test()
    legendre_ek_compute_test()
    legendre_integral_test()
    legendre_set_test()

    lobatto_compute_test()
    lobatto_set_test()

    moulton_set_test()

    nc_compute_weights_test()

    ncc_compute_test()
    ncc_set_test()

    nco_compute_test()
    nco_set_test()

    ncoh_compute_test()
    ncoh_set_test()

    patterson_set_test()

    radau_set_test()

    print('')
    print('QUADRULE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    quadrule_test()
    timestamp()
