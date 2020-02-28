#! /usr/bin/env python
#
def p06_fx ( x ):

#*****************************************************************************80
#
## P06_FX evaluates exp ( x ) - 2 - 1 / ( 10 * x )^2 + 2 / ( 100 * x )^3.
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

  fx = np.exp ( x ) - 2.0 - 1.0 / ( 10.0 * x ) ** 2 + 2.0 / ( 100.0 * x ) ** 3

  return fx

def p06_fx1 ( x ):

#*****************************************************************************80
#
## P06_FX1 evaluates the derivative of the function for problem 6.
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

  fx1 = np.exp ( x ) + 2.0 / ( 100.0 * x ** 3 ) - 6.0 / ( 1000000.0 * x ** 4 )

  return fx1

def p06_fx2 ( x ):

#*****************************************************************************80
#
## P06_FX2 evaluates the second derivative of the function for problem 6.
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

  fx2 = np.exp ( x ) - 6.0 / ( 100.0 * x ** 4 ) + 24.0 / ( 1000000.0 * x ** 5 )

  return fx2

def p06_rang ( ):

#*****************************************************************************80
#
## P06_RANG returns an interval bounding the root for problem 6.
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

  rang = np.array ( [ 0.00001, 20.0 ] )

  return rang

def p06_root ( i ):

#*****************************************************************************80
#
## P06_ROOT returns a root for problem 6.
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
  x = 0.7032048403631358

  return x

def p06_root_num ( ):

#*****************************************************************************80
#
## P06_ROOT_NUM returns the number of known roots for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:7
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer ROOT_NUM, the number of known roots.
#
  root_num = 1

  return root_num

def p06_start ( i ):

#*****************************************************************************80
#
## P06_START returns a starting point for problem 6.
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
    x = 0.0002
  elif ( ( i % 2 ) == 0 ):
    x = 2.0

  return x

def p06_start_num ( ):

#*****************************************************************************80
#
## P06_START_NUM returns the number of starting points for problem 6.
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

def p06_title ( title ):

#*****************************************************************************80
#
## P06_TITLE returns the title of problem 6.
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
  title = 'F(X) = EXP(X) - 2 - 1 / ( 10 * X )^2 - 2 / ( 100 * X )^3'

  return title

