#! /usr/bin/env python
#
def bernstein ( n ):

#*****************************************************************************80
#
## BERNSTEIN returns the BERNSTEIN matrix.
#
#  Discussion:
#
#    The Bernstein matrix of order N is an NxN matrix A which can be used to
#    transform a vector of power basis coefficients C representing a polynomial 
#    P(X) to a corresponding Bernstein basis coefficient vector B:
#
#      B = A * C
#
#    The N power basis vectors are ordered as (1,X,X^2,...X^(N-1)) and the N 
#    Bernstein basis vectors as ((1-X)^(N-1), X*(1-X)^(N-2),...,X^(N-1)).
#
#  Example:
#
#    N = 5
#
#    1    -4     6    -4     1
#    0     4   -12    12    -4
#    0     0     6   -12     6
#    0     0     0     4    -4
#    0     0     0     0     1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the Bernstein matrix.
#
  import numpy as np
  from r8_choose import r8_choose
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      a[i,j] = r8_mop ( j - i ) * r8_choose ( n - 1 - i, j - i ) \
        * r8_choose ( n - 1, i )

  return a

def bernstein_test ( ):

#*****************************************************************************80
#
## BERNSTEIN_TEST tests BERNSTEIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'BERNSTEIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BERNSTEIN computes the BERNSTEIN matrix.' )

  m = 5
  n = m

  a = bernstein ( n )
 
  r8mat_print ( m, n, a, '  BERNSTEIN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BERNSTEIN_TEST' )
  print ( '  Normal end of execution.' )
  return

def bernstein_determinant ( n ):

#*****************************************************************************80
#
## BERNSTEIN_DETERMINANT returns the determinant of the BERNSTEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  from r8_choose import r8_choose

  value = 1.0
  for i in range ( 0, n ):
    value = value * r8_choose ( n - 1, i )

  return value

def bernstein_inverse ( n ):

#*****************************************************************************80
#
## BERNSTEIN_INVERSE returns the inverse of the BERNSTEIN matrix.
#
#  Discussion:
#
#    The inverse Bernstein matrix of order N is an NxN matrix A which can 
#    be used to transform a vector of Bernstein basis coefficients B
#    representing a polynomial P(X) to a corresponding power basis 
#    coefficient vector C:
#
#      C = A * B
#
#    The N power basis vectors are ordered as (1,X,X^2,...X^(N-1)) and the N 
#    Bernstein basis vectors as ((1-X)^(N-1), X*(1_X)^(N-2),...,X^(N-1)).
#
#  Example:
#
#    N = 5
#
#   1.0000    1.0000    1.0000    1.0000    1.0000
#        0    0.2500    0.5000    0.7500    1.0000
#        0         0    0.1667    0.5000    1.0000
#        0         0         0    0.2500    1.0000
#        0         0         0         0    1.0000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse Bernstein matrix.
#
  import numpy as np
  from r8_choose import r8_choose

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      a[i,j] = r8_choose ( j, i ) / r8_choose ( n - 1, i )

  return a

def bernstein_poly_01 ( n, x ):

#*****************************************************************************80
#
## BERNSTEIN_POLY_01 evaluates the Bernstein polynomials defined on [0,1].
#
#  Discussion:
#
#    The Bernstein polynomials are assumed to be based on [0,1].
#
#  Formula:
#
#    B(N,I)(X) = [N!/(I!*(N-I)!)] * (1-X)^(N-I) * X^I
#
#  First values:
#
#    B(0,0)(X) = 1
#
#    B(1,0)(X) =      1-X
#    B(1,1)(X) =               X
#
#    B(2,0)(X) =     (1-X)^2
#    B(2,1)(X) = 2 * (1-X)   * X
#    B(2,2)(X) =               X^2
#
#    B(3,0)(X) =     (1-X)^3
#    B(3,1)(X) = 3 * (1-X)^2 * X
#    B(3,2)(X) = 3 * (1-X)   * X^2
#    B(3,3)(X) =               X^3
#
#    B(4,0)(X) =     (1-X)^4
#    B(4,1)(X) = 4 * (1-X)^3 * X
#    B(4,2)(X) = 6 * (1-X)^2 * X^2
#    B(4,3)(X) = 4 * (1-X)   * X^3
#    B(4,4)(X) =               X^4
#
#  Special values:
#
#    B(N,I)(X) has a unique maximum value at X = I/N.
#
#    B(N,I)(X) has an I-fold zero at 0 and and N-I fold zero at 1.
#
#    B(N,I)(1/2) = C(N,K) / 2^N
#
#    For a fixed X and N, the polynomials add up to 1:
#
#      Sum ( 0 <= I <= N ) B(N,I)(X) = 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the degree of the Bernstein polynomials to be
#    used.  For any N, there is a set of N+1 Bernstein polynomials,
#    each of degree N, which form a basis for polynomials on [0,1].
#
#    Input, real X, the evaluation point.
#
#    Output, real B[0:N], the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np

  b = np.zeros ( n + 1 )

  if ( n == 0 ):
 
    b[0] = 1.0
 
  elif ( 0 < n ):
 
    b[0] = 1.0 - x
    b[1] = x
 
    for i in range ( 1, n ):
      b[i+1] = x * b[i]
      for j in range ( i - 1, -1, -1 ):
        b[j+1] = x * b[j] + ( 1.0 - x ) * b[j+1]
      b[0] = ( 1.0 - x ) * b[0]

  return b

def bernstein_vandermonde ( n ):

#*****************************************************************************80
#
## BERNSTEIN_VANDERMONDE returns the Bernstein Vandermonde matrix.
#
#  Discussion:
#
#    The Bernstein Vandermonde matrix of order N is constructed by
#    evaluating the N Bernstein polynomials of degree N-1 at N equally
#    spaced points between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the Bernstein Vandermonde matrix.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )

  if ( n == 1 ):
    v[0,0] = 1.0
    return v

  for i in range ( 0, n ):
    x = float ( i ) / float ( n - 1 )
    b = bernstein_poly_01 ( n - 1, x )
    for j in range ( 0, n ):
      v[i,j] = b[j]

  return v

def bernstein_vandermonde_test ( ):

#*****************************************************************************80
#
## BERNSTEIN_VANDERMONDE_TEST tests BERNSTEIN_VANDERMONDE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'BERNSTEIN_VANDERMONDE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BERNSTEIN_VANDERMONDE returns an NxN matrix whose (I,J) entry' )
  print ( '  is the value of the J-th Bernstein polynomial of degree N-1' )
  print ( '  evaluated at the I-th equally spaced point in [0,1].' )

  n = 8
  a = bernstein_vandermonde ( n )
  r8mat_print ( n, n, a, '  Bernstein Vandermonde ( 8 ):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BERNSTEIN_VANDERMONDE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernstein_test ( )
  bernstein_vandermonde_test ( )
  timestamp ( )
