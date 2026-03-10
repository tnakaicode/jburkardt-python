#! /usr/bin/env python3
#
import cmath

def aberth_test ( ):

#*****************************************************************************80
#
## aberth_test() tests aberth().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'aberth_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  aberth() uses the Aberth-Ehrlich algorithm' )
  print ( '  to compute all roots of a polynomial.' )

  aberth_test01 ( )

  print ( '' )
  print ( 'aberth_test():' )
  print ( '  Normal end of execution.' )

  return

def aberth_test01 ( ):

#*****************************************************************************80
#
## aberth_test01() considers degree 4 polynomial with a complex pair of roots.
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
  print ( 'aberth_test01():' )
  print ( '  Try aberth() on a degree four polynomial with a pair of complex roots.' )

  c = np.array ( [ -56.0, -75.0, -26.0, 0.0, 1.0 ] )

  print ( '' )
  poly_print ( c, '  Polynomial to be analyzed:' )

  roots = aberth ( c )

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

def poly_and_derivative ( c, z ):

#*****************************************************************************80
#
## poly_and_derivative() evaluates a polynomial and its derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 January 2026
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
#    complex p, dp: the polynomial and derivative value at z.
#
  d = len ( c ) - 1

  p = 0.0 + 0.0j
  dp = 0.0 + 0.0j
  for i in range ( d, -1, -1 ):
    dp = dp * z + p
    p =  p * z + c[i]

  return p, dp

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

def aberth ( c, max_iter=100, tol=1e-12 ):

#*****************************************************************************80
#
## aberth() applies the Aberth-Ehrlich algorithm for polynomial roots.
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

  c = np.asarray ( c, dtype = complex )
  d = len ( c ) - 1
#
#  Compute Cauchy bound for maximum root norm.
#
  radius = 1.0 + max ( abs ( c[0:d] / c[d] ) )
#
#  First estimate is scaled roots of unity.
#
  roots = radius * np.exp ( 2j * np.pi * np.arange ( d ) / d )
#
#  Repeatedly apply the mapping.
#
  if ( verbose ):
    print ( '' )
    print ( '  Iter  Change  ||Poly||' )
    print ( '' )

  for iter in range ( max_iter ):
    roots_old = roots.copy()

    for i in range ( d ):
      zi = roots[i]
      p, dp = poly_and_derivative ( c, zi )

      if ( abs ( p ) < tol ):
        continue
#
#  Aberth correction
#
      sum_term = 0.0
      for j in range ( d ):
        if ( j != i ):
          sum_term = sum_term + 1.0 / ( zi - roots[j] )

      delta = p / dp
      roots[i] = zi - delta / ( 1.0 - delta * sum_term )
#
#  Convergence check
#
    p, dp = poly_and_derivative ( c, roots )

    max_poly = np.max ( abs ( p ) )
    max_change = np.max ( np.abs ( roots - roots_old ) )

    if ( verbose ):
      print ( '  %4d  %11.5g  %11.5g' % ( iter, max_change, max_poly ) )

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
  aberth_test ( )
  timestamp ( )

