#! /usr/bin/env python
#
def p01_fx ( x ):

#*****************************************************************************80
#
## P01_FX evaluates sin ( x ) - x / 2.
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

  fx = np.sin ( x ) - 0.5 * x

  return fx

def p01_fx1 ( x ):

#*****************************************************************************80
#
## P01_FX1 evaluates the derivative of the function for problem 1.
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

  fx1 = np.cos ( x ) - 0.5

  return fx1

def p01_fx2 ( x ):

#*****************************************************************************80
#
## P01_FX2 evaluates the second derivative of the function for problem 1.
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

  fx2 = - np.sin ( x )

  return fx2

def p01_rang ( ):

#*****************************************************************************80
#
## P01_RANG returns an interval bounding the root for problem 1.
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

  rang = np.array ( [ -1000.0, 1001.0 ] )

  return rang

def p01_root ( i ):

#*****************************************************************************80
#
## P01_ROOT returns a root for problem 1.
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
  if ( ( i % 3 ) == 1 ):
    x = - 1.895494267033981
  elif ( ( i % 3 ) == 2 ):
    x = 0.0
  elif ( ( i % 3 ) == 0 ):
    x = 1.895494267033981

  return x

def p01_root_num ( ):

#*****************************************************************************80
#
## P01_ROOT_NUM returns the number of known roots for problem 1.
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
  root_num = 3

  return root_num

def p01_start ( i ):

#*****************************************************************************80
#
## P01_START returns a starting point for problem 1.
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
  import numpy as np

  if ( ( i % 2 ) == 1 ):
    x = 0.5 * np.pi
  elif ( ( i % 2 ) == 0 ):
    x = np.pi

  return x

def p01_start_num ( ):

#*****************************************************************************80
#
## P01_START_NUM returns the number of starting points for problem 1.
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
  start_num = 2

  return start_num

def p01_title ( title ):

#*****************************************************************************80
#
## P01_TITLE returns the title of problem 1.
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
  title = 'F(X) = SIN(X) - 0.5 * X'

  return title

