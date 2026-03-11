#! /usr/bin/env python3
#
def newton_maehly_test ( ):

#*****************************************************************************80
#
## newton_maehly_test() tests newton_maehly().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'newton_maehly_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  newton_maehly() uses the Newton-Maehly algorithm' )
  print ( '  to compute all roots of a polynomial.' )

  newton_maehly_test01 ( )

  print ( '' )
  print ( 'newton_maehly_test():' )
  print ( '  Normal end of execution.' )

  return

def newton_maehly_test01 ( ):

#*****************************************************************************80
#
## newton_maehly_test01() considers degree 4 polynomial with a complex pair of roots.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2026
#
#  Author:
#
#    John Burkardt
#
  from cmath import sqrt
  import numpy as np
  import pprint

  print ( '' )
  print ( 'newton_maehly_test01():' )
  print ( '  Try newton_maehly() on a degree four polynomial with a pair of complex roots.' )

  c = np.array ( [ -56.0, -75.0, -26.0, 0.0, 1.0 ] )

  print ( '' )
  poly_print ( c, '  Polynomial to be analyzed:' )

  roots = newton_maehly ( c )

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

def newton_maehly ( c, tol = 1e-12, maxiter = 100 ):

#*****************************************************************************80
#
## newton_maehly() applies the Newton-Maehly algorithm to a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2026
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
#    real tol: convergence tolerance.
#
#    integer maxiter: maximum number of iterations
#
#  Output:
#
#    complex z[d]: the roots.
#
  import numpy as np

  d = len ( c ) - 1
#
#  Cauchy bound for root norms.
#
  R = 1.0 + np.max ( np.abs ( c[0:d] / c[d] ) )
#
#  Initial guess: roots of unity scaled by R
#
  theta = np.linspace ( 0.0, 2.0 * np.pi, d + 1 )
  z0 = R * np.exp ( theta[0:d] * 1j )

  c = np.asarray ( c, dtype = complex )
  z = np.asarray ( z0, dtype = complex )

  for it in range ( maxiter ):
    z_old = z.copy()

    for k in range ( d ):
      pz, dpz = poly_and_derivative ( c, z[k] )
      s = 0.0
      for j in range ( d ):
        if ( j != k ):
          s = s + 1.0 / ( z[k] - z[j] )

      denom = dpz - pz * s

      if ( denom == 0.0 ):
        raise ZeroDivisionError("Zero denominator encountered.")

      z[k] = z[k] - pz / denom

    if ( np.linalg.norm ( z - z_old, ord = np.inf ) < tol ):
      return z

  raise RuntimeError("Newton-Maehly did not converge")

  return

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
  newton_maehly_test ( )
  timestamp ( )

