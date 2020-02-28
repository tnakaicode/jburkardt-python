#! /usr/bin/env python
#
def r8_invgam_sample ( beta, alpha ):

#*****************************************************************************80
#
## R8_INVGAM_SAMPLE samples an inverse gamma distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real BETA, the rate parameter.
#    0.0 < BETA.
#
#    Input, real ALPHA, the shape parameter.
#    0.0 < ALPHA.
#
#    Output, real VALUE, a sample value.
#
  from r8_gamma_sample import r8_gamma_sample

  value = r8_gamma_sample ( beta, alpha )

  if ( value != 0.0 ):
    value = 1.0 / value

  return value

def r8_invgam_sample_test ( ):

#*****************************************************************************80
#
## R8_INVGAM_SAMPLE_TEST tests R8_INVGAM_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_invgam_pdf import r8_invgam_pdf
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'R8_INVGAM_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_INVGAM_SAMPLE samples an inverse gamma distribution.' )

  print ( '' )
  print ( '           R               A               X              PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    a, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    x = r8_invgam_sample ( r, a )
    pdf = r8_invgam_pdf ( r, a, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( r, a, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_INVGAM_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize()
  timestamp ( )
  r8_invgam_sample_test ( )
  timestamp ( )

