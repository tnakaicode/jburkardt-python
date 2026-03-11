#! /usr/bin/env python3
#
def legendre_exactness_test ( ):

#*****************************************************************************80
#
## legendre_exactness_test() tests legendre_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'legendre_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test legendre_exactness().' )

  legendre_exactness ( 'leg_o004', 10 )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def legendre_exactness ( quad_filename, degree_max ):

#*****************************************************************************80
#
## legendre_exactness() checks a Legendre quadrature rule for exactness.
#
#  Discussion:
#
#    This program investigates a standard Gauss-Legendre quadrature rule
#    by using it to integrate monomials over [-1,+1], and comparing the
#    approximate result to the known exact value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
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
  import numpy as np

  print ( '' )
  print ( 'legendre_exactness():' )
  print ( '  Investigate the polynomial exactness of a Gauss-Legendre' )
  print ( '  quadrature rule by integrating all monomials up to a given' )
  print ( '  degree over the [-1,+1] interval.' )
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
  print ( '  The quadrature rule to be tested is' )
  print ( '  a Gauss-Legendre rule' )
  print ( '  ORDER = ', order )
  print ( '' )
  print ( '  Standard rule:' )
  print ( '    Integral ( -1 <= x <= +1 ) f(x) dx' )
  print ( '    is to be approximated by' )
  print ( '    sum ( 1 <= I <= ORDER ) w(i) * f(x(i)).' )
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
  print ( '  A Gauss-Legendre rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '  Degree          Error' )
  print ( '' )

  for degree in range ( 0, degree_max + 1 ):

    quad_error = legendre_monomial_quadrature ( degree, order, w, x )

    print ( '  %2d  %24.16f' % ( degree, quad_error ) )

  return

def legendre_monomial_integral ( expon ):

#*****************************************************************************80
#
## legendre_monomial_integral() evaluates a monomial Legendre integral.
#
#  Discussion:
#
#    To test a Legendre quadrature rule, we use it to approximate the
#    integral of a monomial:
#
#      integral ( -1 <= x <= +1 ) x^n dx
#
#    This routine is given the value of the exponent, and returns the
#    exact value of the integral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#  Output:
#
#    real EXACT, the value of the exact integral.
#
  if ( ( expon % 2 ) == 0 ):

    exact = 2.0 / ( expon + 1 )
	
  else:

    exact = 0.0

  return exact

def legendre_monomial_quadrature ( expon, order, w, x ):

#*****************************************************************************80
#
## legendre_monomial_quadrature() applies a quadrature rule to a monomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2023
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
#  Get the exact value of the integral.
#
  exact = legendre_monomial_integral ( expon )
#
#  Evaluate the monomial at the quadrature points.
#
  value = x ** expon
#
#  Compute the weighted sum.
#
  quad = np.dot ( w, value )
#
#  Error:
#
  if ( exact == 0.0 ):
    quad_error = np.abs ( quad - exact )
  else:
    quad_error = np.abs ( ( quad - exact ) / exact )

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
  legendre_exactness_test ( )
  timestamp ( )


