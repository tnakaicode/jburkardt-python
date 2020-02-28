#! /usr/bin/env python
#
def i4vec_mean ( n, a ):

#*****************************************************************************80
#
## I4VEC_MEAN computes the mean of an I4VEC.
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
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements.
#
#    Input, integer A(N), the vector.
#
#    Output, real VALUE, the mean of the entries.
#
  value = 0.0

  for i in range ( 0, n ):
    value = value + float ( a[i] )
  value = value / float ( n )

  return value

def i4vec_mean_test ( ):

#*****************************************************************************80
#
## I4VEC_MEAN_TEST tests I4VEC_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ( '' )
  print ( 'I4VEC_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_MEAN computes the mean of an I4VEC.' )

  n = 5
  lo = 0
  hi = 10
  seed = 123456789
  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_mean ( n, a )
  print ( '' )
  print ( '  The mean value is %g' % ( s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_mean_test ( )
  timestamp ( )

