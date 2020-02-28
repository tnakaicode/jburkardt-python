#! /usr/bin/env python
#
def gennor ( av, sd ):

#*****************************************************************************80
#
## GENNOR generates a normal random deviate.
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
#    Output, real VALUE, a random deviate from the distribution.
#
  from snorm import snorm

  value = sd * snorm ( ) + av

  return value

def gennor_test ( phrase ):

#*****************************************************************************80
#
## RANLIB_TEST_GENNOR tests GENNOR, which generates normal deviates.
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
  print ( 'GENNOR_TEST:' )
  print ( '  GENNOR generates normal deviates.' )
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
  low = -10.0
  high = 10.0
  mu = genunf ( low, high )

  low = 0.25
  high = 4.0
  sd = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  MU =   %g' % ( mu ) )
  print ( '  SD =   %g' % ( sd ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = gennor ( mu, sd )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'nor'
  param = np.array ( [ mu, sd ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENNOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  gennor_test ( phrase )
  timestamp ( )

