#! /usr/bin/env python3
#
def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf_inv ( cdf ):

#*****************************************************************************80
#
## NORMAL_01_CDF evaluates the Normal 01 CDF.
#
#  Discussion:
#
#    The result is accurate to about 1 part in 10^16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Wichura,
#    The Percentage Points of the Normal Distribution,
#    Algorithm AS 241,
#    Applied Statistics,
#    Volume 37, Number 3, pages 477-484, 1988.
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Output, real VALUE, the argument of the CDF.
# 
  import numpy as np

  a = np.array ( [ \
    3.3871328727963666080,      1.3314166789178437745e+2, \
    1.9715909503065514427e+3,   1.3731693765509461125e+4, \
    4.5921953931549871457e+4,   6.7265770927008700853e+4, \
    3.3430575583588128105e+4,   2.5090809287301226727e+3 ] )
  b = np.array ( [ \
    1.0,                        4.2313330701600911252e+1, \
    6.8718700749205790830e+2,   5.3941960214247511077e+3, \
    2.1213794301586595867e+4,   3.9307895800092710610e+4, \
    2.8729085735721942674e+4,   5.2264952788528545610e+3 ] )
  c = np.array ( [ \
    1.42343711074968357734,     4.63033784615654529590, \
    5.76949722146069140550,     3.64784832476320460504, \
    1.27045825245236838258,     2.41780725177450611770e-1, \
    2.27238449892691845833e-2,  7.74545014278341407640e-4 ] )
  const1 = 0.180625
  const2 = 1.6
  d = np.array ( [ \
    1.0,                        2.05319162663775882187,    \
    1.67638483018380384940,     6.89767334985100004550e-1, \
    1.48103976427480074590e-1,  1.51986665636164571966e-2, \
    5.47593808499534494600e-4,  1.05075007164441684324e-9 ] )
  e = np.array ( [ \
    6.65790464350110377720,     5.46378491116411436990,    \
    1.78482653991729133580,     2.96560571828504891230e-1, \
    2.65321895265761230930e-2,  1.24266094738807843860e-3, \
    2.71155556874348757815e-5,  2.01033439929228813265e-7 ] )
  f = np.array ( [ \
    1.0,                        5.99832206555887937690e-1, \
    1.36929880922735805310e-1,  1.48753612908506148525e-2, \
    7.86869131145613259100e-4,  1.84631831751005468180e-5, \
    1.42151175831644588870e-7,  2.04426310338993978564e-15 ] )
  r8_huge = 1.79769313486231571E+308
  split1 = 0.425
  split2 = 5.0

  if ( cdf <= 0.0 ):
    value = - r8_huge
    return value

  if ( 1.0 <= cdf ):
    value = r8_huge
    return value

  q = cdf - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r8poly_value_horner ( 7, a, r ) \
              / r8poly_value_horner ( 7, b, r )

  else:

    if ( q < 0.0 ):
      r = cdf
    else:
      r = 1.0 - cdf

    if ( r <= 0.0 ):

      value = r8_huge

    else:

      r = np.sqrt ( - np.log ( r ) )

      if ( r <= split2 ):

        r = r - const2
        value = r8poly_value_horner ( 7, c, r ) \
              / r8poly_value_horner ( 7, d, r )

      else:

         r = r - split2
         value = r8poly_value_horner ( 7, e, r ) \
               / r8poly_value_horner ( 7, f, r )

    if ( q < 0.0 ):
      value = - value

  return value

def normal_01_cdf_inv_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_INV_TEST tests NORMAL_01_CDF_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_CDF_INV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF_INV inverts the CDF;' )
  print ( '' )
  print ( '      CDF             X                         X' )
  print ( '                     (exact)                   (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x1, cdf = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = normal_01_cdf_inv ( cdf )

    print ( '  %14.6g  %24.16g  %24.16g' % ( cdf, x1, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_INV_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_CDF evaluates the Normal 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    A G Adams,
#    Areas Under the Normal Curve,
#    Algorithm 39,
#    Computer j.,
#    Volume 12, pages 197-198, 1969.
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Output, real VALUE, the value of the CDF.
# 
  import numpy as np

  a1 = 0.398942280444
  a2 = 0.399903438504
  a3 = 5.75885480458
  a4 = 29.8213557808
  a5 = 2.62433121679
  a6 = 48.6959930692
  a7 = 5.92885724438
  b0 = 0.398942280385
  b1 = 3.8052E-08
  b2 = 1.00000615302
  b3 = 3.98064794E-04
  b4 = 1.98615381364
  b5 = 0.151679116635
  b6 = 5.29330324926
  b7 = 4.8385912808
  b8 = 15.1508972451
  b9 = 0.742380924027
  b10 = 30.789933034
  b11 = 3.99019417011
#
#  |X| <= 1.28.
#
  if ( abs ( x ) <= 1.28 ):

    y = 0.5 * x * x

    q = 0.5 - abs ( x ) * ( a1 - a2 * y / ( y + a3 \
      - a4 / ( y + a5 \
      + a6 / ( y + a7 ) ) ) )
#
#  1.28 < |X| <= 12.7
#
  elif ( abs ( x ) <= 12.7 ):

    y = 0.5 * x * x

    q = np.exp ( - y ) \
      * b0  / ( abs ( x ) - b1 \
      + b2  / ( abs ( x ) + b3 \
      + b4  / ( abs ( x ) - b5 \
      + b6  / ( abs ( x ) + b7 \
      - b8  / ( abs ( x ) + b9 \
      + b10 / ( abs ( x ) + b11 ) ) ) ) ) )
#
#  12.7 < |X|
#
  else:

    q = 0.0
#
#  Take account of negative X.
#
  if ( x < 0.0 ):
    value = q
  else:
    value = 1.0 - q

  return value

def normal_01_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_TEST tests NORMAL_01_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF evaluates the CDF;' )
  print ( '' )
  print ( '       X              CDF                       CDF' )
  print ( '                     (exact)                   (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, cdf1 = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = normal_01_cdf ( x )

    print ( '  %14.6g  %24.16g  %24.16g' % ( x, cdf1, cdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## NORMAL_01_CDF_VALUES returns some values of the Normal 01 CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0, 1 ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( (\
     0.5000000000000000E+00, \
     0.5398278372770290E+00, \
     0.5792597094391030E+00, \
     0.6179114221889526E+00, \
     0.6554217416103242E+00, \
     0.6914624612740131E+00, \
     0.7257468822499270E+00, \
     0.7580363477769270E+00, \
     0.7881446014166033E+00, \
     0.8159398746532405E+00, \
     0.8413447460685429E+00, \
     0.9331927987311419E+00, \
     0.9772498680518208E+00, \
     0.9937903346742239E+00, \
     0.9986501019683699E+00, \
     0.9997673709209645E+00, \
     0.9999683287581669E+00 ))

  x_vec = np.array ((\
     0.0000000000000000E+00, \
     0.1000000000000000E+00, \
     0.2000000000000000E+00, \
     0.3000000000000000E+00, \
     0.4000000000000000E+00, \
     0.5000000000000000E+00, \
     0.6000000000000000E+00, \
     0.7000000000000000E+00, \
     0.8000000000000000E+00, \
     0.9000000000000000E+00, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.2000000000000000E+01, \
     0.2500000000000000E+01, \
     0.3000000000000000E+01, \
     0.3500000000000000E+01, \
     0.4000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def normal_01_cdf_values_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_VALUES_TEST demonstrates the use of NORMAL_01_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF_VALUES stores values of the unit normal CDF.' )
  print ( '' )
  print ( '      X         NORMAL_01_CDF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_mean ( ):

#*****************************************************************************80
#
## NORMAL_01_MEAN returns the mean of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the mean of the PDF.
# 
  value = 0.0

  return value

def normal_01_mean_test ( ):

#*****************************************************************************80
#
## NORMAL_01_MEAN_TEST tests NORMAL_01_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'NORMAL_01_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_MEAN computes the Normal 01 mean;' )

  m = normal_01_mean ( )

  print ( '' )
  print ( '  PDF mean =      %14g' % ( m ) )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_01_sample ( seed )

  ms = r8vec_mean ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( ms ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_moment ( order ):

#*****************************************************************************80
#
## NORMAL_01_MOMENT evaluates the moments of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#
#    Output, real VALUE, the value of the moment.
# 
  if ( ( order % 2 ) == 0 ):
    value = r8_factorial2 ( order - 1 )
  else:
    value = 0.0

  return value

def normal_01_moment_test ( ):

#*****************************************************************************80
#
## NORMAL_01_MOMENT_TEST tests NORMAL_01_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_MOMENT evaluates moments of the Normal 01 PDF;' )
  print ( '' )
  print ( '   Order     Moment' )
  print ( '' )

  for order in range ( 0, +11 ):

    moment = normal_01_moment ( order )
    print ( '  %6d  %14.6g' % ( order, moment ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_pdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_PDF evaluates the Normal 01 PDF.
#
#  Discussion:
#
#    The Normal 01 PDF is also called the "Standard Normal" PDF, or
#    the Normal PDF with 0 mean and standard deviation 1.
#
#  Formula:
#
#    PDF(x) = exp ( - 0.5 * x^2 ) / sqrt ( 2 * pi )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Output, real VALUE, the value of the PDF.
# 
  import numpy as np

  value = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return value

def normal_01_pdf_test ( ):

#*****************************************************************************80
#
## NORMAL_01_PDF_TEST tests NORMAL_01_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_PDF evaluates the PDF;' )
  print ( '' )
  print ( '       X              PDF' )
  print ( '' )

  for i in range ( -20, +21 ):

    x = float ( i ) / 10.0
    pdf = normal_01_pdf ( x )
    print ( '  %14.6g  %24.16g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_sample ( seed ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLE samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#  Method:
#
#    The Box-Muller method is used, which is efficient, but
#    generates two values at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )

  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return value, seed

def normal_01_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLE_TEST tests NORMAL_01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_SAMPLE returns samples from the normal' )
  print ( '  distribution with mean 0 and standard deviation 1.' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    x, seed = normal_01_sample ( seed )
    print ( '  %4d  %14.6g' % ( i, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_01_variance ( ):

#*****************************************************************************80
#
## NORMAL_01_VARIANCE returns the variance of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the variance of the PDF.
# 
  value = 1.0

  return value

def normal_01_variance_test ( ):

#*****************************************************************************80
#
## NORMAL_01_VARIANCE_TEST tests NORMAL_01_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'NORMAL_01_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_VARIANCE computes the Normal 01 variance;' )

  value = normal_01_variance ( )

  print ( '' )
  print ( '  PDF variance =      %14g' % ( value ) )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_01_sample ( seed )

  value = r8vec_variance ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample variance = %14g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_cdf_inv ( cdf, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_CDF_INV inverts the CDF of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'NORMAL_MS_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    error ( 'NORMAL_MS_CDF_INV - Fatal error!' )

  y = normal_01_cdf_inv ( cdf )

  value = mu + sigma * y

  return value

def normal_ms_cdf_inv_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_CDF_INV_TEST tests NORMAL_MS_CDF_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_MS_CDF_INV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_CDF_INV inverts the CDF' )
  print ( '  of the Normal MS distribution.' )

  mu = 100.0
  sigma = 15.0

  print ( '' )
  print ( '  PDF parameter MU = %g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %g' % ( sigma ) )

  print ( '' )
  print ( '       X              CDF            CDF_INV' )
  print ( '' )

  for i in range ( -20, +21 ):

    x = mu + sigma * float ( i ) / 10.0
    cdf = normal_ms_cdf ( x, mu, sigma )
    x2 = normal_ms_cdf_inv ( cdf, mu, sigma )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_CDF_INV_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_cdf ( x, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_CDF evaluates the CDF of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the value of the CDF.
#
  y = ( x - mu ) / sigma

  value = normal_01_cdf ( y )

  return value

def normal_ms_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_CDF_TEST tests NORMAL_MS_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_MS_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_CDF evaluates the CDF;' )

  mu = 100.0
  sigma = 15.0

  print ( '' )
  print ( '  PDF parameter MU = %g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %g' % ( sigma ) )

  print ( '' )
  print ( '       X              CDF' )
  print ( '' )

  for i in range ( -20, +21 ):

    x = mu + sigma * float ( i ) / 10.0
    cdf = normal_ms_cdf ( x, mu, sigma )
    print ( '  %14.6g  %24.16g' % ( x, cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_mean ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MEAN returns the mean of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the mean of the PDF.
# 
  value = mu

  return value

def normal_ms_mean_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MEAN_TEST tests NORMAL_MS_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'NORMAL_MS_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_MEAN computes the mean' )
  print ( '  of the Normal MS distribution.' )

  mu = 100.0
  sigma = 15.0

  m = normal_ms_mean ( mu, sigma )

  print ( '' )
  print ( '  PDF parameter MU = %g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %g' % ( sigma ) )
  print ( '  PDF mean = %g' % ( m ) )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_ms_sample ( mu, sigma, seed )

  ms = r8vec_mean ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( ms ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_moment_central ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_CENTRAL evaluates central moments of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the central moment.
#
  if ( ( order % 2 ) == 0 ):
    value = r8_factorial2 ( order - 1 ) * sigma ** order
  else:
    value = 0.0

  return value

def normal_ms_moment_central_values ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_CENTRAL_VALUES evaluates central moments 0 through 8 of the Normal PDF.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    0
#      2    sigma^2
#      3    0
#      4    3 sigma^4
#      5    0
#      6    15 sigma^6
#      7    0
#      8    105 sigma^8
#      9    0
#     10    945 sigma^10
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER <= 8.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the central moment.
#
  from sys import exit

  if ( order == 0 ):
    value = 1.0
  elif ( order == 1 ):
    value = 0.0
  elif ( order == 2 ):
    value = sigma ** 2
  elif ( order == 3 ):
    value = 0.0
  elif ( order == 4 ):
    value = 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = 0.0
  elif ( order == 6 ):
    value = 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = 0.0
  elif ( order == 8 ):
    value = 105.0 * sigma ** 8
  elif ( order == 9 ):
    value = 0.0
  elif ( order == 10 ):
    value = 945.0 * sigma ** 10
  else:
    print ( '' )
    print ( 'NORMAL_MS_MOMENT_CENTRAL_VALUES - Fatal error!' )
    print ( '  Only ORDERS 0 through 8 are available.' )
    exit ( 'NORMAL_MS_MOMENT_CENTRAL_VALUES - Fatal error!' )

  return value

def normal_ms_moment_central_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_CENTRAL_TEST tests NORMAL_MS_MOMENT_CENTRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4
  mu_test = np.array ( [ 0.0, 2.0, 10.0, 0.0 ] )
  sigma_test = np.array ( [ 1.0, 1.0, 2.0, 2.0 ] )

  print ( '' )
  print ( 'NORMAL_MS_MOMENT_CENTRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_MOMENT_CENTRAL evaluates central moments' )
  print ( '  of the Normal MS distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    print ( '' )
    print ( '  Mu = %g, Sigma = %g' % ( mu, sigma ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      moment1 = normal_ms_moment_central ( order, mu, sigma )
      moment2 = normal_ms_moment_central_values ( order, mu, sigma )
      print ( '  %2d  %12g  %12g' % ( order, moment1, moment2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_MOMENT_CENTRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_moment ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT evaluates the moments of the Normal MS distribution.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    mu
#      2    mu ** 2 +         sigma ** 2
#      3    mu ** 3 +  3 mu   sigma ** 2
#      4    mu ** 4 +  6 mu ** 2 sigma ** 2 +   3      sigma ** 4
#      5    mu ** 5 + 10 mu ** 3 sigma ** 2 +  15 mu   sigma ** 4
#      6    mu ** 6 + 15 mu ** 4 sigma ** 2 +  45 mu ** 2 sigma ** 4 +  15      sigma ** 6
#      7    mu ** 7 + 21 mu ** 5 sigma ** 2 + 105 mu ** 3 sigma ** 4 + 105 mu   sigma ** 6
#      8    mu ** 8 + 28 mu ** 6 sigma ** 2 + 210 mu ** 4 sigma ** 4 + 420 mu ** 2 sigma ** 6 + 105 sigma ** 8
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the moment.
#
  j_hi = ( order // 2 )

  value = 0.0
  for j in range ( 0, j_hi + 1 ):
    value = value \
      + r8_choose ( order, 2 * j ) \
      * r8_factorial2 ( 2 * j - 1 ) \
      * mu ** ( order - 2 * j ) * sigma ** ( 2 * j )

  return value

def normal_ms_moment_values ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_VALUES evaluates moments 0 through 8 of the Normal PDF.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    mu
#      2    mu ** 2 +         sigma ** 2
#      3    mu ** 3 +  3 mu   sigma ** 2
#      4    mu ** 4 +  6 mu ** 2 sigma ** 2 +   3      sigma ** 4
#      5    mu ** 5 + 10 mu ** 3 sigma ** 2 +  15 mu   sigma ** 4
#      6    mu ** 6 + 15 mu ** 4 sigma ** 2 +  45 mu ** 2 sigma ** 4 +  15      sigma ** 6
#      7    mu ** 7 + 21 mu ** 5 sigma ** 2 + 105 mu ** 3 sigma ** 4 + 105 mu   sigma ** 6
#      8    mu ** 8 + 28 mu ** 6 sigma ** 2 + 210 mu ** 4 sigma ** 4 + 420 mu ** 2 sigma ** 6 + 105 sigma ** 8
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER <= 8.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the central moment.
#
  from sys import exit

  if ( order == 0 ):
    value = 1.0
  elif ( order == 1 ):
    value = mu
  elif ( order == 2 ):
    value = mu ** 2 + sigma ** 2
  elif ( order == 3 ):
    value = mu ** 3 + 3.0 * mu * sigma ** 2
  elif ( order == 4 ):
    value = mu ** 4 + 6.0 * mu ** 2 * sigma ** 2 + 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = mu ** 5 + 10.0 * mu ** 3 * sigma ** 2 + 15.0 * mu * sigma ** 4
  elif ( order == 6 ):
    value = mu ** 6 + 15.0 * mu ** 4 * sigma ** 2 + 45.0 * mu ** 2 * sigma ** 4 \
      + 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = mu ** 7 + 21.0 * mu ** 5 * sigma ** 2 + 105.0 * mu ** 3 * sigma ** 4 \
      + 105.0 * mu * sigma ** 6
  elif ( order == 8 ):
    value = mu ** 8 + 28.0 * mu ** 6 * sigma ** 2 + 210.0 * mu ** 4 * sigma ** 4 \
      + 420.0 * mu ** 2 * sigma ** 6 + 105.0 * sigma ** 8
  else:
    print ( '' )
    print ( 'NORMAL_MS_MOMENT_VALUES - Fatal error!' )
    print ( '  Only ORDERS 0 through 8 are available.' )
    exit ( 'NORMAL_MS_MOMENT_VALUES - Fatal error!' )

  return value

def normal_ms_moment_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_TEST tests NORMAL_MS_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4
  mu_test = np.array ( [ 0.0, 2.0, 10.0, 0.0 ] )
  sigma_test = np.array ( [ 1.0, 1.0, 2.0, 2.0 ] )

  print ( '' )
  print ( 'NORMAL_MS_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_MOMENT evaluates moments of the Normal MS distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    print ( '' )
    print ( '  Mu = %g, Sigma = %g' % ( mu, sigma ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      moment1 = normal_ms_moment ( order, mu, sigma )
      moment2 = normal_ms_moment_values ( order, mu, sigma )
      print ( '  %2d  %12g  %12g' % ( order, moment1, moment2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_pdf ( x, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_PDF evaluates the Normal MS PDF.
#
#  Discussion:
#
#    The Normal MS PDF is also called the Gaussian PDF.
#
#  Formula:
#
#    PDF(X)(MU,SIGMA) = EXP ( - 0.5 * ( ( X - MU ) / SIGMA )^2 ) 
#      / SQRT ( 2 * PI * SIGMA^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the value of the PDF.
# 
  import numpy as np

  value = np.exp ( - 0.5 * ( ( x - mu ) / sigma ) ** 2 ) \
    / np.sqrt ( 2.0 * np.pi * sigma ** 2 )

  return value

def normal_ms_pdf_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_PDF_TEST tests NORMAL_MS_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_MS_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_PDF evaluates the PDF' )
  print ( '  for the Normal MS distribution.' )

  mu = 100.0
  sigma = 15.0
  seed = 123456789

  print ( '' )
  print ( '  PDF parameter MU = %g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %g' % ( sigma ) )

  print ( '' )
  print ( '       X              PDF' )
  print ( '' )

  for i in range ( -20, +21 ):

    x = mu + sigma * float ( i ) / 10.0
    pdf = normal_ms_pdf ( x, mu, sigma )
    print ( '  %14.6g  %24.16g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_sample ( mu, sigma, seed ):

#*****************************************************************************80
#
## NORMAL_MS_SAMPLE samples the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  y, seed = normal_01_sample ( seed )
 
  value = mu + sigma * y

  return value, seed

def normal_ms_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_SAMPLE_TEST tests NORMAL_MS_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_MS_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_SAMPLE samples' )
  print ( '  the Normal MS distribution.' )

  mu = 100.0
  sigma = 15.0
  seed = 123456789

  print ( '' )
  print ( '  PDF parameter MU = %g\n' % ( mu ) )
  print ( '  PDF parameter SIGMA = %g' % ( sigma ) )

  print ( '' )
  for i in range ( 0, 10 ):
    x, seed = normal_ms_sample ( mu, sigma, seed )
    print ( '  %4d  %14.6g' % ( i, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_variance ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_VARIANCE returns the variance of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the variance of the PDF.
# 
  value = sigma * sigma

  return value

def normal_ms_variance_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_VARIANCE_TEST tests NORMAL_MS_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'NORMAL_MS_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_VARIANCE computes the variance' )
  print ( '  of the Normal MS distribution.' )

  mu = 100.0
  sigma = 15.0

  value = normal_ms_variance ( mu, sigma )

  print ( '' )
  print ( '  PDF parameter MU = %g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %g' % ( sigma ) )
  print ( '  PDF variance = %g' % ( value ) )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_ms_sample ( mu, sigma, seed )

  value = r8vec_variance ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample variance = %14g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_choose ( n, k ):

#*****************************************************************************80
#
## R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, K, are the values of N and K.
#
#    Output, real VALUE, the number of combinations of N
#    things taken K at a time.
#
  import numpy as np

  if ( n < 0 ):

    value = 0.0

  elif ( k == 0 ):

    value = 1.0

  elif ( k == 1 ):

    value = float ( n )

  elif ( 1 < k and k < n - 1 ):

    facn = r8_gamma_log ( float ( n + 1 ) )
    fack = r8_gamma_log ( float ( k + 1 ) )
    facnmk = r8_gamma_log ( float ( n - k + 1 ) )

    value = round ( np.exp ( facn - fack - facnmk ) )

  elif ( k == n - 1 ):

    value = float ( n )

  elif ( k == n ):

    value = 1.0

  else:

    value = 0.0

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## R8_CHOOSE_TEST tests R8_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHOOSE evaluates C(N,K).' )
  print ( '' )
  print ( '         N         K       CNK' )
 
  for n in range ( 0, 6 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print ( '  %8d  %8d  %14.6g' % ( n, k, cnk ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_factorial2 ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL2 computes the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the double factorial function.
#    If N is less than 1, VALUE is returned as 1.
#
#    Output, real VALUE, the value of N!!.
#
  value = 1;

  if ( n < 1 ):
    return value

  while ( 1 < n ):
    value = value * n
    n = n - 2

  return value

def r8_factorial2_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL2_TEST tests R8_FACTORIAL2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL2 evaluates the double factorial function.' )
  print ( '' )
  print ( '      N                     Exact' ),
  print ( '                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial2 ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL2_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_factorial2_values ( n_data ):

#*****************************************************************************80
#
## R8_FACTORIAL2_VALUES returns values of the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#    In Mathematica, the function can be evaluated by:
#
#      n!!
#
#  Example:
#
#     N    N!!
#
#     0     1
#     1     1
#     2     2
#     3     3
#     4     8
#     5    15
#     6    48
#     7   105
#     8   384
#     9   945
#    10  3840
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, page 16.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the argument of the function.
#
#    Output, real F, the value of the function.
# 
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( 
          1.0, \
          1.0, \
          2.0, \
          3.0, \
          8.0, \
         15.0, \
         48.0, \
        105.0, \
        384.0, \
        945.0, \
       3840.0, \
      10395.0, \
      46080.0, \
     135135.0, \
     645120.0, \
    2027025.0 ) )

  n_vec = np.array ( ( 
    0, \
     1,  2,  3,  4,  5, \
     6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    f = 0.0
  else:
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, f

def r8_factorial2_values_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL2_VALUES_TEST demonstrates the use of R8_FACTORIAL2_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL2_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL2_VALUES returns values of the double factorial function.' )
  print ( '' )
  print ( '     N        N!!' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %14.6g' % ( n, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL2_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_gamma_log ( x ):

#*****************************************************************************80
#
## R8_GAMMA_LOG evaluates the logarithm of the gamma function.
#
#  Discussion:
#
#    This routine calculates the LOG(GAMMA) function for a positive real
#    argument X.  Computation is based on an algorithm outlined in
#    references 1 and 2.  The program uses rational functions that
#    theoretically approximate LOG(GAMMA) to at least 18 significant
#    decimal digits.  The approximation for X > 12 is from reference
#    3, while approximations for X < 12.0 are similar to those in
#    reference 1, but are unpublished.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz.
#    PYTHON version by John Burkardt.
#
#  Reference:
#
#    William Cody, Kenneth Hillstrom,
#    Chebyshev Approximations for the Natural Logarithm of the
#    Gamma Function,
#    Mathematics of Computation,
#    Volume 21, Number 98, April 1967, pages 198-203.
#
#    Kenneth Hillstrom,
#    ANL/AMD Program ANLC366S, DGAMMA/DLGAMA,
#    May 1969.
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
#    Charles Mesztenyi, John Rice, Henry Thatcher,
#    Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968,
#    LC: QA297.C64.
#
#  Parameters:
#
#    Input, real X, the argument of the function.
#
#    Output, real R8_GAMMA_LOG, the value of the function.
#
  import numpy as np

  c = np.array ( [ \
    -1.910444077728E-03, \
     8.4171387781295E-04, \
    -5.952379913043012E-04, \
     7.93650793500350248E-04, \
    -2.777777777777681622553E-03, \
     8.333333333333333331554247E-02, \
     5.7083835261E-03 ] )
  d1 = -5.772156649015328605195174E-01
  d2 = 4.227843350984671393993777E-01
  d4 = 1.791759469228055000094023E+00
  frtbig = 2.25E+76
  p1 = np.array ( [ \
    4.945235359296727046734888E+00, \
    2.018112620856775083915565E+02, \
    2.290838373831346393026739E+03, \
    1.131967205903380828685045E+04, \
    2.855724635671635335736389E+04, \
    3.848496228443793359990269E+04, \
    2.637748787624195437963534E+04, \
    7.225813979700288197698961E+03 ] )
  p2 = np.array ( [ \
    4.974607845568932035012064E+00, \
    5.424138599891070494101986E+02, \
    1.550693864978364947665077E+04, \
    1.847932904445632425417223E+05, \
    1.088204769468828767498470E+06, \
    3.338152967987029735917223E+06, \
    5.106661678927352456275255E+06, \
    3.074109054850539556250927E+06 ] )
  p4 = np.array ( [ \
    1.474502166059939948905062E+04, \
    2.426813369486704502836312E+06, \
    1.214755574045093227939592E+08, \
    2.663432449630976949898078E+09, \
    2.940378956634553899906876E+10, \
    1.702665737765398868392998E+11, \
    4.926125793377430887588120E+11, \
    5.606251856223951465078242E+11 ] )
  q1 = np.array ( [ \
    6.748212550303777196073036E+01, \
    1.113332393857199323513008E+03, \
    7.738757056935398733233834E+03, \
    2.763987074403340708898585E+04, \
    5.499310206226157329794414E+04, \
    6.161122180066002127833352E+04, \
    3.635127591501940507276287E+04, \
    8.785536302431013170870835E+03 ] )
  q2 = np.array ( [ \
    1.830328399370592604055942E+02, \
    7.765049321445005871323047E+03, \
    1.331903827966074194402448E+05, \
    1.136705821321969608938755E+06, \
    5.267964117437946917577538E+06, \
    1.346701454311101692290052E+07, \
    1.782736530353274213975932E+07, \
    9.533095591844353613395747E+06 ] )
  q4 = np.array ( [ \
    2.690530175870899333379843E+03, \
    6.393885654300092398984238E+05, \
    4.135599930241388052042842E+07, \
    1.120872109616147941376570E+09, \
    1.488613728678813811542398E+10, \
    1.016803586272438228077304E+11, \
    3.417476345507377132798597E+11, \
    4.463158187419713286462081E+11 ] )
  r8_epsilon = 2.220446049250313E-016
  sqrtpi = 0.9189385332046727417803297
  xbig = 2.55E+305
  xinf = 1.79E+308

  y = x

  if ( 0.0 < y and y <= xbig ):

    if ( y <= r8_epsilon ):

      res = - np.log ( y )
#
#  EPS < X <= 1.5.
#
    elif ( y <= 1.5 ):

      if ( y < 0.6796875 ):
        corr = - np.log ( y );
        xm1 = y;
      else:
        corr = 0.0;
        xm1 = ( y - 0.5 ) - 0.5;

      if ( y <= 0.5 or 0.6796875 <= y ):

        xden = 1.0;
        xnum = 0.0;
        for i in range ( 0, 8 ):
          xnum = xnum * xm1 + p1[i]
          xden = xden * xm1 + q1[i]

        res = corr + ( xm1 * ( d1 + xm1 * ( xnum / xden ) ) )

      else:

        xm2 = ( y - 0.5 ) - 0.5
        xden = 1.0
        xnum = 0.0
        for i in range ( 0, 8 ):
          xnum = xnum * xm2 + p2[i]
          xden = xden * xm2 + q2[i]

        res = corr + xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  1.5 < X <= 4.0.
#
    elif ( y <= 4.0 ):

      xm2 = y - 2.0
      xden = 1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm2 + p2[i]
        xden = xden * xm2 + q2[i]

      res = xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  4.0 < X <= 12.0.
#
    elif ( y <= 12.0 ):

      xm4 = y - 4.0
      xden = -1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm4 + p4[i]
        xden = xden * xm4 + q4[i]

      res = d4 + xm4 * ( xnum / xden )
#
#  Evaluate for 12 <= argument.
#
    else:

      res = 0.0

      if ( y <= frtbig ):

        res = c[6]
        ysq = y * y

        for i in range ( 0, 6 ):
          res = res / ysq + c[i]

      res = res / y
      corr = np.log ( y )
      res = res + sqrtpi - 0.5 * corr
      res = res + y * ( corr - 1.0 )
#
#  Return for bad arguments.
#
  else:

    res = xinf

  return res

def r8_gamma_log_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_LOG_TEST tests R8_GAMMA_LOG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_GAMMA_LOG_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_LOG evaluates the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA_LOG(X)    R8_GAMMA_LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma_log ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_LOG_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_mop ( i ):

#*****************************************************************************80
#
## R8_MOP returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the power of -1.
#
#    Output, real R8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## R8_MOP_TEST tests R8_MOP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_MOP evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  R8_MOP(I4)' )
  print ( '' )

  i4_min = -100;
  i4_max = +100;
  seed = 123456789;

  for test in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( i4_min, i4_max, seed )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## R8POLY_PRINT prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the nominal degree of the polynomial.
#
#    Input, real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## R8POLY_PRINT_TEST tests R8POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8POLY_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_PRINT prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_PRINT_TEST:' )
  print ( '  Normal end of execution.' )

  return
 
def r8poly_value_horner ( m, c, x ):

#*****************************************************************************80
#
## R8POLY_VALUE_HORNER evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the degree.
#
#    Input, real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the polynomial value.
#
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8poly_value_horner_test ( ):

#*****************************************************************************80
#
## R8POLY_VALUE_HORNER_TEST tests R8POLY_VALUE_HORNER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'R8POLY_VALUE_HORNER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_VALUE_HORNER evaluates a polynomial at a point' )
  print ( '  using Horners method.' )

  r8poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value_horner ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_VALUE_HORNER_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_linspace ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_LINSPACE creates a column vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    While MATLAB has the built in command 
#
#      x = linspace ( a, b, n )
#
#    that command has the distinct disadvantage of returning a ROW vector.
#
#    4 points evenly spaced between 0 and 12 will yield 0, 4, 8, 12.
#
#    In other words, the interval is divided into N-1 even subintervals,
#    and the endpoints of intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the first and last entries.
#
#    Output, real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):
     x[i] = ( ( n - 1 - i ) * a \
            + (         i ) * b ) \
            / ( n - 1     )
 
  return x

def r8vec_linspace_test ( ):

#*****************************************************************************80
#
## R8VEC_LINSPACE_TEST tests R8VEC_LINSPACE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_LINSPACE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_LINSPACE returns evenly spaced values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_LINSPACE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_max ( n, a ):

#*****************************************************************************80
#
## R8VEC_MAX returns the maximum value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the maximum value in the vector.
#
  r8_huge = 1.79769313486231571E+308

  value = - r8_huge
  for i in range ( 0, n ):
    if ( value < a[i] ):
      value = a[i]

  return value

def r8vec_max_test ( ):

#*****************************************************************************80
#
## R8VEC_MAX_TEST tests R8VEC_MAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_MAX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MAX computes the maximum entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_max ( n, a )
  print ( '' )
  print ( '  Max = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MAX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_mean ( n, a ):

#*****************************************************************************80
#
## R8VEC_MEAN returns the mean of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the mean of the vector.
#
  import numpy as np

  value = np.sum ( a ) / float ( n )

  return value

def r8vec_mean_test ( ):

#*****************************************************************************80
#
## R8VEC_MEAN_TEST tests R8VEC_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MEAN computes the mean of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_mean ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_min ( n, a ):

#*****************************************************************************80
#
## R8VEC_MIN returns the minimum value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the minimum value in the vector.
#
  r8_huge = 1.79769313486231571E+308

  value = r8_huge
  for i in range ( 0, n ):
    if ( a[i] < value ):
      value = a[i]

  return value

def r8vec_min_test ( ):

#*****************************************************************************80
#
## R8VEC_MIN_TEST tests R8VEC_MIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_MIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MIN computes the minimum entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_min ( n, a )
  print ( '' )
  print ( '  Min = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_AB - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_AB computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_variance ( n, a ):

#*****************************************************************************80
#
## R8VEC_VARIANCE returns the variance of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the variance of the vector.
#
  import numpy as np
#
#  DDOF = 1 requests normalization by N-1 rather than N.
#
  value = np.var ( a, ddof = 1 )

  return value

def r8vec_variance_test ( ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_TEST tests R8VEC_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_VARIANCE computes the variance of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_variance ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_cdf_inv ( cdf, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_INV inverts the truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'TRUNCATED_NORMAL_AB_CDF_INV - Fatal error!' )

  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_ab_cdf_inv_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_INV_TEST tests TRUNCATED_NORMAL_AB_CDF_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  sample_num = 10
  seed = 123456789
  a = 50.0
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_INV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_CDF_INV inverts the CDF of' )
  print ( '  the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  print ( '' )
  print ( '             X            CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_ab_sample ( mu, sigma, a, b, seed )
    cdf = truncated_normal_ab_cdf ( x, mu, sigma, a, b )
    x2 = truncated_normal_ab_cdf_inv ( cdf, mu, sigma, a, b )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_INV_TEST' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_cdf ( x, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF evaluates the Truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VALUE, the value of the CDF.
# 
  if ( x < a ):
  
    value = 0.0
    
  elif ( x <= b ):
  
    alpha = ( a - mu ) / sigma
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = normal_01_cdf ( beta )
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )
    
  else:
  
    value = 1.0

  return value

def truncated_normal_ab_cdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_TEST tests TRUNCATED_NORMAL_AB_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_CDF evaluates the CDF' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [a,b]' )

  print ( '' )
  print ( '                                                           Stored         Computed' )
  print ( '       X        Mu         S         A         B             CDF             CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, b, x, cdf1 = truncated_normal_ab_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = truncated_normal_ab_cdf ( x, mu, sigma, a, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, a, b, cdf1, cdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_cdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_VALUES: values of the Truncated Normal AB CDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval [A,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real A, B, the lower and upper truncation limits.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.3371694242213513, \
    0.3685009225506048, \
    0.4006444233448185, \
    0.4334107066903040, \
    0.4665988676496338, \
    0.5000000000000000, \
    0.5334011323503662, \
    0.5665892933096960, \
    0.5993555766551815, \
    0.6314990774493952, \
    0.6628305757786487 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, b, x, f

def truncated_normal_ab_cdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_AB_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_CDF_VALUES stores values of the TRUNCATED_NORMAL_AB_CDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             A             B             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, b, x, f = truncated_normal_ab_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, a, b, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_mean ( mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MEAN returns the mean of the Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the parent Normal Distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VALUE, the mean of the PDF.
#
  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_ab_mean_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MEAN_TEST tests TRUNCATED_NORMAL_AB_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sample_num = 1000
  seed = 123456789
  a = 50.0
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_MEAN computes the mean' )
  print ( '  of the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  m = truncated_normal_ab_mean ( mu, sigma, a, b )

  print ( '' )
  print ( '  PDF mean = %g' % ( m ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_ab_sample ( mu, sigma, a, b, seed )

  ms = r8vec_mean ( sample_num, x )
  xmax = r8vec_max ( sample_num, x )
  xmin = r8vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( ms ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_moment ( order, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENT: moments of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, B, the lower and upper truncation limits.
#    A < B.
#
#    Output, real VALUE, the moment of the PDF.
#
  from sys import exit

  if ( order < 0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  ORDER < 0.' )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  if ( b <= a ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  B <= A.' )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  a_h = ( a - mu ) / sigma
  a_pdf = normal_01_pdf ( a_h )
  a_cdf = normal_01_cdf ( a_h )

  if ( a_cdf == 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because A_CDF is too small.' )
    print ( '  A_PDF = %g' % ( a_pdf ) )
    print ( '  A_CDF = %g' % ( a_cdf ) )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_CDF too small.' )
    print ( '  B_PDF = %g' % ( b_pdf ) )
    print ( '  B_CDF = %g' % ( b_cdf ) )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - ( b_pdf - a_pdf ) / ( b_cdf - a_cdf )
    else:
      ir = ( r - 1 ) * irm2 \
        - ( b_h ** ( r - 1 ) * b_pdf - a_h ** ( r - 1 ) * a_pdf ) \
        / ( b_cdf - a_cdf )

    value = value + r8_choose ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_ab_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENT_TEST tests TRUNCATED_NORMAL_AB_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 9
  mu_test =    np.array ( [  0.0, 0.0,  0.0,  0.0,  1.0, 0.0,  0.0,  0.0, 5.0 ] )
  sigma_test = np.array ( [  1.0, 1.0,  1.0,  2.0,  1.0, 1.0,  1.0,  1.0, 0.5 ] )
  a_test =     np.array ( [ -1.0, 0.0, -1.0, -1.0,  0.0, 0.5, -2.0, -4.0, 4.0 ] )
  b_test =     np.array ( [  1.0, 1.0,  0.0,  1.0,  2.0, 2.0,  2.0,  4.0, 7.0 ] )

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_MOMENT evaluates moments' )
  print ( '  of the Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    a = a_test[test]
    b = b_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, A = %g, B = %g' \
      % ( test, mu, sigma, a, b ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_ab_moment ( order, mu, sigma, a, b )
      print ( '  %2d  %12g' % ( order, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_pdf ( x, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_PDF evaluates the Truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VALUE, the value of the PDF.
# 
  if ( x < a ):
  
    value = 0.0
    
  elif ( x <= b ):
  
    alpha = ( a - mu ) / sigma
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = normal_01_cdf ( beta )
    xi_pdf = normal_01_pdf ( xi )

    value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  else:
  
    value = 0.0
    
  return value

def truncated_normal_ab_pdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_PDF_TEST tests TRUNCATED_NORMAL_AB_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_PDF evaluates the PDF' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [a,b]' )

  print ( '' )
  print ( '                                                           Stored         Computed' )
  print ( '       X        Mu         S         A         B             PDF             PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, b, x, pdf1 = truncated_normal_ab_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = truncated_normal_ab_pdf ( x, mu, sigma, a, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, a, b, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_pdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_PDF_VALUES: values of the Truncated Normal AB PDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval [A,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real A, B, the lower and upper truncation limits.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.01543301171801836, \
    0.01588394472270638, \
    0.01624375997031919, \
    0.01650575046469259, \
    0.01666496869385951, \
    0.01671838200940538, \
    0.01666496869385951, \
    0.01650575046469259, \
    0.01624375997031919, \
    0.01588394472270638, \
    0.01543301171801836 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, b, x, f

def truncated_normal_ab_pdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_PDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_AB_PDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_PDF_VALUES stores values of the TRUNCATED_NORMAL_AB_PDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             A             B             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, b, x, f = truncated_normal_ab_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, a, b, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_sample ( mu, sigma, a, b, seed ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_SAMPLE samples the Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random number generator.
#
  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  u, seed = r8_uniform_01 ( seed )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x, seed

def truncated_normal_ab_sample_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_SAMPLE_TEST tests TRUNCATED_NORMAL_AB_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  sample_num = 10
  seed = 123456789
  a = 50.0
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_SAMPLE samples' )
  print ( '  the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )
  print ( '' )

  print ( '' )
  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_ab_sample ( mu, sigma, a, b, seed )
    print ( '  %4d  %14.6g' % ( i, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_ab_variance ( mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_VARIANCE: variance of the Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VALUE, the variance of the PDF.
#
  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  value = sigma * sigma * ( 1.0 \
    + ( alpha * alpha_pdf - beta * beta_pdf ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value

def truncated_normal_ab_variance_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_VARIANCE_TEST tests TRUNCATED_NORMAL_AB_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sample_num = 1000
  seed = 123456789
  a = 50.0
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_VARIANCE computes the variance' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  value = truncated_normal_ab_variance ( mu, sigma, a, b )

  print ( '' )
  print ( '  PDF variance = %g' % ( value ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_ab_sample ( mu, sigma, a, b, seed )

  value = r8vec_variance ( sample_num, x )

  print ( '' )
  print ( '  Sample size = %d' % ( sample_num ) )
  print ( '  Sample variance = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_cdf_inv ( cdf, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_CDF_INV inverts the lower truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_A_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'TRUNCATED_NORMAL_A_CDF_INV - Fatal error!' )

  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_a_cdf_inv_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_CDF_INV_TEST tests TRUNCATED_NORMAL_A_CDF_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  sample_num = 10
  seed = 123456789
  a = 50.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_CDF_INV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_CDF_INV inverts the CDF of' )
  print ( '  the lower Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,+oo)' % ( a ) )

  print ( '' )
  print ( '             X            CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_a_sample ( mu, sigma, a, seed )
    cdf = truncated_normal_a_cdf ( x, mu, sigma, a )
    x2 = truncated_normal_a_cdf_inv ( cdf, mu, sigma, a )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_CDF_INV_TEST' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_cdf ( x, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_CDF evaluates the lower Truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the value of the CDF.
# 
  if ( x < a ):
  
    value = 0.0
    
  else:
  
    alpha = ( a - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = 1.0
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_a_cdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_CDF_TEST tests TRUNCATED_NORMAL_A_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_CDF evaluates the CDF' )
  print ( '  of the lower Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [a,+oo)' )

  print ( '' )
  print ( '                                                 Stored         Computed' )
  print ( '       X        Mu         S         A             CDF             CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, x, cdf1 = truncated_normal_a_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = truncated_normal_a_cdf ( x, mu, sigma, a )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, a, cdf1, cdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_cdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_CDF_VALUES: values of the Truncated Normal A CDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval [A,+oo).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real A, the lower truncation limit.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  f_vec = np.array ( ( \
    0.3293202045481688, \
    0.3599223134505957, \
    0.3913175216041539, \
    0.4233210140873113, \
    0.4557365629792204, \
    0.4883601253415709, \
    0.5209836877039214, \
    0.5533992365958304, \
    0.5854027290789878, \
    0.6167979372325460, \
    0.6474000461349729 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, x, f

def truncated_normal_a_cdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_CDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_A_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_CDF_VALUES stores values of the TRUNCATED_NORMAL_a_CDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             A             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, x, f = truncated_normal_a_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, a, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_mean ( mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MEAN returns the mean of the lower Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the parent Normal Distribution.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the mean of the PDF.
#
  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = 0.0

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_a_mean_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MEAN_TEST tests TRUNCATED_NORMAL_A_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sample_num = 1000
  seed = 123456789
  a = 50.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_MEAN computes the mean' )
  print ( '  of the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,+oo)' % ( a ) )

  m = truncated_normal_a_mean ( mu, sigma, a )

  print ( '' )
  print ( '  PDF mean = %g' % ( m ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_a_sample ( mu, sigma, a, seed )

  ms = r8vec_mean ( sample_num, x )
  xmax = r8vec_max ( sample_num, x )
  xmin = r8vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( ms ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_moment ( order, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENT: moments of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the moment of the PDF.
#
  value = r8_mop ( order ) \
    * truncated_normal_b_moment ( order, -mu, sigma, -a );

  return value

def truncated_normal_a_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENT_TEST tests TRUNCATED_NORMAL_A_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 6
  mu_test =    np.array ( [  0.0,  0.0,   0.0,   0.0,  0.0,  -5.0 ] )
  sigma_test = np.array ( [  1.0,  1.0,   1.0,   2.0,  2.0,   1.0 ] )
  a_test =     np.array ( [  0.0, -10.0, 10.0, -10.0, 10.0, -10.0 ] )

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_MOMENT evaluates moments' )
  print ( '  of the lower Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    a = a_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, A = %g' \
      % ( test, mu, sigma, a ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_a_moment ( order, mu, sigma, a )
      print ( '  %2d  %12g' % ( order, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_pdf ( x, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_PDF evaluates the lower Truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the value of the PDF.
# 
  if ( x < a ):
  
    value = 0.0
    
  else:
  
    alpha = ( a - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = normal_01_cdf ( alpha )
    beta_cdf = 1.0
    xi_pdf = normal_01_pdf ( xi )

    value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  return value

def truncated_normal_a_pdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_PDF_TEST tests TRUNCATED_NORMAL_A_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_PDF evaluates the PDF' )
  print ( '  of the lower Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [a,+oo)' )

  print ( '' )
  print ( '                                                 Stored         Computed' )
  print ( '       X        Mu         S         A             PDF             PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, x, pdf1 = truncated_normal_a_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = truncated_normal_a_pdf ( x, mu, sigma, a )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, a, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_pdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_PDF_VALUES: values of the Truncated Normal A PDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval [A,+oo).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real A, the lower truncation limit.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  f_vec = np.array ( ( \
     0.01507373507401876, \
     0.01551417047139894, \
     0.01586560931024694, \
     0.01612150073158793, \
     0.01627701240029317, \
     0.01632918226724295, \
     0.01627701240029317, \
     0.01612150073158793, \
     0.01586560931024694, \
     0.01551417047139894, \
     0.01507373507401876 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, x, f

def truncated_normal_a_pdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_PDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_A_PDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_PDF_VALUES stores values of the TRUNCATED_NORMAL_a_PDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             A             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, x, f = truncated_normal_a_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, a, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_sample ( mu, sigma, a, seed ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_SAMPLE samples the lower Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, the lower truncation limit.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random number generator.
#
  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  u, seed = r8_uniform_01 ( seed )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x, seed

def truncated_normal_a_sample_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_SAMPLE_TEST tests TRUNCATED_NORMAL_A_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  sample_num = 10
  seed = 123456789
  a = 50.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_SAMPLE samples' )
  print ( '  the lower Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,+oo)' % ( a ) )
  print ( '' )

  print ( '' )
  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_a_sample ( mu, sigma, a, seed )
    print ( '  %4d  %14.6g' % ( i, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_variance ( mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_VARIANCE: variance of the lower Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the variance of the PDF.
#
  alpha = ( a - mu ) / sigma

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = 0.0

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  value = sigma * sigma * ( 1.0 \
    + ( alpha * alpha_pdf - 0.0 ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value

def truncated_normal_a_variance_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_VARIANCE_TEST tests TRUNCATED_NORMAL_A_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sample_num = 1000
  seed = 123456789
  a = 50.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_VARIANCE computes the variance' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,+oo)' % ( a ) )

  value = truncated_normal_a_variance ( mu, sigma, a )

  print ( '' )
  print ( '  PDF variance = %g' % ( value ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_a_sample ( mu, sigma, a, seed )

  value = r8vec_variance ( sample_num, x )

  print ( '' )
  print ( '  Sample size = %d' % ( sample_num ) )
  print ( '  Sample variance = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_cdf_inv ( cdf, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF_INV inverts the upper truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'TRUNCATED_NORMAL_B_CDF_INV - Fatal error!' )

  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_b_cdf_inv_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF_INV_TEST tests TRUNCATED_NORMAL_B_CDF_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  sample_num = 10
  seed = 123456789
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_CDF_INV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_CDF_INV inverts the CDF of' )
  print ( '  the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )

  print ( '' )
  print ( '             X            CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_b_sample ( mu, sigma, b, seed )
    cdf = truncated_normal_b_cdf ( x, mu, sigma, b )
    x2 = truncated_normal_b_cdf_inv ( cdf, mu, sigma, b )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_CDF_INV_TEST' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_cdf ( x, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF evaluates the upper Truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE, the value of the CDF.
# 
  if ( x <= b ):
  
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = 0.0
    beta_cdf = normal_01_cdf ( beta )
    xi_cdf = normal_01_cdf ( xi )

    value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  else:
  
    value = 1.0
    
  return value

def truncated_normal_b_cdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_TEST tests TRUNCATED_NORMAL_AB_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_CDF evaluates the CDF' )
  print ( '  of the upper Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,b]' )

  print ( '' )
  print ( '                                                 Stored         Computed' )
  print ( '       X        Mu         S         B             CDF             CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, cdf1 = truncated_normal_b_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = truncated_normal_b_cdf ( x, mu, sigma, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, b, cdf1, cdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_cdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF_VALUES: values of the Truncated Normal B CDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval (-oo,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real B, the upper truncation limit.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.3525999538650271, \
    0.3832020627674540, \
    0.4145972709210122, \
    0.4466007634041696, \
    0.4790163122960786, \
    0.5116398746584291, \
    0.5442634370207796, \
    0.5766789859126887, \
    0.6086824783958461, \
    0.6400776865494043, \
    0.6706797954518312 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, b, x, f

def truncated_normal_b_cdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_B_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_CDF_VALUES stores values of the TRUNCATED_NORMAL_B_CDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             B             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, f = truncated_normal_b_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, b, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_mean ( mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MEAN returns the mean of the upper Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the parent Normal Distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE, the mean of the PDF.
#
  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  alpha_pdf = 0.0
  beta_pdf = normal_01_pdf ( beta )

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_b_mean_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MEAN_TEST tests TRUNCATED_NORMAL_B_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sample_num = 1000
  seed = 123456789
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_MEAN computes the mean' )
  print ( '  of the Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )

  m = truncated_normal_b_mean ( mu, sigma, b )

  print ( '' )
  print ( '  PDF mean = %g' % ( m ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_b_sample ( mu, sigma, b, seed )

  ms = r8vec_mean ( sample_num, x )
  xmax = r8vec_max ( sample_num, x )
  xmin = r8vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( ms ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_moment ( order, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MOMENT: moments of upper truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE, the moment of the PDF.
#
  from sys import exit

  if ( order < 0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )
    print ( '  ORDER < 0.' )
    exit ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    exit ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_CDF too small.' )
    print ( '  B_PDF = %g' % ( b_pdf ) )
    print ( '  B_CDF = %g' % ( b_cdf ) )
    exit ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )

  f = b_pdf / b_cdf;

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - f
    else:
      ir = - b_h ** ( r - 1 ) * f + ( r - 1 ) * irm2

    value = value + r8_choose ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_b_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MOMENT_TEST tests TRUNCATED_NORMAL_B_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 6
  mu_test =    np.array ( [ 0.0,  0.0,  0.0,   0.0,   0.0,  5.0 ] )
  sigma_test = np.array ( [ 1.0,  1.0,  1.0,   2.0,   2.0,  1.0 ] )
  b_test =     np.array ( [ 0.0, 10.0, -10.0, 10.0, -10.0, 10.0 ] )

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_MOMENT evaluates moments' )
  print ( '  of the upper Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    b = b_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, B = %g' \
      % ( test, mu, sigma, b ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_b_moment ( order, mu, sigma, b )
      print ( '  %2d  %12g' % ( order, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_pdf ( x, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_PDF evaluates the upper Truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE, the value of the PDF.
# 
  if ( x <= b ):
  
    beta = ( b - mu ) / sigma
    xi = ( x - mu ) / sigma

    alpha_cdf = 0.0
    beta_cdf = normal_01_cdf ( beta )
    xi_pdf = normal_01_pdf ( xi )

    value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  else:
  
    value = 0.0
    
  return value

def truncated_normal_b_pdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_PDF_TEST tests TRUNCATED_NORMAL_B_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_PDF evaluates the PDF' )
  print ( '  of the upper Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean = mu' )
  print ( '    standard deviation = sigma' )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,b]' )

  print ( '' )
  print ( '                                                 Stored         Computed' )
  print ( '       X        Mu         S         B             PDF             PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, pdf1 = truncated_normal_b_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = truncated_normal_b_pdf ( x, mu, sigma, b )

    print ( '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, b, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_pdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_PDF_VALUES: values of the Truncated Normal B PDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval (-oo,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real B, the upper truncation limit.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  b_vec = np.array ( ( \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0, \
     150.0 ))

  f_vec = np.array ( ( \
    0.01507373507401876, \
    0.01551417047139894, \
    0.01586560931024694, \
    0.01612150073158793, \
    0.01627701240029317, \
    0.01632918226724295, \
    0.01627701240029317, \
    0.01612150073158793, \
    0.01586560931024694, \
    0.01551417047139894, \
    0.01507373507401876 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, b, x, f

def truncated_normal_b_pdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_PDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_B_PDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_PDF_VALUES stores values of the TRUNCATED_NORMAL_B_PDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             B             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, f = truncated_normal_b_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, b, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_sample ( mu, sigma, b, seed ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_SAMPLE samples the upper Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random number generator.
#
  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  u, seed = r8_uniform_01 ( seed )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x, seed

def truncated_normal_b_sample_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_SAMPLE_TEST tests TRUNCATED_NORMAL_B_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  sample_num = 10
  seed = 123456789
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_SAMPLE samples' )
  print ( '  the upper Truncated Normal distribution.' )

  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )
  print ( '' )

  print ( '' )
  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_b_sample ( mu, sigma, b, seed )
    print ( '  %4d  %14.6g' % ( i, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_variance ( mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_VARIANCE: variance of the upper Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#
#    Input, real B, the upper truncation limits.
#
#    Output, real VALUE, the variance of the PDF.
#
  beta = ( b - mu ) / sigma

  alpha_pdf = 0.0
  beta_pdf = normal_01_pdf ( beta )

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  value = sigma * sigma * ( 1.0 \
    + ( 0.0 - beta * beta_pdf ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value

def truncated_normal_b_variance_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_VARIANCE_TEST tests TRUNCATED_NORMAL_B_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sample_num = 1000
  seed = 123456789
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_VARIANCE computes the variance' )
  print ( '  of the Truncated Normal distribution.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( sigma ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval (-oo,%g]' % ( b ) )

  value = truncated_normal_b_variance ( mu, sigma, b )

  print ( '' )
  print ( '  PDF variance = %g' % ( value ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_b_sample ( mu, sigma, b, seed )

  value = r8vec_variance ( sample_num, x )

  print ( '' )
  print ( '  Sample size = %d' % ( sample_num ) )
  print ( '  Sample variance = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_TEST tests the TRUNCATED_NORMAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
# 
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TRUNCATED_NORMAL library.' )
#
#  Utilities:
#
  i4_uniform_ab_test ( )

  normal_01_cdf_values_test ( )

  r8_choose_test ( )
  r8_factorial2_test ( )
  r8_factorial2_values_test ( )
  r8_mop_test ( )
  r8_uniform_01_test ( )

  r8poly_print_test ( )
  r8poly_value_horner_test ( )

  r8vec_linspace_test ( )
  r8vec_max_test ( )
  r8vec_mean_test ( )
  r8vec_min_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )
  r8vec_variance_test ( )

  truncated_normal_a_cdf_values_test ( )
  truncated_normal_a_pdf_values_test ( )

  truncated_normal_ab_cdf_values_test ( )
  truncated_normal_ab_pdf_values_test ( )

  truncated_normal_b_cdf_values_test ( )
  truncated_normal_b_pdf_values_test ( )

  timestamp_test ( )
#
#  Library:
#
  normal_01_cdf_test ( )
  normal_01_cdf_inv_test ( )
  normal_01_mean_test ( )
  normal_01_moment_test ( )
  normal_01_pdf_test ( )
  normal_01_sample_test ( )
  normal_01_variance_test ( )

  normal_ms_cdf_test ( )
  normal_ms_cdf_inv_test ( )
  normal_ms_mean_test ( )
  normal_ms_moment_test ( )
  normal_ms_moment_central_test ( )
  normal_ms_pdf_test ( )
  normal_ms_sample_test ( )
  normal_ms_variance_test ( )

  truncated_normal_a_cdf_test ( )
  truncated_normal_a_cdf_inv_test ( )
  truncated_normal_a_mean_test ( )
  truncated_normal_a_moment_test ( )
  truncated_normal_a_pdf_test ( )
  truncated_normal_a_sample_test ( )
  truncated_normal_a_variance_test ( )

  truncated_normal_ab_cdf_test ( )
  truncated_normal_ab_cdf_inv_test ( )
  truncated_normal_ab_mean_test ( )
  truncated_normal_ab_moment_test ( )
  truncated_normal_ab_pdf_test ( )
  truncated_normal_ab_sample_test ( )
  truncated_normal_ab_variance_test ( )

  truncated_normal_b_cdf_test ( )
  truncated_normal_b_cdf_inv_test ( )
  truncated_normal_b_mean_test ( )
  truncated_normal_b_moment_test ( )
  truncated_normal_b_pdf_test ( )
  truncated_normal_b_sample_test ( )
  truncated_normal_b_variance_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  truncated_normal_test ( )
  timestamp ( )
