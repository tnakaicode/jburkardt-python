#! /usr/bin/env python
#
def r8_ren ( seed ):

#*****************************************************************************80
#
## R8_REN is a simple random number generator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Malcolm Pike, David Hill,
#    Algorithm 266:
#    Pseudo-Random Numbers,
#    Communications of the ACM,
#    Volume 8, Number 10, October 1965, page 605.
#
#  Parameters:
#
#    Output, real VALUE, the random value.
#
#    Input/output, integer SEED, a seed for the random number generator.
#
  i4_huge = 2147483647
  seed = ( seed % ( i4_huge // 125 ) )
  seed = seed * 125
  seed = seed - ( seed // 2796203 ) * 2796203
  value = seed / 2796203.0

  return value, seed

def r8_ren_test ( ):

#*****************************************************************************80
#
#% R8_REN_TEST tests R8_REN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i_value = np.array ( [ 1, 2, 3, 4, 10, 100, 1000 ] )

  r_value = np.array ( [ \
    0.470393E+00, \
    0.799066E+00, \
    0.883261E+00, \
    0.407667E+00, \
    0.955566E+00, \
    0.173576E+00, \
    0.121733E-01 ] )

  print ( '' )
  print ( 'R8_REN_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_REN is a random number generator.' )
  print ( '' )
  print ( '             I         R8_REN         Expected' )
  print ( '' )

  seed = 100001
  k = 0
  for i in range ( 1, 1001 ):

    r, seed = r8_ren ( seed )

    if ( i == i_value[k] ):
      print ( '  %14d  %14.6g  %14.6g' % ( i, r, r_value[k] ) )
      k = k + 1

  seed = 100001
  average = 0.0
  for i in range ( 1, 1000000 ):
    r, seed = r8_ren ( seed )
    average = average + r
  average = average / 1000000.0
  print ( '' )
  print ( '       Average =  %14.6g  %14.6g' % ( average, 0.5 ) )

  seed = 100001
  variance = 0.0
  for i in range ( 1, 1000000 ):
    r, seed = r8_ren ( seed )
    variance = variance + ( r - average ) ** 2
  variance = variance / 1000000.0
  print ( '       Variance = %14.6g  %14.6g' % ( variance, 1.0 / 12.0 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_REN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_ren_test ( )
  timestamp ( )

