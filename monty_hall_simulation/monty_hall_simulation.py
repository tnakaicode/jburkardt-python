#! /usr/bin/env python3
#
def monty_hall_simulation ( switch_doors, ndoors = 3 ):

#*****************************************************************************80
#
## monty_hall_simulation() simulates the Monty Hall prize game.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt
#
#  Reference:
#
#    Christian Hill,
#    Learning Scientific Programming With Python,
#    Second Edition,
#    Cambridge University Press, 2020
#    ISBN: 978-1-108-74591-8
#
#  Input:
#
#    boolean switch_doors: True if the user plans to switch.
#
#    integer ndoors: the number of doors.  Usually 3.
#    Must be at least 3.
#
#  Output:
#
#    boolean WIN: 1 if the user chose the prize, 0 otherwise.
#
  import numpy as np
#
#  The prize is hidden behind a random door.
#
  prize_door = np.random.randint ( 1, ndoors + 1 )
#
#  The user chooses a door at random.
#
  chosen_door = np.random.randint ( 1, ndoors + 1 )
#
#  One of the doors is revealed.
#  It is always a door that was not chosen by the user,
#  and which does not contain a prize.
#
  revealable_doors = [ dnum for dnum in range ( 1, ndoors + 1 )
    if dnum not in ( chosen_door, prize_door ) ]

  revealed_door = np.random.choice ( revealable_doors )
#
#  If the user's strategy is to switch, choose one of the 
#  unchosen unrevealed doors.
#
  if ( switch_doors ):

    available_doors = [ dnum for dnum in range ( 1, ndoors + 1 )
      if dnum not in ( chosen_door, revealed_door ) ]

    chosen_door = np.random.choice ( available_doors )
#
#  Did the user win?
#
  win = ( chosen_door == prize_door )

  return win

def monty_hall_simulation_test ( ):

#*****************************************************************************80
#
## monty_hall_simulation_test() tests monty_hall_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2022
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt
#
#  Reference:
#
#    Christian Hill,
#    Learning Scientific Programming With Python,
#    Second Edition,
#    Cambridge University Press, 2020
#    ISBN: 978-1-108-74591-8
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'monty_hall_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  monty_hall_simulation() simulates the Monty Hall' )
  print ( '  prize winning game, in which a prize is hidden behind' )
  print ( '  one of several doors.' )

  ntrials = 100000
  print ( '' )
  print ( '  Number of trials = ', ntrials )

  print ( '' )
  print ( 'Doors  No-switch winning      Switch winning' )
  print ( '       Observed  Predicted  Observed  Predicted' )
  print ( '   n                 1/n              n-1/n-2 * 1/n' )

  for ndoors in range ( 3, 11 ):

    switch_doors = False
    wins_noswitch = 0
    for i in range ( ntrials ):
      win = monty_hall_simulation ( switch_doors, ndoors )
      if ( win ):
        wins_noswitch = wins_noswitch + 1
    ratio_noswitch = wins_noswitch / ntrials

    switch_doors = True
    wins_switch = 0
    for i in range ( ntrials ):
      win = monty_hall_simulation ( switch_doors, ndoors )
      if ( win ):
        wins_switch = wins_switch + 1
    ratio_switch = wins_switch / ntrials

    prob_noswitch, prob_switch = monty_hall_probabilities ( ndoors )
    print ( '  %2d  %8.4g  %8.4g  %8.4g  %8.4g' \
      % ( ndoors, ratio_noswitch, prob_noswitch, ratio_switch, prob_switch ) )

  return

def monty_hall_probabilities ( ndoors ):

#*****************************************************************************80
#
## monty_hall_probabilities() returns Monty Hall winning probabilities.
#
#  Discussion:
#
#    For no switch, you have 1/ndoors chance of picking the prize door.
#
#    For switch, you have 1/ndoors chance of switching from the prize door,
#    so a (ndoors-1)/ndoors chance of having a second chance at the prize.
#    In this second chance, there are ndoors-2 doors, and so you have a
#    1/(ndoors-2) chance of success.  Thus, overall, you have a
#    (ndoors-1)/ndoors * 1/(ndoors-2) chance of rejecting a nonprize 
#    initial selection and successfully choosing the prize on your
#    second guess.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ndoors: the number of doors.
#
#  Output:
#
#    real prob_noswitch, prob_switch: the probability of winning the 
#    Monty Hall game with no-switch or switch strategies.
#
  prob_noswitch = 1.0 / ndoors
  prob_switch = ( ndoors - 1 ) / ndoors / ( ndoors - 2 )

  return prob_noswitch, prob_switch

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

if ( __name__ == "__main__" ):
  timestamp ( )
  monty_hall_simulation_test ( )
  timestamp ( )

