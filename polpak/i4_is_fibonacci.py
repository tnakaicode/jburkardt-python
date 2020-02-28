#! /usr/bin/env python
#
def i4_is_fibonacci ( i4 ):

#*****************************************************************************80
#
## I4_IS_FIBONACCI reports whether an integer is a Fibonacci number.
#
#  Discussion:
#
#    The positive integer i4 is a Fibonacci number if and only if
#    5*I4^2+4 or 5*I4^2-4 is a perfect square.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the index of the Fibonacci number to compute.
#    N should be nonnegative.
#
#    Output, integer F, the value of the N-th Fibonacci number.
#
  import numpy as np

  value = False
#
#  Must be an integer.
#
  if ( i4 != int ( i4 ) ):
    return value
#
#  Must be positive.
#
  if ( i4 <= 0 ):
    return value

  t1 = 5 * i4 ** 2 + 4
  t2 = np.sqrt ( t1 )
  t3 = int ( t2 )
  if ( t3 * t3 == t1 ):
    value = True
    return value

  t1 = 5 * i4 ** 2 - 4
  t2 = np.sqrt ( t1 )
  t3 = int ( t2 )
  if ( t3 * t3 == t1 ):
    value = True
    return value

  return value

def i4_is_fibonacci_test ( ):

#*****************************************************************************80
#
## I4_IS_FIBONACCI_TEST tests I4_IS_FIBONACCI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 10
  i4_test = np.array ( [ - 13, 0, 1, 8, 10, 50, 55, 100, 144, 200 ] )
  print ( '' )
  print ( 'I4_IS_FIBONACCI_TEST' )
  print ( '  I4_IS_FIBONACCI returns T or F depending on' )
  print ( '  whether I4 is a Fibonacci number.' )
  print ( '' )
  print ( '   I4     T/F' )
  print ( '' )

  for i in range ( 0, test_num ):

    i4 = i4_test[i]
    l = i4_is_fibonacci ( i4 )
    print ( '  %4d    %s' % ( i4, l ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_IS_FIBONACCI_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_fibonacci_test ( )
  timestamp ( )

