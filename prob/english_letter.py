#! /usr/bin/env python
#
def english_letter_cdf_inv ( cdf ):

#*****************************************************************************80
#
## ENGLISH_LETTER_CDF_INV inverts the English Letter CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Lewand,
#    Cryptological Mathematics,
#    Mathematics Association of America, 2000,
#    ISBN13: 978-0883857199
#
#  Parameters:
#
#    Input, real CDF, a cumulative probability between 0 and 1.
#
#    Input, character C, the corresponding letter.
#
  import numpy as np

  cdf_vec = np.array ( [ \
    0.00000, \
    0.08167, 0.09659, 0.12441, 0.16694, 0.29396, \
    0.31624, 0.33639, 0.39733, 0.46699, 0.46852, \
    0.47624, 0.51649, 0.54055, 0.60804, 0.68311, \
    0.70240, 0.70335, 0.76322, 0.82649, 0.91705, \
    0.94463, 0.95441, 0.97802, 0.97952, 0.99926, \
    1.00000 ] )

  c = ' '

  for i in range ( 1, 27 ):
    if ( cdf <= cdf_vec[i] ):
      c = chr ( ord ( 'a' ) + i - 1 )
      break

  return c

def english_letter_cdf ( c ):

#*****************************************************************************80
#
## ENGLISH_LETTER_CDF evaluates the English Letter CDF.
#
#  Discussion:
#
#    CDF('c') = 0.12441
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Lewand,
#    Cryptological Mathematics,
#    Mathematics Association of America, 2000,
#    ISBN13: 978-0883857199
#
#  Parameters:
#
#    Input, character C, the letter whose probability is desired.
#    'a' <= c <= 'z', but case is ignored.
#
#    Output, real CDF, the probability that a random letter is less
#    than or equal to C.
#
  import numpy as np

  cdf_vec = np.array ( [ \
    0.00000, \
    0.08167, 0.09659, 0.12441, 0.16694, 0.29396, \
    0.31624, 0.33639, 0.39733, 0.46699, 0.46852, \
    0.47624, 0.51649, 0.54055, 0.60804, 0.68311, \
    0.70240, 0.70335, 0.76322, 0.82649, 0.91705, \
    0.94463, 0.95441, 0.97802, 0.97952, 0.99926, \
    1.00000 ] )

  if ( 'a' <= c and c <= 'z' ):
    i = ord ( c ) - ord ( 'a' ) + 1
    cdf = cdf_vec[i]
  elif ( 'A' <= c and c <= 'Z' ):
    i = ord ( c ) - ord ( 'A' ) + 1
    cdf = cdf_vec[i]
  else:
    cdf = 0.0

  return cdf

def english_letter_cdf_test ( ):

#*****************************************************************************80
#
## ENGLISH_LETTER_CDF_TEST tests ENGLISH_LETTER_CDF, ENGLISH_LETTER_CDF_INV, ENGLISH_LETTER_PDF
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ENGLISH_LETTER_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ENGLISH_LETTER_CDF evaluates the English Letter CDF' )
  print ( '  ENGLISH_LETTER_CDF_INV inverts the English Letter CDF.' )
  print ( '  ENGLISH_LETTER_PDF evaluates the English Letter PDF' )

  seed = 123456789

  print ( '' )
  print ( '   C              PDF             CDF    CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    c, seed = english_letter_sample ( seed )

    pdf = english_letter_pdf ( c )

    cdf = english_letter_cdf ( c )

    c2 = english_letter_cdf_inv ( cdf )

    print ( '  \'%c\'  %14g  %14g        \'%c\'' % ( c, pdf, cdf, c2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ENGLISH_LETTER_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def english_letter_pdf ( c ):

#*****************************************************************************80
#
## ENGLISH_LETTER_PDF evaluates the English Letter PDF.
#
#  Discussion:
#
#    PDF('c') = 0.02782
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Lewand,
#    Cryptological Mathematics,
#    Mathematics Association of America, 2000,
#    ISBN13: 978-0883857199
#
#  Parameters:
#
#    Input, character C, the letter whose probability is desired.
#    'a' <= c <= 'z', but case is ignored.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  pdf_vec = np.array ( [ \
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, \
    0.02228, 0.02015, 0.06094, 0.06966, 0.00153, \
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507, \
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056, \
    0.02758, 0.00978, 0.02361, 0.00150, 0.01974, \
    0.00074 ] )

  if ( 'a' <= c and c <= 'z' ):
    i = ord ( c ) - ord ( 'a' )
    pdf = pdf_vec[i]
  elif ( 'A' <= c and c <= 'Z' ):
    i = ord ( c ) - ord ( 'A' )
    pdf = pdf_vec[i]
  else:
    pdf = 0.0

  return pdf

def english_letter_sample ( seed ):

#*****************************************************************************80
#
## ENGLISH_LETTER_SAMPLE samples the English Letter PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, character C, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  c = english_letter_cdf_inv ( cdf )

  return c, seed

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  english_letter_cdf_test ( )
  timestamp ( )
 
