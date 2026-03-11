#! /usr/bin/env python3
#
def line_nco_rule_test ( ):

#*****************************************************************************80
#
## line_nco_rule_test() tests line_nco_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'line_nco_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test line_nco_rule().' )

  line_nco_rule_test01 ( )
  line_nco_rule_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_nco_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def line_nco_rule ( n, a, b ):

#*****************************************************************************80
#
## line_nco_rule() computes a Newton-Cotes Open quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( A <= X <= B ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the OPEN rule, the abscissas do not include the end points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#
#    real A, B, the left and right ednpoints of the interval.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.linspace ( a, b, n + 2 )
  x = x[1:n+1]

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
        d[n+j-k-1] = ( d[n+j-k-2] - d[n+j-k-1] ) / ( x[n-k] - x[n+j-k-1] )

    for j in range ( 1, n ):
      for k in range ( 1, n - j + 1 ):
        d[n-k-1] = d[n-k-1] - x[n-k-j] * d[n-k]
#
#  Evaluate the antiderivative of the polynomial at the endpoints.
#
    yvala = d[n-1] / n
    for j in range ( n - 1, 0, -1 ):
      yvala = yvala * a + d[j-1] / j
    yvala = yvala * a

    yvalb = d[n-1] / n
    for j in range ( n - 1, 0, -1 ):
      yvalb = yvalb * b + d[j-1] / j
    yvalb = yvalb * b

    w[i] = yvalb - yvala

  return x, w

def line_nco_rule_test01 ( ):

#*****************************************************************************80
#
## line_nco_rule_test01() computes and prints open Newton Cotes rules.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = -1.0
  b = +1.0

  print ( '' )
  print ( 'line_nco_rule_test01():' )
  print ( '  line_nco_rule() computes the open Newton-Cotes rules' )
  print ( '  using N equally spaced points for an interval [A,B].' )

  for n in range ( 1, 13 ):

    x, w = line_nco_rule ( n, a, b )

    print ( '' )
    print ( '  Open Newton-Cotes Rule', n )
    print ( '   I       X(I)            W(I)' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %2d  %14.6g  %14.6g' % ( i, x[i], w[i] ) )
    print ('' )
    print ( '  Sum(|W)|) =  ', np.sum ( np.abs ( w ) ) )

  return

def line_nco_rule_test02 ( ):

#*****************************************************************************80
#
## line_nco_rule_test02() estimates the integral of exp(x) from 0 to 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a =  0.0
  b = +1.0
  exact = np.exp ( b ) - np.exp ( a )

  print ( '' )
  print ( 'line_nco_rule_test02():' )
  print ( '  Use a sequence of Open Newton Cotes rules ' )
  print ( '  for an estimate Q of the integral:' )
  print ( '    I = integral ( 0 <= x <= 1 ) exp(x) dx.' )
  print ( '  The exact value is:' )
  print ( '    I = ', exact )

  print ( '' )
  print ( '   N       Q             |Q-I|' )
  print ( '' )

  for n in range ( 1, 23 ):

    x, w = line_nco_rule ( n, a, b )

    q = np.sum ( w * np.exp ( x ) )
    error = abs ( exact - q )
    print ( '  %2d  %14.6g  %14.6g' % ( n, q, error ) )

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
  line_nco_rule_test ( )
  timestamp ( )

