#! /usr/bin/env python
#
def r8_log10 ( x ):

#*****************************************************************************80
#
## R8_LOG10 evaluates the logarithm, base 10, of an R8.
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
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the logarithm, base 10, of X.
#
  from r8_log import r8_log

  aloge = 0.43429448190325182765112891891661

  value = aloge * r8_log ( x )

  return value

def r8_log10_test ( ):

#*****************************************************************************80
#
## R8_LOG10_TEST tests R8_LOG10.
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
  from log10_values import log10_values

  print ( '' )
  print ( 'R8_LOG10_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LOG10 evaluates the logarithm base 10.' )
  print ( '' )
  print ( '             X        LOG10(X)  R8_LOG10(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = log10_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_log10 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LOG10_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_log10_test ( )
  timestamp ( )
