#! /usr/bin/env python
#
def p15_fx ( x ):

#*****************************************************************************80
#
## P15_FX evaluates a pathological function for Newton's method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 July 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Donovan, Arnold Miller, Timothy Moreland,
#    Pathological Functions for Newton's Method,
#    American Mathematical Monthly, January 1993, pages 53-58.
#
#  Parameters:
#
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX(*), the value of the function at X.
#
  import numpy as np

  if ( x < 0.0 ):
    fx = - abs ( x ) ** ( 1.0 / 3.0 ) * np.exp ( - x ** 2 )
  elif ( x == 0.0 ):
    fx = 0.0
  elif ( 0.0 < x ):
    fx = abs ( x ) ** ( 1.0 / 3.0 ) * np.exp ( - x ** 2 )

  return fx

def p15_fx1 ( x ):

#*****************************************************************************80
#
## P15_FX1 evaluates the derivative of the function for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
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
  from r8_cube_root import r8_cube_root

  fx1 = ( 1.0 - 6.0 * x ** 2 ) * r8_cube_root ( x ) * np.exp ( - x ** 2 ) \
    / ( 3.0 * x )

  return fx1

def p15_fx2 ( x ):

#*****************************************************************************80
#
## P15_FX2 evaluates the second derivative of the function for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
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
  from r8_cube_root import r8_cube_root

  fx2 = ( - 2.0 - 30.0 * x ** 2 + 36.0 * x ** 4 ) * r8_cube_root ( x ) \
    * exp ( - x ** 2 ) / ( 9.0 * x ** 2 )

  return fx2

def p15_rang ( ):

#*****************************************************************************80
#
## P15_RANG returns an interval bounding the root for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
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

  rang = np.array ( [ - 10.0, 10.0 ] )

  return rang

def p15_root ( i ):

#*****************************************************************************80
#
## P15_ROOT returns a root for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
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

def p15_root_num ( ):

#*****************************************************************************80
#
## P15_ROOT_NUM returns the number of known roots for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer ROOT_NUM, the number of known roots.
#
  root_num = 1

  return root_num

def p15_start ( i ):

#*****************************************************************************80
#
## P15_START returns a starting point for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
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
  if ( ( i % 2 ) == 1 ):
    x = 0.01
  elif ( ( i % 2 ) == 0 ):
    x = - 0.25

  return x

def p15_start_num ( ):

#*****************************************************************************80
#
## P15_START_NUM returns the number of starting points for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer START_NUM, the number of starting points.
#
  start_num = 2

  return start_num

def p15_title ( title ):

#*****************************************************************************80
#
## P15_TITLE returns the title of problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'Donovan/Miller/Moreland Pathological Function'

  return title

