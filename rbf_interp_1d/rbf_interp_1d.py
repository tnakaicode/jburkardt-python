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
## phi1() evaluates the multiquadric radial basis function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real R(), the radial separation.
#    0 < R.
#
#    real R0, a scale factor.
#
#  Output:
#
#    real V(), the value of the radial basis function.
#
  import numpy as np

  v = np.sqrt ( r ** 2 + r0 ** 2 )

  return v

def phi1_test ( ):

#*****************************************************************************80
#
## phi1_test() tests phi1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'phi1_test():' )
  print ( '  phi1() evaluates the multiquadric radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 4.0
  print ( '  R0 = %g' % ( r0 ) )

  v = phi1 ( r, r0 )
  r8vec_print ( nd, v, '  phi1(R,R0) = sqrt ( R^2 + R0^2 ):' )

  return

def phi2 ( r, r0 ):

#*****************************************************************************80
#
## phi2() evaluates the inverse multiquadric radial basis function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real R(), the radial separation.
#    0 < R.
#
#    real R0, a scale factor.
#
#  Output:
#
#    real V(), the value of the radial basis function.
#
  import numpy as np

  v = 1.0 / np.sqrt ( r ** 2 + r0 ** 2 )

  return v

def phi2_test ( ):

#*****************************************************************************80
#
## phi2_test() tests phi2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'phi2_test():' )
  print ( '  phi2() evaluates the inverse multiquadric radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 4.0
  print ( '  R0 = %g' % ( r0 ) )

  v = phi2 ( r, r0 )
  r8vec_print ( nd, v, '  phi2(R,R0) = 1 / sqrt ( R^2 + R0^2 ):' )

  return

def phi3 ( r, r0 ):

#*****************************************************************************80
#
## phi3() evaluates the thin-plate spline radial basis function.
#
#  Discussion:
#
#    Note that phi3(R,R0) is negative if R < R0.  Thus, for this basis function,
#    it may be desirable to choose a value of R0 smaller than any possible R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real R(), the radial separation.
#    0 < R.
#
#    real R0, a scale factor.
#
#  Output:
#
#    real V(), the value of the radial basis function.
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
## phi3_test() tests phi3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'phi3_test():' )
  print ( '  phi3() evaluates the thin plate spline radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 0.25
  print ( '  R0 = %g' % ( r0 ) )

  v = phi3 ( r, r0 )
  r8vec_print ( nd, v, '  phi3(R,R0) = thin plate spline):' )

  return

def phi4 ( r, r0 ):

#*****************************************************************************80
#
## phi4() evaluates the gaussian radial basis function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real R(), the radial separation.
#    0 < R.
#
#    real R0, a scale factor.
#
#  Output:
#
#    real V(), the value of the radial basis function.
#
  import numpy as np

  v = np.exp ( - 0.5 * r ** 2 / r0 ** 2 )

  return v

def phi4_test ( ):

#*****************************************************************************80
#
## phi4_test() tests phi4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'phi4_test():' )
  print ( '  phi4() evaluates the gaussian radial basis function.' )

  nd = 5

  r = np.array ( [ 1, 2, 3, 4, 5 ] )
  r8vec_print ( nd, r, '  R:' )

  r0 = 4
  print ( '  R0 = %g' % ( r0 ) )

  v = phi4 ( r, r0 )
  r8vec_print ( nd, v, '  phi4(R,R0) = Gaussian:' )

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

  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def rbf_interp ( m, nd, xd, r0, phi, w, ni, xi ):

#*****************************************************************************80
#
## rbf_interp() evaluates a radial basis function interpolant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer ND, the number of data points.
#
#    real XD(M,ND), the data points.
#
#    real R0, a scale factor.  R0 should be larger than the typical
#    separation between points, but smaller than the maximum separation.
#    The value of R0 has a significant effect on the resulting interpolant.
#
#    function V = phi ( R, R0 ), a function handle to evaluate the radial
#    basis functions.
#
#    real W(ND), the weights, as computed by rbf_weightS.
#
#    integer NI, the number of interpolation points.
#
#    real XI(NI), the interpolation points.
#
#  Output:
#
#    real FI(NI), the interpolated values.
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
## rbf_interp_1d_test() tests rbf_interp_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2018
#
#  Author:
#
#    John Burkardt
#
  from test_interp import p00_data
  from test_interp import p00_data_num
  from test_interp import p00_prob_num
  import numpy as np
  import platform

  print ( '' )
  print ( 'rbf_interp_1d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rbf_interp_1d().' )

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
  print ( 'rbf_interp_1d_test:' )
  print ( '  Normal end of execution.' )
  return

def rbf_interp_1d_test01 ( prob, phi, phi_name, r0 ):

#*****************************************************************************80
#
## rbf_interp_1d_test01 tests rbf_interp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the index of the problem.
#
#    function phi ( R ), a handle for the radial basis function.
#
#    string phi_NAME, the name of the radial basis function.
#
#    real R0, the scale factor.  Typically, this might be
#    a small multiple of the average distance between points.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from test_interp import p00_data
  from test_interp import p00_data_num

  print ( '' )
  print ( 'rbf_interp_1d_test01():' )
  print ( '  Interpolate data from test_interp() problem #%d' % ( prob ) )
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
  xi = np.linspace ( xmin, xmax, ni )
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
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 101
  xmin = min ( xd[0,:] )
  xmax = max ( xd[0,:] )
  xi = np.linspace ( xmin, xmax, ni )
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
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rbf_weight ( m, nd, xd, r0, phi, fd ):

#*****************************************************************************80
#
## rbf_weight() computes weights for radial basis function interpolation.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer ND, the number of data points.
#
#    real XD(M,ND), the data points.
#
#    real R0, a scale factor.  R0 should be larger than the typical
#    separation between points, but smaller than the maximum separation.
#    The value of R0 has a significant effect on the resulting interpolant.
#
#    function V = phi ( R, R0 ), a function handle to evaluate the radial
#    basis functions.
#
#    real FD(ND), the function values at the data points.
#
#  Output:
#
#    real W(ND), the weights.
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
## rbf_weight_test() tests rbf_weight().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'rbf_weight_test():' )
  print ( '  rbf_weight() computes the weights associated with the' )
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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  rbf_interp_1d_test ( )
  timestamp ( )
 
