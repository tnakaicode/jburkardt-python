#! /usr/bin/env python3
#
def snakes_matrix ( ):

#*****************************************************************************80
#
## snakes_matrix() sets up the Snakes and Ladders transition matrix.
#
#  Discussion:
#
#    Snakes and Ladders, also known as Chutes and Ladders, is a game
#    played on a 10x10 board of 100 squares.  A player can be said to
#    start at square 0, that is, off the board.  The player repeatedly
#    rolls a die, and advances between 1 and 6 steps accordingly.
#    The game is won when the player reaches square 100.  In some versions,
#    the player must reach 100 by exact die count, forfeiting the move
#    if 100 is exceeded in others, reaching or exceeding 100 counts as
#    a win.
#
#    Play is complicated by the existence of snakes and ladders.  On
#    landing on a square that begins a snake or ladder, the player is
#    immediately tranported to another square, which will be lower for
#    a snake, or higher for a ladder.
#
#    Typically, several players play, alternating turns.
#
#    Given a vector V(0:100) which is initially all zero except for the
#    first entry, the matrix-vector product A'*V represents the probabilities
#    that a player starting on square 0 will be on any given square after one
#    roll.  Correspondingly, (A')^2*V considers two moves, and so on.  Thus,
#    repeatedly multiplying by A' reveals the probability distribution 
#    associated with the likelihood of occupying any particular square at a 
#    given turn in the game.  
#
#    There is a single eigenvalue of value 1, whose corresponding eigenvector
#    is all zero except for a final entry of 1, representing a player who
#    has reached square 100.  All other eigenvalues have norm less than 1,
#    corresponding to the fact that there are no other long term steady
#    states or cycles in the game.
#
#    Note that no two descriptions of the Snakes and Ladders board seem to
#    agree.  This is the board described by Nick Berry.  The board described 
#    by Higham and Higham is close to this one, but differs in the description 
#    of two of the jumps.
#
#    While most commentators elect to move immediately from a snake mouth or
#    ladder foot, I have decided there are reasons to treat the game in such a
#    way that when you land on a ladder foot or snake mouth, you stay there
#    as though you had landed on an ordinary square the difference arises on
#    your next turn, when, instead of rolling a die, you move up the ladder
#    or down the snake.  This allows the player to "register" a stop at the
#    given square, may be suitable for certain applications, and makes for
#    a transition matrix whose structure is more obvious to understand.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Steve Althoen, Larry King, Kenneth Schilling,
#    How long is a game of Snakes and Ladders?,
#    The Mathematical Gazette,
#    Volume 77, Number 478, March 1993, pages 71-76.
#
#    Nick Berry,
#    Mathematical Analysis of Chutes and Ladders,
#    https://www.datagenetics.com/blog/november12011/index.html
#
#    Desmond Higham, Nicholas Higham,
#    MATLAB Guide,
#    SIAM, 2005,
#    ISBN13: 9780898717891.
#
#  Output:
#
#    real A(1:101,1:101), the matrix.
#
  import numpy as np

  n = 101

  jump = np.arange ( n )

  jump[ 1] =  38
  jump[ 4] =  14
  jump[ 9] =  31
  jump[16] =   6
  jump[21] =  42
  jump[28] =  84
  jump[36] =  44
  jump[48] =  26
  jump[49] =  11
  jump[51] =  67
  jump[56] =  53
  jump[62] =  19
  jump[64] =  60
  jump[71] =  91
  jump[80] = 100
  jump[87] =  24
  jump[93] =  73
  jump[95] =  75
  jump[98] =  78

  A = np.zeros ( [ n, n ] )
#
#  A(I,J) represents the probability that a dice roll will take you from
#  square I to square J.
#
#  Starting in square I...
#
  for i in range ( 0, n ):
#
#  If I is a snake or ladder, go to the next spot.
#
    if ( i != jump[i] ):

      j = jump[i]
      A[i,j] = 1.0
#
#  Otherwise, roll a die
#
    else:

      for die in range ( 1, 7 ):
#
#  so theoretically, our new location J will be I + DIE,
#
        j = i + die
#
#  but if J is greater than 100, move us back to J,
#
        if ( 100 < j ):
          j = 100
  
        A[i,j] = A[i,j] + 1.0 / 6.0

  return A
 
def snakes_matrix_test ( ):

#*****************************************************************************80
#
## snakes_matrix_test() tests snakes_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 March 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'snakes_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  snakes_matrix() constructs the transition matrix for the' )
  print ( '  game of snakes and ladders.' )
#
#  Evaluate the transition matrix for Snakes and Ladders.
#
  A = snakes_matrix ( )
#
#  Use spy to draw an image of the matrix.
#
  plt.spy ( A )
  plt.title ( 'The Snakes and Ladders 101x101 Sparse Matrix' )

  filename = 'snakes_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snakes_matrix_test():' )
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
  snakes_matrix_test ( )
  timestamp ( )


