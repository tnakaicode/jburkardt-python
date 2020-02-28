#! /usr/bin/env python
#
def p17_fx ( x ):

#*****************************************************************************80
#
## P17_FX evaluates the function for problem 17.
#
#  Discussion:
#
#    This simple example is of historical interest, since it was used
#    by Wallis to illustrate the use of Newton's method, and has been
#    a common example ever since.
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
  fx = x ** 3 - 2.0 * x - 5.0

  return fx

def p17_fx1 ( x ):

#*****************************************************************************80
#
## P17_FX1 evaluates the derivative of the function for problem 17.
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
  fx1 = 3.0 * x * x - 2.0

  return fx1

def p17_fx2 ( x ):

#*****************************************************************************80
#
## P17_FX2 evaluates the second derivative of the function for problem 17.
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
#    Output, real FX2, the second derivative at X.
#
  fx2 = 6.0 * x

  return fx2

def p17_rang ( ):

#*****************************************************************************80
#
## P17_RANG returns an interval bounding the root for problem 17.
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

  rang = np.array ( [ 2.0, 3.0 ] )

  return rang

def p17_root ( i ):

#*****************************************************************************80
#
## P17_ROOT returns a root for problem 17.
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
  x = 2.0945514815423265

  return x

def p17_root_num ( ):

#*****************************************************************************80
#
## P17_ROOT_NUM returns the number of known roots for problem 17.
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

def p17_start ( i ):

#*****************************************************************************80
#
## P17_START returns a starting point for problem 17.
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
    x = 2.0
  elif ( ( i % 2 ) == 0 ):
    x = 3.0

  return x

def p17_start_num ( ):

#*****************************************************************************80
#
## P17_START_NUM returns the number of starting points for problem 17.
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

def p17_title ( title ):

#*****************************************************************************80
#
## P17_TITLE returns the title of problem 17.
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
  title = 'The Wallis example, x^3-2x-5=0'

  return title

