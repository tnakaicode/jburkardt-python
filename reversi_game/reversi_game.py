#! /usr/bin/env python3
#
WIDTH = 8
HEIGHT = 8

def reversi_game ( ):

#*****************************************************************************80
#
## reversi_game() pits a player against the computer in a reversi game.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 June 2025
#
#  Author:
#
#    Original Python version by Al Sweigart.
#    This version by John Burkardt
#
#  Reference:
#
#    Al Sweigart,
#    Invent your own computer games with Python,
#    4th Edition, 2017,
#    No Starch Press,
#    ISBN13: 978-1-59327-795-4
#    LC: QA76.76.C672
#
  import platform
  import sys

  print ( 'reversi_game():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  reversi_game() plays the game of Reversi or Othello.' )
  print ( '' )

  playerTile, computerTile = enterPlayerTile ( )

  while ( True ):

    finalBoard = playGame ( playerTile, computerTile )
#
#  Display the final score.
#
  drawBoard ( finalBoard )
  scores = getScoreOfBoard ( finalBoard )
  print ( 'X scored', scores['X'], ' O scored', scores['O'] )

  if ( scores[computerTile] < scores[playerTile] ):
    print ( 'You won by', scores[playerTile] - scores[computerTile], 'points' )
  elif ( scores[playerTile] < scores[computerTile] ):
    print ( 'Computer won by', scores[computerTile] - scores[playerTile], 'points' )
  else:
    print ( 'The game was a tie.' )

  print ( 'Play again? (y/n)' )
  if not input().lower().startswith ( 'y' ):
    sys.exit ( )

  return

def drawBoard ( board ):

## drawBoard() draws the board.
#
  print ( '  12345678' )
  print ( ' +--------+' )
  for y in range ( HEIGHT ):
    print ( '%s|' % ( y + 1 ), end = '' )
    for x in range ( WIDTH ):
      print ( board[x][y], end = '' )
    print ( '|%s' % ( y + 1 ) )
  print ( ' +--------+' )
  print ( '  12345678' )

  return

def getNewBoard ( ):

## getNewBoard() returns a blank board.

  board = []
  for i in range ( WIDTH ):
    board.append ( [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ] )

  return board

def isValidMove ( board, tile, xstart, ystart ):

## isValidMove() flips tiles corresponding to a player's move.

  if ( board[xstart][ystart] != ' ' ):
    return False
  elif ( not isOnBoard ( xstart, ystart ) ):
    return False

  if ( tile == 'X' ):
    otherTile = 'O'
  else:
    otherTile = 'X'

  tilesToFlip = []

  for xdirection, ydirection in \
    [ [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1] ]:
    x, y = xstart, ystart
    x = x + xdirection
    y = y + ydirection
#
#  Keep moving in this direction.
#
    while ( isOnBoard ( x, y ) and board[x][y] == otherTile ):
      x = x + xdirection
      y = y + ydirection
#
#  There are pieces to flip over.
#
      if ( isOnBoard ( x, y ) and board[x][y] == tile ):
        while ( True ):
          x = x - xdirection
          y = y - ydirection
          if ( x == xstart and y == ystart ):
            break
          tilesToFlip.append ( [ x, y ] )

  if ( len ( tilesToFlip ) == 0 ):
    return False

  return tilesToFlip

def isOnBoard ( x, y ):

## isOnBoard() reports whether (x,y) is a legal board position.

  if ( 0 <= x and x <= WIDTH - 1 and 0 <= y and y <= HEIGHT - 1 ):
    value = True
  else:
    value = False

  return value

def getBoardWithValidMoves ( board, tile ):

## getBoardWithValidMoves() returns a board showing valid moves for player.

  boardCopy = getBoardCopy ( board )

  for x, y in getValidMoves ( boardCopy, tile ):
    boardCopy[x][y] = '.'

  return boardCopy

def getValidMoves ( board, tile ):

## getValidMoves() returns a list of valid player moves.

  validMoves = []
  for x in range ( WIDTH ):
    for y in range ( HEIGHT ):
      if ( isValidMove ( board, tile, x, y ) != False ):
        validMoves.append( [ x, y ] )

  return validMoves

def getScoreOfBoard ( board ):

## getScoreOfBoard() returns the scores as a dictionary.

  xscore = 0
  oscore = 0
  for x in range ( WIDTH ):
    for y in range ( HEIGHT ):
      if ( board[x][y] == 'X' ):
        xscore = xscore + 1
      if ( board[x][y] == 'O' ):
        oscore = oscore + 1

  return { 'X':xscore, 'O':oscore }

def enterPlayerTile ( ):

## enterPlayerTile() lets the player choose the tile.

  tile = ''
  while not ( tile == 'X' or tile == 'O' ):
    print ( 'Do you want to be X or O' )
    tile = input().upper ( )

  if ( tile == 'X' ):
    return [ 'X', 'O' ]
  else:
    return [ 'O', 'X' ]

def whoGoesFirst ( ):

## whoGoesFirst() randomly choose who goes first.

  import random

  if ( random.randint ( 0, 1 ) == 0 ):
    return 'computer'
  else:
    return 'player'

def makeMove ( board, tile, xstart, ystart ):

## makeMove() places the tile at (xstart,ystart) and makes flips.

  tilesToFlip = isValidMove ( board, tile, xstart, ystart )

  if ( tilesToFlip == False ):
    return False

  board[xstart][ystart] = tile
  for x, y in tilesToFlip:
    board[x][y] = tile

  return True

def getBoardCopy ( board ):

## Return a copy of the current board.

  boardCopy = getNewBoard ( )

  for x in range ( WIDTH ):
    for y in range ( HEIGHT ):
      boardCopy[x][y] = board[x][y]

  return boardCopy

def isOnCorner ( x, y ):

## isOnCorner() is True if the position is a corner.

  value = ( ( x == 0 or x == WIDTH - 1 ) and 
            ( y == 0 or y == HEIGHT - 1 ) )

  return value

def getPlayerMove ( board, playerTile ):

## getPlayerMove() lets the player enter their move.

  DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()

  while ( True ):

    print ( 'Enter your move (x,y), or "quit" or "hints".' )
    move = input().lower()

    if ( move == 'quit' or move == 'hints' ):
      return move

    if ( len ( move ) == 2 and 
      move[0] in DIGITS1TO8 and 
      move[1] in DIGITS1TO8 ):
      x = int ( move[0] ) - 1
      y = int ( move[1] ) - 1
#
#  I think this can be simplified, but it is misbehaving...
#
      if ( isValidMove ( board, playerTile, x, y ) == False ):
        continue
      else:
        break

    print ( 'That is not a valid move.' )

  return [ x, y ]

def getComputerMove ( board, computerTile ):

## getComputerMove() determines where the computer should move.

  import random

  possibleMoves = getValidMoves ( board, computerTile )
  random.shuffle ( possibleMoves )

  for x, y in possibleMoves:
    if ( isOnCorner ( x, y ) ):
      return [ x, y ]

  bestMove = [ -1, -1 ]
  bestScore = -1
  for x, y in possibleMoves:
    boardCopy = getBoardCopy ( board )
    makeMove ( boardCopy, computerTile, x, y )
    score = getScoreOfBoard ( boardCopy )[computerTile]
    if ( bestScore < score ):
      bestMove = [ x, y ]
      bestScore = score

  return bestMove

def printScore ( board, playerTile, computerTile ):

## printScore() prints the scores.

  scores = getScoreOfBoard ( board )

  print ( '' )
  print ( 'Current scores:' )
  print ( 'You:     ', scores[playerTile] )
  print ( 'Computer:', scores[computerTile] )

  return

def playGame ( playerTile, computerTile ):

## playGame() plays the game.

  import sys

  showHints = False
  turn = whoGoesFirst ( )
  print ( 'The ' + turn + ' will go first.' )
#
#  Set up the board.
#
  board = getNewBoard ( )
  board[3][3] = 'X'
  board[3][4] = 'O'
  board[4][3] = 'O'
  board[4][4] = 'X'

  while ( True ):

    playerValidMoves = getValidMoves ( board, playerTile )
    computerValidMoves = getValidMoves ( board, computerTile )

    if ( playerValidMoves == [] and
         computerValidMoves == [] ):
      return board

    elif ( turn == 'player' ):

      if ( playerValidMoves != [] ):

        if ( showHints ):
          validMovesBoard = getBoardWithValidMoves ( board, playerTile )
          drawBoard ( validMovesBoard )
        else:
          drawBoard ( board )

        printScore ( board, playerTile, computerTile )
        move = getPlayerMove ( board, playerTile )

        if ( move == 'quit' ):
          print ( 'Thanks for playing!' )
          sys.exit ( )
        elif ( move == 'hints' ):
          showHints = not showHints
          continue
        else:
          makeMove ( board, playerTile, move[0], move[1] )

      turn = 'computer'

    elif ( turn == 'computer' ):

      if ( computerValidMoves ):
        drawBoard ( board )
        printScore ( board, playerTile, computerTile )
        input ( 'Press ENTER to see the computer\'s move.' )
        move = getComputerMove ( board, computerTile )
        makeMove ( board, computerTile, move[0], move[1] )

      turn = 'player'

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
  reversi_game ( )
  timestamp ( )


