#! /usr/bin/env python
#
def i4_binomial_sample ( n, pp ):

#*****************************************************************************80
#
## I4_BINOMIAL_SAMPLE generates a binomial random deviate.
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
#    26 July 2015
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
  from r8_uniform_01_sample import r8_uniform_01_sample
  from sys import exit

  if ( pp <= 0.0 or 1.0 <= pp ):
    print ( '' )
    print ( 'I4_BINOMIAL_SAMPLE - Fatal error!' )
    print ( '  PP is out of range.' )
    exit ( 'I4_BINOMIAL_SAMPLE - Fatal error!' )

  p = min ( pp, 1.0 - pp )
  q = 1.0 - p
  xnp = n * p

  if ( xnp < 30.0 ):

    qn = q ** n
    r = p / q
    g = r * float ( n + 1 )

    while ( True ):

      ix = 0
      f = qn
      u = r8_uniform_01_sample ( )

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
        f = f * ( g / float ( ix ) - r )
#
#  The calculation of this data was originally intended to be
#  done once, then saved for later calls.
#
  ffm = xnp + p
  m = np.floor ( ffm )
  fm = m
  xnpq = xnp * q
  p1 = np.floor ( 2.195 * np.sqrt ( xnpq ) - 4.6 * q ) + 0.5
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

    u = r8_uniform_01_sample ( ) * p4
    v = r8_uniform_01_sample ( )
#
#  Triangle
#
    if ( u < p1 ):
      ix = np.floor ( xm - p1 * v + u )
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

      ix = np.floor ( x )

    elif ( u <= p3 ):

      ix = np.floor ( xl + np.log ( v ) / xll )
      if ( ix < 0 ):
        continue

      v = v * ( u - p2 ) * xll

    else:

      ix = np.floor ( xr - np.log ( v ) / xlr )
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
        for i in range (  mp, ix + 1 ):
          f = f * ( g / float ( i ) - r )
      elif ( ix < m ):
        for i in range ( ix + 1, m + 1 ):
          f = f / ( g / float ( i ) - r )

      if ( v <= f ):
        if ( 0.5 < pp ):
          ix = n - ix
        value = ix
        return value

    else:

      amaxp = ( float ( k ) / xnpq ) * ( ( float ( k ) * ( float ( k ) / 3.0 \
        + 0.625 ) + 0.1666666666666 ) / xnpq + 0.5 )
      ynorm = - float ( k * k ) / ( 2.0 * xnpq )
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
      z = float ( n + 1 ) - fm
      w = float ( n - ix + 1 )
      z2 = z * z
      x2 = x1 * x1
      f2 = f1 * f1
      w2 = w * w

      t = xm * np.log ( f1 / x1 ) + ( n - m + 0.5 ) * np.log ( z / w ) \
        + float ( ix - m ) * np.log ( w * p / ( x1 * q ) ) \
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

def i4_binomial_sample_test ( ):

#*****************************************************************************80
#
## I4_BINOMIAL_SAMPLE_TEST tests I4_BINOMIAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_binomial_pdf import i4_binomial_pdf
  from i4_uniform_ab import i4_uniform_ab
  from r8_uniform_ab import r8_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'I4_BINOMIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BINOMIAL_SAMPLE samples the binomial distribution.' )

  print ( '' )
  print ( '     N          P        K       PDF(N,P,K)' )
  print ( '' )

  for i in range ( 0, 10 ):
    n, seed = i4_uniform_ab ( 1, 20, seed )
    p, seed = r8_uniform_ab ( 0.0, 1.0, seed )
    k = i4_binomial_sample ( n, p )
    pdf = i4_binomial_pdf ( n, p, k )
    print ( '  %4d  %14.6g  %2d  %14.6g' % ( n, p, k, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BINOMIAL_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_binomial_sample_test ( )
  timestamp ( )


