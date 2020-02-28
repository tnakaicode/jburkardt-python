#! /usr/bin/env python
#
def ignpoi ( mu ):

#*****************************************************************************80
#
## IGNPOI generates a Poisson random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a Poisson
#    distribution with given mean.
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
#    Computer Generation of Poisson Deviates
#    From Modified Normal Distributions,
#    ACM Transactions on Mathematical Software,
#    Volume 8, Number 2, June 1982, pages 163-179.
#
#  Parameters:
#
#    Input, real MU, the mean of the Poisson distribution
#    from which a random deviate is to be generated.
#
#    Output, integer VALUE, a random deviate from
#    the distribution.
#
  import numpy as np
  from r4_uni_01 import r4_uni_01
  from sexpo import sexpo
  from snorm import snorm

  a0 = -0.5
  a1 =  0.3333333
  a2 = -0.2500068
  a3 =  0.2000118
  a4 = -0.1661269
  a5 =  0.1421878
  a6 = -0.1384794
  a7 =  0.1250060

  fact = np.array ( [ 1.0, 1.0, 2.0, 6.0, 24.0, 120.0, 720.0, 5040.0, 40320.0, 362880.0 ] )
#
#  Start new table and calculate P0.
#
  if ( mu < 10.0 ):

    m = max ( 1, int ( mu ) )
    l = 0
    p = np.exp ( - mu )
    q = p
    p0 = p
#
#  Uniform sample for inversion method.
#
    while ( True ):

      u = r4_uni_01 ( )
      value = 0

      if ( u <= p0 ):
        return value
#
#  Creation of new Poisson probabilities.
#
      for k in range ( 1, 36 ):
        p = p * mu / k
        q = q + p
        if ( u <= q ):
          value = k
          return value

  else:

    s = np.sqrt ( mu )
    d = 6.0 * mu * mu
    l = int ( mu - 1.1484 )
#
#  Normal sample.
#
    g = mu + s * snorm ( )

    if ( 0.0 <= g ):

      value = int ( g )
#
#  Immediate acceptance if large enough.
#
      if ( l <= value ):
        return value
#
#  Squeeze acceptance.
#
      fk = value
      difmuk = mu - fk
      u = r4_uni_01 ( )

      if ( difmuk * difmuk * difmuk <= d * u ):
        return value
#
#  Preparation for steps P and Q.
#
    omega = 0.3989423 / s
    b1 = 0.04166667 / mu
    b2 = 0.3 * b1 * b1
    c3 = 0.1428571 * b1 * b2
    c2 = b2 - 15.0 * c3
    c1 = b1 - 6.0 * b2 + 45.0 * c3
    c0 = 1.0 - b1 + 3.0 * b2 - 15.0 * c3
    c = 0.1069 / mu

    if ( 0.0 <= g ):

      kflag = 0

      if ( value < 10 ):

        px = - mu
        py = mu ** value / fact[value]

      else:

        delta = 0.8333333E-01 / fk
        delta = delta - 4.8 * delta * delta * delta
        v = difmuk / fk

        if ( 0.25 < abs ( v ) ):
          px = fk * np.log ( 1.0 + v ) - difmuk - delta
        else:
          px = fk * v * v * ((((((( a7 \
            * v + a6 ) \
            * v + a5 ) \
            * v + a4 ) \
            * v + a3 ) \
            * v + a2 ) \
            * v + a1 ) \
            * v + a0 ) - delta

        py = 0.3989423 / np.sqrt ( fk )

      x = ( 0.5 - difmuk ) / s
      xx = x * x
      fx = - 0.5 * xx
      fy = omega * ((( c3 * xx + c2 ) * xx + c1 ) * xx + c0 )

      if ( fy - u * fy <= py * np.exp ( px - fx ) ):
        return value
#
#  Exponential sample.
#
    while ( True ):

      e = sexpo ( )
      u = 2.0 * r4_uni_01 ( ) - 1.0
      if ( u < 0.0 ):
        t = 1.8 - abs ( e )
      else:
        t = 1.8 + abs ( e )

      if ( t <= -0.6744 ):
        continue

      value = int ( mu + s * t )
      fk = value
      difmuk = mu - fk

      kflag = 1
#
#  Calculation of PX, PY, FX, FY.
#
      if ( value < 10 ):

        px = - mu
        py = mu ** value / fact[value]

      else:

        delta = 0.8333333E-01 / fk
        delta = delta - 4.8 * delta * delta * delta
        v = difmuk / fk

        if ( 0.25 < abs ( v ) ):
          px = fk * np.log ( 1.0 + v ) - difmuk - delta
        else:
          px = fk * v * v * ((((((( a7 \
            * v + a6 ) \
            * v + a5 ) \
            * v + a4 ) \
            * v + a3 ) \
            * v + a2 ) \
            * v + a1 ) \
            * v + a0 ) - delta

        py = 0.3989423 / np.sqrt ( fk )

      x = ( 0.5 - difmuk ) / s
      xx = x * x
      fx = -0.5 * xx
      fy = omega * ((( c3 * xx + c2 ) * xx + c1 ) * xx + c0 )

      if ( kflag <= 0 ):

        if ( fy - u * fy <= py * np.exp ( px - fx ) ):
          return value

      else:

        if ( c * abs ( u ) <= py * np.exp ( px + e ) - fy * np.exp ( fx + e ) ):
          return value

def ignpoi_test ( phrase ):

#*****************************************************************************80
#
## IGNPOI_TEST tests IGNPOI, which generates Poisson deviates.
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

  n = 1000

  print ( '' )
  print ( 'IGNPOI_TEST' )
  print ( '  IGNPOI generates Poisson deviates.' )
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
  mu = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  MU = %g' % ( mu ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = ignpoi ( mu )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'poi'
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
  print ( 'IGNPOI_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  ignpoi_test ( phrase )
  timestamp ( )

