#! /usr/bin/env python
#
def multinomial_check ( a, b, c ):

#*****************************************************************************80
#
## MULTINOMIAL_CHECK checks the parameters of the Multinomial PDF.
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
#    Input, integer A, the number of trials.
#
#    Input, integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    Input, real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B ) C(I) = 1.0.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  from i4vec_sum import i4vec_sum

  check = True

  if ( b < 1 ):
    print ( '' )
    print ( 'MULTINOMIAL_CHECK - Fatal error!' )
    print ( '  B < 1.' )
    check = False

  for i in range ( 0, b ):

    if ( c[i] < 0.0 or 1.0 < c[i] ):
      print ( '' )
      print ( 'MULTINOMIAL_CHECK - Fatal error!' )
      print ( '  Input C(I) is out of range.' )
      check = False

  c_sum = i4vec_sum ( b, c )

  if ( 0.0001 < abs ( 1.0 - c_sum ) ):
    print ( '' )
    print ( 'MULTINOMIAL_CHECK - Fatal error!' )
    print ( '  The probabilities do not sum to 1.' )
    check = False

  return check

def multinomial_covariance ( a, b, c ):

#*****************************************************************************80
#
## MULTINOMIAL_COVARIANCE returns the covariances of the Multinomial PDF.
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
#    Input, integer A, the number of trials.
#
#    Input, integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    Input, real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B) C(I) = 1.0.
#
#    Output, real COVARIANCE(B,B), the covariance matrix.
#
  import numpy as np

  covariance = np.zeros ( [ b, b ] )

  for i in range ( 0, b ):
    for j in range ( 0, b ):

      if ( i == j ):
        covariance[i,j] = a * c[i] * ( 1.0 - c[i] )
      else:
        covariance[i,j] = - a * c[i] * c[j]

  return covariance

def multinomial_mean ( a, b, c ):

#*****************************************************************************80
#
## MULTINOMIAL_MEAN returns the means of the Multinomial PDF.
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
#    Input, integer A, the number of trials.
#
#    Input, integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    Input, real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B) C(I) = 1.0.
#
#    Output, real MEAN(B), MEAN(I) is the expected value of the
#    number of outcome I in N trials.
#
  import numpy as np

  mean = np.zeros ( b )

  for i in range ( 0, b ):
    mean[i] = a * c[i]

  return mean

def multinomial_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## MULTINOMIAL_PDF computes a Multinomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = Comb(A,B,X) * Product ( 1 <= I <= B ) C(I)^X(I)
#
#    where Comb(A,B,X) is the multinomial coefficient
#      C( A X(1), X(2), ..., X(B) )
#
#    PDF(X)(A,B,C) is the probability that in A trials there
#    will be exactly X(I) occurrences of event I, whose probability
#    on one trial is C(I), for I from 1 to B.
#
#    As soon as A or B gets large, the number of possible X's explodes,
#    and the probability of any particular X can become extremely small.
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
#    Input, integer X(B) X(I) counts the number of occurrences of
#    outcome I, out of the total of A trials.
#
#    Input, integer A, the total number of trials.
#
#    Input, integer B, the number of different possible outcomes on
#    one trial.
#
#    Input, real C(B) C(I) is the probability of outcome I on
#    any one trial.
#
#    Output, real PDF, the value of the multinomial PDF.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log
#
#  To try to avoid overflow, do the calculation in terms of logarithms.
#  Note that Gamma(A+1) = A factorial.
#
  pdf_log = r8_gamma_log ( float ( a + 1 ) )

  for i in range ( 0, b ):
    pdf_log = pdf_log + x[i] * np.log ( c[i] ) - r8_gamma_log ( float ( x[i] + 1 ) )

  pdf = np.exp ( pdf_log )

  return pdf

def multinomial_pdf_test ( ):

#*****************************************************************************80
#
## MULTINOMIAL_PDF_TEST tests MULTINOMIAL_PDF.
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
  from i4vec_print import i4vec_print
  from r8vec_print import r8vec_print

  b = 3

  print ( '' )
  print ( 'MULTINOMIAL_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MULTINOMIAL_PDF evaluates the Multinomial PDF.' )

  x = np.array ( [ 0, 2, 3 ] )

  a = 5

  c = np.array ( [ 0.10, 0.50, 0.40 ] )

  check = multinomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'MULTINOMIAL_PDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  i4vec_print ( b, x, '  PDF argument X:' )

  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  r8vec_print ( b, c, '  PDF parameter C:' )

  pdf = multinomial_pdf ( x, a, b, c )

  print ( '' )
  print ( '  PDF value =     %14g' % ( pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MULTINOMIAL_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def multinomial_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## MULTINOMIAL_SAMPLE samples the Multinomial PDF.
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
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer-Verlag, New York, 1986, page 559.
#
#  Parameters:
#
#    Input, integer A, the total number of trials.
#    0 <= A.
#
#    Input, integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    Input, real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B) C(I) = 1.0.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X(B), X(I) is the number of
#    occurrences of event I during the N trials.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from binomial import binomial_sample

  ntot = a

  sum2 = 1.0

  x = np.zeros ( b, dtype = np.int32 )

  for ifactor in range ( 0, b - 1 ):

    prob = c[ifactor] / sum2
#
#  Generate a binomial random deviate for NTOT trials with
#  single trial success probability PROB.
#
    s, seed = binomial_sample ( ntot, prob, seed )

    x[ifactor] = s

    ntot = ntot - x[ifactor]
    if ( ntot <= 0 ):
      return x, seed

    sum2 = sum2 - c[ifactor]
#
#  The last factor gets what's left.
#
  x[b-1] = ntot

  return x, seed

def multinomial_sample_test ( ):

#*****************************************************************************80
#
## MULTINOMIAL_SAMPLE_TEST tests MULTINOMIAL_SAMPLE.
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
  from i4row_max import i4row_max
  from i4row_mean import i4row_mean
  from i4row_min import i4row_min
  from i4row_variance import i4row_variance
  from r8vec_print import r8vec_print

  b = 3
  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'MULTINOMIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MULTINOMIAL_MEAN computes the Multinomial mean' )
  print ( '  MULTINOMIAL_SAMPLE samples the Multinomial distribution' )
  print ( '  MULTINOMIAL_VARIANCE computes the Multinomial variance' )

  a = 5

  c = np.array ( [ 0.125, 0.500, 0.375 ] )

  check = multinomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'MULTINOMIAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = multinomial_mean ( a, b, c )
  variance = multinomial_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %6d' % ( b ) )

  r8vec_print ( b, c, '  PDF parameter C:' )

  print ( '' )
  print ( '  PDF means and variances:' )
  print ( '' )
  for i in range ( 0, b ):
    print ( '  %14g  %14g' % ( mean[i], variance[i] ) )
   
  x = np.zeros ( [ b, nsample ] )
  for j in range ( 0, nsample ):
    v, seed = multinomial_sample ( a, b, c, seed )
    for i in range ( 0, b ):
      x[i,j] = v[i]

  xmax = i4row_max ( b, nsample, x )
  xmin = i4row_min ( b, nsample, x )
  mean = i4row_mean ( b, nsample, x )
  variance = i4row_variance ( b, nsample, x )

  print ( '' )
  print ( '  Sample size = %6d' % ( nsample ) )
  print ( '  Component Min, Max, Mean, Variance:' )
  for i in range ( 0, b ):
    print ( '  %6d  %6d  %6d  %14g  %14g' \
      % ( i, xmin[i], xmax[i], mean[i], variance[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MULTINOMIAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def multinomial_variance ( a, b, c ):

#*****************************************************************************80
#
## MULTINOMIAL_VARIANCE returns the variances of the Multinomial PDF.
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
#    Input, integer A, the number of trials.
#
#    Input, integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    Input, real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B ) C(I) = 1.0.
#
#    Output, real VARIANCE(B), VARIANCE(I) is the variance of the
#    total number of events of type I.
#
  import numpy as np

  variance = np.zeros ( b )
  for i in range ( 0, b ):
    variance[i] = a * c[i] * ( 1.0 - c[i] )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  multinomial_pdf_test ( )
  multinomial_sample_test ( )
  timestamp ( )
 
