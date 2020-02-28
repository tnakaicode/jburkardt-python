#! /usr/bin/env python
#
def p02_fx ( x ):

#*****************************************************************************80
#
## P02_FX evaluates 2 * x - exp ( - x ).
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
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX(*), the value of the function at X.
#
  import numpy as np

  fx = 2.0 * x - np.exp ( - x )

  return fx

def p02_fx1 ( x ):

#*****************************************************************************80
#
## P02_FX1 evaluates the derivative of the function for problem 2.
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
  import numpy as  np

  fx1 = 2.0 + np.exp ( - x )

  return fx1

def p02_fx2 ( x ):

#*****************************************************************************80
#
## P02_FX2 evaluates the second derivative of the function for problem 2.
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

  fx2 = - np.exp ( - x )

  return fx2

def p02_rang ( ):

#*****************************************************************************80
#
## P02_RANG returns an interval bounding the root for problem 2.
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

  rang = np.array ( [ -10.0, 100.0 ] )

  return rang

def p02_root ( i ):

#*****************************************************************************80
#
## P02_ROOT returns a root for problem 2.
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
  x = 0.35173371124919584

  return x

def p02_root_num ( ):

#*****************************************************************************80
#
## P02_ROOT_NUM returns the number of known roots for problem 2.
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

def p02_start ( i ):

#*****************************************************************************80
#
## P02_START returns a starting point for problem 2.
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
  if ( ( i % 4 ) == 1 ):
    x = 0.0
  elif ( ( i % 4 ) == 2 ):
    x = 1.0
  elif ( ( i % 4 ) == 3 ):
    x = -5.0
  elif ( ( i % 4 ) == 0 ):
    x = 10.0

  return x

def p02_start_num ( ):

#*****************************************************************************80
#
## P02_START_NUM returns the number of starting points for problem 2.
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
  start_num = 4

  return start_num

def p02_title ( title ):

#*****************************************************************************80
#
## P02_TITLE returns the title of problem 2.
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
  title = 'F(X) = 2 * X - EXP ( - X )'

  return title

