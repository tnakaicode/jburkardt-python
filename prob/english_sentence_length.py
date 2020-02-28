#! /usr/bin/env python
#
def english_sentence_length_cdf ( x ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_CDF evaluates the English Sentence Length CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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
  from r8vec_sum import r8vec_sum

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  if ( x < 1 ):
    cdf = 0.0
  elif ( x < word_length_max ):
    cdf = r8vec_sum ( x, pdf_vec ) / pdf_sum
  elif ( word_length_max <= x ):
    cdf = 1.0

  return cdf

def english_sentence_length_cdf_inv ( cdf ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_CDF_INV inverts the English Sentence Length CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

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

def english_sentence_length_cdf_test ( ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_CDF_TEST tests ENGLISH_SENTENCE_LENGTH_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789

  print ( '' )
  print ( 'ENGLISH_SENTENCE_LENGTH_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ENGLISH_SENTENCE_LENGTH_CDF evaluates the English Sentence Length CDF' )
  print ( '  ENGLISH_SENTENCE_LENGTH_CDF_INV inverts the English Sentence Length CDF.' )
  print ( '  ENGLISH_SENTENCE_LENGTH_PDF evaluates the English Sentence Length PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = english_sentence_length_sample ( seed )

    pdf = english_sentence_length_pdf ( x )

    cdf = english_sentence_length_cdf ( x )

    x2 = english_sentence_length_cdf_inv ( cdf )

    print ( '  %12d  %12g  %12g  %12d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ENGLISH_SENTENCE_LENGTH_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def english_sentence_length_mean ( ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_MEAN evaluates the mean of the English Sentence Length PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + float ( j + 1 ) * pdf_vec[j]

  mean = mean / pdf_sum

  return mean

def english_sentence_length_pdf ( x ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_PDF evaluates the English Sentence Length PDF.
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
#    05 April 2016
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

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  if ( 1 <= x and x <= word_length_max ):
    pdf = pdf_vec[x-1] / pdf_sum
  else:
    pdf = 0.0

  return pdf

def english_sentence_length_sample ( seed ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_SAMPLE samples the English Sentence Length PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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

  x = english_sentence_length_cdf_inv ( cdf )

  return x, seed

def english_sentence_length_sample_test ( ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_SAMPLE_TEST tests ENGLISH_SENTENCE_LENGTH_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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
  print ( 'ENGLISH_SENTENCE_LENGTH_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ENGLISH_SENTENCE_LENGTH_MEAN computes the English Sentence Length mean' )
  print ( '  ENGLISH_SENTENCE_LENGTH_SAMPLE samples the English Sentence Length distribution' )
  print ( '  ENGLISH_SENTENCE_LENGTH_VARIANCE computes the English Sentence Length variance.' )

  mean = english_sentence_length_mean ( )
  variance = english_sentence_length_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = english_sentence_length_sample ( seed )

  mean = i4vec_mean ( sample_num, x )
  variance = i4vec_variance ( sample_num, x )
  xmax = i4vec_max ( sample_num, x )
  xmin = i4vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %12d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ENGLISH_SENTENCE_LENGTH_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def english_sentence_length_variance ( ):

#*****************************************************************************80
#
## ENGLISH_SENTENCE_LENGTH_VARIANCE: variance of the English Sentence Length PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

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
  english_sentence_length_cdf_test ( )
  english_sentence_length_sample_test ( )
  timestamp ( )
 
