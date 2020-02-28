#! /usr/bin/env python3
#
def r8_sigmoid ( l, b, m, x ):

#*****************************************************************************80
#
## r8_sigmoid evaluates the sigmoid or logistic function.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#    The sigmoid function is useful for classification problems in
#    machine learning.  Its value is always between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real l, the maximum value of the function.  This is often 1.
#
#    real b, the cutoff value, where the function equals l/2.
#    This is often 0.
#
#    real m, the slope, which determines the steepness of the curve
#    and the width of the uncertainty interval.  This is often 1.
#
#    real x, the argument.
#
#  Output:
#
#    real value, the value.
#
  import numpy as np

  value = l / ( 1.0 + np.exp ( - m * ( x - b ) ) )

  return value

def r8_sigmoid_test ( ):

#*****************************************************************************80
#
## r8_sigmoid_test tests r8_sigmoid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_sigmoid_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sigmoid evaluates the sigmoid function of R8.' )
  print ( '' )
  print ( '      X         R8_SIGMOID(L,B,M,X)' )
  print ( '' )

  x_test = np.array ( [ -4.0, -2.0, -1.0, -0.5, -0.25, 0.0, 0.25, 0.50, 1.0, 2.0, 4.0 ] )

  l = 1.0
  b = 0.0
  m = 1.0

  for i in range ( 0, 11 ):
    x = x_test[i]
    value = r8_sigmoid ( l, b, m, x )
    print ( '  %10.6g  %10.6g' % ( x, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_sigmoid_test' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sigmoid_test ( )
  timestamp ( )

