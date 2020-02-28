#! /usr/bin/env python
#
def p05_fx ( x ):

#*****************************************************************************80
#
## P05_FX evaluates ( x + 3 ) * ( x - 1 )^2.
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
  fx = ( x + 3.0 ) * ( x - 1.0 ) * ( x - 1.0 )

  return fx

def p05_fx1 ( x ):

#*****************************************************************************80
#
## P05_FX1 evaluates the derivative of the function for problem 5.
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
  fx1 = ( 3.0 * x + 5.0 ) * ( x - 1.0 )

  return fx1

def p05_fx2 ( x ):

#*****************************************************************************80
#
## P05_FX2 evaluates the second derivative of the function for problem 5.
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
  fx2 = 6.0 * x + 2.0

  return fx2

def p05_rang ( ):

#*****************************************************************************80
#
## P05_RANGE returns an interval bounding the root for problem 5.
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

  rang = np.array ( [ -1000.0, 1000.0 ] )

  return rang

def p05_root ( i ):

#*****************************************************************************80
#
## P05_ROOT returns a root for problem 5.
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
  if ( ( i % 3 ) == 1 ):
    x = - 3.0
  elif ( ( i % 3 ) == 2 ):
    x = 1.0
  elif ( ( i % 3 ) == 0 ):
    x = 1.0

  return x

def p05_root_num ( ):

#*****************************************************************************80
#
## P05_ROOT_NUM returns the number of known roots for problem 5.
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
  root_num = 3

  return root_num

def p05_start ( i ):

#*****************************************************************************80
#
## P05_START returns a starting point for problem 5.
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
  if ( ( i % 2 ) == 1 ):
    x =  2.0
  elif ( ( i % 2 ) == 0 ):
    x = - 5.0

  return x

def p05_start_num ( ):

#*****************************************************************************80
#
## P05_START_NUM returns the number of starting points for problem 5.
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

def p05_title ( title ):

#*****************************************************************************80
#
## P05_TITLE returns the title of problem 5.
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
  title = 'F(X) = ( X + 3 ) * ( X - 1 )^2'

  return title

