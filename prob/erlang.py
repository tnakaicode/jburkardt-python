#! /usr/bin/env python
#
def erlang_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## ERLANG_CDF evaluates the Erlang CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_gamma_inc import r8_gamma_inc

  if ( x < a ):

    cdf = 0.0

  else:

    x2 = ( x - a ) / b
    p2 = c

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def erlang_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## ERLANG_CDF_INV inverts the Erlang CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Output, real X, the corresponding argument of the CDF.
#
  from sys import exit

  it_max = 100
  r8_huge = 1.0E+30
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a
    return x
  elif ( 1.0 <= cdf ):
    x = r8_huge
    return x

  x1 = a
  cdf1 = 0.0

  x2 = a + 1.0

  while ( True ):

    cdf2 = erlang_cdf ( x2, a, b, c )

    if ( cdf < cdf2 ):
      break

    x2 = a + 2.0 * ( x2 - a )
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = erlang_cdf ( x3, a, b, c )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'ERLANG_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'ERLANG_CDF_INV - Fatal error!' )

    if ( ( cdf3 <= cdf and cdf1 <= cdf ) or ( cdf <= cdf3 and cdf <= cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def erlang_cdf_test ( ):

#*****************************************************************************80
#
## ERLANG_CDF_TEST tests ERLANG_CDF, ERLANG_CDF_INV, ERLANG_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ERLANG_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ERLANG_CDF evaluates the Erlang CDF.' )
  print ( '  ERLANG_CDF_INV inverts the Erlang CDF.' )
  print ( '  ERLANG_PDF evaluates the Erlang PDF.' )

  a = 1.0
  b = 2.0
  c = 3

  check = erlang_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'ERLANG_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = erlang_sample ( a, b, c, seed )

    pdf = erlang_pdf ( x, a, b, c )

    cdf = erlang_cdf ( x, a, b, c )

    x2 = erlang_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ERLANG_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def erlang_check ( a, b, c ):

#*****************************************************************************80
#
## ERLANG_CHECK checks the parameters of the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'ERLANG_CHECK - Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  if ( c <= 0 ):
    print ( '' )
    print ( 'ERLANG_CHECK - Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def erlang_mean ( a, b, c ):

#*****************************************************************************80
#
## ERLANG_MEAN returns the mean of the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean =  a + b * c

  return mean

def erlang_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## ERLANG_PDF evaluates the Erlang PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = ( ( X - A ) / B )^( C - 1 )
#      / ( B * Gamma ( C ) * EXP ( ( X - A ) / B ) )
#
#    for 0 < B, 0 < C integer, A <= X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_factorial import r8_factorial

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = y ** ( c - 1 ) / ( b * r8_factorial ( c - 1 ) * np.exp ( y ) )

  return pdf

def erlang_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## ERLANG_SAMPLE samples the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from exponential import exponential_sample

  a2 = 0.0
  b2 = b
  x = a
  for i in range ( 0, c ):
    x2, seed = exponential_sample ( a2, b2, seed )
    x = x + x2

  return x, seed

def erlang_sample_test ( ):

#*****************************************************************************80
#
## ERLANG_SAMPLE_TEST tests ERLANG_MEAN, ERLANG_SAMPLE, ERLANG_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'ERLANG_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ERLANG_MEAN computes the Erlang mean' )
  print ( '  ERLANG_SAMPLE samples the Erlang distribution' )
  print ( '  ERLANG_VARIANCE computes the Erlang variance.' )

  a = 1.0
  b = 2.0
  c = 3

  check = erlang_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'ERLANG_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = erlang_mean ( a, b, c )
  variance = erlang_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )
  print ( '  PDF mean =     %14g' % ( mean ) )
  print ( '  PDF variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = erlang_sample ( a, b, c, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ERLANG_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def erlang_variance ( a, b, c ):

#*****************************************************************************80
#
## ERLANG_VARIANCE returns the variance of the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance =  b * b * c

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  erlang_cdf_test ( )
  erlang_sample_test ( )
  timestamp ( )
 
