#! /usr/bin/env python3
#
def casino_simulation_test ( ):

#*****************************************************************************80
#
## casino_simulation_test() tests casino_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'casino_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test casino_simulation().' )
#
#  Play one game, and print all the steps.

  stakes_initial = 5000.0
  n = 100
  verbose = True
  stakes, w, l = casino_simulation ( stakes_initial, n, verbose )
#
#  Compute average winnings over many sets of 100 games.
#
  trial_num = 500
  stakes_final = np.zeros ( trial_num )
  lose_num = 0

  for i in range ( 0, trial_num ):
    stakes_initial = 5000.0
    n = 100
    verbose = False
    stakes_final[i], w, l = casino_simulation ( stakes_initial, n, verbose )
    if ( stakes_final[i] < stakes_initial ):
      lose_num = lose_num + 1

  print ( '' )
  print ( '  Number of trials was ', trial_num )
  print ( '  Each trial involved tossing a coin ', n, ' times' )
  print ( '  Initial stakes were ', stakes_initial )
  print ( '  Number of trials with a final loss = ', lose_num )
  print ( '  Minimum final stakes: ', np.min ( stakes_final ) )
  print ( '  Average final stakes: ', np.mean ( stakes_final ) )
  print ( '  Maximum final stakes: ', np.max ( stakes_final ) )
  print ( '  Standard deviation:   ', np.std ( stakes_final ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'casino_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def casino_simulation ( stakes, n, verbose ):

#*****************************************************************************80
#
## casino_simulation() models a casino betting game that seems like a winner.
#
#  Discussion:
#
#    A casino offers the following game:
#    Put your initial stakes S on the table.
#    For N plays in a row, flip a fair coin, and if the result is:
#    * HEADS: we add 20 percent to your current stakes
#    * TAILS: we take 17 percent of your current stakes.
#
#    It seems like this game offers you roughly a 1.5 percent profit on
#    every coin toss, so that in the long run, you would expect to
#    win big.  Is that correct?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2023
#
#  Reference:
#
#    Bruce Boghosian,
#    The Inescapable Casino,
#    Scientific American,
#    November 2019, pages 70-77.
#
#  Input:
#
#    real stakes: the amount of money you begin with.
#
#    integer n: the number of times you play.
#
#    logical verbose: true if you want to see the results of each toss.
#
#  Output:
#
#    real stakes: the current amount of money you have.
#
#    integer w, l: the number of times you won and lost a coin toss.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  if ( verbose ):
    print ( '' )
    print ( '   i   win  lose    stakes' )
    print ( '' )
#
#  Play n games.
#
  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      w = 0
      l = 0
    else:
      coin = rng.integers ( low = 0, high = 1, endpoint = True )
      if ( coin == 0 ):
        l = l + 1
        stakes = 0.83 * stakes
      else:
        stakes = 1.2 * stakes
        w = w + 1

    if ( verbose ):
      print ( '  %5d  %5d  %5d  %14.2f' % ( i, w, l, stakes ) )

  return stakes, w, l

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
  casino_simulation_test ( )
  timestamp ( )

