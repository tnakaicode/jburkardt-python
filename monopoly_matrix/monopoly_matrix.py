#! /usr/bin/env python3
#
def monopoly_chance ( index ):

#*****************************************************************************80
#
## monopoly_chance() returns the text of a chance card.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer INDEX: the index of the card.
#    1 <= INDEX <= 16.
#
#  Output:
#
#    string VALUE: the text of the card.
#
  label = [ \
    "Advance to Boardwalk", \
    "Advance to Go (Collect $200)", \
    "Advance to Illinois Avenue. If you pass Go, collect $200", \
    "Advance to St. Charles Place. If you pass Go, collect $200", \
    "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled", \
    "Advance token to nearest Utility. If unowned, you may buy it from the Bank.  If owned, throw dice and pay owner a total ten times amount thrown.", \
    "Bank pays you dividend of $50", \
    "Get Out of Jail Free", \
    "Go Back 3 Spaces", \
    "Go to Jail.  Go directly to Jail.  Do not pass Go.  Do not collect $200", \
    "Make general repairs on all your property.  For each house pay $25. For each hotel pay $100", \
    "Pay poor tax of $15", \
    "Take a trip to Reading Railroad.  If you pass Go, collect $200", \
    "You have been elected Chairman of the Board.  Pay each player $50", \
    "Your building loan matures. Collect $150" ]

  value = label [ index % 16 ]

  return value

def monopoly_community_chest ( index ):

#*****************************************************************************80
#
## monopoly_community_chest() returns the text of a community chest card.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer INDEX: the index of the card.
#    1 <= INDEX <= 16.
#
#  Output:
#
#    string VALUE: the text of the card.
#
  label = [ \
    "Advance to Go (Collect $200)", \
    "Bank error in your favor. Collect $200", \
    "Doctor's fee. Pay $50", \
    "From sale of stock you get $50", \
    "Get Out of Jail Free", \
    "Go to Jail.  Go directly to jail.  Do not pass Go.  Do not collect $200", \
    "Holiday fund matures. Receive $100", \
    "Income tax refund. Collect $20", \
    "It is your birthday. Collect $10 from every player", \
    "Life insurance matures. Collect $100", \
    "Pay hospital fees of $100", \
    "Pay school fees of $50", \
    "Receive $25 consultancy fee", \
    "You are assessed for street repair.  Pay $40 per house. $115 per hotel", \
    "You have won second prize in a beauty contest. Collect $10", \
    "You inherit $100" ]

  value = label [ index % 16 ]

  return value

def monopoly_labels ( ):

#*****************************************************************************80
#
## monopoly_label() returns the labels for the MONOPOLY matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    cell label(41), the labels.
#
  label = [ \
    "Go", \
    "Mediterranean Avenue", \
    "Community Chest #1", \
    "Baltic Avenue", \
    "Income Tax", \
    "Reading Railroad", \
    "Oriental Avenue", \
    "Chance #1", \
    "Vermont Avenue", \
    "Connecticut Avenue", \
    "Just Visiting", \
    "St Charles Place", \
    "Electric Company", \
    "States Avenue", \
    "Virginia Avenue", \
    "Pennsylvania Railroad", \
    "St James Place", \
    "Community Chest #2", \
    "Tennessee Avenue", \
    "New York Avenue", \
    "Free Parking", \
    "Kentucky Avenue", \
    "Chance #2", \
    "Indiana Avenue", \
    "Illinois Avenue", \
    "B&O Railroad", \
    "Atlantic Avenue", \
    "Ventnor Avenut", \
    "Water Works", \
    "Marvin Gardens", \
    "Go to Jail", \
    "Pacific Avenue", \
    "North Carolina Avenue", \
    "Community Chest #3", \
    "Pennsylvania Avenue", \
    "Short Line Railroad", \
    "Chance #3", \
    "Park Place", \
    "Luxury Tax", \
    "Boardwalk", \
    "Jail" ]

  return label

def monopoly_labels_test ( ):

#*****************************************************************************80
#
## monopoly_labels_test() tests monopoly_labels().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 September 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'monopoly_labels_test():' )
  print ( '  Test monopoly_labels()' )

  label = monopoly_labels ( )

  n = len ( label )

  print ( '' )
  print ( '  Square  Label' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %s' % ( i, label[i] ) )

  return

def monopoly_matrix_test ( ):

#*****************************************************************************80
#
## monopoly_matrix_test() tests monopoly_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'monopoly_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test monopoly_matrix()' )

  monopoly_labels_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'monopoly_matrix_test():' )
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

if ( __name__ == "__main__" ):
  timestamp ( )
  monopoly_matrix_test ( )
  timestamp ( )

