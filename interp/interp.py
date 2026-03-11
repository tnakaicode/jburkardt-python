#! /usr/bin/env python3
#
def interp_test ( ):

#*****************************************************************************80
#
## interp_test() tests interp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'interp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test interp().' )

  interp_test01 ( )

  interp_test02 ( )

  data_num = 6
  interp_test03 ( data_num )

  data_num = 11
  interp_test03 ( data_num )

  data_num = 6
  interp_test04 ( data_num )

  data_num = 11
  interp_test04 ( data_num )
#
#  Terminate.
#
  print ( '' )
  print ( 'interp_test():' )
  print ( '  Normal end of execution.' )

  return

def cc_abscissas_ab ( a, b, n ):

#*****************************************************************************80
#
## cc_abscissas_ab() computes Clenshaw Curtis abscissas for the interval [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = 0.5 * ( b + a )
  else:
    theta = np.linspace ( np.pi, 0.0, n )
    x = 0.5 * ( ( b + a ) + ( b - a ) * np.cos ( theta ) )

  return x

def cc_abscissas ( n ):

#*****************************************************************************80
#
## cc_abscissas() computes the Clenshaw Curtis abscissas.
#
#  Discussion:
#
#    The interval is [ -1, 1 ].
#
#    The abscissas are the cosines of equally spaced angles between
#    180 and 0 degrees, including the endpoints.
#
#      X(I) = cos ( ( ORDER - I ) * PI / ( ORDER - 1 ) )
#
#    except for the basic case ORDER = 1, when
#
#      X(1) = 0.
#
#    If the value of ORDER is increased in a sensible way, then
#    the new set of abscissas will include the old ones.  One such
#    sequence would be ORDER(K) = 2*K+1 for K = 0, 1, 2, ...
#
#    When doing interpolation with Lagrange polynomials, the Clenshaw Curtis
#    abscissas can be a better choice than regularly spaced abscissas.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Clenshaw, Alan Curtis,
#    A Method for Numerical Integration on an Automatic Computer,
#    Numerische Mathematik,
#    Volume 2, Number 1, December 1960, pages 197-205.
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = 0.0
  else:
    theta = np.linspace ( np.pi, 0.0, n )
    x = np.cos ( theta )

  return x

def f1_abscissas_ab ( a, b, n ):

#*****************************************************************************80
#
## f1_abscissas_ab() computes Fejer type 1 abscissas for the interval [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  if ( n == 1 ):
    x = np.zeros ( n )
    x[0] = 0.5 * ( b + a )
  else:
    left = np.pi * ( 2 * n - 1 ) / ( 2 * n )
    rite = np.pi *           1   / ( 2 * n )
    theta = np.linspace ( left, rite, n )
    x = 0.5 * ( ( b + a ) + ( b - a ) * np.cos ( theta ) )

  return x

def f1_abscissas ( n ):

#*****************************************************************************80
#
## f1_abscissas() computes Fejer type 1 abscissas.
#
#  Discussion:
#
#    The interval is [ -1, +1 ].
#
#    The abscissas are the cosines of equally spaced angles, which
#    are the midpoints of N equal intervals between 0 and PI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  if ( n == 1 ):
    x[0] = np.zeros ( n )
  else:
    left = np.pi * ( 2 * n - 1 ) / ( 2 * n )
    rite = np.pi *           1   / ( 2 * n )
    theta = np.linspace ( left, rite, n )
    x = np.cos ( theta )

  return x

def f2_abscissas_ab ( a, b, n ):

#*****************************************************************************80
#
## f2_abscissas_ab() computes Fejer Type 2 abscissas for the interval [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  left = np.pi * n / ( n + 1 )
  ryte = np.pi * 1 / ( n + 1 )
  theta = np.linspace ( left, ryte, n )
  x = 0.5 * ( ( b + a ) + ( b - a ) * np.cos ( theta ) )

  return x

def f2_abscissas ( n ):

#*****************************************************************************80
#
## f2_abscissas() computes Fejer Type 2 abscissas.
#
#  Discussion:
#
#    The interval is [-1,+1].
#
#    The abscissas are the cosines of equally spaced angles.
#    The angles are computed as N+2 equally spaced values between 0 and PI,
#    but with the first and last angle omitted.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x = np.zeros ( n )
    x[0] = 0.0
  elif ( n == 2 ):
    x = np.zeros ( n )
    x[0] = -0.5
    x[1] =  0.5
  else:
    left = np.pi * n / ( n + 1 )
    ryte = np.pi * 1 / ( n + 1 )
    x = np.cos ( theta )

  return x

def f_runge ( n, x ):

#*****************************************************************************80
#
## f_runge() evaluates the Runge function.
#
#  Discussion:
#
#    Interpolation of the Runge function at evenly spaced points in [-1,1]
#    is a common test.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = 1.0 / ( 1.0 + 25.0 * x**2 )

  return f

def interp_lagrange ( data_num, t_data, p_data, interp_num, t_interp ):

#*****************************************************************************80
#
## interp_lagrange(): Lagrange polynomial interpolation to a curve in 1 dimensions.
#
#  Discussion:
#
#    We are given a sequence of
#    DATA_NUM points, which are presumed to be successive samples
#    from a curve of points P.
#
#    We are also given a parameterization of this data, that is,
#    an associated sequence of DATA_NUM values of a variable T.
#
#    Thus, we have a sequence of values P(T), where T is a scalar,
#    and each value of P is of dimension 1.
#
#    We are then given INTERP_NUM values of T, for which values P
#    are to be produced, by linear interpolation of the data we are given.
#
#    The user may request extrapolation.  This occurs whenever
#    a T_INTERP value is less than the minimum T_DATA or greater than the
#    maximum T_DATA.  In that case, extrapolation is used.
#
#    For each spatial component, a polynomial of degree
#    ( DATA_NUM - 1 ) is generated for the interpolation.  In most cases,
#    such a polynomial interpolant begins to oscillate as DATA_NUM
#    increases, even if the original data seems well behaved.  Typically,
#    values of DATA_NUM should be no greater than 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data points.
#
#    real T_DATA(DATA_NUM), the value of the
#    independent variable at the sample points.
#
#    real P_DATA(DATA_NUM), the value of the
#    dependent variables at the sample points.
#
#    integer INTERP_NUM, the number of points
#    at which interpolation is to be done.
#
#    real T_INTERP(INTERP_NUM), the value of the
#    independent variable at the interpolation points.
#
#  Output:
#
#    real P_INTERP(INTERP_NUM), the interpolated
#    values of the dependent variables at the interpolation points.
#
  import numpy as np
#
#  Evaluate the DATA_NUM Lagrange polynomials associated with T_DATA(1:DATA_NUM)
#  for the interpolation points T_INTERP(1:INTERP_NUM).
#
  l_interp = lagrange_value ( data_num, t_data, interp_num, t_interp )
#
#  Multiply P_DATA(1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
#  to get P_INTERP(1:M,1:INTERP_NUM).
#
  p_interp = np.matmul ( np.transpose ( l_interp[0:data_num,0:interp_num] ), \
    p_data[0:data_num] )

  return p_interp

def interp_linear ( data_num, t_data, p_data, interp_num, t_interp ):

#*****************************************************************************80
#
## interp_linear(): piecewise linear interpolation to a curve in 1 dimension.
#
#  Discussion:
#
#    We are given a sequence of
#    DATA_NUM points, which are presumed to be successive samples
#    from a curve of points P.
#
#    We are also given a parameterization of this data, that is,
#    an associated sequence of DATA_NUM values of a variable T.
#    The values of T are assumed to be strictly increasing.
#
#    Thus, we have a sequence of values P(T), where T is a scalar,
#    and each value of P is of dimension 1.
#
#    We are then given INTERP_NUM values of T, for which values P
#    are to be produced, by linear interpolation of the data we are given.
#
#    Note that the user may request extrapolation.  This occurs whenever
#    a T_INTERP value is less than the minimum T_DATA or greater than the
#    maximum T_DATA.  In that case, linear extrapolation is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data points.
#
#    real T_DATA(DATA_NUM), the value of the
#    independent variable at the sample points.  The values of T_DATA
#    must be strictly increasing.
#
#    real P_DATA(DATA_NUM), the value of the
#    dependent variables at the sample points.
#
#    integer INTERP_NUM, the number of points
#    at which interpolation is to be done.
#
#    real T_INTERP(INTERP_NUM), the value of the
#    independent variable at the interpolation points.
#
#  Output:
#
#    real P_INTERP(INTERP_NUM), the interpolated
#    values of the dependent variables at the interpolation points.
#
  import numpy as np

  if ( not r8vec_is_ascending_strictly ( data_num, t_data ) ):
    print ( '' )
    print ( 'interp_linear(): Fatal error!' )
    print ( '  Independent variable array T_DATA is not strictly increasing.' )
    raise Exception ( 'interp_linear(): Fatal error!' )

  p_interp = np.zeros ( interp_num )

  for interp in range ( 0, interp_num ):

    t = t_interp[interp]
#
#  Find the interval [ TDATA(LEFT), TDATA(RIGHT) ] that contains, or is
#  nearest to, TVAL.
#
    left, right = r8vec_bracket ( data_num, t_data, t )

    p_interp[interp] = \
      ( ( t_data[right] - t                ) * p_data[left]    \
      + (                 t - t_data[left] ) * p_data[right] ) \
      / ( t_data[right]     - t_data[left] )

  return p_interp

def interp_nearest_1d ( data_num, t_data, p_data, interp_num, t_interp ):

#*****************************************************************************80
#
## interp_nearest_1d(): Nearest neighbor interpolation to a curve in 1D.
#
#  Discussion:
#
#    From a space of 1 dimension, we are given a sequence of
#    DATA_NUM points, which are presumed to be successive samples
#    from a curve of points P.
#
#    We are also given a parameterization of this data, that is,
#    an associated sequence of DATA_NUM values of a variable T.
#
#    Thus, we have a sequence of values P(T), where T is a scalar,
#    and each value of P is of dimension 1.
#
#    We are then given INTERP_NUM values of T, for which values P
#    are to be produced, by nearest neighbor interpolation.
#
#    The user may request extrapolation.  This occurs whenever
#    a T_INTERP value is less than the minimum T_DATA or greater than the
#    maximum T_DATA.  In that case, extrapolation is used.
#
#    The resulting interpolant is piecewise constant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data points.
#
#    real T_DATA(DATA_NUM), the value of the
#    independent variable at the sample points.
#
#    real P_DATA(M,DATA_NUM), the value of the
#    dependent variables at the sample points.
#
#    integer INTERP_NUM, the number of points
#    at which interpolation is to be done.
#
#    real T_INTERP(INTERP_NUM), the value of the
#    independent variable at the interpolation points.
#
#  Output:
#
#    real P_INTERP(INTERP_NUM), the interpolated
#    values of the dependent variables at the interpolation points.
#
  import numpy as np 
#
#  For each interpolation point, find the index of the nearest data point.
#
  p_interp = np.zeros ( interp_num )

  for ji in range ( 0, interp_num ):
    jd = r8vec_sorted_nearest ( data_num, t_data, t_interp[ji] )

    p_interp[ji] = p_data[jd]

  return p_interp

def interp_test01 ( ):

#*****************************************************************************80
#
## interp_test01() tests interp_nearest() on 1-dimensional data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
  data_num = 11
  m = 1

  print ( '' )
  print ( 'interp_test01():' )
  print ( '  interp_nearest_1d() evaluates a nearest-neighbor interpolant.' )
  print ( '' )
  print ( '  In this example, the function we are interpolating is' )
  print ( '  Runge''s function, with Chebyshev knots.' )

  t_min = -1.0
  t_max = +1.0

  t_data = cc_abscissas_ab ( t_min, t_max, data_num )

  p_data = f_runge ( data_num, t_data )

  print ( '' )
  print ( '  The data to be interpolated:' )
  print ( '' )
  print ( '  Spatial dimension =     ', m )
  print ( '  Number of data values = ', data_num )
  print ( '' )
  print ( '       T_data        P_data' )
  print ( '' )
  for i in range ( 0, data_num ):
    print ( '  %14.6g  %14.6g' % ( t_data[i], p_data[i] ) )
#
#  Our interpolation values will include the original T values, plus
#  3 new values in between each pair of original values.
#
  before = 4
  fat = 3
  after = 2

  interp_num = before + 1 + ( data_num - 1 ) * ( fat + 1 ) + after

  t_interp = r8vec_expand_linear2 ( data_num, t_data, before, fat, after )

  p_interp = interp_nearest_1d ( data_num, t_data, p_data, interp_num, t_interp )

  p_value = f_runge ( interp_num, t_interp )

  print ( '' )
  print ( '  Interpolation:' )
  print ( '' )
  print ( '    T_interp      P_interp        P_exact        Error' )
  print ( '' )

  for interp in range ( 0, interp_num ):

    print ( '  %10.4f  %14.6g  %14.6g  %10.2g'  \
      % ( t_interp[interp], p_interp[interp], p_value[interp], \
          p_interp[interp] - p_value[interp] ) )

  return

def interp_test02 ( ):

#*****************************************************************************80
#
## interp_test02() tests interp_linear() on 1-dimensional data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
  data_num = 11
  m = 1

  print ( '' )
  print ( 'interp_test02():' )
  print ( '  interp_linear() evaluates a piecewise linear spline.' )
  print ( '' )
  print ( '  In this example, the function we are interpolating is' )
  print ( '  Runge''s function, with evenly spaced knots.' )

  t_min = -1.0
  t_max = +1.0

  t_data = ncc_abscissas_ab ( t_min, t_max, data_num )

  p_data = f_runge ( data_num, t_data )

  print ( '' )
  print ( '  The data to be interpolated:' )
  print ( '' )
  print ( '  Spatial dimension =     ', m )
  print ( '  Number of data values = ', data_num )
  print ( '' )
  print ( '       T_data        P_data' )
  print ( '' )
  for i in range ( 0, data_num ):
    print ( '  %14.6g  %14.6g' % ( t_data[i], p_data[i] ) )
#
#  Our interpolation values will include the original T values, plus
#  3 new values in between each pair of original values.
#
  before = 4
  fat = 3
  after = 2

  interp_num = before + 1 + ( data_num - 1 ) * ( fat + 1 ) + after

  t_interp = r8vec_expand_linear2 ( data_num, t_data, before, fat, after )

  p_interp = interp_linear ( data_num, t_data, p_data, interp_num, t_interp )

  p_value = f_runge ( interp_num, t_interp )

  print ( '' )
  print ( '  Interpolation:' )
  print ( '' )
  print ( '    T_interp      P_interp        P_exact        Error' )
  print ( '' )

  for interp in range ( 0, interp_num ):

    print ( '  %10.4f  %14.6g  %14.6g  %10.2g' \
      % ( t_interp[interp], p_interp[interp], p_value[interp], \
      p_interp[interp] - p_value[interp] ) )

  return

def interp_test03 ( data_num ):

#*****************************************************************************80
#
## interp_test03() tests interp_lagrange() on 1-dimensional data, equally spaced data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data values.
#
  m = 1

  print ( '' )
  print ( 'interp_test03():' )
  print ( '  interp_lagrange() evaluates a polynomial interpolant.' )
  print ( '' )
  print ( '  In this example, the function we are interpolating is' )
  print ( '  Runge''s function, with evenly spaced knots.' )

  t_min = -1.0
  t_max = +1.0

  t_data = ncc_abscissas_ab ( t_min, t_max, data_num )

  p_data = f_runge ( data_num, t_data )

  print ( '' )
  print ( '  The data to be interpolated:' )
  print ( '' )
  print ( '  Spatial dimension =     ', m )
  print ( '  Number of data values = ', data_num )
  print ( '' )
  print ( '       T_data        P_data' )
  print ( '' )
  for i in range ( 0, data_num ):
    print ( '  %14.6g  %14.6g' % ( t_data[i], p_data[i] ) )
#
#  Our interpolation values will include the original T values, plus
#  3 new values in between each pair of original values.
#
  before = 4
  fat = 3
  after = 2

  interp_num = before + 1 + ( data_num - 1 ) * ( fat + 1 ) + after

  t_interp = r8vec_expand_linear2 ( data_num, t_data, before, fat, after )

  p_interp = interp_lagrange ( data_num, t_data, p_data, interp_num, t_interp )

  p_value = f_runge ( interp_num, t_interp )

  print ( '' )
  print ( '  Interpolation:' )
  print ( '' )
  print ( '    T_interp      P_interp        P_exact        Error' )
  print ( '' )

  for interp in range ( 0, interp_num ):

    print ( '  %10.4f  %14.6g  %14.6g  %10.2g' \
      % ( t_interp[interp], p_interp[interp], p_value[interp], \
          p_interp[interp] - p_value[interp] ) )

  return

def interp_test04 ( data_num ):

#*****************************************************************************80
#
## interp_test04() tests interp_lagrange() on 1-dimensional data, Clenshaw-Curtis data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data values.
#
  m = 1

  print ( '' )
  print ( 'interp_test04():' )
  print ( '  interp_lagrange() evaluates a polynomial interpolant.' )
  print ( '' )
  print ( '  In this example, the function we are interpolating is' )
  print ( '  Runge''s function, with Clenshaw Curtis knots.' )

  t_min = -1.0
  t_max = +1.0

  t_data = cc_abscissas_ab ( t_min, t_max, data_num )

  p_data = f_runge ( data_num, t_data )

  print ( '' )
  print ( '  The data to be interpolated:' )
  print ( '' )
  print ( '  Spatial dimension =     ', m )
  print ( '  Number of data values = ', data_num )
  print ( '' )
  print ( '       T_data        P_data' )
  print ( '' )
  for i in range ( 0, data_num ):
    print ( '  %14.6g  %14.6g' % ( t_data[i], p_data[i] ) )
#
#  Our interpolation values will include the original T values, plus
#  3 new values in between each pair of original values.
#
  before = 4
  fat = 3
  after = 2

  interp_num = before + 1 + ( data_num - 1 ) * ( fat + 1 ) + after

  t_interp = r8vec_expand_linear2 ( data_num, t_data, before, fat, after )

  p_interp = interp_lagrange ( data_num, t_data, p_data, interp_num, t_interp )

  p_value = f_runge ( interp_num, t_interp )

  print ( '' )
  print ( '  Interpolation:' )
  print ( '' )
  print ( '    T_interp      P_interp        P_exact        Error' )
  print ( '' )

  for interp in range ( 0, interp_num ):

    print ( '  %10.4f  %14.6g  %14.6g  %10.2g' \
      % ( t_interp[interp], p_interp[interp], p_value[interp], \
          p_interp[interp] - p_value[interp] ) )

  return

def lagrange_value ( data_num, t_data, interp_num, t_interp ):

#*****************************************************************************80
#
## lagrange_value() evaluates the Lagrange polynomials.
#
#  Discussion:
#
#    Given DATA_NUM distinct abscissas, T_DATA(1:DATA_NUM),
#    the I-th Lagrange polynomial L(I)(T) is defined as the polynomial of
#    degree DATA_NUM - 1 which is 1 at T_DATA(I) and 0 at the DATA_NUM - 1
#    other abscissas.
#
#    A formal representation is:
#
#      L(I)(T) = Product ( 1 <= J <= DATA_NUM, I /= J )
#       ( T - T(J) ) / ( T(I) - T(J) )
#
#    This routine accepts a set of INTERP_NUM values at which all the Lagrange
#    polynomials should be evaluated.
#
#    Given data values P_DATA at each of the abscissas, the value of the
#    Lagrange interpolating polynomial at each of the interpolation points
#    is then simple to compute by matrix multiplication:
#
#      P_INTERP(1:INTERP_NUM) =
#        P_DATA(1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
#
#    or, in the case where P is multidimensional:
#
#      P_INTERP(1:M,1:INTERP_NUM) =
#        P_DATA(1:M,1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data points.
#    DATA_NUM must be at least 1.
#
#    real T_DATA(DATA_NUM), the data points.
#
#    integer INTERP_NUM, the number of interpolation points.
#
#    real T_INTERP(INTERP_NUM), the interpolation points.
#
#  Output:
#
#    real L_INTERP(DATA_NUM,INTERP_NUM), the values
#    of the Lagrange polynomials at the interpolation points.
#
  import numpy as np
#
#  Evaluate the polynomial.
#
  l_interp = np.ones ( [ data_num, interp_num ] )

  for i in range ( 0, data_num ):
    for j in range ( 0, data_num ):
      if ( j != i ):
        l_interp[i,:] = l_interp[i,:] \
          * ( t_interp[:] - t_data[j] ) / ( t_data[i] - t_data[j] )

  return l_interp

def ncc_abscissas_ab ( a, b, n ):

#*****************************************************************************80
#
## ncc_abscissas_ab() computes the Newton Cotes Closed abscissas for [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x = np.zeros ( n )
    x[0] = 0.5 * ( b + a )
  else:
    x = np.linspace ( a, b, n )

  return x

def ncc_abscissas ( n ):

#*****************************************************************************80
#
## ncc_abscissas() computes the Newton Cotes Closed abscissas.
#
#  Discussion:
#
#    The interval is [ -1, 1 ].
#
#    The abscissas are the equally spaced points between -1 and 1,
#    including the endpoints.
#
#    If N is 1, however, the single abscissas is X = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  if ( n == 1 ):
    x = np.zeros ( n )
  else:
    x = np.linspace ( -1.0, +1.0, n )

  return x

def nco_abscissas_ab ( a, b, n ):

#*****************************************************************************80
#
## nco_abscissas_ab() computes the Newton Cotes Open abscissas for [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  left = ( a * n + b * 1 ) / ( n + 1 )
  ryte = ( a * 1 + b * n ) / ( n + 1 )
  x = np.linspace ( left, ryte, n )

  return x

def nco_abscissas ( n ):

#*****************************************************************************80
#
## nco_abscissas() computes the Newton Cotes Open abscissas.
#
#  Discussion:
#
#    The interval is [ -1, 1 ].
#
#    The abscissas are the equally spaced points between -1 and 1,
#    not including the endpoints.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real X(N), the abscissas.
#
  import numpy as np

  left = ( - n + 1 ) / ( n + 1 )
  ryte = (   n - 1 ) / ( n + 1 )
  x = np.linspace ( left, ryte, n )

  return x

def parameterize_arc_length ( m, data_num, p_data ):

#*****************************************************************************80
#
## parameterize_arc_length() parameterizes data by pseudo-arclength.
#
#  Discussion:
#
#    A parameterization is required for the interpolation.
#
#    This routine provides a parameterization by computing the
#    pseudo-arclength of the data, that is, the Euclidean distance
#    between successive points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer DATA_NUM, the number of data points.
#
#    real P_DATA(M,DATA_NUM), the data values.
#
#  Output:
#
#    real T_DATA(DATA_NUM), parameter values
#    assigned to the data.
#
  import numpy as np

  t_data = np.zeros ( data_num )

  t_data[0] = 0.0
  for j in range ( 1, data_num ):
    t_data[j] = t_data[j-1] \
      + np.sqrt ( np.sum ( ( p_data[:,j] - p_data[:,j-1] )**2 ) )

  return t_data

def parameterize_index ( m, data_num, p_data ):

#*****************************************************************************80
#
## parameterize_index() parameterizes data by its index.
#
#  Discussion:
#
#    A parameterization is required for the interpolation.
#
#    This routine provides a naive parameterization by vector index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer DATA_NUM, the number of data points.
#
#    real P_DATA(M,DATA_NUM), the data values.
#
#  Output:
#
#    real T_DATA(DATA_NUM), parameter values assigned to the data.
#
  import numpy as np

  t_data = np.arange ( data_num )

  return t_data

def r8mat_expand_linear2 ( m, n, a, m2, n2 ):

#*****************************************************************************80
#
## r8mat_expand_linear2() expands an R8MAT by linear interpolation.
#
#  Discussion:
#
#    In this version of the routine, the expansion is indicated
#    by specifying the dimensions of the expanded array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in A.
#
#    real A(M,N), a "small" M by N array.
#
#    integer M2, N2, the number of rows and columns in A2.
#
#  Output:
#
#    real A2(M2,N2), the expanded array, which
#    contains an interpolated version of the data in A.
#
  import numpy as np

  a2 = np.zeros ( [ m2, n2 ] )

  for i in range ( 1, m2 + 1 ):

    if ( m2 == 1 ):
      r = 0.5
    else:
      r = ( i - 1 ) / ( m2 - 1 )

    i1 = 1 + floor ( r * ( m - 1 ) )
    i2 = i1 + 1

    if ( m < i2 ):
      i1 = m - 1
      i2 = m

    r1 = ( i1 - 1 ) / ( m - 1 )
    r2 = ( i2 - 1 ) / ( m - 1 )

    for j in range ( 1, n2 + 1 ):

      if ( n2 == 1 ):
        s = 0.5
      else:
        s = ( j - 1 ) / ( n2 - 1 )
 
      j1 = 1 + floor ( s * ( n - 1 ) )
      j2 = j1 + 1

      if ( n < j2 ):
        j1 = n - 1
        j2 = n

      s1 = ( j1 - 1 ) / ( n - 1 )
      s2 = ( j2 - 1 ) / ( n - 1 )

      a2[i-1,j-1] = \
        ( ( r2 - r ) * ( s2 - s ) * a(i1,j1) \
        + ( r - r1 ) * ( s2 - s ) * a(i2,j1) \
        + ( r2 - r ) * ( s - s1 ) * a(i1,j2) \
        + ( r - r1 ) * ( s - s1 ) * a(i2,j2) ) \
        / ( ( r2 - r1 ) * ( s2 - s1 ) )

  return a2

def r8vec_bracket ( n, x, xval ):

#*****************************************************************************80
#
## r8vec_bracket() searches a sorted array for successive brackets of a value.
#
#  Discussion:
#
#    A naive algorithm is used.
#
#    If the values in the vector are thought of as defining intervals
#    on the real line, then this routine searches for the interval
#    nearest to or containing the given value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, length of input array.
#
#    real X(N), an array that has been sorted into ascending order.
#
#    real XVAL, a value to be bracketed.
#
#  Output:
#
#    integer LEFT, RIGHT, the results of the search.
#    Either:
#      XVAL < X(1), when LEFT = 1, RIGHT = 2
#      XVAL > X(N), when LEFT = N-1, RIGHT = N
#    or
#      X(LEFT) <= XVAL <= X(RIGHT).
#
  for i in range ( 1, n - 1 ):

    if ( xval < x[i] ):
      left = i - 1
      right = i
      return left, right

  left = n - 2
  right = n - 1

  return left, right

def r8vec_expand_linear2 ( n, x, before, fat, after ):

#*****************************************************************************80
#
## r8vec_expand_linear2() linearly interpolates new data into an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    This routine starts with a vector of data.
#
#    The intent is to "fatten" the data, that is, to insert more points
#    between successive values of the original data.
#
#    There will also be extra points placed BEFORE the first original
#    value and AFTER that last original value.
#
#    The "fattened" data is equally spaced between the original points.
#
#    The BEFORE data uses the spacing of the first original interval,
#    and the AFTER data uses the spacing of the last original interval.
#
#  Example:
#
#    N = 3
#    BEFORE = 3
#    FAT = 2
#    AFTER = 1
#
#    X    = (/                   0.0,           6.0,             7.0       /)
#    XFAT = (/ -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 6.33, 6.66, 7.0, 7.66 /)
#            3 "BEFORE's"        Old  2 "FATS"  Old    2 "FATS"  Old  1 "AFTER"
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of input data values.
#    N must be at least 2.
#
#    real X(N), the original data.
#
#    integer BEFORE, the number of "before" values.
#
#    integer FAT, the number of data values to interpolate
#    between each pair of original data values.
#
#    integer AFTER, the number of "after" values.
#
#  Output:
#
#    real XFAT(BEFORE+(N-1)*(FAT+1)+1+AFTER), the "fattened" data.
#
  import numpy as np

  xfat = np.zeros ( before+(n-1)*(fat+1)+1+after )

  k = 0
#
#  Points BEFORE.
#
  for j in range ( 1 - before + fat, fat + 1 ):

    xfat[k] = ( ( fat - j + 1 ) * ( x[0] - ( x[1] - x[0] ) ) \
              + (       j     ) *   x[0]          ) \
              / ( fat     + 1 )
    k = k + 1
#
#  Original points and FAT points.
#
  for i in range ( 1, n ):

    xfat[k] = x[i-1]
    k = k + 1

    for j in range ( 1, fat + 1 ):
      xfat[k] = ( ( fat - j + 1 ) * x[i-1] \
                + (       j     ) * x[i] ) \
                / ( fat     + 1 )
      k = k + 1

  xfat[k] = x[n-1]
  k = k + 1
#
#  Points AFTER.
#
  for j in range ( 1, after + 1 ):
    xfat[k] = ( ( fat - j + 1 ) *   x[n-1] \
              + (       j     ) * ( x[n-1] + ( x[n-1] - x[n-2] ) ) ) \
              / ( fat     + 1 )
    k = k + 1

  return xfat

def r8vec_expand_linear ( n, x, fat ):

#*****************************************************************************80
#
## r8vec_expand_linear() linearly interpolates new data into a vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of input data values.
#
#    real X(N), the original data.
#
#    integer FAT, the number of data values to interpolate
#    between each pair of original data values.
#
#  Output:
#
#    real XFAT((N-1)*(FAT+1)+1), the "fattened" data.
#
  import numpy as np

  xfat = np.zeros ( ( n - 1 ) * ( fat + 1 ) + 1 )

  k = 0

  for i in range ( 1, n ):

    xfat[k] = x[i-1]
    k = k + 1

    for j in range ( 1, fat + 1 ):
      xfat[k] = ( ( fat - j + 1 ) * x[i-1] \
                + (       j     ) * x[i] ) \
                / ( fat     + 1 )
      k = k + 1

  xfat[k] = x[n-1]
  k = k + 1

  return xfat

def r8vec_is_ascending_strictly ( n, x ):

#*****************************************************************************80
#
## r8vec_is_ascending_strictly() determines if an R8VEC is strictly ascending.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    Notice the effect of entry number 6 in the following results:
#
#      X = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.4, 9.8 )
#      Y = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.5, 9.8 )
#      Z = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.6, 9.8 )
#
#      r8vec_is_ascending_strictly ( X ) = false
#      r8vec_is_ascending_strictly ( Y ) = false
#      r8vec_is_ascending_strictly ( Z ) = true
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the array.
#
#    real X(N), the array to be examined.
#
#  Output:
#
#    bool VALUE, is true if the
#    entries of X strictly ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i+1] <= x[i] ):
      value = False
      break

  return value

def r8vec_sorted_nearest ( n, a, value ):

#*****************************************************************************80
#
## r8vec_sorted_nearest() returns the nearest element in a sorted R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    real A(N), a sorted vector.
#
#    real VALUE, the value whose nearest vector entry is sought.
#
#  Output:
#
#    integer INDEX, the index of the nearest entry in the vector.
#
  import numpy as np

  if ( n < 1 ):
    raise Exception ( 'r8vec_sorted_nearest(): n < 1 ' )

  if ( n == 1 ):
    index = 0
    return index
#
#  Ascending sorted vector:
#
  if ( a[0] < a[n-1] ):

    if ( value <= a[0] ):
      index = 0
      return index
    elif ( a[n-1] <= value ):
      index = n - 1
      return index
#
#  Seek an interval containing the value.
#
    lo = 0
    hi = n - 1

    while ( lo < hi - 1 ):

      mid = int ( np.floor ( ( lo + hi ) / 2 ) )

      if ( value == a[mid] ):
        index = mid
        return index
      elif ( value < a[mid] ):
        hi = mid
      else:
        lo = mid
#
#  Take the nearest.
#
    if ( np.abs ( value - a[lo] ) < np.abs ( value - a[hi] ) ):
      index = lo
    else:
      index = hi

    return index
#
#  A descending sorted vector A.
#
  else:

    if ( value <= a[n-1] ):
      index = n - 1
      return index
    elif ( a[0] <= value ):
      index = 0
      return index
#
#  Seek an interval containing the value.
#
    lo = n - 1
    hi = 0

    while ( lo < hi - 1 ):

      mid = np.floor ( ( lo + hi ) / 2 )

      if ( value == a[mid] ):
        index = mid
        return index
      elif ( value < a[mid] ):
        hi = mid
      else:
        lo = mid
#
#  Take the nearest.
#
    if ( np.abs ( value - a[lo] ) < np.abs ( value - a[hi] ) ):
      index = lo
    else:
      index = hi

    return index

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
  interp_test ( )
  timestamp ( )

