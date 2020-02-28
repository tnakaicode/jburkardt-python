#! /usr/bin/env python3
#
def asset_path ( s0, mu, sigma, t1, n ):

#*****************************************************************************80
#
## ASSET_PATH simulates the behavior of an asset price over time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    Black-Scholes for Scientific Computing Students,
#    Computing in Science and Engineering,
#    November/December 2004, Volume 6, Number 6, pages 72-79.
#
#  Parameters:
#
#    Input, real S0, the asset price at time 0.
#
#    Input, real MU, the expected growth rate.
#
#    Input, real SIGMA, the volatility of the asset.
#
#    Input, real T1, the expiry date.
#
#    Input, integer N, the number of steps to take between 0 and T1.
#
#    Output, real S(N+1), the option values from time 0 to T1 in equal steps.
#
  import numpy as np

  dt = t1 / float ( n )

  r = np.random.randn ( n )

  arg = np.exp ( ( mu - sigma ** 2 ) * dt + sigma * np.sqrt ( dt ) * r )

  s = s0 * np.cumprod ( arg )
#
#  Prepend the initial value S0.
#
  s = np.insert ( s, 0, s0, axis = 0 )

  return s

def asset_path_test ( ):

#*****************************************************************************80
#
## ASSET_PATH_TEST tests ASSET_PATH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ASSET_PATH_TEST:' )
  print ( '  Demonstrate the simulation of an asset price path.' )

  s0 = 2.0
  mu = 0.1
  sigma = 0.3
  n = 100
  t0 = 0.0
  t1 = 1.0

  print ( '' )
  print ( '  The asset price at time 0,     S0    = %f' % ( s0 ) )
  print ( '  The asset expected growth rate MU    = %f' % ( mu ) )
  print ( '  The asset volatility           SIGMA = %f' % ( sigma ) )
  print ( '  The expiry date                T1    = %f' % ( t1 ) )
  print ( '  The number of time steps       N     = %d' % ( n ) )

  s = asset_path ( s0, mu, sigma, t1, n )
#
#  Plot.
#
  t = np.linspace ( t0, t1, n + 1 )

  plt.plot ( t, s )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Value --> ' )
  plt.title ( 'Simulated asset path' )

  filename = 'asset_path.png'
  plt.savefig ( filename )
  print ( '  Figure saved as "%s"' % ( filename ) )
  plt.show ( )
  plt.clf ( )
#
#  Print a little.
#
  r8vec_print_some ( n + 1, s, 10, '  Partial results:' )
#
#  Write to a file.
#
  output_filename = 'asset_path.txt'

  r8vec_write ( output_filename, n + 1, s )
 
  print ( '' )
  print ( '  Full results written to "%s".' % ( output_filename ) )

  return

def binomial ( s0, e, r, sigma, t1, m ):

#*****************************************************************************80
#
## BINOMIAL uses the binomial method for a European call.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 August 2017
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    Black-Scholes for Scientific Computing Students,
#    Computing in Science and Engineering,
#    November/December 2004, Volume 6, Number 6, pages 72-79.
#
#  Parameters:
#
#    Input, real S0, the asset price at time 0.
#
#    Input, real E, the exercise price.
#
#    Input, real R, the interest rate.
#
#    Input, real SIGMA, the volatility of the asset.
#
#    Input, real T1, the expiry date.
#
#    Input, integer M, the number of steps to take between 0 and T1.
#
#    Output, real C, the option value at time 0.
#
  import numpy as np

  dt = t1 / float ( m )

  a = 0.5 * ( np.exp ( - r * dt ) + np.exp ( ( r + sigma ** 2 ) * dt ) )

  d = a - np.sqrt ( a ** 2 - 1.0 )
  u = a + np.sqrt ( a ** 2 - 1.0 )

  p = ( np.exp ( r * dt ) - d ) / ( u - d )

  w = np.zeros ( m + 1 )

  for i in range ( 0, m + 1 ):
    w[i] = max ( s0 * d ** ( m - i ) * u ** i - e, 0.0 )
#
#  Trace backwards to get the option value at time 0.
#
  for n in range ( m - 1, -1, -1 ):
    for i in range ( 0, n + 1 ):
      w[i] = ( 1.0 - p ) * w[i] + p * w[i+1]

  for i in range ( 0, m + 1 ):
    w[i] = np.exp ( - r * t1 ) * w[i]

  c = w[0]

  return c

def binomial_test ( ):

#*****************************************************************************80
#
## BINOMIAL_TEST tests BINOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BINOMIAL_TEST:' )
  print ( '  A demonstration of the binomial method' )
  print ( '  for option valuation.' )

  s0 = 2.0
  e = 1.0
  r = 0.05
  sigma = 0.25
  t1 = 3.0
  m = 256

  print ( '' )
  print ( '  The asset price at time 0, S0    = %f' % ( s0 ) )
  print ( '  The exercise price         E     = %f' % ( e ) )
  print ( '  The interest rate          R     = %f' % ( r ) )
  print ( '  The asset volatility       SIGMA = %f' % ( sigma ) )
  print ( '  The expiry date            T1    = %f' % ( t1 ) )
  print ( '  The number of intervals    M     = %d' % ( m ) )

  c = binomial ( s0, e, r, sigma, t1, m )

  print ( '' )
  print ( '  The option value is %f' % ( c ) )

  return

def bsf ( s0, t0, e, r, sigma, t1 ):

#*****************************************************************************80
#
## BSF evaluates the Black-Scholes formula for a European call.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    Black-Scholes for Scientific Computing Students,
#    Computing in Science and Engineering,
#    November/December 2004, Volume 6, Number 6, pages 72-79.
#
#  Parameters:
#
#    Input, real S0, the asset price at time T0.
#
#    Input, real T0, the time at which the asset price is known.
#
#    Input, real E, the exercise price.
#
#    Input, real R, the interest rate.
#
#    Input, real SIGMA, the volatility of the asset.
#
#    Input, real T1, the expiry date.
#
#    Output, real C, the value of the call option.
#
  import numpy as np

  tau = t1 - t0

  if ( 0.0 < tau ):

    d1 = ( np.log ( s0 / e ) + ( r + 0.5 * sigma ** 2 ) * tau ) \
      / ( sigma * np.sqrt ( tau ) )

    d2 = d1 - sigma * np.sqrt ( tau )

    n1 = 0.5 * ( 1.0 + erf ( d1 / np.sqrt ( 2.0 ) ) )
    n2 = 0.5 * ( 1.0 + erf ( d2 / np.sqrt ( 2.0 ) ) )

    c = s0 * n1 - e * np.exp ( - r * tau ) * n2

  else:

    c = max ( s0 - e, 0.0 )

  return c

def bsf_test ( ):

#*****************************************************************************80
#
## BSF_TEST tests BSF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BSF_TEST:' )
  print ( '  A demonstration of the Black-Scholes formula' )
  print ( '  for option valuation.' )

  s0 = 2.0
  t0 = 0.0
  e = 1.0
  r = 0.05
  sigma = 0.25
  t1 = 3.0

  print ( '' )
  print ( '  The asset price at time T0, S0    = %f' % ( s0 ) )
  print ( '  The time                    T0    = %f' % ( t0 ) )
  print ( '  The exercise price          E     = %f' % ( e ) )
  print ( '  The interest rate           R     = %f' % ( r ) )
  print ( '  The asset volatility        SIGMA = %f' % ( sigma ) )
  print ( '  The expiry date             T1    = %f' % ( t1 ) )

  c = bsf ( s0, t0, e, r, sigma, t1 )

  print ( '' )
  print ( '  The option value C = %f' % ( c ) )

  return

def erf ( x ):

#*****************************************************************************80
#
## ERF evaluates the error function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    Original version by John D Cook
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Input, real VALUE, the value of the error function.
#
  import math
#
#  Set constants.
#
  a1 =  0.254829592
  a2 = -0.284496736
  a3 =  1.421413741
  a4 = -1.453152027
  a5 =  1.061405429
  p  =  0.3275911
#
#  Save the sign of x.
#
  sign = 1
  if x < 0:
    sign = -1

  x = abs ( x )
#
#  Abramowitz and Stegun, formula 7.1.26
#
  t = 1.0 / ( 1.0 + p * x )

  y = 1.0 - ((((
      a5   * t 
    + a4 ) * t 
    + a3 ) * t 
    + a2 ) * t 
    + a1 ) * t * math.exp ( - x * x )

  value = sign * y

  return value

def forward ( e, r, sigma, t1, nx, nt, smax ):

#*****************************************************************************80
#
## FORWARD uses the forward difference method to value a European call option.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 August 2017
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    Black-Scholes for Scientific Computing Students,
#    Computing in Science and Engineering,
#    November/December 2004, Volume 6, Number 6, pages 72-79.
#
#  Parameters:
#
#    Input, real E, the exercise price.
#
#    Input, real R, the interest rate.
#
#    Input, real SIGMA, the volatility of the asset.
#
#    Input, real T1, the expiry date.
#
#    Input, integer NX, the number of "space" steps used to divide the 
#    interval [0,L].
#
#    Input, integer NT, the number of time steps.
#
#    Input, real SMAX, the maximum value of S to consider.
#
#    Output, real U(NX-1,NT+1), the value of the European call option.
#
  import numpy as np

  dt = t1 / float ( nt )
  dx = smax / float ( nx )

  a = np.zeros ( nx - 1, dtype = np.float64 )
  b = np.zeros ( nx - 1, dtype = np.float64 )
  c = np.zeros ( nx - 1, dtype = np.float64 )

  for i in range ( 0, nx - 1 ):
    b[i] = 1.0 - r * dt - dt * ( sigma * float ( i + 1 ) ) ** 2

  for i in range ( 0, nx - 2 ):
    c[i] = 0.5 * dt * ( sigma * float ( i + 1 ) ) ** 2 \
      + 0.5 * dt * r * float ( i + 1 )

  for i in range ( 1, nx - 1 ):
    a[i] = 0.5 * dt * ( sigma * float ( i + 1 ) ) ** 2 \
      - 0.5 * dt * r * float ( i + 1 )

  u = np.zeros ( [ nx - 1, nt + 1 ], dtype = np.float64 )

  u0 = 0.0
  for i in range ( 0, nx - 1 ):
    u0 = u0 + dx
    u[i,0] = max ( u0 - e, 0.0 )
  
  for j in range ( 0, nt ):

    t = float ( j ) * t1 / float ( nt )

    p = 0.5 * dt * ( nx - 1 ) * ( sigma * sigma * float ( nx - 1 ) + r ) \
      * ( smax - e * np.exp ( - r * t ) )

    for i in range ( 0, nx - 1 ):
      u[i,j+1] = b[i] * u[i,j]

    for i in range ( 0, nx - 2 ):
      u[i,j+1] = u[i,j+1] + c[i] * u[i+1,j]

    for i in range ( 1, nx - 1 ):
      u[i,j+1] = u[i,j+1] + a[i] * u[i-1,j]

    u[nx-2,j+1] = u[nx-2,j+1] + p

  return u

def forward_test ( ):

#*****************************************************************************80
#
## FORWARD_TEST tests FORWARD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 August 2017
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'FORWARD_TEST:' )
  print ( '  A demonstration of the forward difference method' )
  print ( '  for option valuation.' )

  e = 4.0
  r = 0.03
  sigma = 0.50
  t1 = 1.0
  nx = 11
  nt = 29
  smax = 10.0

  print ( '' )
  print ( '  The exercise price        E =     %g' % ( e ) )
  print ( '  The interest rate         R =     %g' % ( r ) )
  print ( '  The asset volatility      SIGMA = %g' % ( sigma ) )
  print ( '  The expiry date           T1 =    %g' % ( t1 ) )
  print ( '  The number of space steps NX =    %d' % ( nx ) )
  print ( '  The number of time steps  NT =    %d' % ( nt ) )
  print ( '  The value of              SMAX =  %g' % ( smax ) )

  u = forward ( e, r, sigma, t1, nx, nt, smax )

  print ( '' )
  print ( '       Initial          Option' )
  print ( '       Value            Value' )     
  print ( '' )

  smin = 0.0;
  for i in range ( 0, nx - 1 ):
    s = ( float ( nx - i - 2 ) * smin \
        + float (      i + 1 ) * smax ) \
        / float ( nx     - 1 )

    print ( '  %14g  %14g' % ( s, u[i,nt] ) )

  return

def mc ( s0, e, r, sigma, t1, m ):

#*****************************************************************************80
#
## MC uses Monte Carlo valuation on a European call.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    Black-Scholes for Scientific Computing Students,
#    Computing in Science and Engineering,
#    November/December 2004, Volume 6, Number 6, pages 72-79.
#
#  Parameters:
#
#    Input, real S0, the asset price at time 0.
#
#    Input, real E, the exercise price.
#
#    Input, real R, the interest rate.
#
#    Input, real SIGMA, the volatility of the asset.
#
#    Input, real T1, the expiry date.
#
#    Input, integer M, the number of simulations.
#
#    Output, real CONF[2], the estimated range of the valuation.
#
  import numpy as np

  u = np.random.randn ( m )

  svals = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    svals[i] = s0 * np.exp ( ( r - 0.5 * sigma * sigma ) * t1 \
      + sigma * np.sqrt ( t1 ) * u[i] )

  pvals = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    pvals[i] = np.exp ( - r * t1 ) * max ( svals[i] - e, 0.0 )

  pmean = 0.0
  for i in range ( 0, m ):
    pmean = pmean + pvals[i]
  pmean = pmean / float ( m )

  std = 0.0
  for i in range ( 0, m ):
    std = std + ( pvals[i] - pmean ) ** 2
  std = np.sqrt ( std / float ( m - 1 ) )

  width = 1.96 * std / np.sqrt ( float ( m ) )

  conf = np.zeros ( 2, dtype = np.float64 )

  conf[0] = pmean - width
  conf[1] = pmean + width

  return conf

def mc_test ( ):

#*****************************************************************************80
#
## MC_TEST tests MC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'MC_TEST:' )
  print ( '  A demonstration of the Monte Carlo method' )
  print ( '  for option valuation.' )

  s0 = 2.0
  e = 1.0
  r = 0.05
  sigma = 0.25
  t1 = 3.0
  m = 1000000

  print ( '' )
  print ( '  The asset price at time 0, S0    = %f' % ( s0 ) )
  print ( '  The exercise price         E     = %f' % ( e ) )
  print ( '  The interest rate          R     = %f' % ( r ) )
  print ( '  The asset volatility       SIGMA = %f' % ( sigma ) )
  print ( '  The expiry date            T1    = %f' % ( t1 ) )
  print ( '  The number of simulations  M     = %d' % ( m ) )

  conf = mc ( s0, e, r, sigma, t1, m )

  print ( '' )
  print ( '  The confidence interval is [ %f, %f ]' % ( conf[0], conf[1] ) )

  return

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## R8VEC_PRINT_SOME prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    Input, string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec_print_some_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_SOME_TEST tests R8VEC_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1

  print ( '' )
  print ( 'R8VEC_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT_SOME prints some of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  max_print = 10

  r8vec_print_some ( n, a, max_print, '  No more than 10 lines of this vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_write ( filename, n, a ):

#*****************************************************************************80
#
## R8VEC_WRITE writes an R8VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec_write_test ( ):

#*****************************************************************************80
#
## R8VEC_WRITE_TEST tests R8VEC_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8VEC_WRITE, which writes an R8VEC to a file.' )
  filename = 'r8vec_write_test.txt'
  n = 5
  a = np.array ( ( 1.1, 2.2, 3.3, 4.4, 5.5 ) )
  r8vec_write ( filename, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_WRITE_TEST:' )
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

def black_scholes_test ( ):

#*****************************************************************************80
#
## BLACK_SCHOLES_TEST tests the BLACK_SCHOLES library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 August 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BLACK_SCHOLES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the BLACK_SCHOLES library.' )

  asset_path_test ( )
  binomial_test ( )
  bsf_test ( )
  forward_test ( )
  mc_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'BLACK_SCHOLES_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  black_scholes_test ( )
  timestamp ( )
