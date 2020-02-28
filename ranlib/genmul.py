#! /usr/bin/env python
#
def genmul ( n, p, ncat ):

#*****************************************************************************80
#
## GENMUL generates a multinomial random deviate.
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
#    Input, integer N, the number of events, which will be classified into 
#    one of the NCAT categories.
#
#    Input, real P(NCAT-1).  P(I) is the probability that an event
#    will be classified into category I.  Thus, each P(I) must be between
#    0.0 and 1.0.  Only the first NCAT-1 values of P must be defined since
#    P(NCAT) would be 1.0 minus the sum of the first NCAT-1 P's.
#
#    Input, integer NCAT, the number of categories.
#
#    Output, integer IX(NCAT), a random observation from
#    the multinomial distribution.  All IX(i) will be nonnegative and their
#    sum will be N.
#
  import numpy as np
  from ignbin import ignbin
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'GENMUL - Fatal error!' )
    print ( '  N < 0' )
    exit ( 'GENMUL - Fatal error!' )

  if ( ncat <= 1 ):
    print ( '' )
    print ( 'GENMUL - Fatal error!' )
    print ( '  NCAT <= 1' )
    exit ( 'GENMUL - Fatal error!' )

  for i in range ( 0, ncat - 1 ):

    if ( p[i] < 0.0 ):
      print ( ' ' )
      print ( 'GENMUL - Fatal error!' )
      print ( '  Some P(i) < 0.' )
      exit ( 'GENMUL - Fatal error!' )

    if ( 1.0 < p[i] ):
      print ( ' ' )
      print ( 'GENMUL - Fatal error!' )
      print ( '  Some 1 < P(i).' )
      exit ( 'GENMUL - Fatal error!' )

  ptot = np.sum ( p[0:ncat-1] )

  if ( 0.99999 < ptot ):
    print ( ' ' )
    print ( 'GENMUL - Fatal error!' )
    print ( '  1 < Sum of P().' )
    exit ( 'GENMUL - Fatal error!' )
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
## GENMUL_TEST tests GENMUL.
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
  import platform
  from initialize import initialize
  from phrtsd import phrtsd
  from set_initial_seed import set_initial_seed

  print ( '' )
  print ( 'GENMUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GENMUL generates a multinomial random deviate.' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'GENMUL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomize'
  genmul_test ( phrase )
  timestamp ( )

