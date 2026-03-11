#! /usr/bin/env python3
#
def prime_plot ( n_max ):

#*****************************************************************************80
#
## prime_plot() makes a box plot of primes.
#
#  Usage:
#
#    prime_plot ( n_max )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_MAX, the maximum number to be considered.
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'prime_plot():' )
  print ( '  Display primes and composite numbers.' )
  print ( '  If N is composite, Box (N,D) is blue if N is divisible by D.' )
  print ( '  If N is prime, Column (N,:) is red.' )

  plt.clf ( )
#
#  Every box starts out WHITE.
#
  for n in range ( 1, n_max + 1 ):

    for d in range ( 1, n_max + 1 ):

      x1 = n - 0.44
      x2 = n + 0.44
      y1 = d - 0.44
      y2 = d + 0.44

      plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], 'w', edgecolor = None )
#
#  By convention, 1 is NOT a prime!
#
  n = 1
  d = 1

  x1 = n - 0.44
  x2 = n + 0.44
  y1 = d - 0.44
  y2 = d + 0.44
  plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], 'b', edgecolor = None )

  for n in range ( 2, n_max + 1 ):

    prime = True
    d_hi = min ( n_max, n - 1 )

    for d in range ( 2, d_hi + 1 ):

      if ( ( n % d ) == 0 ):
        x1 = n - 0.44
        x2 = n + 0.44
        y1 = d - 0.44
        y2 = d + 0.44
        plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], 'b', edgecolor = None )
        prime = False

    d = n

    if ( prime ):
      x1 = n - 0.44
      x2 = n + 0.44
      y1 = 1 - 0.44
      y2 = d + 0.44
      plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], 'r', edgecolor = None )  
    else:
      x1 = n - 0.44
      x2 = n + 0.44
      y1 = d - 0.44
      y2 = d + 0.44
      plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], 'b', edgecolor = None )  
      x1 = n - 0.44
      x2 = n + 0.44
      y1 = 1 - 0.44
      y2 = 1 + 0.44
      plt.fill ( [ x1, x2, x2, x1 ], [ y1, y1, y2, y2 ], 'b', edgecolor = None )  

  plt.xlabel ( '<---N--->' )
  plt.ylabel ( '<--Divisors-->' )
  plt.title ( 'Primes are red columns blue squares are factors.' )

  filename = 'prime_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def prime_plot_test ( ):

#*****************************************************************************80
#
## prime_plot_test() tests prime_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'prime_plot_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test prime_plot().' )

  n_max = 100
  prime_plot ( n_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'prime_plot_test():' )
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
  prime_plot_test ( )
  timestamp ( )


