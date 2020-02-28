#! /usr/bin/env python3
#
def gegenbauer_alpha_check ( alpha ):

#*****************************************************************************80
#
## GEGENBAUER_ALPHA_CHECK checks the value of ALPHA.
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
#  Parameters:
#
#    Input, real ALPHA, a parameter which is part of the definition of
#    the Gegenbauer polynomials.  It must be greater than -0.5.
#
#    Output, integer CHECK.
#    TRUE, ALPHA is acceptable.
#    FALSE, ALPHA is not acceptable. 
#
  squawk = False

  if ( -0.5 < alpha ):
    check = True
  else:
    check = False

    if ( squawk ):
      print ( '' )
      print ( 'GEGENBAUER_POLYNOMIAL_VALUE - Fatal error!' )
      print ( '  Illegal value of ALPHA.' )
      print ( '  ALPHA = %g' % ( alpha ) )
      print ( '  but ALPHA must be greater than -0.5.' )

  return check

def gegenbauer_alpha_check_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_ALPHA_CHECK_TEST compares GEGENBAUER_ALPHA_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'GEGENBAUER_ALPHA_CHECK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_ALPHA_CHECK checks that ALPHA is legal;' )
  print ( '' )
  print ( '       ALPHA       Check?' )
  print ( '' )

  seed = 123456789

  for n in range ( 0, 10 ):

    alpha, seed = r8_uniform_ab ( -5.0, +5.0, seed )
    check = gegenbauer_alpha_check ( alpha )
    print ( '  %10.4f       %5s' % ( alpha, check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_ALPHA_CHECK_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gegenbauer_alpha_check_test ( )
  timestamp ( )

