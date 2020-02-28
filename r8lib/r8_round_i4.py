#! /usr/bin/env python3
#
def r8_round_i4 ( x ):

#*****************************************************************************80
#
## R8_ROUND_I4 rounds an R8 to the nearest integral value, returning an I4.
#
#  Discussion:
#
#    In MATLAB, it is essentially true that there is little difference between
#    this function and R8_ROUND, because we store our integers in what amounts
#    to a real variable.
#
#  Example:
#
#        X        R8_ROUND_I4
#
#      1.3         1
#      1.4         1
#      1.5         1 or 2
#      1.6         2
#      0.0         0
#     -0.7        -1
#     -1.1        -1
#     -1.6        -2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the value.
#
#    Output, integer R8_ROUND_I4, the rounded value.
#
  if ( x < 0.0 ):
    value = - int ( - x + 0.5 )
  else:
    value =   int ( + x + 0.5 )

  return value
