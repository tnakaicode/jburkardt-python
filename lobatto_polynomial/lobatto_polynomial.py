#! /usr/bin/env python3
#
def lobatto_polynomial_test ( ):

#*****************************************************************************80
#
## lobatto_polynomial_test() tests lobatto_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lobatto_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lobatto_polynomial().' )

  lobatto_polynomial_value_test ( )
  lobatto_polynomial_plot_test ( )
  lobatto_polynomial_derivative_test ( )
  lobatto_polynomial_derivative_plot_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lobatto_polynomial_test():' )
  print ( '  Normal end of execution.' )

  return

def lobatto_polynomial_derivative ( m, n, x ):

#*****************************************************************************80
#
## lobatto_polynomial_derivative(): derivative of completed Lobatto polynomial.
#
#  Discussion:
#
#    L(N,X)  =  N * ( P(N-1,X) - X * P(N,X) ) 
#    L'(N,X) =  N * ( P'(N-1,X) - P(N,X) - X * P'(N,X) )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 August 2023
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
#    Larry Andrews,
#    Special Functions of Mathematics for Engineers,
#    Second Edition,
#    Oxford University Press, 1998,
#    ISBN: 0819426164,
#    LC: QA351.A75.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real LP[M,N+1], the derivative of the completed Lobatto
#    polynomials of order 1 through N at the point X.
#
  import numpy as np

  lp = np.zeros ( [ m, n + 1 ] )

  if ( 1 <= n ):

    lp[:,1] = - 2.0 * x[:]

    if ( 2 <= n ):

      p = np.zeros ( [ m, n + 1 ] )
      p[:,0] = 1.0
      p[:,1] = x[:]
      for j in range ( 2, n + 1 ):
        p[:,j] = ( ( 2 * j - 1 ) * x[:] * p[:,j-1]   \
                 - (     j - 1 ) *        p[:,j-2] ) \
                 / (     j     )

      pp = np.zeros ( [ m, n + 1 ] )
      pp[:,0] = 0.0
      pp[:,1] = 1.0
      for j in range ( 2, n + 1 ):
        pp[:,j] = ( ( 2 * j - 1 ) * ( p[:,j-1] + x[:] * pp[:,j-1] )   \
                  - (     j - 1 ) *                     pp[:,j-2] ) \
                  / (     j     )

      for j in range ( 2, n + 1 ):
        lp[:,j] = \
          j * ( pp[:,j-1] - p[:,j] - x[:] * pp[:,j] )

  return lp

def lobatto_polynomial_derivative_plot ( index, filename ):

#*****************************************************************************80
#
## lobatto_polynomial_derivative_plot() plots Lobatto polynomial derivatives.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index(*): the orders of the polynomials to be plotted.
#
#    string filename: a filename for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np

  m = 501
  x = np.linspace ( -1.0, +1.0, m )
  index_num = len ( index )

  plt.clf ( )
  plt.plot ( np.array ( [-1.0,+1.0] ), np.array ( [0.0,0.0] ), \
    'k-', linewidth = 2 )
  for i in range ( 0, index_num ):
    n = index[i]
    y = lobatto_polynomial_derivative ( m, n, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Lo''(n,x) --->' )
  plt.title ( 'Completed Lobatto derivatives Lo''(n,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def lobatto_polynomial_derivative_plot_test ( ):

#*****************************************************************************80
#
## lobatto_polynomial_derivative_plot_test() tests lobatto_polynomial_derivative_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'lobatto_polynomial_derivative_plot_test():' )
  print ( '  lobatto_polynomial_derivative_plot() plots Lobatto polynomial derivativess.' )

  index = np.array ( [ 1, 2, 3, 4, 5, 6, 7 ] )
  filename = 'lobatto_polynomial_derivative.png'

  lobatto_polynomial_derivative_plot ( index, filename )

  return

def lobatto_polynomial_derivative_test ( ):

#*****************************************************************************80
#
## lobatto_polynomial_derivative_test() tests lobatto_polynomial_derivative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 1

  print ( '' )
  print ( 'lobatto_polynomial_derivative_test():' )
  print ( '  lobatto_polynomial_derivatives() stores derivatives of' )
  print ( '  the completed Lobatto polynomial L(n,x).' )
  print ( '  lobatto_polynomial_derivative() evaluates the completed Lobatto polynomial.' )
  print ( '' )
  print ( '                                       Tabulated                 Computed' )
  print ( '     N        X                        L\'(N,X)                   L\'(N,X)       Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = lobatto_polynomial_derivatives ( n_data )

    if ( n_data == 0 ):
      break

    x_vec = np.array ( [ x ] )
    lp = lobatto_polynomial_derivative ( m, n, x_vec )
    fx2 = lp[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12f  %24g  %24g  %8g' % ( n, x, fx1, fx2, e ) )

  return

def lobatto_polynomial_derivatives ( n_data ):

#*****************************************************************************80
#
## lobatto_polynomial_derivatives(): derivatives of completed Lobatto polynomials.
#
#  Discussion:
#
#    In Mathematica, the completed Lobatto polynomial can be evaluated by:
#
#      n * LegendreP [ n - 1, x ] - n * x * LegendreP [ n, x ]
#
#    The derivative is:
#
#        n * D[LegendreP [ n - 1, x ], {x} ] 
#      - n * LegendreP [ n, x ] 
#      - n * x * D[LegendreP [ n, x ], {x}]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2014
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
#    returns the corresponding data when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 31

  fx_vec = np.array ( ( \
     -0.5, \
      2.437500000000000, \
      4.031250000000000, \
     -3.154296875000000, \
    -10.19165039062500, \
     -1.019622802734375, \
     15.67544555664063, \
     10.97668933868408, \
    -15.91419786214828, \
    -24.33202382177114, \
     12.00000000000000, \
      5.670000000000000, \
      0.9600000000000000, \
     -2.310000000000000, \
     -4.320000000000000, \
     -5.250000000000000, \
     -5.280000000000000, \
     -4.590000000000000, \
     -3.360000000000000, \
     -1.770000000000000, \
      0.0, \
      1.770000000000000, \
      3.360000000000000, \
      4.590000000000000, \
      5.280000000000000, \
      5.250000000000000, \
      4.320000000000000, \
      2.310000000000000, \
     -0.9600000000000000, \
     -5.670000000000000, \
    -12.00000000000000 ))

  n_vec = np.array ( ( \
     1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3 ))

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
   -1.00, \
   -0.90, \
   -0.80, \
   -0.70, \
   -0.60, \
   -0.50, \
   -0.40, \
   -0.30, \
   -0.20, \
   -0.10, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def lobatto_polynomial_plot ( index, filename ):

#*****************************************************************************80
#
## lobatto_polynomial_plot() plots one or more completed Lobatto polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index(*): the orders of the polynomials to be plotted.
#
#    string filename: a file name for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np

  m = 501
  x = np.linspace ( -1.0, +1.0, m )
  index_num = len ( index )

  plt.clf ( )
  plt.plot ( np.array ( [-1.0,+1.0] ), np.array ( [0.0,0.0] ), \
    'k-', linewidth = 2 )
  for i in range ( 0, index_num ):
    n = index[i]
    y = lobatto_polynomial_value ( m, n, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Lo(n,x) --->' )
  plt.title ( 'Completed Lobatto polynomials Lo(n,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def lobatto_polynomial_plot_test ( ):

#*****************************************************************************80
#
## lobatto_polynomial_plot_test() tests lobatto_polynomial_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'lobatto_polynomial_plot_test():' )
  print ( '  lobatto_polynomial_plot() plots Lobatto polynomials.' )

  index = np.array ( [ 1, 2, 3, 4, 5, 6, 7 ] )
  filename = 'lobatto_polynomial_value.png'

  lobatto_polynomial_plot ( index, filename )

  return

def lobatto_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## lobatto_polynomial_value() evaluates the completed Lobatto polynomials Lo(n,x).
#
#  Discussion:
#
#    L(N,X) = ( 1 - X^2 ) * P'(N,X)
#           = N * ( P(N-1,X) - X * P(N,X) ) 
#
#    The Lobatto polynomials are 0 at -1 and +1.
#
#    L( 0,x) = (1-x^2) * 0
#    L( 1,x) = (1-x^2) * 1
#    L( 2,x) = (1-x^2) * 3X
#    L( 3,x) = (1-x^2) * ( -3 + 15x^2 ) / 2
#    L( 4,x) = (1-x^2) * ( -60x + 140x^3 ) / 8
#    L( 5,x) = (1-x^2) * ( -15 - 210x^2 + 315x^4 ) / 8
#    L( 6,x) = (1-x^2) * ( 210x - 1260x^3 + 1386x^5 ) / 16
#    L( 7,x) = (1-x^2) * ( -35 + 945x^2 - 3465x^4 + 3003x^6 ) / 16
#    L( 8,x) = (1-x^2) * ( -2520x + 27720x^3 - 72072x^5 + 51480x^7 ) / 128
#    L( 9,x) = (1-x^2) * ( 315 - 13860x^2 + 90090x^4 - 180180x^6 + 109395x^8 ) / 128
#    L(10,x) = (1-x^2) * ( 6930x - 120120x^3 + 540540x^5 - 875160x^7 + 461890x^9 ) / 256
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 August 2023
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
#    Larry Andrews,
#    Special Functions of Mathematics for Engineers,
#    Second Edition,
#    Oxford University Press, 1998,
#    ISBN: 0819426164,
#    LC: QA351.A75.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer m: the number of evaluation points.
#
#    integer n: the highest order polynomial to evaluate.
#
#    real x[m]: the evaluation points.
#
#  Output:
#
#    real l[m,n+1]: the values of the completed Lobatto
#    polynomials of orders up to N at the point X.
#
  import numpy as np

  l = np.zeros ( [ m, n + 1 ] )

  if ( 1 <= n ):

    l[:,1] = ( 1.0 - x[:] ** 2 )

    if ( 2 <= n ):
#
#  Evaluate Legendre polynomials.
#
      p = np.zeros ( [ m, n + 1 ] )
 
      p[:,0] = 1.0
      p[:,1] = x[:]

      for j in range ( 2, n + 1 ):
        p[:,j] = ( ( 2 * j - 1 ) * x[:] * p[:,j-1]   \
                 - (     j - 1 ) *        p[:,j-2] ) \
                 / (     j     )

      for j in range ( 2, n + 1 ):
        l[:,j] = j * ( p[:,j-1] - x[:] * p[:,j] )

  return l


def lobatto_polynomial_values ( n_data ):

#*****************************************************************************80
#
## lobatto_polynomial_values() returns values of the completed Lobatto polynomials.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      n * LegendreP [ n - 1, x ] - n * x * LegendreP [ n, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2013
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
#    returns the corresponding data when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 31

  fx_vec = np.array ( ( \
    0.9375000000000000, \
    0.7031250000000000, \
   -0.9667968750000000, \
   -1.501464843750000, \
    0.3639221191406250, \
    2.001914978027344, \
    0.6597948074340820, \
   -1.934441328048706, \
   -1.769941113889217, \
    1.215243665501475, \
    0.000000000000000, \
    0.8692500000000000, \
    1.188000000000000, \
    1.109250000000000, \
    0.7680000000000000, \
    0.2812500000000000, \
   -0.2520000000000000, \
   -0.7507500000000000, \
   -1.152000000000000, \
   -1.410750000000000, \
   -1.500000000000000, \
   -1.410750000000000, \
   -1.152000000000000, \
   -0.7507500000000000, \
   -0.2520000000000000, \
    0.2812500000000000, \
    0.7680000000000000, \
    1.109250000000000, \
    1.188000000000000, \
    0.8692500000000000, \
    0.000000000000000 ) )

  n_vec = np.array ( ( \
     1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3 ) )

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
   -1.00, \
   -0.90, \
   -0.80, \
   -0.70, \
   -0.60, \
   -0.50, \
   -0.40, \
   -0.30, \
   -0.20, \
   -0.10, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def lobatto_polynomial_value_test ( ):

#*****************************************************************************80
#
## lobatto_polynomial_value_test() tests lobatto_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 1

  print ( '' )
  print ( 'lobatto_polynomial_value_test():' )
  print ( '  lobatto_polynomial_value() evaluates the completed Lobatto polynomial.' )
  print ( '' )
  print ( '                                       Tabulated                 Computed' )
  print ( '     N        X                        L(N,X)                    L(N,X)        Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = lobatto_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    x_vec = np.array ( [ x ] )

    l = lobatto_polynomial_value ( m, n, x_vec )
    fx2 = l[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12f  %24g  %24g  %8g' % ( n, x, fx1, fx2, e ) )

  return

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
  lobatto_polynomial_test ( )
  timestamp ( )

