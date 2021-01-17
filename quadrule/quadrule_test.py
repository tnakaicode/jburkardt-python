#! /usr/bin/env python3
#
def quadrule_test ( ):

#*****************************************************************************80
#
## QUADRULE_TEST tests the QUADRULE library.
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
  import platform

  from bashforth_set            import bashforth_set_test
  from chebyshev_set            import chebyshev_set_test
  from chebyshev1_compute       import chebyshev1_compute_test
  from chebyshev1_integral      import chebyshev1_integral_test
  from chebyshev1_set           import chebyshev1_set_test
  from chebyshev2_compute       import chebyshev2_compute_test
  from chebyshev2_integral      import chebyshev2_integral_test
  from chebyshev2_set           import chebyshev2_set_test
  from chebyshev3_compute       import chebyshev3_compute_test
  from chebyshev3_integral      import chebyshev3_integral_test
  from chebyshev3_set           import chebyshev3_set_test
  from clenshaw_curtis_compute  import clenshaw_curtis_compute_test
  from clenshaw_curtis_set      import clenshaw_curtis_set_test
  from fejer1_compute           import fejer1_compute_test
  from fejer1_set               import fejer1_set_test
  from fejer2_compute           import fejer2_compute_test
  from fejer2_set               import fejer2_set_test
  from gegenbauer_integral      import gegenbauer_integral_test
  from gegenbauer_ss_compute    import gegenbauer_ss_compute_test
  from gen_hermite_ek_compute   import gen_hermite_ek_compute_test
  from gen_hermite_integral     import gen_hermite_integral_test
  from gen_laguerre_ek_compute  import gen_laguerre_ek_compute_test
  from gen_laguerre_integral    import gen_laguerre_integral_test
  from hermite_ek_compute       import hermite_ek_compute_test
  from hermite_integral         import hermite_integral_test
  from hermite_set              import hermite_set_test
  from hermite_gk16_set         import hermite_gk16_set_test
  from hermite_gk18_set         import hermite_gk18_set_test
  from hermite_gk22_set         import hermite_gk22_set_test
  from hermite_gk24_set         import hermite_gk24_set_test
  from hermite_1_set            import hermite_1_set_test
  from hermite_probabilist_set  import hermite_probabilist_set_test
  from hyper_2f1_values         import hyper_2f1_values_test
  from imtqlx                   import imtqlx_test
  from jacobi_ek_compute        import jacobi_ek_compute_test
  from jacobi_integral          import jacobi_integral_test
  from kronrod_set              import kronrod_set_test
  from laguerre_ek_compute      import laguerre_ek_compute_test
  from laguerre_integral        import laguerre_integral_test
  from laguerre_set             import laguerre_set_test
  from laguerre_1_set           import laguerre_1_set_test
  from legendre_dr_compute      import legendre_dr_compute_test
  from legendre_ek_compute      import legendre_ek_compute_test
  from legendre_integral        import legendre_integral_test
  from legendre_set             import legendre_set_test
  from lobatto_compute          import lobatto_compute_test
  from lobatto_set              import lobatto_set_test
  from moulton_set              import moulton_set_test
  from nc_compute_weights       import nc_compute_weights_test
  from ncc_compute              import ncc_compute_test
  from ncc_set                  import ncc_set_test
  from nco_compute              import nco_compute_test
  from nco_set                  import nco_set_test
  from ncoh_compute             import ncoh_compute_test
  from ncoh_set                 import ncoh_set_test
  from patterson_set            import patterson_set_test
  from psi_values               import psi_values_test
  from r8_epsilon               import r8_epsilon_test
  from r8_factorial             import r8_factorial_test
  from r8_factorial2            import r8_factorial2_test
  from r8_gamma                 import r8_gamma_test
  from r8_huge                  import r8_huge_test
  from r8_hyper_2f1             import r8_hyper_2f1_test
  from r8_psi                   import r8_psi_test
  from r8vec_diff_norm_li       import r8vec_diff_norm_li_test
  from r8vec_indicator1         import r8vec_indicator1_test
  from r8vec_linspace           import r8vec_linspace_test
  from r8vec_print              import r8vec_print_test
  from r8vec_reverse            import r8vec_reverse_test
  from r8vec_uniform_ab         import r8vec_uniform_ab_test
  from radau_set                import radau_set_test
  from timestamp                import timestamp_test

  print ( '' )
  print ( 'QUADRULE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the QUADRULE library.' )
#
#  Utility functions:
#
  hyper_2f1_values_test ( )
  psi_values_test ( )
  r8_epsilon_test ( )
  r8_factorial_test ( )
  r8_factorial2_test ( )
  r8_gamma_test ( )
  r8_huge_test ( )
  r8_hyper_2f1_test ( )
  r8_psi_test ( )
  r8vec_diff_norm_li_test ( )
  r8vec_indicator1_test ( )
  r8vec_linspace_test ( )
  r8vec_print_test ( )
  r8vec_reverse_test ( )
  r8vec_uniform_ab_test ( )
#
#  Library functions:
#
  bashforth_set_test ( )

  chebyshev_set_test ( )

  chebyshev1_compute_test ( )
  chebyshev1_integral_test ( )
  chebyshev1_set_test ( )

  chebyshev2_compute_test ( )
  chebyshev2_integral_test ( )
  chebyshev2_set_test ( )

  chebyshev3_compute_test ( )
  chebyshev3_integral_test ( )
  chebyshev3_set_test ( )

  clenshaw_curtis_compute_test ( )
  clenshaw_curtis_set_test ( )

  fejer1_compute_test ( )
  fejer1_set_test ( )

  fejer2_compute_test ( )
  fejer2_set_test ( )

  gegenbauer_integral_test ( )
  gegenbauer_ss_compute_test ( )

  gen_hermite_ek_compute_test ( )
  gen_hermite_integral_test ( )

  gen_laguerre_ek_compute_test ( )
  gen_laguerre_integral_test ( )

  hermite_ek_compute_test ( )
  hermite_integral_test ( )
  hermite_set_test ( )
  hermite_gk16_set_test ( )
  hermite_gk18_set_test ( )
  hermite_gk22_set_test ( )
  hermite_gk24_set_test ( )
  hermite_1_set_test ( )
  hermite_probabilist_set_test ( )

  imtqlx_test ( )

  jacobi_ek_compute_test ( )
  jacobi_integral_test ( )

  kronrod_set_test ( )

  laguerre_ek_compute_test ( )
  laguerre_integral_test ( )
  laguerre_set_test ( )
  laguerre_1_set_test ( )

  legendre_dr_compute_test ( )
  legendre_ek_compute_test ( )
  legendre_integral_test ( )
  legendre_set_test ( )

  lobatto_compute_test ( )
  lobatto_set_test ( )

  moulton_set_test ( )

  nc_compute_weights_test ( )

  ncc_compute_test ( )
  ncc_set_test ( )

  nco_compute_test ( )
  nco_set_test ( )

  ncoh_compute_test ( )
  ncoh_set_test ( )

  patterson_set_test ( )

  radau_set_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'QUADRULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  quadrule_test ( )
  timestamp ( )
