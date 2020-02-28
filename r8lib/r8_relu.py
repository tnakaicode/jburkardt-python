#! /usr/bin/env python3
#
def r8_relu ( x ):

#*****************************************************************************80
#
## R8_RELLU evaluates the ReLU function of an R8.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#    The ReLU function is max(x,0.0).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the function value.
#
  import numpy as np

  if ( x <= 0.0 ):
    value = 0.0
  else:
    value = x

  return value

def r8_relu_test ( ):

#*****************************************************************************80
#
## R8_RELU_TEST tests R8_RELU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_RELU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_RELU evaluates the ReLU function of an R8.' )
  print ( '  This is max(x,0).' )
  print ( '' )
  print ( '      X             R8_RELU(X)' )
  print ( '' )

  x_test = np.array ( [ \
    -500.0,   -50.0,    -5.0,    -4.0,     -3.0, \
      -2.0,    -1.0,    -0.5,    -0.05,    -0.005, \
      -0.0005,  0.0,     0.0005,  0.005,    0.05, \
       0.5,     1.0,     2.0,     3.0,      4.0, \
       5.0,    50.0,   500.0,  5000.0,  50000.0 ] )

  for i in range ( 0, 25 ):
    x = x_test[i]
    value = r8_relu ( x )
    print ( '  %10.6g  %10.6g' % ( x, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_RELU_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_relu_test ( )
  timestamp ( )
 
