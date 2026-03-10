#! /usr/bin/env python3
#
def hilbert_curve_3d_test ( ):

#*****************************************************************************80
#
## hilbert_curve_3d_test() tests hilbert_curve_3d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hilbert_curve_3d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hilbert_curve_3d().' )

  i4_log2_test ( )
  rmin_test ( )
  h_to_xyz_test ( )
  xyz_to_h_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hilbert_curve_3d_test():' )
  print ( '  Normal end of execution.' )

  return

def h_to_xyz ( h, r ):

#*****************************************************************************80
#
## h_to_xyz() converts a linear Hilbert 3D coordinate to (x,y,z).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer h: the linear Hilbert 3D coordinate.
#
#    integer r: the order of the Hilbert 3D curve.  
#
#  Output:
#
#    integer x, y, z: the coordinates of the lattice point corresponding to H.
#

#
#  Determine least significant octal digit of h.
#
  o = ( h % 8 )

  if ( o == 0 ):
    x = 0
    y = 0
    z = 0
  elif ( o == 1 ):
    x = 1
    y = 0
    z = 0
  elif ( o == 2 ):
    x = 1
    y = 0
    z = 1
  elif ( o == 3 ):
    x = 0
    y = 0
    z = 1
  elif ( o == 4 ):
    x = 0
    y = 1
    z = 1
  elif ( o == 5 ):
    x = 1
    y = 1
    z = 1
  elif ( o == 6 ):
    x = 1
    y = 1
    z = 0
  elif ( o == 7 ):
    x = 0
    y = 1
    z = 0

  w = 2
  h = ( h // 8 )

  while ( 0 < h ):

    o = ( h % 8 )

    xold = x
    yold = y
    zold = z

    if ( o == 0 ):
      x = yold
      y = zold
      z = xold
    elif ( o == 1 ):
      x = zold + w
      y = xold
      z = yold
    elif ( o == 2 ):
      x = zold + w
      y = xold
      z = yold + w
    elif ( o == 3 ):
      x = w - xold - 1
      y = yold
      z = 2 * w - zold - 1
    elif ( o == 4 ):
      x = w - xold - 1
      y = yold + w
      z = 2 * w - zold - 1
    elif ( o == 5 ):
      x = zold + w
      y = 2 * w - xold - 1
      z = 2 * w - yold - 1
    elif ( o == 6 ):
      x = zold + w
      y = 2 * w - xold - 1
      z = w - yold - 1
    elif ( o == 7 ):
      x = w - yold - 1
      y = 2 * w - zold - 1
      z = xold

    h = ( h // 8 )
    w = w * w

  rm = rmin ( x, y, z )
  t = ( r - rm ) % ( 3 )

  if ( t == 1 ):
    xold = x
    yold = y
    zold = z 
    x = yold
    y = zold
    z = xold
  elif ( t == 2 ):
    xold = x
    yold = y
    zold = z 
    x = zold
    y = xold
    z = yold

  return x, y, z

def h_to_xyz_test ( ):

#*****************************************************************************80
#
## h_to_xyz_test() tests h_to_xyz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2024
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'h_to_xyz_test():' )
  print ( '  h_to_xyz() converts a Hilbert 3D curve coordinate H ' )
  print ( '  within a cube of side 2^r into (x,y,z) coordinates' )

  r = 1
        
  print ( '' )
  print ( '  For r = ', r )
  print ( '   h   x   y   z' )
  print ( '' )

  hmax = 2 ** (3*r)-1
  for h in range ( 0, hmax + 1 ):
    x, y, z = h_to_xyz ( h, r )
    print ( '  %2d  %2d  %2d  %2d' % ( h, x, y, z ) )

  xvec = np.zeros ( hmax + 1 )
  yvec = np.zeros ( hmax + 1 )
  zvec = np.zeros ( hmax + 1 )

  for h in range ( 0, hmax + 1 ):
    x, y, z = h_to_xyz ( h, r )
    xvec[h] = x
    yvec[h] = y
    zvec[h] = z

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( xvec, yvec, zvec, linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->' )
  ax.set_ylabel ( '<-- Y -->' )
  ax.set_zlabel ( '<-- Z -->' )
  ax.set_title ( 'HIlbert curve, r = 1' )
  filename = 'hilbert_curve_3d_r1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Make level 2 curve.
#
  r = 2
        
  hmax = 2 ** (3*r)-1
  for h in range ( 0, hmax + 1 ):
    x, y, z = h_to_xyz ( h, r )
    print ( '  %2d  %2d  %2d  %2d' % ( h, x, y, z ) )

  xvec = np.zeros ( hmax + 1 )
  yvec = np.zeros ( hmax + 1 )
  zvec = np.zeros ( hmax + 1 )

  for h in range ( 0, hmax + 1 ):
    x, y, z = h_to_xyz ( h, r )
    xvec[h] = x
    yvec[h] = y
    zvec[h] = z

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( xvec, yvec, zvec, linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->' )
  ax.set_ylabel ( '<-- Y -->' )
  ax.set_zlabel ( '<-- Z -->' )
  ax.set_title ( 'HIlbert curve, r = 1' )
  filename = 'hilbert_curve_3d_r2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def i4_log2 ( i ):

#*****************************************************************************80
#
## i4_log2() returns the integer part of the logarithm base 2 of I.
#
#  Discussion:
#
#    For positive I4_LOG2(I), it should be true that
#      2^I4_LOG2(X) <= |I| < 2^(I4_LOG2(I)+1).
#    The special case of I4_LOG2(0) returns 0.
#
#  Example:
#
#     I  Value
#
#     0   0
#     1,  0
#     2,  1
#     3,  1
#     4,  2
#     5,  2
#     6,  2
#     7,  2
#     8,  3
#     9,  3
#    10,  3
#   127,  6
#   128,  7
#   129,  7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I: the number whose logarithm base 2 is desired.
#
#  Output:
#
#    integer VALUE: the integer part of the logarithm base 2 of I.
#
  if ( i < 0 ):
    print ( '' )
    print ( 'i4_log2(): Fatal error!' )
    print ( '  i < 0' )
    raise Exception ( 'i4_log2(): Fatal error!' )

  value = 0

  while ( 2 <= i ):
    i = i // 2
    value = value + 1

  return value

def i4_log2_test ( ):

#*****************************************************************************80
#
## i4_log2_test() tests i4_log2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2009
#
#  Author:
#
#    John Burkardt
# 
  print ( '' )
  print ( 'i4_log2_test():' )
  print ( '  i4_log2(): whole part of log base 2.' )
  print ( '' )
  print ( '       x     i4_log_2(x)' )
  print ( '' )

  for x in [ 0, 1, 2, 3, 4, 5, 9, 10, 11, 99, 101, 1000, 1023, 1024, 1025 ]:
    print ( '  %6d  %12d' % ( x, i4_log2 ( x ) ) )

  return

def i4_random_ab ( a, b ):

#*****************************************************************************80
#
## i4_random_ab() returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 November 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the minimum and maximum acceptable values.
#
#  Output:
#
#    integer C, the randomly chosen integer.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  c = rng.integers ( low = a, high = b, endpoint = True )

  return c

def rmin ( x, y, z ):

#*****************************************************************************80
#
## rmin() evaluates r, the smallest power of 2 greater than integers x, y and z.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x, y, z: the integers to be tested.
#
#  Output:
#
#    integer r: the smallest value such that 2^r is greater than x, y, and  z.
# 
  r = i4_log2 ( max ( x, max ( y, z ) ) ) + 1

  return r

def rmin_test ( ):

#*****************************************************************************80
#
## rmin_test() tests rmin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2024
#
#  Author:
#
#    John Burkardt
# 
  print ( '' )
  print ( 'rmin_test():' )
  print ( '  rmin() returns r, the smallest power of 2 such than' )
  print ( '  2^r is bigger than any of x, y and z.' )
  print ( '' )
  print ( '   x   y   z   r   2^r' )
  print ( '' )

  for test in range ( 1, 21 ):
    x = i4_random_ab ( 0, 10 )
    y = i4_random_ab ( 0, 6 )
    z = i4_random_ab ( 0, 4 )
    r = rmin ( x, y, z )
    print ( '  %2d  %2d  %2d  %2d  %4d' % ( x, y, z, r, 2**r ) )

  return

def xyz_to_h ( x, y, z, r ):

#*****************************************************************************80
#
## xyz_to_h() converts a 3D Hilbert curve lattice point to a linear H index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer x, y, z: values in [0,2^r) that are lattice coordinates.
#
#  Output:
#
#    integer h: the corresponding linear H index.
#
  rm = rmin ( x, y, z )
  t = ( r - rm ) % ( 3 )

  if ( t == 1 ):
    xold = x
    yold = y
    zold = z
    x = zold
    y = xold
    z = yold
  elif ( t == 2 ):
    xold = x
    yold = y
    zold = z
    x = yold
    y = zold
    z = xold

  h = 0
  w = 2**( rm - 1 )

  for k in range ( rm, 0, -1 ):

    xw = ( x // w )
    yw = ( y // w )
    zw = ( z // w )

    if ( [ xw, yw, zw ] == [ 0, 0, 0 ] ):
      o = 0
      xnew = z
      ynew = x
      znew = y
    elif ( [ xw, yw, zw ] == [ 1, 0, 0 ] ):
      o = 1
      xnew = y
      ynew = z
      znew = x - w
    elif ( [ xw, yw, zw ] == [ 1, 0, 1 ] ):
      o = 2
      xnew = y
      ynew = z - w
      znew = x - w
    elif ( [ xw, yw, zw ] == [ 0, 0, 1 ] ):
      o = 3
      xnew = w - x - 1
      ynew = y
      znew = 2 * w - z - 1
    elif ( [ xw, yw, zw ] == [ 0, 1, 1 ] ):
      o = 4
      xnew = w - x - 1
      ynew = y - 2
      znew = 2 * w - z - 1
    elif ( [ xw, yw, zw ] == [ 1, 1, 1 ] ):
      o = 5
      xnew = 2 * w - y - 1
      ynew = 2 * w - z - 1
      znew = x - w
    elif ( [ xw, yw, zw ] == [ 1, 1, 0 ] ):
      o = 6
      xnew = 2 * w - y - 1
      ynew = w - z - 1
      znew = x - w
    elif ( [ xw, yw, zw ] == [ 0, 1, 0 ] ):
      o = 7
      xnew = z
      ynew = w - x - 1
      znew = 2 * w - y - 1
#
#  Move to updated position.
#
    x = xnew
    y = ynew
    z = znew

    h = 8 * h + o
    w = ( w // 2 )

  return h

def xyz_to_h_test ( ):

#*****************************************************************************80
#
## xyz_to_h_test() tests xyz_to_h().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'xyz_to_h_test():' )
  print ( '  xyz_to_h() converts a 3D Hilbert curve lattice point' )
  print ( '  (x,y,z) to a linear coordinate H.' )

  r = 1

  print ( '' )
  print ( '  r = ', r )
  print ( '   i   x   y   z   h' )
  print ( '' )

  hmax = 2**(3*r)-1

  for h in range ( 0, hmax + 1 ):
    x, y, z = h_to_xyz ( h, r )
    h2 = xyz_to_h ( x, y, z, r )
    print ( '  %2d  %2d  %2d  %2d  %2d' % ( h, x, y, z, h2 ) )
#
#  Level 2.
#
  r = 2

  print ( '' )
  print ( '  r = ', r )
  print ( '   i   x   y   z   h' )
  print ( '' )

  hmax = 2**(3*r)-1

  for h in range ( 0, hmax + 1 ):
    x, y, z = h_to_xyz ( h, r )
    h2 = xyz_to_h ( x, y, z, r )
    print ( '  %2d  %2d  %2d  %2d  %2d' % ( h, x, y, z, h2 ) )

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
#    21 August 2019
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
  hilbert_curve_3d_test ( )
  timestamp ( )


