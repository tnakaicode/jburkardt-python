#! /usr/bin/env python
#
def i4vec_multinomial_sample ( n, p, m ):

#*****************************************************************************80
#
## I4VEC_MULTINOMIAL_SAMPLE generates a multinomial random deviate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the number of trials.
#    0 < N.
#
#    Input, real P(M).  P(I) is the probability that an event
#    will be classified into category I.  Thus, each P(I) must be between
#    0.0 and 1.0.  
#
#    Input, integer M, the number of possible outcomes on one trial.
#
#    Output, integer X(M), the number of occurrences of each outcome 
#    in N trials.
#
  import numpy as np
  from i4_binomial_sample import i4_binomial_sample

  if ( n <= 0 ):
    print ( '' )
    print ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )
    print ( '  N < 0' )
    exit ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )

  if ( m <= 1 ):
    print ( '' )
    print ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )
    print ( '  M <= 1' )
    exit ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )

  for i in range ( 0, m ):

    if ( p[i] < 0.0 ):
      print ( '' )
      print ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )
      print ( '  Some P(i) < 0.' )
      exit ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )

    if ( 1.0 < p[i] ):
      print ( '' )
      print ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )
      print ( '  Some 1 < P(i).' )
      exit ( 'I4VEC_MULTINOMIAL_SAMPLE - Fatal error!' )
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
    x[i] = i4_binomial_sample ( ntot, prob )
    ntot = ntot - x[i]
    if ( ntot <= 0 ):
      return x
    ptot = ptot - p[i]

  x[m-1] = ntot

  return x

def i4vec_multinomial_sample_test ( ):

#*****************************************************************************80
#
## I4VEC_MULTINOMIAL_SAMPLE_TEST tests I4VEC_MULTINOMIAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_multinomial_pdf import i4vec_multinomial_pdf
  from i4_uniform_ab import i4_uniform_ab
  from r8vec_uniform_ab import r8vec_uniform_ab

  seed = 123456789

  print ( '' )
  print ( 'I4VEC_MULTINOMIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_MULTINOMIAL_SAMPLE samples the multinomial distribution.' )
  print ( '' )
  print ( '     N     M     I      P        X        PDF()' )

  for k in range ( 0, 10 ):
    m, seed = i4_uniform_ab ( 2, 10, seed )
    n, seed = i4_uniform_ab ( 1, 5, seed )
    p, seed = r8vec_uniform_ab ( m, 0.0, 1.0, seed )
    ptot = np.sum ( p )
    p = p / ptot
    x = i4vec_multinomial_sample ( n, p, m )
    pdf = i4vec_multinomial_pdf ( n, p, m, x )
    print ( '' )
    for i in range ( 0, m ):
      print ( '              %4d  %8.4f  %4d' % ( i, p[i], x[i] ) )
    print ( '  %4d  %4d                        %14.6g' % ( n, m, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_MULTINOMIAL_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  timestamp ( )
  initialize ( )
  i4vec_multinomial_sample_test ( )
  timestamp ( )

