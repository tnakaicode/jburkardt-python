#! /usr/bin/env python3
#
def heated_plate_test ( ):

#*****************************************************************************80
#
## heated_plate_test() tests heated_plate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'heated_plate_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve for the steady state temperature distribution' )
  print ( '  over a rectangular plate.' )

  m = 200
  n = 200
  tol = 0.001
  heated_plate ( m, n, tol )
#
#  Terminate.
#
  print ( '' )
  print ( 'heated_plate_test():' )
  print ( '  Normal end of execution.' )

  return

def heated_plate ( m, n, epsilon ):

#*****************************************************************************80
#
#  Purpose:
#
#    heated_plate() solves the steady state heat equation on a rectangular region.
#
#  Discussion:
#
#    The sequential version of this program needs approximately
#    18/eps iterations to complete. 
#
#    The physical region, and the boundary conditions, are suggested
#    by this diagram
#
#                   W = 0
#             +------------------+
#             |                  |
#    W = 100  |                  | W = 100
#             |                  |
#             +------------------+
#                   W = 100
#
#    The region is covered with a grid of M by N nodes, and an N by N
#    array W is used to record the temperature.  The correspondence between
#    array indices and locations in the region is suggested by giving the
#    indices of the four corners:
#
#                  I = 0
#          [0][0]-------------[0][N-1]
#             |                  |
#      J = 0  |                  |  J = N-1
#             |                  |
#        [M-1][0]-----------[M-1][N-1]
#                  I = M-1
#
#    The steady state solution to the discrete heat equation satisfies the
#    following condition at an interior grid point:
#
#      W[Central] = (1/4) * ( W[North] + W[South] + W[East] + W[West] )
#
#    where "Central" is the index of the grid point, "North" is the index
#    of its immediate neighbor to the "north", and so on.
#   
#    Given an approximate solution of the steady state heat equation, a
#    "better" solution is given by replacing each interior point by the
#    average of its 4 neighbors - in other words, by using the condition
#    as an ASSIGNMENT statement:
#
#      W[Central]  <=  (1/4) * ( W[North] + W[South] + W[East] + W[West] )
#
#    If this process is repeated often enough, the difference between successive 
#    estimates of the solution will go to zero.
#
#    This program carries out such an iteration, using a tolerance specified by
#    the user, and writes the final estimate of the solution to a file that can
#    be used for graphic processing.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 April 2025
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Michael Quinn,
#    Parallel Programming in C with MPI and OpenMP,
#    McGraw-Hill, 2004,
#    ISBN13: 978-0071232654,
#    LC: QA76.73.C15.Q55.
#
#  Input:
#
#    integer m, n: the number of rows and columns in the grid.
#
#    real EPSILON, the error tolerance.  
#
#  Local:
#
#    real DIFF, the norm of the change in the solution from 
#    one iteration to the next.
#
#    real MEAN, the average of the boundary values, used 
#    to initialize the values of the solution in the interior.
#
#    real U(M,N), the solution at the previous iteration.
#
#    real w[M,N), the solution computed at the latest 
#    iteration.
#
  from matplotlib import cm
  from time import time
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( '  ', m, ' by ', n, ' spatial grid' )
  print ( '' )
  print ( '  The iteration will repeat until the change is <= ', epsilon )
#
#  Set the boundary values, which don't change. 
#
  W = np.zeros ( [ m, n ] )

  W[1:m-1,0] = 100.0
  W[1:m-1,n-1] = 100.0
  W[m-1,0:n-1] = 100.0
  W[0,0:n-1] =   0.0
#
#  Initialize the interior solution to a reasonable initial value.
#
  W[1:m-1,1:n-1] = 50.0
#
#  iterate until the  new solution W differs from the old solution U
#  by no more than EPSILON.
#
  iterations = 0
  iterations_print = 1
  diff = epsilon

  print ( '' )
  print ( ' Iteration  Change' )
  print ( '' )

  seconds = time ( )

  while ( epsilon <= diff ):

    U = W.copy()

    W[1:m-1,1:n-1] = 0.25 * ( \
        U[0:m-2,1:n-1] \
      + U[2:m,1:n-1] \
      + U[1:m-1,0:n-2] \
      + U[1:m-1,2:n] )

    diff = np.max ( np.abs ( U - W ) )

    iterations = iterations + 1

    if ( iterations == iterations_print ):
      print ( '  %8d  %14f' % ( iterations, diff ) )
      iterations_print = 2 * iterations_print

  seconds = time ( ) - seconds

  x = np.linspace ( 1, n, n )
  y = np.linspace ( 1, m, m )
  X, Y = np.meshgrid ( x, y )

  levels = 15
  ax = plt.figure ( )
  plt.contourf ( X, Y, W, levels, cmap = cm.coolwarm )
  plt.colorbar ( )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'The heated plate' )
  filename = 'heated_plate.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  print ( '' )
  print ( '  %8d  %14f' % ( iterations, diff ) )
  print ( '' )
  print ( '  Error tolerance achieved.' )
  print ( '  Wallclock time = ', seconds )
#
#  Terminate.
#
  print ( '' )
  print ( 'heated_plate():' )
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
  heated_plate_test ( )
  timestamp ( )

