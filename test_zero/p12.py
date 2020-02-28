#! /usr/bin/env python
#
factor = 1000.0

def p12_fx ( x ):

#*****************************************************************************80
#
## P12_FX evaluates Flat Stanley.
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
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX(*), the value of the function at X.
#
  import numpy as np
  global factor

  if ( x == 1.0 ):
    fx = 0.0
  elif ( x < 1.0 ):
    fx = - np.exp ( np.log ( factor ) + np.log ( abs ( x - 1.0 ) ) - 1.0 / ( x - 1.0 ) ** 2 )
  elif ( 1.0 < x ):
    fx = + np.exp ( np.log ( factor ) + np.log ( abs ( x - 1.0 ) ) - 1.0 / ( x - 1.0 ) ** 2 )

  return fx

def p12_fx1 ( x ):

#*****************************************************************************80
#
## P12_FX1 evaluates the derivative of the function for problem 12.
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
#    Input, real X, the abscissa.
#
#    Output, real FX1, the first derivative of the function at X.
#
  import numpy as np

  global factor

  if ( x == 1.0 ):
    fx1 = 0.0
  else:
    y = x - 1.0
    fx1 = factor * np.exp ( - 1.0 / y ** 2 ) * ( y ** 2 + 2.0 ) / y ** 2

  return fx1

def p12_fx2 ( x ):

#*****************************************************************************80
#
## P12_FX2 evaluates the second derivative of the function for problem 12.
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
#    Input, real X, the abscissa.
#
#    Output, real FX2, the second derivative of the function at X.
#
  import numpy as np
  global factor

  if ( x == 1.0 ):
    fx2 = 0.0
  else:
    y = x - 1.0
    fx2 = - 2.0 * factor * np.exp ( - 1.0 / y ** 2 ) * ( y ** 2 - 2.0 ) / y ** 5

  return fx2

def p12_rang ( ):

#*****************************************************************************80
#
## P12_RANG returns an interval bounding the root for problem 12.
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
#    Output, real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 4.0, + 4.1 ] )

  return rang

def p12_root ( i ):

#*****************************************************************************80
#
## P12_ROOT returns a root for problem 12.
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
#    Input, integer I, the index of the requested root.
#
#    Output, real X, the value of the root.
#
  x = 1.0

  return x

def p12_root_num ( ):

#*****************************************************************************80
#
## P12_ROOT_NUM returns the number of known roots for problem 12.
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
#    Output, integer ROOT_NUM, the number of known roots.
#
  root_num = 1

  return root_num

def p12_start ( i ):

#*****************************************************************************80
#
## P12_START returns a starting point for problem 12.
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
  if ( ( i % 3 ) == 1 ):
    x = 2.0
  elif ( ( i % 3 ) == 2 ):
    x = 0.50
  elif ( ( i % 3 ) == 0 ):
    x = 4.0

  return x

def p12_start_num ( ):

#*****************************************************************************80
#
## P12_START_NUM returns the number of starting points for problem 12.
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
#    Output, integer START_NUM, the number of starting points.
#
  start_num = 3

  return start_num

def p12_title ( title ):

#*****************************************************************************80
#
## P12_TITLE returns the title of problem 12.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'Flat Stanley (ALL derivatives are zero at the root.)'

  return title

