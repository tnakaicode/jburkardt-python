#! /usr/bin/env python
#
e = 0.8
m = 5.0

def p16_fx ( x ):

#*****************************************************************************80
#
## P16_FX evaluates Kepler's Equation.
#
#  Discussion:
#
#    This is Kepler's equation.  The equation has the form:
#
#      X = M + E * sin ( X )
#
#    X represents the eccentric anomaly of a planet, the angle between the
#    perihelion (the point on the orbit nearest to the sun)
#    through the sun to the center of the ellipse, and the
#    line from the center of the ellipse to the planet.
#
#    There are two parameters:
#
#    E is the eccentricity of the orbit, which should be between 0 and 1.0
#
#    M is the angle from the perihelion made by a fictitious planet traveling
#    on a circular orbit centered at the sun, and traveling at a constant
#    angular velocity equal to the average angular velocity of the true planet.
#    M is usually between 0 and 180 degrees, but can have any value.
#
#    For convenience, X and M are measured in degrees.
#
#    Sample results:
#
#    E        M      X
#    -----  ---  ----------
#    0.100    5    5.554589
#    0.200    5    6.246908
#    0.300    5    7.134960
#    0.400    5    8.313903
#    0.500    5    9.950063
#    0.600    5   12.356653
#    0.700    5   16.167990
#    0.800    5   22.656579
#    0.900    5   33.344447
#    0.990    5   45.361023
#    0.990    1   24.725822
#    0.990   33   89.722155
#    0.750   70  110.302
#    0.990    2   32.361007
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Colwell,
#    Solving Kepler's Equation Over Three Centuries,
#    Willmann-Bell, 1993
#
#    Jean Meeus,
#    Astronomical Algorithms,
#    Willman-Bell, Inc, 1991,
#    QB51.3.E43M42
#
#  Parameters:
#
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX(*), the value of the function at X.
#
  import numpy as np

  global e
  global m

  fx = np.pi * ( x - m ) / 180.0 - e * np.sin ( np.pi * x / 180.0 )

  return fx

def p16_fx1 ( x ):

#*****************************************************************************80
#
## P16_FX1 evaluates the derivative of the function for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the abscissa.
#
#    Output, real FX1, the first derivative of the function at X.
#
  import numpy as np

  global e

  fx1 = ( np.pi / 180.0 ) - e * np.pi * np.cos ( np.pi * x / 180.0  ) / 180.0

  return fx1

def p16_fx2 ( x ):

#*****************************************************************************80
#
## P16_FX2 evaluates the second derivative of the function for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the abscissa.
#
#    Output, real FX2, the second derivative of the function at X.
#
  import numpy as np

  global e

  fx2 = e * np.pi ** 2 * np.sin ( np.pi * x / 180.0  ) / 180.0 / 180.0

  return fx2

def p16_rang ( ):

#*****************************************************************************80
#
## P16_RANG returns an interval bounding the root for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  global m

  rang = np.array ( [ m - 180.0, m + 180.0 ] )

  return rang

def p16_root ( i ):

#*****************************************************************************80
#
## P16_ROOT returns a root for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the index of the requested root.
#
#    Output, real X, the value of the root.
#
  x = 0.0

  return x

def p16_root_num ( ):

#*****************************************************************************80
#
## P16_ROOT_NUM returns the number of known roots for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer ROOT_NUM, the number of known roots.
#
  root_num = 0

  return root_num

def p16_start ( i ):

#*****************************************************************************80
#
## P16_START returns a starting point for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the index of the starting point.
#
#    Output, real X, the starting point.
#
  global m

  if ( ( i % 3 ) == 1 ):
    x = 0.0
  elif ( ( i % 3 ) == 2 ):
    x = m + 180.0
  elif ( ( i % 3 ) == 0 ):
    x = m

  return x

def p16_start_num ( ):

#*****************************************************************************80
#
## P16_START_NUM returns the number of starting points for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer START_NUM, the number of starting points.
#
  start_num = 3

  return start_num

def p16_title ( title ):

#*****************************************************************************80
#
## P16_TITLE returns the title of problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'Kepler''s Eccentric Anomaly Equation, in degrees'

  return title

