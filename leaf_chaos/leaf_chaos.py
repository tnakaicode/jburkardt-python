#! /usr/bin/env python3
#
def leaf_chaos_test ( ):

#*****************************************************************************80
#
## leaf_chaos_test() tests leaf_chaos().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'leaf_chaos_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  leaf_chaos() uses an iterated map to plot a leaf.' )

  n = 5000
  print ( '  Apply the leaf iteration map', n, 'times.' )
  leaf_chaos ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'leaf_chaos_test():' )
  print ( '  Normal end of execution.' )

  return

def leaf_chaos ( n ):

#*****************************************************************************80
#
## leaf_chaos() draws a leaf using an iterated function system.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2025
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Scott Bailey, Theodore Kim, Robert Strichartz,
#    Inside the Levy dragon,
#    American Mathematical Monthly,
#    Volume 109, Number 8, October 2002, pages 689-703.
#
#    Michael Barnsley, Alan Sloan,
#    A Better Way to Compress Images,
#    Byte Magazine,
#    Volume 13, Number 1, January 1988, pages 215-224.
#
#    Michael Barnsley,
#    Fractals Everywhere,
#    Academic Press, 1988,
#    ISBN: 0120790696,
#    LC: QA614.86.B37.
#
#    Michael Barnsley, Lyman Hurd,
#    Fractal Image Compression,
#    Peters, 1993,
#    ISBN: 1568810008,
#    LC: TA1632.B353
#
#    Alexander Dewdney,
#    Mathematical Recreations,
#    Scientific American,
#    Volume 262, Number 5, May 1990, pages 126-129.
#
#    Bernt Wahl, Peter VanRoy, Michael Larsen, Eric Kampman,
#    Exploring Fractals on the Mac,
#    Addison Wesley, 1995,
#    ISBN: 0201626306,
#    LC: QA614.86.W34.
#
#  Input:
#
#    integer n: the number of iterations.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.clf ( )
#
#  Define the linear maps.
#
  A0 = np.array ( [ \
    [  0.800,  0.000 ], \
    [  0.000,  0.800 ] ] )

  A1 = np.array ( [ \
    [  0.500,  0.000 ], \
    [  0.000,  0.500 ] ] )

  A2 = np.array ( [ \
    [  0.355, -0.355 ], \
    [  0.355,  0.355 ] ] )

  A3 = np.array ( [ \
    [  0.355,  0.355 ], \
    [ -0.355,  0.355 ] ] )
#
#  Define the translations.
#
  b0 = np.array ( [ 0.100, 0.040 ] )
  b1 = np.array ( [ 0.250, 0.400 ] )
  b2 = np.array ( [ 0.266, 0.078 ] )
  b3 = np.array ( [ 0.378, 0.434 ] )
#
#  Random starting point in the unit square.
#
  x = np.random.random ( size = 2 )
#
#  Iterate the map n times.
#
  for _ in range ( n ):
    j = np.random.choice ( [ 0, 1, 2, 3 ] )
    if ( j == 0 ):
      x = np.dot ( A0, x ) + b0
    elif ( j == 1 ):
      x = np.dot ( A1, x ) + b1
    elif ( j == 2 ):
      x = np.dot ( A2, x ) + b2
    elif ( j == 3 ):
      x = np.dot ( A3, x ) + b3
    plt.plot ( x[0], x[1], 'bo', markersize = 1 )

  filename = 'leaf_chaos.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
  leaf_chaos_test ( )
  timestamp ( )

