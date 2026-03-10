#! /usr/bin/env python3
#
def collatz_polynomial_next ( p1 ):

#*****************************************************************************80
#
## collatz_polynomial_next() computes the next Collatz polynomial.
#
#  Discussion:
#
#    The Collatz polynomial sequence is defined for polynomials with
#    coeficients mod 2.
#
#    If P1(x) is divisible by x, then
#      P2(x) = P1(x) / x
#    Else
#      P2(x) = P1(x) * (x+1) + 1
#
#    A polynomial of degree N is defined by a vector of length N+1,
#    whose first entry is the constant term, and whose last entry
#    is the coefficient of X^N.
#
#    For this function, it is assumed that all coefficients are 
#    either 0 or 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Polynomial analog of the Collatz conjecture,
#    27 July 2021,
#    https://www.johndcook.com/blog/2021/07/27/polynomial-collatz/
#    
#  Input:
#
#    integer P1(), the current polynomial.
#
#  Output:
#
#    integer P2(), the next polynomial.
#
  import numpy as np

  if ( not i4vec_is_binary ( p1 ) ):
    print ( '' )
    print ( 'collatz_polyomial_next(): Fatal error!' )
    print ( '  Input polynomial has a least one coefficient that is not 0 or 1.' )
    raise Exception ( 'collatz_polyomial_next(): Fatal error!' )

  n = polynomial_degree ( p1 )

  if ( n == 0 ):
    p2 = p1.copy ( )
  elif ( p1[0] == 0 ):
    p2 = np.zeros ( n )
    p2[0:n] = p1[1:n+1]
  else:
    p2 = np.zeros ( n + 2 )
    p2[0:n+1] = p1[0:n+1]
    p2[1:n+2] = p2[1:n+2] + p1[0:n+1]
    p2[0] = p2[0] + 1
    p2 = ( p2 % 2 )

  return p2

def collatz_polynomial_next_test ( ):

#*****************************************************************************80
#
## collatz_polynomial_next_test() tests collatz_polynomial_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'collatz_polynomial_next_test():' )
  print ( '  collatz_polynomial_next() returns the next polynomial' )
  print ( '  in a Collatz sequence.' )

  p0 = np.array ( [ 1, 0, 1 ] )
  p1 = collatz_polynomial_next ( p0 )
  print ( '' )
  print ( '  p0(x) = ', end = '' )
  polynomial_print ( p0 )
  print ( '  p1(x) = ', end = '' )
  polynomial_print ( p1 )

  p0 = np.array ( [ 0, 0, 1, 0, 1, 1 ] )
  p1 = collatz_polynomial_next ( p0 )
  print ( '' )
  print ( '  p0(x) = ', end = '' )
  polynomial_print ( p0 )
  print ( '  p1(x) = ', end = '' )
  polynomial_print ( p1 )

  p0 = np.array ( [ 1 ] )
  p1 = collatz_polynomial_next ( p0 )
  print ( '' )
  print ( '  p0(x) = ', end = '' )
  polynomial_print ( p0 )
  print ( '  p1(x) = ', end = '' )
  polynomial_print ( p1 )

  return

def collatz_polynomial_sequence ( p ):

#*****************************************************************************80
#
## collatz_polynomial_sequence() prints a Collatz polynomial sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Polynomial analog of the Collatz conjecture,
#    27 July 2021,
#    https://www.johndcook.com/blog/2021/07/27/polynomial-collatz/
#    
#  Input:
#
#    integer P(), the initial polynomial.
#
  i = 0

  while ( True ) :   
    print ( '%d: ' % ( i ), end = '' )
    polynomial_print ( p )
    if ( len ( p ) == 1 ):
      break
    p = collatz_polynomial_next ( p )
    i = i + 1

  return

def collatz_polynomial_sequence_test ( ):

#*****************************************************************************80
#
## collatz_polynomial_sequence_test() tests collatz_polynomial_sequence().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'collatz_polynomial_sequence_test():' )
  print ( '  collatz_polynomial_sequence() returns the sequence of' )
  print ( '  Collatz polynomials generated from a given starting polynomial.' )

  print ( '' )
  p0 = np.array ( [ 1, 0, 1 ] )
  collatz_polynomial_sequence ( p0 )

  print ( '' )
  p0 = np.array ( [ 0, 0, 1, 0, 1, 1 ] )
  collatz_polynomial_sequence ( p0 )

  print ( '' )
  p0 = np.array ( [ 1 ] )
  collatz_polynomial_sequence ( p0 )

  return

def collatz_polynomial_test ( ):

#*****************************************************************************80
#
## collatz_polynomial_test() tests collatz_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'collatz_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test collatz_polynomial()' )

  collatz_polynomial_next_test ( )
  collatz_polynomial_sequence_test ( )
  i4vec_is_binary_test ( )
  polynomial_degree_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'collatz_polynomial_test():' )
  print ( '  Normal end of execution.' )

  return

def i4vec_is_binary ( x ):

#*****************************************************************************80
#
## i4vec_is_binary() is true if an I4VEC only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X(N): the vector to be checked.
#
#  Output:
#
#    logical i4vec_is_binary: True if X only contains 0 or 1 entries.
#
  import numpy as np

  value = np.all ( ( x == 1 ) | ( x == 0 ) )

  return value

def i4vec_is_binary_test ( ):

#*****************************************************************************80
#
## i4vec_is_binary_test() tests i4vec_is_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_binary_test():' )
  print ( '  i4vec_is_binary() is TRUE if an I4VEC only contains' )
  print ( '  0 or 1 entries.' )

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  print ( x )
  if ( i4vec_is_binary ( x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1, 0, 1 ] )
  print ( '' )
  print ( x )
  if ( i4vec_is_binary ( x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0, 2, 1 ] )
  print ( '' )
  print ( x )
  if ( i4vec_is_binary ( x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  return

def polynomial_degree ( c ):

#*****************************************************************************80
#
## polynomial_degree() returns the degree of a polynomial.
#
#  Discussion:
#
#    The degree of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#    The degree of a constant polynomial is 0.  The degree of the
#    zero polynomial is debatable, but this routine returns the
#    degree as 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C(), the coefficients of the polynomial.
#
#  Output:
#
#    integer DEGREE, the degree of the polynomial.
#
  n = len ( c ) - 1

  while ( 0 < n ):

    if ( c[n] != 0 ):
      return n

    n = n - 1

  return n

def polynomial_degree_test ( ):

#*****************************************************************************80
#
## polynomial_degree_test() tests polynomial_degree().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polynomial_degree_test():' )
  print ( '  polynomial_degree() returns the degree of an polynomial.' )

  c = np.array ( [ 0, 1, 0, 3, 4, 0, 6, 7, 0, 0, 0 ] )

  print ( '' )
  print ( '  polynomial coefficient vector c:' )
  print ( c )

  print ( '' )
  print ( '  p(x) = ', end = '' )
  polynomial_print ( c )
  degree = polynomial_degree ( c )
  print ( '' )
  print ( '  The polynomial degree =', degree )

  return

def polynomial_print ( c ):

#*****************************************************************************80
#
## polynomial_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = c(0) + c(1)*x + ... + c(n-1)*x^(n-1) + c(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C(1:N+1): the polynomial coefficients.
#
  import numpy as np

  if ( np.all ( c == 0 ) ):
    print ( '0' )
    return

  n = polynomial_degree ( c )

  for i in range ( n, -1, -1 ):

    if ( c[i] < 0.0 ):
      plus_minus = '-'
    elif ( i < n ):
      plus_minus = '+'
    else:
      plus_minus = ''

    mag = abs ( c[i] )
#
#  Don't print terms with a zero coefficient.
#
    if ( mag != 0 ):
#
#  Don't print a coefficient of 1.
#
      if ( mag == 1 ):

        if ( 2 <= i ):
          print ( '%sx^%d' % ( plus_minus, i ), end = '' )
        elif ( i == 1 ):
          print ( '%sx' % ( plus_minus ), end = '' )
        elif ( i == 0 ):
          print ( '%s%d' % ( plus_minus, mag ), end = '' )

      else:

        if ( 2 <= i ):
          print ( '%s%d*x^%d' % ( plus_minus, mag, i ), end = '' )
        elif ( i == 1 ):
          print ( '%s%d*x' % ( plus_minus, mag ), end = '' )
        elif ( i == 0 ):
          print ( '%s%d' % ( plus_minus, mag ), end = '' )

  print ( '' )

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
  collatz_polynomial_test ( )
  timestamp ( )

