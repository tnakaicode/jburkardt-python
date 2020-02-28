#! /usr/bin/env python3
#
def lagrange_basis_1d ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## LAGRANGE_BASIS_1D evaluates a 1D Lagrange basis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data points.
#
#    Input, real XD(ND,1), the interpolation nodes.
#
#    Input, integer NI, the number of evaluation points.
#
#    Input, real XI(NI,1), the evaluation points.
#
#    Output, real LB(NI,ND), the value, at the I-th point XI, of the
#    Jth basis function.
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

def lagrange_basis_1d_test ( ):

#*****************************************************************************80
#
## LAGRANGE_BASIS_1D_TEST tests LAGRANGE_BASIS_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 4
  ni = 21

  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
 
  print ( '' )
  print ( 'LAGRANGE_BASIS_1D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAGRANGE_BASIS_1D evaluates the Lagrange 1D basis' )
  print ( '  functions.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  lb = lagrange_basis_1d ( nd, xd, ni, xi )

  r8mat_print ( ni, nd, lb, '  The Lagrange basis functions:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_BASIS_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_interp_1d_test ( ):

#*****************************************************************************80
#
## LAGRANGE_INTERP_1D_TEST tests the LAGRANGE_INTERP_1D library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LAGRANGE_INTERP_1D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the LAGRANGE_INTERP_1D library.' )
#
#  Utility functions.
#
  p00_prob_num_test ( )
  p00_title_test ( )
  p00_f_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_cheby_extreme_test ( )
  r8vec_norm_test ( )
  r8vec_norm_affine_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )
  r8vec2_print_test ( )
#
#  Library functions.
#
  lagrange_basis_1d_test ( )
  lagrange_value_1d_test ( )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    for nd in ( [ 4, 8, 16, 32, 64 ] ):
      lagrange_interp_1d_test01 ( prob, nd )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    for nd in ( [ 4, 8, 16, 32, 64 ] ):
      lagrange_interp_1d_test02 ( prob, nd )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_INTERP_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_interp_1d_test01 ( prob, nd ):

#*****************************************************************************80
#
## LAGRANGE_INTERP_1D_TEST01 tests LAGRANGE_VALUE_1D with evenly spaced data
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'LAGRANGE_INTERP_1D_TEST01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Interpolate data from TEST_INTERP_1D problem #%d.' % ( prob ) )
  print ( '  Use even spacing for data points.' )
  print ( '  Number of data points = %d' % ( nd ) )

  a = 0.0
  b = 1.0
  xd = np.linspace ( a, b, nd )

  yd = p00_f ( prob, nd, xd )

  if ( nd < 10 ):
    r8vec2_print ( nd, xd, yd, '  Data array:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  int_error = r8vec_norm_affine ( ni, yi, yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  ymin = np.min ( yd )
  ymax = np.max ( yd )

  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  ld = 0.0

  for i in range ( 0, nd - 1 ):
    ld = ld + ( ( xd[i+1] - xd[i] ) / ( b - a ) ) ** 2 \
            + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2
  ld = np.sqrt ( ld )

  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + ( ( xi[i+1] - xi[i] ) / ( b - a ) ) ** 2 \
            + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2
  li = np.sqrt ( li )

  print ( '' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of polynomial interpolant       = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xd, yd, 'ro', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Interpolation data at ' + str ( nd ) + ' even nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_dataeven_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.clf ( )

  print ( '' )
  print ( '  Created plot file "%s"' % ( filename ) )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xi, yi, 'r-', linewidth = 4.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Lagrange/Even Polynomial Interpolant for ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_lageven_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_INTERP_1D_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_interp_1d_test02 ( prob, nd ):

#*****************************************************************************80
#
## LAGRANGE_INTERP_1D_TEST02 tests LAGRANGE_VALUE_1D with Chebyshev spaced data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'LAGRANGE_INTERP_1D_TEST02:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Interpolate data from TEST_INTERP_1D problem #%d.' % ( prob ) )
  print ( '  Use Chebyshev spacing for data points.' )
  print ( '  Number of data points = %d' % ( nd ) )

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
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  int_error = r8vec_norm_affine ( ni, yi, yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  ymin = np.min ( yd )
  ymax = np.max ( yd )

  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  ld = 0.0

  for i in range ( 0, nd - 1 ):
    ld = ld + ( ( xd[i+1] - xd[i] ) / ( b - a ) ) ** 2 \
            + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2
  ld = np.sqrt ( ld )

  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + ( ( xi[i+1] - xi[i] ) / ( b - a ) ) ** 2 \
            + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2
  li = np.sqrt ( li )

  print ( '' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of polynomial interpolant       = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xd, yd, 'ro', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Interpolation data at ' + str ( nd ) + ' Chebyshev nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_datacheby_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.clf ( )

  print ( '' )
  print ( '  Created plot file "%s"' % ( filename ) )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xi, yi, 'r-', linewidth = 4.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Lagrange/Chebyshev Polynomial Interpolant for ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_lagcheby_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_INTERP_1D_TEST02:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_value_1d ( nd, xd, yd, ni, xi ):

#*****************************************************************************80
#
## LAGRANGE_VALUE_1D evaluates the Lagrange interpolant.
#
#  Discussion:
#
#    The Lagrange interpolant L(ND,XD,YD)(X) is the unique polynomial of
#    degree ND-1 which interpolates the points (XD(I),YD(I)) for I = 1
#    to ND.
#
#    The Lagrange interpolant can be constructed from the Lagrange basis
#    polynomials.  Given ND distinct abscissas, XD(1:ND), the I-th Lagrange 
#    basis polynomial LB(ND,XD,I)(X) is defined as the polynomial of degree 
#    ND - 1 which is 1 at  XD(I) and 0 at the ND - 1 other abscissas.
#
#    Given data values YD at each of the abscissas, the value of the
#    Lagrange interpolant may be written as
#
#      L(ND,XD,YD)(X) = sum ( 1 <= I <= ND ) LB(ND,XD,I)(X) * YD(I)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
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
#    Input, real XD(ND,1), the data points.
#
#    Input, real YD(ND,1), the data values.
#
#    Input, integer NI, the number of interpolation points.
#
#    Input, real XI(NI,1), the interpolation points.
#
#    Output, real YI(NI,1), the interpolated values.
#
  import numpy as np

  lb = lagrange_basis_1d ( nd, xd, ni, xi )

  yi = np.dot ( lb, yd )

  return yi

def lagrange_value_1d_test ( ):

#*****************************************************************************80
#
## LAGRANGE_VALUE_1D_TEST tests LAGRANGE_VALUE_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 4
  ni = 21
#
#  Values of f(x) = x^3 - 12 x^2 + 39 x -28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
#
  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
  yd = np.array ( [ -28.0, +10.0, -8.0, +162.0 ] )
 
  print ( '' )
  print ( 'LAGRANGE_VALUE_1D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAGRANGE_VALUE_1D evaluates a Lagrange 1D interpolant.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  r8vec2_print ( ni, xi, yi, '  Table of interpolant values:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_VALUE_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_f ( prob, n, x ):

#*****************************************************************************80
#
## P00_F evaluates the function for any problem.
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
#    Input, integer PROB, the number of the desired test problem.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  from sys import exit

  if ( prob == 1 ):
    value = p01_f ( n, x )
  elif ( prob == 2 ):
    value = p02_f ( n, x )
  elif ( prob == 3 ):
    value = p03_f ( n, x )
  elif ( prob == 4 ):
    value = p04_f ( n, x )
  elif ( prob == 5 ):
    value = p05_f ( n, x )
  elif ( prob == 6 ):
    value = p06_f ( n, x )
  elif ( prob == 7 ):
    value = p07_f ( n, x )
  elif ( prob == 8 ):
    value = p08_f ( n, x )
  else:
    print ( '' )
    print ( 'P00_F - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_F - Fatal error!' )

  return value

def p01_f ( n, x ):

#*****************************************************************************80
#
## P01_F evaluates the function for problem p01.
#
#  Discussion:
#
#    Step function.
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
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = 2.0 * np.ones ( n )

  i = ( x <= 1.0 / 3.0 )
  j = ( 4.0 / 5.0 <= x )

  value[i] = -1.0
  value[j] = +1.0

  return value

def p02_f ( n, x ):

#*****************************************************************************80
#
## P02_F evaluates the function for problem p02.
#
#  Discussion:
#
#    Nondifferentiable function.
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
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.zeros ( n )

  i = ( x <= 1.0 / 3.0 )
  j = ( 1.0 / 3.0 < x )

  value[i] = 1.0 - 3.0 * x[i]
  value[j] = 6.0 * x[j] - 2.0

  return value

def p03_f ( n, x ):

#*****************************************************************************80
#
## P03_F evaluates the function for problem p03.
#
#  Discussion:
#
#    Step function.
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
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = x * ( 10.0 * x - 1.0 ) * ( 5.0 * x - 2.0 ) * ( 5.0 * x - 2.0 ) \
    * ( 4 * x - 3.4 ) * ( x - 1.0 )

  return value

def p04_f ( n, x ):

#*****************************************************************************80
#
## P04_F evaluates the function for problem p04.
#
#  Discussion:
#
#    Step function.
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
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.arctan ( 40.0 * x - 15.0 )

  return value

def p05_f ( n, x ):

#*****************************************************************************80
#
## P05_F evaluates the function for problem p05.
#
#  Discussion:
#
#    Step function.
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
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value =       np.cos (  7.0 * x ) \
        + 5.0 * np.cos ( 11.2 * x ) \
        - 2.0 * np.cos ( 14.0 * x ) \
        + 5.0 * np.cos ( 31.5 * x ) \
        + 7.0 * np.cos ( 63.0 * x )

  return value

def p06_f ( n, x ):

#*****************************************************************************80
#
## P06_F evaluates the function for problem p06.
#
#  Discussion:
#
#    f(x) = exp ( - (4 * x - 1)^2 )
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
#  Reference:
#
#    Alan Genz,
#    A Package for Testing Multiple Integration Subroutines,
#    in Numerical Integration: Recent Developments, Software
#    and Applications,
#    edited by Patrick Keast and Graeme Fairweather,
#    D Reidel, 1987, pages 337-340,
#    LC: QA299.3.N38.
#
#  Parameters:
#
#    Input, integer N, the number of points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.exp ( - ( 4.0 * x - 1.0 ) ** 2 )

  return value

def p07_f ( n, x ):

#*****************************************************************************80
#
## P07_F evaluates the function for problem p07.
#
#  Discussion:
#
#    f(x) = exp ( 4 * x ) if x <= 1/2
#           0                  otherwise
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
#  Reference:
#
#    Alan Genz,
#    A Package for Testing Multiple Integration Subroutines,
#    in Numerical Integration: Recent Developments, Software
#    and Applications,
#    edited by Patrick Keast and Graeme Fairweather,
#    D Reidel, 1987, pages 337-340,
#    LC: QA299.3.N38.
#
#  Parameters:
#
#    Input, integer N, the number of points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.zeros ( n )

  i = ( x < 0.5 )

  value[i] = np.exp ( 4.0 * x[i] )

  return value

def p08_f ( n, x ):

#*****************************************************************************80
#
## P08_F evaluates the function for problem p08.
#
#  Discussion:
#
#    This is a famous example, due to Runge.  If equally spaced
#    abscissas are used, the sequence of interpolating polynomials Pn(X)
#    diverges, in the sense that the max norm of the difference
#    between Pn(X) and F(X) becomes arbitrarily large as N increases.
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
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = 1.0 / ( ( 10.0 * ( x - 0.5 ) ) ** 2 + 1.0 )

  return value

def p00_f_test ( ):

#*****************************************************************************80
#
## P00_F_TEST tests P00_F.
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
  print ( 'P00_F_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_F evaluates any function at N points X.' )

  prob_num = p00_prob_num ( )

  n = 11
  a = 0.0
  b = 1.0
  x = np.linspace ( a, b, n )

  print ( '' )

  for prob in range ( 1, prob_num + 1 ):

    y = p00_f ( prob, n, x )
    title = 'X, Y for problem ' + str ( prob )
    r8vec2_print ( n, x, y, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_F_TEST:' )
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
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PROB_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_title ( prob ):

#*****************************************************************************80
#
## P00_TITLE returns the title of any problem.
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
#    Input, integer PROB, the number of the desired test problem.
#
#    Output, string TITLE, the title of the problem.
#
  from sys import exit

  if ( prob == 1 ):
    title = p01_title ( )
  elif ( prob == 2 ):
    title = p02_title ( )
  elif ( prob == 3 ):
    title = p03_title ( )
  elif ( prob == 4 ):
    title = p04_title ( )
  elif ( prob == 5 ):
    title = p05_title ( )
  elif ( prob == 6 ):
    title = p06_title ( )
  elif ( prob == 7 ):
    title = p07_title ( )
  elif ( prob == 8 ):
    title = p08_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_TITLE - Fatal error!' )

  return title

def p01_title ( ):

#*****************************************************************************80
#
## P01_TITLE returns the title of problem p01.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = steps -1/2/1 at [0,1/3], [1/3,4/5], [4/5,1].'

  return title

def p02_title ( ):

#*****************************************************************************80
#
## P02_TITLE returns the title of problem p02.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = (1-3x), x < 1/3 (6x-2) if 1/3 < x'

  return title

def p03_title ( ):

#*****************************************************************************80
#
## P03_TITLE returns the title of problem p03.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = x (10*x-1) (5x-2) (5x-2) (4x-3.4) (x-1)'

  return title

def p04_title ( ):

#*****************************************************************************80
#
## P04_TITLE returns the title of problem p04.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = atan ( 40 * x - 15 )'

  return title

def p05_title ( ):

#*****************************************************************************80
#
## P05_TITLE returns the title of problem p05.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = cos(7*x)+5*cos(11.2*x)-2*cos(14*x)+5*cos(31.5*x)+7*cos(63*x).'

  return title

def p06_title ( ):

#*****************************************************************************80
#
## P06_TITLE returns the title of problem p06.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( - ( 4*x-1 )^2 )'

  return title

def p07_title ( ):

#*****************************************************************************80
#
## P07_TITLE returns the title of problem p07.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( 2 x ) if x < 0.5, 0 otherwise'

  return title

def p08_title ( ):

#*****************************************************************************80
#
## P08_TITLE returns the title of problem p08.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = 1 / ( 1 + ( 10 * (x-1/2) )^2 )'

  return title

def p00_title_test ( ):

#*****************************************************************************80
#
## P00_TITLE_TEST tests P00_TITLE.
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
  print ( 'P00_TITLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_TITLE returns the title of any test problems.' )

  num = p00_prob_num ( )
  print ( '' )
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )

  print ( '' )
  for prob in range ( 1, num + 1 ):
    title = p00_title ( prob )
    print ( '  #%d  "%s"' % ( prob, title ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_TITLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
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
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
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

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
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
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
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

def r8vec_cheby_extreme ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_CHEBY_EXTREME creates Chebyshev Extreme values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
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
#    Output, real X(N), a vector of Chebyshev spaced data.
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

def r8vec_cheby_extreme_test ( ):

#*****************************************************************************80
#
## R8VEC_CHEBY_EXTREME_TEST tests R8VEC_CHEBY_EXTREME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_CHEBY_EXTREME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_CHEBY_EXTREME returns Chebyshev Extreme values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_cheby_extreme ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_CHEBY_EXTREME_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_chebyspace ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_CHEBYSPACE creates a vector of Chebyshev spaced values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
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
#    Output, real X(N), a vector of Chebyshev spaced data.
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

def r8vec_chebyspace_test ( ):

#*****************************************************************************80
#
## R8VEC_CHEBYSPACE_TEST tests R8VEC_CHEBYSPACE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_CHEBYSPACE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_CHEBYSPACE returns Chebyshev spaced values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_chebyspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_CHEBYSPACE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm_affine ( n, v0, v1 ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE returns the affine norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The affine vector L2 norm is defined as:
#
#      R8VEC_NORM_AFFINE(V0,V1) 
#        = sqrt ( sum ( 1 <= I <= N ) ( V1(I) - V0(I) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the vector dimnension.
#
#    Input, real V0(N), the base vector.
#
#    Input, real V1(N), the vector.
#
#    Output, real VALUE, the affine L2 norm.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ): 
    value = value + ( v0[i] - v1[i] ) ** 2
  value =  np.sqrt ( value )

  return value

def r8vec_norm_affine_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE_TEST tests R8VEC_NORM_AFFINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_AFFINE computes the L2 norm of' )
  print ( '  the difference of two R8VECs.' )

  seed = 123456789;

  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  z = np.zeros ( n )
  for i in range ( 0, n ):
    z[i] = x[i] - y[i]

  print ( '' )
  print ( '  R8VEC_NORM_AFFINE(X,Y) = %g' % ( r8vec_norm_affine ( n, x, y ) ) )
  print ( '  R8VEC_NORM (X-Y):        %g' % ( r8vec_norm ( n, z ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
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
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L2 norm is desired.
#
#    Output, real VALUE, the L2 norm of A.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = np.sqrt ( value )

  return value

def r8vec_norm_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_TEST tests R8VEC_NORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM computes the L2 norm of an R8VEC.' )

  n = 10
  seed = 123456789
  a, seed = r8vec_uniform_01 ( n, seed )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm ( n, a )

  print ( '' )
  print ( '  L2 norm = %g' % ( a_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_TEST:' )
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
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647;

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = numpy.zeros ( n );

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

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_AB - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
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
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_AB computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST:' )
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
  lagrange_interp_1d_test ( )
  timestamp ( )


