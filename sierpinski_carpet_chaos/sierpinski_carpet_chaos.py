#! /usr/bin/env python3
#
def sierpinski_carpet_chaos_test ( ):

#*****************************************************************************80
#
## sierpinski_carpet_chaos_test() tests sierpinski_carpet_chaos().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sierpinski_carpet_chaos_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  sierpinski_carpet_chaos() uses an iterated map to plot' )
  print ( '  the Sierpinski carpet.' )

  n = 10000
  print ( '  Apply the iteration map', n, 'times.' )
  sierpinski_carpet_chaos ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'sierpinski_carpet_chaos_test():' )
  print ( '  Normal end of execution.' )

  return

def sierpinski_carpet_chaos ( n ):

#*****************************************************************************80
#
## sierpinski_carpet_chaos() draws the Sierpinski carpet using an iterated function system.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 August 2025
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
#  Define the linear map.
#
  A = np.array ( [ \
    [  0.333,  0.000 ], \
    [  0.000,  0.333 ] ] )
#
#  Define the translations.
#
  b = np.array ( [ \
    [ 0.000,  0.666 ], \
    [ 0.333,  0.666 ], \
    [ 0.666,  0.666 ], \
    [ 0.000,  0.333 ], \
    [ 0.666,  0.333 ], \
    [ 0.000,  0.000 ], \
    [ 0.333,  0.000 ], \
    [ 0.666,  0.000 ] ] )
#
#  Random starting point in the unit square.
#
  x = np.random.random ( size = 2 )
#
#  Iterate the map n times.
#
  for _ in range ( n ):
    i = np.random.choice ( [ 0, 1, 2, 3, 4, 5, 6, 7 ] )
    x = np.dot ( A, x ) + b[i,:]
    plt.plot ( x[0], x[1], 'bo', markersize = 1 )
  plt.axis ( 'equal' )
  filename = 'sierpinski_carpet_chaos.png'
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
  sierpinski_carpet_chaos_test ( )
  timestamp ( )

