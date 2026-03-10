#! /usr/bin/env python3
#
def gram_abscissas ( m ):

#*****************************************************************************80
#
## gram_abscissas() returns the coordinates of the Gram polynomial abscissas.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Germund Dahlquist, Ake Bjorck,
#    Numerical Methods in Scientific Computing,
#    Volume 1,
#    SIAM, 2008,
#    ISBN: 978-0-898716-44-3,
#    LC: QA297.D335 2008.
#    
#  Input:
#
#    integer m, the number of points used in defining the polynomials.
#
#  Output:
#
#    real x(m), the point coordinates.
#
  import numpy as np

  x = np.linspace ( -1.0, +1.0, m + 1 )
  x = x[0:m]
  x = x + 1.0 / m

  return x

def gram_abscissas_test ( ):

#*****************************************************************************80
#
## gram_abscissas_test() tests gram_abscissas().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gram_abscissas_test():' )
  print ( '  Test gram_abscissas()' )

  for m in [ 3, 4, 5, 10 ]:
    x = gram_abscissas ( m )
    print ( '' )
    print ( '  x = gram_abscissas(', m, ')' )
    print ( x )

  return

def gram_beta ( n, m ):

#*****************************************************************************80
#
## gram_beta() evaluates a factor used in evaluating Gram polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Germund Dahlquist, Ake Bjorck,
#    Numerical Methods in Scientific Computing,
#    Volume 1,
#    SIAM, 2008,
#    ISBN: 978-0-898716-44-3,
#    LC: QA297.D335 2008.
#    
#  Input:
#
#    integer n, the index of the polynomial.
#    n < m.
#
#    integer m, the number of points used in defining the polynomials.
#
#  Output:
#
#    real value, the value of the factor.
#

  if ( n < 0 ):
    value = 0.0
  elif ( m <= 0 ):
    value = 0.0
  elif ( m <= n ):
    value = 0.0
  else:
    value = ( m + n ) * ( m - n ) * n**2 / m**2 / ( 4.0 * n**2 - 1.0 )

  return value

def gram_beta_test ( ):

#*****************************************************************************80
#
## gram_beta_test() tests gram_beta().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gram_beta_test():' )
  print ( '  Test gram_beta()' )
#
#  Check beta.
#
  print ( '' )
  print ( '       M = ' )
  for m in range ( 0, 6 ):
    print ( '         %d' % ( m ), end = '' )
  print ( '' )

  for n in range ( 0, 6 ):
    print ( '  N = %2d:  ' % ( n ), end = '' )
    for m in range ( 0, 6 ):
      if ( n < m ):
        print ( '  %8.4f' % ( gram_beta(n,m) ), end = '' )
      else:
        print ( '  --------', end = '' )
    print ( '' )

  return

def gram_polynomial_coefficients ( n, m ):

#*****************************************************************************80
#
## gram_polynomial_coefficients() returns Gram polynomial coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Germund Dahlquist, Ake Bjorck,
#    Numerical Methods in Scientific Computing,
#    Volume 1,
#    SIAM, 2008,
#    ISBN: 978-0-898716-44-3,
#    LC: QA297.D335 2008.
#    
#  Input:
#
#    integer n, the index of the polynomial.
#    n < m.
#
#    integer m, the number of points used in defining the polynomial.
#
#  Output:
#
#    real c(n+1), the coefficients of the polynomial. starting with constant.
#
  import numpy as np

  a = np.zeros ( n + 1 )
  b = np.zeros ( n + 1 )
  c = np.zeros ( n + 1 )

  for step in range ( 0, n + 1 ):
    if ( step == 0 ):
      c[0] = 1.0
    else:
      a = b.copy()
      b = c.copy()
      c[0:step] = - gram_beta ( step - 1, m ) * a[0:step]
      c[1:step+1] = c[1:step+1] + b[0:step]

  return c

def gram_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## gram_polynomial_coefficients_test() tests gram_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gram_polynomial_coefficients_test():' )
  print ( '  Test polynomial_coefficients_beta()' )

  m = 10
  for n in range ( 0, 6 ):
    c = gram_polynomial_coefficients ( n, m )
    label = ( 'Gram polynomial g(%d,%d)' % ( n, m ) )
    r8poly_print ( c, label )

  return

def gram_polynomial_evaluate ( n, m, x ):

#*****************************************************************************80
#
## gram_polynomial_evaluate() evaluates a Gram polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Germund Dahlquist, Ake Bjorck,
#    Numerical Methods in Scientific Computing,
#    Volume 1,
#    SIAM, 2008,
#    ISBN: 978-0-898716-44-3,
#    LC: QA297.D335 2008.
#    
#  Input:
#
#    integer n, the index of the polynomial.
#    n < m.
#
#    integer m, the number of points used in defining the polynomials.
#
#    real x(*), the evaluation points.
#
#  Output:
#
#    real g(*), the value of the polynomial at the points.
#
  import numpy as np

  k = len ( x )
  pnp1 = np.zeros ( k )

  for step in range ( 0, n + 1 ):
    if ( step == 0 ):
      pn = np.zeros ( k )
      pnp1 = np.ones ( k )
    else:
      pnm1 = pn
      pn   = pnp1
      pnp1 = x * pn - gram_beta ( step - 1, m ) * pnm1

  g = pnp1

  return g

def gram_polynomial_inner_product ( i, j, m ):

#*****************************************************************************80
#
## gram_polynomial_inner_product(): inner product of two Gram polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Germund Dahlquist, Ake Bjorck,
#    Numerical Methods in Scientific Computing,
#    Volume 1,
#    SIAM, 2008,
#    ISBN: 978-0-898716-44-3,
#    LC: QA297.D335 2008.
#    
#  Input:
#
#    integer i, j, the index of the polynomials.
#    i, j < m.
#
#    integer m, the number of points used in defining the polynomials.
#
#  Output:
#
#    real value, the value of the inner product.
#
  import numpy as np

  x = gram_abscissas ( m )
  gi = gram_polynomial_evaluate ( i, m, x )
  gj = gram_polynomial_evaluate ( j, m, x )
  value = np.dot ( gi, gj ) / m

  return value

def gram_polynomial_test ( ):

#*****************************************************************************80
#
## gram_polynomial_test() tests gram_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'gram_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gram_polynomial()' )

  gram_abscissas_test ( )
  gram_beta_test ( )
  gram_polynomial_coefficients_test ( )

  m = 10
  x = np.linspace ( -1.0, 1.0, 101 )
  for n in range ( 0, 6 ):
    g = gram_polynomial_evaluate ( n, m, x )
    plt.clf ( )
    plt.plot ( x, g, linewidth = 3 )
    label = ( 'Gram polynomial p_(%d,%d)(x)' % ( n, m ) )
    plt.title ( label )
    plt.grid ( True )
    filename = 'gram_' + str ( n ) + '_' + str ( m ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Check orthogonality.
#
  A = np.zeros ( [ 6, 6 ] )
  m = 25
  for n1 in range ( 0, 6 ):
    for n2 in range ( 0, 6 ):
      A[n1,n2] = gram_polynomial_inner_product ( n1, n2, m )
  print ( '' )
  print ( '  Orthogonality matrix:' )
  print ( A )
#
#  Orthogonal projection of f(x):
#
  f = lambda x: np.exp ( x )
  m = 50
  n_max = 10
  c = np.zeros ( n_max + 1 )
  for j in range ( 0, n_max + 1 ):
    c[j] = gram_projection ( f, j, m )
 
  print ( '' )
  print ( '  Orthogonal projection of f=exp(x)' )
  print ( c )

  r8poly_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gram_polynomial_test():' )
  print ( '  Normal end of execution.' )

  return

def gram_projection ( f, j, m ):

#*****************************************************************************80
#
## gram_projection(): projection of function onto Gram polynomial gj.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Germund Dahlquist, Ake Bjorck,
#    Numerical Methods in Scientific Computing,
#    Volume 1,
#    SIAM, 2008,
#    ISBN: 978-0-898716-44-3,
#    LC: QA297.D335 2008.
#    
#  Input:
#
#    integer f, a handle for the function.
#
#    integer j, the index of the Gram polynomial.
#    j < m.
#
#    integer m, the number of points used in defining the polynomials.
#
#  Output:
#
#    real value, the value of the inner product (f,gj).
#
  import numpy as np

  x = gram_abscissas ( m )
  fi = f ( x )
  gj = gram_polynomial_evaluate ( j, m, x )
  value = np.dot ( fi, gj ) / np.dot ( gj, gj )

  return value

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
#    09 August 2018
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
  m = len ( a ) - 1

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( all ( a == 0.0 ) ):
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
        print ( '  p(x) = ', end = '' ),
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False
      else:
        print ( '         ', end = '' ),

      if ( 2 <= i ):
        print ( '  %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '  %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '  %c %g' % ( plus_minus, mag ) )

  return

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_print_test():' )
  print ( '  r8poly_print() prints an R8POLY.' )

  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( c, '  The R8POLY:' )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  gram_polynomial_test ( )
  timestamp ( )

