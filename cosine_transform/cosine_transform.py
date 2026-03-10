#! /usr/bin/env python3
#
def cosine_transform_data ( n, d ):

#*****************************************************************************80
#
## cosine_transform_data() does a cosine transform on a vector of data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    real D(N), the vector of data.
#
#  Output:
#
#    real C(N), the cosine transform coefficients.
#
  import numpy as np

  c = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = np.pi * float ( 2 * j + 1 ) * float ( i ) / 2.0 / float ( n )
      c[i] = c[i] + d[j] * np.cos ( angle )

    c[i] = c[i] * np.sqrt ( 2.0 / float ( n ) )
 
  return c

def cosine_transform_inverse ( n, c ):

#*****************************************************************************80
#
## cosine_transform_inverse() does an inverse cosine transform.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    real C(N), the cosine transform coefficients.
#
#  Output:
#
#    real D(N), the vector of data.
#
  import numpy as np

  d = np.zeros ( n )

  for i in range ( 0, n ):
    d[i] = c[0] / 2.0
    for j in range ( 1, n ):
      d[i] = d[i] + np.cos ( np.pi * float ( 2 * i + 1 ) \
        * float ( j ) / 2.0 / float ( n ) ) * c[j]
    d[i] = d[i] * np.sqrt ( 2.0 / float ( n ) )

  return d

def cosine_transform_data_test ( ):

#*****************************************************************************80
#
## cosine_transform_data_test() tests cosine_transform_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  n = 10

  print ( '' )
  print ( 'cosine_transform_data_test():' )
  print ( '  cosine_transform_data() does a cosine transform of data' )
  print ( '  defined by a vector.' )
  print ( '' )
  print ( '  Apply the transform, then its inverse.' )
  print ( '  Let R be a random N vector.' )
  print ( '  Let S be the transform of D.' )
  print ( '  Let T be the transform of E.' )
  print ( '  Then R and T will be equal.' )

  r = rng.random ( size = n )
  s = cosine_transform_data ( n, r )
  t = cosine_transform_inverse ( n, s )

  print ( '' )
  print ( '     I      R(I)        S(I)        T(I)' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %10f  %10f  %10f' % ( i, r[i], s[i], t[i] ) )

  return

def cosine_transform_test ( ):

#*****************************************************************************80
#
## cosine_transform_test() tests cosine_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cosine_transform_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cosine_transform().' )

  cosine_transform_data_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cosine_transform_test():' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  cosine_transform_test ( )
  timestamp ( )
