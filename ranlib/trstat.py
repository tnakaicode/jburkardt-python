#! /usr/bin/env python
#
def trstat ( pdf, parin ):

#*****************************************************************************80
#
## TRSTAT returns the mean and variance for distributions.
#
#  Discussion:
#
#    This procedure returns the mean and variance for a number of statistical
#    distributions as a function of their parameters.
#
#    The input vector PARIN is used to pass in the parameters necessary
#    to specify the distribution.  The number of these parameters varies
#    per distribution, and it is necessary to specify an ordering for the
#    parameters used to a given distribution.  The ordering chosen here
#    is as follows:
#
#    bet
#      PARIN[0] is A
#      PARIN[1] is B
#    bin
#      PARIN[0] is Number of trials
#      PARIN[1] is Prob Event at Each Trial
#    chi
#      PARIN[0] = df
#    exp
#      PARIN[0] = mu
#    f
#      PARIN[0] is df numerator
#      PARIN[1] is df denominator
#    gam
#      PARIN[0] is A
#      PARIN[1] is R
#    nbn
#      PARIN[0] is N
#      PARIN[1] is P
#    nch
#      PARIN[0] is df
#      PARIN[1] is noncentrality parameter
#    nf
#      PARIN[0] is df numerator
#      PARIN[1] is df denominator
#      PARIN[2] is noncentrality parameter
#    nor
#      PARIN[0] is mean
#      PARIN[1] is standard deviation
#    poi
#      PARIN[0] is Mean
#    unf
#      PARIN[0] is LOW bound
#      PARIN[1] is HIGH bound
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, string PDF, indicates the distribution:
#    'bet'  beta distribution
#    'bin'  binomial
#    'chi'  chisquare
#    'exp'  exponential
#    'f'    F (variance ratio)
#    'gam'  gamma
#    'nbn'  negative binomial
#    'nch'  noncentral chisquare
#    'nf'   noncentral f
#    'nor'  normal
#    'poi'  Poisson
#    'unf'  uniform
#
#    Input, real PARIN(*), the parameters of the distribution.
#
#    Output, real AV, the mean of the specified distribution.
#
#    Output, real VAR, the variance of the specified distribuion.
#
  from sys import exit

  if ( pdf.lower() == 'bet' ):

    av = parin[0] / ( parin[0] + parin[1] )
    var = ( av * parin[1] ) / ( ( parin[0] + parin[1] ) * \
      ( parin[0] + parin[1] + 1.0 ) )

  elif ( pdf.lower() == 'bin' ):

    n = int ( parin[0] )
    p = parin[1]
    av = n * p
    var = n * p * ( 1.0 - p )

  elif ( pdf.lower() == 'chi' ):

    av = parin[0]
    var = 2.0 * parin[0]

  elif ( pdf.lower() == 'exp' ):

    av = parin[0]
    var = av ** 2

  elif ( pdf.lower() == 'f' ):

    if ( parin[1] <= 2.0001 ):
      av = -1.0
    else:
      av = parin[1] / ( parin[1] - 2.0 )

    if ( parin[1] <= 4.0001 ):
      var = -1.0
    else:
      var = ( 2.0 * parin[1] ** 2 * ( parin[0] + parin[1] - 2.0 ) ) / \
        ( parin[0] * ( parin[1] - 2.0 ) ** 2 * ( parin[1] - 4.0 ) )

  elif ( pdf.lower() == 'gam' ):

    a = parin[0]
    r = parin[1]
    av = r / a
    var = r / a ** 2

  elif ( pdf.lower() == 'nbn' ):

    n = int ( parin[0] )
    p = parin[1]
    av = n * ( 1.0 - p ) / p
    var = n * ( 1.0 - p ) / p ** 2

  elif ( pdf.lower() == 'nch' ):

    a = parin[0] + parin[1]
    b = parin[1] / a
    av = a
    var = 2.0 * a * ( 1.0 + b )

  elif ( pdf.lower() == 'nf' ):

    if ( parin[1] <= 2.0001 ):
      av = -1.0
    else:
      av = ( parin[1] * ( parin[0] + parin[2] ) ) \
        / ( ( parin[1] - 2.0 ) * parin[0] )

    if ( parin[1] <= 4.0001 ):
      var = -1.0
    else:
      a = ( parin[0] + parin[2] ) ** 2 \
        + ( parin[0] + 2.0 * parin[2] ) * ( parin[1] - 2.0 )
      b = ( parin[1] - 2.0 ) ** 2 * ( parin[1] - 4.0 )
      var = 2.0 * ( parin[1] / parin[0] ) ** 2 * ( a / b )

  elif ( pdf.lower() == 'nor' ):

    av = parin[0]
    var = parin[1] ** 2

  elif ( pdf.lower() == 'poi' ):

    av = parin[0]
    var = parin[0]

  elif ( pdf.lower() == 'unf' ):

    width = parin[1] - parin[0]
    av = parin[0] + width / 2.0
    var = width ** 2 / 12.0

  else:

    print ( '' )
    print ( 'TRSTAT - Fatal error!' )
    print ( '  Illegal input value for PDF.' )
    exit ( 'TRSTAT - Fatal error!' )

  return av, var

def trstat_test ( ):

#*****************************************************************************80
#
## TRSTAT_TEST tests TRSTAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TRSTAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRSTAT returns the mean and variance for distributions.' )

  pdf = 'unf'
  a = 10.0
  b = 20.0
  param = np.array ( [ a, b ] )
  avtr, vartr = trstat ( pdf, param )
  print ( '' );
  print ( '  Distribution: "%s"' % ( pdf ) )
  print ( '  Distribution parameters:    %14.6g  %14.6g' % ( a, b ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRSTAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  trstat_test ( )
  timestamp ( )


