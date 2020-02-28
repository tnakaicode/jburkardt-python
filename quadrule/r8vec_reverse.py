#! /usr/bin/env python
#
def r8vec_reverse ( n, a1 ):

#*****************************************************************************80
#
## R8VEC_REVERSE reverses the elements of an R8VEC.
#
#  Example:
#
#    Input:
#
#      N = 5, A = ( 11.0, 12.0, 13.0, 14.0, 15.0 ).
#
#    Output:
#
#      A = ( 15.0, 14.0, 13.0, 12.0, 11.0 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, real A1(N), the array to be reversed.
#
#    Output, real A2(N), the reversed array.
#
  import numpy as np

  a2 = np.zeros ( n )
  for i in range ( 0, n ):
    a2[i] = a1[n-1-i]

  return a2

def r8vec_reverse_test ( ):

#*****************************************************************************80
#
## R8VEC_REVERSE_TEST tests R8VEC_REVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8VEC_REVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_REVERSE reverses an R8VEC.' )
 
  a1 = np.zeros ( n )
  for i in range ( 0, n ):
    a1[i] = float ( i + 1 )
 
  r8vec_print ( n, a1, '  Original array:' )

  a2 = r8vec_reverse ( n, a1 )

  r8vec_print ( n, a2, '  Reversed array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_REVERSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_reverse_test ( )
  timestamp ( )

