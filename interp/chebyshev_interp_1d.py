#! /usr/bin/env python3
#
def chebyshev_coef_1d ( nd, xd, yd ):

#*****************************************************************************80
#
## CHEBYSHEV_COEF_1D determines the Chebyshev interpolant coefficients.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data points.
#    ND must be at least 1.
#
#    Input, real XD(ND), the data locations.
#
#    Input, real YD(ND), the data values.
#
#    Output, real C(ND), the Chebyshev coefficients.
#
#    Output, real XMIN, XMAX, the interpolation interval.
#
  import numpy as np

  if ( nd == 1 ):
    c = 1.0
    xmin = xd[0]
    xmax = xd[0]
    return c, xmin, xmax

  xmin = min ( xd )
  xmax = max ( xd )
#
#  Map XD to [-1,+1].
#
  x = ( 2.0 * xd - xmin - xmax ) / ( xmax - xmin )
#
#  Form the Chebyshev Vandermonde matrix.
#
  a = np.outer ( np.arccos ( x ), np.arange ( 0, nd ) )
  a = np.cos ( a )
#
#  Solve for the expansion coefficients.
#
  c = np.linalg.solve ( a, yd )

  return c, xmin, xmax

def chebyshev_interp_1d ( nd, xd, yd, ni, xi ):

#*****************************************************************************80
#
## CHEBYSHEV_INTERP_1D determines and evaluates the Chebyshev interpolant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data points.
#    ND must be at least 1.
#
#    Input, real XD(ND), the data locations.
#
#    Input, real YD(ND), the data values.
#
#    Input, integer NI, the number of interpolation points.
#
#    Input, real XI(NI), the interpolation points, which
#    must be each be in the interval [ min(XD), max(XD)].
#
#    Output, real YI(NI), the interpolated values.
#
  c, xmin, xmax = chebyshev_coef_1d ( nd, xd, yd )

  yi = chebyshev_value_1d ( nd, c, xmin, xmax, ni, xi )

  return yi

def chebyshev_interp_1d_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV_INTERP_1D_TEST tests the CHEBYSHEV_INTERP_1D library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBYSHEV_INTERP_1D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CHEBYSHEV_INTERP_1D library.' )

  r8vec_linspace_test ( )

  prob_num = p00_prob_num ( )
  for prob in range ( 1, prob_num + 1 ):
    chebyshev_interp_1d_test01 ( prob )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBYSHEV_INTERP_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def chebyshev_interp_1d_test01 ( prob ):

#*****************************************************************************80
#
## CHEBYSHEV_INTERP_1D_TEST01 tests CHEBYSHEV_VALUE_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2017
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'CHEBYSHEV_INTERP_1D_TEST01:' )
  print ( '  Interpolate data from TEST_INTERP problem #%d.' % ( prob ) )

  nd = p00_data_num ( prob )
  print ( '  Number of data points = %d' % ( nd ) )

  xy = p00_data ( prob, 2, nd )
  
  xd = xy[0,0:nd]
  yd = xy[1,0:nd]

  r8vec2_print ( nd, xd, yd, '  X and Y data values:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = chebyshev_interp_1d ( nd, xd, yd, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  xmin = min ( xd )
  xmax = max ( xd )
  ymin = min ( yd )
  ymax = max ( yd )

  ni = 501
  xi = r8vec_linspace ( ni, xmin, xmax )
  yi = chebyshev_interp_1d ( nd, xd, yd, ni, xi )

  ld = 0.0
  for i in range ( 0, nd - 1 ):
    ld = ld + np.sqrt ( \
        ( ( xd[i+1] - xd[i] ) / ( xmax - xmin ) ) ** 2 \
      + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2 )
 
  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + np.sqrt ( \
        ( ( xi[i+1] - xi[i] ) / ( xmax - xmin ) ) ** 2 \
      + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2 )

  print ( '\n' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of polynomial interpolant       = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd, yd, 'b-', linewidth = 3 )
  plt.plot ( xd, yd, 'k.', markersize = 20 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Piecewise Linear Interpolant' )
  plt.grid ( True )
  filename = 'p%02d_data.png' % ( prob )
  plt.savefig ( filename )
  print ( '' )
  print ( '  Created plot file "%s".' % ( filename ) )
# plt.show ( )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 101
  xmin = min ( xd )
  xmax = max ( xd )
  xi = r8vec_linspace ( ni, xmin, xmax )
  yi = chebyshev_interp_1d ( nd, xd, yd, ni, xi )
  plt.plot ( xi, yi, 'r-', linewidth = 3 )
  plt.plot ( xd, yd, 'b-', linewidth = 3 )
  plt.plot ( xd, yd, 'k.', markersize = 20 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Polynomial Interpolant using Lagrange' )
  plt.grid ( True )
  filename = 'p%02d_poly.png' % ( prob )
  plt.savefig ( filename )
  print ( '  Created plot file "%s".' % ( filename ) )
# plt.show ( )

  return

def chebyshev_value_1d ( nd, c, xmin, xmax, ni, xi ):

#*****************************************************************************80
#
## CHEBYSHEV_VALUE_1D evaluates a Chebyshev interpolant, given its coefficients.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data points.
#    ND must be at least 1.
#
#    Input, real C(ND), the Chebyshev coefficients.
#
#    Output, real XMIN, XMAX, the interpolation interval.
#
#    Input, integer NI, the number of interpolation points.
#
#    Input, real XI(NI), the interpolation points, which
#    must be each be in the interval [XMIN,XMAX].
#
#    Output, real YI(NI), the interpolated values.
#
  import numpy as np

  if ( nd == 1 ):
    yi = c.copy ( )
    return yi
#
#  Map XI to [-1,+1].
#
  x = ( 2.0 * xi - xmin - xmax ) / ( xmax - xmin )

  a = np.outer ( np.arccos ( x ), np.arange ( 0, nd ) )
  a = np.cos ( a )

  yi = np.dot ( a, c )

  return yi

def r8vec_linspace ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_LINSPACE creates a column vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    While MATLAB has the built in command 
#
#      x = linspace ( a, b, n )
#
#    that command has the distinct disadvantage of returning a ROW vector.
#
#    4 points evenly spaced between 0 and 12 will yield 0, 4, 8, 12.
#
#    In other words, the interval is divided into N-1 even subintervals,
#    and the endpoints of intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the first and last entries.
#
#    Output, real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):
     x[i] = ( ( n - 1 - i ) * a \
            + (         i ) * b ) \
            / ( n - 1     )
 
  return x

def r8vec_linspace_test ( ):

#*****************************************************************************80
#
## R8VEC_LINSPACE_TEST tests R8VEC_LINSPACE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_LINSPACE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_LINSPACE returns evenly spaced values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_LINSPACE_TEST' )
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

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_data_num ( prob ):

#*****************************************************************************80
#
## P00_DATA_NUM returns the number of data points for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Output, integer DATA_NUM, the number of data points.
#
  from sys import exit

  if ( prob == 1 ):
    data_num = p01_data_num ( )
  elif ( prob == 2 ):
    data_num = p02_data_num ( )
  elif ( prob == 3 ):
    data_num = p03_data_num ( )
  elif ( prob == 4 ):
    data_num = p04_data_num ( )
  elif ( prob == 5 ):
    data_num = p05_data_num ( )
  elif ( prob == 6 ):
    data_num = p06_data_num ( )
  elif ( prob == 7 ):
    data_num = p07_data_num ( )
  elif ( prob == 8 ):
    data_num = p08_data_num ( )
  else:
    print ( '' )
    print ( 'P00_DATA_NUM - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_DATA_NUM - Fatal error!' )

  return data_num

def p01_data_num ( ):

#*****************************************************************************80
#
## P01_DATA_NUM returns the number of data points for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 18

  return data_num

def p02_data_num ( ):

#*****************************************************************************80
#
## P02_DATA_NUM returns the number of data points for problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 18

  return data_num

def p03_data_num ( ):

#*****************************************************************************80
#
## P03_DATA_NUM returns the number of data points for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 11

  return data_num

def p04_data_num ( ):

#*****************************************************************************80
#
## P04_DATA_NUM returns the number of data points for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 8

  return data_num

def p05_data_num ( ):

#*****************************************************************************80
#
## P05_DATA_NUM returns the number of data points for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 9

  return data_num

def p06_data_num ( ):

#*****************************************************************************80
#
## P06_DATA_NUM returns the number of data points for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 49

  return data_num

def p07_data_num ( ):

#*****************************************************************************80
#
## P07_DATA_NUM returns the number of data points for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 4

  return data_num

def p08_data_num ( ):

#*****************************************************************************80
#
## P08_DATA_NUM returns the number of data points for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 12

  return data_num

def p00_data_num_test ( ):

#*****************************************************************************80
#
## P00_DATA_NUM_TEST tests P00_DATA_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_DATA_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_DATA_NUM returns the number of data points for any problem.' )
  print ( '' )
  print ( '  Problem   Data Num' )
  print ( '' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    data_num = p00_data_num ( prob )

    print ( '  %7d  %9d' % ( prob, data_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_DATA_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_data ( prob, dim_num, data_num ):

#*****************************************************************************80
#
## P00_DATA returns the data for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  from sys import exit

  if ( prob == 1 ):
    p_data = p01_data ( dim_num, data_num )
  elif ( prob == 2 ):
    p_data = p02_data ( dim_num, data_num )
  elif ( prob == 3 ):
    p_data = p03_data ( dim_num, data_num )
  elif ( prob == 4 ):
    p_data = p04_data ( dim_num, data_num )
  elif ( prob == 5 ):
    p_data = p05_data ( dim_num, data_num )
  elif ( prob == 6 ):
    p_data = p06_data ( dim_num, data_num )
  elif ( prob == 7 ):
    p_data = p07_data ( dim_num, data_num )
  elif ( prob == 8 ):
    p_data = p08_data ( dim_num, data_num )
  else:
    print ( '' )
    print ( 'P00_DATA - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_DATA - Fatal error!' )

  return p_data

def p01_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P01_DATA returns the data for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
    [  0.0, 4.0 ], \
    [  1.0, 5.0 ], \
    [  2.0, 6.0 ], \
    [  4.0, 6.0 ], \
    [  5.0, 5.0 ], \
    [  6.0, 3.0 ], \
    [  7.0, 1.0 ], \
    [  8.0, 1.0 ], \
    [  9.0, 1.0 ], \
    [ 10.0, 3.0 ], \
    [ 11.0, 4.0 ], \
    [ 12.0, 4.0 ], \
    [ 13.0, 3.0 ], \
    [ 14.0, 3.0 ], \
    [ 15.0, 4.0 ], \
    [ 16.0, 4.0 ], \
    [ 17.0, 3.0 ], \
    [ 18.0, 0.0 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p02_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P02_DATA returns the data for problem p02.
#
#  Discussion:
#
#    Two pairs of identical X values have now been slightly separated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [  0.00,   0.00 ], \
   [  1.34,   5.00 ], \
   [  5.00,   8.66 ], \
   [ 10.00,  10.00 ], \
   [ 10.60,  10.40 ], \
   [ 10.70,  12.00 ], \
   [ 10.705, 28.60 ], \
   [ 10.80,  30.20 ], \
   [ 11.40,  30.60 ], \
   [ 19.60,  30.60 ], \
   [ 20.20,  30.20 ], \
   [ 20.295, 28.60 ], \
   [ 20.30,  12.00 ], \
   [ 20.40,  10.40 ], \
   [ 21.00,  10.00 ], \
   [ 26.00,   8.66 ], \
   [ 29.66,   5.00 ], \
   [ 31.00,   0.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p03_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P03_DATA returns the data for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
    [  0.0,  0.0 ], \
    [  2.0, 10.0 ], \
    [  3.0, 10.0 ], \
    [  5.0, 10.0 ], \
    [  6.0, 10.0 ], \
    [  8.0, 10.0 ], \
    [  9.0, 10.5 ], \
    [ 11.0, 15.0 ], \
    [ 12.0, 50.0 ], \
    [ 14.0, 60.0 ], \
    [ 15.0, 85.0 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p04_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P04_DATA returns the data for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ 0.00,  0.00 ], \
   [ 0.05,  0.70 ], \
   [ 0.10,  1.00 ], \
   [ 0.20,  1.00 ], \
   [ 0.80,  0.30 ], \
   [ 0.85,  0.05 ], \
   [ 0.90,  0.10 ], \
   [ 1.00,  1.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p05_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P05_DATA returns the data for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
    [ 0.00, 0.00 ], \
    [ 0.10, 0.90 ], \
    [ 0.20, 0.95 ], \
    [ 0.30, 0.90 ], \
    [ 0.40, 0.10 ], \
    [ 0.50, 0.05 ], \
    [ 0.60, 0.05 ], \
    [ 0.80, 0.20 ], \
    [ 1.00, 1.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p06_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P06_DATA returns the data for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ 595.0, 0.644 ], \
   [ 605.0, 0.622 ], \
   [ 615.0, 0.638 ], \
   [ 625.0, 0.649 ], \
   [ 635.0, 0.652 ], \
   [ 645.0, 0.639 ], \
   [ 655.0, 0.646 ], \
   [ 665.0, 0.657 ], \
   [ 675.0, 0.652 ], \
   [ 685.0, 0.655 ], \
   [ 695.0, 0.644 ], \
   [ 705.0, 0.663 ], \
   [ 715.0, 0.663 ], \
   [ 725.0, 0.668 ], \
   [ 735.0, 0.676 ], \
   [ 745.0, 0.676 ], \
   [ 755.0, 0.686 ], \
   [ 765.0, 0.679 ], \
   [ 775.0, 0.678 ], \
   [ 785.0, 0.683 ], \
   [ 795.0, 0.694 ], \
   [ 805.0, 0.699 ], \
   [ 815.0, 0.710 ], \
   [ 825.0, 0.730 ], \
   [ 835.0, 0.763 ], \
   [ 845.0, 0.812 ], \
   [ 855.0, 0.907 ], \
   [ 865.0, 1.044 ], \
   [ 875.0, 1.336 ], \
   [ 885.0, 1.881 ], \
   [ 895.0, 2.169 ], \
   [ 905.0, 2.075 ], \
   [ 915.0, 1.598 ], \
   [ 925.0, 1.211 ], \
   [ 935.0, 0.916 ], \
   [ 945.0, 0.746 ], \
   [ 955.0, 0.672 ], \
   [ 965.0, 0.627 ], \
   [ 975.0, 0.615 ], \
   [ 985.0, 0.607 ], \
   [ 995.0, 0.606 ], \
   [1005.0, 0.609 ], \
   [1015.0, 0.603 ], \
   [1025.0, 0.601 ], \
   [1035.0, 0.603 ], \
   [1045.0, 0.601 ], \
   [1055.0, 0.611 ], \
   [1065.0, 0.601 ], \
   [1075.0, 0.608 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p07_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P07_DATA returns the data for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ 0.0, 1.0 ], \
   [ 1.0, 2.0 ], \
   [ 4.0, 2.0 ], \
   [ 5.0, 1.0 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p08_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P08_DATA returns the data for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ -1.0, 1.00 ], \
   [ -0.8, 0.64 ], \
   [ -0.6, 0.36 ], \
   [ -0.4, 0.16 ], \
   [ -0.2, 0.04 ], \
   [  0.0, 0.00 ], \
   [  0.2, 0.04 ], \
   [  0.20001, 0.05 ], \
   [  0.4, 0.16 ], \
   [  0.6, 0.36 ], \
   [  0.8, 0.64 ], \
   [  1.0, 1.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p00_data_test ( ):

#*****************************************************************************80
#
## P00_DATA_TEST tests P00_DATA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_DATA_TEST tests P00_DATA' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_DATA returns the actual (MxN) data for any problem.' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem %d' % ( prob ) )

    data_num = p00_data_num ( prob )
    print ( '  DATA_NUM = %d' % ( data_num ) )

    dim_num = p00_dim_num ( prob )
    print ( '  DIM_NUM  = %d' % ( dim_num ) )

    p = p00_data ( prob, dim_num, data_num )

    r8mat_transpose_print ( dim_num, data_num, p, '  Data array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_DATA_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_dim_num ( prob ):

#*****************************************************************************80
#
## P00_DIM_NUM returns the spatial dimension for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  if ( prob == 1 ):
    dim_num = p01_dim_num ( )
  elif ( prob == 2 ):
    dim_num = p02_dim_num ( )
  elif ( prob == 3 ):
    dim_num = p03_dim_num ( )
  elif ( prob == 4 ):
    dim_num = p04_dim_num ( )
  elif ( prob == 5 ):
    dim_num = p05_dim_num ( )
  elif ( prob == 6 ):
    dim_num = p06_dim_num ( )
  elif ( prob == 7 ):
    dim_num = p07_dim_num ( )
  elif ( prob == 8 ):
    dim_num = p08_dim_num ( )
  else:
    print ( '' )
    print ( 'P00_DIM_NUM - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_DIM_NUM - Fatal error!' )

  return dim_num

def p01_dim_num ( ):

#*****************************************************************************80
#
## P01_DIM_NUM returns the spatial dimension for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p02_dim_num ( ):

#*****************************************************************************80
#
## P02_DIM_NUM returns the spatial dimension for problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p03_dim_num ( ):

#*****************************************************************************80
#
## P03_DIM_NUM returns the spatial dimension for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p04_dim_num ( ):

#*****************************************************************************80
#
## P04_DIM_NUM returns the spatial dimension for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p05_dim_num ( ):

#*****************************************************************************80
#
## P05_DIM_NUM returns the spatial dimension for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p06_dim_num ( ):

#*****************************************************************************80
#
## P06_DIM_NUM returns the spatial dimension for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p07_dim_num ( ):

#*****************************************************************************80
#
## P07_DIM_NUM returns the spatial dimension for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p08_dim_num ( ):

#*****************************************************************************80
#
## P08_DIM_NUM returns the spatial dimension for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p00_dim_num_test ( ):

#*****************************************************************************80
#
## P00_DIM_NUM_TEST tests P00_DIM_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_DIM_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_DIM_NUM returns the spatial dimension for any problem.' )
  print ( '' )
  print ( '  Problem  Dimension' )
  print ( '' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    dim_num = p00_dim_num ( prob )

    print ( '  %7d  %9d' % ( prob, dim_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_DIM_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_plot ( prob ):

#*****************************************************************************80
#
## P00_PLOT plots the data for any of the tests.
#
#  Discussion:
#
#    For now we assume that the data dimension is 2, so that we are simply
#    creating a single X-Y plot.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from sys import exit

  prob_num = p00_prob_num

  if ( prob < 1 or prob_num < prob ):
    print ( '' )
    print ( 'P00_PLOT - Fatal error!' )
    print ( '  Values of PROB must be between 1 and %d.' % ( prob_num ) )
    exit ( 'P00_PLOT - Fatal error!' )

  data_num = p00_data_num ( prob )

  dim_num = p00_dim_num ( prob )
 
  p = p00_data ( prob, dim_num, data_num )

  x = p[0,:]
  y = p[1,:]

  t = 'TEST_INTERP Data Set #' + str ( prob )
  filename = 'p0' + str ( prob ) + '_plot.png'
#
#  PYLAB commands.
#
  plt.plot ( x, y, linewidth = 2.0 )
  plt.plot ( x, y, 'r.', markersize = 25 )
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )

  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename, '"' );
# plt.show ( )
  plt.clf ( )

  return filename

def p00_plot_test ( ):

#*****************************************************************************80
#
## P00_PLOT_TEST tests P00_PLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_PLOT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_PLOT plots any test problem.' )

  num = p00_prob_num ( )
  print ( '' )
  print ( '  TEST_INTERP includes %d test problems.' % ( num ) )

  print ( '' )
  for prob in range ( 1, num + 1 ):
    filename = p00_plot ( prob )
    print ( '  #%d  "%s"' % ( prob, filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PLOT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_prob_num ( ):

#*****************************************************************************80
#
## P00_PROB_NUM returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer VALUE, the number of problems.
#
  value = 8

  return value

def p00_prob_num_test ( ):

#*****************************************************************************80
#
## P00_PROB_NUM_TEST tests P00_PROB_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_PROB_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_PROB_NUM returns the number of test problems.' )

  num = p00_prob_num ( )

  print ( '' )
  print ( '  TEST_INTERP includes %d test problems.' % ( num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PROB_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_story ( prob ):

#*****************************************************************************80
#
## P00_STORY prints the "story" for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  from sys import exit

  if ( prob == 1 ):
    p01_story ( )
  elif ( prob == 2 ):
    p02_story ( )
  elif ( prob == 3 ):
    p03_story ( )
  elif ( prob == 4 ):
    p04_story ( )
  elif ( prob == 5 ):
    p05_story ( )
  elif ( prob == 6 ):
    p06_story ( )
  elif ( prob == 7 ):
    p07_story ( )
  elif ( prob == 8 ):
    p08_story ( )
  else:
    print ( '' )
    print ( 'P00_STORY - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_STORY - Fatal error!' )

  return

def p01_story ( ):

#*****************************************************************************80
#
## P01_STORY prints the "story" for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hans-Joerg Wenz,
#    Interpolation of Curve Data by Blended Generalized Circles,
#    Computer Aided Geometric Design,
#    Volume 13, Number 8, November 1996, pages 673-680.
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This example is due to Hans-Joerg Wenz.' )
  print ( '  It is an example of good data, which is dense enough in areas' )
  print ( '  where the expected curvature of the interpolant is large.' )
  print ( '  Good results can be expected with almost any reasonable' )
  print ( '  interpolation method.' )

  return

def p02_story ( ):

#*****************************************************************************80
#
## P02_STORY prints the "story" for problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    ETY Lee,
#    Choosing Nodes in Parametric Curve Interpolation,
#    Computer-Aided Design,
#    Volume 21, Number 6, July/August 1989, pages 363-370.
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This example is due to ETY Lee of Boeing.' )
  print ( '  Data near the corners is more dense than in regions of small curvature.' )
  print ( '  A local interpolation method will produce a more plausible' )
  print ( '  interpolant than a nonlocal interpolation method, such as' )
  print ( '  cubic splines.' )

  return

def p03_story ( ):

#*****************************************************************************80
#
## P03_STORY prints the "story" for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This example is due to Fred Fritsch and Ralph Carlson.' )
  print ( '  This data can cause problems for interpolation methods.' )
  print ( '  There are sudden changes in direction, and at the same time,' )
  print ( '  sparsely-placed data.  This can cause an interpolant to overshoot' )
  print ( '  the data in a way that seems implausible.' )

  return

def p04_story ( ):

#*****************************************************************************80
#
## P04_STORY prints the "story" for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Larry Irvine, Samuel Marin, Philip Smith,
#    Constrained Interpolation and Smoothing,
#    Constructive Approximation,
#    Volume 2, Number 1, December 1986, pages 129-151.
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This example is due to Larry Irvine, Samuel Marin and Philip Smith.' )
  print ( '  This data can cause problems for interpolation methods.' )
  print ( '  There are sudden changes in direction, and at the same time,' )
  print ( '  sparsely-placed data.  This can cause an interpolant to overshoot' )
  print ( '  the data in a way that seems implausible.' )

  return

def p05_story ( ):

#*****************************************************************************80
#
## P05_STORY prints the "story" for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Larry Irvine, Samuel Marin, Philip Smith,
#    Constrained Interpolation and Smoothing,
#    Constructive Approximation,
#    Volume 2, Number 1, December 1986, pages 129-151.
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This example is due to Larry Irvine, Samuel Marin and Philip Smith.' )
  print ( '  This data can cause problems for interpolation methods.' )
  print ( '  There are sudden changes in direction, and at the same time,' )
  print ( '  sparsely-placed data.  This can cause an interpolant to overshoot' )
  print ( '  the data in a way that seems implausible.' )

  return

def p06_story ( ):

#*****************************************************************************80
#
## P06_STORY prints the "story" for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl DeBoor, John Rice,
#    Least-squares cubic spline approximation II - variable knots.
#    Technical Report CSD TR 21,
#    Purdue University, Lafayette, Indiana, 1968.
#
#    Carl DeBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  The data is due to Carl deBoor and John Rice.' )
  print ( '  The data represents a temperature dependent property of titanium.' )
  print ( '  The data has been used extensively as an example in spline' )
  print ( '  approximation with variably-spaced knots.' )
  print ( '  DeBoor considers two sets of knots:' )
  print ( '  (595,675,755,835,915,995,1075)' )
  print ( '  and' )
  print ( '  (595,725,850,910,975,1040,1075).' )

  return

def p07_story ( ):

#*****************************************************************************80
#
## P07_STORY prints the "story" for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This data is a simple symmetric set of 4 points,' )
  print ( '  for which it is interesting to develop the Shepard' )
  print ( '  interpolants for varying values of the exponent p.' )

  return

def p08_story ( ):

#*****************************************************************************80
#
## P08_STORY prints the "story" for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( '  This is equally spaced data for y = x^2,' )
  print ( '  except for one extra point whose x value is' )
  print ( '  close to another, but whose y value is not so close.' )
  print ( '  A small disagreement in nearby data can be a disaster.' )
  return

def p00_story_test ( ):

#*****************************************************************************80
#
## P00_STORY_TEST tests P00_STORY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_STORY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_STORY prints the "story" for any problem.' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem %d' % ( prob ) )

    p00_story ( prob )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_STORY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
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
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def test_interp_test ( ):

#*****************************************************************************80
#
## TEST_INTERP_TEST tests the TEST_INTERP library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TEST_INTERP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TEST_INTERP library.' )
#
#  Utility functions.
#
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
#
#  Library functions.
#
  p00_prob_num_test ( )
  p00_story_test ( )
  p00_dim_num_test ( )
  p00_data_num_test ( )
  p00_data_test ( )
  p00_plot_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_INTERP_TEST:' )
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

if ( __name__ == '__main__' ):
  timestamp ( ) 
  chebyshev_interp_1d_test ( )
  timestamp ( )
