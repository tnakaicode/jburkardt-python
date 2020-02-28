#! /usr/bin/env python
#
def discrete_cdf ( x, a, b ):

#*****************************************************************************80
#
## DISCRETE_CDF evaluates the Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the item whose probability is desired.
#
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of outcomes
#    1 through A.  Each entry must be nonnegative.
#
#    Output, real CDF, the value of the CDF.
#
  from r8vec_sum import r8vec_sum

  if ( x < 1 ):
    cdf = 0.0
  elif ( x < a ):
    cdf = r8vec_sum ( x, b ) / r8vec_sum ( a, b )
  elif ( a <= x ):
    cdf = 1.0

  return cdf

def discrete_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## DISCRETE_CDF_INV inverts the Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
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
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of outcomes
#    1 through A.  Each entry must be nonnegative.
#
#    Output, integer X, the corresponding argument for which
#    CDF(X-1) < CDF <= CDF(X)
#
  from r8vec_sum import r8vec_sum
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'DISCRETE_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'DISCRETE_CDF_INV - Fatal error!' )

  b_sum = r8vec_sum ( a, b )

  cum = 0.0
  x = a

  for j in range ( 0, a ):

    cum = cum + b[j] / b_sum

    if ( cdf <= cum ):
      x = j + 1
      break

  return x

def discrete_cdf_test ( ):

#*****************************************************************************80
#
## DISCRETE_CDF_TEST tests DISCRETE_CDF, DISCRETE_CDF_INV, DISCRETE_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print

  a = 6

  print ( '' )
  print ( 'DISCRETE_CDF_TEST' )
  print ( '  DISCRETE_CDF evaluates the Discrete CDF' )
  print ( '  DISCRETE_CDF_INV inverts the Discrete CDF.' )
  print ( '  DISCRETE_PDF evaluates the Discrete PDF' )

  b = np.array ( [ 1.0, 2.0, 6.0, 2.0, 4.0, 1.0 ] )

  check = discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'DISCRETE_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
 
  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )

  r8vec_print ( a, b, '  PDF parameters B:' )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = discrete_sample ( a, b, seed )

    pdf = discrete_pdf ( x, a, b )

    cdf = discrete_cdf ( x, a, b )

    x2 = discrete_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DISCRETE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def discrete_check ( a, b ):

#*****************************************************************************80
#
## DISCRETE_CHECK checks the parameters of the Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  import numpy as np

  check = True

  for j in range ( 0, a ):
    if ( b[j] < 0.0 ):
      print ( '' )
      print ( 'DISCRETE_CHECK - Fatal error!' )
      print ( '  Negative probabilities not allowed.' )
      check = False

  b_sum = np.sum ( b )

  if ( b_sum == 0.0 ):
    print ( '' )
    print ( 'DISCRETE_CHECK - Fatal error!' )
    print ( '  Total probablity is zero.' )
    check = False

  return check

def discrete_mean ( a, b ):

#*****************************************************************************80
#
## DISCRETE_MEAN evaluates the mean of the Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  mean = 0.0
  for j in range ( 0, a ):
    mean = mean + float ( j + 1 ) * b[j]

  mean = mean / b_sum

  return mean

def discrete_pdf ( x, a, b ):

#*****************************************************************************80
#
## DISCRETE_PDF evaluates the Discrete PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = B(X) if 1 <= X <= A
#                = 0    otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the item whose probability is desired.
#
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  if ( 1 <= x and x <= a ):
    pdf = b[x-1] / b_sum
  else:
    pdf = 0.0

  return pdf

def discrete_sample ( a, b, seed ):

#*****************************************************************************80
#
## DISCRETE_SAMPLE samples the Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  b_sum = np.sum ( b )

  cdf, seed = r8_uniform_01 ( seed )

  x = discrete_cdf_inv ( cdf, a, b )

  return x, seed

def discrete_sample_test ( ):

#*****************************************************************************80
#
## DISCRETE_SAMPLE_TEST tests DISCRETE_MEAN, DISCRETE_SAMPLE, DISCRETE_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_max import i4vec_max
  from i4vec_mean import i4vec_mean
  from i4vec_min import i4vec_min
  from i4vec_variance import i4vec_variance
  from r8vec_print import r8vec_print

  a = 6
  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'DISCRETE_SAMPLE_TEST' )
  print ( '  DISCRETE_MEAN computes the Discrete mean' )
  print ( '  DISCRETE_SAMPLE samples the Discrete distribution' )
  print ( '  DISCRETE_VARIANCE computes the Discrete variance.' )

  b = np.array ( [ 1.0, 2.0, 6.0, 2.0, 4.0, 1.0 ] )

  check = discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'DISCRETE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = discrete_mean ( a, b )
  variance = discrete_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )

  r8vec_print ( a, b, '  PDF parameters B:' )

  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )  
  for i in range ( 0,  nsample ):
    x[i], seed = discrete_sample ( a, b, seed )

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
  print ( 'DISCRETE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def discrete_variance ( a, b ):

#*****************************************************************************80
#
## DISCRETE_VARIANCE evaluates the variance of the Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of probabilities assigned.
#
#    Input, real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  mean = discrete_mean ( a, b )

  variance = 0.0
  for j in range ( 0, a ):
    variance = variance + b[j] * ( j + 1 - mean ) ** 2

  variance = variance / b_sum

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  discrete_cdf_test ( )
  discrete_sample_test ( )
  timestamp ( )
 
