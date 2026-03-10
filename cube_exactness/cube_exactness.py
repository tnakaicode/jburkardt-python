#! /usr/bin/env python3
#
def cube_exactness_test ( ):

#*****************************************************************************80
#
## cube_exactness_test() tests cube_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cube_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cube_exactness().' )

  cube_exactness_test01 ( )
  cube_exactness_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cube_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def cube_exactness_test01 ( ):

#*****************************************************************************80
#
## cube_exactness_test01() tests product Gauss-Legendre rules for the Legendre 3D integral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = np.array ( [ -1.0, -1.0, -1.0 ] )
  b = np.array ( [  1.0,  1.0,  1.0 ] )

  print ( '' )
  print ( 'cube_exactness_test01():' )
  print ( '  Product Gauss-Legendre rules for the 3D Legendre integral.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '          -1 <= y <= +1.' )
  print ( '          -1 <= z <= +1.' )
  print ( '  Level: L' )
  print ( '  Exactness: 2*L+1' )
  print ( '  Order: N = (L+1)*(L+1)*(L+1)' )

  for l in range ( 0, 6 ):

    nx = l + 1
    ny = l + 1
    nz = l + 1
    n = nx * ny * nz
    t = 2 * l + 1

    x, y, z, w = legendre_3d_set ( a, b, nx, ny, nz )

    p_max = t + 1
    legendre_3d_exactness ( a, b, n, x, y, z, w, p_max )

  return

def cube_exactness_test02 ( ):

#*****************************************************************************80
#
## cube_exactness_test02() tests product Gauss-Legendre rules for the Legendre 3D integral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = np.array ( [ -1.0, -1.0, -1.0 ] )
  b = np.array ( [  1.0,  1.0,  1.0 ] )

  print ( '' )
  print ( 'cube_exactness_test02():' )
  print ( '  Product Gauss-Legendre rules for the 3D Legendre integral.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '          -1 <= y <= +1.' )
  print ( '          -1 <= z <= +1.' )
  print ( '  Exactness: 3 = 2 * min ( 2, 3, 4 ) - 1' )
  print ( '  Order: N = 2 * 3 * 4' )

  nx = 2
  ny = 3
  nz = 4
  n = nx * ny * nz

  x, y, z, w = legendre_3d_set ( a, b, nx, ny, nz )

  p_max = 4

  legendre_3d_exactness ( a, b, n, x, y, z, w, p_max )

  return

def legendre_3d_exactness ( a, b, n, x, y, z, w, t ):

#*****************************************************************************80
#
## legendre_3d_exactness(): monomial exactness for the 3D Legendre integral.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[2], the lower limits of integration.
#
#    real B[2], the upper limits of integration.
#
#    integer N, the number of points in the rule.
#
#    real X(N), Y(N), Z(N), the quadrature points.
#
#    real W(N), the quadrature weights.
#
#    integer T, the maximum total degree.
#    0 <= T.
#
  import numpy as np

  p = np.zeros ( 3 )

  print ( '' )
  print ( '  Quadrature rule for the 3D Legendre integral.' )
  print ( '  Number of points in rule is ', n )
  print ( '' )
  print ( '   D   I       J       K          Relative Error' )

  for tt in range ( 0, t + 1 ):

    print ( '  %2d' % ( tt ) )

    for k in range ( 0, tt + 1 ):

      for j in range ( 0, tt - k + 1 ):

        i = tt - j - k

        p[0] = i
        p[1] = j
        p[2] = k

        s = legendre_3d_monomial_integral ( a, b, p )

        v = x ** p[0] * y ** p[1] * z ** p[2]

        q = np.dot ( w, v )

        if ( s == 0.0 ):
          e = np.abs ( q )
        else:
          e = np.abs ( q - s ) / np.abs ( s )

        print ( '  %6d  %6d  %6d  %24.16f' % ( p[0], p[1], p[2], e ) )

  return

def legendre_3d_monomial_integral ( a, b, p ):

#*****************************************************************************80
#
## legendre_3d_monomial_integral() the Legendre integral of a monomial.
#
#  Discussion:
#
#    The Legendre integral to be evaluated has the form
#
#      I(f) = integral ( z1 <= z <= z2 )
#             integral ( y1 <= y <= y2 ) 
#             integral ( x1 <= x <= x2 ) x^i y^j z^k dx dy dz
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[2], the lower limits of integration.
#
#    real B[2], the upper limits of integration.
#
#    integer P[2], the exponents of X and Y.
#
#  Output:
#
#    real VALUE, the value of the exact integral.
#
  value = ( b[0] ** ( p[0] + 1 ) - a[0] ** ( p[0] + 1 ) ) / ( p[0] + 1 ) \
        * ( b[1] ** ( p[1] + 1 ) - a[1] ** ( p[1] + 1 ) ) / ( p[1] + 1 ) \
        * ( b[2] ** ( p[2] + 1 ) - a[2] ** ( p[2] + 1 ) ) / ( p[2] + 1 )

  return value

def legendre_3d_set ( a, b, nx, ny, nz ):

#*****************************************************************************80
#
## legendre_3d_set(): set a 3D Gauss-Legendre quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( z1 <= z <= z2 )
#               ( y1 <= y <= y2 ) 
#               ( x1 <= x <= x2 ) f(x,y,z) dx dy dz
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w[i] * f ( x[i],y[i],z[i] )
#
#    where n = nx * ny * nz.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[2], B[2], the lower and upper integration
#    limits.
#
#    integer NX, NY, NZ, the orders in the X and Y directions.
#    These orders must be between 1 and 10.
#
#  Output:
#
#    real X(N), Y(N), Z(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
#
#  Get the rules for [-1,+1].
#
  xx, wx = legendre_set ( nx )
  yy, wy = legendre_set ( ny )
  zz, wz = legendre_set ( nz )
#
#  Adjust from [-1,+1] to [A,B].
#
  for i in range ( 0, nx ):
    xx[i] = ( ( 1.0 - xx[i] ) * a[0]   \
            + ( 1.0 + xx[i] ) * b[0] ) \
            /   2.0
    wx[i] = wx[i] * ( b[0] - a[0] ) / 2.0

  for j in range ( 0, ny ):
    yy[j] = ( ( 1.0 - yy[j] ) * a[1]   \
            + ( 1.0 + yy[j] ) * b[1] ) \
            /   2.0
    wy[j] = wy[j] * ( b[1] - a[1] ) / 2.0

  for k in range ( 0, nz ):
    zz[k] = ( ( 1.0 - zz[k] ) * a[2]   \
            + ( 1.0 + zz[k] ) * b[2] ) \
            /   2.0
    wz[k] = wz[k] * ( b[2] - a[2] ) / 2.0
#
#  Compute the product rule.
#
  n = nx * ny * nz

  x = np.zeros ( n )
  y = np.zeros ( n )
  z = np.zeros ( n )
  w = np.zeros ( n )

  l = 0
  for k in range ( 0, nz ):
    for j in range ( 0, ny ):
      for i in range ( 0, nx ):
        x[l] = xx[i]
        y[l] = yy[j]
        z[l] = zz[k]
        w[l] = wx[i] * wy[j] * wz[k]
        l = l + 1

  return x, y, z, w

def legendre_set ( n ):

#*****************************************************************************80
#
## legendre_set() sets abscissas and weights for Gauss-Legendre quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    Quadrature rule:
#
#      Sum ( 1 <= I <= N ) W[i] * F ( X[i] )
#
#    The quadrature rule will is exact for all polynomials through degree 2*N-1.
#
#    The abscissas are the zeroes of the Legendre polynomial P(N)(X).
#
#    Mathematica can compute the abscissas and weights of a Gauss-Legendre
#    rule of order N for the interval [A,B] with P digits of precision
#    by the commands:
#
#    Needs["NumericalDifferentialEquationAnalysis`"]
#    GaussianQuadratureWeights [ n, a, b, p ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
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
#    Vladimir Krylov,
#    Approximate Calculation of Integrals,
#    Dover, 2006,
#    ISBN: 0486445798,
#    LC: QA311.K713.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 33 or 63/64/65, 127/128/129, 
#    255/256/257.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           0.000000000000000000000000000000 ] )

    w = np.array ( [ \
           2.000000000000000000000000000000 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           -0.577350269189625764509148780502, \
           0.577350269189625764509148780502 ] )

    w = np.array ( [ \
           1.000000000000000000000000000000, \
           1.000000000000000000000000000000 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           -0.774596669241483377035853079956, \
           0.000000000000000000000000000000, \
           0.774596669241483377035853079956 ] )

    w = np.array ( [ \
           0.555555555555555555555555555556, \
           0.888888888888888888888888888889, \
           0.555555555555555555555555555556 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           -0.861136311594052575223946488893, \
           -0.339981043584856264802665759103, \
           0.339981043584856264802665759103, \
           0.861136311594052575223946488893 ] )

    w = np.array ( [ \
           0.347854845137453857373063949222, \
           0.652145154862546142626936050778, \
           0.652145154862546142626936050778, \
           0.347854845137453857373063949222 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           -0.906179845938663992797626878299, \
           -0.538469310105683091036314420700, \
           0.000000000000000000000000000000, \
           0.538469310105683091036314420700, \
           0.906179845938663992797626878299 ] )

    w = np.array ( [ \
           0.236926885056189087514264040720, \
           0.478628670499366468041291514836, \
           0.568888888888888888888888888889, \
           0.478628670499366468041291514836, \
           0.236926885056189087514264040720 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           -0.932469514203152027812301554494, \
           -0.661209386466264513661399595020, \
           -0.238619186083196908630501721681, \
           0.238619186083196908630501721681, \
           0.661209386466264513661399595020, \
           0.932469514203152027812301554494 ] )

    w = np.array ( [ \
           0.171324492379170345040296142173, \
           0.360761573048138607569833513838, \
           0.467913934572691047389870343990, \
           0.467913934572691047389870343990, \
           0.360761573048138607569833513838, \
           0.171324492379170345040296142173 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           -0.949107912342758524526189684048, \
           -0.741531185599394439863864773281, \
           -0.405845151377397166906606412077, \
           0.000000000000000000000000000000, \
           0.405845151377397166906606412077, \
           0.741531185599394439863864773281, \
           0.949107912342758524526189684048 ] )

    w = np.array ( [ \
           0.129484966168869693270611432679, \
           0.279705391489276667901467771424, \
           0.381830050505118944950369775489, \
           0.417959183673469387755102040816, \
           0.381830050505118944950369775489, \
           0.279705391489276667901467771424, \
           0.129484966168869693270611432679 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           -0.960289856497536231683560868569, \
           -0.796666477413626739591553936476, \
           -0.525532409916328985817739049189, \
           -0.183434642495649804939476142360, \
           0.183434642495649804939476142360, \
           0.525532409916328985817739049189, \
           0.796666477413626739591553936476, \
           0.960289856497536231683560868569 ] )

    w = np.array ( [ \
           0.101228536290376259152531354310, \
           0.222381034453374470544355994426, \
           0.313706645877887287337962201987, \
           0.362683783378361982965150449277, \
           0.362683783378361982965150449277, \
           0.313706645877887287337962201987, \
           0.222381034453374470544355994426, \
           0.101228536290376259152531354310 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           -0.968160239507626089835576203, \
           -0.836031107326635794299429788, \
           -0.613371432700590397308702039, \
           -0.324253423403808929038538015, \
           0.000000000000000000000000000, \
           0.324253423403808929038538015, \
           0.613371432700590397308702039, \
           0.836031107326635794299429788, \
           0.968160239507626089835576203 ] )

    w = np.array ( [ \
           0.081274388361574411971892158111, \
           0.18064816069485740405847203124, \
           0.26061069640293546231874286942, \
           0.31234707704000284006863040658, \
           0.33023935500125976316452506929, \
           0.31234707704000284006863040658, \
           0.26061069640293546231874286942, \
           0.18064816069485740405847203124, \
           0.081274388361574411971892158111 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
           -0.973906528517171720077964012, \
           -0.865063366688984510732096688, \
           -0.679409568299024406234327365, \
           -0.433395394129247190799265943, \
           -0.148874338981631210884826001, \
           0.148874338981631210884826001, \
           0.433395394129247190799265943, \
           0.679409568299024406234327365, \
           0.865063366688984510732096688, \
           0.973906528517171720077964012 ] )

    w = np.array ( [ \
           0.066671344308688137593568809893, \
           0.14945134915058059314577633966, \
           0.21908636251598204399553493423, \
           0.26926671930999635509122692157, \
           0.29552422471475287017389299465, \
           0.29552422471475287017389299465, \
           0.26926671930999635509122692157, \
           0.21908636251598204399553493423, \
           0.14945134915058059314577633966, \
           0.066671344308688137593568809893 ] )
  else:

    print ( '' )
    print ( 'legendre_set(): Fatal error!' )
    print ( '  Illegal value of N.' )
    raise Exception ( 'legendre_set(): Fatal error!' )

  return x, w

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
  cube_exactness_test ( )
  timestamp ( )




