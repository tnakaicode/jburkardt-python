#! /usr/bin/env python
#
def i4vec_increment ( n, v ):

#*****************************************************************************80
#
## I4VEC_INCREMENT increments an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the I4VEC.
#
#    Input/output, integer V[N], the vector to be incremented.
#
  v[0:n] = v[0:n] + 1

  return v

def i4vec_increment_test ( ):

#*****************************************************************************80
#
## I4VEC_INCREMENT_TEST tests I4VEC_INCREMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 4

  print ( '' )
  print ( 'I4VEC_INCREMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_INCREMENT increments an I4VEC.' )

  v_lo = -5
  v_hi = 10
  seed = 123456789
  v, seed = i4vec_uniform_ab ( n, v_lo, v_hi, seed )
  i4vec_print ( n, v, '  The I4VEC:' )
  v = i4vec_increment ( n, v )
  i4vec_print ( n, v, '  The I4VEC after incrementing:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_INCREMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_increment_test ( )
  timestamp ( )
