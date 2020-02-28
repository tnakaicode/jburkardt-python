#! /usr/bin/env python
#
def i4vec_indicator1 ( n ):

#*****************************************************************************80
#
## I4VEC_INDICATOR1 sets an I4VEC to the indicator vector ( 1, 2, 3, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Output, integer A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def i4vec_indicator1_test ( ):

#*****************************************************************************80
#
## I4VEC_INDICATOR1_TEST tests I4VEC_INDICATOR1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'I4VEC_INDICATOR1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_INDICATOR1 returns an indicator vector.' )

  n = 10
  a = i4vec_indicator1 ( n )
  i4vec_print ( n, a, '  The indicator1 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_INDICATOR1_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_indicator1_test ( )
  timestamp ( )
