#! /usr/bin/env python3
#
def sudoku_solve ( grid, row_nr, col_nr ):

#*****************************************************************************80
#
## sudoku_solve() uses recursion to solve a sudoku problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 July 2025
#
#  Reference:
#
#    Parineeth MR,
#    The Big Book of Coding Interviews in Python,
#    Third Edition, 2018
#    ISBN13: 978-1983861185
#
  NUM_ROWS = 9
  NUM_COLS = 9
#
#  Have we found a solution?
#
  if ( NUM_ROWS <= row_nr ):
    print ( '' )
    print ( '  Sudoku solution:' );
    sudoku_print ( grid )
    return
#
#  Compute the row and column of the next cell.
#
  next_row = row_nr
  next_col = col_nr + 1
  if ( NUM_COLS <= next_col ):
    next_col = 0
    next_row = row_nr + 1
#
#  If the cell has not been assigned a value, see if one can be set.
#
  if ( grid[row_nr][col_nr] == 0 ):
    for num in range ( 1, 10 ):
      if ( can_fill_cell ( grid, row_nr, col_nr, num ) ):
        grid[row_nr][col_nr] = num
        sudoku_solve ( grid, next_row, next_col )
    grid[row_nr][col_nr] = 0
  else:
    sudoku_solve ( grid, next_row, next_col )

  return

def can_fill_cell ( grid, row_nr, col_nr, num ):

#*****************************************************************************80
#
## can_fill_cell() determines if a given cell can accept a given digit.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 July 2025
#
#  Reference:
#
#    Parineeth MR,
#    The Big Book of Coding Interviews in Python,
#    Third Edition, 2018
#    ISBN13: 978-1983861185
#
  NUM_ROWS = 9
  NUM_COLS = 9

  for i in range ( NUM_ROWS ):
    if ( grid[i][col_nr] == num ):
      return False

  for j in range ( NUM_COLS ):
    if ( grid[row_nr][j] == num ):
      return False

  region_start_row = ( row_nr // 3 ) * 3
  region_start_col = ( col_nr // 3 ) * 3

  for i in range ( region_start_row, region_start_row + 3 ):
    for j in range ( region_start_col, region_start_col + 3 ):
      if ( grid[i][j] == num ):
        return False

  return True

def sudoku_test ( ):

#*****************************************************************************80
#
## sudoku_test() tests sudoku().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'sudoku_test():' )
  print ( '  python version: ' + platform.python_version ( ) )

  grid = [ \
    [ 0, 1, 0, 0, 5, 4, 0, 8, 7 ], \
    [ 8, 0, 2, 0, 0, 7, 0, 5, 0 ], \
    [ 3, 7, 0, 2, 0, 0, 0, 4, 0 ], \
    [ 1, 2, 8, 0, 7, 5, 0, 0, 0 ], \
    [ 0, 0, 9, 0, 4, 2, 6, 0, 1 ], \
    [ 7, 0, 4, 9, 0, 0, 0, 2, 0 ], \
    [ 0, 0, 0, 0, 0, 6, 3, 0, 4 ], \
    [ 6, 5, 1, 4, 0, 0, 0, 0, 0 ], \
    [ 0, 8, 0, 0, 1, 9, 5, 0, 0 ] ]

  print ( '' )
  print ( '  Sudoku puzzle:' );
  sudoku_print ( grid )

  row_nr = 0
  col_nr = 0

  sudoku_solve ( grid, row_nr, col_nr )
#
#  Terminate.
#
  print ( '' )
  print ( 'sudoku_test():' )
  print ( '  Normal end of execution.' )
  return

def sudoku_print ( S ):

#*****************************************************************************80
#
## sudoku_print() prints a partial or filled-in Sudoku puzzle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer S(9,9) contains the Sudoku puzzle.  Each
#    0 entry is interpreted as an empty cell.  Otherwise, it
#    is assumed that an entry is an integer between 1 and 9.
#
  i = 0
  print ( '  +---------+---------+---------+' )
  for i3 in range ( 0, 3 ):
    for i2 in range ( 0, 3 ):
      j = 0
      print ( '  |', end = '' )
      for j3 in range ( 0, 3 ):
        for j2 in range ( 0, 3 ):

          if ( S[i][j] == 0 ):
            s = '_'
          else:
            s = str ( S[i][j] )
          print ( ' ' + s + ' ', end = '' )

          j = j + 1
        print ( '|', end = '' )
      print ( '' )
      i = i + 1
    print ( '  +---------+---------+---------+' )

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
  sudoku_test ( )
  timestamp ( )

