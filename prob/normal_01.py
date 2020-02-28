#! /usr/bin/env python
#
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
#    04 March 2016
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
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  a1 = 0.398942280444E+00
  a2 = 0.399903438504E+00
  a3 = 5.75885480458E+00
  a4 = 29.8213557808E+00
  a5 = 2.62433121679E+00
  a6 = 48.6959930692E+00
  a7 = 5.92885724438E+00
  b0 = 0.398942280385E+00
  b1 = 3.8052E-08
  b2 = 1.00000615302E+00
  b3 = 3.98064794E-04
  b4 = 1.98615381364E+00
  b5 = 0.151679116635E+00
  b6 = 5.29330324926E+00
  b7 = 4.8385912808E+00
  b8 = 15.1508972451E+00
  b9 = 0.742380924027E+00
  b10 = 30.789933034E+00
  b11 = 3.99019417011E+00
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
    cdf = q
  else:
    cdf = 1.0 - q

  return cdf

def normal_01_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_TEST tests NORMAL_01_CDF, NORMAL_01_CDF_INV, NORMAL_01_PDF
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
  import platform

  print ( '' )
  print ( 'NORMAL_01_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF evaluates the Normal 01 CDF' )
  print ( '  NORMAL_01_CDF_INV inverts the Normal 01 CDF.' )
  print ( '  NORMAL_01_PDF evaluates the Normal 01 PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    x, seed = normal_01_sample ( seed )

    pdf = normal_01_pdf ( x )

    cdf = normal_01_cdf ( x )

    x2 = normal_01_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf_inv ( p ):

#*****************************************************************************80
#
## NORMAL_01_CDF_INV inverts the standard normal CDF.
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
#    04 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by Michael Wichura.
#    Python version by John Burkardt.
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
#    Input, real P, the value of the cumulative probability 
#    densitity function.  0 < P < 1.  If P is not in this range, an "infinite"
#    result is returned.
#
#    Output, real VALUE, the normal deviate value with the 
#    property that the probability of a standard normal deviate being 
#    less than or equal to the value is P.
#
  import numpy as np
  from r8poly_value_horner import r8poly_value_horner

  r8_huge = 1.0E+30

  a = np.array ( [ \
        3.3871328727963666080, \
        1.3314166789178437745e+2, \
        1.9715909503065514427e+3, \
        1.3731693765509461125e+4, \
        4.5921953931549871457e+4, \
        6.7265770927008700853e+4, \
        3.3430575583588128105e+4, \
        2.5090809287301226727e+3 ] )

  b = np.array ( [ \
        1.0, \
        4.2313330701600911252e+1, \
        6.8718700749205790830e+2, \
        5.3941960214247511077e+3, \
        2.1213794301586595867e+4, \
        3.9307895800092710610e+4, \
        2.8729085735721942674e+4, \
        5.2264952788528545610e+3 ] )

  c = np.array ( [  
        1.42343711074968357734, \
        4.63033784615654529590, \
        5.76949722146069140550, \
        3.64784832476320460504, \
        1.27045825245236838258, \
        2.41780725177450611770e-1, \
        2.27238449892691845833e-2, \
        7.74545014278341407640e-4 ] )

  const1 = 0.180625
  const2 = 1.6

  d = np.array ( [ 
        1.0, \
        2.05319162663775882187, \
        1.67638483018380384940, \
        6.89767334985100004550e-1, \
        1.48103976427480074590e-1, \
        1.51986665636164571966e-2, \
        5.47593808499534494600e-4, \
        1.05075007164441684324e-9 ] )

  e = np.array ( [ \
        6.65790464350110377720, \
        5.46378491116411436990, \
        1.78482653991729133580, \
        2.96560571828504891230e-1, \
        2.65321895265761230930e-2, \
        1.24266094738807843860e-3, \
        2.71155556874348757815e-5, \
        2.01033439929228813265e-7 ] )

  f = np.array ( [ \
        1.0, \
        5.99832206555887937690e-1, \
        1.36929880922735805310e-1, \
        1.48753612908506148525e-2, \
        7.86869131145613259100e-4, \
        1.84631831751005468180e-5, \
        1.42151175831644588870e-7, \
        2.04426310338993978564e-15 ] )

  split1 = 0.425
  split2 = 5.0

  if ( p <= 0.0 ):
    value = - r8_huge
    return value

  if ( 1.0 <= p ):
    value = r8_huge
    return value

  q = p - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r8poly_value_horner ( 7, a, r ) / r8poly_value_horner ( 7, b, r )

  else:

    if ( q < 0.0 ):
      r = p
    else:
      r = 1.0 - p

    if ( r <= 0.0 ):

      value = r8_huge

    else:

      r = np.sqrt ( - np.log ( r ) )

      if ( r <= split2 ):

        r = r - const2
        value = r8poly_value_horner ( 7, c, r ) / r8poly_value_horner ( 7, d, r )

      else:

        r = r - split2
        value = r8poly_value_horner ( 7, e, r ) / r8poly_value_horner ( 7, f, r )

    if ( q < 0.0 ):
      value = - value

  return value

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
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def normal_01_pdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_PDF evaluates the Normal 01 PDF.
#
#  Discussion:
#
#    The Normal 01 PDF is also called the "Standard Normal" PDF, or
#    the Normal PDF with 0 mean and variance 1.
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
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return pdf

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
#    The Box-Muller method is used.
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
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, X, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )
  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return x, seed

def normal_01_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLE_TEST tests NORMAL_01_MEAN, NORMAL_01_SAMPLE, NORMAL_01_VARIANCE.
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
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'NORMAL_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_MEAN computes the Normal 01 mean' )
  print ( '  NORMAL_01_SAMPLE samples the Normal 01 distribution' )
  print ( '  NORMAL_01_VARIANCE returns the Normal 01 variance.' )

  mean = normal_01_mean ( )
  variance = normal_01_variance ( )

  print ( '' )
  print ( '  PDF mean =      %14g' % ( mean ) )
  print ( '  PDF variance =  %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = normal_01_sample ( seed )

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
  print ( 'NORMAL_01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_01_samples ( n, seed ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLES: multiple samples of the standard normal PDF.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of samples.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, X[N], a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8vec_uniform_01 import r8vec_uniform_01

  r1, seed = r8vec_uniform_01 ( n, seed )
  r2, seed = r8vec_uniform_01 ( n, seed )

  x = np.zeros ( n )
  x[0:n] = np.sqrt ( - 2.0 * np.log ( r1[0:n] ) ) \
    * np.cos ( 2.0 * np.pi * r2[0:n] )

  return x, seed

def normal_01_samples_test ( ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLES_TEST tests NORMAL_01_MEAN, NORMAL_01_SAMPLES, NORMAL_01_VARIANCE.
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
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'NORMAL_01_SAMPLES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_MEAN computes the Normal 01 mean' )
  print ( '  NORMAL_01_SAMPLES samples the Normal 01 distribution' )
  print ( '  NORMAL_01_VARIANCE returns the Normal 01 variance.' )

  mean = normal_01_mean ( )
  variance = normal_01_variance ( )

  print ( '' )
  print ( '  PDF mean =      %14g' % ( mean ) )
  print ( '  PDF variance =  %14g' % ( variance ) )

  x, seed = normal_01_samples ( nsample, seed )

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
  print ( 'NORMAL_01_SAMPLES_TEST' )
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
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = 1.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_cdf_test ( )
  normal_01_sample_test ( )
  normal_01_samples_test ( )
  timestamp ( )

