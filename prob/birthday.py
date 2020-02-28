#! /usr/bin/env python
#
def birthday_cdf ( n ):

#*****************************************************************************80
#
## BIRTHDAY_CDF returns the Birthday Concurrence CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of people whose birthdays have been
#    disclosed.
#
#    Output, real CDF, the probability of at least one matching birthday
#    among N people.
#
  if ( n < 1 ):
    cdf = 0.0
    return cdf
  elif ( 365 < n ):
    cdf = 1.0
    return cdf
#
#  Compute the probability that N people have distinct birthdays.
#
  cdf = 1.0
  for i in range ( 1, n + 1 ):
    cdf = cdf * ( 365 + 1 - i ) / 365.0
#
#  Compute the probability that it is NOT the case that N people
#  have distinct birthdays.  This is the cumulative probability
#  that person 2 matches person 1, or person 3 matches 1 or 2, 
#  etc.
#
  cdf = 1.0 - cdf

  return cdf

def birthday_cdf_inv ( cdf ):

#*****************************************************************************80
#
## BIRTHDAY_CDF_INV inverts the Birthday Concurrence CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the probability that at least
#    two of the N people have matching birthays.
#
#    Output, integer N, the corresponding number of people whose
#    birthdays need to be disclosed.
#
  if ( cdf <= 0.0 ):
    n = 1
    return n
  elif ( 1.0 <= cdf ):
    n = 365
    return n
#
#  Compute the probability that N people have distinct birthdays.
#
  cdf_not = 1.0

  for i in range ( 1, 366 ):
    cdf_not = cdf_not * ( 365 + 1 - i ) / 365.0
    if ( cdf <= 1.0 - cdf_not ):
      n = i
      return n

  n = 365

  return n

def birthday_cdf_test ( ):

#*****************************************************************************80
#
## BIRTHDAY_CDF_TEST tests BIRTHDAY_CDF, BIRTHDAY_CDF_INV, BIRTHDAY_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BIRTHDAY_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BIRTHDAY_CDF evaluates the Birthday CDF' )
  print ( '  BIRTHDAY_CDF_INV inverts the Birthday CDF.' )
  print ( '  BIRTHDAY_PDF evaluates the Birthday PDF' )

  print ( '' )
  print ( '       N            PDF           CDF            CDF_INV' )
  print ( '' )

  for n in range ( 1, 31 ):

    pdf = birthday_pdf ( n )

    cdf = birthday_cdf ( n )

    n2 = birthday_cdf_inv ( cdf )

    print ( '  %8d  %14g  %14g  %8d' % ( n, pdf, cdf, n2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BIRTHDAY_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def birthday_pdf ( n ):

#*****************************************************************************80
#
## BIRTHDAY_PDF returns the Birthday Concurrence PDF.
#
#  Discussion:
#
#    The probability is the probability that the N-th person is the
#    first one to match a birthday with someone earlier.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of people whose birthdays have been
#    disclosed.
#
#    Output, real PDF, the probability that the N-th person
#    is the first to match a birthday with someone earlier.
#
  if ( n < 1 or 365 < n ):
    pdf = 0.0
    return pdf

  pdf = 1.0
#
#  Compute the probability that the first N-1 people have distinct birthdays.
#
  for i in range ( 1, n ):
    pdf = pdf * ( 365 + 1 - i ) / 365.0
#
#  Compute the probability that person N has one of those N-1 birthdays.
#
  pdf = pdf * ( n - 1 ) / 365.0

  return pdf

def birthday_sample ( n, seed ):

#*****************************************************************************80
#
## BIRTHDAY_SAMPLE samples the Birthday Concurrence PDF.
#
#  Discussion:
#
#    The probability is the probability that the N-th person is the
#    first one to match a birthday with someone earlier.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of people whose birthdays have been
#    disclosed.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer VALUE,
#    * 1 if the first N-1 people had distinct
#      birthdays, but person N had a birthday in common with a previous person,
#    * 0 otherwise.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from i4vec_uniform_ab import i4vec_uniform_ab
  from i4vec_unique_count import i4vec_unique_count

  if ( n < 1 ):
    value = 0
    return value, seed
#
#  Choose N birthdays at random.
#
  b, seed = i4vec_uniform_ab ( n, 1, 365, seed )
#
#  Are the first N-1 birthdays unique?
#
  u1 = i4vec_unique_count ( n - 1, b )

  if ( u1 < n - 1 ):
    value = 0
    return value, seed
#
#  Does the N-th birthday match an earlier one?
#
  u2 = i4vec_unique_count ( n, b )

  if ( u2 == n - 1 ):
    value = 1
  else:
    value = 0

  return value, seed

def birthday_sample_test ( ):

#*****************************************************************************80
#
## BIRTHDAY_SAMPLE_TEST tests BIRTHDAY_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_mean import i4vec_mean
#
#  Although other implementations use 10,000 samples, the Python code
#  is too slow for me to wait.
#
  nsample = 10000
  nsample = 1000
  seed = 12345678

  print ( '' )
  print ( 'BIRTHDAY_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BIRTHDAY_SAMPLE samples the Birthday distribution.' )
  print ( '' )
  print ( '   N            Mean           PDF' )
  print ( '' )

  for n in range ( 10, 41 ):

    x = np.zeros ( nsample )
    for i in range ( 0, nsample ):
      x[i], seed = birthday_sample ( n, seed )

    mean = i4vec_mean ( nsample, x )
    pdf = birthday_pdf ( n )

    print ( '  %2d  %14g  %14g' % ( n, mean, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BIRTHDAY_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  birthday_cdf_test ( )
  birthday_sample_test ( )
  timestamp ( )
 
