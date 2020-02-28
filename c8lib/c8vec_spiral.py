#! /usr/bin/env python
#
def c8vec_spiral ( n, m, c1, c2 ):

#*****************************************************************************80
#
## C8VEC_SPIRAL returns N points on a spiral between C1 and C2.
#
#  Discussion:
#
#    A C8VEC is a vector of C8's.
#
#    Let the polar form of C1 be ( R1, T1 ) and the polar form of C2 
#    be ( R2, T2 ) where, if necessary, we increase T2 by 2*PI so that T1 <= T2.
#    
#    Then the polar form of the I-th point C(I) is:
#
#      R(I) = ( ( N - I     ) * R1 
#             + (     I - 1 ) * R2 ) 
#              / ( N    - 1 )
#
#      T(I) = ( ( N - I     ) * T1 
#             + (     I - 1 ) * ( T2 + M * 2 * PI ) ) 
#             / ( N     - 1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of points on the spiral.
#
#    Input, integer M, the number of full circuits the 
#    spiral makes.
#
#    Input, complex C1, C2, the first and last points 
#    on the spiral.
#
#    Output, complex C(N), the points.
#
  import numpy as np
  from c8_arg import c8_arg
  from polar_to_c8 import polar_to_c8

  r1 = abs ( c1 )
  r2 = abs ( c2 )

  t1 = c8_arg ( c1 )
  t2 = c8_arg ( c2 )

  if ( m == 0 ):

    if ( t2 < t1 ):
      t2 = t2 + 2.0 * np.pi

  elif ( 0 < m ):

    if ( t2 < t1 ):
      t2 = t2 + 2.0 * np.pi

    t2 = t2 + m * 2.0 * np.pi

  elif ( m < 0 ):

    if ( t1 < t2 ):
      t2 = t2 - 2.0 * np.pi

    t2 = t2 - m * 2.0 * np.pi

  c = np.zeros ( n, dtype = np.complex128 )

  for i in range ( 0, n ):

    ri = ( float ( n - i - 1 ) * r1 \
         + float (     i     ) * r2 ) \
         / float ( n     - 1 )

    ti = ( float ( n - i - 1 ) * t1 \
         + float (     i     ) * t2 ) \
         / float ( n     - 1 )

    c[i] = polar_to_c8 ( ri, ti )

  return c

def c8vec_spiral_test ( ):

#*****************************************************************************80
#
## C8VEC_SPIRAL_TEST tests C8VEC_SPIRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from c8vec_print import c8vec_print

  n = 13

  print ( '' )
  print ( 'C8VEC_SPIRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8VEC_SPIRAL returns N points on a spiral' )
  print ( '  which includes M complete turns.' )

  m = 1
  c1 = 5.0 + 0.0j
  c2 = 3.0 + 0.0j

  c = c8vec_spiral ( n, m, c1, c2 )

  c8vec_print ( n, c, '  The spiral points:' );
#
#  Terminate.
#
  print ( '' )
  print ( 'C8VEC_SPIRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_spiral_test ( )
  timestamp ( )

