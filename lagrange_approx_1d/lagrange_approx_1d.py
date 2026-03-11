#! /usr/bin/env python3
#
def lagrange_approx_1d_test ( ):

#*****************************************************************************80
#
## lagrange_approx_1d_test() tests lagrange_approx_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2024
#
#  Author:
#
#    John Burkardt
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_interp_1d' )
  from test_interp_1d import p00_prob_num

  import numpy as np
  import platform

  print ( '' )
  print ( 'lagrange_approx_1d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lagrange_approx_1d().' )
  print ( '  These tests need test_interp_1d.' )

  prob_num = p00_prob_num ( )
  for prob in range ( 1, prob_num + 1 ):
    for m in [ 0, 1, 2, 3, 4, 8, 16 ]:
      for nd in [ 16, 64, 1000 ]:
        lagrange_approx_1d_test02 ( prob, m, nd )

  prob_num = p00_prob_num ( )
  for prob in range ( 1, prob_num + 1 ):
    for m in [ 0, 1, 2, 3, 4, 8, 16 ]:
      for nd in [ 16, 64, 1000 ]:
        lagrange_approx_1d_test03 ( prob, m, nd )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_approx_1d_test():' )
  print ( '  Normal end of execution.' )

  return

def lagrange_approx_1d ( m, nd, xd, yd, ni, xi ):

#*****************************************************************************80
#
## lagrange_approx_1d() evaluates the Lagrange approximant of degree M.
#
#  Discussion:
#
#    The Lagrange approximant L(M,ND,XD,YD)(X) is a polynomial of
#    degree M which approximates the data (XD(I),YD(I)) for I = 1 to ND.
#
#    We can represent any polynomial of degree M+1 as the sum of the Lagrange 
#    basis functions at the M+1 Chebyshev points.
#
#      L(M)(X) = sum ( 1 <= I <= M+1 ) C(I) LB(M,XC)(X)
#
#    Given our data, we can seek the M+1 unknown coefficients C which minimize
#    the norm of | L(M)(XD(1:ND)) - YD(1:ND) |.
#
#    Given the coefficients, we can then evaluate the polynomial at the
#    points XI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the polynomial degree.
#
#    integer ND, the number of data points.
#    ND must be at least 1.
#
#    real XD(ND), the data points.
#
#    real YD(ND), the data values.
#
#    integer NI, the number of interpolation points.
#
#    real XI(NI), the interpolation points.
#
#  Output:
#
#    real YI(NI), the interpolated values.
#
  import numpy as np
#
#  Evaluate the Chebyshev points.
#
  xc = r8vec_cheby_extreme ( m + 1, -1.0, +1.0 )
#
#  Evaluate the Lagrange basis functions for the Chebyshev points 
#  at the data points.
#
  ld = lagrange_basis_1d ( m + 1, xc, nd, xd )
#
#  The value of the Lagrange approximant at each data point should
#  approximate the data value: LD * YC = YD, where YC are the unknown
#  coefficients.
#
  yc, junk1, junk2, junk3 = np.linalg.lstsq ( ld, yd, rcond = 1 )
#
#  Now we want to evaluate the Lagrange approximant at the "interpolant
#  points": LI * YC = YI
#
  li = lagrange_basis_1d ( m + 1, xc, ni, xi )
  yi = np.dot ( li, yc )

  return yi

def lagrange_approx_1d_test02 ( prob, m, nd ):

#*****************************************************************************80
#
## lagrange_approx_1d_test02() tests lagrange_approx_1d() with evenly spaced data
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 August 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer M, the polynomial approximant degree.
#
#    integer ND, the number of data points.
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_interp_1d' )
  from test_interp_1d import p00_f

  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lagrange_approx_1d_test02():' )
  print ( '  Approximate evenly spaced data from problem ', prob )
  print ( '  Use polynomial approximant of degree ', m )
  print ( '  Number of data points = ', nd )

  a = 0.0
  b = 1.0
  xd = np.linspace ( a, b, nd )
  yd = p00_f ( prob, nd, xd )

  if ( nd < 10 ):
    r8vec2_print ( nd, xd, yd, '  Data array:' )
#
#  #1:  Does approximant come close to function at data points?
#
  ni = nd
  xi = xd
  yi = lagrange_approx_1d ( m, nd, xd, yd, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / ni

  print ( '' )
  print ( '  L2 approximation error averaged per data node = ', int_error )
#
#  #2: Plot the piecewise linear interpolant and polynomial approximant.
#
  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_approx_1d ( m, nd, xd, yd, ni, xi )

  plt.clf ( )
  plt.plot ( xd, yd, 'k.', markersize = 30 )
  plt.plot ( xd, yd, 'b-', linewidth = 3 )
  plt.plot ( xi, yi, 'r-', linewidth = 4 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Lagrange/Even Approximant of degree ' + str ( m ) \
    + ' for ' + str ( nd ) + ' nodes' )
  plt.grid ( True )

  filename = 'p' + str ( prob ) + '_lageven_' + str ( m ) + '_' \
    + str ( nd ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def lagrange_approx_1d_test03 ( prob, m, nd ):

#*****************************************************************************80
#
## lagrange_approx_1d_test03() tests lagrange_approx_1d() with Chebyshev spaced data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 August 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer M, the polynomial approximant degree.
#
#    integer ND, the number of data points.
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_interp_1d' )
  from test_interp_1d import p00_f

  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lagrange_approx_1d_test03():' )
  print ( '  Approximate Chebyshev-spaced data from test_interp_1d() problem .', prob )
  print ( '  Use polynomial approximant of degree.', m )
  print ( '  Number of data points =', nd )

  a = 0.0
  b = 1.0
  xd = r8vec_cheby_extreme ( nd, a, b )

  yd = p00_f ( prob, nd, xd )

  if ( nd < 10 ):
    r8vec2_print ( nd, xd, yd, '  Data array:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = lagrange_approx_1d ( m, nd, xd, yd, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / ni

  print ( '' )
  print ( '  L2 approximation error averaged per data node = ', int_error )
#
#  #2: Plot the piecewise linear interpolant and polynomial approximants.
#
  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_approx_1d ( m, nd, xd, yd, ni, xi )

  plt.clf ( )
  plt.plot ( xd, yd, 'k.', markersize = 30 )
  plt.plot ( xd, yd, 'b-', linewidth = 3 )
  plt.plot ( xi, yi, 'r-', linewidth = 4 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Lagrange/Chebyshev Approximant of degree ' + str ( m ) \
    + ' for ' + str ( nd ) + ' nodes' )
  plt.grid ( True )

  filename = 'p' + str ( prob ) + '_lagcheby_' + str ( m ) + '_' \
    + str ( nd ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '".' )

  return

def lagrange_basis_1d ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## lagrange_basis_1d() evaluates a 1D Lagrange basis.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND,1), the interpolation nodes.
#
#    integer NI, the number of evaluation points.
#
#    real XI(NI,1), the evaluation points.
#
#  Output:
#
#    real LB(NI,ND), the value, at the I-th point XI, of the Jth basis function.
#
  import numpy as np

  lb = np.zeros ( [ ni, nd ] )
  
  for i in range ( 0, ni ):
    for j in range ( 0, nd ):
      lb[i,j] = 1.0
      for k in range ( 0, nd ):
        if ( k != j ):
          lb[i,j] = lb[i,j] * ( xi[i] - xd[k]  ) / ( xd[j] - xd[k]  )

  return lb

def r8vec_cheby_extreme ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby_extreme() creates Chebyshev Extreme values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_cheby1space ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby1space() creates a vector of Type 1 Chebyshev values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Type 1 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

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
  lagrange_approx_1d_test ( )
  timestamp ( )
