#! /usr/bin/env python3
#
def hermite_polynomial_test ( ):

#*****************************************************************************80
#
## hermite_polynomial_test() tests hermite_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hermite_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hermite_polynomial().' )

  hermite_polynomial_test01 ( )
  hermite_polynomial_test02 ( )
  hermite_polynomial_test03 ( )
  hermite_polynomial_test04 ( )
  hermite_polynomial_test05 ( )
  hermite_polynomial_test06 ( )
  hermite_polynomial_test07 ( )

  p = 5
  b = 0.0
  hermite_polynomial_test08 ( p, b )

  p = 5
  b = 1.0
  hermite_polynomial_test08 ( p, b )

  p = 5
  e = 0
  hermite_polynomial_test09 ( p, e )

  p = 5
  e = 1
  hermite_polynomial_test09 ( p, e )

  p = 5
  b = 0.0
  hermite_polynomial_test10 ( p, b )

  p = 5
  b = 1.0
  hermite_polynomial_test10 ( p, b )

  p = 5
  e = 0
  hermite_polynomial_test11 ( p, e )

  p = 5
  e = 1
  hermite_polynomial_test11 ( p, e )

  p = 5
  b = 0.0
  hermite_polynomial_test12 ( p, b )

  p = 5
  b = 1.0
  hermite_polynomial_test12 ( p, b )

  p = 5
  e = 0
  hermite_polynomial_test13 ( p, e )

  p = 5
  e = 1
  hermite_polynomial_test13 ( p, e )

  hermite_polynomial_test14 ( )

  hermite_polynomial_test15 ( )

  hermite_polynomial_test16 ( )
  hermite_polynomial_test17 ( )
  hermite_polynomial_test18 ( )

  hermite_polynomial_plot01 ( )
  hermite_polynomial_plot02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hermite_polynomial_test():' )
  print ( '  Normal end of execution.' )

  return

def exp_fun ( n, x ):

#*****************************************************************************80
#
## exp_fun() evaluates the exponential function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  value = np.exp ( x )

  return value

def h_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## h_to_monomial_matrix(): physicist's Hermite to monomial conversion matrix.
#
#  Discussion:
#
#    Here we are using the physicist's Hermite polynomial.
#
#  Example:
#
#    N = 11
#
#      1  .  -2   .    12     .    -120     .   1680     .   -30240
#      .  2   .  12     .   120      .  -1680      . 30240        .
#      .  .   4   .   -48     .     720     . -13440     .   302400
#      .  .   .   8     .  -160       .  3360   .   -80640        .
#      .  .   .   .    16     .    -480     .  13440     .  -403200
#      .  .   .   .     .    32       . -1344      . 48384        .
#      .  .   .   .     .     .      64     .  -3584     .   161280
#      .  .   .   .     .     .       .   128      . -9216        .
#      .  .   .   .     .     .       .     .    256     .   -23040
#      .  .   .   .     .     .       .     .      .   512        .
#      .  .   .   .     .     .       .     .      .     .     1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  if ( n <= 0 ):
    return A

  A[0,0] = 1.0

  if ( n == 1 ):
    return A

  A[1,1] = 2.0 

  for j in range ( 3, n + 1 ):
    for i in range ( 1, n + 1 ):
      if ( i == 1 ):
        A[i-1,j-1] =                  - 2.0 * ( j - 2 ) * A[i-1,j-3]
      else:
        A[i-1,j-1] = 2.0 * A(i-2,j-2) - 2.0 * ( j - 2 ) * A[i-1,j-3]

  return A

def he_double_product_integral ( i, j ):

#*****************************************************************************80
#
## he_double_product_integral(): integral of He(i,x)*He(j,x)*e^(-x^2/2).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#    VALUE = integral ( -oo < x < +oo ) H(i,x)*H(j,x) exp(-x^2/2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the polynomial indices.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.math import factorial

  if ( i != j ):
    value = 0.0
  else:
    value = factorial ( i )

  return value

def he_integral ( n ):

#*****************************************************************************80
#
## he_integral() evaluates the integral of He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#    The integral computed is:
#
#      integral ( -oo < x < +oo ) He(i,x) exp(-x^2/2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the integral.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):

    value = 0.0

  else:

    value = r8_factorial2 ( n - 1 ) * np.sqrt ( 2.0 * np.pi )

  return value

def hen_exponential_product ( p, b ):

#*****************************************************************************80
#
## hen_exponential_product(): exponential product exp(b*x)*Hen(i,x)*Hen(j,x).
#
#  Discussion:
#
#    Hen(i,x) is the normalized probabilist's Hermite polynomial of degree I.
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of exp(B*X) with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -oo < X < +oo ) exp(B*X) * Hen(I,X) * Hen(J,X) exp(-0.5*X*X) dx
#
#    We will estimate these integrals using Gauss-Hermite quadrature.
#    Because of the exponential factor exp(B*X), the quadrature will not 
#    be exact.
#
#    However, when B = 0, the quadrature is exact, and moreoever, the
#    table will be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    real B, the coefficient of X in the exponential factor.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.  TABLE(I,J)
#    represents the weighted integral of exp(B*X) * Hen(I+1,X) * Hen(J+1,X).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = ( ( 3 * p + 4 ) // 2 )

  x_table, w_table = he_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    h_table = hen_polynomial_value ( 1, p, x )
#
#  The following formula is an outer product in H_TABLE.
#
    table = table \
      + w_table[k] * np.exp ( b * x ) * np.outer ( h_table, h_table )

  return table

def hen_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## hen_polynomial_value() evaluates Hen(i,x).
#
#  Discussion:
#
#    Hen(i,x) is the normalized probabilist's Hermite polynomial of degree I.
#
#    These polynomials satisfy the orthonormality condition:
#
#      Integral ( -oo < X < +oo ) exp ( - 0.5 * X^2 ) * Hen(M,X) Hen(N,X) dX 
#      = delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521192255,
#    LC: QA331.N57.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real P(M,N+1), the values of the polynomials of index 0 through N.
#
  from scipy.special import gamma
  import numpy as np

  x = np.atleast_1d ( x )

  p = np.zeros ( [ m, n + 1 ] )

  p[0:m,0] = 1.0

  if ( n == 0 ):
    return p

  p[0:m,1] = x[0:m]
 
  for j in range ( 2, n + 1 ):
    p[0:m,j] = x[0:m] * p[0:m,j-1] - ( j - 1 ) * p[0:m,j-2]
#
#  Normalize.
#
  arg = np.linspace ( 1, n + 1, n + 1 )

  d = np.diag ( 1.0 / np.sqrt ( gamma ( arg ) * np.sqrt ( 2.0 * np.pi ) ) )

  p = np.matmul ( p, d )

  return p

def hen_power_product ( p, e ):

#*****************************************************************************80
#
## hen_power_product(): power products, x^e*Hen(i,x)*Hen(j,x).
#
#  Discussion:
#
#    Hen(i,x) is the normalized probabilist's Hermite polynomial of degree I.
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of X with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -oo < X < +oo ) X^E * Hen(I,X) * Hen(J,X) exp(-0.5*X*X) dx
#
#    We will estimate these integrals using Gauss-Hermite quadrature.
#
#    When E is 0, the computed table should be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    integer E, the exponent of X in the integrand.
#    0 <= E.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.  TABLE(I,J)
#    represents the weighted integral of X^E * Hen(I+1,X) * Hen(J+1,X).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = p + 1 + ( ( e + 1 ) // 2 )

  x_table, w_table = he_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    h_table = hen_polynomial_value ( 1, p, x )
#
#  The following formula is an outer product in H_TABLE.
#
    if ( e == 0 ):
      table = table + w_table[k] * np.outer ( h_table, h_table )
    else:
      table = table + w_table[k] * x**e * np.outer ( h_table, h_table )

  return table

def hen_projection_data ( m, n, x, d ):

#*****************************************************************************80
#
## hen_projection_data(): project data onto Hen(0:n,x).
#
#  Discussion:
#
#    Hen(i,x) is the normalized probabilist's Hermite polynomial of degree I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of data values.
#
#    integer N, the degree of the highest Hermite polynomial.
#    0 <= N.
#
#    real X(M,1), the data abscissas.  These need not be sorted.
#
#    real D(M,1), the data values.
#
#  Output:
#
#    real C(N+1,1), the approximate projection coefficients.
#
  from scipy.linalg import lstsq
#
#  Compute the M by N+1 Hermite Vandermonde matrix.
#
  V = hen_polynomial_value ( m, n, x )
#
#  Compute the least-squares solution.
#  Solve V*c = d
#
  c, _, _, _  = lstsq ( V, d )

  return c

def hen_projection ( n, f ):

#*****************************************************************************80
#
## hen_projection() projects a function f onto polynomials Hen(i,x).
#
#  Discussion:
#
#    Hen(i,x) is the normalized probabilist's Hermite polynomial of degree I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#
#    function handle F, of the form
#    function v = f ( n, x )
#
#  Output:
#
#    real C(N+1,1), projection coefficients for Hen(0,x) through Hen(N,x).
#
  import numpy as np

  c = np.zeros ( n + 1 )

  x, w = he_quadrature_rule ( n + 1 )

  f_vec = f ( n + 1, x )

  PHI = hen_polynomial_value ( n + 1, n, x )

  for i in range ( 0, n + 1 ):
    PHI[i,:] = PHI[i,:] * w[i]

  c = np.matmul ( np.transpose ( PHI ), f_vec )

  return c

def hen_projection_value ( n, c, m, x ):

#*****************************************************************************80
#
## hen_projection_value(): evaluation projection onto Hen(i,x).
#
#  Discussion:
#
#    Hen(i,x) is the normalized probabilist's Hermite polynomial of degree I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the highest order polynomial.
#
#    real C(N+1), the projection coefficients.
#
#    real M, the number of evaluation points.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real V(M), the value of the projection function.
#
  import numpy as np

  PHI = hen_polynomial_value ( m, n, x )

  v = np.matmul ( PHI, c )

  return v

def he_plot ( a, b, index, filename ):

#*****************************************************************************80
#
## he_plot() plots HE(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the plotting range.
#
#    integer INDEX(*), the orders of 1 or more Hermite functions
#    to be plotted together.
#
#    string FILENAME, the name into which the graphics information is
#    to be stored.  Note that the PNG format will be used.
#
  import matplotlib.pyplot as plt
  import numpy as np

  m = 501
  x = np.linspace ( a, b, m )
  index_num = len ( index )

  plt.clf ( )

  for i in range ( 0, index_num ):
    n = index[i]
    y = he_polynomial_value ( m, n, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- He(i,x) --->' )
  plt.title ( 'Hermite polynomials He(n,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def he_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## he_polynomial_coefficients(): coefficients of He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     1
#     2     -1     0      1
#     3      0    -3      0      1
#     4      3     0     -6      0       1
#     5      0    15      0    -10       0     1
#     6    -15     0     45      0     -15     0      1
#     7      0  -105      0    105       0   -21      0     1
#     8    105     0   -420      0     210     0    -28     0      1
#     9      0   945      0  -1260       0   378      0   -36      0   1
#    10   -945     0   4725      0   -3150     0    630     0    -45   0    1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the Hermite polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  if ( n < 0 ):
    return c

  c[0,0] = 1.0

  if ( n == 0 ):
    return c

  c[1,1] = 1.0
 
  for i in range ( 2, n + 1 ):
    c[i,0]     =                             - ( i - 1 ) * c[i-2,0]
    c[i,1:i-1] =                c[i-1,0:i-2] - ( i - 1 ) * c[i-2,1:i-1]
    c[i,  i-1] =                c[i-1,  i-2]
    c[i,  i]   =                c[i-1,  i-1]

  return c

def he_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## he_polynomial_value() evaluates He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#  Differential equation:
#
#    ( exp ( - 0.5 * x^2 ) * He(n,x)' )' + n * exp ( - 0.5 * x^2 ) * He(n,x) = 0
#
#  First terms:
#
#   1
#   X
#   X^2  -  1
#   X^3  -  3 X
#   X^4  -  6 X^2 +   3
#   X^5  - 10 X^3 +  15 X
#   X^6  - 15 X^4 +  45 X^2 -   15
#   X^7  - 21 X^5 + 105 X^3 -  105 X
#   X^8  - 28 X^6 + 210 X^4 -  420 X^2 +  105
#   X^9  - 36 X^7 + 378 X^5 - 1260 X^3 +  945 X
#   X^10 - 45 X^8 + 630 X^6 - 3150 X^4 + 4725 X^2 - 945
#
#  Recursion:
#
#    He(0,X) = 1,
#    He(1,X) = X,
#    He(N,X) = X * He(N-1,X) - (N-1) * He(N-2,X)
#
#  Orthogonality:
#
#    Integral ( -oo < X < +oo ) exp ( - 0.5 * X^2 ) * He(M,X) He(N,X) dX 
#    = sqrt ( 2 * pi ) * N! * delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521192255,
#    LC: QA331.N57.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real P(M,N+1), the values of the probabilist's Hermite polynomials 
#    of index 0 through N.
#
  import numpy as np

  x = np.atleast_1d ( x )

  p = np.zeros ( [ m, n + 1 ] )

  p[0:m,0] = 1.0

  if ( n == 0 ):
    return p

  p[0:m,1] = x[0:m]
 
  for j in range ( 2, n + 1 ):
    p[0:m,j] = x[0:m] * p[0:m,j-1] - ( j - 1 ) * p[0:m,j-2]

  return p

def he_polynomial_values ( n_data ):

#*****************************************************************************80
#
## he_polynomial_values(): tabulated values of He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#    In Mathematica, the function can be evaluated by:
#
#      He(n,x) = HermiteH[n,x/Sqrt[2]] / Sqrt[2^n] 
#
#  First terms:
#
#   1
#   X
#   X^2  -  1
#   X^3  -  3 X
#   X^4  -  6 X^2 +   3
#   X^5  - 10 X^3 +  15 X
#   X^6  - 15 X^4 +  45 X^2 -   15
#   X^7  - 21 X^5 + 105 X^3 -  105 X
#   X^8  - 28 X^6 + 210 X^4 -  420 X^2 +  105
#   X^9  - 36 X^7 + 378 X^5 - 1260 X^3 +  945 X
#   X^10 - 45 X^8 + 630 X^6 - 3150 X^4 + 4725 X^2 - 945
#
#  Recursion:
#
#    He(0,X) = 1,
#    He(1,X) = X,
#    He(N,X) = X * He(N-1,X) - (N-1) * He(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < +oo ) exp ( - 0.5 * X^2 ) * He(M,X) He(N,X) dX 
#    = sqrt ( 2 * pi ) * N! * delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ((\
    1.000000000000000E+00, \
    5.000000000000000E+00, \
    24.00000000000000E+00, \
    110.0000000000000E+00, \
    478.0000000000000E+00, \
    1950.000000000000E+00, \
    7360.000000000000E+00, \
    25100.00000000000E+00, \
    73980.00000000000E+00, \
    169100.0000000000E+00, \
    179680.0000000000E+00, \
   -792600.0000000000E+00, \
   -5939480.000000000E+00, \
    0.000000000000000E+00, \
    6.281250000000000E+00, \
    6.000000000000000E+00, \
    18.00000000000000E+00, \
    90150.00000000000E+00 ))

  n_vec = np.array ((\
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5,  5 ))

  x_vec = np.array ((\
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    0.0E+00, \
    0.5E+00, \
    1.0E+00, \
    3.0E+00, \
    1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def he_polynomial_zeros ( nt ):

#*****************************************************************************80
#
## he_polynomial_zeros() computes the zeros of He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the degree of the polynomial.
#
#  Output:
#
#    real Z(NT,1), the zeros of the polynomial.
#
  import numpy as np

  aj = np.zeros ( nt )
  arg = np.linspace ( 1, nt, nt ) / 2.0
  bj = np.sqrt ( (arg ) )
  wts = np.zeros ( nt )
  wts[0] = np.sqrt ( np.sqrt ( np.pi ) )

  z, wts = imtqlx ( nt, aj, bj, wts )
#
#  Adjust for probabilist.
#
  z = z * np.sqrt ( 2.0 )

  return z

def he_quadrature_rule ( nt ):

#*****************************************************************************80
#
## he_quadrature_rule(): quadrature for He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the order of the rule.
#
#  Output:
#
#    real T(NT,1), WTS(NT,1), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( nt )
  arg = np.linspace ( 1, nt, nt ) / 2.0
  bj = np.sqrt ( arg )
  wts = np.zeros ( nt )
  wts[0] = np.sqrt ( np.sqrt ( np.pi ) )

  t, wts = imtqlx ( nt, aj, bj, wts )

  wts = wts ** 2
#
#  Adjust for probabilist.
#
  t = t * np.sqrt ( 2.0 )
  wts = wts * np.sqrt ( 2.0 )

  return t, wts

def hermite_function_values ( n_data ):

#*****************************************************************************80
#
## hermite_function_values(): values of the Hermite function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Hf(n,x) = HermiteH[n,x] 
#        * Exp [ -1/2 * x^2] / Sqrt [ 2^n * n! * Sqrt[Pi] ]
#
#    The Hermite functions are orthonormal:
#
#      Integral ( -oo < x < +oo ) Hf(m,x) Hf(n,x) dx = delta ( m, n )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 23

  f_vec = np.array ( ( \
    0.7511255444649425E+00,  0.0000000000000000E+00, -0.5311259660135985E+00, \
    0.0000000000000000E+00,  0.4599685791773266E+00,  0.0000000000000000E+00, \
    0.4555806720113325E+00,  0.6442883651134752E+00,  0.3221441825567376E+00, \
   -0.2630296236233334E+00, -0.4649750762925110E+00, -0.5881521185179581E-01, \
    0.3905052515434106E+00,  0.2631861423064045E+00, -0.2336911435996523E+00, \
   -0.3582973361472840E+00,  0.6146344487883041E-01,  0.3678312067984882E+00, \
    0.9131969309166278E-01,  0.4385750950032321E+00, -0.2624689527931006E-01, \
    0.5138426125477819E+00,  0.09355563118061758E+00 ))

  n_vec = np.array ( ( \
    0,  1,  2,  \
    3,  4,  5,  \
    0,  1,  2,  \
    3,  4,  5,  \
    6,  7,  8,  \
    9, 10, 11,  \
   12,  5,  5,  \
    5,  5  ))

  x_vec = np.array ( ( \
    0.0E+00, 0.0E+00, 0.0E+00, \
    0.0E+00, 0.0E+00, 0.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 0.5E+00, 2.0E+00, \
    3.0E+00, 4.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def hermite_polynomial_plot01 ( ):

#*****************************************************************************80
#
## hermite_polynomial_plot01() tests hf_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_polynomial_plot01():' )
  print ( '  hf_plot() creates a plot of one or more Hermite functions.' )

  a = - 5.0
  b = + 5.0
  index = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'hf_plot.png'

  hf_plot ( a, b, index, filename )

  return

def hermite_polynomial_plot02 ( ):

#*****************************************************************************80
#
## hermite_polynomial_plot02() tests he_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_polynomial_plot02():' )
  print ( '  he_plot() plots one or more Hermite polynomials.' )

  a = - 2.0
  b = + 2.0
  index = np.array ( [ 0, 1, 2, 3, 4 ] )
  filename = 'he_plot.png'

  he_plot ( a, b, index, filename )

  return

def hermite_polynomial_test01 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test01() tests h_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_polynomial_test01():' )
  print ( '  h_polynomial_values() stores values of' )
  print ( '  the physicist Hermite polynomials.' )
  print ( '  h_polynomial_value() evaluates the polynomial.' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           H(N,X)                    H(N,X)                     Error' )

  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = h_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2_vec = h_polynomial_value ( 1, n, x )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12f  %24.16e  %24.16e  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def hermite_polynomial_test02 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test02() tests he_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_polynomial_test02():' )
  print ( '  he_polynomial_values() stores values of' )
  print ( '  the probabilist Hermite polynomials.' )
  print ( '  he_polynomial_value() evaluates the polynomial.' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X          He(N,X)                   He(N,X)                     Error' )

  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = he_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2_vec = he_polynomial_value ( 1, n, x )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12f  %24.16e  %24.16e  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def hermite_polynomial_test03 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test03() tests hf_function_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_polynomial_test03():' )
  print ( '  hf_function_values() stores values of' )
  print ( '  the Hermite function Hf(n,x).' )
  print ( '  hf_function_value() evaluates the function.' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X          Hf(N,X)                   Hf(N,X)                     Error' )

  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = hf_function_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2_vec = hf_function_value ( 1, n, x )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12f  %24.16e  %24.16e  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def hermite_polynomial_test04 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test04() tests h_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_polynomial_test04():' )
  print ( '  h_polynomial_zeros() computes the zeros of H(n,x)' )
  print ( '  Check by calling h_polynomial() there.' )

  for degree in range ( 1, 6 ):

    z = h_polynomial_zeros ( degree )
    my_title = '  Computed zeros for H(' + str ( degree ) + ',z):'
    r8vec_print ( degree, z, my_title )

    hz = h_polynomial_value ( degree, degree + 1, z )
    my_title = '  Evaluate H(' + str ( degree ) + ',z):'
    r8vec_print ( degree, hz[0:degree,degree], my_title )

  return

def hermite_polynomial_test05 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test05() tests he_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_polynomial_test05():' )
  print ( '  he_polynomial_zeros() computes the zeros of He(n,x)' )
  print ( '  Check by calling he_polynomial() there.' )

  for degree in range ( 1, 6 ):

    z = he_polynomial_zeros ( degree )
    my_title = '  Computed zeros for He(' + str ( degree ) + ',z):'
    r8vec_print ( degree, z, my_title )

    hz = he_polynomial_value ( degree, degree + 1, z )
    my_title = '  Evaluate He(' + str ( degree ) + ',z):'
    r8vec_print ( degree, hz[0:degree,degree], my_title )

  return

def hermite_polynomial_test06 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test06() tests h_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_polynomial_test06():' )
  print ( '  h_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with H(n,x)' )

  n = 7
  x, w = h_quadrature_rule ( n )

  r8vec2_print ( x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -oo < X < +00 ) X^E exp(-X^2) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  for e in range ( 0, 2 * n ):

    if ( e == 0 ):
      f = np.ones ( n )
    else:
      f = x ** e

    q = np.dot ( w, f )
    q_exact = h_integral ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def hermite_polynomial_test07 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test07() tests he_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_polynomial_test07():' )
  print ( '  he_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with He(n,x)' )

  n = 7
  x, w = he_quadrature_rule ( n )

  r8vec2_print ( x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -oo < X < +00 ) X^E exp(-X^2) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  for e in range ( 0, 2 * n ):

    if ( e == 0 ):
      f = np.ones ( n )
    else:
      f = x ** e

    q = np.dot ( w, f )
    q_exact = he_integral ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def hermite_polynomial_test08 ( p, b ):

#*****************************************************************************80
#
## hermite_polynomial_test08() tests hn_exponential_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    real B, the coefficient of X in the exponential factor.
#
  print ( '' )
  print ( 'hermite_polynomial_test08():' )
  print ( '  Compute a normalized physicist Hermite exponential product table.' )
  print ( '' )
  print ( '  Tij = integral ( -oo < X < +oo ) exp(B*X) Hn(I,X) Hn(J,X) exp(-X*X) dx' )
  print ( '' )
  print ( '  where Hn(I,X) = normalized physicist Hermite polynomial of degree I.' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponential argument coefficient B = ', b )

  table = hn_exponential_product ( p, b )

  r8mat_print ( p + 1, p + 1, table, '  Exponential product table:' )

  return

def hermite_polynomial_test09 ( p, e ):

#*****************************************************************************80
#
## hermite_polynomial_test09() tests hn_power_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    integer E, the exponent of X in the integrand.
#
  print ( '' )
  print ( 'hermite_polynomial_test09():' )
  print ( '  Compute a normalized physicist Hermite polynomial power product table.' )
  print ( '' )
  print ( '  Tij = integral ( -oo < X < +oo ) X^E Hn(I,X) Hn(J,X) exp(-X*X) dx' )
  print ( '' )
  print ( '  where Hn(I,X) = normalized physicist Hermite polynomial of degree I.' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponent of X = ', e )

  table = hn_power_product ( p, e )

  r8mat_print ( p + 1, p + 1, table, '  Power product table:' )

  return

def hermite_polynomial_test10 ( p, b ):

#*****************************************************************************80
#
## hermite_polynomial_test10() tests hen_exponential_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    real B, the coefficient of X in the exponential factor.
#
  print ( '' )
  print ( 'hermite_polynomial_test10():' )
  print ( '  Compute a normalized probabilist Hermite exponential product table.' )
  print ( '' )
  print ( '  Tij = integral ( -oo < X < +oo ) exp(B*X) Hen(I,X) Hen(J,X) exp(-0.5*X*X) dx' )
  print ( '' )
  print ( '  where Hen(I,X) = normalized physicist Hermite polynomial of degree I.' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponential argument coefficient B = ', b )

  table = hen_exponential_product ( p, b )

  r8mat_print ( p + 1, p + 1, table, '  Exponential product table:' )

  return

def hermite_polynomial_test11 ( p, e ):

#*****************************************************************************80
#
## hermite_polynomial_test11() tests hen_power_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    integer E, the exponent of X in the integrand.
#
  print ( '' )
  print ( 'hermite_polynomial_test11():' )
  print ( '  Compute a normalized probabilist Hermite polynomial power product table.' )
  print ( '' )
  print ( '  Tij = integral ( -oo < X < +oo ) X^E Hen(I,X) Hen(J,X) exp(-0.5*X*X) dx' )
  print ( '' )
  print ( '  where Hen(I,X) = normalized probabilist Hermite polynomial of degree I.' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponent of X = ', e )

  table = hen_power_product ( p, e )

  r8mat_print ( p + 1, p + 1, table, '  Power weighted table:' )

  return

def hermite_polynomial_test12 ( p, b ):

#*****************************************************************************80
#
## hermite_polynomial_test12() tests hf_exponential_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    real B, the coefficient of X in the exponential factor.
#
  print ( '' )
  print ( 'hermite_polynomial_test12():' )
  print ( '  Compute a Hermite function exponential product table.' )
  print ( '' )
  print ( '  Tij = integral ( -oo < X < +oo ) exp(B*X) Hf(I,X) Hf(J,X) dx' )
  print ( '' )
  print ( '  where Hf(I,X) = Hermite function of "degree" I.' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponential argument coefficient B = ', b )

  table = hf_exponential_product ( p, b )

  r8mat_print ( p + 1, p + 1, table, '  Exponential product table:' )

  return

def hermite_polynomial_test13 ( p, e ):

#*****************************************************************************80
#
## hermite_polynomial_test13() tests hf_power_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    integer E, the exponent of X in the integrand.
#
  print ( '' )
  print ( 'hermite_polynomial_test13():' )
  print ( '  Compute a Hermite function power product table.' )
  print ( '' )
  print ( '  Tij = integral ( -oo < X < +oo ) X^E Hf(I,X) Hf(J,X) dx' )
  print ( '' )
  print ( '  where Hf(I,X) = Hermite function of "degree" I.' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponent of X = ', e )

  table = hf_power_product ( p, e )

  r8mat_print ( p + 1, p + 1, table, '  Power product table:' )

  return

def hermite_polynomial_test14 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test14() tests h_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'hermite_polynomial_test14():' )
  print ( '  h_polynomial_coefficients() determines the physicist Hermite ' )
  print ( '  polynomial coefficients.' )

  c = h_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):

    print ( '' )
    print ( '  H(', i, ') = ' )
    print ( '' )

    for j in range ( i, -1, -1 ):

      if ( c[i,j] == 0.0 ):
        pass
      elif ( j == 0 ):
        print ( '  %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '  %f * x' % ( c[i,j] ) )
      else:
        print ( '  %f * x^%d' % ( c[i,j], j ) )

  return

def hermite_polynomial_test15 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test15() tests he_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'hermite_polynomial_test15():' )
  print ( '  he_polynomial_coefficients() determines the probabilist Hermite ' )
  print ( '  polynomial coefficients.' )

  c = he_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):

    print ( '' )
    print ( '  He(', i, ') = ' )
    print ( '' )

    for j in range ( i, -1, -1 ):

      if ( c[i,j] == 0.0 ):
        pass
      elif ( j == 0 ):
        print ( '  %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '  %f * x' % ( c[i,j] ) )
      else:
        print ( '  %f * x^%d' % ( c[i,j], j ) )

  return

def hermite_polynomial_test16 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test16() tests Hermite projection.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_polynomial_test16():' )
  print ( '  As a sanity check, make sure that the projection of' )
  print ( '  He(i,x) is 1 for the i-th component and zero for all others.' )

  n = 3

  x, w = he_quadrature_rule ( n + 1 )

  PHI = hen_polynomial_value ( n + 1, n, x )

  for j in range ( 0, n + 1 ):

    c = np.zeros ( n + 1 )

    PHIW = np.zeros ( [ n + 1, n + 1 ] )

    for i in range ( 0, n + 1 ):
      PHIW[i,0:n+1] = PHI[i,0:n+1] * w[i]

    c = np.matmul ( np.transpose ( PHIW ), PHI[0:n+1,j] )
    title =  '  Coefficients for He(' + str ( j ) + ',x)'

    r8vec_print ( n + 1, c, title )

  return

def hermite_polynomial_test17 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test17() tests hen_projection() and hen_projection_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_polynomial_test17():' )
  print ( '  hen_projection() is given a function F(x), and computes' )
  print ( '  N+1 coefficients C that define Fhat(x), the projection of F(x)' )
  print ( '  onto the first N+1 normalized Hermite polynomials Hen(i,x).' )
  print ( '' )
  print ( '  It should be the case that the following two integrals are equal' )
  print ( '  for J = 0 to N:' )
  print ( '' )
  print ( '  Q1 = integral ( -oo < x < oo ) f(x)    Hen(j,x) exp(-x*x/2) dx' )
  print ( '  Q2 = integral ( -oo < x < oo ) Fhat(x) Hen(j,x) exp(-x*x/2) dx' )
#
#  Project f = poly1(1) onto Hermite polynomials 0 through 6.
#
  n = 6
  c1 = hen_projection ( n, poly1 )
#
#  Get a quadrature rule suitable for products of Hermite polynomials
#  up to degree 6.
#
  m = n + 1
  x, w = he_quadrature_rule ( m )
#
#  Evaluate Hermite polynomials 0 through N at the M quadrature points.
#
  phi = hen_polynomial_value ( m, n, x )
#
#  Evaluate the projected function, and the original function, 
#  at the quadrature points.
#
  v1 = poly1 ( m, x )
  v2 = hen_projection_value ( n, c1, m, x )
#
#  Compare the integrals of the function and its projection against
#  the Hermite polynomials of degree 0 through N.
#
  print ( '' )
  print ( '   J    Q1        Q2' )
  print ( '' )

  for j in range ( 0, n ):

    q1 = 0.0
    q2 = 0.0

    for i in range ( 0, m ):
      q1 = w[i] * v1[i] * phi[i,j]
      q2 = w[i] * v2[i] * phi[i,j]

    print ( '  %2d  %8g  %8g' % ( j, q1, q2 ) )

  return

def hermite_polynomial_test18 ( ):

#*****************************************************************************80
#
## hermite_polynomial_test18() tests hen_projection_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_polynomial_test18():' )
  print ( '  hen_projection_data() is given M data points (x,fx)' )
  print ( '  and uses least squares to derive projection coefficients' )
  print ( '  onto the first N+1 normalized Hermite polynomials Hen(0:n,x).' )
#
#  Project 20 data values (x,exp(x)) onto Hermite polynomials 0 through 5.
#
  a = -5.0
  b = +5.0
  m = 21
  x = np.linspace ( a, b, m )
  d = np.exp ( x )
  n = 5
  c = hen_projection_data ( m, n, x, d )
  r8vec_print ( n + 1, c, \
    '  Hen(0:5) projection coefficients for 21 exp(x) data values' )
#
#  Project 6 data values from (x,exp(x)) onto Hermite polynomials 0 through 5.
#
  a = -5.0
  b = +5.0
  m = 6
  x = np.linspace ( a, b, m )
  d = np.exp ( x )
  n = 5
  c = hen_projection_data ( m, n, x, d )
  r8vec_print ( n + 1, c, \
    '  Hen(0:5) projection coefficients for 6 exp(x) data values' )
#
#  Project exp(x) onto Hermite polynomials 0 through 5.
#
  n = 5
  c = hen_projection ( n, exp_fun )
  r8vec_print ( n + 1, c, \
    '  Hen(0:5) projection coefficients for exp(x) function' )

  return

def hermite_poly_phys_values ( n_data ):

#*****************************************************************************80
#
## hermite_poly_phys_values() returns some values of the physicist's Hermite polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      HermiteH[n,x]
#
#  Differential equation:
#
#    Y'' - 2 X Y' + 2 N Y = 0
#
#  First terms:
#
#      1
#      2 X
#      4 X^2     -  2
#      8 X^3     - 12 X
#     16 X^4     - 48 X^2     + 12
#     32 X^5    - 160 X^3    + 120 X
#     64 X^6    - 480 X^4    + 720 X^2    - 120
#    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
#    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
#    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
#   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < +oo ) exp ( - X^2 ) * H(N,X)^2 dX
#    = sqrt ( PI ) * 2^N * N!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.1000000000000000E+02, \
      0.9800000000000000E+02, \
      0.9400000000000000E+03, \
      0.8812000000000000E+04, \
      0.8060000000000000E+05, \
      0.7178800000000000E+06, \
      0.6211600000000000E+07, \
      0.5206568000000000E+08, \
      0.4212712000000000E+09, \
      0.3275529760000000E+10, \
      0.2432987360000000E+11, \
      0.1712370812800000E+12, \
      0.0000000000000000E+00, \
      0.4100000000000000E+02, \
     -0.8000000000000000E+01, \
      0.3816000000000000E+04, \
      0.3041200000000000E+07 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5,  5 ))

  x_vec = np.array ( ( \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     0.0E+00, \
     0.5E+00, \
     1.0E+00, \
     3.0E+00, \
     1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def hermite_poly_prob_values ( n_data ):

#*****************************************************************************80
#
## hermite_poly_prob_values(): values of the probabilist's Hermite polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      He(n,x) = HermiteH[n,x/Sqrt[2]] / Sqrt [ 2^n ] 
#
#  First terms:
#
#   1
#   X
#   X^2  -  1
#   X^3  -  3 X
#   X^4  -  6 X^2 +   3
#   X^5  - 10 X^3 +  15 X
#   X^6  - 15 X^4 +  45 X^2 -   15
#   X^7  - 21 X^5 + 105 X^3 -  105 X
#   X^8  - 28 X^6 + 210 X^4 -  420 X^2 +  105
#   X^9  - 36 X^7 + 378 X^5 - 1260 X^3 +  945 X
#   X^10 - 45 X^8 + 630 X^6 - 3150 X^4 + 4725 X^2 - 945
#
#  Recursion:
#
#    He(0,X) = 1,
#    He(1,X) = X,
#    He(N,X) = X * He(N-1,X) - (N-1) * He(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < +oo ) exp ( - 0.5 * X^2 ) * He(M,X) He(N,X) dX 
#    = sqrt ( 2 * pi ) * N! * delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ((\
    1.000000000000000E+00, \
    5.000000000000000E+00, \
    24.00000000000000E+00, \
    110.0000000000000E+00, \
    478.0000000000000E+00, \
    1950.000000000000E+00, \
    7360.000000000000E+00, \
    25100.00000000000E+00, \
    73980.00000000000E+00, \
    169100.0000000000E+00, \
    179680.0000000000E+00, \
   -792600.0000000000E+00, \
   -5939480.000000000E+00, \
    0.000000000000000E+00, \
    6.281250000000000E+00, \
    6.000000000000000E+00, \
    18.00000000000000E+00, \
    90150.00000000000E+00 ))

  n_vec = np.array ((\
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5,  5 ))

  x_vec = np.array ((\
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    0.0E+00, \
    0.5E+00, \
    1.0E+00, \
    3.0E+00, \
    1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def he_triple_product_integral ( i, j, k ):

#*****************************************************************************80
#
## he_triple_product_integral(): integral of H(i,x)*H(j,x)*H(k,x)*e^(-x^2/2).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#    VALUE = integral ( -oo < x < +oo ) H(i,x)*H(j,x)*H(k,x) exp(-x^2/2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongbin Xiu,
#    Numerical Methods for Stochastic Computations: A Spectral Method Approach,
#    Princeton, 2010,
#    ISBN13: 978-0-691-14212-8,
#    LC: QA274.23.X58.
#
#  Input:
#
#    integer I, J, K, the polynomial indices.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.math import factorial

  s = ( ( i + j + k ) // 2 )

  if ( s < i or s < j or s < k ):
    value = 0.0
  elif ( ( ( i + j + k ) % 2 ) != 0 ):
    value = 0.0
  else:
    value = factorial ( i ) / factorial ( s - i ) \
          * factorial ( j ) / factorial ( s - j ) \
          * factorial ( k ) / factorial ( s - k )

  return value

def hf_exponential_product ( p, b ):

#*****************************************************************************80
#
## hf_exponential_product(): exponential products, exp(b*x)*Hf(i,x)*Hf(j,x).
#
#  Discussion:
#
#    Hf(I,X) represents the Hermite function of "degree" I.  
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of exp(B*X) with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -oo < X < +oo ) exp(B*X) * Hf(I,X) * Hf(J,X) dx
#
#    We will estimate these integrals using Gauss-Hermite quadrature.
#    Because of the exponential factor exp(B*X), the quadrature will not 
#    be exact.
#
#    However, when B = 0, the quadrature is exact, and moreoever, the
#    table will be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    real B, the coefficient of X in the exponential factor.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.  TABLE(I,J)
#    represents the integral of exp(B*X) * Hf(I+1,X) * Hf(J+1,X).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = ( ( 3 * p + 4 ) // 2 )

  x_table, w_table = hf_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    h_table = hf_function_value ( 1, p, x )
#
#  The following formula is an outer product in H_TABLE.
#
    table = table + \
      + w_table[k] * np.exp ( b * x ) * np.outer ( h_table, h_table )

  return table

def hf_function_value ( m, n, x ):

#*****************************************************************************80
#
## hf_function_value() evaluates Hf(i,x).
#
#  Discussion:
#
#    Hf(I,X) represents the Hermite function of "degree" I.  
#
#    The Hermite function of degree n is related to the physicist's
#    Hermite polynomial H(n,x):
#
#      Hf(n,x) = H(n,x) * exp ( - 0.5 * x^2 ) / sqrt ( 2^n n! sqrt ( pi ) )
#
#    The Hermite functions are orthonormal:
#
#      Integral ( -oo < x < +oo ) Hf(m,x) Hf(n,x) dx = delta ( m, n )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521192255,
#    LC: QA331.N57.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real F(M,N+1), the values of the Hermite functions 
#    of index 0 through N at the evaluation points.
#
  import numpy as np

  x = np.atleast_1d ( x )

  f = np.zeros ( [ m, n + 1 ] )

  f[0:m,0] = np.exp ( - 0.5 * x[0:m]**2 ) / np.sqrt ( np.sqrt ( np.pi ) )

  if ( n == 0 ):
    return f

  f[0:m,1] = 2.0 * np.exp ( - 0.5 * x[0:m]**2 ) * x[0:m] \
    / np.sqrt ( 2.0 * np.sqrt ( np.pi ) )

  for j in range ( 2, n + 1 ):
    f[0:m,j] = ( np.sqrt ( 2.0 ) * x[0:m] * f[0:m,j-1] \
      - np.sqrt ( j - 1 ) * f[0:m,j-2] ) / np.sqrt ( j )
 
  return f

def hf_function_values ( n_data ):

#*****************************************************************************80
#
## hf_function_values(): tabulated values of Hf(i,x).
#
#  Discussion:
#
#    Hf(I,X) represents the Hermite function of "degree" I.  
#
#    In Mathematica, the function can be evaluated by:
#
#      Hf(n,x) = HermiteH[n,x] 
#        * Exp [ -1/2 * x^2] / Sqrt [ 2^n * n! * Sqrt[Pi] ]
#
#    The Hermite functions are orthonormal:
#
#      Integral ( -oo < x < +oo ) Hf(m,x) Hf(n,x) dx = delta ( m, n )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 23

  f_vec = np.array ( ( \
    0.7511255444649425E+00,  0.0000000000000000E+00, -0.5311259660135985E+00, \
    0.0000000000000000E+00,  0.4599685791773266E+00,  0.0000000000000000E+00, \
    0.4555806720113325E+00,  0.6442883651134752E+00,  0.3221441825567376E+00, \
   -0.2630296236233334E+00, -0.4649750762925110E+00, -0.5881521185179581E-01, \
    0.3905052515434106E+00,  0.2631861423064045E+00, -0.2336911435996523E+00, \
   -0.3582973361472840E+00,  0.6146344487883041E-01,  0.3678312067984882E+00, \
    0.9131969309166278E-01,  0.4385750950032321E+00, -0.2624689527931006E-01, \
    0.5138426125477819E+00,  0.09355563118061758E+00 ))

  n_vec = np.array ( ( \
    0,  1,  2,  \
    3,  4,  5,  \
    0,  1,  2,  \
    3,  4,  5,  \
    6,  7,  8,  \
    9, 10, 11,  \
   12,  5,  5,  \
    5,  5  ))

  x_vec = np.array ( ( \
    0.0E+00, 0.0E+00, 0.0E+00, \
    0.0E+00, 0.0E+00, 0.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 0.5E+00, 2.0E+00, \
    3.0E+00, 4.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def hf_plot ( a, b, index, filename ):

#*****************************************************************************80
#
## hf_plot() plots Hermite functions Hf(i,x).
#
#  Discussion:
#
#    Hf(I,X) represents the Hermite function of "degree" I.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the plotting range.
#
#    integer INDEX(*), the orders of 1 or more Hermite functions
#    to be plotted together.
#
#    string FILENAME, the name into which the graphics information is
#    to be stored.  Note that the PNG format will be used.
#
  import matplotlib.pyplot as plt
  import numpy as np

  m = 501
  x = np.linspace ( a, b, m )
  index_num = len ( index )

  plt.clf ( )

  for i in range ( 0, index_num ):
    n = index[i]
    y = hf_function_value ( m, n, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Hf(n,x) --->' )
  plt.title ( 'Hermite functions Hf(n,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hf_power_product ( p, e ):

#*****************************************************************************80
#
## hf_power_product(): power products x^e*Hf(i,x)*Hf(j,x).
#
#  Discussion:
#
#    Hf(I,X) represents the Hermite function of "degree" I.  
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of X with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -oo < X < +oo ) X^E * Hf(I,X) * Hf(J,X) dx
#
#    We will estimate these integrals using Gauss-Hermite quadrature.
#
#    When E is 0, the computed table should be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    integer E, the exponent of X in the integrand.
#    0 <= E.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.  TABLE(I,J)
#    represents the integral of X^E * Hf(I+1,X) * Hf(J+1,X).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = p + 1 + ( ( e + 1 ) // 2 )

  x_table, w_table = hf_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    h_table = hf_function_value ( 1, p, x )
#
#  The following formula is an outer product in H_TABLE.
#
    if ( e == 0 ):
      table = table + w_table[k] * np.outer ( h_table, h_table )
    else:
      table = table + w_table[k] * x ** e * np.outer ( h_table, h_table )

  return table

def hf_quadrature_rule ( nt ):

#*****************************************************************************80
#
## hf_quadrature_rule(): quadrature for Hf(i,x).
#
#  Discussion:
#
#    Hf(I,X) represents the Hermite function of "degree" I.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the order of the rule.
#
#  Output:
#
#    real T(NT,1), WTS(NT,1), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( nt )
  arg = np.linspace ( 1, nt, nt ) / 2.0
  bj = np.sqrt ( arg )
  wts = np.zeros ( nt )
  wts[0] = np.sqrt ( np.sqrt ( np.pi ) )

  t, wts = imtqlx ( nt, aj, bj, wts )

  wts = wts ** 2 * np.exp ( t ** 2 )

  return t, wts

def h_integral ( n ):

#*****************************************************************************80
#
## h_integral() evaluates the integral of H(i,x).
#
#  Discussion:
#
#    H(i,x) is the physicist's Hermite polynomial of degree I.
#
#    The integral computed is:
#
#      integral ( -oo < x < +oo ) H(i,x) exp(-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the integral.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):

    value = 0.0

  else:

    value = r8_factorial2 ( n - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( n / 2 )

  return value

def hn_exponential_product ( p, b ):

#*****************************************************************************80
#
## hn_exponential_product(): exponential products exp(b*x)*Hn(i,x)*Hn(j,x).
#
#  Discussion:
#
#    Hn(i,x) is the normalized physicist's Hermite polynomial of degree I. 
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of exp(B*X) with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -oo < X < +oo ) exp(B*X) * Hn(I,X) * Hn(J,X) exp(-X*X) dx
#
#    We will estimate these integrals using Gauss-Hermite quadrature.
#    Because of the exponential factor exp(B*X), the quadrature will not 
#    be exact.
#
#    However, when B = 0, the quadrature is exact, and moreoever, the
#    table will be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    real B, the coefficient of X in the exponential factor.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.  TABLE(I,J)
#    represents the weighted integral of exp(B*X) * Hn(I+1,X) * Hn(J+1,X).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = ( ( 3 * p + 4 ) // 2 )

  x_table, w_table = h_quadrature_rule ( order )
  r8vec2_print ( x_table, w_table, '  Quadrature rule:' )

  for k in range ( 0, order ):

    x = x_table[k]
    h_table = hn_polynomial_value ( 1, p, x )
#
#  The following formula is an outer product in H_TABLE.
#
    table = table \
      + w_table[k] * np.exp ( b * x ) * np.outer ( h_table, h_table )

  return table

def hn_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## hn_polynomial_value() evaluates the normalized physicist's Hermite polynomials.
#
#  Discussion:
#
#    Hn(i,x) is the normalized physicist's Hermite polynomial of degree I. 
#
#    These polynomials satisfy the orthonormality condition:
#
#      Integral ( -oo < X < +oo ) exp ( - X^2 ) * Hn(M,X) Hn(N,X) dX = delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521192255,
#    LC: QA331.N57.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real P(M,N+1), the values of the polynomials of index 0 through N.
#
  from scipy.special import gamma
  import numpy as np

  x = np.atleast_1d ( x )

  P = np.zeros ( [ m, n + 1 ] )

  P[0:m,0] = 1.0

  if ( n == 0 ):
    return P

  P[0:m,1] = 2.0 * x[0:m]
 
  for j in range ( 2, n + 1 ):
    P[0:m,j] = 2.0 * x[0:m] * P[0:m,j-1] - 2.0 * ( j - 1 ) * P[0:m,j-2]
#
#  Normalize.
#
  arg1 = np.linspace ( 1, n + 1, n + 1 )
  arg2 = 2.0 ** np.linspace ( 0, n, n + 1 )

  D = np.diag ( 1.0 / np.sqrt ( gamma ( arg1 ) * arg2 * np.sqrt ( np.pi ) ) )

  P = np.matmul ( P, D )

  return P

def hn_power_product ( p, e ):

#*****************************************************************************80
#
## hn_power_product(): power products x^e*Hn(i,x)*Hn(j,x).
#
#  Discussion:
#
#    Hn(i,x) is the normalized physicist's Hermite polynomial of degree I. 
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of X with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -oo < X < +oo ) X^E * Hn(I,X) * Hn(J,X) exp(-X*X) dx
#
#    We will estimate these integrals using Gauss-Hermite quadrature.
#
#    When E is 0, the computed table should be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    integer E, the exponent of X in the integrand.
#    0 <= E.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.  TABLE(I,J)
#    represents the weighted integral of X^E * Hn(I+1,X) * Hn(J+1,X).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = p + 1 + ( ( e + 1 ) // 2 )

  x_table, w_table = h_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    h_table = hn_polynomial_value ( 1, p, x )
#
#  The following formula is an outer product in H_TABLE.
#
    if ( e == 0 ):
      table = table + w_table[k] * np.outer ( h_table, h_table )
    else:
      table = table + w_table[k] * x ** e * np.outer ( h_table, h_table )

  return table

def h_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## h_polynomial_coefficients(): coefficients of H(i,x).
#
#  Discussion:
#
#    H(i,x) is the physicist's Hermite polynomial of degree I.
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     2
#     2     -2     0      4
#     3      0   -12      0      8
#     4     12     0    -48      0      16
#     5      0   120      0   -160       0    32
#     6   -120     0    720      0    -480     0     64
#     7      0 -1680      0   3360       0 -1344      0   128
#     8   1680     0 -13440      0   13440     0  -3584     0    256
#     9      0 30240      0 -80640       0 48384      0 -9216      0 512
#    10 -30240     0 302400      0 -403200     0 161280     0 -23040   0 1024 
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the Hermite polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  if ( n < 0 ):
    return c

  c[0,0] = 1.0

  if ( n == 0 ):
    return c

  c[1,1] = 2.0
 
  for i in range ( 2, n + 1 ):
    c[i,0]     =  -2.0 * ( i - 1 ) * c[i-2,0]
    c[i,1:i-1] =   2.0             * c[i-1,0:i-2] \
                  -2.0 * ( i - 1 ) * c[i-2,1:i-1]
    c[i,  i-1] =   2.0             * c[i-1,  i-2]
    c[i,  i]   =   2.0             * c[i-1,  i-1]
 
  return c

def h_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## h_polynomial_value() evaluates H(i,x).
#
#  Discussion:
#
#    H(i,x) is the physicist's Hermite polynomial of degree I.
#
#  Differential equation:
#
#    Y'' - 2 X Y' + 2 N Y = 0
#
#  First terms:
#
#      1
#      2 X
#      4 X^2     -  2
#      8 X^3     - 12 X
#     16 X^4     - 48 X^2     + 12
#     32 X^5    - 160 X^3    + 120 X
#     64 X^6    - 480 X^4    + 720 X^2    - 120
#    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
#    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
#    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
#   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Orthogonality:
#
#    Integral ( -oo < X < +oo ) exp ( - X^2 ) * H(M,X) H(N,X) dX 
#    = sqrt ( pi ) * 2^N * N! * delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521192255,
#    LC: QA331.N57.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real P(M,N+1), the values of the physicist's Hermite polynomials 
#    of index 0 through N.
#
  import numpy as np

  x = np.atleast_1d ( x )

  p = np.zeros ( [ m, n + 1 ] )

  p[0:m,0] = 1.0

  if ( n == 0 ):
    return p

  p[0:m,1] = 2.0 * x[0:m]
 
  for j in range ( 2, n + 1 ):
    p[0:m,j] = 2.0 * x[0:m] * p[0:m,j-1] - 2.0 * ( j - 1 ) * p[0:m,j-2]
 
  return p

def h_polynomial_values ( n_data ):

#*****************************************************************************80
#
## h_polynomial_values(): tabulated values of H(i,x).
#
#  Discussion:
#
#    H(i,x) is the physicist's Hermite polynomial of degree I.
#
#    In Mathematica, the function can be evaluated by:
#
#      HermiteH[n,x]
#
#  Differential equation:
#
#    Y'' - 2 X Y' + 2 N Y = 0
#
#  First terms:
#
#      1
#      2 X
#      4 X^2     -  2
#      8 X^3     - 12 X
#     16 X^4     - 48 X^2     + 12
#     32 X^5    - 160 X^3    + 120 X
#     64 X^6    - 480 X^4    + 720 X^2    - 120
#    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
#    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
#    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
#   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < +oo ) exp ( - X^2 ) * H(N,X)^2 dX
#    = sqrt ( PI ) * 2^N * N!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.1000000000000000E+02, \
      0.9800000000000000E+02, \
      0.9400000000000000E+03, \
      0.8812000000000000E+04, \
      0.8060000000000000E+05, \
      0.7178800000000000E+06, \
      0.6211600000000000E+07, \
      0.5206568000000000E+08, \
      0.4212712000000000E+09, \
      0.3275529760000000E+10, \
      0.2432987360000000E+11, \
      0.1712370812800000E+12, \
      0.0000000000000000E+00, \
      0.4100000000000000E+02, \
     -0.8000000000000000E+01, \
      0.3816000000000000E+04, \
      0.3041200000000000E+07 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5,  5 ))

  x_vec = np.array ( ( \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     0.0E+00, \
     0.5E+00, \
     1.0E+00, \
     3.0E+00, \
     1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def h_polynomial_zeros ( nt ):

#*****************************************************************************80
#
## h_polynomial_zeros(): zeros of H(i,x).
#
#  Discussion:
#
#    H(i,x) is the physicist's Hermite polynomial of degree I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the degree of the polynomial.
#
#  Output:
#
#    real Z(NT,1), the zeros of the polynomial.
#
  import numpy as np

  aj = np.zeros ( nt )
  arg = np.linspace ( 1, nt, nt ) / 2.0
  bj = np.sqrt ( arg )
  wts = np.zeros ( nt )
  wts[0] = np.sqrt ( np.sqrt ( np.pi ) )

  z, wts = imtqlx ( nt, aj, bj, wts )

  return z

def h_quadrature_rule ( nt ):

#*****************************************************************************80
#
## h_quadrature_rule(): quadrature for H(i,x).
#
#  Discussion:
#
#    H(i,x) is the physicist's Hermite polynomial of degree I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the order of the rule.
#
#  Output:
#
#    real T(NT,1), WTS(NT,1), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( nt )
  arg = np.linspace ( 1, nt, nt ) / 2.0
  bj = np.sqrt ( arg )
  wts = np.zeros ( nt )
  wts[0] = np.sqrt ( np.sqrt ( np.pi ) )

  t, wts = imtqlx ( nt, aj, bj, wts )

  wts = wts ** 2

  return t, wts

def imtqlx ( n, d, e, z ):

#*****************************************************************************80
#
## imtqlx() diagonalizes a symmetric tridiagonal matrix.
#
#  Discussion:
#
#    This routine is a version of the EISPACK routine to
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
#    25 February 2024
#
#  Author:
#
#    Original Fortran77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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

  epsilon = np.finfo(float).eps

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= epsilon * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
          break

      p = lam[l-1]

      if ( m == l ):
        break

      if ( itn <= j ):
        print ( '' )
        print ( 'imtqlx(): Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'imtqlx(): Fatal error!' )

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

def monomial_to_h_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_h_matrix(): the monomial to Physicist's Hermite conversion matrix.
#
#  Example:
#
#    N = 11
#    Each column must be scaled by the divisor listed below it.
#
#    1  .  2  .  12  .  120    .  1680     . 30240
#    .  1  .  6     60    .  840     . 15120     .
#    .  .  1  .  12  .  180    .  3369     . 75600
#    .  .  .  1   . 20    .  420     . 10080     .
#    .  .  .  .   1  .   30    .   840     . 24200
#    .  .  .  .   .  1    .   42     .  1512     .
#    .  .  .  .   .  .    1    .    56     .  2520
#    .  .  .  .   .  .    .    1     .    72     .
#    .  .  .  .   .  .    .    .     1     .    90
#    .  .  .  .   .  .    .    .     .     1     .
#    .  .  .  .   .  .    .    .     .     .     1
#
#   /1 /2 /4 /8 /16 /32 /64 /128  /256  /512 /1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  A[0,0] = 1.0

  if ( n == 1 ):
    return A

  A[1,1] = 0.5

  for j in range ( 3, n + 1 ):
    for i in range ( 1, n + 1 ):
      if ( i == 1 ):
        A[i-1,j-1] = ( ( j - 2 ) * A[i-1,j-3]              ) / 2.0
      else:
        A[i-1,j-1] = ( ( j - 2 ) * A[i-1,j-3] + A[i-2,j-2] ) / 2.0

  return A

def poly1 ( n, x ):

#*****************************************************************************80
#
## poly1() evaluates a sample polynomial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N:
#
#    real X: the evaluation point.
#
#  Output:
#
#    real VALUE: the value of the polynomial.
#
  value = 1.0 + 2.0 * x + 3.0 * x**2 + 4.0 * x**3 + 5.0 * x**5

  return value

def r8_factorial2 ( n ):

#*****************************************************************************80
#
## r8_factorial2() computes the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the double factorial function.
#    If N is less than 1, VALUE is returned as 1.
#
#  Output:
#
#    real VALUE, the value of the double factorial of N.
#
  value = 1;

  if ( n < 1 ):
    return value

  while ( 1 < n ):
    value = value * n
    n = n - 2

  return value

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
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

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value
 
def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#    In Python, use:
#
#      print ( title )
#      print ( np.c_ [ a1, a2 ] )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2024
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
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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
#    25 February 2024
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
  import numpy as np

  a = np.atleast_1d ( a )

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
#    25 February 2024
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
  hermite_polynomial_test ( )
  timestamp ( )

