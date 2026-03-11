#! /usr/bin/env python3
#
def laguerre_polynomial_test ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test() tests laguerre_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'laguerre_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test laguerre_polynomial().' )

  laguerre_polynomial_test01 ( )
  laguerre_polynomial_test02 ( )
  laguerre_polynomial_test03 ( )
  laguerre_polynomial_test04 ( )
  laguerre_polynomial_test05 ( )
  laguerre_polynomial_test06 ( )

  p = 5
  b = 0.0
  laguerre_polynomial_test07 ( p, b )

  p = 5
  b = 0.5
  laguerre_polynomial_test07 ( p, b )

  p = 5
  e = 0
  laguerre_polynomial_test08 ( p, e )

  p = 5
  e = 1
  laguerre_polynomial_test08 ( p, e )
#
#  Make some plots.
#
  a = 0.0
  b = 5.0
  index = np.array ( [ 0, 1, 2, 3, 4, 5, 10 ] )
  filename = 'l_polynomial.png'
  l_polynomial_plot ( a, b, index, filename )

  a = 0.0
  b = 5.0
  index = np.array ( [ 0, 1, 2, 3, 4, 5, 10 ] )
  index2 = np.array ( [ 1, 1, 1, 1, 1, 1, 1 ] )
  filename = 'lm1_polynomial.png'
  lm_polynomial_plot ( a, b, index, index2, filename )

  a = 0.0
  b = 5.0
  index = np.array ( [ 0, 1, 2, 3, 4, 5, 10 ] )
  index2 = np.array ( [ 2, 2, 2, 2, 2, 2, 2 ] )
  filename = 'lm2_polynomial.png'
  lm_polynomial_plot ( a, b, index, index2, filename )

  a = 0.0
  b = 5.0
  index =  np.array ( [ 0,   1,   2,   3,   4,   5,   10 ] )
  index2 = np.array ( [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 ] )
  filename = 'lf05_function.png'
  lf_function_plot ( a, b, index, index2, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'laguerre_polynomial_test():' )
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

def laguerre_polynomial_test01 ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test01() tests l_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 1

  print ( '' )
  print ( 'laguerre_polynomial_test01():' )
  print ( '  l_polynomial_values() stores values of' )
  print ( '  the Laguerre polynomials.' )
  print ( '  l_polynomial() evaluates the polynomial.' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           L(N,X)                    L(N,X)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = l_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xarray = np.array ( [ x ] )
    v = l_polynomial ( m, n, xarray )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12.6g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def laguerre_polynomial_test02 ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test02() tests l_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'laguerre_polynomial_test02()' )
  print ( '  l_polynomial_coefficients() determines polynomial coefficients of L(n,x).' )

  c = l_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):

    print ( '' )
    print ( '  L(', i, ') = ' )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( c[i,j] == 0.0 ):
        pass
      elif ( j == 0 ):
        print ( '  %g' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '  %g * x' % ( c[i,j] ) )
      else:
        print ( '  %g * x^%d' % ( c[i,j], j ) )
 
  return

def laguerre_polynomial_test03 ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test03() tests l_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laguerre_polynomial_test03():' )
  print ( '  l_polynomial_zeros() computes the zeros of L(n,x)' )
  print ( '  Check by calling l_polynomial() there.' )

  for degree in range ( 1, 6 ):

    z = l_polynomial_zeros ( degree )
    title = '  Computed zeros for L(' + str ( degree ) + ',z):'
    r8vec_print ( degree, z, title )

    lz = l_polynomial ( degree, degree, z )
    title = '  Evaluate L(' + str ( degree ) + ',z):'
    r8vec_print ( degree, lz[0:degree,degree], title )

  return

def laguerre_polynomial_test04 ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test04() tests l_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laguerre_polynomial_test04():' )
  print ( '  l_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with L(n,x)' )

  n = 7

  x, w = l_quadrature_rule ( n )

  r8vec2_print ( x, w,  '                  X             W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( 0 <= X < +00 ) X^E exp(-X) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  for e in range ( 0, 2 * n ):

    if ( e == 0 ):
      f = np.ones ( n )
    else:
      f = x**e

    q = np.dot ( w, f )
    q_exact = l_integral ( e )
    print ( '  %2d  %14.6g  %14.6g' % ( e, q, q_exact ) )

  return

def laguerre_polynomial_test05 ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test05() tests lm_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  mm = 1

  print ( '' )
  print ( 'laguerre_polynomial_test05():' )
  print ( '  lm_polynomial_values() stores values of' )
  print ( '  the Laguerre polynomial Lm(n,m,x)' )
  print ( '  lm_polynomial() evaluates the polynomial.' )
  print ( '' )
  print ( '                                 Tabulated                 Computed' )
  print ( '     N     M        X            Lm(N,M,X)                 Lm(N,M,X)               Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, fx1 = lm_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    v = lm_polynomial ( mm, n, m, x )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12.6g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def laguerre_polynomial_test06 ( ):

#*****************************************************************************80
#
## laguerre_polynomial_test06() tests lm_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'laguerre_polynomial_test06():' )
  print ( '  lm_polynomial_coefficients() determines polynomial coefficients of Lm(n,m,x).' )

  for m in range ( 0, 5 ):

    c = lm_polynomial_coefficients ( n, m )
 
    for i in range ( 0, n + 1 ):

      print ( '' )
      print ( '  Lm(', i, ',', m, ') = ' )
      print ( '' )

      for j in range ( i, -1, -1 ):

        if ( c[i,j] == 0.0 ):
          pass
        elif ( j == 0 ):
          print ( '  %g' % ( c[i,j] ) )
        elif ( j == 1 ):
          print ( '  %g * x' % ( c[i,j] ) )
        else:
          print ( '  %g * x^%d' % ( c[i,j], j ) )
 
  return

def laguerre_polynomial_test07 ( p, b ):

#*****************************************************************************80
#
## laguerre_polynomial_test07() tests l_exponential_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
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
  print ( 'laguerre_polynomial_test07():' )
  print ( '  Compute an exponential product table for L(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( 0 <= x < +oo ) exp(b*x) Ln(i,x) Ln(j,x) exp(-x) dx' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponential argument coefficient B = ', b )

  table = l_exponential_product ( p, b )

  r8mat_print ( p + 1, p + 1, table, '  Exponential product table:' )

  return

def laguerre_polynomial_test08 ( p, e ):

#*****************************************************************************80
#
## laguerre_polynomial_test08() tests l_power_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial factors.
#
#    integer E, the exponent of X.
#
  print ( '' )
  print ( 'laguerre_polynomial_test08():' )
  print ( '  Compute a power product table for L(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( 0 <= x < +oo ) x^e L(i,x) L(j,x) exp(-x) dx' )

  print ( '' )
  print ( '  Maximum degree P = ', p )
  print ( '  Exponent of X, E = ', e )

  table = l_power_product ( p, e )

  r8mat_print ( p + 1, p + 1, table, '  Power product table:' )

  return

def l_exponential_product ( p, b ):

#*****************************************************************************80
#
## l_exponential_product(): exponential product table for L(n,x).
#
#  Discussion:
#
#    Let L(n,x) represent the Laguerre polynomial of degree n.  
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of exp(B*X) with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( 0 <= X < +oo ) exp(b*x) * L(i,x) * L(j,x) * exp (-x) dx
#
#    Because of the exponential factor, the quadrature will not be exact.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial 
#    factors.  0 <= P.
#
#    real B, the coefficient of X in the exponential factor.
#
#  Output:
#
#    real TABLE(1:P+1,1:P+1), the table of integrals.  
#    TABLE(I+1,J+1) represents the weighted integral of exp(B*X) * L(i,x) * L(j,x).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = ( ( 3 * p + 4 ) // 2 )

  x_table, w_table = l_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    l_table = l_polynomial ( 1, p, x )

    for j in range ( 0, p + 1 ):
      for i in range ( 0, p + 1 ):
        table[i,j] = table[i,j] \
          + w_table[k] * np.exp ( b * x ) * l_table[0,i] * l_table[0,j]

  return table

def lf_function ( m, n, alpha, x ):

#*****************************************************************************80
#
## lf_function() evaluates the Laguerre function Lf(n,alpha,x).
#
#  Recursion:
#
#    Lf(0,ALPHA,X) = 1
#    Lf(1,ALPHA,X) = 1+ALPHA-X
#
#    Lf(N,ALPHA,X) = (2*N-1+ALPHA-X)/N * Lf(N-1,ALPHA,X) 
#                      - (N-1+ALPHA)/N * Lf(N-2,ALPHA,X)
#
#  Restrictions:
#
#    -1 < ALPHA
#
#  Special values:
#
#    Lf(N,0,X) = L(N,X).
#    Lf(N,M,X) = LM(N,M,X) for M integral.
#
#  Norm:
#
#    Integral ( 0 <= X < +oo ) exp ( - X ) * Lf(N,ALPHA,X)^2 dX
#    = Gamma ( N + ALPHA + 1 ) / N!
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2024
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
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order function to compute.
#
#    real ALPHA, the parameter.  -1 < ALPHA is required.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(M,N+1), the functions of 
#    degrees 0 through N at the evaluation points.
#
  import numpy as np

  v = np.zeros ( [ m, n + 1 ] )

  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'lf_function(): Fatal error!' )
    print ( '  The input value of ALPHA is #g', alpha )
    print ( '  but ALPHA must be greater than -1.' )
    raise Exception ( 'lf_function(): Fatal error!' )
 
  if ( n < 0 ):
    return v

  v[0:m,0] = 1.0

  if ( n == 0 ):
    return v

  v[0:m,1] = 1.0 + alpha - x[0:m]

  for j in range ( 2, n + 1 ):
    v[0:m,j] = ( ( 2 * j - 1 + alpha - x[0:m] ) * v[0:m,j-1]     \
              +  (   - j + 1 - alpha          ) * v[0:m,j-2] ) \
                /      j
  return v

def lf_function_plot ( a, b, index, index2, filename ):

#*****************************************************************************80
#
## lf_function_plot() plots Laguerre functions Lf(n,alpha,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the plotting range.
#
#    integer INDEX(*), the orders of 1 or more Laguerre functions.
#
#    integer INDEX2(*), the second "ALPHA" index.
#
#    string FILENAME, the name into which the graphics information is
#    to be stored.  Note that the PNG format will be used.
#
  import matplotlib.pyplot as plt
  import numpy as np

  mm = 501
  x = np.linspace ( a, b, mm )
  index_num = len ( index )

  plt.clf (  )

  for i in range ( 0, index_num ):
    n = index[i]
    alpha = index2[i]
    y = lf_function ( mm, n, alpha, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<---Lf(n,alpha,x) --->' )
  plt.title ( 'Laguerre Functions Lf(n,alpha,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def lf_function_values ( n_data ):

#*****************************************************************************80
#
## lf_function_values() returns some values of the Laguerre function Lf(n,alpha,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LaguerreL[n,a,x]
#
#    The functions satisfy the following differential equation:
#
#      X * Y'' + (ALPHA+1-X) * Y' + N * Y = 0
#
#    Function values can be generated by the recursion:
#
#      Lf(0,ALPHA,X) = 1
#      Lf(1,ALPHA,X) = 1+ALPHA-X
#
#      Lf(N,ALPHA,X) = ( (2*N-1+ALPHA-X) * Lf(N-1,ALPHA,X)
#                          - (N-1+ALPHA) * Lf(N-2,ALPHA,X) ) / N
#
#    The parameter ALPHA is required to be greater than -1.
#
#    For ALPHA = 0, the generalized Laguerre function Lf(N,ALPHA,X)
#    is equal to the Laguerre polynomial L(N,X).
#
#    For ALPHA integral, the generalized Laguerre function
#    Lf(N,ALPHA,X) equals the associated Laguerre polynomial Lm(N,ALPHA,X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real A, the parameter.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     0.00E+00, \
     0.25E+00, \
     0.50E+00, \
     0.75E+00, \
     1.50E+00, \
     2.50E+00, \
     5.00E+00, \
     1.20E+00, \
     1.20E+00, \
     1.20E+00, \
     1.20E+00, \
     1.20E+00, \
     1.20E+00, \
     5.20E+00, \
     5.20E+00, \
     5.20E+00, \
     5.20E+00, \
     5.20E+00, \
     5.20E+00, \
     5.20E+00 ))

  f_vec = np.array ( ( \
      0.3726399739583333E-01, \
      0.3494791666666667E+00, \
      0.8710042317708333E+00, \
      0.1672395833333333E+01, \
      0.6657625325520833E+01, \
      0.2395726725260417E+02, \
      0.2031344319661458E+03, \
      0.1284193996800000E+02, \
      0.5359924801587302E+01, \
      0.9204589064126984E+00, \
     -0.1341585114857143E+01, \
     -0.2119726307555556E+01, \
     -0.1959193658349206E+01, \
      0.1000000000000000E+01, \
      0.5450000000000000E+01, \
      0.1720125000000000E+02, \
      0.4110393750000000E+02, \
      0.8239745859375000E+02, \
      0.1460179186171875E+03, \
      0.2359204608298828E+03 ))

  n_vec = np.array ( ( \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     8, \
     8, \
     8, \
     8, \
     8, \
     8, \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     6 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     1.00E+00, \
     0.75E+00, \
     0.75E+00, \
     0.75E+00, \
     0.75E+00, \
     0.75E+00, \
     0.75E+00, \
     0.75E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, a, x, f

def lf_function_zeros ( n, alpha ):

#*****************************************************************************80
#
## lf_function_zeros() returns the zeros of Lf(n,alpha,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
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
#  Input:
#
#    integer N, the order.
#
#    real ALPHA, the exponent of the X factor.
#    ALPHA must be nonnegative.
#
#  Output:
#
#    real X(N), the zeros.
#
  from scipy.special import gamma
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = gamma ( alpha + 1.0 )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = ( i + 1 ) * ( i + 1 + alpha )
  bj = np.sqrt ( bj )

  x = np.linspace ( 1, 2 * n - 1 ) + alpha

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  return x

def lf_integral ( n, alpha ):

#*****************************************************************************80
#
## lf_integral() evaluates a monomial integral associated with Lf(n,alpha,x).
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * x^alpha * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the exponent.
#    0 <= N.
#
#    real ALPHA, the exponent of X in the weight function.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  arg = alpha + n + 1

  value = gamma ( arg )

  return value

def lf_quadrature_rule ( n, alpha ):

#*****************************************************************************80
#
## lf_quadrature_rule(): Gauss-Laguerre quadrature rule for Lf(n,alpha,x)
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) exp ( - x ) * x^alpha * f(x) dx
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
#    24 February 2024
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
#    integer N, the order.
#
#    real ALPHA, the exponent of the X factor.
#    ALPHA must be nonnegative.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  from scipy.special import gamma
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = gamma ( alpha + 1.0 )
#
#  Define the Jacobi matrix.
#
  b = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = ( i + 1 ) * ( i + 1 + alpha )
  bj = np.sqrt ( bj )

  x = np.linspace ( 1, 2 * n - 1, n ) + alpha

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  w = w**2

  return x, w

def l_integral ( n ):

#*****************************************************************************80
#
## l_integral() evaluates a monomial integral associated with L(n,x).
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the exponent.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial

  value = factorial ( n )

  return value

def lm_integral ( n, m ):

#*****************************************************************************80
#
## lm_integral() evaluates a monomial integral associated with Lm(n,m,x).
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * x^m * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    Input, integer N, the exponent.
#    0 <= N.
#
#    Input, integer M, the parameter.
#    0 <= M.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial

  value = factorial ( n + m )

  return value

def lm_polynomial_coefficients ( n, m ):

#*****************************************************************************80
#
## lm_polynomial_coefficients(): coefficients of Laguerre polynomial Lm(n,m,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2024
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
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    integer M, the parameter.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the
#    Laguerre polynomials of degree 0 through N.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  if ( n < 0 ):
    return c

  c[0,0] = 1.0

  if ( n == 0 ):
    return c

  c[1,0] = m + 1
  c[1,1] = -1.0
 
  for i in range ( 2, n + 1 ):

    c[i,0:i+1] = ( (   m + 2 * i - 1 ) * c[i-1,0:i+1]     \
             +     ( - m     - i + 1 ) * c[i-2,0:i+1] ) \
             /                 i

    c[i,1:i+1] = c[i,1:i+1] - c[i-1,0:i] / i

  return c

def lm_polynomial ( mm, n, m, x ):

#*****************************************************************************80
#
## lm_polynomial() evaluates Laguerre polynomials Lm(n,m,x).
#
#  First terms:
#
#    M = 0
#
#    Lm(0,0,X) =   1
#    Lm(1,0,X) =  -X   +  1
#    Lm(2,0,X) =   X^2 -  4 X   +  2
#    Lm(3,0,X) =  -X^3 +  9 X^2 -  18 X   +    6
#    Lm(4,0,X) =   X^4 - 16 X^3 +  72 X^2 -   96 X +     24
#    Lm(5,0,X) =  -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -  600 x   +  120
#    Lm(6,0,X) =   X^6 - 36 X^5 + 450 X^4 - 2400 X^3 + 5400 X^2 - 4320 X + 720
#
#    M = 1
#
#    Lm(0,1,X) =    0
#    Lm(1,1,X) =   -1,
#    Lm(2,1,X) =    2 X - 4,
#    Lm(3,1,X) =   -3 X^2 + 18 X - 18,
#    Lm(4,1,X) =    4 X^3 - 48 X^2 + 144 X - 96
#
#    M = 2
#
#    Lm(0,2,X) =    0
#    Lm(1,2,X) =    0,
#    Lm(2,2,X) =    2,
#    Lm(3,2,X) =   -6 X + 18,
#    Lm(4,2,X) =   12 X^2 - 96 X + 144
#
#    M = 3
#
#    Lm(0,3,X) =    0
#    Lm(1,3,X) =    0,
#    Lm(2,3,X) =    0,
#    Lm(3,3,X) =   -6,
#    Lm(4,3,X) =   24 X - 96
#
#    M = 4
#
#    Lm(0,4,X) =    0
#    Lm(1,4,X) =    0
#    Lm(2,4,X) =    0
#    Lm(3,4,X) =    0
#    Lm(4,4,X) =   24
#
#  Recursion:
#
#    Lm(0,M,X)   = 1 
#    Lm(1,M,X)   = (M+1-X)
#
#    if 2 <= N:
#
#      Lm(N,M,X)   = ( (M+2*N-1-X) * Lm(N-1,M,X) 
#                   +   (1-M-N)    * Lm(N-2,M,X) ) / N
#
#  Special values:
#
#    For M = 0, the associated Laguerre polynomials Lm(N,M,X) are equal 
#    to the Laguerre polynomials L(N,X).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2024
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
#  Input:
#
#    integer MM, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    integer M, the parameter.  M must be nonnegative.
#
#    real X(MM), the evaluation points.
#
#  Output:
#
#    real V(MM,N+1), the associated Laguerre polynomials 
#    of degrees 0 through N evaluated at the evaluation points.
#
  import numpy as np

  v = np.zeros ( [ mm, n + 1 ] )

  if ( m < 0 ):
    print ( '' )
    print ( 'lm_polynomial(): Fatal error!' )
    print ( '  Input value of M = ', m )
    print ( '  but M must be nonnegative.' )
    raise Exception ( 'lm_polynomial(): Fatal error!' )

  if ( n < 0 ):
    return v
#
#  If MM = 1, make sure x "looks like" an array.
#
  if ( mm == 1 ):
    x = np.atleast_1d ( x )

  v[0:mm,0] = 1.0

  if ( n == 0 ):
    return v

  v[0:mm,1] = m + 1 - x[0:mm]

  for j in range ( 2, n + 1 ):
    v[0:mm,j] = \
      ( ( (   m + 2 * j - 1 ) - x[0:mm] ) * v[0:mm,j-1]     \
        + ( - m     - j + 1 )             * v[0:mm,j-2] ) \
        /             j

  return v

def lm_polynomial_plot ( a, b, index, index2, filename ):

#*****************************************************************************80
#
## lm_polynomial_plot() plots Laguerre polynomials Lm(n,m,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the plotting range.
#
#    integer INDEX(*), the orders of 1 or more Laguerre polynomials
#    to be plotted together.
#
#    integer INDEX2(*), the second "M" index of the Laguerre polynomials.
#
#    string FILENAME, the name into which the graphics information is
#    to be stored.  Note that the PNG format will be used.
#
  import matplotlib.pyplot as plt
  import numpy as np

  mm = 501
  x = np.linspace ( a, b, mm )
  index_num = len ( index )

  plt.clf ( )

  for i in range ( 0, index_num ):
    n = index[i]
    m = index2[i]
    y = lm_polynomial ( mm, n, m, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<---Lm(n,m,x) --->' )
  plt.title ( 'Laguerre Polynomials Lm(n,m,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def lm_polynomial_values ( n_data ):

#*****************************************************************************80
#
## lm_polynomial_values() returns some values of Laguerre polynomials Lm(n,m,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LaguerreL[n,m,x]
#
#    The associated Laguerre polynomials may be generalized so that the 
#    parameter M is allowed to take on arbitrary noninteger values.
#    The resulting function is known as the generalized Laguerre function.
#    
#    The polynomials satisfy the differential equation:
#
#      X * Y'' + (M+1-X) * Y' + (N-M) * Y = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    integer M, the parameter.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.1625000000000000E+01, \
     0.1479166666666667E+01, \
     0.1148437500000000E+01, \
     0.4586666666666667E+00, \
     0.2878666666666667E+01, \
     0.8098666666666667E+01, \
     0.1711866666666667E+02, \
     0.1045328776041667E+02, \
     0.1329019368489583E+02, \
     0.5622453647189670E+02, \
     0.7484729341779436E+02, \
     0.3238912982762806E+03, \
     0.4426100000097533E+03, \
     0.1936876572288250E+04 ))

  m_vec = np.array ( ( \
    0, 0, 0, 0, \
    0, 1, 1, 1, \
    1, 0, 1, 2, \
    3, 2, 2, 3, \
    3, 4, 4, 5 ))

  n_vec = np.array ( ( \
    1,  2,  3,  4, \
    5,  1,  2,  3, \
    4,  3,  3,  3, \
    3,  4,  5,  6, \
    7,  8,  9, 10 ))

  x_vec = np.array ( ( \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def lm_polynomial_zeros ( n, m ):

#*****************************************************************************80
#
## lm_polynomial_zeros() returns the zeros for Lm(n,m,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
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
#  Input:
#
#    integer N, the order.
#
#    integer M, the parameter.
#    0 <= M.
#
#  Output:
#
#    real X(N), the zeros.
#
  from scipy.special import factorial
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = factorial ( m )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = ( i + 1 ) * ( i + 1 + m )
  bj = np.sqrt ( bj )

  x = np.linspace ( 1, 2 * n - 1, n ) + m

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  return x
 
def lm_quadrature_rule ( n, m ):

#*****************************************************************************80
#
## lm_quadrature_rule(): Gauss-Laguerre quadrature rule for Lm(n,m,x)
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) exp ( - x ) * x^m * f(x) dx
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
#    24 February 2024
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
#    integer N, the order.
#
#    integer M, the parameter.
#    0 <= M.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  from scipy.special import factorial
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = factorial ( m )
#
#  Define the Jacobi matrix.
#
  b = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = ( i + 1 ) * ( i + 1 + m )
  bj = np.sqrt ( bj )

  x = np.linspace ( 1, 2 * n - 1, n ) + m

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  w = w**2

  return x, w

def l_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## l_polynomial_coefficients(): coefficients of the Laguerre polynomial L(n,x).
#
#  First terms:
#
#    0: 1
#    1: 1  -1
#    2: 1  -2  1/2
#    3: 1  -3  3/2  1/6
#    4: 1  -4  4   -2/3  1/24
#    5: 1  -5  5   -5/3  5/24  -1/120
#
#  Recursion:
#
#    L(0) = ( 1,  0, 0, ..., 0 )
#    L(1) = ( 1, -1, 0, ..., 0 )
#    L(N) = (2*N-1-X) * L(N-1) - (N-1) * L(N-2) / N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
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
#    real C(1:N+1,1:N+1), the coefficients of the Laguerre polynomials 
#    of degree 0 through N.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  if ( n < 0 ):
    return c

  c[0:n+1,0] = 1.0

  if ( n == 0 ):
    return c

  c[1,1] = -1.0
 
  for i in range ( 2, n + 1 ):

    c[i,1:n+1] = ( \
        ( 2 * i - 1 ) * c[i-1,1:n+1] \
      + (   - i + 1 ) * c[i-2,1:n+1] \
      -                 c[i-1,0:n] ) / ( i )

  return c

def l_polynomial ( m, n, x ):

#*****************************************************************************80
#
## l_polynomial() evaluates the Laguerre polynomial L(n,x).
# 
#  First terms:
#
#      1
#     -X     +  1
#   (  X^2 -  4 X      +  2 ) / 2
#   ( -X^3 +  9 X^2 -  18 X    +    6 ) / 6
#   (  X^4 - 16 X^3 +  72 X^2 -   96 X +      24 ) / 24
#   ( -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -   600 X    +  120 ) / 120
#   (  X^6 - 36 X^5 + 450 X^4 - 2400 X^3 +  5400 X^2 -  4320 X     + 720 ) 
#     / 720
#   ( -X^7 + 49 X^6 - 882 X^5 + 7350 X^4 - 29400 X^3 + 52920 X^2 - 35280 X 
#     + 5040 ) / 5040
#
#  Recursion:
#
#    L(0,X) = 1
#    L(1,X) = 1 - X
#    L(N,X) = (2*N-1-X)/N * L(N-1,X) - (N-1)/N * L(N-2,X)
#
#  Orthogonality:
#
#    Integral ( 0 <= X < oo ) exp ( - X ) * L(N,X) * L(M,X) dX = delta ( M, N )
#
#  Relations:
#
#    L(N,X) = (-1)^N / N! * exp ( x ) * (d/dx)^n ( exp ( - x ) * x^n )  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2024
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
#    real V(M,1:N+1), the function values.
#
  import numpy as np

  v = np.zeros ( [ m, n + 1 ] )

  if ( n < 0 ):
    return v

  v[0:m,0] = 1.0

  if ( n == 0 ):
    return v
#
#  If M = 1, make sure X "looks like" an array.
#
  if ( m == 1 ):
    x = np.atleast_1d ( x )

  v[0:m,1] = 1.0 - x[0:m]
 
  for j in range ( 2, n + 1 ):

    v[0:m,j] = ( ( ( 2 * j - 1 ) - x[0:m] ) * v[0:m,j-1]   \
               +   (   - j + 1 )            * v[0:m,j-2] ) \
               /         j

  return v

def l_polynomial_plot ( a, b, index, filename ):

#*****************************************************************************80
#
## l_polynomial_plot() plots Laguerre polynomials L(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the plotting range.
#
#    integer INDEX(*), the orders of 1 or more Laguerre polynomials
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
    y = l_polynomial ( m, n, x )
    plt.plot ( x, y[:,n], linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<---L(n,x) --->' )
  plt.title ( 'Laguerre Polynomials L(n,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def l_polynomial_values ( n_data ):

#*****************************************************************************80
#
## l_polynomial_values() returns some values of the Laguerre polynomial.
#
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LaguerreL[n,x]
#
#  Differential equation:
#
#    X * Y'' + (1-X) * Y' + N * Y = 0
#
#  First terms:
#
#      1
#     -X   +  1
#   (  X^2 -  4 X   +   2 ) / 2
#   ( -X^3 +  9 X^2 -  18 X   +    6 ) / 6
#   (  X^4 - 16 X^3 +  72 X^2 -   96 X +      24 ) / 24
#   ( -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -   600 X   +   120 ) / 120
#   (  X^6 - 36 X^5 + 450 X^4 - 2400 X^3 +  5400 X^2 -  4320 X   +   720 ) / 720
#   ( -X^7 + 49 X^6 - 882 X^5 + 7350 X^4 - 29400 X^3 + 52920 X^2 - 35280 X + 5040 ) / 5040
#
#  Recursion:
#
#    L(0)(X) = 1,
#    L(1)(X) = 1-X,
#    N * L(N)(X) = (2*N-1-X) * L(N-1)(X) - (N-1) * L(N-2)(X)
#
#  Orthogonality:
#
#    Integral ( 0 <= X < oo ) exp ( - X ) * L(N)(X) * L(M)(X) dX
#    = 0 if N /= M
#    = 1 if N == M
#
#  Special values:
#
#    L(N)(0) = 1.
#
#  Relations:
#
#    L(N)(X) = (-1)^N / N! * exp ( x ) * (d/dx)^n ( exp ( - x ) * X^n )  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
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
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.0000000000000000E+00, \
     -0.5000000000000000E+00, \
     -0.6666666666666667E+00, \
     -0.6250000000000000E+00, \
     -0.4666666666666667E+00, \
     -0.2569444444444444E+00, \
     -0.4047619047619048E-01, \
      0.1539930555555556E+00, \
      0.3097442680776014E+00, \
      0.4189459325396825E+00, \
      0.4801341790925124E+00, \
      0.4962122235082305E+00, \
     -0.4455729166666667E+00, \
      0.8500000000000000E+00, \
     -0.3166666666666667E+01, \
      0.3433333333333333E+02 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5 ))

  x_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.5E+00, \
     3.0E+00, \
     5.0E+00, \
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

def l_polynomial_zeros ( n ):

#*****************************************************************************80
#
## l_polynomial_zeros(): zeros of the Laguerre polynomial L(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
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
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real X(N), the zeros.
#
  import numpy as np

  if ( n == 0 ):
    x = []
    return x
#
#  Define the zero-th moment.
#
  zemu = 1.0
#
#  Define the Jacobi matrix.
#
  bj = np.linspace ( 1, n, n )
  x = np.linspace ( 1, 2 * n - 1, n )
  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  return x

def l_power_product ( p, e ):

#*****************************************************************************80
#
## l_power_product(): power product table for L(n,x).
#
#  Discussion:
#
#    Let L(n,x) represent the Laguerre polynomial of degree n.  
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of X^E with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( 0 <= X < +oo ) x^e * L(i,x) * L(j,x) * exp (-x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial 
#    factors.  0 <= P.
#
#    integer E, the exponent of X.
#    0 <= E.
#
#  Output:
#
#    real TABLE(1:P+1,1:P+1), the table of integrals.  
#    TABLE(I+1,J+1) represents the weighted integral of x^E * L(i,x) * L(j,x).
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )

  order = p + 1 + ( ( e + 1 ) // 2 )

  x_table, w_table = l_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    l_table = l_polynomial ( 1, p, x )

    if ( e == 0 ):

      for j in range ( 0, p + 1 ):
        for i in range ( 0, p + 1 ):
          table[i,j] = table[i,j] + w_table[k] * l_table[0,i] * l_table[0,j]

    else:

      for j in range ( 0, p + 1 ):
        for i in range ( 0, p + 1 ):
          table[i,j] = table[i,j] \
            + w_table[k] * ( x ** e ) * l_table[0,i] * l_table[0,j]

  return table

def l_quadrature_rule ( n ):

#*****************************************************************************80
#
## l_quadrature_rule(): Gauss-Laguerre quadrature based on L(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
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
#    integer N, the order.
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
  zemu = 1.0
#
#  Define the Jacobi matrix.
#
  bj = np.linspace ( 1, n, n )
  x = np.linspace ( 1, 2 * n - 1, n )
  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  w = w**2

  return x, w

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
#    08 May 2020
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
#    08 May 2020
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
#    03 June 2013
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
#    05 October 2022
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
  laguerre_polynomial_test ( )
  timestamp ( )

