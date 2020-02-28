#! /usr/bin/env python
#
def jacobi_integral ( expon, alpha, beta ):

#*****************************************************************************80
#
## JACOBI_INTEGRAL evaluates the integral of a monomial with Jacobi weight.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) x^EXPON (1-x)^ALPHA (1+x)^BETA dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer EXPON, the exponent.
#
#    Input, real ALPHA, the exponent of (1-X) in the weight factor.
#
#    Input, real BETA, the exponent of (1+X) in the weight factor.
#
#    Output, real VALUE, the value of the integral.
#
  from r8_gamma import r8_gamma
  from r8_hyper_2f1 import r8_hyper_2f1

  c = expon

  if ( ( expon % 2 ) == 0 ):
    s = +1.0
  else:
    s = -1.0

  arg1 = - alpha
  arg2 =   1.0 + c
  arg3 =   2.0 + beta + c
  arg4 = - 1.0

  value1 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  arg1 = - beta
  arg2 =   1.0 + c
  arg3 =   2.0 + alpha + c
  arg4 = - 1.0

  value2 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  value = r8_gamma ( 1.0 + c ) * ( \
      s * r8_gamma ( 1.0 + beta  ) * value1 / r8_gamma ( 2.0 + beta  + c ) \
    +     r8_gamma ( 1.0 + alpha ) * value2 / r8_gamma ( 2.0 + alpha + c ) )

  return value

def jacobi_integral_test ( ):

#*****************************************************************************80
#
## JACOBI_INTEGRAL_TEST tests JACOBI_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  alpha = 1.5
  beta = 0.5

  print ( '' )
  print ( 'JACOBI_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JACOBI_INTEGRAL evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n (1-x)^alpha (1+x)^beta dx' )
  print ( '' )
  print ( '  Use ALPHA = %g' % ( alpha ) )
  print ( '      BETA =  %g' % ( beta ) )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = jacobi_integral ( n, alpha, beta )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JACOBI_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  jacobi_integral_test ( )
  timestamp ( )

