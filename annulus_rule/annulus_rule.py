#! /usr/bin/env python3
#
def annulus_area ( center, r1, r2 ):

#*****************************************************************************80
#
## annulus_area() computes the area of a circular annulus in 2D.
#
#  Discussion:
#
#    A circular annulus with center (XC,YC), inner radius R1 and
#    outer radius R2, is the set of points (X,Y) so that
#
#      R1^2 <= (X-XC)^2 + (Y-YC)^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CENTER(2), the coordinates of the center.
#    This data is actually not necessary for area calculations.
#
#    real R1, R2, the inner and outer radii of the annulus.
#    0.0 <= R1 <= R2.
#
#  Output:
#
#    real AREA, the area of the annulus.
#
  import numpy as np

  if ( r1 < 0.0 ):
    print ( '' )
    print ( 'annulus_area - Fatal error!' )
    print ( '  Inner radius R1 < 0.0.' )
    raise Exception ( 'annulus_area - Fatal error!' )

  if ( r2 < r1 ):
    print ( '' )
    print ( 'annulus_area - Fatal error!' )
    print ( '  Outer radius R1 < R1 = inner radius.' )
    raise Exception ( 'annulus_area - Fatal error!' )

  area = np.pi * ( r2 + r1 ) * ( r2 - r1 )

  return area

def annulus_area_test ( ):

#*****************************************************************************80
#
## annulus_area_test() test annulus_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'annulus_area_test():' )
  print ( '  annulus_area() computes the area of an annulus with' )
  print ( '  center = (CX,CY), inner radius R1 and outer radius R2.' )
  print ( '' )
  print ( '  (   CX        CY     )    R1         R2         Area' )
  print ( '' )

  center = np.zeros ( 2 )

  for i in range ( 0, 10 ):
    data = rng.random ( size = 4 )
    center[0] = 10.0 * data[0] - 5.0
    center[1] = 10.0 * data[1] - 5.0
    r1 = data[2]
    r2 = r1 + data[3]
    area = annulus_area ( center, r1, r2 )
    print ( '  (%9.6f,%9.6f)  %9.6f  %9.6f  %9.6f' \
      % ( center[0], center[1], r1, r2, area ) )

  return

def annulus_rule_compute ( center, r1, r2, nr, nt ):

#*****************************************************************************80
#
## annulus_rule_compute() computes a quadrature rule for an annulus.
#
#  Discussion:
#
#    The integration region is points (X,Y) such that
#
#      R1^2 <= ( X - CENTER(1) )^2 + ( Y - CENTER(2) )^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Peirce,
#    Numerical Integration Over the Planar Annulus,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 5, Issue 2, June 1957, pages 66-73.
#
#  Input:
#
#    real CENTER(2), the center of the annulus.
#
#    real R1, R2, the inner and outer radius.
#
#    integer NR, the number of points in the radial rule.
#
#    integer NT, the number of angles to use.
#    The value NT=4*NR is recommended.
#
#  Output:
#
#    real W(NR*NT), the weights for the rule.
#
#    real X(NR*NT), Y(NR*NT), the points for the rule.
#
  import numpy as np
#
#  Get the Legendre rule for [-1,+1].
#
  ra, rw = legendre_ek_compute ( nr )
#
#  Adjust the rule from [-1,+1] to [r1^2,r2^2].
#
  a = -1.0
  b = +1.0
  c = r1 * r1
  d = r2 * r2
  ra, rw = rule_adjust ( a, b, c, d, nr, ra, rw )
#
#  Convert from R^2 to R.
#
  ra = np.sqrt ( ra )
  rw = rw / ( r2 + r1 ) / ( r2 - r1 )
#
#  Set the angular weight.
#
  tw = 1.0 / nt
#
#  Get area of annulus.
#
  area = annulus_area ( center, r1, r2 )
#
#  Form the abscissa and weight vectors.
#
  x = np.zeros ( nr * nt )
  y = np.zeros ( nr * nt )
  w = np.zeros ( nr * nt )

  k = 0
  for i in range ( 0, nt ):
    t = 2.0 * np.pi * float ( i ) / float ( nt )
    for j in range ( 0, nr ):
      x[k] = center[0] + ra[j] * np.cos ( t )
      y[k] = center[1] + ra[j] * np.sin ( t )
      w[k] = area * tw * rw[j]
      k = k + 1

  return w, x, y

def annulus_rule_compute_test ( ):

#*****************************************************************************80
#
## annulus_rule_compute_test() tests annulus_rule_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'annulus_rule_compute_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test annulus_rule_compute().' )

  center = np.array ( [ 0.0, 0.0 ] )
  r1 = 0.5
  r2 = 1.0
  nr = 3
  nt = 12

  w, x, y = annulus_rule_compute ( center, r1, r2, nr, nt )

  r8vec3_print ( nr * nt, w, x, y, '  W, X, Y for annulus quadrature:' )

  return

def annulus_rule_monomial_test ( center, r1, r2 ):

#*****************************************************************************80
#
## annulus_rule_monomial_test() estimates monomial integrals using quadrature.
#
#  Discussion:
#
#    If CENTER=(0,0) and R1 = 0 and R2 = 1, then we can compare exact values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CENTER(2), the coordinates of the center.
#
#    real R1, R2, the inner and outer radii of the annulus.
#    0.0 <= R1 <= R2.
#
  import numpy as np
  import platform

  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 2, 0 ], \
    [ 0, 2 ], \
    [ 4, 0 ], \
    [ 2, 2 ], \
    [ 0, 4 ], \
    [ 6, 0 ] ] )

  print ( '' )
  print ( 'annulus_rule_monomial_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  annulus_rule_compute() can supply a quadrature rule for' )
  print ( '  the annulus centered at (%g,%g) with R1 = %g, R2 = %g' \
    % ( center[0], center[1], r1, r2 ) )
  print ( '  Apply this rule to a variety of monomials.' )

  print ( '' )
  print ( '    NR    NT           1              X^2             Y^2             X^4               X^2Y^2           Y^4             X^6' )
  print ( '' )

  nr = 4
  
  while ( nr <= 64 ):

    nt = 4 * nr
    n = nr * nt

    w, x, y = annulus_rule_compute ( center, r1, r2, nr, nt )

    xy = np.zeros ( [ 2, n ] )
    xy[0,:] = x[:]
    xy[1,:] = y[:]

    print ( '  %4d  %4d' % ( nr, nt ), end = '' )
 
    for i in range ( 0, 7 ):
      e = e_test[i,:]
      value = monomial_value ( 2, n, e, xy )
      result = np.sum ( w[:] * value[:] )
      print ( '  %14.6g' % ( result ), end = '' )
    print ( '' )

    nr = 2 * nr

  if ( \
    center[0] == 0.0 and \
    center[1] == 0.0 and \
    r1 == 0.0 and \
    r2 == 1.0 ):
    print ( '' )
    print ( '     Exact  ', end = '' )
    for i in range ( 0, 7 ):
      e = e_test[i,:]
      result = disk01_monomial_integral ( e )
      print ( '  %14.6g' % ( result ), end = '' )
    print ( '' )

  return

def annulus_rule_test ( ):

#*****************************************************************************80
#
## annulus_rule_test() tests annulus_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'annulus_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test annulus_rule().' )

  annulus_area_test ( )
  annulus_rule_compute_test ( )

  center = np.array ( [ 0.0, 0.0 ] )
  r1 = 0.0
  r2 = 1.0
  annulus_rule_monomial_test ( center, r1, r2 )

  center = np.array( [ 0.0, 0.0 ] )
  r1 = 0.5
  r2 = 1.0
  annulus_rule_monomial_test ( center, r1, r2 )

  center = np.array ( [ 1.0, 0.0 ] )
  r1 = 0.0
  r2 = 1.0
  annulus_rule_monomial_test ( center, r1, r2 )

  rule_adjust_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'annulus_rule_test():' )
  print ( '  Normal end of execution.' )
  return

def disk01_monomial_integral ( e ):

#*****************************************************************************80
#
## disk01_monomial_integral() returns monomial integrals in the unit disk.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E(2), the exponents of X and Y in the 
#    monomial.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma

  r = 1.0

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'disk01_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'disk01_monomial_integral - Fatal error!' )

  if ( ( ( e[0] % 2 ) == 1 ) or ( ( e[1] % 2 ) == 1 ) ):

    integral = 0.0

  else:

    integral = 2.0

    for i in range ( 0, 2 ):
      arg = 0.5 * float ( e[i] + 1 )
      integral = integral * gamma ( arg )

    arg = 0.5 * float ( e[0] + e[1] + 2 )
    integral = integral / gamma ( arg )
#
#  The surface integral is now adjusted to give the volume integral.
#
  s = e[0] + e[1] + 2

  integral = integral * r ** s / float ( s )

  return integral

def imtqlx ( n, d, e, z ):

#*****************************************************************************80
#
## imtqlx() diagonalizes a symmetric tridiagonal matrix.
#
#  Discussion:
#
#    This routine is a slightly modified version of the EISPACK routine to
#    perform the implicit QL algorithm on a symmetric tridiagonal matrix.
#
#    The authors thank the authors of EISPACK for permission to use this
#    routine.
#
#    It has been modified to produce the product Q' * Z, where Z is an input
#    vector and Q is the orthogonal matrix diagonalizing the input matrix.
#    The changes consist (essentially) of applying the orthogonal 
#    transformations directly to Z as they are generated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#    Roger Martin, James Wilkinson,
#    The Implicit QL Algorithm,
#    Numerische Mathematik,
#    Volume 12, Number 5, December 1968, pages 377-383.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real D(N), the diagonal entries of the matrix.
#
#    real E(N), the subdiagonal entries of the
#    matrix, in entries E(1) through E(N-1). 
#
#    real Z(N), a vector to be operated on.
#
#  Output:
#
#    real LAM(N), the diagonal entries of the diagonalized matrix.
#
#    real QTZ(N), the value of Q' * Z, where Q is the matrix that 
#    diagonalizes the input symmetric tridiagonal matrix.
#
  import numpy as np

  lam = np.zeros ( n )
  for i in range ( 0, n ):
    lam[i] = d[i]

  qtz = np.zeros ( n )
  for i in range ( 0, n ):
    qtz[i] = z[i]

  if ( n == 1 ):
    return lam, qtz

  itn = 30

  prec = 2.220446049250313E-016

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= prec * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
          break

      p = lam[l-1]

      if ( m == l ):
        break

      if ( itn <= j ):
        print ( '' )
        print ( 'imtqlx - Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'imtqlx - Fatal error!' )

      j = j + 1
      g = ( lam[l] - p ) / ( 2.0 * e[l-1] )
      r = np.sqrt ( g * g + 1.0 )

      if ( g < 0.0 ):
        t = g - r
      else:
        t = g + r

      g = lam[m-1] - p + e[l-1] / ( g + t )
 
      s = 1.0
      c = 1.0
      p = 0.0
      mml = m - l

      for ii in range ( 1, mml + 1 ):

        i = m - ii
        f = s * e[i-1]
        b = c * e[i-1]

        if ( abs ( g ) <= abs ( f ) ):
          c = g / f
          r = np.sqrt ( c * c + 1.0 )
          e[i] = f * r
          s = 1.0 / r
          c = c * s
        else:
          s = f / g
          r = np.sqrt ( s * s + 1.0 )
          e[i] = g * r
          c = 1.0 / r
          s = s * c

        g = lam[i] - p
        r = ( lam[i-1] - g ) * s + 2.0 * c * b
        p = s * r
        lam[i] = g + p
        g = c * r - b
        f = qtz[i]
        qtz[i]   = s * qtz[i-1] + c * f
        qtz[i-1] = c * qtz[i-1] - s * f

      lam[l-1] = lam[l-1] - p
      e[l-1] = g
      e[m-1] = 0.0

  for ii in range ( 2, n + 1 ):

     i = ii - 1
     k = i
     p = lam[i-1]

     for j in range ( ii, n + 1 ):

       if ( lam[j-1] < p ):
         k = j
         p = lam[j-1]

     if ( k != i ):

       lam[k-1] = lam[i-1]
       lam[i-1] = p

       p        = qtz[i-1]
       qtz[i-1] = qtz[k-1]
       qtz[k-1] = p

  return lam, qtz

def imtqlx_test ( ):

#*****************************************************************************80
#
## imtqlx_test() tests imtqlx().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'imtqlx_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  imtqlx() takes a symmetric tridiagonal matrix A' )
  print ( '  and computes its eigenvalues LAM.' )
  print ( '  It also accepts a vector Z and computes Q\'*Z,' )
  print ( '  where Q is the matrix that diagonalizes A.' )

  n = 5
  d = np.zeros ( n )
  for i in range ( 0, n ):
    d[i] = 2.0;
  e = np.zeros ( n )
  for i in range ( 0, n - 1 ):
    e[i] = -1.0
  e[n-1] = 0.0
  z = np.ones ( n )

  lam, qtz = imtqlx ( n, d, e, z )

  r8vec_print ( n, lam, '  Computed eigenvalues:' )

  lam2 = np.zeros ( n )
  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam2[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  r8vec_print ( n, lam2, '  Exact eigenvalues:' )

  r8vec_print ( n, z, '  Vector Z:' )
  r8vec_print ( n, qtz, '  Vector Q''*Z:' )

  return

def legendre_ek_compute ( n ):

#*****************************************************************************80
#
## legendre_ek_compute(): Gauss-Legendre, Elhay-Kautsky method.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 < x < +1 ) f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = 2.0
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    ip1_r8 = float ( i + 1 )
    bj[i] = ip1_r8 * ip1_r8 / ( 4.0 * ip1_r8 * ip1_r8 - 1.0 )
    bj[i] = np.sqrt ( bj[i] )

  x = np.zeros ( n )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def legendre_ek_compute_test ( ):

#*****************************************************************************80
#
## legendre_ek_compute_test() tests legendre_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_ek_compute_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  legendre_ek_compute() computes' )
  print ( '  a Legendre quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = legendre_ek_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def monomial_value ( m, n, e, x ):

#*****************************************************************************80
#
## monomial_value() evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= m ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer E(M), the exponents.
#
#    real X(M,N), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( 0 != e[i] ):
      for j in range ( 0, n ):
        v[j] = v[j] * x[i,j] ** e[i]

  return v

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

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec3_print ( n, a1, a2, a3, title ):

#*****************************************************************************80
#
## r8vec3_print() prints an R8VEC3.
#
#  Discussion:
#
#    An R8VEC3 is a dataset consisting of 3 vectors of N real values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), A3(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g  %12g' % ( i, a1[i], a2[i], a3[i] ) )

  return

def r8vec3_print_test ( ):

#*****************************************************************************80
#
## r8vec3_print_test() tests r8vec3_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec3_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec3_print() prints an R8VEC.' )

  n = 6

  t = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  u = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  v = np.array ( [ 0.0, 0.24, 0.56, 0.96, 1.44, 2.0 ], dtype = np.float64 )

  r8vec3_print ( n, t, u, v, '  X, X^2, X+X^2\'s:' )

  return

def rule_adjust ( a, b, c, d, norder, x, w ):

#*****************************************************************************80
#
## rule_adjust() maps a quadrature rule from [A,B] to [C,D].
#
#  Discussion:
#
#    Most quadrature rules are defined on a special interval, like
#    [-1,1] or [0,1].  To integrate over an interval, the abscissas
#    and weights must be adjusted.  This can be done on the fly,
#    or by calling this routine.
#
#    If the weight function W(X) is not 1, then the W vector will
#    require further adjustment by the user.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the definition interval.
#
#    real C, D, the endpoints of the integration interval.
#
#    integer NORDER, the number of abscissas and weights.
#
#    real X(NORDER), W(NORDER), the abscissas
#    and weights defined on [A,B].
#
#  Output:
#
#    real X_NEW(NORDER), W_NEW(NORDER), the abscissas
#    and weights, redefined on [C,D].
#
  x_new = \
    ( ( b - x[:]     ) * c   \
    + (     x[:] - a ) * d ) \
    / ( b        - a )

  w_new = ( ( d - c ) / ( b - a ) ) * w[:]

  return x_new, w_new

def rule_adjust_test ( ):

#*****************************************************************************80
#
## rule_adjust_test() tests rule_adjust().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rule_adjust_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rule_adjust() adjusts a quadrature rule from [A,B] to [C,D].' )

  n = 7

  x = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
    angle = np.pi * float ( n - i ) / float ( n + 1 )
    w[i] = np.pi / float ( n + 1 ) * ( np.sin ( angle ) ) ** 2
    x[i] = np.cos ( angle )

  r8vec2_print ( n, w, x, '  W, X defined on [-1,+1]' )

  a = - 1.0;
  b = + 1.0;

  c = 0.0;
  d = +1.0;
  [ x_new, w_new ] = rule_adjust ( a, b, c, d, n, x, w )

  r8vec2_print ( n, w_new, x_new, '  W, X adjusted to [0,1]' )

  return

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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  annulus_rule_test ( )
  timestamp ( )

