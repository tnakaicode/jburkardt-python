#! /usr/bin/env python
#
def rat_width ( a, b ):

#*****************************************************************************80
#
## RAT_WIDTH returns the "width" of a rational number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the rational number.
#
#    Output, integer WIDTH, the "width" of the rational number.
#
  width = 1
  ten_pow = 10

  if ( a == 0 ):
    return width
  
  abs_a = abs ( a )

  while ( ten_pow <= abs_a ):
    width = width + 1
    ten_pow = ten_pow * 10
#
#  If the fraction is negative, a minus sign will be prepended to the
#  numerator.
#
  if ( a * b < 0 ):
    width = width + 1
    ten_pow = ten_pow * 10

  abs_b = abs ( b )

  while ( ten_pow <= abs_b ):
    width = width + 1
    ten_pow = ten_pow * 10

  return width

def rat_width_test ( ):

#*****************************************************************************80
#
## RAT_WIDTH_TEST tests RAT_WIDTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_test = 17

  a_test = np.array ( \
    [ 1000, 1000, 1000, 1000,  1000,    1,      -1, -10, -100, -1000, \
         1,   10,  100, 1000, 10000,   17, 4000000 ] )
  b_test = np.array ( \
    [    3,   40,  500, 6000, 70000,    1,     200, 200,  200,   200, \
      -200, -200, -200, -200,  -200, 3000, 4000000 ] )

  print ( '' )
  print ( 'RAT_WIDTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_WIDTH determines the "width" of a rational.' )
  print ( '' )
  print ( '       Top    Bottom   Width' )
  print ( '' )

  for i in range ( 0, n_test ):
    a = a_test[i]
    b = b_test[i]
    width = rat_width ( a, b )
    print ( '  %8d  %8d  %6d' % ( a, b, width ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAT_WIDTH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_width_test ( )
  timestamp ( )

