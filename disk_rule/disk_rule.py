#! /usr/bin/env python3
#
def disk01_area ( ):

#*****************************************************************************80
#
## disk01_area() returns the area of the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real AREA, the area of the unit disk.
#
  import numpy as np

  r = 1.0
  value = np.pi * r * r

  return value

def disk01_area_test ( ) :

#*****************************************************************************80
#
## disk01_area_test() tests disk01_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'disk01_area_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  disk01_area returns the area of the unit disk.' )

  value = disk01_area ( )

  print ( '' )
  print ( '  disk01_area() = %g' % ( value ) )

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
    print ( 'disk01_monomial_integral(): Fatal error!' )
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

def disk01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## disk01_integral_test uses disk01_sample() to estimate various integrals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 2
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'disk01_monomial_integral_test()' )
  print ( '  disk01_monomial_integral() computes monomial integrals' )
  print ( '  over the interior of the unit disk in 2D.' )
  print ( '  Compare with a Monte Carlo value.' )
#
#  Get sample points.
#
  x = disk01_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose X,Y exponents between 0 and 8.
#
  print ( '' )
  print ( '  If any exponent is odd, the integral is zero.' )
  print ( '  We will restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    e[0] = e[0] * 2
    e[1] = e[1] * 2

    value = monomial_value ( m, n, e, x )

    result = disk01_area ( ) * np.sum ( value ) / float ( n )
    exact = disk01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], result, exact, error ) )

  return

def disk01_rule ( nr, nt ):

#*****************************************************************************80
#
## disk01_rule() computes a quadrature rule for the unit disk.
#
#  Discussion:
#
#    The unit disk is the region:
#
#      x * x + y * y <= 1.
#
#    The integral I(f) is then approximated by
#
#      Q(f) = pi * sum ( 1 <= j <= NT ) sum ( 1 <= i <= NR ) 
#        W(i) * F ( R(i) * cos(T(j)), R(i) * sin(T(j)) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NR, the number of points in the radial rule.
#
#    integer NT, the number of angles to use.
#
#  Output:
#
#    real W(NR), the weights for the disk rule.
#
#    real R(NR), T(NT), the (R,Theta) points for the rule.
#
  import numpy as np
#
#  Request a Legendre rule for [-1,+1].
#
  xr, wr = legendre_ek_compute ( nr )
#
#  Shift the rule to [0,1].
#
  for i in range ( 0, nr ):
    xr[i] = ( xr[i] + 1.0 ) / 2.0
    wr[i] = wr[i] / 2.0
#
#  Compute the disk rule.
#
  w = np.zeros ( nr )
  r = np.zeros ( nr )
  t = np.zeros ( nt )

  for it in range ( 0, nt ):
    t[it] = 2.0 * np.pi * float ( it ) / float ( nt )

  for ir in range ( 0, nr ):
    w[ir] = wr[ir] / float ( nt )
    r[ir] = np.sqrt ( xr[ir] )

  return w, r, t

def disk01_rule_test ( ):

#*****************************************************************************80
#
## disk01_rule_test() tests disk01_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nr = 4
  nt = 8

  print ( '' )
  print ( 'disk01_rule_test()' )
  print ( '  disk01_rule() computes a rule Q(f) for the unit disk' )
  print ( '  using NT equally spaced angles and NR radial distances.' )
  print ( '' )
  print ( '  NT = %d' % ( nt ) )
  print ( '  NR = %d' % ( nr ) )
  print ( '' )
  print ( '  Estimate integrals I(f) where f = x^e(1) * y^e(2).' )
#
#  Compute the quadrature rule.
#
  w, r, t = disk01_rule ( nr, nt )
#
#  Apply it to integrands.
#
  print ( '' )
  print ( '  E(1)  E(2)    I(f)            Q(f)' )
  print ( '' )
#
#  Specify a monomial.
#
  e = np.zeros ( 2 )

  for e1 in range ( 0, 7, 2 ):

    e[0] = e1

    for e2 in range ( e1, 7, 2 ):

      e[1] = e2

      q = 0.0
      for j in range ( 0, nt ):
        for i in range ( 0, nr ):
          x = r[i] * np.cos ( t[j] )
          y = r[i] * np.sin ( t[j] )
          q = q + w[i] * x ** e[0] * y ** e[1]

      q = np.pi * q

      exact = disk01_monomial_integral ( e )

      print ( '   %2d  %2d  %14.6g  %14.6g' % ( e[0], e[1], exact, q ) )

  return

def disk01_sample ( n, rng ):

#*****************************************************************************80
#
## disk01_sample() uniformly samples the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(2,N), the points.
#
  import numpy as np

  x = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
#
#  Fill a vector with normally distributed values.
#
    v = rng.standard_normal ( size = 2 )
#
#  Compute the length of the vector.
#
    norm = np.sqrt ( v[0] ** 2 + v[1] ** 2 )
#
#  Normalize the vector.
#
    v[0] = v[0] / norm
    v[1] = v[1] / norm
#
#  Now compute a value to map the point ON the disk INTO the disk.
#
    r = rng.random ( )

    x[0,j] = np.sqrt ( r ) * v[0]
    x[1,j] = np.sqrt ( r ) * v[1]

  return x

def disk01_sample_test ( rng ):

#*****************************************************************************80
#
## disk01_sample_test() tests disk01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'disk01_sample_test():' )
  print ( '  disk01_sample() samples the unit disk.' )

  n = 10

  x = disk01_sample ( n, rng )

  print ( '' )
  print ( '  Sample points in the unit disk' )
  print ( x )

  return

def disk_rule_compute ( nr, nt, xc, yc, rc ):

#*****************************************************************************80
#
## disk_rule_compute() computes a quadrature rule for a general disk.
#
#  Discussion:
#
#    The general disk is the region:
#
#      ( x - xc ) ^ 2 + ( y - yc ) ^ 2 <= rc ^ 2.
#
#    The integral I(f) is then approximated by
#
#      S(f) = sum ( 1 <= i <= NT * NR ) W(i) * F ( X(i), Y(i) ).
#
#      Area = pi * RC ^ 2
#
#      Q(f) = Area * S(f)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NR, the number of points in the radial rule.
#
#    integer NT, the number of angles to use.
#
#    real XC, YC, the coordinates of the disk center.
#
#    real RC, the radius of the disk.
#
#  Output:
#
#    real W(NR*NT), the weights for the rule.
#
#    real X(NR*NT), Y(NR*NT), the points for the rule.
#
  import numpy as np

  w01, r01, t01 = disk01_rule ( nr, nt )
#
#  Recompute the rule for the general circle in terms of X, Y.
#
  w = np.zeros ( nr * nt )
  x = np.zeros ( nr * nt )
  y = np.zeros ( nr * nt )

  k = 0
  for j in range ( 0, nt ):
    for i in range ( 0, nr ):
      w[k] = w01[i]
      x[k] = xc + rc * r01[i] * np.cos ( t01[j] )
      y[k] = yc + rc * r01[i] * np.sin ( t01[j] )
      k = k + 1

  return w, x, y

def disk_rule_compute_test ( ):

#*****************************************************************************80
#
## disk_rule_compute_test() tests disk_rule_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nr = 4
  nt = 8
#
#  Tabulated exact integrals of 1, x, y, x^2, xy, y^2, x^3, ..., y^4
#  over circle centered at (1,2) with radius 3.
#
  exact = np.pi * np.array ( [ 
       9.0, \
       9.0,        18.0, \
     117.0 / 4.0,  18.0,        225.0 / 4.0, \
     279.0 / 4.0, 117.0 / 2.0,  225.0 / 4.0, 387.0 / 2.0, \
    1773.0 / 8.0, 279.0 / 2.0, 1341.0 / 8.0, 387.0 / 2.0, 5769.0 / 8.0 ] )
 
  print ( '' )
  print ( 'disk_rule_compute_test():' )
  print ( '  disk_rule_compute() computes a rule Q(f) for a general disk' )
  print ( '  centered at (XC,YC) with radius RC,' )
  print ( '  using NT equally spaced angles and NR radial distances.' )
  print ( '' )
  print ( '  NT = %d' % ( nt ) )
  print ( '  NR = %d' % ( nr ) )
  print ( '' )
  print ( '  Estimate integrals I(f) where f = x^ex * y^ey.' )
#
#  Define center and radius of non-unit disk.
#
  xc = 1.0
  yc = 2.0
  rc = 3.0
#
#  Compute the quadrature rule for a unit disk.
#
  w, x, y = disk_rule_compute ( nr, nt, xc, yc, rc )

  print ( '' )
  print ( '   Ex  Ey         I(f)            Q(f)' )
  print ( '' )
#
#  Specify a monomial F(X,Y) = X^Ex * Y^Ey.
#
  e = np.zeros ( 2 )

  i = 0

  for d in range ( 0, 5 ):

    for ex in range ( d, -1, -1 ):

      ey = d - ex
#
#  Evaluate the function at all the quadrature points.
#
      s = 0.0
      for k in range ( 0, nr * nt ):
        f = x[k] ** ex * y[k] ** ey
        s = s + w[k] * f
#
#  Compute the disk area.
#
      area = np.pi * rc ** 2
#
#  Q is the quadrature estimate.
#
      q = area * s

      print ( '   %2d  %2d  %14.6g  %14.6g' % ( ex, ey, exact[i], q ) )

      i = i + 1

  return

def disk_rule_test ( ):

#*****************************************************************************80
#
## disk_rule_test() tests disk_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 April 2016
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk_rule().' )

  rng = default_rng ( )

  disk_rule_compute_test ( )
  disk01_area_test ( )
  disk01_monomial_integral_test ( rng )
  disk01_rule_test ( )
  disk01_sample_test ( rng )
  imtqlx_test ( )
  legendre_ek_compute_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_rule_test():' )
  print ( '  Normal end of execution.' )
  return

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

  print ( '' )
  print ( 'imtqlx_test()' )
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
  print ( '' )
  print ( 'legendre_ek_compute_test():' )
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
  disk_rule_test ( )
  timestamp ( )

