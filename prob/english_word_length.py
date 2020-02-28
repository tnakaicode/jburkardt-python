#! /usr/bin/env python
#
def english_word_length_cdf ( x ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_CDF evaluates the English Word Length CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Parameters:
#
#    Input, integer X, the word length whose CDF is desired.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from i4vec_sum import i4vec_sum

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  if ( x < 1 ):
    cdf = 0.0
  elif ( x < word_length_max ):
    cdf = i4vec_sum ( x, pdf_vec ) / pdf_sum
  elif ( word_length_max <= x ):
    cdf = 1.0

  return cdf

def english_word_length_cdf_inv ( cdf ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_CDF_INV inverts the English Word Length CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Output, integer X, the corresponding word length for which
#    CDF(X-1) < CDF <= CDF(X)
#
  import numpy as np
  from sys import exit

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'ENGLISH_WORD_LENGTH_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'ENGLISH_WORD_LENGTH_CDF_INV - Fatal error!' )

  cum = 0.0

  for j in range ( 0, word_length_max ):

    cum = cum + pdf_vec[j]

    if ( cdf <= cum / pdf_sum ):
      x = j + 1
      return x

  x = word_length_max
  
  return x

def english_word_length_cdf_test ( ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_CDF_TEST tests ENGLISH_WORD_LENGTH_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789

  print ( '' )
  print ( 'ENGLISH_WORD_LENGTH_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ENGLISH_WORD_LENGTH_CDF evaluates the English Word Length CDF' )
  print ( '  ENGLISH_WORD_LENGTH_CDF_INV inverts the English Word Length CDF.' )
  print ( '  ENGLISH_WORD_LENGTH_PDF evaluates the English Word Length PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = english_word_length_sample ( seed )

    pdf = english_word_length_pdf ( x )

    cdf = english_word_length_cdf ( x )

    x2 = english_word_length_cdf_inv ( cdf )

    print ( '  %12d  %12g  %12g  %12d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ENGLISH_WORD_LENGTH_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def english_word_length_mean ( ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_MEAN evaluates the mean of the English Word Length PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Parameters:
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + ( j + 1 ) * pdf_vec[j]

  mean = mean / pdf_sum

  return mean

def english_word_length_pdf ( x ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_PDF evaluates the English Word Length PDF.
#
#  Discussion:
#
#    PDF(A,BX) = B(X) if 1 <= X <= A
#                = 0    otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Parameters:
#
#    Input, integer X, the word length whose probability is desired.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  if ( 1 <= x and x <= word_length_max ):
    pdf = pdf_vec[x-1] / pdf_sum
  else:
    pdf = 0.0

  return pdf

def english_word_length_sample ( seed ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_SAMPLE samples the English Word Length PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Parameters:
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = english_word_length_cdf_inv ( cdf )

  return x, seed

def english_word_length_sample_test ( ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_SAMPLE_TEST tests ENGLISH_WORD_LENGTH_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
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

  sample_num = 1000

  seed = 123456789

  print ( '' )
  print ( 'ENGLISH_WORD_LENGTH_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ENGLISH_WORD_LENGTH_MEAN computes the English Word Length mean' )
  print ( '  ENGLISH_WORD_LENGTH_SAMPLE samples the English Word Length distribution' )
  print ( '  ENGLISH_WORD_LENGTH_VARIANCE computes the English Word Length variance.' )

  mean = english_word_length_mean ( )
  variance = english_word_length_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = english_word_length_sample ( seed )

  mean = i4vec_mean ( sample_num, x )
  variance = i4vec_variance ( sample_num, x )
  xmax = i4vec_max ( sample_num, x )
  xmin = i4vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %12d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14d' % ( xmax ) )
  print ( '  Sample minimum =  %14d' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ENGLISH_WORD_LENGTH_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def english_word_length_variance ( ):

#*****************************************************************************80
#
## ENGLISH_WORD_LENGTH_VARIANCE: variance of the English Word Length PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Parameters:
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + ( j + 1 ) * pdf_vec[j]

  mean = mean / pdf_sum

  variance = 0.0
  for j in range ( 0, word_length_max ):
    variance = variance + pdf_vec[j] * ( j + 1 - mean ) ** 2 

  variance = variance / pdf_sum

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  english_word_length_cdf_test ( )
  english_word_length_sample_test ( )
  timestamp ( )
