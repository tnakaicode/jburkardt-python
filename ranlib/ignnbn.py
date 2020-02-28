#! /usr/bin/env python
#
def ignnbn ( n, p ):

#*****************************************************************************80
#
## IGNNBN generates a negative binomial random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a negative binomial
#    distribution.
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
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer, 1986,
#    ISBN: 0387963057,
#    LC: QA274.D48.
#
#  Parameters:
#
#    Input, integer N, the required number of events.
#    0 <= N.
#
#    Input, real P, the probability of an event during a
#    Bernoulli trial.  0.0 < P < 1.0.
#
#    Output, integer VALUE, a random deviate from
#    the distribution.
#
  from gengam import gengam
  from ignpoi import ignpoi
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'IGNNBN - Fatal error!' )
    print ( '  N < 0.' )
    exit ( 'IGNNBN - Fatal error!' )

  if ( p <= 0.0 ):
    print ( '' )
    print ( 'IGNNBN - Fatal error!' )
    print ( '  P <= 0.0' )
    exit ( 'IGNNBN - Fatal error!' )

  if ( 1.0 <= p ):
    print ( '' )
    print ( 'IGNNBN - Fatal error!' )
    print ( '  1.0 <= P' )
    exit ( 'IGNNBN - Fatal error!' )
#
#  Generate Y, a random gamma (n,(1-p)/p) variable.
#
  r = float ( n )
  a = p / ( 1.0 - p )
  y = gengam ( a, r )
#
#  Generate a random Poisson ( y ) variable.
#
  value = ignpoi ( y )

  return value

def ignnbn_test ( phrase ):

#*****************************************************************************80
#
## IGNNBN_TEST tests IGNNBN, which generates Negative Binomial deviates.
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
  print ( 'IGNNBN_TEST' )
  print ( '  IGNNBN generates negative binomial deviates.' )
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
  high = 20.0
  nn = int ( genunf ( low, high ) )

  low = 0.0
  high = 1.0
  pp = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  NN = %d' % ( nn ) )
  print ( '  PP = %g' % ( pp ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = ignnbn ( nn, pp )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'nbn'
  param = np.array ( [ nn, pp ] )
 
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'IGNNBN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  ignnbn_test ( phrase )
  timestamp ( )

