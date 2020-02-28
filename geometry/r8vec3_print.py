#! /usr/bin/env python
#
def r8vec3_print ( n, a1, a2, a3, title ):

#*****************************************************************************80
#
## R8VEC3_PRINT prints an R8VEC3.
#
#  Discussion:
#
#    An R8VEC3 is a dataset consisting of 3 vectors of N real values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), A3(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g  %12g' % ( i, a1[i], a2[i], a3[i] ) )

  return

def r8vec3_print_test ( ):

#*****************************************************************************80
#
## R8VEC3_PRINT_TEST tests R8VEC3_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC3_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC3_PRINT prints an R8VEC.' )

  n = 6

  t = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  u = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  v = np.array ( [ 0.0, 0.24, 0.56, 0.96, 1.44, 2.0 ], dtype = np.float64 )

  r8vec3_print ( n, t, u, v, '  X, X^2, X+X^2\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC3_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec3_print_test ( )
  timestamp ( )

