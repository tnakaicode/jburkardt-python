#! /usr/bin/env python3
#
def line01_length ( ):

#*****************************************************************************80
#
## line01_length(): length of the unit line in 1D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the length.
#
  value = 1.0

  return value

def line01_length_test ( ) :

#*****************************************************************************80
#
## line01_length_test() tests line01_length().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'line01_length_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  line01_length returns the length of the unit line.' )

  value = line01_length ( )

  print ( '' )
  print ( '  line01_length() = %g' % ( value ) )

  return

def line01_monomial_integral ( e ):

#*****************************************************************************80
#
## line01_monomial_integral(): monomial integral over the unit line in 1D.
#
#  Discussion:
#
#    The integration region is 
#
#      0 <= X <= 1.
#
#    The monomial is F(X) = X^E.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer E, the exponent.
#    E must not equal -1.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  if ( e == -1 ):
    print ( '' )
    print ( 'line01_monomial_integral(): Fatal error!' )
    print ( '  Exponent E = -1 is not allowed!' )
    raise Exception ( 'line01_monomial_integral(): Fatal error!' )

  integral = 1.0 / float ( e + 1 )

  return integral

def line01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## line01_monomial_integral_test() tests line01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 1
  n = 4192
  test_num = 11

  print ( '' )
  print ( 'line01_monomial_integral_test():' )
  print ( '  line01_monomial_integral() computes integrals of monomials' )
  print ( '  along the length of the unit line in 1D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = line01_sample_random ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
  print ( '' )
  print ( '   E     MC-Estimate      Exact           Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = test

    value = monomial_value_1d ( n, e, x )

    result = line01_length ( ) * np.sum ( value ) / float ( n )
    exact = line01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %14.6g  %14.6g  %10.2g' % ( e, result, exact, error ) )

  return

def line01_sample_ergodic ( n, shift ):

#*****************************************************************************80
#
## line01_sample_ergodic() samples the unit line in 1D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real SHIFT, a value between 0 and 1.
#
#  Output:
#
#    real X(N), the points.
#
#    real SHIFT, an updated shift.
#
  import numpy as np

  golden = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  x = np.zeros ( n, dtype = np.float64 )

  shift = np.mod ( shift, 1.0 );

  for j in range ( 0, n ):
    x[j] = shift
    shift = np.mod ( shift + golden, 1.0 )

  return x, shift

def line01_sample_ergodic_test ( ):

#*****************************************************************************80
#
## line01_sample_ergodic_test() tests line01_sample_ergodic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'line01_sample_ergodic_test' )
  print ( '  line01_sample_ergodic ergodically samples the unit line segment.' )
  print ( '  Use it to estimate integrals.' )
  print ( '' )
  print ( '         N', end = '' )
  print ( '        1', end = '' )
  print ( '               X' ) ,
  print ( '              X^2', end = '' )
  print ( '             X^3', end = '' )
  print ( '             X^4', end = '' )
  print ( '             X^5', end = '' )
  print ( '           X^6' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    shift = 0.0
    x, shift = line01_sample_ergodic ( n, shift )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e = j

      value = monomial_value_1d ( n, e, x )

      result = line01_length ( ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 7 ):

    e = j

    result = line01_monomial_integral ( e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def line01_sample_random ( n, rng ):

#*****************************************************************************80
#
## line01_sample_random() samples the unit line in 1D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(N), the points.
#
  import numpy as np

  x = rng.random ( size = n )

  return x

def line01_sample_random_test ( rng ):

#*****************************************************************************80
#
## line01_sample_random_test() tests line01_sample_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'line01_sample_random_test():' )
  print ( '  line01_sample_random() randomly samples the unit line segment.' )
  print ( '  Use it to estimate integrals.' )
  print ( '' )
  print ( '         N', end = '' )
  print ( '        1', end = '' )
  print ( '               X' ) ,
  print ( '              X^2', end = '' )
  print ( '             X^3', end = '' )
  print ( '             X^4', end = '' )
  print ( '             X^5', end = '' )
  print ( '           X^6' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    x = line01_sample_random ( n, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e = j

      value = monomial_value_1d ( n, e, x )

      result = line01_length ( ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 7 ):

    e = j

    result = line01_monomial_integral ( e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def monomial_value_1d ( n, e, x ):

#*****************************************************************************80
#
## monomial_value_1d() evaluates a monomial in 1D.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      x^e
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    integer E, the exponent.
#
#    real X(N), the point coordinates.
#
#  Output:
#
#    real VALUE(N), the value of the monomial.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, n ):
    value[i] = x[i] ** e

  return value

def monomial_value_1d_test ( rng ):

#*****************************************************************************80
#
## monomial_value_1d_test() tests monomial_value_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'monomial_value_1d_test():' )
  print ( '  monomial_value_1d() evaluates a monomial of a 1D argument.' )
  print ( '' )
  print ( '      X^(-1)       X^(0)       X^(1)       X^(2)       X^(5)' )
  print ( '' )

  n = 5
  x_min = -2.0
  x_max = +10.0
  x = x_min + ( x_max - x_min ) * rng.random ( size = n )

  e = -1
  vm1 = monomial_value_1d ( n, e, x )
  e = 0
  v0 = monomial_value_1d ( n, e, x )
  e = 1
  v1 = monomial_value_1d ( n, e, x )
  e = 2
  v2 = monomial_value_1d ( n, e, x )
  e = 5
  v5 = monomial_value_1d ( n, e, x )

  for j in range ( 0, n ):
    print ( '  %10g  %10g  %10g  %10g  %10g' \
      % ( vm1[j], v0[j], v1[j], v2[j], v5[j] ) )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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

  return None

def line_monte_carlo_test ( ):

#*****************************************************************************80
#
## line_monte_carlo_test() tests line_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2017
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'line_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test line_monte_carlo().' )

  rng = default_rng ( )

  line01_length_test ( )
  line01_monomial_integral_test ( rng )
  line01_sample_ergodic_test ( )
  line01_sample_random_test ( rng )
  monomial_value_1d_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  line_monte_carlo_test ( )
  timestamp ( )
