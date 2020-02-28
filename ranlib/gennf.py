#! /usr/bin/env python
#
def gennf ( dfn, dfd, xnonc ):

#*****************************************************************************80
#
## GENNF generates a noncentral F random deviate.
#
#  Discussion:
#
#    This procedure generates a random deviate from the noncentral F
#    (variance ratio) distribution with DFN degrees of freedom in the
#    numerator, and DFD degrees of freedom in the denominator, and
#    noncentrality parameter XNONC.
#
#    It directly generates the ratio of noncentral numerator chisquare variate
#    to central denominator chisquare variate.
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
#    Input, real DFN, the numerator degrees of freedom.
#    1.0 < DFN.
#
#    Input, real DFD, the denominator degrees of freedom.
#    0.0 < DFD.
#
#    Input, real XNONC, the noncentrality parameter.
#    0.0 <= XNONC.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  from genchi import genchi
  from gennch import gennch
  from sys import exit

  if ( dfn <= 1.0 ):
    print ( '' )
    print ( 'GENNF - Fatal error!' )
    print ( '  DFN <= 1.0' )
    exit ( 'GENNF - Fatal error!' )

  if ( dfd <= 0.0 ):
    print ( '' )
    print ( 'GENNF - Fatal error!' )
    print ( '  DFD <= 0.0' )
    exit ( 'GENNF - Fatal error!' )

  if ( xnonc < 0.0 ):
    print ( '' )
    print ( 'GENNF - Fatal error!' )
    print ( '  XNONC < 0.0' )
    exit ( 'GENNF - Fatal error!' )

  xnum = gennch ( dfn, xnonc ) / dfn
  xden = genchi ( dfd ) / dfd

  value = xnum / xden

  return value

def gennf_test ( phrase ):

#*****************************************************************************80
#
## GENNF_TEST tests GENNF, which generates noncentral F deviates.
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
  from genunf import genunf
  from initialize import initialize
  from phrtsd import phrtsd
  from set_initial_seed import set_initial_seed
  from stats import stats
  from trstat import trstat

  n = 10000

  print ( '' )
  print ( 'GENNF_TEST' )
  print ( '  GENNF generates noncentral F deviates.' )
#
#  Initialize the generators.
#
  initialize ( )
#
#  Set the seeds based on the phrase.
#
  seed1, seed2 = phrtsd ( phrase )
#
#  Initialize all generators.
#
  set_initial_seed ( seed1, seed2 )
#
#  Select the parameters at random within a given range.
#
  low = 3.0
  high = 10.0
  dfn = genunf ( low, high )

  low = 5.0
  high = 10.0
  dfd = genunf ( low, high )

  low = 0.0
  high = 2.0
  xnonc = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  DFN =   %g' % ( dfn ) )
  print ( '  DFD =   %g' % ( dfd ) )
  print ( '  XNONC = %g' % ( xnonc ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = gennf ( dfn, dfd, xnonc )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'nf'
  param = np.array ( [ dfn, dfd, xnonc ] )

  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENNF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  gennf_test ( phrase )
  timestamp ( )

