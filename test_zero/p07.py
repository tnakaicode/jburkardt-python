#! /usr/bin/env python
#
def p07_fx ( x ):

#*****************************************************************************80
#
## P07_FX evaluates the function for problem 07.
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
  fx = x ** 3

  return fx

def p07_fx1 ( x ):

#*****************************************************************************80
#
## P07_FX1 evaluates the derivative of the function for problem 7.
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
  fx1 = 3.0 * x ** 2

  return fx1

def p07_fx2 ( x ):

#*****************************************************************************80
#
## P07_FX2 evaluates the second derivative of the function for problem 7.
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
  fx2 = 6.0 * x

  return fx2

def p07_rang ( ):

#*****************************************************************************80
#
## P07_RANG returns an interval bounding the root for problem 7.
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

  rang = np.array ( [ -1000.0, 999.0 ] )

  return rang

def p07_root ( i ):

#*****************************************************************************80
#
## P07_ROOT returns a root for problem 7.
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

def p07_root_num ( ):

#*****************************************************************************80
#
## P07_ROOT_NUM returns the number of known roots for problem 7.
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

def p07_start ( i ):

#*****************************************************************************80
#
## P07_START returns a starting point for problem 7.
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
    x = 1.0
  elif ( ( i % 2 ) == 0 ):
    x = -1000.0

  return x

def p07_start_num ( ):

#*****************************************************************************80
#
## P07_START_NUM returns the number of starting points for problem 7.
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

def p07_title ( title ):

#*****************************************************************************80
#
## P07_TITLE returns the title of problem 7.
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
  title = 'F(X) = X^3, only linear Newton convergence.'

  return title

