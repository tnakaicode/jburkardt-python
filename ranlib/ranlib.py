#! /usr/bin/env python3
#
def genbet ( aa, bb ):

#*****************************************************************************80
#
## genbet() generates a beta random deviate.
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
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Reference:
#
#    Russell Cheng,
#    Generating Beta Variates with Nonintegral Shape Parameter Values,
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
#  Output:
#
#    real VALUE, a beta random variate.
#
  from rnglib import r4_uni_01
  import numpy as np

  if ( aa <= 0.0 ):
    fprintf ( 1, '' )
    fprintf ( 1, 'genbet(): Fatal error!' )
    fprintf ( 1, '  AA <= 0.0' )
    raise Exception ( 'genbet(): Fatal error!' )

  if ( bb <= 0.0 ):
    fprintf ( 1, '' )
    fprintf ( 1, 'genbet(): Fatal error!' )
    fprintf ( 1, '  BB <= 0.0' )
    raise Exception ( 'genbet(): Fatal error!' )
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

      u1 = r4_uni_01 ( )
      u2 = r4_uni_01 ( )
      v = beta * np.log ( u1 / ( 1.0 - u1 ) )
#
#  EXP ( V ) replaced by r4_exp ( V ), to truncate at large magnitude inputs.
#
      w = a * r4_exp ( v )

      z = u1 ** 2 * u2
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

      u1 = r4_uni_01 ( )
      u2 = r4_uni_01 ( )

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
            value = b / ( b + w )

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

def genbet_test ( phrase ):

#*****************************************************************************80
#
## genbet_test() tests genbet(), which generates Beta deviates.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2019
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'genbet_test():' )
  print ( '  genbet() generates Beta deviates.' )
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

  low = 1.0
  high = 10.0
  b = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameter values:' )
  print ( '' )
  print ( '  A = %g' % ( a ) )
  print ( '  B = %g' % ( b ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = genbet ( a, b )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'bet'
  param = np.array ( [ a, b ] )

  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )

  return

def genchi ( df ):

#*****************************************************************************80
#
## genchi() generates a Chi-Square random deviate.
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
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  if ( df <= 0.0 ):
    print ( ' ' )
    print ( 'genchi(): Fatal error!' )
    print ( '  DF <= 0.' )
    print ( '  Value of DF: %g' % ( df ) )
    raise Exception ( 'genchi(): Fatal error!' )

  arg1 = 1.0
  arg2 = df / 2.0

  value = 2.0 * gengam ( arg1, arg2 )

  return value

def genchi_test ( phrase ):

#*****************************************************************************80
#
## genchi_test() tests genchi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'genchi_test():' )
  print ( '  genchi() generates Chi-square deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def genexp ( av ):

#*****************************************************************************80
#
## genexp generates an exponential random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from an exponential
#    distribution with mean AV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Computer Methods for Sampling From the
#    Exponential and Normal Distributions,
#    Communications of the ACM,
#    Volume 15, Number 10, October 1972, pages 873-882.
#
#  Input:
#
#    real AV, the mean of the exponential distribution
#    from which a random deviate is to be generated.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  value = sexpo ( ) * av

  return value

def genexp_test ( phrase ):

#*****************************************************************************80
#
## genexp_test() tests genexp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'genexp_test():' )
  print ( '  genexp() generates exponential deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def genf ( dfn, dfd ):

#*****************************************************************************80
#
## genf generates an F random deviate.
#
#  Discussion:
#
#    This procedure generates a random deviate from the F (variance ratio)
#    distribution with DFN degrees of freedom in the numerator
#    and DFD degrees of freedom in the denominator.
#
#    It directly generates the ratio of chisquare variates
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real DFN, the numerator degrees of freedom.
#    0.0 < DFN.
#
#    real DFD, the denominator degrees of freedom.
#    0.0 < DFD.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  if ( dfn <= 0.0 ):
    print ( ' ' )
    print ( 'genf(): Fatal error!' )
    print ( '  DFN <= 0.0' )
    raise Exception ( 'genf(): Fatal error!' )

  if ( dfd <= 0.0 ):
    print ( ' ' )
    print ( 'genf(): Fatal error!' )
    print ( '  DFD <= 0.0' )
    raise Exception ( 'genf(): Fatal error!' )

  xnum = genchi ( dfn ) / dfn
  xden = genchi ( dfd ) / dfd
  value = xnum / xden

  return value

def genf_test ( phrase ):

#*****************************************************************************80
#
## genf_test() tests genf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 10000

  print ( '' )
  print ( 'genf_test():' )
  print ( '  genf() generates F deviates.' )
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
  high = 10.0
  dfn = genunf ( low, high )

  low = 5.0
  high = 10.0
  dfd = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameter values:' )
  print ( '' )
  print ( '  DFN =   %g' % ( dfn ) )
  print ( '  DFD =   %g' % ( dfd ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = genf ( dfn, dfd )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'f'
  param = np.array ( [ dfn, dfd ] )

  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )

  return

def gengam ( a, r ):

#*****************************************************************************80
#
## gengam() generates a Gamma random deviate.
#
#  Discussion:
#
#    This procedure generates random deviates from the gamma distribution whose
#    density is (A^R)/Gamma(R) * X^(R-1) * Exp(-A*X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
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
#    real A, the location parameter.
#
#    real R, the shape parameter.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  value = sgamma ( r ) / a

  return value

def gengam_test ( phrase ):

#*****************************************************************************80
#
## gengam_test() tests gengam().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'gengam_test():' )
  print ( '  gengam() generates Gamma deviates.' )
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

  low = 1.0
  high = 10.0
  r = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameter values:' )
  print ( '' )
  print ( '  A = %g' % ( a ) )
  print ( '  R = %g' % ( r ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = gengam ( a, r )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'gam'
  param = np.array ( [ a, r ] )
  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )

  return

def genmn ( parm ):

#*****************************************************************************80
#
## genmn() generates a multivariate normal deviate.
#
#  Discussion:
#
#    The method is:
#    1) Generate P independent standard normal deviates - Ei ~ N(0,1)
#    2) Using Cholesky decomposition find A so that A'*A = COVM
#    3) A' * E + MEANV ~ N(MEANV,COVM)
#
#    Note that PARM contains information needed to generate the
#    deviates, and is set up by setgmn.
#
#    PARM(1) contains the size of the deviates, P
#    PARM(2:P+1) contains the mean vector.
#    PARM(P+2:P*(P+3)/2+1) contains the upper half of the Cholesky
#    decomposition of the covariance matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real PARM(P*(P+3)/2+1), parameters set by setgmn.
#
#  Output:
#
#    real X(P), a random deviate from the distribution.
#
  import numpy as np

  p = int ( parm[0] )
#
#  Generate P independent normal deviates.
#
  work = np.zeros ( p )
  for i in range ( 0, p ):
    work[i] = snorm ( )
#
#  Compute X = MEANV + A' * WORK
#
  x = np.zeros ( p )

  for i in range ( 1, p + 1 ):
    k = 0
    ae = 0.0
    for j in range ( 1, i + 1 ):
      k = k + j - 1
      ae = ae + parm[i+(j-1)*p-k+p] * work[j-1]

    x[i-1] = ae + parm[i]

  return x

def setgmn ( meanv, covm, p ):

#*****************************************************************************80
#
## setgmn() sets data for the generation of multivariate normal deviates.
#
#  Discussion:
#
#    This procedure packs P, MEANV, and the Cholesky factorization of
#    COVM in PARM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real MEANV(P), the means of the multivariate
#    normal distribution.
#
#    real COVM(P,P).  On the covariance
#    matrix of the multivariate distribution.  On the information
#    in COVM has been overwritten.
#
#    integer P, the number of dimensions.
#
#  Output:
#
#    real PARM(P*(P+3)/2+1), parameters needed to generate
#    multivariate normal deviates.
#
  import numpy as np

  parm = np.zeros ( p * ( p + 3 ) / 2 + 1 )

  if ( p <= 0 ):
    print ( '' )
    print ( 'setgmn(): Fatal error!' )
    print ( '  P was not positive.' )
    raise Exception ( 'setgmn(): Fatal error!' )
#
#  Store P.
#
  parm[0] = p
#
#  Store MEANV.
#
  for i in range ( 1, p + 1 ):
    parm[i] = meanv[i-1]
#
#  Compute the Cholesky decomposition.
#
  covm_fac, info = spofa ( covm, p, p )

  if ( info != 0 ):
    print ( '' )
    print ( 'setgmn(): Fatal error!' )
    print ( '  spofa() finds COVM matrix not positive definite.' )
    raise Exception ( 'setgmn(): Fatal error!' )
#
#  Store the upper half of the Cholesky factor.
#
  k = p

  for i in range ( 0, p ):
    for j in range ( i, p ):
      k = k + 1
      parm[k] = covm_fac[i,j]

  return parm

def genmn_test ( phrase ):

#*****************************************************************************80
#
## genmn_test() tests genmn().
#
#  Discussion:
#
#    I didn't feel up to creating a test problem for this function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
  print ( '' )
  print ( 'genmn_test():' )
  print ( '  genmn() generates multivariate normal deviates.' )
  print ( '  Warning! - No test code has been provided.' )
  print ( '' )
  print ( 'genmn_test():' )
  print ( '  Normal end of execution.' )

  return

def genmul ( n, p, ncat ):

#*****************************************************************************80
#
## genmul() generates a multinomial random deviate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
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
#    integer N, the number of events, which will be classified into 
#    one of the NCAT categories.
#
#    real P(NCAT-1).  P(I) is the probability that an event
#    will be classified into category I.  Thus, each P(I) must be between
#    0.0 and 1.0.  Only the first NCAT-1 values of P must be defined since
#    P(NCAT) would be 1.0 minus the sum of the first NCAT-1 P's.
#
#    integer NCAT, the number of categories.
#
#  Output:
#
#    integer IX(NCAT), a random observation from
#    the multinomial distribution.  All IX(i) will be nonnegative and their
#    sum will be N.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'genmul(): Fatal error!' )
    print ( '  N < 0' )
    raise Exception ( 'genmul(): Fatal error!' )

  if ( ncat <= 1 ):
    print ( '' )
    print ( 'genmul(): Fatal error!' )
    print ( '  NCAT <= 1' )
    raise Exception ( 'genmul(): Fatal error!' )

  for i in range ( 0, ncat - 1 ):

    if ( p[i] < 0.0 ):
      print ( ' ' )
      print ( 'genmul(): Fatal error!' )
      print ( '  Some P(i) < 0.' )
      raise Exception ( 'genmul(): Fatal error!' )

    if ( 1.0 < p[i] ):
      print ( ' ' )
      print ( 'genmul(): Fatal error!' )
      print ( '  Some 1 < P(i).' )
      raise Exception ( 'genmul(): Fatal error!' )

  ptot = np.sum ( p[0:ncat-1] )

  if ( 0.99999 < ptot ):
    print ( ' ' )
    print ( 'genmul(): Fatal error!' )
    print ( '  1 < Sum of P().' )
    raise Exception ( 'genmul(): Fatal error!' )
#
#  Initialize variables.
#
  ntot = n
  ptot = 1.0
  ix = np.zeros ( ncat )
#
#  Generate the observation.
#
  for icat in range ( 0, ncat - 1 ):
    prob = p[icat] / ptot
    ix[icat] = ignbin ( ntot, prob )
    ntot = ntot - ix[icat]
    if ( ntot <= 0 ):
      return ix
    ptot = ptot - p[icat]

  ix[ncat-1] = ntot

  return ix

def genmul_test ( phrase ):

#*****************************************************************************80
#
## genmul_test() tests genmul().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  print ( '' )
  print ( 'genmul_test():' )
  print ( '  genmul() generates a multinomial random deviate.' )
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

  n = 100
  p = np.array ( [ 0.35, 0.15, 0.05, 0.30 ] )
  ncat = 5

  print ( '' )
  print ( '  Try 10 successive trials:' )
  print ( '' )

  for test in range ( 0, 10 ):
    ix = genmul ( n, p, ncat )
    print ( '    ' ),
    for i in range ( 0, ncat ):
      print ( '%2d' % ( ix[i] ) ),
    print ( '' )

  return

def gennch ( df, xnonc ):

#*****************************************************************************80
#
## gennch() generates a noncentral Chi-Square random deviate.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    1.0 < DF.
#
#    real XNONC, the noncentrality parameter.
#    0.0 <= XNONC.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  import numpy as np

  if ( df <= 1.0 ):
    print ( ' ' )
    print ( 'gennch(): Fatal error!' )
    print ( '  DF <= 1.' )
    raise Exception ( 'gennch(): Fatal error!' )

  if ( xnonc < 0.0 ):
    print ( ' ' )
    print ( 'gennch(): Fatal error!' )
    print ( '  XNONC < 0.0.' )
    raise Exception ( 'gennch(): Fatal error!' )

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
## gennch_test() tests gennch().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'gennch_test():' )
  print ( '  gennch() generates noncentral Chi-square deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def gennf ( dfn, dfd, xnonc ):

#*****************************************************************************80
#
## gennf() generates a noncentral F random deviate.
#
#  Discussion:
#
#    This procedure generates a random deviate from the noncentral F
#    (variance ratio) distribution with DFN degrees of freedom in the
#    numerator, and DFD degrees of freedom in the denominator, and
#    noncentrality parameter XNONC.
#
#    It directly generates the ratio of noncentral numerator chisquare variate
#    to central denominator chisquare variate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real DFN, the numerator degrees of freedom.
#    1.0 < DFN.
#
#    real DFD, the denominator degrees of freedom.
#    0.0 < DFD.
#
#    real XNONC, the noncentrality parameter.
#    0.0 <= XNONC.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  if ( dfn <= 1.0 ):
    print ( '' )
    print ( 'gennf(): Fatal error!' )
    print ( '  DFN <= 1.0' )
    raise Exception ( 'gennf(): Fatal error!' )

  if ( dfd <= 0.0 ):
    print ( '' )
    print ( 'gennf(): Fatal error!' )
    print ( '  DFD <= 0.0' )
    raise Exception ( 'gennf(): Fatal error!' )

  if ( xnonc < 0.0 ):
    print ( '' )
    print ( 'gennf(): Fatal error!' )
    print ( '  XNONC < 0.0' )
    raise Exception ( 'gennf(): Fatal error!' )

  xnum = gennch ( dfn, xnonc ) / dfn
  xden = genchi ( dfd ) / dfd

  value = xnum / xden

  return value

def gennf_test ( phrase ):

#*****************************************************************************80
#
## gennf_test() tests gennf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 10000

  print ( '' )
  print ( 'gennf_test():' )
  print ( '  gennf() generates noncentral F deviates.' )
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
  high = 10.0
  dfn = genunf ( low, high )

  low = 5.0
  high = 10.0
  dfd = genunf ( low, high )

  low = 0.0
  high = 2.0
  xnonc = genunf ( low, high )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameter values:' )
  print ( '' )
  print ( '  DFN =   %g' % ( dfn ) )
  print ( '  DFD =   %g' % ( dfd ) )
  print ( '  XNONC = %g' % ( xnonc ) )
#
#  Generate N samples.
#
  array = np.zeros ( n )
  for i in range ( 0, n ):
    array[i] = gennf ( dfn, dfd, xnonc )
#
#  Compute statistics on the samples.
#
  av, var, xmin, xmax = stats ( array, n )
#
#  Request expected value of statistics for this distribution.
#
  pdf = 'nf'
  param = np.array ( [ dfn, dfd, xnonc ] )

  avtr, vartr = trstat ( pdf, param )

  print ( '' )
  print ( '  Sample data range:          %14.6g  %14.6g' % ( xmin, xmax ) )
  print ( '  Sample mean, variance:      %14.6g  %14.6g' % ( av,   var ) )
  print ( '  Distribution mean, variance %14.6g  %14.6g' % ( avtr, vartr ) )

  return

def gennor ( av, sd ):

#*****************************************************************************80
#
## gennor() generates a normal random deviate.
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
#    03 September 2018
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
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  value = sd * snorm ( ) + av

  return value

def gennor_test ( phrase ):

#*****************************************************************************80
#
## gennor_test() tests gennor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'gennor_test():' )
  print ( '  gennor() generates normal deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def genprm ( a, n ):

#*****************************************************************************80
#
## genprm() generates and applies a random permutation to an array.
#
#  Discussion:
#
#    To see the permutation explicitly, let the input array be
#    1, 2, ..., N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    integer A(N), an array to be permuted.
#
#    integer N, the number of entries in the array.
#
#  Output:
#
#    integer A2(N), a permuted copy of the array.
#
  a2 = a.copy ( )
  for i in range ( 0, n ):
    j = ignuin ( i, n - 1 )
    itmp  = a2[j]
    a2[j] = a2[i]
    a2[i] = itmp

  return a2

def genprm_test ( phrase ):

#*****************************************************************************80
#
## genprm_test() tests genprm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  print ( '' )
  print ( 'genprm_test():' )
  print ( '  genprm() generates a random permutation.' )
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

  n = 10

  p1 = np.array ( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
  p2 = genprm ( p1, n )

  print ( '' )
  print ( '  Array:   ' ),
  for i in range ( 0, n ):
    print ( '%d' % p1[i] ),
  print ( '' )
  print ( '  Permuted:' ),
  for i in range ( 0, n ):
    print ( '%d' % p2[i] ),
  print ( '' )

  return

def genunf ( low, high ):

#*****************************************************************************80
#
## genunf() generates a uniform random deviate.
#
#  Discussion:
#
#    This procedure generates a real deviate uniformly distributed between
#    LOW and HIGH.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real LOW, HIGH, the lower and upper bounds.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  from rnglib import r4_uni_01

  value = low + ( high - low ) * r4_uni_01 ( )

  return value

def genunf_test ( phrase ):

#*****************************************************************************80
#
## genunf_test() tests genunf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'genunf_test():' )
  print ( '  genunf() generates uniform deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def ignbin ( n, pp ):

#*****************************************************************************80
#
## ignbin() generates a binomial random deviate.
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
#    03 September 2018
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
#  Output:
#
#    integer VALUE, a random deviate from the distribution.
#
  from rnglib import r4_uni_01
  import numpy as np

  if ( pp <= 0.0 or 1.0 <= pp ):
    print ( ' ' )
    print ( 'ignbin(): Fatal error!' )
    print ( '  PP is out of range.' )
    raise Exception ( 'ignbin(): Fatal error!' )

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
## ignbin_test() tests ignbin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2013
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 10000

  print ( '' )
  print ( 'ignbin_test():' )
  print ( '  ignbin() generates binomial deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def ignnbn ( n, p ):

#*****************************************************************************80
#
## ignnbn() generates a negative binomial random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a negative binomial
#    distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
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
#    integer N, the required number of events.
#    0 <= N.
#
#    real P, the probability of an event during a
#    Bernoulli trial.  0.0 < P < 1.0.
#
#  Output:
#
#    integer VALUE, a random deviate from
#    the distribution.
#
  if ( n < 0 ):
    print ( '' )
    print ( 'ignnbn(): Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'ignnbn(): Fatal error!' )

  if ( p <= 0.0 ):
    print ( '' )
    print ( 'ignnbn(): Fatal error!' )
    print ( '  P <= 0.0' )
    raise Exception ( 'ignnbn(): Fatal error!' )

  if ( 1.0 <= p ):
    print ( '' )
    print ( 'ignnbn(): Fatal error!' )
    print ( '  1.0 <= P' )
    raise Exception ( 'ignnbn(): Fatal error!' )
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
## ignnbn_test() tests ignnbn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 10000

  print ( '' )
  print ( 'ignnbn_test():' )
  print ( '  ignnbn() generates negative binomial deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def ignpoi ( mu ):

#*****************************************************************************80
#
## ignpoi() generates a Poisson random deviate.
#
#  Discussion:
#
#    This procedure generates a single random deviate from a Poisson
#    distribution with given mean.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Computer Generation of Poisson Deviates From
#    Modified Normal Distributions,
#    ACM Transactions on Mathematical Software,
#    Volume 8, Number 2, June 1982, pages 163-179.
#
#  Input:
#
#    real MU, the mean of the Poisson distribution from
#    which a random deviate is to be generated.
#
#  Output:
#
#    integer VALUE, a random deviate from
#    the distribution.
#
  from rnglib import r4_uni_01
  import numpy as np

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
## ignpoi_test() tests ignpoi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2013
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  n = 1000

  print ( '' )
  print ( 'ignpoi_test():' )
  print ( '  ignpoi() generates Poisson deviates.' )
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
  print ( '  Parameter values:' )
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

  return

def ignuin ( low, high ):

#*****************************************************************************80
#
## ignuin() generates a random integer in a given range.
#
#  Discussion:
#
#    Each deviate K satisfies LOW <= K <= HIGH.
#
#    If (HIGH-LOW) > 2,147,483,561, this procedure prints an error message
#    and stops the program.
#
#    IGNLGI generates integers between 1 and 2147483562.
#
#    MAXNUM is 1 less than the maximum generatable value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    integer LOW, HIGH, the lower and upper bounds.
#
#  Output:
#
#    integer VALUE, a random deviate from
#    the distribution.
#
  from rnglib import i4_uni

  maxnum = 2147483561

  high = int ( high )
  low = int ( low )

  if ( high < low ):
    print ( ' ' )
    print ( 'ignuin(): Fatal error!' )
    print ( '  HIGH < LOW.' )
    raise Exception ( 'ignuin(): Fatal error!' )

  width = high - low

  if ( maxnum < width ):
    print ( ' ' )
    print ( 'ignuin(): Fatal error!' )
    print ( '  Range HIGH-LOW is too large.' )
    raise Exception ( 'ignuin(): Fatal error!' )

  if ( low == high ):
    value = low
    return value

  ranp1 = width + 1
  maxnow = ( maxnum / ranp1 ) * ranp1

  while ( True ):

    ign = i4_uni ( ) - 1

    if ( ign <= maxnow ):
      break

  value = int ( low + ( ign % ranp1 ) )

  return value

def ignuin_test ( phrase ):

#*****************************************************************************80
#
## ignuin_test() tests ignuin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  from rnglib import set_initial_seed

  print ( '' )
  print ( 'ignuin_test():' )
  print ( '  ignuin() generates uniformly distributed integers in a range.' )
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

  a = -1000.0
  b = +1000.0
  low = int ( genunf ( a, b ) )

  a = low + 10.0
  b = a + 1000.0
  high = int ( genunf ( a, b ) )

  n = 10

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameter values:' )
  print ( '' )
  print ( '  LOW  = %d' % ( low ) )
  print ( '  HIGH = %d' % ( high ) )

  print ( '' )
  for test in range ( 0, n ):
    x = ignuin ( low, high )
    print ( '  %d' % ( x ) )

  return

def lennob ( s ):

#*****************************************************************************80
#
## lennob() returns the length of a character string to the last nonblank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#   03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, a string.
#
#  Output:
#
#    integer LEN_TRIM, the length of the string to the last nonblank.
#
  n = len ( s )

  for i in range ( n - 1, -1, -1 ):
    if ( s[i] != ' ' ):
      value = i + 1
      return value

  value = 0
  return value

def lennob_test ( ):

#*****************************************************************************80
#
## lennob_test() tests lennob().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lennob_test():' )
  print ( '  lennob() returns the length of string to the last nonblank.' )
  print ( '' )
  print ( '  LEN  lennob  ---------S---------' )
  print ( '' )

  s = 'Hi, Bob!'
  l1 = len ( s )
  l2 = lennob ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  s = '  How   are   you?     '
  l1 = len ( s )
  l2 = lennob ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  s = '    '
  l1 = len ( s )
  l2 = lennob ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  return

def low_level_test ( ):

#*****************************************************************************80
#
## low_level_test() tests the low level random generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import cgn_set
  from rnglib import i4_uni
  from rnglib import init_generator
  from rnglib import initialize
  from rnglib import set_initial_seed
  import numpy as np

  genlst = np.array ( [ 1, 5, 10, 20, 32 ] )

  print ( '' )
  print ( 'low_level_test()' )
  print ( '  Test the lower level random number generators.' )
  print ( '' )
  print ( '  Five of the 32 generators will be tested.' )
  print ( '  We generate 100000 numbers, reset the block' )
  print ( '  and do it again.  No disagreements should occur.' )
#
#  Initialize the generators.
#
  initialize ( )
#
#  Set up all generators.
#
  seed1 = 12345
  seed2 = 54321
  set_initial_seed ( seed1, seed2 )
#
#  For a selected set of generators
#
  nbad = 0
  answer = np.zeros ( 10000 )

  for ixgen in range ( 0, 5 ):

    igen = genlst[ixgen]
    cgn_set ( igen )
    print ( '  Testing generator %d' % ( igen ) )
#
#  Use 10 blocks, and generate 1000 numbers per block
#
    init_generator ( 0 )

    for iblock in range ( 1, 11 ):
      for ians in range ( 1, 1001 ):
        ix = ians + ( iblock - 1 ) * 1000
        answer[ix-1] = i4_uni ( )
      init_generator ( 2 )
#
#  Do it again and compare answers
#  Use 10 blocks, and generate 1000 numbers.
#
    init_generator ( 0 )

    for iblock in range ( 1, 11 ):
      for ians in range ( 1, 1001 ):
        ix = ians + ( iblock - 1 ) * 1000
        itmp = i4_uni ( )

        if ( itmp != answer[ix-1] ):

          print ( '' )
          print ( 'low_level_test(): Warning!' )
          print ( '  Data disagreement:' )
          print ( '  Block = %d' % ( iblock ) )
          print ( '  N within block = %d' % ( ians ) )
          print ( '  Index in ANSWER = %d' % ( ix ) )
          print ( '  First value =  %d' % ( answer[ix] ) )
          print ( '  Second value = %d' % ( itmp ) )

          nbad = nbad + 1

          if ( 10 < nbad ):
            print ( '' )
            print ( 'low_level_test(): Warning!' )
            print ( '  More than 10 mismatches.' )
            print ( '  Tests terminated early.' )
            return

      init_generator ( 2 )

  print ( '' )
  print ( '  Number of disagreements found was %d' % ( nbad ) )

  return

def phrtsd ( phrase ):

#*****************************************************************************80
#
## phrtsd() converts a phrase to a pair of random number generator seeds.
#
#  Discussion:
#
#    This procedure uses a character string to generate two seeds for the RGN
#    random number generator.
#
#    Trailing blanks are eliminated before the seeds are generated.
#
#    Generated seed values will fall in the range 1 to 2^30 = 1,073,741,824.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    string PHRASE, a phrase to be used for the random number generation.
#
#  Output:
#
#    integer SEED1, SEED2, the two seeds for the
#    random number generator, based on PHRASE.
#
  import numpy as np

  table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@#$#^...*()_+[]:''"<>?,./'

  twop30 = 1073741824

  shift = np.array ( [ 1, 64, 4096, 262144, 16777216 ] )

  seed1 = 1234567890
  seed2 = 123456789

  values = np.zeros ( 5 )

  lphr = lennob ( phrase )

  for i in range ( 0, lphr ):

    c = phrase[i]
    ichr = table.find ( c )

    if ( ichr == -1 ):
      ichr = 0
    else:
      ichr = ichr + 1

    ichr = ( ichr % 64 )

    if ( ichr == 0 ):
      ichr = 63

    for j in range ( 0, 5 ):
      values[j] = ichr - j - 1
      if ( values[j] < 1 ):
        values[j] = values[j] + 63

    for j in range ( 0, 5 ):
      seed1 = ( ( seed1 + shift[j] * values[j]   ) % twop30 )
      seed2 = ( ( seed2 + shift[j] * values[4-j] ) % twop30 )

  return seed1, seed2

def phrtsd_test ( ):

#*****************************************************************************80
#
## phrtsd_test() tests phrtsd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'phrtsd_test():' )
  print ( '  phrtsd() converts a phrase into two numeric seeds.' )

  s = 'A1'
  seed1, seed2 = phrtsd ( s )
  print ( '' )
  print ( '  Phrase: "%s"' % ( s ) )
  print ( '  Seeds:  %d  %d' % ( seed1, seed2 ) )

  s = 'shazam'
  seed1, seed2 = phrtsd ( s )
  print ( '' )
  print ( '  Phrase: "%s"' % ( s ) )
  print ( '  Seeds:  %d  %d' % ( seed1, seed2 ) )

  s = 'Happy birthday'
  seed1, seed2 = phrtsd ( s )
  print ( '' )
  print ( '  Phrase: "%s"' % ( s ) )
  print ( '  Seeds:  %d  %d' % ( seed1, seed2 ) )

  return

def prcomp ( maxobs, p, mean, xcovar, answer ):

#*****************************************************************************80
#
## prcomp() prints covariance information.
#
#  Discussion:
#
#    I didn't feel up to creating a test problem for this function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    integer MAXOBS, the number of observations.
#
#    integer P, the number of variables.
#
#    real MEAN(P), the mean for each column.
#
#    real XCOVAR(P,P), the variance/covariance matrix.
#
#    real ANSWER(MAXOBS,P), the observed values.
#
  import numpy as np

  print ( '' )
  print ( 'prcomp():' )
  print ( '  Print and compare covariance information' )
  print ( '' )

  rmean = np.zeros ( p )
  rvar = np.zeros ( p )

  for j in range ( 0, p ):
    rmean, rvar, rmin, rmax = stats ( answer[0:maxobs,j], maxobs )
    print ( '  Variable Number %d' % ( j ) )
    print ( '  Mean     %12g  Generated %12g' % ( mean[j], rmean ) )
    print ( '  Variance %12g  Generated 512g' % ( xcovar[j,j], rvar ) )

  print ( '' )
  print ( '  Covariances:' )
  print ( '' )

  for i in range ( 0, p ):
    for j in range ( 0, i ):
      print ( '  I = %d, J = %d' % ( i, j ) )
      rcovar[i,j] = r4vec_covariance ( maxobs, answer[0:maxobs,i], answer[0:maxobs,j] )
      print ( '  Covariance %12g  Generated %12g' % ( xcovar[i,j], rcovar[i,j] ) )

  return

def prcomp_test ( ):

#*****************************************************************************80
#
## prcomp_test() tests prcomp().
#
#  Discussion:
#
#    I didn't feel up to creating a test problem for this function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
  print ( '' )
  print ( 'prcomp_test()' )
  print ( '  prcomp() prints and compares covariance information.' )
  print ( '  Warning! - No test code has been provided.' )
  print ( '' )
  print ( 'prcomp_test:' )
  print ( '  Normal end of execution.' )

  return

def r4_exponential_sample ( lam ):

#*****************************************************************************80
#
## r4_exponential_sample() samples the exponential PDF.
#
#  Discussion:
#
#    Note that the parameter LAM is a multiplier.  In some formulations,
#    it is used as a divisor instead.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real LAM, the parameter of the PDF.
#
#  Output:
#
#    real VALUE, a sample of the PDF.
#
  from rnglib import r4_uni_01
  import numpy as np

  r = r4_uni_01 ( );

  value = - np.log ( r ) * lam

  return value

def r4_exponential_sample_test ( ):

#*****************************************************************************80
#
## r4_exponential_test() tests r4_exponential().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  test_num = 20

  print ( '' )
  print ( 'r4_exponential_test():' )
  print ( '  r4_exponential() samples the exponential distribution.' )
  print ( '' )

  lam = 0.5

  for test in range ( 0, test_num ):

    x = r4_exponential_sample ( lam )
    print ( '  %f' % ( x ) )

  return

def r4_exp ( x ):

#*****************************************************************************80
#
## r4_exp() computes the exponential function, avoiding overflow and underflow.
#
#  Discussion:
#
#    For arguments of very large magnitude, the evaluation of the
#    exponential function can cause computational problems.  Some languages
#    and compilers may return an infinite value or a "Not-a-Number".  
#    An alternative, when dealing with a wide range of inputs, is simply
#    to truncate the calculation for arguments whose magnitude is too large.
#    Whether this is the right or convenient approach depends on the problem
#    you are dealing with, and whether or not you really need accurate
#    results for large magnitude inputs, or you just want your code to
#    stop crashing.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the exponential function.
#
#  Output:
#
#    real VALUE, the value of exp ( X ).
#
  import numpy as np

  r4_huge = 1.0E+30
  r4_log_max = +69.0776
  r4_log_min = -69.0776

  if ( x <= r4_log_min ):
    value = 0.0
  elif ( x < r4_log_max ):
    value = np.exp ( x )
  else:
    value = r4_huge

  return value

def r4_exp_test ( ):

#*****************************************************************************80
#
## r4_exp_test() tests r4_exp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r4_exp_test():' )
  print ( '  r4_exp() returns the exponential of a real number.' )
  print ( '' )
  print ( '        X           r4_exp(X)' )
  print ( '' )

  for i in range ( -80, +90, 10 ):
    x = float ( i )
    print ( '  %12g  %12g' % ( x, r4_exp ( x ) ) )

  return

def r4vec_covariance ( n, x, y ):

#*****************************************************************************80
#
## r4vec_covariance() computes the covariance of two vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the dimension of the two vectors.
#
#    real X(N), Y(N), the two vectors.
#
#  Output:
#
#    real VALUE, the covariance of the two vectors.
#
  import numpy as np

  x_average = np.mean ( x[0:n] )
  y_average = np.mean ( y[0:n] )
  
  value = 0.0
  for i in range ( 0, n ):
    value = value + ( x[i] - x_average ) * ( y[i] - y_average )

  value = value / float ( n - 1 )

  return value

def r4vec_covariance_test ( ):

#*****************************************************************************80
#
## r4vec_covariance_test() tests r4vec_covariance().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import r4_uni_01
  import numpy as np

  print ( '' )
  print ( 'r4vec_covariance_test():' )
  print ( '  r4vec_covariance() computes the covariance of two R4VECs.' )

  n = 2

  v1 = np.array ( [ 1.0, 0.0 ] )
  print ( '' )
  print ( '  Vector V1:' ),
  for i in range ( 0, n ):
    print ( '%g' % ( v1[i] ) ),
  print ( '' )

  for i in range ( 0, 12 ):
    angle = float ( 2 * i ) * np.pi / 12.0
    r = r4_uni_01 ( )
    v2 = r * np.array ( [ np.cos(angle), np.sin(angle) ] )
    print ( '' )
    print ( '  Vector V2:' ),
    for i in range ( 0, n ):
      print ( '%g' % ( v2[i] ) ),
    print ( '' )
    value = r4vec_covariance ( n, v1, v2 )
    print ( '  Covariance(V1,V2) = %g' % ( value ) )

  return

def r8_exponential_sample ( lam ):

#*****************************************************************************80
#
## r8_exponential_sample() samples the exponential PDF.
#
#  Discussion:
#
#    Note that the parameter LAM is a multiplier.  In some formulations,
#    it is used as a divisor instead.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real LAM, the parameter of the PDF.
#
#  Output:
#
#    real VALUE, a sample of the PDF.
#
  from rnglib import r8_uni_01
  import numpy as np

  r = r8_uni_01 ( );

  value = - np.log ( r ) * lam

  return value

def r8_exponential_sample_test ( ):

#*****************************************************************************80
#
## r8_exponential_test() tests r8_exponential().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  test_num = 20

  print ( '' )
  print ( 'r8_exponential_test():' )
  print ( '  r8_exponential() samples the exponential distribution.' )
  print ( '' )

  lam = 0.5

  for test in range ( 0, test_num ):

    x = r8_exponential_sample ( lam )
    print ( '  %f' % ( x ) )

  return

def r8vec_covariance ( n, x, y ):

#*****************************************************************************80
#
## r8vec_covariance() computes the covariance of two vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the dimension of the two vectors.
#
#    real X(N), Y(N), the two vectors.
#
#  Output:
#
#    real VALUE, the covariance of the two vectors.
#
  import numpy as np

  x_average = np.mean ( x[0:n] )
  y_average = np.mean ( y[0:n] )
  
  value = 0.0
  for i in range ( 0, n ):
    value = value + ( x[i] - x_average ) * ( y[i] - y_average )

  value = value / float ( n - 1 )

  return value

def r8vec_covariance_test ( ):

#*****************************************************************************80
#
## r8vec_covariance_test() tests r8vec_covariance().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import r8_uni_01
  import numpy as np

  print ( '' )
  print ( 'r8vec_covariance_test():' )
  print ( '  r8vec_covariance() computes the covariance of two R8VECs.' )

  n = 2

  v1 = np.array ( [ 1.0, 0.0 ] )
  print ( '' )
  print ( '  Vector V1:' ),
  for i in range ( 0, n ):
    print ( '%g' % ( v1[i] ) ),
  print ( '' )

  for i in range ( 0, 12 ):
    angle = float ( 2 * i ) * np.pi / 12.0
    r = r8_uni_01 ( )
    v2 = r * np.array ( [ np.cos(angle), np.sin(angle) ] )
    print ( '' )
    print ( '  Vector V2:' ),
    for i in range ( 0, n ):
      print ( '%g' % ( v2[i] ) ),
    print ( '' )
    value = r8vec_covariance ( n, v1, v2 )
    print ( '  Covariance(V1,V2) = %g' % ( value ) )

  return

def ranlib_test ( ):

#*****************************************************************************80
#
## ranlib_test() tests ranlib().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  from rnglib import initialize
  import numpy as np
  import platform

  phrase = 'Randomizer'

  initialize ( )

  print ( '' )
  print ( 'ranlib_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ranlib()' )

  genbet_test ( phrase )
  genchi_test ( phrase )
  genexp_test ( phrase )
  genf_test ( phrase )
  gengam_test ( phrase )
  genmn_test ( phrase )
  genmul_test ( phrase )
  gennch_test ( phrase )
  gennf_test ( phrase )
  gennor_test ( phrase )
  genprm_test ( phrase )
  genunf_test ( phrase )
  ignbin_test ( phrase )
  ignnbn_test ( phrase )
  ignpoi_test ( phrase )
  ignuin_test ( phrase )
  lennob_test ( )
  low_level_test ( )
  phrtsd_test ( )
  prcomp_test ( )
  r4_exp_test ( )
  r4_exponential_sample_test ( )
  r4vec_covariance_test ( )
  r8_exponential_sample_test ( )
  r8vec_covariance_test ( )
  setcov_test ( )
  sexpo_test ( )
  sgamma_test ( )
  snorm_test ( )
  spofa_test ( )
  stats_test ( )
  trstat_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ranlib_test():' )
  print ( '  Normal end of execution.' )
  return

def setcov ( p, var, corr ):

#*****************************************************************************80
#
## setcov() sets a covariance matrix from variance and common correlation.
#
#  Discussion:
#
#    This procedure sets the covariance matrix from the variance and
#    common correlation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    integer P, the number of variables.
#
#    real VAR(P), the variances.
#
#    real CORR, the common correlaton.
#
#  Output:
#
#    real COVAR(P,P), the covariance matrix.
#
  import numpy as np

  if ( any ( var[0:p] < 0.0 ) ):
    print ( '' )
    print ( 'setcov(): Fatal error!' )
    print ( '  No variance should be negative.' )
    raise Exception ( 'setcov(): Fatal error!' )

  covar = np.zeros ( [ p, p ] )

  for i in range ( 0, p ):
    for  j in range ( 0, p ):
      if ( i == j ):
        covar[i,j] = var[i]
      else:
        covar[i,j] = corr * np.sqrt ( var[i] * var[j] )

  return covar

def setcov_test ( ):

#*****************************************************************************80
#
## setcov_test() tests setcov().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  print ( '' )
  print ( 'setcov_test():' )
  print ( '  setcov() sets a covariance matrix.' )

  p = 3
  var = np.array ( [ 0.5, 0.2, 0.9 ] )
  corr = 0.25

  print ( '' )
  print ( '  Number of variables P = %d' % ( p ) )
  print ( '  Common correlation = %g' % ( corr ) )
  print ( '  Variances:' )
  print ( '    ' ),
  for i in range ( 0, p ):
    print ( '%g' % ( var[i] ) ),
  print ( '' )

  cov = setcov ( p, var, corr )

  print ( '' )
  print ( '  Covariance matrix:' )
  print ( '' )
  for i in range ( 0, p ):
    print ( '    ' ),
    for j in range ( 0, p ):
      print ( '%8f' % ( cov[i,j] ) ),
    print ( '' )

  return

def sexpo ( ):

#*****************************************************************************80
#
## sexpo() samples the standard exponential distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm SA in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Computer Methods for Sampling From the
#    Exponential and Normal Distributions,
#    Communications of the ACM,
#    Volume 15, Number 10, October 1972, pages 873-882.
#
#  Output:
#
#    real VALUE, a random deviate from the standard
#    exponential distribution.
#
  from rnglib import r4_uni_01
  import numpy as np

  q = np.array ( [ \
       0.6931472, \
       0.9333737, \
       0.9888778, \
       0.9984959, \
       0.9998293, \
       0.9999833, \
       0.9999986, \
       0.9999999 ] )

  a = 0.0
  u = r4_uni_01 ( )

  while ( True ):

    u = u + u

    if ( 1.0 < u ):
      break

    a = a + q[0]

  u = u - 1.0

  if ( u <= q[0] ):
    value = a + u
    return value

  i = 1
  ustar = r4_uni_01 ( )
  umin = ustar

  while ( True ):

    ustar = r4_uni_01 ( )
    umin = min ( umin, ustar )
    i = i + 1

    if ( u <= q[i-1] ):
      break

  value = a + umin * q[0]

  return value

def sexpo_test ( ):

#*****************************************************************************80
#
## sexpo_test() tests sexpo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2018
#
#  Author:
#
#    John Burkardt
#
  test_num = 20

  print ( '' )
  print ( 'sexpo_test():' )
  print ( '  sexpo() generates exponentially distributed random values.' )
  print ( '' )

  for test in range ( 0, test_num ):

    x = sexpo ( )
    print ( '  %f' % ( x ) )

  return

def sgamma ( a ):

#*****************************************************************************80
#
## sgamma() samples the standard Gamma distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm GD in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
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
#    real A, the parameter of the standard gamma
#    distribution.  0.0 < A < 1.0.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  from rnglib import r4_uni_01
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
    t = snorm ( )
    x = s + 0.5 * t
    value = x * x

    if ( 0.0 <= t ):
      return value
#
#  Squeeze acceptance.
#
    u = r4_uni_01 ( )
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

      e = sexpo ( )
      u = 2.0 * r4_uni_01 ( ) - 1.0

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

      p = b * r4_uni_01 ( )

      if ( p < 1.0 ):

        value = np.exp ( np.log ( p ) / a )

        if ( value <= sexpo ( ) ):
          return value

        continue

      value = - np.log ( ( b - p ) / a )

      if ( ( 1.0 - a ) * np.log ( value ) <= sexpo ( ) ):
        break

  return value

def sgamma_test ( ):

#*****************************************************************************80
#
## sgamma_test() tests sgamma().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  test_num = 20

  print ( '' )
  print ( 'sgamma_test():' )
  print ( '  sgamma() generates gamma distributed random values.' )
  print ( '' )

  a = 0.5

  for test in range ( 0, test_num ):

    x = sgamma ( a )
    print ( '  %f' % ( x ) )

  return

def snorm ( ):

#*****************************************************************************80
#
## snorm() samples the standard normal distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm FL, with M = 5, in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2018
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
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  from rnglib import r4_uni_01
  import numpy as np

  a = np.array ( [ \
        0.0000000,     0.3917609E-01, 0.7841241E-01, 0.1177699, \
        0.1573107,     0.1970991,     0.2372021,     0.2776904, \
        0.3186394,     0.3601299,     0.4022501,     0.4450965, \
        0.4887764,     0.5334097,     0.5791322,     0.6260990, \
        0.6744898,     0.7245144,     0.7764218,     0.8305109, \
        0.8871466,     0.9467818,     1.009990,      1.077516, \
        1.150349,      1.229859,      1.318011,      1.417797, \
        1.534121,      1.675940,      1.862732,      2.153875 ] )

  d = np.array ( [ \
        0.0000000, 0.0000000, 0.0000000, 0.0000000, \
        0.0000000, 0.2636843, 0.2425085, 0.2255674, \
        0.2116342, 0.1999243, 0.1899108, 0.1812252, \
        0.1736014, 0.1668419, 0.1607967, 0.1553497, \
        0.1504094, 0.1459026, 0.1417700, 0.1379632, \
        0.1344418, 0.1311722, 0.1281260, 0.1252791, \
        0.1226109, 0.1201036, 0.1177417, 0.1155119, \
        0.1134023, 0.1114027, 0.1095039 ] )

  h = np.array ( [ \
        0.3920617E-01, 0.3932705E-01, 0.3950999E-01, 0.3975703E-01, \
        0.4007093E-01, 0.4045533E-01, 0.4091481E-01, 0.4145507E-01, \
        0.4208311E-01, 0.4280748E-01, 0.4363863E-01, 0.4458932E-01, \
        0.4567523E-01, 0.4691571E-01, 0.4833487E-01, 0.4996298E-01, \
        0.5183859E-01, 0.5401138E-01, 0.5654656E-01, 0.5953130E-01, \
        0.6308489E-01, 0.6737503E-01, 0.7264544E-01, 0.7926471E-01, \
        0.8781922E-01, 0.9930398E-01, 0.1155599,     0.1404344, \
        0.1836142,     0.2790016,     0.7010474 ] )

  t = np.array ( [ \
        0.7673828E-03, 0.2306870E-02, 0.3860618E-02, 0.5438454E-02, \
        0.7050699E-02, 0.8708396E-02, 0.1042357E-01, 0.1220953E-01, \
        0.1408125E-01, 0.1605579E-01, 0.1815290E-01, 0.2039573E-01, \
        0.2281177E-01, 0.2543407E-01, 0.2830296E-01, 0.3146822E-01, \
        0.3499233E-01, 0.3895483E-01, 0.4345878E-01, 0.4864035E-01, \
        0.5468334E-01, 0.6184222E-01, 0.7047983E-01, 0.8113195E-01, \
        0.9462444E-01, 0.1123001,     0.1364980,     0.1716886, \
        0.2276241,     0.3304980,     0.5847031 ] )

  u = r4_uni_01 ( )
  if ( u <= 0.5 ):
    s = 0.0
  else:
    s = 1.0

  u = 2.0 * u - s
  u = 32.0 * u
  i = int ( u )

  if ( i == 32 ):
    i = 31
#
#  Center
#
  if ( i != 0 ):

    ustar = u - i
    aa = a[i-1]

    while ( True ):

      if ( t[i-1] < ustar ):

        w = ( ustar - t[i-1] ) * h[i-1]

        y = aa + w

        if ( s != 1.0 ):
          value = y
        else:
          value = -y

        return value

      u = r4_uni_01 ( )
      w = u * ( a[i] - aa )
      tt = ( 0.5 * w + aa ) * w

      while ( True ):

        if ( tt < ustar ):
          y = aa + w
          if ( s != 1.0 ):
            value = y
          else:
            value = - y
          return value

        u = r4_uni_01 ( )

        if ( ustar < u ):
          break

        tt = u
        ustar = r4_uni_01 ( )

      ustar = r4_uni_01 ( )
#
#  Tail
#
  else:

    i = 6
    aa = a[31]

    while ( True ):

      u = u + u

      if ( 1.0 <= u ):
        break

      aa = aa + d[i-1]
      i = i + 1

    u = u - 1.0
    w = u * d[i-1]
    tt = ( 0.5 * w + aa ) * w

    while ( True ):

      ustar = r4_uni_01 ( )

      if ( tt < ustar ):
        y = aa + w
        if ( s != 1.0 ):
          value = y
        else:
          value = -y
        return value

      u = r4_uni_01 ( )

      if ( u <= ustar ):
        tt = u
      else:
        u = r4_uni_01 ( )
        w = u * d[i-1]
        tt = ( 0.5 * w + aa ) * w

  return value

def snorm_test ( ):

#*****************************************************************************80
#
## snorm_test() tests snorm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2018
#
#  Author:
#
#    John Burkardt
#
  test_num = 20

  print ( '' )
  print ( 'snorm_test():' )
  print ( '  snorm() generates normally distributed random values.' )
  print ( '' )

  for test in range ( 0, test_num ):

    x = snorm ( )
    print ( '  %f' % ( x ) )

  return

def spofa ( a, lda, n ):

#*****************************************************************************80
#
## spofa() factors a real symmetric positive definite matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    FORTRAN77 version by Cleve Moler.
#    This version by John Burkardt.
#
#  Input:
#
#    real A(LDA,N), the symmetric matrix to be factored.  Only the 
#    diagonal and upper triangle are accessed.
#
#    integer LDA, the leading dimension of the array A.
#    N <= LDA.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A_FAC(LDA,N), an upper triangular matrix R such that
#    A = R' * R.  If INFO is nonzero, the factorization was not completed.
#
#    integer INFO, error flag.
#    0, no error was detected.
#    K, the leading minor of order K is not positive definite.
#
  import numpy as np

  a_fac = a.copy ( )

  for i in range ( 1, n ):
    for j in range ( 0, i ):
      a_fac[i,j] = 0.0

  info = 0

  for j in range ( 0, n ):
    s = 0.0
    for k in range ( 0, j ):
      t = a_fac[k,j]
      for i in range ( 0, k ):
        t = t - a_fac[i,k] * a_fac[i,j]
      t = t / a_fac[k,k]
      a_fac[k,j] = t
      s = s + t * t

    s = a_fac[j,j] - s
    if ( s <= 0.0 ):
      info = j + 1
      return a_fac, info

    a_fac[j,j] = np.sqrt ( s )

  return a_fac, info

def spofa_test ( ):

#*****************************************************************************80
#
## spofa_test() tests spofa().
#
#  Discussion:
#
#    spofa factors a symmetric positive definite matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  n = 5
  lda = n

  print ( '' )
  print ( 'spofa_test():' )
  print ( '  spofa() LU factors a symmetric positive definite matrix,' )
#
#  Set the matrix A.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    a[i,i] = 2.0
    if ( 0 < i ):
      a[i,i-1] = -1.0
    if ( i < n - 1 ):
      a[i,i+1] = -1.0

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '    ' ),
    for j in range ( 0, n ):
      print ( '%g' % ( a[i,j] ) ),
    print ( '' )
#
#  Factor the matrix.
#
  print ( '' )
  print ( '  Call spofa() to factor the matrix.' )

  a_lu, info = spofa ( a, lda, n )
 
  if ( info != 0 ):
    print ( '' )
    print ( '  Error, spofa() returns INFO = %d' % ( info ) )
    return

  print ( '' )
  print ( '  Upper triangular factor U:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '    ' ),
    for j in range ( 0, n ):
      print ( '%8g' % ( a_lu[i,j] ) ),
    print ( '' )

  uut = np.dot ( np.transpose ( a_lu ), a_lu )

  print ( '' )
  print ( '  Product Ut * U:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '    ' ),
    for j in range ( 0, n ):
      print ( '%8g' % ( uut[i,j] ) ),
    print ( '' )

  return

def stats ( x, n ):

#*****************************************************************************80
#
## stats() computes statistics for a given array.
#
#  Discussion:
#
#    This procedure computes the average and variance of an array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    real X(N), the array to be analyzed.
#
#    integer N, the dimension of the array.
#
#  Output:
#
#    real AV, the average value.
#
#    real VAR, the variance.
#
#    real XMIN, XMAX, the minimum and maximum entries.
#
  import numpy as np

  xmin = np.min ( x[0:n] )
  xmax = np.max ( x[0:n] )
  av = np.mean ( x[0:n] )
  var = np.var ( x[0:n], ddof = 1 )
 
  return av, var, xmin, xmax

def stats_test ( ):

#*****************************************************************************80
#
## stats_test() tests stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  print ( '' )
  print ( 'stats_test():' )
  print ( '  stats() computes min, max, mean and variance for a vector.' )

  n = 5
  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  print ( '' )
  print ( '  Vector X:' )
  print ( '    ' ),
  for i in range ( 0, n ):
    print ( '%g' % ( x[i] ) ),
  print ( '' )

  av, var, xmin, xmax = stats ( x, n )

  print ( '' )
  print ( '  %g <= X <= %g' % ( xmin, xmax ) )
  print ( '  Mean = %g, Variance = %g' % ( av, var ) )

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

def trstat ( pdf, parin ):

#*****************************************************************************80
#
## trstat() returns the mean and variance for distributions.
#
#  Discussion:
#
#    This procedure returns the mean and variance for a number of statistical
#    distributions as a function of their parameters.
#
#    The input vector PARIN is used to pass in the parameters necessary
#    to specify the distribution.  The number of these parameters varies
#    per distribution, and it is necessary to specify an ordering for the
#    parameters used to a given distribution.  The ordering chosen here
#    is as follows:
#
#    bet
#      PARIN[0] is A
#      PARIN[1] is B
#    bin
#      PARIN[0] is Number of trials
#      PARIN[1] is Prob Event at Each Trial
#    chi
#      PARIN[0] = df
#    exp
#      PARIN[0] = mu
#    f
#      PARIN[0] is df numerator
#      PARIN[1] is df denominator
#    gam
#      PARIN[0] is A
#      PARIN[1] is R
#    nbn
#      PARIN[0] is N
#      PARIN[1] is P
#    nch
#      PARIN[0] is df
#      PARIN[1] is noncentrality parameter
#    nf
#      PARIN[0] is df numerator
#      PARIN[1] is df denominator
#      PARIN[2] is noncentrality parameter
#    nor
#      PARIN[0] is mean
#      PARIN[1] is standard deviation
#    poi
#      PARIN[0] is Mean
#    unf
#      PARIN[0] is LOW bound
#      PARIN[1] is HIGH bound
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    This version by John Burkardt.
#
#  Input:
#
#    string PDF, indicates the distribution:
#    'bet'  beta distribution
#    'bin'  binomial
#    'chi'  chisquare
#    'exp'  exponential
#    'f'    F (variance ratio)
#    'gam'  gamma
#    'nbn'  negative binomial
#    'nch'  noncentral chisquare
#    'nf'   noncentral f
#    'nor'  normal
#    'poi'  Poisson
#    'unf'  uniform
#
#    real PARIN(*), the parameters of the distribution.
#
#  Output:
#
#    real AV, the mean of the specified distribution.
#
#    real VAR, the variance of the specified distribuion.
#
  if ( pdf.lower() == 'bet' ):

    av = parin[0] / ( parin[0] + parin[1] )
    var = ( av * parin[1] ) / ( ( parin[0] + parin[1] ) * \
      ( parin[0] + parin[1] + 1.0 ) )

  elif ( pdf.lower() == 'bin' ):

    n = int ( parin[0] )
    p = parin[1]
    av = n * p
    var = n * p * ( 1.0 - p )

  elif ( pdf.lower() == 'chi' ):

    av = parin[0]
    var = 2.0 * parin[0]

  elif ( pdf.lower() == 'exp' ):

    av = parin[0]
    var = av ** 2

  elif ( pdf.lower() == 'f' ):

    if ( parin[1] <= 2.0001 ):
      av = -1.0
    else:
      av = parin[1] / ( parin[1] - 2.0 )

    if ( parin[1] <= 4.0001 ):
      var = -1.0
    else:
      var = ( 2.0 * parin[1] ** 2 * ( parin[0] + parin[1] - 2.0 ) ) / \
        ( parin[0] * ( parin[1] - 2.0 ) ** 2 * ( parin[1] - 4.0 ) )

  elif ( pdf.lower() == 'gam' ):

    a = parin[0]
    r = parin[1]
    av = r / a
    var = r / a ** 2

  elif ( pdf.lower() == 'nbn' ):

    n = int ( parin[0] )
    p = parin[1]
    av = n * ( 1.0 - p ) / p
    var = n * ( 1.0 - p ) / p ** 2

  elif ( pdf.lower() == 'nch' ):

    a = parin[0] + parin[1]
    b = parin[1] / a
    av = a
    var = 2.0 * a * ( 1.0 + b )

  elif ( pdf.lower() == 'nf' ):

    if ( parin[1] <= 2.0001 ):
      av = -1.0
    else:
      av = ( parin[1] * ( parin[0] + parin[2] ) ) \
        / ( ( parin[1] - 2.0 ) * parin[0] )

    if ( parin[1] <= 4.0001 ):
      var = -1.0
    else:
      a = ( parin[0] + parin[2] ) ** 2 \
        + ( parin[0] + 2.0 * parin[2] ) * ( parin[1] - 2.0 )
      b = ( parin[1] - 2.0 ) ** 2 * ( parin[1] - 4.0 )
      var = 2.0 * ( parin[1] / parin[0] ) ** 2 * ( a / b )

  elif ( pdf.lower() == 'nor' ):

    av = parin[0]
    var = parin[1] ** 2

  elif ( pdf.lower() == 'poi' ):

    av = parin[0]
    var = parin[0]

  elif ( pdf.lower() == 'unf' ):

    width = parin[1] - parin[0]
    av = parin[0] + width / 2.0
    var = width ** 2 / 12.0

  else:

    print ( '' )
    print ( 'trstat(): Fatal error!' )
    print ( '  Illegal input value for PDF.' )
    raise Exception ( 'trstat(): Fatal error!' )

  return av, var

def trstat_test ( ):

#*****************************************************************************80
#
## trstat_test() tests trstat().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
 
  print ( '' )
  print ( 'trstat_test():' )
  print ( '  trstat() returns the mean and variance for distributions.' )

  pdf = 'unf'
  a = 10.0
  b = 20.0
  param = np.array ( [ a, b ] )
  avtr, vartr = trstat ( pdf, param )
  print ( '' );
  print ( '  Distribution: "%s"' % ( pdf ) )
  print ( '  Distribution parameter values:  %14.6g  %14.6g' % ( a, b ) )
  print ( '  Distribution mean, variance     %14.6g  %14.6g' % ( avtr, vartr ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  ranlib_test ( )
  timestamp ( )

