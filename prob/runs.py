#! /usr/bin/env python
#
def runs_mean ( m, n ):

#*****************************************************************************80
#
## RUNS_MEAN returns the mean of the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = float ( m + 2 * m * n + n ) / float ( m + n )

  return mean

def runs_pdf ( m, n, r ):

#*****************************************************************************80
#
## RUNS_PDF evaluates the Runs PDF.
#
#  Discussion:
#
#    Suppose we have M symbols of one type and N of another, and we consider
#    the various possible permutations of these symbols.
#
#    Let "R" be the number of runs in a given permutation.  By a "run", we
#    mean a maximal sequence of identical symbols.  Thus, for instance,
#    the permutation
#
#      ABBBAAAAAAAA
#
#    has three runs.
#
#    The probability that a permutation of M+N symbols, with M of one kind
#    and N of another, will have exactly R runs is:
#
#      PDF(M,N)(R) = 2 * C(M-1,R/2-1) * C(N-1,R/2-1)
#                    / C(M+N,N) for R even
#
#                  = ( C(M-1,(R-1)/2) * C(N-1,(R-3)/2 )
#                    + C(M-1,(R-3)/2) * C(N-1,(R-1)/2 )
#                    ) / C(M+N,N) for R odd.
#
#    Note that the maximum number of runs for a given M and N is:
#
#      M + N,                if M = N
#      2 * min ( M, N ) + 1  otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kalimutha Krishnamoorthy,
#    Handbook of Statistical Distributions with Applications,
#    Chapman and Hall, 2006,
#    ISBN: 1-58488-635-8,
#    LC: QA273.6.K75.
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#
#    Input, integer R, the number of runs.
#
#    Output, real PDF, the value of the PDF.
#
  from i4_choose import i4_choose
  from sys import exit

  if ( m < 0 ):
    print ( '' )
    print ( 'RUN_PDF - Fatal error!' )
    print ( '  M must be at least 0.' )
    print ( '  The input value of M = %d' % ( m ) )
    exit ( 'RUN_PDF - Fatal error!' )

  if ( n < 0 ):
    print ( '' )
    print ( 'RUN_PDF - Fatal error!' )
    print ( '  N must be at least 0.' )
    print ( '  The input value of N = %d' % ( n ) )
    exit ( 'RUN_PDF - Fatal error!' )

  if ( n + m <= 0 ):
    print ( '' )
    print ( 'RUN_PDF - Fatal error!' )
    print ( '  M+N must be at least 1.' )
    print ( '  The input value of M+N = %d' % ( m + n ) )
    exit ( 'RUN_PDF - Fatal error!' )
#
#  If all the symbols are of one type, there is always 1 run.
#
  if ( m == 0 or n == 0 ):
    if ( r == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0
    return pdf
#
#  Take care of extreme values of R.
#
  if ( r < 2 or m + n < r ):
    pdf = 0.0
    return pdf
#
#  The normal cases.
#
  if ( ( r % 2 ) == 0 ):

    pdf = float ( 2 * i4_choose ( m - 1, ( r / 2 ) - 1 ) \
                    * i4_choose ( n - 1, ( r / 2 ) - 1 ) ) \
        / float (     i4_choose ( m + n, n ) )

  else:

    pdf = float (   i4_choose ( m - 1, ( r - 1 ) / 2 ) \
                  * i4_choose ( n - 1, ( r - 3 ) / 2 ) \
                  + i4_choose ( m - 1, ( r - 3 ) / 2 ) \
                  * i4_choose ( n - 1, ( r - 1 ) / 2 ) ) \
        / float (   i4_choose ( m + n, n ) )

  return pdf

def runs_pdf_test ( ):

#*****************************************************************************80
#
## RUNS_PDF_TEST tests RUNS_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RUNS_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RUNS_PDF evaluates the Runs PDF' )
  print ( '' )
  print ( '  M is the number of symbols of one kind,' )
  print ( '  N is the number of symbols of the other kind,' )
  print ( '  R is the number of runs (sequences of one symbol)' )
  print ( '' )
  print ( '         M         N         R      PDF' )
  print ( '' )

  m = 6

  for n in range ( 0, 9 ):

    print ( '' )
    pdf_total = 0.0

    for r in range ( 1, 2 * min ( m, n ) + 3 ):

      pdf = runs_pdf ( m, n, r )
      print ( '  %8d  %8d  %8d  %14g' % ( m, n, r, pdf ) )
      pdf_total = pdf_total + pdf

    print ( '  %8d                      %14g' % ( m, pdf_total ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RUNS_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def runs_sample ( m, n, seed ):

#*****************************************************************************80
#
## RUNS_SAMPLE samples the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer R, the number of runs.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from i4vec_run_count import i4vec_run_count

  a, seed = runs_simulate ( m, n, seed )

  r = i4vec_run_count ( m + n, a )

  return r, seed

def runs_sample_test ( ):

#*****************************************************************************80
#
## RUNS_SAMPLE_TEST tests RUNS_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_max import i4vec_max
  from i4vec_mean import i4vec_mean
  from i4vec_min import i4vec_min
  from i4vec_variance import i4vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'RUNS_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RUNS_MEAN computes the Runs mean' )
  print ( '  RUNS_SAMPLE samples the Runs distribution.' )
  print ( '  RUNS_VARIANCE computes the Runs variance' )

  m = 10
  n = 5

  print ( '' )
  print ( '  PDF parameter M = %14g' % ( m ) )
  print ( '  PDF parameter N = %14g' % ( n ) )

  mean = runs_mean ( m, n )
  variance = runs_variance ( m, n )

  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = runs_sample ( m, n, seed )

  mean = i4vec_mean ( nsample, x )
  variance = i4vec_variance ( nsample, x )
  xmax = i4vec_max ( nsample, x )
  xmin = i4vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RUNS_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def runs_simulate ( m, n, seed ):

#*****************************************************************************80
#
## RUNS_SIMULATE simulates a case governed by the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(M+N), a sequence of M 0's and N 1's chosen
#    uniformly at random.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  a = np.zeros ( m + n )

  for i in range ( m, m + n ):
    a[i] = 1

  for i in range ( 0, m + n - 1 ):

    j, seed = i4_uniform_ab ( i, m + n - 1, seed )

    k    = a[i]
    a[i] = a[j]
    a[j] = k

  return a, seed

def runs_variance ( m, n ):

#*****************************************************************************80
#
## RUNS_VARIANCE returns the variance of the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = float ( 2 * m * n * ( 2 * m * n - m - n ) ) \
           / float ( ( m + n ) * ( m + n ) * ( m + n - 1 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  runs_pdf_test ( )
  runs_sample_test ( )
  timestamp ( )
 
