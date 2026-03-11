#! /usr/bin/env python3
#
def legendre_shifted_polynomial_test ( ):

#*****************************************************************************80
#
## legendre_shifted_polynomial_test() tests legendre_shifted_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'legendre_shifted_polynomial_test:' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test the legendre_shifted_polynomial library.' )

  p01_polynomial_value_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_shifted_polynomial_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def p01_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## p01_polynomial_value() evaluates the shifted Legendre polynomials p01(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real V(0:M-1,0:N), the values of the shifted Legendre polynomials 
#    of order 0 through N at the points X.
#
  import numpy as np

  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0

  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = 2.0 * x[i] - 1.0

  for j in range ( 2, n + 1 ):

    for i in range ( 0, m ):
 
      v[i,j] = ( ( 2 * j - 1 ) * ( 2.0 * x[i] - 1.0 ) * v[i,j-1]   \
              -  (     j - 1 ) *                        v[i,j-2] ) \
              /  (     j     )

  return v

def p01_polynomial_value_test ( ):

#*****************************************************************************80
#
## p01_polynomial_value_test() tests p01_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 1
  xvec = np.zeros ( m )

  print ( '' )
  print ( 'p01_polynomial_value_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p01_polynomial_value evaluates the shifted Legendre polynomial p01(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X         p01(N,X)                  p01(N,X)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = p01_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x
    v = p01_polynomial_value ( m, n, xvec )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12g  %24g  %24g  %8g' % ( n, x, fx1, fx2, e ) )

  return

def p01_polynomial_values ( n_data ):

#*****************************************************************************80
#
## p01_polynomial_values() returns values of the shifted Legendre polynomials.
#
#  Discussion:
#
#    If we denote the Legendre polynomial by P(n)(x), and the shifted 
#    Legendre polynomial by p01(n)(x), then
#
#      p01(n)(x) = P(n)(2*x-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Input:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.2500000000000000E+00, \
     -0.4062500000000000E+00, \
     -0.3359375000000000E+00, \
      0.1577148437500000E+00, \
      0.3397216796875000E+00, \
      0.2427673339843750E-01, \
     -0.2799186706542969E+00, \
     -0.1524540185928345E+00, \
      0.1768244206905365E+00, \
      0.2212002165615559E+00, \
      0.0000000000000000E+00, \
     -0.1475000000000000E+00, \
     -0.2800000000000000E+00, \
     -0.3825000000000000E+00, \
     -0.4400000000000000E+00, \
     -0.4375000000000000E+00, \
     -0.3600000000000000E+00, \
     -0.1925000000000000E+00, \
      0.8000000000000000E-01, \
      0.4725000000000000E+00, \
      0.1000000000000000E+01 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3 ))

  x_vec = np.array ( ( \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.50E+00, \
     0.55E+00, \
     0.60E+00, \
     0.65E+00, \
     0.70E+00, \
     0.75E+00, \
     0.80E+00, \
     0.85E+00, \
     0.90E+00, \
     0.95E+00, \
     1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def p01_polynomial_values_test ( ):

#*****************************************************************************80
#
## p01_polynomial_values_test() tests p01_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p01_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p01_polynomial_values stores values of the shifted Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = p01_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12g  %24.16g' % ( n, x, f ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  legendre_shifted_polynomial_test ( )
  timestamp ( )
 
