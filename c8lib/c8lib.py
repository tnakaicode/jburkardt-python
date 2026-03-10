#! /usr/bin/env python3
#
def c8_abs ( c ):

#*****************************************************************************80
#
## c8_abs() evaluates the absolute value of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    real VALUE, the absolute value.
#
  import numpy as np

  value = np.sqrt ( ( c.real ) ** 2 + ( c.imag ) ** 2 )

  return value

def c8_abs_test ( ):

#*****************************************************************************80
#
## c8_abs_test() tests c8_abs().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_aBS_test' )
  print ( '  c8_aBS computes the absolute value of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_aBS(C1)             R3=ABS(C1)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_abs ( c1 )
    r3 = abs ( c1 )
    print ( '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 ) )

  return

def c8_acosh ( c ):

#*****************************************************************************80
#
## c8_acosh() evaluates the inverse hyperbolic cosine of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#    Here we use the relationship:
#
#      c8_acosh ( Z ) = i * c8_acos ( Z ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = 1j * c8_acos ( c )

  return value

def c8_acosh_test ( ):

#*****************************************************************************80
#
## c8_acosh_test() tests c8_acosh().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_acosh_test' )
  print ( '  c8_acosh computes the inverse hyperbolic cosine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_acosh(C1)             C3=c8_cosh(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_acosh ( c1 )
    c3 = c8_cosh ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_acos ( c ):

#*****************************************************************************80
#
## c8_acos() evaluates the inverse cosine of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#    Here we use the relationship:
#
#      c8_acos ( Z ) = pi/2 - c8_asin ( Z ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  import numpy as np

  value = 0.5 * np.pi - c8_asin ( c )

  return value

def c8_acos_test ( ):

#*****************************************************************************80
#
## c8_acos_test() tests c8_acos().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_acos_test' )
  print ( '  c8_acos computes the inverse cosine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_acos(C1)             C3=c8_cos(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_acos ( c1 )
    c3 = c8_cos ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_add ( c1, c2 ):

#*****************************************************************************80
#
## c8_add() adds two C8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values to add.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = c1 + c2

  return value

def c8_add_test ( ):

#*****************************************************************************80
#
## c8_add_test() tests c8_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_add_test' )
  print ( '  c8_add adds two C8s.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          C3=c8_add(C1,C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    c3 = c8_add ( c1, c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_arg ( c ):

#*****************************************************************************80
#
## c8_arg() returns the argument of a C8.
#
#  Discussion:
#
#    The value returned by this function will always lie between 0 and 2*PI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value whose argument is desired.
#
#  Output:
#
#    real VALUE, the argument.
#
  import numpy as np

  if ( c.imag == 0.0 and c.real  == 0.0  ):

    value = 0.0

  else:

    r1 = c.imag
    r2 = c.real
    value = np.arctan2 ( r1, r2 )

  return value

def c8_arg_test ( ):

#*****************************************************************************80
#
## c8_arg_test() tests c8_arg().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_arg_test' )
  print ( '  c8_arg computes the argument of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_arg(C1)             R3=NP.ANGLE(C1)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_arg ( c1 )
    r3 = np.angle ( c1 )
    print ( '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 ) )

  return

def c8_asinh ( c ):

#*****************************************************************************80
#
## c8_asinh() evaluates the inverse hyperbolic sine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_asinh ( Z ) = - i * c8_asin ( i * Z ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = - 1j * c8_asin ( 1j * c )

  return value

def c8_asinh_test ( ):

#*****************************************************************************80
#
## c8_asinh_test() tests c8_asinh().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_asinh_test' )
  print ( '  c8_asinh computes the inverse sine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_asinh(C1)            C3=sinh(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_asinh ( c1 )
    c3 = np.sinh ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_asin ( c ):

#*****************************************************************************80
#
## c8_asin() evaluates the inverse sine of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#    Here we use the relationship:
#
#      c8_asin ( Z ) = - i * log ( i * z + sqrt ( 1 - z * z ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  import numpy as np

  value = - 1j * np.log ( 1j * c + np.sqrt ( 1.0 - c * c ) )

  return value

def c8_asin_test ( ):

#*****************************************************************************80
#
## c8_asin_test() tests c8_asin().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_asin_test' )
  print ( '  c8_asin computes the inverse sine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_asin(C1)             C3=c8_sin(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_asin ( c1 )
    c3 = c8_sin ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_atanh ( c ):

#*****************************************************************************80
#
## c8_atanh() evaluates the inverse tangent of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_atanh ( Z ) = - i * c8_atan ( i * Z ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = - 1j * c8_atan ( 1j * c )

  return value

def c8_atanh_test ( ):

#*****************************************************************************80
#
## c8_atanh_test() tests c8_atanh().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_atanh_test' )
  print ( '  c8_atanh computes the inverse hyperbolic tangent of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_atanh(C1)             C3=c8_tanh(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_atanh ( c1 )
    c3 = c8_tanh ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_atan ( c ):

#*****************************************************************************80
#
## c8_atan() evaluates the inverse tangent of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_atan ( Z ) = ( i / 2 ) * log ( ( 1 - i * z ) / ( 1 + i * z ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  arg = ( 1.0 - 1j * c ) / ( 1.0 + 1j * c )

  value = 0.5 * 1j * c8_log ( arg )

  return value

def c8_atan_test ( ):

#*****************************************************************************80
#
## c8_atan_test() tests c8_atan().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_atan_test' )
  print ( '  c8_atan computes the inverse tangent of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_atan(C1)             C3=c8_tan(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_atan ( c1 )
    c3 = c8_tan ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_conj ( c ):

#*****************************************************************************80
#
## c8_conj() evaluates the conjugate of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = c.real - 1j * c.imag

  return value

def c8_conj_test ( ):

#*****************************************************************************80
#
## c8_conj_test() tests c8_conj().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_conj_test' )
  print ( '  c8_conj computes the conjugate of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_conj(C1)             C3=c8_conj(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_conj ( c1 )
    c3 = c8_conj ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_cosh ( c ):

#*****************************************************************************80
#
## c8_cosh() evaluates the hyperbolic cosine of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = ( c8_exp ( c ) + c8_exp ( -c ) ) / 2.0

  return value

def c8_cosh_test ( ):

#*****************************************************************************80
#
## c8_cosh_test() tests c8_cosh().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_cosh_test' )
  print ( '  c8_cosh computes the cosine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_cosh(C1)             C3=c8_acosh(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_cosh ( c1 )
    c3 = c8_acosh ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_cos ( c ):

#*****************************************************************************80
#
## c8_cos() evaluates the cosine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_cos ( C ) = ( c8_exp ( i * C ) + c8_exp ( - i * C ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = ( c8_exp ( 1j * c ) + c8_exp ( - 1j * c ) ) / 2.0

  return value

def c8_cos_test ( ):

#*****************************************************************************80
#
## c8_cos_test() tests c8_cos().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_cos_test' )
  print ( '  c8_cos computes the cosine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_cos(C1)             C3=c8_acos(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_cos ( c1 )
    c3 = c8_acos ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_cube_root ( c ):

#*****************************************************************************80
#
## c8_cube_root() returns the principal square root of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the number whose square root is desired.
#
#  Output:
#
#    complex VALUE, the square root of X.
#
  import numpy as np

  arg = c8_arg ( c )
  mag = c8_mag ( c );

  mag = mag ** ( 1.0 / 3.0 )
  arg = arg / 3.0
  value = mag * complex ( np.cos ( arg ), np.sin ( arg ) )

  return value

def c8_cube_root_test ( ):

#*****************************************************************************80
#
## c8_cube_root_test() tests c8_cube_root().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_cube_root_test' )
  print ( '  c8_cube_root computes the cube root of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_cube_root(C1)             C3=C2*C2*C2' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_cube_root ( c1 )
    c3 = c2 * c2 * c2;
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_div ( c1, c2 ):

#*****************************************************************************80
#
## c8_div() divides two C8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values.
#
#  Output:
#
#    complex VALUE, the function value.
#
  a = c1.real
  b = c1.imag
  c = c2.real
  d = c2.imag

  e = c * c + d * d

  f = ( a * c + b * d ) / e
  g = ( b * c - a * d ) / e

  value = f + g * 1j

  return value

def c8_div_test ( ):

#*****************************************************************************80
#
## c8_div_test() tests c8_div().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_div_test' )
  print ( '  c8_div divides two C8s.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          C3=c8_div(C1,C2)      C4=C1/C2' )
  print ( '     ---------------------     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    c3 = c8_div ( c1, c2 )
    c4 = c1 / c2
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag, c4.real, c4.imag ) )

  return

def c8_div_r8 ( c1, r2 ):

#*****************************************************************************80
#
## c8_div_r8() divides a C8 by an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, real R2, the values.
#
#  Output:
#
#    complex VALUE, the function value.
#
  a = c1.real / r2
  b = c1.imag / r2

  value = a + b * 1j

  return value

def c8_div_r8_test ( ):

#*****************************************************************************80
#
## c8_div_r8_test() tests c8_div_r8().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'c8_div_r8_test' )
  print ( '  c8_div_r8 divides a C8 by an R8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=R8_uniform_01          C3=c8_div_r8(C1,RC2)      C4=C1/R2' )
  print ( '     ---------------------     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = rng.random ( )
    c3 = c8_div_r8 ( c1, r2 )
    c4 = c1 / r2
    print ( '  (%12f,%12f)   %12f               (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, r2, c3.real, c3.imag, c4.real, c4.imag ) )

  return

def c8_exp ( c ):

#*****************************************************************************80
#
## c8_exp() evaluates the exponential of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  import numpy as np

  cr = c.real;
  ci = c.imag;

  value = np.exp ( cr ) * ( np.cos ( ci ) + np.sin ( ci ) * 1j );

  return value

def c8_exp_test ( ):

#*****************************************************************************80
#
## c8_exp_test() tests c8_exp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_exp_test' )
  print ( '  c8_exp computes the exponential of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_exp(C1)             C3=c8_log(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_exp ( c1 )
    c3 = c8_log ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_imag ( c ):

#*****************************************************************************80
#
## c8_imag() returns the imaginary part of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    real VALUE, the real part of C.
#
  value = c.imag

  return value

def c8_imag_test ( ):

#*****************************************************************************80
#
## c8_imag_test() tests c8_imag().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_imag_test' )
  print ( '  c8_imag computes the imaginary part of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_imag(C1)         R3=C1.Imag' )
  print ( '     ---------------------     ---------------------  ------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_imag ( c1 )
    r3 = c1.imag
    print ( '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 ) )

  return

def c8_inv ( c ):

#*****************************************************************************80
#
## c8_inv() evaluates the inverse of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = c8_conj ( c ) / ( c8_mag ( c )  ) ** 2

  return value

def c8_inv_test ( ):

#*****************************************************************************80
#
## c8_inv_test() tests c8_inv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_inv_test' )
  print ( '  c8_inv computes the inverse of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_inv(C1)             C3=c8_inv(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_inv ( c1 )
    c3 = c8_inv ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_i ( ):

#*****************************************************************************80
#
## c8_i() returns the value of the imaginary unit as a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the value of the imaginary unit.
#
  value = 1j

  return value

def c8_i_test ( ):

#*****************************************************************************80
#
## c8_i_test() tests c8_i().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_i_test' )
  print ( '  c8_i returns the value of the imaginary unit.' )

  c1 = c8_i ( )
  print ( '' )
  print ( '  C1=c8_i ( ) = (%g,%g)' % ( c1.real, c1.imag ) )
  c2 = c1 * c1
  print ( '' )
  print ( '  C2= C1 * C1 = (%g,%g)' % ( c2.real, c2.imag ) )

  return

def c8_le_l1 ( c1, c2 ):

#*****************************************************************************80
#
## c8_le_l1() := C1 <= C1 for C8's, and the L1 norm.
#
#  Discussion:
#
#    The L1 norm can be defined here as:
#
#      c8_norm_l1(C) = abs ( real (C) ) + abs ( imag (C) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values to be compared.
#
#  Output:
#
#    bool VALUE, is TRUE if C1 <= C2.
#
  if ( abs ( c1.real ) + abs ( c1.imag ) <= abs ( c2.real ) + abs ( c2.imag ) ) :
    value = True
  else:
    value = False

  return value

def c8_le_l1_test ( ):

#*****************************************************************************80
#
## c8_le_l1_test() tests c8_le_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_le_l1_test' )
  print ( '  c8_le_l1 evalues (C1 <= C2) using the L1 norm.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          L3=c8_le_l1(C1,C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    l3 = c8_le_l1 ( c1, c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  %s' \
      % ( c1.real, c1.imag, c2.real, c2.imag, l3 ) )

  return

def c8_le_l2 ( c1, c2 ):

#*****************************************************************************80
#
## c8_le_l2() := C1 <= C1 for C8's, and the L2 norm.
#
#  Discussion:
#
#    The L2 norm can be defined here as:
#
#      c8_norm_l2(C) = sqrt ( ( real (C) ) ^ 2 + abs ( imag (C) ) ^ 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values to be compared.
#
#  Output:
#
#    bool VALUE, is TRUE if C1 <= C2.
#
  if ( c1.real ** 2 + c1.imag ** 2 <= c2.real ** 2 + c2.imag ** 2 ) :
    value = True
  else:
    value = False

  return value

def c8_le_l2_test ( ):

#*****************************************************************************80
#
## c8_le_l2_test() tests c8_le_l2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_le_l2_test' )
  print ( '  c8_le_l2 evalues (C1 <= C2) using the L2 norm.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          L3=c8_le_l2(C1,C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    l3 = c8_le_l2 ( c1, c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  %s' \
      % ( c1.real, c1.imag, c2.real, c2.imag, l3 ) )

  return

def c8_le_li ( c1, c2 ):

#*****************************************************************************80
#
## c8_le_li() := C1 <= C1 for C8's, and the Loo norm.
#
#  Discussion:
#
#    The Loo norm can be defined here as:
#
#      c8_norm_li(C) = max ( abs ( real (C) ) + abs ( imag (C) ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values to be compared.
#
#  Output:
#
#    bool VALUE, is TRUE if C1 <= C2.
#
  if ( max ( abs ( c1.real ), abs ( c1.imag ) ) \
    <= max ( abs ( c2.real ), abs ( c2.imag ) ) ) :
    value = True
  else:
    value = False

  return value

def c8_le_li_test ( ):

#*****************************************************************************80
#
## c8_le_li_test() tests c8_le_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_le_li_test' )
  print ( '  c8_le_li evalues (C1 <= C2) using the Loo norm.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          L3=c8_le_li(C1,C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    l3 = c8_le_li ( c1, c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  %s' \
      % ( c1.real, c1.imag, c2.real, c2.imag, l3 ) )

  return

def c8lib_test ( ):

#*****************************************************************************80
#
## c8lib_test() tests c8lib().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8lib_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test c8lib().' )

  c8_abs_test ( )
  c8_acos_test ( )
  c8_acosh_test ( )
  c8_add_test ( )
  c8_arg_test ( )
  c8_asin_test ( )
  c8_asinh_test ( )
  c8_atan_test ( )
  c8_atanh_test ( )
  c8_conj_test ( )
  c8_cos_test ( )
  c8_cosh_test ( )
  c8_cube_root_test ( )
  c8_div_test ( )
  c8_div_r8_test ( )
  c8_exp_test ( )
  c8_i_test ( )
  c8_imag_test ( )
  c8_inv_test ( )
  c8_le_l1_test ( )
  c8_le_l2_test ( )
  c8_le_li_test ( )
  c8_log_test ( )
  c8_mag_test ( )
  c8_mul_test ( )
  c8_nint_test ( )
  c8_norm_l1_test ( )
  c8_norm_l2_test ( )
  c8_norm_li_test ( )
  c8_normal_01_test ( )
  c8_one_test ( )
  c8_print_test ( )
  c8_real_test ( )
  c8_sin_test ( )
  c8_sinh_test ( )
  c8_sqrt_test ( )
  c8_tan_test ( )
  c8_tanh_test ( )
  c8_to_cartesian_test ( )
  c8_to_polar_test ( )
  c8_uniform_01_test ( )
  c8_zero_test ( )

  c8mat_identity_test ( )
  c8mat_indicator_test ( )
  c8mat_norm_fro_test ( )
  c8mat_norm_l1_test ( )
  c8mat_norm_li_test ( )
  c8mat_print_test ( )
  c8mat_print_some_test ( )
  c8mat_uniform_01_test ( )

  c8vec_indicator_test ( )
  c8vec_nint_test ( )
  c8vec_norm_l1_test ( )
  c8vec_norm_l2_test ( )
  c8vec_norm_li_test ( )
  c8vec_print_test ( )
  c8vec_print_part_test ( )
  c8vec_sort_a_l1_test ( )
  c8vec_sort_a_l2_test ( )
  c8vec_sort_a_li_test ( )
  c8vec_spiral_test ( )
  c8vec_uniform_01_test ( )
  c8vec_unity_test ( )

  cartesian_to_c8_test ( )

  polar_to_c8_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8lib_test():' )
  print ( '  Normal end of execution.' )

def c8_log ( c ):

#*****************************************************************************80
#
## c8_log() evaluates the logarithm of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_log ( Z ) = LOG ( mag ( Z ) ) + i * ARG ( Z )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  import numpy as np

  arg = c8_arg ( c );
  mag = c8_mag ( c );

  value = np.log ( mag ) + arg * 1j;

  return value

def c8_log_test ( ):

#*****************************************************************************80
#
## c8_log_test() tests c8_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_log_test' )
  print ( '  c8_log computes the logarithm of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_log(C1)             C3=c8_exp(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_log ( c1 )
    c3 = c8_exp ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_mag ( c ):

#*****************************************************************************80
#
## c8_mag() returns the magnitude of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value.
#
#  Output:
#
#    real VALUE, the magnitude.
#
  import numpy as np

  r1 = c.imag
  r2 = c.real
  value = np.sqrt ( r1 * r1 + r2 * r2 )

  return value

def c8_mag_test ( ):

#*****************************************************************************80
#
## c8_mag_test() tests c8_mag().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_mag_test' )
  print ( '  c8_mag computes the magnitude of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_mag(C1)             R3=NP.ABSOLUTE(C1)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_mag ( c1 )
    r3 = np.absolute ( c1 )
    print ( '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 ) )

  return

def c8mat_identity ( n ):

#*****************************************************************************80
#
## c8mat_identity() returns the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    complex C(N,N), the identity matrix.
#
  import numpy as np

  c = np.zeros ( ( n, n ), 'complex' )

  for i in range ( 0, n ): 
    c[i][i] = complex ( 1.0, 0.0 )

  return c

def c8mat_identity_test ( ):

#*****************************************************************************80
#
## c8mat_identity_test() tests c8mat_identity().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 4

  print ( '' )
  print ( 'c8mat_identity_test' )
  print ( '  c8mat_identity returns the complex identity matrix.' )

  c = c8mat_identity ( n )

  c8mat_print ( m, n, c, '  identity matrix:' )

  return

def c8mat_indicator ( m, n ):

#*****************************************************************************80
#
## c8mat_indicator() returns the indicator matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    complex C(M,N), the indicator matrix.
#
  import numpy as np

  c = np.zeros ( ( m, n ), 'complex' )

  for j in range ( 0, n ): 
    for i in range ( 0, m ):
      c[i][j] = complex ( i + 1, - j - 1 )

  return c

def c8mat_indicator_test ( ):

#*****************************************************************************80
#
## c8mat_indicator_test() tests c8mat_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 3

  print ( '' )
  print ( 'c8mat_indicator_test' )
  print ( '  c8mat_indicator returns the complex indicator matrix.' )

  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  indicator matrix:' )

  return

def c8mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## c8mat_mm() multiplies two C8MAT's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    complex A(N1,N2), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    complex C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ), dtype = np.complex64 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def c8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## c8mat_norm_fro() returns the Frobenius norm of a C8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      c8mat_norm_fro = sqrt (
#        sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J) * A(I,J) )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      c8vec_norm_l2 ( A * x ) <= c8mat_norm_fro ( A ) * c8vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    complex A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  import numpy as np

  value = \
    np.sqrt \
    ( \
      np.sum \
      ( \
        np.sum \
        ( \
          ( \
            np.abs \
            ( \
              a \
            ) \
          ) ** 2 \
        ) \
      ) \
   )

  return value

def c8mat_norm_fro_test ( ):

#*****************************************************************************80
#
## c8mat_norm_fro_test() tests c8mat_norm_fro().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8mat_norm_fro_test' )
  print ( '  c8mat_norm_fro computes the Frobenius norm of a C8MAT.' )

  m = 5
  n = 4
  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  The indicator matrix:' )

  value = c8mat_norm_fro ( m, n, c )

  print ( '' )
  print ( '  Frobenius norm = %g' % ( value ) )

  return

def c8mat_norm_l1 ( m, n, a ):

#*****************************************************************************80
#
## c8mat_norm_l1() returns the L1 norm of a C8MAT.
#
#  Discussion:
#
#    The L1 norm is defined as
#
#      c8mat_norm_l1 = max ( 1 <= J <= N )
#        sum ( 1 <= I <= M ) abs ( A(I,J) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    complex A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  import numpy as np

  value = 0.0

  for j in range ( 0, n ):
    col_sum = 0.0
    for i in range ( 0, m ):
      col_sum = col_sum + abs ( a[i,j] )
    value = max ( value, col_sum )

  return value

def c8mat_norm_l1_test ( ):

#*****************************************************************************80
#
## c8mat_norm_l1_test() tests c8mat_norm_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8mat_norm_l1_test' )
  print ( '  c8mat_norm_l1 computes the L1 norm of a C8MAT.' )

  m = 5
  n = 4
  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  The indicator matrix:' )

  value = c8mat_norm_l1 ( m, n, c )

  print ( '' )
  print ( '  L1 norm = %g' % ( value ) )

  return

def c8mat_norm_li ( m, n, a ):

#*****************************************************************************80
#
## c8mat_norm_li() returns the Loo norm of a C8MAT.
#
#  Discussion:
#
#    The Loo norm is defined as
#
#      c8mat_norm_li = max ( 1 <= I <= M ) sum ( 1 <= J <= N ) abs ( A(I,J) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    complex A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  import numpy as np

  value = 0.0

  for i in range ( 0, m ):
    row_sum = 0.0
    for j in range ( 0, n ):
      row_sum = row_sum + abs ( a[i,j] )
    value = max ( value, row_sum )

  return value

def c8mat_norm_li_test ( ):

#*****************************************************************************80
#
## c8mat_norm_li_test() tests c8mat_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8mat_norm_li_test' )
  print ( '  c8mat_norm_li computes the Loo norm of a C8MAT.' )

  m = 5
  n = 4
  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  The indicator matrix:' )

  value = c8mat_norm_li ( m, n, c )

  print ( '' )
  print ( '  Loo norm = %g' % ( value ) )

  return

def c8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## c8mat_print() prints a C8MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    complex A(M,N), the matrix.
#
#    string TITLE, a title.
#
  c8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def c8mat_print_test ( ):

#*****************************************************************************80
#
## c8mat_print_test() tests c8mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8mat_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_print prints an C8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0) ] ], \
    dtype = np.complex128 )

  c8mat_print ( m, n, v, '  Here is a C8MAT:' )

  return

def c8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## c8mat_print_some() prints out a portion of an C8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    complex A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 4

  print ( '' )
  print  ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '       %7d              ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  %12gi ' % ( a.real[i,j], a.imag[i,j] ), end = '' )

      print ( '' )

  return

def c8mat_print_some_test ( ):

#*****************************************************************************80
#
## c8mat_print_some_test() tests c8mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_print_some prints some of an C8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0), \
      complex(10.0, 4.0), complex(10.0, 5.0), complex(10.0, 6.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0), \
      complex(20.0, 4.0), complex(20.0, 5.0), complex(20.0, 6.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0), \
      complex(30.0, 4.0), complex(30.0, 5.0), complex(30.0, 6.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0), \
      complex(40.0, 4.0), complex(40.0, 5.0), complex(40.0, 6.0) ] ], \
    dtype = np.complex128 )

  c8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is a C8MAT:' )

  return

def c8mat_uniform_01 ( m, n ):

#*****************************************************************************80
#
## c8mat_uniform_01() returns a unit pseudorandom C8MAT.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix.
#
#  Output:
#
#    complex C(M,N), the pseudorandom complex matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  c = np.zeros ( ( m, n ), 'complex' )

  for i2 in range ( 0, n ): 
    for i1 in range ( 0, m ):

      r = rng.random ( )
      r = np.sqrt ( r )
      theta = 2.0 * np.pi * rng.random ( )

      c[i1,i2] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c

def c8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## c8mat_uniform_01_test() tests c8mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 3

  print ( '' )
  print ( 'c8mat_uniform_01_test' )
  print ( '  c8mat_uniform_01 computes a random C8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )

  v = c8mat_uniform_01 ( m, n )

  c8mat_print ( m, n, v, '  Random C8MAT:' )

  return

def c8_mul ( c1, c2 ):

#*****************************************************************************80
#
## c8_mul() multiplies two C8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values.
#
#  Output:
#
#    complex VALUE, the function value.
#
  a1 = c1.real
  b1 = c1.imag
  a2 = c2.real
  b2 = c2.imag

  a3 = a1 * a2 - b1 * b2
  b3 = a1 * b2 + b1 * a2

  value = a3 + b3 * 1j

  return value

def c8_mul_test ( ):

#*****************************************************************************80
#
## c8_mul_test() tests c8_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_mul_test' )
  print ( '  c8_mul multiplies two C8s.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          C3=c8_mul(C1,C2)      C4=C1*C2' )
  print ( '     ---------------------     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    c3 = c8_mul ( c1, c2 )
    c4 = c1 * c2
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag, c4.real, c4.imag ) )

  return

def c8_nint ( c ):

#*****************************************************************************80
#
## c8_nint() returns the nearest complex integer of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, the value to be NINT'ed.
#
#  Output:
#
#    complex VALUE, the NINT'ed value.
#
  import numpy as np

  xc = c.real
  yc = c.imag
#
#  Lower left.
#
  x = np.floor ( xc )
  y = np.floor ( yc )
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  r_min = r
  x_min = x
  y_min = y
#
#  Lower right.
#
  x = np.floor ( xc ) + 1.0
  y = np.floor ( yc )
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  if ( r < r_min ):
    r_min = r
    x_min = x
    y_min = y
#
#  Upper right.
#
  x = np.floor ( xc ) + 1.0
  y = np.floor ( yc ) + 1.0
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  if ( r < r_min ):
    r_min = r
    x_min = x
    y_min = y
#
#  Upper left.
#
  x = np.floor ( xc )
  y = np.floor ( yc ) + 1.0
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  if ( r < r_min ):
    r_min = r
    x_min = x
    y_min = y
 
  value = x_min + 1j * y_min

  return value

def c8_nint_test ( ):

#*****************************************************************************80
#
## c8_nint_test() tests c8_nint().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_nint_test' )
  print ( '  c8_nint computes the nearest integer to a C8.' )
  print ( '' )
  print ( '       C1=10*c8_uniform_01     C2=c8_nint(C1)' )
  print ( '     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c1 = 10.0 * c1
    c2 = c8_nint ( c1 )
    print ( '  (%12f,%12f)  (%12f,%12f)' % ( c1.real, c1.imag, c2.real, c2.imag ) )

  return

def c8_normal_01 ( ):

#*****************************************************************************80
#
## c8_normal_01() returns a unit normally distributed complex number.
#
#  Discussion:
#
#    The value has mean 0 and standard deviation 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex C, a sample of the PDF.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  v1 = rng.random ( )
  v2 = rng.random ( )

  x = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.cos ( 2.0 * np.pi * v2 )
  y = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.sin ( 2.0 * np.pi * v2 )

  c = x + y * 1j

  return c

def c8_normal_01_test ( ):

#*****************************************************************************80
#
## c8_normal_01_test() tests c8_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8_normal_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8_normal_01 computes pseudonormal complex values.' )
  print ( '' )

  for i in range ( 1, 11 ):
    c = c8_normal_01 ( )
    print ( '  %6d  ( %f, %f )' % ( i, c.real, c.imag ) )

  return

def c8_norm_l1 ( c ):

#*****************************************************************************80
#
## c8_norm_l1() evaluates the L1 norm of a C8.
#
#  Discussion:
#
#    Numbers of equal norm lie along diamonds centered at (0,0).
#
#    The L1 norm can be defined here as:
#
#      c8_norm_l1(X) = abs ( real (X) ) + abs ( imag (X) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value whose norm is desired.
#
#  Output:
#
#    real VALUE, the L1 norm of C.
#
  value = abs ( c.real ) + abs ( c.imag )

  return value

def c8_norm_l1_test ( ):

#*****************************************************************************80
#
## c8_norm_l1_test() tests c8_norm_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_norm_l1_test' )
  print ( '  c8_norm_l1 computes the L1 norm of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_norm_l1(C1)' )
  print ( '     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_norm_l1 ( c1 )
    print ( '  (%12f,%12f)  %12f' % ( c1.real, c1.imag, r2 ) )

  return

def c8_norm_l2 ( c ):

#*****************************************************************************80
#
## c8_norm_l2() evaluates the L2 norm of a C8.
#
#  Discussion:
#
#    Numbers of equal norm lie along diamonds centered at (0,0).
#
#    The L2 norm can be defined here as:
#
#      c8_norm_l2(X) = aqrt ( ( real (X) ) ^ 2 + abs ( imag (X) ) ^ 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value whose norm is desired.
#
#  Output:
#
#    real VALUE, the L2 norm of C.
#
  import numpy as np

  value = np.sqrt ( ( c.real ) ** 2 + ( c.imag ) ** 2 )

  return value

def c8_norm_l2_test ( ):

#*****************************************************************************80
#
## c8_norm_l2_test() tests c8_norm_l2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_norm_l2_test' )
  print ( '  c8_norm_l2 computes the L2 norm of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_norm_l21(C1)' )
  print ( '     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_norm_l2 ( c1 )
    print ( '  (%12f,%12f)  %12f' % ( c1.real, c1.imag, r2 ) )

  return

def c8_norm_li ( c ):

#*****************************************************************************80
#
## c8_norm_li() evaluates the Loo norm of a C8.
#
#  Discussion:
#
#    Numbers of equal norm lie along diamonds centered at (0,0).
#
#    The Loo norm can be defined here as:
#
#      c8_norm_li(X) = max ( abs ( real (X) ), abs ( imag (X) ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value whose norm is desired.
#
#  Output:
#
#    real VALUE, the Loo norm of C.
#
  value = max ( abs ( c.real ), abs ( c.imag ) )

  return value

def c8_norm_li_test ( ):

#*****************************************************************************80
#
## c8_norm_li_test() tests c8_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_norm_li_test' )
  print ( '  c8_norm_l1 computes the Loo norm of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_norm_li(C1)' )
  print ( '     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_norm_li ( c1 )
    print ( '  (%12f,%12f)  %12f' % ( c1.real, c1.imag, r2 ) )

  return

def c8_one ( ):

#*****************************************************************************80
#
## c8_one() returns the value of one as a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the value of the imaginary unit.
#
  value = 1 + 0j

  return value

def c8_one_test ( ):

#*****************************************************************************80
#
## c8_one_test() tests c8_one().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8_one_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8_one returns the value of one as a C8' )

  c1 = c8_one ( )
  print ( '' )
  print ( '  C1=c8_one ( ) = (%g,%g)' % ( c1.real, c1.imag ) )
  c2 = c1 + c1
  print ( '' )
  print ( '  C2= C1 + C1 = (%g,%g)' % ( c2.real, c2.imag ) )

  return

def c8_print ( a, title ):

#*****************************************************************************80
#
## c8_print() prints a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex A, the value to be printed.
#
#    string TITLE, a title.
#
  print ( '%s  ( %g, %g )' % ( title, a.real, a.imag ) )

  return

def c8_print_test ( ):

#*****************************************************************************80
#
## c8_print_test() tests c8_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_print_test' )
  print ( '  c8_print prints a C8.' )
  print ( '' )

  c1 = 0.0 + 0.0j
  c2 = 1.0 + 0.0j
  c3 = np.pi + 0.0j
  c4 =  0.0 + 1.0j
  c5 = 1.0 + 2.0j
  c6 = -12.34 + 56.78j
  c7 = 0.001 + 0.000002j
  c8 = 3.0E+08 - 4.5E+09j

  c8_print ( c1, '  zero:' )
  c8_print ( c2, '  One:' )
  c8_print ( c3, '  Pi:' )
  c8_print ( c4, '  i:' )
  c8_print ( c5, '  1+2i:' )
  c8_print ( c6, ' -12.34 + 56.78i:' )
  c8_print ( c7, '  1E-3 + 2E-6i' )
  c8_print ( c8, '  3E8 - 4.5E9i:' )

  return

def c8_real ( c ):

#*****************************************************************************80
#
## c8_real() returns the real part of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    real VALUE, the real part of C.
#
  value = c.real

  return value

def c8_real_test ( ):

#*****************************************************************************80
#
## c8_real_test() tests c8_real().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_real_test' )
  print ( '  c8_real computes the real part of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          R2=c8_real(C1)         R3=C1.real' )
  print ( '     ---------------------     ---------------------  ------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2 = c8_real ( c1 )
    r3 = c1.real
    print ( '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 ) )

  return

def c8_sinh ( c ):

#*****************************************************************************80
#
## c8_sinh() evaluates the hyperbolic sine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_sinh ( C ) = ( c8_exp ( C ) - c8_exp ( - C ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value =  ( c8_exp ( c ) - c8_exp ( - c ) ) / 2.0

  return value

def c8_sinh_test ( ):

#*****************************************************************************80
#
## c8_sinh_test() tests c8_sinh().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_sinh_test' )
  print ( '  c8_sinh computes the hyperbolic sine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_sinh(C1)             C3=c8_asinh(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_sinh ( c1 )
    c3 = c8_asinh ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_sin ( c ):

#*****************************************************************************80
#
## c8_sin() evaluates the sine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      c8_sin ( C ) = -i ( c8_exp ( i * C ) - c8_exp ( - i * C ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = - 1j * ( c8_exp ( 1j * c ) - c8_exp ( - 1j * c ) ) / 2.0

  return value

def c8_sin_test ( ):

#*****************************************************************************80
#
## c8_sin_test() tests c8_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_sin_test' )
  print ( '  c8_sin computes the sine of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_sin(C1)             C3=c8_asin(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_sin ( c1 )
    c3 = c8_asin ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_sqrt ( c ):

#*****************************************************************************80
#
## c8_sqrt() returns the principal square root of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the number whose square root is desired.
#
#  Output:
#
#    complex VALUE, the square root of X.
#
  import numpy as np

  argument = c8_arg ( c )
  magnitude = c8_mag ( c );

  value = np.sqrt ( magnitude ) \
    * complex ( np.cos ( argument / 2.0 ), np.sin ( argument / 2.0 ) )

  return value

def c8_sqrt_test ( ):

#*****************************************************************************80
#
## c8_sqrt_test() tests c8_sqrt().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8_sqrt_test' )
  print ( '  c8_sqrt computes the square root of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_sqrt(C1)             C3=C2*C2' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_sqrt ( c1 )
    c3 = c2 * c2;
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_sub ( c1, c2 ):

#*****************************************************************************80
#
## c8_sub() subtracts two C8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C1, C2, the values to subtract.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = c1 - c2

  return value

def c8_sub_test ( ):

#*****************************************************************************80
#
## c8_sub_test() tests c8_sub().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_sub_test' )
  print ( '  c8_sub subtracts two C8s.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_uniform_01          C3=c8_sub(C1,C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_uniform_01 ( )
    c3 = c8_sub ( c1, c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_tanh ( c ):

#*****************************************************************************80
#
## c8_tanh() evaluates the hyperbolic tangent of a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value = ( c8_exp ( c ) - c8_exp ( - c ) ) / ( c8_exp ( c ) + c8_exp ( - c ) )

  return value

def c8_tanh_test ( ):

#*****************************************************************************80
#
## c8_tanh_test() tests c8_tanh().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_tanh_test' )
  print ( '  c8_tanh computes the hyperbolic tangent of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_tanh(C1)             C3=c8_atanh(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_tanh ( c1 )
    c3 = c8_atanh ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_tan ( c ):

#*****************************************************************************80
#
## c8_tan() evaluates the tangent of a C8.
#
#  Discussion:
#
#    We use the relationship:
#
#      c8_tan ( C ) = - i * ( c8_exp ( i * C ) - c8_exp ( - i * C ) ) 
#                         / ( c8_exp ( I * C ) + c8_exp ( - i * C ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the argument.
#
#  Output:
#
#    complex VALUE, the function value.
#
  value =  - 1j * ( c8_exp ( 1j * c ) - c8_exp ( - 1j * c ) ) \
     /            ( c8_exp ( 1j * c ) + c8_exp ( - 1j * c ) )

  return value

def c8_tan_test ( ):

#*****************************************************************************80
#
## c8_tan_test() tests c8_tan().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_tan_test' )
  print ( '  c8_tan computes the tangent of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01          C2=c8_tan(C1)             C3=c8_atan(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    c2 = c8_tan ( c1 )
    c3 = c8_atan ( c2 );
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag ) )

  return

def c8_to_cartesian ( c ):

#*****************************************************************************80
#
## c8_to_cartesian() converts a C8 to cartesian form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value.
#
#  Output:
#
#    real X, Y, the cartesian form.
#
  x = c.real
  y = c.imag

  return x, y

def c8_to_cartesian_test ( ):

#*****************************************************************************80
#
## c8_to_cartesian_test() tests c8_to_cartesian().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_to_cartesian_test' )
  print ( '  c8_to_cartesian computes the cartesian form of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01       (X2,Y2)=c8_to_cartesian(C1)    C3=cartesian_to_c8(X2,Y2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    x2, y2 = c8_to_cartesian ( c1 )
    c3 = cartesian_to_c8 ( x2, y2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( c1.real, c1.imag, x2, y2, c3.real, c3.imag ) )

  return

def c8_to_polar ( c ):

#*****************************************************************************80
#
## c8_to_polar() converts a C8 to polar form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex C, the value.
#
#  Output:
#
#    real R, T, the polar form.
#
  r = c8_mag ( c )
  t = c8_arg ( c )

  return r, t

def c8_to_polar_test ( ):

#*****************************************************************************80
#
## c8_to_polar_test() tests c8_to_polar().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'c8_to_polar_test' )
  print ( '  c8_to_polar computes the polar form of a C8.' )
  print ( '' )
  print ( '       C1=c8_uniform_01       (R2,T2)=c8_to_polar(C1)    C3=polar_to_c8(R2,T2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    c1 = c8_uniform_01 ( )
    r2, t2 = c8_to_polar ( c1 )
    c3 = polar_to_c8 ( r2, t2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( c1.real, c1.imag, r2, t2, c3.real, c3.imag ) )

  return

def c8_uniform_01 ( ):

#*****************************************************************************80
#
## c8_uniform_01() returns a unit pseudorandom C8.
#
#  Discussion:
#
#    The angle should be uniformly distributed between 0 and 2 * PI,
#    the square root of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex C, the pseudorandom complex value.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  r = rng.random ( )
  r = np.sqrt ( r )

  theta = 2.0 * np.pi * rng.random ( )

  c = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c

def c8_uniform_01_test ( ):

#*****************************************************************************80
#
## c8_uniform_01_test() tests c8_uniform_01().
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
  import platform

  print ( '' )
  print ( 'c8_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8_uniform_01 computes pseudorandom complex values' )
  print ( '  in the unit circle.' )
  print ( '' )

  for i in range ( 0, 10 ):
    x = c8_uniform_01 ( )
    print ( '  %6d  ( %g, %g )' % ( i, x.real, x.imag ) )

  return

def c8vec_indicator ( n ):

#*****************************************************************************80
#
## c8vec_indicator() sets a C8VEC to the indicator vector.
#
#  Discussion:
#
#    X(1:N) = ( 1-1i, 2-2i, 3-3i, 4-4i, ... )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#  Output:
#
#    complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    a[i] = float ( i + 1 ) - float ( i + 1 ) * 1j

  return a

def c8vec_indicator_test ( ):

#*****************************************************************************80
#
## c8vec_indicator_test() tests c8vec_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_indicator_test' )
  print ( '  c8vec_indicator returns the indicator vector.' )

  n = 10

  x = c8vec_indicator ( n )

  c8vec_print ( n, x, '  The indicator vector:' )

  return

def c8vec_nint ( n, c ):

#*****************************************************************************80
#
## c8vec_nint() rounds the entries of a C8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values to compute.
#
#    complex C(N), the vector.
#
#  Output:
#
#    complex C(N), the rounded vector.
#
  for i in range ( 0, n ):
    c[i] = c8_nint ( c[i] )

  return c

def c8vec_nint_test ( ):

#*****************************************************************************80
#
## c8vec_nint_test() tests c8vec_nint().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_nint_test' )
  print ( '  c8vec_nint rounds a C8VEC.' )

  n = 5
  c = c8vec_uniform_01 ( n )

  s = 5.0 + 3.0j
  for i in range ( 0, n ):
    c[i] = s * c[i]

  c8vec_print ( n, c, '  The initial vector:' )

  a = c8vec_nint ( n, c )

  c8vec_print ( n, c, '  The rounded vector:' )

  return

def c8vec_norm_l1 ( n, c ):

#*****************************************************************************80
#
## c8vec_norm_l1() returns the L1 norm of a C8VEC.
#
#  Discussion:
#
#    The vector L1 norm is defined as:
#
#      c8vec_norm_l1 =  sum ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    complex C(N), the vector.
#
#  Output:
#
#    real VALUE, the number.
#
  value = 0.0

  for i in range ( 0, n ):
    value = value + abs ( c[i] )

  return value

def c8vec_norm_l1_test ( ):

#*****************************************************************************80
#
## c8vec_norm_l1_test() tests c8vec_norm_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_norm_l1_test' )
  print ( '  c8vec_norm_l1 computes the L1 norm of a C8VEC.' )

  n = 5
  c = c8vec_indicator ( n )

  c8vec_print ( n, c, '  The indicator vector:' )

  value = c8vec_norm_l1 ( n, c )

  print ( '' )
  print ( '  L1 norm = %g' % ( value ) )

  return

def c8vec_norm_l2 ( n, c ):

#*****************************************************************************80
#
## c8vec_norm_l2() returns the L2 norm of a C8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      c8vec_norm_l1 =  sqrt ( sum ( 1 <= I <= N ) abs ( A(I) ) ^ 2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    complex C(N), the vector.
#
#  Output:
#
#    real VALUE, the number.
#
  import numpy as np

  value = 0.0

  for i in range ( 0, n ):
    value = value + ( abs ( c[i] ) ) ** 2
  value = np.sqrt ( value )

  return value

def c8vec_norm_l2_test ( ):

#*****************************************************************************80
#
## c8vec_norm_l2_test() tests c8vec_norm_l2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_norm_l2_test' )
  print ( '  c8vec_norm_l2 computes the L2 norm of a C8VEC.' )

  n = 5
  c = c8vec_indicator ( n )

  c8vec_print ( n, c, '  The indicator vector:' )

  value = c8vec_norm_l2 ( n, c )

  print ( '' )
  print ( '  L2 norm = %g' % ( value ) )

  return

def c8vec_norm_li ( n, c ):

#*****************************************************************************80
#
## c8vec_norm_li() returns the Loo norm of a C8VEC.
#
#  Discussion:
#
#    The vector L1 norm is defined as:
#
#      c8vec_norm_l1 =  max ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    complex C(N), the vector.
#
#  Output:
#
#    real VALUE, the number.
#
  value = 0.0

  for i in range ( 0, n ):
    value = max ( value, abs ( c[i] ) )

  return value

def c8vec_norm_li_test ( ):

#*****************************************************************************80
#
## c8vec_norm_li_test() tests c8vec_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_norm_li_test' )
  print ( '  c8vec_norm_li computes the Loo norm of a C8VEC.' )

  n = 5
  c = c8vec_indicator ( n )

  c8vec_print ( n, c, '  The indicator vector:' )

  value = c8vec_norm_li ( n, c )

  print ( '' )
  print ( '  Loo norm = %g' % ( value ) )

  return

def c8vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## c8vec_print_part() prints "part" of an C8VEC.
#
#  Discussion:
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    complex A(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )
    print ( '  ......  ..............  ..............' )
    i = n - 1
    print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  %14g  ...more entries...' % ( i, a.real[i], a.imag[i] ) )

  return

def c8vec_print_part_test ( ):

#*****************************************************************************80
#
## c8vec_print_part_test() tests c8vec_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_print_part_test' )
  print ( '  c8vec_print_part prints part of a C8VEC.' )

  n = 100
  a = c8vec_indicator ( n )

  max_print = 10

  c8vec_print_part ( n, a, max_print, '  Part of the C8VEC:' )

  return

def c8vec_print ( n, a, title ):

#*****************************************************************************80
#
## c8vec_print() prints a C8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    complex A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] ) )

  return

def c8vec_print_test ( ):

#*****************************************************************************80
#
## c8vec_print_test() tests c8vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8vec_print prints an C8VEC.' )

  n = 4
  v = np.array ( [ complex ( 1.0, 2.0 ), \
                   complex ( 3.0, 4.0 ), \
                   complex ( 5.0, 6.0 ), \
                   complex ( 7.0, 8.0 ) ], dtype = np.complex128 )
  c8vec_print ( n, v, '  Here is a C8VEC:' )

  return

def c8vec_sort_a_l1 ( n, x ):

#*****************************************************************************80
#
## c8vec_sort_a_l1() ascending sorts a C8VEC by L1 norm.
#
#  Discussion:
#
#    The L1 norm of A+Bi is abs(A) + abs(B).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    complex X(N), an unsorted array.
#
#  Output:
#
#    complex X(N), the sorted array.
#
  if ( 1 < n ):

    i = 0
    indx = 0
    isgn = 0
    j = 0
    i_save = 0
    j_save = 0
    k_save = 0
    l_save = 0
    n_save = 0

    while ( True ):

      [ indx, i, j, i_save, j_save, k_save, l_save, n_save ] = sort_safe_rc ( \
        n, indx, isgn, i_save, j_save, k_save, l_save, n_save )

      if ( 0 < indx ):

        temp = x[i-1]
        x[i-1] = x[j-1]
        x[j-1] = temp

      elif ( indx < 0 ):

        if ( c8_le_l1 ( x[i-1], x[j-1] ) ):
          isgn = -1
        else:
          isgn = +1

      elif ( indx == 0 ):

        break

  return x

def c8vec_sort_a_l1_test ( ):

#*****************************************************************************80
#
## c8vec_sort_a_l1_test() tests c8vec_sort_a_l1();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_sort_a_l1_test' )
  print ( '  c8vec_sort_a_l1 sorts a C8VEC by L1 norm.' )

  n = 10
  a = c8vec_uniform_01 (  n )
 
  c8vec_print ( n, a, '  The unsorted vector:' )

  a = c8vec_sort_a_l1 ( n, a )

  print ( '' )
  print ( '   I                  A(I)                   ||A(I)||' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %2d  (%14.6g,%14.6g)  %14.6g' \
      % ( i, a.real[i], a.imag[i], c8_norm_l1 ( a[i] ) ) )

  return

def c8vec_sort_a_l2 ( n, x ):

#*****************************************************************************80
#
## c8vec_sort_a_l2() ascending sorts a C8VEC by L2 norm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    complex X(N), an unsorted array.
#
#  Output:
#
#    complex X(N), the sorted array.
#
  if ( 1 < n ):

    i = 0
    indx = 0
    isgn = 0
    j = 0
    i_save = 0
    j_save = 0
    k_save = 0
    l_save = 0
    n_save = 0

    while ( True ):

      [ indx, i, j, i_save, j_save, k_save, l_save, n_save ] = sort_safe_rc ( \
        n, indx, isgn, i_save, j_save, k_save, l_save, n_save )

      if ( 0 < indx ):

        temp = x[i-1]
        x[i-1] = x[j-1]
        x[j-1] = temp

      elif ( indx < 0 ):

        if ( c8_le_l2 ( x[i-1], x[j-1] ) ):
          isgn = -1
        else:
          isgn = +1

      elif ( indx == 0 ):

        break

  return x

def c8vec_sort_a_l2_test ( ):

#*****************************************************************************80
#
## c8vec_sort_a_l2_test() tests c8vec_sort_a_l2();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_sort_a_l2_test' )
  print ( '  c8vec_sort_a_l2 sorts a C8VEC by L2 norm.' )

  n = 10
  a = c8vec_uniform_01 (  n )
 
  c8vec_print ( n, a, '  The unsorted vector:' )

  a = c8vec_sort_a_l2 ( n, a )

  print ( '' )
  print ( '   I                  A(I)                   ||A(I)||' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %2d  (%14.6g,%14.6g)  %14.6g' \
      % ( i, a.real[i], a.imag[i], c8_norm_l2 ( a[i] ) ) )

  return

def c8vec_sort_a_li ( n, x ):

#*****************************************************************************80
#
## c8vec_sort_a_li() ascending sorts a C8VEC by Loo norm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    complex X(N), an unsorted array.
#
#  Output:
#
#    complex X(N), the sorted array.
#
  if ( 1 < n ):

    i = 0
    indx = 0
    isgn = 0
    j = 0
    i_save = 0
    j_save = 0
    k_save = 0
    l_save = 0
    n_save = 0

    while ( True ):

      [ indx, i, j, i_save, j_save, k_save, l_save, n_save ] = sort_safe_rc ( \
        n, indx, isgn, i_save, j_save, k_save, l_save, n_save )

      if ( 0 < indx ):

        temp = x[i-1]
        x[i-1] = x[j-1]
        x[j-1] = temp

      elif ( indx < 0 ):

        if ( c8_le_li ( x[i-1], x[j-1] ) ):
          isgn = -1
        else:
          isgn = +1

      elif ( indx == 0 ):

        break

  return x

def c8vec_sort_a_li_test ( ):

#*****************************************************************************80
#
## c8vec_sort_a_li_test() tests c8vec_sort_a_li();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_sort_a_li_test' )
  print ( '  c8vec_sort_a_li sorts a C8VEC by Loo norm.' )

  n = 10
  a = c8vec_uniform_01 ( n )
 
  c8vec_print ( n, a, '  The unsorted vector:' )

  a = c8vec_sort_a_li ( n, a )

  print ( '' )
  print ( '   I                  A(I)                   ||A(I)||' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %2d  (%14.6g,%14.6g)  %14.6g' \
      % ( i, a.real[i], a.imag[i], c8_norm_li ( a[i] ) ) )

  return

def c8vec_spiral ( n, m, c1, c2 ):

#*****************************************************************************80
#
## c8vec_spiral() returns N points on a spiral between C1 and C2.
#
#  Discussion:
#
#    A C8VEC is a vector of C8's.
#
#    Let the polar form of C1 be ( R1, T1 ) and the polar form of C2 
#    be ( R2, T2 ) where, if necessary, we increase T2 by 2*PI so that T1 <= T2.
#    
#    Then the polar form of the I-th point C(I) is:
#
#      R(I) = ( ( N - I     ) * R1 
#             + (     I - 1 ) * R2 ) 
#              / ( N    - 1 )
#
#      T(I) = ( ( N - I     ) * T1 
#             + (     I - 1 ) * ( T2 + M * 2 * PI ) ) 
#             / ( N     - 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points on the spiral.
#
#    integer M, the number of full circuits the 
#    spiral makes.
#
#    complex C1, C2, the first and last points 
#    on the spiral.
#
#  Output:
#
#    complex C(N), the points.
#
  import numpy as np

  r1 = np.abs ( c1 )
  r2 = np.abs ( c2 )

  t1 = c8_arg ( c1 )
  t2 = c8_arg ( c2 )

  if ( m == 0 ):

    if ( t2 < t1 ):
      t2 = t2 + 2.0 * np.pi

  elif ( 0 < m ):

    if ( t2 < t1 ):
      t2 = t2 + 2.0 * np.pi

    t2 = t2 + m * 2.0 * np.pi

  elif ( m < 0 ):

    if ( t1 < t2 ):
      t2 = t2 - 2.0 * np.pi

    t2 = t2 - m * 2.0 * np.pi

  c = np.zeros ( n, dtype = np.complex128 )

  for i in range ( 0, n ):

    ri = ( float ( n - i - 1 ) * r1 \
         + float (     i     ) * r2 ) \
         / float ( n     - 1 )

    ti = ( float ( n - i - 1 ) * t1 \
         + float (     i     ) * t2 ) \
         / float ( n     - 1 )

    c[i] = polar_to_c8 ( ri, ti )

  return c

def c8vec_spiral_test ( ):

#*****************************************************************************80
#
## c8vec_spiral_test() tests c8vec_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  n = 13

  print ( '' )
  print ( 'c8vec_spiral_test' )
  print ( '  c8vec_spiral returns N points on a spiral' )
  print ( '  which includes M complete turns.' )

  m = 1
  c1 = 5.0 + 0.0j
  c2 = 3.0 + 0.0j

  c = c8vec_spiral ( n, m, c1, c2 )

  c8vec_print ( n, c, '  The spiral points:' );

  return

def c8vec_uniform_01 ( n ):

#*****************************************************************************80
#
## c8vec_uniform_01() returns a unit pseudorandom C8VEC.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#  Input:
#
#    integer N, the number of values to compute.
#
#  Output:
#
#    complex C(N), the pseudorandom complex vector.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  c = np.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    r = rng.random ( )
    r = np.sqrt ( r )

    theta = 2.0 * np.pi * rng.random ( )

    c[j] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c

def c8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## c8vec_uniform_01_test() tests c8vec_uniform_01().
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
  import platform

  print ( '' )
  print ( 'c8vec_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8vec_uniform_01 computes pseudorandom complex values' )
  print ( '  in the unit circle.' )
  print ( '' )

  n = 10

  x = c8vec_uniform_01 ( n )

  for i in range ( 0, n ):
    print ( '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag ) )

  return

def c8vec_unity ( n ):

#*****************************************************************************80
#
## c8vec_unity() returns the N roots of unity.
#
#  Discussion:
#
#    X(1:N) = exp ( 2 * PI * (0:N-1) / N )
#
#    X(1:N)^N = ( (1,0), (1,0), ..., (1,0) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#  Output:
#
#    complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    t = 2.0 * np.pi * float ( i ) / float ( n )
    a[i] = np.cos ( t ) + 1j * np.sin ( t )

  return a

def c8vec_unity_test ( ):

#*****************************************************************************80
#
## c8vec_unity_test() tests c8vec_unity().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'c8vec_unity_test' )
  print ( '  c8vec_unity returns the N roots of unity.' )

  n = 12

  x = c8vec_unity ( n )

  c8vec_print ( n, x, '  The N roots of unity:' )

  return

def c8_zero ( ):

#*****************************************************************************80
#
## c8_zero() returns the value of zero as a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the value of the imaginary unit.
#
  value = 0 + 0j

  return value

def c8_zero_test ( ):

#*****************************************************************************80
#
## c8_zero_test() tests c8_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8_zero_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8_zero returns the value of zero as a C8' )

  c1 = c8_zero ( )
  print ( '' )
  print ( '  C1=c8_zero ( ) = (%g,%g)' % ( c1.real, c1.imag ) )

  return

def cartesian_to_c8 ( x, y ):

#*****************************************************************************80
#
## cartesian_to_c8() converts cartesian form to a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the cartesian form.
#
#  Output:
#
#    complex C, the value.
#
  import numpy as np

  c = x + 1j * y

  return c

def cartesian_to_c8_test ( ):

#*****************************************************************************80
#
## cartesian_to_c8_test() tests cartesian_to_c8().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'cartesian_to_c8_test' )
  print ( '  cartesian_to_c8 computes the cartesian form of a C8.' )
  print ( '' )
  print ( '     X1,Y1=r8_uniform_01       C2=cartesian_to_c8(X1,Y1)    X3,Y3=c8_to_cartesian(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    x1 = rng.random ( )
    y1 = rng.random ( )
    c2 = cartesian_to_c8 ( x1, y1 )
    x3, y3 = c8_to_cartesian ( c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( x1, y1, c2.real, c2.imag, x3, y3 ) )

  return

def polar_to_c8 ( r, t ):

#*****************************************************************************80
#
## polar_to_c8() converts polar form to a C8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, T, the polar form.
#
#  Output:
#
#    complex C, the value.
#
  import numpy as np

  c = r * ( np.cos ( t ) + 1j * np.sin ( t ) )

  return c

def polar_to_c8_test ( ):

#*****************************************************************************80
#
## polar_to_c8_test() tests polar_to_c8().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'polar_to_c8_test' )
  print ( '  polar_to_c8 computes the polar form of a C8.' )
  print ( '' )
  print ( '     R1,T1=R8_uniform_01       C2=polar_to_c8(R1,T1)    R3,T3=c8_to_polar(C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  for i in range ( 0, 10 ):
    r1 = rng.random ( )
    t1 = rng.random ( )
    t1 = t1 * 2.0 * np.pi
    c2 = polar_to_c8 ( r1, t1 )
    r3, t3 = c8_to_polar ( c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( r1, t1, c2.real, c2.imag, r3, t3 ) )

  return

def sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save ):

#*****************************************************************************80
#
## sort_safe_rc() externally sorts a list of items into ascending order.
#
#  Discussion:
#
#    This is a version of SORT_RC which does not rely on
#    storing certain work variables internally to the function.  This makes
#    the function somewhat more awkward to call, but easier to program
#    in a variety of languages, and safe to use in a parallel programming
#    environment, or in cases where the sorting of several vectors is to
#    be carried out at more or less the same time.
#
#    The actual list of data is not passed to the routine.  Hence this
#    routine may be used to sort integers, reals, numbers, names,
#    dates, shoe sizes, and so on.  After each call, the routine asks
#    the user to compare or interchange two items, until a special
#    return value signals that the sorting is completed.
#
#  Example:
#
#    n = 100
#    indx = 0
#    isgn = 0
#    i_save = 0
#    j_save = 0
#    k_save = 0
#    l_save = 0
#    n_save = 0
#
#    while ( 1 )
#
#      indx, i, j, i_save, j_save, k_save, l_save, n_save = 
#        sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save )
#
#      if ( indx < 0 )
#
#        isgn = 1
#        if ( a(i) <= a(j) )
#          isgn = -1
#        end
#
#      elseif ( 0 < indx )
#
#        k    = a(i)
#        a(i) = a(j)
#        a(j) = k
#
#      else
#
#        break
#
#      end
#
#    end
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    Original FORTRAN77 version by Albert Nijenhuis, Herbert Wilf.
#    This version by John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf.
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of items to be sorted.
#
#    integer INDX, the main communication signal.
#    The user must set INDX to 0 before the first call.
#    Thereafter, the user should set the input value of INDX
#    to the output value from the previous call.
#
#    integer ISGN, results of comparison of elements I and J.
#    (Used only when the previous call returned INDX less than 0).
#    ISGN <= 0 means I is less than or equal to J
#    0 <= ISGN means I is greater than or equal to J.
#
#    integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, workspace 
#    needed by the routine.  Before calling the function,
#    the user should declare variables to hold these values, but should
#    not change them, and need not ever examine them.
#
#  Output:
#
#    integer INDX, the main communication signal.
#    If INDX is
#    * greater than 0, the user should:
#      interchange items I and J
#      call again.
#    * less than 0, the user should:
#      compare items I and J
#      set ISGN = -1 if I < J, ISGN = +1 if J < I
#      call again.
#    * equal to 0, the sorting is done.
#
#    integer I, J, the indices of two items.
#    On return with INDX positive, elements I and J should be interchanged.
#    On return with INDX negative, elements I and J should be compared, and
#    the result reported in ISGN on the next call.
#
#    integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, workspace 
#    needed by the routine.  Before calling the function,
#    the user should declare variables to hold these values, but should
#    not change them, and need not ever examine them.
#

#
#  INDX = 0: This is the first call.
#
  if ( indx == 0 ):
      
    k_save = ( n // 2 )
    l_save = k_save
    n_save = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
  elif ( indx < 0 ):

    if ( indx == -2 ):

      if ( isgn < 0 ):
        i_save = i_save + 1

      j_save = l_save
      l_save = i_save
      indx = -1
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save
 
    if ( 0 < isgn ):
      indx = 2
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    if ( k_save <= 1 ):

      if ( n_save == 1 ):
        i_save = 0
        j_save = 0
        indx = 0
      else:
        i_save = n_save
        n_save = n_save - 1
        j_save = 1
        indx = 1

      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    k_save = k_save - 1
    l_save = k_save
#
#  0 < INDX, the user was asked to make an interchange.
#
  elif ( indx == 1 ):

    l_save = k_save

  while ( True ):

    i_save = 2 * l_save

    if ( i_save == n_save ):
      j_save = l_save
      l_save = i_save
      indx = -1
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save
    elif ( i_save <= n_save ):
      j_save = i_save + 1
      indx = -2
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    if ( k_save <= 1 ):
      break

    k_save = k_save - 1
    l_save = k_save

  if ( n_save == 1 ):
    i_save = 0
    j_save = 0
    indx = 0
    i = i_save
    j = j_save
  else:
    i_save = n_save
    n_save = n_save - 1
    j_save = 1
    indx = 1
    i = i_save
    j = j_save

  return indx, i, j, i_save, j_save, k_save, l_save, n_save

def sort_safe_rc_i4vec_test ( ):

#*****************************************************************************80
#
## sort_safe_rc_i4vec_test() tests sort_safe_rc() on an integer vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 20

  print ( '' )
  print ( 'sort_safe_rc_i4vec_test' )
  print ( '  sort_safe_rc sorts objects externally.' )
  print ( '  This function does not use persistent memory.' )
#
#  Generate some data to sort.
#
  a = rng.integers ( low = 1, high = n, size = n, endpoint = True )
 
  i4vec_print ( n, a, '  Unsorted array:' )
#
#  Sort the data.
#
  indx = 0
  isgn = 0
  i_save = 0
  j_save = 0
  k_save = 0
  l_save = 0
  n_save = 0

  while ( True ):

    indx, i, j, i_save, j_save, k_save, l_save, n_save = \
      sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save )
 
    if ( indx < 0 ):
      isgn = 1
      if ( a[i-1] <= a[j-1] ):
        isgn = -1
    elif ( 0 < indx ):
      k      = a[i-1]
      a[i-1] = a[j-1]
      a[j-1] = k
    else:
      break
#
#  Display the sorted data.
#
  i4vec_print ( n, a, '  Sorted array:' )

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

def timestamp_test ( ):

#*****************************************************************************80
#
## timestamp_test() tests timestamp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'timestamp_test():' )
  print ( '  timestamp() prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  c8lib_test ( )
  timestamp ( )

