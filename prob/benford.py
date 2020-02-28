#! /usr/bin/env python
#
def benford_cdf ( x ):

#*****************************************************************************80
#
## BENFORD_CDF returns the Benford CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the string of significant digits to be checked.
#    If X is 1, then we are asking for the Benford probability that
#    a value will have first digit 1.  If X is 123, we are asking for
#    the probability that the first three digits will be 123, and so on.
#
#    Output, real CDF, the Benford probability that an item taken
#    from a real world distribution will have the initial digit of X or less.
#
  import numpy as np
  from i4_is_power_of_10 import i4_is_power_of_10

  if ( x <= 0 ):
    cdf = 0.0
  elif ( i4_is_power_of_10 ( x + 1 ) ):
    cdf = 1.0
  else:
    cdf = np.log10 ( float ( x + 1 ) )
    cdf = ( cdf % 1.0 )

  return cdf

def benford_cdf_test ( ):

#*****************************************************************************80
#
## BENFORD_CDF_TEST tests BENFORD_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BENFORD_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BENFORD_CDF evaluates the Benford CDF.' )

  print ( '' )
  print ( '       N          CDF(N)     CDF(N) by summing' )
  print ( '' )

  cdf2 = 0.0
  for n in range ( 1, 10 ):
    cdf = benford_cdf ( n )
    pdf = benford_pdf ( n )
    cdf2 = cdf2 + pdf
    print ( '  %6d  %14g  %14g' % ( n, cdf, cdf2 ) )

  print ( '' )
  print ( '       N          CDF(N)     CDF(N) by summing' )
  print ( '' )

  cdf2 = 0.0
  for n in range ( 10, 100 ):
    cdf = benford_cdf ( n )
    pdf = benford_pdf ( n )
    cdf2 = cdf2 + pdf
    print ( '  %6d  %14g  %14g' % ( n, cdf, cdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BENFORD_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def benford_pdf ( x ):

#*****************************************************************************80
#
## BENFORD_PDF returns the Benford probability of one or more significant digits.
#
#  Discussion:
#
#    Benford's law is an empirical formula explaining the observed
#    distribution of initial digits in lists culled from newspapers,
#    tax forms, stock market prices, and so on.  It predicts the observed
#    high frequency of the initial digit 1, for instance.
#
#    Note that the probabilities of digits 1 through 9 are guaranteed
#    to add up to 1, since
#      LOG10 ( 2/1 ) + LOG10 ( 3/2) + LOG10 ( 4/3 ) + ... + LOG10 ( 10/9 )
#      = LOG10 ( 2/1 * 3/2 * 4/3 * ... * 10/9 ) = LOG10 ( 10 ) = 1.
#
#    PDF(X) = LOG10 ( ( X + 1 ) / X ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    F Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    Ted Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    R Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Parameters:
#
#    Input, integer X, the string of significant digits to be checked.
#    If X is 1, then we are asking for the Benford probability that
#    a value will have first digit 1.  If X is 123, we are asking for
#    the probability that the first three digits will be 123, and so on.
#
#    Output, real PDF, the Benford probability that an item taken
#    from a real world distribution will have the initial digits X.
#
  import numpy as np

  if ( x <= 0 ):
    pdf = 0.0
  else:
    pdf = np.log10 ( float ( x + 1 ) / float ( x ) )

  return pdf

def benford_pdf_test ( ):

#*****************************************************************************80
#
## BENFORD_PDF_TEST tests BENFORD_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BENFORD_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BENFORD_PDF evaluates the Benford PDF.' )

  print ( '' )
  print ( '       N          PDF(N)' )
  print ( '' )

  for n in range ( 1, 10 ):
    pdf = benford_pdf ( n )
    print ( '  %6d  %14g' % ( n, pdf ) )

  print ( '' )
  print ( '       N          PDF(N)' )
  print ( '' )

  for n in range ( 10, 100 ):
    pdf = benford_pdf ( n )
    print ( '  %6d  %14g' % ( n, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BENFORD_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  benford_cdf_test ( )
  benford_pdf_test ( )
  timestamp ( )
 
