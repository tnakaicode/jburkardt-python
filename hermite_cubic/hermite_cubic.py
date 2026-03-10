#! /usr/bin/env python3
#
def hermite_cubic_test ( ):

#*****************************************************************************80
#
## hermite_cubic_test() tests hermite_cubic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hermite_cubic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hermite_cubic().' )

  hermite_cubic_test01 ( )
  hermite_cubic_test02 ( )
  hermite_cubic_test03 ( )
  hermite_cubic_test04 ( )
  hermite_cubic_test05 ( )
  hermite_cubic_test06 ( )
  hermite_cubic_test07 ( )
  hermite_cubic_test08 ( )
  hermite_cubic_test09 ( )
  hermite_cubic_test10 ( )
  hermite_cubic_test11 ( )
  hermite_cubic_test12 ( )
  hermite_cubic_test13 ( )
  hermite_cubic_test14 ( )
  hermite_cubic_test15 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hermite_cubic_test():' )
  print ( '  Normal end of execution.' )

  return

def cubic_antiderivative ( x ):

#*****************************************************************************80
#
## cubic_antiderivative() evaluates the antiderivative function of a cubic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real G, the value.
#
  g = x * x * ( 5.0 + x * ( - 7.0 / 3.0 + x * 1.0 / 4.0 ) )

  return g

def cubic_integrate ( a, b ):

#*****************************************************************************80
#
## cubic_integrate() integrates the cubic from A to B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the integration interval.
#
#  Output:
#
#    real Q, the integral from A to B.
#
  q = cubic_antiderivative ( b ) - cubic_antiderivative ( a )

  return q

def cubic_value ( x ):

#*****************************************************************************80
#
## cubic_value() evaluates a cubic function.
#
#  Discussion:
#
#    f(x) =   x^3 -  7 x^2 + 10 x
#    d(x) = 3 x^2 - 14 x   + 10
#    s(x) = 6 x   - 14
#    t(x) = 6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real F, D, S, T, the value and first three derivatives of
#    the cubic function.
#
  f = 0.0 + x * ( 10.0 + x * (  - 7.0 + x * 1.0 ) )
  d =             10.0 + x * ( - 14.0 + x * 3.0 )
  s =                          - 14.0 + x * 6.0
  t =                                       6.0

  return f, d, s, t

def hermite_cubic_integral ( x1, f1, d1, x2, f2, d2 ):

#*****************************************************************************80
#
## hermite_cubic_integral() returns the integral of a Hermite cubic polynomial.
#
#  Discussion:
#
#    The integral is taken over the definition interval [X1,X2].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, F1, D1, the left endpoint, function value and derivative.
#
#    real X2, F2, D2, the right endpoint, function value and derivative.
#
#  Output:
#
#    real Q, the integral of the Hermite cubic polynomial
#    over the interval X1 <= X <= X2.
#
  h = x2 - x1

  q = 0.5 * h * ( f1 + f2 + h * ( d1 - d2 ) / 6.0 )

  return q

def hermite_cubic_integrate ( x1, f1, d1, x2, f2, d2, a, b ):

#*****************************************************************************80
#
## hermite_cubic_integrate() integrates a Hermite cubic polynomial from A to B.
#
#  Discussion:
#
#    A and B may be scalars, or one may be a vector, or both
#    may be vectors of the same size.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, F1, D1, the left endpoint, function value and derivative.
#
#    real X2, F2, D2, the right endpoint, function value and derivative.
#
#    real A, B, the left and right endpoints of the interval
#    of integration.
#
#  Output:
#
#    real Q, the integral of the Hermite cubic polynomial
#    over the interval A <= X <= B.
#
  h = x2 - x1
  ta1 = ( a - x1 ) / h
  ta2 = ( x2 - a ) / h
  tb1 = ( b - x1 ) / h
  tb2 = ( x2 - b ) / h

  ua1 = ta1 * ta1 * ta1
  phia1 = ua1 * ( 2.0 - ta1 )
  psia1 = ua1 * ( 3.0 * ta1 - 4.0 )

  ua2 = ta2 * ta2 * ta2
  phia2 =  ua2 * ( 2.0 - ta2 )
  psia2 = -ua2 * ( 3.0 * ta2 - 4.0 )

  ub1 = tb1 * tb1 * tb1
  phib1 = ub1 * ( 2.0 - tb1 )
  psib1 = ub1 * ( 3.0 * tb1 - 4.0 )

  ub2 = tb2 * tb2 * tb2
  phib2 =  ub2 * ( 2.0 - tb2 )
  psib2 = -ub2 * ( 3.0 * tb2 - 4.0 )

  fterm =   f1 * ( phia2 - phib2 ) + f2 * ( phib1 - phia1 )
  dterm = ( d1 * ( psia2 - psib2 ) + d2 * ( psib1 - psia1 ) ) * ( h / 6.0 )

  q = 0.5 * h * ( fterm + dterm )

  return q

def hermite_cubic_lagrange_integral ( x1, x2 ):

#*****************************************************************************80
#
## hermite_cubic_lagrange_integral(): Hermite cubic Lagrange integrals.
#
#  Discussion:
#
#    The Hermite cubic polynomial P(X) for interval (X1,X2) and data
#    (F1,D1,F2,D2) satisfies:
#
#      P(X1) = F1,
#      P'(X1) = D1,
#      P(X2) = F2,
#      P'(X2) = D2.
#
#    We can determine four Lagrange polynomials L1(X) through L4(X) so that
#
#      P(X) = F1 * L1(X) + D1 * L2(X) + F2 * L3(X) + D2 * L4(X).
#
#    This function returns the integrals of these four polynomials over
#    the domain of definition [X1,X2].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, X2, the endpoints.
#
#  Output:
#
#    real Q(4), the integrals of the Hermite cubic Lagrange polynomials
#    from X1 to X2.
#
  import numpy as np

  h = x2 - x1

  q = np.array ( [ h / 2.0, h**2 / 12.0, h / 2.0, - h**2 / 12.0 ] )

  return q

def hermite_cubic_lagrange_integrate ( x1, x2, a, b ):

#*****************************************************************************80
#
## hermite_cubic_lagrange_integrate() integrates Hermite cubic Lagrange polynomials.
#
#  Discussion:
#
#    A and B may be scalars, or one may be a vector, or both
#    may be vectors of the same size.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, X2, the endpoints of the interval of definition.
#
#    real A, B, the left and right endpoints of the interval
#    of integration.
#
#  Output:
#
#    real Q(4), the integrals of the Hermite cubic Lagrange polynomials
#    over the interval A <= X <= B.
#
  import numpy as np

  h = x2 - x1
  ta1 = ( a - x1 ) / h
  ta2 = ( x2 - a ) / h
  tb1 = ( b - x1 ) / h
  tb2 = ( x2 - b ) / h

  ua1 = ta1 * ta1 * ta1
  phia1 = ua1 * ( 2.0 - ta1 )
  psia1 = ua1 * ( 3.0 * ta1 - 4.0 )

  ua2 = ta2 * ta2 * ta2
  phia2 =  ua2 * ( 2.0 - ta2 )
  psia2 = -ua2 * ( 3.0 * ta2 - 4.0 )

  ub1 = tb1 * tb1 * tb1
  phib1 = ub1 * ( 2.0 - tb1 )
  psib1 = ub1 * ( 3.0 * tb1 - 4.0 )

  ub2 = tb2 * tb2 * tb2
  phib2 =  ub2 * ( 2.0 - tb2 )
  psib2 = -ub2 * ( 3.0 * tb2 - 4.0 )

  q = np.array ( [ \
    0.5 * h * ( phia2 - phib2 ), \
    0.5 * h * ( psia2 - psib2 ) * ( h / 6.0 ), \
    0.5 * h * ( phib1 - phia1 ), \
    0.5 * h * ( psib1 - psia1 ) * ( h / 6.0 ) ] )

  return q

def hermite_cubic_lagrange_value ( x1, x2, n, x ):

#*****************************************************************************80
#
## hermite_cubic_lagrange_value() evaluates the Hermite cubic Lagrange polynomials.
#
#  Discussion:
#
#    The Hermite cubic polynomial P(X) for interval (X1,X2) and data
#    (F1,D1,F2,D2) satisfies:
#
#      P(X1) = F1,
#      P'(X1) = D1,
#      P(X2) = F2,
#      P'(X2) = D2.
#
#    We can determine four Lagrange polynomials L1(X) through L4(X) so that
#
#      P(X) = F1 * L1(X) + D1 * L2(X) + F2 * L3(X) + D2 * L4(X).
#
#    This function returns the values and derivatives of these four
#    polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, X2, the endpoints.
#
#    integer N, the number of sample points.
#
#    real X(N), the sample points.
#
#  Output:
#
#    real F[N,4], D[N,4], S[N,4], T[N,4], the value and first
#    three derivatives of the Hermite cubic Lagrange polynomials at X.
#
  import numpy as np

  f = np.zeros ( [ n, 4 ] )
  d = np.zeros ( [ n, 4 ] )
  s = np.zeros ( [ n, 4 ] )
  t = np.zeros ( [ n, 4 ] )

  h = x2 - x1
  dx = x - x1
#
#  F1.
#
  f[:,0] = 1.0 + (  dx / h )    * ( dx / h ) * ( - 3.0 + ( dx / h ) *  2.0 )
  d[:,0] =       ( 1.0 / h )    * ( dx / h ) * ( - 6.0 + ( dx / h ) *  6.0 )
  s[:,0] =       ( 1.0 / h )**2              * ( - 6.0 + ( dx / h ) * 12.0 )
  t[:,0] =       ( 1.0 / h )**3                                     * 12.0
#
#  D1
#
  f[:,1] = dx  * ( 1.0 + ( dx  / h ) *  ( - 2.0 + ( dx / h )     ) )
  d[:,1] = 1.0         + ( dx  / h ) *  ( - 4.0 + ( dx / h ) * 3.0 )
  s[:,1] =               ( 1.0 / h ) *  ( - 4.0 + ( dx / h ) * 6.0 )
  t[:,1] =               ( 1.0 / h )**2                      * 6.0
#
#  F2
#
  f[:,2] = (  dx / h ) * ( dx  / h )    * ( 3.0 -  2.0 * ( dx / h ) )
  d[:,2] = ( 1.0 / h ) * ( dx  / h )    * ( 6.0 -  6.0 * ( dx / h ) )
  s[:,2] =               ( 1.0 / h )**2 * ( 6.0 - 12.0 * ( dx / h ) )
  t[:,2] =               ( 1.0 / h )**3 * (     - 12.0              )
#
#  D2
#
  f[:,3] = dx * ( dx  / h ) * ( - 1.0 + ( dx / h )       )
  d[:,3] =      ( dx  / h ) * ( - 2.0 + ( dx / h ) * 3.0 )
  s[:,3] =      ( 1.0 / h ) * ( - 2.0 + ( dx / h ) * 6.0 )
  t[:,3] =      ( 1.0 / h )                        * 6.0

  return f, d, s, t

def hermite_cubic_spline_integral ( nn, xn, fn, dn ):

#*****************************************************************************80
#
## hermite_cubic_spline_integral(): Hermite cubic spline integral.
#
#  Discussion:
#
#    The integral is taken over the definition interval [X(1),X(NN)].
#
#    Note that if the intervals are equal in size, then the derivative
#    information in DN has no effect on the integral value,
#    except for the first and last entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    integer NN, the number of data points.
#
#    real XN(NN), the coordinates of the data points.
#    The entries in XN must be in strictly ascending order.
#
#    real FN(NN), the function values.
#
#    real DN(NN), the derivative values.
#
#  Output:
#
#    real Q, the integral of the Hermite cubic spline
#    over the interval X(1) <= X <= X(NN).
#
  import numpy as np
#
#  Index the left and right values for each interval.
#
  il = np.arange ( 0, nn - 1 )
  ir = np.arange ( 1, nn )

  h = xn[ir] - xn[il]

  q = np.sum ( 0.5 * h * ( fn[il] + fn[ir] + h * ( dn[il] - dn[ir] ) / 6.0 ) )

  return q

def hermite_cubic_spline_integrate ( nn, xn, fn, dn, n, a, b ):

#*****************************************************************************80
#
## hermite_cubic_spline_integrate() integrates a Hermite cubic spline over [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    integer NN, the number of data points.
#
#    real XN(NN), the coordinates of the data points.
#    The entries in XN must be in strictly ascending order.
#
#    real FN(NN), the function values.
#
#    real DN(NN), the derivative values.
#
#    integer N, the number of integration intervals.
#
#    real A(N), B(N), the integration endpoints.
#
#  Output:
#
#    real Q(N), the integral over the interval [A,B].
#
  import numpy as np

  q = np.zeros ( n )

  for ii in range ( 0, n ):

    if ( a[ii] <= b[ii] ):
      aa = a[ii]
      bb = b[ii]
      s = + 1.0
    else:
      aa = b[ii]
      bb = a[ii]
      s = - 1.0

    i = r8vec_bracket5 ( nn, xn, aa )
    j = r8vec_bracket5 ( nn, xn, bb )
#
#  Evaluate the polynomial with the appropriate data.
#
    if ( i == j ):

      q[ii] = hermite_cubic_integrate ( xn[i], fn[i], dn[i], \
        xn[i+1], fn[i+1], dn[i+1], aa, bb )

    else:

      q[ii] = hermite_cubic_integrate ( xn[i], fn[i], dn[i], \
        xn[i+1], fn[i+1], dn[i+1], aa, xn[i+1] )

      for k in range ( i + 1, j ):
        q[ii] = q[ii] + hermite_cubic_integral ( xn[k], fn[k], dn[k], \
          xn[k+1], fn[k+1], dn[k+1] )

      q[ii] = q[ii] + hermite_cubic_integrate ( xn[j], fn[j], dn[j], \
        xn[j+1], fn[j+1], dn[j+1], xn[j], bb )

    q[ii] = s * q[ii]

  return q

def hermite_cubic_spline_quad_rule ( nn, xn ):

#*****************************************************************************80
#
## hermite_cubic_spline_quad_rule(): Hermite cubic spline quadrature rule.
#
#  Discussion:
#
#    The integral is taken over the definition interval [X(1),X(NN)].
#
#    Note that if the intervals are equal in size, then the derivative
#    information in DN has no effect on the integral value,
#    except for the first and last entries.
#
#    The quadrature rule is
#
#      Integral ( XN(1) <= X <= XN(NN) ) F(X) dX is approximately
#
#      Sum ( 1 <= I <= NN ) W(1,I) * F(X(I)) + W(2,I) * F'(X(I))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    integer NN, the number of data points.
#
#    real XN(NN), the coordinates of the data points.
#    The entries in XN must be in strictly ascending order.
#
#  Output:
#
#    real W[NN,2], the quadrature weights for F(1:NN)
#    and DN(1:NN).
#
  import numpy as np

  w = np.zeros ( [ nn, 2 ] );

  w[0,0]      = 0.5 * ( xn[1]    - xn[0]      )
  w[1:nn-1,0] = 0.5 * ( xn[2:nn] - xn[0:nn-2] )
  w[nn-1,0]   = 0.5 * ( xn[nn-1] - xn[nn-2]   )

  w[0,1]      =   ( xn[1]    - xn[0] )**2 / 12.0
  w[1:nn-1,1] =   ( xn[2:nn] - xn[0:nn-2] ) \
                * ( xn[2:nn] - 2.0 * xn[1:nn-1] + xn[0:nn-2] ) / 12.0
  w[nn-1,1]   = - ( xn[nn-1] - xn[nn-2] )**2 / 12.0

  return w

def hermite_cubic_spline_value ( nn, xn, fn, dn, n, x ):

#*****************************************************************************80
#
## hermite_cubic_spline_value() evaluates a Hermite cubic spline.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    integer NN, the number of data points.
#
#    real XN(NN), the coordinates of the data points.
#    The entries in XN must be in strictly ascending order.
#
#    real FN(NN), the function values.
#
#    real DN(NN), the derivative values.
#
#    integer N, the number of sample points.
#
#    real X(N), the coordinates of the sample points.
#
#  Output:
#
#    real F(N), the function value at the sample points.
#
#    real D(N), the derivative value at the sample points.
#
#    real S(N), the second derivative value at the sample points.
#
#    real T(N), the third derivative value at the sample points.
#
  import numpy as np
#
#  Find bracketing interval xn[i1[i]] <= x[i] <= xn[i1[i]+1]
#
  i1 = np.zeros ( n, dtype = int )

  for i in range ( 0, n ):
    i1[i] = r8vec_bracket5 ( nn, xn, x[i] )

  i2 = i1 + 1
#
#  Evaluate cubic spline.
#
  f, d, s, t = hermite_cubic_value ( xn[i1], fn[i1], dn[i1], \
                                     xn[i2], fn[i2], dn[i2], n, x )

  return f, d, s, t

def hermite_cubic_test01 ( ):

#*****************************************************************************80
#
## hermite_cubic_test01() tests hermite_cubic_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_cubic_test01():' )
  print ( '  hermite_cubic_value() evaluates a Hermite cubic polynomial.' )
  print ( '  Try out four sets of data:' )
  print ( '  (F1,D1,F2,D2) = (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)' )
  print ( '  on [0,1] and [1.0,-2.0] (interval reversed)' )

  for x_interval in [ 1, 2 ]:

    if ( x_interval == 1 ):
      x1 = 0.0
      x2 = 1.0
    else:
      x1 = 1.0
      x2 = -2.0

    for i in [ 1, 2, 3, 4 ]:
      f1 = 0.0
      d1 = 0.0
      f2 = 0.0
      d2 = 0.0
      if ( i == 1 ):
        f1 = 1.0
      elif ( i == 2 ):
        d1 = 1.0
      elif ( i == 3 ):
        f2 = 1.0
      elif ( i == 4 ):
        d2 = 1.0

      print ( '' )
      print ( '    J      X           F           D' )
      print ( '' )

      for j in range ( -3, 13 ):
        x = ( ( 10 - j ) * x1   \
            +        j   * x2 ) \
              / 10.0

        f, d, s, t = hermite_cubic_value ( x1, f1, d1, x2, f2, d2, 1, x )

        if ( j == 0 ):
          print ( '*Data  %10f  %10f  %10f' % ( x1, f1, d1 ) )
        print ( '  %3d  %10f  %10f  %10f' % ( j, x, f, d ) )
        if ( j == 10 ):
           print ( '*Data  %10f  %10f  %10f' % ( x2, f2, d2 ) )

  return

def hermite_cubic_test02 ( ):

#*****************************************************************************80
#
## hermite_cubic_test02() tests hermite_cubic_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_cubic_test02():' )
  print ( '  hermite_cubic_value() evaluates a Hermite cubic polynomial.' )
  print ( '  Try out data from a cubic function:' )
  print ( '  on [0,10] and [-1.0,1.0] and [0.5,0.75]' )

  for x_interval in [ 1, 2, 3 ]:

    if ( x_interval == 1 ):
      x1 = 0.0
      x2 = 10.0
    elif ( x_interval == 2 ):
      x1 = -1.0
      x2 = +1.0
    elif ( x_interval == 3 ):
      x1 = 0.5
      x2 = 0.75

    f1, d1, s1, t1 = cubic_value ( x1 )
    f2, d2, s2, t2 = cubic_value ( x2 )

    print ( '' )
    print ( '    J      X           F           D           S           T' )

    for j in range ( -3, 13 ):
      x = ( ( 10 - j ) * x1   \
          +        j   * x2 ) \
            / 10.0

      f,  d,  s,  t  = hermite_cubic_value ( x1, f1, d1, x2, f2, d2, 1, x )
      fc, dc, sc, tc = cubic_value ( x )

      print ( '' )
      if ( j == 0 ):
        print ( '*Data  %10f  %10f  %10f' % ( x1, f1, d1 ) )
      print ( 'Exact  %10f  %10f  %10f  %10f  %10f' % (    x,  fc, dc, sc, tc ) )
      print ( '  %3d  %10f  %10f  %10f  %10f  %10f' % ( j, x,  f,  d,  s,  t ) )
      if ( j == 10 ):
        print ( '*Data  %10f  %10f  %10f' % ( x2, f2, d2 ) )

  return

def hermite_cubic_test03 ( ):

#*****************************************************************************80
#
## hermite_cubic_test03() tests hermite_cubic_integrate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_cubic_test03():' )
  print ( '  hermite_cubic_integrate() integrates a Hermite cubic' )
  print ( '  polynomial from A to B.' )

  for x_interval in [ 1, 2, 3 ]:

    if ( x_interval == 1 ):
      x1 = 0.0
      x2 = 10.0
    elif ( x_interval == 2 ):
      x1 = -1.0
      x2 = +1.0
    elif ( x_interval == 3 ):
      x1 = 0.5
      x2 = 0.75

    f1, d1, s1, t1 = cubic_value ( x1 )
    f2, d2, s2, t2 = cubic_value ( x2 )

    print ( '' )
    print ( '                                 Exact       Computed' )
    print ( '    J      A           B         Integral    Integral' )
    print ( '' )

    a = x1 - 1.0

    for j in range ( -3, 13 ):

      b = ( ( 10 - j ) * x1   \
          +        j   * x2 ) \
            / 10.0

      q_exact = cubic_integrate ( a, b )
      q_computed = hermite_cubic_integrate ( x1, f1, d1, x2, f2, d2, a, b )

      print ( '  %3d  %10f  %10f  %10.6g  %10.6g' \
        % ( j, a, b, q_exact, q_computed ) )

  return

def hermite_cubic_test04 ( ):

#*****************************************************************************80
#
## hermite_cubic_test04() tests hermite_cubic_spline_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_cubic_test04():' )
  print ( '  hermite_cubic_spline_value() evaluates a Hermite cubic spline.' )

  x1 = 0.0
  x2 = 10.0

  nn = 11
  xn = np.linspace ( x1, x2, nn )
  fn = np.sin ( xn )
  dn = np.cos ( xn )

  n = 51
  x = np.linspace ( x1, x2, n )
  f, d, s, t = hermite_cubic_spline_value ( nn, xn, fn, dn, n, x )

  print ( '' )
  print ( '     I      X       F computed     F exact      Error' )
  print ( '' )

  for i in range ( 0, n ):
    u = np.sin ( x[i] )
    v = np.abs ( f[i] - u )
    print ( '  %4d  %10f  %10f  %10f  %10.2e' % ( i, x[i], f[i], u, v ) )

  print ( '' )
  print ( '     I      X       D computed     D exact      Error' )
  print ( '' )

  for i in range ( 0, n ):
    u = np.cos ( x[i] )
    v = np.abs ( d[i] - u )
    print ( '  %4d  %10f  %10f  %10f  %10.2e' % ( i, x[i], d[i], u, v ) )

  return

def hermite_cubic_test05 ( ):

#*****************************************************************************80
#
## hermite_cubic_test05() tests hermite_cubic_to_power_cubic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_cubic_test05():' )
  print ( '  hermite_cubic_to_power_cubic() converts the Hermite data' )
  print ( '  to the coefficients of the power form of the polynomial' )
  print ( '  power_cubic_to_hermite_cubic() converts the power form' )
  print ( '  to Hermite form' )

  x1 = -1.0
  x2 = +1.0

  f1, d1, s1, t1 = cubic_value ( x1 )
  f2, d2, s2, t2 = cubic_value ( x2 )

  print ( '' )
  print ( '  Hermite data:' )
  print ( '' )
  print ( '  X1, F1, D1:  %10f  %10f  %10f' % ( x1, f1, d1 ) )
  print ( '  X2, F2, D2:  %10f  %10f  %10f' % ( x2, f2, d2 ) )

  c0, c1, c2, c3 = hermite_cubic_to_power_cubic ( x1, f1, d1, x2, f2, d2 )

  print ( '' )
  print ( '  Power form:' )
  print ( '    p(x) = %f + %f * x + %f * x^2 + %f * x^3' % ( c0, c1, c2, c3 ) )

  print ( '' )
  print ( '      X       F (Hermite)  F (power)' )
  print ( '' )

  for j in range ( - 3, 13 ):
    x = ( ( 10 - j ) * x1   \
        +        j   * x2 ) \
        / 10.0

    f, d, s, t = hermite_cubic_value ( x1, f1, d1, x2, f2, d2, 1, x )
    fp = c0 + x * ( c1 + x * ( c2 + x * c3 ) )

    print ( '  %10f  %10f  %10f' % ( x, f, fp ) )

  f1r, d1r, f2r, d2r = power_cubic_to_hermite_cubic ( c0, c1, c2, c3, x1, x2 )

  print ( '' )
  print ( '  Use power_cubic_to_hermite_cubic() to recover the' )
  print ( '  original Hermite data:' )
  print ( '' )
  print ( '         Original   Recovered' )
  print ( '' )
  print ( '  F1:  %10f  %10f' % ( f1, f1r ) )
  print ( '  D1:  %10f  %10f' % ( d1, d1r ) )
  print ( '  F2:  %10f  %10f' % ( f2, f2r ) )
  print ( '  D2:  %10f  %10f' % ( d2, d2r ) )

  return

def hermite_cubic_test06 ( ):

#*****************************************************************************80
#
#% hermite_cubic_test06() tests hermite_cubic_integrate() using vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_cubic_test06():' )
  print ( '  hermite_cubic_integrate() integrates a Hermite cubic' )
  print ( '  polynomial from A to B.' )
  print ( '  Use A, B vectors for the calculation.' )

  x1 = 0.0
  x2 = 10.0

  f1, d1, s1, t1 = cubic_value ( x1 )
  f2, d2, s2, t2 = cubic_value ( x2 )
#
#  A is a scalar, but B is a vector.
#
  n = 16
  a = ( x1 - 1.0 ) * np.ones ( n )
  b = np.linspace ( ( 13 * x1 - 3 * x2 ) / 10, ( -2 * x1 + 12 * x2 ) / 10, n )

  q_exact = cubic_integrate ( a, b )

  q_computed = hermite_cubic_integrate ( x1, f1, d1, x2, f2, d2, a, b )

  print ( '' )
  print ( '                                 Exact       Computed' )
  print ( '    J      A           B         Integral    Integral' )
  print ( '' )

  for i in range ( 0, n ):

    print ( '  %3d  %10f  %10f  %10.6g  %10.6g' \
      % ( i, a[i], b[i], q_exact[i], q_computed[i] ) )

  return

def hermite_cubic_test07 ( ):

#*****************************************************************************80
#
## hermite_cubic_test07() tests hermite_cubic_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_cubic_test07():' )
  print ( '  hermite_cubic_integral() integrates a Hermite cubic' )
  print ( '  polynomial over the definition interval [X1,X2].' )
  print ( '' )
  print ( '                            Exact       Computed' )
  print ( '     X1          X2         Integral    Integral' )
  print ( '' )

  for x_interval in [ 1, 2, 3 ]:

    if ( x_interval == 1 ):
      x1 = 0.0
      x2 = 10.0
    elif ( x_interval == 2 ):
      x1 = -1.0
      x2 = +1.0
    elif ( x_interval == 3 ):
      x1 = 0.5
      x2 = 0.75

    f1, d1, s1, t1 = cubic_value ( x1 )
    f2, d2, s2, t2 = cubic_value ( x2 )

    q_exact = cubic_integrate ( x1, x2 )
    q_computed = hermite_cubic_integral ( x1, f1, d1, x2, f2, d2 )

    print ( '  %10f  %10f  %10.6g  %10.6g' % ( x1, x2, q_exact, q_computed ) )

  return

def hermite_cubic_test08 ( ):

#*****************************************************************************80
#
## hermite_cubic_test08() tests hermite_cubic_spline_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_cubic_test08():' )
  print ( '  hermite_cubic_spline_integral() integrates a Hermite' )
  print ( '  cubic spline over the definition interval [X1,XNN].' )
  print ( '' )
  print ( '                            Exact       Computed' )
  print ( '     X1          XNN        Integral    Integral' )
  print ( '' )

  for test in [ 1, 2, 3 ]:

    if ( test == 1 ):
      nn = 11
      xn = np.linspace ( 0.0, 1.0, nn )
      fn = xn * ( 4.0 * xn - 1.0 ) * ( xn - 1.0 )
      dn = 1.0 + xn * ( - 10.0 + xn * 12.0 )
      q_exact = \
        ( xn[nn-1] * xn[nn-1] * ( 0.5 + xn[nn-1] * ( - ( 5.0 / 3.0 ) + xn[nn-1] ) ) ) \
      - ( xn[0]    * xn[0]    * ( 0.5 + xn[0]    * ( - ( 5.0 / 3.0 ) + xn[0]  ) ) )
#
#  Use variable spacing.
#
    elif ( test == 2 ):
      nn = 11
      xn = np.linspace ( 0.0, 1.0, nn )
      xn = np.sqrt ( xn )
      fn = xn * ( 4.0 * xn - 1.0 ) * ( xn - 1.0 )
      dn = 1.0 + xn * ( - 10.0 + xn * 12.0 )
      q_exact = \
        ( xn[nn-1] * xn[nn-1] * ( 0.5 + xn[nn-1] * ( - ( 5.0 / 3.0 ) + xn[nn-1] ) ) ) \
      - ( xn[0]    * xn[0]    * ( 0.5 + xn[0]    * ( - ( 5.0 / 3.0 ) + xn[0]  ) ) )
#
#  Try a non-cubic.
#
    elif ( test == 3 ):
      nn = 11
      xn = np.linspace ( 0.0, np.pi, nn )
      fn = np.sin ( xn )
      dn = np.cos ( xn )
      q_exact = - np.cos ( xn[nn-1] ) + np.cos ( xn[0] )

    q_computed = hermite_cubic_spline_integral ( nn, xn, fn, dn )

    print ( '  %10f  %10f  %10.6g  %10.6g' \
      % ( xn[0], xn[nn-1], q_exact, q_computed ) )

  return

def hermite_cubic_test09 ( ):

#*****************************************************************************80
#
#% hermite_cubic_test09() tests hermite_cubic_spline_integrate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_cubic_test09():' )
  print ( '  hermite_cubic_spline_integrate() integrates a Hermite' )
  print ( '  cubic spline from A to B.' )
#
#  Define the cubic spline.
#
  x1 = 0.0
  x2 = 10.0

  nn = 11
  xn = np.linspace ( x1, x2, nn )
  fn, dn, sn, tn = cubic_value ( xn )

  n = 25
  a = np.linspace ( 2.5, 2.5, n )
  b = np.linspace ( x1 - 1.0, x2 + 1.0, n )

  q = hermite_cubic_spline_integrate ( nn, xn, fn, dn, n, a, b )

  print ( '' )
  print ( '                                 Exact       Computed' )
  print ( '    I      A           B         Integral    Integral' )
  print ( '' )

  for i in range ( 0, n ):

    q_exact = cubic_integrate ( a[i], b[i] )

    print ( '  %3d  %10f  %10f  %10.6g  %10.6g' \
      % ( i, a[i], b[i], q_exact, q[i] ) )

  return

def hermite_cubic_test10 ( ):

#*****************************************************************************80
#
## hermite_cubic_test10() tests hermite_cubic_spline_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'hermite_cubic_test10():' )
  print ( '  hermite_cubic_spline_integral() integrates a Hermite' )
  print ( '  cubic spline over the definition interval [X1,XNN].' )
  print ( '' )
  print ( '  If the subintervals are equally spaced, the derivative' )
  print ( '  information has no effect on the result, except for' )
  print ( '  the first and last values, DN(1) and DN(NN).' )
  print ( '' )
  print ( '                            Exact       Computed' )
  print ( '     X1          XNN        Integral    Integral  Comment' )
  print ( '' )

  for test in [ 1, 2, 3, 4, 5 ]:
#
#  Equal spacing.
#
    if ( test == 1 ):
      nn = 11
      xn = np.linspace ( 0.0, np.pi, nn )
      fn = np.sin ( xn )
      dn = np.cos ( xn )
      integral_exact = - np.cos ( xn[nn-1] ) + np.cos ( xn[0] )
      comment = 'Equal spacing, correct DN'
#
#  Equal spacing, reset DN(2:NN-1) to random numbers.
#
    elif ( test == 2 ):
      nn = 11
      xn = np.linspace ( 0.0, np.pi, nn )
      fn = np.sin ( xn )
      dn = np.cos ( xn )
      dn[1:nn-1] = 1000.0 * rng.random ( nn - 2 )
      integral_exact = - np.cos ( xn[nn-1] ) + np.cos ( xn[0] )
      comment = 'Equal spacing, DN(2:N-1) random'
#
#  Equal spacing, now reset all of DN to random numbers.
#
    elif ( test == 3 ):
      nn = 11
      xn = np.linspace ( 0.0, np.pi, nn )
      fn = np.sin ( xn )
      dn = 1000.0 * rng.random ( nn )
      integral_exact = - np.cos ( xn[nn-1] ) + np.cos ( xn[0] )
      comment = 'Equal spacing, DN(1:N) random'
#
#  Variable spacing, correct data.
#
    elif ( test == 4 ):
      nn = 11
      xn = np.linspace ( 0.0, np.pi**2, nn )
      xn = np.sqrt ( xn )
      fn = np.sin ( xn )
      dn = np.cos ( xn )
      integral_exact = - np.cos ( xn[nn-1] ) + np.cos ( xn[0] )
      comment = 'Variable spacing, correct DN'
#
#  Variable spacing, change one entry in DN.
#
    elif ( test == 5 ):
      nn = 11
      xn = np.linspace ( 0.0, np.pi**2, nn )
      xn = np.sqrt ( xn )
      fn = np.sin ( xn )
      dn = np.cos ( xn )
      r = rng.random ( )
      dn[ ( nn + 1 ) // 2 ] = 1000.0 * r
      integral_exact = - np.cos ( xn[nn-1] ) + np.cos ( xn[0] )
      comment = 'Variable spacing, a single internal DN randomized.'

    integral_computed = hermite_cubic_spline_integral ( nn, xn, fn, dn )

    print ( '  %10f  %10f  %10.6g  %10.6g  %s' \
      % ( xn[0], xn[nn-1], integral_exact, integral_computed, comment ) )

  return

def hermite_cubic_test11 ( ):

#*****************************************************************************80
#
## hermite_cubic_test11() tests hermite_cubic_lagrange_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_cubic_test11():' )
  print ( '  hermite_cubic_lagrange_value() evaluates the four' )
  print ( '  Lagrange basis functions associated with F1, D1,' )
  print ( '  F2 and D2 such that' )
  print ( '' )
  print ( '  P(X) = F1 * LF1(X) + D1 * LD1(X)' )
  print ( '       + F2 * LF2(X) + D2 * LD2(X).' )
  print ( '' )
  print ( '  The first, second and third derivatives of these four' )
  print ( '  Lagrange basis functions are also computed.' )
  print ( '' )

  x1 = 1.0
  x2 = 2.0
  n = 11
  x = np.linspace ( 0.0, 2.5, n )

  f, d, s, t = hermite_cubic_lagrange_value ( x1, x2, n, x )

  print ( '' )
  print ( '  The Lagrange basis functions:' )
  print ( '' )
  print ( '     I        X           LF1         LD1         LF2         LD2' )
  print ( '' )
  for j in range ( 0, n ):
    print ( '  %4d  %10.4f  %10.4f  %10.4f  %10.4f  %10.4f' \
      % ( j, x[j], f[j,0], f[j,1], f[j,2], f[j,3] ) )

  print ( '' )
  print ( '  The derivative of the Lagrange basis functions:' )
  print ( '' )
  print ( '     I        X           LF1         LD1         LF2         LD2' )
  print ( '' )
  for j in range ( 0, n ):
    print ( '  %4d  %10.4f  %10.4f  %10.4f  %10.4f  %10.4f' \
      % ( j, x[j], d[j,0], d[j,1], d[j,2], d[j,3] ) )

  return

def hermite_cubic_test12 ( ):

#*****************************************************************************80
#
## hermite_cubic_test12() tests hermite_cubic_lagrange_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_cubic_test12():' )
  print ( '  hermite_cubic_lagrange_integral() returns the integrals' )
  print ( '  of the four Lagrange basis functions associated ' )
  print ( '  with F1, D1, F2 and D2 such that' )
  print ( '' )
  print ( '  P(X) = F1 * LF1(X) + D1 * LD1(X)' )
  print ( '       + F2 * LF2(X) + D2 * LD2(X).' )
  print ( '' )
  print ( '  The Lagrange basis function integrals:' )
  print ( '' )
  print ( '        X1          X2          LF1         LD1         LF2         LD2' )
  print ( '' )

  x2 = 1.0
  for x1 in range ( -6, 3 ):
    q = hermite_cubic_lagrange_integral ( x1, x2 )
    print ( '  %10.4f  %10.4f  %10.4f  %10.4f  %10.4f  %10.4f' \
      % ( x1, x2, q[0], q[1], q[2], q[3] ) )

  return

def hermite_cubic_test13 ( ):

#*****************************************************************************80
#
## hermite_cubic_test13() tests hermite_cubic_lagrange_integrate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_cubic_test13():' )
  print ( '  hermite_cubic_lagrange_integrate() integrates a Hermite cubic' )
  print ( '  Lagrange polynomial from A to B.' )
  print ( '' )
  print ( '  Compute each result TWICE:' )
  print ( '  First row computed using hermite_cubic_integrate().' )
  print ( '  Second row computed using hermite_cubic_lagrange_integrate().' )

  x1 = 0.0
  x2 = 10.0

  print ( '' )
  print ( '        A           B           LF1         LD1         LF2         LD2' )
  print ( '' )

  a = x1 - 1.0

  for j in range ( -3, 13 ):

    b = ( ( 10 - j ) * x1   \
        +        j   * x2 ) \
        /   10.0

    p = np.zeros ( 4 )
    p[0] = hermite_cubic_integrate ( x1, 1.0, 0.0, x2, 0.0, 0.0, a, b )
    p[1] = hermite_cubic_integrate ( x1, 0.0, 1.0, x2, 0.0, 0.0, a, b )
    p[2] = hermite_cubic_integrate ( x1, 0.0, 0.0, x2, 1.0, 0.0, a, b )
    p[3] = hermite_cubic_integrate ( x1, 0.0, 0.0, x2, 0.0, 1.0, a, b )

    q = hermite_cubic_lagrange_integrate ( x1, x2, a, b )

    print ( '  %10.4f  %10.4f  %10.4f  %10.4f  %10.4f  %10.4f' \
      % ( a, b, p[0], p[1], p[2], p[3] ) )
    print ( '                          %10.4f  %10.4f  %10.4f  %10.4f' \
      % ( q[0], q[1], q[2], q[3] ) )

  return

def hermite_cubic_test14 ( ):

#*****************************************************************************80
#
## hermite_cubic_test14() tests hermite_cubic_spline_quad_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 11

  print ( '' )
  print ( 'hermite_cubic_test14():' )
  print ( '  hermite_cubic_spline_quad_rule() returns a quadrature rule' )
  print ( '  for Hermite cubic splines.' )

  for k in [ 1, 2 ]:

    print ( '' )
    if ( k == 1 ):
      print ( '  Case 1: Random spacing' )
      r = rng.random ( n )
      x = np.zeros ( n )
      x[0] = r[0]
      for i in range ( 1, n ):
        x[i] = x[i-1] + r[i]
    elif ( k == 2 ):
      print ( '  Case 2: Uniform spacing' )
      print ( '  F(2:N-1) have equal weight.' )
      print ( '  D(2:N-1) have zero weight.' )
      x = np.linspace ( 1.0, 2.0, 11 )

    w = hermite_cubic_spline_quad_rule ( n, x )

    print ( '' )
    print ( '   I   J        X         W                Q' )
    print ( '' )

    for i in [ 0, 1 ]:

      for j in range ( 0, n ):

        fn = np.zeros ( n )
        dn = np.zeros ( n )

        if ( i == 0 ):
          fn[j] = 1.0
        else:
          dn[j] = 1.0

        q = hermite_cubic_spline_integral ( n, x, fn, dn )

        print ( '  %2d  %2d  %10f  %14f  %14f' % ( i, j, x[j], w[j,i], q ) )

  return

def hermite_cubic_test15 ( ):

#*****************************************************************************80
#
## hermite_cubic_test15() tests hermite_cubic_spline_quad_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  n = 11

  rng = default_rng ( )

  print ( '' )
  print ( 'hermite_cubic_test15():' )
  print ( '  hermite_cubic_spline_quad_rule() returns a quadrature rule' )
  print ( '  for Hermite cubic splines.' )

  r = rng.random (  n )
  x = np.zeros ( n )

  x[0] = r[0]
  for j in range ( 1, n ):
    x[j] = x[j-1] + r[j]

  print ( '' )
  print ( '  Random spacing' )
  print ( '  Number of points N = ', n )
  print ( '  Interval = [', x[0], ',', x[n-1], ']' )

  w = hermite_cubic_spline_quad_rule ( n, x )

  fn, dn, s, t = cubic_value ( x )

  q = np.dot ( w[:,0], fn ) + np.dot ( w[:,1], dn )

  q_exact = cubic_integrate ( x[0], x[n-1] )

  print ( '' )
  print ( '  Q         = ', q )
  print ( '  Q (exact) = ', q_exact )

  return

def hermite_cubic_value ( x1, f1, d1, x2, f2, d2, n, x ):

#*****************************************************************************80
#
## hermite_cubic_value() evaluates a Hermite cubic polynomial.
#
#  Discussion:
#
#    The input arguments can be vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, F1, D1, the left endpoint, function value and derivative.
#
#    real X2, F2, D2, the right endpoint, function value and derivative.
#
#    integer N, the number of sample points.
#
#    real X(N), the point at which the Hermite cubic is to be evaluated.
#
#  Output:
#
#    real F(N), D(N), S(N), T(N), the value and first three derivatives
#    of the Hermite cubic at X.
#
  h =    x2 - x1
  df = ( f2 - f1 ) / h

  c2 = - ( 2.0 * d1 - 3.0 * df + d2 ) / h
  c3 =   (       d1 - 2.0 * df + d2 ) / h / h

  dx = x - x1
  f = f1 + dx * ( d1 + dx * (       c2 + dx *       c3 ) )
  d =             d1 + dx * ( 2.0 * c2 + dx * 3.0 * c3 )
  s =                         2.0 * c2 + dx * 6.0 * c3
  t =                                         6.0 * c3

  return f, d, s, t

def hermite_cubic_to_power_cubic ( x1, f1, d1, x2, f2, d2 ):

#*****************************************************************************80
#
## hermite_cubic_to_power_cubic() converts a Hermite cubic to power form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real X1, F1, D1, the left endpoint, function value and derivative.
#
#    real X2, F2, D2, the right endpoint, function value and derivative.
#
#  Output:
#
#    real C0, C1, C2, C3, the power form of the polynomial.
#
  h =    x2 - x1
  df = ( f2 - f1 ) / h
#
#  Polynomial in terms of X - X1:
#
  c0 = f1
  c1 = d1
  c2 = - ( 2.0 * d1 - 3.0 * df + d2 ) / h
  c3 =   (       d1 - 2.0 * df + d2 ) / h / h
#
#  Shift polynomial to X.
#
  c2 = c2 - x1 * c3
  c1 = c1 - x1 * c2
  c0 = c0 - x1 * c1
  c2 = c2 - x1 * c3
  c1 = c1 - x1 * c2
  c2 = c2 - x1 * c3

  return c0, c1, c2, c3

def power_cubic_to_hermite_cubic ( c0, c1, c2, c3, x1, x2 ):

#*****************************************************************************80
#
## power_cubic_to_hermite_cubic() converts a power cubic to Hermite form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Fred Fritsch, Ralph Carlson,
#    Monotone Piecewise Cubic Interpolation,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 2, April 1980, pages 238-246.
#
#  Input:
#
#    real C0, C1, C2, C3, the power form of the polynomial.
#
#    real X1, X2, the left and right endpoints of the Hermite form.
#
#  Output:
#
#    real F1, D1, the function and derivative values at X1.
#
#    real F2, D2, the function and derivative values at X2.
#
  f1 = c0 + x1 * ( c1 + x1 * (       c2 + x1       * c3 ) )
  d1 =             c1 + x1 * ( 2.0 * c2 + x1 * 3.0 * c3 )

  f2 = c0 + x2 * ( c1 + x2 * (       c2 + x2       * c3 ) )
  d2 =             c1 + x2 * ( 2.0 * c2 + x2 * 3.0 * c3 )

  return f1, d1, f2, d2

def r8vec_bracket5 ( nd, xd, xi ):

#*****************************************************************************80
#
## r8vec_bracket5() brackets data between successive entries of a sorted R8VEC.
#
#  Discussion:
#
#    We assume XD is sorted.
#
#    If XI is contained in the interval [XD(1),XD(N)], then the returned 
#    value B indicates that XI is contained in [ XD(B), XD(B+1) ].
#
#    If XI is not contained in the interval [XD(1),XD(N)], then B = -1.
#
#    This code implements a version of binary search which is perhaps more
#    understandable than the usual ones.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data values.
#
#    real XD(N), the sorted data.
#
#    real XD, the query value.
#
#  Output:
#
#    integer B: xi is assigned to interval (xd[b],xd[b+1]).
#
  import numpy as np
#
#  Assign very left values to ( xd[0], xd[1] )
#
  if ( xi <= xd[0] ):

    b = 0
#
#  Assign very right values to ( xd[nd-2], xd[nd-1] )
#
  elif ( xd[nd-1] <= xi ):

    b = nd - 2
#
#  We assume xd[0] < xi < xd[nd-1].
#
  else:

    l = 0
    r = nd - 1

    while ( l + 1 < r ):
      m = ( l + r ) // 2
      if ( xi < xd[m] ):
        r = m
      else:
        l = m

    b = l

  return b

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
  hermite_cubic_test ( )
  timestamp ( )

