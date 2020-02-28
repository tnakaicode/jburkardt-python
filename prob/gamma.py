#! /usr/bin/env python
#
def gamma_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## GAMMA_CDF evaluates the Gamma CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    A <= X
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_gamma_inc import r8_gamma_inc

  x2 = ( x - a ) / b
  p2 = c

  cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def gamma_cdf_test ( ):

#*****************************************************************************80
#
## GAMMA_CDF_TEST tests GAMMA_CDF, GAMMA_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = 1.0
  b = 1.5
  c = 3.0

  print ( '' )
  print ( 'GAMMA_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_CDF evaluates the Gamma CDF.' )
  print ( '  GAMMA_PDF evaluates the Gamma PDF.' )
  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )

  check = gamma_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'GAMMA_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  seed = 123456789

  print ( '' )
  print ( '  X  PDF   CDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = gamma_sample ( a, b, c, seed )

    cdf = gamma_cdf ( x, a, b, c )

    pdf = gamma_pdf ( x, a, b, c )

    print ( '  %12g  %12g  %12g' % ( x, pdf, cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GAMMA_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def gamma_check ( a, b, c ):

#*****************************************************************************80
#
## GAMMA_CHECK checks the parameters of the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
    print ( 'GAMMA_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    print ( '  B = %g' % ( b ) )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'GAMMA_CHECK - Fatal error!' )
    print ( '  C <= 0.' )
    print ( '  C = %g' % ( c ) )
    check = False

  return check

def gamma_mean ( a, b, c ):

#*****************************************************************************80
#
## GAMMA_MEAN returns the mean of the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
#    Output, real MEAN, the mean of the PDF.
#
  mean = a + b * c

  return mean

def gamma_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## GAMMA_PDF evaluates the Gamma PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = EXP ( - ( X - A ) / B ) * ( ( X - A ) / B )^(C-1)
#      / ( B * GAMMA ( C ) )
#
#    GAMMA_PDF(A,B,C), where C is an integer, is the Erlang PDF.
#    GAMMA_PDF(A,B,1) is the Exponential PDF.
#    GAMMA_PDF(0,2,C/2) is the Chi Squared PDF with C degrees of freedom.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    A <= X.
#
#    Input, real A, B, C, the parameters of the PDF.
#    A controls the location of the peak  A is often chosen to be 0.0.
#    B is the "scale" parameter 0.0 < B, and is often 1.0.
#    C is the "shape" parameter 0.0 < C, and is often 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = y ** ( c - 1.0 ) / ( b * r8_gamma ( c ) * np.exp ( y ) )

  return pdf

def gamma_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## GAMMA_SAMPLE samples the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2004
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    J H Ahrens and U Dieter,
#    Generating Gamma Variates by a Modified Rejection Technique,
#    Communications of the ACM,
#    Volume 25, Number 1, January 1982, pages 47 - 54.
#
#    J H Ahrens and U Dieter,
#    Computer Methods for Sampling from Gamma, Beta, Poisson and
#    Binomial Distributions.
#    Computing, Volume 12, 1974, pages 223 - 246.
#
#    J H Ahrens, K D Kohrt, and U Dieter,
#    Algorithm 599,
#    ACM Transactions on Mathematical Software,
#    Volume 9, Number 2, June 1983, pages 255-257.
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from exponential_01 import exponential_01_sample
  from normal_01 import normal_01_sample
  from r8_uniform_01 import r8_uniform_01

  a1 =   0.3333333
  a2 = - 0.2500030
  a3 =   0.2000062
  a4 = - 0.1662921
  a5 =   0.1423657
  a6 = - 0.1367177
  a7 =   0.1233795
  e1 = 1.0
  e2 = 0.4999897
  e3 = 0.1668290
  e4 = 0.0407753
  e5 = 0.0102930
  euler = 2.71828182845904
  q1 =   0.04166669
  q2 =   0.02083148
  q3 =   0.00801191
  q4 =   0.00144121
  q5 = - 0.00007388
  q6 =   0.00024511
  q7 =   0.00024240
#
#  Allow C = 0.
#
  if ( c == 0.0 ):
    x = a
    return x, seed
#
#  C < 1.
#
  if ( c < 1.0 ):

    while ( True ):

      u, seed = r8_uniform_01 ( seed )
      t = 1.0 + c / euler
      p = u * t

      s, seed = exponential_01_sample ( seed )

      if ( p < 1.0 ):
        x = np.exp ( np.log ( p ) / c )
        if ( x <= s ):
          break
      else:
        x = - np.log ( ( t - p ) / c )
        if ( ( 1.0 - c ) * np.log ( x ) <= s ):
          break

    x = a + b * x
    return x, seed
#
#  1 <= C.
#
  else:

    s2 = c - 0.5
    s = np.sqrt ( c - 0.5 )
    d = np.sqrt ( 32.0 ) - 12.0 * np.sqrt ( c - 0.5 )

    t, seed = normal_01_sample ( seed )
    x = ( np.sqrt ( c - 0.5 ) + 0.5 * t ) ** 2

    if ( 0.0 <= t ):
      x = a + b * x
      return x, seed

    u, seed = r8_uniform_01 ( seed )

    if ( d * u <= t ** 3 ):
      x = a + b * x
      return x, seed

    r = 1.0 / c

    q0 = ( ( ( ( ( ( \
           q7   * r \
         + q6 ) * r \
         + q5 ) * r \
         + q4 ) * r \
         + q3 ) * r \
         + q2 ) * r \
         + q1 ) * r

    if ( c <= 3.686 ):
      bcoef = 0.463 + s - 0.178 * s2
      si = 1.235
      co = 0.195 / s - 0.079 + 0.016 * s
    elif ( c <= 13.022 ):
      bcoef = 1.654 + 0.0076 * s2
      si = 1.68 / s + 0.275
      co = 0.062 / s + 0.024
    else:
      bcoef = 1.77
      si = 0.75
      co = 0.1515 / s

    if ( 0.0 < np.sqrt ( c - 0.5 ) + 0.5 * t ):

      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * ( ( ( ( ( ( \
               a7   * v \
             + a6 ) * v \
             + a5 ) * v \
             + a4 ) * v \
             + a3 ) * v \
             + a2 ) * v \
             + a1 ) * v

      if ( np.log ( 1.0 - u ) <= q ):
        x = a + b * x
        return x, seed

    while ( True ):

      e, seed = exponential_01_sample ( seed )

      u, seed = r8_uniform_01 ( seed )

      u = 2.0 * u - 1.0
      if ( u < 0.0 ):
        t = bcoef - si * e
      else:
        t = bcoef + si * e

      if ( - 0.7187449 <= t ):

        v = 0.5 * t / s

        if ( 0.25 < abs ( v ) ):
          q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
        else:
          q = q0 + 0.5 * t * t * ( ( ( ( ( ( \
               a7   * v \
             + a6 ) * v \
             + a5 ) * v \
             + a4 ) * v \
             + a3 ) * v \
             + a2 ) * v \
             + a1 ) * v

        if ( 0.0 < q ):

          if ( 0.5 < q ):
            w = np.exp ( q ) - 1.0
          else:
            w = ( ( ( ( \
                    e5   * q \
                  + e4 ) * q \
                  + e3 ) * q \
                  + e2 ) * q \
                  + e1 ) * q

          if ( co * abs ( u ) <= w * np.exp ( e - 0.5 * t * t ) ):
            x = a + b * ( s + 0.5 * t ) ** 2
            return x, seed

  return x, seed

def gamma_sample_test ( ):

#*****************************************************************************80
#
## GAMMA_SAMPLE_TEST tests GAMMA_MEAN, GAMMA_SAMPLE, GAMMA_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
  test_num = 2
  seed = 123456789

  print ( '' )
  print ( 'GAMMA_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_MEAN computes the Gamma mean' )
  print ( '  GAMMA_SAMPLE samples the Gamma distribution' )
  print ( '  GAMMA_VARIANCE computes the Gamma variance.' )

  a_test = np.array ( [ 1.0, 2.0 ] )
  b_test = np.array ( [ 3.0, 0.5 ] )
  c_test = np.array ( [ 2.0, 0.5 ] )

  for test_i in range ( 0, 2 ):

    a = a_test[test_i]
    b = b_test[test_i]
    c = c_test[test_i]

    check = gamma_check ( a, b, c )

    if ( not check ):
      print ( '' )
      print ( 'GAMMA_SAMPLE_TEST - Fatal error!' )
      print ( '  The parameters are not legal.' )
      return

    mean = gamma_mean ( a, b, c )
    variance = gamma_variance ( a, b, c )

    print ( '' )
    print ( '  TEST NUMBER: %6d' % ( test_i ) )
    print ( '' )
    print ( '  PDF parameter A =             %14g' % ( a ) )
    print ( '  PDF parameter B =             %14g' % ( b ) )
    print ( '  PDF parameter C =             %14g' % ( c ) )
    print ( '  PDF mean =                    %14g' % ( mean ) )
    print ( '  PDF variance =                %14g' % ( variance ) )
  
    x = np.zeros ( nsample )
    for i in range ( 0, nsample ):
      x[i], seed = gamma_sample ( a, b, c, seed )

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
  print ( 'GAMMA_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def gamma_variance ( a, b, c ):

#*****************************************************************************80
#
## GAMMA_VARIANCE returns the variance of the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = b * b * c

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gamma_cdf_test ( )
  gamma_sample_test ( )
  timestamp ( )
 
