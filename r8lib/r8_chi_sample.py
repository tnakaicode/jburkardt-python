#! /usr/bin/env python
#
def r8_chi_sample ( df ):

#*****************************************************************************80
#
## R8_CHI_SAMPLE generates a Chi-Square random deviate.
#
#  Discussion:
#
#    This procedure generates a random deviate from the chi square distribution
#    with DF degrees of freedom random variable.
#
#    The algorithm exploits the relation between chisquare and gamma.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real DF, the degrees of freedom.
#    0.0 < DF.
#
#    Output, real VALUE, a random deviate 
#    from the distribution.
#
  from r8_gamma_sample import r8_gamma_sample
  from sys import exit

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'R8_CHI_SAMPLE - Fatal error!' )
    print ( '  DF <= 0.' )
    print ( '  Value of DF: %g' % ( df ) )
    exit ( 'R8_BETA_PDF - Fatal error!' )

  arg1 = 1.0
  arg2 = df / 2.0

  value = 2.0 * r8_gamma_sample ( arg1, arg2 )

  return value

def r8_chi_sample_test ( ):

#*****************************************************************************80
#
## R8_CHI_SAMPLE_TEST tests R8_CHI_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab
  from r8_chi_pdf import r8_chi_pdf

  print ( '' )
  print ( 'R8_CHI_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHI_SAMPLE samples the CHI distribution:' )
  print ( '' )
  print ( '           DF              R              PDF' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    df, seed = r8_uniform_ab ( 0.0, +20.0, seed )
    r = r8_chi_sample ( df )
    pdf = r8_chi_pdf ( df, r )
    print ( '  %14.6g  %14.6g  %14.6g' % ( df, r, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHI_SAMPLE_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  timestamp ( )
  initialize ( )
  r8_chi_sample_test ( )
  timestamp ( )
