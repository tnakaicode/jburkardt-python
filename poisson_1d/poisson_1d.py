#! /usr/bin/env python3
#
def poisson_1d_test ( ):

#*****************************************************************************80
#
## poisson_1d_test() tests poisson_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'poisson_1d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  poisson_1d() solves a boundary value problem.' )

  plt.clf ( )

  for n in [ 5, 9, 17 ]:
    x1 = np.linspace ( 0.0, 1.0, n )
    u1 = poisson_1d ( n )
    plt.plot ( x1, u1, '-o' )

  x2 = np.linspace ( 0.0, 1.0, 101 )
  u2 = poisson_1d_exact ( x2 )
  plt.plot ( x2, u2, 'b-' )
  plt.legend ( [ 'n=4', 'n=8', 'n=16', 'Exact' ] )
  plt.grid ( True )
  filename = 'poisson_1d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def poisson_1d ( n ):

#*****************************************************************************80
#
## poisson_1d() uses an n-point discretization to solve a Poisson problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of nodes.
#
#  Output:
#
#    real u(n): the estimate solution.
#
  import numpy as np

  x = np.linspace ( 0.0, 1.0, n )
  h = 1.0 / ( n - 1 )
  
  A = np.zeros ( [ n, n ] )
  b = np.zeros ( n )
  
  for i in range ( 0, n ):
    if ( i == 0 ):
      A[i,i] = 1.0
      b[i] = 0.0
    elif ( i < n - 1 ):
      A[i,i-1] = - 1.0 / h**2
      A[i,i]   =   2.0 / h**2
      A[i,i+1] = - 1.0 / h**2
      b[i] = x[i] * ( x[i] + 3.0 ) * np.exp ( x[i] )
    else:
      A[i,i] = 1.0
      b[i] = 0.0
      
  u = np.linalg.solve ( A, b )
  
  return u

def poisson_1d_exact ( x ):

#*****************************************************************************80
#
## poisson_1d_exact() returns the exact solution of a Poisson problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the evaluation points.
#
#  Output:
#
#    real u: the value of the exact solution.
#
  import numpy as np
  u = - x * ( x - 1.0 ) * np.exp ( x )
  return u

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
  poisson_1d_test ( )
  timestamp ( )

