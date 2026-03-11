#! /usr/bin/env python3
#
def wdk_test ( ):

#*****************************************************************************80
#
## wdk_test() tests wdk().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'wdk_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  wdk() uses the Weierstass-Durand-Kerner algorithm' )
  print ( '  to compute all roots of a polynomial.' )

  wdk_test01 ( )

  return

def wdk_test01 ( ):

#*****************************************************************************80
#
## wdk_test01() considers degree 4 polynomial with a complex pair of roots.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2026
#
#  Author:
#
#    John Burkardt
#
  from cmath import sqrt
  import numpy as np
  import pprint

  print ( '' )
  print ( 'wdk_test01():' )
  print ( '  Try wdk() on a degree four polynomial with a pair of complex roots.' )

  c = np.array ( [ -56.0, -75.0, -26.0, 0.0, 1.0 ] )

  print ( '' )
  poly_print ( c, '  Polynomial to be analyzed:' )

  roots = wdk ( c )

  print ( '' )
  print ( '  Computed roots:' )
  print ( '' )
  pprint.pprint ( roots )

  exact = np.array ( [ \
    0.5 * (   5.0 + sqrt ( 57.0 ) ), \
    0.5 * (   5.0 - sqrt ( 57.0 ) ), \
    0.5 * ( - 5.0 + sqrt ( -3.0 ) ), \
    0.5 * ( - 5.0 - sqrt ( -3.0 ) ) ] )
  print ( '' )
  print ( '  Exact roots:' )
  print ( '' )
  pprint.pprint ( exact )

  return

def poly_eval ( c, z ):

#*****************************************************************************80
#
## poly_eval() evaluates a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex c[d+1]: the polynomial coefficients.  c[0] is the constant term
#    and c[d] is the coefficients of x**d.
#
#    complex z: the evaluation point.
#
#  Output:
#
#    complex p: the polynomial value at z.
#
  import numpy as np

  d = len ( c ) - 1

  p = np.zeros_like ( z )
  for i in range ( d, -1, -1 ):
    p = p * z + c[i]

  return p

def poly_print ( a, title ):

#*****************************************************************************80
#
## poly_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  import numpy as np

  m = len ( a ) - 1

  print ( title )

  if ( np.all ( a == 0.0 ) ):
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
        print ( '  p(x) =', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False

      if ( 2 <= i ):
        print ( ' %c %g * x^%d' % ( plus_minus, mag, i ), end = '' )
      elif ( i == 1 ):
        print ( ' %c %g * x' % ( plus_minus, mag ), end = '' )
      elif ( i == 0 ):
        print ( ' %c %g' % ( plus_minus, mag ), end = '' )

  print ( '' )

  return

def wdk ( c, tol = 1e-12, max_iter = 1000 ):

#*****************************************************************************80
#
## wdk() applies the Weierstrass-Durand-Kerner algorithm for polynomial roots.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex c[d+1]: the polynomial coefficients.  c[0] is the constant.
#
#  Output:
#
#    complex roots[d]: the computed roots.
#
  import numpy as np

  verbose = True

  d = len ( c ) - 1
#
#  Cauchy bound for initial radius
#
  R = 1.0 + np.max ( np.abs ( c[0:d] / c[d] ) )
#
#  Initial guess: roots of unity scaled by R
#
  theta = np.linspace ( 0.0, 2.0 * np.pi, d + 1 )
  roots = R * np.exp ( theta[0:d] * 1j )
#
#  Repeatedly apply the mapping.
#
  if ( verbose ):
    print ( '' )
    print ( '  Iter  Change  ||Poly(root)||' )
    print ( '' )

  for iter in range ( max_iter ):

    roots_old = roots.copy ( )

    for i in range ( d ):
      zi = roots_old[i]
      denom = 1.0
      for j in range ( d ):
        if ( i != j ):
          denom = denom * ( zi - roots[j] )

      roots[i] = zi - poly_eval ( c, zi ) / denom

    max_change = np.max ( np.abs ( roots - roots_old ) )
    max_poly = np.max ( np.abs ( poly_eval ( c, roots ) ) )
#
#  Optional report.
#
    if ( verbose ):
      print ( '  %4d  %11.5g  %11.5g' % ( iter, max_change, max_poly ) )
#
#  Exit the loop if the roots haven't changed much.
#
    if ( max_change < tol ):
      break

  return roots

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  wdk_test ( )
  timestamp ( )

