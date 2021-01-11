#! /usr/bin/env python
#
def r8_cos_deg ( x ):

#*****************************************************************************80
#
## R8_COS_DEG evaluates the cosine of an R8 argument in degrees.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real X, the argument in degrees.
#
#    Output, real VALUE, the cosine of X.
#
  import numpy as np
  from r8_cos import r8_cos

  raddeg = 0.017453292519943295769236907684886

  value = r8_cos ( raddeg * x )

  if ( ( x % 90.0 ) == 0.0 ):

    n = np.floor ( abs ( x ) / 90.0 + 0.5 )
    n = ( n % 2 )

    if ( n == 1 ):
      value = 0.0
    elif ( value < 0.0 ):
      value = - 1.0
    else:
      value = + 1.0

  return value

def r8_cos_deg_test ( ):

#*****************************************************************************80
#
## R8_COS_DEG_TEST tests R8_COS_DEG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from cos_degree_values import cos_degree_values

  print ( '' )
  print ( 'R8_COS_DEG_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_COS_DEG evaluates the cosine of an argument in degrees.' )
  print ( '' )
  print ( '             X     COS_DEG(X)  R8_COS_DEG(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cos_degree_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cos_deg ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_COS_DEG_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cos_deg_test ( )
  timestamp ( )
