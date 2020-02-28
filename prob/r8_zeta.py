#! /usr/bin/env python
#
def r8_zeta ( p ):

#*****************************************************************************80
#
## R8_ZETA estimates the Riemann Zeta function.
#
#  Discussion:
#
#    For 1 < P, the Riemann Zeta function is defined as:
#
#      ZETA ( P ) = Sum ( 1 <= N < oo ) 1 / N ^ P
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, real P, the power to which the integers are raised.
#    P must be greater than 1.  For integral P up to 20, a
#    precomputed value of ZETA is returned otherwise the infinite
#    sum is approximated.
#
#    Output, real VALUE, an approximation to the Riemann
#    Zeta function.
#
  import numpy as np
  from r8_huge import r8_huge

  if ( p <= 1.0 ):
    value = r8_huge ( )
  elif ( p == 2.0 ):
    value = np.pi ** 2 / 6.0
  elif ( p == 3.0 ):
    value = 1.2020569032
  elif ( p == 4.0 ):
    value = np.pi ** 4 / 90.0
  elif ( p == 5.0 ):
    value = 1.0369277551
  elif ( p == 6.0 ):
    value = np.pi ** 6 / 945.0
  elif ( p == 7.0 ):
    value = 1.0083492774
  elif ( p == 8.0 ):
    value = np.pi ** 8 / 9450.0
  elif ( p == 9.0 ):
    value = 1.0020083928
  elif ( p == 10.0 ):
    value = np.pi ** 10 / 93555.0
  elif ( p == 11.0 ):
    value = 1.0004941886
  elif ( p == 12.0 ):
    value = 1.0002460866
  elif ( p == 13.0 ):
    value = 1.0001227133
  elif ( p == 14.0 ):
    value = 1.0000612482
  elif ( p == 15.0 ):
    value = 1.0000305882
  elif ( p == 16.0 ):
    value = 1.0000152823
  elif ( p == 17.0 ):
    value = 1.0000076372
  elif ( p == 18.0 ):
    value = 1.0000038173
  elif ( p == 19.0 ):
    value = 1.0000019082
  elif ( p == 20.0 ):
    value = 1.0000009540
  else:

    zsum = 0.0
    n = 0

    while ( True ):

      n = n + 1
      zsum_old = zsum
      zsum = zsum + 1.0 / n ** p

      if ( zsum <= zsum_old ):
        break

    value = zsum

  return value

def r8_zeta_test ( ):

#*****************************************************************************80
#
## R8_ZETA_TEST tests R8_ZETA.
#
#  Discussion:
#
#    Note that SCIPY provides a ZETA function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_ZETA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ZETA estimates the Zeta function.' )

  print ( '' )
  print ( '       P     R8_Zeta(P)' )
  print ( '' )
  for p in range ( 1, 26 ):
    v = r8_zeta ( p )
    print ( '  %6d  %14.6g' % ( p, v ) )

  print ( '' )
  for i in range ( 0, 9 ):
    p = 3.0 + float ( i ) / 8.0
    v = r8_zeta ( p )
    print ( '  %6g  %14.6g' % ( p, v ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ZETA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_zeta_test ( )
  timestamp ( )
 
