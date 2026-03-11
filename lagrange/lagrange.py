#! /usr/bin/env python3
#
def lagrange_test ( ):

#*****************************************************************************80
#
## lagrange_test() tests lagrange().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lagrange_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lagrange().' )

  lagrange_basis_antideriv_test ( )
  lagrange_basis_coef_test ( )
  lagrange_basis_deriv_test ( )
  lagrange_basis_deriv2_test ( )
  lagrange_basis_value_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_test():' )
  print ( '  Normal end of execution.' )

  return

def lagrange_basis_antideriv ( npol, ipol, xpol ):

#*****************************************************************************80
#
## lagrange_basis_antideriv() returns the antiderivative of a Lagrange basis polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the
#    Lagrange polynomials.  The entries in XPOL must be distinct.
#
#  Output:
#
#    real PCOF_ANTIDERIV(1:NPOL+1), the standard polynomial
#    coefficients of the antiderivative of the IPOL-th Lagrange polynomial:
#      L(IPOL)(X) = SUM ( 0 <= I <= NPOL ) PCOF_ANTIDERIV(I+1) * X^I
#

#
#  Get the standard polynomial coefficients of the ipol-th Lagrange
#  basis polynomial.
#
  pcof = lagrange_basis_coef ( npol, ipol, xpol )
#
#  Get the standard polynomial coefficients of the antiderivative of
#  the ipol-th Lagrange basis polynomial.
#
  pcof_antideriv = r8poly_ant_coef ( npol-1, pcof )

  return pcof_antideriv

def lagrange_basis_antideriv_test ( ):

#*****************************************************************************80
#
## lagrange_basis_antideriv_test() tests lagrange_basis_antideriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lagrange_basis_antideriv_test():' )
  print ( '  lagrange_basis_antideriv() evaluates the antiderivative' )
  print ( '  of a Lagrange basis polynomial.' )

  npol = 7
  ipol = 2
  xpol = np.linspace ( -3.0, +3.0, npol )
#
#  Get coefficients of antiderivative.
#
  pcof_antideriv = lagrange_basis_antideriv ( npol, ipol, xpol )

  nplot = 101
  xplot = np.linspace ( -3.3, +3.5, nplot )
  yplot = np.zeros ( nplot )

  for i in range ( 0, nplot ):
    yplot[i] = r8poly_value ( npol, pcof_antideriv, xplot[i] )

  plt.clf ( )
  plt.plot ( xplot, yplot, 'b-', linewidth = 2 )
  plt.plot ( [ -3.3, +3.5 ], [ 0.0, 0.0 ], 'k--' )
  for i in range ( 0, npol ):
    plt.plot ( xpol[i], 0.0, 'r.', markersize = 25 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- Antideriv(L(i)(X)) -->' )
  plt.title ( 'Anti(L(i)(X)) = i-th Lagrange basis polynomial antiderivative' )
  filename = 'lagrange_basis_antideriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def lagrange_basis_coef_test ( ):

#*****************************************************************************80
#
## lagrange_basis_coef_test() tests lagrange_basis_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  npol = 5

  print ( '' )
  print ( 'lagrange_basis_coef_test():' )
  print ( '  lagrange_basis_coef() returns the coefficients' )
  print ( '  for a Lagrange basis polynomial.' )

  npol = 7
  xpol = np.linspace ( -3.0, +3.0, npol )

  r8vec_print ( npol, xpol, '  Abscissas:' )

  for ipol in range ( 1, npol + 1 ):

    pcof = lagrange_basis_coef ( npol, ipol, xpol )

    s = '  L(%d)(x):' % ( ipol )
    r8poly_print ( pcof, s )

  return

def lagrange_basis_coef ( npol, ipol, xpol ):

#*****************************************************************************80
#
## lagrange_basis_coef() returns the coefficients of a Lagrange polynomial.
#
#  Discussion:
#
#    Given distinct abscissas XPOL(1:NPOL), the IPOL-th Lagrange
#    polynomial L(IPOL)(X) is defined as the polynomial of degree
#    NPOL - 1 which is 1 at XPOL(IPOL) and 0 at the NPOL - 1 other
#    abscissas.
#
#    A formal representation is:
#
#      L(IPOL)(X) = Product ( 1 <= I <= NPOL, I /= IPOL )
#       ( X - X(I) ) / ( X(IPOL) - X(I) )
#
#    However sometimes it is desirable to be able to write down
#    the standard polynomial coefficients of L(IPOL)(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the
#    Lagrange polynomials.  The entries in XPOL must be distinct.
#
#  Output:
#
#    real PCOF(1:NPOL), the standard polynomial
#    coefficients of the IPOL-th Lagrange polynomial:
#      L(IPOL)(X) = SUM ( 0 <= I <= NPOL-1 ) PCOF(I+1) * X^I
#
  import numpy as np
#
#  Make sure IPOL is legal.
#
  if ( ipol < 1 or npol < ipol ):
    print ( '' )
    print ( 'lagrange_basis_coef(): Fatal error!' )
    print ( '  1 <= IPOL <= NPOL is required.' )
    raise Exception ( 'lagrange_basis_coef(): Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'r8poly_lagrange_coef(): Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    raise Exception ( 'r8poly_lagrange_coef(): Fatal error!' )

  pcof = np.zeros ( npol )

  pcof[0] = 1.0

  indx = 0

  for i in range ( 1, npol + 1 ):

    if ( i != ipol ):

      indx = indx + 1

      for j in range ( indx, -1, -1 ):

        pcof[j] = - xpol[i-1] * pcof[j] / ( xpol[ipol-1] - xpol[i-1] )

        if ( 0 < j ):
          pcof[j] = pcof[j] + pcof[j-1] / ( xpol[ipol-1] - xpol[i-1] )

  return pcof

def lagrange_basis_deriv ( npol, ipol, xpol, xval ):

#*****************************************************************************80
#
## lagrange_basis_deriv(): derivative of the IPOL-th Lagrange basis polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the Lagrange
#    polynomials.  The entries in XPOL must be distinct.
#
#    real XVAL, the evaluation point.
#
#  Output:
#
#    real DPDX, the derivative of the IPOL-th 
#    Lagrange polynomial at XVAL.
#

#
#  Make sure IPOL is legal.
#
  if ( ipol < 1 or npol < ipol ):
    print ( '' )
    print ( 'lagrange_basis_deriv(): Fatal error!' )
    print ( '  1 <= IPOL <= NPOL is required.' )
    raise Exception ( 'lagrange_basis_deriv(): Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'lagrange_basis_deriv(): Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    raise Exception ( 'lagrange_basis_deriv(): Fatal error!' )
#
#  Evaluate the derivative, which can be found by summing up the result
#  of differentiating one factor at a time, successively.
#
  dpdx = 0.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      p = 1.0
      for j in range ( 0, npol ):

        if ( j == i ):
          p = p                      / ( xpol[ipol] - xpol[j] )
        elif ( j != ipol ):
          p = p * ( xval - xpol[j] ) / ( xpol[ipol] - xpol[j] )

      dpdx = dpdx + p

  return dpdx

def lagrange_basis_deriv_test ( ):

#*****************************************************************************80
#
## lagrange_basis_deriv_test() tests lagrange_basis_deriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lagrange_basis_deriv_test():' )
  print ( '  lagrange_basis_deriv() evaluates the derivative of a' )
  print ( '  Lagrange basis polynomial.' )

  npol = 7
  ipol = 2
  xpol = np.linspace ( -3.0, +3.0, npol )

  nplot = 101
  xplot = np.linspace ( -3.3, +3.5, nplot )
  yplot = np.zeros ( nplot )
  for i in range ( 0, nplot ):
    yplot[i] = lagrange_basis_deriv ( npol, ipol, xpol, xplot[i] )

  plt.clf ( )
  plt.plot ( xplot, yplot, 'b-', linewidth = 2 )
  plt.plot ( [ -3.3, +3.5 ], [ 0.0, 0.0 ], 'k--' )
  for i in range ( 0, npol ):
    plt.plot ( xpol[i], 0.0, 'r.', markersize = 25 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- d/dx L(i)(X) -->' )
  plt.title ( 'd/dx L(i)(X) = i-th Lagrange basis polynomial derivative' )
  filename = 'lagrange_basis_deriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def lagrange_basis_deriv2 ( npol, ipol, xpol, xval ):

#*****************************************************************************80
#
## lagrange_basis_deriv2(): second derivative of the IPOL-th Lagrange basis polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the Lagrange
#    polynomials.  The entries in XPOL must be distinct.
#
#    real XVAL, the evaluation point.
#
#  Output:
#
#    real D2PDX2, the second derivative of the IPOL-th 
#    Lagrange polynomial at XVAL.
#

#
#  Make sure IPOL is legal.
#
  if ( ipol < 1 or npol < ipol ):
    print ( '' )
    print ( 'lagrange_basis_deriv2(): Fatal error!' )
    print ( '  1 <= IPOL <= NPOL is required.' )
    raise Exception ( 'lagrange_basis_deriv2(): Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'lagrange_basis_deriv2(): Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    raise Exception ( 'lagrange_basis_deriv2(): Fatal error!' )
#
#  Evaluate the second derivative, by summing up the result
#  of differentiating with respect to every pair of components,
#  omitting IPOL.
#
  d2pdx2 = 0.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      for j in range ( 0, npol ):

        if ( j != ipol and j != i ):

          p = 1.0
          for k in range ( 0, npol ):

            if ( k != ipol ):

              if ( k == i or k == j ):
                p = p                      / ( xpol[ipol] - xpol[k] )
              else:
                p = p * ( xval - xpol[k] ) / ( xpol[ipol] - xpol[k] )

      d2pdx2 = d2pdx2 + p

  return d2pdx2

def lagrange_basis_deriv2_test ( ):

#*****************************************************************************80
#
## lagrange_basis_deriv2_test() tests lagrange_basis_deriv2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lagrange_basis_deriv_test():' )
  print ( '  lagrange_basis_deriv() evaluates the derivative of a' )
  print ( '  Lagrange basis polynomial.' )

  npol = 7
  ipol = 2
  xpol = np.linspace ( -3.0, +3.0, npol )

  nplot = 101
  xplot = np.linspace ( -3.3, +3.5, nplot )
  yplot = np.zeros ( nplot )
  for i in range ( 0, nplot ):
    yplot[i] = lagrange_basis_deriv2 ( npol, ipol, xpol, xplot[i] )

  plt.clf ( )
  plt.plot ( xplot, yplot, 'b-', linewidth = 2 )
  plt.plot ( [ -3.3, +3.5 ], [ 0.0, 0.0 ], 'k--' )
  for i in range ( 0, npol ):
    plt.plot ( xpol[i], 0.0, 'r.', markersize = 25 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- d2/dx2 L(i)(X) -->' )
  plt.title ( 'd2/dx2 L(i)(X) = i-th Lagrange basis polynomial second derivative' )
  filename = 'lagrange_basis_deriv2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def lagrange_basis_value ( npol, ipol, xpol, xval ):

#*****************************************************************************80
#
## lagrange_basis_value() evaluates the IPOL-th Lagrange polynomial.
#
#  Discussion:
#
#    Given NPOL distinct abscissas, XPOL(1:NPOL), the IPOL-th Lagrange
#    polynomial L(IPOL)(X) is defined as the polynomial of degree
#    NPOL - 1 which is 1 at XPOL(IPOL) and 0 at the NPOL - 1 other
#    abscissas.
#
#    A formal representation is:
#
#      L(IPOL)(X) = Product ( 1 <= I <= NPOL, I /= IPOL )
#       ( X - X(I) ) / ( X(IPOL) - X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the Lagrange
#    polynomials.  The entries in XPOL must be distinct.
#
#    real XVAL, the point at which the IPOL-th 
#    Lagrange polynomial is to be evaluated.
#
#  Output:
#
#    real PVAL, the value of the IPOL-th Lagrange
#    polynomial at XVAL.
#
#    real DPDX, the derivative of the IPOL-th 
#    Lagrange polynomial at XVAL.
#

#
#  Make sure IPOL is legal.
#
  if ( ipol < 0 or npol <= ipol ):
    print ( '' )
    print ( 'lagrange_basis_value(): Fatal error!' )
    print ( '  0 <= IPOL < NPOL is required.' )
    raise Exception ( 'lagrange_basis_value(): Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'lagrange_basis_value(): Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    raise Exception ( 'lagrange_basis_value(): Fatal error!' )
#
#  Evaluate the polynomial.
#
  pval = 1.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      pval = pval * ( xval - xpol[i] ) / ( xpol[ipol] - xpol[i] )
#
#  Evaluate the derivative, which can be found by summing up the result
#  of differentiating one factor at a time, successively.
#
  dpdx = 0.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      p2 = 1.0
      for j in range ( 0, npol ):

        if ( j == i ):
          p2 = p2                      / ( xpol[ipol] - xpol[j] )
        elif ( j != ipol ):
          p2 = p2 * ( xval - xpol[j] ) / ( xpol[ipol] - xpol[j] )

      dpdx = dpdx + p2

  return pval, dpdx

def lagrange_basis_value_test ( ):

#*****************************************************************************80
#
## lagrange_basis_value_test() tests lagrange_basis_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lagrange_basis_value_test():' )
  print ( '  lagrange_basis_value() evaluates Lagrange basis polynomials.' )

  npol = 7
  ipol = 2
  xpol = np.linspace ( -3.0, +3.0, npol )

  nplot = 101
  xplot = np.linspace ( -3.3, +3.5, nplot )
  yplot = np.zeros ( nplot )
  for i in range ( 0, nplot ):
    yplot[i], _ = lagrange_basis_value ( npol, ipol, xpol, xplot[i] )

  plt.clf ( )
  plt.plot ( xplot, yplot, 'b-', linewidth = 2 )
  plt.plot ( [ -3.3, +3.5 ], [ 0.0, 0.0 ], 'k--' )
  for i in range ( 0, npol ):
    plt.plot ( xpol[i], 0.0, 'r.', markersize = 25 )
  plt.plot ( [ xpol[ipol], xpol[ipol] ], [ 0.0, 1.0 ], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- L(i)(X) -->' )
  plt.title ( 'L(i)(X) = i-th Lagrange basis polynomial' )
  filename = 'lagrange_basis_value.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def r8poly_ant_coef ( n, poly_cof ):

#*****************************************************************************80
#
## r8poly_ant_coef() integrates a polynomial in standard form.
#
#  Discussion:
#
#    The antiderivative of a polynomial P(X) is any polynomial Q(X)
#    with the property that d/dX Q(X) = P(X).
#
#    This routine chooses the antiderivative whose constant term is zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real POLY_COF(1:N+1), the polynomial coefficients.
#    POLY_COF(1) is the constant term, and POLY_COF(N+1) is the
#    coefficient of X^(N).
#
#  Output:
#
#    real POLY_COF2(1:N+2), the coefficients of
#    the antiderivative polynomial, in standard form.  The constant
#    term is set to zero.
#
  import numpy as np

  poly_cof2 = np.zeros ( n + 2 )
#
#  Set the constant term.
#
  poly_cof2[0] = 0.0
#
#  Integrate the polynomial.
#
  for i in range ( 1, n + 2 ):
    poly_cof2[i] = poly_cof[i-1] / float ( i )

  return poly_cof2

def r8poly_print ( a, title ):

#*****************************************************************************80
#
## r8poly_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  import numpy as np

  m = len ( a ) - 1

  print ( title )

  if ( np.all ( a == 0.0 ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) =', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False

      if ( 2 <= i ):
        print ( ' %c %g * x^%d' % ( plus_minus, mag, i ), end = '' )
      elif ( i == 1 ):
        print ( ' %c %g * x' % ( plus_minus, mag ), end = '' )
      elif ( i == 0 ):
        print ( ' %c %g' % ( plus_minus, mag ), end = '' )

  print ( '' )

  return

def r8poly_value ( m, c, x ):

#*****************************************************************************80
#
## r8poly_value() evaluates a polynomial using a naive method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the polynomial value.
#
  value = c[0]
  xi = 1.0
  for i in range ( 1, m + 1 ):
    xi = xi * x
    value = value + c[i] * xi

  return value

def r8vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## r8vec_is_distinct() is true if the entries in an R8VEC are distinct.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be checked.
#
#  Output:
#
#    bool VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

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
  lagrange_test ( )
  timestamp ( )


