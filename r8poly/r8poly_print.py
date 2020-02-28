#! /usr/bin/env python3
#
def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## R8POLY_PRINT prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
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
#    Input, integer M, the nominal degree of the polynomial.
#
#    Input, real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    Input, string TITLE, a title.
#
  from r8vec_is_zero import r8vec_is_zero

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( r8vec_is_zero ( m + 1, a ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) = ', end = '' ),
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False
      else:
        print ( '         ', end = '' ),

      if ( 2 <= i ):
        print ( '  %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '  %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '  %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## R8POLY_PRINT_TEST tests R8POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8POLY_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_PRINT prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_PRINT_TEST:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_print_test ( )
  timestamp ( )
