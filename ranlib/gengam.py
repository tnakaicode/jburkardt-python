#! /usr/bin/env python
#
def gengam ( a, r ):

#*****************************************************************************80
#
## GENGAM generates a Gamma random deviate.
#
#  Discussion:
#
#    This procedure generates random deviates from the gamma distribution whose
#    density is (A^R)/Gamma(R) * X^(R-1) * Exp(-A*X)
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
#    Input, real A, the location parameter.
#
#    Input, real R, the shape parameter.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  from sgamma import sgamma

  value = sgamma ( r ) / a

  return value

def gengam_test ( phrase ):

#*****************************************************************************80
#
## GENGAM_TEST tests GENGAM, which generates Gamma deviates.
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

  n = 1000

  print ( '' )
  print ( 'GENGAM_TEST' )
  print ( '  GENGAM generates Gamma deviates.' )
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
  low = 1.0
  high = 10.0
  a = genunf ( low, high )

  low = 1.0
  high = 10.0
  r = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  A = %g' % ( a ) )
  print ( '  R = %g' % ( r ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = gengam ( a, r )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'gam'
  param = np.array ( [ a, r ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENGAM_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  gengam_test ( phrase )
  timestamp ( )

