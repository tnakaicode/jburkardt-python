#! /usr/bin/env python
#
def p09_fx ( x ):

#*****************************************************************************80
#
## P09_FX evaluates the Newton Baffler.
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
  fx = 0.0

  if ( x < 6.0 ):
    fx = 0.75 * ( x - 6.25 ) - 0.3125
  elif ( x <= 6.50 ):
    fx = 2.00 * ( x - 6.25 )
  else:
    fx = 0.75 * ( x - 6.25 ) + 0.3125

  return fx

def p09_fx1 ( x ):

#*****************************************************************************80
#
## P09_FX1 evaluates the derivative of the function for problem 9.
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
  x2 = x - 6.25

  if ( x2 < - 0.25 ):
    fx1 = 0.75
  elif ( x2 < 0.25 ):
    fx1 = 2.0
  else:
    fx1 = 0.75

  return fx1

def p09_fx2 ( x ):

#*****************************************************************************80
#
## P09_FX2 evaluates the second derivative of the function for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 September 1999
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
  fx2 = 0.0

  return fx2

def p09_rang ( ):

#*****************************************************************************80
#
## P09_RANG returns an interval bounding the root for problem 9.
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

  rang = np.array ( [ - 5.0, + 16.0 ] )

  return rang

def p09_root ( i ):

#*****************************************************************************80
#
## P09_ROOT returns a root for problem 9.
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
  x = 6.25

  return x

def p09_root_num ( ):

#*****************************************************************************80
#
## P09_ROOT_NUM returns the number of known roots for problem 9.
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

def p09_start ( i ):

#*****************************************************************************80
#
## P09_START returns a starting point for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2011
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
    x = 6.25 + 5.0
  elif ( ( i % 3 ) == 2 ):
    x = 6.25 - 1.0
  elif ( ( i % 3 ) == 0 ):
    x = 6.25 + 0.1

  return x

def p09_start_num ( ):

#*****************************************************************************80
#
## P09_START_NUM returns the number of starting points for problem 9.
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
  start_num = 3

  return start_num

def p09_title ( title ):

#*****************************************************************************80
#
## P09_TITLE returns the title of problem 9.
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
  title = 'The Newton Baffler'

  return title

