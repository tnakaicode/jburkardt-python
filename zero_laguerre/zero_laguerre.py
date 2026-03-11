#! /usr/bin/env python3
#
def zero_laguerre ( x0, degree, abserr, kmax, f ):

#*****************************************************************************80
#
## zero_laguerre() implements the Laguerre rootfinding method for polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eldon Hansen, Merrell Patrick,
#    A Family of Root Finding Methods,
#    Numerische Mathematik,
#    Volume 27, 1977, pages 257 - 269.
#
#  Input:
#
#    real x0: initial estimate for a root.
#
#    integer degree: the polynomial degree, at least 2.
#
#    real ABSERR: an error tolerance.
#
#    integer KMAX: the maximum number of iterations allowed.
#
#    real F ( x, ider ): evaluates the function or its first two derivatives.
#
#  Output:
#
#    real X: the estimated solution, if IERROR=0.
#
#    integer IERROR: error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K: the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  x = x0
  ierror = 0
  k = 0

  beta = 1.0 / ( degree - 1 )

  k = 0
#
#  Iteration loop:
#
  while ( True ):

    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      break

    z = dfx * dfx - ( beta + 1.0 ) * fx * d2fx
    z = max ( z, 0.0 )

    bot = beta * dfx + np.sqrt ( z )

    if ( bot == 0.0 ):
      ierror = 3
      break
#
#  Set the increment.
#
    dx = - ( beta + 1.0 ) * fx / bot
#
#  Update the iterate and function values.
#
    x = x + dx

  return x, ierror, k

def zero_laguerre_test ( ):

#*****************************************************************************80
#
## zero_laguerre_test() tests zero_laguerre().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( "" )
  print ( "zero_laguerre_test():" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  Test zero_laguerre()." )

  test01 ( )
  test02 ( )
  test03 ( )
#
#  Terminate.
#
  print ( "" )
  print ( "zero_laguerre_test():" )
  print ( "  Normal end of execution." )

  return

def test01 ( ):

#*****************************************************************************80
#
## test01() runs the tests on a polynomial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#

#
#  Give a starting point.
#
  x0 = 1.0
#
#  The polynomial degree.
#
  degree = 3
#
#  Set the error tolerance.
#
  abserr = 0.00001
#
#  KMAX is the maximum number of iterations.
#
  kmax = 30

  print ( "" )
  print ( "test01():" )
  print ( "  p(x)=(x+3)*(x+3)*(x-2)" )

  x, ierror, k = zero_laguerre ( x0, degree, abserr, kmax, func01 )

  print ( "" )
  if ( ierror != 0 ):
    print ( "  Iteration failed with ierror = ", ierror )
  else:
    print ( "  Iteration steps taken: ", k )
    print ( "  Estimated root X = ", x )
    print ( "  F(X) = ", func01 ( x, 0 ) )

  return

def func01 ( x, ider ):

#*****************************************************************************80
#
## func01() computes the function value for the first test.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 December 1998
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the evaluation is to take place.
#
#    integer IDER, specifies what is to be evaluated:
#    0, evaluate the function.
#    1, evaluate the first derivative.
#    2, evaluate the second derivative.
#
#  Output:
#
#    real FUNC01, the value of the function or derivative.
#
  if ( ider == 0 ):
    value = ( x + 3.0 )**2 * ( x - 2.0 )
  elif ( ider == 1 ):
    value = ( x + 3.0 ) * ( 3.0 * x - 1.0 )
  elif ( ider == 2 ):
    value = 6.0 * x + 8.0

  return value

def test02 ( ):

#*****************************************************************************80
#
## test02() runs the tests on the Newton polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#

#
#  Give a starting point.
#
  x0 = 1.0
#
#  The polynomial degree.
#
  degree = 3
#
#  Set the error tolerance.
#
  abserr = 0.00001
#
#  KMAX is the maximum number of iterations.
#
  kmax = 30

  print ( "" )
  print ( "test02():" )
  print ( "  p(x) = x^3 - 2x - 5" )

  x, ierror, k = zero_laguerre ( x0, degree, abserr, kmax, func02 )

  print ( "" )
  if ( ierror != 0 ):
    print ( "  Iteration failed with ierror = ", ierror )
  else:
    print ( "  Iteration steps taken: ", k )
    print ( "  Estimated root X = ", x )
    print ( "  F(X) = ", func02 ( x, 0 ) )

  return

def func02 ( x, ider ):

#*****************************************************************************80
#
## func02() computes the function value for the Newton polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the evaluation is to take place.
#
#    integer IDER, specifies what is to be evaluated:
#    0, evaluate the function.
#    1, evaluate the first derivative.
#    2, evaluate the second derivative.
#
#  Output:
#
#    real FUNC02, the value of the function or derivative.
#
  if ( ider == 0 ):
    value = x**3 - 2.0 * x - 5.0
  elif ( ider == 1 ):
    value = 3.0 * x**2 - 2.0
  elif ( ider == 2 ):
    value = 6.0 * x 

  return value

def test03 ( ):

#*****************************************************************************80
#
## test03() runs the tests on the 123456 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#

#
#  Give a starting point.
#
  x0 = 1.0
#
#  The polynomial degree.
#
  degree = 5
#
#  Set the error tolerance.
#
  abserr = 0.00001
#
#  KMAX is the maximum number of iterations.
#
  kmax = 30

  print ( "" )
  print ( "test03():" )
  print ( "  p(x) = x^5 + 2x^4 + 3x^3 + 4x^2 + 5x + 6" )

  x, ierror, k = zero_laguerre ( x0, degree, abserr, kmax, func03 )

  print ( "" )
  if ( ierror != 0 ):
    print ( "  Iteration failed with ierror = ", ierror )
  else:
    print ( "  Iteration steps taken: ", k )
    print ( "  Estimated root X = ", x )
    print ( "  F(X) = ", func03 ( x, 0 ) )

  return

def func03 ( x, ider ):

#*****************************************************************************80
#
## func03() computes the function value for the 123456 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the evaluation is to take place.
#
#    integer IDER, specifies what is to be evaluated:
#    0, evaluate the function.
#    1, evaluate the first derivative.
#    2, evaluate the second derivative.
#
#  Output:
#
#    real FUNC02, the value of the function or derivative.
#
  if ( ider == 0 ):
    value = x**5 + 2 * x**4 + 3 * x**3 + 4 * x**2 + 5 * x + 6
  elif ( ider == 1 ):
    value = 5 * x**4 + 8 * x**3 + 9 * x**2 + 8 * x + 5
  elif ( ider == 2 ):
    value = 20 * x**3 + 24 * x**2 + 18 * x + 8

  return value

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
  zero_laguerre_test ( )
  timestamp ( )

