#! /usr/bin/env python
#
def p14_fx ( x ):

#*****************************************************************************80
#
## P14_FX evaluates the Camel.
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
#    Output, real FX(*), the value of the function at X.
#
  fx =   1.0 / ( ( x - 0.3 ) ** 2 + 0.01 ) \
       + 1.0 / ( ( x - 0.9 ) ** 2 + 0.04 ) \
       + 2.0 * x - 5.2

  return fx

def p14_fx1 ( x ):

#*****************************************************************************80
#
## P14_FX1 evaluates the derivative of the function for problem 14.
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
  fx1 = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 ) ** 2 + 0.01 ) ** 2 \
        - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 ) ** 2 + 0.04 ) ** 2 \
        + 2.0

  return fx1

def p14_fx2 ( x ):

#*****************************************************************************80
#
## P14_FX2 evaluates the second derivative of the function for problem 14.
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
#    Output, real FX2, the second derivative of the function at X.
#
  t1 = - 2.0
  b1 = ( 0.04 + ( x - 0.9 ) ** 2 ) ** 2

  t2 = 8.0 * ( x - 0.9 ) ** 2
  b2 = ( 0.04 + ( x - 0.9 ) ** 2 ) ** 3

  t3 = 80.0 * ( 3.0 - 10.0 * x ) ** 2
  b3 = ( 1.0 - 6.0 * x + 10.0 * x ** 2 ) ** 3

  t4 = - 200.0
  b4 = ( 1.0 - 6.0 * x + 10.0 * x ** 2 ) ** 2

  fx2 = t1 / b1 + t2 / b2 + t3 / b3 + t4 / b4

  return fx2

def p14_rang ( ):

#*****************************************************************************80
#
## P14_RANG returns an interval bounding the root for problem 14.
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

  rang = np.array ( [ - 10.0, 10.0 ] )

  return rang

def p14_root ( i ):

#*****************************************************************************80
#
## P14_ROOT returns a root for problem 14.
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
  if ( ( i % 3 ) == 1 ):
    x = - 0.1534804948126991
  elif ( ( i % 3 ) == 2 ):
    x = 1.8190323925159182
  elif ( ( i % 3 ) == 0 ):
    x = 2.1274329318603367

  return x

def p14_root_num ( ):

#*****************************************************************************80
#
## P14_ROOT_NUM returns the number of known roots for problem 14.
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
  root_num = 3

  return root_num

def p14_start ( i ):

#*****************************************************************************80
#
## P14_START returns a starting point for problem 14.
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
  if ( ( i % 4 ) == 1 ):
    x = 3.0
  elif ( ( i % 4 ) == 2 ):
    x = - 0.5
  elif ( ( i % 4 ) == 3 ):
    x = 0.0
  elif ( ( i % 3 ) == 0 ):
    x = 2.12742

  return x

def p14_start_num ( ):

#*****************************************************************************80
#
## P14_START_NUM returns the number of starting points for problem 14.
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
  start_num = 4

  return start_num

def p14_title ( title ):

#*****************************************************************************80
#
## P14_TITLE returns the title of problem 14.
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
  title = 'The Camel (double hump and some shallow roots.)'

  return title

