#! /usr/bin/env python3
#
def boundary_word_area ( s ):

#*****************************************************************************80
#
## boundary_word_area() returns the area of a polyomino defined by a boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Srecko Briek, Gilbert Labelle, Ariane Lacasse,
#    Algorithms for polyominoes based on the discrete Green theorem,
#    Discrete Applied Mathematics,
#    Volume 147, pages 187-205, 2005.
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    integer area: the area of the polyomino.
#
  check = boundary_word_check ( s )

  if ( not check ):
    area = -1
    return area

  s_len = len ( s )
  s.lower ( )

  x = 0
  y = 0
  area = 0
  for i in range ( 0, s_len ):

    if ( s[i] == 'u' ):
      y = y + 1
      area = area + x
    elif ( s[i] == 'd' ):
      y = y - 1
      area = area - x
    elif ( s[i] == 'l' ):
      x = x - 1
    elif ( s[i] == 'r' ):
      x = x + 1

  return area

def boundary_word_area_test ( ):

#*****************************************************************************80
#
## boundary_word_area_test() tests boundary_word_area.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_area_test():' )
  print ( '  boundary_word_area() returns the area of the polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  s = 'rrururullulddldd'
  area = boundary_word_area ( s )
  print ( '  Polyomino defined by "', s, '" has area', area )

  return

def boundary_word_boundary ( s ):

#*****************************************************************************80
#
## boundary_word_boundary(): boundary of a polyomino defined by a boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(n): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    integer X(n+1), Y(n+1): the coordinates of the boundary curve.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    print ( '' )
    print ( 'boundary_word_boundary - Fatal error!' )
    print ( '  Input boundary word "', s, '" is illegal.' )
    return

  s.lower ( )
  s_len = len ( s )
  x = np.zeros ( s_len + 1 )
  y = np.zeros ( s_len + 1 )

  x[0] = 0
  y[0] = 0

  for i in range ( 0, s_len ):

    if ( s[i] == 'r' ):
      x[i+1] = x[i] + 1
      y[i+1] = y[i]
    elif ( s[i] == 'l' ):
      x[i+1] = x[i] - 1
      y[i+1] = y[i]
    elif ( s[i] == 'u' ):
      x[i+1] = x[i]
      y[i+1] = y[i] + 1
    elif ( s[i] == 'd' ):
      x[i+1] = x[i]
      y[i+1] = y[i] - 1

  return x, y

def boundary_word_boundary_plot ( s ):

#*****************************************************************************80
#
## boundary_word_boundary_plot() plots perimeter of polyomino given boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(n): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
  import matplotlib.pyplot as plt
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    print ( '' )
    print ( 'boundary_word_boundary_plot - Fatal error!' )
    print ( '  Input boundary word "', s, '" is illegal.' )
    return

  x, y = boundary_word_boundary ( s )

  plt.clf ( )
  plt.plot ( x, y, '-x', linewidth = 5 )

  v = np.arange ( min ( x ), max ( x ) + 1, 1 )
  plt.xticks ( v )
  v = np.arange ( min ( y ), max ( y ) + 1, 1 )
  plt.yticks ( v )
  plt.grid ( True )
  plt.title ( s )
  plt.axis ( 'equal' )

  return

def boundary_word_boundary_plot_test ( ):

#*****************************************************************************80
#
## boundary_word_boundary_plot_test() tests boundary_word_boundary_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_word_boundary_plot_test():' )
  print ( '  boundary_word_boundary_plot() plots the boundary of a polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  for i in range ( 0, 5 ):

    if ( i == 0 ):
      s = 'rrururullulddldd'
    elif ( i == 1 ):
      s = 'rurdrururulurullddlldldd'
    elif ( i == 2 ):
      s = 'rurdruuluulldrdldd'
    elif ( i == 3 ):
      s = 'rurdrdldrdrurulururdrurululdlulurululdldrdldluldldrd'
    else:
      s = 'rurdruuuldluldldrd'

    boundary_word_boundary_plot ( s )
    filename = s + '_boundary.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "%s"' % ( filename ) )

  return

def boundary_word_boundary_test ( ):

#*****************************************************************************80
#
## boundary_word_boundary_test() tests boundary_word_boundary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_boundary_test():' )
  print ( '  boundary_word_boundary() returns the boundary of a polyomino' )
  print ( '  defined by a given boundary word.' )

  for i in range ( 0, 5 ):

    if ( i == 0 ):
      s = 'rrururullulddldd'
    elif ( i == 1 ):
      s = 'rurdrururulurullddlldldd'
    elif ( i == 2 ):
      s = 'rurdruuluulldrdldd'
    elif ( i == 3 ):
      s = 'rurdrdldrdrurulururdrurululdlulurululdldrdldluldldrd'
    else:
      s = 'rurdruuuldluldldrd'

    x, y = boundary_word_boundary ( s )
    r8vec2_print ( x, y, s )

  return

def boundary_word_centroid ( s ):

#*****************************************************************************80
#
## boundary_word_centroid(): centroid of a polyomino defined by a boundary word.
#
#  Discussion:
#
#    The description of the polyomino is assumed to begin at (0,0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Srecko Briek, Gilbert Labelle, Ariane Lacasse,
#    Algorithms for polyominoes based on the discrete Green theorem,
#    Discrete Applied Mathematics,
#    Volume 147, pages 187-205, 2005.
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    real xc, yc: the coordinates of the centroid.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    xc = np.nan
    yc = np.nan
    return xc, yc

  s_len = len ( s )
  s.lower ( )

  x = 0
  y = 0
  xc = 0.0
  yc = 0.0

  for i in range ( 0, s_len ):

    if ( s[i] == 'u' ):
      y = y + 1
      xc = xc + x**2 / 2.0
    elif ( s[i] == 'd' ):
      y = y - 1
      xc = xc - x**2 / 2.0
    elif ( s[i] == 'l' ):
      x = x - 1
      yc = yc + y**2 / 2.0
    elif ( s[i] == 'r' ):
      x = x + 1
      yc = yc - y**2 / 2.0

  area = boundary_word_area ( s )

  xc = xc / area
  yc = yc / area

  return xc, yc

def boundary_word_centroid_test ( ):

#*****************************************************************************80
#
## boundary_word_centroid_test() tests boundary_word_centroid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_centroid_test():' )
  print ( '  boundary_word_centroid() returns the centroid of the polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  s = 'rrururullulddldd'
  xc, yc = boundary_word_centroid ( s )
  print ( '  Polyomino defined by "', s, '"' )
  print ( '  has centroid (', xc, ',', yc, ')' )

  return

def boundary_word_check ( s ):

#*****************************************************************************80
#
## boundary_word_check() checks a boundary word.
#
#  Discussion:
#
#    A valid boundary word must contain an even number of entries, with
#    equal numbers of 'u' and 'd', and equal numbers of 'l' and 'r'.
#
#    The pairs 'lr', 'rl', 'ud' and 'du' must not occur.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    boolean check: true if s represent a valid string.
#
  s_len = len ( s )
  s.lower ( )

  for i in range ( 0, s_len - 1 ):

    if ( i < s_len - 1 ):
      c1 = s[i]
      c2 = s[i+1]
    else:
      c1 = s[i]
      c2 = s[0]

    if ( ( c1 == 'u' and c2 == 'd' ) or \
         ( c1 == 'd' and c2 == 'u' ) or \
         ( c1 == 'l' and c2 == 'r' ) or \
         ( c1 == 'r' and c2 == 'l' ) ):
      check = False
      return check

  v = 0
  h = 0

  for i in range ( 0, s_len ):

    if ( s[i] == 'u' ):
      v = v + 1
    elif ( s[i] == 'd' ):
      v = v - 1
    elif ( s[i] == 'l' ):
      h = h - 1
    elif ( s[i] == 'r' ):
      h = h + 1
    else:
      check = False
      return check

  check = ( ( v == 0 ) and ( h == 0 ) )

  return check

def boundary_word_check_test ( ):

#*****************************************************************************80
#
## boundary_word_check_test() tests boundary_word_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_check_test():' )
  print ( '  boundary_word_check() checks that a boundary word is valid.' )
  print ( '' )

  s = 'rrudururullulddldd'
  check = boundary_word_check ( s )
  print ( '  boundary word "', s, '" check is ', check )

  s = 'rrururullulddldd'
  check = boundary_word_check ( s )
  print ( '  boundary word "', s, '" check is ', check )
  
  s = 'rrururullulldldd'
  check = boundary_word_check ( s )
  print ( '  boundary word "', s, '" check is ', check )

  s = 'rrururullwlldldd'
  check = boundary_word_check ( s )
  print ( '  boundary word "', s, '" check is ', check )

  return

def boundary_word_is_convex ( s ):

#*****************************************************************************80
#
## boundary_word_is_convex(): true if the polygon is convex.
#
#  Discussion:
#
#    Because our boundary word alphabet is limited to four letters,
#    our shapes are limited to strictly horizontal and vertical sides.
#    Under these restrictions, the only convex shape is a rectangle.
#
#    We can easily detect this by considering the first four distinct
#    characters in the boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Srecko Briek, Gilbert Labelle, Ariane Lacasse,
#    Algorithms for polyominoes based on the discrete Green theorem,
#    Discrete Applied Mathematics,
#    Volume 147, pages 187-205, 2005.
#
#  Input:
#
#    char s(*): a vector of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    logical VALUE: true if the polyomino is convex.
#
  import numpy as np

  value = False
#
#  Lowercase the string.
#
  s.lower ( )
#
#  Check that the string is legal.
#
  check = boundary_word_check ( s )

  if ( not check ):
    print ( '' )
    print ( 'boundary_word_is_convex(): Fatal error!' )
    print ( '  The boundary word does not pass boundary_word_check().' )
    return value
#
#  Replace the string by its representative.
#
  s2 = boundary_word_representative ( s )
#
#  Remove repeated characters.
#
  s3 = chvec_reduce ( s2 )
#
#  The representative must be of length 4.
#
  s3_len = len ( s3 )
  if ( s3_len != 4 ):
    return value
#
#  The representative can only be one of two strings.
#
  if ( chvec_eq ( s3, 'dlur' ) or chvec_eq ( s3, 'drul' ) ):
    value = True

  return value

def boundary_word_is_convex_test ( ):

#*****************************************************************************80
#
## boundary_word_is_convex_test() tests boundary_word_is_convex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Bell,
#    The dynamics of spinning polyominoes,
#    Gathering for Gardner, G4G13.
#
  print ( '' )
  print ( 'boundary_word_is_convex_test():' )
  print ( '  boundary_word_is_convex() reports whether a shape is' )
  print ( '  convex, given its boundary word.' )
  print ( '' )

  for i in range ( 0, 12 ):
    c = pentomino_symbol ( i )
    s = pentomino_to_boundary_word ( c )
    convex = boundary_word_is_convex ( s )
    if ( convex ):
      print ( '  ', c, ' pentomino defined by "', s, '" is     convex.' )
    else:
      print ( '  ', c, ' pentomino defined by "', s, '" is NOT convex.' )

  return

def boundary_word_moment ( s ):

#*****************************************************************************80
#
## boundary_word_moment(): moment of inertia of polyomino given boundary word.
#
#  Discussion:
#
#    The description of the polyomino is assumed to begin at (0,0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Bell,
#    The dynamics of spinning polyominoes,
#    Gathering for Gardner, G4G13.
#
#    Srecko Briek, Gilbert Labelle, Ariane Lacasse,
#    Algorithms for polyominoes based on the discrete Green theorem,
#    Discrete Applied Mathematics,
#    Volume 147, pages 187-205, 2005.
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    real xc, yc: the coordinates of the centroid.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    moment = np.nan
    return moment

  s_len = len ( s )
  s.lower ( )

  x = 0
  y = 0
  moment = 0.0

  for i in range ( 0, s_len ):

    if ( s[i] == 'u' ):
      moment = moment + x * y + x / 3.0 + x**3 / 3.0 + x * y**2
      y = y + 1
    elif ( s[i] == 'd' ):
      moment = moment + x * y - x / 3.0 - x**3 / 3.0 - x * y**2
      y = y - 1
    elif ( s[i] == 'l' ):
      x = x - 1
    elif ( s[i] == 'r' ):
      x = x + 1

  area = boundary_word_area ( s )
  xc, yc = boundary_word_centroid ( s )

  moment = moment - area * ( xc**2 + yc**2 )

  return moment

def boundary_word_moment_test ( ):

#*****************************************************************************80
#
## boundary_word_moment_test() tests boundary_word_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Bell,
#    The dynamics of spinning polyominoes,
#    Gathering for Gardner, G4G13.
#
  print ( '' )
  print ( 'boundary_word_moment_test():' )
  print ( '  boundary_word_moment() returns the moment of inertia of the ' )
  print ( '  polyomino defined by a given boundary word.' )
  print ( '' )

  s = 'rrururullulddldd'
  moment = boundary_word_moment ( s )
  print ( '  Polyomino defined by "', s, '" has moment', moment )

  for i in range ( 0, 12 ):
    c = pentomino_symbol ( i )
    s = pentomino_to_boundary_word ( c )
    moment_exact = pentomino_moment ( c )
    moment_computed = boundary_word_moment ( s )
    print ( ' ', c, ' pentomino defined by "', s, '"', end = '' )
    print ( ' has moment', moment_computed, ', exact is ', moment_exact )

  return

def boundary_word_parity ( s ):

#*****************************************************************************80
#
## boundary_word_parity(): parity of a polyomino defined by a boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    integer parity: the parity of the polyomino.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    parity = np.nan
    return parity

  s_len = len ( s )
  s.lower ( )

  bw = np.zeros ( 2, dtype = int )

  for i in range ( 0, s_len ):

    if ( i == 0 ):
      if ( s[i] == 'u' or s[i] == 'r' ):
        color = 0
      else:
        color = 1
    elif ( s[i] == s[i-1] ):
      color = 1 - color

    bw[color] = bw[color] + 1

  parity = ( bw[0] - bw[1] ) // 4

  return parity

def boundary_word_parity_test ( ):

#*****************************************************************************80
#
## boundary_word_parity_test() tests boundary_word_parity().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_parity_test():' )
  print ( '  boundary_word_parity() returns the parity of the polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  for i in range ( 0, 5 ):

    if ( i == 0 ):
      s = 'rrururullulddldd'
    elif ( i == 1 ):
      s = 'rurdrururulurullddlldldd'
    elif ( i == 2 ):
      s = 'rurdruuluulldrdldd'
    elif ( i == 3 ):
      s = 'rurdrdldrdrurulururdrurululdlulurululdldrdldluldldrd'
    else:
      s = 'rurdruuuldluldldrd'

    parity = boundary_word_parity ( s )
    print ( '  Polyomino defined by "', s, '" has parity', parity )

  return

def boundary_word_perimeter ( s ):

#*****************************************************************************80
#
## boundary_word_perimeter(): perimeter of a polyomino defined by a boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    integer perimeter: the perimeter of the polyomino define by the boundary
#    word.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    perimeter = np.nan
    return perimeter

  perimeter = len ( s )

  return perimeter

def boundary_word_perimeter_test ( ):

#*****************************************************************************80
#
## boundary_word_perimeter_test() tests boundary_word_perimeter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_perimeter_test():' )
  print ( '  boundary_word_perimeter() returns the perimeter of the polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  s = 'rrururullulddldd'
  perimeter = boundary_word_perimeter ( s )
  print ( '  Polyomino defined by "', s, '" has perimeter', perimeter )

  return

def boundary_word_plot ( s ):

#*****************************************************************************80
#
## boundary_word_plot() plots a polyomino defined by a boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
  import matplotlib.pyplot as plt

  check = boundary_word_check ( s )

  if ( not check ):
    print ( '' )
    print ( 'boundary_word_plot(): Fatal error!' )
    print ( '  Input boundary word "', s, '" is illegal.' )
    return

  xpoly, ypoly = boundary_word_boundary ( s )

  xmin, xmax, ymin, ymax = boundary_word_range ( s )

  plt.clf ( )

  for x in range ( xmin, xmax ):
    for y in range ( ymin, ymax ):
      interior = polygon_contains_point ( xpoly, ypoly, x+0.5, y+0.5 )
      if ( interior ):
        if ( ( ( x + y ) % 2 ) == 0 ):
          plt.fill ( [ x, x+1, x+1, x ], [ y, y, y+1, y+1 ], 'red' )
        else:
          plt.fill ( [ x, x+1, x+1, x ], [ y, y, y+1, y+1 ], 'black' )
#
#  Mark the origin.
#
  plt.plot ( 0.0, 0.0, 'k.', markersize = 40 )

  plt.title ( s, fontsize = 16 )
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  return

def boundary_word_plot_test ( ):

#*****************************************************************************80
#
## boundary_word_plot_test() tests boundary_word_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'boundary_word_plot_test():' )
  print ( '  boundary_word_plot() plots a polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  for i in range ( 0, 5 ):

    if ( i == 0 ):
      s = 'rrururullulddldd'
    elif ( i == 1 ):
      s = 'rurdrururulurullddlldldd'
    elif ( i == 2 ):
      s = 'rurdruuluulldrdldd'
    elif ( i == 3 ):
      s = 'rurdrdldrdrurulururdrurululdlulurululdldrdldluldldrd'
    elif ( i == 4 ):
      s = 'rurdruuuldluldldrd'

    boundary_word_plot ( s )
    filename = s + '_plot.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "%s"' % ( filename ) )
    plt.show ( block = False )
    plt.close ( )

  return

def boundary_word_range ( s ):

#*****************************************************************************80
#
## boundary_word_range(): range of a polyomino defined by a boundary word.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#  Output:
#
#    integer xmin, xmax, ymin, ymax: the range of the polyomino.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    area = np.nan
    return area

  s.lower ( )
  s_len = len ( s )
  x = np.zeros ( s_len + 1, dtype = int )
  y = np.zeros ( s_len + 1, dtype = int )

  x[0] = 0
  y[0] = 0

  for i in range ( 0, s_len ):

    if ( s[i] == 'r' ):
      x[i+1] = x[i] + 1
      y[i+1] = y[i]
    elif ( s[i] == 'l' ):
      x[i+1] = x[i] - 1
      y[i+1] = y[i]
    elif ( s[i] == 'u' ):
      x[i+1] = x[i]
      y[i+1] = y[i] + 1
    elif ( s[i] == 'd' ):
      x[i+1] = x[i]
      y[i+1] = y[i] - 1

  xmin = min ( x )
  xmax = max ( x )
  ymin = min ( y )
  ymax = max ( y )

  return xmin, xmax, ymin, ymax

def boundary_word_range_test ( ):

#*****************************************************************************80
#
## boundary_word_range_test() tests boundary_word_range().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_range_test():' )
  print ( '  boundary_word_range() determines the range of a polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  for i in range ( 0, 5 ):

    if ( i == 0 ):
      s = 'rrururullulddldd'
    elif ( i == 1 ):
      s = 'rurdrururulurullddlldldd'
    elif ( i == 2 ):
      s = 'rurdruuluulldrdldd'
    elif ( i == 3 ):
      s = 'rurdrdldrdrurulururdrurululdlulurululdldrdldluldldrd'
    else:
      s = 'rurdruuuldluldldrd'

    xmin, xmax, ymin, ymax = boundary_word_range ( s )
    print ( '  Polyomino defined by "', s, '"' )
    print ( '  has', xmin, '<= x <=', xmax, ',', ymin, '<= y <=', ymax )

  return

def boundary_word_representative ( c ):

#*****************************************************************************80
#
## boundary_word_representative() finds the representative for a boundary word.
#
#  Discussion:
#
#    Mathematically, a boundary word is a "necklace", that is, an equivalence
#    class of strings of characters, invariant under rotation.  Thus,
#    the following five boundary words are in the same equivalence class:
#      'abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd' 
#    This function is given a boundary word, and returns the representative
#    for the class, that is, the lexically first element.
#
#    Two boundary words are equal if and only if they have the same
#    representative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char c(*): a boundary word.
#
#  Output:
#
#    char crep(*): the representative for the boundary word.
#
  import numpy as np

  n = len ( c )

  crep = c

  for i in range ( 0, n ):
    if ( i == 0 ):
      c1 = c
      crep = c
    else:
      c1 = c1[1:n] + c1[0]
      if ( chvec_lt ( c1, crep ) ):
        crep = c1

  return crep
 
def boundary_word_representative_test ( ):

#*****************************************************************************80
#
## boundary_word_representative_test() tests boundary_word_representative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'boundary_word_representative_test():' )
  print ( '  boundary_word_representative() returns the representative' )
  print ( '  for a boundary word.' )
  print ( '' )
  print ( '  boundary word                   representative' )
  print ( '' )

  for i in range ( 0, 8 ):

    if ( i == 0 ):
      c = 'cdeab'
    elif ( i == 1 ):
      c = 'carpathian'
    elif ( i == 2 ):
      c = 'pathiancar'
    elif ( i == 3 ):
      c = 'naihtaprac'
    elif ( i == 4 ):
      c = 'rrururullulddldd'
    elif ( i == 5 ):
      c = 'rurdrururulurullddlldldd'
    elif ( i == 6 ):
      c = 'llddlldlddrurdrururuluru'
    elif ( i == 7 ):
      c = 'ddldllddllurulurururdrur'

    crep = boundary_word_representative ( c )
    print ( '  %-25s  %-25s' % ( c, crep ) )

  return

def boundary_word_sense ( s ):

#*****************************************************************************80
#
## boundary_word_sense() returns the sense of a boundary word.
#
#  Discussion:
#
#    The sense is +1 if the boundary word traces the boundary of the polyomino
#    in a counterclockwise sense, and -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char c(*): a character string of 'u', 'd', 'l' and 'r' that
#    represents a path around the boundary of a polyomino.
#
#  Output:
#
#    integer sense: the sense.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    sense = np.nan
    return sense

  s_len = len ( s )
  s.lower ( )

  sense = 0
 
  for i in range ( 0, s_len ):

    if ( i < s_len - 1 ):
      c1 = s[i]
      c2 = s[i+1]
    else:
      c1 = s[i]
      c2 = s[0]

    if ( ( c1 == 'd' and c2 == 'r' ) or \
         ( c1 == 'l' and c2 == 'd' ) or \
         ( c1 == 'r' and c2 == 'u' ) or \
         ( c1 == 'u' and c2 == 'l' ) ):
      sense = sense + 1
    elif ( ( c1 == 'd' and c2 == 'l' ) or \
           ( c1 == 'l' and c2 == 'u' ) or \
           ( c1 == 'r' and c2 == 'd' ) or \
           ( c1 == 'u' and c2 == 'r' ) ):
      sense = sense - 1

  sense = sense // 4

  return sense

def boundary_word_sense_test ( ):

#*****************************************************************************80
#
## boundary_word_sense_test() tests boundary_word_sense().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'boundary_word_sense_test():' )
  print ( '  boundary_word_sense() returns the sense of the polyomino' )
  print ( '  defined by a given boundary word.' )
  print ( '' )

  transforms = np.array ( [ \
    'udlr', \
    'udrl', \
    'dulr', \
    'durl', \
    'lrdu', \
    'lrud', \
    'rlud', \
    'rldu' ] )

  c = 'F'
  s = pentomino_to_boundary_word ( c )
  print ( '  Polyomino "', c, '" has boundary word "', s, '"' )
  print ( '' )

  for i in range ( 0, 8 ):
    udlr = transforms[i]
    s2 = boundary_word_transform ( s, udlr )
    sense = boundary_word_sense ( s2 )
    print ( '  "', s2, '" has sense', sense )

  return

def boundary_word_square_test ( ):

#*****************************************************************************80
#
## boundary_word_square_test() tests boundary_word_square().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'boundary_word_square_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test boundary_word_square()' )

  boundary_word_area_test ( )
  boundary_word_boundary_test ( )
  boundary_word_boundary_plot_test ( )
  boundary_word_centroid_test ( )
  boundary_word_check_test ( )
  boundary_word_is_convex_test ( )
  boundary_word_moment_test ( )
  boundary_word_parity_test ( )
  boundary_word_perimeter_test ( )
  boundary_word_plot_test ( )
  boundary_word_range_test ( )
  boundary_word_representative_test ( )
  boundary_word_sense_test ( )
  boundary_word_transform_test ( )

  chvec_lt_test ( )

  pentomino_moment_test ( )
  pentomino_symbol_test ( )
  pentomino_to_boundary_word_test ( )

  polygon_contains_point_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'boundary_word_square_test():' )
  print ( '  Normal end of execution.' )

  return

def boundary_word_transform ( s, udlr ):

#*****************************************************************************80
#
## boundary_word_transform() transforms a boundary word.
#
#  Discussion:
#
#    The boundary word defines a path along the boundary of a polyomino.
#    This path has a sense: +1 for counterclockwise, -1 otherwise.
#    The transformed boundary word will have the same sense as the original.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    numpy.str s(*): a string of the characters 'u', 'd', 'l' and 'r' that should
#    represent a path around the boundary of a polyomino.
#
#    numpy.str udlr(4): a permutation of the characters.  
#    The following are legal:
#    'udlr': no change
#    'udrl': up/down reflection
#    'dulr': left/right reflection
#    'durl': up/down reflection and left/right reflection = rotation by 180
#    'lrdu': rotation by 90
#    'lrud': rotation by 90, then up/down reflection
#    'rlud': rotation by 270
#    'rldu': rotation by 270, then up/down reflection
#
#  Output:
#
#    numpy.str s2: the boundary word for the transformed string.
#
  import numpy as np

  check = boundary_word_check ( s )

  if ( not check ):
    s2 = ''
    return s2

  s.lower ( )

  n = len ( s )

  s2 = ''

  for i in range ( 0, n ):
    if ( s[i] == 'u' ):
      s2 = s2 + udlr[0]
    elif ( s[i] == 'd' ):
      s2 = s2 + udlr[1]
    elif ( s[i] == 'l' ):
      s2 = s2 + udlr[2]
    elif ( s[i] == 'r' ):
      s2 = s2 + udlr[3]
#
#  If the transformation would reverse the sense of the boundary word,
#  reverse the boundary word to preserve the sense.
#
  if ( ( udlr[0] == 'u' and udlr[1] == 'd' and udlr[2] == 'r' and udlr[3] == 'l' ) or \
       ( udlr[0] == 'u' and udlr[1] == 'd' and udlr[2] == 'r' and udlr[3] == 'l' ) or \
       ( udlr[0] == 'u' and udlr[1] == 'd' and udlr[2] == 'r' and udlr[3] == 'l' ) or \
       ( udlr[0] == 'u' and udlr[1] == 'd' and udlr[2] == 'r' and udlr[3] == 'l' ) ):
    s3 = s2
    s2 = ''
    for i in range ( 0, n ):
      s2 = s2 + s3[n-1-i]

  return s2

def boundary_word_transform_test ( ):

#*****************************************************************************80
#
## boundary_word_transform_test() tests boundary_word_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  transforms = [ \
    'udlr', \
    'udrl', \
    'dulr', \
    'durl', \
    'lrdu', \
    'lrud', \
    'rlud', \
    'rldu' ]

  print ( '' )
  print ( 'boundary_word_transform_test():' )
  print ( '  boundary_word_transform() returns the boundary word of a ' )
  print ( '  transformed polyomino.' )
  print ( '' )

  c = 'F'
  s = pentomino_to_boundary_word ( c )
  print ( '  Polyomino "', c, '" has boundary word"', s, '"' )

  for i in range ( 0, 8 ):
    udlr = transforms[i]
    s2 = boundary_word_transform ( s, udlr )
    print ( '  ', udlr, ' transforms boundary word to "', s2, '"' )
    boundary_word_plot ( s2 )
    filename = s2 + '_' + udlr + '_transform.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "%s"' % ( filename ) )
    plt.show ( block = False )
    plt.close ( )

  return

def chvec_eq ( c1, c2 ):

#*****************************************************************************80
#
## chvec_eq() is TRUE if one character vector is equal to another.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char C1(N1), C2(N2): two character vectors.
#
#  Output:
#
#    logical equals: is TRUE if N1=N2 and C1=C2 for all entries.
#
  n1 = len ( c1 )
  n2 = len ( c2 )

  if ( n1 != n2 ):
    return False

  n = n1
  for i in range ( 0, n ):
    if ( c1[i] != c2[i] ):
      return False

  return True

def chvec_lt ( c1, c2 ):

#*****************************************************************************80
#
## chvec_lt() is TRUE if one character vector is less than another.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char C1(N1), C2(N2): two character vectors.
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

def chvec_lt_test ( ):

#*****************************************************************************80
#
## chvec_lt_test() tests chvec_lt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chvec_lt_test():' )
  print ( '  chvec_lt(c1,c2) is TRUE if c1 < c2' )
  print ( '  for character strings c1 and c2.' )
  print ( '' )
  print ( '  C1                    C2                    C1<C2?' )
  print ( '' )

  c1 = 'minnesota'
  c2 = 'minnesota'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'Minnesota'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minnesota2'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minnesot'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minne'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'minnesotan'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = ' minnesota'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'alaska'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  c1 = 'minnesota'
  c2 = 'wyoming'
  is_less_than = chvec_lt ( c1, c2 )
  print ( '  %-20s  %-20s  %s' % ( c1, c2, is_less_than ) )

  return

def chvec_reduce ( cv1 ):

#*****************************************************************************80
#
## chvec_reduce() reduces strings of the same character to a single instance.
#
#  Example:
#
#    Input:
#
#      cv1 = ( 'A', 'L', 'L', 'I', 'F', 'E', 'E', 'L' ).
#
#    Output:
#
#      cv2 = ( 'A', 'L', 'I', 'F', 'E', 'L' ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character cv1(n1): the vector to be reduced.
#
#  Output:
#
#    character cv2(n2): the reduced vector.
#
  n1 = len ( cv1 )

  n2 = 0
  cv2 = ''

  if ( n1 < 1 ):
    return cv2

  i = 0
  n2 = 0
  cv2 = cv1[i]
  co = cv1[i]

  for i in range ( 1, n1 ):
    if ( cv1[i] != co ):
      n2 = n2 + 1
      cv2 = cv2 + cv1[i]
    co = cv1[i]

  return cv2

def chvec_reduce_test ( ):

#*****************************************************************************80
#
## chvec_reduce_test tests chvec_reduce().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2021
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chvec_reduce_test():' )
  print ( '  chvec_reduce() replaces a string of the same character' )
  print ( '  by a single occurrence.' )
  print ( '' )
  print ( '  cv1                    cv2' )
  print ( '' )

  cv1 = 'minnesota'
  cv2 = chvec_reduce ( cv1 )
  print ( '  %-20s  %-20s' % ( cv1, cv2 ) )

  cv1 = 'all love ends'
  cv2 = chvec_reduce ( cv1 );
  print ( '  %-20s  %-20s' % ( cv1, cv2 ) )

  cv1 = 'allloveends'
  cv2 = chvec_reduce ( cv1 )
  print ( '  %-20s  %-20s' % ( cv1, cv2 ) )

  cv1 = 'allLoveEnds'
  cv2 = chvec_reduce ( cv1 )
  print ( '  %-20s  %-20s' % ( cv1, cv2 ) )

  cv1 = 'July year 1776'
  cv2 = chvec_reduce ( cv1 )
  print ( '  %-20s  %-20s' % ( cv1, cv2 ) )

  return

def pentomino_moment ( c ):

#*****************************************************************************80
#
## pentomino_moment() returns the moment of a pentomino.
#
#  Discussion:
#
#    Legal symbols are F, I, L, P, N, T, U, V, W, X, Y, Z.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char c: the symbol for a pentomino.
#
#  Output:
#
#    real moment: the moment of inertia of the pentomino.
#
  c.upper ( )

  if ( c == 'F' ):
    moment = 4.8
  elif ( c == 'I' ):
    moment = 10.0
  elif ( c == 'L' ):
    moment = 7.6
  elif ( c == 'P' ):
    moment = 4.0
  elif ( c == 'N' ):
    moment = 6.4
  elif ( c == 'T' ):
    moment = 5.2
  elif ( c == 'U' ):
    moment = 5.2
  elif ( c == 'V' ):
    moment = 6.4
  elif ( c == 'W' ):
    moment = 5.6
  elif ( c == 'X' ):
    moment = 4.0
  elif ( c == 'Y' ):
    moment = 6.0
  elif ( c == 'Z' ):
    moment = 6.0
  else:
    print ( '' )
    print ( 'pentomino_moment - Fatal error!' )
    print ( '  Unrecognized pentomino symbol "', c, '".' )

  moment = moment + 5.0 / 6.0

  return moment

def pentomino_moment_test ( ):

#*****************************************************************************80
#
## pentomino_moment_test() tests pentomino_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pentomino_moment_test():' )
  print ( '  pentomino_moment() returns the moment of inertia' )
  print ( '  for the i-th pentomino.' )
  print ( '' )

  for i in range ( 0, 12 ):
    c = pentomino_symbol ( i )
    moment = pentomino_moment ( c )
    print ( '  %2d  "%s"  %g' % ( i, c, moment ) )

  return

def pentomino_symbol ( i ):

#*****************************************************************************80
#
## pentomino_symbol() returns the symbol of a pentomino.
#
#  Discussion:
#
#    Legal symbols are F, I, L, P, N, T, U, V, W, X, Y, Z.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer i: the index for a pentomino, from 1 to 12.
#
#  Output:
#
#    char c: the symbol for a pentomino.
#
  s = 'FILPNTUVWXYZ'

  if ( 0 <= i and i < 12 ):
    c = s[i]
  else:
    print ( '' )
    print ( 'pentomino_symbol- Fatal error!' )
    print ( '  Illegal pentomino index', i )

  return c

def pentomino_symbol_test ( ):

#*****************************************************************************80
#
## pentomino_symbol_test() tests pentomino_symbol().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pentomino_symbol_test():' )
  print ( '  pentomino_symbol() returns the symbol for the i-th pentomino.' )
  print ( '' )

  for i in range ( 0, 12 ):
    c = pentomino_symbol ( i )
    print ( '  %2d  "%s"' % ( i, c ) )

  return

def pentomino_to_boundary_word ( c ):

#*****************************************************************************80
#
## pentomino_to_boundary_word() is given a pentomino and returns its boundary word.
#
#  Discussion:
#
#    Legal pentomino symbols are F, I, L, P, N, T, U, V, W, X, Y, Z.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    char c: the symbol for a pentomino.
#
#  Output:
#
#    char s(*): the boundary word that describes the pentomino.
#
  c.upper ( )

  if ( c == 'F' ):
    s = 'ruurulldldrd'
  elif ( c == 'I' ):
    s = 'ruuuuulddddd'
  elif ( c == 'L' ):
    s = 'rruluuuldddd'
  elif ( c == 'P' ):
    s = 'ruruullddd'
  elif ( c == 'N' ):
    s = 'ruuruuldlddd'
  elif ( c == 'T' ):
    s = 'ruurullldrdd'
  elif ( c == 'U' ):
    s = 'rrruuldluldd'
  elif ( c == 'V' ):
    s = 'rrrulluulddd'
  elif ( c == 'W' ):
    s = 'rrulululddrd'
  elif ( c == 'X' ):
    s = 'rurululdldrd'
  elif ( c == 'Y' ):
    s = 'ruurululdddd'
  elif ( c == 'Z' ):
    s = 'rruluulldrdd'
  else:
    print ( '' )
    print ( 'pentomino_to_boundary_word - Fatal error!' )
    print ( '  Unrecognized pentomino symbol "', c, '".' )

  return s

def pentomino_to_boundary_word_test ( ):

#*****************************************************************************80
#
## pentomino_to_boundary_word_test() tests pentomino_to_boundary word().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pentomino_to_boundary_word_test():' )
  print ( '  pentomino_to_boundary_word() returns the boundary word' )
  print ( '  for the i-th pentomino.' )
  print ( '' )

  for i in range ( 0, 12 ):
    c = pentomino_symbol ( i )
    s = pentomino_to_boundary_word ( c )
    print ( ' ', i, ' ', c, ' ', s )

  return

def polygon_contains_point ( px, py, qx, qy ):

#*****************************************************************************80
#
## polygon_contains_point() finds if a point is inside a simple polygon.
#
#  Discussion:
#
#    A simple polygon is one whose boundary never crosses itself.
#    The polygon does not need to be convex.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Shimrat,
#    Position of Point Relative to Polygon,
#    ACM Algorithm 112,
#    Communications of the ACM,
#    Volume 5, Number 8, page 434, August 1962.
#
#  Input:
#
#    real PX(N), PY(N): the coordinates of the vertices of the polygon.
#
#    real QX, QY: the coordinates of the point to be tested.
#
#  Output:
#
#    logical INSIDE: TRUE if the point is inside the polygon.
#
  inside = False

  n = len ( px )

  x1 = px[n-1]
  y1 = py[n-1]

  for i in range ( 0, n ):

    x2 = px[i]
    y2 = py[i]

    if ( ( y1 < qy and qy <= y2 ) or ( qy <= y1 and y2 < qy ) ):
      if ( ( qx - x1 ) - ( qy - y1 ) * ( x2 - x1 ) / ( y2 - y1 ) < 0.0 ):
        inside = not inside

    x1 = x2
    y1 = y2

  return inside

def polygon_contains_point_test ( ):

#*****************************************************************************80
#
## polygon_contains_point_test() tests polygon_contains_point().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  test_num = 4
 
  px = np.array ( [ 0.0, 1.0, 2.0, 1.0, 0.0 ] )
  py = np.array ( [ 0.0, 0.0, 1.0, 2.0, 2.0 ] )

  qx = np.array ( [ 1.0, 3.0, 0.1,  0.5 ] )
  qy = np.array ( [ 1.0, 4.0, 1.0, -0.25 ] )

  print ( '' )
  print ( 'polygon_contains_point_test():' )
  print ( '  polygon_contains_point() determines if' )
  print ( '  a point is in a polygon.' )

  r8vec2_print ( px, py, '  The polygon vertices:' )

  print ( '' )
  print ( '          P          Inside' )
  print ( '' )

  for i in range ( 0, test_num ):
  
    inside = polygon_contains_point ( px, py, qx[i], qy[i] )

    print ( '  (%8.4f,%8.4f)    %s' % ( qx[i], qy[i], inside ) )
 
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  from r8mat_print_some import r8mat_print_some

  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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
  boundary_word_square_test ( )
  timestamp ( )

