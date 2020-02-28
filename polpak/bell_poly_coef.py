#! /usr/bin/env python
#
def bell_poly_coef ( n ):

#*****************************************************************************80
#
## BELL_POLY_COEF: Coefficients of a Bell polynomial.
#
#  First terms:
#
#    N    0    1    2    3    4    5    6    7    8
#
#    0    1
#    1    0    1    
#    2    0    1    1
#    3    0    1    3    1
#    4    0    1    7    6    1
#    5    0    1   15   25   10    1
#    6    0    1   31   90   65   15    1
#    7    0    1   63  301  350  140   21    1
#    8    0    1  127  966 1701 1050  266   28    1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Output, integer C[0:N], the coefficients.
#
  import numpy as np

  c = np.zeros ( n + 1 )

  c[0] = 1
 
  for i in range ( 1, n + 1 ):
    for j in range ( i, 0, -1 ):
      c[j] = j * c[j] + c[j-1]
    c[0] = 0
 
  return c

def bell_poly_coef_test ( ):

#*****************************************************************************80
#
## BELL_POLY_COEF_TEST tests BELL_POLY_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  n_max = 10

  print ( '' )
  print ( 'BELL_POLY_COEF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BELL_POLY_COEF returns the coefficients of a Bell polynomial.' )
  print ( '' )
  print ( '  Table of polyomial coefficients:' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):

    c = bell_poly_coef ( n )
    print ( '  %2d:' % ( n ) ),
    for i in range ( 0, n + 1 ):
      print ( '%5d' % ( c[i] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BELL_POLY_COEF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bell_poly_coef_test ( )
  timestamp ( )
