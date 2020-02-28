#! /usr/bin/env python
#
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
  from lagrange_basis_1d                import lagrange_basis_1d_test
  from lagrange_value_1d                import lagrange_value_1d_test
  from p00_prob_num                     import p00_prob_num
  from p00_prob_num                     import p00_prob_num_test
  from p00_title                        import p00_title_test
  from p00_f                            import p00_f_test
  from r8mat_print                      import r8mat_print_test
  from r8mat_print_some                 import r8mat_print_some_test
  from r8vec_cheby_extreme              import r8vec_cheby_extreme_test
  from r8vec_norm_affine                import r8vec_norm_affine_test
  from r8vec_norm                       import r8vec_norm_test
  from r8vec_print                      import r8vec_print_test
  from r8vec_uniform_ab                 import r8vec_uniform_ab_test
  from r8vec2_print                     import r8vec2_print_test

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
  from lagrange_value_1d import lagrange_value_1d
  from p00_f import p00_f
  from r8vec_norm_affine import r8vec_norm_affine
  from r8vec2_print import r8vec2_print

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
  from lagrange_value_1d import lagrange_value_1d
  from p00_f import p00_f
  from r8vec_cheby_extreme import r8vec_cheby_extreme
  from r8vec_norm_affine import r8vec_norm_affine
  from r8vec2_print import r8vec2_print

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

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lagrange_interp_1d_test ( )
  timestamp ( )

