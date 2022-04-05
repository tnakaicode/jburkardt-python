#! /usr/bin/env python
#
def r8_normal_sample ( av, sd ):

#*****************************************************************************80
#
## R8_NORMAL_SAMPLE generates a normal random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a normal distribution
#    with mean AV, and standard deviation SD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Extensions of Forsythe's Method for Random
#    Sampling from the Normal Distribution,
#    Mathematics of Computation,
#    Volume 27, Number 124, October 1973, page 927-937.
#
#  Parameters:
#
#    Input, real AV, the mean.
#
#    Input, real SD, the standard deviation.
#
#    Output, real VALUE, a random deviate 
#    from the distribution.
#
  from r8_normal_01_sample import r8_normal_01_sample

  value = sd * r8_normal_01_sample ( ) + av

  return value

def r8_normal_sample_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_SAMPLE_TEST tests R8_NORMAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_normal_pdf import r8_normal_pdf
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'R8_NORMAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NORMAL_SAMPLE samples the normal distribution.' )

  print ( '' )
  print ( '            MU            SIGMA            X       PDF(MU,SIGMA)' )
  print ( '' )

  for i in range ( 0, 10 ):
    mu, seed = r8_uniform_ab ( -100.0, +100.0, seed )
    sigma, seed = r8_uniform_ab ( 0.0, 1.0, seed )
    x = r8_normal_sample ( mu, sigma )
    pdf = r8_normal_pdf ( mu, sigma, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( mu, sigma, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NORMAL_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize()
  timestamp ( )
  r8_normal_sample_test ( )
  timestamp ( )

