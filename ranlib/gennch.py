#! /usr/bin/env python
#
def gennch ( df, xnonc ):

#*****************************************************************************80
#
## GENNCH generates a noncentral Chi-Square random deviate.
#
#  Discussion:
#
#    This procedure generates a random deviate from the  distribution of a
#    noncentral chisquare with DF degrees of freedom and noncentrality parameter
#    XNONC.
#
#    It uses the fact that the noncentral chisquare is the sum of a chisquare
#    deviate with DF-1 degrees of freedom plus the square of a normal
#    deviate with mean XNONC and standard deviation 1.
#
#    A subtle ambiguity arises in the original formulation:
#
#      value = genchi ( arg1 ) + ( gennor ( arg2, arg3 ) ) ^ 2
#
#    because the compiler is free to invoke either genchi or gennor
#    first, both of which alter the random number generator state,
#    resulting in two distinct possible results.
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
#    1.0 < DF.
#
#    Input, real XNONC, the noncentrality parameter.
#    0.0 <= XNONC.
#
#    Output, real VALUE, a random deviate from the distribution.
#
  import numpy as np
  from genchi import genchi
  from gennor import gennor
  from sys import exit

  if ( df <= 1.0 ):
    print ( ' ' )
    print ( 'GENNCH - Fatal error!' )
    print ( '  DF <= 1.' )
    exit ( 'GENNCH - Fatal error!' )

  if ( xnonc < 0.0 ):
    print ( ' ' )
    print ( 'GENNCH - Fatal error!' )
    print ( '  XNONC < 0.0.' )
    exit ( 'GENNCH - Fatal error!' )

  arg1 = df - 1.0
  arg2 = np.sqrt ( xnonc )
  arg3 = 1.0

  t1 = genchi ( arg1 )
  t2 = gennor ( arg2, arg3 )
  value = t1 + t2 * t2

  return value

def gennch_test ( phrase ):

#*****************************************************************************80
#
## GENNCH_TEST tests GENNCH, which generates noncentral Chi-Square deviates.
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
  print ( 'GENNCH_TEST' )
  print ( '  GENNCH generates noncentral Chi-square deviates.' )
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
  low = 2.0
  high = 10.0
  df = genunf ( low, high )

  low = 0.0
  high = 2.0
  xnonc = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  DF =    %g' % ( df ) )
  print ( '  XNONC = %g' % ( xnonc ))
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = gennch ( df, xnonc )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'nch'
  param = np.array ( [ df, xnonc ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENNCH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  gennch_test ( phrase )
  timestamp ( )

