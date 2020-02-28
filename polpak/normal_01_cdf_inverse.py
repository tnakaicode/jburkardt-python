#! /usr/bin/env python
#
def normal_01_cdf_inverse ( p ):

#*****************************************************************************80
#
## NORMAL_01_CDF_INVERSE inverts the standard normal CDF.
#
#  Discussion:
#
#    The result is accurate to about 1 part in 10^16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by Michael Wichura.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Michael Wichura,
#    The Percentage Points of the Normal Distribution,
#    Algorithm AS 241,
#    Applied Statistics,
#    Volume 37, Number 3, pages 477-484, 1988.
#
#  Parameters:
#
#    Input, real P, the value of the cumulative probability 
#    densitity function.  0 < P < 1.  If P is not in this range, an "infinite"
#    result is returned.
#
#    Output, real VALUE, the normal deviate value with the 
#    property that the probability of a standard normal deviate being 
#    less than or equal to the value is P.
#
  import numpy as np
  from r8_huge import r8_huge
  from r8poly_value_horner import r8poly_value_horner

  a = np.array ( (\
        3.3871328727963666080,      1.3314166789178437745e+2, \
        1.9715909503065514427e+3,   1.3731693765509461125e+4, \
        4.5921953931549871457e+4,   6.7265770927008700853e+4, \
        3.3430575583588128105e+4,   2.5090809287301226727e+3 ))

  b = np.array ( (\
        1.0,                        4.2313330701600911252e+1, \
        6.8718700749205790830e+2,   5.3941960214247511077e+3, \
        2.1213794301586595867e+4,   3.9307895800092710610e+4, \
        2.8729085735721942674e+4,   5.2264952788528545610e+3 ))

  c = np.array ( (\
        1.42343711074968357734,     4.63033784615654529590, \
        5.76949722146069140550,     3.64784832476320460504, \
        1.27045825245236838258,     2.41780725177450611770e-1, \
        2.27238449892691845833e-2,  7.74545014278341407640e-4 ))

  const1 = 0.180625

  const2 = 1.6

  d = np.array ( (\
        1.0,                        2.05319162663775882187,    \
        1.67638483018380384940,     6.89767334985100004550e-1, \
        1.48103976427480074590e-1,  1.51986665636164571966e-2, \
        5.47593808499534494600e-4,  1.05075007164441684324e-9 ))

  e = np.array ( (\
        6.65790464350110377720,     5.46378491116411436990,    \
        1.78482653991729133580,     2.96560571828504891230e-1, \
        2.65321895265761230930e-2,  1.24266094738807843860e-3, \
        2.71155556874348757815e-5,  2.01033439929228813265e-7 ))

  f = np.array ( (\
        1.0,               5.99832206555887937690e-1, \
        1.36929880922735805310e-1,  1.48753612908506148525e-2, \
        7.86869131145613259100e-4,  1.84631831751005468180e-5, \
        1.42151175831644588870e-7,  2.04426310338993978564e-15 ))

  split1 = 0.425
  split2 = 5.0

  if ( p <= 0.0 ):
    value = - r8_huge ( )
    return value
 
  if ( 1.0 <= p ):
    value = r8_huge ( )
    return value

  q = p - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r8poly_value_horner ( 7, a, r ) \
              / r8poly_value_horner ( 7, b, r )

  else:

    if ( q < 0.0 ):
      r = p
    else:
      r = 1.0 - p

    if ( r <= 0.0 ):

      value = r8_huge ( )

    else:

      r = np.sqrt ( - np.log ( r ) )

      if ( r <= split2 ):

        r = r - const2
        value = r8poly_value_horner ( 7, c, r ) \
              / r8poly_value_horner ( 7, d, r )

      else:

        r = r - split2
        value = r8poly_value_horner ( 7, e, r ) \
              / r8poly_value_horner ( 7, f, r )

    if ( q < 0.0 ):
      value = - value

  return value

def normal_01_cdf_inverse_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_INVERSE_TEST tests NORMAL_01_CDF_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from normal_01_cdf_values import normal_01_cdf_values

  print ( '' )
  print ( 'NORMAL_01_CDF_INVERSE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF_INVERSE inverts the error function.' )
  print ( '' )
  print ( '       FX                       X         NORMAL_01_CDF_INVERSE(FX)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x1, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = normal_01_cdf_inverse ( fx )

    print ( '  %12g  %24.16g  %24.16g' % ( fx, x1, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_INVERSE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  normal_01_cdf_inverse_test ( )
  timestamp ( )
