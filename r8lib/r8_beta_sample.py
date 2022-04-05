#! /usr/bin/env python
#
def r8_beta_sample ( aa, bb ):

#*****************************************************************************80
#
## R8_BETA_SAMPLE generates a beta random deviate.
#
#  Discussion:
#
#    This procedure returns a single random deviate from the beta distribution
#    with parameters A and B.  The density is
#
#      x^(a-1) * (1-x)^(b-1) / Beta(a,b) for 0 < x < 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Russell Cheng,
#    Generating Beta Variates with Nonintegral Shape Parameters,
#    Communications of the ACM,
#    Volume 21, Number 4, April 1978, pages 317-322.
#
#  Parameters:
#
#    Input, real AA, the first parameter of the beta distribution.
#    0.0 < AA.
#
#    Input, real BB, the second parameter of the beta distribution.
#    0.0 < BB.
#
#    Output, real VALUE, a random deviate 
#    from the distribution.
#
  import numpy as np
  from r8_uniform_01_sample import r8_uniform_01_sample
  from sys import exit

  if ( aa <= 0.0 ):
    print ( '' )
    print ( 'R8_BETA_SAMPLE - Fatal error!' )
    print ( '  AA <= 0.0' )
    exit ( 'R8_BETA_SAMPLE - Fatal error!\n' )

  if ( bb <= 0.0 ):
    print ( '' )
    print ( 'R8_BETA_SAMPLE - Fatal error!' )
    print ( '  BB <= 0.0' )
    exit ( 'R8_BETA_SAMPLE - Fatal error!\n' )
#
#  Algorithm BB
#
  if ( 1.0 < aa and 1.0 < bb ):

    a = min ( aa, bb )
    b = max ( aa, bb )
    alpha = a + b
    beta = np.sqrt ( ( alpha - 2.0 ) / ( 2.0 * a * b - alpha ) )
    gamma = a + 1.0 / beta

    while ( True ):

      u1 = r8_uniform_01_sample ( );
      u2 = r8_uniform_01_sample ( );
      v = beta * np.log ( u1 / ( 1.0 - u1 ) )
      w = a * np.exp ( v )

      z = u1 ** 2 * u2;
      r = gamma * v - np.log ( 4.0 )
      s = a + r - w

      if ( 5.0 * z <= s + 1.0 + np.log ( 5.0 ) ):
        break

      t = np.log ( z )

      if ( t <= s ):
        break

      if ( t <= ( r + alpha * np.log ( alpha / ( b + w ) ) ) ):
        break
#
#  Algorithm BC
#
  else:

    a = max ( aa, bb )
    b = min ( aa, bb )
    alpha = a + b
    beta = 1.0 / b
    delta = 1.0 + a - b

    k1 = delta * ( 1.0 / 72.0 + b / 24.0 ) / ( a / b - 7.0 / 9.0 )
    k2 = 0.25 + ( 0.5 + 0.25 / delta ) * b

    while ( True ):

      u1 = r8_uniform_01_sample ( )
      u2 = r8_uniform_01_sample ( );

      if ( u1 < 0.5 ):

        y = u1 * u2
        z = u1 * y

        if ( k1 <= 0.25 * u2 + z - y ):
          continue

      else:

        z = u1 ** 2 * u2

        if ( z <= 0.25 ):

          v = beta * np.log ( u1 / ( 1.0 - u1 ) )
          w = a * np.exp ( v )

          if ( aa == a ):
            value = w / ( b + w )
          else:
            value = b / ( b + w );

          return value

        if ( k2 < z ):
          continue

      v = beta * np.log ( u1 / ( 1.0 - u1 ) )
      w = a * np.exp ( v )

      if ( np.log ( z ) <= alpha * ( np.log ( alpha / ( b + w ) ) + v ) - np.log ( 4.0 ) ):
        break

  if ( aa == a ):
    value = w / ( b + w )
  else:
    value = b / ( b + w )

  return value

def r8_beta_sample_test ( ):

#*****************************************************************************80
#
## R8_BETA_SAMPLE_TEST tests R8_BETA_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_beta_pdf import r8_beta_pdf
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'R8_BETA_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_BETA_SAMPLE samples the beta distribution.' )

  print ( '' )
  print ( '            ALPHA        BETA             X       PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    alpha, seed = r8_uniform_ab ( 0.0, +5.0, seed )
    beta, seed = r8_uniform_ab ( 0.0, +5.0, seed )
    x = r8_beta_sample ( alpha, beta )
    pdf = r8_beta_pdf ( alpha, beta, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( alpha, beta, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_BETA_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize()
  timestamp ( )
  r8_beta_sample_test ( )
  timestamp ( )

