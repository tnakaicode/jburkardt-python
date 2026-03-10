#! /usr/bin/env python3
#
def clenshaw_curtis_rule_test ( ):

#*****************************************************************************80
#
## clenshaw_curtis_rule_test() tests clenshaw_curtis_rule().
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
  print ( 'clenshaw_curtis_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test clenshaw_curtis_rule().' )

  n = 5
  a = -1.0
  b = +1.0
  filename = 'cc_o5'

  clenshaw_curtis_rule ( n, a, b, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'clenshaw_curtis_rule_test()' )
  print ( '  Normal end of execution.' )

  return

def clenshaw_curtis_rule ( n, a, b, filename ):

#*****************************************************************************80
#
## clenshaw_curtis_rule() generates a Clenshaw Curtis quadrature rule.
#
#  Discussion:
#
#    This code computes a standard Clenshaw Curtis quadrature rule
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
#    real A, B, the endpoints
#
#    character FILENAME, the root name of the output files.
#
  import numpy as np

  print ( '' )
  print ( 'clenshaw_curtis_rule():' )
  print ( '  Compute a Clenshaw Curtis rule for approximating' )
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
#  Construct the rule and output it.
#
  xi, rho = clenshaw_curtis_m1p1 ( n )

  x = 0.5 * ( ( xi + 1.0 ) * b - ( xi - 1.0 ) * a )
  w = 0.5 * ( b - a ) * rho
  r = np.array ( [ a, b ] )
#
#  Write the rule.
#
  filename_x = filename + '_x.txt'
  np.savetxt ( filename_x, x )
  print ( '  abscissas saved to "' + filename_x + '"' )
  filename_w = filename + '_w.txt'
  np.savetxt ( filename_w, w )
  print ( '  weights saved to "' + filename_w + '"' )
  filename_r = filename + '_r.txt'
  np.savetxt ( filename_r, r )
  print ( '  region saved to "' + filename_r + '"' )

  return

def clenshaw_curtis_m1p1 ( n ):

#*****************************************************************************80
#
## clenshaw_curtis_m1p1() computes a Clenshaw Curtis quadrature rule for [-1,+1].
#
#  Discussion:
#
#    Our convention is that the abscissas are numbered from left to right.
#
#    The rule is defined on [-1,1].
#
#    The integral to approximate:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of the rule.  1 <= N.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  w = np.zeros ( n )
  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = 0.0
    w[0] = 2.0
    return x, w

  for i in range ( 0, n ):
    x[i] = np.cos ( ( n - i - 1 ) * np.pi / ( n - 1 ) )

  w = np.ones ( n )

  for i in range ( 0, n ):

    theta = i * np.pi / ( n - 1 )

    jhi = int ( ( n - 1 ) / 2 )
    for j in range ( 1, jhi + 1 ):

      if ( 2 * j == ( n - 1 ) ):
        b = 1.0
      else:
        b = 2.0

      w[i] = w[i] - b * np.cos ( 2.0 * j * theta ) / ( 4 * j * j - 1 )

  w[0]     =       w[0]     / ( n - 1 )
  w[1:n-1] = 2.0 * w[1:n-1] / ( n - 1 )
  w[n-1]   =       w[n-1]   / ( n - 1 )

  return x, w

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
  clenshaw_curtis_rule_test ( )
  timestamp ( )




