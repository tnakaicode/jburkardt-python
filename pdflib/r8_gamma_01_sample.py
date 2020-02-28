#! /usr/bin/env python
#
def r8_gamma_01_sample ( a ):

#*****************************************************************************80
#
## R8_GAMMA_01_SAMPLE samples the standard Gamma distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm GD in the reference.
#
#    pdf ( a x ) = 1/gamma(a) * x^(a-1) * exp ( - x )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Generating Gamma Variates by a Modified Rejection Technique,
#    Communications of the ACM,
#    Volume 25, Number 1, January 1982, pages 47-54.
#
#  Parameters:
#
#    Input, real A, the shape parameter.
#    0.0 < A.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  import numpy as np
  from r8_exponential_01_sample import r8_exponential_01_sample
  from r8_normal_01_sample import r8_normal_01_sample
  from r8_uniform_01_sample import r8_uniform_01_sample

  a1 =  0.3333333
  a2 = -0.2500030
  a3 =  0.2000062
  a4 = -0.1662921
  a5 =  0.1423657
  a6 = -0.1367177
  a7 =  0.1233795

  e1 = 1.0
  e2 = 0.4999897
  e3 = 0.1668290
  e4 = 0.0407753
  e5 = 0.0102930

  q1 =  0.04166669
  q2 =  0.02083148
  q3 =  0.00801191
  q4 =  0.00144121
  q5 = -0.00007388
  q6 =  0.00024511
  q7 =  0.00024240

  sqrt32 = 5.656854

  if ( 1.0 <= a ):

    s2 = a - 0.5
    s = np.sqrt ( s2 )
    d = sqrt32 - 12.0 * s
#
#  Immediate acceptance.
#
    t = r8_normal_01_sample ( )
    x = s + 0.5 * t
    value = x * x

    if ( 0.0 <= t ):
      return value
#
#  Squeeze acceptance.
#
    u = r8_uniform_01_sample ( )

    if ( d * u <= t * t * t ):
      return value

    r = 1.0 / a
    q0 = (((((( q7 \
      * r + q6 ) \
      * r + q5 ) \
      * r + q4 ) \
      * r + q3 ) \
      * r + q2 ) \
      * r + q1 ) \
      * r
#
#  Approximation depending on size of parameter A.
#
    if ( 13.022 < a ):
      b = 1.77
      si = 0.75
      c = 0.1515 / s
    elif ( 3.686 < a ):
      b = 1.654 + 0.0076 * s2
      si = 1.68 / s + 0.275
      c = 0.062 / s + 0.024
    else:
      b = 0.463 + s + 0.178 * s2
      si = 1.235
      c = 0.195 / s - 0.079 + 0.16 * s
#
#  Quotient test.
#
    if ( 0.0 < x ):

      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * (((((( a7 \
          * v + a6 ) \
          * v + a5 ) \
          * v + a4 ) \
          * v + a3 ) \
          * v + a2 ) \
          * v + a1 ) \
          * v

      if ( np.log ( 1.0 - u ) <= q ):
        return value

    while ( True ):

      e = r8_exponential_01_sample ( )
      u = 2.0 * r8_uniform_01_sample ( ) - 1.0

      if ( 0.0 <= u ):
        t = b + abs ( si * e )
      else:
        t = b - abs ( si * e )
#
#  Possible rejection.
#
      if ( t < -0.7187449 ):
        continue
#
#  Calculate V and quotient Q.
#
      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * (((((( a7 \
          * v + a6 ) \
          * v + a5 ) \
          * v + a4 ) \
          * v + a3 ) \
          * v + a2 ) \
          * v + a1 ) \
          * v
#
#  Hat acceptance.
#
      if ( q <= 0.0 ):
        continue

      if ( 0.5 < q ):
        w = np.exp ( q ) - 1.0
      else:
        w = (((( e5 * q + e4 ) * q + e3 ) * q + e2 ) * q + e1 ) * q
#
#  May have to sample again.
#
      if ( c * abs ( u ) <= w * np.exp ( e - 0.5 * t * t ) ):
        break

    x = s + 0.5 * t
    value = x * x

    return value
#
#  Method for A < 1.
#
  else:

    b = 1.0 + 0.3678794 * a

    while ( True ):

      p = b * r8_uniform_01_sample ( )

      if ( p < 1.0 ):

        value = np.exp ( np.log ( p ) / a )

        if ( value <= r8_exponential_01_sample ( ) ):
          return value

        continue

      value = - np.log ( ( b - p ) / a )

      if ( ( 1.0 - a ) * np.log ( value ) <= r8_exponential_01_sample ( ) ):
        break

  return value

def r8_gamma_01_sample_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_01_SAMPLE_TEST tests R8_GAMMA_01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_gamma_01_pdf import r8_gamma_01_pdf
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'R8_GAMMA_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_01_SAMPLE samples the standard gamma distribution.' )

  print ( '' )
  print ( '            A                X       PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    a, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    x = r8_gamma_01_sample ( a )
    pdf = r8_gamma_01_pdf ( a, x )
    print ( '  %14.6g  %14.6g  %14.6g' % ( a, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_01_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize()
  timestamp ( )
  r8_gamma_01_sample_test ( )
  timestamp ( )

