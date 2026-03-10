#! /usr/bin/env python3
#
def cross_chaos_test ( ):

#*****************************************************************************80
#
## cross_chaos_test() tests cross_chaos().
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
  print ( 'cross_chaos_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  cross_chaos() uses an iterated map to plot a cross.' )

  n = 5000
  print ( '  Apply the cross iteration map', n, 'times.' )
  cross_chaos ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'cross_chaos_test():' )
  print ( '  Normal end of execution.' )

  return

def cross_chaos ( n ):

#*****************************************************************************80
#
## cross_chaos() draws a cross using an iterated function system.
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
#
#  Define the linear map.
#
  A = np.array ( [ \
    [ 1.0 / 3.0, 0.0       ], \
    [ 0.0,       1.0 / 3.0 ] ] )
#
#  Define the five possible translations.
#
  b = np.array ( [ \
    [ 1.0 / 3.0, 0.0,       1.0 / 3.0, 2.0 / 3.0, 1.0 / 3.0 ], \
    [ 0.0,       1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0, 2.0 / 3.0 ] ] )

#
#  Random starting point in the unit square.
#
  x = np.random.random ( size = 2 )
#
#  Iterate the map n times.
#
  plt.clf ( )

  for _ in range ( n ):
    x = np.dot ( A, x.copy ( ) )
    j = np.random.choice ( [ 0, 1, 2, 3, 4 ] )
    x = x + b[:,j]
    plt.plot ( x[0], x[1], 'bo', markersize = 1 )

  filename = 'cross_chaos.png'
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
  cross_chaos_test ( )
  timestamp ( )

