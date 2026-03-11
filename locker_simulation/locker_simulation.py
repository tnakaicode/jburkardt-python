#! /usr/bin/env python3
#
def locker_simulation_test ( ):

#*****************************************************************************80
#
## locker_simulation_test() tests locker_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'locker_simulation_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test several strategies for the locker puzzle.' )

  rng = default_rng ( )

  strategy1_test ( rng )
  strategy2_test ( rng )
  strategy3_test ( rng )
  strategy4_test ( rng )

  print ( '' )
  print ( 'locker_simulation_test()' )
  print ( '  Normal end of execution.' )

  return

def strategy1 ( locker_num, locker_value, player_num, try_max, rng ):

#*****************************************************************************80
#
## strategy1() uses strategy #1 on the locker problem.
#
#  Discussion:
#
#    The lockers are checked at random.  
#
#    In fact, a list is prepared in advance, and may contain duplicates.
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
#    integer locker_num: the number of lockers.
#
#    integer locker_value(locker_num): the number stored in each locker.
#
#    integer player_num: the number of players.
#
#    integer try_max: the maximum number of tries allowed.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer found: the number of wallets that were found.
#
  found = 0

  for player in range ( 0, player_num ):

    locker_index = rng.integers ( low = 0, high = locker_num, size = try_max, endpoint = False )

    for trial in range ( 0, try_max ):
      locker = locker_index[trial]
      if ( locker_value[locker] == player ):
        found = found + 1
        break

  return found

def strategy1_test ( rng ):

#*****************************************************************************80
#
## strategy1_test() tests locker strategy #1.
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'strategy1_test():' )
  print ( '  Each player simply opens lockers at random.' )
  print ( '  They may even open some lockers several times.' )

  locker_num = 100
  player_num = 100
  try_max = 50

  trial_num = 1000
  found = np.zeros ( trial_num )
  found_all = 0

  for test in range ( 0, trial_num ):
    locker_value = rng.permutation ( locker_num )
    found[test] = strategy1 ( locker_num, locker_value, player_num, try_max, rng )
    if ( found[test] == player_num ):
      found_all = found_all + 1

  found = found / player_num

  print ( '' )
  print ( '  Number of lockers was ', locker_num )
  print ( '  Number of players was ', player_num )
  print ( '  Number of lockers a player can check ', try_max )
  print ( '  Number of trials was ', trial_num )
  print ( '' )
  print ( '  Success rate = number of players who found wallet / number of players.' )
  print ( '' )
  print ( '  Minimum  = ', np.min ( found ) )
  print ( '  Maximum  = ', np.max ( found ) )
  print ( '  Mean     = ', np.mean ( found ) )
  print ( '  STD      = ', np.std ( found ) )
  print ( '' )
  print ( '  All players found their wallets %d times out of %d' % ( found_all, trial_num ) )

  return

def strategy2 ( locker_num, locker_value, player_num, try_max, rng ):

#*****************************************************************************80
#
## strategy2() uses strategy #2 on the locker problem.
#
#  Discussion:
#
#    Strategy 1 used a completely random list of lockers.
#    Strategy 2 uses a list that is random, except that there are no duplicates.
#    
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer locker_num: the number of lockers.
#
#    integer locker_value(locker_num): the number stored in each locker.
#
#    integer player_num: the number of players.
#
#    integer try_max: the maximum number of tries allowed.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer found: the number of wallets that were found.
#
  if ( locker_num < try_max ):
    try_max = locker_num

  found = 0

  for player in range ( 0, player_num ):

    locker_index = rng.choice ( locker_num, size = locker_num, replace = False )

    for trial in range ( 0, try_max ):
      locker = locker_index[trial]
      if ( locker_value[locker] == player ):
        found = found + 1
        break

  return found

def strategy2_test ( rng ):

#*****************************************************************************80
#
## strategy2_test() tests locker strategy #2.
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'strategy2_test():' )
  print ( '  Each player opens lockers based on a random list.' )
  print ( '  However, this list has no duplicates.' )

  locker_num = 100
  player_num = 100
  try_max = 50

  trial_num = 1000
  found = np.zeros ( trial_num )
  found_all = 0

  for test in range ( 0, trial_num ):
    locker_value = rng.permutation ( locker_num )
    found[test] = strategy2 ( locker_num, locker_value, player_num, try_max, rng )
    if ( found[test] == player_num ):
      found_all = found_all + 1

  found = found / player_num

  print ( '' )
  print ( '  Number of lockers was ', locker_num )
  print ( '  Number of players was ', player_num )
  print ( '  Number of lockers a player can check ', try_max )
  print ( '  Number of trials was ', trial_num )
  print ( '' )
  print ( '  Success rate = number of players who found wallet / number of players.' )
  print ( '' )
  print ( '  Minimum  = ', np.min ( found ) )
  print ( '  Maximum  = ', np.max ( found ) )
  print ( '  Mean     = ', np.mean ( found ) )
  print ( '  STD      = ', np.std ( found ) )
  print ( '' )
  print ( '  All players found their wallets %d times out of %d' % ( found_all, trial_num ) )

  return

def strategy3 ( locker_num, locker_value, player_num, try_max ):

#*****************************************************************************80
#
## strategy3() uses strategy #3 on the locker problem.
#
#  Discussion:
#
#    Strategy 1 used a completely random list of lockers.
#    Strategy 2 uses a list that is random, except that there are no duplicates.
#    Strategy 3 starts at the player's own locker, then to the locker 
#      "pointed to" by the wallet inside, and so on.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer locker_num: the number of lockers.
#
#    integer locker_value(locker_num): the number stored in each locker.
#
#    integer player_num: the number of players.
#
#    integer try_max: the maximum number of tries allowed.
#
#  Output:
#
#    integer found: the number of wallets that were found.
#
  if ( locker_num < try_max ):
    try_max = locker_num

  found = 0

  for player in range ( 0, player_num ):

    locker = player

    for trial in range ( 0, try_max ):
      if ( locker_value[locker] == player ):
        found = found + 1
        break
      locker = locker_value[locker]

  return found

def strategy3_test ( rng ):

#*****************************************************************************80
#
## strategy3_test() tests locker strategy #3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'strategy3_test():' )
  print ( '  Each player starts at their own locker.' )
  print ( '  Next try the locker corresponding to the wallet they found.' )

  locker_num = 100
  player_num = 100
  try_max = 50

  trial_num = 1000
  found = np.zeros ( trial_num )
  found_all = 0

  for test in range ( 0, trial_num ):
    locker_value = rng.permutation ( locker_num )
    found[test] = strategy3 ( locker_num, locker_value, player_num, try_max )
    if ( found[test] == player_num ):
      found_all = found_all + 1

  found = found / player_num

  print ( '' )
  print ( '  Number of lockers was ', locker_num )
  print ( '  Number of players was ', player_num )
  print ( '  Number of lockers a player can check ', try_max )
  print ( '  Number of trials was ', trial_num )
  print ( '' )
  print ( '  Success rate = number of players who found wallet / number of players.' )
  print ( '' )
  print ( '  Minimum  = ', np.min ( found ) )
  print ( '  Maximum  = ', np.max ( found ) )
  print ( '  Mean     = ', np.mean ( found ) )
  print ( '  STD      = ', np.std ( found ) )
  print ( '' )
  print ( '  All players found their wallets %d times out of %d' % ( found_all, trial_num ) )

  return

def strategy4 ( locker_num, locker_value, player_num, try_max, rng ):

#*****************************************************************************80
#
## strategy4() uses strategy #4 on the locker problem.
#
#  Discussion:
#
#    Strategy 1 used a completely random list of lockers.
#    Strategy 2 uses a list that is random, except that there are no duplicates.
#    Strategy 3 starts at the player's own locker, then to the locker 
#      "pointed to" by the wallet inside, and so on.
#    Strategy 4 starts at a random locker, then to the locker 
#      "pointed to" by the wallet inside, and so on.
#
#    Surprisingly, strategy 4 is very bad.  It is WORSE than strategy 2.
#    That might seem impossible until you realize that the player may easily
#    end up in a "short loop" that does not include his wallet, and hence 
#    in 50 searches may actually only view far fewer distinct wallets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer locker_num: the number of lockers.
#
#    integer locker_value(locker_num): the number stored in each locker.
#
#    integer player_num: the number of players.
#
#    integer try_max: the maximum number of tries allowed.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer found: the number of wallets that were found.
#
  if ( locker_num < try_max ):
    try_max = locker_num

  found = 0

  for player in range ( 0, player_num ):

    locker = rng.integers ( low = 0, high = locker_num, endpoint = False )

    for trial in range ( 0, try_max ):
      if ( locker_value[locker] == player ):
        found = found + 1
        break
      locker = locker_value[locker]

  return found

def strategy4_test ( rng ):

#*****************************************************************************80
#
## strategy4_test() tests locker strategy #4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'strategy4_test():' )
  print ( '  Each player starts at a random locker.' )
  print ( '  Next try the locker corresponding to the wallet they found.' )

  locker_num = 100
  player_num = 100
  try_max = 50

  trial_num = 1000
  found = np.zeros ( trial_num )
  found_all = 0

  for test in range ( 0, trial_num ):
    locker_value = rng.permutation ( locker_num )
    found[test] = strategy4 ( locker_num, locker_value, player_num, try_max, rng )
    if ( found[test] == player_num ):
      found_all = found_all + 1

  found = found / player_num

  print ( '' )
  print ( '  Number of lockers was ', locker_num )
  print ( '  Number of players was ', player_num )
  print ( '  Number of lockers a player can check ', try_max )
  print ( '  Number of trials was ', trial_num )
  print ( '' )
  print ( '  Success rate = number of players who found wallet / number of players.' )
  print ( '' )
  print ( '  Minimum  = ', np.min ( found ) )
  print ( '  Maximum  = ', np.max ( found ) )
  print ( '  Mean     = ', np.mean ( found ) )
  print ( '  STD      = ', np.std ( found ) )
  print ( '' )
  print ( '  All players found their wallets %d times out of %d' % ( found_all, trial_num ) )

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
  locker_simulation_test ( )
  timestamp ( )

