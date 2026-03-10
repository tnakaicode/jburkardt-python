#! /usr/bin/env python3
#
def hermite_exactness_test ( ):

#*****************************************************************************80
#
## hermite_exactness_test() tests hermite_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hermite_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hermite_exactness().' )

  hermite_exactness ( 'hermite_probabilist_010', 18, 4 )
#
#  Terminate.
#
  print ( '' )
  print ( 'hermite_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def hermite_exactness ( quad_filename, degree_max, option ):

#*****************************************************************************80
#
## hermite_exactness() tests a Hermite quadrature rule for exactness.
#
#  Discussion:
#
#    This program investigates a standard Gauss-Hermite quadrature rule
#    by using it to integrate monomials over (-oo,+oo), and comparing the
#    approximate result to the known exact value.
#
#    The user specifies:
#    * the "root" name of the R, W and X files that specify the rule
#    * DEGREE_MAX, the maximum monomial degree to be checked.
#    * the OPTION (unweighted/physicist weight/probabilist weight)
#
#    OPTION indicates the weight function and normalization:
#    0, Integral ( -oo < x < +oo ) x ** n exp(-x*x)               dx.
#    1, Integral ( -oo < x < +oo ) x ** n exp(-x*x)               dx.
#    2, Integral ( -oo < x < +oo ) x ** n exp(-x*x/2)             dx.
#    3, Integral ( -oo < x < +oo ) x ** n exp(-x*x)   / sqrt (pi) dx.
#    4, Integral ( -oo < x < +oo ) x ** n exp(-x*x/2) / sqrt(2pi) dx.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character QUAD_FILENAME, the "root" name of the R, W and X files 
#    that specify the rule
#
#    integer DEGREE_MAX, the maximum monomial degree to be checked.
#
#    integer OPTION, indicates the weight function and normalization:
#
  import numpy as np

  print ( '' )
  print ( 'hermite_exactness():' )
  print ( '  Investigate the polynomial exactness of a Gauss-Hermite' )
  print ( '  quadrature rule by integrating exponentially weighted' )
  print ( '  monomials up to a given degree over the (-oo,+oo) interval.' )
#
#  Create the names of:
#    the quadrature X file
#    the quadrature W file
#    the quadrature R file
#
  quad_x_filename = quad_filename + '_x.txt'
  quad_w_filename = quad_filename + '_w.txt'
  quad_r_filename = quad_filename + '_r.txt'
#
#  Summarize the input.
#
  print ( '' )
  print ( 'User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".' )
  print ( '  Quadrature rule R file = "' + quad_r_filename + '".' )
  print ( '  Maximum degree to check = ', degree_max )
#
#  Read the X file.
#
  x = np.loadtxt ( quad_x_filename )
  order = x.shape[0]
#
#  Read the W file.
#
  w = np.loadtxt ( quad_w_filename )
#
#  Read the R file.
#
  r = np.loadtxt ( quad_r_filename )
#
#  Print the input quadrature rule.
#
  print ( '' )
  print ( '  Test a Gauss-Hermite quadrature rule of' )
  print ( '  ORDER = ', order )
  print ( '' )
  if ( option == 0 ):
    print ( '  OPTION = 0, the unweighted rule for:' )
    print ( '  Integral ( -oo < x < +oo ) f(x) dx' )
  elif ( option == 1 ):
    print ( '  OPTION = 1, the physicist weighted rule for:' )
    print ( '  Integral ( -oo < x < +oo ) f(x) * exp(-x*x) dx' )
  elif ( option == 2 ):
    print ( '  OPTION = 2, the probabilist weighted rule for:' )
    print ( '  Integral ( -oo < x < +oo ) f(x) * exp(-x*x/2) dx' )
  elif ( option == 3 ):
    print ( '  OPTION = 3, the physicist normalized weighted rule for:' )
    print ( '  Integral ( -oo < x < +oo ) f(x) * exp(-x*x) / sqrt(pi) dx' )
  elif ( option == 4 ):
    print ( '  OPTION = 4, the probabilist normalized weighted rule for:' )
    print ( '  Integral ( -oo < x < +oo ) f(x) * exp(-x*x/2) / sqrt(2 pi) dx' )

  print ( '' )
  print ( '  Weights W:' )
  print ( '' )
  print ( w )
  print ( '' )
  print ( '  Abscissas X:' )
  print ( '' )
  print ( x )
  print ( '' )
  print ( '  Region R:' )
  print ( '' )
  print ( r )
#
#  Explore the monomials.
#
  print ( '' )
  print ( '  A Gauss-Hermite rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '  Degree      Error' )
  print ( '' )

  for degree in range ( 0, degree_max + 1 ):

    quad_error = hermite_monomial_quadrature ( degree, order, option, w, x )

    print ( '  %2d  %24.16f' % ( degree, quad_error ) )

  return

def hermite_integral ( n, option ):

#*****************************************************************************80
#
## hermite_integral() evaluates a monomial Hermite integral.
#
#  Discussion:
#
#    H(n,1) = Integral ( -oo < x < +oo ) x ** n exp(-x ** 2) dx
#    H(n,1) is 0 for n odd.
#    H(n,1) = (n-1)!! * sqrt(pi) / 2 ** (n/2) for n even.
#
#    H(n,2) = Integral ( -oo < x < +oo ) x ** n exp(-x ** 2/2) dx
#    H(n,2) is 0 for n odd.
#    H(n,2) = (n-1)!! * sqrt(2*pi) for n even.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2023
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
#    integer OPTION, the integral has the form:
#    0, Integral ( -oo < x < +oo ) x ** n exp(-x*x)               dx.
#    1, Integral ( -oo < x < +oo ) x ** n exp(-x*x)               dx.
#    2, Integral ( -oo < x < +oo ) x ** n exp(-x*x/2)             dx.
#    3, Integral ( -oo < x < +oo ) x ** n exp(-x*x)   / sqrt (pi) dx.
#    4, Integral ( -oo < x < +oo ) x ** n exp(-x*x/2) / sqrt(2pi) dx.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial2
  import numpy as np

  if ( n < 0 ):

    exact = - np.inf

  elif ( ( n % 2 ) == 1 ):

    exact = 0.0

  elif ( option == 0 ):

    exact = factorial2 ( n - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( n / 2 )

  elif ( option == 1 ):

    exact = factorial2 ( n - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( n / 2 )

  elif ( option == 2 ):

    exact = factorial2 ( n - 1 ) * np.sqrt ( 2.0 * np.pi )

  elif ( option == 3 ):

    exact = factorial2 ( n - 1 ) / 2.0 ** ( n / 2 )

  elif ( option == 4 ):

    exact = factorial2 ( n - 1 )

  return exact

def hermite_monomial_quadrature ( expon, order, option, w, x ):

#*****************************************************************************80
#
## hermite_monomial_quadrature() applies a quadrature rule to a monomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    intege ORDER, the number of points in the rule.
#
#    integer OPTION, the integral has the form:
#    0, Integral ( -oo < x < +oo ) x ** n exp(-x*x)               dx.
#    1, Integral ( -oo < x < +oo ) x ** n exp(-x*x)               dx.
#    2, Integral ( -oo < x < +oo ) x ** n exp(-x*x/2)             dx.
#    3, Integral ( -oo < x < +oo ) x ** n exp(-x*x)   / sqrt (pi) dx.
#    4, Integral ( -oo < x < +oo ) x ** n exp(-x*x/2) / sqrt(2pi) dx.
#
#    real W(ORDER), the quadrature weights.
#
#    real X(ORDER), the quadrature points.
#
#  Output:
#
#    real QUAD_ERROR, the quadrature error.
#
  import numpy as np
#
#  Get the exact value of the integral of the unscaled monomial.
#
  exact = hermite_integral ( expon, option )
#
#  Evaluate the unweighted monomial at the quadrature points.
#
  if ( option == 0 ):
    value = np.exp ( - x ** 2 ) * x ** expon
  elif ( option == 1 ):
    value = x ** expon
  elif ( option == 2 ):
    value = x ** expon
  elif ( option == 3 ):
    value = x ** expon
  elif ( option == 4 ):
    value = x ** expon
#
#  Compute the weighted sum.
#
  quad = np.dot ( w, value )
#
#  Absolute error for cases where exact integral is zero,
#  Relative error otherwise.
#
  if ( exact == 0.0 ):
    quad_error = np.abs ( quad )
  else:
    quad_error = np.abs ( quad - exact ) / np.abs ( exact )

  return quad_error

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
  hermite_exactness_test ( )
  timestamp ( )


