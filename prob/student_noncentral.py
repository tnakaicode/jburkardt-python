#! /usr/bin/env python
#
def student_noncentral_cdf ( x, idf, d ):

#*****************************************************************************80
#
## STUDENT_NONCENTRAL_CDF evaluates the noncentral Student T CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Algorithm AS 5,
#    Applied Statistics,
#    Volume 17, 1968, page 193.
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, integer IDF, the number of degrees of freedom.
#
#    Input, real D, the noncentrality parameter.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from normal_01 import normal_01_cdf
  from r8_gamma_log import r8_gamma_log
  from tfn import tfn

  a_max = 100
  emin = 12.5

  f = idf

  if ( idf == 1 ):

    a = x / np.sqrt ( f )
    b = f / ( f + x * x )
    drb = d * np.sqrt ( b )

    cdf2 = normal_01_cdf ( drb )
    cdf = 1.0 - cdf2 + 2.0 * tfn ( drb, a )

  elif ( idf <= a_max ):

    a = x / np.sqrt ( f )
    b = f / ( f + x * x )
    drb = d * np.sqrt ( b )
    sum2 = 0.0

    fmkm2 = 0.0
    if ( abs ( drb ) < emin ):
      cdf2 = normal_01_cdf ( a * drb )
      fmkm2 = a * np.sqrt ( b ) * np.exp ( - 0.5 * drb * drb ) \
        * cdf2 / np.sqrt ( 2.0 * np.pi )

    fmkm1 = b * d * a * fmkm2
    if ( abs ( d ) < emin ):
      fmkm1 = fmkm1 + 0.5 * b * a * np.exp ( - 0.5 * d * d ) / np.pi

    if ( ( idf % 2 ) == 0 ):
      sum2 = fmkm2
    else:
      sum2 = fmkm1

    ak = 1.0

    for k in range ( 2, idf - 1, 2 ):

      fk = float ( k )

      fmkm2 = b * ( d * a * ak * fmkm1 + fmkm2 ) * ( fk - 1.0 ) / fk

      ak = 1.0 / ( ak * ( fk - 1.0 ) )
      fmkm1 = b * ( d * a * ak * fmkm2 + fmkm1 ) * fk / ( fk + 1.0 )

      if ( ( idf % 2 ) == 0 ):
        sum2 = sum2 + fmkm2
      else:
        sum2 = sum2 + fmkm1

      ak = 1.0 / ( ak * fk )

    if ( ( idf % 2 ) == 0 ):
      cdf2 = normal_01_cdf ( d )
      cdf = 1.0 - cdf2 + sum2 * np.sqrt ( 2.0 * np.pi )
    else:
      cdf2 = normal_01_cdf ( drb )
      cdf = 1.0 - cdf2 + 2.0 * ( sum2 + tfn ( drb, a ) )
#
#  Normal approximation.
#
  else:

    a = np.sqrt ( 0.5 * f ) * np.exp ( r8_gamma_log ( 0.5 * ( f - 1.0 ) ) \
      - r8_gamma_log ( 0.5 * f ) ) * d

    temp = ( x - a ) / np.sqrt ( f * ( 1.0 + d * d ) / ( f - 2.0 ) - a * a )

    cdf2 = normal_01_cdf ( temp )
    cdf = cdf2r8_

  return cdf

def student_noncentral_cdf_test ( ):

#*****************************************************************************80
#
## STUDENT_NONCENTRAL_CDF_TEST tests STUDENT_NONCENTRAL_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'STUDENT_NONCENTRAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STUDENT_NONCENTRAL_CDF evaluates the Student Noncentral CDF' )

  x = 0.50

  idf = 10
  b = 1.0

  cdf = student_noncentral_cdf ( x, idf, b )

  print ( '' )
  print ( '  PDF argument X =              %14g' % ( x ) )
  print ( '  PDF parameter IDF =           %6d' % ( idf ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  CDF value =                   %14g' % ( cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STUDENT_NONCENTRAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  student_noncentral_cdf_test ( )
  timestamp ( )

