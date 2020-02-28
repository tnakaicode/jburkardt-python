#! /usr/bin/env python
#
def rfrac_to_cfrac ( m, p, q ):

#*****************************************************************************80
#
## RFRAC_TO_CFRAC converts a rational polynomial fraction to a continued fraction.
#
#  Discussion:
#
#    That is, it accepts
#
#      P(1) + P(2) * X + ... + P(M) * X^(M-1)
#      -------------------------------------------------------
#      Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
#
#    and returns the equivalent continued fraction:
#
#      1 / ( T(1) + X / ( T(2) + X / (...T(2*M-1) + X / ( T(2*M) ... )))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer M, defines the number of P coefficients,
#    and is one less than the number of Q coefficients, and one
#    half the number of T coefficients.
#
#    Input, real P(M), Q(M+1), the coefficients defining the rational
#    polynomial fraction.
#
#    Output, real T(2*M), the coefficients defining the continued fraction.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( [ m + 1, 2 * m + 1 ] )
  t = np.zeros ( 2 * m )

  for i in range ( 0, m + 1 ):
    a[i,0] = q[i]

  for i in range ( 0, m ):
    a[i,1] = p[i]

  t[0] = a[0,0] / a[0,1]
  ta = a[m,0]

  for i in range ( 1, m + 1 ):
    a[m-i,2*i] = ta

  for k in range ( 1, 2 * m - 1 ):

    ihi = ( 2 * m - k ) // 2

    for i in range ( 1, ihi + 1 ):
      a[i-1,k+1] = a[i,k-1] - t[k-1] * a[i,k]

    if ( a[0,k+1] == 0.0 ):
      print ( '' )
      print ( 'RFRAC_TO_CFRAC - Fatal error!' )
      print ( '  A(1,K+2) is zero for K = %d' % ( k ) )
      exit ( 'RFRAC_TO_CFRAC - Fatal error!' )

    t[k] = a[0,k] / a[0,k+1]

  t[2*m-1] = a[0,2*m-1] / a[0,2*m]

  return t

def rfrac_to_cfrac_test ( ):

#*****************************************************************************80
#
## RFRAC_TO_CFRAC_TEST tests RFRAC_TO_CFRAC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from cfrac_to_rfrac import cfrac_to_rfrac
  from r8vec_print import r8vec_print

  maxm = 10
  m = 3

  p = np.array ( [ 1.0, 1.0, 2.0 ] )
  q = np.array ( [ 1.0, 3.0, 1.0, 1.0 ] )

  print ( '' )
  print ( 'RFRAC_TO_CFRAC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RFRAC_TO_CFRAC: rational polynomial fraction to continued fraction.' )

  r8vec_print ( m, p, '  Rational polynomial numerator coefficients:' )
  r8vec_print ( m + 1, q, '  Rational polynomial numerator coefficients:' )
 
  h = rfrac_to_cfrac ( m, p, q )
 
  r8vec_print ( 2 * m, h, '  Continued fraction coefficients:' )

  g = np.ones ( 2 * m )

  p2, q2 = cfrac_to_rfrac ( 2 * m, g, h )
 
  r8vec_print ( m, p2, '  Recovered rational polynomial numerator coefficients:' )
  r8vec_print ( m + 1, q2, '  Recovered rational polynomial numerator coefficients:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RFRAC_TO_CFRAC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rfrac_to_cfrac_test ( )
  timestamp ( )

