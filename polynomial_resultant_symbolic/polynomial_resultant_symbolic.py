#! /usr/bin/env python3
#
def polynomial_resultant_symbolic_test ( ):

#*****************************************************************************80
#
## polynomial_resultant_symbolic_test() tests polynomial_resultant_symbolic().
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
  print ( 'polynomial_resultant_symbolic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomial_resultant_symbolic().' )

  coefficients_test ( )
  sylvester_matrix_test ( )
  resultant_user_test ( )
  resultant_sympy_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomial_resultant_symbolic_test():' )
  print ( '  Normal end of execution.' )

  return

def coefficients ( P ):

#*****************************************************************************80
#
## coefficients() returns coefficient vector of a polynomial.
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
#    Original Python version by andreuinyu.
#    This version by John Burkardt.
#
#  Input:
#
#    Poly P: the polynomial.
#
#  Output:
#
#    tuple C[]: the coefficient vector.
#
  D = []
  for i in range ( P.degree(), -1, -1 ):
    D.append ( P.nth(i) )
  C = tuple ( D )

  return C

def coefficients_test ( ):

#*****************************************************************************80
#
## coefficients_test() tests coefficients().
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
#    Original Python version by andreuinyu
#    This version by John Burkardt.
#
  from sympy import symbols
  from sympy import Poly
  x = symbols ( 'x' )

  print ( '' )
  print ( 'coefficients_test ( ):' )
  print ( '  Return vector of polynomial coefficients.' )

  P = Poly ( 6*x**5 - 3*x**4 + 2*x**2 - x + 9, x )

  print ( '' )
  print ( '  Polynomial P:' )
  print ( '    ', end = '' )
  print ( P )

  C = coefficients ( P )
  print ( '' )
  print ( '  Coefficient vector C:' )
  print ( '    ', end = '' )
  print ( C )

  return

def resultant_user ( P, Q ):

#*****************************************************************************80
#
## resultant_user() computes the resultant of two polynomials.
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
#    Original Python version by andreuinyu
#    This version by John Burkardt.
#
#  Input:
#
#    Poly P, Q: two polynomials.
#
#  Output:
#
#    real r: the resultant.
#
  S = sylvester_matrix ( P, Q )
  r = S.det()

  return r

def resultant_user_test ( ):

#*****************************************************************************80
#
## resultant_user_test() tests resultant_user().
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
#    Original Python version by andreuinyu
#    This version by John Burkardt.
#
  from sympy import Poly
  from sympy import symbols
  x = symbols ( 'x' )

  print ( '' )
  print ( 'resultant_user_test():' )
  print ( '  Test resultant_user(),' )
  print ( '  user-written code which' )
  print ( '  which computes the resultant R of polynomials P and Q' )

  P = Poly ( 2*x**4+3*x**3+4*x**2+5*x+6, x )
  print ( '' )
  print ( '  Polynomial P:' )
  print ( '    ', end = '' )
  print ( P )

  Q = Poly ( 7*x**3+8*x**2+9*x+10, x )
  print ( '' )
  print ( '  Polynomial Q:' )
  print ( '    ', end = '' )
  print ( Q )

  r = resultant_user ( P, Q )
  print ( '' )
  print ( '  Resultant r = ', r )

  return 

def resultant_sympy_test ( ):

#*****************************************************************************80
#
## resultant_sympy_test() tests the sympy resultant() function.
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
#    John Burkardt.
#
  from sympy import Poly
  from sympy import symbols
  from sympy import resultant

  x = symbols ( 'x' )

  print ( '' )
  print ( 'resultant_sympy_test():' )
  print ( '  Test the resultant() function,' )
  print ( '  a utility that is part of the sympy package,' )
  print ( '  which computes the resultant R of polynomials P and Q' )

  P = Poly ( 2*x**4+3*x**3+4*x**2+5*x+6, x )
  print ( '' )
  print ( '  Polynomial P:' )
  print ( '    ', end = '' )
  print ( P )

  Q = Poly ( 7*x**3+8*x**2+9*x+10, x )
  print ( '' )
  print ( '  Polynomial Q:' )
  print ( '    ', end = '' )
  print ( Q )

  r = resultant ( P, Q )
  print ( '' )
  print ( '  Resultant r = ', r )

  return 

def sylvester_matrix ( P, Q ):

#*****************************************************************************80
#
## sylvester_matrix() tests sylvester_matrix().
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
#    Original Python version by andreuinyu.
#    This version by John Burkardt.
#
#  Input:
#
#    Poly P, Q: two polynomials.
#
#  Output:
#
#    Matrix S: the Sylvester matrix of P and Q.
#
  from sympy import Matrix

  rows = []
  m = P.degree()
  n = Q.degree()
  size = m + n
  CP = coefficients ( P )
  CQ = coefficients ( Q )

  for i in range ( size ):

    tail = []
    row = []

    if i in range ( 0, n ):
      row = list ( CP )
      row.extend ( ( n - 1 - i ) * [0] )
      row[:0] = [0] * i
      rows.append ( row )

    if i in range ( n, size ):
      row = list ( CQ )
      row.extend ( ( size-1-i) * [0] )
      row[:0] = [0] * ( size - len ( row ) )
      rows.append ( row )

  S = Matrix ( rows )

  return S

def sylvester_matrix_test ( ):

#*****************************************************************************80
#
## sylvester_matrix_test() tests sylvester_matrix().
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
#    Original Python version by andreuinyu
#    This version by John Burkardt.
#
  from sympy import Poly
  from sympy import pprint
  from sympy import symbols
  x = symbols ( 'x' )

  print ( '' )
  print ( 'sylvester_matrix_test ( ):' )
  print ( '  Test sylvester_matrix(),' )
  print ( '  which computes S, the sylvester matrix of polynomials P and Q.' )

  P = Poly ( 2*x**4+3*x**3+4*x**2+5*x+6, x )
  print ( '' )
  print ( '  Polynomial P:' )
  print ( '    ', end = '' )
  print ( P )

  Q = Poly ( 7*x**3+8*x**2+9*x+10, x )
  print ( '' )
  print ( '  Polynomial Q:' )
  print ( '    ', end = '' )
  print ( Q )

  S = sylvester_matrix ( P, Q )
  print ( '' )
  print ( '  Matrix S:' )
  pprint ( S )

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
  polynomial_resultant_symbolic_test ( )
  timestamp ( )

