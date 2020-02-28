#! /usr/bin/env python
#
def genunf ( low, high ):

#*****************************************************************************80
#
## GENUNF generates a uniform random deviate.
#
#  Discussion:
#
#    This procedure generates a real deviate uniformly distributed between
#    LOW and HIGH.
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
#    Input, real LOW, HIGH, the lower and upper bounds.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  from r4_uni_01 import r4_uni_01

  value = low + ( high - low ) * r4_uni_01 ( )

  return value

def genunf_test ( phrase ):

#*****************************************************************************80
#
## RANLIB_TEST_GENUNF tests GENUNF, which generates uniform deviates.
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
  from initialize import initialize
  from phrtsd import phrtsd
  from set_initial_seed import set_initial_seed
  from stats import stats
  from trstat import trstat

  n = 1000

  print ( '' )
  print ( 'GENUNF_TEST:' )
  print ( '  GENUNF generates uniform deviates.' )
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

  low = a + 1.0
  high = a + 10.0
  b = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  A = %g' % ( a ) )
  print ( '  B = %g' % ( b ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = genunf ( a, b )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'unf'
  param = np.array ( [ a, b ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENUNF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  genunf_test ( phrase )
  timestamp ( )

