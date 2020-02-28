#! /usr/bin/env python
#
epsilon = 0.00001

def p11_fx ( x ):

#*****************************************************************************80
#
## P11_FX evaluates the Pinhead.
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
  global epsilon

  fx = ( 16.0 - x ** 4 ) / ( 16.0 * x ** 4 + epsilon )

  return fx

def p11_fx1 ( x ):

#*****************************************************************************80
#
## P11_FX1 evaluates the derivative of the function for problem 11.
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
  global epsilon

  fx1 = - 4.0 * x ** 3 * ( epsilon + 256.0 ) / ( 16.0 * x ** 4 + epsilon ) ** 2

  return fx1

def p11_fx2 ( x ):

#*****************************************************************************80
#
## P11_FX2 evaluates the second derivative of the function for problem 11.
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
  global epsilon

  fx2 = - 4.0 * ( epsilon + 256.0 ) \
    * ( 3.0 * epsilon - 80.0 * x ** 4 ) * x ** 2 \
    / ( 16.0 * x ** 4 + epsilon ) ** 3

  return fx2

def p11_rang ( ):

#*****************************************************************************80
#
## P11_RANG returns an interval bounding the root for problem 11.
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

  rang = np.array ( [ 0.0, + 10.0 ] )
 
  return rang

def p11_root ( i ):

#*****************************************************************************80
#
## P11_ROOT returns a root for problem 11.
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
  if (  ( i % 2 ) == 1 ):
    x = - 2.0
  elif ( ( i % 2 ) == 0 ):
    x = 2.0

  return x

def p11_root_num ( ):

#*****************************************************************************80
#
## P11_ROOT_NUM returns the number of known roots for problem 11.
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
  root_num = 2

  return root_num

def p11_start ( i ):

#*****************************************************************************80
#
## P11_START returns a starting point for problem 11.
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
    x = 0.25
  elif ( ( i % 3 ) == 2 ):
    x = 5.0
  elif ( ( i % 3 ) == 0 ):
    x = 1.1

  return x

def p11_start_num ( ):

#*****************************************************************************80
#
## P11_START_NUM returns the number of starting points for problem 11.
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

def p11_title ( title ):

#*****************************************************************************80
#
## P11_TITLE returns the title of problem 11.
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
  title = 'The Pinhead'

  return title

