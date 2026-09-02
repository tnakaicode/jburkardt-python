#! /usr/bin/env python3
#
def spherical_harmonic_test ( ):

#*****************************************************************************80
#
## spherical_harmonic_test() tests spherical_harmonic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'spherical_harmonic_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test spherical_harmonic().' )

  spherical_harmonic_test01 ( )
  spherical_harmonic_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'spherical_harmonic_test():' )
  print ( '  Normal end of execution.' )

  return

def spherical_harmonic_test01 ( ):

#*****************************************************************************80
#
## spherical_harmonic_test01() tests legendre_associated_normalized().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 May 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'spherical_harmonic_test01():' )
  print ( '  legendre_associated_normalized() evaluates the' )
  print ( '  associated Legrendre functions, using a' )
  print ( '  normalization appropriate for spherical harmonics.' )
  print ( '  legendre_associated_normalized_values() returns some exact values.' )
  print ( '' )
  print ( '      N       M    X     Exact F     PNM(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, fx = legendre_associated_normalized_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = legendre_associated_normalized ( n, m, x )

    print ( '  %6d  %6d  %6f  %12f  %12f' % ( n, m, x, fx, fx2[n] ) )

  return

def spherical_harmonic_test02 ( ):

#*****************************************************************************80
#
## spherical_harmonic_test02() tests spherical_harmonic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 May 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'spherical_harmonic_test02():' )
  print ( '  spherical_harmonic() evaluates the spherical harmonic function.' )
  print ( '  spherical_harmonic_values() returns some exact values.' )
  print ( '' )
  print ( '      L       M    THETA   PHI   YR   YI' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, l, m, theta, phi, yr, yi = spherical_harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    c, s = spherical_harmonic ( l, m, theta, phi )

    print ( '  %6d  %6d  %6f  %6f  %12f  %12f' % ( l, m, theta, phi, yr, yi ) )
    print ( '                                      %12f  %12f' % ( c[l], s[l] ) )

  return

def legendre_associated_normalized ( n, m, x ):

#*****************************************************************************80
#
## legendre_associated_normalized(): normalized associated Legendre functions.
#
#  Discussion:
#
#    The unnormalized associated Legendre functions P_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( P_N^M(X) )^2 dX
#      = 2 * ( N + M )! / ( ( 2 * N + 1 ) * ( N - M )! )
#
#    By dividing the function by the square root of this term,
#    the normalized associated Legendre functions have norm 1.
#
#    However, we plan to use these functions to build spherical
#    harmonics, so we use a slightly different normalization factor of
#
#      sqrt ( ( ( 2 * N + 1 ) * ( N - M )! ) / ( 4 * pi * ( N + M )! ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    real X, the point at which the function is to be
#    evaluated.  X must satisfy -1 <= X <= 1.
#
#  Output:
#
#    real CX(1:N+1), the values of the first N+1 function.
#
  import math
  import numpy as np

  if ( m < 0 ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of M is ', m )
    print ( '  but M must be nonnegative.' )
    raise Exception ( 'legendre_associated_normalized(): Fatal error!' )
 
  if ( n < m ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of M = #d', m )
    print ( '  Input value of N = #d', n )
    print ( '  but M must be less than or equal to N.' )
    raise Exception ( 'legendre_associated_normalized(): Fatal error!' )
 
  if ( x < -1.0 ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of X = #g', x )
    print ( '  but X must be no less than -1.' )
    raise Exception ( 'legendre_associated_normalized(): Fatal error!' )

  if ( 1.0 < x ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of X = #g', x )
    print ( '  but X must be no more than 1.' )
    raise Exception ( 'legendre_associated_normalized(): Fatal error!' )
  
  cx = np.zeros ( n + 1 )

  cx[m] = 1.0
  somx2 = np.sqrt ( 1.0 - x * x )
 
  fact = 1.0
  for i in range ( 0, m ):
    cx[m] = - cx[m] * fact * somx2
    fact = fact + 2.0
 
  if ( m < n ):
    cx[m+1] = x * ( 2 * m + 1 ) * cx[m]

  for i in range ( m + 2, n + 1 ):
    cx[i] = ( ( 2 * i     - 1 ) * x * cx[i-1] \
              + (   - i - m + 1 ) *   cx[i-2] ) \
              / (     i - m     )
#
#  Normalization.
#
  for mm in range ( m, n + 1 ):
    factor = np.sqrt ( ( ( 2 * mm + 1 ) * math.factorial ( mm - m ) ) \
      / ( 4.0 * np.pi * math.factorial ( mm + m ) ) )
    cx[mm] = cx[mm] * factor

  return cx
 
def legendre_associated_normalized_values ( n_data ):

#*****************************************************************************80
#
## legendre_associated_normalized_values(): normalized associated Legendre.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#    The function is normalized by dividing by
#
#      sqrt ( 4 * pi * ( n + m )! / ( 2 * n + 1 ) / ( n - m )! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2010
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, integer M, real X,
#    the arguments of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( [ \
     0.2820947917738781, \
     0.2443012559514600, \
    -0.2992067103010745, \
    -0.07884789131313000, \
    -0.3345232717786446, \
     0.2897056515173922, \
    -0.3265292910163510, \
    -0.06997056236064664, \
     0.3832445536624809, \
    -0.2709948227475519, \
    -0.2446290772414100, \
     0.2560660384200185, \
     0.1881693403754876, \
    -0.4064922341213279, \
     0.2489246395003027, \
     0.08405804426339821, \
     0.3293793022891428, \
    -0.1588847984307093, \
    -0.2808712959945307, \
     0.4127948151484925, \
    -0.2260970318780046 ] )

  m_vec = np.array ( [ \
    0, 0, 1, 0, \
    1, 2, 0, 1, \
    2, 3, 0, 1, \
    2, 3, 4, 0, \
    1, 2, 3, 4, \
    5 ] )

  n_vec = np.array ( [ \
    0,  1,  1,  2, \
    2,  2,  3,  3, \
    3,  3,  4,  4, \
    4,  4,  4,  5, \
    5,  5,  5,  5, \
    5 ] )

  x_vec = np.array ( [ \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50 ] )

  if ( n_data < 0 ):
    n_data = 0

  n_data = n_data + 1

  if ( n_max < n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data-1]
    m = m_vec[n_data-1]
    x = x_vec[n_data-1]
    fx = fx_vec[n_data-1]

  return n_data, n, m, x, fx

def spherical_harmonic_angle_table ( l, m, theta_num, phi_num ):

#*****************************************************************************80
#
## spherical_harmonic_angle_table() tabulates a spherical harmonic over angles.
#
#  Discussion:
#
#    This function produces a table of the spherical harmonic 
#    function Y(l,m,theta,phi) over a range of angular values of theta and phi.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L, M, the indices of the spherical harmonic.
#
#    integer THETA_NUM, PHI_NUM, the number of values of THETA
#    and PHI to be used to construct the evaluation grid.
#
#  Output:
#
#    real ZC(THETA_NUM,PHI_NUM), ZS(THETA_NUM,PHI_NUM), the
#    table of components of the harmonic function.
#
  import numpy as np

  phi_min = 0.0
  phi_max = np.pi
  theta_min = 0.0
  theta_max = 2 * np.pi

  zc = np.zeros ( [ theta_num, phi_num ] )
  zs = np.zeros ( [ theta_num, phi_num ] )

  for j in range ( 1, phi_num + 1 ):

    phi = ( ( phi_num - j     ) * phi_min \
          + (           j - 1 ) * phi_max ) \
          / ( phi_num     - 1 )

    for i in range ( 1, theta_num + 1 ):

      theta = ( ( theta_num - i     ) * theta_min \
              + (             i - 1 ) * theta_max ) \
              / ( theta_num     - 1 )

      a, b = spherical_harmonic ( l, m, phi, theta )
      zc[i-1,j-1] = a[l]
      zs[i-1,j-1] = b[l]

  return zc, zs

def spherical_harmonic ( l, m, theta, phi ):

#*****************************************************************************80
#
## spherical_harmonic() evaluates spherical harmonic functions.
#
#  Discussion:
#
#    The spherical harmonic function Y(L,M,THETA,PHI)(X) is the
#    angular part of the solution to Laplace's equation in spherical
#    coordinates.
#
#    Y(L,M,THETA,PHI)(X) is related to the associated Legendre
#    function as follows:
#
#      Y(L,M,THETA,PHI)(X) = FACTOR * P(L,M)(cos(THETA)) * exp ( i * M * PHI )
#
#    Here, FACTOR is a normalization factor:
#
#      FACTOR = sqrt ( ( 2 * L + 1 ) * ( L - M )! / ( 4 * PI * ( L + M )! ) )
#
#    In Mathematica, a spherical harmonic function can be evaluated by
#
#      SphericalHarmonicY [ l, m, theta, phi ]
#
#    Note that notational tradition in physics requires that THETA
#    and PHI represent the reverse of what they would normally mean
#    in mathematical notation that is, THETA goes up and down, and
#    PHI goes around.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1999.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer L, the first index of the spherical harmonic function.
#    Normally, 0 <= L.
#
#    integer M, the second index of the spherical harmonic function.
#    Normally, -L <= M <= L.
#
#    real THETA, the polar angle, for which
#    0 <= THETA <= PI.
#
#    real PHI, the longitudinal angle, for which
#    0 <= PHI <= 2*PI.
#
#  Output:
#
#    real C(1:L+1), S(1:L+1), the real and imaginary
#    parts of the functions Y(L,0:L,THETA,PHI).
#
  import numpy as np

  m_abs = np.abs ( m )

  plm = legendre_associated_normalized ( l, m_abs, np.cos ( theta ) )

  c = plm * np.cos ( m * phi )
  s = plm * np.sin ( m * phi )

  if ( m < 0 ):
    c = - c
    s = - s

  return c, s

def spherical_harmonic_values ( n_data ):

#*****************************************************************************80
#
## spherical_harmonic_values() returns values of spherical harmonic functions.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      SphericalHarmonicY [ l, m, theta, phi ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer L, integer M, real THETA, PHI, the arguments
#    of the function.
#
#    real YR, YI, the real and imaginary parts of
#    the function.
#
  import numpy as np

  n_max = 20

  l_vec = np.array ( [ \
     0,  1,  2,  \
     3,  4,  5,  \
     5,  5,  5,  \
     5,  4,  4,  \
     4,  4,  4,  \
     3,  3,  3,  \
     3,  3 ] )

  m_vec = np.array ( [ \
     0,  0,  1,  \
     2,  3,  5,  \
     4,  3,  2,  \
     1,  2,  2,  \
     2,  2,  2,  \
    -1, -1, -1,  \
    -1, -1 ] )

  phi_vec = np.array ( [ \
    0.1047197551196598E+01, 0.1047197551196598E+01, 0.1047197551196598E+01, \
    0.1047197551196598E+01, 0.1047197551196598E+01, 0.6283185307179586E+00, \
    0.6283185307179586E+00, 0.6283185307179586E+00, 0.6283185307179586E+00, \
    0.6283185307179586E+00, 0.7853981633974483E+00, 0.7853981633974483E+00, \
    0.7853981633974483E+00, 0.7853981633974483E+00, 0.7853981633974483E+00, \
    0.4487989505128276E+00, 0.8975979010256552E+00, 0.1346396851538483E+01, \
    0.1795195802051310E+01, 0.2243994752564138E+01 ] )

  theta_vec = np.array ( [ \
    0.5235987755982989E+00, 0.5235987755982989E+00, 0.5235987755982989E+00, \
    0.5235987755982989E+00, 0.5235987755982989E+00, 0.2617993877991494E+00, \
    0.2617993877991494E+00, 0.2617993877991494E+00, 0.2617993877991494E+00, \
    0.2617993877991494E+00, 0.6283185307179586E+00, 0.1884955592153876E+01, \
    0.3141592653589793E+01, 0.4398229715025711E+01, 0.5654866776461628E+01, \
    0.3926990816987242E+00, 0.3926990816987242E+00, 0.3926990816987242E+00, \
    0.3926990816987242E+00, 0.3926990816987242E+00 ] )

  yi_vec = np.array ( [ \
    0.0000000000000000E+00,  0.0000000000000000E+00, -0.2897056515173922E+00, \
    0.1916222768312404E+00,  0.0000000000000000E+00,  0.0000000000000000E+00, \
    0.3739289485283311E-02, -0.4219517552320796E-01,  0.1876264225575173E+00, \
   -0.3029973424491321E+00,  0.4139385503112256E+00, -0.1003229830187463E+00, \
    0.0000000000000000E+00, -0.1003229830187463E+00,  0.4139385503112256E+00, \
   -0.1753512375142586E+00, -0.3159720118970196E+00, -0.3940106541811563E+00, \
   -0.3940106541811563E+00, -0.3159720118970196E+00 ] )

  yr_vec = np.array ( [ \
   0.2820947917738781E+00,  0.4231421876608172E+00, -0.1672616358893223E+00, \
  -0.1106331731112457E+00,  0.1354974113737760E+00,  0.5390423109043568E-03, \
  -0.5146690442951909E-02,  0.1371004361349490E-01,  0.6096352022265540E-01, \
  -0.4170400640977983E+00,  0.0000000000000000E+00,  0.0000000000000000E+00, \
   0.0000000000000000E+00,  0.0000000000000000E+00,  0.0000000000000000E+00, \
   0.3641205966137958E+00,  0.2519792711195075E+00,  0.8993036065704300E-01, \
  -0.8993036065704300E-01, -0.2519792711195075E+00 ] )

  if ( n_data < 0 ):
    n_data = 0

  n_data = n_data + 1

  if ( n_max < n_data ):
    n_data = 0
    l = 0
    m = 0
    theta = 0.0
    phi = 0
    yr = 0.0
    yi = 0.0
  else:
    l = l_vec[n_data-1]
    m = m_vec[n_data-1]
    theta = theta_vec[n_data-1]
    phi = phi_vec[n_data-1]
    yr = yr_vec[n_data-1]
    yi = yi_vec[n_data-1]

  return n_data, l, m, theta, phi, yr, yi

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
  spherical_harmonic_test ( )
  timestamp ( )

