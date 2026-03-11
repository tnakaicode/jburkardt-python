#! /usr/bin/env python3
#
def polynomial_resultant_roots ( p1, p2 ):

#*****************************************************************************80
#
## polynomial_resultant_roots() computes the resultant of polynomials p1 and p2.
#
#  Discussion:
#
#    This algorithm computes the resultant using knowledge of the roots
#    of the polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Pohst, Hans Zassenhaus,
#    Algorithmic Algebraic Number Theory,
#    Cambridge University Press, 1989
#    LC: QA247.P58
#    ISBN: 0-521-33060-2
#
#  Input:
#
#    real p1(np1), p2(np2): two polynomials.
#    On input, the first entry is the constant coefficient.
#
#  Output:
#
#    real r: the resultant.
#
  import numpy as np
  from numpy.polynomial.polynomial import polyroots
#
#  Get roots of polynomials.
#
  r1 = polyroots ( p1 )
  r2 = polyroots ( p2 )
#
#  The roots() function doesn't return multiple copies of a multiple root.
#
# r1 = np.roots ( p1 )
# r2 = np.roots ( p2 )
#
#  Determine number of roots.
#
  n1 = len ( r1 )
  n2 = len ( r2 )
#
#  Retrieve highest order coefficients.
#
  a1 = p1[-1]
  a2 = p2[-1]

#
#  Compute resultant.
#
  r = 1.0
  for i in range ( 0, n1 ):
    for j in range ( 0, n2 ):
      r = r * ( r1[i] - r2[j] )

  r = r * a1**n2 * a2**n1

  return r

def polynomial_resultant_roots_test ( ):

#*****************************************************************************80
#
## polynomial_resultant_roots_test() tests polynomial_resultant_roots().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polynomial_resultant_roots_test():' )
  print ( '  polynomial_resultant_roots() computes ' )
  print ( '  the resultant R of polynomials P and Q' )
  print ( '  based on knowledge of the roots of P and Q.' )

  n_data = 0

  while ( True ):

    n_data, p, q, r1 = polynomial_resultant_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    r8poly_print ( p, 'P(x):' )
    r8poly_print ( q, 'Q(x):' )
    print ( '   R (tabulated):   ', r1 )

    r2 = polynomial_resultant_roots ( p, q )

    print ( '   R (calculated):  ', np.round ( r2 ) )

  return

def polynomial_resultant_sylvester ( p1, p2 ):

#*****************************************************************************80
#
## polynomial_resultant_sylvester() computes the resultant of polynomials p1 and p2.
#
#  Discussion:
#
#    This algorithm computes the resultant by constructing the Sylvester
#    matrix and taking the determinant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Pohst, Hans Zassenhaus,
#    Algorithmic Algebraic Number Theory,
#    Cambridge University Press, 1989
#    LC: QA247.P58
#    ISBN: 0-521-33060-2
#
#  Input:
#
#    real p1(np1), p2(np2): two polynomials.
#    On input, the first entry is the highest order coefficient.
#
#  Output:
#
#    real r: the resultant.
#
  from scipy.linalg import det

  A = sylvester_matrix ( p1, p2 )

  if ( len ( A ) == 0 ):
    r = 1.0
  else:
    r = det ( A )

  return r

def polynomial_resultant_sylvester_test ( ):

#*****************************************************************************80
#
## polynomial_resultant_sylvester_test() tests polynomial_resultant_sylvester().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'polynomial_resultant_sylvester_test():' )
  print ( '  polynomial_resultant_sylvester() computes ' )
  print ( '  the resultant R of polynomials P and Q' )
  print ( '  based on the determinant of the Sylvester matrix.' )

  n_data = 0

  while ( True ):

    n_data, p, q, r1 = polynomial_resultant_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    r8poly_print ( p, 'P(x):' )
    r8poly_print ( q, 'Q(x):' )
    print ( '   R (tabulated):   ', r1 )

    r2 = polynomial_resultant_sylvester ( p, q )

    print ( '   R (calculated):  ', r2 )

  return

def polynomial_resultant_test ( ):

#*****************************************************************************80
#
## polynomial_resultant_test() tests polynomial_resultant().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'polynomial_resultant_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomial_resultant().' )

  polynomial_resultant_roots_test ( )
  polynomial_resultant_sylvester_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomial_resultant_test()' )
  print ( '  Normal end of execution.' )

  return

def polynomial_resultant_values ( n_data ):

#*****************************************************************************80
#
## polynomial_resultant_values() returns polynomial resultants.
#
#  Discussion:
#
#    Each call to this routine returns two polynomials P and Q,
#    defined by their coefficient vectors, with the constant
#    coefficient first, such that
#
#      resultant ( p, q ) = r
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n_data: the user sets N_DATA to 0 before the first call.  
#    Thereafter, it should simply be the value returned by the previous call.
#
#  Output:
#
#    integer n_data: the routine increments the input value of N_DATA by 1. 
#    But when there is no more data, the output value of N_DATA will be 0.
#
#    real p(np): the first polynomial.
#
#    real q(nq): the second polynomial.
#
#    real r: the resultant.
#
  import numpy as np

  n_max = 7

  if ( n_data < 0 ):
    n_data = 0

  n_data = n_data + 1

  if ( n_max < n_data ):

    n_data = 0
    p = np.array ( [] )
    q = np.array ( [] )
    r = 0.0

  elif ( n_data == 1 ):

    p = np.array ( [ 1 ] )
    q = np.array ( [ 2 ] )
    r = 1

  elif ( n_data == 2 ):

    p = np.array ( [ 3, 3 ] )
    q = np.array ( [ 1, 2, 1 ] )
    r = 0

  elif ( n_data == 3 ):

    p = np.array ( [ 1, 3, 3, 1 ] )
    q = np.array ( [ -1, 0, 1 ] )
    r = 0

  elif ( n_data == 4 ):

    p = np.array ( [ 4, 3, 2, 1 ] )
    q = np.array ( [ 7, 6, 5 ] )
    r = 832

  elif ( n_data == 5 ):

    p = np.array ( [ 4, 3, 2, 1 ] )
    q = np.array ( [ 1, 2, 3, 4 ] )
    r = -2000

  elif ( n_data == 6 ):

    p = np.array ( [ 0, -2, 5, -4, 1 ] )
    q = np.array ( [ 1, -2, 5, -4, 1 ] )
    r = 1

  elif ( n_data == 7 ):

    p = np.array ( [ 0, -2, 5, -4, 1 ] )
    q = np.array ( [ 0, 64, -192, 240, -160, 60, -12, 1 ] )
    r = 0

  return n_data, p, q, r

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

def sylvester_matrix ( p1, p2 ):

#*****************************************************************************80
#
## sylvester_matrix() returns the SYLVESTER matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jacqueline Burm, Paul Fishback,
#    Period-3 Orbits Via Sylvester's Theorem and Resultants,
#    Mathematics Magazine,
#    Volume 74, Number 1, February 2001, pages 47-51.
#
#  Input:
#
#    real p1(n1), p2(n2): two polynomials.
#    On input, the constant coefficient is listed first.
#
#  Output:
#
#    real A(n1+n2,n1_n2): the Sylvester matrix.
#
  import numpy as np

  n1 = len ( p1 ) - 1
  n2 = len ( p2 ) - 1
#
#  Reverse coefficient order.
#
  p1 = np.flip ( p1 )
  p2 = np.flip ( p2 )

  A = np.zeros ( [ n1+n2, n1+n2 ] )

  for i in range ( 0, n2 ):
    A[i,i:n1+1+i] = p1[0:n1+1]

  for i in range ( 0, n1 ):
    A[i+n2,i:n2+1+i] = p2[0:n2+1]

  return A

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
  polynomial_resultant_test ( )
  timestamp ( )

