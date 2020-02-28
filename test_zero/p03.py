#! /usr/bin/env python
#
def p03_fx ( x ):

#*****************************************************************************80
#
## P03_FX evaluates x * exp ( - x ).
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

  fx = x * np.exp ( - x )

  return fx

def p03_fx1 ( x ):

#*****************************************************************************80
#
## P03_FX1 evaluates the derivative of the function for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
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

  fx1 = np.exp ( - x ) * ( 1.0 - x )

  return fx1

def p03_fx2 ( x ):

#*****************************************************************************80
#
## P03_FX2 evaluates the second derivative of the function for problem 3.
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

  fx2 = np.exp ( - x ) * ( x - 2.0 )

  return fx2

def p03_rang ( ):

#*****************************************************************************80
#
## P03_RANG returns an interval bounding the root for problem 3.
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

  rang = np.array ( [ -10.0, 100.0 ] )

  return rang

def p03_root ( i ):

#*****************************************************************************80
#
## P03_ROOT returns a root for problem 3.
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

def p03_root_num ( ):

#*****************************************************************************80
#
## P03_ROOT_NUM returns the number of known roots for problem 3.
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

def p03_start ( i ):

#*****************************************************************************80
#
## P03_START returns a starting point for problem 3.
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
    x = -1.0
  elif ( ( i % 3 ) == 2 ):
    x =  0.5
  elif ( ( i % 3 ) == 0 ):
    x =  2.0

  return x

def p03_start_num ( ):

#*****************************************************************************80
#
## P03_START_NUM returns the number of starting points for problem 3.
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

def p03_title ( title ):

#*****************************************************************************80
#
## P03_TITLE returns the title of problem 3.
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
  title = 'F(X) = X * EXP ( - X )'

  return title

