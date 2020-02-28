#! /usr/bin/env python3
#
def ffwt ( n, x ):

#*****************************************************************************80
#
## FFWT performs an in-place fast Walsh transform.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    Python version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Parameters:
#
#    Input, integer N, the number of items in X.
#    N must be a power of 2.
#
#    Input, real X(N), the data to be transformed.
#
#    Output, real X(N), the transformed data.
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

def ffwt_test ( ):

#*****************************************************************************80
#
## FFWT_TEST tests FFWT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  n = 16

  print ( '' )
  print ( 'FFWT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FFWT computes a fast Walsh transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      seed = 123456789
      w, seed = r8vec_uniform_01 ( n, seed )
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
## FWT performs a fast Walsh transform.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    Python version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Parameters:
#
#    Input, integer N, the number of items in X.
#    N must be a power of 2.
#
#    Input, real X(N), the data to be transformed.
#
#    Output, real X(N), the transformed data.
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

def fwt_test ( ):

#*****************************************************************************80
#
## FWT_TEST tests FWT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  n = 16

  print ( '' )
  print ( 'FWT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FWT computes a fast Walsh transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      seed = 123456789
      w, seed = r8vec_uniform_01 ( n, seed )
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
## HAAR performs a Haar transform.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    Python version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Parameters:
#
#    Input, integer N, the number of items in X.
#    N must be a power of 2.
#
#    Input, real X(N), the data to be transformed.
#
#    Output, real X(N), the transformed data.
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

def haar_test ( ):

#*****************************************************************************80
#
## HAAR_TEST tests HAAR, HAARIN and HNORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  n = 16

  print ( '' )
  print ( 'HAAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HAAR computes a Haar transform.' )
  print ( '  HNORM normalizes the transformed data.' )
  print ( '  HAARIN computes an inverse Haar transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      seed = 123456789
      w, seed = r8vec_uniform_01 ( n, seed )
    else:
      w = np.linspace ( 1, n, n )

    x = w.copy ( )

    w = haar ( n, w )

    y = w.copy ( )

    w = hnorm ( n, w )

    z = w.copy ( )

    w = haarin ( n, w )

    print ( '' )
    print ( '     I        X(I)    Y=HAAR(X)  Z=HNORM(Y)  W=HAARIN(Z)' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %10f  %10f  %10f  %10f' % ( i, x[i], y[i], z[i], w[i] ) )

  return

def haarin ( n, x ):

#*****************************************************************************80
#
## HAARIN inverts a Haar transform.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    Python version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Parameters:
#
#    Input, integer N, the number of items in X.
#    N must be a power of 2.
#
#    Input, real X(N), the data to be transformed.
#
#    Output, real X(N), the transformed data.
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
## HNORM computes normalization factors for a forward or inverse Haar transform.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Ken Beauchamp
#    Python version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Parameters:
#
#    Input, integer N, the number of items in X.
#    N must be a power of 2.
#
#    Input, real X(N), the data to be normalized.
#
#    Output, real X(N), the normalized data.
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
## I4_LOG_2 returns the integer part of the logarithm base 2 of |I|.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose logarithm base 2 is desired.
#
#    Output, integer VALUE, the integer part of the logarithm base 2 of
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
## I4_LOG_2_TEST tests I4_LOG_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  test_num = 17

  x_test = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, \
    -3, -9, 1000, 1023, 1024, 1025 ]
 
  print ( '' )
  print ( 'I4_LOG_2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_LOG_2: whole part of log base 2.' )
  print ( '' )
  print ( '       X     I4_LOG_2' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test]
    j = i4_log_2 ( x )
    print ( '  %6d  %12d' % ( x, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_LOG_2_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## I4_MODP returns the nonnegative remainder of I4 division.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number to be divided.
#
#    Input, integer J, the number that divides I.
#
#    Output, integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  from sys import exit

  if ( j == 0 ):
    print ( '' )
    print ( 'I4_MODP - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    exit ( 'I4_MODP - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## I4_MODP_TEST tests I4_MODP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  test_num = 4

  n_vec = np.array ( [ 107, 107, -107, -107 ], dtype = np.int32 )
  d_vec = np.array ( [ 50, -50, 50, -50 ], dtype = np.int32 )

  print ( '' )
  print ( 'I4_MODP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_MODP factors a number' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_MODP_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## I4_WRAP forces an integer to lie between given limits by wrapping.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer IVAL, an integer value.
#
#    Input, integer ILO, IHI, the desired bounds for the integer value.
#
#    Output, integer VALUE, a "wrapped" version of IVAL.
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
## I4_WRAP_TEST tests I4_WRAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'I4_WRAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_WRAP forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  I4_WRAP(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_WRAP_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def walsh ( n, x ):

#*****************************************************************************80
#
## WALSH performs a fast Walsh transform.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    Original MATLAB version by Ken Beauchamp
#    Python version by John Burkardt
#
#  Reference:
#
#    Ken Beauchamp,
#    Walsh functions and their applications,
#    Academic Press, 1975,
#    ISBN: 0-12-084050-2,
#    LC: QA404.5.B33.
#
#  Parameters:
#
#    Input, integer N, the number of items in X.
#    N must be a power of 2.
#
#    Input, real X(N), the data to be transformed.
#
#    Output, real X(N), the transformed data.
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

def walsh_test ( ):

#*****************************************************************************80
#
## WALSH_TEST tests WALSH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  n = 16

  print ( '' )
  print ( 'WALSH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WALSH computes a fast Walsh transform.' )

  for j in range ( 1, 3 ):

    if ( j == 1 ):
      seed = 123456789
      w, seed = r8vec_uniform_01 ( n, seed )
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

def walsh_tests ( ):

#*****************************************************************************80
#
## WALSH_TESTS tests the WALSH library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'WALSH_TESTS' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the WALSH library.' )

  ffwt_test ( )
  fwt_test ( )
  haar_test ( )
  walsh_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'WALSH_TESTS' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  walsh_tests ( )
  timestamp ( )
