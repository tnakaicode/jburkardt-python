#! /usr/bin/env python
#
def genmn ( parm ):

#*****************************************************************************80
#
## GENMN generates a multivariate normal deviate.
#
#  Discussion:
#
#    The method is:
#    1) Generate P independent standard normal deviates - Ei ~ N(0,1)
#    2) Using Cholesky decomposition find A so that A'*A = COVM
#    3) A' * E + MEANV ~ N(MEANV,COVM)
#
#    Note that PARM contains information needed to generate the
#    deviates, and is set up by SETGMN.
#
#    PARM(1) contains the size of the deviates, P
#    PARM(2:P+1) contains the mean vector.
#    PARM(P+2:P*(P+3)/2+1) contains the upper half of the Cholesky
#    decomposition of the covariance matrix.
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
#    Input, real PARM(P*(P+3)/2+1), parameters set by SETGMN.
#
#    Output, real X(P), a random deviate from the distribution.
#
  import numpy as np
  from snorm import snorm

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
## SETGMN sets data for the generation of multivariate normal deviates.
#
#  Discussion:
#
#    This procedure packs P, MEANV, and the Cholesky factorization of
#    COVM in PARM.
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
#    Input, real MEANV(P), the means of the multivariate
#    normal distribution.
#
#    Input/output, real COVM(P,P).  On input, the covariance
#    matrix of the multivariate distribution.  On output, the information
#    in COVM has been overwritten.
#
#    Input, integer P, the number of dimensions.
#
#    Output, real PARM(P*(P+3)/2+1), parameters needed to generate
#    multivariate normal deviates.
#
  import numpy as np
  from spofa import spofa
  from sys import exit

  parm = np.zeros ( p * ( p + 3 ) / 2 + 1 )

  if ( p <= 0 ):
    print ( '' )
    print ( 'SETGMN - Fatal error!' )
    print ( '  P was not positive.' )
    exit ( 'SETGMN - Fatal error!' )
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
    print ( 'SETGMN - Fatal error!' )
    print ( '  SPOFA finds COVM not positive definite.' )
    exit ( 'SETGMN - Fatal error!' )
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
## GENMN_TEST tests GENMN.
#
#  Discussion:
#
#    I didn't feel up to creating a test problem for this function.
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
  print ( '' )
  print ( 'GENMN_TEST' )
  print ( '  GENMN generates multivariate normal deviates.' )
  print ( '  Warning! - No test code has been provided.' )
  print ( '' )
  print ( 'GENMN_TEST:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  genmn_test ( )
  timestamp ( )

