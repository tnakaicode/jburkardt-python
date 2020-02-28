#! /usr/bin/env python
#
def deranged_cdf ( x, a ):

#*****************************************************************************80
#
## DERANGED_CDF evaluates the Deranged CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the maximum number of items in their correct places.
#    0 <= X <= A.
#
#    Input, integer A, the number of items.
#    1 <= A.
#
#    Output, real CDF, the value of the CDF.
#
  from i4_choose import i4_choose
  from r8_factorial import r8_factorial

  if ( x < 0 or a < x ):
    cdf = 0.0
  else:
    sum2 = 0
    for x2 in range ( 0, x + 1 ):
      cnk = i4_choose ( a, x2 )
      dnmk = deranged_enum ( a - x2 )
      sum2 = sum2 + cnk * dnmk
    nfact = r8_factorial ( a )
    cdf = sum2 / nfact

  return cdf

def deranged_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## DERANGED_CDF_INV inverts the Deranged CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, integer A, the number of items.
#    1 <= A.
#
#    Output, integer X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'DERANGED_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'DERANGED_CDF_INV - Fatal error!' )

  cdf2 = 0.0

  for x2 in range ( 0, a + 1 ):

    pdf = deranged_pdf ( x2, a )

    cdf2 = cdf2 + pdf

    if ( cdf <= cdf2 ):
      x = x2
      return x

  x = a

  return x

def deranged_cdf_test ( ):

#*****************************************************************************80
#
## DERANGED_CDF_TEST tests DERANGED_CDF, DERANGED_CDF_INV, DERANGED_PDF
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DERANGED_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DERANGED_CDF evaluates the Deranged CDF' )
  print ( '  DERANGED_CDF_INV inverts the Deranged CDF.' )
  print ( '  DERANGED_PDF evaluates the Deranged PDF' )

  a = 7

  check = deranged_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'DERANGED_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for x in range ( 0, a + 1 ):

    pdf = deranged_pdf ( x, a )

    cdf = deranged_cdf ( x, a )

    x2 = deranged_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DERANGED_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def deranged_check ( a ):

#*****************************************************************************80
#
## DERANGED_CHECK checks the parameter of the Deranged PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the total number of items.
#    1 <= A.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 1 ):
    print ( '' )
    print ( 'DERANGED_CHECK - Fatal error!' )
    print ( '  A < 1.' )
    check = False

  return check

def deranged_enum ( n ):

#*****************************************************************************80
#
## DERANGED_ENUM returns the number of derangements of N objects.
#
#  Discussion:
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#  Recursion:
#
#      D(0) = 1
#      D(1) = 0
#      D(2) = 1
#      D(N) = (N-1) * ( D(N-1) + D(N-2) )
#
#    or
#
#      D(0) = 1
#      D(1) = 0
#      D(N) = N * D(N-1) + (-1)^N
#
#  Formula:
#
#    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
#
#    Based on the inclusion/exclusion law.
#
#    D(N) is the number of ways of placing N non-attacking rooks on
#    an N by N chessboard with one diagonal deleted.
#
#    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
#
#    The number of permutations with exactly K items in the right
#    place is COMB(N,K) * D(N-K).
#
#  First values:
#
#     N         D(N)
#     0           1
#     1           0
#     2           1
#     3           2
#     4           9
#     5          44
#     6         265
#     7        1854
#     8       14833
#     9      133496
#    10     1334961
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects to be permuted.
#
#    Output, integer DN, the number of derangements of N objects.
#
  if ( n < 0 ):

    dn = 0

  elif ( n == 0 ):

    dn = 1

  elif ( n == 1 ):

    dn = 0

  elif ( n == 2 ):

    dn = 1

  else:

    dnm1 = 0
    dn = 1

    for i in range ( 3, n + 1 ):
      dnm2 = dnm1
      dnm1 = dn
      dn = ( i - 1 ) * ( dnm1 + dnm2 )

  return dn

def deranged_mean ( a ):

#*****************************************************************************80
#
## DERANGED_MEAN returns the mean of the Deranged CDF.
#
#  Discussion:
#
#    The mean is computed by straightforward summation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of items.
#    1 <= A.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = 0.0

  for x in range ( 0, a + 1 ):
    pdf = deranged_pdf ( x, a )
    mean = mean + pdf * x

  return mean

def deranged_pdf ( x, a ):

#*****************************************************************************80
#
## DERANGED_PDF evaluates the Deranged PDF.
#
#  Discussion:
#
#    PDF(X)(A) is the probability that exactly X items will occur in
#    their proper place after a random permutation of A items.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the number of items in their correct places.
#    0 <= X <= A.
#
#    Input, integer A, the total number of items.
#    1 <= A.
#
#    Output, real PDF, the value of the PDF.
#
  from i4_choose import i4_choose
  from r8_factorial import r8_factorial

  if ( x < 0 or a < x ):
    pdf = 0.0
  else:
    cnk = i4_choose ( a, x )
    dnmk = deranged_enum ( a - x )
    nfact = r8_factorial ( a )
    pdf = cnk * dnmk / nfact

  return pdf

def deranged_sample ( a, seed ):

#*****************************************************************************80
#
## DERANGED_SAMPLE samples the Deranged PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of items.
#    1 <= A.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = deranged_cdf_inv ( cdf, a )

  return x, seed

def deranged_sample_test ( ):

#*****************************************************************************80
#
## DERANGED_SAMPLE_TEST tests DERANGED_MEAN, DERANGED_VARIANCE, DERANGED_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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
  print ( 'DERANGED_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DERANGED_MEAN computes the Deranged mean.' )
  print ( '  DERANGED_VARIANCE computes the Deranged variance.' )
  print ( '  DERANGED_SAMPLE samples the Deranged distribution.' )

  a = 7

  check = deranged_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'DERANGED_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = deranged_mean ( a )
  variance = deranged_variance ( a )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = deranged_sample ( a, seed )

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
  print ( 'DERANGED_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def deranged_variance ( a ):

#*****************************************************************************80
#
## DERANGED_VARIANCE returns the variance of the Deranged CDF.
#
#  Discussion:
#
#    The variance is computed by straightforward summation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of items.
#    1 <= A.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  mean = deranged_mean ( a )

  variance = 0.0
  for x in range ( 0, a + 1 ):
    pdf = deranged_pdf ( x, a )
    variance = variance + pdf * ( x - mean ) ** 2

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  deranged_cdf_test ( )
  deranged_sample_test ( )
  timestamp ( )


