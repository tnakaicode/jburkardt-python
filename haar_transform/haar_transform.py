#! /usr/bin/env python3
#
def haar_1d ( n, x ):

#*****************************************************************************80
#
## haar_1d() computes the Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real X[N], the vector to be transformed.
#
#  Output:
#
#    real U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n, dtype = np.float64 )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1

  while ( k * 2 <= n ):

    k = k * 2
  
  while ( 1 < k ):

    k = k // 2

    v[0:k]   = ( u[0:2*k-1:2] + u[1:2*k:2] ) / s
    v[k:2*k] = ( u[0:2*k-1:2] - u[1:2*k:2] ) / s

    u[0:2*k] = v[0:2*k].copy ( )

  return u

def haar_1d_inverse ( n, x ):

#*****************************************************************************80
#
## haar_1d_inverse() computes the inverse Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.  
#
#    real X[N], the vector to be transformed.
#
#  Output:
#
#    real U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n )

  k = 1
  while ( k * 2 <= n ):

    v[0:2*k-1:2] = ( u[0:k] + u[0+k:k+k] ) / s
    v[1:2*k:2]   = ( u[0:k] - u[0+k:k+k] ) / s

    u[0:2*k] = v[0:2*k].copy ( )
    k = k * 2

  return u

def haar_1d_test ( rng ):

#*****************************************************************************80
#
## haar_1d_test() tests haar_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'haar_1d_test():' )
  print ( '  haar_1d() computes the Haar transform of a vector.' )
#
#  Random data.
#
  n = 16
  u = rng.random ( size = n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Constant signal.
#
  n = 8
  u = np.ones ( n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Linear signal.
#
  n = 16
  u = np.linspace ( 1, n, n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Quadratic data.
#
  n = 8
  u = np.array ( [ \
    25.0, 16.0,  9.0,  4.0,  1.0, \
     0.0,  1.0,  4.0 ] )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  N not a power of 2.
#
  n = 99
  u = rng.random ( size = n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )

  return

def haar_2d ( m, n, x ):

#*****************************************************************************80
#
## haar_2d() computes the Haar transform of an array.
#
#  Discussion:
#
#    For the classical Haar transform, M and N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimensions of the array.
#
#    real X[M*N], the array to be transformed.
#
#  Output:
#
#    real U[M*N], the transformed array.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = u.copy ( )
#
#  Determine K, the largest power of 2 such that K <= M.
#
  k = 1
  while ( k * 2 <= m ):
    k = k * 2
#
#  Transform all columns.
#
  while ( 1 < k ):

    k = k // 2

    v[  0:  k,0:n] = ( u[0:2*k-1:2,0:n] + u[1:2*k:2,0:n] ) / s
    v[k+0:k+k,0:n] = ( u[0:2*k-1:2,0:n] - u[1:2*k:2,0:n] ) / s

    u[0:2*k,0:n] = v[0:2*k,0:n].copy ( )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
#
#  Transform all rows.
#
  while ( 1 < k ):

    k = k // 2

    v[0:m,  0:  k] = ( u[0:m,0:2*k-1:2] + u[0:m,1:2*k:2] ) / s
    v[0:m,k+0:k+k] = ( u[0:m,0:2*k-1:2] - u[0:m,1:2*k:2] ) / s

    u[0:m,0:2*k] = v[0:m,0:2*k].copy ( )

  return u

def haar_2d_inverse ( m, n, x ):

#*****************************************************************************80
#
## haar_2d_inverse() inverts the Haar transform of an array.
#
#  Discussion:
#
#    For the classical Haar transform, M and N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimensions of the array.
#
#    real X[M*N], the array to be transformed.
#
#  Output:
#
#    real U[M*N], the transformed array.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = u.copy ( )
#
#  Inverse transform of all rows.
#
  k = 1

  while ( k * 2 <= n ):

    v[0:m,0:2*k-1:2] = ( u[0:m,0:k] + u[0:m,0+k:k+k] ) / s
    v[0:m,1:2*k:2]   = ( u[0:m,0:k] - u[0:m,0+k:k+k] ) / s

    u[0:m,0:2*k] = v[0:m,0:2*k].copy ( )

    k = k * 2
#
#  Inverse transform of all columns.
#
  k = 1

  while ( k * 2 <= m ):

    v[0:2*k-1:2,0:n] = ( u[0:k,0:n] + u[0+k:k+k,0:n] ) / s
    v[1:2*k:2,0:n]   = ( u[0:k,0:n] - u[0+k:k+k,0:n] ) / s

    u[0:2*k,0:n] = v[0:2*k,0:n].copy ( )

    k = k * 2

  return u

def haar_2d_test ( rng ):

#*****************************************************************************80
#
## haar_2d_test() tests haar_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'haar_2d_test():' )
  print ( '  haar_2d() computes the Haar transform of an array.' )
  print ( '  haar_2d_inverse() inverts the transform.' )
#
#  Demonstrate successful inversion.
#
  m = 16
  n = 4
  u = rng.random ( size = [ m, n ] )

  print ( '' )
  print ( '  Input array U:' )
  print ( u )

  v = haar_2d ( m, n, u )

  print ( '' )
  print ( '  Transformed array V:' )
  print ( v )

  w = haar_2d_inverse ( m, n, v )

  print ( '' )
  print ( '  Recovered array W:' )
  print ( w )
#
#  M, N not powers of 2.
#
  m = 37
  n = 53
  u = rng.random ( size = [ m, n ] )

  v = haar_2d ( m, n, u )

  w = haar_2d_inverse ( m, n, v )

  err = np.linalg.norm ( u - w, 'fro' )

  print ( '' )
  print ( '  M = %d, N = %d, ||haar_2d_inverse(haar_2d(u))-u|| = %g' \
    % ( m, n, err ) )

  return

def haar_transform_test ( ):

#*****************************************************************************80
#
## haar_transform_test() tests haar_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'haar_transform_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test haar_transform().' )

  rng = default_rng ( )

  haar_1d_test ( rng )
  haar_2d_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'haar_transform_test():' )
  print ( '  Normal end of execution.' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  haar_transform_test ( )
  timestamp ( )

