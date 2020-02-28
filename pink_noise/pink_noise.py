#! /usr/bin/env python3
#
def cdelay2 ( m, q ):

#*****************************************************************************80
#
## CDELAY2 is a circular buffer implementation of M-fold delay.
#
#  Example:
#
#    Suppose we call CDELAY2 12 times, always with M = 3, and with
#    Q having the input value 3 on the first call.  Q will go through
#    the following sequence of values over the 12 calls:
#
#    I   M  Qin  Qout
#
#    1   3   3   2
#    2   3   2   1
#    3   3   1   0
#    4   3   0   3
#    5   3   3   2
#    6   3   2   1
#    7   3   1   0
#    8   3   0   3
#    9   3   3   2
#   10   3   2   1
#   11   3   1   0
#   12   3   0   3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    Original C version by Sophocles Orfanidis.
#    This Python version by John Burkardt.
#
#  Reference:
#
#    Sophocles Orfanidis,
#    Introduction to Signal Processing,
#    Prentice-Hall, 1995,
#    ISBN: 0-13-209172-0,
#    LC: TK5102.5.O246.
#
#  Parameters:
#
#    Input, integer M, the maximum value that Q can have.
#
#    Input, integer Q, a counter to be decremented.  
#
#    Output, integer Q, the decremented counter.  The value "after" 0 is M.  
#

#
#  Decrement the offset.
#
  q = q - 1
#
#  Q = - 1 wraps to Q = M.
#
  q = wrap2 ( m, q )

  return q

def cdelay2_test ( ):

#*****************************************************************************80
#
## CDELAY2_TEST tests CDELAY2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'CDELAY2_TEST' )
  print ( '  CDELAY2 is a circular buffer implementation' )
  print ( '  of an M-fold delay.  Q is a counter' )
  print ( '  which is decremented by CDELAY2, but reset to M' )
  print ( '  after it reaches 0.' )

  for m in range ( 2, 5 ):
    print ( '' )
    print ( '   I   M  Qin  Qout' )
    print ( '' )
    q = m
    for i in range ( 1, 3 * ( m + 1 ) + 1 ):
      q_in = q
      q = cdelay2 ( m, q )
      print ( '  %2d  %2d  %2d  %2d' % ( i, m, q_in, q ) )

  return

def corr ( n, x, m ):

#*****************************************************************************80
#
## CORR computes the sample correlation of a signal sample.
#
#  Discussion:
#
#    The sample correlation is defined, for 0 <= i < N, as
#
#      R(i) = 1/N * sum ( 0 <= j <= N - 1 - i ) X(i+j) * X(j)
#
#    The sample correlation is an estimate of the correlation function.
#
#    It is usually the case that the signal X is assumed to
#    have zero mean.  Here, we compute the mean and adjust the
#    calculation accordingly:
#
#      R(i) = 1/N * sum ( 0 <= j <= N - 1 - i )
#        ( X(i+j) - Xbar ) * ( X(j) - Xbar )
#
#    Experience suggests that only the first 5 or 10 percent of
#    the lags are statistically reliable, so that one might choose
#    M = N / 20 or M = N / 10, for instance.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sophocles Orfanidis,
#    Introduction to Signal Processing,
#    Prentice-Hall, 1995,
#    ISBN: 0-13-209172-0,
#    LC: TK5102.5.O246.
#
#  Parameters:
#
#    Input, integer N, the number of equally spaced signal
#    samples.
#
#    Input, real X(N), the signal samples.
#
#    Input, integer M, the maximum lag to consider.
#    0 <= M < N.
#
#    Output, real R(1:M+1), the sample correlations.
#
  import numpy as np

  r = np.zeros ( m + 1, dtype = np.float64 )

  xbar = np.sum ( x[0:n] ) / float ( n )

  for i in range ( 0, m + 1 ):
    for j in range ( 0, n - i ):
      r[i] = r[i] + ( x[i+j] - xbar ) * ( x[j] - xbar )

  r[0:m+1] = r[0:m+1] / float ( n )

  return r

def corr_test ( ):

#*****************************************************************************80
#
## CORR_TEST tests CORR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'CORR_TEST' )
  print ( '  CORR computes the sample correlations of a signal.' )

  n = 101
  x = np.linspace ( 0.0, 6.0 * np.pi, n )
  y = np.sin ( x )
#
#  Idiotic FLOOR command returns a FLOAT!
#
  m = int ( np.floor ( n / 10 ) )

  c = corr ( n, y, m )

  r8vec_print ( m + 1, c, '  Correlations of y=sin(x) with lags 0, 1, 2, ...' )

  return

def cross_corr ( n, x, y, m ):

#*****************************************************************************80
#
## CROSS_CORR computes the sample cross correlation between two signal samples.
#
#  Discussion:
#
#    The sample cross correlation is defined, for 0 <= i < N, as
#
#      R(i) = 1/N * sum ( 0 <= j <= N - 1 - i ) X(i+j) * Y(j)
#
#    The sample cross correlation is an estimate of the cross
#    correlation function.
#
#    It is usually the case that the signals X and Y are assumed to
#    have zero mean.  Here, we compute the means and adjust the
#    calculation accordingly:
#
#      R(i) = 1/N * sum ( 0 <= j <= N - 1 - i )
#        ( X(i+j) - Xbar ) * ( Y(j) - Ybar )
#
#    Experience suggests that only the first 5 or 10 percent of
#    the lags are statistically reliable, so that one might choose
#    M = N / 20 or M = N / 10, for instance.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sophocles Orfanidis,
#    Introduction to Signal Processing,
#    Prentice-Hall, 1995,
#    ISBN: 0-13-209172-0,
#    LC: TK5102.5.O246.
#
#  Parameters:
#
#    Input, integer N, the number of equally spaced signal
#    samples.
#
#    Input, real X(N), Y(N), the signal samples.
#
#    Input, integer M, the maximum lag to consider.
#    0 <= M < N.
#
#    Output, real R(1:M+1), the sample correlations.
#
  import numpy as np

  r = np.zeros ( m + 1, dtype = np.float64 )

  xbar = np.sum ( x[0:n] ) / float ( n )
  ybar = np.sum ( y[0:n] ) / float ( n )

  for i in range ( 0, m + 1 ):
    for j in range ( 0, n - i ):
      r[i] = r[i] + ( x[i+j] - xbar ) * ( y[j] - ybar )

  r[0:m+1] = r[0:m+1] / float ( n )

  return r

def cross_corr_test ( ):

#*****************************************************************************80
#
## CROSS_CORR_TEST tests CROSS_CORR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'CROSS_CORR_TEST' )
  print ( '  CROSS_CORR computes the sample cross correlations' )
  print ( '  between two signals.' )

  n = 101
  x = np.linspace ( 0.0, 6.0 * np.pi, n )
  y1 = np.sin ( x )
  y2 = np.sin ( x + np.pi / 10.0 )
  m = int ( np.floor ( n / 10 ) )

  c = cross_corr ( n, y1, y2, m )

  r8vec_print ( m + 1, c, \
    '  Correlations of y1=sin(x), y2=sin(x+pi/10) with lags 0, 1, 2, ...' )

  return

def pink_noise_test ( ):

#*****************************************************************************80
#
## PINK_NOISE_TEST tests the PINK_NOISE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PINK_NOISE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the PINK_NOISE library.' )

  cdelay2_test ( )
  corr_test ( )
  cross_corr_test ( )
  ran1f_test ( )
  ranh_test ( )
  wrap2_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'PINK_NOISE_TEST:' )
  print ( '  Normal end of execution.' )
  print ( '' )

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

def ran1f ( b, u, q ):

#*****************************************************************************80
#
## RAN1F is a 1/F random number generator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    Original C version by Sophocles Orfanidis.
#    This Python version by John Burkardt.
#
#  Reference:
#
#    Sophocles Orfanidis,
#    Introduction to Signal Processing,
#    Prentice-Hall, 1995,
#    ISBN: 0-13-209172-0,
#    LC: TK5102.5.O246.
#
#  Parameters:
#
#    Input, integer B, the number of signals to combine.
#    For this algorithm, B cannot be more than 31!
#
#    Input, real U(B), the signals to combine.  It is expected
#    that each of the initial values of U will be drawn from a distribution
#    with zero mean.
#
#    Input, int Q(B), a set of counters that determine when each
#    entry of U is to be updated.
#
#    Output, real Z, the value.
#
#    Output, real U(B), the signals, some of which may have been updated.
#
#    Output, integer Q(B), the counters, which have been updated.
#
  if ( 31 < b ):
    print ( '' )
    print ( 'RAN1F - Fatal error!' )
    print ( '  32 <= B, too many signals.' )
    error ( 'RAN1F - Fatal error!' )

  z = 0.0

  j = 1
  for i in range ( 0, b ):
    y, u[i], q[i] = ranh ( j, u[i], q[i] )
    z = z + y
    j = j * 2

  if ( 0 < b ):
    z = z / float ( b )

  return z, u, q

def ran1f_test ( ):

#*****************************************************************************80
#
## RAN1F_TEST tests RAN1F.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'RAN1F_TEST' )
  print ( '  RAN1F generates random values with an approximate' )
  print ( '  1/F distribution.' )

  b = 1

  while ( b < 32 ):

    for rep in range ( 0, 4 ):

      u = np.random.rand ( b )
      q = np.zeros ( b, dtype = np.int32 )

      print ( '' )
      print ( '   B   I      Y' )
      print ( '' )

      for i in range ( 1, 21 ):
        y, u, q = ran1f ( b, u, q )
        print ( '  %2d  %2d  %10f' % ( b, i, y ) )

    b = b * 2

  return

def ranh ( d, u, q ):

#*****************************************************************************80
#
## RANH is a hold random number generator of period D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    Original C version by Sophocles Orfanidis.
#    This Python version by John Burkardt.
#
#  Reference:
#
#    Sophocles Orfanidis,
#    Introduction to Signal Processing,
#    Prentice-Hall, 1995,
#    ISBN: 0-13-209172-0,
#    LC: TK5102.5.O246.
#
#  Parameters:
#
#    Input, int D, the hold period.  D must be at least 1.
#
#    Input, real U, a value to be held until Q has decremented to 0.
#
#    Input, int *Q, a counter which is decremented by 1 on each call
#    until reaching 0.
#
#    Output, double Y, the input value of U.
#
#    Output, real U, a value which will have been randomly reset
#    if Q reached 0.
#
#    Output, integer Q, the decremented counter.
#
  import numpy as np
  from sys import exit

  if ( d < 1 ):
    print ( '' )
    print ( 'RANH - Fatal error!' )
    print ( '  D < 1.' )
    exit ( 'RANH - Fatal error!' )
#
#  Hold this sample for D calls.
#
  y = u
#
#  Decrement Q and wrap mod D.
#
  q = cdelay2 ( d - 1, q )
#
#  Every D calls, get a new U with zero mean.
#
  if ( q == 0 ):
    u = 2.0 * np.random.rand ( 1 ) - 1.0

  return y, u, q

def ranh_test ( ):

#*****************************************************************************80
#
## RANH_TEST tests RANH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'RANH_TEST' )
  print ( '  RANH is a random hold function.' )
  print ( '  Given a value U and a delay D, it returns the value' )
  print ( '  U for D calls, then resets U.' )

  for d in range ( 5, 0, -1 ):
    print ( '' )
    print ( '   I   D   Q      U           Y' )
    print ( '' )
    u = 0.5
    q = 3
    for i in range ( 1, 21 ):
      y, u, q = ranh ( d, u, q )
      print ( '  %2d  %2d  %2d  %10f  %10f' % ( i, d, q, u, y ) )

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

def wrap2 ( m, q ):

#*****************************************************************************80
#
## WRAP2 is a circular wrap of the pointer offset Q.
#
#  Discussion:
#
#    Input values of Q between 0 and M are 'legal'.
#    Values of Q below 0 are incremented by M + 1 until they are legal.
#    Values of Q above M are decremented by M + 1 until they become legal.
#    The legal value is the output value of the function.
#
#  Example:
#
#    M  Qin  Qout
#
#    3  -5   3
#    3  -4   0
#    3  -3   1
#    3  -2   2
#    3  -1   3
#    3   0   0
#    3   1   1
#    3   2   2
#    3   3   3
#    3   4   0
#    3   5   1
#    3   6   2
#    3   7   3
#    3   8   0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    Original C version by Sophocles Orfanidis.
#    This Python version by John Burkardt.
#
#  Reference:
#
#    Sophocles Orfanidis,
#    Introduction to Signal Processing,
#    Prentice-Hall, 1995,
#    ISBN: 0-13-209172-0,
#    LC: TK5102.5.O246.
#
#  Parameters:
#
#    Input, integer M, the maximum acceptable value for outputs.
#    M must be at least 0.
#
#    Input, integer Q, the value to be wrapped.
#
#    Output, integer Q, the wrapped value.
#
  from sys import exit

  if ( m < 0 ):
    print ( '' )
    print ( 'WRAP2 - Fatal error!' )
    print ( '  M < 0.' )
    exit ( 'WRAP2 - Fatal error!' )
#
#  When Q = M + 1, it wraps to Q = 0.
#
  while ( m < q ):
    q = q - m - 1
#
#  When Q = - 1, it wraps to Q = M.
#
  while ( q < 0 ):
    q = q + m + 1

  return q

def wrap2_test ( ):

#*****************************************************************************80
#
## WRAP2_TEST tests WRAP2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'WRAP2_TEST' )
  print ( '  WRAP2 performs a circular wrap.' )
  print ( '  Q is expected to range between 0 and M.' )
  print ( '  WRAP2 takes an input value of Q, and either' )
  print ( '  increments it by M+1 until in the range, or' )
  print ( '  decrements it by M+1 until in the range,' )
  print ( '  and returns the result as the function value.' )

  for m in range ( 2, 5 ):
    print ( '' )
    print ( '   M  Qin  Qout' )
    print ( '' )
    for i in range ( -5, 3 * m ):
      q = i
      q_in = q
      q = wrap2 ( m, q )
      print ( '  %2d  %2d  %2d' % ( m, q_in, q ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  pink_noise_test ( )
  timestamp ( )
