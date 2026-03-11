#! /usr/bin/env python3
#
def truel_simulation ( p, strategy, truel_num, rng ):

#*****************************************************************************80
#
## truel_simulation() simulates a truel (a 3-way duel).
#
#  Discussion:
#
#    Three players fight a three-sided duel, or "truel".
#
#    Player 1 chooses a target (player 2, player 3, or nobody), and fires.
#    If aimed at a player, he hits with a probability of P(1).
#
#    Then it is Player 2's turn, and Player 3's turn.
#
#    Play continues to alternate until there is only one survivor.
#
#    Strategy 1:
#
#      Each player uses their turn to fire at the opponent with the
#      highest accuracy.
#
#    Strategy 2:
#      Each player fires at the "next" player.  1->2, 2->3, 3->1
#      until there are only two players.
#
#    Strategy 3:
#      Each player chooses their target at random.
#
#    Strategy 4:
#
#    * The player with the highest accuracy will always aim at the player
#      with the next highest accuracy.
#    * The player with the medium accuracy will always aim at the player
#      with the highest accuracy if that player is dead, then the player
#      will aim at the player with lowest accuracy.
#    * The player with lowest accuracy will aim at NO ONE, as long as
#      the other two players are both alive.  Once there is only one
#      opponent, he will aim at that opponent.  
#
#    Although the program was written to simulate a 3-way duel, it can
#    handle duels with an arbitrary number of players.  It determines the number 
#    of players from the length of the P array.  Therefore, to play a duel with 
#    4 players, simply supply 4 numbers in P.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Martin Gardner,
#    "The Triangular Duel",
#    The Second Scientific American Book of Mathematical
#    Puzzles and Diversions,
#    Simon and Schuster, 1961.
#
#    Marc Kilgour, Steven Brams,
#    The Truel,
#    Mathematics Magazine,
#    Volume 70, Number 5, December 1997, pages 315-326.
#
#    Paul Nahin,
#    Duelling Idiots and Other Probability Puzzlers,
#    Princeton University Press, 2000,
#    ISBN13: 978-0691009797,
#    LC: QA273.N29.
#
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(*), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#    integer STRATEGY, the index of the strategy.
#    1: each player fires at best opponent.
#    2: each player fires at "next" opponent.
#    3: each player fires at random opponent.
#    4: player 1 at 2, player 2 at 1, player 3 withholds.
#
#    integer TRUEL_NUM, the number of truels to run.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real S(*), the estimated probablity that player I will survive.
#
#    real TURN_AVERAGE, the average number of turns required to
#    complete the truel.
#
  import numpy as np

  print ( '' )
  print ( 'truel_simulation():' )
 
  player_num = len ( p )

  s = np.zeros ( player_num )
  turn_average = 0

  for duel in range ( 0, truel_num ):

    if ( strategy == 1 ):
      survivor, turn_num = truel_strategy1 ( p, rng )
    elif ( strategy == 2 ):
      survivor, turn_num = truel_strategy2 ( p, rng )
    elif ( strategy == 3 ):
      survivor, turn_num = truel_strategy3 ( p, rng )
    elif ( strategy == 4 ):
      survivor, turn_num = truel_strategy4 ( p, rng )

    s[survivor] = s[survivor] + 1
    turn_average = turn_average + turn_num

  s = s / truel_num
  turn_average = turn_average / truel_num

  return s, turn_average

def truel_strategy1 ( p, rng ):

#*****************************************************************************80
#
## truel_strategy1() returns the outcome of a truel with strategy 1.
#
#  Discussion
#
#    Strategy 1:
#
#    * Each player chooses the opponent with highest accuracy as target.
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
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(*), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer SURVIVOR, the survivor.
#
  import numpy as np

  player_num = len ( p )
  alive_num = player_num
  q = p.copy()

  turn_num = 0
 
  while ( True ):

    for i in range ( 0, player_num ):
#
#  Use the Q vector to keep track of who's alive, and who's worth
#  shooting at.  To avoid shooting yourself, temporarily zero your
#  own P value.
#
      if ( 0.0 < q[i] ):

        turn_num = turn_num + 1

        q_save = q[i]
        q[i] = 0.0

        q_max = np.max ( q )
        target = np.argmax ( q )

        r = rng.random ( )
        if ( r <= q_save ):
          q[target] = 0.0
          alive_num = alive_num - 1
          if ( alive_num == 1 ):
            survivor = i
            return survivor, turn_num

        q[i] = q_save

  return survivor, turn_num

def truel_strategy2 ( p, rng ):

#*****************************************************************************80
#
## truel_strategy2() returns the outcome of a truel with strategy 2.
#
#  Discussion
#
#    Strategy 2:
#
#    * Each player fires at the "next" player.  0->1, 1->2, 2->0
#      until there are only two players.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(*), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer SURVIVOR, the survivor.
#
  import numpy as np

  player_num = len ( p )
  alive_num = player_num
  q = p.copy()

  turn_num = 0
 
  while ( True ):

    for i in range ( 0, player_num ):
#
#  Use the Q vector to keep track of who's alive, and who's worth
#  shooting at.  To avoid shooting yourself, temporarily zero your
#  own P value.
#
      if ( 0.0 < q[i] ):

        turn_num = turn_num + 1
#
#  Choose target.
#
        ip1 = ( i + 1 ) % 3
        ip2 = ( i + 2 ) % 3
        if ( 0 < q[ip1] ):
          target = ip1
        else:
          target = ip2
#
#  Fire at target
#
        r = rng.random ( )
        if ( r <= q[i] ):
          q[target] = 0.0
          alive_num = alive_num - 1
          if ( alive_num == 1 ):
            survivor = i
            return survivor, turn_num

  return survivor, turn_num

def truel_strategy3 ( p, rng ):

#*****************************************************************************80
#
## truel_strategy3() returns the outcome of a truel with strategy 3.
#
#  Discussion
#
#    Strategy 3:
#
#    * Each player fires at a random opponent.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(*), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer SURVIVOR, the survivor.
#
  import numpy as np

  player_num = len ( p )
  alive_num = player_num
  q = p.copy()

  turn_num = 0
 
  while ( True ):

    for i in range ( 0, player_num ):
#
#  Use the Q vector to keep track of who's alive, and who's worth
#  shooting at.  To avoid shooting yourself, temporarily zero your
#  own P value.
#
      if ( 0.0 < q[i] ):

        turn_num = turn_num + 1
#
#  Choose target.
#
        ip1 = ( i + 1 ) % 3
        ip2 = ( i + 2 ) % 3
        if ( 0 == q[ip1] ):
          target = ip2
        elif ( 0 == q[ip2] ):
          target = ip1
        else:
          r = rng.random ( )
          if ( r <= 0.0 ):
            target = ip1
          else:
            target = ip2
#
#  Fire at target
#
        r = rng.random ( )
        if ( r <= q[i] ):
          q[target] = 0.0
          alive_num = alive_num - 1
          if ( alive_num == 1 ):
            survivor = i
            return survivor, turn_num

  return survivor, turn_num

def truel_strategy4 ( p, rng ):

#*****************************************************************************80
#
## truel_strategy4() returns the outcome of a truel with strategy 4.
#
#  Discussion
#
#    Strategy 4:
#
#    * The player with the highest accuracy will always aim at the player
#      with the next highest accuracy.
#    * The player with the medium accuracy will always aim at the player
#      with the highest accuracy if that player is dead, then the player
#      will aim at the player with lowest accuracy.
#    * The player with lowest accuracy will aim at NO ONE, as long as
#      the other two players are both alive.  Once there is only one
#      opponent, he will aim at that opponent.  
#
#    With the probabilities ( 2/6, 4/6, 5/6), the weakest player has about 
#    a 70% chance of surviving, using this strategy.
#
#    With the probabilities ( 5/6, 4/6, 2/6), the weakest player has about
#    a 40% chance of surviving.
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
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(*), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer SURVIVOR, the survivor.
#
  import numpy as np

  player_num = len ( p )
  alive_num = player_num
  p_min = np.min ( p )
  p_max = np.max ( p )
#
#  Make a copy of P that we can manipulate.
#
  q = p.copy()

  turn_num = 0
 
  while ( True ):

    for i in range ( 0, player_num ):
#
#  Use the Q vector to keep track of who's alive, and who's worth
#  shooting at.  To avoid shooting yourself, temporarily zero your
#  own P value.
#
      if ( 0.0 < q[i] ):

        turn_num = turn_num + 1
#
#  If there's more than one other player,
#  and you're the worst player,
#  and you're strictly a worst player,
#  then don't do anything.
#
        if ( 2 < alive_num and q[i] == p_min and p_min < p_max ):

          continue
#
#  Otherwise, aim at the target (highest opponent) and
#  hit them with your accuracy.
#
        else:

          q_save = q[i]
          q[i] = 0.0
          q_target = np.max ( q )
          target = np.argmax ( q )
          r = rng.random ( )

          if ( r <= q_save ):
            q[target] = 0.0
            alive_num = alive_num - 1
            if ( alive_num == 1 ):
              survivor = i
              return survivor, turn_num

          q[i] = q_save

  return survivor, turn_num
 
def truel_simulation_test ( ):

#*****************************************************************************80
#
## truel_simulation_test() tests truel_simulation().
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
  print ( 'truel_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test truel_simulation().' )

  rng = default_rng ( )

  for strategy in [ 1, 2, 3, 4 ]:

    p = np.array ( [ 2/6, 4/6, 5/6 ] )
    truel_num = 1000
    s, turn_average = truel_simulation ( p, strategy, truel_num, rng )

    print ( '' )
    print ( '  Truel statistics estimated from', truel_num, 'simulations' )
    print ( '  Strategy = ', strategy )
    print ( '  Average number of shots fired =', turn_average )
    print ( '' )
    print ( '  Player  Accuracy  Survival' )
    print ( '' )
    for i in range ( 0, 3 ):
      print ( '  %d  %8.2f  %8.2f'% ( i, p[i], s[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'truel_simulation_test():' )
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
  truel_simulation_test ( )
  timestamp ( )

