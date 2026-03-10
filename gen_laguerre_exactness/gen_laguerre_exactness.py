#! /usr/bin/env python3
#
def gen_laguerre_exactness_test ( ):

#*****************************************************************************80
#
## gen_laguerre_exactness_test() tests gen_laguerre_exactness().
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
  print ( 'gen_laguerre_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gen_laguerre_exactness().' )

  gen_laguerre_exactness ( 'gen_lag_o8_a0.5', 18, 0.5, 0 )

  gen_laguerre_exactness ( 'gen_lag_o8_a0.5_modified', 18, 0.5, 1 )
#
#  Terminate.
#
  print ( '' )
  print ( 'gen_laguerre_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def gen_laguerre_exactness ( quad_filename, degree_max, alpha, option ):

#*****************************************************************************80
#
## gen_laguerre_exactness() investigates exactness of generalized Laguerre quadrature.
#
#  Discussion:
#
#    This program investigates a generalized Gauss-Laguerre quadrature rule
#    by using it to integrate monomials over [0,+oo), and comparing the
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
#    integer OPTION, whether the rule is for x^alpha*exp(-x)*f(x) or f(x).
#
  import numpy as np

  print ( '' )
  print ( 'gen_laguerre_exactness():' )
  print ( '  Investigate the polynomial exactness of a generalized Gauss-Laguerre' )
  print ( '  quadrature rule by integrating exponentially weighted' )
  print ( '  monomials up to a given degree over the [0,+oo) interval.' )
  print ( '' )
  print ( '  The rule may be defined on another interval, [A,+oo)' )
  print ( '  in which case it is adjusted to the [0,+oo) interval.' )
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
  print ( '  Quadrature rule X file = "' + quad_x_filename + "'" )
  print ( '  Quadrature rule W file = "' + quad_w_filename + "'" )
  print ( '  Quadrature rule R file = "' + quad_r_filename + "'" )
  print ( '  Maximum degree to check = ', degree_max )
  print ( '  Weighting function exponent ALPHA = ', alpha )
  if ( option == 0 ):
    print ( '  OPTION = 0, integrate x^alpha*exp(-x)*f(x).' )
  else:
    print ( '  OPTION = 1, integrate                 f(x).' )
#
#  Read the X file.
#
  x = np.loadtxt ( quad_x_filename )
  order = x.shape[0]

  print ( '' )
  print ( '  Number of points = ', order )
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
  a = r[0]
  print ( '' )
  print ( '  The quadrature rule to be tested is' )
  print ( '  a generalized Gauss-Laguerre rule' )
  print ( '  ORDER = ', order )
  print ( '  A =     ', a )
  print ( '  ALPHA = ', alpha )
  print ( '' )
  if ( option == 0 ):
    print ( '  OPTION = 0, standard rule:' )
    print ( '    Integral ( A <= x < oo ) x^alpha exp(-x) f(x) dx' )
    print ( '    is to be approximated by' )
    print ( '    sum ( 1 <= I <= ORDER ) w(i) * f(x(i)).' )
  else:
    print ( '  OPTION = 1, modified rule:' )
    print ( '    Integral ( A <= x < oo ) f(x) dx' )
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
#  Supposing the input rule is defined on [A,+oo),
#  rescale the weights, and translate the abscissas, 
#  so our rule is defined on [0,+oo).
#
  volume = np.exp ( - a )
  w = w / volume

  x = x - a
#
#  Explore the monomials.
#
  print ( '' )
  print ( '  A generalized Gauss-Laguerre rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '      Degree  Error' )
  print ( '' )

  for degree in range ( 0, degree_max + 1 ):

    quad_error = monomial_quadrature_gen_laguerre ( degree, alpha, order, option, w, x )

    print ( '  %2d  %24.16f' % ( degree, quad_error ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gen_laguerre_exactness():' )
  print ( '  Normal end of execution.' )

  return

def gen_laguerre_integral ( expon, alpha ):

#*****************************************************************************80
#
## gen_laguerre_integral() evaluates a monomial generalized Laguerre integral.
#
#  Discussion:
#
#    The integral being computed is
#
#      integral ( 0 <= x < +oo ) x^n * x^alpha * exp ( -x ) dx
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
#    integer EXPON, the exponent.
#    0 <= EXPON.
#
#    real ALPHA, the exponent of X in the weight function.
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import gamma

  exact = gamma ( alpha + expon + 1 )

  return exact

def monomial_quadrature_gen_laguerre ( expon, alpha, order, option, w, x ):

#*****************************************************************************80
#
## monomial_quadrature_gen_laguerre() applies a quadrature rule to a monomial.
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
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of X in the weight factor.
#
#    intege ORDER, the number of points in the rule.
#
#    integer OPTION, indicates standard or modified rule.
#    0, standard generalized Gauss-Laguerre rule for 
#       integrand x^alpha*exp(-x)*f(x).
#    1, modified generalized Gauss-Laguerre rule for 
#       integrand                 f(x).
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
  exact = gen_laguerre_integral ( expon, alpha )
#
#  Evaluate the unweighted monomial at the quadrature points.
#
  if ( option == 0 ):
    value = x ** expon
  else:
    value = x ** alpha * np.exp ( - x  ) * x ** expon
#
#  Compute the weighted sum.
#
  quad = np.dot ( w, value )
#
#  Error:
#
  quad_error = abs ( ( quad - exact ) / exact )

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
  gen_laguerre_exactness_test ( )
  timestamp ( )

