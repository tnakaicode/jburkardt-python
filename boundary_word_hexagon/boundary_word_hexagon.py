#! /usr/bin/env python3
#
def boundary_word_hexagon_test ( ):

#*****************************************************************************80
#
## boundary_word_hexagon_test() tests boundary_word_hexagon().
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
  print ( 'boundary_word_hexagon_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  boundary_word_hexagon() is a library of boundary word functions' )
  print ( '  for polyhexes, shapes defined on a grid of hexagons.' )

  boolean_to_string_test ( )

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
  boundary_to_vertex_test ( )
  boundary_translate_test ( )

  ch_to_digit_test ( )

  grid_plot_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'boundary_word_hexagon_test():' )
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

def boundary_is_legal ( w, p ):

#*****************************************************************************80
#
## boundary_is_legal() determines if a polyhex boundary word is legal.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
#
#    After a step of index K, the next step must be K-1 or K+1 (modulo 6).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2024
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
  verbose = False

  s = list_to_string ( w )
#
#  Only the characters 1 through 6 can appear.
#
  l = s.count ( '1' ) \
    + s.count ( '2' ) \
    + s.count ( '3' ) \
    + s.count ( '4' ) \
    + s.count ( '5' ) \
    + s.count ( '6' )

  if ( len ( w ) != l ):
    if ( verbose ):
      print ( '' )
      print ( 'boundary_is_legal():' )
      print ( '  W contains illegal characters.' )

    value = False
    return value
#
#  Each pair 1/4, 2/5 and 3/6 must match.
#
  if ( s.count ( '1' ) != s.count ( '4' ) ):
    if ( verbose ):
      print ( '' )
      print ( 'boundary_is_legal():' )
      print ( '  1 and 4 characters do not match.' )

    value = False
    return value

  if ( s.count ( '2' ) != s.count ( '5' ) ):
    if ( verbose ):
      print ( '' )
      print ( 'boundary_is_legal():' )
      print ( '  2 and 5 characters do not match.' )

    value = False
    return value

  if ( s.count ( '3' ) != s.count ( '6' ) ):
    if ( verbose ):
      print ( '' )
      print ( 'boundary_is_legal():' )
      print ( '  3 and 6 characters do not match.' )

    value = False
    return value
#
#  The step index must change by exactly 1 unit.
#
  wn = len ( w )
  cnew = w[-1]
  pnew = ch_to_digit ( cnew )

  for i in range ( 0, wn ):
    cold = cnew
    pold = pnew
    cnew = w[i]
    pnew = ch_to_digit ( cnew )
    if ( pold == 6 and pnew == 1 ):
      continue
    elif ( pold == 1 and pnew == 6 ):
      continue
    else:
      if ( abs ( pold - pnew ) != 1 ):
        if ( verbose ):
          print ( '' )
          print ( 'boundary_is_legal():' )
          print ( '  On step ', i, ', illegal step "'+ cold + '" to "' + cnew + '"'  )
        value = False
        return value
#
#  All tests passed.
#
  value = True

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
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'boundary_is_legal_test():' )
  print ( '  boundary_is_legal() checks whether a polyhex' )
  print ( '  boundary word is legal.' )
  print ( '' )
  print ( '                  Name     Boundary word       Legal?' )
  print ( '' )

  for k in range ( 1, 8 ):
    w, p = tetrahex_word ( k )
    s = list_to_string ( w )
    name = tetrahex_name ( k )
    legal = boundary_is_legal ( w, p )
    tf = boolean_to_string ( legal )
    print ( '  %20s  %20s  %s' % ( name, s, tf ) )
#
#  Use an illegal character in the word.
#
  w = list ( '123230323456560656' )
  s = list_to_string ( w )
  p = np.array ( [ 0, 0 ] )
  name = 'Illegal character'
  legal = boundary_is_legal ( w, p )
  tf = boolean_to_string ( legal )
  print ( '  %20s  %20s  %s' % ( name, s, tf ) )
#
#  3 and 6 don't match.
#
  w = list ( '123232323456565356' )
  s = list_to_string ( w )
  p = np.array ( [ 0, 0 ] )
  name = '3 and 6 do not match'
  legal = boundary_is_legal ( w, p )
  tf = boolean_to_string ( legal )
  print ( '  %20s  %20s  %s' % ( name, s, tf ) )
#
#  Illegal nonunit step.
#
  w = list ( '123234356565656232' )
  s = list_to_string ( w )
  p = np.array ( [ 0, 0 ] )
  name = 'Nonunit step'
  legal = boundary_is_legal ( w, p )
  tf = boolean_to_string ( legal )
  print ( '  %20s  %20s  %s' % ( name, s, tf ) )

  return

def boundary_plot ( w, p, color, number ):

#*****************************************************************************80
#
## boundary_plot() plots a polyhex from its boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
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
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_plot_test():' )
  print ( '  boundary_plot() plots a polyhex from its boundary word.' )

  for k in range ( 1, 8 ):
    w, p = tetrahex_word ( k )
    label = tetrahex_name ( k )
    filename = label + '_boundary.png'
    boundary_plot_demo ( w, p, label, filename )
 
  return

def boundary_plot_demo ( w, p, label, filename ):

#*****************************************************************************80
#
## boundary_plot_demo plots the boundary of a polyhex.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list W: the boundary word.
#
#    integer P[2]: the base point.
#
#    string LABEL: a title for the plot.
#
#    string FILENAME: the name of a file in which to save the plot.
#
  import matplotlib.pyplot as plt
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
  plt.title ( label )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def boundary_print ( w, p, label ):

#*****************************************************************************80
#
## boundary_print() prints the boundary word of a polyhex.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
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
#    list W: the boundary word. 
#
#    integer P(2): the boundary word start point.
#
#    string LABEL: a label to be printed.  
#
  s = list_to_string ( w )

  print ( '' )
  print ( label )
  print ( '  hex boundary word:  "' + s + '"' )
  print ( '  base point (i,j)   :  [', p[0], ',', p[1], ']' )

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
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_print_test():' )
  print ( '  boundary_print() prints the boundary word of a polyhex.' )
 
  for k in range ( 1, 8 ):
    w, p = tetrahex_word ( k )
    name = tetrahex_name ( k )
    name =  '  ' + name
    boundary_print ( w, p, name )

  return

def boundary_range ( w, p ):

#*****************************************************************************80
#
## boundary_range() determines the range of a polyhex from its boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2024
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

    if ( w[k] == '1' ):
      i = i + 1
    elif ( w[k] == '2' ):
      j = j + 1
    elif ( w[k] == '3' ):
      i = i - 1
      j = j + 1
    elif ( w[k] == '4' ):
      i = i - 1
    elif ( w[k] == '5' ):
      j = j - 1
    elif ( w[k] == '6' ):
      i = i + 1
      j = j - 1
 
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
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_range_test():' )
  print ( '  boundary_range() finds the minimum and maximum I and J' )
  print ( '  coordinates of a polyhex described by its boundary word W' )
  print ( '  and starting at P(i,j).' )
  print ( '' )
  print ( '        Name  Imin  Imax  Jmin  Jmax  Pi  Pj  W' )
  print ( '' )

  for k in range ( 1, 8 ):
    name = tetrahex_name ( k )
    w, p = tetrahex_word ( k )
    s = list_to_string ( w )
    imin, imax, jmin, jmax = boundary_range ( w, p )
    print ( '  %10s  %4d  %4d  %4d  %4d  %2d  %2d  %s'
      % ( name, imin, imax, jmin, jmax, p[0], p[1], '"' + s + '"' ) )

  return

def boundary_reflect ( w, p, r ):

#*****************************************************************************80
#
## boundary_reflect() reflects a polyhex described by a boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2024
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
#    1: reflect about the 0 degree axis
#    2: reflect about the 60 degree axis
#    3: reflect about the 120 degree axis.
#
#  Output:
#
#    list W2: the boundary word for the reflected shape.  
#
#    integer P2(2): the starting point for the reflected shape.
#
  c1 = [ '1', '2', '3', '4', '5', '6' ]

  if ( r == 1 ):
    c2 = [ '1', '6', '5', '4', '3', '2' ]
  elif ( r == 2 ):
    c2 = [ '3', '2', '1', '6', '5', '4' ]
  elif ( r == 3 ):
    c2 = [ '5', '4', '3', '2', '1', '6' ]
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
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_reflect_test():' )
  print ( '  boundary_reflect() is given a boundary word W and base' )
  print ( '  point P, and reflects about the 0, 60, or 120 degree axis.' )

  k = 4
  w0, p0 = tetrahex_word ( k )
  boundary_print ( w0, p0, '  pistol' )
  r = 1
  w1, p1 = boundary_reflect ( w0, p0, r )
  boundary_print ( w1, p1, '  pistol, 0 degree reflection' )
  r = 2
  w2, p2 = boundary_reflect ( w0, p0, r )
  boundary_print ( w2, p2, '  pistol, 60 degree reflection' )
  r = 3
  w3, p3 = boundary_reflect ( w0, p0, r )
  boundary_print ( w3, p3, '  pistol, 120 degree reflection' )
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
  number = False
# boundary_plot ( w0, p0, color, number )

  color = 'magenta'
  number = False
  boundary_plot ( w1, p1, color, number )

  color = 'yellow'
  number = False
  boundary_plot ( w2, p2, color, number )

  color = 'blue'
  number = False
  boundary_plot ( w3, p3, color, number )

  plt.axis ( 'equal' )
  plt.axis ( 'off' )
  plt.title ( 'boundary reflect test' )

  filename = 'boundary_reflect_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "#s"', filename )

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
#      '12346', '123456', '234561', '345612', '456123', '561234' 
#
#    This function is given a boundary word, and returns the representative
#    for the class, that is, the lexically first element.
#
#    MATLAB makes lexical comparison easy for strings, which are 
#    actually distinct from character arrays.  We assume the user is
#    working with strings, and so we have to internally convert back
#    and forth.
#
#    Two boundary words are equal if and only if they have the same representative.
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
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_representative_test():' )
  print ( '  boundary_representative() is given a boundary word, and' )
  print ( '  returns the representative of its equivalence class.' )

  k = 1
  w, p = tetrahex_word ( k )
  name = tetrahex_name ( k )

  for r in range ( 0, 10 ):

    name1 = '  "rotated" ' + name + ':'
    w1 = w[r:] + w[0:r]
    boundary_print ( w1, p, name1 )

    name2 = '  "rotated" ' + name + ' representative:'
    w2 = boundary_representative ( w1 )
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
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
#
#  Example:
#
#    w  = '66543445432121'
#    r  = 2
#    w2 = '22165661654343'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2024
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

  c = [ '1', '2', '3', '4', '5', '6' ]

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
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_rotate_test():' )
  print ( '  boundary_rotate() rotates a polyhex' )
  print ( '  described by its boundary word.' )

  k = 7

  for r in range ( 0, 6 ):
    w, p = tetrahex_word ( k )
    w2, p2 = boundary_rotate ( w, p, r )
    name = 'boundary_rotate_worm_' + str ( r * 60 )
    plt.clf ( )
    color = 'cyan'
    number = False
    boundary_plot ( w2, p2, color, number )
    plt.title ( name )
    filename = name + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )

  return

def boundary_snap ( w, p ):

#*****************************************************************************80
#
## boundary_snap() "snaps" a polyhex to have minimum I and J coordinates of 0.
#
#  Discussion:
#
#    We "snap" a shape by translating it so that its least I and
#    least J node coordinates are 0.
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
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
#    list W: the boundary word.  
#
#    integer P(2): the starting point.
#
#  Output:
#
#    list W2: the boundary word for the snapped shape.  
#
#    integer P2(2): the starting point for the snapped shape.
#
  import numpy as np

  imin, imax, jmin, jmax = boundary_range ( w, p )

  w2 = w.copy()
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
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'boundary_snap_test():' )
  print ( '  boundary_snap() translates a polyhex so that it has' )
  print ( '  minimum I and J node coordinates of 0.' )
#
#  Start with the pistol.
#
  k = 4
  w1, p1 = tetrahex_word ( k )
#
#  Translate it.
#
  d = np.array ( [ 6, 3 ] )
  w2, p2 = boundary_translate ( w1, p1, d )
#
#  Request a snapped version.
#
  w3, p3 = boundary_snap ( w2, p2 )
#
#  Plot the translated and snapped shapes.
#
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
#  Draw the shapes.
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
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
#
#    Sorting "rotates" the boundary word to produce the lexically smallest 
#    base point P.
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
#    list W: the boundary word.  
#
#    integer P(2): the starting point.
#
#  Output:
#
#    list W2: the boundary word for the sorted shape.  
#
#    integer P2(2): the starting point for the sorted shape.
#
  w2 = w.copy()
  p2 = p.copy()

  wn = len ( w2 )
  p3 = p.copy()

  for i in range ( 0, wn ):

    c = w[i]

    if ( c == '1' ):
      p3[0] = p3[0] + 1
    elif ( c == '2' ):
      p3[1] = p3[1] + 1
    elif ( c == '3' ):
      p3[0] = p3[0] - 1
      p3[1] = p3[1] + 1
    elif ( c == '4' ):
      p3[0] = p3[0] - 1
    elif ( c == '5' ):
      p3[1] = p3[1] - 1
    elif ( c == '6' ):
      p3[0] = p3[0] + 1
      p3[1] = p3[1] - 1

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
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_sort_test():' )
  print ( '  boundary_sort() is given a boundary word and base point' )
  print ( '  and "rotates" it to have lexically smallest base point.' )

  for k in range ( 1, 8 ):

    name = tetrahex_name ( k )

    w, p = tetrahex_word ( k )
    name1 = '  ' + name
    boundary_print ( w, p, name1 )

    w2, p2 = boundary_sort ( w, p )
    name2 = '  ' + name + ' after sorting:'
    boundary_print ( w2, p2, name2 )

  return

def boundary_to_edge ( w, p ):

#*****************************************************************************80
#
## boundary_to_edge() computes the edges of a shape from its boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
#
#    The edge list contains the sequence of parallelogram IJ coordinates
#    of the nodes that lie on the boundary of the shape, listed
#    in counterclockwise order.
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
#    list W: the boundary word.
#
#    integer P(2): the starting point.
#
#  Output:
#
#    integer E(EN,2): the IJ coordinates of the edge node sequence.  
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

    if ( c == '1' ):
      i = i + 1
    elif ( c == '2' ):
      j = j + 1
    elif ( c == '3' ):
      i = i - 1
      j = j + 1
    elif ( c == '4' ):
      i = i - 1
    elif ( c == '5' ):
      j = j - 1
    elif ( c == '6' ):
      i = i + 1
      j = j - 1
    else:
      print ( '' )
      print ( 'boundary_to_edge(): Fatal error!' )
      print ( '  Illegal boundary word character w(', wi, ')=' + c )
      raise Exception ( 'boundary_to_edge(): Fatal error!' ) 

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
#    20 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_to_edge_test():' )
  print ( '  boundary_to_edge() uses a boundary word to determine' )
  print ( '  the (i,j) coordinates of the edge nodes.' )

  k = 4
  w, p = tetrahex_word ( k )
  name = '  boundary word'
  boundary_print ( w, p, name )

  e = boundary_to_edge ( w, p )
  name = '  edge node coordinates:'

  print ( '' )
  print ( name )
  print ( '' )

  en = e.shape[0]

  for i in range ( 0, en ):
    print ( '  %2d:  %2d  %2d' % ( i, e[i,0], e[i,1] ) )

  return

def boundary_to_vertex ( w, p ):

#*****************************************************************************80
#
## boundary_to_vertex() converts a polyhex description from boundary to vertex.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
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
#    list W: the boundary word.
#
#    integer P(2): the boundary word starting point.
#
#  Output:
#
#    integer V(VN,2): the IJ parallelogram point coordinates of the 
#    vertices bounding the shape.  
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

    if ( c == '1' ):
      i = i + 1
    elif ( c == '2' ):
      j = j + 1
    elif ( c == '3' ):
      i = i - 1
      j = j + 1
    elif ( c == '4' ):
      i = i - 1
    elif ( c == '5' ):
      j = j - 1
    elif ( c == '6' ):
      i = i + 1
      j = j - 1
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
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_to_vertex_test():' )
  print ( '  boundary_to_vertex() converts a boundary word to a vertex list.' )

  k = 4
  w, p = tetrahex_word ( k )
  name = '  boundary word'
  boundary_print ( w, p, name )

  v = boundary_to_vertex ( w, p )
  name = '  vertex list'

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
## boundary_translate() translates a polyhex described by a boundary word.
#
#  Discussion:
#
#    The boundary word describes how to trace the boundary by starting
#    at a base point P=(i,j), and taking a sequence of steps of unit length 
#    in one of 6 directions, as suggested by these diagrams:
#
#          3     2-----*             3     2     *  
#      ^        /                ^    \         /   
#     /        /                /      \       /     
#    J  4-----P     1          J  4     P-----1      
#      /       \                       /             
#     /         \                     /              
#    *     5     6             *-----5     6         
#
#          I-->                      I-->           
#
#    If the current position P has parallelogram coordinates (I,J), then
#    the step of given index moves to
#
#      1  (I+1,J)
#      2  (I,  J+1)
#      3  (I-1,J+1)
#      4  (I-1,J)
#      5  (I,  J-1)
#      6  (I+1,J-1)
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
#    19 June 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'boundary_translate_test():' )
  print ( '  boundary_translate() translates a shape' )
  print ( '  described by its boundary word.' )

  k = 4
  w0, p0 = tetrahex_word ( k )

  d = np.array ( [ -2, + 6 ] )
  w1, p1 = boundary_translate ( w0, p0, d )
#
#  Get the plot range.
#
  imin0, imax0, jmin0, jmax0 = boundary_range ( w0, p0 )
  imin1, imax1, jmin1, jmax1 = boundary_range ( w1, p1 )

  imin = min ( 0, imin0, imin1 )
  imax = max ( 0, imax0, imax1 ) + 1
  jmin = min ( 0, jmin0, jmin1 )
  jmax = max ( 0, jmax0, jmax1 ) + 1
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

def ch_to_digit ( c ):

#*****************************************************************************80
#
## ch_to_digit() returns the integer value of a base 10 digit.
#
#  Example:
#
#     C   DIGIT
#    ---  -----
#    '0'    0
#    '1'    1
#    ...  ...
#    '9'    9
#    ' '   -1
#    'X'   -1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C, the decimal digit, '0' through '9' are legal.
#
#  Output:
#
#    integer DIGIT, the corresponding integer value.  If C was
#    'illegal', then DIGIT is -1.
#
  i0 = ord ( '0' )
  i9 = ord ( '9' )
  ic = ord ( c )

  if ( i0 <= ic and ic <= i9 ):

    digit = ic - i0

  else:

    digit = -1

  return digit

def ch_to_digit_test ( ):

#*****************************************************************************80
#
## ch_to_digit_test() tests ch_to_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', '?', ' ' ] )

  print ( '' )
  print ( 'ch_to_digit_test():' )
  print ( '  ch_to_digit(): character -> decimal digit' )
  print ( '' )
 
  for i in range ( 0, 13 ):
    c = c_test[i]
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )

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
#    19 June 2024
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
#    19 June 2024
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

def tetrahex_name ( index ):

#*****************************************************************************80
#
## tetrahex_name() returns the name of one of the tetrahex polyomonoes.
#
#  Discussion:
#
#    There is a standard name for each:  
#
#     1  bar
#     2  worm
#     3  pistol
#     4  propeller
#     5  arch
#     6  bee
#     7  wave
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
#    integer INDEX, a value between 1 and 7.
#
#  Output:
#
#    string NAME, is the corresponding name.
#
  if ( index == 1 ):
    name = 'arch'
  elif ( index == 2 ):
    name = 'bar'
  elif ( index == 3 ):
    name = 'bee'
  elif ( index == 4 ):
    name = 'pistol'
  elif ( index == 5 ):
    name = 'propeller'
  elif ( index == 6 ):
    name = 'wave'
  elif ( index == 7 ):
    name = 'worm'
  else:
    name = '?'

  return name

def tetrahex_word ( k ):

#*****************************************************************************80
#
## tetrahex_word() returns the boundary word for a tetrahex.
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
#    integer K, a tile index.
#
#  Output:
#
#    list W: the boundary word.
#
#    integer P_IJ(2): the (i,j) coordinates of the base point.
#
  import numpy as np

  p_ij = np.array ( [ 0, 0 ] )

  if ( k == 1 ):
    w = list ( '121232343456165456' )
  elif ( k == 2 ):
    w = list ( '123232323456565656' )
  elif ( k == 3 ):
    w = list ( '12123434545616' )
  elif ( k == 4 ):
    w = list ( '1232123434565656' )
  elif ( k == 5 ):
    w = list ( '121612343234565456' )
  elif ( k == 6 ):
    w = list ( '121232123454565456' )
  elif ( k == 7 ):
    w = list ( '123232123454565656' )
  else:
    print ( '' )
    print ( 'tetrahex_word(): Fatal error!' )
    print ( '  Illegal tile index ', i )
    raise Exception ( 'tetrahex_word(): Fatal error!' )

  return w, p_ij

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
#    19 June 2024
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

if ( __name__ == '__main__' ):
  timestamp ( )
  boundary_word_hexagon_test ( )
  timestamp ( )

