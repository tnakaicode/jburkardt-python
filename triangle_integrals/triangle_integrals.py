#! /usr/bin/env python3
#
def i4_to_pascal_degree ( k ):

#*****************************************************************************80
#
## I4_TO_PASCAL_DEGREE converts a linear index to a Pascal triangle degree.
#
#  Discussion:
#
#    We describe the grid points in Pascal's triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#    The quantity D represents the "degree" of the corresponding monomial,
#    that is, D = I + J.
#
#    We can compute D directly from K using the quadratic formula.
#
#  Example:
#
#     K  I  J  D
#
#     1  0  0  0
#
#     2  1  0  1
#     3  0  1  1
#
#     4  2  0  2
#     5  1  1  2
#     6  0  2  2
#
#     7  3  0  3
#     8  2  1  3
#     9  1  2  3
#    10  0  3  3
#
#    11  4  0  4
#    12  3  1  4
#    13  2  2  4
#    14  1  3  4
#    15  0  4  4
#
#    16  5  0  5
#    17  4  1  5
#    18  3  2  5
#    19  2  3  5
#    20  1  4  5
#    21  0  5  5
#
#    22  6  0  6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the linear index of the (I,J) element.
#    1 <= K.
#
#    Output, integer D, the degree (sum) of the corresponding Pascal indices.
#
  import numpy as np
  from sys import exit

  if ( k <= 0 ):
    print ( '' )
    print ( 'I4_TO_PASCAL_DEGREE - Fatal error!' )
    print ( '  K must be positive.' )
    exit ( 'I4_TO_PASCAL_DEGREE - Fatal error!' )

  d = int ( 0.5 * ( - 1.0 + np.sqrt ( 1.0 + 8.0 * ( k - 1 ) ) ) )

  return d

def i4_to_pascal_degree_test ( ):

#*****************************************************************************80
#
#% I4_TO_PASCAL_DEGREE_TEST tests I4_TO_PASCAL_DEGREE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_TO_PASCAL_DEGREE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_TO_PASCAL_DEGREE converts a linear index to' )
  print ( '  the degree of the corresponding Pascal triangle indices.' )
  print ( '' )
  print ( '     K  =>   D' )
  print ( '' )

  for k in range ( 1, 21 ):

    d = i4_to_pascal_degree ( k )

    print ( '  %4d    %4d' % ( k, d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_TO_PASCAL_DEGREE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_to_pascal ( k ):

#*****************************************************************************80
#
#% I4_TO_PASCAL converts a linear index to Pascal triangle coordinates.
#
#  Discussion:
#
#    We describe the grid points in Pascal's triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#  Example:
#
#     K  I  J
#
#     1  0  0
#     2  1  0
#     3  0  1
#     4  2  0
#     5  1  1
#     6  0  2
#     7  3  0
#     8  2  1
#     9  1  2
#    10  0  3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the linear index of the (I,J) element.
#    1 <= K.
#
#    Output, integer I, J, the Pascal indices.
#
  from sys import exit

  if ( k <= 0 ):
    print ( '' )
    print ( 'I4_TO_PASCAL - Fatal error!' )
    print ( '  K must be positive.' )
    exit ( 'I4_TO_PASCAL - Fatal error!' )

  d = i4_to_pascal_degree ( k )

  j = k - ( d * ( d + 1 ) ) // 2 - 1
  i = d - j

  return i, j

def i4_to_pascal_test ( ):

#*****************************************************************************80
#
## I4_TO_PASCAL_TEST tests I4_TO_PASCAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_TO_PASCAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_TO_PASCAL converts a linear index to' )
  print ( '  Pascal triangle indices.' )
  print ( '' )
  print ( '     K  =>   I     J' )
  print ( '' )

  for k in range ( 1, 21 ):

    i, j = i4_to_pascal ( k )

    print ( '  %4d    %4d  %4d' % ( k, i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_TO_PASCAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pascal_to_i4 ( i, j ):

#*****************************************************************************80
#
## PASCAL_TO_I4 converts Pacal triangle coordinates to a linear index.
#
#  Discussion:
#
#    We describe the grid points in a Pascal triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#  Example:
#
#     K  I  J
#
#     1  0  0
#     2  1  0
#     3  0  1
#     4  2  0
#     5  1  1
#     6  0  2
#     7  3  0
#     8  2  1
#     9  1  2
#    10  0  3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the row and column indices.  I and J must
#    be nonnegative.
#
#    Output, integer K, the linear index of the (I,J) element.
#
  from sys import exit

  if ( i < 0 ):
    print ( '' )
    print ( 'PASCAL_TO_I4 - Fatal error!' )
    print ( '  I < 0.' )
    print ( '  I = %d' % ( i ) )
    exit ( 'PASCAL_TO_I4 - Fatal error!' );
  elif ( j < 0 ):
    print ( '' )
    print ( 'PASCAL_TO_I4 - Fatal error!' )
    print ( '  J < 0.' )
    print ( '  J = %d' % ( j ) )
    exit ( 'PASCAL_TO_I4 - Fatal error!' )

  d = i + j

  k = ( d * ( d + 1 ) ) // 2 + j + 1

  return k

def pascal_to_i4_test ( ):

#*****************************************************************************80
#
#% PASCAL_TO_I4_TEST tests PASCAL_TO_I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PASCAL_TO_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PASCAL_TO_I4 converts Pascal triangle indices to a' )
  print ( '  linear index.' )
  print ( '' )
  print ( '     I     J =>    K' )
  print ( '' )

  for d in range ( 0, 5 ):
    for i in range ( d, -1, -1 ):
      j = d - i;
      k = pascal_to_i4 ( i, j )
      print ( '  %4d  %4d    %4d' % ( i, j, k ) )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PASCAL_TO_I4_TEST:' )
  print ( '  Normal end of execution.' )
  return

def poly_power_linear ( d1, p1, n ):

#*****************************************************************************80
#
## POLY_POWER_LINEAR computes the polynomial ( a + b*x + c*y ) ^ n.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/poly_power_linear.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D1, the degree of the linear polynomial,
#    which should be 1.
#
#    Input, real P1(M1), the coefficients of the linear polynomial.
#    M1 = ( (D1+1)*(D1+2) ) / 2, which should be 3.
#
#    Input, integer N, the power to which the polynomial is to be raised.
#    0 <= N.
#
#    Output, integer D2, the degree of the power polyynomial, which
#    should be D2 = N * D1 = N.
#
#    Output, real P2(M2), the coefficients of the power polynomial.
#    M2 = ( (D2+1)*(D2+2) ) / 2, which should be ((N+1)*(N+2))/2.
#
  import numpy as np
  from sys import exit

  if ( d1 < 0 ):
    print ( '' )
    print ( 'POLY_POWER_LINEAR - Fatal error!' )
    print ( '  D1 < 0.' )
    exit ( 'POLY_POWER_LINEAR - Fatal error!' )

  if ( n < 0 ):
    print ( '' )
    print ( 'POLY_POWER_LINEAR - Fatal error!' )
    print ( '  N < 0.' )
    exit ( 'POLY_POWER_LINEAR - Fatal error!' )

  d2 = n * d1
  m2 = ( ( d2 + 1 ) * ( d2 + 2 ) ) // 2
  p2 = np.zeros ( m2 )

  if ( d1 == 0 ):
    p2[0] = p1[0] ** n
    return d2, p2

  if ( n == 0 ):
    p2[0] = 1.0
    return d2, p2
#
#  Use the Trinomial formula.
#
  for i in range ( 0, n + 1 ):
    for j in range ( 0, n - i + 1 ):
      for k in range ( 0, n - i - j + 1 ):
#
#  We store X^J Y^K in location L.
#
        l = pascal_to_i4 ( j, k )
        lm1 = l - 1
        p2[lm1] = trinomial ( i, j, k ) * p1[0] ** i * p1[1] ** j * p1[2] ** k

  return d2, p2

def poly_power_linear_test ( ):

#*****************************************************************************80
#
## POLY_POWER_LINEAR_TEST tests POLY_POWER_LINEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLY_POWER_LINEAR_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLY_POWER_LINEAR computes the N-th power of' )
  print ( '  a linear polynomial in X and Y.' )
#
#  P = ( 1 + 2 x + 3 y )^2
#
  d1 = 1
  p1 = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ( '' )
  poly_print ( d1, p1, '  p1(x,y)' )

  dp, pp = poly_power_linear ( d1, p1, 2 )
  print ( '' )
  poly_print ( dp, pp, '  p1(x,y)^n' )

  dc = 2
  pc = np.array ( [ 1.0, 4.0, 6.0, 4.0, 12.0, 9.0 ] )
  print ( '' )
  poly_print ( dc, pc, '  Correct answer: p1(x,y)^2' )
#
#  P = ( 2 - x + 3 y )^3
#
  d1 = 1
  p1 = np.array ( [ 2.0, -1.0, 3.0 ] )
  print ( '' )
  poly_print ( d1, p1, '  p1(x,y)' )

  dp, pp = poly_power_linear ( d1, p1, 3 )
  print ( '' )
  poly_print ( dp, pp, '  p1(x,y)^3' )

  dc = 3
  pc = np.array ( [ 8.0, -12.0, 36.0, 6.0, -36.0, 54.0, -1.0, 9.0, -27.0, 27.0 ] )
  print ( '' )
  poly_print ( dc, pc, '  Correct answer: p1(x,y)^n' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLY_POWER_LINEAR_TEST' )
  print ( '  Normal end of execution.' )
  return

def poly_power ( d1, p1, n ):

#*****************************************************************************80
#
## POLY_POWER computes a power of a polynomial.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/poly_power.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D1, the degree of the polynomial.
#
#    Input, real P1(M1), the polynomial coefficients.
#    M1 = ((D1+1)*(D1+2))/2.
#
#    Input, integer N, the nonnegative integer power.
#
#    Output, integer D2, the degree of the power polynomial.
#    D2 = N * D1.
#
#    Output, real P2(M2), the polynomial power.
#    M2 = ((D2+1)*(D2+2))/2.
#
  import numpy as np
#
#  Create P2, a polynomial representation of 1.
#
  d2 = 0
  m2 = ( ( d2 + 1 ) * ( d2 + 2 ) ) // 2
  p2 = np.zeros ( m2 )
  p2[0] = 1.0
#
#  Iterate N times:
#    P2 <= P2 * P1
#
  for i in range ( 0, n ):
    d2, p2 = poly_product ( d2, p2, d1, p1 )

  return d2, p2

def poly_power_test ( ):

#*****************************************************************************80
#
## POLY_POWER_TEST tests POLY_POWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLY_POWER_TEST:' )
  print ( '  POLY_POWER computes the N-th power of an X,Y polynomial.' )
#
#  P1 = ( 1 + 2 x + 3 y )
#  P2 = P1^2 = 1 + 4x + 6y + 4x^2 + 12xy + 9y^2 
#
  d1 = 1
  p1 = np.array ( [ 1.0, 2.0, 3.0 ] )
  n = 2

  print ( '' )
  poly_print ( d1, p1, '  p1(x,y)' )

  d2, p2 = poly_power ( d1, p1, n )
  print ( '' )
  poly_print ( d2, p2, '  p2(x,y) = p1(x,y)^2' )

  d3 = 2
  p3 = np.array ( [ 1.0, 4.0, 6.0, 4.0, 12.0, 9.0 ] )
  print ( '' )
  poly_print ( d3, p3, '  p3(x,y)=correct answer' )
#
#  P1 = ( 1 - 2 x + 3 y - 4 x^2 + 5 xy - 6 y^2 )
#  P2 = P1^3 =
#    1
#    -6x +9y
#    +0x^2 - 21xy + 9y^2
#    +40x^3 - 96x^2y  + 108x^y2 - 81y^3
#    +0x^4 + 84x^3y - 141 x^2y^2 +171xy^3 - 54y^4
#    -96x^5 + 384x^4y -798x^3y^2 + 1017 x^2y^3 - 756 xy^4 + 324 y^5
#    -64x^6 + 240x^5y - 588x^4y^2 + 845 x^3y^3 - 882 x^2y^4 +540 xy^5 - 216y^6
#
  d1 = 2
  p1 = np.array ( [ 1.0, -2.0, 3.0, -4.0, +5.0, -6.0 ] )
  n = 3

  print ( '' )
  poly_print ( d1, p1, '  p1(x,y)' )

  d2, p2 = poly_power ( d1, p1, n )
  print ( '' )
  poly_print ( d2, p2, '  p2(x,y) = p1(x,y)^3' )

  d3 = 6
  p3 = np.array ( [ \
      1.0, \
     -6.0,  9.0, \
      0.0, -21.0,    9.0, \
     40.0, -96.0,  108.0,  -81.0, \
      0.0,  84.0, -141.0,  171.0,  -54.0, \
    -96.0, 384.0, -798.0, 1017.0, -756.0, 324.0, \
    -64.0, 240.0, -588.0,  845.0, -882.0, 540.0, -216.0 ] );
  print ( '' )
  poly_print ( d3, p3, '  p3(x,y)=correct answer' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLY_POWER_TEST' )
  print ( '  Normal end of execution.' )
  return

def poly_print ( d, p, title ):

#*****************************************************************************80
#
## POLY_PRINT prints an XY polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D, the degree of the polynomial.
#
#    Output, real P(M), the coefficients of all monomials of degree 0 through D.
#    P must contain ((D+1)*(D+2))/2 entries.
#
#    Input, string TITLE, a title string.
#
  m = ( ( d + 1 ) * ( d + 2 ) ) // 2

  allzero = True

  for i in range ( 0, m ):
    if ( p[i] != 0.0 ):
      allzero = False
  
  if ( allzero ):

    print ( '%s = 0.0' % ( title ) )

  else:

    print ( '%s = ' % ( title ) )

    for k in range ( 1, m + 1 ):

      i, j = i4_to_pascal ( k )
      di = i + j
      km1 = k - 1

      if ( p[km1] != 0.0 ):

        if ( p[km1] < 0.0 ):
          print ( '  -%g' % ( abs ( p[km1] ) ) ),
        else:
          print ( '  +%g' % ( p[km1] ) ),

        if ( di != 0 ):
          print ( '' ),
#
#  "PASS" does nothing, but Python requires a statement here.
#
#  Python idiotically insists on putting a space between successive prints,
#  and I don't feel like calling sys.stdout.write ( string ) in order to
#  suppress something I shouldn't have to deal with in the first place,
#  so pretend you like it.
#
        if ( i == 0 ):
          pass
        elif ( i == 1 ):
          print ( 'x' ),
        else:
          print ( 'x^%d' % ( i ) ),

        if ( j == 0 ):
          pass
        elif ( j == 1 ):
          print ( 'y' ),
        else:
          print ( 'y^%d' % ( j ) ),

        print ( '' )

  return

def poly_print_test ( ):

#*****************************************************************************80
#
## POLY_PRINT_TEST tests POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLY_PRINT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLY_PRINT can print a D-degree polynomial in X and Y.' )
#
#  P = 12.34
#
  d = 0
  p = np.array ( [ 12.34 ] )
  print ( '' )
  poly_print ( d, p, '  p1(x,y)' )
#
#  P = 1.0 + 2.0 * x + 3.0 * Y
#
  d = 1
  p = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ( '' )
  poly_print ( d, p, '  p2(x,y)' )
#
#  P = XY
#
  d = 2
  p = np.array ( [ 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ] )
  print ( '' )
  poly_print ( d, p, '  p3(x,y) = xy' )
#
#  P = 1 - 2.1 * x + 3.2 * y - 4.3 * x^2 + 5.4 * xy - 6.5 * y^2
#    + 7.6 * x^3 - 8.7 * x^2y + 9.8 * xy^2 - 10.9 * y^3.
#
  d = 3
  p = np.array ( [ 1.0, -2.1, +3.2, -4.3, +5.4, -6.5, +7.6, -8.7, +9.8, -10.9 ] )
  print ( '' )
  poly_print ( d, p, '  p4(x,y)' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLY_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def poly_product ( d1, p1, d2, p2 ):

#*****************************************************************************80
#
#% POLY_PRODUCT computes P3(x,y) = P1(x,y) * P2(x,y) for polynomials.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/poly_product.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D1, the degree of factor 1.
#
#    Input, real P1(M1), the factor 1 coefficients.
#    M1 = ((D1+1)*(D1+2))/2.
#
#    Input, integer D2, the degree of factor 2.
#
#    Input, real P2(M2), the factor2 coefficients.
#    M2 = ((D2+1)*(D2+2))/2.
#
#    Output, integer D3, the degree of the result.
#
#    Output, real P3(M3), the result coefficients.
#    M3 = ((D3+1)*(D3+2))/2.
#
  import numpy as np

  d3 = d1 + d2
  m3 = ( ( d3 + 1 ) * ( d3 + 2 ) ) // 2
  p3 = np.zeros ( m3 )
#
#  Consider each entry in P1:
#    P1(K1) * X^I1 * Y^J1
#  and multiply it by each entry in P2:
#    P2(K2) * X^I2 * Y^J2
#  getting 
#    P3(K3) = P3(K3) + P1(K1) * P2(X2) * X^(I1+I2) * Y(J1+J2)
#
  m1 = ( ( d1 + 1 ) * ( d1 + 2 ) ) // 2
  m2 = ( ( d2 + 1 ) * ( d2 + 2 ) ) // 2

  for k1m1 in range ( 0, m1 ):
    k1 = k1m1 + 1
    i1, j1 = i4_to_pascal ( k1 )
    for k2m1 in range ( 0, m2 ):
      k2 = k2m1 + 1
      i2, j2 = i4_to_pascal ( k2 )
      i3 = i1 + i2
      j3 = j1 + j2
      k3 = pascal_to_i4 ( i3, j3 )
      k3m1 = k3 - 1
      p3[k3m1] = p3[k3m1] + p1[k1m1] * p2[k2m1]

  return d3, p3

def poly_product_test ( ):

#*****************************************************************************80
#
## POLY_PRODUCT_TEST tests POLY_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLY_PRODUCT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLY_PRODUCT computes the product of two X,Y polynomials.' )
#
#  P1 = ( 1 + 2 x + 3 y )
#  P2 = ( 4 + 5 x )
#  P3 = 4 + 13x + 12y + 10x^2 + 15xy + 0y^2 
#
  d1 = 1
  p1 = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ( '' )
  poly_print ( d1, p1, '  p1(x,y)' )

  d2 = 1
  p2 = np.array ( [ 4.0, 5.0, 0.0 ] )
  print ( '' )
  poly_print ( d2, p2, '  p2(x,y)' )

  d3, p3 = poly_product ( d1, p1, d2, p2 )
  print ( '' )
  poly_print ( d3, p3, '  p3(x,y) = p1(x,y) * p2(x,y)' )

  dc = 2
  pc = np.array ( [ 4.0, 13.0, 12.0, 10.0, 15.0, 0.0 ] )
  print ( '' )
  poly_print ( dc, pc, '  Correct answer: p3(x,y)=p1(x,y)*p2(x,y)' )
#
#  P1 = ( 1 - 2 x + 3 y - 4x^2 + 5xy - 6y^2)
#  P2 = ( 7 + 3x^2 )
#  P3 = 7 
#    - 14x + 21y 
#    - 25 x^2 + 35 xy -  42y^2 
#    -  6x^3  + 9x^2y +  0xy^2   + 0y^3
#    - 12x^4 + 15x^3y - 18x^2y^2 + 0 xy^3 + 0y^4
#
  d1 = 2
  p1 = np.array ( [ 1.0, -2.0, 3.0, -4.0, +5.0, -6.0 ] )
  print ( '' )
  poly_print ( d1, p1, '  p1(x,y)' )

  d2 = 2
  p2 = np.array ( [ 7.0, 0.0, 0.0, 3.0, 0.0, 0.0 ] )
  print ( '' )
  poly_print ( d2, p2, '  p2(x,y)' )

  d3, p3 = poly_product ( d1, p1, d2, p2 )
  print ( '' )
  poly_print ( d3, p3, '  p3(x,y) = p1(x,y) * p2(x,y)' )

  dc = 4
  pc = np.array ( [ \
      7.0, \
    -14.0,  21.0, \
    -25.0, +35.0, -42.0, \
     -6.0,   9.0,   0.0, 0.0, \
    -12.0, +15.0, -18.0, 0.0, 0.0 ] )
  print ( '' )
  poly_print ( dc, pc, '  Correct answer: p3(x,y)=p1(x,y)*p2(x,y)' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLY_PRODUCT_TEST' )
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

def rs_to_xy_map ( t ):

#*****************************************************************************80
#
## RS_TO_XY_MAP returns the linear map from reference to physical triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_poly_integral/rs_to_xy_map.py
#
#  Discussion:
#
#    This function returns the coefficients of the linear map that sends
#    the vertices of the reference triangle, (0,0), (1,0) and (0,1), to
#    the vertices of a physical triangle T, of the form:
#
#      X = A + B * R + C * S;
#      Y = D + E * R + F * S.
#
#  Reference Element:
#
#    |
#    1  3
#    |  |\
#    |  | \
#    S  |  \
#    |  |   \
#    |  |    \
#    0  1-----2
#    |
#    +--0--R--1-->
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T[3,2], the coordinates of the vertices.  The vertices are 
#    assumed to be the images of (0,0), (1,0) and (0,1) respectively.
#
#    Output, real A, B, C, D, E, F, the mapping coefficients.
#
  a = t[0,0]
  b = t[1,0] - t[0,0]
  c = t[2,0] - t[0,0]

  d = t[0,1]
  e = t[1,1] - t[0,1]
  f = t[2,1] - t[0,1]

  return a, b, c, d, e, f

def rs_to_xy_map_test ( ):

#*****************************************************************************80
#
## RS_TO_XY_MAP_TEST tests RS_TO_XY_MAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'RS_TO_XY_MAP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RS_TO_XY_MAP determines the coefficients of the linear map' )
  print ( '  from a the reference in RS coordinates to the physical' )
  print ( '  triangle in XY coordinates:' )
  print ( '    X = a + b * R + c * S' )
  print ( '    Y = d + e * R + f * S' )

  tr = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  t = np.array ( [ \
    [ 2.0, 0.0 ], \
    [ 3.0, 4.0 ], \
    [ 0.0, 3.0 ] ] )

  r8mat_print ( 3, 2, t, '  XY triangle vertices:' )

  a, b, c, d, e, f = rs_to_xy_map ( t )

  print ( '' )
  print ( '  Mapping coefficients are:' )
  print ( '' )
  print ( '    X = %g + %g * R + %g * S' % ( a, b, c ) )
  print ( '    Y = %g + %g * R + %g * S' % ( d, e, f ) )

  print ( '' )
  print ( '  Apply map to RS triangle vertices.' )
  print ( '  Recover XY vertices (2,0), (3,4) and (0,3).' )
  print ( '' )

  for i in range ( 0, 3 ):
    x = a + b * tr[i,0] + c * tr[i,1]
    y = d + e * tr[i,0] + f * tr[i,1]
    print ( '  V(%d) = ( %g, %g )' % ( i, x, y ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RS_TO_XY_MAP_TEST:' )
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

def triangle01_monomial_integral ( i, j ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL: monomial integrals in the unit triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle01_monomial_integral.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the exponents.  
#    Each exponent must be nonnegative.
#
#    Output, real Q, the integral.
#
  k = 0
  q = 1.0

  for l in range ( 1, i + 1 ):
    k = k + 1
    q = q * float ( l ) / float ( k )

  for l in range ( 1, j + 1 ):
    k = k + 1
    q = q * float ( l ) / float ( k )

  for l in range ( 1, 3 ):
    k = k + 1
    q = q / float ( k )

  return q

def triangle01_monomial_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL_TEST estimates integrals over the unit triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE01_MONOMIAL_INTEGRAL returns the integral Q of' )
  print ( '  a monomial X^I Y^J over the interior of the unit triangle.' )

  print ( '' )
  print ( '   I   J         Q(I,J)' )

  for d in range ( 0, 6 ):
    print ( '' )
    for i in range ( 0, d + 1 ):
      j = d - i
      q = triangle01_monomial_integral ( i, j )
      print ( '  %2d  %2d  %14.6g' % ( i, j, q ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle01_poly_integral ( d, p ):

#*****************************************************************************80
#
## TRIANGLE01_POLY_INTEGRAL: polynomial integral over the unit triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle01_poly_integral.py
#
#  Discussion:
#
#    The unit triangle is T = ( (0,0), (1,0), (0,1) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D, the degree of the polynomial.
#
#    Input, real P(M), the polynomial coefficients.
#    M = ((D+1)*(D+2))/2.
#
#    Output, real Q, the integral.
#
  m = ( ( d + 1 ) * ( d + 2 ) ) // 2

  q = 0.0
  for k in range ( 1, m + 1 ):
    km1 = k - 1
    i, j = i4_to_pascal ( k )
    qk = triangle01_monomial_integral ( i, j )
    q = q + p[km1] * qk

  return q

def triangle01_poly_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_POLY_INTEGRAL_TEST: polynomial integrals over the unit triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  d_max = 6
  k_max = ( ( d_max + 1 ) * ( d_max + 2 ) ) // 2
  qm = np.zeros ( k_max, dtype = np.int32 )
  for k in range ( 1, k_max + 1 ):
    km1 = k - 1
    i, j = i4_to_pascal ( k )
    qm[km1] = triangle01_monomial_integral ( i, j )

  print ( '' )
  print ( 'TRIANGLE01_POLY_INTEGRAL_TEST' )
  print ( '  TRIANGLE01_POLY_INTEGRAL returns the integral Q of' )
  print ( '  a polynomial P(X,Y) over the interior of the unit triangle.' )

  d = 1
  m = ( ( d + 1 ) * ( d + 2 ) ) // 2
  p = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ( '' )
  poly_print ( d, p, '  p(x,y)' )
  q = triangle01_poly_integral ( d, p )
  print ( '' )
  print ( '  Q =         %g' % ( q ) )
  q2 = np.dot ( p, qm[0:m] )
  print ( '  Q (exact) = %g' % ( q2 ) )

  d = 2
  m = ( ( d + 1 ) * ( d + 2 ) ) // 2
  p = np.array ( [ 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ] )
  print ( '' )
  poly_print ( d, p, '  p(x,y)' )
  q = triangle01_poly_integral ( d, p )
  print ( '' )
  print ( '  Q =         %g' % ( q ) )
  q2 = np.dot ( p, qm[0:m] )
  print ( '  Q (exact) = %g' % ( q2 ) )

  d = 2
  m = ( ( d + 1 ) * ( d + 2 ) ) // 2
  p = np.array ( [ 1.0, -2.0, 3.0, -4.0, 5.0, -6.0 ] )
  print ( '' )
  poly_print ( d, p, '  p(x,y)' )
  q = triangle01_poly_integral ( d, p )
  print ( '' )
  print ( '  Q =         %g' % ( q ) )
  q2 = np.dot ( p, qm[0:m] )
  print ( '  Q (exact) = %g' % ( q2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE01_POLY_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_area ( t ):

#*****************************************************************************80
#
## TRIANGLE_AREA returns the area of a triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_area.py
#
#  Discussion:
#
#    If the vertices are given in counter clockwise order, the area
#    will be positive.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real T[3,2], the vertices of the triangle.
#
#    Output, real AREA, the area of the triangle.
#
  area = 0.5 * \
    ( \
        ( t[1,0] - t[0,0] ) * ( t[2,1] - t[0,1] ) \
      - ( t[2,0] - t[0,0] ) * ( t[1,1] - t[0,1] ) \
    )

  return area

def triangle_area_test ( ):

#*****************************************************************************80
#
## TRIANGLE_AREA_TEST tests TRIANGLE_AREA_MAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TRIANGLE_AREA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_AREA determines the (signed) area of a triangle.' )

  print ( '' )
  print ( '  Triangle vertices are:' )
  print ( '    (X1,Y1) = (0,0)' )
  print ( '    (X2,Y2) = 2*(cos(angle),sin(angle))' )
  print ( '    (X3,Y3) = (0,1)' )
  print ( '  where angle will sweep from 0 to 360 degrees.' )

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 2.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  r = 2.0

  print ( '' )
  print ( '   I      Angle         X2          Y2           Area' )
  print ( '        (degrees)' )
  print ( '' )

  for i in range ( 0, 25 ):
    angled = float ( i ) * 180.0 / 12.0
    angler = float ( i ) * np.pi / 12.0
    t[1,0] = r * np.cos ( angler );
    t[1,1] = r * np.sin ( angler );
    area = triangle_area ( t )
    print ( '  %2d  %10.4f  %10.4f  %10.4f  %14.6g' \
      % ( i, angled, t[1,0], t[1,1], area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_integrals_test ( ):

#*****************************************************************************80
#
## TRIANGLE_INTEGRALS_TEST tests the TRIANGLE_INTEGRALS library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE_INTEGRALS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TRIANGLE_INTEGRALS library.' )
#
#  Utilities:
#
  i4_to_pascal_test ( )
  i4_to_pascal_degree_test ( )
  pascal_to_i4_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  timestamp_test ( )
  trinomial_test ( )

  rs_to_xy_map_test ( )
  xy_to_rs_map_test ( )

  poly_print_test ( )
  poly_power_linear_test ( )
  poly_power_test ( )
  poly_product_test ( )
#
#  Library functions:
#
  triangle01_monomial_integral_test ( )
  triangle01_poly_integral_test ( )

  triangle_area_test ( )
  triangle_xy_integral_test ( )
  triangle_monomial_integral_test ( )
  triangle_poly_integral_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_INTEGRALS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def triangle_monomial_integral ( i, j, t ):

#*****************************************************************************80
#
## TRIANGLE_MONOMIAL_INTEGRAL integrates a monomial over an arbitrary triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_monomial_integral.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the exponents of X and Y in the monomial.
#    0 <= I, J.
#
#    Input, real T(2,3), the vertices of the triangle.
#
#    Output, real Q, the integral of X^I * Y^J over triangle T.
#
  import numpy as np
#
#  Get map coefficients from reference RS triangle to general XY triangle.
#    R = a+b*X+c*Y
#    S = d+e*X+f*Y
#
  a, b, c, d, e, f = rs_to_xy_map ( t )
#
#  Compute
#    P1(R,S) = (a+b*R+c*S)^i.
#    P2(R,S) = (d+e*R+f*S)^j.
#
  d1 = 1
  p1 = np.array ( [ a, b, c ] )
  dp1, pp1 = poly_power_linear ( d1, p1, i )

  d2 = 1
  p2 = np.array ( [ d, e, f ] )
  dp2, pp2 = poly_power_linear ( d2, p2, j )
#
#  Compute the product 
#    P3(R,S) = (a+b*R+c*S)^i * (d+e*R+f*S)^j.
#
  d3, p3 = poly_product ( dp1, pp1, dp2, pp2 )
#
#  Compute the integral of P3(R,S) over the reference triangle.
#
  q = triangle01_poly_integral ( d3, p3 )
#
#  Multiply by the area of the physical triangle T(X,Y) divided by
#  the area of the reference triangle.
#
  q = q * triangle_area ( t ) / 0.5

  return q
  
def triangle_monomial_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE_MONOMIAL_INTEGRAL_TEST estimates integrals over a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TRIANGLE_MONOMIAL_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_MONOMIAL_INTEGRAL returns the integral Q of' )
  print ( '  a monomial X^I Y^J over the interior of a triangle.' )
#
#  Test 1:
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 0.0, 1.0 ] ] )

  i = 1
  j = 0

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )
  print ( '  Integrand = x^%d * y^%d\n' % ( i, j ) )

  q = triangle_monomial_integral ( i, j, t )
  q2 = 1.0 / 6.0

  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Test 2:
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 1.0, 2.0 ] ] )

  i = 1
  j = 1

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )
  print ( '  Integrand = x^%d * y^%d\n' % ( i, j ) )


  q = triangle_monomial_integral ( i, j, t )
  q2 = 0.5

  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Test 3:
#
  t = np.array ( [ \
     [ -3.0, 0.0 ], \
     [  6.0, 0.0 ], \
     [  0.0, 3.0 ] ] )

  i = 1
  j = 0

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )
  print ( '  Integrand = x^%d * y^%d\n' % ( i, j ) )

  q = triangle_monomial_integral ( i, j, t )
  q2 = 13.5

  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Test 4:
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 4.0, 0.0 ], \
     [ 0.0, 1.0 ] ] )

  i = 1
  j = 1

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )
  print ( '  Integrand = x^%d * y^%d\n' % ( i, j ) )

  q = triangle_monomial_integral ( i, j, t )
  q2 = 2.0 / 3.0

  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )

#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_MONOMIAL_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_poly_integral ( d, p, t ):

#*****************************************************************************80
#
## TRIANGLE_POLY_INTEGRAL: polynomial integral over a triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_poly_integral.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D, the degree of the polynomial.
#
#    Input, real P(M), the polynomial coefficients.
#    M = ((D+1)*(D+2))/2.
#
#    Input, real T(2,3), the vertices of the triangle.
#
#    Output, real Q, the integral.
#
  m = ( ( d + 1 ) * ( d + 2 ) ) // 2

  q = 0.0
  for k in range ( 1, m + 1 ):
    km1 = k - 1
    i, j = i4_to_pascal ( k )
    qk = triangle_monomial_integral ( i, j, t )
    q = q + p[km1] * qk

  return q

def triangle_poly_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE_POLY_INTEGRAL_TEST estimates integrals over a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TRIANGLE_POLY_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_POLY_INTEGRAL returns the integral Q of' )
  print ( '  a polynomial over the interior of a triangle.' )
#
#  Test 1:
#  Integrate x over reference triangle.
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 0.0, 1.0 ] ] )

  d = 1
  p = np.array ( [ 0.0, 1.0, 0.0 ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )

  print ( '' )
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = 1.0 / 6.0

  print ( '' )
  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Test 2:
#  Integrate xy over a general triangle.
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 1.0, 2.0 ] ] )

  d = 2
  p = np.array ( [ 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )

  print ( '' )
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = 0.5

  print ( '' )
  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Test 3:
#  Integrate 2-3x+xy over a general triangle.
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 1.0, 3.0 ] ] )

  d = 2
  p = np.array ( [ 2.0, -3.0, 0.0, 0.0, 1.0, 0.0 ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )

  print ( '' )
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = 9.0 / 8.0

  print ( '' )
  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Test 4:
#  Integrate -40y + 6x^2 over a general triangle.
#
  t = np.array ( [ \
     [ 0.0, 3.0 ], \
     [ 1.0, 1.0 ], \
     [ 5.0, 3.0 ] ] )

  d = 2
  p = np.array ( [ 0.0, 0.0,-40.0, 6.0, 0.0, 0.0 ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] ) )
  print ( '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] ) )
  print ( '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] ) )

  print ( '' )
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = - 935.0 / 3.0

  print ( '' )
  print ( '  Computed Q = %g' % ( q ) )
  print ( '  Exact Q    = %g' % ( q2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_POLY_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_xy_integral ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## TRIANGLE_XY_INTEGRAL computes the integral of XY over a triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_xy_integral.py
#
#  Discussion:
#
#    This function was written as a special test case for the general
#    problem of integrating a monomial x^alpha * y^beta over a general 
#    triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X1, Y1, X2, Y2, X3, Y3, the coordinates of the
#    triangle vertices.
#
#    Output, real Q, the integral of X*Y over the triangle.
#

#
#  x = x1 * ( 1 - xi - eta )
#    + x2 *       xi
#    + x3 *            eta
#
#  y = y1 * ( 1 - xi - eta )
#    + y2 *       xi
#    + y3 *            eta
#
#  Rewrite as linear polynomials in (xi,eta):
#
#  x = x1 + ( x2 - x1 ) * xi + ( x3 - x1 ) * eta
#  y = y1 + ( y2 - y1 ) * xi + ( y3 - y1 ) * eta
#
#  Jacobian:
#
#    J = [ ( x2 - x1 )  ( x3 - x1 ) ]
#        [ ( y2 - y1 )  ( y3 - y1 ) ]
#
#    det J = ( x2 - x1 ) * ( y3 - y1 ) - ( y2 - y1 ) * ( x3 - x1 )
#
#  Integrand
#
#    x * y = ( x1 + ( x2 - x1 ) * xi + ( x3 - x1 ) * eta )
#          * ( y1 + ( y2 - y1 ) * xi + ( y3 - y1 ) * eta )
#
#  Rewrite as linear combination of monomials:
#
#    x * y = 1      * x1 * y1
#          + eta    * ( x1 * ( y3 - y1 ) + ( x3 - x1 ) * y1 )
#          + xi     * ( x1 * ( y2 - y1 ) + ( x2 - x1 ) * y1 )
#          + eta^2  * ( x3 - x1 ) * ( y3 - y1 )
#          + xi*eta * ( ( x2 - x1 ) * ( y3 - y1 ) + ( x3 - x1 ) * ( y2 - y1 ) )
#          + xi^2   * ( x2 - x1 ) * ( y2 - y1 )
#
  det = ( x2 - x1 ) * ( y3 - y1 ) - ( y2 - y1 ) * ( x3 - x1 )

  p00 = x1 * y1

  p01 = x1 * ( y3 - y1 ) + ( x3 - x1 ) * y1
  p10 = x1 * ( y2 - y1 ) + ( x2 - x1 ) * y1

  p02 = ( x3 - x1 ) * ( y3 - y1 )
  p11 = ( x2 - x1 ) * ( y3 - y1 ) + ( x3 - x1 ) * ( y2 - y1 )
  p20 = ( x2 - x1 ) * ( y2 - y1 )

  q = 0.0
  q = q + p00 * triangle01_monomial_integral ( 0, 0 )
  q = q + p10 * triangle01_monomial_integral ( 1, 0 )
  q = q + p01 * triangle01_monomial_integral ( 0, 1 )
  q = q + p20 * triangle01_monomial_integral ( 2, 0 )
  q = q + p11 * triangle01_monomial_integral ( 1, 1 )
  q = q + p02 * triangle01_monomial_integral ( 0, 2 )

  q = q * det

  return q

def triangle_xy_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE_XY_INTEGRAL_TEST tests TRIANGLE_XY_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE_XY_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_XY_INTEGRAL determines Q, the integral of the' )
  print ( '  monomial X*Y over a triangle (X1,Y1), (X2,Y2), (X3,Y3). )' )

  x1 = 0.0
  y1 = 0.0

  x2 = 1.0
  y2 = 0.0

  x3 = 1.0
  y3 = 2.0

  q = triangle_xy_integral ( x1, y1, x2, y2, x3, y3 )

  print ( '' )
  print ( '  (X1,Y1) = ( %g,%g )' % ( x1, y1 ) )
  print ( '  (X2,Y2) = ( %g,%g )' % ( x2, y2 ) )
  print ( '  (X3,Y3) = ( %g,%g )' % ( x3, y3 ) )
  print ( '  Q = %g' % ( q ) )
  print ( '  (Expecting answer 1/2.' )

  x1 = 0.0
  y1 = 0.0

  x2 = 4.0
  y2 = 0.0

  x3 = 0.0
  y3 = 1.0

  q = triangle_xy_integral ( x1, y1, x2, y2, x3, y3 )

  print ( '' )
  print ( '  (X1,Y1) = ( %g,%g )' % ( x1, y1 ) )
  print ( '  (X2,Y2) = ( %g,%g )' % ( x2, y2 ) )
  print ( '  (X3,Y3) = ( %g,%g )' % ( x3, y3 ) )
  print ( '  Q = %g' % ( q ) )
  print ( '  (Expecting answer 2/3.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_XY_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def trinomial ( i, j, k ):

#*****************************************************************************80
#
## TRINOMIAL computes a trinomial coefficient.
#
#  Discussion:
#
#    The trinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where I objects are of type 1, J of type 2, and K of type 3.
#    and N = I + J + K.
#
#    T(I,J,K) = N! / ( I! J! K! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, K, the factors.
#    All should be nonnegative.
#
#    Output, integer VALUE, the trinomial coefficient.
#
  from sys import exit
#
#  Each factor must be nonnegative.
#
  if ( i < 0 or j < 0 or k < 0 ):
    print ( '' )
    print ( 'TRINOMIAL - Fatal error!' )
    print ( '  Negative factor encountered.' )
    exit ( 'TRINOMIAL - Fatal error!' )

  value = 1

  t = 1

  for l in range ( 1, i + 1 ):
#   value = value * t // l
    t = t + 1

  for l in range ( 1, j + 1 ):
    value = value * t // l
    t = t + 1

  for l in range ( 1, k + 1 ):
    value = value * t // l
    t = t + 1
  
  return value

def trinomial_test ( ):

#*****************************************************************************80
#
## TRINOMIAL_TEST tests TRINOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRINOMIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRINOMIAL evaluates the trinomial coefficient:' )
  print ( '' )
  print ( '  T(I,J,K) = (I+J+K)! / I! / J! / K!' )
  print ( '' )
  print ( '     I     J     K    T(I,J,K)' )
  print ( '' )
 
  for k in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      for i in range ( 0, 5 ):
        t = trinomial ( i, j, k )
        print ( '  %4d  %4d  %4d  %8d' % ( i, j, k, t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRINOMIAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def xy_to_rs_map ( t ):

#*****************************************************************************80
#
## XY_TO_RS_MAP returns the linear map from physical to reference triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/xy_to_rs_map.py
#
#  Discussion:
#
#    Given the vertices T of an arbitrary triangle in the (X,Y) coordinate
#    system, this function returns the coefficients of the linear map
#    that sends the vertices of T to (0,0), (1,0) and (0,1) respectively
#    in the reference triangle with coordinates (R,S):
#
#      R = A + B * X + C * Y;
#      S = D + E * X + F * Y.
#
#  Reference Element T3:
#
#    |
#    1  3
#    |  |\
#    |  | \
#    S  |  \
#    |  |   \
#    |  |    \
#    0  1-----2
#    |
#    +--0--R--1-->
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T[3,2], the X and Y coordinates
#    of the vertices.  The vertices are assumed to be the images of
#    (0,0), (1,0) and (0,1) respectively.
#
#    Output, real A, B, C, D, E, F, the mapping coefficients.
#
  g =   ( ( t[2,1] - t[0,1] ) * ( t[1,0] - t[0,0] )   \
        - ( t[2,0] - t[0,0] ) * ( t[1,1] - t[0,1] ) )

  a = ( - ( t[2,1] - t[0,1] ) * t[0,0]   \
        + ( t[2,0] - t[0,0] ) * t[0,1] ) / g

  b =     ( t[2,1] - t[0,1] ) / g

  c =   - ( t[2,0] - t[0,0] ) / g

  d = (   ( t[1,1] - t[0,1] ) * t[0,0] \
        - ( t[1,0] - t[0,0] ) * t[0,1] ) / g

  e =   - ( t[1,1] - t[0,1] ) / g

  f =     ( t[1,0] - t[0,0] ) / g

  return a, b, c, d, e, f


def xy_to_rs_map_test ( ):

#*****************************************************************************80
#
## XY_TO_RS_MAP_TEST tests XY_TO_RS_MAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'XY_TO_RS_MAP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  XY_TO_RS_MAP determines the coefficients of the linear map' )
  print ( '  from a general triangle in XY coordinates to the reference' )
  print ( '  triangle in RS coordinates:' )
  print ( '    R = a + b * X + c * Y' )
  print ( '    S = d + e * X + f * Y' )

  t = np.array ( [ \
    [ 2.0, 0.0 ], \
    [ 3.0, 4.0 ], \
    [ 0.0, 3.0 ] ] )

  r8mat_print ( 3, 2, t, '  XY triangle vertices:' )

  a, b, c, d, e, f = xy_to_rs_map ( t )

  print ( '' )
  print ( '  Mapping coefficients are:' )
  print ( '' )
  print ( '    R = %g + %g * X + %g * Y' % ( a, b, c ) )
  print ( '    S = %g + %g * X + %g * Y' % ( d, e, f ) )

  print ( '' )
  print ( '  Apply map to XY triangle vertices.' )
  print ( '  Recover RS vertices (0,0), (1,0) and (0,1).' )
  print ( '' )
  for i in range ( 0, 3 ):
    r = a + b * t[i,0] + c * t[i,1]
    s = d + e * t[i,0] + f * t[i,1]
    print ( '  V(%d) = (%g,%g)' % ( i, r, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'XY_TO_RS_MAP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_integrals_test ( )
  timestamp ( )

