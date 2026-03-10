#! /usr/bin/env python3
#
def gen_hermite_exactness_test ( ):

#*****************************************************************************80
#
## gen_hermite_exactness_test() tests gen_hermite_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gen_hermite_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gen_hermite_exactness().' )

  gen_hermite_exactness ( 'gen_herm_o8_a1.0', 18, 1.0, 0 )

  gen_hermite_exactness ( 'gen_herm_o8_a1.0_modified', 18, 1.0, 1 )
#
#  Terminate.
#
  print ( '' )
  print ( 'gen_hermite_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def gen_hermite_exactness ( quad_filename, degree_max, alpha, option ):

#*****************************************************************************80
#
## gen_hermite_exactness(): exactness of a generalized Hermite quadrature rule.
#
#  Discussion:
#
#    This program investigates a generalized Gauss-Hermite quadrature rule
#    by using it to integrate monomials over (-oo,+oo), and comparing the
#    approximate result to the known exact value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2023
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
#    integer DEGREE_MAX, the maximum monomial degree to be checked
#
#    real ALPHA, the power of X in the weighting function
#
#    integer OPTION, whether the rule is for |x|^alpha*exp(-x*x)*f(x) or f(x).
#
  import numpy as np

  print ( '' )
  print ( 'gen_hermite_exactness():' )
  print ( '  Investigate the polynomial exactness of a generalized Gauss-Hermite' )
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
  print ( '  Weighting function exponent ALPHA = ', alpha )
  if ( option == 0 ):
    print ( '  OPTION = 0, integrate |x|^alpha*exp(-x*x)*f(x).' )
  else:
    print ( '  OPTION = 1, integrate                     f(x).' )
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
  print ( '  a generalized Gauss-Hermite rule' )
  print ( '  ORDER = ', order )
  print ( '  ALPHA = ', alpha )
  print ( '' )
  if ( option == 0 ):
    print ( '  OPTION = 0, standard rule:' )
    print ( '    Integral ( -oo < x < +oo ) |x|^alpha exp(-x*x) f(x) dx' )
    print ( '    is to be approximated by' )
    print ( '    sum ( 1 <= I <= ORDER ) w(i) * f(x(i)).' )
  else:
    print ( '  OPTION = 1, modified rule:' )
    print ( '    Integral ( -oo < x < +oo ) f(x) dx' )
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
  print ( '  A generalized Gauss-Hermite rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '  Degree    Error' )
  print ( '' )

  for degree in range ( 0, degree_max + 1 ):

    quad_error = monomial_quadrature_gen_hermite ( degree, alpha, order, \
      option, w, x )

    print ( '  %2d  %24.16f' % ( degree, quad_error ) )

  return

def gen_hermite_integral ( expon, alpha ):

#*****************************************************************************80
#
## gen_hermite_integral() evaluates a monomial generalized Hermite integral.
#
#  Discussion:
#
#    H(n,alpha) = Integral ( -oo < x < +oo ) x^n |x|^alpha exp(-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int EXPON, the exponent of the monomial.
#
#    real ALPHA, the exponent of |X| in the integral.
#    -1.0 < ALPHA.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  if ( ( expon % 2 ) == 1 ):

    value = 0.0

  else:

    a = alpha + expon

    if ( a <= -1.0 ):

      value = - np.inf

    else:

      value = gamma ( ( a + 1.0 ) / 2.0 )

  return value

def monomial_quadrature_gen_hermite ( expon, alpha, order, option, w, x ):

#*****************************************************************************80
#
## monomial_quadrature_gen_hermite() applies a quadrature rule to a monomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of X in the weight factor.
#
#    intege ORDER, the number of points in the rule.
#
#    integer OPTION, indicates standard or modified rule.
#    0, standard generalized Gauss-Hermite rule for 
#       integrand |x|^alpha*exp(-x*x)*f(x).
#    1, modified generalized Gauss-Laguerre rule for 
#       integrand                     f(x).
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
#  Get the exact value of the integral of the monomial.
#
  exact = gen_hermite_integral ( expon, alpha )
#
#  Evaluate the unweighted monomial at the quadrature points.
#
  if ( option == 0 ):
    value = x ** expon
  else:
    value = ( np.abs ( x ) ) ** alpha * np.exp ( - x**2 ) * x ** expon
#
#  Compute the weighted sum.
#
  quad = np.dot ( w, value )
#
#  Error:
#
  if ( exact == 0.0 ):
    quad_error = np.abs ( quad )
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
  gen_hermite_exactness_test ( )
  timestamp ( )

