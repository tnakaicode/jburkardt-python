#! /usr/bin/env python3
#
def sine_integral_test ( ):

#*****************************************************************************80
#
## sine_integral_test() tests sine_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sine_integral_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sine_integral().' )

  si_test ( );
  si_plot ( );
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_integral_test():' )
  print ( '  Normal end of execution.' )

  return

def si ( x ):

#*****************************************************************************80
#
## si() computes the sine integral Si(x).
#
#  Discussion:
#
#    The original version of this code seems to assume 0 <= x.
#
#  Licensing:
#
#    This routine is copyrighted by Shanjie Zhang and Jianming Jin.  However,
#    they give permission to incorporate this routine into a user program
#    provided that the copyright is acknowledged.
#
#  Modified:
#
#    26 March 2025
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
#    real x: the argument.
#
#  Output:
#
#    real value: the value of Si(x).
#
  import numpy as np

  p2 = 1.570796326794897
  el = 0.5772156649015329
  eps = 1.0E-15

  xabs = np.abs ( x )
  if ( x < 0.0 ):
    xsign = -1.0
  else:
    xsign = +1.0

  x2 = x * x

  if ( x == 0.0 ):

    value = 0.0

  elif ( xabs <= 16.0 ):

    xr = xabs
    value = xabs
    for k in range ( 1, 41 ):
      xr = -0.5 * xr * ( 2 * k - 1 ) / k / ( 4 * k * k + 4 * k + 1 ) * x2
      value = value + xr
      if ( np.abs ( xr ) < np.abs ( value ) * eps ):
        return xsign * value

  elif ( xabs <= 32.0 ):

    bj = np.zeros ( 101 )
    m = int ( 47.2 + 0.82 * xabs )
    xa1 = 0.0
    xa0 = 1.0E-100
    for k in range ( m, 0, -1 ):
      xa = 4.0 * k * xa0 / xabs - xa1
      bj[k-1] = xa
      xa1 = xa0
      xa0 = xa

    xs = bj[0]
    for k in range ( 2, m, 2 ):
      xs = xs + 2.0 * bj[k]

    bj[0] = bj[0] / xs
    for k in range ( 1, m ):
      bj[k] = bj[k] / xs

    xr = 1.0
    xg1 = bj[0]
    for k in range ( 2, m + 1 ):
      xr = 0.25 * xr * ( 2.0 * k - 3.0 )**2  \
        / ( ( k - 1.0 ) * ( 2.0 * k - 1.0 )**2 ) * xabs
      xg1 = xg1 + bj[k-1] * xr

    xr = 1.0
    xg2 = bj[0]
    for k in range ( 2, m + 1 ):
      xr = 0.25 * xr * ( 2.0 * k - 5.0 )**2 \
        / ( ( k - 1.0 ) * ( 2.0 * k - 3.0 )**2 ) * xabs
      xg2 = xg2 + bj[k-1] * xr

    xcs = np.cos ( xabs / 2.0 )
    xss = np.sin ( xabs / 2.0 )
    value = xsign * ( xabs * xcs * xg1 + 2.0 * xss * xg2 - np.sin ( xabs ) )

  else:

    xr = 1.0
    xf = 1.0
    for k in range ( 1, 10 ):
      xr = -2.0 * xr * k * ( 2 * k - 1 ) / x2
      xf = xf + xr
    xr = 1.0 / xabs
    xg = xr
    for k in range ( 1, 9 ):
      xr = -2.0 * xr * ( 2 * k + 1 ) * k / x2
      xg = xg + xr
    value = xabs * ( p2 - xf * np.cos ( xabs ) / xabs - xg * np.sin ( xabs ) / xabs )

  return value

def si_plot ( ):

#*****************************************************************************80
#
## si_plot() plots si().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'si_plot():' )
  print ( '  si() evaluates the sine integral function.' )

  a = -10.0
  b =  10.0
  nplot = 101
  x = np.linspace ( a, b, nplot )
  y = np.zeros ( nplot )
  for i in range ( 0, nplot ):
    y[i] = si ( x[i] )

  plt.plot ( x, y, 'b-', linewidth = 2 )
  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Si(x) --->' )
  plt.title ( 'The sine integral function' )
  filename = 'si_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def si_test ( ):

#*****************************************************************************80
#
## si_test() tests si().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'si_test():' )
  print ( '  si() evalues the sine integral function.' )
  print ( '' )
  print ( '      X            SI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = si_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = si ( x )

    print ( '  %14.6g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def si_values ( n_data ):

#*****************************************************************************80
#
## si_values() returns some values of the sine integral function.
#
#  Discussion:
#
#    SI(X) = integral ( 0 <= T <= X ) sin ( T ) / T dt
#
#    In Mathematica, the function can be evaluated by:
#
#      SinIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
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
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( \
     0.4931074180430667E+00, \
     0.5881288096080801E+00, \
     0.6812222391166113E+00, \
     0.7720957854819966E+00, \
     0.8604707107452929E+00, \
     0.9460830703671830E+00, \
     0.1108047199013719E+01, \
     0.1256226732779218E+01, \
     0.1389180485870438E+01, \
     0.1505816780255579E+01, \
     0.1605412976802695E+01, \
     0.1778520173443827E+01, \
     0.1848652527999468E+01, \
     0.1833125398665997E+01, \
     0.1758203138949053E+01, \
     0.1654140414379244E+01 ))

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

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
  sine_integral_test ( )
  timestamp ( )

