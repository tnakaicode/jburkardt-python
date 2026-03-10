#! /usr/bin/env python3
#
def dragon_chaos_test ( ):

#*****************************************************************************80
#
## dragon_chaos_test() tests dragon_chaos().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'dragon_chaos_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  dragon_chaos() uses an iterated map to plot a dragon.' )

  n = 10000
  print ( '  Apply the dragon iteration map', n, 'times.' )
  dragon_chaos ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'dragon_chaos_test():' )
  print ( '  Normal end of execution.' )

  return

def dragon_chaos ( n ):

#*****************************************************************************80
#
## dragon_chaos() draws a dragon using an iterated function system.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 August 2025
#
#  Author:
#
#    Original version by John D Cook.
#    This version by John Burkardt.
#
#  Reference:
#
#    Scott Bailey, Theodore Kim, Robert Strichartz,
#    Inside the Levy Dragon,
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
#    John D Cook,
#    Randomly generated dragon,
#    https://www.johndcook.com/blog/2025/08/16/randomly-generated-dragon/
#    Posted 16 August 2025
#
#    Darst, Palagallo, Price. 
#    Fractal Tilings in the Plane. 
#    Mathematics Magazine [71]:1, 1998.
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
#  Random starting point in the unit square.
#
  x = np.random.random ( )
  y = np.random.random ( )
#
#  Iterate the map n times.
#
  for _ in range ( n ):
    xold = x
    yold = y
    x = ( - xold + yold ) / 2.0 - np.random.choice ( [ 0.0, 1.0 ] )
    y = ( - xold - yold ) / 2.0

    plt.plot ( x, y, 'bo', markersize = 1 )

  filename = 'dragon_chaos.png'
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
  dragon_chaos_test ( )
  timestamp ( )

