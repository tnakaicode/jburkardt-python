#! /usr/bin/env python3
#
def polynomial_multiply ( p, q ):

#*****************************************************************************80
#
## polynomial_multiply() multiplies two polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real p(*), q(*): all the coefficients of two polynomials, zero or nonzero.
#
#  Output:
#
#    real r(*): all the coefficients of the product polynomial.
#
  import numpy as np

  pn = len ( p ) - 1
  while ( p[pn] == 0 and 0 < pn ):
    pn = pn - 1

  qn = len ( q ) - 1
  while ( q[qn] == 0 and 0 < qn ):
    qn = qn - 1

  rn = qn + pn + 1
  r = np.zeros ( rn )
  for i in range ( 0, pn + 1 ):
    for j in range ( 0, qn + 1 ):
      k = i + j
      r[k] = r[k] + p[i] * q[j]

  return r

def polynomial_multiply_test ( ):

#*****************************************************************************80
#
## polynomial_multiply_test() tests polynomial_multiply().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polynomial_multiply_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomial_multiply().' )

  p1 = np.array ( [ 0, 2, 0, 4 ] )
  p2 = polynomial_multiply ( p1, p1 )
  p3 = polynomial_multiply ( p1, p2 )
  print ( '' )
  print ( '  p1(x) = 2 x + 4 x^3' )
  print ( p1 )
  print ( '  p2(x) = p1(x) * p1(x)' )
  print ( p2 )
  print ( '  p3(x) = p1(x) * p2(x)' )
  print ( p3 )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomial_multiply():' )
  print ( '  Normal end of execution.' )

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
  polynomial_multiply_test ( )
  timestamp ( )

