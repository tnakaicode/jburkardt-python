#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import platform

sys.path.append(os.path.join('../'))
from pdflib.i4_binomial_pdf import i4_binomial_pdf_test
from pdflib.i4_binomial_sample import i4_binomial_sample_test
from pdflib.i4_uni import i4_uni_test
from pdflib.i4_uniform_ab import i4_uniform_ab_test
from pdflib.i4_uniform_sample import i4_uniform_sample_test
from pdflib.i4vec_multinomial_pdf import i4vec_multinomial_pdf_test
from pdflib.i4vec_multinomial_sample import i4vec_multinomial_sample_test
from pdflib.initialize import initialize
from pdflib.r8_beta_pdf import r8_beta_pdf_test
from pdflib.r8_beta_sample import r8_beta_sample_test
from pdflib.r8_chi_pdf import r8_chi_pdf_test
from pdflib.r8_chi_sample import r8_chi_sample_test
from pdflib.r8_choose import r8_choose_test
from pdflib.r8_exponential_01_pdf import r8_exponential_01_pdf_test
from pdflib.r8_exponential_01_sample import r8_exponential_01_sample_test
from pdflib.r8_exponential_pdf import r8_exponential_pdf_test
from pdflib.r8_exponential_sample import r8_exponential_sample_test
from pdflib.r8_gamma_01_pdf import r8_gamma_01_pdf_test
from pdflib.r8_gamma_01_sample import r8_gamma_01_sample_test
from pdflib.r8_gamma_log import r8_gamma_log_test
from pdflib.r8_gamma_pdf import r8_gamma_pdf_test
from pdflib.r8_gamma_sample import r8_gamma_sample_test
from pdflib.r8_invchi_pdf import r8_invchi_pdf_test
from pdflib.r8_invchi_sample import r8_invchi_sample_test
from pdflib.r8_invgam_pdf import r8_invgam_pdf_test
from pdflib.r8_invgam_sample import r8_invgam_sample_test
from pdflib.r8_normal_01_pdf import r8_normal_01_pdf_test
from pdflib.r8_normal_01_sample import r8_normal_01_sample_test
from pdflib.r8_normal_pdf import r8_normal_pdf_test
from pdflib.r8_normal_sample import r8_normal_sample_test
from pdflib.r8_scinvchi_pdf import r8_scinvchi_pdf_test
from pdflib.r8_scinvchi_sample import r8_scinvchi_sample_test
from pdflib.r8_uni_01 import r8_uni_01_test
from pdflib.r8_uniform_01_pdf import r8_uniform_01_pdf_test
from pdflib.r8_uniform_01_sample import r8_uniform_01_sample_test
from pdflib.r8_uniform_ab import r8_uniform_ab_test
from pdflib.r8_uniform_pdf import r8_uniform_pdf_test
from pdflib.r8_uniform_sample import r8_uniform_sample_test
from pdflib.r8ge import r8ge_print_test
from pdflib.r8ge import r8ge_print_some_test
from pdflib.r8mat_norm_fro_affine import r8mat_norm_fro_affine_test
from pdflib.r8mat_uniform_01 import r8mat_uniform_01_test
from pdflib.r8po import r8po_mv_test
from pdflib.r8ut import r8ut_sl_test
from pdflib.r8vec_indicator1 import r8vec_indicator1_test
from pdflib.r8vec_norm import r8vec_norm_test
from pdflib.r8vec_multinormal_pdf import r8vec_multinormal_pdf_test
from pdflib.r8vec_multinormal_sample import r8vec_multinormal_sample_test
from pdflib.r8vec_print import r8vec_print_test
from pdflib.r8vec_uniform_ab import r8vec_uniform_ab_test


def pdflib_test():

    # *****************************************************************************80
    #
    # PDFLIB_TEST tests the PDFLIB library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PDFLIB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the PDFLIB library.')

    #  Initialize the random number generator package.
    initialize()

    #  Support functions.
    i4_uni_test()
    i4_uniform_ab_test()

    r8_choose_test()
    r8_gamma_log_test()
    r8_uni_01_test()
    r8_uniform_ab_test()

    r8ge_print_test()
    r8ge_print_some_test()

    r8mat_norm_fro_affine_test()
    r8mat_uniform_01_test()

    r8po_mv_test()
    r8ut_sl_test()

    r8vec_indicator1_test()
    r8vec_norm_test()
    r8vec_print_test()
    r8vec_uniform_ab_test()

    #  Library functions.
    i4_binomial_pdf_test()
    i4_binomial_sample_test()

    i4_uniform_sample_test()

    i4vec_multinomial_pdf_test()
    i4vec_multinomial_sample_test()

    r8_beta_pdf_test()
    r8_beta_sample_test()

    r8_chi_pdf_test()
    r8_chi_sample_test()

    r8_exponential_01_pdf_test()
    r8_exponential_01_sample_test()

    r8_exponential_pdf_test()
    r8_exponential_sample_test()

    r8_gamma_01_pdf_test()
    r8_gamma_01_sample_test()

    r8_gamma_pdf_test()
    r8_gamma_sample_test()

    r8_invchi_pdf_test()
    r8_invchi_sample_test()

    r8_invgam_pdf_test()
    r8_invgam_sample_test()

    r8_normal_01_pdf_test()
    r8_normal_01_sample_test()

    r8_normal_pdf_test()
    r8_normal_sample_test()

    r8_scinvchi_pdf_test()
    r8_scinvchi_sample_test()

    r8_uniform_01_pdf_test()
    r8_uniform_01_sample_test()

    r8_uniform_pdf_test()
    r8_uniform_sample_test()

    r8vec_multinormal_pdf_test()
    r8vec_multinormal_sample_test()

    print('')
    print('PDFLIB_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    pdflib_test()
    timestamp()
