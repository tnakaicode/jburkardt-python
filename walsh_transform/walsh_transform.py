#! /usr/bin/env python3
#
def ffwt ( n, x ):

#*****************************************************************************80
#
## ffwt() performs an in-place fast Walsh transform.
#
#  Discussion:
#
#    This routine performs a fast Walsh transform on an input series X
#    leaving the transformed results in X.
#    X is dimensioned N, which must be a power of 2.
#    The results of this Walsh transform are in sequency order.
#
#    The output sequence could be normalized by dividing by N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    This version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Input:
#
#    integer N, the number of items in X.
#    N must be a power of 2.
#
#    real X(N), the data to be transformed.
#
#  Output:
#
#    real X(N), the transformed data.
#
  import numpy as np
  
  m = i4_log_2 ( n )

  two_power = np.zeros ( m, dtype = np.int32 )

  two_power[m-1] = 1
  for i in range ( m - 2, -1, -1 ):
    two_power[i] = 2 * two_power[i+1]

  nz = 1
  
  for l in range ( 0, m ):

    nzi = 2 * nz
    nzn = int ( n / nzi )
    nz2 = int ( nz / 2 )
    if ( nz2 == 0 ):
      nz2 = 1

    for i in range ( 0, nzn ):

      js = i * nzi - 1
      z = 1.0

      for ii in range ( 0, 2 ):

        for j in range ( 0, nz2 ):
          js = js + 1
          j2 = js + nz
          hold = x[js] + z * x[j2]
          z = - z
          x[j2] = x[js] + z * x[j2]
          x[js] = hold
          z = - z

        if ( l == 0 ):
          break

        z = - 1.0
        
    nz = nz * 2
#
#  Bit reversal section.
#
  nw = 0
  
  for k in range ( 1, n + 1 ):
#
#  Choose correct index and switch elements if not already switched.
#
    if ( k < nw + 1 ):
      hold = x[nw]
      x[nw] = x[k-1]
      x[k-1] = hold
#
#  Bump up series by 1.
#
    for i in range ( 1, m + 1 ):

      ii = i
      if ( nw < two_power[i-1] ):
        break

      mw = int ( nw / two_power[i-1] )
      mw1 = int ( mw / 2 )
      if ( mw <= 2 * mw1 ):
        break

      nw = nw - two_power[i-1]

    nw = nw + two_power[ii-1]

  return x

def ffwt_test ( rng ):

#*****************************************************************************80
#
## ffwt_test() tests ffwt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np
   
  n = 16

  print ( '' )
  print ( 'ffwt_test():' )
  print ( '  ffwt() computes a fast Walsh transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      w = rng.random ( size = n )
    else:
      w = np.linspace ( 1, n, n )

    x = w.copy ( )
    
    w = ffwt ( n, w )
    
    y = w.copy ( )
    for i in range ( 0, n ):
      y[i] = y[i] / float ( n )

    w = ffwt ( n, w )
    
    z = w.copy ( )
    for i in range ( 0, n ):
      z[i] = z[i] / float ( n )

    print ( '' )
    print ( '     I        X(I)   Y=FFWT(X)/N  Z=FFWT(Y)/N' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %10f  %10f  %10f' % ( i, x[i], y[i], z[i] ) )

  return

def fwt ( n, x ):

#*****************************************************************************80
#
## fwt() performs a fast Walsh transform.
#
#  Discussion:
#
#    This routine performs a fast Walsh transform on an input series X
#    leaving the transformed results in X.
#    X is dimensioned N, which must be a power of 2.
#    The results of this Walsh transform are in sequency order.
#
#    The output sequence could be normalized by dividing by N.
#
#    Note that the program text in the reference included the line
#      y(jd) = abs ( x(j) - x(j2) )
#    which has been corrected to:
#      y(jd) = x(j) - x(j2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    This version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Input:
#
#    integer N, the number of items in X.
#    N must be a power of 2.
#
#    real X(N), the data to be transformed.
#
#  Output:
#
#    real X(N), the transformed data.
#
  import numpy as np
  
  y = np.zeros ( n )
  n2 = int ( n / 2 )
  m = i4_log_2 ( n )

  nz = 1
  
  for l in range ( 0, m ):

    ny = 0
    nzi = 2 * nz
    nzn = int ( n / nzi )

    for i in range ( 0, nzn ):

      nx = ny + 1
      ny = ny + nz
      js = i * nzi
      jd = js + nzi + 1

      for j in range ( nx, ny + 1 ):
        js = js + 1
        j2 = j + n2
        y[js-1] = x[j-1] + x[j2-1]
        jd = jd - 1
        y[jd-1] = x[j-1] - x[j2-1]

    x = y.copy ( )
    
    nz = nz * 2

  return x

def fwt_test ( rng ):

#*****************************************************************************80
#
## fwt_test() tests fwt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np
 
  n = 16

  print ( '' )
  print ( 'fwt_test():' )
  print ( '  fwt() computes a fast Walsh transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      w = rng.random ( size = n )
    else:
      w = np.linspace ( 1, n, n )

    x = w.copy ( )

    w = fwt ( n, w )
    
    y = w.copy ( )
    for i in range ( 0, n ):
      y[i] = y[i] / float ( n )
      
    w = fwt ( n, w )
    
    z = w.copy ( )
    for i in range ( 0, n ):
      z[i] = z[i] / float ( n )

    print ( '' )
    print ( '     I        X(I)    Y=FWT(X)/N   Z=FWT(Y)/N' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %10f  %10f  %10f' % ( i, x[i], y[i], z[i] ) )
      
  return

def haar ( n, x ):

#*****************************************************************************80
#
## haar() performs a Haar transform.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    This version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Input:
#
#    integer N, the number of items in X.
#    N must be a power of 2.
#
#    real X(N), the data to be transformed.
#
#  Output:
#
#    real X(N), the transformed data.
#
  import numpy as np
  
  k = i4_log_2 ( n )

  l2 = 2 ** k
  
  for i in range ( 0, k ):

    l2 = l2 // 2

    y = np.zeros ( 2 * l2 )
    for j in range ( 0, 2 * l2 ):
      y[j] = x[j]

    for j in range ( 1, l2 + 1 ):
      l3 = l2 + j
      jj = 2 * j - 1
      x[j-1] = y[jj-1] + y[jj]
      x[l3-1] = y[jj-1] - y[jj]

  return x

def haar_test ( rng ):

#*****************************************************************************80
#
## haar_test() tests haar(), haar_inverse() and hnorm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np
  
  n = 16

  print ( '' )
  print ( 'haar_test()' )
  print ( '  haar() computes a Haar transform.' )
  print ( '  hnorm() normalizes the transformed data.' )
  print ( '  haar_inverse() computes an inverse Haar transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      w = rng.random ( size = n )
    else:
      w = np.linspace ( 1, n, n )

    x = w.copy ( )

    w = haar ( n, w )

    y = w.copy ( )

    w = hnorm ( n, w )

    z = w.copy ( )

    w = haar_inverse ( n, w )

    print ( '' )
    print ( '     I        X(I)    Y=HAAR(X)  Z=HNORM(Y)  W=haar_inverse(Z)' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %10f  %10f  %10f  %10f' % ( i, x[i], y[i], z[i], w[i] ) )

  return

def haar_inverse ( n, x ):

#*****************************************************************************80
#
## haar_inverse() inverts a Haar transform.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    This version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Input:
#
#    integer N, the number of items in X.
#    N must be a power of 2.
#
#    real X(N), the data to be transformed.
#
#  Output:
#
#    real X(N), the transformed data.
#
  import numpy as np
  
  k = i4_log_2 ( n )

  l = 1
  
  for i in range ( 0, k ):

    y = np.zeros ( 2 * l )
    for j in range ( 0, 2 * l ):
      y[j] = x[j]

    for j in range ( 1, l + 1 ):
      lj = l + j
      jj = 2 * j
      jj1 = jj - 1
      x[jj-1] = y[j-1] - y[lj-1]
      x[jj1-1] = y[j-1] + y[lj-1]

    l = l * 2
    
  return x

def hnorm ( n, x ):

#*****************************************************************************80
#
## hnorm() computes normalization factors for a forward or inverse Haar transform.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Ken Beauchamp
#    This version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Input:
#
#    integer N, the number of items in X.
#    N must be a power of 2.
#
#    real X(N), the data to be normalized.
#
#  Output:
#
#    real X(N), the normalized data.
#
  k = i4_log_2 ( n )

  x[0] = x[0] / 2.0 ** k

  if ( 1 <= k ):
    x[1] = x[1] / 2.0 ** k

  for ii in range ( 2, k + 1 ):

    i = ii - 1
    wlk = 1.0 / 2.0 ** ( k - i )
    jmin = 2 ** i + 1
    jmax = 2 ** ii

    for j in range ( jmin, jmax + 1 ):
      x[j-1] = x[j-1] * wlk

  return x

def i4_log_2 ( i ):

#*****************************************************************************80
#
## i4_log_2() returns the integer part of the logarithm base 2 of |I|.
#
#  Discussion:
#
#    For positive I4_LOG_2(I), it should be true that
#      2^I4_LOG_2(X) <= |I| < 2^(I4_LOG_2(I)+1).
#    The special case of I4_LOG_2(0) returns -HUGE().
#
#  Example:
#
#     I  Value
#
#     0  -1
#     1,  0
#     2,  1
#     3,  1
#     4,  2
#     5,  2
#     6,  2
#     7,  2
#     8,  3
#     9,  3
#    10,  3
#   127,  6
#   128,  7
#   129,  7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 2 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 2 of
#    the absolute value of I.
#
  i = int ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0

    i = abs ( i )

    while ( 2 <= i ):
      i = ( i // 2 )
      value = value + 1

  return value

def i4_log_2_test ( ):

#*****************************************************************************80
#
## i4_log_2_test() tests i4_log_2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  test_num = 17

  x_test = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, \
    -3, -9, 1000, 1023, 1024, 1025 ]
 
  print ( '' )
  print ( 'i4_log_2_test():' )
  print ( '  i4_log_2() computes the whole part of log base 2.' )
  print ( '' )
  print ( '       X     I4_LOG_2' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test]
    j = i4_log_2 ( x )
    print ( '  %6d  %12d' % ( x, j ) )

  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = I4_MODP ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, I4_MODP(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  I4_MODP    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  n_vec = np.array ( [ 107, 107, -107, -107 ], dtype = np.int32 )
  d_vec = np.array ( [ 50, -50, 50, -50 ], dtype = np.int32 )

  print ( '' )
  print ( 'i4_modp_test():' )
  print ( '  i4_modp() factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IVAL, an integer value.
#
#    integer ILO, IHI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of IVAL.
#
  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test():' )
  print ( '  i4_wrap() forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  I4_WRAP(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def walsh ( n, x ):

#*****************************************************************************80
#
## walsh() performs a fast Walsh transform.
#
#  Discussion:
#
#    This routine performs a fast Wash transform on an input series X
#    leaving the transformed results in X.  The array Y is working space.
#    X and Y are dimensioned N, which must be a power of 2.
#    The results of this Walsh transform are in sequency order.
#
#    The output sequence could be normalized by dividing by N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    This version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Input:
#
#    integer N, the number of items in X.
#    N must be a power of 2.
#
#    real X(N), the data to be transformed.
#
#  Output:
#
#    real X(N), the transformed data.
#
  import numpy as np
  
  y = np.zeros ( n )
  
  n2 = int ( n / 2 )
  m = i4_log_2 ( n )
  z = - 1.0

  for j in range ( 1, m + 1 ):

    n1 = 2 ** ( m - j + 1 )
    j1 = 2 ** ( j - 1 )

    for l in range ( 1, j1 + 1 ):

      iss = ( l - 1 ) * n1 + 1
      i1 = 0
      w = z

      for i in range ( iss, iss + n1, 2 ):
        a = x[i-1]
        x[iss+i1-1] = a + x[i]
        i1 = i1 + 1
        y[i1-1] = ( x[i] - a ) * w
        w = w * z

      n2 = int ( n1 / 2 )
      
      for k in range ( 0, n2 ):
        x[n2+iss+k-1] = y[k]

  return x

def walsh_test ( rng ):

#*****************************************************************************80
#
## walsh_test() tests walsh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np
  
  n = 16

  print ( '' )
  print ( 'walsh_test():' )
  print ( '  walsh() computes a fast Walsh transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      w = rng.random ( size = n )
    else:
      w = np.linspace ( 1, n, n )

    x = w.copy ( )

    w = walsh ( n, w )
    
    y = w.copy ( )
    for i in range ( 0, n ):
      y[i] = y[i] / float ( n )
      
    w = walsh ( n, w )
    
    z = w.copy ( )
    for i in range ( 0, n ):
      z[i] = z[i] / float ( n )
      
    print ( '' )
    print ( '     I        X(I)    Y=FWT(X)/N   Z=FWT(Y)/N' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %10f  %10f  %10f' % ( i, x[i], y[i], z[i] ) )

  return

def walsh_transform_test ( ):

#*****************************************************************************80
#
## walsh_transform_test() tests walsh_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform
  
  print ( '' )
  print ( 'walsh_transform_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test walsh_transform().' )

  rng = default_rng ( )

  ffwt_test ( rng )
  fwt_test ( rng )
  haar_test ( rng )
  walsh_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'walsh_transform_test()' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  walsh_transform_test ( )
  timestamp ( )

