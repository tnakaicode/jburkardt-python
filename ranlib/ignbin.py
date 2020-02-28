#! /usr/bin/env python
#
def ignbin ( n, pp ):

#*****************************************************************************80
#
## IGNBIN generates a binomial random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a binomial
#    distribution whose number of trials is N and whose
#    probability of an event in each trial is P.
#
#    The previous version of this program relied on the assumption that
#    local memory would be preserved between calls.  It set up data
#    one time to be preserved for use over multiple calls.  In the
#    interests of portability, this assumption has been removed, and
#    the "setup" data is recomputed on every call.
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
#    Voratas Kachitvichyanukul, Bruce Schmeiser,
#    Binomial Random Variate Generation,
#    Communications of the ACM,
#    Volume 31, Number 2, February 1988, pages 216-222.
#
#  Parameters:
#
#    Input, integer N, the number of binomial trials, from which a
#    random deviate will be generated.
#    0 < N.
#
#    Input, real PP, the probability of an event in each trial of
#    the binomial distribution from which a random deviate is to be generated.
#    0.0 < PP < 1.0.
#
#    Output, integer VALUE, a random deviate from the distribution.
#
  import numpy as np
  from r4_uni_01 import r4_uni_01
  from sys import exit

  if ( pp <= 0.0 or 1.0 <= pp ):
    print ( ' ' )
    print ( 'IGNBIN - Fatal error!' )
    print ( '  PP is out of range.' )
    exit ( 'IGNBIN - Fatal error!' )

  p = min ( pp, 1.0 - pp )
  q = 1.0 - p
  xnp = n * p

  if ( xnp < 30.0 ):

    qn = q ** n
    r = p / q
    g = r * ( n + 1 )

    while ( True ):

      ix = 0
      f = qn
      u = r4_uni_01 ( )

      while ( True ):

        if ( u < f ):
          if ( 0.5 < pp ):
            ix = n - ix
          value = ix
          return value

        if ( 110 < ix ):
          break

        u = u - f
        ix = ix + 1
        f = f * ( g / ix - r )
#
#  The calculation of this data was originally intended to be
#  done once, then saved for later calls.
#
  ffm = xnp + p
  m = int ( ffm )
  fm = m
  xnpq = xnp * q
  p1 = int ( 2.195 * np.sqrt ( xnpq ) - 4.6 * q ) + 0.5
  xm = fm + 0.5
  xl = xm - p1
  xr = xm + p1
  c = 0.134 + 20.5 / ( 15.3 + fm )
  al = ( ffm - xl ) / ( ffm - xl * p )
  xll = al * ( 1.0 + 0.5 * al )
  al = ( xr - ffm ) / ( xr * q )
  xlr = al * ( 1.0 + 0.5 * al )
  p2 = p1 * ( 1.0 + c + c )
  p3 = p2 + c / xll
  p4 = p3 + c / xlr
#
#  Generate a variate.
#
  while ( True ):

    u = r4_uni_01 ( ) * p4
    v = r4_uni_01 ( )
#
#  Triangle
#
    if ( u < p1 ):
      ix = int ( xm - p1 * v + u )
      if ( 0.5 < pp ):
        ix = n - ix
      value = ix
      return value
#
#  Parallelogram
#
    if ( u <= p2 ):

      x = xl + ( u - p1 ) / c
      v = v * c + 1.0 - abs ( xm - x ) / p1

      if ( v <= 0.0 or 1.0 < v ):
        continue

      ix = int ( x )

    elif ( u <= p3 ):

      ix = int ( xl + np.log ( v ) / xll )
      if ( ix < 0 ):
        continue
      v = v * ( u - p2 ) * xll

    else:

      ix = int ( xr - np.log ( v ) / xlr )
      if ( n < ix ):
        continue
      v = v * ( u - p3 ) * xlr

    k = abs ( ix - m )

    if ( k <= 20 or xnpq / 2.0 - 1.0 <= k ):

      f = 1.0
      r = p / q
      g = float ( n + 1 ) * r

      if ( m < ix ):
        mp = m + 1

        for i in range ( mp, ix + 1 ):
          f = f * ( g / float ( i ) - r )

      elif ( ix < m ):
        ix1 = ix + 1

        for i in range ( ix1, m + 1 ):
          f = f / ( g / float ( i ) - r )

      if ( v <= f ):
        if ( 0.5 < pp ):
          ix = n - ix
        value = ix
        return value

    else:

      amaxp = ( k / xnpq ) * ( ( k * ( k / 3.0 \
        + 0.625 ) + 0.1666666666666 ) / xnpq + 0.5 )
      ynorm = - ( k * k ) / ( 2.0 * xnpq )
      alv = np.log ( v )

      if ( alv < ynorm - amaxp ):
        if ( 0.5 < pp ):
          ix = n - ix
        value = ix
        return value

      if ( ynorm + amaxp < alv ):
        continue

      x1 = ix + 1
      f1 = fm + 1.0
      z = n + 1 - fm
      w = n - ix + 1
      z2 = z * z
      x2 = x1 * x1
      f2 = f1 * f1
      w2 = w * w

      t = xm * np.log ( f1 / x1 ) + ( n - m + 0.5 ) * np.log ( z / w ) \
        + float ( ix - m ) * np.log ( w * p / ( x1 * q )) \
        + ( 13860.0 - ( 462.0 - ( 132.0 - ( 99.0 - 140.0 \
        / f2 ) / f2 ) / f2 ) / f2 ) / f1 / 166320.0 \
        + ( 13860.0 - ( 462.0 - ( 132.0 - ( 99.0 - 140.0 \
        / z2 ) / z2 ) / z2 ) / z2 ) / z / 166320.0 \
        + ( 13860.0 - ( 462.0 - ( 132.0 - ( 99.0 - 140.0 \
        / x2 ) / x2 ) / x2 ) / x2 ) / x1 / 166320.0 \
        + ( 13860.0 - ( 462.0 - ( 132.0 - ( 99.0 - 140.0 \
        / w2 ) / w2 ) / w2 ) / w2 ) / w / 166320.0

      if ( alv <= t ):
        if ( 0.5 < pp ):
          ix = n - ix
        value = ix
        return value

  return value

def ignbin_test ( phrase ):

#*****************************************************************************80
#
## IGNBIN_TEST tests IGNBIN, which generates Binomial deviates.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2013
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
  print ( 'IGNBIN_TEST' )
  print ( '  IGNBIN generates binomial deviates.' )
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
  low = 0.5
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
    array[i] = ignbin ( nn, pp )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'bin'
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
  print ( 'IGNBIN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  ignbin_test ( phrase )
  timestamp ( )

