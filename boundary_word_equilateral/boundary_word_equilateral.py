#! /usr/bin/env python3
#
def boundary_word_equilateral_test ( ):

#*****************************************************************************80
#
## boundary_word_equilateral_test() tests boundary_word_equilateral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'boundary_word_equilateral_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test boundary_word_equilateral().' )

  boolean_to_string_test ( )

  boundary_hexiamond_test ( )
  boundary_is_legal_test ( )
  boundary_plot_test ( )
  boundary_print_test ( )
  boundary_range_test ( )
  boundary_reflect_test ( )
  boundary_representative_test ( )
  boundary_rotate_test ( )
  boundary_snap_test ( )
  boundary_sort_test ( )
  boundary_to_edge_test ( )
  boundary_to_triangle_test ( )
  boundary_to_vertex_test ( )
  boundary_translate_test ( )

  grid_plot_test ( )

  vertex_plot_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'boundary_word_equilateral_test():' )
  print ( '  Normal end of execution.' )

  return

def boolean_to_string ( b ):

#*****************************************************************************80
#
# boolean_to_string() returns 'True' or 'False' depending on a boolean value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    boolean B: the boolean value.
#
#  Output:
#
#    string S: the corresponding string.
#
  if ( b ):
    s = 'True'
  else:
    s = 'False'

  return s

def boolean_to_string_test ( ):

#*****************************************************************************80
#
## boolean_to_string_test() tests boolean_to_string().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boolean_to_string_test():' )
  print ( '  boolean_to_string() creates the string "True" or "False"' )
  print ( '  based on a boolean value.' )
  print ( '  This can be useful when printing boolean results.' )

  print ( '' )
  print ( '   I   isPrime?' )
  print ( '' );

  for i in range ( 1, 11 ):
    b = ( i == 2 ) or ( i == 3 ) or ( i == 5 ) or ( i == 7 )
    s = boolean_to_string ( b )
    print ( '  ', i, '  ', s )

  return

def boundary_gort ( ):

#*****************************************************************************80
#
## boundary_gort(): the boundary word defining the Gort polyiamond.
#
#  Discussion:
#
#    5           x x x x-x x              *      * 4 *
#                 /\  / /                3 5    3    0
#    4         x-x x x x x          * 4 *   *  *    *
#             /    \/ /            3        5 3    0
#    3       x-x x x x x          * 1 *      *    *
#              \    /                  2         0
#    2     x x x x x x                  *       *
#             /     \                  3          5
#    1   x-x-x x x x          * 4 * 4 *             *
#       /         /          3                    0
#    0 x-x-x-x-x-x          * 1 * 1 * 1 * 1 * 1 *
#    J
#    I 0 1 2 3 4 5          Boundary word
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
  import numpy as np

  w = list ( '111110500043355343123443' )

  p = np.array ( [ 0, 0 ] )

  return w, p

def boundary_hexiamond ( index ):

#*****************************************************************************80
#
## boundary_hexiamond(): the boundary word for a hexiamond.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer INDEX: a value between 1 and 12.
#
#  Output:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
  import numpy as np
#
#  bat/chevron
# 
  if ( index == 1 ):
    w = list ( '11004343' )
    p = np.array ( [ 0, 0 ] )
#
#  butterfly
#
  elif ( index == 2 ):
    w = list ( '11504423' )
    p = np.array ( [ 1, 0 ] )
#
#  club/crook
#
  elif ( index == 3 ):
    w = list ( '11044532' )
    p = np.array ( [ 1, 0 ] )
#
#  crown
#
  elif ( index == 4 ):
    w = list ( '11045342' ) 
    p = np.array ( [ 1, 0 ] )
#
#  hexagon
#
  elif ( index == 5 ):
    w = list ( '105432' ) 
    p = np.array ( [ 1, 0 ] )
#
#  lobster
#
  elif ( index == 6 ):
    w = list ( '02055332' )
    p = np.array ( [ 1, 0 ] )
#
#  pistol/signpost
#
  elif ( index == 7 ):
    w =  list ( '01045332' )
    p = np.array ( [ 1, 0 ] )
#
#  rhomboid/bar
#
  elif ( index == 8 ):
    w = list ( '11104443' )
    p = np.array ( [ 0, 0 ] )
#
#  shoe/hook
#
  elif ( index == 9 ):
    w = list ( '10205433' )
    p = np.array ( [ 0, 0 ] )
#
#  snake
#
  elif ( index == 10 ):
    w = list ( '01053432' )
    p = np.array ( [ 1, 0 ] )
#
#  sphinx
#
  elif ( index == 11 ):
    w = list ( '11154533' )
    p = np.array ( [ 0, 0 ] )
#
#  yacht
#
  elif ( index == 12 ):
    w = list ( '11053533' )
    p = np.array ( [ 0, 0 ] )
#
#  Not a valid index.
#
  else:
    w = list ( '' )
    p = np.array ( [] )

  return w, p

def boundary_hexiamond_test ( ):

#*****************************************************************************80
#
## boundary_hexiamond_test() tests boundary_hexiamond().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_hexiamond_test():' )
  print ( '  boundary_hexiamond() returns the boundary word of a hexiamond.' )

  for k in range ( 1, 13, 3 ):
    w, p = boundary_hexiamond ( k )
    name = name_hexiamond ( k )
    name = '  ' + name
    boundary_print ( w, p, name )

  return

def boundary_is_legal ( w, p ):

#*****************************************************************************80
#
## boundary_is_legal() determines if a polyiamond boundary word is legal.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    boolean VALUE: is TRUE if the boundary word is legal.
#
  s = list_to_string ( w )
#
#  Only the characters 0 through 5 can appear.
#
  l = s.count ( '0' ) \
    + s.count ( '1' ) \
    + s.count ( '2' ) \
    + s.count ( '3' ) \
    + s.count ( '4' ) \
    + s.count ( '5' )

  if ( len ( s ) != l ):
    value = False
    return value
#
#  The boundary must close, so right and left, and up and down, 
#  must match.
#
  r = s.count ( '1' ) + s.count ( '2' )
  l = s.count ( '4' ) + s.count ( '5' )
  u = s.count ( '0' ) + s.count ( '5' )
  d = s.count ( '2' ) + s.count ( '3' )

  value = ( ( r == l ) and ( u == d ) )

  return value

def boundary_is_legal_test ( ):

#*****************************************************************************80
#
## boundary_is_legal_test() tests boundary_is_legal().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_is_legal_test():' )
  print ( '  boundary_is_legal() checks whether a polyiamond' )
  print ( '  boundary word is legal.' )
  print ( '' )
  print ( '  Index     Name     Boundary   Legal' )
  print ( '' )

  for k in range ( 1, 13 ):
    w, p = boundary_hexiamond ( k )
    s = list_to_string ( w )
    name = name_hexiamond ( k )
    legal = boundary_is_legal ( w, p )
    tf = boolean_to_string ( legal )
    print ( '  %2d  %10s  %10s    %s' % ( k, name, '"' + s + '"', tf ) )

  return

def boundary_plot ( w, p, color, number ):

#*****************************************************************************80
#
## boundary_plot() plots a polyiamond from its boundary word.
#
#  Discussion:
#
#    The user should call "clf()" before this function.
#    More plotting commands may be issued if preceded by the "hold on"
#    command.
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P(2): the IJ coordinates of the boundary word starting point.
#
#    color COLOR: the color to use.
#
#    logical NUMBER: true if the triangle indices should be printed.
#
  v = boundary_to_vertex ( w, p )

  vertex_plot ( v, color, number )

  return

def boundary_plot_test ( ):

#*****************************************************************************80
#
## boundary_plot_test() tests boundary_plot().
#
#  Discussion:
#
#    5           x x x x-x x
#                 /|  / /
#    4         x-x x x x x
#             /    |/ /
#    3       x-x x x x x
#              |    /
#    2     x x x x x x
#             /    |
#    1   x-x-x x x x
#       /         /
#    0 x-x-x-x-x-x
#
#      0 1 2 3 4 5
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_plot_test():' )
  print ( '  boundary_plot() plots a polyiamond from its boundary word.' )

  w, p = boundary_gort ( )
#
#  Draw the parallelogram grid.
#
  imin, imax, jmin, jmax = boundary_range ( w, p )
  imax = imax + 1
  jmax = jmax + 1

  plt.clf ( )
  r = 0.85
  color_back = 'cyan'
  color_tri =  'yellow'
  number = False
  grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number )
#
#  Draw the polyiamond.
#
  color = 'blue'
  number = True
  boundary_plot ( w, p, color, number )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )
  plt.title ( 'Boundary plot test: gort' )

  filename = 'boundary_plot_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def boundary_print ( w, p, label ):

#*****************************************************************************80
#
## boundary_print() prints the boundary word of a polyiamond.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word. 
#
#    integer P(2): the boundary word start point.
#
#    string LABEL: a label to be printed.  
#
  s = list_to_string ( w )

  print ( '' )
  print ( label )
  print ( '  boundary word:  "' + s + '"' )
  print ( '  base point   :  [', p[0], ',', p[1], ']' )

  return

def boundary_print_test ( ):

#*****************************************************************************80
#
## boundary_print_test() tests boundary_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_print_test():' )
  print ( '  boundary_print() prints a polyiamond' )
  print ( '  from its boundary word.' )

  for k in range ( 1, 13, 3 ):
    w, p = boundary_hexiamond ( k )
    name = name_hexiamond ( k )
    name = '  ' + name
    boundary_print ( w, p, name )
 
  return

def boundary_range ( w, p ):

#*****************************************************************************80
#
## boundary_range() determines the range of a polyiamond from its boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    The polyiamond is drawn by starting at position (0,0) and then following
#    the instructions of the boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    integer IMIN, IMAX, JMIN, JMAX: the I and J ranges of the polyiamond.
#
  imin = p[0]
  imax = p[0]
  jmin = p[1]
  jmax = p[1]

  i = p[0]
  j = p[1]
  
  wn = len ( w )

  for k in range ( 0, wn ):

    if ( w[k] == '0' ):
      j = j + 1
    elif ( w[k] == '1' ):
      i = i + 1
    elif ( w[k] == '2' ):
      i = i + 1
      j = j - 1
    elif ( w[k] == '3' ):
      j = j - 1
    elif ( w[k] == '4' ):
      i = i - 1
    elif ( w[k] == '5' ):
      i = i - 1
      j = j + 1
 
    imin = min ( imin, i )
    imax = max ( imax, i )
    jmin = min ( jmin, j )
    jmax = max ( jmax, j )
 
  return imin, imax, jmin, jmax

def boundary_range_test ( ):

#*****************************************************************************80
#
## boundary_range_test() tests boundary_range().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_range_test():' )
  print ( '  boundary_range() finds the minimum and maximum I and J' )
  print ( '  coordinates of a polyiamond drawn from its boundary word' )
  print ( '  and starting at P.' )
  print ( '' )
  print ( '        Name  Imin  Imax  Jmin  Jmax  Pi  Pj  Word' )
  print ( '' )

  name = 'tiny'
  w, p = boundary_tiny ( )
  s = list_to_string ( w )
  imin, imax, jmin, jmax = boundary_range ( w, p )
  print ( '  %10s  %4d  %4d  %4d  %4d  %2d  %2d  %s' \
    % ( name, imin, imax, jmin, jmax, p[0], p[1], '"'+s+'"' ) )

  for k in range ( 1, 13 ):
    name = name_hexiamond ( k )
    w, p = boundary_hexiamond ( k )
    s = list_to_string ( w )
    imin, imax, jmin, jmax = boundary_range ( w, p )
    print ( '  %10s  %4d  %4d  %4d  %4d  %2d  %2d  %s' \
      % ( name, imin, imax, jmin, jmax, p[0], p[1], '"'+s+'"' ) )
 
  name = 'gort'
  w, p = boundary_gort ( )
  s = list_to_string ( w )
  imin, imax, jmin, jmax = boundary_range ( w, p )
  print ( '  %10s  %4d  %4d  %4d  %4d  %2d  %2d  %s' \
    % ( name, imin, imax, jmin, jmax, p[0], p[1], '"'+s+'"' ) )

  return

def boundary_reflect ( w, p, r ):

#*****************************************************************************80
#
## boundary_reflect() reflects a polyiamond described by a boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    Reflection replaces each character K in the boundary word by 5-K.
#
#  Example:
#
#    w  = '0053422134444'
#    w2 = '5502133421111'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.  
#
#    integer P(2): the starting point.
#
#    integer R: the reflection option.
#    0: no reflection
#    1: reflect about the I axis
#    2: reflect about the J axis
#    3: reflect about both I and J axes.
#
#  Output:
#
#    list W2: the boundary word for the reflected shape.  
#
#    integer P2(2): the starting point for the reflected shape.
#
  c1 = [ '0', '1', '2', '3', '4', '5' ]

  if ( r == 1 ):
    c2 = [ '5', '4', '3', '2', '1', '0' ]
  elif ( r == 2 ):
    c2 = [ '2', '1', '0', '5', '4', '3' ]
  elif ( r == 3 ):
    c2 = [ '3', '4', '5', '0', '1', '2' ]
  else:
    w2 = w.copy()
    p2 = p.copy()
    return w2, p2
#
#  Reflect the boundary word.
#
  w2 = w.copy()
  for i in range ( 0, len ( w ) ):
    for j in range ( 0, 6 ):
      if ( w[i] == c1[j] ):
        w2[i] = c2[j]
#
#  Reflect the base point.
#
  p2 = p.copy()

  if ( r == 1 ):
    p2[0] = - p2[0] - p2[1]
  elif ( r == 2 ):
    p2[0] =   p2[0] + p2[1]
    p2[1] = - p2[1]
  elif ( r == 3 ):
    p2[0] = - p2[0]
    p2[1] = - p2[1]

  return w2, p2

def boundary_reflect_test ( ):

#*****************************************************************************80
#
## boundary_reflect_test() tests boundary_reflect().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_reflect_test():' )
  print ( '  boundary_reflect() is given a polyiamond boundary word' )
  print ( '  to reflect about the x, y, or xy axis.' )

  k = 10
  w0, p0 = boundary_hexiamond ( 10 )
  name0 = name_hexiamond ( k )
  boundary_print ( w0, p0, name0 )

  r1 = 1
  w1, p1 = boundary_reflect ( w0, p0, r1 )
  name1 = 'Reflect r = 1'
  boundary_print ( w1, p1, name1 )

  r2 = 2
  w2, p2 = boundary_reflect ( w0, p0, r2 )
  name2 = 'Reflect r = 2'
  boundary_print ( w2, p2, name2 )

  r3 = 3
  w3, p3 = boundary_reflect ( w0, p0, r3 )
  name3 = 'Reflect r = 3'
  boundary_print ( w3, p3, name3 )
#
#  Get the plot range.
#
  imin0, imax0, jmin0, jmax0 = boundary_range ( w0, p0 )
  imin1, imax1, jmin1, jmax1 = boundary_range ( w1, p1 )
  imin2, imax2, jmin2, jmax2 = boundary_range ( w2, p2 )
  imin3, imax3, jmin3, jmax3 = boundary_range ( w3, p3 )

  imin = min ( 0, imin0, imin1, imin2, imin3 )
  imax = max ( 0, imax0, imax1, imax2, imax3 ) + 1
  jmin = min ( 0, jmin0, jmin1, jmin2, jmin3 )
  jmax = max ( 0, jmax0, jmax1, jmax2, jmax3 ) + 1
#
#  Draw the grid.
#
  plt.clf ( )
  r = 0.85
  color_back = 'cyan'
  color_tri =  'white'
  number = False
  grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number )
#
#  Draw the polyiamonds.
#
  color = 'cyan'
  number = True
  boundary_plot ( w0, p0, color, number )

  color = 'magenta'
  number = True
  boundary_plot ( w1, p1, color, number )

  color = 'yellow'
  number = True
  boundary_plot ( w2, p2, color, number )

  color = 'blue'
  number = True
  boundary_plot ( w3, p3, color, number )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )
  plt.title ( 'boundary reflect test' )

  filename = 'boundary_reflect_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def boundary_representative ( w ):

#*****************************************************************************80
#
## boundary_representative(): representative for a boundary word.
#
#  Discussion:
#
#    Mathematically, a boundary word is a "necklace", that is, an equivalence
#    class of strings of characters, invariant under rotation.  Thus,
#    the following boundary words are in the same equivalence class:
#      '012345', '123450', '234501', '345012', '450123', '501234' 
#
#    This function is given a boundary word, and returns the representative
#    for the class, that is, the lexically first element.
#
#    Two boundary words are equal if and only if they have the same representative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list w: a boundary word.
#
#  Output:
#
#    list wrep: the representative for the boundary word.
#
  n = len ( w )

  for i in range ( 0, n ):

    if ( i == 0 ):
      w1 = w.copy ( )
      s1 = list_to_string ( w1 )
      wrep = w1.copy()
      srep = s1
    else:
      w1 = w1[1:n] + w1[0:1]
      s1 = list_to_string ( w1 )
      if ( s1 < srep ):
        wrep = w1.copy()
        srep = s1

  return wrep
 
def boundary_representative_test ( ):

#*****************************************************************************80
#
## boundary_representative_test() tests boundary_representative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_representative_test():' )
  print ( '  boundary_representative() is given a boundary word, and' )
  print ( '  returns the representative of its equivalence class.' )

  for k in range ( 1, 13 ):
    w, p = boundary_hexiamond ( k )
    name = name_hexiamond ( k )
    name2 = '  ' + name + ':'
    boundary_print ( w, p, name2 )
    w2 = boundary_representative ( w )
    name2 = '  ' + name + ' representative:'
    boundary_print ( w2, p, name2 )

  return

def boundary_rotate ( w, p, r ):

#*****************************************************************************80
#
## boundary_rotate() rotates by k*60 degrees a polyiamond using its boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    Rotation replaces each character K in the boundary word by K+R.
#
#  Example:
#
#    w  = '0053422134444'
#    k  = 2
#    w2 = '2215044350000'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.  
#
#    integer P(2): the boundary word starting point.
#
#    integer R: the number of 60 degree turns clockwise (R positive) or
#    counterclockwise (R negative)
#
#  Output:
#
#    list W2: the boundary word for the reflected shape.  
#
#    integer P2(2): the starting point for the reflected shape.
#
  import numpy as np

  c = [ '0', '1', '2', '3', '4', '5' ]

  w2 = w.copy()

  for i in range ( 0, 6 ):
    for j in range ( 0, len ( w ) ):
      if ( w[j] == c[i] ):
        v = ( i + r ) % 6
        w2[j] = c[v]
#
#  Rotate the base point.
#
  p2 = np.array ( [ p[0], p[1] ] )
#
#  Clockwise
#
  if ( 0 < r ):

    A = np.array ( [ \
      [  1, 1 ], \
      [ -1, 0 ] ] )

    for k in range ( 0, r ):
      p2 = np.matmul ( A, p2 )
#
#  Counterclockwise
#
  elif ( r < 0 ):

    A = np.array ( [ \
      [  0, -1 ], \
      [  1,  1 ] ] )

    for k in range ( 0, - r ):
      p2 = np.matmul ( A, p2 )

  return w2, p2

def boundary_rotate_test ( ):

#*****************************************************************************80
#
## boundary_rotate_test() tests boundary_rotate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_rotate_test():' )
  print ( '  boundary_rotate() rotates a polyiamond' )
  print ( '  described by its boundary word.' )

  for r in range ( 0, 7 ):

    k = 10
    name = name_hexiamond ( k )
    w, p = boundary_hexiamond ( k )
    w2, p2 = boundary_rotate ( w, p, r )
    name2 = 'boundary_rotate_snake_' + str ( r * 60 )
    boundary_print ( w2, p2, name2 )

    plt.clf ( )
    color = 'cyan'
    number = False
    boundary_plot ( w2, p2, color, number )
    plt.title ( name2 )
    filename =  name2 + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )

  return

def boundary_snap ( w, p ):

#*****************************************************************************80
#
## boundary_snap() "snaps" a polyiamond described by its boundary word.
#
#  Discussion:
#
#    We "snap" a polyiamond by translating it so that its least I and
#    least J node coordinates are 0.
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.  
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    list W2: the boundary word for the snapped polyiamond.  
#
#    integer P2(2): the boundary word starting point for the 
#    snapped polyiamond.
#
  import numpy as np

  imin, imax, jmin, jmax = boundary_range ( w, p )

  w2 = w.copy( )
  p2 = np.array ( [ p[0] - imin, p[1] - jmin ] )

  return w2, p2

def boundary_snap_test ( ):

#*****************************************************************************80
#
## boundary_snap_test() tests boundary_snap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'boundary_snap_test():' )
  print ( '  boundary_snap() snaps a polyiamond so that it has' )
  print ( '  minimum I and J node coordinates of 0.' )

  w1, p1 = boundary_tiny ( )
  name1 = 'tiny'
  boundary_print ( w1, p1, name1 )

  d = np.array ( [ 4, 3 ] )
  w2, p2 = boundary_translate ( w1, p1, d )
  name2 = 'tiny + [4,3]'
  boundary_print ( w2, p2, name2 )

  w3, p3 = boundary_snap ( w2, p2 )
  name3 = 'snap ( tiny + [4,3] )'
  boundary_print ( w3, p3, name3 )

  plt.clf ( )
#
#  Draw the parallelogram grid.
#
  v = boundary_to_vertex ( w2, p2 )
  imin = 0
  imax = max ( v[:,0] ) + 1
  jmin = 0
  jmax = max ( v[:,1] ) + 1
  r = 0.85
  color_back = 'cyan'
  color_tri =  'yellow'
  number = False
  grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number )
#
#  Draw the polyiamonds.
#
  color = 'cyan'
  number = True
  boundary_plot ( w2, p2, color, number )

  color = 'red'
  number = True
  boundary_plot ( w3, p3, color, number )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )
  plt.title ( 'boundary snap: cyan snapped to red' )
 
  filename = 'boundary_snap_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def boundary_sort ( w, p ):

#*****************************************************************************80
#
## boundary_sort() sorts the boundary word of a polyiamond.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    Sorting "rotates" the boundary word to produce the lexically smallest 
#    base point P.
#
#  Example:
#
#    w  = 432105, p = [5,10]
#
#    w2 = 321054, p2 = [4,9]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.  
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    list W2: the boundary word for the sorted shape.  
#
#    integer P2(2): the boundary word starting point for the sorted shape.
#
  w2 = w.copy()
  p2 = p.copy()

  wn = len ( w2 )
  p3 = p.copy()

  for i in range ( 0, wn ):

    c = w[i]

    if ( c == '0' ):
      p3[1] = p3[1] + 1
    elif ( c == '1' ):
      p3[0] = p3[0] + 1
    elif ( c == '2' ):
      p3[0] = p3[0] + 1
      p3[1] = p3[1] - 1
    elif ( c == '3' ):
      p3[1] = p3[1] - 1
    elif ( c == '4' ):
      p3[0] = p3[0] - 1
    elif ( c == '5' ):
      p3[0] = p3[0] - 1
      p3[1] = p3[1] + 1

    if ( ( p3[0] < p2[0] ) or \
         ( p3[0] == p2[0] and p3[1] < p2[1] ) ):
      p2 = p3.copy()
      w2 = w[i:] + w[0:i]

  return w2, p2

def boundary_sort_test ( ):

#*****************************************************************************80
#
## boundary_sort_test() tests boundary_sort().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'boundary_sort_test():' )
  print ( '  boundary_sort() is given a polyiamond boundary word' )
  print ( '  and sorts it to have lexically smallest base point.' )

  w = list ( '432105' )
  p = np.array ( [ 5, 10 ] )
  boundary_print ( w, p, '  hexagon boundary word (rotated)' )

  w2, p2 = boundary_sort ( w, p )
  boundary_print ( w2, p2, '  sorted hexagon boundary word' )

  w, p = boundary_hexiamond ( 10 )
  boundary_print ( w, p, '  snake boundary word' )

  w2, p2 = boundary_sort ( w, p )
  boundary_print ( w2, p2, '  sorted snake boundary word' )

  return

def boundary_tiny ( ):

#*****************************************************************************80
#
## boundary_tiny(): the boundary word defining the tiny polyiamond.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    The tiny polyiamond looks like this:
#
#  ^       2 *-------*-------*-------*
#  |        / \     / \     / \     /
#  J       /   \   /   \   /   \   /
#         /  C  \ /     \ /     \ /
#      1 *-------*-------*-------*
#       / \     / \     / \     /
#      /   \ A / B \   /   \   /
#     /     \ /     \ /     \ /
#  0 *-------*-------*-------*
#    0       1       2       3 
#
#                I -->
#
#    Thus, the boundary word for this example can be computed as:
#
#            *-------*-------*-------*
#           / \     / \     / \     /
#          3   5   /   \   /   \   /
#         /     \ /     \ /     \ /
#        *-------*-------*-------*
#       / \     / \     / \     /
#      /   2   /   5   /   \   /
#     /     \ /     \ /     \ /
#    *-------*---1---*-------*
#
#    or, as a string, '21553'.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
  import numpy as np

  w = list ( '21553' )
  p = np.array ( [ 1, 0 ] )

  return w, p

def boundary_to_edge ( w, p ):

#*****************************************************************************80
#
## boundary_to_edge() converts a polyiamond description from boundary to edge.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P with coordinates (i,j), and taking a sequence of 
#    steps of unit length in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    The edge list contains the sequence of parallelogram IJ coordinates
#    of the nodes that lie on the boundary of the polyiamond, listed
#    in counterclockwise order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P(2): the starting point.
#
#  Output:
#
#    integer E(EN,2): the IJ parallelogram point coordinates of the 
#    sequence of nodes that bound the shape.  
#
  import numpy as np

  wn = len ( w )
  e = np.zeros ( [ wn + 1, 2 ], dtype = int )

  i = p[0]
  j = p[1]
  e[0,0] = i
  e[0,1] = j
  c = w[0]

  for wi in range ( 0, wn ):

    c_old = c
    c = w[wi]

    if ( c == '0' ):
      j = j + 1
    elif ( c == '1' ):
      i = i + 1
    elif ( c == '2' ):
      i = i + 1
      j = j - 1
    elif ( c == '3' ):
      j = j - 1
    elif ( c == '4' ):
      i = i - 1
    elif ( c == '5' ):
      i = i - 1
      j = j + 1
    else:
      print ( '' )
      print ( 'boundary_to_edge(): Fatal error!' )
      print ( '  Illegal boundary word character w(', w_i, ')=' + c )
      error ( 'boundary_to_edge(): Fatal error!' ) 

    e[wi+1,0] = i
    e[wi+1,1] = j

  return e

def boundary_to_edge_test ( ):

#*****************************************************************************80
#
## boundary_to_edge_test() tests boundary_to_edge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_to_edge_test():' )
  print ( '  boundary_to_edge() converts a boundary word to an edge list.' )

  w, p = boundary_gort ( )
  name = '  Gort: boundary word'
  boundary_print ( w, p, name )

  e = boundary_to_edge ( w, p )
  name = '  Gort: edge list'

  print ( '' )
  print ( name )
  print ( '' )

  en = e.shape[0]

  for i in range ( 0, en ):
    print ( '  %2d:  %2d  %2d' % ( i, e[i,0], e[i,1] ) )

  return

def boundary_to_triangle ( w, p ):

#*****************************************************************************80
#
## boundary_to_triangle() converts a polyiamond description from boundary to triangle.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    The triangle list is a list of the IJK parallelogram triangles
#    that constitute the polyiamond.
#    If k = 0, the "ijk" triangle has vertices
#      (i-1,j-1), (i,j-1), (i-1,j).
#    If k = 1, the "ijk" triangle has vertices
#      (i,j), (i-1,j), (i,j-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    integer T(TN,3): the IJK parallelogram coordinates of the 
#    triangles forming the polyiamond.  
#
  v = boundary_to_vertex ( w, p )
  t = vertex_to_triangle ( v )

  return t

def boundary_to_triangle_test ( ):

#*****************************************************************************80
#
## boundary_to_triangle_test() tests boundary_to_triangle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_to_triangle_test():' )
  print ( '  boundary_to_triangle() converts a boundary word' )
  print ( '  to a triangle list.' )

  w, p = boundary_gort ( )
  name = '  Gort boundary word'
  boundary_print ( w, p, name )

  t = boundary_to_triangle ( w, p )
  name = '  Gort triangle list'

  print ( '' )
  print ( name )
  print ( '' )

  m = t.shape[0]

  for i in range ( 0, m ):
    print ( ' %2d:  %2d  %2d  %2d' % ( i, t[i,0], t[i,1], t[i,2] ) )

  return

def boundary_to_vertex ( w, p ):

#*****************************************************************************80
#
## boundary_to_vertex() converts a polyiamond description from boundary to vertex.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#    The vertex list of a polyiamond gives the IJ coordinates of the
#    polygonal vertices, in counterclockwise order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    integer V(VN,2): the IJ parallelogram point coordinates of the 
#    vertices bounding the polyiamond.  
#
  import numpy as np

  w_n = len ( w )

  w_i = -1
  v = np.zeros ( [ 0, 2 ], dtype = int )
  i = p[0]
  j = p[1]
  v = np.append ( v, [[ i, j ]], axis = 0 )
  c = w[0]

  while ( w_i + 1 < w_n ):

    w_i = w_i + 1
    c_old = c
    c = w[w_i]

    if ( c != c_old or w_i + 1 == w_n ):
      v = np.append ( v, [[ i, j ]], axis = 0 )

    if ( c == '0' ):
      j = j + 1
    elif ( c == '1' ):
      i = i + 1
    elif ( c == '2' ):
      i = i + 1
      j = j - 1
    elif ( c == '3' ):
      j = j - 1
    elif ( c == '4' ):
      i = i - 1
    elif ( c == '5' ):
      i = i - 1
      j = j + 1
    else:
      print ( '' )
      print ( 'boundary_to_vertex(): Fatal error!' )
      print ( '  Illegal boundary word character w(', w_i, ')=' + c )
      raise Exception ( 'boundary_to_vertex(): Fatal error!' )

  return v

def boundary_to_vertex_test ( ):

#*****************************************************************************80
#
## boundary_to_vertex_test() tests boundary_to_vertex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_to_vertex_test():' )
  print ( '  boundary_to_vertex() converts a boundary word to a vertex list.' )

  w, p = boundary_gort ( )
  name = '  Gort boundary word'
  boundary_print ( w, p, name )

  v = boundary_to_vertex ( w, p )
  name = '  Gort vertex list'

  print ( '' )
  print ( name )
  print ( '' )

  vn = v.shape[0]

  for i in range ( 0, vn ):
    print ( '  %2d:  %2d  %2d' % ( i, v[i,0], v[i,1] ) )

  return

def boundary_translate ( w, p, pp ):

#*****************************************************************************80
#
## boundary_translate() translates a polyiamond described by a boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point (i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by this diagram:
#
#          5-----0-----*
#      ^  / \   / \   /
#     /  /   \ /   \ /
#    J  4-----P-----1
#      / \   / \   /
#     /   \ /   \ /
#    *-----3-----2
#
#          I-->
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      0  (I,  J+1)
#      1  (I+1,J  )
#      2  (I+1,J-1)
#      3  (I,  J-1)
#      4  (I-1,J  )
#      5  (I-1,J+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.  
#
#    integer P(2): the starting point.
#
#    integer PP(2): the translation.
#
#  Output:
#
#    list W2: the boundary word for the translated shape.  
#
#    integer P2(2): the starting point for the translated shape.
#
  w2 = w.copy()
  p2 = p + pp

  return w2, p2

def boundary_translate_test ( ):

#*****************************************************************************80
#
## boundary_translate_test() tests boundary_translate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'boundary_translate_test():' )
  print ( '  boundary_translate() translates a polyiamond' )
  print ( '  described by its boundary word.' )

  w0, p0 = boundary_gort ( )

  d = np.array ( [ -2, + 6 ] )
  w1, p1 = boundary_translate ( w0, p0, d )
#
#  Get the plot range.
#
  imin0, imax0, jmin0, jmax0 = boundary_range ( w0, p0 )
  imin1, imax1, jmin1, jmax1 = boundary_range ( w1, p1 )

  imin = min ( [ 0, imin0, imin1 ] )
  imax = max ( [ 0, imax0, imax1 ] ) + 1
  jmin = min ( [ 0, jmin0, jmin1 ] )
  jmax = max ( [ 0, jmax0, jmax1 ] ) + 1
#
#  Draw the parallelogram grid.
#
  plt.clf ( )
  r = 0.85
  color_back = 'cyan'
  color_tri =  'white'
  number = False
  grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number )
#
#  Draw the polyiamond.
#
  color = 'cyan'
  number = False
  boundary_plot ( w0, p0, color, number )

  color = 'red'
  number = False
  boundary_plot ( w1, p1, color, number )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )
  plt.title ( 'Boundary translate test' )

  filename = 'boundary_translate_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number ):

#*****************************************************************************80
#
## grid_plot() displays a parallelogram grid.
#
#  Discussion:
#
#    The user should call "clf()" before this function.
#
#    The user should call "hold('off')" to close this plot.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IMIN, IMAX, JMIN, JMAX: the range of the parallelogram.
#
#    real R: controls the size of the component triangles.
#    0 <= R<= 1.  Use R=0.95 for triangles that don't completely fill
#    the region.
#
#    color COLOR_BACK, COLOR_TRI: colors for the background and the triangles.
#
#    logical NUMBER: true if the triangle grid indices should be plotted.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Ensure the origin is included.
#
  imin2 = min ( imin, 0 )
  imax2 = max ( imax, 0 )
  jmin2 = min ( jmin, 0 )
  jmax2 = max ( jmax, 0 )
#
#  Determine (x,y) coordinates.
#
  x1 = imin2 - 1 + ( jmin2 - 1 ) / 2
  y1 =             ( jmin2 - 1 ) * np.sin ( np.pi / 3.0 )

  x2 = imax2     + ( jmin2 - 1 ) / 2
  y2 =             ( jmin2 - 1 ) * np.sin ( np.pi / 3.0 )

  x3 = imax2     +   jmax2       / 2
  y3 =               jmax2       * np.sin ( np.pi / 3.0 )

  x4 = imin2 - 1 +   jmax2       / 2
  y4 =               jmax2       * np.sin ( np.pi / 3.0 )

  plt.fill ( [ x1, x2, x3, x4 ], [ y1, y2, y3, y4 ], color_back )

  label = ''

  for i in range ( imin2, imax2 + 1 ):
    for j in range ( jmin2, jmax2 + 1 ):
      for k in range ( 0, 2 ):
        ijk = np.array ( [ i, j, k ] )
        ijk_fill ( ijk, r, color_tri, label )

  if ( number ):
    for i in range ( imin, imax + 1 ):
      for j in range ( jmin, jmax + 1 ):
        for k in range ( 0, 2 ):
          grid_index = 1 + 2 * ( i - 1 + imax * ( j - 1 ) ) + k
          label = str ( grid_index )
          ijk = np.array ( [ i, j, k ] )
          ijk_fill ( ijk, r, color_tri, label )
#
#  Mark the origin.
#
  plt.plot ( 0.0, 0.0, 'k.', markersize = 35 )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  return

def grid_plot_test ( ):

#*****************************************************************************80
#
## grid_plot_test() tests grid_plot().
#
#  Discussion:
#
#    5           x x x x-x x
#                 /|  / /
#    4         x-x x x x x
#             /    |/ /
#    3       x-x x x x x
#              |    /
#    2     x x x x x x
#             /    |
#    1   x-x-x x x x
#       /         /
#    0 x-x-x-x-x-x
#
#      0 1 2 3 4 5
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'grid_plot_test():' )
  print ( '  grid_plot() plots a polyiamond grid from its boundary word.' )
#
#  Draw the parallelogram grid.
#
  plt.clf ( )
 
  imin = 0
  imax = 8
  jmin = 0
  jmax = 5
  r = 0.85
  color_back = 'cyan'
  color_tri = np.array ( [ 1, 1, 0 ] )
  number = False

  grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )
  plt.title ( 'grid plot' )

  filename = 'grid_plot_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def ijk_fill ( ijk, r, color, label ):

#*****************************************************************************80
#
## ijk_fill() plots a filled ijk triangle.
#
#  Discussion:
#
#    The (i,j) coordinates refer to a parallelogram whose basic cell
#    is the unit parallelogram outlined by points (A,B,C,D)
#    with (i,j) coordinates
#      A = (0,0) --> B = (1,0) --> C = (1,1) --> D = (0,1).
#
#         D-----C
#        /     /
#       /     /
#      A-----B
#
#    Each cell is divided into k=0 and k=1 triangles:
#
#         *-----*
#        / \ 1 /
#       / 0 \ /
#      *-----*
#
#    Triangles are identified by a related (i,j,k) coordinate based 
#    on the (i,j) coordinates of its vertices:
#      If k = 0, the "ijk" triangle has vertices (i-1,j-1), (i,j-1), (i-1,j).
#      If k = 1, the "ijk" triangle has vertices (i,j),     (i-1,j), (i,j-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IJK[3], the indices of the cell.
#
#    real R, a size factor for the triangles, between 0 and 1.
#
#    color COLOR, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The circle is filled with this color.
#
#    string LABEL: an optional label.
#
  import matplotlib.pyplot as plt
  import numpy as np

  x, y = ijk_to_xy ( ijk )

  xm = np.sum ( x ) / 3.0
  ym = np.sum ( y ) / 3.0

  x = r * x + ( 1.0 - r ) * xm
  y = r * y + ( 1.0 - r ) * ym

  plt.fill ( x, y, color )

  if ( 0 < len ( label ) ):
    plt.text ( xm, ym, label, horizontalalignment = 'center' )

  return

def ijk_to_xy ( ijk ):

#*****************************************************************************80
#
## ijk_to_xy() returns the (x,y) coordinates of a triangle in the ijk system.
#
#  Discussion:
#
#    The (i,j) coordinates refer to a parallelogram whose basic cell
#    is the unit parallelogram outlined by points (A,B,C,D)
#    with (i,j) coordinates
#      A = (0,0) --> B = (1,0) --> C = (1,1) --> D = (0,1).
#
#         D-----C
#        /     /
#       /     /
#      A-----B
#
#    Each cell is divided into k=0 and k=1 triangles:
#
#         *-----*
#        / \ 1 /
#       / 0 \ /
#      *-----*
#
#    Triangles are identified by a related (i,j,k) coordinate based 
#    on the (i,j) coordinates of its vertices:
#      If k = 0, the "ijk" triangle has vertices (i-1,j-1), (i,j-1), (i-1,j).
#      If k = 1, the "ijk" triangle has vertices (i,j),     (i-1,j), (i,j-1).
#
#    The (x,y) coordinates refer to the standard Cartesian coordinate
#    system, so that the unit parallelogram vertices have
#    (x,y) coordinates:
#      A = (0,0) --> B = (1,0) --> C = (1+c,s) --> D = (c,s),
#    where c = cos(60) = 0.5 and s = sin(60) = sqrt(3)/2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IJK(3), the parallelogram coordinates of a triangle.
#
#  Output:
#
#    real X(3), Y(3): the Cartesian coordinates of the vertices.
#
  import numpy as np

  x = np.zeros ( 3 )
  y = np.zeros ( 3 )

  i = ijk[0]
  j = ijk[1]
  k = ijk[2]

  if ( k == 0 ):
    q1 = ij_to_xy ( np.array ( [ i - 1, j - 1 ] ) )
    q2 = ij_to_xy ( np.array ( [ i,     j - 1 ] ) )
    q3 = ij_to_xy ( np.array ( [ i - 1, j     ] ) )
  elif ( k == 1 ):
    q1 = ij_to_xy ( np.array ( [ i,     j     ] ) )
    q2 = ij_to_xy ( np.array ( [ i - 1, j     ] ) )
    q3 = ij_to_xy ( np.array ( [ i,     j - 1 ] ) )
  else:
    print ( '' )
    print ( 'ijk_to_xy(): Fatal error!' )
    print ( '  Triangle has illegal value k = ', k )
    raise Exception ( 'ijk_to_xy(): Fatal error!' )

  x = np.array ( [ q1[0], q2[0], q3[0] ] )
  y = np.array ( [ q1[1], q2[1], q3[1] ] )

  return x, y

def ij_to_xy ( p ):

#*****************************************************************************80
#
## ij_to_xy() converts a point's (i,j) coordinates to (x,y) form.
#
#  Discussion:
#
#    The (i,j) coordinates refer to a parallelogram whose basic cell
#    is the unit parallelogram outlined by points (A,B,C,D)
#    with (i,j) coordinates
#      A = (0,0) --> B = (1,0) --> C = (1,1) --> D = (0,1).
#
#         D-----C
#        /     /
#       /     /
#      A-----B
#
#    The (x,y) coordinates refer to the standard Cartesian coordinate
#    system, so that the unit parallelogram vertices have
#    (x,y) coordinates:
#      A = (0,0) --> B = (1,0) --> C = (1+c,s) --> D = (c,s),
#    where c = cos(60) = 0.5 and s = sin(60) = sqrt(3)/2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(2) the parallelogram coordinates of a point.
#
#  Output:
#
#    real Q(2): the Cartesian coordinates of the point.
#
  import numpy as np

  c = np.cos ( np.pi / 3.0 )
  s = np.sin ( np.pi / 3.0 )

  q = np.zeros ( 2 )

  q[0] = p[0] + p[1] * c
  q[1] =        p[1] * s

  return q

def list_to_string ( w ):

#*****************************************************************************80
#
## list_to_string() converts a list of characters to a string.
#
#  Discussion:
#
#    w = [ 'H', 'e', 'l', 'l', 'o' }
#    s = 'Hello'
#
#    Just keep repeating to yourself the idiotic "Python strings are immutable"
#
#    To reverse the process, the corresponding "string_to_list()" would be
#
#      w = list ( s )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: a list of characters.
#
#  Output:
#
#    string S: the corresponding string.
#
  s = "".join ( w )

  return s

def s_lt ( c1, c2 ):

#*****************************************************************************80
#
## s_lt() is TRUE if one string is less than another.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string C1(N1), C2(N2): two strings.
#
#  Output:
#
#    logical is_less_than: is TRUE if C1 < C2.
#
  is_less_than = True

  n1 = len ( c1 )
  n2 = len ( c2 )
  n = min ( n1, n2 )

  for i in range ( 0, n ):

    if ( c1[i] < c2[i] ):
      is_less_than = True
      return is_less_than
    elif ( c2[i] < c1[i] ):
      is_less_than = False
      return is_less_than

  if ( n1 < n2 ):
    is_less_than = True
  else:
    is_less_than = False

  return is_less_than

def s_lt_test ( ):

#*****************************************************************************80
#
## s_lt_test() tests s_lt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 's_lt_test():' )
  print ( '  s_lt(c1,c2) is TRUE if c1 < c2' )
  print ( '  for strings c1 and c2.' )
  print ( '' )
  print ( '  C1                    C2                    C1<C2?' )
  print ( '' )

  c1 = 'minnesota'
  c2 = 'minnesota'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'Minnesota'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minnesota2'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minnesot'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minne'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minnesotan'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = ' minnesota'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'alaska'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'wyoming'
  is_less_than = s_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  return

def name_hexiamond ( index ):

#*****************************************************************************80
#
## name_hexiamond() returns the name of hexiamonds 1 through 12.
#
#  Discussion:
#
#    There is a standard name for each hexiamond, suggested by its shape.  
#
#     1  bat (chevron)
#     2  butterfly
#     3  club (crook)
#     4  crown
#     5  hexagon
#     6  lobster
#     7  pistol (signpost)
#     8  rhomboid (bar)
#     9  shoe (hook)
#    10  snake
#    11  sphinx
#    12  yacht
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer INDEX, a value between 1 and 12.
#
#  Output:
#
#    string NAME, is the corresponding name.
#
  if ( index == 1 ):
    name = 'bat'
  elif ( index == 2 ):
    name = 'butterfly'
  elif ( index == 3 ):
    name = 'club'
  elif ( index == 4 ):
    name = 'crown'
  elif ( index == 5 ):
    name = 'hexagon'
  elif ( index == 6 ):
    name = 'lobster'
  elif ( index == 7 ):
    name = 'pistol'
  elif ( index == 8 ):
    name = 'rhomboid'
  elif ( index == 9 ):
    name = 'shoe'
  elif ( index == 10 ):
    name = 'snake'
  elif ( index == 11 ):
    name = 'sphinx'
  elif ( index == 12 ):
    name = 'yacht'
  else:
    name = '?'

  return name

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

def vertex_contains_ijk ( v, ijk ):

#*****************************************************************************80
#
## vertex_contains_ijk(): is a triangle in a polyiamond, given vertex list.
#
#  Discussion:
#
#    The vertex list of a polyiamond gives the IJ coordinates of the
#    polygonal vertices, in counterclockwise order.
#
#    This computation assumes that both the vertex list and the IJK
#    triangle description both use the same coordinate system, 
#    either the (i,j) coordinate system (which is expected) or 
#    the (x,y) coordinate system (which is generally NOT expected, but
#    should work).
#
#    The (i,j) coordinates refer to a parallelogram whose basic cell
#    is the unit parallelogram outlined by points (A,B,C,D)
#    with (i,j) coordinates
#      A = (0,0) --> B = (1,0) --> C = (1,1) --> D = (0,1).
#
#         D-----C
#        /     /
#       /     /
#      A-----B
#
#    Each cell is divided into k=0 and k=1 triangles:
#
#         *-----*
#        / \ 1 /
#       / 0 \ /
#      *-----*
#
#    Triangles are identified by a related (i,j,k) coordinate based 
#    on the (i,j) coordinates of its vertices:
#      If k = 0, the "ijk" triangle has vertices (i-1,j-1), (i,j-1), (i-1,j).
#      If k = 1, the "ijk" triangle has vertices (i,j),     (i-1,j), (i,j-1).
#
#    The (x,y) coordinates refer to the standard Cartesian coordinate
#    system, so that the unit parallelogram vertices have
#    (x,y) coordinates:
#      A = (0,0) --> B = (1,0) --> C = (1+c,s) --> D = (c,s),
#    where c = cos(60) = 0.5 and s = sin(60) = sqrt(3)/2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer V(VN,2): the parallelogram point indices of the
#    vertices, in counterclockwise order.
#
#    integer IJK(3): the parallelogram triangle index.
#
#  Output:
#
#    logical VALUE: is true if the triangle is in the region.
#
  import numpy as np

  i = ijk[0]
  j = ijk[1]
  k = ijk[2]

  it = np.zeros ( 3, dtype = float )
  jt = np.zeros ( 3, dtype = float )

  if ( k == 0 ):
    it[0] = i - 1
    it[1] = i
    it[2] = i - 1
    jt[0] = j - 1
    jt[1] = j - 1
    jt[2] = j
  else:
    it[0] = i
    it[1] = i - 1
    it[2] = i
    jt[0] = j
    jt[1] = j
    jt[2] = j - 1

  im = np.mean ( it )
  jm = np.mean ( jt )
  p = np.array ( [ im, jm ] )

  value = vertex_contains_point ( v, p )

  return value

def vertex_contains_point ( v, p ):

#*****************************************************************************80
#
## vertex_contains_point(): is a point inside a polyiamond given its vertex list?
#
#  Discussion:
#
#    The vertex list of a polyiamond gives the IJ coordinates of the
#    polygonal vertices, in counterclockwise order.
#
#    There are two different coordinate systems in use:
#    (I,J) refers to the parallelogram grid coordinates.
#    (X,Y) refers to the Cartesian coordinates.
#
#    There is an affine relationship between these two systems.
#    As long as both V and P are reported in the same coordinate system,
#    this function should give correct results.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real V(VN,2): the coordinates of the polygon vertices.
#
#    real P(2): the coordinates of the point, using the same
#    coordinate system as V.
#
#  Output:
#
#    logical INSIDE, is TRUE if the point is inside the polygon.
#
  vn = v.shape[0]

  inside = False

  vx1 = v[0,0]
  vy1 = v[0,1]
  xints = p[0] - 1.0

  for i in range ( 0, vn ):

    vx2 = v[((i+1)%vn),0]
    vy2 = v[((i+1)%vn),1]

    if ( min ( vy1, vy2 ) < p[1] ):
      if ( p[1] <= max ( vy1, vy2 ) ):
        if ( p[0] <= max ( vx1, vx2 ) ):

          if ( vy1 != vy2 ):
            xints = ( p[1] - vy1 ) * ( vx2 - vx1 ) / ( vy2 - vy1 ) + vx1

          if ( vx1 == vx2 or p[0] <= xints ):
            inside = not inside

    vx1 = vx2
    vy1 = vy2

  return inside

def vertex_plot ( v, color, number ):

#*****************************************************************************80
#
## vertex_plot() plots a polyiamond from its vertex list.
#
#  Discussion:
#
#    The vertex list of a polyiamond gives the IJ coordinates of the
#    polygonal vertices, in counterclockwise order.
#
#    The user should call "clf()" before this function.
#    More plotting commands may be issued if preceded by the "hold on"
#    command.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer V(VN,2): the vertices, in counterclockwise order.
#
#    color COLOR: the color to use.
#
#    logical NUMBER: true if the triangle indices should be printed.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Determine the extent of the parallelogram grid.
#
  imin = min ( v[:,0] )
  imax = max ( v[:,0] )
  jmin = min ( v[:,1] )
  jmax = max ( v[:,1] )
#
#  Ensure inclusion of origin.
#
  imin = min ( imin, 0 )
  imax = max ( imax, 0 )
  jmin = min ( jmin, 0 )
  jmax = max ( jmax, 0 )
#
#  Consider each triangle in the parallelogram grid.
#  If it is in the region, color it in.
#
  r = 1.0
  counter = 0

  for j in range ( jmin + 1, jmax + 2 ):
    for i in range ( imin + 1, imax + 2 ):
      for k in range ( 0, 2 ):

        ijk = np.array ( [ i, j, k ] )

        if ( vertex_contains_ijk ( v, ijk ) ):
          counter = counter + 1

          if ( number ):
            label = str ( counter )
          else:
            label = ''

          ijk_fill ( ijk, r, color, label )
#
#  Mark the origin.
#
  plt.plot ( 0.0, 0.0, 'k.', markersize = 35 )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  return

def vertex_plot_test ( ):

#*****************************************************************************80
#
## vertex_plot_test() tests vertex_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'vertex_plot_test():' )
  print ( '  vertex_plot() plots an object from its vertex list.' )

  w, p = boundary_gort ( )
  name = '  Gort boundary word'
  boundary_print ( w, p, name )

  v = boundary_to_vertex ( w, p )
  name = '  Gort vertex list'

  print ( '' )
  print ( name )
  print ( '' )

  vn = v.shape[0]

  for i in range ( 0, vn ):
    print ( '  %2d:  %2d  %2d' % ( i, v[i,0], v[i,1] ) )
#
#  Determine the extent of the parallelogram grid.
#
  imin = min ( v[:,0] )
  imax = max ( v[:,0] )
  jmin = min ( v[:,1] )
  jmax = max ( v[:,1] )
#
#  Ensure inclusion of origin.
#
  imin = min ( imin, 0 )
  imax = max ( imax, 0 )
  jmin = min ( jmin, 0 )
  jmax = max ( jmax, 0 )
#
#  Make the plot.
#
  plt.clf ( )

  r = 0.85
  color_back = 'cyan'
  color_tri =  'yellow'
  number = False
  grid_plot ( imin, imax, jmin, jmax, r, color_back, color_tri, number )

  color = 'red'
  number = True
  vertex_plot ( v, color, number )

  filename = 'vertex_plot_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def vertex_to_triangle ( v ):

#*****************************************************************************80
#
## vertex_to_triangle() converts a polyiamond from vertex list to triangle list.
#
#  Discussion:
#
#    The vertex list of a polyiamond gives the IJ coordinates of the
#    polygonal vertices, in counterclockwise order.
#
#    The triangle list is a list of the IJK parallelogram triangles
#    that constitute the polyiamond.
#    If k = 0, the "ijk" triangle has vertices
#      (i-1,j-1), (i,j-1), (i-1,j).
#    If k = 1, the "ijk" triangle has vertices
#      (i,j), (i-1,j), (i,j-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer V(VN,2): the (I,J) parallelogram vertices, in counterclockwise order.
#
#  Output:
#
#    integer T(TN,3), the IJK parallelogram triangle coordinates of the 
#    triangles making up the shape.  
#
  import numpy as np
#
#  Determine the extent of the parallelogram grid.
#
  imin = min ( v[:,0] )
  imax = max ( v[:,0] )
  jmin = min ( v[:,1] )
  jmax = max ( v[:,1] )
#
#  Consider each triangle in the parallelogram grid.
#  If it is in the region, add it to the list.
#
  tn = 0
  t = np.zeros ( [ tn, 3 ], dtype = int )

  for j in range ( jmin + 1, jmax + 2 ):
    for i in range ( imin + 1, imax + 2 ):
      for k in range ( 0, 2 ):
        ijk = np.array ( [ i, j, k ] )
        if ( vertex_contains_ijk ( v, ijk ) ):
          tn = tn + 1
          t = np.append ( t, [[ i, j, k ]], axis = 0 )

  return t

if ( __name__ == '__main__' ):
  timestamp ( )
  boundary_word_equilateral_test ( )
  timestamp ( )

