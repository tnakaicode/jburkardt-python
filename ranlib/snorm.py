#! /usr/bin/env python
#
def snorm ( ):

#*****************************************************************************80
#
## SNORM samples the standard normal distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm FL, with M = 5, in the reference.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Extensions of Forsythe's Method for Random
#    Sampling from the Normal Distribution,
#    Mathematics of Computation,
#    Volume 27, Number 124, October 1973, page 927-937.
#
#  Parameters:
#
#    Output, real VALUE, a random deviate from the distribution.
#
  import numpy as np
  from r4_uni_01 import r4_uni_01

  a = np.array ( [ \
        0.0000000,     0.3917609E-01, 0.7841241E-01, 0.1177699, \
        0.1573107,     0.1970991,     0.2372021,     0.2776904, \
        0.3186394,     0.3601299,     0.4022501,     0.4450965, \
        0.4887764,     0.5334097,     0.5791322,     0.6260990, \
        0.6744898,     0.7245144,     0.7764218,     0.8305109, \
        0.8871466,     0.9467818,     1.009990,      1.077516, \
        1.150349,      1.229859,      1.318011,      1.417797, \
        1.534121,      1.675940,      1.862732,      2.153875 ] )

  d = np.array ( [ \
        0.0000000, 0.0000000, 0.0000000, 0.0000000, \
        0.0000000, 0.2636843, 0.2425085, 0.2255674, \
        0.2116342, 0.1999243, 0.1899108, 0.1812252, \
        0.1736014, 0.1668419, 0.1607967, 0.1553497, \
        0.1504094, 0.1459026, 0.1417700, 0.1379632, \
        0.1344418, 0.1311722, 0.1281260, 0.1252791, \
        0.1226109, 0.1201036, 0.1177417, 0.1155119, \
        0.1134023, 0.1114027, 0.1095039 ] )

  h = np.array ( [ \
        0.3920617E-01, 0.3932705E-01, 0.3950999E-01, 0.3975703E-01, \
        0.4007093E-01, 0.4045533E-01, 0.4091481E-01, 0.4145507E-01, \
        0.4208311E-01, 0.4280748E-01, 0.4363863E-01, 0.4458932E-01, \
        0.4567523E-01, 0.4691571E-01, 0.4833487E-01, 0.4996298E-01, \
        0.5183859E-01, 0.5401138E-01, 0.5654656E-01, 0.5953130E-01, \
        0.6308489E-01, 0.6737503E-01, 0.7264544E-01, 0.7926471E-01, \
        0.8781922E-01, 0.9930398E-01, 0.1155599,     0.1404344, \
        0.1836142,     0.2790016,     0.7010474 ] )

  t = np.array ( [ \
        0.7673828E-03, 0.2306870E-02, 0.3860618E-02, 0.5438454E-02, \
        0.7050699E-02, 0.8708396E-02, 0.1042357E-01, 0.1220953E-01, \
        0.1408125E-01, 0.1605579E-01, 0.1815290E-01, 0.2039573E-01, \
        0.2281177E-01, 0.2543407E-01, 0.2830296E-01, 0.3146822E-01, \
        0.3499233E-01, 0.3895483E-01, 0.4345878E-01, 0.4864035E-01, \
        0.5468334E-01, 0.6184222E-01, 0.7047983E-01, 0.8113195E-01, \
        0.9462444E-01, 0.1123001,     0.1364980,     0.1716886, \
        0.2276241,     0.3304980,     0.5847031 ] )

  u = r4_uni_01 ( )
  if ( u <= 0.5 ):
    s = 0.0
  else:
    s = 1.0

  u = 2.0 * u - s
  u = 32.0 * u
  i = int ( u )

  if ( i == 32 ):
    i = 31
#
#  Center
#
  if ( i != 0 ):

    ustar = u - i
    aa = a[i-1]

    while ( True ):

      if ( t[i-1] < ustar ):

        w = ( ustar - t[i-1] ) * h[i-1]

        y = aa + w

        if ( s != 1.0 ):
          value = y
        else:
          value = -y

        return value

      u = r4_uni_01 ( )
      w = u * ( a[i] - aa )
      tt = ( 0.5 * w + aa ) * w

      while ( True ):

        if ( tt < ustar ):
          y = aa + w
          if ( s != 1.0 ):
            value = y
          else:
            value = - y
          return value

        u = r4_uni_01 ( )

        if ( ustar < u ):
          break

        tt = u
        ustar = r4_uni_01 ( )

      ustar = r4_uni_01 ( )
#
#  Tail
#
  else:

    i = 6
    aa = a[31]

    while ( True ):

      u = u + u

      if ( 1.0 <= u ):
        break

      aa = aa + d[i-1]
      i = i + 1

    u = u - 1.0
    w = u * d[i-1]
    tt = ( 0.5 * w + aa ) * w

    while ( True ):

      ustar = r4_uni_01 ( )

      if ( tt < ustar ):
        y = aa + w
        if ( s != 1.0 ):
          value = y
        else:
          value = -y
        return value

      u = r4_uni_01 ( )

      if ( u <= ustar ):
        tt = u
      else:
        u = r4_uni_01 ( )
        w = u * d[i-1]
        tt = ( 0.5 * w + aa ) * w

  return value

def snorm_test ( ):

#*****************************************************************************80
#
## SNORM_TEST tests SNORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  test_num = 20

  print ( '' )
  print ( 'SNORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SNORM generates normally distributed' )
  print ( '  random values.' )
  print ( '' )

  for test in range ( 0, test_num ):

    x = snorm ( )
    print ( '  %f' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SNORM_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  snorm_test ( )
  timestamp ( )

