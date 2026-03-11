#! /usr/bin/env python3
#
def usa_box_plot_test ( ):

#*****************************************************************************80
#
## usa_box_plot_test() tests usa_box_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'usa_box_plot_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  usa_box_plot() uses boxes to suggest a map of the USA.' )

  election_box_plot ( )
  starbucks_box_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'usa_box_plot_test():' )
  print ( '  Normal end of execution.' )

  return

def box_fill ( m, i, j, color, label1, label2 ):

#*****************************************************************************80
#
## box_fill() plots a filled unit square centered at matrix position (I,J)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    integer I, J, the matrix indices of the box.
#
#    color COLOR, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The box is filled with this color.
#
#    character vector LABEL1: a short label, usually the state abbreviation.
#
#    character vector LABEL2: a short label to print below the first.
#
  import matplotlib.pyplot as plt

  xc = j - 0.5
  yc = m - i + 0.5

  r = 0.45

  a = xc - r
  b = xc + r
  c = yc - r
  d = yc + r

  plt.fill ( [ a, b, b, a ], [ c, c, d, d ], color )
#
#  Place the texts.
#
  plt.text ( xc, yc, label1, horizontalalignment = 'center' )

  plt.text ( xc, yc-0.25, label2, horizontalalignment = 'center' )

  return

def election_box_plot ( ):

#*****************************************************************************80
#
## election_box_plot() creates a box plot of the USA election results.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Set up a 8x11 board of gray cells on a white background.
#
  plt.clf ( )

  m = 8
  n = 11
  r = 0.45

  d = 0.0
#
#  Fill the rectangle with the background color.
#  If I specify the color [1,1,1], which should be WHITE, I get BLACK.  Morons!
#
  plt.fill ( [ -d, n+d, n+d, -d ], [ -d, -d, m+d, m+d ], 'w' )

  for i in range ( 1, m + 1 ):
    for j in range ( 1, n + 1 ):
      box_fill ( m, i, j, 'w', '', '' )
#
#  Place red and blue squares.
#
  box_fill ( m, 1, 1, 'tomato', 'AK', '3' )
  box_fill ( m, 3, 1, 'lightblue', 'WA', '12' )
  box_fill ( m, 4, 1, 'lightblue', 'OR', '7' )
  box_fill ( m, 5, 1, 'lightblue', 'CA', '55' )
  box_fill ( m, 8, 1, 'lightblue', 'HI', '4' )

  box_fill ( m, 3, 2, 'tomato', 'ID', '4' )
  box_fill ( m, 4, 2, 'tomato', 'UT', '6' )
  box_fill ( m, 5, 2, 'lightblue', 'NV', '6' )
  box_fill ( m, 6, 2, 'lightblue', 'AZ', '11' )

  box_fill ( m, 3, 3, 'tomato', 'MT', '3' )
  box_fill ( m, 4, 3, 'tomato', 'WY', '3' )
  box_fill ( m, 5, 3, 'lightblue', 'CO', '9' )
  box_fill ( m, 6, 3, 'lightblue', 'NM', '5' )

  box_fill ( m, 3, 4, 'tomato', 'ND', '3' )
  box_fill ( m, 4, 4, 'tomato', 'SD', '3' )
  box_fill ( m, 5, 4, 'tomato', 'NE', '5' )
  box_fill ( m, 6, 4, 'tomato', 'KS', '6' )
  box_fill ( m, 7, 4, 'tomato', 'OK', '7' )
  box_fill ( m, 8, 4, 'tomato', 'TX', '38' )

  box_fill ( m, 3, 5, 'lightblue', 'MN', '10' )
  box_fill ( m, 4, 5, 'tomato', 'IA', '6' )
  box_fill ( m, 5, 5, 'tomato', 'MO', '10' )
  box_fill ( m, 6, 5, 'tomato', 'AR', '6' )
  box_fill ( m, 7, 5, 'tomato', 'LA', '8' )

  box_fill ( m, 4, 6, 'lightblue', 'WI', '10' )
  box_fill ( m, 5, 6, 'lightblue', 'IL', '20' )
  box_fill ( m, 6, 6, 'tomato', 'TN', '11' )
  box_fill ( m, 7, 6, 'tomato', 'MS', '6' )

  box_fill ( m, 4, 7, 'lightblue', 'MI', '16' )
  box_fill ( m, 5, 7, 'tomato', 'IN', '11' )
  box_fill ( m, 6, 7, 'tomato', 'KY', '8' )
  box_fill ( m, 7, 7, 'tomato', 'AL', '9' )

  box_fill ( m, 3, 8, 'tomato', 'OH', '18' )
  box_fill ( m, 4, 8, 'tomato', 'WV', '5' )
  box_fill ( m, 5, 8, 'tomato', 'NC', '15' )
  box_fill ( m, 6, 8, 'tomato', 'SC', '9' )
  box_fill ( m, 7, 8, 'lightblue', 'GA', '16' )
  box_fill ( m, 8, 8, 'tomato', 'FL', '29' )

  box_fill ( m, 3, 9, 'lightblue', 'NY', '29' )
  box_fill ( m, 4, 9, 'lightblue', 'PA', '20' )
  box_fill ( m, 5, 9, 'lightblue', 'MD', '10' )
  box_fill ( m, 6, 9, 'lightblue', 'VA', '13' )

  box_fill ( m, 2, 10, 'lightblue', 'VT', '3' )
  box_fill ( m, 3, 10, 'lightblue', 'CT', '7' )
  box_fill ( m, 4, 10, 'lightblue', 'NJ', '14' )
  box_fill ( m, 5, 10, 'lightblue', 'DE', '3' )
  box_fill ( m, 6, 10, 'lightblue', 'DC', '3' )

  box_fill ( m, 1, 11, 'lightblue', 'ME', '4' )
  box_fill ( m, 2, 11, 'lightblue', 'NH', '4' )
  box_fill ( m, 3, 11, 'lightblue', 'MA', '11' )
  box_fill ( m, 4, 11, 'lightblue', 'RI', '4' )
  box_fill ( m, 8, 11, 'lightgray', 'PR', '0' )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  filename = 'election_box_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def starbucks_box_plot ( ):

#*****************************************************************************80
#
## starbucks_box_plot() creates a box plot of Yanzhi Zhang's Starbucks cups.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Set up a 8x11 board of gray cells on a white background.
#
  plt.clf ( )
  m = 8
  n = 11
  r = 0.45

  d = max ( 0.5 - r,  0.0 )
#
#  Fill the rectangle with the background color.
#  If I specify the color [1,1,1], which should be WHITE, I get BLACK.  Morons!
#
  plt.fill ( [ -d, n+d, n+d, -d ], [ -d, -d, m+d, m+d ], 'white' )

  for i in range ( 1, m + 1 ):

    for j in range ( 1, n + 1 ):

      box_fill ( m, i, j, 'white', '', '' )
#
#  Place red and blue squares.
#
  box_fill ( m, 1, 1, 'tomato', 'AK', '' )
  box_fill ( m, 3, 1, 'lightblue', 'WA', '' )
  box_fill ( m, 4, 1, 'tomato', 'OR', '' )
  box_fill ( m, 5, 1, 'tomato', 'CA', '' )
  box_fill ( m, 8, 1, 'tomato', 'HI', '' )

  box_fill ( m, 3, 2, 'tomato', 'ID', '' )
  box_fill ( m, 4, 2, 'tomato', 'UT', '' )
  box_fill ( m, 5, 2, 'tomato', 'NV', '' )
  box_fill ( m, 6, 2, 'tomato', 'AZ', '' )

  box_fill ( m, 3, 3, 'tomato', 'MT', '' )
  box_fill ( m, 4, 3, 'tomato', 'WY', '' )
  box_fill ( m, 5, 3, 'lightblue', 'CO', '' )
  box_fill ( m, 6, 3, 'lightblue', 'NM', '' )

  box_fill ( m, 3, 4, 'tomato', 'ND', '' )
  box_fill ( m, 4, 4, 'tomato', 'SD', '' )
  box_fill ( m, 5, 4, 'lightblue', 'NE', '' )
  box_fill ( m, 6, 4, 'lightblue', 'KS', '' )
  box_fill ( m, 7, 4, 'lightblue', 'OK', '' )
  box_fill ( m, 8, 4, 'tomato', 'TX', '' )

  box_fill ( m, 3, 5, 'tomato', 'MN', '' )
  box_fill ( m, 4, 5, 'lightblue', 'IA', '' )
  box_fill ( m, 5, 5, 'lightblue', 'MO', '' )
  box_fill ( m, 6, 5, 'lightblue', 'AR', '' )
  box_fill ( m, 7, 5, 'tomato', 'LA', '' )

  box_fill ( m, 4, 6, 'tomato', 'WI', '' )
  box_fill ( m, 5, 6, 'lightblue', 'IL', '' )
  box_fill ( m, 6, 6, 'lightblue', 'TN', '' )
  box_fill ( m, 7, 6, 'tomato', 'MS', '' )

  box_fill ( m, 4, 7, 'tomato', 'MI', '' )
  box_fill ( m, 5, 7, 'lightblue', 'IN', '' )
  box_fill ( m, 6, 7, 'lightblue', 'KY', '' )
  box_fill ( m, 7, 7, 'tomato', 'AL', '' )

  box_fill ( m, 3, 8, 'tomato', 'OH', '' )
  box_fill ( m, 4, 8, 'tomato', 'WV', '' )
  box_fill ( m, 5, 8, 'tomato', 'NC', '' )
  box_fill ( m, 6, 8, 'lightblue', 'SC', '' )
  box_fill ( m, 7, 8, 'tomato', 'GA', '' )
  box_fill ( m, 8, 8, 'lightblue', 'FL', '' )

  box_fill ( m, 3, 9, 'tomato', 'NY', '' )
  box_fill ( m, 4, 9, 'lightblue', 'PA', '' )
  box_fill ( m, 5, 9, 'tomato', 'MD', '' )
  box_fill ( m, 6, 9, 'tomato', 'VA', '' )

  box_fill ( m, 2, 10, 'tomato', 'VT', '' )
  box_fill ( m, 3, 10, 'tomato', 'CT', '' )
  box_fill ( m, 4, 10, 'tomato', 'NJ', '' )
  box_fill ( m, 5, 10, 'tomato', 'DE', '' )
  box_fill ( m, 6, 10, 'tomato', 'DC', '' )

  box_fill ( m, 1, 11, 'tomato', 'ME', '' )
  box_fill ( m, 2, 11, 'tomato', 'NH', '' )
  box_fill ( m, 3, 11, 'tomato', 'MA', '' )
  box_fill ( m, 4, 11, 'lightblue', 'RI', '' )
  box_fill ( m, 8, 11, 'tomato', 'PR', '' )
#
#  These two commands apply to the axis of the map.
#
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  plt.title ( 'The Starbucks Collection' )
#
#  These two commands apply to the axis of the Starbucks logo!
#
  plt.axis ( 'equal' )

  filename = 'starbucks_box_plot.png'
  print ( '  Graphics saved as "' + filename + '"' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

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
  usa_box_plot_test ( )
  timestamp ( )

