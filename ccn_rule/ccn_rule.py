#! /usr/bin/env python3
#
def ccn_rule_test ( ):

#*****************************************************************************80
#
## ccn_rule_test() tests ccn_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ccn_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ccn_rule().' )

  n = 9
  a = -1.0
  b = +1.0
  filename = 'ccn_o9'

  ccn_rule ( n, a, b, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'ccn_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def ccn_rule ( n, a, b, filename ):

#*****************************************************************************80
#
## ccn_rule() generates a nested Clenshaw Curtis rule.
#
#  Discussion:
#
#    This program computes a nested Clenshaw Curtis quadrature rule
#    and writes it to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points in the rule
#
#    real A, the left endpoint
#
#    real B, the right endpoint
#
#    character FILENAME, the root name of the output files.
#
  import numpy as np

  print ( '' )
  print ( 'ccn_rule():' )
  print ( '  Compute a nested Clenshaw Curtis rule for approximating' )
  print ( '    Integral ( A <= x <= B ) f(x) dx' )
  print ( '  of order N.' )
  print ( '' )
  print ( '  The user specifies N, A, B, and FILENAME.' )
  print ( '' )
  print ( '  N is the number of points:' )
  print ( '  A is the left endpoint' )
  print ( '  B is the right endpoint' )
  print ( '  FILENAME is used to generate 3 files:' )
  print ( '' )
  print ( '    filename_w.txt - the weight file' )
  print ( '    filename_x.txt - the abscissa file.' )
  print ( '    filename_r.txt - the region file.' )
#
#  Input summary.
#
  print ( '' )
  print ( '  N = ', n )
  print ( '  A = ', a )
  print ( '  B = ', b )
  print ( '  FILENAME = "' + filename + '".' )
#
#  Construct the rule for [-1,+1]
#
  r = np.array ( [ a, b ] )

  x = ccn_compute_points ( n )

  x_min = -1.0
  x_max = +1.0

  w = nc_compute ( n, x_min, x_max, x )
#
#  Rescale the rule to [A,B].
#
  x = 0.5 * ( ( x + 1.0 ) * b - ( x - 1.0 ) * a )

  w = 0.5 * ( b - a ) * w
#
#  Write the rule.
#
  filename_x = filename + '_x.txt'
  np.savetxt ( filename_x, x )
  print ( '  Abscissas saved as "' + filename_x + '"' )
  filename_w = filename + '_w.txt'
  np.savetxt ( filename_w, w )
  print ( '  Weights saved as "' + filename_w + '"' )
  filename_r = filename + '_r.txt'
  np.savetxt ( filename_r, r )
  print ( '  Region saved as ""' + filename_r + '"' )

  return

def ccn_compute_points ( n ):

#*****************************************************************************80
#
## ccn_compute_points(): compute Clenshaw Curtis Nested points.
#
#  Discussion:
#
#    We want to compute the following sequence:
#
#    1/2,
#    0, 1
#    1/4, 3/4
#    1/8, 3/8, 5/8, 7/8,
#    1/16, 3/16, 5/16, 7/16, 9/16, 11/16, 13/16, 15/16, and so on.
#
#    But we'd prefer that the numbers in each row be regrouped in pairs
#    that are symmetric about 1/2, with the number above 1/2 coming first.
#    Thus, the last row might become:
#    (9/16, 7/16), (11/16, 5/16), ..., (15/16, 1/16).
#
#    Once we have our sequence, we apply the Chebyshev transformation
#    which maps [0,1] to [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements to compute.
#
#  Output:
#
#    real X(N), the elements of the sequence.
#
  import numpy as np

  x = np.zeros ( n )
#
#  Handle first three entries specially.
#
  if ( 1 <= n ):
    x[0] = 0.5

  if ( 2 <= n ):
    x[1] = 1.0

  if ( 3 <= n ):
    x[2] = 0.0

  m = 3
  d = 2

  while ( m < n ):

    tu = np.arange ( d + 1, 2 * d + 1, 2 )
    td = np.arange ( d - 1, 0, -2 )
    t = np.concatenate ( [ tu, td ] )
    k = min ( d, n - m )
    x[m:m+k] = t[0:k] / d / 2.0
    m = m + k
    d = d * 2
#
#  Apply the Chebyshev transformation.
#
  x = np.cos ( x * np.pi )

  x[0] = 0.0
  if ( 1 <= n ):
    x[1] = -1.0
  if ( 2 <= n ):
    x[2] = +1.0

  return x

def nc_compute ( n, x_min, x_max, x ):

#*****************************************************************************80
#
## nc_compute() computes a Newton-Cotes quadrature rule.
#
#  Discussion:
#
#    For the interval [X_MIN,X_MAX], the Newton-Cotes quadrature rule
#    estimates
#
#      Integral ( X_MIN <= X <= X_MAX ) F(X) dX
#
#    using N abscissas X and weights W:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the CLOSED rule, the equally spaced abscissas include A and B.
#    For the OPEN rule, the equally spaced abscissas do not include A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#
#    real X_MIN, X_MAX, the endpoints of the interval.
#
#    real X(N), the abscissas.
#
#  Output:
#
#    real W(N,1), the weights.
#
  import numpy as np

  d = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Compute the Lagrange basis polynomial which is 1 at X(I),
#  and zero at the other nodes.
#
    d = np.zeros ( n )
    d[i] = 1.0

    for j in range ( 2, n + 1 ):
      for k in range ( j, n + 1 ):
        d[n+j-k-1] = ( d[n+j-k-1-1] - d[n+j-k-1] ) / ( x[n+1-k-1] - x[n+j-k-1] )

    for j in range ( 1, n ):
      for k in range ( 1, n - j + 1):
        d[n-k-1] = d[n-k-1] - x[n-k-j+1-1] * d[n-k+1-1]
#
#  Evaluate the antiderivative of the polynomial at the endpoints.
#
    yvala = d[n-1] / n
    for j in range ( n - 2, -1, -1 ):
      yvala = yvala * x_min + d[j] / ( j + 1 )
    yvala = yvala * x_min

    yvalb = d[n-1] / n
    for j in range ( n - 2, -1, -1 ):
      yvalb = yvalb * x_max + d[j] / ( j + 1 )

    yvalb = yvalb * x_max

    w[i] = yvalb - yvala

  return w

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
  ccn_rule_test ( )
  timestamp ( )


