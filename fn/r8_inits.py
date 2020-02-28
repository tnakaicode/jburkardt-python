#! /usr/bin/env python
#
def r8_inits ( dos, nos, eta ):

#*****************************************************************************80
#
## R8_INITS initializes a Chebyshev series.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Parameters:
#
#    Input, real DOS(NOS), the Chebyshev coefficients.
#
#    Input, integer NOS, the number of coefficients.
#
#    Input, real ETA, the desired accuracy.
#
#    Output, integer VALUE, the number of terms of the series needed
#    to ensure the requested accuracy.
#
  from sys import exit

  if ( nos < 1 ):
    print ( '' )
    print ( 'R8_INITS - Fatal error!' )
    print ( '  Number of coefficients < 1.' )
    exit ( 'R8_INITS - Fatal error!' )

  if ( eta < dos[nos-1] ):

    print ( '' )
    print ( 'R8_INITS - Warning!' )
    print ( '  ETA may be too small.' )
    print ( '  The requested accuracy cannot be guaranteed' )
    print ( '  even if all available coefficients are used.' )
    value = nos

  else:

    err = 0.0

    for i in range ( nos - 1, -1, -1 ):
      value = i
      err = err + abs ( dos[value] )
      if ( eta < err ):
        break

  return value

def r8_inits_test ( ):

#*****************************************************************************80
#
## R8_INITS_TEST tests R8_INITS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sincs = np.array ( [ \
    -0.374991154955873175839919279977323464E+00, \
    -0.181603155237250201863830316158004754E+00, \
    +0.005804709274598633559427341722857921E+00, \
    -0.000086954311779340757113212316353178E+00, \
    +0.000000754370148088851481006839927030E+00, \
    -0.000000004267129665055961107126829906E+00, \
    +0.000000000016980422945488168181824792E+00, \
    -0.000000000000050120578889961870929524E+00, \
    +0.000000000000000114101026680010675628E+00, \
    -0.000000000000000000206437504424783134E+00, \
    +0.000000000000000000000303969595918706E+00, \
    -0.000000000000000000000000371357734157E+00, \
    +0.000000000000000000000000000382486123E+00, \
    -0.000000000000000000000000000000336623E+00, \
    +0.000000000000000000000000000000000256E+00 ] )

  print ( '' )
  print ( 'R8_INITS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_INITS determines the Chebyshev interpolant degree' )
  print ( '  necessary to guarantee a desired accuracy level.' )
  print ( '' )
  print ( '  Here, we use a 15 term Chebyshev expansion for the' )
  print ( '  sine function.' )
  print ( '' )
  print ( '  Accuracy    Terms Needed' )
  print ( '' )

  tol = 1.0
  for i in range ( 1, 19 ):
    n = r8_inits ( sincs, 15, tol )
    print ( '  %14.6g  %4d' % ( tol, n ) )
    tol = tol / 10.0
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_INITS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_inits_test ( )
  timestamp ( )
