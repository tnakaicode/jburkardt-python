#! /usr/bin/env python3
#
def chuckaluck_frequency_plot ( counts ):

#*****************************************************************************80
#
## chuckaluck_frequency_plot_test tests chuckaluck_frequency_plot
#
#  Discussion:
#
#    This code makes a histogram of the frequency of 0, 1, 2 or 3 matches
#    given a fixed choice for the user's spot.
#      
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer counts[4], the frequency with which 0, 1, 2 and 3 matches
#    were encountered.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Make a bar plot.
#
  x = np.arange ( 4 )
  plt.bar ( x, counts )
  plt.grid ( True )
  plt.title ( 'Chuckaluck matches', fontsize = 16 )
  plt.xlabel ( '<-- Number of matches -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  filename = 'chuckaluck_frequency.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
# plt.show ( )
  plt.clf ( )

def chuckaluck_frequency_plot_test ( ):

#*****************************************************************************80
#
## chuckaluck_frequency_plot_test tests chuckaluck_frequency_plot
#
#  Discussion:
#
#    This code makes a histogram of the frequency of 0, 1, 2 or 3 matches
#    given a fixed choice for the user's spot.
#      
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  spot = np.random.randint ( 1, 7 )
  rounds = 10000
#
#  Throw all three dice, ROUNDS times.
#
#  (As a consequence of Python's MORONIC conventions, you get integers between
#  1 and 6 by using a range of 1 to 7.)
#
  throws = np.random.randint ( 1, 7, [ rounds, 3 ] )
#
#  Count the number of dice that match SPOT.
#
  matches = ( throws == spot )
#
#  Sum the number of dice that match SPOT on each round
#
  scores = np.sum ( matches, axis = 1 )
#
#  Count the number of times each score was achieved.
#
  counts = np.zeros ( 4 )
  for i in range ( 0, 4 ):
    counts[i] = np.count_nonzero ( scores == i )
#
#  Make a bar plot of the frequency of each score.
#
  chuckaluck_frequency_plot ( counts )

  return

def chuckaluck_game ( spot ):

#*****************************************************************************80
#
## chuckaluck_game simulates one chuckaluck game.
#    
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer spot, the player's chosen number.
#
#  Output:
#
#    integer win, the payoff (-1, 1, 2 or 10 ).
#
  dice = np.random.randint ( 1, 7, 3 )

  win = chuckaluck_payoff ( spot, dice )

  return win

def chuckaluck_games ( spot, rounds ):

#*****************************************************************************80
#
## chuckaluck_games simulates many chuckaluck games.
#    
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer spot, the player's chosen number.
#
#    integer rounds, the number of games to play.
#
#  Output:
#
#    integer wins, the total payoff.
#
  wins = 0
  for i in range ( 0, rounds ):
    dice = np.random.randint ( 1, 7, 3 )
    wins = wins + chuckaluck_payoff ( spot, dice )

  return wins

def chuckaluck_history_plot ( wins ):

#*****************************************************************************80
#
## chuckaluck_history_plot_test tests chuckaluck_history_plot
#
#  Discussion:
#
#    This code plots the player's total winnings at each stage of a sequence
#    of chuckaluck games.
#      
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer wins[n], the total winnings at each stage of a sequence of
#    chuckaluck games.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = len ( wins )
  games = np.arange ( n )
  plt.plot ( games, wins, linewidth = 3 )
  plt.plot ( [0,n], [0,0], 'r-', linewidth = 3 )
  plt.title ( 'Chuckaluck winnings', fontsize = 16 )
  plt.xlabel ( '<-- Number of games -->', fontsize = 16 )
  plt.ylabel ( '<-- Winnings ($) -->', fontsize = 16 )
  plt.grid ( True )
  filename = 'chuckaluck_history.png'
  plt.savefig ( filename )
  print ( 'Graphics saved as "', filename, '".' )
# plt.show ( )
  plt.clf ( )

def chuckaluck_history_plot_test ( ):

#*****************************************************************************80
#
## chuckaluck_history_plot_test tests chuckaluck_history_plot
# 
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  spot = np.random.randint ( 1, 7 )
  rounds = 10000
  win_sum = np.zeros ( rounds + 1 )
  for i in range ( 0, rounds ):
    dice = np.random.randint ( 1, 7, 3 )
    win = chuckaluck_payoff ( spot, dice )
    win_sum[i+1] = win_sum[i] + win

  chuckaluck_history_plot ( win_sum )

  return

def chuckaluck_payoff ( spot, dice ):

#*****************************************************************************80
#
## chuckaluck_payoff returns the payoff for a game of chuckaluck.
#  
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer spot, the user's choice, between 1 and 6.
#
#    integer dice[3], the values of the dice roll.
#
#  Output:
#
#    integer win, the payoff.
#
#
  import numpy as np

  match = np.count_nonzero ( dice == spot )
  if ( match == 0 ):
    win = -1
  elif ( match == 1 ):
    win = +1
  elif ( match == 2 ):
    win = +2
  elif ( match == 3 ):
    win = +10
    
  return win

def chuckaluck_probability ( rounds ):

#*****************************************************************************80
#
## chuckaluck_probability estimates chuckaluck probabilities.
#
#  Discussion:
#
#    This code plays a number of games and estimates the probability of
#    0, 1, 2 or 3 matches.
#      
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer rounds, the number of rounds of the game.
#
#  Output:
#
#    real prob[4], the estimated probabilities of 0, 1, 2 or 3 matches.
#
  import numpy as np
#
#  Arbitrarily choose SPOT.
#
  spot = np.random.randint ( 1, 7 )
#
#  Throw all three dice, ROUNDS times.
#
  throws = np.random.randint ( 1, 7, [ rounds, 3 ] )
#
#  Count the number of dice that match SPOT.
#
  matches = ( throws == spot )
#
#  Sum the number of dice that match SPOT on each round
#
  scores = np.sum ( matches, axis = 1 )
#
#  Count the number of times each score was achieved.
#
  counts = np.zeros ( 4 )
  for i in range ( 0, 4 ):
    counts[i] = np.count_nonzero ( scores == i )

  prob = counts / rounds

  return prob

def chuckaluck_probability_test ( ):

#*****************************************************************************80
#
## chuckaluck_probability_test tests chuckaluck_probability.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'chuckaluck_probability_test:' )
  print ( '  chuckaluck_probability estimates the probability of' )
  print ( '  0, 1, 2, or 3 matches in chuckaluck, by simulating' )
  print ( '  n games.' )
  print ( '' )
  print ( '        n        0        1        2        3' )
  print ( '' )

  n = 1
  for log10n in range ( 0, 7 ):
    prob = chuckaluck_probability ( n )
    print ( '  %7d  %8.6f  %8.6f  %8.6f  %8.6f' \
      % ( n, prob[0], prob[1], prob[2], prob[3] ) )
    n = n * 10

  exact = np.array ( [ 5**3, 3 * 5**2, 3 * 5, 1 ] ) / 6**3
  print ( '' )
  print ( '  Exact:   %8.6f  %8.6f  %8.6f  %8.6f' \
    % ( exact[0], exact[1], exact[2], exact[3] ) )

  return

def chuckaluck_simulation_test ( ):

#*****************************************************************************80
#
## chuckaluck_simulation_test tests chuckaluck_simulation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2019
#
#  Author:
#
#    John Burkardt
#
  import platform
  print ( '' )
  print ( 'chuckaluck_simulation_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test chuckaluck_simulation.' )

  spot = 1
  rounds = 1000
  bet = 100
  triple = 10
# chuckaluck_simulation ( spot, rounds, bet, triple )

  chuckaluck_frequency_plot_test ( )

  chuckaluck_history_plot_test ( )

  chuckaluck_probability_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'chuckaluck_simulation_test:' )
  print ( '  Normal end of execution.' )
  print ( '' )
  timestamp ( )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  chuckaluck_simulation_test ( )
  timestamp ( )

