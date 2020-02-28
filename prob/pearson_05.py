#! /usr/bin/env python3
#
def pearson_05_check ( a, b, c ):

#*****************************************************************************80
#
## PEARSON_05_CHECK checks the parameters of the Pearson 5 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'PEARSON_05_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'PEARSON_05_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def pearson_05_mean ( a, b, c ):

#*****************************************************************************80
#
## PEARSON_05_MEAN evaluates the mean of the Pearson 5 PDF.
#
#  Discussion:
#
#    The mean is undefined for B <= 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  from sys import exit

  if ( b <= 1.0 ):
    print ( '' )
    print ( 'PEARSON_05_MEAN - Fatal error!' )
    print ( '  MEAN undefined for B <= 1.' )
    exit ( 'PEARSON_05_MEAN - Fatal error!' )

  mean = c + a / ( b - 1.0 )

  return mean

def pearson_05_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## PEARSON_05_PDF evaluates the Pearson 5 PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = A^B * ( X - C )^(-B-1)
#      * exp ( - A / ( X - C ) ) / Gamma ( B )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    v
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    C < X
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  if ( x <= c ):
    pdf = 0.0
  else:
    pdf = a ** b * ( x - c ) ** ( - b - 1.0 ) \
      * np.exp ( - a / ( x - c ) ) / r8_gamma ( b )

  return pdf

def pearson_05_pdf_test ( ):

#*****************************************************************************80
#
## PEARSON_05_PDF_TEST tests PEARSON_05_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PEARSON_05_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PEARSON_05_PDF evaluates the Pearson 05 PDF.' )

  x = 5.0

  a = 1.0
  b = 2.0
  c = 3.0

  check = pearson_05_check ( a, b, c )
 
  if ( not check ):
    print ( '' )
    print ( 'PEARSON_05_PDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  pdf = pearson_05_pdf ( x, a, b, c )

  print ( '' )
  print ( '  PDF argument X =  %14g' % ( x ) )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF value =       %14g' % ( pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PEARSON_05_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def pearson_05_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## PEARSON_05_SAMPLE samples the Pearson 5 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from gamma_sample import gamma_sample

  a2 = 0.0
  b2 = b
  c2 = 1.0 / a

  x2, seed = gamma_sample ( a2, b2, c2, seed )

  x = c + 1.0 / x2

  return x, seed

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  pearson_05_pdf_test ( )
  timestamp ( )
 
