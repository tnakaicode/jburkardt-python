#! /usr/bin/env python
#
def sexpo ( ):

#*****************************************************************************80
#
## SEXPO samples the standard exponential distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm SA in the reference.
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
#    MATLAB version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Computer Methods for Sampling From the
#    Exponential and Normal Distributions,
#    Communications of the ACM,
#    Volume 15, Number 10, October 1972, pages 873-882.
#
#  Parameters:
#
#    Output, real VALUE, a random deviate from the standard
#    exponential distribution.
#
  import numpy as np
  from r4_uni_01 import r4_uni_01

  q = np.array ( [ \
       0.6931472, \
       0.9333737, \
       0.9888778, \
       0.9984959, \
       0.9998293, \
       0.9999833, \
       0.9999986, \
       0.9999999 ] )

  a = 0.0
  u = r4_uni_01 ( )

  while ( True ):

    u = u + u

    if ( 1.0 < u ):
      break

    a = a + q[0]

  u = u - 1.0

  if ( u <= q[0] ):
    value = a + u
    return value

  i = 1
  ustar = r4_uni_01 ( )
  umin = ustar

  while ( True ):

    ustar = r4_uni_01 ( )
    umin = min ( umin, ustar )
    i = i + 1

    if ( u <= q[i-1] ):
      break

  value = a + umin * q[0]

  return value

def sexpo_test ( ):

#*****************************************************************************80
#
## SEXPO_TEST tests SEXPO.
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
  print ( 'SEXPO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SEXPO generates exponentially distributed' )
  print ( '  random values.' )
  print ( '' )

  for test in range ( 0, test_num ):

    x = sexpo ( )
    print ( '  %f' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SEXPO_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sexpo_test ( )
  timestamp ( )

