#! /usr/bin/env python
#
def genchi ( df ):

#*****************************************************************************80
#
## GENCHI generates a Chi-Square random deviate.
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
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real DF, the degrees of freedom.
#    0.0 < DF.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  from gengam import gengam
  from sys import exit

  if ( df <= 0.0 ):
    print ( ' ' )
    print ( 'GENCHI - Fatal error!' )
    print ( '  DF <= 0.' )
    print ( '  Value of DF: %g' % ( df ) )
    exit ( 'GENCHI - Fatal error!' )

  arg1 = 1.0
  arg2 = df / 2.0

  value = 2.0 * gengam ( arg1, arg2 )

  return value

def genchi_test ( phrase ):

#*****************************************************************************80
#
## GENCHI_TEST tests GENCHI, which generates Chi-Square deviates.
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
  print ( 'GENCHI_TEST' )
  print ( '  GENCHI generates Chi-square deviates.' )
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
  df = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  DF = %g' % ( df ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = genchi ( df )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'chi'
  param = np.array ( [ df ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENCHI_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  genchi_test ( phrase )
  timestamp ( )

