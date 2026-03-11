#! /usr/bin/env python3
#
def ising_2d_simulation ( m, n, iterations, thresh, rng ):

#*****************************************************************************80
#
## ising_2d_simulation() carries out a 2D Ising simulation.
#
#  Discussion:
#
#    Note that, when all the cells are updated in a single cycle, there is
#    a mathematically stable checkerboard solution, in which all the reds
#    and blacks flip color repeatedly.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the dimensions of the region.
#
#    integer ITERATIONS: the number of iterations.
#
#    real THRESH: the threshold value.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'ising_2d_simulation():' )
  print ( '  Monte Carlo simulation of a 2D Ising model.' )
#
#  Define the probability of flipping if you are in a neighborhood of
#  1, 2, 3, 4, or 5 of the same sign.
#
#  This should really be some kind of exponential dependent on "temperature".
#
  prob = np.array ( [ 0.98, 0.85, 0.50, 0.15, 0.02 ] )

  print ( '' )
  print ( '  The row dimension M =', m )
  print ( '  The column dimension N =', n )
  print ( '  The number of iterations taken is ITERATIONS =', iterations )
  print ( '  The threshhold THRESH =', thresh )
  print ( '' )
  print ( '  The transition probability table, based on the number of' )
  print ( '  neighbors with the same charge:' )
  print ( '' )
  print ( prob )
#
#  Initialize C1.
#
  c1 = ising_2d_initialize ( m, n, thresh, rng )
#
#  Do the simulation.
#
  c1 = transition ( m, n, iterations, prob, c1, rng )

  return

def ising_2d_agree ( m, n, c1 ):

#*****************************************************************************80
#
## ising_2d_agree() returns the number of neighbors agreeing with each cell.
#
#  Discussion:
#
#    The count includes the cell itself, so it is between 1 and 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of cells in each spatial dimension.
#
#    integer C1(M,N), an array of 1's and -1's.
#
#  Output:
#
#    integer C5(M,N), the number of neighbors that agree.
#    1, 2, 3, 4, or 5.
#
  import numpy as np

  c5 = c1 \
     + np.roll ( c1, -1, axis = 0 ) \
     + np.roll ( c1,  1, axis = 0 ) \
     + np.roll ( c1, -1, axis = 1 ) \
     + np.roll ( c1,  1, axis = 1 )

  c5[0<c1] = ( 5 + c5[0<c1] ) / 2
  c5[c1<0] = ( 5 - c5[c1<0] ) / 2

  return c5

def ising_2d_display ( step, m, n, c1 ):

#*****************************************************************************80
#
## ising_2d_display() displays the current Ising status.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP, the step number.
#
#    integer M, N, the number of rows and columnss.
#
#    integer C1(M,N), the status of each cell:
#    -1, display as a shade of red.
#    +1, display as a shade of blue.
#
  import matplotlib.pyplot as plt
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Determine the plot range.
#
  margin = 0.05

  x_axes_min = 1.0 - 0.5 - margin
  x_axes_max = m   + 0.5 + margin
  y_axes_min = 1.0 - 0.5 - margin
  y_axes_max = n   + 0.5 + margin
#
#  Fill in the background with black.
#
  x1 = x_axes_min
  x2 = x_axes_max
  y1 = y_axes_min
  y2 = y_axes_max

  rgb = [ 0.5, 0.5, 0.5 ]

  plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], color = rgb )
#
#  Draw a square, representing the bed,
#  with most of the length and width, centered at (I,J).
#
  for i in range ( 0, m ):
    for j in range ( 0, n ):

      x1 = j + 1 - 0.47
      x2 = j + 1 + 0.47
      y1 = ( m - i ) - 0.47
      y2 = ( m - i ) + 0.47

      if ( c1[i,j] == - 1 ):
        rgb = [ 1.0, 0.0, 0.0 ]
      elif ( c1[i,j] == + 1 ):
        rgb = [ 0.0, 0.0, 1.0 ]

      plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], color = rgb )
#
#  Make a title.
#
  s = ( 'Ising charges +1/-1 on step %d' % ( step ) )

  plt.title ( s )
#
#  Choose the aspect ratio and other plot details.
#
  plt.xlim ( [ x_axes_min, x_axes_max ] )
  plt.ylim ( [ y_axes_min, y_axes_max ] )
  plt.axis ( 'equal' )

  filename = 'ising_2d_display.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def ising_2d_initialize ( m, n, thresh, rng ):

#*****************************************************************************80
#
## ising_2d_initialize() initializes the Ising array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real THRESH, the threshhold value, between 0 and 1.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer C1(M,N), an array of 1's and -1's.
#
  import numpy as np

  c1 = np.ones ( [ m, n ] )

  r = rng.random ( [ m, n ] )

  c1[r <= thresh] = -1

  return c1

def ising_2d_stats ( step, m, n, c1 ):

#*****************************************************************************80
#
## ising_2d_stats() prints information about the current step.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP, the step number.
#
#    integer M, N, the number of rows and columns.
#
#    integer C1(M,N), the current state of the system.
#
  import numpy as np

  if ( step == 0 ):
    print ( '' )
    print ( '  Step       Positives       Negatives' )
    print ( '             #     %          #     %' )
    print ( '' )

  pos_count = np.sum ( 0 < c1 )
  neg_count = m * n - pos_count
  pos_percent = ( 100 * pos_count ) / ( m * n )
  neg_percent = ( 100 * neg_count ) / ( m * n )

  print ( '  %4d  %6d  %6.2f  %6d  %6.2f' \
    % ( step, pos_count, pos_percent, neg_count, neg_percent ) )

  return

def neighbor_2d_display ( step, m, n, c1, c5 ):

#*****************************************************************************80
#
## neighbor_2d_display() displays the current Ising neighbor status.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP, the step number.
#
#    integer M, N, the number of rows and columnss.
#
#    integer C1(M,N), the status of each cell:
#
#    integer C5(M,N), the number of agreeable neighbors.
#
  import matplotlib.pyplot as plt
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Determine the plot range.
#
  margin = 0.05

  x_axes_min = 1.0 - 0.5 - margin
  x_axes_max = m   + 0.5 + margin
  y_axes_min = 1.0 - 0.5 - margin
  y_axes_max = n   + 0.5 + margin
#
#  Fill in the background with black.
#
  x1 = x_axes_min
  x2 = x_axes_max
  y1 = y_axes_min
  y2 = y_axes_max

  rgb = [ 0.5, 0.5, 0.5 ]

  plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], color = rgb )
#
#  Draw a square, representing the bed,
#  with most of the length and width, centered at (I,J).
#
  for i in range ( 0, m ):
    for j in range ( 0, n ):

      x1 = j + 1 - 0.47
      x2 = j + 1+ 0.47
      y1 = ( m - i ) - 0.47
      y2 = ( m - i ) + 0.47

      c = c1[i,j] * c5[i,j]

      if ( c == - 5 ):
        rgb = [ 1.0, 0.0, 0.0 ]
      elif ( c == - 4 ):
        rgb = [ 1.0, 0.2, 0.2 ]
      elif ( c == - 3 ):
        rgb = [ 1.0, 0.4, 0.4 ]
      elif ( c == - 2 ):
        rgb = [ 1.0, 0.7, 0.7 ]
      elif ( c == - 1 ):
        rgb = [ 1.0, 0.8, 0.8 ]
      elif ( c == 0 ):
        rgb = [ 1.0, 1.0, 1.0 ]
      elif ( c == + 1 ):
        rgb = [ 0.7, 0.7, 1.0 ]
      elif ( c == + 2 ):
        rgb = [ 0.6, 0.6, 1.0 ]
      elif ( c == + 3 ):
        rgb = [ 0.4, 0.4, 1.0 ]
      elif ( c == + 4 ):
        rgb = [ 0.2, 0.2, 1.0 ]
      elif ( c == + 5 ):
        rgb = [ 0.0, 0.0, 1.0 ]

      plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], color = rgb )
#
#  Make a title.
#
  s = ( 'Ising neighborhoods -5 to +5, step %d to step %d' % ( step-1, step ) )

  plt.title ( s )
#
#  Choose the aspect ratio and other plot details.
#
  plt.xlim ( [ x_axes_min, x_axes_max ] )
  plt.ylim ( [ y_axes_min, y_axes_max ] )
  plt.axis ( 'equal' )

  filename = 'neighbor_2d_display.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def neighbor_2d_stats ( step, m, n, c1, c5 ):

#*****************************************************************************80
#
## neighbor_2d_stats() prints neighbor statistics about the current step.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP, the step number.
#
#    integer M, N, the number of rows and columns.
#
#    integer C1(M,N), the current state of the system.
#
#    integer C5(M,N), the number of agreeable neighbors.
#
  import numpy as np

  if ( step == 0 ):
    print ( '' )
    print ( '  Step     Neighborhood Charge:' )
    print ( '           -5    -4    -3    -2    -1    +1    +2    +3    +4    +5' )
    print ( '' )

  print ( '  %4d', step, end = '' )

  for n in range ( -5, 6 ):
    if ( n != 0 ):
      c = np.sum ( c1 * c5 == n )
      print ( '  %4d', c, end = '' )
  print ( '' )
  
  return

def transition ( m, n, iterations, prob, c1, rng ):

#*****************************************************************************80
#
## transition() carries out a Monte Carlo simulation of a 2D Ising model.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of cells in each spatial dimension.
#
#    integer ITERATIONS, the number of iterations to carry out.
#
#    real PROB(1:5).  PROB(I) represents the probability
#    that the spin of a given cell will be reversed, given that it has I immediate
#    neighbors (including itself) with spin the same as its own.
#
#    integer C1(M,N), the current state of the system. 
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer C1(M,N): the state of the system after the iterations.
#
  import numpy as np

  step = 0
  ising_2d_stats ( step, m, n, c1 )
  ising_2d_display ( step, m, n, c1 )

  for step in range ( 1, iterations + 1 ):
#
#  C5 contains 1 through 5, the number of cells that agree with the center cell.
#
    c5 = ising_2d_agree ( m, n, c1 )

    if ( False ):
      neighbor_2d_stats ( step, m, n, c1, c5 )

    if ( False ):
      neighbor_2d_display ( step, m, n, c1, c5 )
#
#  Determine the chances of flipping cell (I,J).
#
    threshhold = np.zeros ( [ m, n ] )

    for j in range ( 1, 6 ):
      threshhold[c5==j] = prob[j-1]

    r = rng.random ( [ m, n ] )

    c1[r<threshhold] = - c1[r<threshhold]

    ising_2d_stats ( step, m, n, c1 )
    ising_2d_display ( step, m, n, c1 )

  return c1
 
def ising_2d_simulation_test ( ):

#*****************************************************************************80
#
## ising_2d_simulation_test() tests ising_2d_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'ising_2d_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ising_2d_simulation().' )

  rng = default_rng ( )

  m = 10
  n = 10
  iterations = 15
  thresh = 0.50
  ising_2d_simulation ( m, n, iterations, thresh, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'ising_2d_simulation_test():' )
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
  ising_2d_simulation_test ( )
  timestamp ( )

