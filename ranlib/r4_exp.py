#! /usr/bin/env python
#
def r4_exp ( x ):

#*****************************************************************************80
#
## R4_EXP computes the exponential function, avoiding overflow and underflow.
#
#  Discussion:
#
#    For arguments of very large magnitude, the evaluation of the
#    exponential function can cause computational problems.  Some languages
#    and compilers may return an infinite value or a "Not-a-Number".  
#    An alternative, when dealing with a wide range of inputs, is simply
#    to truncate the calculation for arguments whose magnitude is too large.
#    Whether this is the right or convenient approach depends on the problem
#    you are dealing with, and whether or not you really need accurate
#    results for large magnitude inputs, or you just want your code to
#    stop crashing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the exponential function.
#
#    Output, real VALUE, the value of exp ( X ).
#
  import numpy as np

  r4_huge = 1.0E+30
  r4_log_max = +69.0776
  r4_log_min = -69.0776

  if ( x <= r4_log_min ):
    value = 0.0
  elif ( x < r4_log_max ):
    value = np.exp ( x )
  else:
    value = r4_huge

  return value

def r4_exp_test ( ):

#*****************************************************************************80
#
## R4_EXP_TEST tests R4_EXP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R4_EXP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_EXP returns the exponential of a real number.' )
  print ( '' )
  print ( '        X           R4_EXP(X)' )
  print ( '' )

  for i in range ( -80, +90, 10 ):
    x = float ( i )
    print ( '  %12g  %12g' % ( x, r4_exp ( x ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_EXP_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4_exp_test ( )
  timestamp ( )

