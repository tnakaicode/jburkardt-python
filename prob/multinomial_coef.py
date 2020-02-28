#! /usr/bin/env python
#
def multinomial_coef_test ( ):

#*****************************************************************************80
#
## MULTINOMIAL_COEF_TEST tests MULTINOMIAL_COEF1, MULTINOMIAL_COEF2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'MULTINOMIAL_COEF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MULTINOMIAL_COEF1 computes multinomial coefficients using the Gamma function' )
  print ( '  MULTINOMIAL_COEF2 computes multinomial coefficients directly.' )

  print ( '' )
  print ( '  Line 10 of the BINOMIAL table:' )
  print ( '' )

  n = 10
  nfactor = 2
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i
    factor[1] = n - i

    ncomb1 = multinomial_coef1 ( nfactor, factor )

    ncomb2 = multinomial_coef2 ( nfactor, factor )

    print ( '  %4d  %4d  %5d  %5d' % ( factor[0], factor[1], ncomb1, ncomb2 ) )

  print ( '' )
  print ( '  Level 5 of the TRINOMIAL coefficients:' )

  n = 5
  nfactor = 3
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i

    print ( '' )

    for j in range ( 0, n - factor[0] + 1 ):

      factor[1] = j
      factor[2] = n - factor[0] - factor[1]

      ncomb1 = multinomial_coef1 ( nfactor, factor )

      ncomb2 = multinomial_coef2 ( nfactor, factor )

      print ( '  %4d  %4d  %4d  %5d  %5d' \
        % ( factor[0], factor[1], factor[2], ncomb1, ncomb2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MULTINOMIAL_COEF_TEST' )
  print ( '  Normal end of execution.' )
  return

def multinomial_coef1 ( nfactor, factor ):

#*****************************************************************************80
#
## MULTINOMIAL_COEF1 computes a Multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    The log of the gamma function is used, to avoid overflow.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NFACTOR, the number of factors.
#    1 <= NFACTOR.
#
#    Input, integer FACTOR(NFACTOR), contains the factors.
#    0.0 <= FACTOR(I).
#
#    Output, integer NCOMB, the value of the multinomial coefficient.
#
  import numpy as np
  from i4vec_sum import i4vec_sum
  from r8_gamma_log import r8_gamma_log
#
#  The factors sum to N.
#
  n = i4vec_sum ( nfactor, factor )

  facn = r8_gamma_log ( float ( n + 1 ) )

  for i in range ( 0, nfactor ):

    facn = facn - r8_gamma_log ( float ( factor[i] + 1 ) )

  ncomb = int ( round ( np.exp ( facn ) ) )

  return ncomb

def multinomial_coef2 ( nfactor, factor ):

#*****************************************************************************80
#
## MULTINOMIAL_COEF2 computes a Multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    A direct method is used, which should be exact.  However, there
#    is a possibility of intermediate overflow of the result.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NFACTOR, the number of factors.
#    1 <= NFACTOR.
#
#    Input, integer FACTOR(NFACTOR), contains the factors.
#    0.0 <= FACTOR(I).
#
#    Output, integer NCOMB, the value of the multinomial coefficient.
#
  ncomb = 1
  k = 0

  for i in range ( 0, nfactor ):

    for j in range ( 1, factor[i] + 1 ):
      k = k + 1
      ncomb = ( ncomb * k ) / j

  return ncomb

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  multinomial_coef_test ( )
  timestamp ( )
 
