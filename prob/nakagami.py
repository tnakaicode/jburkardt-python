#! /usr/bin/env python
#
def nakagami_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## NAKAGAMI_CDF evaluates the Nakagami CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_gamma_inc import r8_gamma_inc

  if ( x <= 0.0 ):

    cdf = 0.0

  elif ( 0.0 < x ):

    y = ( x - a ) / b
    x2 = c * y * y
    p2 = c

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def nakagami_cdf_test ( ):

#*****************************************************************************80
#
## NAKAGAMI_CDF_TEST tests NAKAGAMI_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'NAKAGAMI_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NAKAGAMI_CDF evaluates the Nakagami CDF' )
  print ( '  NAKAGAMI_PDF evaluates the Nakagami PDF' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = nakagami_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'NAKAGAMI_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 1, 11 ):

    x = a + b + np.sqrt ( float ( i ) / c / 10.0 )

    pdf = nakagami_pdf ( x, a, b, c )

    cdf = nakagami_cdf ( x, a, b, c )

    x2 = nakagami_cdf_inv ( cdf, a, b, c )

    print ( '  %14.6g%14.6g%14.6g%14.6g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NAKAGAMI_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def nakagami_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## NAKAGAMI_CDF_INV inverts the Nakagami CDF.
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
#    03 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, real X, the corresponding argument of the CDF.
#
  from r8_huge import r8_huge
  from sys import exit

  it_max = 100
  tol = 0.000001

  if ( cdf <= 0.0 ):
    x = c * a * a
    return x
  elif ( 1.0 <= cdf ):
    x = r8_huge ( )
    return x

  x1 = a
  cdf1 = 0.0

  x2 = a + 1.0

  while ( True ):

    cdf2 = nakagami_cdf ( x2, a, b, c )

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
    cdf3 = nakagami_cdf ( x3, a, b, c )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      return x

    if ( it_max < it ):
      print ( '' )
      print ( 'NAKAGAMI_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'NAKAGAMI_CDF_INV - Fatal error!' )

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def nakagami_check ( a, b, c ):

#*****************************************************************************80
#
## NAKAGAMI_CHECK checks the parameters of the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'NAKAGAMI_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'NAKAGAMI_CHECK - Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def nakagami_mean ( a, b, c ):

#*****************************************************************************80
#
## NAKAGAMI_MEAN returns the mean of the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  mean = a + b * r8_gamma ( c + 0.5 ) / ( np.sqrt ( c ) * r8_gamma ( c ) )

  return mean

def nakagami_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## NAKAGAMI_PDF evaluates the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  if ( x <= 0.0 ):

    pdf = 0.0

  elif ( 0.0 < x ):

    y = ( x - a ) / b

    pdf = 2.0 * c ** c / ( b * r8_gamma ( c ) ) * y ** ( 2.0 * c - 1.0 ) \
    * np.exp ( -c * y * y )

  return pdf

def nakagami_sample_test ( ):

#*****************************************************************************80
#
## NAKAGAMI_SAMPLE_TEST tests NAKAGAMI_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NAKAGAMI_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NAKAGAMI_MEAN computes the Nakagami mean' )
  print ( '  NAKAGAMI_VARIANCE computes the Nakagami variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = nakagami_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'NAKAGAMI_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = nakagami_mean ( a, b, c )
  variance = nakagami_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NAKAGAMI_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def nakagami_variance ( a, b, c ):

#*****************************************************************************80
#
## NAKAGAMI_VARIANCE returns the variance of the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from r8_gamma import r8_gamma

  t1 = r8_gamma ( c + 0.5 )
  t2 = r8_gamma ( c )

  variance = b * b * ( 1.0 - t1 * t1 / ( c * t2 * t2 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  nakagami_cdf_test ( )
  nakagami_sample_test ( )
  timestamp ( )
