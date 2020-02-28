#! /usr/bin/env python
#
def p19_fx ( x ):

#*****************************************************************************80
#
## P19_FX evaluates the function for problem 19.
#
#  Discussion:
#
#    This function looks like an elevated cosine curve, connected by a 
#    sudden drop to a submerged cosine curve.
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
  from scipy.special import erf

  fx = np.cos ( 100.0 * x ) - 4.0 * erf ( 30.0 * x - 10.0 )

  return fx

def p19_fx1 ( x ):

#*****************************************************************************80
#
## P19_FX1 evaluates the derivative of the function for problem 19.
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
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX1(*), the value of the derivative at X.
#
  import numpy as np

  arg = - ( 10.0 - 30.0 * x ) ** 2

  fx1 = - 100.0 * np.sin ( 100.0 * x ) + 240.0 * np.exp ( arg ) \
    / np.sqrt ( np.pi )

  return fx1

def p19_fx2 ( x ):

#*****************************************************************************80
#
## P19_FX2 evaluates the second derivative of the function for problem 19.
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
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX2(*), the value of the second derivative at X.
#
  import numpy as np

  arg = - ( 10.0 - 30.0 * x ) ** 2

  fx2 = - 10000.0 * np.cos ( 100.0 * x ) \
    + 14400.0 * np.exp ( arg ) * ( 10.0 - 30.0 * x ) / np.sqrt ( np.pi )

  return fx2

def p19_rang ( ):

#*****************************************************************************80
#
## P19_RANG returns an interval bounding the root for problem 19.
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
#    Output, real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 0.0, 1.0 ] )

  return rang

def p19_root ( i ):

#*****************************************************************************80
#
## P19_ROOT returns a root for problem 19.
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
#    Input, integer I, the index of the requested root.
#
#    Output, real X, the value of the root.
#
  x = 0.33186603357456253747

  return x

def p19_root_num ( ):

#*****************************************************************************80
#
## P19_ROOT_NUM returns the number of known roots for problem 19.
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
#    Output, integer ROOT_NUM, the number of known roots.
#
  root_num = 1

  return root_num

def p19_start ( i ):

#*****************************************************************************80
#
## P19_START returns a starting point for problem 19.
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
#    Input, integer I, the index of the starting point.
#
#    Output, real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 0.0
  elif ( ( i % 3 ) == 2 ):
    x = 1.0
  elif ( ( i % 3 ) == 0 ):
    x = 0.5

  return x

def p19_start_num ( ):

#*****************************************************************************80
#
## P19_START_NUM returns the number of starting points for problem 19.
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
#    Output, integer START_NUM, the number of starting points.
#
  start_num = 3

  return start_num

def p19_title ( title ):

#*****************************************************************************80
#
## P19_TITLE returns the title of problem 19.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'The jumping cosine'

  return title

