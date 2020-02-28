#! /usr/bin/env python
#
def hypergeometric_cdf ( x, n, m, l ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_CDF evaluates the Hypergeometric CDF.
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
#  Parameters:
#
#    Input, integer X, the argument of the CDF.
#
#    Input, integer N, the number of balls selected.
#    0 <= N <= L.
#
#    Input, integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    Input, integer L, the number of balls to select from.
#    0 <= L.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from i4_choose_log import i4_choose_log

  c1_log = i4_choose_log ( l - m, n )
  c2_log = i4_choose_log ( l, n )

  pdf = np.exp ( c1_log - c2_log )
  cdf = pdf

  for x2 in range ( 0, x ):

    pdf = pdf * float ( ( m - x2 ) * ( n - x2 ) ) \
      / float ( ( x2 + 1 ) * ( l - m - n + x2 + 1 ) )

    cdf = cdf + pdf

  return cdf

def hypergeometric_cdf_test ( ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_CDF_TEST tests HYPERGEOMETRIC_CDF.
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

  print ( '' )
  print ( 'HYPERGEOMETRIC_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HYPERGEOMETRIC_CDF evaluates the Hypergeometric CDF.' )
  print ( '  HYPERGEOMETRIC_PDF evaluates the Hypergeometric PDF.' )

  x = 7

  n = 10
  m = 7
  l = 100

  check = hypergeometric_check ( n, m, l )

  if ( not check ):
    print ( '' )
    print ( 'HYPERGEOMETRIC_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  pdf = hypergeometric_pdf ( x, n, m, l )

  cdf = hypergeometric_cdf ( x, n, m, l )

  print ( '' )
  print ( '  PDF argument X =                %6d' % ( x ) )
  print ( '  Total number of balls =         %6d' % ( l ) )
  print ( '  Number of white balls =         %6d' % ( m ) )
  print ( '  Number of balls taken =         %6d' % ( n ) )
  print ( '  PDF value =                   = %14g' % ( pdf ) )
  print ( '  CDF value =                   = %14g' % ( cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HYPERGEOMETRIC_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def hypergeometric_check ( n, m, l ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_CHECK checks the parameters of the Hypergeometric CDF.
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
#  Parameters:
#
#    Input, integer N, the number of balls selected.
#    0 <= N <= L.
#
#    Input, integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    Input, integer L, the number of balls to select from.
#    0 <= L.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( n < 0 or l < n ):
    print ( '' )
    print ( 'HYPERGEOMETRIC_CHECK - Fatal error!' )
    print ( '  Input N is out of range.' )
    check = False

  if ( m < 0 or l < m ):
    print ( '' )
    print ( 'HYPERGEOMETRIC_CHECK - Fatal error!' )
    print ( '  Input M is out of range.' )
    check = False

  if ( l < 0 ):
    print ( '' )
    print ( 'HYPERGEOMETRIC_CHECK - Fatal error!' )
    print ( '  Input L is out of range.' )
    check = False

  return check

def hypergeometric_mean ( n, m, l ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_MEAN returns the mean of the Hypergeometric PDF.
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
#  Parameters:
#
#    Input, integer N, the number of balls selected.
#    0 <= N <= L.
#
#    Input, integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    Input, integer L, the number of balls to select from.
#    0 <= L.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = float ( n * m ) / float ( l )

  return mean

def hypergeometric_pdf ( x, n, m, l ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_PDF evaluates the Hypergeometric PDF.
#
#  Discussion:
#
#    PDF(X)(N,M,L) = C(M,X) * C(L-M,N-X) / C(L,N).
#
#    PDF(X)(N,M,L) is the probability of drawing X white balls in a
#    single random sample of size N from a population containing
#    M white balls and a total of L balls.
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
#  Parameters:
#
#    Input, integer X, the desired number of white balls.
#    0 <= X <= N, usually, although any value of X can be given.
#
#    Input, integer N, the number of balls selected.
#    0 <= N <= L.
#
#    Input, integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    Input, integer L, the number of balls to select from.
#    0 <= L.
#
#    Output, real PDF, the probability of exactly K white balls.
#
  import numpy as np
  from i4_choose_log import i4_choose_log
#
#  Special cases.
#
  if ( x < 0 ):

    pdf = 1.0

  elif ( n < x ):

    pdf = 0.0

  elif ( m < x ):

    pdf = 0.0

  elif ( l < x ):

    pdf = 0.0

  elif ( n == 0 ):

    if ( x == 0 ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    c1 = i4_choose_log (     m,     x )
    c2 = i4_choose_log ( l - m, n - x )
    c3 = i4_choose_log ( l,     n     )

    pdf_log = c1 + c2 - c3

    pdf = np.exp ( pdf_log )

  return pdf

def hypergeometric_sample ( n, m, l, seed ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_SAMPLE samples the Hypergeometric PDF.
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
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 165.
#
#  Parameters:
#
#    Input, integer N, the number of balls selected.
#    0 <= N <= L.
#
#    Input, integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    Input, integer L, the number of balls to select from.
#    0 <= L.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_choose_log import i4_choose_log
  from r8_uniform_01 import r8_uniform_01

  c1_log = i4_choose_log ( l - m, n )
  c2_log = i4_choose_log ( l, n,  )

  a = np.exp ( c1_log - c2_log )
  b = a

  u, seed = r8_uniform_01 ( seed )

  x = 0

  while ( a < u ):

    b = b * float ( ( m - x ) * ( n - x ) ) / float ( ( x + 1 ) * ( l - m - n + x + 1 ) )

    a = a + b

    x = x + 1

  return x, seed

def hypergeometric_sample_test ( ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_SAMPLE_TEST tests HYPERGEOMETRIC_SAMPLE.
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

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'HYPERGEOMETRIC_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HYPERGEOMETRIC_MEAN computes the Hypergeometric mean' )
  print ( '  HYPERGEOMETRIC_SAMPLE samples the Hypergeometric distribution' )
  print ( '  HYPERGEOMETRIC_VARIANCE computes the Hypergeometric variance.' )

  n = 10
  m = 7
  l = 100

  check = hypergeometric_check ( n, m, l )

  if ( not check ):
    print ( '' )
    print ( 'HYPERGEOMETRIC_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = hypergeometric_mean ( n, m, l )
  variance = hypergeometric_variance ( n, m, l )

  print ( '' )
  print ( '  PDF parameter N =             %6d' % ( n ) )
  print ( '  PDF parameter M =             %6d' % ( m ) )
  print ( '  PDF parameter L =             %6d' % ( l ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = hypergeometric_sample ( n, m, l, seed )

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
  print ( 'HYPERGEOMETRIC_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def hypergeometric_variance ( n, m, l ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_VARIANCE returns the variance of the Hypergeometric PDF.
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
#  Parameters:
#
#    Input, integer N, the number of balls selected.
#    0 <= N <= L.
#
#    Input, integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    Input, integer L, the number of balls to select from.
#    0 <= L.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = float ( n * m * ( l - m ) * ( l - n ) ) / float ( l * l * ( l - 1 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  hypergeometric_cdf_test ( )
  hypergeometric_sample_test ( )
  timestamp ( )
