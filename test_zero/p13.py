#! /usr/bin/env python
#
slope = 0.00000000001

def p13_fx ( x ):

#*****************************************************************************80
#
## P13_FX evaluates Lazy Boy.
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
  global slope

  fx = slope * ( x - 100.0 )

  return fx

def p13_fx1 ( x ):

#*****************************************************************************80
#
## P13_FX1 evaluates the derivative of the function for problem 13.
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
  global slope

  fx1 = slope

  return fx1

def p13_fx2 ( x ):

#*****************************************************************************80
#
## P13_FX2 evaluates the second derivative of the function for problem 13.
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
  fx2 = 0.0

  return fx2

def p13_rang ( ):

#*****************************************************************************80
#
## P13_RANG returns an interval bounding the root for problem 13.
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

  rang = np.array ( [ - 10000000000000.0, 10000000000000.0 ] )

  return rang

def p13_root ( i ):

#*****************************************************************************80
#
## P13_ROOT returns a root for problem 13.
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
  x = 100.0

  return x

def p13_root_num ( ):

#*****************************************************************************80
#
## P13_ROOT_NUM returns the number of known roots for problem 13.
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

def p13_start ( i ):

#*****************************************************************************80
#
## P13_START returns a starting point for problem 13.
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
    x = 100000000.0
  elif ( ( i % 3 ) == 2 ):
    x = - 100000000000.0
  elif ( ( i % 3 ) == 0 ):
    x = 100000013.0

  return x

def p13_start_num ( ):

#*****************************************************************************80
#
## P13_START_NUM returns the number of starting points for problem 13.
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

def p13_title ( title ):

#*****************************************************************************80
#
## P13_TITLE returns the title of problem 13.
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
  title = 'Lazy Boy (Linear function, almost flat.)'

  return title

