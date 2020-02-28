#! /usr/bin/env python
#
def p10_fx ( x ):

#*****************************************************************************80
#
## P10_FX evaluates the Repeller.
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
  fx = 20.0 * x / ( 100.0 * x * x + 1.0 )

  return fx

def p10_fx1 ( x ):

#*****************************************************************************80
#
## P10_FX1 evaluates the derivative of the function for problem 10.
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
  fx1 = ( 1.0 - 10.0 * x ) * ( 1.0 + 10.0 * x ) / ( 100.0 * x * x + 1.0 ) ** 2

  return fx1

def p10_fx2 ( x ):

#*****************************************************************************80
#
## P10_FX2 evaluates the second derivative of the function for problem 10.
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
  fx2 = - 200.0 * x * ( 3.0 - 100.0 * x ** 2 ) / ( 100.0 * x * x + 1.0 ) ** 3

  return fx2

def p10_rang ( ):

#*****************************************************************************80
#
## P10_RANG returns an interval bounding the root for problem 10.
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

  rang = np.array ( [ - 10.0, + 11.0 ] )

  return rang

def p10_root ( i ):

#*****************************************************************************80
#
## P10_ROOT returns a root for problem 10.
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
  x = 0.0

  return x

def p10_root_num ( ):

#*****************************************************************************80
#
## P10_ROOT_NUM returns the number of known roots for problem 10.
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

def p10_start ( i ):

#*****************************************************************************80
#
## P10_START returns a starting point for problem 10.
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
    x = 1.0
  elif ( ( i % 3 ) == 2 ):
    x = - 0.14
  elif ( ( i % 3 ) == 0 ):
    x = 0.041

  return x

def p10_start_num ( ):

#*****************************************************************************80
#
## P10_START_NUM returns the number of starting points for problem 10.
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

def p10_title ( title ):

#*****************************************************************************80
#
## P10_TITLE returns the title of problem 10.
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
  title = 'The Repeller'

  return title

