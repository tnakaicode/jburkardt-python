#! /usr/bin/env python
#
def genexp ( av ):

#*****************************************************************************80
#
## GENEXP generates an exponential random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from an exponential
#    distribution with mean AV.
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
#    Computer Methods for Sampling From the
#    Exponential and Normal Distributions,
#    Communications of the ACM,
#    Volume 15, Number 10, October 1972, pages 873-882.
#
#  Parameters:
#
#    Input, real AV, the mean of the exponential distribution
#    from which a random deviate is to be generated.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  from sexpo import sexpo

  value = sexpo ( ) * av

  return value

def genexp_test ( phrase ):

#*****************************************************************************80
#
## GENEXP_TEST tests GENEXP, which generates exponential deviates.
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
  print ( 'GENEXP_TEST' )
  print ( '  GENEXP generates exponential deviates.' )
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
  low =  0.5
  high = 10.0
  mu = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  MU =   %g' % ( mu ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = genexp ( mu )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'exp'
  param = np.array ( [ mu ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENEXP_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  genexp_test ( phrase )
  timestamp ( )

