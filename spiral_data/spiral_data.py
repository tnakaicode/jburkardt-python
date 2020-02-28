#! /usr/bin/env python3
#
def grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi ):

#*****************************************************************************80
#
## GRID_2D returns a regular 2D grid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of X values to use.
#
#    Input, real X_LO, X_HI, the range of X values.
#
#    Input, integer Y_NUM, the number of Y values to use.
#
#    Input, real Y_LO, Y_HI, the range of Y values.
#
#    Output, real X(X_NUM*Y_NUM), Y(X_NUM*Y_NUM), the coordinates of the grid.
#
  import numpy as np

  x = np.zeros ( x_num * y_num )
  y = np.zeros ( x_num * y_num )

  if ( x_num == 1 ):
    xi = ( x_lo + x_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        x[k] = xi
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        xi = ( float ( x_num - i - 1 ) * x_lo   \
             + float (         i     ) * x_hi ) \
             / float ( x_num     - 1 )
        x[k] = xi
        k = k + 1

  if ( y_num == 1 ):
    yj = ( y_lo + y_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      yj = ( float ( y_num - j - 1 ) * y_lo   \
           + float (         j     ) * y_hi ) \
           / float ( y_num     - 1 )
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1

  return x, y

def grid_2d_test ( ):

#*****************************************************************************80
#
## GRID_2D_TEST makes a small 2D grid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GRID_2D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Generate a regular grid.' )

  x_lo = 10.0
  x_hi = 20.0
  x_num = 5

  y_lo = 5.0
  y_hi = 6.0
  y_num = 3

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  print ( '' )
  k = 0
  for j in range ( 0, y_num ):
    for i in range ( 0, x_num):
      print ( '  %2d  %2d  %2d  %14.6f  %14.6f' % ( k, i, j, x[k], y[k] ) )
      k = k + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'GRID_2D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_amax ( n, a ):

#*****************************************************************************80
#
## R8VEC_AMAX returns the maximum absolute value in an R8VEC.
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
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the maximum absolute value in the vector.
#
  value = 0.0
  for i in range ( 0, n ):
    if ( value < abs ( a[i] ) ):
      value = abs ( a[i] )

  return value

def r8vec_amax_test ( ):

#*****************************************************************************80
#
## R8VEC_AMAX_TEST tests R8VEC_AMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_AMAX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_AMAX computes the maximum absolute value entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_amax ( n, a )
  print ( '' )
  print ( '  Max Abs = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_AMAX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_amin ( n, a ):

#*****************************************************************************80
#
## R8VEC_AMIN returns the minimum absolute value in an R8VEC.
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
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the minimum absolute value in the vector.
#
  r8_huge = 1.79769313486231571E+308

  value = r8_huge
  for i in range ( 0, n ):
    if ( abs ( a[i] ) < value ):
      value = abs ( a[i] )

  return value

def r8vec_amin_test ( ):

#*****************************************************************************80
#
## R8VEC_AMIN_TEST tests R8VEC_AMIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_AMIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_AMIN computes the minimum absolute entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_amin ( n, a )
  print ( '' )
  print ( '  Min Abs = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_AMIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_max ( n, a ):

#*****************************************************************************80
#
## R8VEC_MAX returns the maximum value in an R8VEC.
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
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the maximum value in the vector.
#
  r8_huge = 1.79769313486231571E+308

  value = - r8_huge
  for i in range ( 0, n ):
    if ( value < a[i] ):
      value = a[i]

  return value

def r8vec_max_test ( ):

#*****************************************************************************80
#
## R8VEC_MAX_TEST tests R8VEC_MAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_MAX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MAX computes the maximum entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_max ( n, a )
  print ( '' )
  print ( '  Max = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MAX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_min ( n, a ):

#*****************************************************************************80
#
## R8VEC_MIN returns the minimum value in an R8VEC.
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
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the minimum value in the vector.
#
  r8_huge = 1.79769313486231571E+308

  value = r8_huge
  for i in range ( 0, n ):
    if ( a[i] < value ):
      value = a[i]

  return value

def r8vec_min_test ( ):

#*****************************************************************************80
#
## R8VEC_MIN_TEST tests R8VEC_MIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_MIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MIN computes the minimum entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_min ( n, a )
  print ( '' )
  print ( '  Min = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MIN_TEST:' )
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
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

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

def resid_spiral ( n, x, y, c ):

#*****************************************************************************80
#
## RESID_SPIRAL computes the residual for a spiral velocity vector field.
#
#  Discussion:
#
#    Note that the continuous velocity field (U,V)(X,Y) that is discretely
#    sampled here satisfies the homogeneous continuity equation, that is,
#    it has zero divergence.  In other words:
#
#      dU/dX + dV/dY = 0.
#
#    This is by construction, since we have
#
#      U(X,Y) =  10 * d/dY ( PHI(X) * PHI(Y) )
#      V(X,Y) = -10 * d/dX ( PHI(X) * PHI(Y) )
#
#    which guarantees zero divergence.
#
#    The underlying function PHI is defined by
#
#      PHI(Z) = ( 1 - cos ( C * pi * Z ) ) * ( 1 - Z )^2
#
#    where C is a parameter.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the coordinates of the evaluation points.
#
#    Input, real C, a parameter, typically between 0 and 2 * PI.
#
#    Output, real PR(N), the residual in the continuity equation.
#
  import numpy as np

  pr = np.zeros ( n )
  u = np.zeros ( n )
  ux = np.zeros ( n )
  v = np.zeros ( n )
  vy = np.zeros ( n )

  u =   10.0 * ( 1.0 - np.cos ( c * np.pi * x ) ) \
           * ( 1.0 - x ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * y ) ) \
             * 2.0 * ( 1.0 - y ) \
             )

  ux =   10.0 * \
    ( \
      c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * x ) ) \
      * 2.0 * ( 1.0 - x ) \
    ) \
    * \
    ( \
      c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * y ) ) \
      * 2.0 * ( 1.0 - y ) \
    );

  v = - 10.0 * ( 1.0 - np.cos ( c * np.pi * y ) ) \
           * ( 1.0 - y ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * x ) ) \
             * 2.0 * ( 1.0 - x ) \
             );

  vy =  - 10.0 * \
    ( \
      c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * x ) ) \
      * 2.0 * ( 1.0 - x ) \
    ) \
    * \
    ( \
      c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * y ) ) \
      * 2.0 * ( 1.0 - y ) \
    )

  pr = ux + vy;

  return pr

def resid_spiral_test ( ):

#*****************************************************************************80
#
## RESID_SPIRAL_TEST generates a field and samples its residuals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'RESID_SPIRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Sample a spiral velocity field and estimate the' )
  print ( '  range of residuals in the continuity equation.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = 0.0

  c = 1.00

  pr = resid_spiral ( n, x, y, c )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RESID_SPIRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def spiral_data_test ( ):

#*****************************************************************************80
#
## SPIRAL_DATA_TEST tests the SPIRAL_DATA library.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/spiral_data/spiral_data_test.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPIRAL_DATA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SPIRAL_DATA library.' )

  r8vec_amax_test ( )
  r8vec_amin_test ( )
  r8vec_max_test ( )
  r8vec_min_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )
  grid_2d_test ( )
  uv_spiral_test ( )
  resid_spiral_test ( )
  spiral_gnuplot_test ( )
  spiral_matplotlib_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPIRAL_DATA_TEST:' )
  print ( '  Normal end of execution.' )
  return

def spiral_gnuplot ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## SPIRAL_GNUPLOT writes the spiral vector field to files for GNUPLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string HEADER, a header to be used to name the files.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the coordinates of the evaluation points.
#
#    Input, real U(N), V(N), the velocity components.
#
#    Input, real S, a scale factor for the velocity vectors.
#

#
#  Write the data file.
#
  data_filename = header + '_data.txt'

  data_unit = open ( data_filename, 'w' )

  for i in range ( 0, n ):
    st = '  %g' % ( x[i] )
    data_unit.write ( st )
    st = '  %g' % ( y[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * u[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * v[i] )
    data_unit.write ( st )
    data_unit.write ( '\n' );

  data_unit.close ( )

  print ( '' )
  print ( '  Data written to "%s".' % ( data_filename ) )
#
#  Write the command file.
#
  command_filename = header + '_commands.txt'
  plot_filename = header + '.png'

  command_unit = open ( command_filename, 'w' )

  command_unit.write ( '#  %s\n' % ( command_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "%s"\n' % ( plot_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add titles and labels.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set xlabel "<--- X --->"\n' )
  command_unit.write ( 'set ylabel "<--- Y --->"\n' )
  command_unit.write ( 'set title "Spiral velocity flow"\n' )
  command_unit.write ( 'unset key\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add grid lines.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set size ratio -1\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Timestamp the plot.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set timestamp\n' )
  command_unit.write ( 'plot "%s" using 1:2:3:4 with vectors \\\n' % ( data_filename ) )
  command_unit.write ( '  head filled lt 2 linecolor rgb "blue"\n' )
  command_unit.write ( 'quit\n' )

  data_unit.close ( )

  print ( '  Commands written to "%s".' % ( command_filename ) )

  return

def spiral_gnuplot_test ( ):

#*****************************************************************************80
#
## SPIRAL_GNUPLOT_TEST generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPIRAL_GNUPLOT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Generate a spiral velocity field on a regular grid.' )
  print ( '  Store in GNUPLOT data and command files.' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
  c = 1.0

  u, v = uv_spiral ( n, x, y, c )

  header = 'spiral_data'
  s = 0.05
  spiral_gnuplot ( header, n, x, y, u, v, s )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPIRAL_GNUPLOT_TEST: ' )
  print ( '  Normal end of execution.' )
  return

def spiral_matplotlib ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## SPIRAL_MATPLOTLIB plots the velocity vector field with MATPLOTLIB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string HEADER, a header to be used to name the files.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the coordinates of the evaluation points.
#
#    Input, real U(N), V(N), the velocity components.
#
#    Input, real S, a scale factor for the velocity vectors.
#
  import matplotlib.pyplot as plt

  myplot = plt.figure ( )
  ax = plt.gca ( )
  ax.quiver ( x, y, u, v )
  ax.set_xlabel ( '<--X-->' )
  ax.set_ylabel ( '<--Y-->' )
  ax.set_title ( header )
  ax.axis ( 'equal' )
  plt.draw ( )
  plt.show ( block = False )

  plot_filename = header + '_matplotlib.png'
  myplot.savefig ( plot_filename )

  return

def spiral_matplotlib_test ( ):

#*****************************************************************************80
#
## SPIRAL_MATPLOTLIB_TEST generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPIRAL_MATPLOTLIB_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Generate a spiral velocity field on a regular grid.' )
  print ( '  Display it using MATPLOTLIB' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
  c = 1.0

  u, v = uv_spiral ( n, x, y, c )

  header = 'spiral'
  s = 0.05
  spiral_matplotlib ( header, n, x, y, u, v, s )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPIRAL_MATPLOTLIB_TEST:' )
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

def uv_spiral ( n, x, y, c ):

#*****************************************************************************80
#
## UV_SPIRAL computes a spiral velocity vector field.
#
#  Discussion:
#
#    Note that the continuous velocity field (U,V)(X,Y) that is discretely
#    sampled here satisfies the homogeneous continuity equation, that is,
#    it has zero divergence.  In other words:
#
#      dU/dX + dV/dY = 0.
#
#    This is by construction, since we have
#
#      U(X,Y) =  10 * d/dY ( PHI(X) * PHI(Y) )
#      V(X,Y) = -10 * d/dX ( PHI(X) * PHI(Y) )
#
#    which guarantees zero divergence.
#
#    The underlying function PHI is defined by
#
#      PHI(Z) = ( 1 - cos ( C * pi * Z ) ) * ( 1 - Z )^2
#
#    where C is a parameter.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the coordinates of the evaluation points.
#
#    Input, real C, a parameter, typically between 0 and 2 * PI.
#
#    Output, real U(N), V(N), the velocity components.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )

  u =   10.0 * ( 1.0 - np.cos ( c * np.pi * x ) ) \
           * ( 1.0 - x ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * y ) ) \
             * 2.0 * ( 1.0 - y ) \
             )

  v = - 10.0 * ( 1.0 - np.cos ( c * np.pi * y ) ) \
           * ( 1.0 - y ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * x ) ) \
             * 2.0 * ( 1.0 - x ) \
             )

  return u, v

def uv_spiral_test ( ):

#*****************************************************************************80
#
## UV_SPIRAL_TEST generates a field and estimates its range.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nu = 1.0
  rho = 1.0

  print ( '' )
  print ( 'UV_SPIRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Sample a spiral velocity field and estimate' )
  print ( '  the range of the solution values.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  c = 1.0
  u, v = uv_spiral ( n, x, y, c )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UV_SPIRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  spiral_data_test ( )
  timestamp ( )

