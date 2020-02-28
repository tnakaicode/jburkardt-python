#! /usr/bin/env python3
#
def r82poly2_print ( a, b, c, d, e, f ):

#*****************************************************************************80
#
## R82POLY2_PRINT prints a second order polynomial in two variables.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, D, E, F, the coefficients.
#
  print ( '  p(x,y) = %g * x^2 + %g * y^2 + %g * xy' % ( a, b, c ) )
  print ( '         + %g * x + %g * y + %g' % ( d, e, f ) )

  return

def r82poly2_print_test ( ):

#*****************************************************************************80
#
## R82POLY2_PRINT_TEST tests R82POLY2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R82POLY2_PRINT_TEST' )
  print ( '  R82POLY2_PRINT prints an R82POLY2,' )
  print ( '  a quadratic polynomial in x and y.' )

  a = 1.0
  b = 2.0
  c = 3.0
  d = 4.0
  e = 5.0
  f = 6.0

  print ( '' )
  print ( '  Coefficients a, b, c, d, e, f:' )
  print ( '  %g  %g  %g  %g  %g  %g' % ( a, b, c, d, e, f ) )
  print ( '' )

  r82poly2_print ( a, b, c, d, e, f  )
#
#  Terminate.
#
  print ( '' )
  print ( 'R82POLY2_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r82poly2_print_test ( )
  timestamp ( )

