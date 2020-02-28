#! /usr/bin/env python
#
def r8_gamma_sample ( r, a ):

#*****************************************************************************80
#
## R8_GAMMA_SAMPLE generates a Gamma random deviate.
#
#  Discussion:
#
#    This procedure generates random deviates from the gamma distribution whose
#    density is (R^A)/Gamma(A) * X^(A-1) * Exp(-R*X)
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
#    John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Generating Gamma Variates by a Modified Rejection Technique,
#    Communications of the ACM,
#    Volume 25, Number 1, January 1982, pages 47-54.
#
#    Joachim Ahrens, Ulrich Dieter,
#    Computer Methods for Sampling from Gamma, Beta, Poisson and
#    Binomial Distributions,
#    Computing,
#    Volume 12, Number 3, September 1974, pages 223-246.
#
#  Parameters:
#
#    Input, real R, the rate parameter.
#    A nonzero.
#
#    Input, real A, the shape parameter.
#    0 < A.
#
#    Output, real VALUE, a random deviate 
#    from the distribution.
#
  from r8_gamma_01_sample import r8_gamma_01_sample

  value = r8_gamma_01_sample ( a ) / r

  return value

def r8_gamma_sample_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_SAMPLE_TEST tests R8_GAMMA_SAMPLE.
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
  from r8_gamma_pdf import r8_gamma_pdf
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'R8_GAMMA_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_SAMPLE samples a gamma distribution.' )

  print ( '' )
  print ( '           R               A               X              PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    a, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    x = r8_gamma_sample ( r, a )
    pdf = r8_gamma_pdf ( r, a, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( r, a, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize()
  timestamp ( )
  r8_gamma_sample_test ( )
  timestamp ( )

