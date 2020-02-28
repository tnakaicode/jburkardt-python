#! /usr/bin/env python
#
def r8vec_step ( x0, n, x ):

#*****************************************************************************80
#
## R8VEC_STEP evaluates a unit step function.
#
#  Discussion:
#
#    F(X) = 0 if X < X0
#           1 if     X0 <= X
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X0, the location of the jump.
#
#    Input, integer N, the number of argument values.
#
#    Output, real X(N), the arguments.
#
#    Output, real FX(N), the function values.
#
  import numpy

  fx = numpy.zeros ( n );

  for i in range ( 0, n ):
    if ( x[i] < x0 ):
      fx[i] = 0.0
    else:
      fx[i] = 1.0

  return fx

def r8vec_step_test ( ):

#*****************************************************************************80
#
## R8VEC_TEST tests R8VEC_STEP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'R8VEC_STEP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_STEP evaluates a step function.' )
  print ( '' )
  print ( '        X0         X           STEP(X0,X)' )
  print ( '' )

  x0 = 0.31
  n = 21

  x = np.linspace ( 0.0, 1.0, n )
  v = r8vec_step ( x0, n, x )

  r8vec2_print ( n, x, v, '  Step function with X0 = 0.31' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_STEP_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_step_test ( )
  timestamp ( )

