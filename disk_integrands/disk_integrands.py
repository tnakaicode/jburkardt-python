#! /usr/bin/env python3
#
def disk_integrands_test ( ):

#*****************************************************************************80
#
## disk_integrands_test() tests disk_integrands().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_integrands_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk_integrands().' )

  rng = default_rng ( )

  disk_integrands_test00 ( rng )
  disk_integrands_test01 ( rng )
  disk_integrands_test02 ( rng )
  disk_integrands_test03 ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_integrands_test():' )
  print ( '  Normal end of execution.' )

  return

def disk_integrands_test00 ( rng ):

#*****************************************************************************80
#
## disk_integrands_test00(): integral of X^0 in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
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
  print ( 'disk_integrands_test00():' )
  print ( '  Use a simple Monte Carlo approach to estimate the' )
  print ( '  integral of X^EX inside the disk of radius 1' )
  print ( '  centered at the origin.' )
  print ( '' )
  print ( '           N   EX      Exact Approximate   Error' )

  for ex in range ( 0, 2, 2 ):
    print ( '' )
    p01_parameters ( ex )
    n = 1
    for n_log2 in range ( 0, 3 ):
      xy = disk_unit_sample ( n, rng )
      f = p01_f ( n, xy )
      q = disk_unit_area ( ) * np.sum ( f ) / n
      t = p01_exact ( )
      print ( '  %10d  %2d  %10.4f  %10.4f  %10.4e' \
        % ( n, ex, t, q, np.abs ( t - q ) ) )
      n = n * 2

  return

def disk_integrands_test01 ( rng ):

#*****************************************************************************80
#
## disk_integrands_test01(): integral of X^EX in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
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
  print ( 'disk_integrands_test01():' )
  print ( '  Use a simple Monte Carlo approach to estimate the' )
  print ( '  integral of X^EX inside the disk of radius 1' )
  print ( '  centered at the origin.' )
  print ( '' )
  print ( '           N   EX      Exact Approximate   Error' )

  for ex in range ( 2, 7, 2 ):
    print ( '' )
    p01_parameters ( ex )
    n = 1
    for n_log2 in range ( 0, 21 ):
      xy = disk_unit_sample ( n, rng )
      f = p01_f ( n, xy )
      q = disk_unit_area ( ) * np.sum ( f ) / n
      t = p01_exact ( )
      print ( '  %10d  %2d  %10.4f  %10.4f  %10.4e' \
        % ( n, ex, t, q, np.abs ( t - q ) ) )
      n = n * 2

  return

def disk_integrands_test02 ( rng ):

#*****************************************************************************80
#
## disk_integrands_test02(): integral of R^EX in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
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
  print ( 'disk_integrands_test02():' )
  print ( '  Use a simple Monte Carlo approach to estimate the' )
  print ( '  integral of R^EX over the disk of radius 1' )
  print ( '  centered at the origin.' )
  print ( '' )
  print ( '           N   EX      Exact Approximate   Error' )

  for ex in range ( 1, 6, 2 ):
    print ( '' )
    p02_parameters ( ex )
    n = 1
    for n_log2 in range ( 0, 21 ):
      xy = disk_unit_sample ( n, rng )
      f = p02_f ( n, xy )
      q = disk_unit_area ( ) * np.sum ( f ) / n
      t = p02_exact ( )
      print ( '  %10d  %2d  %10.4f  %10.4f  %10.4e' \
        % ( n, ex, t, q, np.abs ( t - q ) ) )
      n = n * 2

  return

def disk_integrands_test03 ( rng ):

#*****************************************************************************80
#
## disk_integrands_test03(): integral of exp(x) in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
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
  print ( 'disk_integrands_test03():' )
  print ( '  Use a simple Monte Carlo approach to estimate the' )
  print ( '  integral of exp(X) over the disk of radius 1' )
  print ( '  centered at the origin.' )
  print ( '' )
  print ( '           N       Exact Approximate   Error' )
  print ( '' )

  n = 1
  for n_log2 in range ( 0, 21 ):
    xy = disk_unit_sample ( n, rng )
    f = p03_f ( n, xy )
    q = disk_unit_area ( ) * np.sum ( f ) / n
    t = p03_exact ( )
    print ( '  %10d  %10.4f  %10.4f  %10.4e' % ( n, t, q, np.abs ( t - q ) ) )
    n = n * 2

  return

def cos_power_int ( a, b, n ):

#*****************************************************************************80
#
## cos_power_int() evaluates the cosine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      COS_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( cos ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral cos^n ( t ) = -(1/n) * (
#        cos^(n-1)(t) * sin(t) + ( n-1 ) * Integral cos^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of integration.
#
#    integer N, the power.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'cos_power_int(): Fatal error!' )
    print ( '  Power N < 0.' )
    raise Exception ( 'cos_power_int(): Fatal error!' )

  sa = np.sin ( a )
  sb = np.sin ( b )
  ca = np.cos ( a )
  cb = np.cos ( b )

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = sb - sa
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value - ca ** ( m - 1 ) * sa \
                                + cb ** ( m - 1 ) * sb ) / m

  return value

def disk_unit_area ( ):

#*****************************************************************************80
#
## disk_unit_area() returns the area of the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real AREA, the area.
#
  import numpy as np

  r = 1.0
  area = np.pi * r * r

  return area

def disk_unit_sample ( n, rng ):

#*****************************************************************************80
#
## disk_unit_sample() returns sample points from the unit disk.
#
#  Discussion:
#
#    The unit disk has center at the origin, and radius 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 October 2022
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
#    real XY(2,N), the points.
#
  import numpy as np

  r = rng.random ( size = n )
  r = np.sqrt ( r )

  t = rng.random ( size = n )
  t = 2.0 * np.pi * t

  xy = np.zeros ( [ 2, n ] )
  xy[0,:] = r * np.cos ( t )
  xy[1,:] = r * np.sin ( t )

  return xy

def p00_num ( ):

#*****************************************************************************80
#
## p00_num() returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer VALUE, the number of problems.
#
  value = 3

  return value

def p01_exact ( ):

#*****************************************************************************80
#
## p01_exact() returns the exact integral of function 1 over the unit disk.
#
#  Discussion:
#
#    The integral depends on a parameter EX which can be set or
#    retrieved through p01_parameters().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the exact integral.
#
  import numpy as np

  ex = p01_parameters ( )

  value = cos_power_int ( 0.0, 2.0 * np.pi, ex ) / ( ex + 2.0 )

  return value

def p01_f ( n, x ):

#*****************************************************************************80
#
## p01_f() evaluates test function #1 in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(2,N), the arguments.
#
#  Output:
#
#    real VALUE(N,1), the values of the integrand.
#
  ex = p01_parameters ( )

  value = x[0,:] ** ex

  return value

def p01_parameters ( ex_user = None ):

#*****************************************************************************80
#
## p01_parameters() returns parameters for disk integrand problem 1.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ex_user: a new value for the exponent.
#
#  Output:
#
#    integer ex: the exponent.
#

#
#  Initialize defaults.
#
  if not hasattr ( p01_parameters, "ex_default" ):
    p01_parameters.ex_default = 0
#
#  Update defaults if input was supplied.
#
  if ( ex_user is not None ):
    p01_parameters.ex_default = ex_user
#
#  Return values.
#
  ex = p01_parameters.ex_default

  return ex

def p02_exact ( ):

#*****************************************************************************80
#
## p02_exact() returns the exact integral of function 2 over the unit disk.
#
#  Discussion:
#
#    The integral depends on a parameter EX which must be set by calling
#    p02_parameters() before calling this function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the exact integral.
#
  import numpy as np

  ex = p02_parameters ( )

  value = 2.0 * np.pi / ( ex + 2.0 )

  return value

def p02_f ( n, x ):

#*****************************************************************************80
#
## p02_f() evaluates test function #2 in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 December 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(2,N), the arguments.
#
#  Output:
#
#    real VALUE(N,1), the values of the integrand.
#
  import numpy as np

  ex = p02_parameters ( )

  r = np.linalg.norm ( x, axis = 0 )

  value = r ** ex

  return value

def p02_parameters ( ex_user = None ):

#*****************************************************************************80
#
## p02_parameters() returns parameters for disk integrand problem 2.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ex_user: a new value for the exponent.
#
#  Output:
#
#    integer ex: the exponent.
#

#
#  Initialize defaults.
#
  if not hasattr ( p02_parameters, "ex_default" ):
    p02_parameters.ex_default = 0
#
#  Update defaults if input was supplied.
#
  if ( ex_user is not None ):
    p02_parameters.ex_default = ex_user
#
#  Return values.
#
  ex = p02_parameters.ex_default

  return ex

def p03_exact ( ):

#*****************************************************************************80
#
## p03_exact() returns the exact integral of function 3 over the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the exact integral.
#
  from scipy.special import iv
  import numpy as np

  nu = 1.0
  z = 1.0
  value = 2.0 * np.pi * iv ( nu, z )

  return value

def p03_f ( n, x ):

#*****************************************************************************80
#
## p03_f() evaluates test function #3 in the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 December 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(2,N), the arguments.
#
#  Output:
#
#    real VALUE(N,1), the values of the integrand.
#
  import numpy as np

  value = np.exp ( x[0,:] )

  return value

def sin_power_int ( a, b, n ):

#*****************************************************************************80
#
## sin_power_int() evaluates the sine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      SIN_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( sin ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral sin^n ( t ) = (1/n) * (
#        sin^(n-1)(t) * cos(t) + ( n-1 ) * Integral sin^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of integration.
#
#    integer N, the power of the sine function.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  if ( n < 0 ):
    print ( '' )
    print ( 'sin_power_int(): Fatal error!' )
    print ( '  Power N < 0.' )
    raise Exception ( 'sin_power_int(): Fatal error!' )

  sa = np.sin ( a )
  sb = np.sin ( b )
  ca = np.cos ( a )
  cb = np.cos ( b )

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = ca - cb
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value + sa ** ( m - 1 ) * ca \
                                - sb ** ( m - 1 ) * cb ) / m
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
  disk_integrands_test ( )
  timestamp ( )


