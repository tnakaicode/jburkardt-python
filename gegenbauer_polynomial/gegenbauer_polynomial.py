#! /usr/bin/env python3
#
def gegenbauer_polynomial_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_POLYNOMIAL_TEST tests the GEGENBAUER_POLYNOMIAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  from gegenbauer_alpha_check           import gegenbauer_alpha_check_test
  from gegenbauer_ek_compute            import gegenbauer_ek_compute_test
  from gegenbauer_integral              import gegenbauer_integral_test
  from gegenbauer_polynomial_value      import gegenbauer_polynomial_value_test
  from gegenbauer_ss_compute            import gegenbauer_ss_compute_test

  from imtqlx                           import imtqlx_test

  from r8_gamma                         import r8_gamma_test
  from r8_hyper_2f1                     import r8_hyper_2f1_test
  from r8_psi                           import r8_psi_test
  from r8_uniform_ab                    import r8_uniform_ab_test

  print ( '' )
  print ( 'GEGENBAUER_POLYNOMIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the GEGENBAUER_POLYNOMIAL library.' )

  gegenbauer_alpha_check_test ( )
  gegenbauer_ek_compute_test ( )
  gegenbauer_integral_test ( )
  gegenbauer_polynomial_value_test ( )
  gegenbauer_ss_compute_test ( )

  imtqlx_test ( )

  r8_gamma_test ( )
  r8_hyper_2f1_test ( )
  r8_psi_test ( )
  r8_uniform_ab_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gegenbauer_polynomial_test ( )
  timestamp ( )
