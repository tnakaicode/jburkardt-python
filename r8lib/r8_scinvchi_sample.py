#! /usr/bin/env python
#
def r8_scinvchi_sample ( df, s ):

#*****************************************************************************80
#
## R8_SCINVCHI_SAMPLE: sample a scaled inverse chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real DF, the degrees of freedom.
#    0.0 < DF.
#
#    Input, real S, the scale factor.
#    0.0 < S.
#
#    Input, real VALUE, a sample value.
#
  from r8_gamma_sample import r8_gamma_sample

  a = 0.5 * df * s
  b = 0.5 * df

  value = r8_gamma_sample ( a, b )

  if ( value != 0.0 ):
    value = 1.0 / value

  return value

def r8_scinvchi_sample_test ( ):

#*****************************************************************************80
#
## R8_SCINVCHI_SAMPLE_TEST tests R8_SCINVCHI_SAMPLE.
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
  from r8_scinvchi_pdf import r8_scinvchi_pdf
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'R8_SCINVCHI_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SCINVCHI_SAMPLE samples a scaled inverse chi square distribution.' )
  print ( '' )
  print ( '           DF              XI               X              PDF' )
  print ( '' )

  for i in range ( 0, 10 ):
    df, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    xi, seed = r8_uniform_ab ( 0.0, 5.0, seed )
    x = r8_scinvchi_sample ( df, xi )
    pdf = r8_scinvchi_pdf ( df, xi, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( df, xi, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SCINVCHI_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize()
  timestamp ( )
  r8_scinvchi_sample_test ( )
  timestamp ( )

