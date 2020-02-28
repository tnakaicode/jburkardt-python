#! /usr/bin/env python
#
def p18_fx ( x ):

#*****************************************************************************80
#
## P18_FX evaluates the function for problem 18.
#
#  Discussion:
#
#    F(X) = 10^14 * (x-1)^7, but is written in term by term form.
#
#    This polynomial becomes difficult to evaluate accurately when 
#    written this way.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625.
#
#  Parameters:
#
#    Input, real X(*), the point at which F is to be evaluated.
#
#    Output, real FX(*), the value of the function at X.
#
  horners = False

  if ( horners ):

    fx = 10.0 ** 14 * ( ( ( ( ( ( ( ( \
                  1.0 ) 
           * x -  7.0 ) 
           * x + 21.0 )
           * x - 35.0 )
           * x + 35.0 )
           * x - 21.0 )
           * x +  7.0 )
           * x -  1.0 )

  else:

    fx = 10.0 ** 14 * (
             1.0 * x ** 7 
          -  7.0 * x ** 6 
          + 21.0 * x ** 5
          - 35.0 * x ** 4
          + 35.0 * x ** 3
          - 21.0 * x ** 2
          +  7.0 * x
          -  1.0 )

  return fx

def p18_fx1 ( x ):

#*****************************************************************************80
#
## P18_FX1 evaluates the derivative of the function for problem 18.
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
#    Output, real FX1(*), the value of the derivative at X.
#
  fx1 = 10.0 ** 14 * ( \
          7 * x ** 6 \
      -  42 * x ** 5 \
      + 105 * x ** 4 \
      - 140 * x ** 3 \
      + 105 * x ** 2 \
      -  42 * x ** 1 \
      +   7 )

  return fx1

def p18_fx2 ( x ):

#*****************************************************************************80
#
## P18_FX2 evaluates the second derivative of the function for problem 18.
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
#    Output, real FX2(*), the value of the second derivative at X.
#
  fx2 = 10.0 ** 14 * ( \
         42 * x ** 5 \
      - 210 * x ** 4 \
      + 420 * x ** 3 \
      - 420 * x ** 2 \
      + 210 * x    \
      -  42 )

  return fx2

def p18_rang ( ):

#*****************************************************************************80
#
## P18_RANG returns an interval bounding the root for problem 18.
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

  rang = np.array ( [ 0.988, 1.012 ] )

  return rang

def p18_root ( i ):

#*****************************************************************************80
#
## P18_ROOT returns a root for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
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
  x = 1.0

  return x

def p18_root_num ( ):

#*****************************************************************************80
#
## P18_ROOT_NUM returns the number of known roots for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
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

def p18_start ( i ):

#*****************************************************************************80
#
## P18_START returns a starting point for problem 18.
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
  if ( i == 1 ):
    x = 0.990
  elif ( i == 2 ):
    x = 1.013

  return x

def p18_start_num ( ):

#*****************************************************************************80
#
## P18_START_NUM returns the number of starting points for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
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

def p18_title ( title ):

#*****************************************************************************80
#
## P18_TITLE returns the title of problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = '10^14 * (x-1)^7, written term by term.'

  return title

