#! /usr/bin/env python3
#
#  Without this statement, Python will moronically
#  A) decide that some data is integers, and
#  B) conclude that A/B is zero.
#
from __future__ import division

def phi1 ( r, r0 ):

#*****************************************************************************80
#
## PHI1 evaluates the multiquadric radial basis function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Parameters:
#
#    Input, real R(), the radial separation.
#    0 < R.
#
#    Input, real R0, a scale factor.
#
#    Output, real V(), the value of the radial basis function.
#
  import numpy as np

  v = np.sqrt ( r ** 2 + r0 ** 2 )

  return v

def phi1_test ( ):

#*****************************************************************************80
#
## PHI1_TEST tests PHI1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
  import numpy as np

  print ( '' )
  print ( 'PHI1_TEST' )
  print ( '  PHI1 evaluates the multiquadric radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 4.0
  print ( '  R0 = %g' % ( r0 ) )

  v = phi1 ( r, r0 )
  r8vec_print ( nd, v, '  PHI1(R,R0) = sqrt ( R^2 + R0^2 ):' )

  return

def phi2 ( r, r0 ):

#*****************************************************************************80
#
## PHI2 evaluates the inverse multiquadric radial basis function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Parameters:
#
#    Input, real R(), the radial separation.
#    0 < R.
#
#    Input, real R0, a scale factor.
#
#    Output, real V(), the value of the radial basis function.
#
  import numpy as np

  v = 1.0 / np.sqrt ( r ** 2 + r0 ** 2 )

  return v

def phi2_test ( ):

#*****************************************************************************80
#
## PHI2_TEST tests PHI2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
  import numpy as np

  print ( '' )
  print ( 'PHI2_TEST' )
  print ( '  PHI2 evaluates the inverse multiquadric radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 4.0
  print ( '  R0 = %g' % ( r0 ) )

  v = phi2 ( r, r0 )
  r8vec_print ( nd, v, '  PHI2(R,R0) = 1 / sqrt ( R^2 + R0^2 ):' )

  return

def phi3 ( r, r0 ):

#*****************************************************************************80
#
## PHI3 evaluates the thin-plate spline radial basis function.
#
#  Discussion:
#
#    Note that PHI3(R,R0) is negative if R < R0.  Thus, for this basis function,
#    it may be desirable to choose a value of R0 smaller than any possible R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Parameters:
#
#    Input, real R(), the radial separation.
#    0 < R.
#
#    Input, real R0, a scale factor.
#
#    Output, real V(), the value of the radial basis function.
#
  import numpy as np

  n = np.size ( r )
  v = np.zeros ( n )
  for i in range ( 0, n ):
    if ( r[i] != 0.0 ):
      v[i] = r[i] ** 2 * np.log ( r[i] / r0 )

  return v

def phi3_test ( ):

#*****************************************************************************80
#
## PHI3_TEST tests PHI3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
  import numpy as np

  print ( '' )
  print ( 'PHI3_TEST' )
  print ( '  PHI3 evaluates the thin plate spline radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 0.25
  print ( '  R0 = %g' % ( r0 ) )

  v = phi3 ( r, r0 )
  r8vec_print ( nd, v, '  PHI3(R,R0) = thin plate spline):' )

  return

def phi4 ( r, r0 ):

#*****************************************************************************80
#
## PHI4 evaluates the gaussian radial basis function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Parameters:
#
#    Input, real R(), the radial separation.
#    0 < R.
#
#    Input, real R0, a scale factor.
#
#    Output, real V(), the value of the radial basis function.
#
  import numpy as np

  v = np.exp ( - 0.5 * r ** 2 / r0 ** 2 )

  return v

def phi4_test ( ):

#*****************************************************************************80
#
## PHI4_TEST tests PHI4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
  import numpy as np

  print ( '' )
  print ( 'PHI4_TEST' )
  print ( '  PHI2 evaluates the gaussian radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 4
  print ( '  R0 = %g' % ( r0 ) )

  v = phi4 ( r, r0 )
  r8vec_print ( nd, v, '  PHI4(R,R0) = Gaussian:' )

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
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

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

  r8vec_print ( n, x, '  The linspace vector:' )
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

def rbf_interp ( m, nd, xd, r0, phi, w, ni, xi ):

#*****************************************************************************80
#
## RBF_INTERP evaluates a radial basis function interpolant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer ND, the number of data points.
#
#    Input, real XD(M,ND), the data points.
#
#    Input, real R0, a scale factor.  R0 should be larger than the typical
#    separation between points, but smaller than the maximum separation.
#    The value of R0 has a significant effect on the resulting interpolant.
#
#    Input, function V = PHI ( R, R0 ), a function handle to evaluate the radial
#    basis functions.
#
#    Input, real W(ND), the weights, as computed by RBF_WEIGHTS.
#
#    Input, integer NI, the number of interpolation points.
#
#    Input, real XI(NI), the interpolation points.
#
#    Output, real FI(NI), the interpolated values.
#
  import numpy as np

  fi = np.zeros ( ni )
  r = np.zeros ( nd )

  for i in range ( 0, ni ):

    for j in range ( 0, nd ):
      r[j] = np.sqrt ( np.sum ( ( xi[:,i] - xd[:,j] ) ** 2 ) )

    v = phi ( r, r0 )

    fi[i] = np.dot ( v, w )

  return fi

def rbf_interp_1d_test ( ):

#*****************************************************************************80
#
## RBF_INTERP_1D_TEST tests the RBF_INTERP_1D library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from test_interp import p00_data
  from test_interp import p00_data_num
  from test_interp import p00_prob_num

  print ( '' )
  print ( 'RBF_INTERP_1D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the RBF_INTERP_1D library.' )

  phi1_test ( )
  phi2_test ( )
  phi3_test ( )
  phi4_test ( )

  rbf_weight_test ( )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):
#
#  Determine an appropriate value of R0, the spacing parameter.
#
    nd = p00_data_num ( prob )
    xy = p00_data ( prob, 2, nd )
    xd = xy[0,0:nd]
    xd = np.reshape ( xd, nd )
    xmax = max ( xd )
    xmin = min ( xd )
    r0 = ( xmax - xmin ) / float ( nd - 1 )

    rbf_interp_1d_test01 ( prob, phi1, 'phi1', r0 )
    rbf_interp_1d_test01 ( prob, phi2, 'phi2', r0 )
    rbf_interp_1d_test01 ( prob, phi3, 'phi3', r0 )
    rbf_interp_1d_test01 ( prob, phi4, 'phi4', r0 )
#
#  Terminate.
#
  print ( '' )
  print ( 'RBF_INTERP_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rbf_interp_1d_test01 ( prob, phi, phi_name, r0 ):

#*****************************************************************************80
#
## RBF_INTERP_1D_TEST01 tests RBF_INTERP
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the index of the problem.
#
#    Input, function PHI ( R ), a handle for the radial basis function.
#
#    Input, string PHI_NAME, the name of the radial basis function.
#
#    Input, real R0, the scale factor.  Typically, this might be
#    a small multiple of the average distance between points.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from test_interp import p00_data
  from test_interp import p00_data_num

  print ( '' )
  print ( 'RBF_INTERP_1D_TEST01:' )
  print ( '  Interpolate data from TEST_INTERP problem #%d' % ( prob ) )
  print ( '  using radial basis function %s' % ( phi_name ) )
  print ( '  Scale factor R0 = %g' % ( r0 ) )

  m = 1;
  nd = p00_data_num ( prob )
  print ( '  Number of data points = %d' % ( nd ) )

  xy = p00_data ( prob, 2, nd )
  
  xd = np.zeros ( [ 1, nd ] )
  yd = np.zeros ( [ 1, nd ] )

  xd[0,:] = xy[0,0:nd]
# xd = np.reshape ( xd, nd )

  yd[:] = xy[1,0:nd]
  yd = np.reshape ( yd, nd )

  for j in range ( 0, nd ):
    print ( '  %8.4f  %8.4f' % ( xd[0,j], yd[j] ) )

  m = 1
  w = rbf_weight ( m, nd, xd, r0, phi, yd )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = rbf_interp ( m, nd, xd, r0, phi, w, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' \
    % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  xmin = min ( xd[0,:] )
  xmax = max ( xd[0,:] )
  ymin = min ( yd )
  ymax = max ( yd )

  ni = 501
  xi = r8vec_linspace ( ni, xmin, xmax )
  xi = np.reshape ( xi, [1,ni] );
  yi = rbf_interp ( m, nd, xd, r0, phi, w, ni, xi )

  ld = 0.0
  for i in range ( 0, nd - 1 ):
    ld = ld + np.sqrt ( \
        ( ( xd[0,i+1] - xd[0,i] ) / ( xmax - xmin ) ) ** 2 \
      + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2 )
 
  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + np.sqrt ( \
        ( ( xi[0,i+1] - xi[0,i] ) / ( xmax - xmin ) ) ** 2 \
      + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2 )

  print ( '\n' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of polynomial interpolant       = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd[0,:], yd, 'b-', linewidth = 3 )
  plt.plot ( xd[0,:], yd, 'k.', markersize = 20 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Piecewise Linear Interpolant' )
  plt.grid ( True )
  filename = 'p%02d_data.png' % ( prob )
  plt.savefig ( filename )
  print ( '' )
  print ( '  Created plot file "%s".' % ( filename ) )
  plt.show ( block = False )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 101
  xmin = min ( xd[0,:] )
  xmax = max ( xd[0,:] )
  xi = r8vec_linspace ( ni, xmin, xmax )
  xi = np.reshape ( xi, [1,ni] );
  yi = rbf_interp ( m, nd, xd, r0, phi, w, ni, xi )
  plt.plot ( xi[0,:], yi, 'r-', linewidth = 3 )
  plt.plot ( xd[0,:], yd, 'b-', linewidth = 3 )
  plt.plot ( xd[0,:], yd, 'k.', markersize = 20 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Interpolant using RBF basis' )
  plt.grid ( True )
  filename = 'p%02d_%s_poly.png' % ( prob, phi_name )
  plt.savefig ( filename )
  print ( '  Created plot file "%s".' % ( filename ) )
  plt.show ( block = False )

  return

def rbf_weight ( m, nd, xd, r0, phi, fd ):

#*****************************************************************************80
#
## RBF_WEIGHT computes weights for radial basis function interpolation.
#
#  Discussion:
#
#    We assume that there are N (nonsingular) equations in N unknowns.
#
#    However, it should be clear that, if we are willing to do some kind
#    of least squares calculation, we could allow for singularity,
#    inconsistency, or underdetermine systems.  This could be associated
#    with data points that are very close or repeated, a smaller number
#    of data points than function values, or some other ill-conditioning
#    of the system arising from a peculiarity in the point spacing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer ND, the number of data points.
#
#    Input, real XD(M,ND), the data points.
#
#    Input, real R0, a scale factor.  R0 should be larger than the typical
#    separation between points, but smaller than the maximum separation.
#    The value of R0 has a significant effect on the resulting interpolant.
#
#    Input, function V = PHI ( R, R0 ), a function handle to evaluate the radial
#    basis functions.
#
#    Input, real FD(ND), the function values at the data points.
#
#    Output, real W(ND), the weights.
#
  import numpy as np

  a = np.zeros ( [ nd, nd ] )
  r = np.zeros ( nd )

  for i in range ( 0, nd ):

    if ( m == 1 ):

      for j in range ( 0, nd ):
        r[j] = abs ( xd[0,i] - xd[0,j] )

    else:

      for j in range ( 0, nd ):
        d = xd[:,j] - xd[:,i]
        r[j] = np.sqrt ( np.sum ( d ** 2 ) )
      
    v = phi ( r, r0 )
 
    a[i,:] = v.copy ( )

  w = np.linalg.solve ( a, fd )

  return w

def rbf_weight_test ( ):

#*****************************************************************************80
#
## RBF_WEIGHT_TEST tests RBF_WEIGHT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'RBF_WEIGHT_TEST:' )
  print ( '  RBF_WEIGHT computes the weights associated with the' )
  print ( '  data abscissa values XD.' )

  m = 1
  nd = 5
  xd = np.array ( [ [ 0.0, 1.0, 2.0, 3.0, 4.0 ] ] )
  r0 = 1.5
  fd = np.array ( [ 0.0, 1.0, 4.0, 9.0, 16.0 ] )

  w = rbf_weight ( m, nd, xd, r0, phi1, fd )
 
  r8vec_print ( nd, w, '  Weights:' )

  return w

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
  rbf_interp_1d_test ( )
  timestamp ( )
