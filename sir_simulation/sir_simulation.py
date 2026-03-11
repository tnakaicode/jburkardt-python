#! /usr/bin/env python3
#
def sir_area_display ( t_max, sir, filename ):

#*****************************************************************************80
#
## sir_area_display() displays an area plot of the SIR data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Models of Infection: Person to Person,
#    Computing in Science and Engineering,
#    Volume 6, Number 1, January/February 2004.
#
#    Dianne OLeary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
#  Input:
#
#    integer T_MAX, the number of days of data.
#
#    integer SIR(T_MAX,3), the percentages of susceptible,
#    infected, and recovered patients for each day.
#
#    string filename: a filename for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.arange ( 0, t_max )

  plt.clf ( )
  plt.stackplot ( t, sir[:,0], sir[:,1], sir[:,2], labels = [ 'S', 'I', 'R' ] )
  plt.xlabel ( '<-- Days -->' )
  plt.ylabel ( '<-- Relative magnitude -->' )
  plt.title ( filename )
  plt.legend ( [ 'Suscepible', 'Infected', 'Recovered' ] )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sir_line_display ( t_max, sir, filename ):

#*****************************************************************************80
#
## sir_line_display() displays a line plot of the SIR data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Models of Infection: Person to Person,
#    Computing in Science and Engineering,
#    Volume 6, Number 1, January/February 2004.
#
#    Dianne OLeary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
#  Input:
#
#    integer T_MAX, the number of days of data.
#
#    integer SIR(T_MAX,3), the percentages of susceptible,
#    infected, and recovered patients for each day.
#
#    string filename: a filename for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.arange ( 0, t_max )
 
  plt.clf ( )
  plt.plot ( t, sir[:,0], 'g-', linewidth = 3 )
  plt.plot ( t, sir[:,1], 'r-', linewidth = 3 )
  plt.plot ( t, sir[:,2], 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.legend ( [ 'Suscepible', 'Infected', 'Recovered' ] )
  plt.xlabel ( '<-- Days -->' )
  plt.ylabel ( '<-- Relative magnitude -->' )
  plt.title ( filename )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sir_simulation ( m, n, A, k, tau, t_max ):

#*****************************************************************************80
#
## sir_simulation() simulates an SIR model of disease transmission.
#
#  Discussion:
#
#    We assume that a hospital ward comprises an array of M by N beds.
#
#    The status of each patient is recorded as an integer in an array A.
#
#    Susceptible patients, with a status of 0, have never had the disease.
#
#    Infected patients, with a positive status between 1 and K, have
#    had the disease for A[i,j] days.
#
#    Recovered patients, with a status of -1, have had the disease for K
#    days, are no longer infected, and cannot get the disease again.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne OLeary,
#    Models of Infection: Person to Person,
#    Computing in Science and Engineering,
#    Volume 6, Number 1, January/February 2004.
#
#    Dianne OLeary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
#  Input:
#
#    integer M, N, the number of rows and columns of beds.
#
#    integer A(M,N), status of each patient on day T = 1.
#
#    integer K, the maximum number of days of infection.
#
#    real TAU, the probability of transmission of the disease
#    over one day, due to one neighboring patient who is infected.
#
#    integer T_MAX, the number of days to model.
#
#  Output:
#
#    real SIR(T_MAX,3), the relative numbers of susceptible,
#    infected, and recovered patients.  The sum of these three values
#    will be 1 for each day.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng()

  sir = np.zeros ( [ t_max, 3 ] )

  for t in range ( 0, t_max ):

    if ( t == 0 ):
      pass
    else:
#
#  Update the patient status for the next day.
#
      A_new = np.zeros ( [ m, n ] )

      for i in range ( 0, m ):
        for j in range ( 0, n ):
#
#  Recovered patients never change.
#
          if ( A[i,j] == -1 ):
            A_new[i,j] = -1
#
#  Infected patients, knock one more day off their agony.
#
          elif ( A[i,j] < -1 ):
            A_new[i,j] = A[i,j] + 1
#
#  Susceptible, look for infected neighbors.
#
          else:

            A_new[i,j] = 0

            im1 = ( i - 1 ) % m
            ip1 = ( i + 1 ) % m
            jm1 = ( j - 1 ) % n
            jp1 = ( j + 1 ) % n

            neighbors = int ( \
              ( A[im1,j] < -1 ) + \
              ( A[ip1,j] < -1 ) + \
              ( A[i,jm1] < -1 ) + \
              ( A[i,jp1] < -1 ) )

            for neighbor in range ( 0, neighbors ):
              if ( rng.random ( ) <= tau ):
                A_new[i,j] = -k
#
#  Copy new data into A.
#
      A = A_new.copy ( )
#
#  Compute SIR.
#
    sir[t,0] = np.sum ( A ==  0 ) / m / n
    sir[t,1] = np.sum ( A <  -1 ) / m / n
    sir[t,2] = np.sum ( A == -1 ) / m / n
#
#  Plot the current A data.
#
    timestep_display ( m, n, A, k, t )
#
#  Quit if no infected persons.
#
    if ( sir[t,1] == 0 ):
      print ( '  Terminate simulation: No infected individuals remain.' )

      sir[t+1:t_max,0] = sir[t,0]
      sir[t+1:t_max,1] = sir[t,1]
      sir[t+1:t_max,2] = sir[t,2]
      break

  return sir

def sir_simulation_test ( ):

#*****************************************************************************80
#
## sir_simulation_test() tests sir_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sir_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sir_simulation().' )

  m = 10
  n = 10
  k = 5
  A = np.zeros( [ m, n ] )
  A[4,4] = -k
  tau = 0.2
  t_max = 50

  sir = sir_simulation ( m, n, A, k, tau, t_max )
  print ( '' )
  print ( '  At final time:' )
  print ( '  S = ', sir[-1,0] )
  print ( '  I = ', sir[-1,1] )
  print ( '  R = ', sir[-1,2] )

  filename = 'sir_line.png'
  sir_line_display ( t_max, sir, filename )

  filename = 'sir_area.png'
  sir_area_display ( t_max, sir, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'sir_simulation_test():' )
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

def timestep_display ( m, n, A, k, t ):

#*****************************************************************************80
#
## timestep_display() displays the SIR status of all patients at one timestep.
#
#  Discussion:
#
#    We assume that a hospital ward comprises an array of M by N beds.
#
#    The status of each patient is recorded as an integer in an array A.
#
#    Susceptible patients, with a status of 0, have never had the disease.
#
#    Infected patients, with a positive status between 1 and K, have
#    had the disease for A[i,j] days.
#
#    Recovered patients, with a status of -1, have had the disease for K
#    days, are no longer infected, and cannot get the disease again.
#
#    The dynamics for how the disease starts and spreads are handled elsewhere.
#    This routine simply displays the patient status on a given day.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Models of Infection: Person to Person,
#    Computing in Science and Engineering,
#    Volume 6, Number 1, January/February 2004.
#
#    Dianne OLeary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
#  Input:
#
#    integer M, N, the number of rows and columns of beds.
#
#    integer A(M,N), the status of each patient:
#     0, "Susceptible", display as WHITE.
#     1 through K, "Infected", display as shades of RED.
#    -1, "Recovered", display as GRAY.
#
#    integer K, the maximum number of days of infection.
#
#    integer T, the index of the current day.
#
  import matplotlib.pyplot as plt
  import numpy as np

  grid = np.zeros ( [ m, n ] )
#
#  Clear the graphics frame.
#
  plt.clf ( )
  plt.axis ( 'equal' )
  plt.axis ( 'off' )
#
#  Draw a square, representing the bed,
#  with most of the length and width, centered at [i,j].
#
#  Recovered patients have a light gray bed.
#  Suspectible patients have a green bed.
#  Infected patients are very red on the first day, then fade to gray.
#
  rgb = np.array ( [ 0.0, 0.0, 0.0 ] )
  plt.fill ( [ -0.5, n-0.5, n-0.5, -0.5 ], [ -0.5, -0.5, m-0.5, m-0.5 ], \
    color = rgb )
  
  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( A[i,j] == -1 ):
        rgb = np.array ( [ 0.8, 0.8, 0.8 ] )
      elif ( A[i,j] == 0 ):
        rgb = np.array ( [ 0.0, 0.8, 0.0 ] )
      else:
        rgb = ( (       - A[i,j] ) * np.array ( [ 1.0, 0.0, 0.0 ] ) \
              + ( k + 1 + A[i,j] ) * np.array ( [ 0.8, 0.8, 0.8 ] ) ) \
              / ( k + 1 )

      a = j - 0.47
      b = j + 0.47
      c = i - 0.47
      d = i + 0.47
      plt.fill ( [ a, b, b, a ], [ c, c, d, d ], color = rgb )

  filename = 'sir_day' + str ( t ) + '.png'
  plt.title ( filename )
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename, '"' )
  plt.close ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  sir_simulation_test ( )
  timestamp ( )

