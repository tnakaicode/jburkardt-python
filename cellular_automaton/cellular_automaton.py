#! /usr/bin/env python3
#
def cellular_automaton ( cell_num, step_num ):

#*****************************************************************************80
#
## cellular_automaton() computes the evolution of a rule #30 cellular automaton.
#
#  Discussion:
#
#    Given an initial linear array of 0's and 1's, rule 30 produces a new
#    array using the rules:
#
#      111  110  101  100  011  010  001  000
#       V    V    V    V    V    V    V    V
#       0    0    0    1    1    1    1    0     
#
#    Note that there are 256 = 2^8 possible ways to fill in this output
#    chart, and that rule 30 gets its index by the fact that
#    (0,0,0,1,1,1,1,0) can be interpreted as the binary representation of 30.
#
#    For instance, if the current values of x[4), x[5) and x[6) are
#    0, 1 and 1, respectively, then the new value of x[5) will be 1.
#
#    The first and last entries of the array must be treated specially, since
#    they don't have a left or right neighbor.  One simple treatment is 
#    to assume that there are phantom neighbors whose values are both 0.
#    Another is to enforce periodic boundary conditions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    A New Kind of Science,
#    Wolfram Media, 2002,
#    ISBN13: 978-1579550080,
#    LC: QA267.5.C45.W67.
#
#  Input:
#
#    integer cell_num: the number of cells.
#
#    integer step_num: the number of steps.
#
#  Output:
#
#    integer x[step_num+1,cell_num): the cellular data.
#
  import numpy as np
#
#  Compute the entire X array.
#
  x = np.zeros ( [ step_num + 1, cell_num ], dtype = int  )
#
#  Set the initial condition in row 1.
#
  mid = ( cell_num - 1 ) // 2
  x[0,mid] = 1
#
#  Compute rows 2 through step_num+1 by applying rule 30.
#
  for i in range ( 1, step_num + 1 ):

    for j in range ( 1, cell_num - 1 ):

      if ( ( x[i-1,j-1] == 0 and x[i-1,j] == 0 and x[i-1,j+1] == 1 ) or \
           ( x[i-1,j-1] == 0 and x[i-1,j] == 1 and x[i-1,j+1] == 0 ) or \
           ( x[i-1,j-1] == 0 and x[i-1,j] == 1 and x[i-1,j+1] == 1 ) or \
           ( x[i-1,j-1] == 1 and x[i-1,j] == 0 and x[i-1,j+1] == 0 ) ):
        x[i,j] = 1

  return x

def cellular_automaton_plot ( cell_num, step_num, x ):

#*****************************************************************************80
#
## cellular_automaton_plot() plots the evolution of the rule #30 cellular automaton.
#
#  Discussion:
#
#    Given an initial linear array of 0's and 1's, rule 30 produces a new
#    array using the rules:
#
#      111  110  101  100  011  010  001  000
#       V    V    V    V    V    V    V    V
#       0    0    0    1    1    1    1    0     
#
#    Note that there are 256 = 2^8 possible ways to fill in this output
#    chart, and that rule 30 gets its index by the fact that
#    (0,0,0,1,1,1,1,0) can be interpreted as the binary representation of 30.
#
#    For instance, if the current values of x[4), x[5) and x[6) are
#    0, 1 and 1, respectively, then the new value of x[5) will be 1.
#
#    The first and last entries of the array must be treated specially, since
#    they don't have a left or right neighbor.  Assuming we start with a single
#    1 at the center of the array, we can simply set step_num, the number of
#    steps to take, small enough that the boundary cells never have a chance
#    to affect the computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    A New Kind of Science,
#    Wolfram Media, 2002,
#    ISBN13: 978-1579550080,
#    LC: QA267.5.C45.W67.
#
#  Input:
#
#    integer cell_num: the number of cells.
#
#    integer step_num: the number of steps.
#
#    integer x[step_num+1,cell_num): the cellular data.
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'cellular_automaton_plot():' )
  print ( '  Plot the evolution of the rule #30 cellular automaton.' )
#
#  Now plot the results.
#
  plt.clf ( )

  radius = 0.35
  cr = 'r'
  ck = 'k'
  for i in range ( 0, step_num + 1 ):
    for j in range ( 0, cell_num ):
      if ( x[i,j] == 1 ):
        circle_ij_fill ( step_num + 1, i, j, radius, cr )
#
#  Turn on this option to add open circles corresponding to 0 values.
#
      else:
        if ( False ):
          circle_ij_outline ( step_num + 1, i, j, radius, ck )

  plt.axis ( 'off' )
  plt.axis ( 'equal' )

  filename = 'cellular_automaton.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def cellular_automaton_print ( cell_num, step_num, x ):

#*****************************************************************************80
#
## cellular_automaton_print() prints output from rule #30 cellular automaton.
#
#  Discussion:
#
#    Given an initial linear array of 0's and 1's, rule 30 produces a new
#    array using the rules:
#
#      111  110  101  100  011  010  001  000
#       V    V    V    V    V    V    V    V
#       0    0    0    1    1    1    1    0     
#
#    Note that there are 256 = 2^8 possible ways to fill in this output
#    chart, and that rule 30 gets its index by the fact that
#    (0,0,0,1,1,1,1,0) can be interpreted as the binary representation of 30.
#
#    For instance, if the current values of x[4), x[5) and x[6) are
#    0, 1 and 1, respectively, then the new value of x[5) will be 1.
#
#    The first and last entries of the array must be treated specially, since
#    they don't have a left or right neighbor.  One simple treatment is 
#    to assume that there are phantom neighbors whose values are both 0.
#    Another is to enforce periodic boundary conditions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    A New Kind of Science,
#    Wolfram Media, 2002,
#    ISBN13: 978-1579550080,
#    LC: QA267.5.C45.W67.
#
#  Input:
#
#    integer cell_num: the number of cells.
#
#    integer step_num: the number of steps.
#
#    integer x[step_num+1,cell_num): the cellular data.
#
  import numpy as np

  print ( '' )
  print ( 'cellular_automaton_print():' )
  print ( '' )
  zero_one = np.array ( [ ' ', '*' ] )
  cx = np.zeros ( cell_num, dtype = str )

  for i in range ( 0, step_num + 1 ):
    for j in range ( 0, cell_num ):
      print ( zero_one[x[i,j]], end = '' )
    print ( '' )

  return

def cellular_automaton_test ( ):

#*****************************************************************************80
#
## cellular_automaton_test() tests cellular_automaton().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cellular_automaton_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cellular_automaton().' )

  cell_num = 75
  step_num = ( cell_num - 3 ) // 2

  print ( '' )
  print ( '  Print and plot the evolution of the rule #30 cellular automaton' )
  print ( '  starting with an array of ', cell_num, ' horizontal cells,' )
  print ( '  with a single nonzero cell in the middle.' )
  print ( '  Apply rule #30 for ', step_num, ' steps forward in time.' )
  print ( '' )

  x = cellular_automaton ( cell_num, step_num )

  cellular_automaton_print ( cell_num, step_num, x )

  cellular_automaton_plot ( cell_num, step_num, x )
#
#  Terminate.
#
  print ( '' )
  print ( 'cellular_automaton_test():' )
  print ( '  Normal end of execution.' )

  return

def circle_ij_fill ( m, i, j, r, c ):

#*****************************************************************************80
#
## circle_ij_fill() plots a filled circle in cell (I,J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    real I, J, the indices of the cell.
#
#    real R, the radius of the circle.
#
#    color C, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The circle is filled with this color.
#
  import matplotlib.pyplot as plt
  import numpy as np

  a = np.linspace ( 0.0, 2.0 * np.pi, 25 )
  x =     j - 0.5 + r * np.cos ( a )
  y = m - i + 0.5 + r * np.sin ( a )

  plt.fill ( x, y, color = c, edgecolor = None )

  return

def circle_ij_outline ( m, i, j, r, c ):

#*****************************************************************************80
#
## circle_ij_outline() plots an outlined circle in cell (I,J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    real I, J, the indices of the cell.
#
#    real R, the radius of the circle.
#
#    color C, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The circle is drawn with this color.
#
  import matplotlib.pyplot as plt
  import numpy as np

  a = np.linspace ( 0.0, 2.0 * np.pi, 25 )
  x =     j - 0.5 + r * np.cos ( a )
  y = m - i + 0.5 + r * np.sin ( a )

  plt.plot ( x, y, color = c )

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
  cellular_automaton_test ( )
  timestamp ( )

