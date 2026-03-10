#! /usr/bin/env python3
#
def dirichlet_test ( ):

#*****************************************************************************80
#
## dirichlet_test() tests dirichlet().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'dirichlet_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test dirichlet().' )
#
#  Plots.
#
  print ( '' )
  print ( '  Plot f(x,n) for several values of n' )
  print ( '' )

  for n in [ 2, 3, 4, 5, 10, 15, 20, 25 ]:
    x = np.linspace ( -10.0, 10.0, 501 )
    fx = dirichlet ( x, n )
    plt.clf ( )
    plt.plot ( x, fx, linewidth = 2 )
    plt.title ( 'dirichlet f(x,' + str ( n ) + ')' )
    plt.grid ( True )
    filename = 'dirichlet_' + str ( n ).zfill(2) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'dirichlet_test():' )
  print ( '  Normal end of execution.' )

  return

def dirichlet ( x, n ):

#*****************************************************************************80
#
## dirichlet() evaluates the Dirichlet kernel function.
#
#  Discussion:
#
#    The Dirichlet kernel function is also called the periodic sinc function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument of the function.
#
#    integer n: the degree of the function.
#
#  Output:
#
#    real value: the value of the function.
#
  import numpy as np

  value = np.ones_like ( x )

  nz = ( np.sin ( 0.5 * x ) != 0.0 )

  value[nz] = np.sin ( 0.5 * n * x[nz] ) / n / np.sin ( 0.5 * x[nz] )

  return value

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
  dirichlet_test ( )
  timestamp ( )

