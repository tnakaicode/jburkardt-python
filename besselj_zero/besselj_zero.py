#! /usr/bin/env python3
#
def besselj_zero_test ( ):

#*****************************************************************************80
#
## besselj_zero_test() tests besselj_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'besselj_zero_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test besselj_zero()' )

  n = 0;
  nt = 10;
  z0 = jn_zeros ( n, nt );

  n = 1;
  z1 = jn_zeros ( n, nt );

  print ( '' )
  print ( '    i    J0(root i)  J1(root i)' )
  print ( '' )
  for i in range ( 0, nt ):
    print ( '  %2d  %14.6g  %14.6g' % ( i, z0[i], z1[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'besselj_zero_test():' )
  print ( '  Normal end of execution.' )

  return

def jn_zeros ( n, nt ):

#*****************************************************************************80
#
## jn_zeros() computes the zeros of a Bessel function Jn(x).
#
#  Licensing:
#
#    This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
#    they give permission to incorporate this routine into a user program
#    provided that the copyright is acknowledged.
#
#  Modified:
#
#    14 June 2025
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45.
#
#  Input:
#
#    integer N: the order of the Bessel functions.
#
#    integer NT: the number of zeros.
#
#  Output:
#
#    real RJ0(NT): the first NT zeros of Jn(x).
#
  import numpy as np

  rj0 = np.zeros ( nt )

  if ( n <= 20 ):
    x = 2.82141 + 1.15859 * n
  else:
    x = n + 1.85576 * n**0.33333 + 1.03315 / n**0.33333

  l = 0

  while ( True ):

    x0 = x
    bjn, djn = jyndd ( n, x )
    x = x - bjn / djn

    if ( 1.0E-09 < abs ( x - x0 ) ):
      continue

    rj0[l] = x
    l = l + 1
    x = x + 3.1416 + ( 0.0972 + 0.0679 * n - 0.000354 * n**2 ) / l

    if ( nt <= l ):
      break

  return rj0

def jyndd ( n, x ):

#*****************************************************************************80
#
## jyndd() evaluates a Bessel function Jn(x) and derivative.
#
#  Licensing:
#
#    This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
#    they give permission to incorporate this routine into a user program
#    provided that the copyright is acknowledged.
#
#  Modified:
#
#    13 June 2025
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45.
#
#  Input:
#
#    integer N, the order.
#
#    real X, the argument.
#
#  Output:
#
#    real BJN, DJN, the values of Jn(x), Jn'(x).
#
  import numpy as np

  bj = np.zeros ( n + 2 )

  for nt in range ( 1, 901 ):

    mt = np.floor ( 0.5 * np.log10 ( 6.28 * nt ) \
      - nt * np.log10 ( 1.36 * np.abs ( x ) / nt ) )

    if ( 20 < mt ):
      break

  m = nt
  bs = 0.0
  f0 = 0.0
  f1 = 1.0E-35
  su = 0.0

  for k in range ( m, -1, -1 ):
 
    f = 2.0 * ( k + 1.0 ) * f1 / x - f0
 
    if ( k <= n + 1 ):
      bj[k] = f
 
    if ( ( k % 2 ) == 0 ):
      bs = bs + 2.0 * f
      if ( k != 0 ):
        su = su + ( -1.0 )**( k / 2 ) * f / k

    f0 = f1
    f1 = f

  for k in range ( 0, n + 2 ):
    bj[k] = bj[k] / ( bs - f )

  bjn = bj[n]
  djn = - bj[n+1] + n * bj[n] / x

  return bjn, djn

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  besselj_zero_test ( )
  timestamp ( )

