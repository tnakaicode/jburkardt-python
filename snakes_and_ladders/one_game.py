#! /usr/bin/env python3
#
def one_game ( ):

#*****************************************************************************80
#
## ONE_GAME plays one game of Snakes and Ladders, printing every move.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from numpy.random import random_integers  
#
#  FINAL[I] indicates where you end up if your die roll takes you to square I.
#
  final = np.linspace ( 0, 100, 101, dtype = np.int32 )

  final[ 1] =  38
  final[ 4] =  14
  final[ 9] =  31
  final[16] =   6
  final[21] =  42
  final[28] =  84
  final[36] =  44
  final[48] =  26
  final[49] =  11
  final[51] =  67
  final[56] =  53
  final[62] =  10
  final[64] =  60
  final[71] =  91
  final[80] = 100
  final[87] =  24
  final[93] =  73
  final[95] =  75
  final[98] =  78
#
#  Initial position is 0.
#
  i = 0
  moves = 0
#
#  Play until you reach 100.
#
  while ( i < 100 ):
    d = random_integers ( 1, 6 )
    moves = moves + 1
    print ( 'You rolled %d ' % ( d ), end = '' )
    i = i + d
    print ( 'and moved to %d ' % ( i ), end = '' )
    if ( 100 < i ):
      i = 100
      print ( 'and moved back to %d ' % ( i ), end = '' )
    if ( i < final [ i ] ):
      i = final [ i ]
      print ( 'and took a ladder up to %d ' % ( i ), end = '' )
    elif ( final [ i ] < i ):
      i = final [ i ]
      print ( 'and took a snake down to %d' % ( i ), end = '' )

    if ( 100 <= i ):
      print ( 'and you won after %d moves!' % moves )
    else:
      print ( '.' )

if ( __name__ == '__main__' ):
  one_game ( )

