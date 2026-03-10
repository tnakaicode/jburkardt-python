#! /usr/bin/env python3
#
def chebyshev_matrix_test ( ):

#*****************************************************************************80
#
## chebyshev_matrix_test() tests chebyshev_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'chebyshev_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test chebyshev_matrix().' )

  chebyshev_grid_print ( )
  chebyshev_matrix_print ( )
  chebyshev_differentiation_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'chebyshev_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def chebyshev_differentiation_test ( ):

#*****************************************************************************80
#
## chebyshev_differentiation_test() plots error in derivative estimates.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2025
#
#  Author:
#
#    Original MATLAB version by Lloyd Trefethen.
#    This version by John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'chebyshev_differentiation_test():' )
  print ( '  Use the  Chebyshev differentiation matrix to estimate' )
  print ( '  the derivative of a smooth function.' )

  xx = np.linspace ( -1.0, +1.0, 201 )
  uu = np.exp ( xx ) * np.sin ( 5.0 * xx )

  for n in [ 10, 20 ]:

    x = chebyshev_grid ( n )
    D = chebyshev_matrix ( n ) 

    u = np.exp ( x ) * np.sin ( 5.0 * x )

    err = np.dot ( D, u ) - np.exp ( x ) \
      * ( np.sin ( 5.0 * x ) + 5.0 * np.cos ( 5.0 * x ) )

    fig, ( ax1, ax2 ) = plt.subplots ( 1, 2 )
 
    ax1.plot ( x, u, '.', markersize = 14 )
    ax1.grid ( True )
    ax1.plot ( xx, uu )
    ax1.set_title ( 'u(x),  n=' + str ( n ) )

    ax2.plot ( x, err, '.', markersize = 14 )
    ax2.grid ( True )
    ax2.plot ( x, err )
    ax2.set_title ( '  error in u\'(x),  n =' + str ( n ) )

    filename = 'chebyshev_differentiation_n' + str ( n ) + '.png'
    print ( filename )
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )

  return

def chebyshev_grid ( n ):

#*****************************************************************************80
#
## chebyshev_grid() computes the Chebyshev grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2025
#
#  Author:
#
#    Original MATLAB version by Lloyd Trefethen.
#    This version by John Burkardt.
#
#  Reference:
#
#    Lloyd Trefethen,
#    Spectral methods in MATLAB,
#    SIAM, 2000,
#    LC: QA377.T65
#    ISBN: 978-0-898714-65-4
#
#  Input:
#
#    integer n: the order of the grid.
#
#  Output:
#
#    real x(n+1): the Chebyshev grid.
#
  import numpy as np

  if ( n == 0 ):
    x = np.ones ( 1 )
  else:
    x = np.linspace ( 0.0, 1.0, n + 1 )
    x = np.cos ( np.pi * x )

  return x

def chebyshev_grid_print ( ):

#*****************************************************************************80
#
## chebyshev_grid_print() tests chebyshev_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_grid_print():' )
  print ( '  Print the Chebyshev grid points.' )

  n = 5
  x = chebyshev_grid ( n )
  
  print ( '' )
  print ( '  The Chebyshev grid points, n = ', n )
  print ( x )

  return

def chebyshev_matrix ( n ):

#*****************************************************************************80
#
## chebyshev_matrix() computes the Chebyshev differentiation matrix.
#
#  Discussion:
#
#    Given a grid function v defined on the points of a Chebyshev grid,
#    the discrete derivative w is found by w = D * v.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2025
#
#  Author:
#
#    Original MATLAB version by Lloyd Trefethen.
#    This version by John Burkardt.
#
#  Reference:
#
#    Lloyd Trefethen,
#    Spectral methods in MATLAB,
#    SIAM, 2000,
#    LC: QA377.T65
#    ISBN: 978-0-898714-65-4
#
#  Input:
#
#    integer n: the order of the grid.
#
#  Output:
#
#    real d(n+1,n+1): the differentiation matrix.
#
  import numpy as np

  if ( n == 0 ):
    D = []
    return D
#
#  Compute the Chebyshev points.
#
  print ( "size of n = ", n )

  x = np.linspace ( 0.0, 1.0, n + 1 )
  x = np.cos ( np.pi * x )

  c = np.ones ( n + 1 )
  c[0] = 2.0
  c[n] = 2.0
  c[1::2] = - c[1::2]

  x_column = x[...,None]
  X = np.tile ( x_column, n + 1 )

  dX = X - np.transpose ( X )
#
#  Set the offdiagonal entries.
#       
  E = np.outer ( c, ( 1.0 / c ) ) 
  F = dX + np.identity ( n + 1 )
  D = E / F
#
#  Set diagonal entries.
#
  D  = D - np.diag ( np.sum ( np.transpose ( D ), axis = 0 ) )

  return D

def chebyshev_matrix_print ( ):

#*****************************************************************************80
#
## chebyshev_matrix_print() prints a Chebyshev differentiation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_matrix_print():' )
  print ( '  Print a Chebyshev differentiation matrix.' )

  n = 5
  D = chebyshev_matrix ( n )

  print ( '' )
  print ( '  Chebyshev differentiation matrix for n = ', n )
  print ( D )

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
  chebyshev_matrix_test ( )
  timestamp ( )

