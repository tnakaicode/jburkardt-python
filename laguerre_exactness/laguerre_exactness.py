#! /usr/bin/env python3
#
def laguerre_exactness_test ( ):

#*****************************************************************************80
#
## laguerre_exactness_test() tests laguerre_exactness().
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
  print ( 'laguerre_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test laguerre_exactness().' )

  laguerre_exactness ( 'lag_o04', 8, 0 )
#
#  Terminate.
#
  print ( '' )
  print ( 'laguerre_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def laguerre_exactness ( quad_filename, degree_max, option ):

#*****************************************************************************80
#
## laguerre_exactness() checks a Laguerre quadrature rule for exactness.
#
#  Discussion:
#
#    This program investigates a standard Gauss-Laguerre quadrature rule
#    by using it to integrate monomials over [0,+oo), and comparing the
#    approximate result to the known exact value.
#
#    The user specifies:
#    * the "root" name of the R, W and X files that specify the rule
#    * DEGREE_MAX, the maximum monomial degree to be checked.
#    * OPTION, whether the rule is for exp(-x)*f(x) or f(x).
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
#    character quad_filename,  the "root" name of the R, W and X files 
#    that specify the rule
#
#    integer DEGREE_MAX, the maximum monomial degree to be checked.
#
#    integer OPTION, whether the rule is for exp(-x)*f(x) or f(x).
#
  import numpy as np

  print ( '' )
  print ( 'laguerre_exactness():' )
  print ( '  Investigate the exactness of a Gauss-Laguerre' )
  print ( '  quadrature rule for integrating monomials' )
  print ( '  with density exp(-x) or density 1' )
  print ( '  over the [A,+oo) interval.' )
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
  if ( option == 0 ):
    print ( '  OPTION = 0, integrate exp(-x)*f(x).' )
  else:
    print ( '  OPTION = 1, integrate         f(x).' )
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
  a = r[0]
  print ( '' )
  print ( '  The quadrature rule to be tested is' )
  print ( '  a Gauss-Laguerre quadrature rule of ORDER = ', order )
  print ( '  for integrals of the type:' )
  if ( option == 0 ):
    print ( '    Integral ( ', a, ' <= x < +oo ) f(x) exp(-x) dx' )
  elif ( option == 1 ):
    print ( '    Integral ( ', a, ' <= x < +oo ) f(x) dx' )
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
#  so our revised rule is defined on [0,+oo).
#
  volume = np.exp ( - a )
  w = w / volume
  x = x - a
#
#  Explore the monomials.
#
  print ( '' )
  print ( '  A Gauss-Laguerre rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '  Degree      Error' )
  print ( '' )

  for degree in range ( 0, degree_max + 2 ):

    quad_error = laguerre_monomial_quadrature ( degree, order, option, w, x )

    print ( '  %2d  %24.16f'% ( degree, quad_error ) )

  return

def laguerre_monomial_integral ( n ):

#*****************************************************************************80
#
## laguerre_monomial_integral() evaluates a monomial Laguerre integral.
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
#    integer N, the order of the integral.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial

  value = factorial ( n )

  return value

def laguerre_monomial_quadrature ( expon, order, option, w, x ):

#*****************************************************************************80
#
## laguerre_monomial_quadrature() applies a quadrature rule to a monomial.
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
#    integer OPTION, indicates standard or modified rule.
#    0, standard Gauss-Laguerre rule for integrand exp(-x)*f(x).
#    1, modified Gauss-Laguerre rule for integrand         f(x).
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
  exact = laguerre_monomial_integral ( expon )

  if ( option == 0 ):
    value = x ** expon
  else:
    value = np.exp ( - x ) * x ** expon
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
  laguerre_exactness_test ( )
  timestamp ( )

