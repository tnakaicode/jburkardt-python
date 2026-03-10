#! /usr/bin/env python3
#
def chebyshev2_exactness_test ( ):

#*****************************************************************************80
#
## chebyshev2_exactness_test() tests chebyshev2_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'chebyshev2_exactness_test:' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test chebyshev2_exactness.' )

  chebyshev2_exactness ( 'cheby2_o4', 10 )
#
#  Terminate.
#
  print ( '' )
  print ( 'chebyshev2_exactness_test:' )
  print ( '  Normal end of execution.' )

  return

def chebyshev2_exactness ( quad_filename, degree_max ):

#*****************************************************************************80
#
## chebyshev2_exactness() reports the exactness of Chebyshev type 2 quadrature.
#
#  Discussion:
#
#    This program investigates a standard Gauss-Chebvyshev type 2 quadrature rule
#    by using it to integrate monomials over [-1,+1], and comparing the
#    approximate result to the known exact value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
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
  print ( 'chebyshev2_exactness():' )
  print ( '  Investigate the polynomial exactness of a Gauss-Chebyshev1' )
  print ( '  type 2 quadrature rule by integrating all monomials up to a given' )
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
  print ( 'chebyshev2_exactness: User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".' )
  print ( '  Quadrature rule R file = "' + quad_r_filename + '".' )
  print ( '  Maximum degree to check =', degree_max )
#
#  Read the X file.
#
  x = np.loadtxt ( quad_x_filename )
  order = x.shape[0]

  print ( '' )
  print ( '  Number of points  =', order )
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
  print ( '  a Gauss-Chebyshev type 2 rule' )
  print ( '  ORDER = ', order )
  print ( '' )
  print ( '  Standard rule:' )
  print ( '    Integral ( -1 <= x <= +1 ) f(x) * ( 1 - x^2 ) dx' )
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
  print ( '  A Gauss-Chebyshev type 2 rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '      Error    Degree' )
  print ( '' )

  for degree in range ( 0, degree_max + 1 ):
    quad_error = monomial_quadrature_chebyshev2 ( degree, order, w, x )
    print ( '  %24.16f   %2d' % ( quad_error, degree ) )

  return

def chebyshev2_integral ( expon ):

#*****************************************************************************80
#
## chebyshev2_integral() evaluates a monomial Chebyshev type 2 integral.
#
#  Discussion:
#
#    To test a Chebyshev type 2 quadrature rule, we use it to approximate the
#    integral of a monomial:
#
#      integral ( -1 <= x <= +1 ) x^n * sqrt ( 1 - x^2 ) dx
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
#    18 May 2023
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
  import numpy as np
#
#  Get the exact value of the integral.
#
  if ( ( expon % 2 ) == 0 ):

    top = 1
    bot = 1
    for i in range ( 2, expon + 1, 2 ):
      top = top * ( i - 1 )
      bot = bot *   i

    bot = bot * ( expon + 2 )

    exact = np.pi * top / bot

  else:

    exact = 0.0

  return exact

def monomial_quadrature_chebyshev2 ( expon, order, w, x ):

#*****************************************************************************80
#
## monomial_quadrature_chebyshev2d() applies a quadrature rule to a monomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2008
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
  exact = chebyshev2_integral ( expon )
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
  chebyshev2_exactness_test ( )
  timestamp ( )


