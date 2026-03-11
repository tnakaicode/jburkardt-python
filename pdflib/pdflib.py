#! /usr/bin/env python3
#
a_save = [ \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False ];

cg1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
cg2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

g_save = 1

ig1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
ig2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

initialized_save = False

lg1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
lg2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

def antithetic_get ( ):

#*****************************************************************************80
#
## antithetic_get() queries the antithetic value for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    bool VALUE, is TRUE if generator G is antithetic.
#
  i = -1
  value = []
  value = antithetic_memory ( i, value )

  return value

def antithetic_memory ( i, value ):

#*****************************************************************************80
#
## antithetic_memory() stores the antithetic value for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    bool VALUE.  For I = +1, VALUE is an input quantity.
#
#  Output:
#
#    bool VALUE.  For I = -1, VALUE is an output quantity.
#
  global a_save

  g_max = 32

  if ( i < 0 ):
    g = cgn_get ( )
    value = a_save[g-1]
  elif ( i == 0 ):
    a_save = [];
    for i in range ( 1, g_max + 1 ):
      a_save.append ( False )
    value = false
  elif ( 0 < i ):
    g = cgn_get ( )
    a_save[g-1] = value

  return value

def antithetic_set ( value ):

#*****************************************************************************80
#
## antithetic_set() sets the antithetic value for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    bool VALUE, is TRUE if the current generator is to be antithetic.
#
  i = +1
  value = antithetic_memory ( i, value )

  return

def cg_get ( g ):

#*****************************************************************************80
#
## cg_get() queries the CG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#  Output:
#
#    integer CG1, CG2, the CG values for generator G.
#
  i = -1
  cg1 = []
  cg2 = []
  cg1, cg2 = cg_memory ( i, g, cg1, cg2 )

  return cg1, cg2

def cg_memory ( i, g, cg1, cg2 ):

#*****************************************************************************80
#
## cg_memory() stores the CG values for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    integer CG1, CG2.  For I = +1, these are new values of the
#    CG parameter for generator G.
#
#  Output:
#
#    integer CG1, CG2.  For I = -1, these are 
#    old values of the CG parameter for generator G.
#
  global cg1_save
  global cg2_save

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ( '' )
    print ( 'cg_memory(): Fatal error!' )
    print ( '  Input generator index G is out of bounds.' )
    raise Exception ( 'cg_memory(): Fatal error!' )

  if ( i < 0 ):
    cg1 = cg1_save[g-1]
    cg2 = cg2_save[g-1]
  elif ( i == 0 ):
    for i in range ( 1, g_max + 1 ):
      cg1_save[i-1] = 0
      cg2_save[i-1] = 0
    cg1 = 0
    cg2 = 0
  elif ( 0 < i ):
    cg1_save[g-1] = cg1
    cg2_save[g-1] = cg2

  return cg1, cg2

def cgn_get ( ):

#*****************************************************************************80
#
## cgn_get() gets the current generator index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer G, the current generator index.
#
  i = -1
  g = []
  g = cgn_memory ( i, g )

  return g

def cgn_memory ( i, g ):

#*****************************************************************************80
#
## cgn_memory() stores the current generator index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get the value.
#    0, initialize the value.
#    1, set the value.
#
#    integer G.  For I = +1, an input quantity.
#
#  Output:
#
#    integer G.  For I = -1 or 0, an output quantity.
#
  global g_save

  g_max = 32

  if ( i < 0 ):

    g = g_save

  elif ( i == 0 ):

    g_save = 1
    g = g_save

  elif ( 0 < i ):

    if ( g < 1 or g_max < g ):
      print ( '' )
      print ( 'cgn_memory(): Fatal error!' )
      print ( '  Input generator index G is out of bounds.' )
      raise Exception ( 'cgn_memory(): Fatal error!' )

    g_save = g

  return g

def cgn_set ( g ):

#*****************************************************************************80
#
## cgn_set() sets the current generator index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the current generator index.
#    1 <= G <= 32.
#
  i = +1
  g = cgn_memory ( i, g )

  return

def cg_set ( g, cg1, cg2 ):

#*****************************************************************************80
#
## cg_set() sets the CG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#    integer CG1, CG2, the CG values for generator G.
#
  i = +1
  cg1, cg2 = cg_memory ( i, g, cg1, cg2 )

  return

def i4_binomial_pdf ( n, p, k ):

#*****************************************************************************80
#
## i4_binomial_pdf() evaluates the binomial PDF.
#
#  Discussion:
#
#    pdf(n,p,k) = C(n,k) p^k (1-p)^(n-k)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of binomial trials.
#    0 < N.
#
#    real P, the probability of a success in one trial.
#
#    integer K, the number of successes.
#
#  Output:
#
#    real VALUE, the probability of K successes
#    in N trials with a per-trial success probability of P.
#
  from scipy.special import comb

  if ( k < 0 ):
    value = 0.0
  elif ( k <= n ):
    value = comb ( n, k ) * ( p ** k ) * ( 1.0 - p ) ** ( n - k )
  else:
    value = 0.0

  return value

def i4_binomial_pdf_values ( n_data ):

#*****************************************************************************80
#
## i4_binomial_pdf_values() returns some values of the binomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability of X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = BinomialDistribution [ n, p ]
#      PDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition, CRC Press, 1996, pages 651-652.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer A, a parameter of the function.
#
#    real B, a parameter of the function.
#
#    integer X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  a_vec = np.array ( ( \
     5, 12,  6, 13,  9, \
     1,  2, 17,  6,  8 ))

  b_vec = np.array ( ( \
    0.8295092339327006, \
    0.06611873491603133, \
    0.0438289977791071, \
    0.4495389603071763, \
    0.7972869541062562, \
    0.3507523379805466, \
    0.8590968552798568, \
    0.007512364073964213, \
    0.1136640464424993, \
    0.2671322702601793 ))

  f_vec = np.array ( ( \
    0.3927408939646697, \
    0.0006199968732461383, \
    0.764211224733124, \
    0.0004260353334364943, \
    0.302948289145794, \
    0.3507523379805466, \
    0.01985369619202562, \
    0.006854388879646552, \
    0.000002156446446382985, \
    0.0005691150511772053 ) )

  x_vec = np.array ( ( \
     5, 5, 0, 0, 7, \
     1, 0, 2, 6, 7 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def i4_binomial_pdf_test ( ):

#*****************************************************************************80
#
## i4_binomial_pdf_test() tests i4_binomial_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'i4_binomial_pdf_test():' )
  print ( '  i4_binomial_pdf() evaluates the binomial pdf' )
  print ( '  pdf(n,p,k) = probability, in n trials, of k successes,' )
  print ( '  if a single success has probability p.' )
  print ( '' )
  print ( '     N          P        K       PDF(N,P,K)       PDF(N,P,K)' )
  print ( '                                 tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, n, p, k, pdf1 = i4_binomial_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = i4_binomial_pdf ( n, p, k )
    print ( '  %4d  %14.6g  %2d  %14.6g  %14.6g' % ( n, p, k, pdf1, pdf2 ) )

  return

def i4_binomial_sample ( n, pp, rng ):

#*****************************************************************************80
#
## i4_binomial_sample() generates a binomial random deviate.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Reference:
#
#    Voratas Kachitvichyanukul, Bruce Schmeiser,
#    Binomial Random Variate Generation,
#    Communications of the ACM,
#    Volume 31, Number 2, February 1988, pages 216-222.
#
#  Input:
#
#    integer N, the number of binomial trials, from which a
#    random deviate will be generated.
#    0 < N.
#
#    real PP, the probability of an event in each trial of
#    the binomial distribution from which a random deviate is to be generated.
#    0.0 < PP < 1.0.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer VALUE, a random deviate from the distribution.
#
  import numpy as np

  if ( pp <= 0.0 or 1.0 <= pp ):
    print ( '' )
    print ( 'i4_binomial_sample(): Fatal error!' )
    print ( '  PP is out of range.' )
    raise Exception ( 'i4_binomial_sample(): Fatal error!' )

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
      u = rng.random ( )

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

    u = p4 * rng.random ( )
    v = rng.random ( )
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

def i4_binomial_sample_test ( rng ):

#*****************************************************************************80
#
## i4_binomial_sample_test() tests i4_binomial_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4_binomial_sample_test():' )
  print ( '  i4_binomial_sample() samples the binomial distribution.' )

  print ( '' )
  print ( '     N          P        K       PDF(N,P,K)' )
  print ( '' )

  for i in range ( 0, 10 ):
    n = rng.integers ( low = 1, high = 20, endpoint = True )
    p = rng.random ( )
    k = i4_binomial_sample ( n, p, rng )
    pdf = i4_binomial_pdf ( n, p, k )
    print ( '  %4d  %14.6g  %2d  %14.6g' % ( n, p, k, pdf ) )

  return

def i4_uniform_sample ( a, b, rng ):

#*****************************************************************************80
#
## i4_uniform_sample() returns a scaled pseudorandom I4 between A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer C, the randomly chosen integer.
#
  import numpy as np
#
#  We prefer A < B.
#
  a2 = min ( a, b )
  b2 = max ( a, b )

  u = rng.random ( )
#
#  Scale to [A2-0.5,B2+0.5].
#
  u = ( 1.0 - u ) * ( a2 - 0.5 ) \
    +         u   * ( b2 + 0.5 )
#
#  Round.
#
  value = round ( u )
#
#  Enforce limits.
#
  value = max ( value, a2 )
  value = min ( value, b2 )

  return value

def i4_uniform_sample_test ( rng ):

#*****************************************************************************80
#
## i4_uniform_sample_test() tests i4_uniform_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  initialize ( )

  print ( '' )
  print ( 'i4_uniform_sample_test():' )
  print ( '  i4_uniform_sample() samples the uniform distribution on integers.' )
  print ( '  Generate C between A and B.' )
  print ( '' )
  print ( '    A    B    C' )
  print ( '' )

  for i in range ( 0, 10 ):
    a = i4_uniform_sample ( -10, 10, rng )
    b = i4_uniform_sample ( a, 20, rng )
    c = i4_uniform_sample ( a, b, rng )
    print ( '  %3d  %3d  %3d' % ( a, b, c ) )

  return

def i4_uni ( ):

#*****************************************************************************80
#
## i4_uni() generates a random positive integer.
#
#  Discussion:
#
#    This procedure returns a random integer following a uniform distribution
#    over (1, 2147483562) using the current generator.
#
#    The original name of this function was "random()", but this conflicts
#    with a standard library function name in C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Output:
#
#    integer VALUE, the random integer.
#
  a1 = 40014
  a2 = 40692
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'i4_uni - Note:' )
    print ( '  Initializing RNGLIB package.' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  Retrieve the seeds for the current generator.
#
  cg1, cg2 = cg_get ( g )
#
#  Update the seeds.
#
  k = ( cg1 // 53668 )
  cg1 = a1 * ( cg1 - k * 53668 ) - k * 12211

  if ( cg1 < 0 ):
    cg1 = cg1 + m1

  k = ( cg2 // 52774 )
  cg2 = a2 * ( cg2 - k * 52774 ) - k * 3791

  if ( cg2 < 0 ):
    cg2 = cg2 + m2
#
#  Store the updated seeds.
#
  cg_set ( g, cg1, cg2 )
#
#  Construct the random integer from the seeds.
#
  z = cg1 - cg2

  if ( z < 1 ):
    z = z + m1 - 1
#
#  If the generator is in antithetic mode, we must reflect the value.
#
  value = antithetic_get ( )

  if ( value ):
    z = m1 - z

  return z

def i4_uni_test ( ):

#*****************************************************************************80
#
## i4_uni_test() tests i4_uni().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_uni_test():' )
  print ( '  i4_uni() returns a random positive integer.' )
  print ( '' )

  for i in range ( 1, 21 ):
    value = i4_uni ( )
    print ( '  %d' % ( value ) )

  return

def i4vec_multinomial_pdf ( n, p, m, x ):

#*****************************************************************************80
#
## i4vec_multinomial_pdf() evaluates the multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of trials.
#    0 < N.
#
#    real P(M), the probability of each outcome on one trial.
#    0.0 <= P(I) <= 1.0
#    sum P = 1
#
#    integer M, the number of possible outcomes on one trial.
#    0 < M.
#
#    integer X(M), the results of N trials,
#    with X(I) the number of times outcome I occurred.
#    0 <= X(I) <= N.
#    sum X = N.
#
#  Output:
#
#    real VALUE, the probability
#    density function evaluated at X.
#

#
#  The combinatorial coefficient is an integer.
#
  c = 1
  top = n
  for i in range ( 0, m ):
    bot = 1
    for j in range ( 0, x[i] ):
      c = ( c * top ) // bot
      top = top - 1
      bot = bot + 1

  value = c
  for i in range ( 0, m ):
    value = value * p[i] ** x[i]

  return value

def multinomial_pdf_sizes ( n_data ):

#*****************************************************************************80
#
## multinomial_pdf_sizes() returns sizes of some multinomial PDF data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer M, the size of the given problem
#
  import numpy as np

  n_max = 10

  m_vec = np.array ( ( \
     2, 2, 2, 3, 5, \
     5, 5, 5, 5, 5 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
  else:
    m = m_vec[n_data]
    n_data = n_data + 1

  return n_data, m

def multinomial_pdf_values ( n_data, m ):

#*****************************************************************************80
#
## multinomial_pdf_values() returns some values of the multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer M, the number of outcomes.
#
#    integer N, the number of trials.
#
#    real P(M), the probability of each outcome on one trial.
#
#    integer X(M), the number of times each outcome occurred in
#    N trials.
#
#    real PDF, the probability of X.
#
  import numpy as np

  n_max = 10

  n_vec = np.array ( ( \
     3, 4, 3, 3, 3, \
     3, 3, 3, 3, 3 ))

  p_cell = ( \
    ( 0.7, 0.3 ), \
    ( 0.7, 0.3 ), \
    ( 0.5, 0.5 ), \
    ( 0.6, 0.0, 0.4 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ) )

  x_cell = ( \
    ( 2, 1 ), \
    ( 2, 2 ), \
    ( 2, 1 ), \
    ( 1, 1, 1 ), \
    ( 3, 0, 0, 0, 0 ), \
    ( 2, 1, 0, 0, 0 ), \
    ( 1, 0, 2, 0, 0 ), \
    ( 1, 0, 0, 1, 1 ), \
    ( 0, 0, 0, 3, 0 ), \
    ( 0, 1, 1, 1, 0 ) )

  pdf_vec = np.array ( ( \
    0.441, \
    0.2646, \
    0.375, \
    0.0, \
    0.216, \
    0.108, \
    0.018, \
    0.036, \
    0.001, \
    0.006 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    p = []
    x = []
    pdf = 0.0
  else:
    n = n_vec[n_data]
    p = p_cell[n_data]
    x = x_cell[n_data]
    pdf = pdf_vec[n_data]
    n_data = n_data + 1

  return n_data, n, p, x, pdf

def i4vec_multinomial_pdf_test ( ):

#*****************************************************************************80
#
## i4vec_multinomial_pdf_test() tests i4vec_multinomial_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'i4vec_multinomial_pdf_test():' )
  print ( '  i4vec_multinomial_pdf() evaluates the multinomial PDF.' )
  print ( '  Given M possible outcomes on a single trial,' )
  print ( '  with each outcome having probability P,' )
  print ( '  PDF is the probability that after N trials,' )
  print ( '  outcome I occurred X(I) times.' )
  print ( '' )
  print ( '     N     M     I      P        X        PDF()            PDF()' )
  print ( '                                          tabulated        computed' )
  
  n_data1 = 0
  n_data2 = 0

  while ( True ):

    n_data1, m             = multinomial_pdf_sizes ( n_data1 )
    n_data2, n, p, x, pdf1 = multinomial_pdf_values ( n_data2, m )

    if ( n_data1 == 0 ):
      break

    pdf2 = i4vec_multinomial_pdf ( n, p, m, x )

    print ( '' )
    for i in range ( 0, m ):
      print ( '              %4d  %8.4f  %4d' % ( i, p[i], x[i] ) )
    print ( '  %4d  %4d                        %14.6g  %14.6g' \
      % ( n, m, pdf1, pdf2 ) )

  return

def i4vec_multinomial_sample ( n, p, m, rng ):

#*****************************************************************************80
#
## i4vec_multinomial_sample() generates a multinomial random deviate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer, 1986,
#    ISBN: 0387963057,
#    LC: QA274.D48.
#
#  Input:
#
#    integer N, the number of trials.
#    0 < N.
#
#    real P(M).  P(I) is the probability that an event
#    will be classified into category I.  Thus, each P(I) must be between
#    0.0 and 1.0.  
#
#    integer M, the number of possible outcomes on one trial.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer X(M), the number of occurrences of each outcome 
#    in N trials.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'i4vec_multinomial_sample(): Fatal error!' )
    print ( '  N < 0' )
    raise Exception ( 'i4vec_multinomial_sample(): Fatal error!' )

  if ( m <= 1 ):
    print ( '' )
    print ( 'i4vec_multinomial_sample(): Fatal error!' )
    print ( '  M <= 1' )
    raise Exception ( 'i4vec_multinomial_sample(): Fatal error!' )

  for i in range ( 0, m ):

    if ( p[i] < 0.0 ):
      print ( '' )
      print ( 'i4vec_multinomial_sample(): Fatal error!' )
      print ( '  Some P(i) < 0.' )
      raise Exception ( 'i4vec_multinomial_sample(): Fatal error!' )

    if ( 1.0 < p[i] ):
      print ( '' )
      print ( 'i4vec_multinomial_sample(): Fatal error!' )
      print ( '  Some 1 < P(i).' )
      raise Exception ( 'i4vec_multinomial_sample(): Fatal error!' )
#
#  Initialize variables.
#
  ntot = n
  ptot = 1.0
  x = np.zeros ( m, dtype = np.int32 )
#
#  Generate the observation.
#
  for i in range ( 0, m - 1 ):
    prob = p[i] / ptot
    x[i] = i4_binomial_sample ( ntot, prob, rng )
    ntot = ntot - x[i]
    if ( ntot <= 0 ):
      return x
    ptot = ptot - p[i]

  x[m-1] = ntot

  return x

def i4vec_multinomial_sample_test ( rng ):

#*****************************************************************************80
#
## i4vec_multinomial_sample_test() tests i4vec_multinomial_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_multinomial_sample_test():' )
  print ( '  i4vec_multinomial_sample() samples the multinomial distribution.' )
  print ( '' )
  print ( '     N     M     I      P        X        PDF()' )

  for k in range ( 0, 10 ):
    m = rng.integers ( low = 2, high = 10, endpoint = True )
    n = rng.integers ( low = 1, high = 5, endpoint = True )
    p = rng.random ( size = m )
    ptot = np.sum ( p )
    p = p / ptot
    x = i4vec_multinomial_sample ( n, p, m, rng )
    pdf = i4vec_multinomial_pdf ( n, p, m, x )
    print ( '' )
    for i in range ( 0, m ):
      print ( '              %4d  %8.4f  %4d' % ( i, p[i], x[i] ) )
    print ( '  %4d  %4d                        %14.6g' % ( n, m, pdf ) )

  return

def ig_get ( g ):

#*****************************************************************************80
#
## ig_get() queries the IG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#  Output:
#
#    integer IG1, IG2, the IG values for generator G.
#
  i = -1
  ig1 = []
  ig2 = []
  ig1, ig2 = ig_memory ( i, g, ig1, ig2 )

  return ig1, ig2

def ig_memory ( i, g, ig1, ig2 ):

#*****************************************************************************80
#
## ig_memory() stores the IG values for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    integer IG1, IG2.  For I = +1, these are new values 
#    of the IG parameter for generator G.
#
#  Output:
#
#    integer IG1, IG2.  For I = -1, these are the
#    old values of the IG parameter for generator G.
#
  global ig1_save
  global ig2_save

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ( '' )
    print ( 'ig_memory(): Fatal error!' )
    print ( '  Input generator index G is out of bounds.' )
    raise Exception ( 'ig_memory(): Fatal error!' )

  if ( i < 0 ):
    ig1 = ig1_save[g-1]
    ig2 = ig2_save[g-1]
  elif ( i == 0 ):
    for j in range ( 1, g_max + 1 ):
      ig1_save[j-1] = 0
      ig2_save[j-1] = 0
    ig1 = 0
    ig2 = 0
  elif ( 0 < i ):
    ig1_save[g-1] = ig1
    ig2_save[g-1] = ig2

  return ig1, ig2

def ig_set ( g, ig1, ig2 ):

#*****************************************************************************80
#
## ig_set() sets the IG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#    integer IG1, IG2, the IG values for generator G.
#
  i = +1
  ig1, ig2 = ig_memory ( i, g, ig1, ig2 )

  return

def init_generator ( t ):

#*****************************************************************************80
#
## init_generator() sets the current generator to initial, last or new seed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer T, the seed type:
#    0, use the seed chosen at initialization time.
#    1, use the last seed.
#    2, use a new seed set 2^30 values away.
#
  a1_w = 1033780774
  a2_w = 1494757890
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'init_generator - Note:' )
    print ( '  Initializing RNGLIB package.' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  0: Restore the initial seed.
#
  if ( t == 0 ):

    ig1, ig2 = ig_get ( g )
    lg1 = ig1
    lg2 = ig2
    lg_set ( g, lg1, lg2 )
#
#  1: Restore the last seed.
#
  elif ( t == 1 ):

    lg1, lg2 = lg_get ( g );
#
#  Advance to a new seed.
#
  elif ( t == 2 ):

    lg1, lg2 = lg_get ( g )
    lg1 = multmod ( a1_w, lg1, m1 )
    lg2 = multmod ( a2_w, lg2, m2 )
    lg_set ( g, lg1, lg2 )

  else:

    print ( '' )
    print ( 'init_generator(): Fatal error!' )
    print ( '  Input parameter T out of bounds.' )
    raise Exception ( 'init_generator(): Fatal error!' )
#
#  Store the new seed.
#
  cg1 = lg1
  cg2 = lg2
  cg_set ( g, cg1, cg2 )

  return

def initialized_get ( ):

#*****************************************************************************80
#
## initialized_get() gets the INITIALIZED value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    bool INITIALIZED, is true if the package has been initialized.
#
  i = -1
  initialized = []
  initialized = initialized_memory ( i, initialized )

  return initialized

def initialized_memory ( i, initialized ):

#*****************************************************************************80
#
## initialized_memory() stores the INITIALIZED value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    bool INITIALIZED.  For I = +1, an input quantity.
#
#  Output:
#
#    bool INITIALIZED.  For I = -1, an output quantity.
#
  global initialized_save

  if ( i < 0 ):
    initialized = initialized_save
  elif ( i == 0 ):
    initialized_save = False
    initialized = False
  elif ( 0 < i ):
    initialized_save = initialized

  return initialized

def initialized_set ( ):

#*****************************************************************************80
#
## initialized_set() sets the INITIALIZED value to true.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  i = +1
  initialized = True
  initialized = initialized_memory ( i, initialized )

  return

def initialize ( ):

#*****************************************************************************80
#
## initialize() initializes the random number generator library.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
  g_max = 32
#
#  Remember that we have called INITIALIZE().
#
  initialized_set ( )
#
#  Initialize all generators to have FALSE antithetic value.
#
  value = False
  for g in range ( 1, g_max + 1 ):
    cgn_set ( g )
    antithetic_set ( value )
#
#  Set the initial seeds.
#
  ig1 = 1234567890
  ig2 = 123456789
  set_initial_seed ( ig1, ig2 )
#
#  Initialize the current generator index to 1.
#
  g = 1
  cgn_set ( g )

  print ( '' )
  print ( 'initialize():' )
  print ( '  rnglib() has been initialized.' )
  return

def lg_get ( g ):

#*****************************************************************************80
#
## lg_get() queries the LG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#  Output:
#
#    integer LG1, LG2, the LG values for generator G.
#
  i = -1
  lg1 = []
  lg2 = []
  lg1, lg2 = lg_memory ( i, g, lg1, lg2 )

  return lg1, lg2

def lg_memory ( i, g, lg1, lg2 ):

#*****************************************************************************80
#
## lg_memory() stores the LG values for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    integer LG1, LG2.  For I = +1, these are 
#    new values of the LG parameter for generator G.
#
#  Output:
#
#    integer LG1, LG2.  For I = -1,
#    old values of the LG parameter for generator G.
#
  global lg1_save
  global lg2_save

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ( '' )
    print ( 'lg_memory(): Fatal error!' )
    print ( '  Input generator index G is out of bounds.' )
    raise Exception ( 'lg_memory(): Fatal error!' )

  if ( i < 0 ):
    lg1 = lg1_save[g-1]
    lg2 = lg2_save[g-1]
  elif ( i == 0 ):
    for j in range ( 1, g_max + 1 ):
      lg1_save[j-1] = 0
      lg2_save[j-1] = 0
    lg1 = 0
    lg2 = 0
  elif ( 0 < i ):
    lg1_save[g-1] = lg1
    lg2_save[g-1] = lg2

  return lg1, lg2

def lg_set ( g, lg1, lg2 ):

#*****************************************************************************80
#
## lg_set() sets the LG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#    integer LG1, LG2, the LG values for generator G.
#
  i = +1
  lg_memory ( i, g, lg1, lg2 )

  return

def multmod ( a, s, m ):

#*****************************************************************************80
#
## multmod() carries out modular multiplication.
#
#  Discussion:
#
#    This procedure returns
#
#      ( A * S ) mod M
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer A, S, M, the arguments.
#
#  Output:
#
#    integer VALUE, the value of the product of A and S,
#    modulo M.
#
  h = 32768

  if ( a <= 0 ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  A <= 0.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( m <= a ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  M <= A.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( s <= 0 ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  S <= 0.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( m <= s ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  M <= S.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( a < h ):

    a0 = a
    p = 0

  else:

    a1 = ( a // h )
    a0 = a - h * a1
    qh = ( m // h )
    rh = m - h * qh

    if ( h <= a1 ):

      a1 = a1 - h
      k = ( s // qh )
      p = h * ( s - k * qh ) - k * rh

      while ( p < 0 ):
        p = p + m

    else:

      p = 0

    if ( a1 != 0 ):

      q = ( m // a1 )
      k = ( s // q )
      p = p - k * ( m - a1 * q )

      if ( 0 < p ):
        p = p - m

      p = p + a1 * ( s - k * q )

      while ( p < 0 ):
        p = p + m

    k = ( p // qh )
    p = h * ( p - k * qh ) - k * rh

    while ( p < 0 ):
      p = p + m

  if ( a0 != 0 ):

    q = ( m // a0 )
    k = ( s // q )
    p = p - k * ( m - a0 * q )

    if ( 0 < p ):
      p = p - m

    p = p + a0 * ( s - k * q )

    while ( p < 0 ):
      p = p + m

  return p

def pdflib_test ( ):

#*****************************************************************************80
#
## pdflib_test() tests pdflib().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'pdflib_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pdflib().' )
#
#  Initialize the random number generator package.
#
  rng = default_rng ( )
  initialize ( )
#
#  Support functions.
#
  i4_uni_test ( )

  r8_uni_01_test ( )

  r8ge_print_test ( )
  r8ge_print_some_test ( )

  r8mat_norm_fro_affine_test ( rng )

  r8po_mv_test ( )

  r8ut_sl_test ( )

  r8vec_indicator1_test ( )
#
#  Library functions.
#
  i4_binomial_pdf_test ( )
  i4_binomial_sample_test ( rng )

  i4_uniform_sample_test ( rng )

  i4vec_multinomial_pdf_test ( )
  i4vec_multinomial_sample_test ( rng )

  r8_beta_pdf_test ( )
  r8_beta_sample_test ( rng )

  r8_chi_pdf_test ( )
  r8_chi_sample_test ( rng )

  r8_exponential_01_pdf_test ( )
  r8_exponential_01_sample_test ( rng )

  r8_exponential_pdf_test ( )
  r8_exponential_sample_test ( rng )

  r8_gamma_01_pdf_test ( )
  r8_gamma_01_sample_test ( rng )

  r8_gamma_pdf_test ( )
  r8_gamma_sample_test ( rng )

  r8_invchi_pdf_test ( )
  r8_invchi_sample_test ( rng )

  r8_invgam_pdf_test ( )
  r8_invgam_sample_test ( rng )

  r8_normal_01_pdf_test ( )
  r8_normal_01_sample_test ( rng )

  r8_normal_pdf_test ( )
  r8_normal_sample_test ( rng )

  r8_scinvchi_pdf_test ( )
  r8_scinvchi_sample_test ( rng )

  r8_uniform_01_pdf_test ( rng )
  r8_uniform_01_sample_test ( rng )

  r8_uniform_pdf_test ( rng )
  r8_uniform_sample_test ( rng )

  r8vec_multinormal_pdf_test ( rng )
  r8vec_multinormal_sample_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'pdflib_test():' )
  print ( '  Normal end of execution.' )
  return

def r8_beta_pdf ( alpha, beta, rval ):

#*****************************************************************************80
#
## r8_beta_pdf() evaluates the PDF of a beta distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real ALPHA, BETA, shape parameter values.
#    0.0 < ALPHA, BETA.
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from scipy.special import gammaln

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'r8_beta_pdf(): Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    raise Exception ( 'r8_beta_pdf(): Fatal error!' )

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'r8_beta_pdf(): Fatal error!' )
    print ( '  Parameter BETA is not positive.' )
    raise Exception ( 'r8_beta_pdf(): Fatal error!' )

  if ( rval <= 0.0 or 1.0 <= rval ):

    value = 0.0

  else:

    temp = gammaln ( alpha + beta ) - gammaln ( alpha ) \
      - gammaln ( beta )

    value = np.exp ( temp ) \
      * rval ** ( alpha - 1.0 ) * ( 1.0 - rval ) ** ( beta - 1.0 )
 
  return value

def beta_pdf_values ( n_data ):

#*****************************************************************************80
#
## beta_pdf_values() returns some values of the Beta PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real ALPHA, BETA, the parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  alpha_vec = np.array ( ( \
       1.092091484911879, \
       2.808477213834471, \
       1.287888961910225, \
       3.169828561512062, \
       2.006531407488083, \
    0.009191855792026001, \
       0.472723751058401, \
       4.204237253278341, \
       1.301514988836825, \
       1.758143299519481 ))

  beta_vec = np.array ( ( \
       4.781587882544648, \
       2.076535407379806, \
       0.549783967662353, \
      0.3086361453280091, \
       3.773367432107051, \
       4.487520304498656, \
     0.06808445791730976, \
      0.6155195788227712, \
       4.562418534907164, \
       4.114436583429598 ))

  f_vec = np.array ( ( \
    0.002826137156803199, \
     0.04208950342768649, \
      0.2184064957817208, \
      0.1335142301445414, \
      0.1070571849830009, \
    0.005796394377470491, \
      0.5518796772414584, \
                     0.0, \
        2.87907465409348, \
       2.126992854611924 ) )

  x_vec = np.array ( ( \
      0.8667224264776531, \
     0.04607764003473368, \
     0.02211617261254013, \
      0.4582543823302144, \
      0.8320834756642252, \
      0.3520587633290876, \
       0.898529119425846, \
    -0.01692420862048847, \
     0.09718884992568674, \
      0.2621671905296927 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    beta = 0.0
    x = 0.0
    f = 0.0
  else:
    alpha = alpha_vec[n_data]
    beta = beta_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, beta, x, f

def r8_beta_pdf_test ( ):

#*****************************************************************************80
#
## r8_beta_pdf_test() tests r8_beta_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_beta_pdf_test():' )
  print ( '  r8_beta_pdf() evaluates the BETA PDF.' )
  print ( '' )
  print ( '         ALPHA         BETA         X           PDF()         PDF()' )
  print ( '                                                tabulated     computed' )  
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, alpha, beta, x, pdf1 = beta_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_beta_pdf ( alpha, beta, x )

    print ( '  %12g  %12g  %12g  %12g  %12g' % ( alpha, beta, x, pdf1, pdf2 ) )

  return

def r8_beta_sample ( aa, bb, rng ):

#*****************************************************************************80
#
## r8_beta_sample() generates a beta random deviate.
#
#  Discussion:
#
#    This procedure returns a single random deviate from the beta distribution
#    with parameters A and B.  The density is
#
#      x^(a-1) * (1-x)^(b-1) / Beta(a,b) for 0 < x < 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Russell Cheng,
#    Generating Beta Variates with Nonintegral Shape Parameter values,
#    Communications of the ACM,
#    Volume 21, Number 4, April 1978, pages 317-322.
#
#  Input:
#
#    real AA, the first parameter of the beta distribution.
#    0.0 < AA.
#
#    real BB, the second parameter of the beta distribution.
#    0.0 < BB.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  import numpy as np

  if ( aa <= 0.0 ):
    print ( '' )
    print ( 'r8_beta_sample(): Fatal error!' )
    print ( '  AA <= 0.0' )
    raise Exception ( 'r8_beta_sample(): Fatal error!\n' )

  if ( bb <= 0.0 ):
    print ( '' )
    print ( 'r8_beta_sample(): Fatal error!' )
    print ( '  BB <= 0.0' )
    raise Exception ( 'r8_beta_sample(): Fatal error!\n' )
#
#  Algorithm BB
#
  if ( 1.0 < aa and 1.0 < bb ):

    a = min ( aa, bb )
    b = max ( aa, bb )
    alpha = a + b
    beta = np.sqrt ( ( alpha - 2.0 ) / ( 2.0 * a * b - alpha ) )
    gamma = a + 1.0 / beta

    while ( True ):

      u1 = rng.random ( )
      u2 = rng.random ( )
      v = beta * np.log ( u1 / ( 1.0 - u1 ) )
      w = a * np.exp ( v )

      z = u1 ** 2 * u2;
      r = gamma * v - np.log ( 4.0 )
      s = a + r - w

      if ( 5.0 * z <= s + 1.0 + np.log ( 5.0 ) ):
        break

      t = np.log ( z )

      if ( t <= s ):
        break

      if ( t <= ( r + alpha * np.log ( alpha / ( b + w ) ) ) ):
        break
#
#  Algorithm BC
#
  else:

    a = max ( aa, bb )
    b = min ( aa, bb )
    alpha = a + b
    beta = 1.0 / b
    delta = 1.0 + a - b

    k1 = delta * ( 1.0 / 72.0 + b / 24.0 ) / ( a / b - 7.0 / 9.0 )
    k2 = 0.25 + ( 0.5 + 0.25 / delta ) * b

    while ( True ):

      u1 = rng.random ( )
      u2 = rng.random ( )

      if ( u1 < 0.5 ):

        y = u1 * u2
        z = u1 * y

        if ( k1 <= 0.25 * u2 + z - y ):
          continue

      else:

        z = u1 ** 2 * u2

        if ( z <= 0.25 ):

          v = beta * np.log ( u1 / ( 1.0 - u1 ) )
          w = a * np.exp ( v )

          if ( aa == a ):
            value = w / ( b + w )
          else:
            value = b / ( b + w );

          return value

        if ( k2 < z ):
          continue

      v = beta * np.log ( u1 / ( 1.0 - u1 ) )
      w = a * np.exp ( v )

      if ( np.log ( z ) <= alpha * ( np.log ( alpha / ( b + w ) ) + v ) - np.log ( 4.0 ) ):
        break

  if ( aa == a ):
    value = w / ( b + w )
  else:
    value = b / ( b + w )

  return value

def r8_beta_sample_test ( rng ):

#*****************************************************************************80
#
## r8_beta_sample_test() tests r8_beta_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_beta_sample_test():' )
  print ( '  r8_beta_sample() samples the beta distribution.' )

  print ( '' )
  print ( '            ALPHA        BETA             X       PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    alpha = 5.0 * rng.random ( )
    beta = 5.0 * rng.random ( )
    x = r8_beta_sample ( alpha, beta, rng )
    pdf = r8_beta_pdf ( alpha, beta, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( alpha, beta, x, pdf ) )

  return

def r8_chi_pdf ( df, rval ):

#*****************************************************************************80
#
## r8_chi_pdf() evaluates the PDF of a chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from scipy.special import gammaln

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'r8_chi_pdf(): Fatal error!' )
    print ( '  Degrees of freedom must be positive.' )
    raise Exception ( 'r8_chi_pdf(): Fatal error!' )
      
  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp2 = df * 0.5;

    temp1 = ( temp2 - 1.0 ) * np.log ( rval ) - 0.5 * rval \
      - temp2 * np.log ( 2.0 ) - gammaln ( temp2 )

    value = np.exp ( temp1 )

  return value

def r8_chi_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_chi_pdf_values() returns some values of the standard Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real DF, the degrees of freedom
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 21

  df_vec = np.array ( ( \
     1.0,  2.0,  1.0,  2.0,  1.0,  \
     2.0,  3.0,  4.0,  1.0,  2.0,  \
     3.0,  4.0,  5.0,  3.0,  3.0,  \
     3.0,  3.0,  3.0, 10.0, 10.0, \
    10.0 ))

  f_vec = np.array ( ( \
         3.969525474770117, \
        0.4975062395963412, \
         2.792879016972342, \
        0.4950249168745841, \
        0.5164415474672784, \
        0.4093653765389909, \
        0.2065766189869113, \
       0.08187307530779819, \
        0.2419707245191434, \
        0.3032653298563167, \
        0.2419707245191434, \
        0.1516326649281584, \
       0.08065690817304777, \
        0.2075537487102974, \
        0.1541803298037693, \
        0.1079819330263761, \
       0.07322491280963248, \
       0.04865217332964145, \
     0.0007897534631674914, \
       0.00766415502440505, \
       0.02353325907815472 ))

  x_vec = np.array ( ( \
     0.01, \
     0.01, \
     0.02, \
     0.02, \
     0.40, \
     0.40, \
     0.40, \
     0.40, \
     1.00, \
     1.00, \
     1.00, \
     1.00, \
     1.00, \
     2.00, \
     3.00, \
     4.00, \
     5.00, \
     6.00, \
     1.00, \
     2.00, \
     3.00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0.0
    x = 0.0
    f = 0.0
  else:
    df = df_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, df, x, f

def r8_chi_pdf_test ( ):

#*****************************************************************************80
#
## r8_chi_pdf_test() tests r8_chi_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'r8_chi_pdf_test():' )
  print ( '  r8_chi_pdf() evaluates the standard chi PDF.' )
  print ( '' )
  print ( '           DF             X              PDF()          PDF()' )
  print ( '                                         tabulated      computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, df, x, pdf1 = r8_chi_pdf_values ( n_data )

    if ( n_data == 0 ): 
      break

    pdf2 = r8_chi_pdf ( df, x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( df, x, pdf1, pdf2 ) )

  return

def r8_chi_sample ( df, rng ):

#*****************************************************************************80
#
## r8_chi_sample() generates a Chi-Square random deviate.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a random deviate  from the distribution.
#
  if ( df <= 0.0 ):
    print ( '' )
    print ( 'r8_chi_sample(): Fatal error!' )
    print ( '  DF <= 0.' )
    print ( '  Value of DF:', df )
    raise Exception ( 'r8_chi_sample(): Fatal error!' )

  arg1 = 1.0
  arg2 = df / 2.0

  value = 2.0 * r8_gamma_sample ( arg1, arg2, rng )

  return value

def r8_chi_sample_test ( rng ):

#*****************************************************************************80
#
## r8_chi_sample_test() tests r8_chi_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_chi_sample_test():' )
  print ( '  r8_chi_sample() samples the CHI distribution:' )
  print ( '' )
  print ( '           DF              R              PDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    df = 20.0 * rng.random ( )
    r = r8_chi_sample ( df, rng )
    pdf = r8_chi_pdf ( df, r )
    print ( '  %14.6g  %14.6g  %14.6g' % ( df, r, pdf ) )

  return

def r8_exponential_01_pdf ( rval ):

#*****************************************************************************80
#
## r8_exponential_01_pdf(): PDF of a standard exponential distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF.
#
  import numpy as np

  if ( rval < 0.0 ):
    value = 0.0
  else:
    value = np.exp ( - rval )

  return value

def r8_exponential_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_exponential_01_pdf_values(): some values of the standard Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( ( \
    0.4959398481993681, \
    0.00856777959135697, \
    0.01720937842266235, \
    0.07507070056996956, \
    0.1679332083261492, \
    0.0, \
    0.399845179478639, \
    0.9005384971416223, \
    0.0, \
    0.05044803826563792 ))

  x_vec = np.array ( ( \
        0.7013006334030669, \
         4.759746670799113, \
         4.062300786629853, \
         2.589324935217918, \
         1.784188948117787, \
       -0.1363469579618277, \
        0.9166778581012469, \
        0.1047623644285883, \
       -0.2589405122149109, \
         2.986811417663269 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def r8_exponential_01_pdf_test ( ):

#*****************************************************************************80
#
## r8_exponential_01_pdf_test() tests r8_exponential_01_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'r8_exponential_01_pdf_test():' )
  print ( '  r8_exponential_01_pdf() evaluates the standard exponential pdf.' )
  print ( '' )
  print ( '           X           PDF()            PDF()' )
  print ( '                       tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, x, pdf1 = r8_exponential_01_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_exponential_01_pdf ( x )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, pdf1, pdf2 ) )

  return

def r8_exponential_01_sample ( rng ):

#*****************************************************************************80
#
## r8_exponential_01_sample() samples the standard exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a sample of the PDF.
#
  import numpy as np

  r = rng.random ( )

  value = - np.log ( r )

  return value

def r8_exponential_01_sample_test ( rng ):

#*****************************************************************************80
#
## r8_exponential_01_sample_test() tests r8_exponential_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_exponential_01_sample_test():' )
  print ( '  r8_exponential_01_sample() samples the standard exponential PDF:' )
  print ( '' )
  print ( '          R               PDF(R)' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_exponential_01_sample ( rng )
    pdf = r8_exponential_01_pdf ( r )
    print ( '  %14.6g  %14.6g' % ( r, pdf ) )

  return

def r8_exponential_pdf ( beta, x ):

#*****************************************************************************80
#
## r8_exponential_pdf() evaluates the PDF of an exponential distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real BETA, the scale value.
#    0.0 < BETA.
#
#    real X, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'r8_exponential_pdf(): Fatal error!' )
    print ( '  BETA parameter must be positive.' )
    raise Exception ( 'r8_exponential_pdf(): Fatal error!' )

  if ( x < 0.0 ):
    value = 0.0
  else:
    value = np.exp ( - x / beta ) / beta

  return value

def r8_exponential_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_exponential_pdf_values(): some values of the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real BETA, the shape parameter.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  beta_vec = np.array ( ( \
         1.092091484911879, \
         4.147546169663503, \
         2.076535407379806, \
         1.287888961910225, \
        0.2191449888955355, \
        0.3086361453280091, \
         2.006531407488083, \
         3.986434770531281, \
         4.487520304498656, \
         0.472723751058401 ))

  f_vec = np.array ( ( \
     0.0001446999730194618, \
       0.06289850821824726, \
        0.3663607831924032, \
        0.3542787877169571, \
     1.472582451176006e-12, \
     1.829637907028298e-06, \
       0.01173398427218792, \
                       0.0, \
        0.1034724689882351, \
          1.95394780436833 ))

  x_vec = np.array ( ( \
         9.558807522740191, \
         5.573123971945631, \
        0.5677992226519164, \
         1.010563614677953, \
         6.303053694254367, \
         4.440343499102481, \
         7.522202212856243, \
      -0.08143245130010748, \
         3.442598613603521, \
       0.03753060499296568 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    beta = 0.0
    x = 0.0
    f = 0.0
  else:
    beta = beta_vec[n_data];
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, beta, x, f

def r8_exponential_pdf_test ( ):

#*****************************************************************************80
#
## r8_exponential_pdf_test() tests r8_exponential_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'r8_exponential_pdf_test():' )
  print ( '  r8_exponential_pdf() evaluates the exponential PDF.' )
  print ( '' )
  print ( '           BETA             X          PDF()            PDF()' )
  print ( '                                       tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, beta, x, pdf1 = r8_exponential_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_exponential_pdf ( beta, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( beta, x, pdf1, pdf2 ) )

  return

def r8_exponential_sample ( beta, rng ):

#*****************************************************************************80
#
## r8_exponential_sample() samples the exponential PDF.
#
#  Discussion:
#
#    Note that the parameter LAMBDA is a multiplier.  In some formulations,
#    it is used as a divisor instead.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real BETA, the parameter of the PDF.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a sample of the PDF.
#
  import numpy as np

  r = rng.random ( )

  value = - np.log ( r ) * beta

  return value

def r8_exponential_sample_test ( rng ):

#*****************************************************************************80
#
## r8_exponential_sample_test() tests r8_exponential_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_exponential_sample_test():' )
  print ( '  r8_exponential_sample() samples the general exponential PDF:' )
  print ( '' )
  print ( '            BETA               R          PDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    beta = 10.0 * rng.random ( )
    r = r8_exponential_sample ( beta, rng )
    pdf = r8_exponential_pdf ( beta, r )
    print ( '  %14.6g  %14.6g  %14.6g' % ( beta, r, pdf ) )

  return

def r8_gamma_01_pdf ( alpha, rval ):

#*****************************************************************************80
#
## r8_gamma_01_pdf() evaluates the PDF of a standard gamma distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real ALPHA, the shape parameter.
#    0.0 < ALPHA.
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from scipy.special import gammaln

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'r8_gamma_01_pdf(): Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    raise Exception ( 'r8_gamma_01_pdf(): Fatal error!' )

  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp = ( alpha - 1.0 ) * np.log ( rval ) - rval - gammaln ( alpha )

    value = np.exp ( temp )

  return value

def r8_gamma_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_gamma_01_pdf_values() returns some values of the standard Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real ALPHA, the shape parameter.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  alpha_vec = np.array ( ( \
         1.092091484911879, \
         4.147546169663503, \
         2.076535407379806, \
         1.287888961910225, \
        0.2191449888955355, \
        0.3086361453280091, \
         2.006531407488083, \
         3.986434770531281, \
         4.487520304498656, \
         0.472723751058401 ))

  f_vec = np.array ( ( \
    0.00009260811963612823, \
        0.1260335478747823, \
        0.1363536772414351, \
        0.5114450139194701, \
     0.0001230139468263628, \
      0.001870342832511005, \
      0.004476000451227789, \
                       0.0, \
        0.2056668486524041, \
                       0.0 ))

  x_vec = np.array ( ( \
         9.541334553343761, \
          5.39780214905239, \
        0.1942467166183289, \
        0.6545463320909413, \
         6.156639979175331, \
         4.220159083225351, \
         7.424071607424807, \
       -0.4806971028367454, \
          3.18289954879574, \
       -0.3570226383736496 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    x = 0.0
    f = 0.0
  else:
    alpha = alpha_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, x, f

def r8_gamma_01_pdf_test ( ):

#*****************************************************************************80
#
## r8_gamma_01_pdf_test() tests r8_gamma_01_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'r8_gamma_01_pdf_test():' )
  print ( '  r8_gamma_01_pdf() evaluates the standard gamma PDF.' )
  print ( '' )
  print ( '           ALPHA          X              PDF(0,1)       PDF(0,1)' )
  print ( '                                         tabulated      computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, alpha, x, pdf1 = r8_gamma_01_pdf_values ( n_data )

    if ( n_data == 0 ): 
      break

    pdf2 = r8_gamma_01_pdf ( alpha, x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( alpha, x, pdf1, pdf2 ) )

  return

def r8_gamma_01_sample ( a, rng ):

#*****************************************************************************80
#
## r8_gamma_01_sample() samples the standard Gamma distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm GD in the reference.
#
#    pdf ( a x ) = 1/gamma(a) * x^(a-1) * exp ( - x )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Generating Gamma Variates by a Modified Rejection Technique,
#    Communications of the ACM,
#    Volume 25, Number 1, January 1982, pages 47-54.
#
#  Input:
#
#    real A, the shape parameter.
#    0.0 < A.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  import numpy as np

  a1 =  0.3333333
  a2 = -0.2500030
  a3 =  0.2000062
  a4 = -0.1662921
  a5 =  0.1423657
  a6 = -0.1367177
  a7 =  0.1233795

  e1 = 1.0
  e2 = 0.4999897
  e3 = 0.1668290
  e4 = 0.0407753
  e5 = 0.0102930

  q1 =  0.04166669
  q2 =  0.02083148
  q3 =  0.00801191
  q4 =  0.00144121
  q5 = -0.00007388
  q6 =  0.00024511
  q7 =  0.00024240

  sqrt32 = 5.656854

  if ( 1.0 <= a ):

    s2 = a - 0.5
    s = np.sqrt ( s2 )
    d = sqrt32 - 12.0 * s
#
#  Immediate acceptance.
#
    t = r8_normal_01_sample ( rng )
    x = s + 0.5 * t
    value = x * x

    if ( 0.0 <= t ):
      return value
#
#  Squeeze acceptance.
#
    u = rng.random ( )

    if ( d * u <= t * t * t ):
      return value

    r = 1.0 / a
    q0 = (((((( q7 \
      * r + q6 ) \
      * r + q5 ) \
      * r + q4 ) \
      * r + q3 ) \
      * r + q2 ) \
      * r + q1 ) \
      * r
#
#  Approximation depending on size of parameter A.
#
    if ( 13.022 < a ):
      b = 1.77
      si = 0.75
      c = 0.1515 / s
    elif ( 3.686 < a ):
      b = 1.654 + 0.0076 * s2
      si = 1.68 / s + 0.275
      c = 0.062 / s + 0.024
    else:
      b = 0.463 + s + 0.178 * s2
      si = 1.235
      c = 0.195 / s - 0.079 + 0.16 * s
#
#  Quotient test.
#
    if ( 0.0 < x ):

      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * (((((( a7 \
          * v + a6 ) \
          * v + a5 ) \
          * v + a4 ) \
          * v + a3 ) \
          * v + a2 ) \
          * v + a1 ) \
          * v

      if ( np.log ( 1.0 - u ) <= q ):
        return value

    while ( True ):

      e = r8_exponential_01_sample ( rng )
      u = 2.0 * rng.random ( ) - 1.0

      if ( 0.0 <= u ):
        t = b + abs ( si * e )
      else:
        t = b - abs ( si * e )
#
#  Possible rejection.
#
      if ( t < -0.7187449 ):
        continue
#
#  Calculate V and quotient Q.
#
      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * (((((( a7 \
          * v + a6 ) \
          * v + a5 ) \
          * v + a4 ) \
          * v + a3 ) \
          * v + a2 ) \
          * v + a1 ) \
          * v
#
#  Hat acceptance.
#
      if ( q <= 0.0 ):
        continue

      if ( 0.5 < q ):
        w = np.exp ( q ) - 1.0
      else:
        w = (((( e5 * q + e4 ) * q + e3 ) * q + e2 ) * q + e1 ) * q
#
#  May have to sample again.
#
      if ( c * abs ( u ) <= w * np.exp ( e - 0.5 * t * t ) ):
        break

    x = s + 0.5 * t
    value = x * x

    return value
#
#  Method for A < 1.
#
  else:

    b = 1.0 + 0.3678794 * a

    while ( True ):

      p = b * rng.random ( )

      if ( p < 1.0 ):

        value = np.exp ( np.log ( p ) / a )

        if ( value <= r8_exponential_01_sample ( rng ) ):
          return value

        continue

      value = - np.log ( ( b - p ) / a )

      if ( ( 1.0 - a ) * np.log ( value ) <= r8_exponential_01_sample ( rng ) ):
        break

  return value

def r8_gamma_01_sample_test ( rng ):

#*****************************************************************************80
#
## r8_gamma_01_sample_test() tests r8_gamma_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np


  print ( '' )
  print ( 'r8_gamma_01_sample_test():' )
  print ( '  r8_gamma_01_sample() samples the standard gamma distribution.' )

  print ( '' )
  print ( '            A                X       PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    a = 5.0 * rng.random ( )
    x = r8_gamma_01_sample ( a, rng )
    pdf = r8_gamma_01_pdf ( a, x )
    print ( '  %14.6g  %14.6g  %14.6g' % ( a, x, pdf ) )

  return

def r8_gamma_pdf ( beta, alpha, rval ):

#*****************************************************************************80
#
## r8_gamma_pdf() evaluates the PDF of a gamma distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real BETA, the rate parameter.
#    0.0 < BETA.
#
#    real ALPHA, the shape parameter.
#    0.0 < ALPHA.
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from scipy.special import gammaln

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'r8_gamma_pdf(): Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    raise Exception ( 'r8_gamma_pdf(): Fatal error!' )

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'r8_gamma_pdf(): Fatal error!' )
    print ( '  Parameter BETA is not positive.' )
    raise Exception ( 'r8_gamma_pdf(): Fatal error!' )

  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp = alpha * np.log ( beta ) + ( alpha - 1.0 ) * np.log ( rval ) \
      - beta * rval - gammaln ( alpha )

    value = np.exp ( temp )

  return value

def r8_gamma_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_gamma_pdf_values() returns some values of a Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real BETA, the rate parameter.
#
#    real ALPHA, the shape parameter.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  beta_vec = np.array ( ( \
         1.092091484911879, \
         2.808477213834471, \
         1.287888961910225, \
         3.169828561512062, \
         2.006531407488083, \
      0.009191855792026001, \
         0.472723751058401, \
         4.204237253278341, \
         1.301514988836825, \
         1.758143299519481 ))

  alpha_vec = np.array ( ( \
         4.781587882544648, \
         2.076535407379806, \
         0.549783967662353, \
        0.3086361453280091, \
         3.773367432107051, \
         4.487520304498656, \
       0.06808445791730976, \
        0.6155195788227712, \
         4.562418534907164, \
         4.114436583429598 ))

  f_vec = np.array ( ( \
        0.1672017697220646, \
        0.8522122814089312, \
         2.122272611165834, \
     6.993771842317114e-05, \
       0.01679379733182281, \
     6.687464259463117e-10, \
      0.001295436045931343, \
                       0.0, \
       0.01189893036865762, \
        0.3658836103539945 ))

  x_vec = np.array ( ( \
         4.942957250382744, \
        0.2099361564793942, \
       0.07173978623046406, \
         2.587141553904492, \
         4.743179115458788, \
         1.974664495479389, \
         5.126400502735112, \
       -0.1534233427414219, \
        0.5047170879434957, \
         1.456220075613112 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    beta = 0.0
    alpha = 0.0
    x = 0.0
    f = 0.0
  else:
    beta = beta_vec[n_data]
    alpha = alpha_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, beta, alpha, x, f

def r8_gamma_pdf_test ( ):

#*****************************************************************************80
#
## r8_gamma_pdf_test() tests r8_gamma_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'r8_gamma_pdf_test():' )
  print ( '  r8_gamma_pdf() evaluates a gamma PDF.' )
  print ( '' )
  print ( '           BETA            ALPHA          X            PDF              PDF' )
  print ( '                                                       tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, beta, alpha, x, pdf1 = r8_gamma_pdf_values ( n_data )

    if ( n_data == 0 ): 
      break

    pdf2 = r8_gamma_pdf ( beta, alpha, x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g' % ( beta, alpha, x, pdf1, pdf2 ) )

  return

def r8_gamma_sample ( r, a, rng ):

#*****************************************************************************80
#
## r8_gamma_sample() generates a Gamma random deviate.
#
#  Discussion:
#
#    This procedure generates random deviates from the gamma distribution whose
#    density is (R^A)/Gamma(A) * X^(A-1) * Exp(-R*X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
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
#  Input:
#
#    real R, the rate parameter.
#    A nonzero.
#
#    real A, the shape parameter.
#    0 < A.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  value = r8_gamma_01_sample ( a, rng ) / r

  return value

def r8_gamma_sample_test ( rng ):

#*****************************************************************************80
#
## r8_gamma_sample_test() tests r8_gamma_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_gamma_sample_test():' )
  print ( '  r8_gamma_sample() samples a gamma distribution.' )

  print ( '' )
  print ( '           R               A               X              PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = 5.0 * rng.random ( )
    a = 5.0 * rng.random ( )
    x = r8_gamma_sample ( r, a, rng )
    pdf = r8_gamma_pdf ( r, a, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( r, a, x, pdf ) )

  return

def r8ge_cg ( n, a, b, x ):

#*****************************************************************************80
#
## r8ge_cg() uses the conjugate gradient method on an R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The matrix A must be a positive definite symmetric band matrix.
#
#    The method is designed to reach the solution after N computational
#    steps.  However, roundoff may introduce unacceptably large errors for
#    some problems.  In such a case, calling the routine again, using
#    the computed solution as the new starting estimate, should improve
#    the results.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Beckman,
#    The Solution of Linear Equations by the Conjugate Gradient Method,
#    in Mathematical Methods for Digital Computers,
#    edited by John Ralston, Herbert Wilf,
#    Wiley, 1967,
#    ISBN: 0471706892,
#    LC: QA76.5.R3.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(N,N), the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X(N), an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N), the approximate solution vector.
#
  import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r8ge_mv ( n, n, a, x )

  r = np.zeros ( n, dtype = np.float64 )
  for i in range ( 0, n ):
    r[i] = b[i] - ap[i]

  p = np.zeros ( n, dtype = np.float64 )
  for i in range ( 0, n ):
    p[i] = b[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r8ge_mv ( n, n, a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr = np.dot ( p, r )

    if ( pap == 0.0 ):
      return x

    alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
    for i in range ( 0, n ):
      x[i] = x[i] + alpha * p[i]

    for i in range ( 0, n ):
      r[i] = r[i] - alpha * ap[i]
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
    rap = np.dot ( r, ap )

    beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
    for i in range ( 0, n ):
      p[i] = r[i] + beta * p[i]

  return x

def r8ge_cg_test ( rng ):

#*****************************************************************************80
#
## r8ge_cg_test() tests r8ge_cg() for a full storage matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_cg_test():' )
  print ( '  r8ge_cg() applies CG to an R8GE matrix.' )
#
#  Choose a random positive definite symmetric matrix A.
#
  n = 10
  key = 123456789

  a = pds_random ( n, key, rng )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r8ge_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r8ge_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r8ge_det ( n, a_lu, pivot ):

#*****************************************************************************80
#
## r8ge_det(): determinant of a matrix factored by r8ge_fa() or r8ge_trf().
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979,
#    ISBN13: 978-0-898711-72-1,
#    LC: QA214.L56.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa 
#    or r8ge_TRF.
#
#    integer PIVOT(N), as computed by r8ge_fa or r8ge_TRF.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i]
    if ( pivot[i] != i ):
      value = - value

  return value

def r8ge_dif2 ( m, n ):

#*****************************************************************************80
#
## r8ge_dif2() returns the DIF2 matrix in R8GE format.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is a special case of the TRIS or tridiagonal scalar matrix.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.68
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Birkhauser, 1980,
#    ISBN: 0817608117,
#    LC: QA297.T58.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      if ( j == i - 1 ):
        a[i,j] = -1.0
      elif ( j == i ):
        a[i,j] = 2.0
      elif ( j == i + 1 ):
        a[i,j] = -1.0

  return a

def r8ge_dilu ( m, n, a ):

#*****************************************************************************80
#
## r8ge_dilu() produces the diagonal incomplete LU factor of an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the R8GE matrix.
#
#  Output:
#
#    real D(M), the DILU factor.
#
  import numpy as np

  d = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    if ( i < n ):
      d[i] = a[i,i]

  mn = min ( m, n )

  for i in range ( 0, mn ):
    d[i] = 1.0 / d[i]
    for j in range ( i + 1, mn ):
      d[j] = d[j] - a[j,i] * d[i] * a[i,j]

  return d

def r8ge_fa ( n, a ):

#*****************************************************************************80
#
## r8ge_fa() performs a LINPACK style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_fa is a simplified version of the LINPACK routine R8GEFA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(N,N), the matrix to be factored.
#
#  Output:
#
#    real A_LU(N,N), an upper triangular matrix and 
#    the multipliers used to obtain it.  The factorization 
#    can be written A = L * U, where L is a product of 
#    permutation and unit lower triangular matrices and U 
#    is upper triangular.
#
#    integer PIVOT(N), a vector of pivot indices.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np

  a_lu = r8ge_zeros ( n, n )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_lu[i,j] = a[i,j]

  info = 0

  pivot = np.zeros ( n, dtype = np.int32 )

  for k in range ( 0, n - 1 ):
#
#  Find L, the index of the pivot row.
#
    l = k
    for i in range ( k + 1, n ):
      if ( abs ( a_lu[l,k] ) < abs ( a_lu[i,k] ) ):
        l = i

    pivot[k] = l
#
#  If the pivot index is zero, the algorithm has failed.
#
    if ( a_lu[l,k] == 0.0 ):
      info = k
      return a_lu, pivot, info
#
#  Interchange rows L and K if necessary.
#
    if ( l != k ):
      t         = a_lu[l,k]
      a_lu[l,k] = a_lu[k,k]
      a_lu[k,k] = t
#
#  Normalize the values that lie below the pivot entry A(K,K).
#
    for i in range ( k + 1, n ):
      a_lu[i,k] = - a_lu[i,k] / a_lu[k,k]
#
#  Row elimination with column indexing.
#
    for j in range ( k + 1, n ):

      if ( l != k ):
        t         = a_lu[l,j]
        a_lu[l,j] = a_lu[k,j]
        a_lu[k,j] = t

      for i in range ( k + 1, n ):
        a_lu[i,j] = a_lu[i,j] + a_lu[i,k] * a_lu[k,j]

  pivot[n-1] = n - 1

  if ( a_lu[n-1,n-1] == 0.0 ):
    info = n - 1

  return a_lu, pivot, info

def r8ge_fa_test01 ( ):

#*****************************************************************************80
#
## r8ge_fa_test01() tests r8ge_fa(), r8ge_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8ge_fa_test01():' )
  print ( '  r8ge_fa() computes the LU factors,' )
  print ( '  r8ge_sl() solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_fa_test01 - Warning!' )
    print ( '  r8ge_fa declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  for i in range ( 0, n ):
    x[i] = 1.0
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 1
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_fa_test02 ( ):

#*****************************************************************************80
#
## r8ge_fa_test02() tests r8ge_fa(), r8ge_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8ge_fa_test02():' )
  print ( '  r8ge_fa() computes the LU factors,' )
  print ( '  r8ge_sl() solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )

  r8ge_print ( n, n, a, '  The matrix:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_fa_test02 - Warning!' )
    print ( '  r8ge_fa declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
#
#  Display the gory details.
#
  r8ge_print ( n, n, a_lu, '  The compressed LU factors:' )

  i4vec_print ( n, pivot, '  The pivot vector P:' )
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8ge_identity ( n ):

#*****************************************************************************80
#
## r8ge_identity() copies the identity matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the N by N identity matrix.
#
  import numpy as np

  a = r8ge_zeros ( n, n )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def r8ge_ml ( n, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## r8ge_ml() computes A * x or A' * x, using r8ge_fa factors.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that r8ge_fa has overwritten the original matrix
#    information by LU factors.  r8ge_ml is able to reconstruct the
#    original matrix from the LU factor data.
#
#    r8ge_ml allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa.
#
#    integer PIVOT(N), the pivot vector computed by r8ge_fa.
#
#    real X(N), the vector to be multiplied.
#
#    integer JOB, specifies the operation to be done:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * X.
#
#  Output:
#
#    real B(N), the result of the multiplication.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    b[i] = x[i]

  if ( job == 0 ):
#
#  Y = U * X.
#
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        b[i] = b[i] + a_lu[i,j] * b[j]
      b[j] = a_lu[j,j] * b[j]
#
#  B = PL * Y = PL * U * X = A * x.
#
    for j in range ( n - 2, -1, -1 ):

      for i in range ( j + 1, n ):
        b[i] = b[i] - a_lu[i,j] * b[j]
      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

  else:
#
#  Y = (PL)' * X:
#
    for j in range ( 0, n - 1 ):

      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

      for i in range ( j + 1, n ):
        b[j] = b[j] - b[i] * a_lu[i,j]
#
#  B = U' * Y = ( PL * U )' * X = A' * X.
#
    for i in range ( n - 1, -1, -1 ):
      for j in range ( i + 1, n ):
        b[j] = b[j] + b[i] * a_lu[i,j]
      b[i] = b[i] * a_lu[i,i]

  return b

def r8ge_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8ge_mm() multiplies two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = r8ge_zeros ( n1, n3 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8ge_mm_test ( ):

#*****************************************************************************80
#
## r8ge_mm_test() tests r8ge_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8ge_mm_test():' )
  print ( '  r8ge_mm() computes a matrix-matrix product C = A * B;' )

  a = r8ge_zeros ( n1, n2 )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8ge_mm ( n1, n2, n3, a, b )

  r8ge_print ( n1, n2, a, '  A:' )
  r8ge_print ( n2, n3, b, '  B:' )
  r8ge_print ( n1, n3, c, '  C = A*B:' )

  return

def r8ge_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8ge_mtm() computes A' * B for two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A' * B.
#
  import numpy as np

  c = r8ge_zeros ( n1, n3 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8ge_mtm_test ( ):

#*****************************************************************************80
#
## r8ge_mtm_test() tests r8ge_mtm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 Augsut 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8ge_mtm_test():' )
  print ( '  r8ge_mtm() computes a matrix-matrix product C = A\' * B;' )

  a = r8ge_zeros ( n2, n1 )

  for i in range ( 0, n2 ): 
    for j in range ( 0, n1 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = a

  c = r8ge_mtm ( n1, n2, n3, a, b )

  r8ge_print ( n2, n1, a, '  A:' )
  r8ge_print ( n2, n3, b, '  B:' )
  r8ge_print ( n1, n3, c, '  C = A\'*B:' )

  return

def r8ge_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ge_mtv() multiplies a vector by a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8GE matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j] = x[i] * a[i,j]

  return b

def r8ge_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ge_mv() multiplies an R8GE matrix times a vector.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8GE matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ge_print() prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_test ( ):

#*****************************************************************************80
#
## r8ge_print_test() tests r8ge_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_test():' )
  print ( '  r8ge_print() prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8MAT:' )

  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ge_print_some() prints out a portion of an R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## r8ge_print_some_test() tests r8ge_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_some_test():' )
  print ( '  r8ge_print_some() prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8GE matrix:' )

  return

def r8ge_random ( m, n, rng ):

#*****************************************************************************80
#
## r8ge_random() randomizes a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(M,N), the R8GE matrix.
#
  import numpy as np

  a = rng.random ( size = [ m, n ] )

  return a

def r8ge_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## r8ge_res() computes the residual vector for an R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the original, UNFACTORED R8GE matrix.
#
#    real X(N), the estimated solution.
#
#    real B(M), the right hand side vector.
#
#  Output:
#
#    real R(M), the residual vector, b - A * x.
#
  import numpy as np

  r = np.zeros ( m )

  for i in range ( 0, m ):
    r[i] = b[i]
    for j in range ( 0, n ):
      r[i] = r[i] - a[i,j] * x[j]

  return r

def r8ge_sl ( n, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## r8ge_sl()() solves a system factored by r8ge_fa.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_sl is a simplified version of the LINPACK routine R8GESL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa.
#
#    integer PIVOT(N), the pivot vector from r8ge_fa.
#
#    real B(N), the right hand side vector.
#
#    integer JOB, specifies the operation.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Solve A * x = b.
#
  if ( job == 0 ):
#
#  Solve PL * Y = B.
#
    for k in range ( 0, n - 1 ):

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

      for i in range ( k + 1, n ):
        x[i] = x[i] + a_lu[i,k] * x[k]
#
#  Solve U * X = Y.
#
    for k in range ( n - 1, -1, -1 ):
      x[k] = x[k] / a_lu[k,k]
      for i in range ( 0, k ):
        x[i] = x[i] - a_lu[i,k] * x[k]
#
#  Solve A' * X = B.
#
  else:
#
#  Solve U' * Y = B.
#
    for k in range ( 0, n ):
      for i in range ( 0, k ):
        x[k] = x[k] - x[i] * a_lu[i,k]
      x[k] = x[k] / a_lu[k,k]
#
#  Solve ( PL )' * X = Y.
#
    for k in range ( n - 2, -1, -1 ):
      for i in range ( k + 1, n ):
        x[k] = x[k] + x[i] * a_lu[i,k]

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

  return x

def r8ge_to_r8po ( n, a ):

#*****************************************************************************80
#
## r8ge_to_r8po() copies an R8GE matrix to an R8PO matrix.
#
#  Discussion:
#
#    The R8PO format assumes the matrix is square and symmetric; it is also 
#    typically assumed that the matrix is positive definite.  These are not
#    required here.  The copied R8PO matrix simply zeros out the lower triangle
#    of the R8GE matrix.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8PO storage format is used for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#    R8PO storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8GE matrix.
#
#  Output:
#
#    real B(N,N), the R8PO matrix.
#
  import numpy as np

  b = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      b[i,j] = a[i,j]

  return b

def r8ge_to_r8po_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8po_test() tests r8ge_to_r8po().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8ge_to_r8po_test():' )
  print ( '  r8ge_to_r8po() converts an R8GE matrix to R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ge_random ( n, n )

  r8ge_print ( n, n, a, '  The random R8GE matrix:' )
 
  b = r8ge_to_r8po ( n, a )

  r8po_print ( n, b, '  The R8PO matrix:' )

  return

def r8ge_zeros ( m, n ):

#*****************************************************************************80
#
## r8ge_zeros() zeroes an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(M,N), the zeroed out matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ge_zeros_test ( ):

#*****************************************************************************80
#
## r8ge_zeros_test() tests r8ge_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_zeros_test():' )
  print ( '  r8ge_zeros() zeros out space for a general matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ge_zeros ( m, n )

  r8ge_print ( m, n, a, '  Matrix A:' )

  return

def r8_invchi_pdf ( df, x ):

#*****************************************************************************80
#
## r8_invchi_pdf() evaluates the PDF of an inverse chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#    real X, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from scipy.special import gammaln

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'r8_invchi_pdf(): Fatal error!' )
    print ( '  Degrees of freedom must be positive.' )
    raise Exception ( 'r8_invchi_pdf(): Fatal error!' )

  if ( x <= 0.0 ):

    value = 0.0

  else:

    temp2 = df * 0.5;
    temp1 = - temp2 * np.log ( 2.0 ) - ( temp2 + 1.0 ) * np.log ( x ) \
      - 0.5 / x - gammaln ( temp2 )

    value = np.exp ( temp1 )

  return value

def inverse_chi_square_pdf_values ( n_data ):

#*****************************************************************************80
#
## inverse_chi_square_pdf_values() returns values of the inverse chi square PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real DF, the degrees of freedom.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  df_vec = np.array ( [ \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     3.0, \
     4.0, \
     1.0, \
     2.0, \
     3.0, \
     4.0, \
     5.0, \
     3.0, \
     3.0, \
     3.0, \
     3.0, \
     3.0, \
    10.0, \
    10.0, \
    10.0 ] )
  fx_vec = np.array ( [ \
    0.08500366602520342, \
    0.3368973499542734, \
    0.3661245640481622, \
    1.026062482798735, \
    0.4518059816704532, \
    0.8953274901880941, \
    1.129514954176133, \
    1.119159362735118, \
    0.2419707245191433, \
    0.3032653298563167, \
    0.2419707245191433, \
    0.1516326649281584, \
    0.08065690817304778, \
    0.05492391118346530, \
    0.02166329508030457, \
    0.01100204146138436, \
    0.006457369034861447, \
    0.004162370481945731, \
    0.0007897534631674914, \
    0.00001584474249412852, \
    1.511920090468204E-06 ] )
  x_vec = np.array ( [ \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40, \
    0.40, \
    0.40, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    2.00, \
    3.00, \
    4.00, \
    5.00, \
    6.00, \
    1.00, \
    2.00, \
    3.00 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0.0
    x = 0.0
    fx = 0.0
  else:
    df = df_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1
 
  return n_data, df, x, fx

def r8_invchi_pdf_test ( ):

#*****************************************************************************80
#
## r8_invchi_pdf_test() tests r8_invchi_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_invchi_pdf_test:' )
  print ( '  r8_invchi_pdf returns values of' )
  print ( '  the inverse Chi Square Probability Density Function.' )
  print ( '' )
  print ( '        DF         X         PDF          PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, x, pdf1 = inverse_chi_square_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_invchi_pdf ( df, x )

    print ( '  %8g  %8g  %24.16g  %24.16g' % ( df, x, pdf1, pdf2 ) )

  return

def r8_invchi_sample ( df, rng ):

#*****************************************************************************80
#
## r8_invchi_sample() samples an inverse chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a sample value.
#
  a = 0.5
  b = 0.5 * df

  value = r8_gamma_sample ( a, b, rng )

  if ( value != 0.0 ):
    value = 1.0 / value

  return value

def r8_invchi_sample_test ( rng ):

#*****************************************************************************80
#
## r8_invchi_sample_test() tests r8_invchi_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_invchi_sample_test():' )
  print ( '  r8_invchi_sample() samples an inverse chi square distribution.' )
  print ( '' )
  print ( '           DF               X              PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    df = 5.0 * rng.random ( )
    x = r8_invchi_sample ( df, rng )
    pdf = r8_invchi_pdf ( df, x )
    print ( '  %14.6g  %14.6g  %14.6g' % ( df, x, pdf ) )

  return

def r8_invgam_pdf ( beta, alpha, rval ):

#*****************************************************************************80
#
## r8_invgam_pdf() evaluates the PDF of an inverse gamma distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real BETA, the rate parameter.
#    0.0 < BETA.
#
#    real ALPHA, the shape parameter.
#    0.0 < ALPHA.
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from scipy.special import gammaln

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'r8_invgam_pdf(): Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    raise Exception ( 'r8_invgam_pdf(): Fatal error!' )

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'r8_invgam_pdf(): Fatal error!' )
    print ( '  Parameter BETA is not positive.' )
    raise Exception ( 'r8_invgam_pdf(): Fatal error!' )

  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp = alpha * np.log ( beta ) - ( alpha + 1.0 ) * np.log ( rval ) \
      - beta / rval - gammaln ( alpha )

    value = np.exp ( temp )

  return value

def inverse_gamma_pdf_values ( n_data ):

#*****************************************************************************80
#
## inverse_gamma_pdf_values() returns values of the inverse gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real ALPHA, BETA, the parameters.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 12

  alpha_vec = np.array ( [ \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    2.00, \
    3.00, \
    4.00, \
    5.00 ] )
  beta_vec = np.array ( [ \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    2.00, \
    3.00, \
    4.00, \
    5.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00 ] )
  fx_vec = np.array ( [ \
    0.3032653298563167, \
    0.09735009788392561, \
    0.04702676249392300, \
    0.02757802820576861, \
    0.1839397205857212, \
    0.1673476201113224, \
    0.1353352832366127, \
    0.1026062482798735, \
    0.07606179541223586, \
    0.02535393180407862, \
    0.005634207067573026, \
    0.0009390345112621711 ] )
  x_vec = np.array ( [ \
    1.00, \
    2.00, \
    3.00, \
    4.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00, \
    3.00, \
    3.00, \
    3.00, \
    3.00 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    beta = 0.0
    x = 0.0
    fx = 0.0
  else:
    alpha = alpha_vec[n_data]
    beta = beta_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, beta, x, fx

def r8_invgam_pdf_test ( ):

#*****************************************************************************80
#
## r8_invgam_pdf_test() tests r8_invgam_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_invgam_pdf_test:' )
  print ( '  r8_invgam_pdf evaluates' )
  print ( '  the inverse gamma Probability Density Function.' )
  print ( '' )
  print ( '        ALPHA     BETA       X         PDF       PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, alpha, beta, x, pdf1 = inverse_gamma_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_invgam_pdf ( beta, alpha, x )

    print ( '  %8g  %8g  %8g  %24.16g  %24.16g' % ( alpha, beta, x, pdf1, pdf2 ) )

  return

def r8_invgam_sample ( beta, alpha, rng ):

#*****************************************************************************80
#
## r8_invgam_sample() samples an inverse gamma distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real BETA, the rate parameter.
#    0.0 < BETA.
#
#    real ALPHA, the shape parameter.
#    0.0 < ALPHA.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a sample value.
#
  value = r8_gamma_sample ( beta, alpha, rng )

  if ( value != 0.0 ):
    value = 1.0 / value

  return value

def r8_invgam_sample_test ( rng ):

#*****************************************************************************80
#
## r8_invgam_sample_test() tests r8_invgam_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_invgam_sample_test():' )
  print ( '  r8_invgam_sample() samples an inverse gamma distribution.' )

  print ( '' )
  print ( '           R               A               X              PDF()' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = 5.0 * rng.random ( )
    a = 5.0 * rng.random ( )
    x = r8_invgam_sample ( r, a, rng )
    pdf = r8_invgam_pdf ( r, a, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( r, a, x, pdf ) )

  return

def r8mat_norm_fro_affine ( m, n, a1, a2 ):

#*****************************************************************************80
#
## r8mat_norm_fro_affine() returns the Frobenius norm of an R8MAT difference.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    real A1(M,N), A2(M,N), the matrices for whose difference 
#    the Frobenius norm is desired.
#
#  Output:
#
#    real VALUE, the Frobenius norm of A1 - A2.
#
  import numpy as np
 
  value = np.sqrt ( sum ( sum ( ( a1 - a2 ) ** 2 ) ) )

  return value

def r8mat_norm_fro_affine_test ( rng ):

#*****************************************************************************80
#
## r8mat_norm_fro_affine_test() tests r8mat_norm_fro_affine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4
  a = rng.random ( size = [ m, n ] )
  b = rng.random ( size = [ m, n ] )

  print ( '' )
  print ( 'r8mat_norm_fro_affine_test():' )
  print ( '  r8mat_norm_fro_affine() computes the Frobenius norm' )
  print ( '  of the difference of two R8MAT\'s;' )

  t1 = 0.0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      t1 = t1 + ( a[i,j] - b[i,j] ) ** 2

  t1 = np.sqrt ( t1 );

  t2 = r8mat_norm_fro_affine ( m, n, a, b );

  print ( '' )
  print ( '  Expected norm = %g' % ( t1 ) )
  print ( '  Computed norm = %g' % ( t2 ) )

  return

def r8_normal_01_pdf ( rval ):

#*****************************************************************************80
#
## r8_normal_01_pdf() evaluates the PDF of a standard normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np

  value = np.exp ( - 0.5 * rval ** 2 ) / np.sqrt ( 2.0 * np.pi )

  return value

def r8_normal_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_normal_01_pdf_values() returns some values of the standard Normal PDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0.0, 1.0 ]
#      PDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( ( \
    0.03155059887555709, \
    0.0005094586261557538, \
    0.01235886992552887, \
    0.353192862601275, \
    0.3171212685764107, \
    0.0009653372813755943, \
    0.06083856556197816, \
    0.003066504313116445, \
    0.0005116437388114821, \
    0.2246444116615346 ))

  x_vec = np.array ( ( \
    -2.252653624140994, \
     3.650540612071437, \
     2.636073871461605, \
     0.4935635421351536, \
    -0.6775433481923101, \
    -3.471050120671749, \
    -1.939377660943641, \
    -3.120345651740235, \
    -3.649368017767143, \
     1.0717256984193 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def r8_normal_01_pdf_test ( ):

#*****************************************************************************80
#
## r8_normal_01_pdf_test() tests r8_normal_01_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'r8_normal_01_pdf_test:' )
  print ( '  r8_normal_01_pdf evaluates the standard normal pdf' )
  print ( '  with mean = 0 and standard deviation = 1.' )
  print ( '' )
  print ( '            X                     PDF(0,1)                  PDF(0,1)' )
  print ( '                                  tabulated                 computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, x, pdf1 = r8_normal_01_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_normal_01_pdf ( x )
    print ( '  %24.16g  %24.16g  %24.16g' % ( x, pdf1, pdf2 ) )

  return

def r8_normal_01_sample ( rng ):

#*****************************************************************************80
#
## r8_normal_01_sample() returns a unit pseudonormal R8.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used, which is efficient, but
#    generates two values at a time.  
#
#    Typically, we would use one value and save the other for the next call.
#    However, the fact that this function has saved memory makes it difficult
#    to correctly handle cases where we want to re-initialize the code,
#    or to run in parallel.  Therefore, we will instead use the first value
#    and DISCARD the second.
#
#    EFFICIENCY must defer to SIMPLICITY.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a sample of the standard normal PDF.
#
  import numpy as np

  r1 = rng.random ( )
  r2 = rng.random ( )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  value = x

  return value

def r8_normal_01_sample_test ( rng ):

#*****************************************************************************80
#
## r8_normal_01_sample_test() tests r8_normal_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_normal_01_sample_test():' )
  print ( '  r8_normal_01_sample() samples the normal distribution.' )

  print ( '' )
  print ( '      X        PDF(X)' )
  print ( '' )

  for i in range ( 0, 10 ):
    x = r8_normal_01_sample ( rng )
    pdf = r8_normal_01_pdf ( x )
    print ( '  %14.6g  %14.6g' % ( x, pdf ) )

  return

def r8_normal_pdf ( av, sd, x ):

#*****************************************************************************80
#
## r8_normal_pdf() evaluates the PDF of a normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    Original FORTRAN90 version by Guannan Zhang.
#    This version by John Burkardt.
#
#  Input:
#
#    real AV, the mean value.
#
#    real SD, the standard deviation.
#    0.0 < SD.
#
#    real X, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  import numpy as np

  if ( sd <= 0.0 ):
    print ( '' )
    print ( 'r8_normal_pdf(): Fatal error!' )
    print ( '  Standard deviation must be positive.' )
    raise Exception ( 'r8_normal_pdf(): Fatal error!' )

  rtemp = 0.5 * ( ( x - av ) / sd ) ** 2

  value = np.exp ( - rtemp ) / sd / np.sqrt ( 2.0 * np.pi )

  return value

def r8_normal_pdf_values ( n_data ):

#*****************************************************************************80
#
## r8_normal_pdf_values() returns some values of the Normal PDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ mu, sigma ]
#      PDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real MU, the mean of the distribution.
#
#    real SIGMA, the standard deviation of the distribution.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( ( \
    0.01180775937213258, \
    0.006307849174478944, \
    0.0147514774470322, \
    0.9468437743011001, \
    0.02140312299941794, \
    0.05939959967353488, \
    0.2348929157422787, \
    0.007207515678571277, \
    0.005944396897656727, \
    0.03637663165771322 ))

  mu_vec = np.array ( ( \
   -56.31634060352484, \
     12.33908855337884, \
    -48.48444152359102, \
      26.7931424604825, \
    -19.73874370047668, \
    -99.63232576831896, \
    -81.09104995766396, \
     68.16949013113364, \
    -47.93940044652702, \
    -29.67426801922078 ))

  sigma_vec = np.array ( ( \
    4.785956124893755, \
    2.13500469923221, \
    0.6387882883091059, \
    0.4024634224214489, \
    3.79790008346491, \
    4.497769898408682, \
    0.1667227687589636, \
    0.7032091872463158, \
    4.57117016420902, \
    4.132147851761006 ))

  x_vec = np.array ( ( \
  -46.85424018542929, \
    6.781057314200307, \
  -50.23282168570062, \
   26.67129012408019, \
  -12.9643468135976, \
 -103.6600156181528, \
  -80.73183222587458, \
   66.09155915000321, \
  -58.53544475210675, \
  -35.44773135435396 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, x, f

def r8_normal_pdf_test ( ):

#*****************************************************************************80
#
## r8_normal_pdf_test() tests r8_normal_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'r8_normal_pdf_test:' )
  print ( '  r8_normal_pdf evaluates the normal pdf' )
  print ( '  pdf(mu,sigma) is the normal pdf with' )
  print ( '  mu = mean, sigma = standard deviation.' )
  print ( '' )
  print ( '            MU                       SIGMA                      X' ),
  print ( '                     PDF(MU,SIGMA)             PDF(MU,SIGMA)' )
  print ( '                                                                 ' ),
  print ( '                     tabulated                 computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, mu, sigma, x, pdf1 = r8_normal_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_normal_pdf ( mu, sigma, x )
    print ( '  %24.16g  %24.16g  %24.16g  %24.16g  %24.16g' % ( mu, sigma, x, pdf1, pdf2 ) )

  return

def r8_normal_sample ( av, sd, rng ):

#*****************************************************************************80
#
## r8_normal_sample() generates a normal random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a normal distribution
#    with mean AV, and standard deviation SD.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Extensions of Forsythe's Method for Random
#    Sampling from the Normal Distribution,
#    Mathematics of Computation,
#    Volume 27, Number 124, October 1973, page 927-937.
#
#  Input:
#
#    real AV, the mean.
#
#    real SD, the standard deviation.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  value = sd * r8_normal_01_sample ( rng ) + av

  return value

def r8_normal_sample_test ( rng ):

#*****************************************************************************80
#
## r8_normal_sample_test() tests r8_normal_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_normal_sample_test():' )
  print ( '  r8_normal_sample() samples the normal distribution.' )

  print ( '' )
  print ( '            MU            SIGMA            X       PDF(MU,SIGMA)' )
  print ( '' )

  for i in range ( 0, 10 ):
    mu = -100.0 + 200.0 * rng.random ( )
    sigma = rng.random ( )
    x = r8_normal_sample ( mu, sigma, rng )
    pdf = r8_normal_pdf ( mu, sigma, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( mu, sigma, x, pdf ) )

  return

def r8po_det ( n, a_lu ):

#*****************************************************************************80
#
## r8po_det() computes the determinant of a matrix factored by r8po_fa.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A_LU(N,N), the factor from r8po_fa.
#
#  Output:
#
#    real VALUE, the determinant of A.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i] ** 2

  return value

def r8po_det_test ( ):

#*****************************************************************************80
#
## r8po_det_test() tests r8po_det();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_det_test():' )
  print ( '  r8po_det find the determinant of a positive definite symmetric' )
  print ( '  matrix after it has been factored.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = min ( i, j ) + 1

  r8po_print ( n, a, '  The matrix A:' )
#
#  Get R, the Cholesky factor of A.
#
  r = r8po_fa ( n, a )
#
#  Get the determinant of A.
#
  value = r8po_det ( n, r )
  print ( '' )
  print ( '  Determinant of A = %g' % ( value ) )

  return

def r8po_dif2 ( n ):

#*****************************************************************************80
#
## r8po_dif2() returns the second difference matrix in R8PO format.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  return a

def r8po_dif2_test ( ):

#*****************************************************************************80
#
## r8po_dif2_test() tests r8po_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_dif2_test():' )
  print ( '  r8po_dif2 returns the second difference matrix in R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8po_dif2 ( n )

  r8po_print ( n, a, '  The matrix:' )

  return

def r8po_fa ( n, a ):

#*****************************************************************************80
#
## r8po_fa() factors a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#    The positive definite symmetric matrix A has a Cholesky factorization
#    of the form:
#
#      A = R' * R
#
#    where R is an upper triangular matrix with positive elements on
#    its diagonal.  This routine overwrites the matrix A with its
#    factor R.
#
#    This function failed miserably when I wrote "r = a", because of a
#    disastrously misconceived feature of Python, which does not copy
#    one matrix to another, but makes them both point to the same object.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix in R8PO storage.
#
#  Output:
#
#    real R(N,N), the Cholesky factor R in R8GE storage.
#
#    integer INFO, error flag.
#    0, normal return.
#    K, error condition.  The principal minor of order K is not
#    positive definite, and the factorization was not completed.
#
  import numpy as np

  r = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      r[i,j] = a[i,j]

  for j in range ( 0, n ):

    for k in range ( 0, j ):
      t = 0.0
      for i in range ( 0, k ):
        t = t + r[i,k] * r[i,j]
      r[k,j] = ( r[k,j] - t ) / r[k,k]

    t = 0.0
    for i in range ( 0, j ):
      t = t + r[i,j] ** 2

    s = r[j,j] - t

    if ( s <= 0.0 ):
      print ( '' )
      print ( 'r8po_fa(): Fatal error!' )
      print ( '  Factorization fails on column %d.' % ( j ) )
      raise Exception ( 'r8po_fa(): Fatal error!' )

    r[j,j] = np.sqrt ( s )
#
#  Since the Cholesky factor is stored in R8GE format, be sure to
#  zero out the lower triangle.
#
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      r[i,j] = 0.0

  return r

def r8po_fa_test ( ):

#*****************************************************************************80
#
## r8po_fa_test() tests r8po_fa()();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_fa_test():' )
  print ( '  r8po_fa factors a positive definite symmetric' )
  print ( '  linear system,' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = min ( i, j ) + 1

  r8po_print ( n, a, '  The matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )

  r8ut_print ( n, n, r, '  The factor R (a R8UT matrix):' )
#
#  Compute the product R' * R.
#
  rtr = r8ut_mtm ( n, r, r )

  r8ge_print ( n, n, rtr, '  The product R\' * R:' )

  return

def r8po_indicator ( n ):

#*****************************************************************************80
#
## r8po_indicator() sets up a R8PO indicator matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(N,N), the R8PO matrix.
#
  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8po_indicator_test ( ):

#*****************************************************************************80
#
## r8po_indicator_test() tests r8po_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_indicator_test():' )
  print ( '  r8po_indicator sets up an R8PO indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8po_indicator ( n )

  r8po_print ( n, a, '  The R8PO indicator matrix:' )

  return

def r8po_inverse ( n, r ):

#*****************************************************************************80
#
## r8po_inverse() computes the inverse of a matrix factored by r8po_fa.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real R(N,N), the Cholesky factor, in R8GE storage, returned by r8po_fa.
#
#  Output:
#
#    real B(N,N), the inverse matrix, in R8PO storage.
#
  import numpy as np

  b = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      b[i,j] = r[i,j]
#
#  Compute Inverse ( R ).
#
  for k in range ( 0, n ):

    b[k,k] = 1.0 / b[k,k]
    for i in range ( 0, k ):
      b[i,k] = - b[i,k] * b[k,k]

    for j in range ( k + 1, n ):
      t = b[k,j]
      b[k,j] = 0.0
      for i in range ( 0, k + 1 ):
        b[i,j] = b[i,j] + t * b[i,k]
#
#  Compute Inverse ( R ) * ( Inverse ( R ) )'.
#
  for j in range ( 0, n ):

    for k in range ( 0, j ):
      t = b[k,j]
      for i in range ( 0, k + 1 ):
        b[i,k] = b[i,k] + t * b[i,j]

    t = b[j,j]
    for k in range ( 0, j + 1 ):
      b[k,j] = b[k,j] * t

  return b

def r8po_inverse_test ( ):

#*****************************************************************************80
#
## r8po_inverse_test() tests r8po_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'r8po_inverse_test():' )
  print ( '  r8po_inverse computes the inverse of' )
  print ( '  a symmetric positive definite matrix' )
  print ( '  factored by r8po_fa.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = min ( i, j ) + 1

  r8po_print ( n, a, '  Matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )
#
#  Compute the inverse.
#
  b = r8po_inverse ( n, r )

  r8po_print ( n, b, '  Inverse matrix B:' )
#
#  Check.
#
  c = r8po_mm ( n, a, b )

  r8po_print ( n, c, '  Product A * B:' )

  return

def r8po_mm ( n, a, b ):

#*****************************************************************************80
#
## r8po_mm() multiplies two R8PO matrices.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#    N must be positive.
#
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  import numpy as np

  c = r8po_zeros ( n )
  
  for i in range ( 0, n ):

    for j in range ( i, n ):
      for k in range ( 0, n ):

        if ( i <= k ):
          aik = a[i,k]
        else:
          aik = a[k,i]

        if ( k <= j ):
          bkj = b[k,j]
        else:
          bkj = b[j,k]

        c[i,j] = c[i,j] + aik * bkj

  return c

def r8po_mm_test ( ):

#*****************************************************************************80
#
## r8po_mm_test() tests r8po_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_mm_test():' )
  print ( '  r8po_mm computes the product of two' )
  print ( '  symmetric positive definite matrices.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set (the upper half of) matrix A.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8po_print ( n, a, '  Matrix A:' )
#
#  Set (the upper half of) matrix B.
#
  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    b[i,i] = float ( i + i + 1 )
  for i in range ( 0, n - 1 ):
    b[i,i+1] = float ( i + i + 1 + 1 )

  r8po_print ( n, b, '  Matrix B:' )
#
#  Compute the product.
#
  c = r8po_mm ( n, a, b )

  r8po_print ( n, c, '  Product matrix C = A * B:' )

  return

def r8po_mv ( n, a, x ):

#*****************************************************************************80
#
## r8po_mv() multiplies a R8PO matrix times a vector.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      b[i] = b[i] + a[j,i] * x[j]
    for j in range ( i, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8po_mv_test ( ):

#*****************************************************************************80
#
## r8po_mv_test() tests r8po_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_mv_test():' )
  print ( '  r8po_mv computes the product of an R8PO matrix and a vector.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set (the upper half of) matrix A.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8po_print ( n, a, '  Matrix A:' )
#
#  Set the vector V.
#
  v = r8vec_indicator1 ( n )

  r8vec_print ( n, v, '  Vector V:' )
#
#  Compute the product.
#
  w = r8po_mv ( n, a, v )

  r8vec_print ( n, w, '  Product w = A * v:' )

  return

def r8po_print ( n, a, title ):

#*****************************************************************************80
#
## r8po_print() prints a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an SPO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#    string TITLE, a title to be printed.
#
  r8po_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8po_print_test ( ):

#*****************************************************************************80
#
## r8po_print_test() tests r8po_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8po_print_test():' )
  print ( '  r8po_print prints an R8PO matrix.' )

  n = 5
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0 ], 
    [ 12.0, 22.0, 23.0, 24.0, 25.0, ], 
    [ 13.0, 23.0, 33.0, 34.0, 35.0 ], 
    [ 14.0, 24.0, 34.0, 44.0, 45.0 ],
    [ 14.0, 25.0, 35.0, 45.0, 55.0 ] ], dtype = np.float64 )

  r8po_print ( n, v, '  Here is an R8PO matrix:' )

  return

def r8po_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8po_print_some() prints some of a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( i <= j ):
          print ( '%12g  ' % ( a[i,j] ) ),
        else:
          print ( '%12g  ' % ( a[j,i] ) ),

      print ( '' )

  return

def r8po_print_some_test ( ):

#*****************************************************************************80
#
## r8po_print_some_test() tests r8po_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8po_print_some_test():' )
  print ( '  r8po_print_some prints some of an R8PO matrix.' )

  n = 5
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0 ], 
    [ 12.0, 22.0, 23.0, 24.0, 25.0, ], 
    [ 13.0, 23.0, 33.0, 34.0, 35.0 ], 
    [ 14.0, 24.0, 34.0, 44.0, 45.0 ],
    [ 14.0, 25.0, 35.0, 45.0, 55.0 ] ], dtype = np.float64 )

  r8po_print_some ( n, v, 0, 3, 3, 4, '  Here is an R8PO matrix:' )

  return

def r8po_random ( n, rng ):

#*****************************************************************************80
#
## r8po_random() randomizes a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#    The matrix computed here is not simply a set of random numbers in
#    the nonzero slots of the R8PO array.  It is also a positive definite
#    matrix.  It is computed by setting a "random" upper triangular
#    Cholesky factor R, and then computing A = R'*R.
#    The randomness is limited by the fact that all the entries of
#    R will be between 0 and 1.  A truly random R is only required
#    to have positive entries on the diagonal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(N,N), the R8PO matrix.
#
  import numpy as np

  a = r8po_zeros ( n )

  for i in range ( n - 1, -1, -1 ):
#
#  Set row I of R.
#
    for j in range ( i, n ):
      a[i,j] = rng.random ( )
#
#  Consider element J of row I, last to first.
#
    for j in range ( n - 1, i - 1, -1 ):
#
#  Add multiples of row I to lower elements of column J.
#
      for i2 in range ( i + 1, j + 1 ):
        a[i2,j] = a[i2,j] + a[i,i2] * a[i,j]
#
#  Reset element J.
#
      a[i,j] = a[i,i] * a[i,j]

  return a

def r8po_random_test ( ):

#*****************************************************************************80
#
## r8po_random_test() tests r8po_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_random_test:' )
  print ( '  r8po_random computes a random positive definite' )
  print ( '  symmetric matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8po_random ( n )

  r8po_print ( n, a, '  The random R8PO matrix:' )

  return

def r8po_sl ( n, r, b ):

#*****************************************************************************80
#
## r8po_sl() solves a R8PO system factored by r8po_fa.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real R(N,N), the Cholesky factor, in R8GE storage, 
#    returned by r8po_fa.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Solve R' * y = b.
#
  for k in range ( 0, n ):
    t = 0.0
    for i in range ( 0, k ):
      t = t + x[i] * r[i,k]
    x[k] = ( x[k] - t ) / r[k,k]
#
#  Solve R * x = y.
#
  for k in range ( n - 1, -1, -1 ):
    x[k] = x[k] / r[k,k]
    for i in range ( 0, k ):
      x[i] = x[i] - r[i,k] * x[k]

  return x

def r8po_sl_test ( ):

#*****************************************************************************80
#
## r8po_sl_test() tests r8po_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_sl_test():' )
  print ( '  r8po_sl solves a linear system with an R8PO matrix' )
  print ( '  after it has been factored by r8po_fa.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set (the upper half of) matrix A.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8po_print ( n, a, '  Matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )
#
#  Set the right hand side.
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8po_sl ( n, r, b )
  r8vec_print ( n, x, '  Solution x:' )

  return

def r8po_to_r8ge ( n, a ):

#*****************************************************************************80
#
## r8po_to_r8ge() copies a R8PO matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  b = r8ge_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        b[i,j] = a[i,j]
      else:
        b[i,j] = a[j,i]

  return b

def r8po_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8po_to_r8ge_test() tests r8po_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_to_r8ge_test():' )
  print ( '  r8po_to_r8ge converts a R8PO matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8po_random ( n )

  r8po_print ( n, a, '  The random R8PO matrix:' )
 
  r8ge_print ( n, n, a, '  The random R8PO matrix (printed by r8ge_print):' )

  b = r8po_to_r8ge ( n, a )

  r8ge_print ( n, n, b, '  The random R8GE matrix (printed by r8ge_print):' )

  return

def r8po_zeros ( n ):

#*****************************************************************************80
#
## r8po_zeros() zeroes an R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is used for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#    R8PO storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(N,N), the R8PO matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  return a

def r8po_zeros_test ( ):

#*****************************************************************************80
#
## r8po_zeros_test() tests r8po_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_zeros_test():' )
  print ( '  r8po_zeros zeros out space for a' )
  print ( '  symmetric positive definite matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8po_zeros ( n )

  r8po_print ( n, a, '  Matrix A:' )

  return

def r8_scinvchi_pdf ( df, s, x ):

#*****************************************************************************80
#
## r8_scinvchi_pdf(): PDF for a scaled inverse chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#    real S, the scale factor.
#    0.0 < S.
#
#    real X, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF.
#
  import numpy as np
  from scipy.special import gammaln

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'r8_scinvchi_pdf(): Fatal error!' )
    print ( '  Degrees of freedom must be positive.' )
    raise Exception ( 'r8_scinvchi_pdf(): Fatal error!' )

  if ( s <= 0.0 ):
    print ( '' )
    print ( 'r8_scinvchi_pdf(): Fatal error!' )
    print ( '  Scale parameter must be positive.' )
    raise Exception ( 'r8_scinvchi_pdf(): Fatal error!' )

  if ( x <= 0.0 ):

    value = 0.0

  else:

    temp2 = df * 0.5
    temp1 = temp2 * np.log ( temp2 ) + temp2 * np.log ( s ) \
      - ( temp2 * s / x ) \
      - ( temp2 + 1.0 ) * np.log ( x ) - gammaln ( temp2 )

    value = np.exp ( temp1 )

  return value

def scaled_inverse_chi_square_pdf_values ( n_data ):

#*****************************************************************************80
#
## scaled_inverse_chi_square_pdf_values(): scaled inverse chi square PDF values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real DF, the degrees of freedom.
#
#    real XI, the scale parameter.
#
#    real X, the argument of the function.
#
#    Output real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  df_vec = np.array ( [ \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0 ] )
  fx_vec = np.array ( [ \
     0.7322491280963244, \
     0.3368973499542734, \
     0.9036119633409063, \
     1.026062482798735, \
     0.5968580144169457, \
     0.8953274901880941, \
     0.08500366602520342, \
     0.004539992976248485, \
     0.3661245640481622, \
     0.1684486749771367, \
     0.4518059816704532, \
     0.5130312413993675, \
     0.0008099910956089117, \
     4.122307244877116E-07, \
     0.04250183301260171, \
     0.002269996488124243, \
     0.1830622820240811, \
     0.08422433748856834 ] )
  x_vec = np.array ( [ \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40, \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40, \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40 ] )
  xi_vec = np.array ( [ \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0.0
    xi = 0.0
    x = 0.0
    fx = 0.0
  else:
    df = df_vec[n_data]
    xi = xi_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, df, xi, x, fx

def r8_scinvchi_pdf_test ( ):

#*****************************************************************************80
#
## r8_scinvchi_pdf_test() tests r8_scinvchi_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_scinvchi_pdf_test:' )
  print ( '  r8_scinvchi_pdf evaluates' )
  print ( '  the scaled inverse Chi Square Probability Density Function.' )
  print ( '' )
  print ( '        DF        XI         X         PDF       PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, xi, x, pdf1 = scaled_inverse_chi_square_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_scinvchi_pdf ( df, xi, x  )

    print ( '  %8g  %8g  %8g  %24.16g  %24.16g' % ( df, xi, x, pdf1, pdf2 ) )

  return

def r8_scinvchi_sample ( df, s, rng ):

#*****************************************************************************80
#
## r8_scinvchi_sample(): sample a scaled inverse chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#    real S, the scale factor.
#    0.0 < S.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a sample value.
#
  a = 0.5 * df * s
  b = 0.5 * df

  value = r8_gamma_sample ( a, b, rng )

  if ( value != 0.0 ):
    value = 1.0 / value

  return value

def r8_scinvchi_sample_test ( rng ):

#*****************************************************************************80
#
## r8_scinvchi_sample_test() tests r8_scinvchi_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_scinvchi_sample_test():' )
  print ( '  r8_scinvchi_sample() samples a scaled inverse chi square distribution.' )
  print ( '' )
  print ( '           DF              XI               X              PDF' )
  print ( '' )

  for i in range ( 0, 10 ):
    df = 5.0 * rng.random ( )
    xi = 5.0 * rng.random ( )
    x = r8_scinvchi_sample ( df, xi, rng )
    pdf = r8_scinvchi_pdf ( df, xi, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( df, xi, x, pdf ) )

  return

def r8_uni_01 ( ):

#*****************************************************************************80
#
## r8_uni_01() returns a uniform random real number in [0,1].
#
#  Discussion:
#
#    This procedure returns a random floating point number from a uniform
#    distribution over (0,1), not including the endpoint values, using the
#    current random number generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Output:
#
#    real VALUE, a uniform random value in [0,1].
#

#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'r8_uni_01:' )
    print ( '  Initializing RNGLIB package.' )
    initialize ( )
#
#  Get a random positive integer.
#
  i = i4_uni ( )
#
#  Scale it to a random real in [0,1].
#
  value = i * 4.656613057E-10

  return value

def r8_uni_01_test ( ):

#*****************************************************************************80
#
## r8_uni_01_test() tests r8_uni_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_uni_01_test():' )
  print ( '  r8_uni_01 produces a sequence of random values.' )

  print ( '' )
  print ( '  r8_uni_01()' )
  print ( '' )
  for i in range ( 0, 10 ):
    x = r8_uni_01 ()
    print ( '  %g' % ( x ) )

  return

def r8_uniform_01_pdf ( rval ):

#*****************************************************************************80
#
## r8_uniform_01_pdf() evaluates the PDF of a standard uniform distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  if ( rval < 0.0 ):
    value = 0.0
  elif ( rval <= 1.0 ):
    value = 1.0
  else:
    value = 0.0

  return value

def r8_uniform_01_pdf_test ( rng ):

#*****************************************************************************80
#
## r8_uniform_01_pdf_test() tests r8_uniform_01_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_uniform_01_pdf_test():' )
  print ( '  r8_uniform_01_pdf() evaluates the standard uniform PDF.' )
  print ( '' )
  print ( '            X                           PDF()' )
  print ( '' )
  
  for i in range ( 0, 10 ):

    x = - 0.5 + 2.0 * rng.random ( )
 
    pdf = r8_uniform_01_pdf ( x )
    print ( '  %24.16g  %14.6g' % ( x, pdf ) )

  return

def r8_uniform_01_sample ( rng ):

#*****************************************************************************80
#
## r8_uniform_01_sample() generates a uniform random deviate from [0,1].
#
#  Discussion:
#
#    This function should be the only way that the package accesses random
#    numbers.
#
#    Setting OPTION to 0 accesses the r8_uni_01() function in RNGLIB,
#    for which there are versions in various languages, which should result
#    in the same values being returned.  This should be the only function
#    that invokes a function from RNGLIB.
#
#    Setting OPTION to 1 in the This version calls the system
#    RNG "rand()".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real VALUE, a random deviate from the distribution.
#
#    rng: the current random number generator.
#
  import numpy as np

  option = 0

  if ( option == 0 ):
    value = r8_uni_01 ( )
  else:
    value = rng.random ( )
 
  return value

def r8_uniform_01_sample_test ( rng ):

#*****************************************************************************80
#
## r8_uniform_01_sample_test() tests r8_uniform_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  print ( '' )
  print ( 'r8_uniform_01_sample_test():' )
  print ( '  r8_uniform_01_sample returns random values in [0,1]:' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_uniform_01_sample ( rng )
    print ( '  %g' % ( r ) )

  return

def r8_uniform_pdf ( lower, upper, rval ):

#*****************************************************************************80
#
## r8_uniform_pdf() evaluates the PDF of a uniform distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real LOWER, UPPER, the lower and upper range limits.
#    LOWER < UPPER.
#
#    real RVAL, the point where the PDF is evaluated.
#
#  Output:
#
#    real VALUE, the value of the PDF at RVAL.
#
  if ( upper <= lower ):
    print ( '' )
    print ( 'r8_uniform_pdf(): Fatal error!' )
    print ( '  For uniform PDF, the lower limit must be ' )
    print ( '  less than the upper limit.' )
    raise Exception ( 'r8_uniform_pdf(): Fatal error!' )

  if ( rval < lower ):
    value = 0.0
  elif ( rval <= upper ):
    value = 1.0 / ( upper - lower )
  else:
    value = 0.0

  return value

def r8_uniform_pdf_test ( rng ):

#*****************************************************************************80
#
## r8_uniform_pdf_test() tests r8_uniform_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_uniform_pdf_test():' )
  print ( '  r8_uniform_pdf() evaluates the uniform pdf over [A,B].' )
  print ( '' )
  print ( '            A               B               X           PDF()' )
  print ( '' )
  
  for i in range ( 0, 10 ):

    a = -100.0 + 200.0 * rng.random ( )
    b = -100.0 + 200.0 * rng.random ( )
    t = max ( a, b )
    a = min ( a, b )
    b = t
    x = -100.0 + 200.0 * rng.random ( )

    pdf = r8_uniform_pdf ( a, b, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( a, b, x, pdf ) )

  return

def r8_uniform_sample ( a, b, rng ):

#*****************************************************************************80
#
## r8_uniform_sample() generates a uniform random deviate from [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real A, B, the lower and upper limits of the interval.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  import numpy as np

  if ( b <= a ):
    print ( '' )
    print ( 'r8_uniform_sample(): Fatal error!' )
    print ( '  For uniform PDF, the lower limit must be ' )
    print ( '  less than the upper limit.' )
    raise Exception ( 'r8_uniform_sample(): Fatal error!' )

  value = a + ( b - a ) * rng.random ( )
 
  return value

def r8_uniform_sample_test ( rng ):

#*****************************************************************************80
#
## r8_uniform_sample_test() tests r8_uniform_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_uniform_sample_test():' )
  print ( '  r8_uniform_sample() returns random values in [A,B]:' )
  print ( '' )
  print ( '            A               B               R' )
  print ( '' )

  for i in range ( 0, 10 ):

    a = - 100.0 + 200.0 * rng.random ( )
    b = - 100.0 + 200.0 * rng.random ( )
    t = max ( a, b )
    a = min ( a, b )
    b = t
    r = r8_uniform_sample ( a, b, rng )
    print ( '  %14.6g  %14.6g  %14.6g' % ( a, b, r ) )

  return

def r8ut_indicator ( m, n ):

#*****************************************************************************80
#
## r8ut_indicator() sets up a R8UT indicator matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#    M and N must be positive.
#
#  Output:
#
#    real A(M,N), the R8UT matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8ut_zeros ( m, n )
  for i in range ( 0, m ):
    jhi = min ( i, n )
    for j in range ( i, n ):
      a[i,j] = float ( fac * i + j )

  return a

def r8ut_indicator_test ( ):

#*****************************************************************************80
#
## r8ut_indicator_test() tests r8ut_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_indicator_test():' )
  print ( '  r8ut_indicator sets up an indicator matrix in R8UT format' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = r8ut_indicator ( m, n )

  r8ut_print ( m, n, a, '  The indicator matrix:' )

  return

def r8ut_mm ( n, a, b ):

#*****************************************************************************80
#
## r8ut_mm() computes C = A * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will also be an upper trangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#    N must be positive.
#
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  c = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      for k in range ( i, j + 1 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8ut_mm_test ( ):

#*****************************************************************************80
#
## r8ut_mm_test() tests r8ut_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5
 
  print ( '' )
  print ( 'r8ut_mm_test():' )
  print ( '  r8ut_mm computes C = A * B for R8UT matrices.' )
 
  a = r8ut_zeros ( n, n )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = 1.0

  r8ut_print ( n, n, a, '  The matrix A:' )

  c = r8ut_mm ( n, a, a )
  r8ut_print ( n, n, c, '  The product C = A * A' )

  return

def r8ut_mtm ( n, a, b ):

#*****************************************************************************80
#
## r8ut_mtm() computes C = A' * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will NOT be an R8UT matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#    N must be positive.
#
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  c = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k_hi = min ( i + 1, j + 1 )
      for k in range ( 0, k_hi ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8ut_mtm_test ( ):

#*****************************************************************************80
#
## r8ut_mtm_test() tests r8ut_mtm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5
 
  print ( '' )
  print ( 'r8ut_mtm_test():' )
  print ( '  r8ut_mtm computes C = A\' * B for R8UT matrices.' )
 
  a = r8ut_zeros ( n, n )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = 1.0

  r8ut_print ( n, n, a, '  The matrix A:' )

  c = r8ut_mtm ( n, a, a )
  r8ge_print ( n, n, c, '  The product C = A\' * A' )

  return

def r8ut_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ut_mtv()() multiplies a vector by a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    jhi = min ( i + 1, m )
    for j in range ( 0, jhi ):
      b[i] = b[i] + x[j] * a[j,i]

  return b

def r8ut_mtv_test ( ):

#*****************************************************************************80
#
## r8ut_mtv_test() tests r8ut_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_mtv_test():' )
  print ( '  r8ut_mtv computes a matrix product b=A\'*x for an R8UT matrix.' )

  a = r8ut_indicator ( m, n )
  r8ut_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector X:' )

  b = r8ut_mtv ( m, n, a, x )
  r8vec_print ( n, b, '  The vector b=A''*x:' )

  return

def r8ut_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ut_mv() multiplies a R8UT matrix times a vector.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( i, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ut_mv_test ( ):

#*****************************************************************************80
#
## r8ut_mv_test() tests r8ut_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_mv_test():' )
  print ( '  r8ut_mv computes a product b=A*x for an R8UT matrix.' )

  a = r8ut_indicator ( m, n )
  r8ut_print ( m, n, a, '  The R8UT matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Vector x:' )

  b = r8ut_mv ( m, n, a, x )
  r8vec_print ( m, b, '  Vector b = A*x:' )

  return

def r8ut_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ut_print() prints a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    string TITLE, a title to be printed.
#
  r8ut_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ut_print_test ( ):

#*****************************************************************************80
#
## r8ut_print_test() tests r8ut_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ut_print_test():' )
  print ( '  r8ut_print prints an R8UT matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [  0.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [  0.0,  0.0, 33.0, 34.0, 35.0, 36.0 ], 
    [  0.0,  0.0,  0.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ut_print ( m, n, v, '  Here is an R8MAT:' )

  return

def r8ut_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ut_print_some() prints some of a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )
#
#  Determine the range of the rows in this strip.
#
    inc = j2hi + 1 - j2lo
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )
    i2hi = min ( i2hi, j2hi )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( j < i ):
          print ( '              ' ),
        else:
          print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

def r8ut_print_some_test ( ):

#*****************************************************************************80
#
## r8ut_print_some_test() tests r8ut_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ut_print_some_test():' )
  print ( '  r8ut_print_some prints some of an R8UT matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [  0.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [  0.0,  0.0, 33.0, 34.0, 35.0, 36.0 ], 
    [  0.0,  0.0,  0.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ut_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8UT matrix:' )

  return

def r8ut_sl ( n, a, b ):

#*****************************************************************************80
#
## r8ut_sl() solves a linear system A*x=b with an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8UT matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )
  
  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( n - 1, -1, -1 ):
    x[j] = x[j] / a[j,j]
    for i in range ( 0, j ):
      x[i] = x[i] - a[i,j] * x[j]

  return x

def r8ut_sl_test ( ):

#*****************************************************************************80
#
## r8ut_sl_test() tests r8ut_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8ut_sl_test():' )
  print ( '  r8ut_sl solves a linear system A*x=b with R8UT matrix' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( j + 1 )

  r8ut_print ( n, n, a, '  The upper triangular matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ut_mv ( n, n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8ut_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8ut_slt ( n, a, b ):

#*****************************************************************************80
#
## r8ut_slt() solves a linear system A'*x=b with an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8UT matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 0, n ):
    x[j] = x[j] / a[j,j]
    for i in range ( j + 1, n ):
      x[i] = x[i] - x[j] * a[j,i]

  return x

def r8ut_slt_test ( ):

#*****************************************************************************80
#
## r8ut_slt_test() tests r8ut_slt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'r8ut_slt_test():' )
  print ( '  r8ut_slt solves a linear system A''x=b with R8UT matrix' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( j + 1 )

  r8ut_print ( n, n, a, '  The upper triangular matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ut_mtv ( n, n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8ut_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8ut_zeros ( m, n ):

#*****************************************************************************80
#
## r8ge_zeros() zeroes an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ut_zeros_test ( ):

#*****************************************************************************80
#
## r8ut_zeros_test() tests r8ut_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_zeros_test():' )
  print ( '  r8ut_zeros zeros out space for an R8UT matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ut_zeros ( m, n )

  r8ut_print ( m, n, a, '  Matrix A:' )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_multinormal_pdf ( n, mu, r, c_det, x ):

#*****************************************************************************80
#
## r8vec_multinormal_pdf() evaluates a multivariate normal PDF.
#
#  Discussion:
#
#    PDF ( MU(1:N), C(1:N,1:N); X(1:N) ) = 
#      1 / ( 2 * pi ) ^ ( N / 2 ) * 1 / det ( C )
#      * exp ( - ( X - MU )' * inverse ( C ) * ( X - MU ) / 2 )
#
#    Here,
#
#      X is the argument vector of length N,
#      MU is the mean vector of length N,
#      C is an N by N positive definite symmetric covariance matrix.
#
#    The properties of C guarantee that it has an upper triangular
#    matrix R, the Cholesky factor, such that C = R' * R.  It is the
#    matrix R that is required by this routine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the spatial dimension.
#
#    real MU(N), the mean vector.
#
#    real R(N,N), the upper triangular Cholesky
#    factor of the covariance matrix C.
#
#    real C_det, the determinant of the
#    covariance matrix C.
#
#    real X(N), a sample of the distribution.
#
#  Output:
#
#    real VALUE, the PDF evaluated
#    at X.
#
  import numpy as np
#
#  Compute:
#    inverse(R')*(x-mu) = y
#  by solving:
#    R'*y = x-mu
#
  b = x - mu
  y = r8ut_slt ( n, r, b )
#
#  Compute:
#    (x-mu)' * inv(C)          * (x-mu)
#  = (x-mu)' * inv(R'*R)       * (x-mu)
#  = (x-mu)' * inv(R) * inv(R) * (x-mu)
#  = y' * y.
#
  xcx = np.dot ( y, y )

  value = 1.0 / np.sqrt ( ( 2.0 * np.pi ) ** n ) \
  * 1.0 / np.sqrt ( c_det ) \
  * np.exp ( - 0.5 * xcx )

  return value

def r8vec_multinormal_pdf_test ( rng ):

#*****************************************************************************80
#
## r8vec_multinormal_pdf_test() tests r8vec_multinormal_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  initialize ( )

  n = 5

  print ( '' )
  print ( 'r8vec_multinormal_pdf_test():' )
  print ( '  r8vec_multinormal_pdf() evaluates the PDF for the' )
  print ( '  multinormal distribution.' )
  print ( '' )
  print ( '  The covariance matrix is C.' )
  print ( '  The definition uses the inverse of C;' )
  print ( '  r8vec_multinormal_pdf uses the Cholesky factor R' )
  print ( '  Verify that the algorithms are equivalent.' )
#
#  Generate a random upper triangular matrix with positive diagonal.
#
  r1 = r8ut_zeros ( n, n )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      r1[i,j] = rng.random ( )

  r8ut_print ( n, n, r1, '  R1:' );
#
#  Compute a positive definite symmetric covariance matrix C.
#
  c_ge = np.dot ( np.transpose ( r1 ), r1 )

  r8ge_print ( n, n, c_ge, '  C:' )
#
#  Convert to R8PO format.
#
  c = r8ge_to_r8po ( n, c_ge )
#
#  Compute the Cholesky factor R.
#
  r2 = r8po_fa ( n, c )

  r8ut_print ( n, n, r2, '  R2:' );
#
#  Compute the determinant of C.
#
  c_det = r8po_det ( n, r2 )
  print ( '' )
  print ( '  Determinant of C = %g' % ( c_det ) )
#
#  Compute the inverse of C.
#
  c_inv = r8po_inverse ( n, r2 )
  r8po_print ( n, c_inv, '  inverse(C):' )
#
#  Compute a random set of means.
#
  mu = np.zeros ( n )
  for i in range ( 0, n ):
    mu[i] = r8_normal_01_sample ( rng )
  r8vec_print ( n, mu, '  MU:' )
#
#  Compute X as small variations from MU.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    eps = 0.01 * r8_normal_01_sample ( rng )
    x[i] = ( 1.0 + eps ) * mu[i]
  r8vec_print ( n, x, '  X: ' );
#
#  Compute PDF1 from the function.
#
  pdf1 = r8vec_multinormal_pdf ( n, mu, r2, c_det, x )
#
#  Compute PDF2 from the definition.
#
  y = x - mu

  ciy = r8po_mv ( n, c_inv, y )

  xcx = np.dot ( y, ciy )

  pdf2 = 1.0 / np.sqrt ( ( 2.0 * np.pi ) ** n ) \
  * 1.0 / np.sqrt ( c_det ) * np.exp ( - 0.5 * xcx )

  print ( '' )
  print ( '  PDF1 = ', pdf1 )
  print ( '  PDF2 = ', pdf2 )

  return

def r8vec_multinormal_sample ( n, mu, r, rng ):

#*****************************************************************************80
#
## r8vec_multinormal_sample() samples a multivariate normal PDF.
#
#  Discussion:
#
#    PDF ( MU(1:N), C(1:N,1:N); X(1:N) ) = 
#      1 / ( 2 * pi ) ^ ( N / 2 ) * 1 / sqrt ( det ( C ) )
#      * exp ( - ( X - MU )' * inverse ( C ) * ( X - MU ) / 2 )
#
#    Here,
#
#      X is the argument vector of length N,
#      MU is the mean vector of length N,
#      C is an N by N positive definite symmetric covariance matrix.
#
#    The properties of C guarantee that it has an upper triangular
#    matrix R, the Cholesky factor, such that C = R' * R.  It is the
#    matrix R that is required by this routine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the spatial dimension.
#
#    real MU(N), the mean vector.
#
#    real R(N,N), the upper triangular Cholesky
#    factor of the covariance matrix C.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), a sample of the distribution.
#
  import numpy as np
#
#  Compute X = MU + R' * Z
#  where Z is a vector of standard normal variates.
#
  z = np.zeros ( n );
  for j in range ( 0, n ):
    z[j] = r8_normal_01_sample ( rng )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = mu[i]
    for j in range ( 0, i + 1 ):
      x[i] = x[i] + r[j,i] * z[j]

  return x

def r8vec_multinormal_sample_test ( rng ):

#*****************************************************************************80
#
## r8vec_multinormal_sample_test() tests r8vec_multinormal_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  initialize ( )

  n = 5
#
#  Set the covariance matrix C.
#
  c = r8po_dif2 ( n )
#
#  Set the determinant.
#
  c_det = float ( n + 1 )
#
#  Set the upper triangular Cholesky factor.
#
  r = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    r[i,i] = np.sqrt ( float ( i + 2 ) ) / np.sqrt ( float ( i + 1 ) )

  for i in range ( 1, n ):
    r[i-1,i] = - np.sqrt ( float ( i ) ) / np.sqrt ( float ( i + 1 ) )

  print ( '' )
  print ( 'r8vec_multinormal_sample_test():' )
  print ( '  r8vec_multinormal_sample() samples the multinormal distribution.' )
  print ( '' )
  print ( '     N     I      MU        X           PDF()' )

  for k in range ( 0, 10 ):
    mu = -5.0 + 10.0 * rng.random ( size = n )
    x = r8vec_multinormal_sample ( n, mu, r, rng )
    pdf = r8vec_multinormal_pdf ( n, mu, r, c_det, x )
    print ( '' )
    for i in range ( 0, n ):
      print ( '        %4d  %8.4f  %8.4f' % ( i, mu[i], x[i] ) )
    print ( '  %4d                            %14.6g' % ( n, pdf ) )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def set_initial_seed ( ig1, ig2 ):

#*****************************************************************************80
#
## set_initial_seed() resets the initial seed and state for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer IG1, IG2, the initial seed values
#    for the first generator.
#    1 <= IG1 < 2147483563
#    1 <= IG2 < 2147483399
#
  a1_vw = 2082007225
  a2_vw = 784306273
  g_max = 32
  m1 = 2147483563
  m2 = 2147483399

  if ( ig1 < 1 or m1 <= ig1 ):
    print ( '' )
    print ( 'set_initial_seed(): Fatal error!' )
    print ( '  Input parameter IG1 out of bounds.' )
    raise Exception ( 'set_initial_seed(): Fatal error!' )

  if ( ig2 < 1 or m2 <= ig2 ):
    print ( '' )
    print ( 'set_initial_seed(): Fatal error!' )
    print ( '  Input parameter IG2 out of bounds.' )
    raise Exception ( 'set_initial_seed(): Fatal error!' )
#
#  Because INITIALIZE calls set_initial_seed, it's not easy to correct
#  the error that arises if set_initial_seed is called before INITIALIZE.
#  So don't bother trying.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'set_initial_seed(): Fatal error!' )
    print ( '  The RNGLIB package has not been initialized.' )
    raise Exception ( 'set_initial_seed(): Fatal error!' )
#
#  Set the initial seed, then initialize the first generator.
#
  g = 1
  cgn_set ( g )

  ig_set ( g, ig1, ig2 )

  t = 0
  init_generator ( t )
#
#  Now do similar operations for the other generators.
#
  for g in range ( 2, g_max + 1 ):
    cgn_set ( g )
    ig1 = multmod ( a1_vw, ig1, m1 )
    ig2 = multmod ( a2_vw, ig2, m2 )
    ig_set ( g, ig1, ig2 )
    init_generator ( t )
#
#  Now choose the first generator.
#
  g = 1
  cgn_set ( g )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  pdflib_test ( )
  timestamp ( )
 
