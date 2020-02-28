#! /usr/bin/env python
#
def p04_fx ( x ):

#*****************************************************************************80
#
## P04_FX evaluates exp ( x ) - 1 / ( 10 * x )^2.
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

  fx = np.exp ( x ) - 1.0 / ( 100.0 * x * x )

  return fx

def p04_fx1 ( x ):

#*****************************************************************************80
#
## P04_FX1 evaluates the derivative of the function for problem 4.
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
  import numpy as np

  fx1 = np.exp ( x ) + 2.0 / ( 100.0 * x * x * x )

  return fx1

def p04_fx2 ( x ):

#*****************************************************************************80
#
## P04_FX2 evaluates the second derivative of the function for problem 4.
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
  import numpy as np

  fx2 = np.exp ( x ) - 6.0 / ( 100.0 * x * x * x * x )

  return fx2

def p04_rang ( ):

#*****************************************************************************80
#
## P04_RANG returns an interval bounding the root for problem 4.
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

  rang = np.array ( [ 0.00001, 20.0 ] )

  return rang

def p04_root ( i ):

#*****************************************************************************80
#
## P04_ROOT returns a root for problem 4.
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
  x = 0.09534461720025875

  return x

def p04_root_num ( ):

#*****************************************************************************80
#
## P04_ROOT_NUM returns the number of known roots for problem 4.
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

def p04_start ( i ):

#*****************************************************************************80
#
## P04_START returns a starting point for problem 4.
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
    x = 0.03
  elif ( ( i % 2 ) == 0 ):
    x = 1.0

  return x

def p04_start_num ( ):

#*****************************************************************************80
#
## P04_START_NUM returns the number of starting points for problem 4.
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

def p04_title ( title ):

#*****************************************************************************80
#
## P04_TITLE returns the title of problem 4.
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
  title = 'F(X) = EXP ( X ) - 1 / ( 10 * X )^2'

  return title

