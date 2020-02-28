#! /usr/bin/env python
#
def i4vec_mean_i4 ( n, a ):

#*****************************************************************************80
#
## I4VEC_MEAN_I4 computes the I4 mean of an I4VEC.
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
#    04 March 2017
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
#    Output, integer VALUE, the rounded mean of the entries.
#
  mean = 0.0

  for i in range ( 0, n ):
    mean = mean + float ( a[i] )
  mean = mean / float ( n )

  value = int ( round ( mean ) )

  return value

def i4vec_mean_i4_test ( ):

#*****************************************************************************80
#
## I4VEC_MEAN_I4_TEST tests I4VEC_MEAN_I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ( '' )
  print ( 'I4VEC_MEAN_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_MEAN_I4 computes the I4 mean of an I4VEC.' )

  n = 5
  lo = 0
  hi = 10
  seed = 123456789
  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_mean_i4 ( n, a )
  print ( '' )
  print ( '  The I4 mean value is %d' % ( s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_MEAN_I4_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_mean_i4_test ( )
  timestamp ( )

