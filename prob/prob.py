#! /usr/bin/env python3
#
def angle_cdf ( x, n ):

#*****************************************************************************80
#
## angle_cdf() evaluates the Angle CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation and Sensitivity of Queueing Networks,
#    Wiley, 1986.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    integer N, the spatial dimension.
#    N must be at least 2.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( n < 2 ):
    print ( '' )
    print ( 'angle_cdf(): Fatal error!' )
    print ( '  N must be at least 2.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'angle_cdf(): Fatal error!' )

  if ( x <= 0.0 ):
    cdf = 0.0
  elif ( np.pi <= x ):
    cdf = 1.0
  elif ( n == 2 ):
    cdf = x / np.pi
  else:
    cdf = sin_power_int ( 0.0, x, n - 2 ) * gamma ( n / 2.0 ) \
      / ( np.sqrt ( np.pi ) * gamma ( ( n - 1 ) / 2.0 ) )

  return cdf

def angle_cdf_test ( rng ):

#*****************************************************************************80
#
## angle_cdf_test() tests angle_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'angle_cdf_test():' )
  print ( '  angle_cdf() evaluates the Angle CDF' )

  n = 5
  x = 0.50

  cdf = angle_cdf ( x, n )

  print ( '' )
  print ( '  PDF parameter N = %6d' % ( n ) )
  print ( '  PDF argument X =  %14g' % ( x ) )
  print ( '  CDF value =       %14g' % ( cdf ) )

  return

def angle_mean ( n ):

#*****************************************************************************80
#
## angle_mean() returns the mean of the Angle PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the spatial dimension.
#    N must be at least 2.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = np.pi / 2.0

  return mean

def angle_mean_test ( ):

#*****************************************************************************80
#
## angle_mean_test() tests angle_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'angle_mean_test():' )
  print ( '  angle_mean() computes the Angle mean' )

  n = 5
  mean = angle_mean ( n )

  print ( '' )
  print ( '  PDF parameter N = %6d' % ( n ) )
  print ( '  PDF mean =        %14g' % ( mean ) )

  return

def angle_pdf ( x, n ):

#*****************************************************************************80
#
## angle_pdf() evaluates the Angle PDF.
#
#  Discussion:
#
#    X is an angle between 0 and PI, corresponding to the angle
#    made in an N-dimensional space, between a fixed line passing
#    through the origin, and an arbitrary line that also passes
#    through the origin, which is specified by a choosing any point
#    on the N-dimensional sphere with uniform probability.
#
#  Formula:
#
#    PDF(X) = ( sin ( X ) )^(N-2) * Gamma ( N / 2 )
#             / ( sqrt ( PI ) * Gamma ( ( N - 1 ) / 2 ) )
#
#    PDF(X) = 1 / PI if N = 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation and Sensitivity of Queueing Networks,
#    Wiley, 1986.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    integer N, the spatial dimension.
#    N must be at least 2.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( n < 2 ):
    print ( '' )
    print ( 'angle_pdf(): Fatal error!' )
    print ( '  N must be at least 2.' )
    print ( '  The input value of N = ', n )
    raise Exception ( 'angle_pdf(): Fatal error!' )

  if ( x < 0.0 or np.pi < x ):
    pdf = 0.0
  elif ( n == 2 ):
    pdf = 1.0 / np.pi
  else:
    pdf = ( np.sin ( x ) ) ** ( n - 2 ) * gamma ( n / 2.0 ) \
      / ( np.sqrt ( np.pi ) * gamma ( ( n - 1 ) / 2.0 ) )

  return pdf

def angle_pdf_test ( ):

#*****************************************************************************80
#
## angle_pdf_test() tests angle_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'angle_pdf_test():' )
  print ( '  angle_pdf() evaluates the Angle PDF' )

  n = 5
  x = 0.50

  pdf = angle_pdf ( x, n )

  print ( '' )
  print ( '  PDF parameter N = %6d' % ( n ) )
  print ( '  PDF argument X =  %14g' % ( x ) )
  print ( '  PDF value =       %14g' % ( pdf ) )

  return

def anglit_cdf ( x ):

#*****************************************************************************80
#
## anglit_cdf() evaluates the Anglit CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <  -0.25 * np.pi ):
    cdf = 0.0
  elif ( x < 0.25 * np.pi ):
    cdf = 0.5 - 0.5 * np.cos ( 2.0 * x + np.pi / 2.0 )
  else:
    cdf = 1.0

  return cdf

def anglit_cdf_inv ( cdf ):

#*****************************************************************************80
#
## anglit_cdf_inv() inverts the Anglit CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'anglit_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'anglit_cdf_inv(): Fatal error!' )

  x = 0.5 * ( np.arccos ( 1.0 - 2.0 * cdf ) - np.pi / 2.0 )

  return x

def anglit_cdf_test ( rng ):

#*****************************************************************************80
#
## anglit_cdf_test() tests anglit_cdf(), anglit_cdf_inv(), anglit_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'anglit_cdf_test():' )
  print ( '  anglit_cdf() evaluates the Anglit CDF' )
  print ( '  anglit_cdf_inv() inverts the Anglit CDF.' )
  print ( '  anglit_pdf() evaluates the Anglit PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = anglit_sample ( rng )

    pdf = anglit_pdf ( x )

    cdf = anglit_cdf ( x )

    x2 = anglit_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def anglit_mean ( ):

#*****************************************************************************80
#
## anglit_mean() returns the mean of the Anglit PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def anglit_pdf ( x ):

#*****************************************************************************80
#
## anglit_pdf() evaluates the Anglit PDF.
#
#  Formula:
#
#    PDF(X) = SIN ( 2 * X + PI / 2 ) for -PI/4 <= X <= PI/4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= -0.25 * np.pi or 0.25 * np.pi <= x ):
    pdf = 0.0
  else:
    pdf = np.sin ( 2.0 * x + 0.25 * np.pi )

  return pdf

def anglit_sample ( rng ):

#*****************************************************************************80
#
## anglit_sample() samples the Anglit PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = anglit_cdf_inv ( cdf )

  return x

def anglit_sample_test ( rng ):

#*****************************************************************************80
#
## anglit_sample_test() tests anglit_mean(), anglit_sample(), anglit_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'anglit_sample_test():' )
  print ( '  anglit_mean() computes the Anglit mean' )
  print ( '  anglit_sample() samples the Anglit distribution' )
  print ( '  anglit_variance() computes the Anglit variance.' )

  mean = anglit_mean ( )
  variance = anglit_variance ( )

  print ( '' )
  print ( '  PDF mean =     %14g' % ( mean ) )
  print ( '  PDF variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = anglit_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def anglit_variance ( ):

#*****************************************************************************80
#
## anglit_variance() returns the variance of the Anglit PDF.
#
#  Discussion:
#
#    Variance =
#      Integral ( -PI/4 <= X <= PI/4 ) X^2 * SIN ( 2 * X + PI / 2 )
#
#    Antiderivative =
#      0.5 * X * SIN ( 2 * X + PI / 2 )
#      + ( 0.25 - 0.5 * X^2 ) * COS ( 2 * X + PI / 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = 0.0625 * np.pi ** 2 - 0.5

  return variance

def arcsin_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## arcsin_cdf_inv() inverts the Arcsin CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, the parameter of the CDF.
#    A must be positive.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'arcsin_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'arcsin_cdf_inv(): Fatal error!' )

  x = a * np.sin ( np.pi * ( cdf - 0.5 ) )

  return x

def arcsin_cdf ( x, a ):

#*****************************************************************************80
#
## arcsin_cdf() evaluates the Arcsin CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, the parameter of the CDF.
#    A must be positive.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= -a ):
    cdf = 0.0
  elif ( x < a ):
    cdf = 0.5 + np.arcsin ( x / a ) / np.pi
  else:
    cdf = 1.0

  return cdf

def arcsin_cdf_test ( rng ):

#*****************************************************************************80
#
## arcsin_cdf_test() tests arcsin_cdf(), arcsin_cdf_inv(), arcsin_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'arcsin_cdf_test():' )
  print ( '  arcsin_cdf() evaluates the Arcsin CDF' )
  print ( '  arcsin_cdf_inv() inverts the Arcsin CDF.' )
  print ( '  arcsin_pdf() evaluates the Arcsin PDF' )

  a = 1.0

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  if ( not arcsin_check ( a ) ):
    print ( '' )
    print ( 'arcsin_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    raise Exception ( 'arcsin_cdf_test(): Fatal error!' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = arcsin_sample ( a, rng )

    pdf = arcsin_pdf ( x, a )

    cdf = arcsin_cdf ( x, a )

    x2 = arcsin_cdf_inv ( cdf, a )

    print ( ' %14f  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def arcsin_check ( a ):

#*****************************************************************************80
#
## arcsin_check() checks the parameter of the Arcsin CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are OK.
#
  if ( a <= 0.0 ):
    print ( '' )
    print ( 'arcsin_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False
  else:
    check = True

  return check

def arcsin_mean ( a ):

#*****************************************************************************80
#
## arcsin_mean() returns the mean of the Arcsin PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the CDF.
#    A must be positive.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def arcsin_pdf ( x, a ):

#*****************************************************************************80
#
## arcsin_pdf() evaluates the Arcsin PDF.
#
#  Discussion:
#
#    The LOGISTIC EQUATION has the form:
#
#      X(N+1) = 4.0 * LAMBDA * ( 1.0 - X(N) ).
#
#    where 0 < LAMBDA <= 1.  This nonlinear difference equation maps
#    the unit interval into itself, and is a simple example of a system
#    exhibiting chaotic behavior.  Ulam and von Neumann studied the
#    logistic equation with LAMBDA = 1, and showed that iterates of the
#    function generated a sequence of pseudorandom numbers with
#    the Arcsin probability density function.
#
#    The derived sequence
#
#      Y(N) = ( 2 / PI ) * Arcsin ( SQRT ( X(N) ) )
#
#    is a pseudorandom sequence with the uniform probability density
#    function on [0,1].  For certain starting values, such as X(0) = 0, 0.75,
#    or 1.0, the sequence degenerates into a constant sequence, and for
#    values very near these, the sequence takes a while before becoming
#    chaotic.
#
#    PDF(X) = 1 / ( PI * Sqrt ( A^2 - X^2 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger and Stephen Kokoska,
#    CRC Standard Probability and Statistics Tables and Formulae,
#    Chapman and Hall/CRC, 2000, pages 114-115.
#
#  Input:
#
#    real X, the argument of the PDF.
#    -A < X < A.
#
#    real A, the parameter of the CDF.
#    A must be positive.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'arcsin_pdf(): Fatal error!' )
    print ( '  Parameter A must be positive.' )
    raise Exception ( 'arcsin_pdf(): Fatal error!' )

  if ( x <= - a or a <= x ):
    pdf = 0.0
  else:
    pdf = 1.0 / ( np.pi * np.sqrt ( a * a - x * x ) )

  return pdf

def arcsin_sample ( a, rng ):

#*****************************************************************************80
#
## arcsin_sample() samples the Arcsin PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the CDF.
#    A must be positive.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = arcsin_cdf_inv ( cdf, a )

  return x

def arcsin_sample_test ( rng ):

#*****************************************************************************80
#
## arcsin_sample_test() tests arcsin_mean(), arcsin_sample(), arcsin_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'arcsin_sample_test():' )
  print ( '  arcsin_mean() computes the Arcsin mean' )
  print ( '  arcsin_sample() samples the Arcsin distribution' )
  print ( '  arcsin_variance() computes the Arcsin variance.' )

  for i in range ( 1, 3 ):

    if ( i == 1 ):
      a = 1.0
    elif ( i == 2 ):
      a = 16.0

    print ( '' )
    print ( '  PDF parameter A = %14g' % ( a ) )

    if ( not arcsin_check ( a ) ):
      print ( '' )
      print ( 'arcsin_sample_test(): Fatal error!' )
      print ( '  The parameters are not legal.' )
      return

    mean = arcsin_mean ( a )
    variance = arcsin_variance ( a )

    print ( '  PDF mean =        %14g' % ( mean ) )
    print ( '  PDF variance =    %14g' % ( variance ) )
  
    x = np.zeros ( nsample )
    for j in range ( 0, nsample ):
      x[j] = arcsin_sample ( a, rng )

    mean = np.mean ( x )
    variance = np.var ( x )
    xmax = np.max ( x )
    xmin = np.min ( x )

    print ( '' )
    print ( '  Sample size =     %6d' % ( nsample ) )
    print ( '  Sample mean =     %14g' % ( mean ) )
    print ( '  Sample variance = %14g' % ( variance ) )
    print ( '  Sample maximum =  %14g' % ( xmax ) )
    print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def arcsin_variance ( a ):

#*****************************************************************************80
#
## arcsin_variance() returns the variance of the Arcsin PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the CDF.
#    A must be positive.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a * a / 2.0

  return variance

def benford_cdf ( x ):

#*****************************************************************************80
#
## benford_cdf() returns the Benford CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the string of significant digits to be checked.
#    If X is 1, then we are asking for the Benford probability that
#    a value will have first digit 1.  If X is 123, we are asking for
#    the probability that the first three digits will be 123, and so on.
#
#  Output:
#
#    real CDF, the Benford probability that an item taken from
#    a real world distribution will have the initial digit of X or less.
#
  import numpy as np

  if ( x <= 0 ):
    cdf = 0.0
  elif ( i4_is_power_of_10 ( x + 1 ) ):
    cdf = 1.0
  else:
    cdf = np.log10 ( float ( x + 1 ) )
    cdf = ( cdf % 1.0 )

  return cdf

def benford_cdf_test ( rng ):

#*****************************************************************************80
#
## benford_cdf_test() tests benford_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'benford_cdf_test():' )
  print ( '  benford_cdf() evaluates the Benford CDF.' )

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

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = benford_sample ( rng )

    pdf = benford_pdf ( x )

    cdf = benford_cdf ( x )

    x2 = benford_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def benford_cdf_inv ( cdf ):

#*****************************************************************************80
#
## benford_cdf_inv() inverts the Benford CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    Ted Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    Ralph Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Input:
#
#    real CDF: the Benford probability that an item taken
#    from a real world distribution will have the initial 
#    digit X or less.
#
#  Output:
#
#    integer X: a value between 1 and 9 for which the cumulative
#    Benford distribution is CDF.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'benford_cdf_inv(): Fatal error!' )
    print ( '  0.0 <= cdf <= 1.0 required.' )
    print ( '  input value is cdf =', cdf )
    raise Exception ( 'benford_cdf_inv(): Fatal error!' )

  x = np.floor ( 10**cdf - 0.0001 )

  return x

def benford_mean ( ):

#*****************************************************************************80
#
## benford_mean() returns the mean of the Benford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    Ted Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    Ralph Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Output:
#
#    real MU: the mean of the Benford PDF.
#
  import numpy as np

  mu = 0.0
  for i in range ( 1, 10 ):
    mu = mu + i * np.log10 ( ( i + 1 ) / i )

  return mu

def benford_pdf ( x ):

#*****************************************************************************80
#
## benford_pdf() returns the Benford probability of one or more significant digits.
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
#    This code is distributed under the MIT license.
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
#    Frank Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    Ted Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    Ralph Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Input:
#
#    integer X, the string of significant digits to be checked.
#    If X is 1, then we are asking for the Benford probability that
#    a value will have first digit 1.  If X is 123, we are asking for
#    the probability that the first three digits will be 123, and so on.
#
#  Output:
#
#    real PDF, the Benford probability that an item taken from
#    a real world distribution will have the initial digits X.
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
## benford_pdf_test() tests benford_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'benford_pdf_test():' )
  print ( '  benford_pdf() evaluates the Benford PDF.' )

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

  return

def benford_sample ( rng ):

#*****************************************************************************80
#
## benford_sample() samples the Benford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    Ted Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    Ralph Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  cdf = rng.random ( )

  x = benford_cdf_inv ( cdf )

  return x

def benford_sample_test ( rng ):

#*****************************************************************************80
#
## benford_sample_test() tests benford_mean(), benford_sample(), benford_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 10000
 
  print ( '' )
  print ( 'benford_sample_test():' )
  print ( '  benford_mean() computes the mean;' )
  print ( '  benford_sample() samples the distribution;' )
  print ( '  benford_variance() computes the variance.' )

  pdf_mean = benford_mean ( )
  pdf_var = benford_variance ( )

  print ( '' )
  print ( '  PDF mean =        ', pdf_mean )
  print ( '  PDF variance =    ', pdf_var )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = benford_sample ( rng )

  xmean = np.mean ( x )
  xvar = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     ', nsample )
  print ( '  Sample mean =     ', xmean )
  print ( '  Sample variance = ', xvar )
  print ( '  Sample maximum =  ', xmax )
  print ( '  Sample minimum =  ', xmin )

  return

def benford_variance ( ):

#*****************************************************************************80
#
## benford_variance() returns the variance of the Benford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    Ted Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    Ralph Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Output:
#
#    real VARIANCE: the variance of the Benford PDF.
#
  import numpy as np

  mu = 0.0
  for i in range ( 1, 10 ):
    mu = mu + i * np.log10 ( ( i + 1 ) / i )

  variance = 0.0
  for i in range ( 1, 10 ):
    variance = variance + np.log10 ( ( i + 1 ) / i ) * ( i - mu )**2

  return variance

def bernoulli_cdf ( x, a ):

#*****************************************************************************80
#
## bernoulli_cdf() evaluates the Bernoulli CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the number of successes on a single trial.
#    X = 0 or 1.
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 0 ):
    cdf = 0.0
  elif ( x == 0 ):
    cdf = 1.0 - a
  else:
    cdf = 1.0

  return cdf

def bernoulli_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## bernoulli_cdf_inv() inverts the Bernoulli CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, the parameter of the PDF.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    integer X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'bernoulli_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'bernoulli_cdf_inv(): Fatal error!' )

  if ( cdf <= 1.0 - a ):
    x = 0
  else:
    x = 1

  return x

def bernoulli_cdf_test ( rng ):

#*****************************************************************************80
#
## bernoulli_cdf_test() tests bernoulli_cdf(), bernoulli_cdf_inv(), bernoulli_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'bernoulli_cdf_test():' )
  print ( '  bernoulli_cdf() evaluates the Bernoulli CDF' )
  print ( '  bernoulli_cdf_inv() inverts the Bernoulli CDF.' )
  print ( '  bernoulli_pdf() evaluates the Bernoulli PDF' )

  a = 0.75

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  check = bernoulli_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'bernoulli_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = bernoulli_sample ( a, rng )

    pdf = bernoulli_pdf ( x, a )

    cdf = bernoulli_cdf ( x, a )

    x2 = bernoulli_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def bernoulli_check ( a ):

#*****************************************************************************80
#
## bernoulli_check() checks the parameter of the Bernoulli CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are OK.
#
  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'bernoulli_check(): Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False
  else:
    check = True

  return check

def bernoulli_mean ( a ):

#*****************************************************************************80
#
## bernoulli_mean() returns the mean of the Bernoulli PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def bernoulli_pdf ( x, a ):

#*****************************************************************************80
#
## bernoulli_pdf() evaluates the Bernoulli PDF.
#
#  Discussion:
#
#    PDF(X)(A) = A^X * ( 1.0 - A )^( X - 1 )
#
#    X = 0 or 1.
#
#    The Bernoulli PDF describes the simple case in which a single trial
#    is carried out, with two possible outcomes, called "success" and
#    "failure" the probability of success is A.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the number of successes on a single trial.
#    X = 0 or 1.
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0 ):
    pdf = 0.0
  elif ( x == 0 ):
    pdf = 1.0 - a
  elif ( x == 1 ):
    pdf = a
  else:
    pdf = 0.0

  return pdf

def bernoulli_sample ( a, rng ):

#*****************************************************************************80
#
## bernoulli_sample() samples the Bernoulli PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = bernoulli_cdf_inv ( cdf, a )

  return x

def bernoulli_sample_test ( rng ):

#*****************************************************************************80
#
## bernoulli_sample_test() tests bernoulli_mean(), bernoulli_sample(), bernoulli_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'bernoulli_sample_test():' )
  print ( '  bernoulli_mean() computes the Bernoulli mean' )
  print ( '  bernoulli_sample() samples the Bernoulli distribution' )
  print ( '  bernoulli_variance() computes the Bernoulli variance.' )

  a = 0.75

  check = bernoulli_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'bernoulli_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = bernoulli_mean ( a )
  variance = bernoulli_variance ( a )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = bernoulli_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def bernoulli_variance ( a ):

#*****************************************************************************80
#
## bernoulli_variance() returns the variance of the Bernoulli PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a * ( 1.0 - a )

  return variance

def bessel_i0 ( arg ):

#*****************************************************************************80
#
## bessel_i0() evaluates the modified Bessel function of the first kind and order zero.
#
#  Discussion:
#
#    The main computation evaluates slightly modified forms of
#    minimax approximations generated by Blair and Edwards, Chalk
#    River (Atomic Energy of Canada Limited) Report AECL-4928,
#    October, 1974.  This transportable program is patterned after
#    the machine dependent FUNPACK packet NATSI0, but cannot match
#    that version for efficiency or accuracy.  This version uses
#    rational functions that theoretically approximate I-SUB-0(X)
#    to at least 18 significant decimal digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz.
#    This version by John Burkardt.
#
#  Input:
#
#    real ARG, the argument.
#
#  Output:
#
#    real VALUE, the value of the modified Bessel function
#    of the first kind.
#
  import numpy as np

  exp40 = 2.353852668370199854E+17

  p = np.array ( [ \
    -5.2487866627945699800E-18, \
    -1.5982226675653184646E-14, \
    -2.6843448573468483278E-11, \
    -3.0517226450451067446E-08, \
    -2.5172644670688975051E-05, \
    -1.5453977791786851041E-02, \
    -7.0935347449210549190E+00, \
    -2.4125195876041896775E+03, \
    -5.9545626019847898221E+05, \
    -1.0313066708737980747E+08, \
    -1.1912746104985237192E+10, \
    -8.4925101247114157499E+11, \
    -3.2940087627407749166E+13, \
    -5.5050369673018427753E+14, \
    -2.2335582639474375249E+15 ] )

  pp = np.array ( [ \
    -3.9843750000000000000E-01, \
     2.9205384596336793945E+00, \
    -2.4708469169133954315E+00, \
     4.7914889422856814203E-01, \
    -3.7384991926068969150E-03, \
    -2.6801520353328635310E-03, \
     9.9168777670983678974E-05, \
    -2.1877128189032726730E-06 ] )

  q = np.array ( [ \
    -3.7277560179962773046E+03, \
     6.5158506418655165707E+06, \
    -6.5626560740833869295E+09, \
     3.7604188704092954661E+12, \
    -9.7087946179594019126E+14 ] )

  qq = np.array ( [ \
    -3.1446690275135491500E+01, \
     8.5539563258012929600E+01, \
    -6.0228002066743340583E+01, \
     1.3982595353892851542E+01, \
    -1.1151759188741312645E+00, \
     3.2547697594819615062E-02, \
    -5.5194330231005480228E-04 ] )

  rec15 = 6.6666666666666666666E-02
  xmax = 91.9E+00
  xsmall = 2.98E-08

  x = abs ( arg )

  if ( x < xsmall ):
    value = 1.0
  elif ( x < 15.0 ):
#
#  XSMALL <= ABS(ARG) < 15.0
#
    xx = x * x
    sump = p[0]
    for i in range ( 1, 15 ):
      sump = sump * xx + p[i]

    xx = xx - 225.0
    sumq = (((( \
           xx + q[0] ) \
         * xx + q[1] ) \
         * xx + q[2] ) \
         * xx + q[3] ) \
         * xx + q[4]

    value = sump / sumq

  elif ( 15.0 <= x ):

    if ( xmax < x ):
      value = np.finfo(float).max
    else:
#
#  15.0 <= ABS(ARG)
#
      xx = 1.0 / x - rec15

      sump = ((((((  \
                  pp[0] \
           * xx + pp[1] ) \
           * xx + pp[2] ) \
           * xx + pp[3] ) \
           * xx + pp[4] ) \
           * xx + pp[5] ) \
           * xx + pp[6] ) \
           * xx + pp[7]

      sumq = (((((( \
             xx + qq[0] ) \
           * xx + qq[1] ) \
           * xx + qq[2] ) \
           * xx + qq[3] ) \
           * xx + qq[4] ) \
           * xx + qq[5] ) \
           * xx + qq[6]

      value = sump / sumq
#
#  Calculation reformulated to avoid premature overflow.
#
      if ( x <= xmax - 15.0 ):
        a = np.exp ( x )
        b = 1.0
      else:
        a = np.exp ( x - 40.0 )
        b = exp40

      value = ( ( value * a - pp[0] * a ) / np.sqrt ( x ) ) * b

  return value

def bessel_i0_test ( ):

#*****************************************************************************80
#
## bessel_i0_test() tests bessel_i0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_i0_test():' )
  print ( '  bessel_i0() evaluates the Bessel function I0(X)' )
  print ( '' )
  print ( '       X                 Exact F                 I0(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i0_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = bessel_i0 ( x )

    print ( '  %8g  %24.16g  %24.16g' % ( x, fx, fx2 ) )

  return

def bessel_i0_values ( n_data ):

#*****************************************************************************80
#
## bessel_i0_values() returns some values of the I0 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function I0(Z) corresponds to N = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[0,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1010025027795146E+01, \
     0.1040401782229341E+01, \
     0.1092045364317340E+01, \
     0.1166514922869803E+01, \
     0.1266065877752008E+01, \
     0.1393725584134064E+01, \
     0.1553395099731217E+01, \
     0.1749980639738909E+01, \
     0.1989559356618051E+01, \
     0.2279585302336067E+01, \
     0.3289839144050123E+01, \
     0.4880792585865024E+01, \
     0.7378203432225480E+01, \
     0.1130192195213633E+02, \
     0.1748117185560928E+02, \
     0.2723987182360445E+02, \
     0.6723440697647798E+02, \
     0.4275641157218048E+03, \
     0.2815716628466254E+04 ) )

  x_vec = np.array ( ( \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     0.10E+01, \
     0.12E+01, \
     0.14E+01, \
     0.16E+01, \
     0.18E+01, \
     0.20E+01, \
     0.25E+01, \
     0.30E+01, \
     0.35E+01, \
     0.40E+01, \
     0.45E+01, \
     0.50E+01, \
     0.60E+01, \
     0.80E+01, \
     0.10E+02  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def bessel_i0_values_test ( ):

#*****************************************************************************80
#
## bessel_i0_values_test() tests bessel_i0_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_i0_values_test():' )
  print ( '  bessel_i0_values() stores values of the Bessel I function. of order 0.' )
  print ( '' )
  print ( '      X           I(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_i1 ( arg ):

#*****************************************************************************80
#
## bessel_i1() evaluates the Bessel I function of order I.
#
#  Discussion:
#
#    The main computation evaluates slightly modified forms of
#    minimax approximations generated by Blair and Edwards.
#    This transportable program is patterned after the machine-dependent
#    FUNPACK packet NATSI1, but cannot match that version for efficiency
#    or accuracy.  This version uses rational functions that theoretically
#    approximate I-SUB-1(X) to at least 18 significant decimal digits.
#    The accuracy achieved depends on the arithmetic system, the compiler,
#    the intrinsic functions, and proper selection of the machine-dependent
#    constants.
#
#  Machine-dependent constants:
#
#    beta   = Radix for the floating-point system.
#    maxexp = Smallest power of beta that overflows.
#    XMAX =   Largest argument acceptable to BESI1  Solution to
#             equation:
#               EXP(X) * (1-3/(8*X)) / SQRT(2*PI*X) = beta^maxexp
#
#
#    Approximate values for some important machines are:
#
#                            beta       maxexp    XMAX
#
#    CRAY-1        (S.P.)       2         8191    5682.810
#    Cyber 180/855
#      under NOS   (S.P.)       2         1070     745.894
#    IEEE (IBM/XT,
#      SUN, etc.)  (S.P.)       2          128      91.906
#    IEEE (IBM/XT,
#      SUN, etc.)  (D.P.)       2         1024     713.987
#    IBM 3033      (D.P.)      16           63     178.185
#    VAX           (S.P.)       2          127      91.209
#    VAX D-Format  (D.P.)       2          127      91.209
#    VAX G-Format  (D.P.)       2         1023     713.293
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz
#    This version by John Burkardt.
#
#  Reference:
#
#    Blair and Edwards,
#    Chalk River Report AECL-4928,
#    Atomic Energy of Canada, Limited,
#    October, 1974.
#
#  Input:
#
#    real ARG, the argument.
#
#  Output:
#
#    real VALUE, the value of the Bessel I1 function.
#
  import numpy as np

  exp40 = 2.353852668370199854E+17
  forty = 40.0E+00
  half = 0.5E+00
  one = 1.0E+00
  one5 = 15.0E+00

  p = np.array ( [ \
    -1.9705291802535139930E-19, \
    -6.5245515583151902910E-16, \
    -1.1928788903603238754E-12, \
    -1.4831904935994647675E-09, \
    -1.3466829827635152875E-06, \
    -9.1746443287817501309E-04, \
    -4.7207090827310162436E-01, \
    -1.8225946631657315931E+02, \
    -5.1894091982308017540E+04, \
    -1.0588550724769347106E+07, \
    -1.4828267606612366099E+09, \
    -1.3357437682275493024E+11, \
    -6.9876779648010090070E+12, \
    -1.7732037840791591320E+14, \
    -1.4577180278143463643E+15 ] )

  pbar = 3.98437500E-01

  pp = np.array ( [ \
    -6.0437159056137600000E-02, \
     4.5748122901933459000E-01, \
    -4.2843766903304806403E-01, \
     9.7356000150886612134E-02, \
    -3.2457723974465568321E-03, \
    -3.6395264712121795296E-04, \
     1.6258661867440836395E-05, \
    -3.6347578404608223492E-07 ] )

  q = np.array ( [ \
    -4.0076864679904189921E+03, \
     7.4810580356655069138E+06, \
    -8.0059518998619764991E+09, \
     4.8544714258273622913E+12, \
    -1.3218168307321442305E+15 ] )

  qq = np.array ( [ \
    -3.8806586721556593450E+00, \
     3.2593714889036996297E+00, \
    -8.5017476463217924408E-01, \
     7.4212010813186530069E-02, \
    -2.2835624489492512649E-03, \
     3.7510433111922824643E-05 ] )

  rec15 = 6.6666666666666666666E-02
  two25 = 225.0E+00
  xmax = 713.987E+00
  zero = 0.0E+00

  x = abs ( arg )
#
#  ABS(ARG) < EPSILON
#
  if ( x < np.finfo(float).eps ):

    value = half * x
#
#  EPSILON <= ABS(ARG) < 15.0
#
  elif ( x < one5 ):

    xx = x * x
    sump = p[0]
    for j in range ( 1, 15 ):
      sump = sump * xx + p[j]

    xx = xx - two25

    sumq = ((((     \
          xx + q[0] \
      ) * xx + q[1] \
      ) * xx + q[2] \
      ) * xx + q[3] \
      ) * xx + q[4]

    value = ( sump / sumq ) * x

  elif ( xmax < x ):

    value = np.finfo(float).max
#
#  15.0 <= ABS(ARG)
#
  else:

    xx = one / x - rec15

    sump = ((((((    \
               pp[0] \
        * xx + pp[1] \
      ) * xx + pp[2] \
      ) * xx + pp[3] \
      ) * xx + pp[4] \
      ) * xx + pp[5] \
      ) * xx + pp[6] \
      ) * xx + pp[7]

    sumq = (((((     \
          xx + qq[0] \
      ) * xx + qq[1] \
      ) * xx + qq[2] \
      ) * xx + qq[3] \
      ) * xx + qq[4] \
      ) * xx + qq[5]

    value = sump / sumq

    if ( xmax - one5 < x ):
      a = np.exp ( x - forty )
      b = exp40
    else:
      a = np.exp ( x )
      b = one

    value = ( ( value * a + pbar * a ) / np.sqrt ( x ) ) * b

  if ( arg < zero ):
    value = -value

  return value

def bessel_i1_test ( ):

#*****************************************************************************80
#
## bessel_i1_test() tests bessel_i1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_i1_test():' )
  print ( '  bessel_i1() evaluates the Bessel function I1(X)' )
  print ( '' )
  print ( '       X                 Exact F                 I1(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = bessel_i1 ( x )

    print ( '  %8f  %24.16g  %24.16g' % ( x, fx, fx2 ) )

  return

def bessel_i1_values ( n_data ):

#*****************************************************************************80
#
## bessel_i1_values() returns some values of the I1 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[1,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1005008340281251E+00, \
     0.2040267557335706E+00, \
     0.3137040256049221E+00, \
     0.4328648026206398E+00, \
     0.5651591039924850E+00, \
     0.7146779415526431E+00, \
     0.8860919814143274E+00, \
     0.1084810635129880E+01, \
     0.1317167230391899E+01, \
     0.1590636854637329E+01, \
     0.2516716245288698E+01, \
     0.3953370217402609E+01, \
     0.6205834922258365E+01, \
     0.9759465153704450E+01, \
     0.1538922275373592E+02, \
     0.2433564214245053E+02, \
     0.6134193677764024E+02, \
     0.3998731367825601E+03, \
     0.2670988303701255E+04 ) )

  x_vec = np.array ( ( \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     0.10E+01, \
     0.12E+01, \
     0.14E+01, \
     0.16E+01, \
     0.18E+01, \
     0.20E+01, \
     0.25E+01, \
     0.30E+01, \
     0.35E+01, \
     0.40E+01, \
     0.45E+01, \
     0.50E+01, \
     0.60E+01, \
     0.80E+01, \
     0.10E+02  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def bessel_i1_values_test ( ):

#*****************************************************************************80
#
## bessel_i1_values_test() tests bessel_i1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_i1_values_test():' )
  print ( '  bessel_i1_values() stores values of the Bessel I function. of order 1.' )
  print ( '' )
  print ( '      X           I(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def beta_binomial_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## beta_binomial_cdf_inv() inverts the Beta Binomial CDF.
#
#  Discussion:
#
#    A simple discrete approach is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= C.
#
#  Output:
#
#    integer X, the smallest X whose cumulative density function
#    is greater than or equal to CDF.
#

  if ( cdf <= 0.0 ):

    x = 0

  else:

    cum = 0.0

    for y in range ( 0, c + 1 ):

      pdf = r8_beta ( a + y, b + c - y ) / ( ( c + 1 ) \
        * r8_beta ( y + 1, c - y + 1 ) * r8_beta ( a, b ) )

      cum = cum + pdf

      if ( cdf <= cum ):
        x = y
        return x

    x = c

  return x

def beta_binomial_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## beta_binomial_cdf() evaluates the Beta Binomial CDF.
#
#  Discussion:
#
#    A simple summing approach is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the CDF.
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 0 ):

    cdf = 0.0

  elif ( x < c ):

    cdf = 0.0
    for y in range ( 0, x + 1 ):
      pdf = r8_beta ( a + y, b + c - y ) / ( ( c + 1 ) \
        * r8_beta ( y + 1,  c - y + 1 ) * r8_beta ( a, b ) )
      cdf = cdf + pdf

  elif ( c <= x ):

    cdf = 1.0

  return cdf

def beta_binomial_cdf_test ( rng ):

#*****************************************************************************80
#
## beta_binomial_cdf_test() tests beta_binomial_cdf(), beta_binomial_cdf_inv(), beta_binomial_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'beta_binomial_cdf_test():' )
  print ( '  beta_binomial_cdf() evaluates the Beta Binomial CDF' )
  print ( '  beta_binomial_cdf_inv() inverts the Beta Binomial CDF.' )
  print ( '  beta_binomial_pdf() evaluates the Beta Binomial PDF' )

  a = 2.0
  b = 3.0
  c = 4

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )

  check = beta_binomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'beta_binomial_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = beta_binomial_sample ( a, b, c, rng )

    pdf = beta_binomial_pdf ( x, a, b, c )

    cdf = beta_binomial_cdf ( x, a, b, c )

    x2 = beta_binomial_cdf_inv ( cdf, a, b, c )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def beta_binomial_check ( a, b, c ):

#*****************************************************************************80
#
## beta_binomial_check() checks the parameters of the Beta Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= C.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are OK.
#
  if ( a <= 0.0 ):
    print ( '' )
    print ( 'beta_binomial_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False
    return check

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'beta_binomial_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False
    return check

  if ( c < 0 ):
    print ( '' )
    print ( 'beta_binomial_check(): Fatal error!' )
    print ( '  C < 0.' )
    check = False
    return check

  check = True

  return check

def beta_binomial_mean ( a, b, c ):

#*****************************************************************************80
#
## beta_binomial_mean() returns the mean of the Beta Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= N.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = c * a / ( a + b )

  return mean

def beta_binomial_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## beta_binomial_pdf() evaluates the Beta Binomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = Beta(A+X,B+C-X)
#      / ( (C+1) * Beta(X+1,C-X+1) * Beta(A,B) )  for 0 <= X <= C.
#
#    This PDF can be reformulated as:
#
#      The beta binomial probability density function for X successes
#      out of N trials is
#
#      PDF2(X)( N, MU, THETA ) =
#        C(N,X) * Product ( 0 <= R <= X - 1 ) ( MU + R * THETA )
#               * Product ( 0 <= R <= N - X - 1 ) ( 1 - MU + R * THETA )
#               / Product ( 0 <= R <= N - 1 )  ( 1 + R * THETA )
#
#      where
#
#        C(N,X) is the combinatorial coefficient
#        MU is the expectation of the underlying Beta distribution
#        THETA is a shape parameter.
#
#      A THETA value of 0 ( or A+B --> Infinity ) results in the binomial
#      distribution:
#
#        PDF2(X) ( N, MU, 0 ) = C(N,X) * MU**X * ( 1 - MU )**(N-X)
#
#    Given A, B, C for PDF, then the equivalent PDF2 has:
#
#      N     = C
#      MU    = A / ( A + B )
#      THETA = 1 / ( A + B )
#
#    Given N, MU, THETA for PDF2, the equivalent PDF has:
#
#      A = MU / THETA
#      B = ( 1 - MU ) / THETA
#      C = N
#
#    beta_binomial_pdf(X)(1,1,C) = uniform_discrete_pdf(X)(0,C-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0 ):

    pdf = 0.0

  elif ( x <= c ):

    pdf = r8_beta ( a + x, b + c - x ) \
      / ( ( c + 1 ) * r8_beta ( x + 1, c - x + 1 ) * r8_beta ( a, b ) )

  elif ( c < x ):

    pdf = 0.0

  return pdf

def beta_binomial_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## beta_binomial_sample() samples the Beta Binomial CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= C.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = beta_binomial_cdf_inv ( cdf, a, b, c )

  return x

def beta_binomial_sample_test ( rng ):

#*****************************************************************************80
#
## beta_binomial_sample_test() tests beta_binomial_mean(), beta_binomial_sample(), beta_binomial_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'beta_binomial_sample_test():' )
  print ( '  beta_binomial_mean() computes the Beta Binomial mean' )
  print ( '  beta_binomial_sample() samples the Beta Binomial distribution' )
  print ( '  beta_binomial_variance() computes the Beta Binomial variance.' )

  a = 2.0
  b = 3.0
  c = 4

  check = beta_binomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'beta_binomial_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = beta_binomial_mean ( a, b, c )
  variance = beta_binomial_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
 
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = beta_binomial_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def beta_binomial_variance ( a, b, c ):

#*****************************************************************************80
#
## beta_binomial_variance() returns the variance of the Beta Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    integer C, a parameter of the PDF.
#    0 <= C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = c * a * b * ( a + b + c ) / ( ( a + b ) ** 2 * ( a + b + 1.0 ) )

  return variance

def beta_cdf_values ( n_data ):

#*****************************************************************************80
#
## beta_cdf_values() returns some values of the Beta CDF.
#
#  Discussion:
#
#    The incomplete Beta function may be written
#
#      beta_inc(A,B,X) = Integral (0 to X) T^(A-1) * (1-T)^(B-1) dT
#                      / Integral (0 to 1) T^(A-1) * (1-T)^(B-1) dT
#
#    Thus,
#
#      beta_inc(A,B,0.0) = 0.0;
#      beta_inc(A,B,1.0) = 1.0
#
#    The incomplete Beta function is also sometimes called the
#    "modified" Beta function, or the "normalized" Beta function
#    or the Beta CDF (cumulative density function).
#
#    In Mathematica, the function can be evaluated by:
#
#      BETA[X,A,B] / BETA[A,B]
#
#    The function can also be evaluated by using the Statistics package:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = BetaDistribution [ a, b ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
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
#    Karl Pearson,
#    Tables of the Incomplete Beta Function,
#    Cambridge University Press, 1968.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real A, B, the parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 45

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.5E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     30.0E+00, \
     30.0E+00, \
     40.0E+00, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.2E+01, \
      0.3E+01, \
      0.4E+01, \
      0.5E+01, \
      1.30625, \
      1.30625, \
      1.30625 ))

  b_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.0E+00, \
      0.5E+00, \
      5.0E+00, \
      5.0E+00, \
     10.0E+00, \
      5.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.2E+01, \
     0.3E+01, \
     0.4E+01, \
     0.5E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
    11.7562, \
    11.7562, \
    11.7562 ))

  f_vec = np.array ( ( \
     0.6376856085851985E-01, \
     0.2048327646991335E+00, \
     0.1000000000000000E+01, \
     0.0000000000000000E+00, \
     0.5012562893380045E-02, \
     0.5131670194948620E-01, \
     0.2928932188134525E+00, \
     0.5000000000000000E+00, \
     0.2800000000000000E-01, \
     0.1040000000000000E+00, \
     0.2160000000000000E+00, \
     0.3520000000000000E+00, \
     0.5000000000000000E+00, \
     0.6480000000000000E+00, \
     0.7840000000000000E+00, \
     0.8960000000000000E+00, \
     0.9720000000000000E+00, \
     0.4361908850559777E+00, \
     0.1516409096347099E+00, \
     0.8978271484375000E-01, \
     0.1000000000000000E+01, \
     0.5000000000000000E+00, \
     0.4598773297575791E+00, \
     0.2146816102371739E+00, \
     0.9507364826957875E+00, \
     0.5000000000000000E+00, \
     0.8979413687105918E+00, \
     0.2241297491808366E+00, \
     0.7586405487192086E+00, \
     0.7001783247477069E+00, \
     0.5131670194948620E-01, \
     0.1055728090000841E+00, \
     0.1633399734659245E+00, \
     0.2254033307585166E+00, \
     0.3600000000000000E+00, \
     0.4880000000000000E+00, \
     0.5904000000000000E+00, \
     0.6723200000000000E+00, \
     0.2160000000000000E+00, \
     0.8370000000000000E-01, \
     0.3078000000000000E-01, \
     0.1093500000000000E-01, \
     0.918884684620518, \
     0.21052977489419, \
     0.1824130512500673 ) )

  x_vec = np.array ( ( \
     0.01E+00, \
     0.10E+00, \
     1.00E+00, \
     0.00E+00, \
     0.01E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     0.50E+00, \
     0.90E+00, \
     0.50E+00, \
     1.00E+00, \
     0.50E+00, \
     0.80E+00, \
     0.60E+00, \
     0.80E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.70E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.225609, \
     0.0335568, \
     0.0295222  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def beta_cdf_values_test ( ):

#*****************************************************************************80
#
## beta_cdf_values_test() tests beta_cdf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'beta_cdf_values_test():' )
  print ( '  beta_cdf_values() stores values of the Beta function.' )
  print ( '' )
  print ( '      A         B         X        beta_cdf(A,B,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = beta_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16g' % ( a, b, x, f ) )

  return

def beta_inc ( a, b, x ):

#*****************************************************************************80
#
## beta_inc() returns the value of the incomplete Beta function.
#
#  Discussion:
#
#    This calculation requires an iteration.  In some cases, the iteration
#    may not converge rapidly, or may become inaccurate.
#
#    beta_inc(A,B,X)
#
#      =   Integral ( 0 <= T <= X ) T^(A-1) (1-T)^(B-1) dT
#        / Integral ( 0 <= T <= 1 ) T^(A-1) (1-T)^(B-1) dT
#
#      =   Integral ( 0 <= T <= X ) T^(A-1) (1-T)^(B-1) dT
#        / BETA(A,B)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by Majumder, Bhattacharjee.
#    This version by John Burkardt.
#
#  Reference:
#
#    Majumder and Bhattacharjee,
#    Algorithm AS63,
#    Applied Statistics,
#    1973, volume 22, number 3.
#
#  Input:
#
#    A, B, the parameters of the function.
#    0.0 < A,
#    0.0 < B.
#
#    real X, the argument of the function.
#    Normally, 0.0 <= X <= 1.0.
#
#  Output:
#
#    beta_inc, the value of the function.
#
  import numpy as np

  it_max = 1000
  tol = 1.0E-07

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'beta_inc(): Fatal error!' )
    print ( '  A <= 0.' )
    raise Exception ( 'beta_inc(): Fatal error!' )

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'beta_inc(): Fatal error!' )
    print ( '  B <= 0.' )
    raise Exception ( 'beta_inc(): Fatal error!' )

  if ( x <= 0.0 ):
    value = 0.0
    return value
  elif ( 1.0 <= x ):
    value = 1.0
    return value
#
#  Change tail if necessary and determine S.
#
  psq = a + b

  if ( a < ( a + b ) * x ):
    xx = 1.0 - x
    cx = x
    pp = b
    qq = a
    indx = 1
  else:
    xx = x
    cx = 1.0 - x
    pp = a
    qq = b
    indx = 0

  term = 1.0
  i = 1
  value = 1.0

  ns = np.floor ( qq + cx * ( a + b ) )
#
#  Use Soper's reduction formulas.
#
  rx = xx / cx

  temp = qq - i
  if ( ns == 0 ):
    rx = xx

  it = 0

  while ( True ):

    it = it + 1

    if ( it_max < it ):
      print ( '' )
      print ( 'beta_inc(): Fatal error!' )
      print ( '  Maximum number of iterations exceeded!' )
      print ( '  IT_max = %d' % ( it_max ) )
      raise Exception ( 'beta_inc(): Fatal error!' )

    term = term * temp * rx / ( pp + i )
    value = value + term
    temp = abs ( term )

    if ( temp <= tol and temp <= tol * value ):
      break

    i = i + 1
    ns = ns - 1

    if ( 0 <= ns ):
      temp = qq - i
      if ( ns == 0 ):
        rx = xx
    else:
      temp = psq
      psq = psq + 1.0
#
#  Finish calculation.
#
  value = value * np.exp ( pp * np.log ( xx ) \
    + ( qq - 1.0 ) * np.log ( cx ) ) \
    / ( r8_beta ( a, b ) * pp )

  if ( indx ):
    value = 1.0 - value

  return value

def beta_inc_test ( ):

#*****************************************************************************80
#
## beta_inc_test() tests beta_inc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'beta_inc_test():' )
  print ( '  beta_inc() evaluates the normalized incomplete Beta' )
  print ( '  function beta_inc(A,B,X).' )
  print ( '' )
  print ( '      A           B           X               Exact F     beta_inc(A,B,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = beta_inc ( a, b, x )

    print ( '  %10g  %10g  %10g  %14g  %14g' % ( a, b, x, fx, fx2 ) )

  return

def beta_inc_values ( n_data ):

#*****************************************************************************80
#
## beta_inc_values() returns some values of the incomplete Beta function.
#
#  Discussion:
#
#    The incomplete Beta function may be written
#
#      beta_inc(A,B,X) = Integral (0 to X) T^(A-1) * (1-T)^(B-1) dT
#                      / Integral (0 to 1) T^(A-1) * (1-T)^(B-1) dT
#
#    Thus,
#
#      beta_inc(A,B,0.0) = 0.0;
#      beta_inc(A,B,1.0) = 1.0
#
#    The incomplete Beta function is also sometimes called the
#    "modified" Beta function, or the "normalized" Beta function
#    or the Beta CDF (cumulative density function).
#
#    In Mathematica, the function can be evaluated by:
#
#      BETA[X,A,B] / BETA[A,B]
#
#    The function can also be evaluated by using the Statistics package:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = BetaDistribution [ a, b ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
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
#    Karl Pearson,
#    Tables of the Incomplete Beta Function,
#    Cambridge University Press, 1968.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real A, B, the parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 45

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.5E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     30.0E+00, \
     30.0E+00, \
     40.0E+00, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.2E+01, \
      0.3E+01, \
      0.4E+01, \
      0.5E+01, \
      1.30625, \
      1.30625, \
      1.30625 ))

  b_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.0E+00, \
      0.5E+00, \
      5.0E+00, \
      5.0E+00, \
     10.0E+00, \
      5.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.2E+01, \
     0.3E+01, \
     0.4E+01, \
     0.5E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
    11.7562, \
    11.7562, \
    11.7562 ))

  f_vec = np.array ( ( \
     0.6376856085851985E-01, \
     0.2048327646991335E+00, \
     0.1000000000000000E+01, \
     0.0000000000000000E+00, \
     0.5012562893380045E-02, \
     0.5131670194948620E-01, \
     0.2928932188134525E+00, \
     0.5000000000000000E+00, \
     0.2800000000000000E-01, \
     0.1040000000000000E+00, \
     0.2160000000000000E+00, \
     0.3520000000000000E+00, \
     0.5000000000000000E+00, \
     0.6480000000000000E+00, \
     0.7840000000000000E+00, \
     0.8960000000000000E+00, \
     0.9720000000000000E+00, \
     0.4361908850559777E+00, \
     0.1516409096347099E+00, \
     0.8978271484375000E-01, \
     0.1000000000000000E+01, \
     0.5000000000000000E+00, \
     0.4598773297575791E+00, \
     0.2146816102371739E+00, \
     0.9507364826957875E+00, \
     0.5000000000000000E+00, \
     0.8979413687105918E+00, \
     0.2241297491808366E+00, \
     0.7586405487192086E+00, \
     0.7001783247477069E+00, \
     0.5131670194948620E-01, \
     0.1055728090000841E+00, \
     0.1633399734659245E+00, \
     0.2254033307585166E+00, \
     0.3600000000000000E+00, \
     0.4880000000000000E+00, \
     0.5904000000000000E+00, \
     0.6723200000000000E+00, \
     0.2160000000000000E+00, \
     0.8370000000000000E-01, \
     0.3078000000000000E-01, \
     0.1093500000000000E-01, \
     0.918884684620518, \
     0.21052977489419, \
     0.1824130512500673 ) )

  x_vec = np.array ( ( \
     0.01E+00, \
     0.10E+00, \
     1.00E+00, \
     0.00E+00, \
     0.01E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     0.50E+00, \
     0.90E+00, \
     0.50E+00, \
     1.00E+00, \
     0.50E+00, \
     0.80E+00, \
     0.60E+00, \
     0.80E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.70E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.225609, \
     0.0335568, \
     0.0295222  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def beta_inc_values_test ( ):

#*****************************************************************************80
#
## beta_inc_values_test() tests beta_inc_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'beta_inc_values_test():' )
  print ( '  beta_inc_values() stores values of the BETA function.' )
  print ( '' )
  print ( '      A         B         X        beta_inc(A,B,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16g' % ( a, b, x, f ) )

  return

def beta_cdf ( x, a, b ):

#*****************************************************************************80
#
## beta_cdf() evaluates the Beta CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= 0.0 ):
    cdf = 0.0
  elif ( x <= 1.0 ):
    cdf = beta_inc ( a, b, x )
  else:
    cdf = 1.0

  return cdf

def beta_cdf_inv ( cdf, p, q ):

#*****************************************************************************80
#
## beta_cdf_inv() computes inverse of the incomplete Beta function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by GW Cran, KJ Martin, GE Thomas.
#    This version by John Burkardt.
#
#  Reference:
#
#    GW Cran, KJ Martin, GE Thomas,
#    Remark AS R19 and Algorithm AS 109:
#    A Remark on Algorithms AS 63: The Incomplete Beta Integral
#    and AS 64: Inverse of the Incomplete Beta Integeral,
#    Applied Statistics,
#    Volume 26, Number 1, 1977, pages 111-114.
#
#  Input:
#
#    real P, Q, the parameters of the incomplete
#    Beta function.
#
#    real CDF, the value of the incomplete Beta
#    function.  0 <= CDF <= 1.
#
#  Output:
#
#    real VALUE, the argument of the Beta CDF which produces 
#    the value CDF.
#
#  Local:
#
#    real SAE, the most negative decimal exponent
#    which does not cause an underflow.
#
  import numpy as np
  from scipy.special import gamma

  sae = -37.0

  fpu = 10.0 ** sae
#
#  Test for admissibility of parameters.
#
  if ( p <= 0.0 ):
    print ( '' )
    print ( 'beta_cdf_inv(): Fatal error!' )
    print ( '  P <= 0.' )
    raise Exception ( 'beta_cdf_inv(): Fatal error!' )

  if ( q <= 0.0 ):
    print ( '' )
    print ( 'beta_cdf_inv(): Fatal error!' )
    print ( '  Q <= 0.' )
    raise Exception ( 'beta_cdf_inv(): Fatal error!' )

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'beta_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'beta_cdf_inv(): Fatal error!' )
#
#  If the value is easy to determine, return immediately.
#
  if ( cdf == 0.0 ):
    value = 0.0
    return value

  if ( cdf == 1.0 ):
    value = 1.0
    return value

  beta_log = np.log ( gamma ( p ) ) + np.log ( gamma ( q ) ) \
    - np.log ( gamma ( p + q ) )
#
#  Change tail if necessary.
#
  if ( 0.5 < cdf ):
    a = 1.0 - cdf
    pp = q
    qq = p
    indx = 1
  else:
    a = cdf
    pp = p
    qq = q
    indx = 0
#
#  Calculate the initial approximation.
#
  r = np.sqrt ( - np.log ( a * a ) )

  y = r - ( 2.30753 + 0.27061 * r ) \
    / ( 1.0 + ( 0.99229 + 0.04481 * r ) * r )

  if ( 1.0 < pp and 1.0 < qq ):

    r = ( y * y - 3.0 ) / 6.0
    s = 1.0 / ( pp + pp - 1.0 )
    t = 1.0 / ( qq + qq - 1.0 )
    h = 2.0 / ( s + t )
    w = y * np.sqrt ( h + r ) / h - ( t - s ) \
      * ( r + 5.0 / 6.0 - 2.0 / ( 3.0 * h ) )
    value = pp / ( pp + qq * np.exp ( w + w ) )

  else:

    r = qq + qq
    t = 1.0 / ( 9.0 * qq )
    t = r * ( 1.0 - t + y * np.sqrt ( t ) ) ** 3

    if ( t <= 0.0 ):
      value = 1.0 - np.exp ( ( np.log ( ( 1.0 - a ) * qq ) + beta_log ) / qq )
    else:

      t = ( 4.0 * pp + r - 2.0 ) / t

      if ( t <= 1.0 ):
        value = np.exp ( ( np.log ( a * pp ) + beta_log ) / pp )
      else:
        value = 1.0 - 2.0 / ( t + 1.0 )
#
#  Solve for X by a modified Newton-Raphson method.
#
  r = 1.0 - pp
  t = 1.0 - qq
  yprev = 0.0
  sq = 1.0
  prev = 1.0

  if ( value < 0.0001 ):
    value = 0.0001

  if ( 0.9999 < value ):
    value = 0.9999

  iex = max ( - 5.0 / pp / pp - 1.0 / a ** 0.2 - 13.0, sae )

  acu = 10.0 ** iex

  while ( True ):

    y = beta_inc ( pp, qq, value )

    xin = value
    y = ( y - a ) * np.exp ( beta_log + r * np.log ( xin ) + t * np.log ( 1.0 - xin ) )

    if ( y * yprev <= 0.0 ):
      prev = max ( sq, fpu )

    g = 1.0

    while ( True ):

      while ( True ):

        adj = g * y
        sq = adj * adj

        if ( sq < prev ):

          tx = value - adj

          if ( 0.0 <= tx and tx <= 1.0 ):
            break

        g = g / 3.0

      if ( prev <= acu ):
        if ( indx ):
          value = 1.0 - value
        return value

      if ( y * y <= acu ):
        if ( indx ):
          value = 1.0 - value
        return value

      if ( tx != 0.0 and tx != 1.0 ):
        break

      g = g / 3.0

    if ( tx == value ):
      break
 
    value = tx
    yprev = y

  if ( indx ):
    value = 1.0 - value

  return value

def beta_cdf_test ( rng ):

#*****************************************************************************80
#
## beta_cdf_test() tests beta_cdf(), beta_cdf_inv(), beta_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'beta_cdf_test():' )
  print ( '  beta_cdf() evaluates the Beta CDF' )
  print ( '  beta_cdf_inv() inverts the Beta CDF.' )
  print ( '  beta_pdf() evaluates the Beta PDF' )

  a = 12.0
  b = 12.0

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  check = beta_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'beta_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '        A               B               X               ' ),
  print ( 'PDF             CDF             CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = beta_sample ( a, b, rng )

    pdf = beta_pdf ( x, a, b )

    cdf = beta_cdf ( x, a, b )

    x2 = beta_cdf_inv ( cdf, a, b )

    print ( '%14g  %14g  %14g  %14g  %14g  %14g' % ( a, b, x, pdf, cdf, x2 ) )

  return

def beta_check ( a, b ):

#*****************************************************************************80
#
## beta_check() checks the parameters of the Beta PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  if ( a <= 0.0 ):
    print ( '' )
    print ( 'beta_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False
    return check

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'beta_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False
    return check

  check = True

  return check

def beta_mean ( a, b ):

#*****************************************************************************80
#
## beta_mean() returns the mean of the Beta PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a / ( a + b )

  return mean

def beta_pdf ( x, a, b ):

#*****************************************************************************80
#
## beta_pdf() evaluates the Beta PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = X^(A-1) * (1-X)^(B-1) / BETA(A,B).
#
#    A = B = 1 yields the Uniform distribution on [0,1].
#    A = B = 1/2 yields the Arcsin distribution.
#        B = 1 yields the power function distribution.
#    A = B -> Infinity tends to the Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0.0 or 1.0 < x ):
    pdf = 0.0
  else:
    pdf = x ** ( a - 1.0 ) * ( 1.0 - x ) ** ( b - 1.0 ) / r8_beta ( a, b )

  return pdf

def beta_sample ( a, b, rng ):

#*****************************************************************************80
#
## beta_sample() samples the Beta PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    William Kennedy and James Gentle,
#    Algorithm BN,
#    Statistical Computing,
#    Dekker, 1980.
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  mu = ( a - 1.0 ) / ( a + b - 2.0 )
  stdev = 0.5 / np.sqrt ( a + b - 2.0 )

  while ( True ):

    y = rng.standard_normal ( )
 
    x = mu + stdev * y

    if ( x < 0.0 or 1.0 < x ):
      continue

    u = rng.random ( )

    test =     ( a - 1.0 )     * np.log (         x   / ( a - 1.0 ) ) \
             + ( b - 1.0 )     * np.log ( ( 1.0 - x ) / ( b - 1.0 ) ) \
             + ( a + b - 2.0 ) * np.log ( a + b - 2.0 ) + 0.5 * y ** 2

    if ( np.log ( u ) <= test ):
      break

  return x

def beta_sample_test ( rng ):

#*****************************************************************************80
#
## beta_sample_test() tests beta_mean(), beta_sample(), beta_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'beta_sample_test():' )
  print ( '  beta_mean() computes the Beta mean' )
  print ( '  beta_sample() samples the Beta distribution' )
  print ( '  beta_variance() computes the Beta variance.' )

  a = 2.0
  b = 3.0

  check = beta_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'beta_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = beta_mean ( a, b )
  variance = beta_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = beta_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def beta_variance ( a, b ):

#*****************************************************************************80
#
## beta_variance() returns the variance of the Beta PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( a * b ) / ( ( a + b ) ** 2 * ( 1.0 + a + b ) )

  return variance

def beta_values ( n_data ):

#*****************************************************************************80
#
## beta_values() returns some values of the Beta function.
#
#  Discussion:
#
#    Beta(X,Y) = ( Gamma(X) * Gamma(Y) ) / Gamma(X+Y)
#
#    Both X and Y must be greater than 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      Beta[X,Y]
#
#  Properties:
#
#    Beta(X,Y) = Beta(Y,X).
#    Beta(X,Y) = Integral ( 0 <= T <= 1 ) T^(X-1) (1-T)^(Y-1) dT.
#    Beta(X,Y) = Gamma(X) * Gamma(Y) / Gamma(X+Y)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real X, Y, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
     0.5000000000000000E+01, \
     0.2500000000000000E+01, \
     0.1666666666666667E+01, \
     0.1250000000000000E+01, \
     0.5000000000000000E+01, \
     0.2500000000000000E+01, \
     0.1000000000000000E+01, \
     0.1666666666666667E+00, \
     0.3333333333333333E-01, \
     0.7142857142857143E-02, \
     0.1587301587301587E-02, \
     0.2380952380952381E-01, \
     0.5952380952380952E-02, \
     0.1984126984126984E-02, \
     0.7936507936507937E-03, \
     0.3607503607503608E-03, \
     0.8325008325008325E-04 ) )

  x_vec = np.array ( ( \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  y_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.2E+00, \
     0.4E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, f

def beta_values_test ( ):

#*****************************************************************************80
#
## beta_values_test() tests beta_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'beta_values_test():' )
  print ( '  beta_values() stores values of the Beta function.' )
  print ( '' )
  print ( '      X         Y         BETA(X,Y)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( x, y, f ) )

  return

def binomial_cdf ( x, a, b ):

#*****************************************************************************80
#
## binomial_cdf() evaluates the Binomial CDF.
#
#  Discussion:
#
#    CDF(X)(A,B) is the probability of at most X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    A sequence of trials with fixed probability of success on
#    any trial is known as a sequence of Bernoulli trials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the desired number of successes.
#    0 <= X <= A.
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  from scipy.special import comb

  if ( x < 0 ):

    cdf = 0.0

  elif ( a <= x ):

    cdf = 1.0

  elif ( b == 0.0 ):

    cdf = 1.0

  elif ( b == 1.0 ):

    cdf = 0.0

  else:

    cdf = 0.0

    for j in range ( 0, x + 1 ):

      cnk = comb ( a, j )

      pr = cnk * b ** j * ( 1.0 - b ) ** ( a - j )

      cdf = cdf + pr

  return cdf

def binomial_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## binomial_cdf_inv() inverts the Binomial CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    integer X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'binomial_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'binomial_cdf_inv(): Fatal error!' )

  cdf2 = 0.0

  for x2 in range ( 0, a + 1 ):

    pdf = binomial_pdf ( x2, a, b )

    cdf2 = cdf2 + pdf

    if ( cdf <= cdf2 ):
      x = x2
      return x

  return x

def binomial_cdf_test ( rng ):

#*****************************************************************************80
#
## binomial_cdf_test() tests binomial_cdf(), binomial_cdf_inv(), binomial_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'binomial_cdf_test():' )
  print ( '  binomial_cdf() evaluates the Binomial CDF' )
  print ( '  binomial_cdf_inv() inverts the Binomial CDF.' )
  print ( '  binomial_pdf() evaluates the Binomial PDF' )

  a = 5
  b = 0.65

  check = binomial_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'binomial_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = binomial_sample ( a, b, rng )

    pdf = binomial_pdf ( x, a, b )

    cdf = binomial_cdf ( x, a, b )

    x2 = binomial_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def binomial_check ( a, b ):

#*****************************************************************************80
#
## binomial_check() checks the parameter of the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  if ( a < 1 ):
    print ( '' )
    print ( 'binomial_check(): Fatal error!' )
    print ( '  A < 1.' )
    check = False
    return check

  if ( b < 0.0 or 1.0 < b ):
    print ( '' )
    print ( 'binomial_check(): Fatal error!' )
    print ( '  B < 0 or 1 < B.' )
    check = False
    return check

  check = True

  return check

def binomial_mean ( a, b ):

#*****************************************************************************80
#
## binomial_mean() returns the mean of the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    real MEAN, the expected value of the number of
#    successes in A trials.
#
  mean = a * b

  return mean

def binomial_pdf ( x, a, b ):

#*****************************************************************************80
#
## binomial_pdf() evaluates the Binomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability of exactly X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    PDF(X)(A,B) = C(N,X) * B^X * ( 1.0 - B )^( A - X )
#
#    binomial_pdf(X)(1,B) = bernoulli_pdf(X)(B).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the desired number of successes.
#    0 <= X <= A.
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  from scipy.special import comb

  if ( a < 1 ):

    pdf = 0.0

  elif ( x < 0 or a < x ):

    pdf = 0.0

  elif ( b == 0.0 ):

    if ( x == 0 ):
      pdf = 1.0
    else:
      pdf = 0.0

  elif ( b == 1.0 ):

    if ( x == a ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    cnk = float ( comb ( a, x ) )

    pdf = cnk * b ** x * ( 1.0 - b ) ** ( a - x )

  return pdf

def binomial_sample ( a, b, rng ):

#*****************************************************************************80
#
## binomial_sample() samples the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Kennedy and James Gentle,
#    Algorithm BU,
#    Statistical Computing,
#    Dekker, 1980.
#
#  Input:
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  x = 0

  for i in range ( 0, a ):

    u = rng.random ( )

    if ( u <= b ):
      x = x + 1

  return x

def binomial_sample_test ( rng ):

#*****************************************************************************80
#
## binomial_sample_test() tests binomial_mean(), binomial_sample(), binomial_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'binomial_sample_test():' )
  print ( '  binomial_mean() computes the Binomial mean' )
  print ( '  binomial_sample() samples the Binomial distribution' )
  print ( '  binomial_variance() computes the Binomial variance.' )

  a = 5
  b = 0.30

  check = binomial_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'binomial_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = binomial_mean ( a, b )
  variance = binomial_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = binomial_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def binomial_variance ( a, b ):

#*****************************************************************************80
#
## binomial_variance() returns the variance of the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#    1 <= A.
#
#    real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a * b * ( 1.0 - b )

  return variance

def birthday_cdf ( n ):

#*****************************************************************************80
#
## birthday_cdf() returns the Birthday Concurrence CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of people whose birthdays have been
#    disclosed.
#
#  Output:
#
#    real CDF, the probability of at least one matching birthday
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
## birthday_cdf_inv() inverts the Birthday Concurrence CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the probability that at least
#    two of the N people have matching birthays.
#
#  Output:
#
#    integer N, the corresponding number of people whose
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

def birthday_cdf_test ( rng ):

#*****************************************************************************80
#
## birthday_cdf_test() tests birthday_cdf(), birthday_cdf_inv(), birthday_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'birthday_cdf_test():' )
  print ( '  birthday_cdf() evaluates the Birthday CDF' )
  print ( '  birthday_cdf_inv() inverts the Birthday CDF.' )
  print ( '  birthday_pdf() evaluates the Birthday PDF' )

  print ( '' )
  print ( '       N            PDF           CDF            CDF_inv' )
  print ( '' )

  for n in range ( 1, 31 ):

    pdf = birthday_pdf ( n )

    cdf = birthday_cdf ( n )

    n2 = birthday_cdf_inv ( cdf )

    print ( '  %8d  %14g  %14g  %8d' % ( n, pdf, cdf, n2 ) )

  return

def birthday_pdf ( n ):

#*****************************************************************************80
#
## birthday_pdf() returns the Birthday Concurrence PDF.
#
#  Discussion:
#
#    The probability is the probability that the N-th person is the
#    first one to match a birthday with someone earlier.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of people whose birthdays have been
#    disclosed.
#
#  Output:
#
#    real PDF, the probability that the N-th person
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

def birthday_sample ( n, rng ):

#*****************************************************************************80
#
## birthday_sample() samples the Birthday Concurrence PDF.
#
#  Discussion:
#
#    The probability is the probability that the N-th person is the
#    first one to match a birthday with someone earlier.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of people whose birthdays have been
#    disclosed.
#
#  Output:
#
#    integer VALUE,
#    * 1 if the first N-1 people had distinct
#      birthdays, but person N had a birthday in common with a previous person,
#    * 0 otherwise.
#
  import numpy as np

  if ( n < 1 ):
    value = 0
    return value
#
#  Choose N birthdays at random.
#
  b = rng.integers ( low = 1, high = 365, size = n, endpoint = True )
#
#  Are the first N-1 birthdays unique?
#
  u1 = i4vec_unique_count ( n - 1, b )

  if ( u1 < n - 1 ):
    value = 0
    return value
#
#  Does the N-th birthday match an earlier one?
#
  u2 = i4vec_unique_count ( n, b )

  if ( u2 == n - 1 ):
    value = 1
  else:
    value = 0

  return value

def birthday_sample_test ( rng ):

#*****************************************************************************80
#
## birthday_sample_test() tests birthday_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
#
#  Although other implementations use 10,000 samples, the Python code
#  is too slow for me to wait.
#
  nsample = 10000
  nsample = 1000

  print ( '' )
  print ( 'birthday_sample_test():' )
  print ( '  birthday_sample() samples the Birthday distribution.' )
  print ( '' )
  print ( '   N            Mean           PDF' )
  print ( '' )

  for n in range ( 10, 41 ):

    x = np.zeros ( nsample )
    for i in range ( 0, nsample ):
      x[i] = birthday_sample ( n, rng )

    mean = np.mean ( x )
    pdf = birthday_pdf ( n )

    print ( '  %2d  %14g  %14g' % ( n, mean, pdf ) )

  return

def bradford_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## bradford_cdf_inv() inverts the Bradford CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'bradford_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'bradford_cdf_inv(): Fatal error!' )

  if ( cdf <= 0.0 ):
    x = a
  elif ( cdf < 1.0 ):
    x = a + ( b - a ) * ( ( c + 1.0 ) ** cdf - 1.0 ) / c
  elif ( 1.0 <= cdf ):
    x = b

  return x

def bradford_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## bradford_cdf() evaluates the Bradford CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= a ):
    cdf = 0.0
  elif ( x <= b ):
    cdf = np.log ( 1.0 + c * ( x - a ) / ( b - a ) ) / np.log ( c + 1.0 )
  elif ( b < x ):
    cdf = 1.0

  return cdf

def bradford_cdf_test ( rng ):

#*****************************************************************************80
#
## bradford_cdf_test() tests bradford_cdf(), bradford_cdf_inv(), bradford_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'bradford_cdf_test():' )
  print ( '  bradford_cdf() evaluates the Bradford CDF' )
  print ( '  bradford_cdf_inv() inverts the Bradford CDF.' )
  print ( '  bradford_pdf() evaluates the Bradford PDF' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = bradford_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'bradford_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = bradford_sample ( a, b, c, rng )

    pdf = bradford_pdf ( x, a, b, c )

    cdf = bradford_cdf ( x, a, b, c )

    x2 = bradford_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def bradford_check ( a, b, c ):

#*****************************************************************************80
#
## bradford_check() checks the parameters of the Bradford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( b <= a ):
    print ( '' )
    print ( 'bradford_check(): Fatal error!' )
    print ( '  B <= A.' )
    check = False
  elif ( c <= 0.0 ):
    print ( '' )
    print ( 'bradford_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def bradford_mean ( a, b, c ):

#*****************************************************************************80
#
## bradford_mean() returns the mean of the Bradford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = ( c * ( b - a ) + np.log ( c + 1.0 ) * ( a * ( c + 1.0 ) - b ) ) \
    / ( c * np.log ( c + 1.0 ) )

  return mean

def bradford_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## bradford_pdf() evaluates the Bradford PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) =
#      C / ( ( C * ( X - A ) + B - A ) * log ( C + 1 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= a ):
    pdf = 0.0
  elif ( x <= b ):
    pdf = c / ( ( c * ( x - a ) + b - a ) * np.log ( c + 1.0 ) )
  elif ( b < x ):
    pdf = 0.0

  return pdf

def bradford_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## bradford_sample() samples the Bradford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = a + ( b - a ) * ( ( c + 1.0 ) ** cdf - 1.0 ) / c

  return x

def bradford_sample_test ( rng ):

#*****************************************************************************80
#
## bradford_sample_test() tests bradford_mean(), bradford_sample(), bradford_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'bradford_sample_test():' )
  print ( '  bradford_mean() computes the Bradford mean' )
  print ( '  bradford_sample() samples the Bradford distribution' )
  print ( '  bradford_variance() computes the Bradford variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = bradford_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'bradford_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = bradford_mean ( a, b, c )
  variance = bradford_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = bradford_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def bradford_variance ( a, b, c ):
 
#*****************************************************************************80
#
## bradford_variance() returns the variance of the Bradford PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A < B,
#    0.0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = ( b - a ) ** 2 * \
    ( c * ( np.log ( c + 1.0 ) - 2.0 ) + 2.0 * np.log ( c + 1.0 ) ) \
    / ( 2.0 * c * ( np.log ( c + 1.0 ) ) ** 2 )

  return variance

def buffon_box_pdf ( a, b, l ):

#*****************************************************************************80
#
## buffon_box_pdf() evaluates the Buffon Box PDF.
#
#  Discussion:
#
#    In the Buffon-Laplace needle experiment, we suppose that the plane has been
#    tiled into a grid of rectangles of width A and height B, and that a
#    needle of length L is dropped "at random" onto this grid.  
# 
#    We may assume that one end, the "eye" of the needle falls at the point
#    (X1,Y1), taken uniformly at random in the cell [0,A]x[0,B].
#
#    ANGLE, the angle that the needle makes is taken to be uniformly random.
#    The point of the needle, (X2,Y2), therefore lies at
#
#      (X2,Y2) = ( X1+L*cos(ANGLE), Y1+L*sin(ANGLE) )
#
#    The needle will have crossed at least one grid line if any of the 
#    following are true:
#
#      X2 <= 0, A <= X2, Y2 <= 0, B <= Y2.
#
#    If L is larger than sqrt ( A*A + B*B ), then the needle will
#    cross every time, and the computation is uninteresting.  However, if
#    L is smaller than this limit, then the probability of a crossing on
#    a single trial is
#
#      P(L,A,B) = ( 2 * L * ( A + B ) - L * L ) / ( PI * A * B )
#
#    and therefore, a record of the number of hits for a given number of
#    trials can be used as a very roundabout way of estimating PI.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sudarshan Raghunathan,
#    Making a Supercomputer Do What You Want: High Level Tools for 
#    Parallel Programming,
#    Computing in Science and Engineering,
#    Volume 8, Number 5, September/October 2006, pages 70-80.
#
#  Input:
#
#    real A, B, the horizontal and vertical dimensions
#    of each cell of the grid.  0 <= A, 0 <= B.
#
#    real L, the length of the needle.
#    0 <= L <= min ( A, B ).
#
#  Output:
#
#    real PDF, the PDF.
#
  import numpy as np

  if ( a < 0.0 ):
    print ( '' )
    print ( 'buffon_box_pdf(): Fatal error!' )
    print ( '  Input A < 0.' )
    raise Exception ( 'buffon_box_pdf(): Fatal error!' )
  elif ( a == 0.0 ):
    pdf = 1.0
    return pdf

  if ( b < 0.0 ):
    print ( '' )
    print ( 'buffon_box_pdf(): Fatal error!' )
    print ( '  Input B < 0.' )
    raise Exception ( 'buffon_box_pdf(): Fatal error!' )
  elif ( b == 0.0 ):
    pdf = 1.0
    return pdf

  if ( l < 0.0 ):
    print ( '' )
    print ( 'buffon_box_pdf(): Fatal error!' )
    print ( '  Input L < 0.' )
    raise Exception ( 'buffon_box_pdf(): Fatal error!' )
  elif ( l == 0.0 ):
    pdf = 0.0
    return pdf
  elif ( min ( a, b ) < l ):
    print ( '' )
    print ( 'buffon_box_pdf(): Fatal error!' )
    print ( '  min ( A, B ) < L.' )
    raise Exception ( 'buffon_box_pdf(): Fatal error!' )
    
  pdf = l * ( 2.0 * ( a + b ) - l ) / ( np.pi * a * b )

  return pdf

def buffon_box_pdf_test ( ):

#*****************************************************************************80
#
## buffon_box_pdf_test() tests buffon_box_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'buffon_box_pdf_test():' )
  print ( '  buffon_box_pdf() evaluates the Buffon-Laplace PDF,' )
  print ( '  the probability that, on a grid of cells of width A' )
  print ( '  and height B, a needle of length L, dropped at random,' )
  print ( '  will cross at least one grid line.' )
  print ( '' )
  print ( '      A         B         L        PDF' )
  print ( '' )

  for i in range ( 1, 6 ):
    a = float ( i )
    for j in range ( 1, 6 ):
      b = float ( j )
      for k in range ( 0, 6 ):
        l = float ( k ) * min ( a, b ) / 5.0
        pdf = buffon_box_pdf ( a, b, l )
        print ( '  %8.4g  %8.4g  %8.4g  %14g' % ( a, b, l, pdf ) )

      print ( '' )

  return

def buffon_box_sample ( a, b, l, trial_num, rng ):

#*****************************************************************************80
#
## buffon_box_sample() samples the Buffon Box distribution.
#
#  Discussion:
#
#    In the Buffon-Laplace needle experiment, we suppose that the plane has been
#    tiled into a grid of rectangles of width A and height B, and that a
#    needle of length L is dropped "at random" onto this grid.  
# 
#    We may assume that one end, the "eye" of the needle falls at the point
#    (X1,Y1), taken uniformly at random in the cell [0,A]x[0,B].
#
#    ANGLE, the angle that the needle makes is taken to be uniformly random.
#    The point of the needle, (X2,Y2), therefore lies at
#
#      (X2,Y2) = ( X1+L*cos(ANGLE), Y1+L*sin(ANGLE) )
#
#    The needle will have crossed at least one grid line if any of the 
#    following are true:
#
#      X2 <= 0, A <= X2, Y2 <= 0, B <= Y2.
#
#    This routine simulates the tossing of the needle, and returns the number
#    of times that the needle crossed at least one grid line.
#
#    If L is larger than sqrt ( A*A + B*B ), then the needle will
#    cross every time, and the computation is uninteresting.  However, if
#    L is smaller than this limit, then the probability of a crossing on
#    a single trial is
#
#      P(L,A,B) = ( 2 * L * ( A + B ) - L * L ) / ( PI * A * B )
#
#    and therefore, a record of the number of hits for a given number of
#    trials can be used as a very roundabout way of estimating PI.  
#    (Particularly roundabout, since we actually will use a good value of
#    PI in order to pick the random angles%)
#
#    Note that this routine will try to generate 5 * TRIAL_NUM random
#    real values at one time, using automatic arrays.  
#    When I tried this with TRIAL_NUM = 1,000,000, the program failed,
#    because of internal system limits on such arrays.
#
#    Such a problem could be avoided by using a DO loop running through
#    each trial individually, but this tend to run much more slowly than
#    necessary.
# 
#    Since this routine invokes the random number generator,
#    the user should initialize the random number generator, particularly
#    if it is desired to control whether the sequence is to be varied
#    or repeated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sudarshan Raghunathan,
#    Making a Supercomputer Do What You Want: High Level Tools for 
#    Parallel Programming,
#    Computing in Science and Engineering,
#    Volume 8, Number 5, September/October 2006, pages 70-80.
#
#  Input:
#
#    real A, B, the horizontal and vertical dimensions
#    of each cell of the grid.  0 <= A, 0 <= B.
#
#    real L, the length of the needle.
#    0 <= L <= min ( A, B ).
#
#    integer TRIAL_NUM, the number of times the needle is
#    to be dropped onto the grid.
#
#  Output:
#
#    integer buffon_box_sample, the number of times the needle crossed
#    at least one line of the grid of cells.
#
#  Local:
#
#    integer BATCH_SIZE, specifies the number of trials to be done
#    in a single batch.  Setting BATCH_SIZE to 1 will be very slow.
#    Replacing it by TRIAL_NUM would be fine except that your system
#    may have a limit on the size of automatic arrays.  We have set a default 
#    value of 10,000 here which should be large enough to be efficient
#    but small enough not to annoy the system.
#
  import numpy as np
 
  batch_size = 10000

  hits = 0

  for i in range ( 0, trial_num ):
#
#  Randomly choose the location of the eye of the needle in [0,0]x[A,B],
#  and the angle the needle makes.
#
    x1 = rng.random ( )
    y1 = rng.random ( )
    angle = rng.random ( )

    x1 = a * x1
    y1 = b * y1
    angle = 2.0 * np.pi * angle
#
#  Compute the location of the point of the needle.
#
    x2 = x1 + l * np.cos ( angle )
    y2 = y1 + l * np.sin ( angle )
#
#  Count the end locations that lie outside the cell.
#
    if ( x2 <= 0.0 or a <= x2 or y2 <= 0.0 or b <= y2 ):
      hits = hits + 1

  return hits

def buffon_box_sample_test ( rng ):

#*****************************************************************************80
#
## buffon_box_sample_test() tests buffon_sample_test().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  trial_num_test = np.array ( [ 10, 100, 10000, 1000000 ] )

  a = 1.0
  b = 1.0
  l = 1.0

  print ( '' )
  print ( 'buffon_box_sample_test():' )
  print ( '  buffon_box_sample() simulates a Buffon-Laplace needle dropping' )
  print ( '  experiment.  On a grid of cells of width A and height B' )
  print ( '  a needle of length L is dropped at random.  We count' )
  print ( '  the number of times it crosses at least one grid line,' )
  print ( '  and use this to estimate the value of PI.' )

  print ( '' )
  print ( '  Cell width A =    %g' % ( a ) )
  print ( '  Cell height B =   %g' % ( b ) )
  print ( '  Needle length L = %g' % ( l ) )
  print ( '' )
  print ( '    Trials      Hits          Est(Pi)         Err' )
  print ( '' )

  for test in range ( 0, 4 ):

    trial_num = trial_num_test[test]

    hits = buffon_box_sample ( a, b, l, trial_num, rng )

    if ( 0 < hits ):
      pi_est = ( 2.0 * l * ( a + b ) - l * l ) * trial_num  / ( a * b * hits )
    else:
      pi_est = 1.0E+30

    err = abs ( pi_est - np.pi )

    print ( '  %8d  %8d  %14g  %14g' % ( trial_num, hits, pi_est, err ) )

  return

def buffon_pdf ( a, l ):

#*****************************************************************************80
#
## buffon_pdf() evaluates the Buffon PDF.
#
#  Discussion:
#
#    In the Buffon needle experiment, we suppose that the plane has been
#    ruled by vertical lines with a spacing of A units, and that a
#    needle of length L is dropped "at random" onto this grid.
#
#    Because of the various symmetries, we may assume that this eye of
#    this needle lands in the first infinite strip, and we may further
#    assume that its Y coordinate is 0.  Thus, we have
#    the eye as (X1,Y1) with 0 <= X1 <= A and Y1 = 0.
#
#    ANGLE, the angle that the needle makes is taken to be uniformly random.
#    The point of the needle, (X2,Y2), therefore lies at
#
#      (X2,Y2) = ( X1+L*cos(ANGLE), Y1+L*sin(ANGLE) )
#
#    The needle will have crossed at least one grid line if any of the
#    following are true:
#
#      X2 <= 0, A <= X2.
#
#    The probability of a crossing on a single trial is
#
#      P(A,L) = ( 2 * L ) / ( PI * A )
#
#    and therefore, a record of the number of hits for a given number of
#    trials can be used as a very roundabout way of estimating PI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the horizontal spacing between the
#    vertical grid lines.  0 <= A.
#
#    real L, the length of the needle.
#
#  Output:
#
#    real PDF, the Buffon PDF.
#
  import numpy as np

  if ( a < 0.0 ):
    print ( '' )
    print ( 'buffon_pdf(): Fatal error!' )
    print ( '  Input A < 0.' )
    raise Exception ( 'buffon_pdf(): Fatal error!' )
  elif ( a == 0.0 ):
    pdf = 1.0
    return pdf

  if ( l < 0.0 ):
    print ( '' )
    print ( 'buffon_pdf(): Fatal error!' )
    print ( '  Input L < 0.' )
    raise Exception ( 'buffon_pdf(): Fatal error!' )
  elif ( l == 0.0 ):
    pdf = 0.0
    return pdf

  pdf = ( 2.0 * l ) / ( np.pi * a )

  return pdf

def buffon_pdf_test ( ):

#*****************************************************************************80
#
## buffon_pdf_test() tests buffon_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'buffon_pdf_test():' )
  print ( '  buffon_pdf() evaluates the Buffon PDF,' )
  print ( '  the probability that, on a grid of cells of width A,' )
  print ( '  a needle of length L, dropped at random,' )
  print ( '  will cross at least one grid line.' )
  print ( '' )
  print ( '      A         L        PDF' )
  print ( '' )

  for i in range ( 1, 6 ):
    a = float ( i )
    for k in range ( 0, 6 ):
      l = float ( k ) * a / 5.0
      pdf = buffon_pdf ( a, l )
      print ( '  %8.4g  %8.4g  %14g' % ( a, l, pdf ) )

    print ( '' )

  return

def buffon_sample ( a, l, trial_num, rng ):

#*****************************************************************************80
#
## buffon_sample() simulates a Buffon needle experiment.
#
#  Discussion:
#
#    In the Buffon needle experiment, we suppose that the plane has been
#    ruled by vertical lines with a spacing of A units, and that a
#    needle of length L is dropped "at random" onto this grid.
#
#    Because of the various symmetries, we may assume that this eye of
#    this needle lands in the first infinite strip, and we may further
#    assume that its Y coordinate is 0.  Thus, we have
#    the eye as (X1,Y1) with 0 <= X1 <= A and Y1 = 0.
#
#    ANGLE, the angle that the needle makes is taken to be uniformly random.
#    The point of the needle, (X2,Y2), therefore lies at
#
#      (X2,Y2) = ( X1+L*cos(ANGLE), Y1+L*sin(ANGLE) )
#
#    The needle will have crossed at least one grid line if any of the
#    following are true:
#
#      X2 <= 0, A <= X2.
#
#    The probability of a crossing on a single trial is
#
#      P(A,L) = ( 2 * L ) / ( PI * A )
#
#    and therefore, a record of the number of hits for a given number of
#    trials can be used as a very roundabout way of estimating PI.
#
#    Note that this routine will try to generate 4 * TRIAL_NUM random
#    values at one time, using automatic arrays.
#    When I tried this with TRIAL_NUM = 1,000,000, the program failed,
#    because of internal system limits on such arrays.
#
#    Such a problem could be avoided by using a DO loop running through
#    each trial individually, but this tend to run much more slowly than
#    necessary.
#
#    Since this routine invokes the random number generator,
#    the user should initialize the random number generator, particularly
#    if it is desired to control whether the sequence is to be varied
#    or repeated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the horizontal spacing between the
#    vertical grid lines.  0 <= A.
#
#    real L, the length of the needle.
#
#    integer TRIAL_NUM, the number of times the needle is
#    to be dropped onto the grid.
#
#  Output:
#
#    integer buffon_sample, the number of times the needle
#    crossed at least one line of the grid of cells.
#
#  Local:
#
#    integer BATCH_SIZE, specifies the number of trials to be done
#    in a single batch.  Setting BATCH_SIZE to 1 will be very slow.
#    Replacing it by TRIAL_NUM would be fine except that your system
#    may have a limit on the size of automatic arrays.  We have set a default
#    value of 10,000 here which should be large enough to be efficient
#    but small enough not to annoy the system.
#
  import numpy as np

  batch_size = 10000

  hits = 0

  for batch in range ( 0, trial_num ):
#
#  Randomly choose the location (X1,Y1) of the eye of the needle
#  in [0,0]x[A,0], and the angle the needle makes.
#
    x1 = rng.random ( )
    x1 = a * x1
    angle = rng.random ( )
    angle = 2.0 * np.pi * angle
#
#  Compute the location of the point of the needle.
#  We only need to know the value of X2, not Y2!
#
    x2 = x1 + l * np.cos ( angle )
#
#  Count the end locations that lie outside the cell.
#
    if ( x2 <= 0.0 or a <= x2 ):
      hits = hits + 1

  return hits

def buffon_sample_test ( rng ):

#*****************************************************************************80
#
## buffon_sample_test() tests buffon_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  test_num = 4

  trial_num_test = np.array ( [ 10, 100, 10000, 1000000 ] )

  a = 1.0
  l = 1.0

  print ( '' )
  print ( 'buffon_sample_test():' )
  print ( '  buffon_sample() simulates a Buffon-Laplace' )
  print ( '  needle dropping experiment.  On a grid of cells of ' )
  print ( '  width A, a needle of length L is dropped' )
  print ( '  at random.  We count the number of times it crosses' )
  print ( '  at least one grid line, and use this to estimate ' )
  print ( '  the value of PI.' )

  print ( '' )
  print ( '  Cell width A =    %g' % ( a ) )
  print ( '  Needle length L = %g' % ( l ) )
  print ( '' )
  print ( '    Trials      Hits          Est(Pi)     Err' )
  print ( '' )
 
  for test in range ( 0, 4 ):

    trial_num = trial_num_test[test]

    hits = buffon_sample ( a, l, trial_num, rng )

    if ( 0 < hits ):
      pi_est = ( 2.0 * l * trial_num ) / ( a * hits )
    else:
      pi_est = 1.0E+30

    err = abs ( pi_est - np.pi )

    print ( '  %8d  %8d  %14g  %14g' % ( trial_num, hits, pi_est, err ) )

  return

def burr_cdf ( x, a, b, c, d ):

#*****************************************************************************80
#
## burr_cdf() evaluates the Burr CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= a ):

    cdf = 0.0

  else:

    y = ( x - a ) / b

    cdf = 1.0 - 1.0 / ( 1.0 + y ** c  ) ** d

  return cdf

def burr_cdf_inv ( cdf, a, b, c, d ):

#*****************************************************************************80
#
## burr_cdf_inv() inverts the Burr CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'burr_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'burr_cdf_inv(): Fatal error!' )

  y = ( ( 1.0 / ( 1.0 - cdf ) ) ** ( 1.0 / d ) - 1.0 ) ** ( 1.0 / c )

  x = a + b * y

  return x

def burr_cdf_test ( rng ):

#*****************************************************************************80
#
## burr_cdf_test() tests burr_cdf(), burr_cdf_inv(), burr_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'burr_cdf_test():' )
  print ( '  burr_cdf() evaluates the Burr CDF' )
  print ( '  burr_cdf_inv() inverts the Burr CDF.' )
  print ( '  burr_pdf() evaluates the Burr PDF' )

  a = 1.0
  b = 2.0
  c = 3.0
  d = 2.0

  check = burr_check ( a, b, c, d )

  if ( not check ):
    print ( '' )
    print ( 'burr_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF parameter D = %14g' % ( d ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = burr_sample ( a, b, c, d, rng )

    pdf = burr_pdf ( x, a, b, c, d )

    cdf = burr_cdf ( x, a, b, c, d )

    x2 = burr_cdf_inv ( cdf, a, b, c, d )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def burr_check ( a, b, c, d ):

#*****************************************************************************80
#
## burr_check() checks the parameters of the Burr CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'burr_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0 ):
    print ( '' )
    print ( 'burr_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def burr_mean ( a, b, c, d ):

#*****************************************************************************80
#
## burr_mean() returns the mean of the Burr PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  from scipy.special import gamma

  ymean = d * gamma ( d       - 1.0 / c ) \
            * gamma (     1.0 + 1.0 / c ) \
            / gamma ( d + 1.0           )

  mean = a + b * ymean

  return mean

def burr_pdf ( x, a, b, c, d ):

#*****************************************************************************80
#
## burr_pdf() evaluates the Burr PDF.
#
#  Discussion:
#
#    Y = ( X - A ) / B;
#
#    PDF(X)(A,B,C,D) = ( C * D / B ) * Y ^ ( C - 1 ) / ( 1 + Y ^ C ) ^ ( D + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M E Johnson,
#    Multivariate Statistical Simulation,
#    Wiley, New York, 1987.
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = ( c * d / b ) * y ** ( c - 1.0 ) / ( 1.0 + y ** c ) ** ( d + 1.0 )

  return pdf

def burr_sample ( a, b, c, d, rng ):

#*****************************************************************************80
#
## burr_sample() samples the Burr PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = burr_cdf_inv ( cdf, a, b, c, d )

  return x

def burr_sample_test ( rng ):

#*****************************************************************************80
#
## burr_sample_test() tests burr_mean(), burr_variance(), burr_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'burr_sample_test():' )
  print ( '  burr_mean() computes the Burr mean' )
  print ( '  burr_variance() computes the Burr variance' )
  print ( '  burr_sample() samples the Burr distribution' )

  a = 1.0
  b = 2.0
  c = 3.0
  d = 2.0

  check = burr_check ( a, b, c, d )

  if ( not check ):
    print ( '' )
    print ( 'burr_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = burr_mean ( a, b, c, d )
  variance = burr_variance ( a, b, c, d )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF parameter D = %14g' % ( d ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = burr_sample ( a, b, c, d, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14f' % ( mean ) )
  print ( '  Sample variance = %14f' % ( variance ) )
  print ( '  Sample maximum =  %14f' % ( xmax ) )
  print ( '  Sample minimum =  %14f' % ( xmin ) )

  return

def burr_variance ( a, b, c, d ):

#*****************************************************************************80
#
## burr_variance() returns the variance of the Burr PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  from scipy.special import gamma
  import numpy as np

  if ( c <= 2.0 ):

    print ( '' )
    print ( 'burr_variance(): Warning!' )
    print ( '  Variance undefined for C <= 2.' )
    variance = np.finfo(float).max

  else:

    mu1 = b     * d * gamma ( ( c * d     - 1.0 ) / c ) \
                    * gamma ( (         c + 1.0 ) / c ) \
                    / gamma ( ( c * d + c       ) / c )

    mu2 = b * b * d * gamma ( ( c * d     - 2.0 ) / c ) \
                    * gamma ( (         c + 2.0 ) / c ) \
                    / gamma ( ( c * d + c       ) / c )

    variance = - mu1 * mu1 + mu2

  return variance

def cardioid_cdf ( x, a, b ):

#*****************************************************************************80
#
## cardioid_cdf() evaluates the Cardioid CDF.
#
#  Discussion:
#
#    The angle X is assumed to lie between A - PI and A + PI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 <= B <= 0.5.
#
#  Output:
#
#    real CDF, the value of the PDF.
#
  import numpy as np

  if ( x <= a - np.pi ):
    cdf = 0.0
  elif ( x < a + np.pi ):
    cdf = ( np.pi + x - a + 2.0 * b * np.sin ( x - a ) ) / ( 2.0 * np.pi )
  else:
    cdf = 1.0

  return cdf

def cardioid_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## cardioid_cdf_inv() inverts the Cardioid CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0 <= CDF <= 1.
#
#    real A, B, the parameters.
#    0.0 <= B <= 0.5.
#
#  Output:
#
#    real X, the argument with the given CDF.
#    A - PI <= X <= A + PI.
#
  import numpy as np

  tol = 0.000001

  if ( cdf <= 0.0 ):

    x = a - np.pi

  elif ( cdf < 1.0 ):

    x = a

    it = 0

    while ( True ):

      fx = cdf - ( np.pi + x - a + 2.0 * b * np.sin ( x - a ) ) / ( 2.0 * np.pi )

      if ( abs ( fx ) < tol ):
        break
 
      if ( 10 < it ):
        raise Exception ( 'cardioid_cdf_inv - Too many iterations!' )

      fp = - ( 1.0 + 2.0 * b * np.cos ( x - a ) ) / ( 2.0 * np.pi )

      x = x - fx / fp
      x = max ( x, a - np.pi )
      x = min ( x, a + np.pi )

      it = it + 1

  else:

    x = a + np.pi

  return x

def cardioid_cdf_test ( rng ):

#*****************************************************************************80
#
## cardioid_cdf_test() tests cardioid_cdf(), cardioid_cdf_inv() and cardioid_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  a = 0.0
  b = 0.25

  print ( '' )
  print ( 'cardioid_cdf_test():' )
  print ( '  cardioid_cdf() evaluates the Cardioid CDF' )
  print ( '  cardioid_cdf_inv() inverts the Cardioid CDF.' )
  print ( '  cardioid_pdf() evaluates the Cardioid PDF' )

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )

  if ( not cardioid_check ( a, b ) ):
    print ( '' )
    print ( 'cardioid_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = cardioid_sample ( a, b, rng )
    pdf = cardioid_pdf ( x, a, b )
    cdf = cardioid_cdf ( x, a, b )
    x2 = cardioid_cdf_inv ( cdf, a, b )

    print ( '  %12g  %12g  %12g  %12g' % ( x, pdf, cdf, x2 ) )

  return

def cardioid_check ( a, b ):

#*****************************************************************************80
#
## cardioid_check() checks the parameters of the Cardioid CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    -0.5 <= B <= 0.5.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b < -0.5 or 0.5 < b ):
    print ( '' )
    print ( 'cardioid_check(): Fatal error!' )
    print ( '  B < -0.5 or 0.5 < B.' )
    check = False

  return check

def cardioid_mean ( a, b ):

#*****************************************************************************80
#
## cardioid_mean() returns the mean of the Cardioid PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= B <= 0.5.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def cardioid_pdf ( x, a, b ):

#*****************************************************************************80
#
## cardioid_pdf() evaluates the Cardioid PDF.
#
#  Discussion:
#
#    The cardioid PDF can be thought of as being applied to points on
#    a circle.  Compare this distribution with the "Cosine PDF".
#
#    PDF(A,BX) = ( 1 / ( 2 * PI ) ) * ( 1 + 2 * B * COS ( X - A ) )
#    for 0 <= B <= 1/2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    N I Fisher,
#    Statistical Analysis of Circular Data,
#    Cambridge, 1993.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 <= B <= 0.5.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = ( 1.0 + 2.0 * b * np.cos ( x - a ) ) / ( 2.0 * np.pi )

  return pdf

def cardioid_sample ( a, b, rng ):

#*****************************************************************************80
#
## cardioid_sample() samples the Cardioid PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= B <= 0.5.
#
#  Output:
#
#    real X, a sample of the PDF.
#    A - PI <= X <= A + PI.
#
  import numpy as np

  cdf = rng.random ( )

  x = cardioid_cdf_inv ( cdf, a, b )

  return x

def cardioid_sample_test ( rng ):

#*****************************************************************************80
#
## cardioid_sample_test() tests cardioid_mean(), cardioid_sample(), cardioid_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000

  a = 0.0
  b = 0.25

  print ( '' )
  print ( 'cardioid_sample_test():' )
  print ( '  cardioid_mean() computes the Cardioid mean' )
  print ( '  cardioid_sample() samples the Cardioid distribution' )
  print ( '  cardioid_variance() computes the Cardioid variance.' )

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )

  if ( not cardioid_check ( a, b ) ):
    print ( '' )
    print ( 'cardioid_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = cardioid_mean ( a, b )
  variance = cardioid_variance ( a, b )

  print ( '' )
  print ( '  PDF mean =                    %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = cardioid_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def cardioid_variance ( a, b ):

#*****************************************************************************80
#
## cardioid_variance() returns the variance of the Cardioid PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= B <= 0.5.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a

  return variance

def cauchy_cdf ( x, a, b ):

#*****************************************************************************80
#
## cauchy_cdf() evaluates the Cauchy CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  y = ( x - a ) / b

  cdf = 0.5 + np.arctan ( y ) / np.pi

  return cdf

def cauchy_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## cauchy_cdf_inv() inverts the Cauchy CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  x = a + b * np.tan ( np.pi * ( cdf - 0.5 ) )

  return x

def cauchy_cdf_test ( rng ):

#*****************************************************************************80
#
## cauchy_cdf_test() tests cauchy_cdf(), cauchy_cdf_inv(), cauchy_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'cauchy_cdf_test():' )
  print ( '  cauchy_cdf() evaluates the Cauchy CDF' )
  print ( '  cauchy_cdf_inv() inverts the Cauchy CDF.' )
  print ( '  cauchy_pdf() evaluates the Cauchy PDF' )

  a = 2.0
  b = 3.0

  check = cauchy_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'cauchy_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = cauchy_sample ( a, b, rng )

    pdf = cauchy_pdf ( x, a, b )

    cdf = cauchy_cdf ( x, a, b )

    x2 = cauchy_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def cauchy_check ( a, b ):

#*****************************************************************************80
#
## cauchy_check() checks the parameters of the Cauchy CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'cauchy_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def cauchy_mode ( a, b ):

#*****************************************************************************80
#
## cauchy_mode() returns the mode of the Cauchy PDF.
#
#  Discussion:
#
#    The mean of the Cauchy PDF is infinite.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real mode: the mode of the PDF.
#
  mode = a

  return mode

def cauchy_pdf ( x, a, b ):

#*****************************************************************************80
#
## cauchy_pdf() evaluates the Cauchy PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = 1 / ( PI * B * ( 1 + ( ( X - A ) / B )^2 ) )
#
#    The Cauchy PDF is also known as the Breit-Wigner PDF.  It
#    has some unusual properties.  In particular, the integrals for the
#    expected value and higher order moments are "singular", in the
#    sense that the limiting values do not exist.  A result can be
#    obtained if the upper and lower limits of integration are set
#    equal to +T and -T, and the limit as T=>INFINITY is taken, but
#    this is a very weak and unreliable sort of limit.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  y = ( x - a ) / b

  pdf = 1.0 / ( np.pi * b * ( 1.0 + y * y ) )

  return pdf

def cauchy_sample ( a, b, rng ):

#*****************************************************************************80
#
## cauchy_sample() samples the Cauchy PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = cauchy_cdf_inv ( cdf, a, b )

  return x

def cauchy_sample_test ( rng ):

#*****************************************************************************80
#
## cauchy_sample_test() tests cauchy_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'cauchy_sample_test():' )
  print ( '  cauchy_sample() samples the Cauchy distribution.' )

  a = 2.0
  b = 3.0

  check = cauchy_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'cauchy_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        Infinite' )
  print ( '  PDF variance =    Infinite' )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = cauchy_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def cauchy_variance ( a, b ):

#*****************************************************************************80
#
## cauchy_variance() returns the variance of the Cauchy PDF.
#
#  Discussion:
#
#    The variance of the Cauchy PDF is not well defined.  This routine
#    is made available for completeness only, and simply returns
#    a "very large" number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the mean of the PDF.
#
  import numpy as np

  variance = np.finfo(float).max

  return variance

def chebyshev1_cdf ( x ):

#*****************************************************************************80
#
## chebyshev1_cdf() evaluates the Chebyshev1 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < - 1.0 ):
    cdf = 0.0
  elif ( 1.0 < x ):
    cdf = 1.0
  else:
    cdf = 0.5 + np.arcsin ( x ) / np.pi

  return cdf

def chebyshev1_cdf_inv ( cdf ):

#*****************************************************************************80
#
## chebyshev1_cdf_inv() inverts the Chebyshev1 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'chebyshev1_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'chebyshev1_cdf_inv(): Fatal error!' )

  x = np.sin ( np.pi * ( cdf - 0.5 ) )

  return x

def chebyshev1_cdf_test ( rng ):

#*****************************************************************************80
#
## chebyshev1_cdf_test() tests chebyshev1_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 AUgust 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'chebyshev1_cdf_test():' )
  print ( '  chebyshev1_cdf() evaluates the Chebyshev1 CDF' )
  print ( '  chebyshev1_cdf_inv() inverts the Chebyshev1 CDF.' )
  print ( '  chebyshev1_pdf() evaluates the Chebyshev1 PDF' )
  print ( '' )
  print ( '       X            PDF           CDF            CDF_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = chebyshev1_sample ( rng )

    pdf = chebyshev1_pdf ( x )

    cdf = chebyshev1_cdf ( x )

    x2 = chebyshev1_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def chebyshev1_mean ( ):

#*****************************************************************************80
#
## chebyshev1_mean() returns the mean of the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def chebyshev1_pdf ( x ):

#*****************************************************************************80
#
## chebyshev1_pdf() evaluates the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= -1.0 or 1.0 <= x ):
    pdf = 0.0
  else:
    pdf = 1.0 / np.pi / np.sqrt ( 1.0 - x * x )

  return pdf

def chebyshev1_sample ( rng ):

#*****************************************************************************80
#
## chebyshev1_sample() samples the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Output:
#
#    real VALUE, a random value between 0 and 1.
#
  import numpy as np

  cdf = rng.random ( )

  value = chebyshev1_cdf_inv ( cdf )

  return value

def chebyshev1_sample_test ( rng ):

#*****************************************************************************80
#
## chebyshev1_sample_test() tests chebyshev1_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'chebyshev1_sample_test():' )
  print ( '  chebyshev1_mean() computes the Chebyshev1 mean' )
  print ( '  chebyshev1_sample() samples the Chebyshev1 distribution' )
  print ( '  chebyshev1_variance() computes the Chebyshev1 variance.' )

  mean = chebyshev1_mean ( )
  variance = chebyshev1_variance ( )

  print ( '' )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = chebyshev1_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def chebyshev1_variance ( ):

#*****************************************************************************80
#
## chebyshev1_variance() returns the variance of the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 0.5

  return variance

def chi_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## chi_cdf() evaluates the Chi CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= a ):

    cdf = 0.0

  else:

    y = ( x - a ) / b
    x2 = 0.5 * y * y
    p2 = 0.5 * c

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def chi_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## chi_cdf_inv() inverts the Chi CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a
    return x
  elif ( 1.0 <= cdf ):
    x = np.finfo(float).max
    return x

  x1 = a
  cdf1 = 0.0

  x2 = a + 1.0

  while ( True ):

    cdf2 = chi_cdf ( x2, a, b, c )

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
    cdf3 = chi_cdf ( x3, a, b, c )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      return x

    if ( it_max < it ):
      print ( '' )
      print ( 'chi_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'chi_cdf_inv(): Fatal error!' )

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def chi_cdf_test ( rng ):

#*****************************************************************************80
#
## chi_cdf_test() tests chi_cdf(), chi_cdf_inv(), chi_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'chi_cdf_test():' )
  print ( '  chi_cdf() evaluates the Chi CDF.' )
  print ( '  chi_cdf_inv() inverts the Chi CDF.' )
  print ( '  chi_pdf() evaluates the Chi PDF.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = chi_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'chi_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = chi_sample ( a, b, c, rng )

    pdf = chi_pdf ( x, a, b, c )

    cdf = chi_cdf ( x, a, b, c )

    x2 = chi_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def chi_check ( a, b, c ):

#*****************************************************************************80
#
## chi_check() checks the parameters of the Chi CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'chi_check(): Fatal error!' )
    print ( '  B <= 0.0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'chi_check(): Fatal error!' )
    print ( '  C <= 0.0.' )
    check = False

  return check

def chi_mean ( a, b, c ):

#*****************************************************************************80
#
## chi_mean() returns the mean of the Chi PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real MEAN, the mean value.
#
  import numpy as np
  from scipy.special import gamma

  mean = a + np.sqrt ( 2.0 ) * b * gamma ( 0.5 * ( c + 1.0 ) ) \
    / gamma ( 0.5 * c )

  return mean

def chi_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## chi_pdf() evaluates the Chi PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = EXP ( - 0.5 * ( ( X - A ) / B )^2 )
#      * ( ( X - A ) / B )^( C - 1 ) /
#      ( 2^( 0.5 * C - 1 ) * B * GAMMA ( 0.5 * C ) )
#
#    CHI(A,B,1) is the Half Normal PDF
#    CHI(0,B,2) is the Rayleigh PDF
#    CHI(0,B,3) is the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = np.exp ( - 0.5 * y * y ) * y ** ( c - 1.0 ) \
      / ( 2.0 ** ( 0.5 * c - 1.0 ) * b * gamma ( 0.5 * c ) )

  return pdf

def chi_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## chi_sample() samples the Chi PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  x = chi_square_sample ( c, rng )

  x = a + b * np.sqrt ( x )

  return x

def chi_sample_test ( rng ):

#*****************************************************************************80
#
## chi_sample_test() tests chi_mean(), chi_sample(), chi_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'chi_sample_test():' )
  print ( '  chi_mean() computes the Chi mean' )
  print ( '  chi_variance() computes the Chi variance' )
  print ( '  chi_sample() samples the Chi distribution.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = chi_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'chi_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = chi_mean ( a, b, c )
  variance = chi_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = chi_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def chi_variance ( a, b, c ):

#*****************************************************************************80
#
## chi_variance() returns the variance of the Chi PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  from scipy.special import gamma

  variance = b * b * ( c - 2.0 * ( gamma ( 0.5 * ( c + 1.0 ) ) \
    / gamma ( 0.5 * c ) ) ** 2 )

  return variance

def chi_square_noncentral_check ( a, b ):

#*****************************************************************************80
#
## chi_square_noncentral_check() checks the parameters of the noncentral Chi Squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the parameter of the PDF.
#    1.0 <= A.
#
#    real B, the noncentrality parameter of the PDF.
#    0.0 <= B.
#
#  Output:
#
#    bool CHECK, is TRUE if the data was legal.
#
  check = True

  if ( a < 1.0 ):
    print ( '' )
    print ( 'chi_square_noncentral_check(): Fatal error!' )
    print ( '  A < 1.' )
    check = False

  if ( b < 0.0 ):
    print ( '' )
    print ( 'chi_square_noncentral_check(): Fatal error!' )
    print ( '  B < 0.' )
    check = False

  return check

def chi_square_noncentral_mean ( a, b ):

#*****************************************************************************80
#
## chi_square_noncentral_mean() returns the mean of the noncentral Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the parameter of the PDF.
#    1.0 <= A.
#
#    real B, the noncentrality parameter of the PDF.
#    0.0 <= B.
#
#  Output:
#
#    real MEAN, the mean value.
#
  mean = a + b

  return mean

def chi_square_noncentral_sample ( a, b, rng ):

#*****************************************************************************80
#
## chi_square_noncentral_sample() samples the noncentral Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the parameter of the PDF.
#    1.0 <= A.
#
#    real B, the noncentrality parameter of the PDF.
#    0.0 <= B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  a1 = a - 1.0

  x1 = chi_square_sample ( a1, rng )

  a2 = np.sqrt ( b )
  b2 = 1.0
  x2 = normal_sample ( a2, b2, rng )

  x = x1 + x2 * x2

  return x

def chi_square_noncentral_sample_test ( rng ):

#*****************************************************************************80
#
## chi_square_noncentral_sample_test() tests chi_square_noncentral_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'chi_square_noncentral_sample_test():' )
  print ( '  chi_square_noncentral_mean() computes the Chi Square Noncentral mean.' )
  print ( '  chi_square_noncentral_sample() samples the Chi Square Noncentral PDF.' )
  print ( '  chi_square_noncentral_variance() computes the Chi Square Noncentral variance.' )

  a = 3.0
  b = 2.0

  check = chi_square_noncentral_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'chi_square_noncentral_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = chi_square_noncentral_mean ( a, b )
  variance = chi_square_noncentral_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = chi_square_noncentral_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def chi_square_noncentral_variance ( a, b ):

#*****************************************************************************80
#
## chi_square_noncentral_variance() returns the variance of the noncentral Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    1 <= A.
#
#    real B, the noncentrality parameter of the PDF.
#    0.0 <= B.
#
#  Output:
#
#    real VARIANCE, the variance value.
#
  variance = 2.0 * ( a + 2.0 * b )

  return variance

def chi_square_cdf ( x, a ):

#*****************************************************************************80
#
## chi_square_cdf() evaluates the Chi squared CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the value of the random deviate.
#
#    real A, the parameter of the distribution, usually
#    the number of degrees of freedom.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  x2 = 0.5 * x

  a2 = 0.0
  b2 = 1.0
  c2 = 0.5 * a

  cdf = gamma_cdf ( x2, a2, b2, c2 )

  cdf = 1.0 - cdf

  return cdf

def chi_square_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## chi_square_cdf_inv() inverts the Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Best and Roberts,
#    The Percentage Points of the Chi-Squared Distribution,
#    Algorithm AS 91,
#    Applied Statistics,
#    Volume 24, Number ?, pages 385-390, 1975.
#
#  Input:
#
#    real CDF, a value of the chi-squared cumulative
#    probability density function.
#    0.000002 <= CDF <= 0.999998.
#
#    real A, the parameter of the chi-squared
#    probability density function.  0 < A.
#
#  Output:
#
#    real X, the value of the chi-squared random deviate
#    with the property that the probability that a chi-squared random
#    deviate with parameter A is less than or equal to PPCHI2 is P.
#
  import numpy as np
  from scipy.special import gammaln

  aa = 0.6931471806
  c1 = 0.01
  c2 = 0.222222
  c3 = 0.32
  c4 = 0.4
  c5 = 1.24
  c6 = 2.2
  c7 = 4.67
  c8 = 6.66
  c9 = 6.73
  c10 = 13.32
  c11 = 60.0
  c12 = 70.0
  c13 = 84.0
  c14 = 105.0
  c15 = 120.0
  c16 = 127.0
  c17 = 140.0
  c18 = 175.0
  c19 = 210.0
  c20 = 252.0
  c21 = 264.0
  c22 = 294.0
  c23 = 346.0
  c24 = 420.0
  c25 = 462.0
  c26 = 606.0
  c27 = 672.0
  c28 = 707.0
  c29 = 735.0
  c30 = 889.0
  c31 = 932.0
  c32 = 966.0
  c33 = 1141.0
  c34 = 1182.0
  c35 = 1278.0
  c36 = 1740.0
  c37 = 2520.0
  c38 = 5040.0
  cdf_max = 0.999998
  cdf_min = 0.000002
  e = 0.0000005
  it_max = 20

  if ( cdf < cdf_min ):
    x = -1.0
    print ( '' )
    print ( 'chi_square_cdf_inv(): Fatal error!' )
    print ( '  CDF < CDf_min.' )
    raise Exception ( 'chi_square_cdf_inv(): Fatal error!' )

  if ( cdf_max < cdf ):
    x = -1.0
    print ( '' )
    print ( 'chi_square_cdf_inv(): Fatal error!' )
    print ( '  CDf_max < CDF.' )
    raise Exception ( 'chi_square_cdf_inv(): Fatal error!' )

  xx = 0.5 * a
  c = xx - 1.0
#
#  Compute Log ( Gamma ( A/2 ) ).
#
  g = gammaln ( a / 2.0 )
#
#  Starting approximation for small chi-squared.
#
  if ( a < - c5 * np.log ( cdf ) ):

    ch = ( cdf * xx * np.exp ( g + xx * aa ) ) ** ( 1.0 / xx )

    if ( ch < e ):
      x = ch
      return x
#
#  Starting approximation for A less than or equal to 0.32.
#
  elif ( a <= c3 ):

    ch = c4
    a2 = np.log ( 1.0 - cdf )

    while ( True ):

      q = ch
      p1 = 1.0 + ch * ( c7 + ch )
      p2 = ch * ( c9 + ch * ( c8 + ch ) )

      t = - 0.5 + ( c7 + 2.0 * ch ) / p1 - ( c9 + ch * ( c10 + 3.0 * ch ) ) / p2

      ch = ch - ( 1.0 - np.exp ( a2 + g + 0.5 * ch + c * aa ) * p2 / p1 ) / t

      if ( abs ( q / ch - 1.0 ) <= c1 ):
        break
#
#  Call to algorithm AS 111.
#  Note that P has been tested above.
#  AS 241 could be used as an alternative.
#
  else:

    x2 = normal_01_cdf_inv ( cdf )
#
#  Starting approximation using Wilson and Hilferty estimate.
#
    p1 = c2 / a
    ch = a * ( x2 * np.sqrt ( p1 ) + 1.0 - p1 ) ** 3
#
#  Starting approximation for P tending to 1.
#
    if ( c6 * a + 6.0 < ch ):
      ch = -2.0 * ( np.log ( 1.0 - cdf ) - c * np.log ( 0.5 * ch ) + g )
#
#  Call to algorithm AS 239 and calculation of seven term Taylor series.
#
  for i in range ( 0, it_max ):

    q = ch
    p1 = 0.5 * ch
    p2 = cdf - r8_gamma_inc ( xx, p1 )
    t = p2 * np.exp ( xx * aa + g + p1 - c * np.log ( ch ) )
    b = t / ch
    a2 = 0.5 * t - b * c

    s1 = ( c19 + a2 \
       * ( c17 + a2 \
       * ( c14 + a2 \
       * ( c13 + a2 \
       * ( c12 + a2 \
       *   c11 ) ) ) ) ) / c24

    s2 = ( c24 + a2 \
       * ( c29 + a2 \
       * ( c32 + a2 \
       * ( c33 + a2 \
       *   c35 ) ) ) ) / c37

    s3 = ( c19 + a2 \
       * ( c25 + a2 \
       * ( c28 + a2 \
       *   c31 ) ) ) / c37

    s4 = ( c20 + a2 \
       * ( c27 + a2 \
       *   c34 ) + c \
       * ( c22 + a2 \
       * ( c30 + a2 \
       *   c36 ) ) ) / c38

    s5 = ( c13 + c21 * a2 + c * ( c18 + c26 * a2 ) ) / c37

    s6 = ( c15 + c * ( c23 + c16 * c ) ) / c38

    ch = ch + t * ( 1.0 + 0.5 * t * s1 - b * c \
      * ( s1 - b \
      * ( s2 - b \
      * ( s3 - b \
      * ( s4 - b \
      * ( s5 - b \
      *   s6 ) ) ) ) ) )

    if ( e < abs ( q / ch - 1.0 ) ):
      x = ch
      return x

  x = ch
  print ( '' )
  print ( 'chi_square_cdf_inv - Warning!' )
  print ( '  Convergence not reached.' )

  return x

def chi_square_cdf_test ( rng ):

#*****************************************************************************80
#
## chi_square_cdf_test() tests chi_square_cdf(), chi_square_cdf_inv(), chi_square_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'chi_square_cdf_test():' )
  print ( '  chi_square_cdf() evaluates the Chi Square CDF' )
  print ( '  chi_square_cdf_inv() inverts the Chi Square CDF.' )
  print ( '  chi_square_pdf() evaluates the Chi Square PDF' )

  a = 4.0

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  check = chi_square_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'chi_square_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = chi_square_sample ( a, rng )

    pdf = chi_square_pdf ( x, a )

    cdf = chi_square_cdf ( x, a )

    x2 = chi_square_cdf_inv ( cdf, a )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def chi_square_check ( a ):

#*****************************************************************************80
#
## chi_square_check() checks the parameter of the central Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the distribution.
#    1 <= A.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 1.0 ):
    print ( '' )
    print ( 'chi_square_check(): Fatal error!' )
    print ( '  A < 1.0.' )
    check = False

  return check

def chi_square_mean ( a ):

#*****************************************************************************80
#
## chi_square_mean() returns the mean of the central Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the distribution.
#    1 <= A.
#
#  Output:
#
#    real MEAN, the mean value.
#
  mean = a

  return mean

def chi_square_pdf ( x, a ):

#*****************************************************************************80
#
## chi_square_pdf() evaluates the central Chi squared PDF.
#
#  Discussion:
#
#    PDF(X)(A) =
#      EXP ( - X / 2 ) * X^((A-2)/2) / ( 2^(A/2) * GAMMA ( A/2 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#    real A, the parameter of the PDF.
#    1 <= A.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    b = a / 2.0
    pdf = np.exp ( - 0.5 * x ) * x ** ( b - 1.0 ) / ( 2.0 ** b * gamma ( b ) )
 
  return pdf

def chi_square_sample ( a, rng ):

#*****************************************************************************80
#
## chi_square_sample() samples the central Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    1 <= A.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  it_max = 100

  n = int ( a )

  if ( n == a and n <= it_max ):

    x = 0.0
    for i in range ( 0, n ):
      x2 = normal_01_sample ( rng )
      x = x + x2 * x2

  else:

    a2 = 0.0
    b2 = 1.0
    c2 = a / 2.0

    x = gamma_sample ( a2, b2, c2, rng )

    x = 2.0 * x

  return x

def chi_square_sample_test ( rng ):

#*****************************************************************************80
#
## chi_square_sample_test() tests chi_square_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'chi_square_sample_test():' )
  print ( '  chi_square_mean() computes the Chi Square mean' )
  print ( '  chi_square_sample() samples the Chi Square distribution' )
  print ( '  chi_square_variance() computes the Chi Square variance.' )

  a = 10.0

  check = chi_square_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'chi_square_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = chi_square_mean ( a )
  variance = chi_square_variance ( a )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = chi_square_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def chi_square_variance ( a ):

#*****************************************************************************80
#
## chi_square_variance() returns the variance of the central Chi squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the distribution.
#    1 <= A.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 2.0 * a

  return variance

def circular_normal_01_mean ( ):

#*****************************************************************************80
#
## circular_normal_01_mean() returns the mean of the Circular Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN(2), the mean of the PDF.
#
  import numpy as np

  mean = np.zeros ( 2 )

  return mean

def circular_normal_01_pdf ( x, pdf ):

#*****************************************************************************80
#
## circular_normal_01_pdf() evaluates the Circular Normal 01 PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - 0.5 * ( X(1)^2 + X(2)^2 ) ) / ( 2 * PI )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(2), the argument of the PDF.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - 0.5 * ( x[0] ** 2 + x[1] ** 2 ) ) / ( 2.0 * np.pi )

  return pdf

def circular_normal_01_sample ( rng ):

#*****************************************************************************80
#
## circular_normal_01_sample() samples the Circular Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(2), a sample of the PDF.
#
  import numpy as np

  v1 = rng.random ( )
  v2 = rng.random ( )

  x = np.zeros ( 2 )
  x[0] = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.cos ( 2.0 * np.pi * v2 )
  x[1] = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.sin ( 2.0 * np.pi * v2 )

  return x

def circular_normal_01_sample_test ( rng ):

#*****************************************************************************80
#
## circular_normal_01_sample_test() tests circular_normal_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  nsample = 1000

  print ( '' )
  print ( 'circular_normal_01_sample_test():' )
  print ( '  circular_normal_01_mean() computes the Circular Normal 01 mean' )
  print ( '  circular_normal_01_sample() samples the Circular Normal 01 distribution' )
  print ( '  circular_normal_01_variance() computes the Circular Normal 01 variance.' )

  mean = circular_normal_01_mean ( )
  variance = circular_normal_01_variance ( )

  print ( '' )
  print ( '  PDF means =               %14g  %14g' % ( mean[0], mean[1] ) )
  print ( '  PDF variances =           %14g  %14g' % ( variance[0], variance[1] ) )
  
  x_table = np.zeros ( nsample )
  y_table = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x = circular_normal_01_sample ( rng )
    x_table[i] = x[0]
    y_table[i] = x[1]

  xmean = np.mean ( x_table )
  xvariance = np.var ( x_table )
  xmax = np.max ( x_table )
  xmin = np.min ( x_table )

  ymean = np.mean ( y_table )
  yvariance = np.var ( y_table )
  ymax = np.max ( y_table )
  ymin = np.min ( y_table )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g  %14g' % ( xmean, ymean ) )
  print ( '  Sample variance = %14g  %14g' % ( xvariance, yvariance ) )
  print ( '  Sample maximum =  %14g  %14g' % ( xmax, ymax ) )
  print ( '  Sample minimum =  %14g  %14g' % ( xmin, ymin ) )

  return

def circular_normal_01_variance ( ):

#*****************************************************************************80
#
## circular_normal_01_variance() returns the variance of the Circular Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE(2), the variance of the PDF.
#
  import numpy as np

  variance = np.ones ( 2 )

  return variance

def circular_normal_mean ( a, b ):

#*****************************************************************************80
#
## circular_normal_mean() returns the mean of the Circular Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2), a parameter of the PDF, the mean value.
#
#    real B, a parameter of the PDF, the standard deviation.
#
#  Output:
#
#    real MEAN(2), the mean of the PDF.
#
  import numpy as np

  mean = np.zeros ( 2 )

  mean[0] = a[0]
  mean[1] = a[1]

  return mean

def circular_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## circular_normal_pdf() evaluates the Circular Normal PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - 0.5 * ( ( (X(1)-A(1))^2 + (X(2)-A(2))^2 ) / B^2 )
#      / ( 2 * PI * B^2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(2), the argument of the PDF.
#
#    real A(2), a parameter of the PDF, the mean value.
#
#    real B, a parameter of the PDF, the standard deviation.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  d = ( ( x[0] - a[0] ) ** 2 + ( x[1] - a[1] ) ** 2 ) / b ** 2

  pdf = np.exp ( - 0.5 * d ) / ( 2.0 * b ** 2 * np.pi )

  return pdf

def circular_normal_sample ( a, b, rng ):

#*****************************************************************************80
#
## circular_normal_sample() samples the Circular Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2), a parameter of the PDF, the mean value.
#
#    real B, a parameter of the PDF, the standard deviation.
#
#  Output:
#
#    real X(2), a sample of the PDF.
#
  import numpy as np

  v1 = rng.random ( )
  v2 = rng.random ( )

  r = np.sqrt ( - 2.0 * np.log ( v1 ) )

  x = np.zeros ( 2 )

  x[0] = a[0] + b * r * np.cos ( 2.0 * np.pi * v2 )
  x[1] = a[1] + b * r * np.sin ( 2.0 * np.pi * v2 )

  return x

def circular_normal_sample_test ( rng ):

#*****************************************************************************80
#
## circular_normal_sample_test() tests circular_normal_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  a = np.array ( [ 1.0, 5.0 ] )
  b = 0.75

  print ( '' )
  print ( 'circular_normal_sample_test():' )
  print ( '  circular_normal_mean() computes the Circular Normal mean' )
  print ( '  circular_normal_sample() samples the Circular Normal distribution' )
  print ( '  circular_normal_variance() computes the Circular Normal variance.' )

  mean = circular_normal_mean ( a, b )
  variance = circular_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF means =               %14g  %14g' % ( mean[0], mean[1] ) )
  print ( '  PDF variances =           %14g  %14g' % ( variance[0], variance[1] ) )
  
  x_table = np.zeros ( nsample )
  y_table = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x = circular_normal_sample ( a, b, rng )
    x_table[i] = x[0]
    y_table[i] = x[1]

  xmean = np.mean ( x_table )
  xvariance = np.var ( x_table )
  xmax = np.max ( x_table )
  xmin = np.min ( x_table )

  ymean = np.mean ( y_table )
  yvariance = np.var ( y_table )
  ymax = np.max ( y_table )
  ymin = np.min ( y_table )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g  %14g' % ( xmean, ymean ) )
  print ( '  Sample variance = %14g  %14g' % ( xvariance, yvariance ) )
  print ( '  Sample maximum =  %14g  %14g' % ( xmax, ymax ) )
  print ( '  Sample minimum =  %14g  %14g' % ( xmin, ymin ) )

  return

def circular_normal_variance ( a, b ):

#*****************************************************************************80
#
## circular_normal_variance() returns the variance of the Circular Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2), a parameter of the PDF, the mean value.
#
#    real B, a parameter of the PDF, the standard deviation.
#
#  Output:
#
#    real VARIANCE(2), the variance of the PDF.
#
  import numpy as np

  variance = np.zeros ( 2 )

  variance[0] = b ** 2
  variance[1] = b ** 2

  return variance

def cosine_cdf ( x, a, b ):

#*****************************************************************************80
#
## cosine_cdf() evaluates the Cosine CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= a - np.pi * b ):

    cdf = 0.0

  elif ( x <= a + np.pi * b ):

    y = ( x - a ) / b

    cdf = 0.5 + ( y + np.sin ( y ) ) / ( 2.0 * np.pi )

  elif ( a + np.pi * b < x ):

    cdf = 1.0

  return cdf

def cosine_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## cosine_cdf_inv() inverts the Cosine CDF.
#
#  Discussion:
#
#    A simple bisection method is used on the interval
#    [ A - PI * B, A + PI * B ].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a - np.pi * b
    return x
  elif ( 1.0 <= cdf ):
    x = a + np.pi * b
    return x

  x1 = a - np.pi * b
  cdf1 = 0.0

  x2 = a + np.pi * b
  cdf2 = 1.0
#
#  Now use bisection.
#
  it = 0

  for it in range ( 0, it_max ):

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = cosine_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      return x

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  print ( '' )
  print ( 'cosine_cdf_inv - Warning!' )
  print ( '  Iteration limit exceeded.' )

  return x

def cosine_cdf_test ( rng ):

#*****************************************************************************80
#
## cosine_cdf_test() tests cosine_cdf(), cosine_cdf_inv(), cosine_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'cosine_cdf_test():' )
  print ( '  cosine_cdf() evaluates the Cosine CDF.' )
  print ( '  cosine_cdf_inv() inverts the Cosine CDF.' )
  print ( '  cosine_pdf() evaluates the Cosine PDF.' )

  a = 2.0
  b = 1.0

  check = cosine_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'cosine_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = cosine_sample ( a, b, rng )

    pdf = cosine_pdf ( x, a, b )

    cdf = cosine_cdf ( x, a, b )

    x2 = cosine_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %g' % ( x, pdf, cdf, x2 ) )

  return

def cosine_check ( a, b ):

#*****************************************************************************80
#
## cosine_check() checks the parameters of the Cosine CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'cosine_check(): Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def cosine_mean ( a, b ):

#*****************************************************************************80
#
## cosine_mean() returns the mean of the Cosine PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def cosine_pdf ( x, a, b ):

#*****************************************************************************80
#
## cosine_pdf() evaluates the Cosine PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = ( 1 / ( 2 * PI * B ) ) * COS ( ( X - A ) / B )
#    for A - PI * B <= X <= A + PI * B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a - np.pi * b ):

    pdf = 0.0

  elif ( x <= a + np.pi * b ):

    y = ( x - a ) / b

    pdf = 1.0 / ( 2.0 * np.pi * b ) * np.cos ( y )

  elif ( a + np.pi * b < x ):

    pdf = 0.0

  return pdf

def cosine_sample ( a, b, rng ):

#*****************************************************************************80
#
## cosine_sample() samples the Cosine PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = cosine_cdf_inv ( cdf, a, b )

  return x

def cosine_sample_test ( rng ):

#*****************************************************************************80
#
## cosine_sample_test() tests cosine_mean(), cosine_sample(), cosine_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'cosine_sample_test():' )
  print ( '  cosine_mean() computes the Cosine mean' )
  print ( '  cosine_sample() samples the Cosine distribution' )
  print ( '  cosine_variance() computes the Cosine variance.' )

  a = 2.0
  b = 1.0

  check = cosine_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'cosine_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = cosine_mean ( a, b )
  variance = cosine_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )
  print ( '  PDF mean =        %g' % ( mean ) )
  print ( '  PDF variance =    %g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = cosine_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d'% ( nsample ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )

  return

def cosine_variance ( a, b ):

#*****************************************************************************80
#
## cosine_variance() returns the variance of the Cosine PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = ( np.pi * np.pi / 3.0 - 2.0 ) * b * b

  return variance

def coupon_complete_pdf ( type_num, box_num ):

#*****************************************************************************80
#
## coupon_complete_pdf() evaluates the Complete Coupon Collection PDF.
#
#  Discussion:
#
#    PDF(TYPE_NUM,BOX_NUM) is the probability that, given an inexhaustible 
#    supply of boxes, inside each of which there is one of TYPE_NUM distinct
#    coupons, which are uniformly distributed among the boxes, that it will 
#    require opening exactly BOX_NUM boxes to achieve at least one of each
#    kind of coupon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Herbert Wilf,
#    Some New Aspects of the Coupon Collector's Problem,
#    SIAM Review,
#    Volume 48, Number 3, September 2006, pages 549-565.
#
#  Input:
#
#    integer BOX_NUM, the number of boxes that had to be opened
#    in order to just get at least one of each coupon.
#    0 <= BOX_NUM.  If BOX_NUM < TYPE_NUM, then PDF is surely 0.
#
#    integer TYPE_NUM, the number of distinct coupons.
#    1 <= TYPE_NUM.
#
#  Output:
#
#    real PDF, the value of the PDF.
#

#
#  Nonsense cases.
#
  if ( box_num < 0 ):

    pdf = 0.0

  elif ( type_num < 1 ):

    pdf = 0.0
#
#  Degenerate but meaningful case.
#
  elif ( type_num == 1 ):

    if ( box_num == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0
#
#  Easy cases.
#
  elif ( box_num < type_num ):

    pdf = 0.0
#
#  General case.
#
  else:

    factor = 1.0
    for i in range ( 1, type_num + 1 ):
      factor = factor * float ( i ) / float ( type_num )

    for i in range ( type_num + 1, box_num + 1 ):
      factor = factor / float ( type_num )
    
    pdf = factor * stirling2_number ( box_num - 1, type_num - 1 )

  return pdf

def coupon_complete_pdf_test ( ):

#*****************************************************************************80
#
## coupon_complete_pdf_test() tests coupon_complete_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'coupon_complete_pdf_test():' )
  print ( '  coupon_complete_pdf() evaluates the Coupon Complete PDF.' )
  print ( '' )

  for type_num in range ( 2, 5 ):

    print ( '' )
    print ( '  Number of coupon types is %d' % ( type_num ) )
    print ( '' )
    print ( '   BOX_NUM      PDF             CDF' )
    print ( '' )
    cdf = 0.0
    for box_num in range ( 1, 21 ):
      pdf = coupon_complete_pdf ( type_num, box_num )
      cdf = cdf + pdf
      print ( '  %8d  %14g  %14g' % ( box_num, pdf, cdf ) )

  return

def coupon_mean ( j, n ):

#*****************************************************************************80
#
## coupon_mean() returns the mean of the Coupon PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer J, the number of distinct coupons to be collected.
#    J must be between 1 and N.
#
#    integer N, the number of distinct coupons.
#
#  Output:
#
#    real MEAN, the mean number of coupons that
#    must be collected in order to just get J distinct kinds.
#
  if ( n < j ):
    print ( '' )
    print ( 'coupon_mean(): Fatal error!' )
    print ( '  Number of distinct coupons desired must be no more' )
    print ( '  than the total number of distinct coupons.' )
    raise Exception ( 'coupon_mean(): Fatal error!' )

  mean = 0.0
  for i in range ( 1, j + 1 ):
    mean = mean + 1.0 / float ( n - i + 1 )
  mean = mean * float ( n )

  return mean

def coupon_sample ( n_type, rng ):

#*****************************************************************************80
#
## coupon_sample() simulates the coupon collector's problem.
#
#  Discussion:
#
#    The coupon collector needs to collect one of each of N_TYPE
#    coupons.  The collector may draw one coupon on each trial,
#    and takes as many trials as necessary to complete the task.
#    On each trial, the probability of picking any particular type
#    of coupon is always 1 / N_TYPE.
#
#    The most interesting question is, what is the expected number
#    of drawings necessary to complete the collection?
#    how does this number vary as N_TYPE increases?  What is the
#    distribution of the numbers of each type of coupon in a typical
#    collection when it is just completed?
#
#    As N increases, the number of coupons necessary to be
#    collected in order to get a complete set in any simulation
#    strongly tends to the value N_TYPE * LOG ( N_TYPE ).
#
#    If N_TYPE is 1, the simulation ends with a single drawing.
#
#    If N_TYPE is 2, then we may call the coupon taken on the first drawing
#    a "Head", say, and the process then is similar to the question of the
#    length, plus one, of a run of Heads or Tails in coin flipping.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_TYPE, the number of types of coupons.
#
#  Output:
#
#    integer COUPON(N_TYPE), the number of coupons of each type
#    that were collected during the simulation.
#
#    integer N_COUPON, the total number of coupons collected.
#
  import numpy as np

  max_coupon = 2000

  coupon = np.zeros ( n_type )

  straight = 0
  n_coupon = 0
#
#  Draw another coupon.
#
  while ( n_coupon < max_coupon ):

    i = rng.integers ( low = 1, high = n_type, endpoint = True )
#
#  Increment the number of I coupons.
#
    coupon[i-1] = coupon[i-1] + 1
    n_coupon = n_coupon + 1
#
#  If I is the next one we needed, increase STRAIGHT by 1.
#
    if ( i == straight + 1 ):

      while ( True ):

        straight = straight + 1
#
#  If STRAIGHT = N_TYPE, we have all of them.
#
        if ( n_type <= straight ):
          return coupon, n_coupon
#
#  If the next coupon has not been collected, our straight is over.
#
        if ( coupon[straight] <= 0 ):
          break

  print ( '' )
  print ( 'coupon_sample(): Fatal error!' )
  print ( '  Maximum number of coupons drawn without success.' )

  return coupon, n_coupon

def coupon_sample_test ( rng ):

#*****************************************************************************80
#
## coupon_sample_test() tests coupon_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n_trial = 10
  max_type = 25

  print ( '' )
  print ( 'coupon_sample_test():' )
  print ( '  coupon_sample() samples the coupon PDF.' )
  print ( '' )

  for n_type in range ( 5, max_type + 1, 5 ):

    print ( '' )
    print ( '  Number of coupon types is %d' % ( n_type ) )

    expect = n_type * np.log ( float ( n_type ) )

    print ( '  Expected wait is about %g' % ( expect ) )
    print ( '' )

    average = 0.0
    for i in range ( 0, n_trial ):
      coupon, n_coupon = coupon_sample ( n_type, rng )
      print ( '  %6d  %6d' % ( i, n_coupon ) )
      average = average + n_coupon

    average = average / float ( n_trial )

    print ( '' )
    print ( '  Average wait was %g' % ( average ) )

  return

def coupon_variance ( j, n ):

#*****************************************************************************80
#
## coupon_variance() returns the variance of the Coupon PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer J, the number of distinct coupons to be collected.
#    J must be between 1 and N.
#
#    integer N, the number of distinct coupons.
#
#  Output:
#
#    real VARIANCE, the variance of the number of
#    coupons that must be collected in order to just get J distinct kinds.
#
  if ( n < j ):
    print ( '' )
    print ( 'coupon_variance(): Fatal error!' )
    print ( '  Number of distinct coupons desired must be no more' )
    print ( '  than the total number of distinct coupons.' )
    raise Exception ( 'coupon_variance(): Fatal error!' )

  variance = 0.0
  for i in range ( 1, j + 1 ):
    variance = variance + float ( i - 1 ) / float ( ( n - i + 1 ) ** 2 )
  variance = variance * float ( n )

  return variance

def deranged_cdf ( x, a ):

#*****************************************************************************80
#
## deranged_cdf() evaluates the Deranged CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the maximum number of items in their correct places.
#    0 <= X <= A.
#
#    integer A, the number of items.
#    1 <= A.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  from scipy.special import comb
  from scipy.special import factorial

  if ( x < 0 or a < x ):
    cdf = 0.0
  else:
    sum2 = 0
    for x2 in range ( 0, x + 1 ):
      cnk = comb ( a, x2 )
      dnmk = deranged_enum ( a - x2 )
      sum2 = sum2 + cnk * dnmk
    nfact = factorial ( a )
    cdf = sum2 / nfact

  return cdf

def deranged_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## deranged_cdf_inv() inverts the Deranged CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    integer A, the number of items.
#    1 <= A.
#
#  Output:
#
#    integer X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'deranged_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'deranged_cdf_inv(): Fatal error!' )

  cdf2 = 0.0

  for x2 in range ( 0, a + 1 ):

    pdf = deranged_pdf ( x2, a )

    cdf2 = cdf2 + pdf

    if ( cdf <= cdf2 ):
      x = x2
      return x

  x = a

  return x

def deranged_cdf_test ( rng ):

#*****************************************************************************80
#
## deranged_cdf_test() tests deranged_cdf(), deranged_cdf_inv(), deranged_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'deranged_cdf_test():' )
  print ( '  deranged_cdf() evaluates the Deranged CDF' )
  print ( '  deranged_cdf_inv() inverts the Deranged CDF.' )
  print ( '  deranged_pdf() evaluates the Deranged PDF' )

  a = 7

  check = deranged_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'deranged_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for x in range ( 0, a + 1 ):

    pdf = deranged_pdf ( x, a )

    cdf = deranged_cdf ( x, a )

    x2 = deranged_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def deranged_check ( a ):

#*****************************************************************************80
#
## deranged_check() checks the parameter of the Deranged PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the total number of items.
#    1 <= A.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 1 ):
    print ( '' )
    print ( 'deranged_check(): Fatal error!' )
    print ( '  A < 1.' )
    check = False

  return check

def deranged_enum ( n ):

#*****************************************************************************80
#
## deranged_enum() returns the number of derangements of N objects.
#
#  Discussion:
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#  Recursion:
#
#      D(0) = 1
#      D(1) = 0
#      D(2) = 1
#      D(N) = (N-1) * ( D(N-1) + D(N-2) )
#
#    or
#
#      D(0) = 1
#      D(1) = 0
#      D(N) = N * D(N-1) + (-1)^N
#
#  Formula:
#
#    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
#
#    Based on the inclusion/exclusion law.
#
#    D(N) is the number of ways of placing N non-attacking rooks on
#    an N by N chessboard with one diagonal deleted.
#
#    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
#
#    The number of permutations with exactly K items in the right
#    place is COMB(N,K) * D(N-K).
#
#  First values:
#
#     N         D(N)
#     0           1
#     1           0
#     2           1
#     3           2
#     4           9
#     5          44
#     6         265
#     7        1854
#     8       14833
#     9      133496
#    10     1334961
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects to be permuted.
#
#  Output:
#
#    integer DN, the number of derangements of N objects.
#
  if ( n < 0 ):

    dn = 0

  elif ( n == 0 ):

    dn = 1

  elif ( n == 1 ):

    dn = 0

  elif ( n == 2 ):

    dn = 1

  else:

    dnm1 = 0
    dn = 1

    for i in range ( 3, n + 1 ):
      dnm2 = dnm1
      dnm1 = dn
      dn = ( i - 1 ) * ( dnm1 + dnm2 )

  return dn

def deranged_mean ( a ):

#*****************************************************************************80
#
## deranged_mean() returns the mean of the Deranged CDF.
#
#  Discussion:
#
#    The mean is computed by straightforward summation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of items.
#    1 <= A.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.0

  for x in range ( 0, a + 1 ):
    pdf = deranged_pdf ( x, a )
    mean = mean + pdf * x

  return mean

def deranged_pdf ( x, a ):

#*****************************************************************************80
#
## deranged_pdf() evaluates the Deranged PDF.
#
#  Discussion:
#
#    PDF(X)(A) is the probability that exactly X items will occur in
#    their proper place after a random permutation of A items.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the number of items in their correct places.
#    0 <= X <= A.
#
#    integer A, the total number of items.
#    1 <= A.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  from scipy.special import comb
  from scipy.special import factorial

  if ( x < 0 or a < x ):
    pdf = 0.0
  else:
    cnk = comb ( a, x )
    dnmk = deranged_enum ( a - x )
    nfact = factorial ( a )
    pdf = cnk * dnmk / nfact

  return pdf

def deranged_sample ( a, rng ):

#*****************************************************************************80
#
## deranged_sample() samples the Deranged PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of items.
#    1 <= A.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = deranged_cdf_inv ( cdf, a )

  return x

def deranged_sample_test ( rng ):

#*****************************************************************************80
#
## deranged_sample_test() tests deranged_mean(), deranged_variance(), deranged_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'deranged_sample_test():' )
  print ( '  deranged_mean() computes the Deranged mean.' )
  print ( '  deranged_variance() computes the Deranged variance.' )
  print ( '  deranged_sample() samples the Deranged distribution.' )

  a = 7

  check = deranged_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'deranged_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = deranged_mean ( a )
  variance = deranged_variance ( a )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = deranged_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def deranged_variance ( a ):

#*****************************************************************************80
#
## deranged_variance() returns the variance of the Deranged CDF.
#
#  Discussion:
#
#    The variance is computed by straightforward summation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of items.
#    1 <= A.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  mean = deranged_mean ( a )

  variance = 0.0
  for x in range ( 0, a + 1 ):
    pdf = deranged_pdf ( x, a )
    variance = variance + pdf * ( x - mean ) ** 2

  return variance

def digamma ( x ):

#*****************************************************************************80
#
## digamma() calculates DIGAMMA ( X ) = d ( LOG ( GAMMA ( X ) ) ) / dX
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by Jose Bernardo.
#    This version by John Burkardt.
#
#  Reference:
#
#    Jose Bernardo,
#    Algorithm AS 103:
#    Psi ( Digamma ) Function,
#    Applied Statistics,
#    Volume 25, Number 3, 1976, pages 315-317.
#
#  Input:
#
#    real X, the argument of the digamma function.
#    0 < X.
#
#  Output:
#
#    real VALUE, the value of the digamma function at X.
#
  import numpy as np
#
#  Check the input.
#
  if ( x <= 0.0 ):
    value = 0.0
    return value
#
#  Initialize.
#
  value = 0.0
#
#  Use approximation for small argument.
#
  if ( x <= 0.000001 ):
    euler_mascheroni = 0.57721566490153286060
    value = - euler_mascheroni - 1.0 / x + 1.6449340668482264365 * x
    return value
#
#  Reduce to DIGAMA(X + N).
#
  while ( x < 8.5 ):
    value = value - 1.0 / x
    x = x + 1.0
#
#  Use Stirling's (actually de Moivre's) expansion.
#
  r = 1.0 / x
  value = value + np.log ( x ) - 0.5 * r
  r = r * r
  value = value \
    - r * ( 1.0 / 12.0 \
    - r * ( 1.0 / 120.0 \
    - r * ( 1.0 / 252.0 \
    - r * ( 1.0 / 240.0 \
    - r * ( 1.0 / 132.0 ) ) ) ) )

  return value

def digamma_test ( ):

#*****************************************************************************80
#
## digamma_test() tests digamma().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'digamma_test():' )
  print ( '  digamma() computes the Digamma or Psi function.' )
  print ( '  Compare the result to tabulated values.' )
  print ( '' )
  print ( '          X         ' ),
  print ( 'FX                        FX2' )
  print ( '                    ' ),
  print ( '(Tabulated)               (DIGAMMA)               DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = digamma ( x )

    print ( '  %12.4g  %24.16g  %24.16g  %10.4g' % ( x, fx, fx2, abs ( fx - fx2 ) ) )

  return

def dipole_cdf ( x, a, b ):

#*****************************************************************************80
#
## dipole_cdf() evaluates the Dipole CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
#    is interesting, and -1.0 <= B <= 1.0.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 0.5 + ( 1.0 / np.pi ) * np.arctan ( x ) + b * b \
    * ( x * np.cos ( 2.0 * a ) - np.sin ( 2.0 * a ) ) \
    / ( np.pi * ( 1.0 + x * x ) )

  return cdf

def dipole_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## dipole_cdf_inv() inverts the Dipole CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    -1.0 <= B <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  it_max = 100
  tol = 0.0001
#
#  Take care of horrible input.
#
  if ( cdf <= 0.0 ):
    x = - np.finfo(float).max
    return x
  elif ( 1.0 <= cdf ):
    x = np.finfo(float).max
    return x
#
#  Seek X1 < X < X2.
#
  x1 = -1.0

  while ( True ):

    cdf1 = dipole_cdf ( x1, a, b )

    if ( cdf1 <= cdf ):
      break

    x1 = 2.0 * x1

  x2 = 1.0

  while ( True ):

    cdf2 = dipole_cdf ( x2, a, b )

    if ( cdf <= cdf2 ):
      break

    x2 = 2.0 * x2
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = dipole_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'dipole_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'dipole_cdf_inv(): Fatal error!' )

    if ( ( cdf3 <= cdf and cdf1 <= cdf ) or ( cdf <= cdf3 and cdf <= cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def dipole_cdf_test ( rng ):

#*****************************************************************************80
#
## dipole_cdf_test() tests dipole_cdf(), dipole_cdf_inv(), dipole_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'dipole_cdf_test():' )
  print ( '  dipole_cdf() evaluates the Dipole CDF.' )
  print ( '  dipole_cdf_inv() inverts the Dipole CDF.' )
  print ( '  dipole_pdf() evaluates the Dipole PDF.' )

  atest = np.array ( [ 0.0, np.pi / 4.0, np.pi / 2.0 ] )
  btest = np.array ( [ 1.0, 0.5, 0.0 ] )

  for itest in range ( 0, 3 ):

    a = atest[itest]
    b = btest[itest]

    check = dipole_check ( a, b )

    if ( not check ):
      print ( '' )
      print ( 'dipole_cdf_test(): Fatal error!' )
      print ( '  The parameters are not legal.' )
      return
  
    print ( '' )
    print ( '  PDF parameter A = %14g' % ( a ) )
    print ( '  PDF parameter B = %14g' % ( b ) )
    print ( '' )
    print ( '       X            PDF           CDF            CDf_inv' )
    print ( '' )

    for i in range ( 0, 10 ):

      x = dipole_sample ( a, b, rng )

      pdf = dipole_pdf ( x, a, b )

      cdf = dipole_cdf ( x, a, b )

      x2 = dipole_cdf_inv ( cdf, a, b )

      print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def dipole_check ( a, b ):

#*****************************************************************************80
#
## dipole_check() checks the parameters of the Dipole CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
#    is interesting, and -1.0 <= B <= 1.0.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b < -1.0 or 1.0 < b ):
    print ( '' )
    print ( 'dipole_check(): Fatal error!' )
    print ( '  -1.0 <= B <= 1.0 is required.' )
    print ( '  The input B = %g' % ( b ) )
    check = False

  return check

def dipole_pdf ( x, a, b ):

#*****************************************************************************80
#
## dipole_pdf() evaluates the Dipole PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) =
#        1 / ( PI * ( 1 + X^2 ) )
#      + B^2 * ( ( 1 - X^2 ) * cos ( 2 * A ) + 2.0 * X * sin ( 2 * A ) )
#      / ( PI * ( 1 + X )^2 )
#
#    Densities of this kind commonly occur in the analysis of resonant
#    scattering of elementary particles.
#
#    dipole_pdf(X)(A,0) = cauchy_pdf(X)(A)
#    A = 0, B = 1 yields the single channel dipole distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Knop,
#    Algorithm 441,
#    ACM Transactions on Mathematical Software.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
#      is interesting,
#    and -1.0 <= B <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = 1.0 / ( np.pi * ( 1.0 + x * x ) ) \
    + b * b * ( ( 1.0 - x * x ) * np.cos ( 2.0 * a ) \
    + 2.0 * x * np.sin ( 2.0 * x ) ) \
    / ( np.pi * ( 1.0 + x * x ) * ( 1.0 + x * x ) )

  return pdf

def dipole_sample ( a, b, rng ):

#*****************************************************************************80
#
## dipole_sample() samples the Dipole PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Knop,
#    Algorithm 441,
#    ACM Transactions on Mathematical Software.
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
#      is interesting,
#    and -1.0 <= B <= 1.0.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np
#
#  Find (X1,X2) at random in a circle.
#
  a2 = b * np.sin ( a )
  b2 = b * np.cos ( a )
  c2 = 1.0

  x1, x2 = disk_sample ( a2, b2, c2, rng )
#
#  The dipole variate is the ratio X1 / X2.
#
  x = x1 / x2

  return x

def dipole_sample_test ( rng ):

#*****************************************************************************80
#
## dipole_sample_test() tests dipole_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000
  ntest = 3

  print ( '' )
  print ( 'dipole_sample_test():' )
  print ( '  dipole_sample() samples the Dipole distribution.' )

  atest = np.array ( [ 0.0, np.pi / 4.0, np.pi / 2.0 ] )
  btest = np.array ( [ 1.0, 0.5, 0.0 ] )

  for itest in range ( 0, 3 ):

    a = atest[itest]
    b = btest[itest]

    check = dipole_check ( a, b )

    if ( not check ):
      print ( '' )
      print ( 'dipole_sample_test(): Fatal error!' )
      print ( '  The parameters are not legal.' )
      return

    print ( '' )
    print ( '  PDF parameter A = %14g' % ( a ) )
    print ( '  PDF parameter B = %14g' % ( b ) )
  
    x = np.zeros ( nsample )

    for i in range ( 0, nsample ):
      x[i] = dipole_sample ( a, b, rng )

    mean = np.mean ( x )
    variance = np.var ( x )
    xmax = np.max ( x )
    xmin = np.min ( x )

    print ( '' )
    print ( '  Sample size =     %6d' % ( nsample ) )
    print ( '  Sample mean =     %14g' % ( mean ) )
    print ( '  Sample variance = %14g' % ( variance ) )
    print ( '  Sample maximum =  %14g' % ( xmax ) )
    print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def dirichlet_mix_check ( comp_num, elem_num, a, comp_weight ):

#*****************************************************************************80
#
## dirichlet_mix_check() checks the parameters of a Dirichlet mixture PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    integer ELEM_NUM, the number of elements of an observation.
#
#    real A(ELEM_NUM,COMP_NUM), the probabilities
#    for element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  for comp_i in range ( 0, comp_num ):

    for elem_i in range ( 0, elem_num ):
      if ( a[elem_i,comp_i] <= 0.0 ):
        print ( '' )
        print ( 'dirichlet_mix_check(): Fatal error!' )
        print ( '  A(ELEM,COMP) <= 0.' )
        print ( '  COMP = %d' % ( comp_i ) )
        print ( '  ELEM = %d' % ( elem_i ) )
        print ( '  A[COMP,ELEM] = %f' % ( a[elem_i,comp_i] ) )
        check = False
        return check

  positive = False

  for comp_i in range ( 0, comp_num ):

    if ( comp_weight[comp_i] < 0.0 ):
      print ( '' )
      print ( 'dirichlet_mix_check(): Fatal error!' )
      print ( '  COMP_WEIGHT(COMP) < 0.' )
      print ( '  COMP = %d' % ( comp_i ) )
      print ( '  COMP_WEIGHT(COMP) = %d' % ( comp_weight[comp_i] ) )
      check = False
      return check
    elif ( 0.0 < comp_weight[comp_i] ):
      positive = True

  if ( not positive ):
    print ( '' )
    print ( 'dirichlet_mix_check(): Fatal error!' )
    print ( '  All component weights are zero.' )
    check = False

  return check

def dirichlet_mix_mean ( comp_num, elem_num, a, comp_weight ):

#*****************************************************************************80
#
## dirichlet_mix_mean() returns the means of a Dirichlet mixture PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    integer ELEM_NUM, the number of elements of an observation.
#
#    real A(ELEM_NUM,COMP_NUM), the probabilities for
#    element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#  Output:
#
#    real MEAN(ELEM_NUM), the means for each element.
#
  import numpy as np

  comp_weight_sum = np.sum ( comp_weight )

  mean = np.zeros ( elem_num )
  a_column = np.zeros ( elem_num )

  for j in range ( 0, comp_num ):
    for i in range ( 0, elem_num ):
      a_column[i] = a[i,j]
    comp_mean = dirichlet_mean ( elem_num, a_column )
    for i in range ( 0, elem_num ):
      mean[i] = mean[i] + comp_weight[j] * comp_mean[i]

  for i in range ( 0, elem_num ):
    mean[i] = mean[i] / comp_weight_sum

  return mean

def dirichlet_mix_pdf ( x, comp_num, elem_num, a, comp_weight ):

#*****************************************************************************80
#
## dirichlet_mix_pdf() evaluates a Dirichlet mixture PDF.
#
#  Discussion:
#
#    The PDF is a weighted sum of Dirichlet PDF's.  Each PDF is a
#    "component", with an associated weight.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(ELEM_NUM), the argument of the PDF.
#
#    integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    integer ELEM_NUM, the number of elements of an observation.
#
#    real A(ELEM_NUM,COMP_NUM), the probabilities for
#    element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  comp_weight_sum = np.sum ( comp_weight )

  a_column = np.zeros ( elem_num )

  pdf = 0.0

  for j in range ( 0, comp_num ):

    for i in range ( 0, elem_num ):
      a_column[i] = a[i,j]

    comp_pdf = dirichlet_pdf ( x, elem_num, a_column )

    pdf = pdf + comp_weight[j] * comp_pdf / comp_weight_sum

  return pdf

def dirichlet_mix_pdf_test ( ):

#*****************************************************************************80
#
## dirichlet_mix_pdf_test() tests dirichlet_mix_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  comp_num = 2
  elem_num = 3

  print ( '' )
  print ( 'dirichlet_mix_pdf_test():' )
  print ( '  dirichlet_mix_pdf() evaluates the Dirichlet Mix PDF.' )

  x = np.array ( [ 0.500, 0.125, 0.375 ] )

  a = np.array ( [ \
    [ 0.250, 1.500 ], \
    [ 0.500, 0.500 ], \
    [ 1.250, 2.000 ] ] )

  comp_weight = np.array ( [ 1.0, 2.0 ] )

  check = dirichlet_mix_check ( comp_num, elem_num, a, comp_weight )

  if ( not check ):
    print ( '' )
    print ( 'dirichlet_mix_pdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '  Number of elements ELEM_NUM =   %6d' % ( elem_num ) )
  print ( '  Number of components COMP_NUM = %6d' % ( comp_num ) )

  r8mat_print ( elem_num, comp_num, a, '  PDF parameters A(ELEM,COMP):' )

  r8vec_print ( comp_num, comp_weight, '  Component weights:' )

  pdf = dirichlet_mix_pdf ( x, comp_num, elem_num, a, comp_weight )

  print ( '' )
  print ( '  PDF value =           %14g' % ( pdf ) )

  return

def dirichlet_mix_sample ( comp_num, elem_num, a, comp_weight, rng ):

#*****************************************************************************80
#
## dirichlet_mix_sample() samples a Dirichlet mixture PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    integer ELEM_NUM, the number of elements of an observation.
#
#    real A(ELEM_NUM,COMP_NUM), the probabilities for
#    element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#  Output:
#
#    real X(ELEM_NUM), a sample of the PDF.
#
#    integer COMP, the index of the component of the Dirichlet
#    mixture that was chosen to generate the sample.
#
  import numpy as np
#
#  Choose a particular density component COMP.
#
  comp = discrete_sample ( comp_num, comp_weight, rng )
#
#  Sample the density number COMP.
#
  a_column = np.zeros ( elem_num )
  for i in range ( 0, elem_num ):
    a_column[i] = a[i,comp-1]

  x = dirichlet_sample ( elem_num, a_column, rng )

  return x, comp

def dirichlet_mix_sample_test ( rng ):

#*****************************************************************************80
#
## dirichlet_mix_sample_test() tests dirichlet_mix_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  comp_num = 2
  elem_num = 3
  sample_num = 1000

  print ( '' )
  print ( 'dirichlet_mix_sample_test():' )
  print ( '  dirichlet_mix_sample() samples the Dirichlet Mix distribution' )
  print ( '  dirichlet_mix_mean() computes the Dirichlet Mix mean' )

  a = np.array ( [ \
    [ 0.250, 1.500 ], \
    [ 0.500, 0.500 ], \
    [ 1.250, 2.000 ] ] )

  comp_weight = np.array ( [ 1.0, 2.0 ] )

  check = dirichlet_mix_check ( comp_num, elem_num, a, comp_weight )

  if ( not check ):
    print ( '' )
    print ( 'dirichlet_mix_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  Number of elements ELEM_NUM =   %6d' % ( elem_num ) )
  print ( '  Number of components COMP_NUM = %6d' % ( comp_num ) )

  r8mat_print ( elem_num, comp_num, a, '  PDF parameters A(ELEM,COMP):' )

  r8vec_print ( comp_num, comp_weight, '  Component weights:' )

  mean = dirichlet_mix_mean ( comp_num, elem_num, a, comp_weight )

  r8vec_print ( elem_num, mean, '  PDF mean:' )

  x = np.zeros ( [ elem_num, sample_num ] )
  for j in range ( 0, sample_num ):
    v, comp = dirichlet_mix_sample ( comp_num, elem_num, a, comp_weight, rng )
    for i in range ( 0, elem_num ):
      x[i,j] = v[i]

  xmax = r8row_max ( elem_num, sample_num, x )

  xmin = r8row_min ( elem_num, sample_num, x )

  mean = r8row_mean ( elem_num, sample_num, x )

  variance = r8row_variance ( elem_num, sample_num, x )

  print ( '' )
  print ( '  Sample size = %6d' % ( sample_num ) )
  print ( '' )
  print ( '  Observed Min, Max, Mean, Variance:' )
  print ( '' )

  for i in range ( 0, elem_num ):
    print ( '  %6d  %14g  %14g  %14g  %14g' \
    % ( i, xmin[i], xmax[i], mean[i], variance[i] ) )

  return

def dirichlet_check ( n, a ):

#*****************************************************************************80
#
## dirichlet_check() checks the parameters of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components.
#
#    real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True
  positive = False

  for i in range ( 0, n ):

    if ( a[i] <= 0.0 ):
      print ( '' )
      print ( 'dirichlet_check(): Fatal error!' )
      print ( '  A(I) <= 0.' )
      print ( '  For I = %d' % ( i ) )
      print ( '  A(I) = %f' % ( a[i] ) )
      check = False
      return check
    elif ( 0.0 < a[i] ):
      positive = True

  if ( not positive ):
    print ( '' )
    print ( 'dirichlet_check(): Fatal error!' )
    print ( '  All parameters are zero!' )
    check = False

  return check

def dirichlet_mean ( n, a ):

#*****************************************************************************80
#
## dirichlet_mean() returns the means of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components.
#
#    real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#  Output:
#
#    real MEAN(N), the means of the PDF.
#
  import numpy as np
  
  a_sum = np.sum ( a )

  mean = np.zeros ( n )
  for i in range ( 0, n ):
    mean[i] = a[i] / a_sum

  return mean

def dirichlet_moment2 ( n, a ):

#*****************************************************************************80
#
## dirichlet_moment2() returns the second moments of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components.
#
#    real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#  Output:
#
#    real M2(N,N), the second moments of the PDF.
#
  import numpy as np

  a_sum = np.sum ( a )

  m2 = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        m2[i,j] = a[i] * ( a[i] + 1.0 ) / ( a_sum * ( a_sum + 1.0 ) )
      else:
        m2[i,j] = a[i] * a[j] / ( a_sum * ( a_sum + 1.0 ) )

  return m2

def dirichlet_pdf ( x, n, a ):

#*****************************************************************************80
#
## dirichlet_pdf() evaluates the Dirichlet PDF.
#
#  Discussion:
#
#    PDF(X)(N,A) = Product ( 1 <= I <= N ) X(I)^( A(I) - 1 )
#      * Gamma ( A_SUM ) / A_PROD
#
#    where
#
#      0 < A(I) for all I
#      0 <= X(I) for all I
#      Sum ( 1 <= I <= N ) X(I) = 1
#      A_SUM = Sum ( 1 <= I <= N ) A(I).
#      A_PROD = Product ( 1 <= I <= N ) Gamma ( A(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the argument of the PDF.  Each X(I) should
#    be greater than 0.0, and the X(I)'s must add up to 1.0.
#
#    integer N, the number of components.
#
#    real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  from scipy.special import gamma
  import numpy as np

  tol = 0.0001

  for i in range ( 0, n ):
    if ( x[i] <= 0.0 ):
      print ( '' )
      print ( 'dirichlet_pdf(): Fatal error!' )
      print ( '  X(I) <= 0.' )
      raise Exception ( 'dirichlet_pdf(): Fatal error!' )

  x_sum = np.sum ( x )

  if ( tol < abs ( x_sum - 1.0 ) ):
    print ( '' )
    print ( 'dirichlet_pdf(): Fatal error!' )
    print ( '  SUM X(I) =/= 1.' )

  a_sum = np.sum ( a )

  a_prod = 1.0
  for i in range ( 0, n ):
    a_prod = a_prod * gamma ( a[i] )

  pdf = gamma ( a_sum ) / a_prod
  for i in range ( 0, n ):
    pdf = pdf * x[i] ** ( a[i] - 1.0 )

  return pdf

def dirichlet_pdf_test ( ):

#*****************************************************************************80
#
## dirichlet_pdf_test() tests dirichlet_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'dirichlet_pdf_test():' )
  print ( '  dirichlet_pdf() evaluates the Dirichlet PDF.' )

  x = np.array ( [ 0.500, 0.125, 0.375 ] )

  a = np.array ( [ 0.250, 0.500, 1.250 ] )

  check = dirichlet_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'dirichlet_pdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  Number of components N = %6d' % ( n ) )

  r8vec_print ( n, a, '  PDF parameters A:' )
  r8vec_print ( n, x, '  PDF arguments X:' )

  pdf = dirichlet_pdf ( x, n, a )

  print ( '' )
  print ( '  PDF value = %14g' % ( pdf ) )

  return

def dirichlet_sample ( n, a, rng ):

#*****************************************************************************80
#
## dirichlet_sample() samples the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 169.
#
#  Input:
#
#    integer N, the number of components.
#
#    real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#  Output:
#
#    real X(N), a sample of the PDF.  The entries
#    of X should sum to 1.
#
  import numpy as np

  a2 = 0.0
  b2 = 1.0

  x = np.zeros ( n )

  for i in range ( 0, n ):
    c2 = a[i]
    x[i] = gamma_sample ( a2, b2, c2, rng )
#
#  Rescale the vector to have unit sum.
#
  x_sum = np.sum ( x )
  for i in range ( 0, n ):
    x[i] = x[i] / x_sum

  return x

def dirichlet_sample_test ( rng ):

#*****************************************************************************80
#
## dirichlet_sample_test() tests dirichlet_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 3
  nsample = 1000

  print ( '' )
  print ( 'dirichlet_sample_test():' )
  print ( '  dirichlet_sample() samples the Dirichlet distribution' )
  print ( '  dirichlet_mean() computes the Dirichlet mean' )
  print ( '  dirichlet_variance() computes the Dirichlet variance.' )

  a = np.array ( [ 0.250, 0.500, 1.250 ] )

  check = dirichlet_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'dirichlet_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  Number of components N = %6d' % ( n ) )

  r8vec_print ( n, a, '  PDF parameters A:' )

  mean = dirichlet_mean ( n, a )

  variance = dirichlet_variance ( n, a )

  print ( '' )
  print ( '  PDF mean, variance:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %6d  %14g  %14g' % ( i, mean[i], variance[i] ) )

  m2 = dirichlet_moment2 ( n, a )
  
  r8mat_print ( n, n, m2, '  Second moment matrix:' )

  x = np.zeros ( [ n, nsample ] )
  for j in range ( 0, nsample ):
    v = dirichlet_sample ( n, a, rng )
    for i in range ( 0, n ):
      x[i,j] = v[i]
 
  xmax = r8row_max ( n, nsample, x )
  xmin = r8row_min ( n, nsample, x )
  mean = r8row_mean ( n, nsample, x )
  variance = r8row_variance ( n, nsample, x )

  print ( '' )
  print ( '  Sample size = %d' % ( nsample ) )

  print ( '' )
  print ( '  Observed Min, Max, Mean, Variance:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %6d  %14g  %14g  %14g  %14g' \
    % ( i, xmin[i], xmax[i], mean[i], variance[i] ) )

  return

def dirichlet_variance ( n, a ):

#*****************************************************************************80
#
## dirichlet_variance() returns the variances of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components.
#
#    real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#  Output:
#
#    real VARIANCE(N), the variances of the PDF.
#
  import numpy as np

  a_sum = np.sum ( a )

  variance = np.zeros ( n )

  for i in range ( 0, n ):
    variance[i] = a[i] * ( a_sum - a[i] ) / ( a_sum ** 2 * ( a_sum + 1.0 ) )

  return variance

def discrete_cdf ( x, a, b ):

#*****************************************************************************80
#
## discrete_cdf() evaluates the Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the item whose probability is desired.
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of outcomes
#    1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < 1 ):
    cdf = 0.0
  elif ( x < a ):
    cdf = np.sum ( b[0:x] ) / np.sum ( b[0:a] )
  elif ( a <= x ):
    cdf = 1.0

  return cdf

def discrete_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## discrete_cdf_inv() inverts the Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of outcomes
#    1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    integer X, the corresponding argument for which
#    CDF(X-1) < CDF <= CDF(X)
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'discrete_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'discrete_cdf_inv(): Fatal error!' )

  b_sum = np.sum ( b[0:a] )

  cum = 0.0
  x = a

  for j in range ( 0, a ):

    cum = cum + b[j] / b_sum

    if ( cdf <= cum ):
      x = j + 1
      break

  return x

def discrete_cdf_test ( rng ):

#*****************************************************************************80
#
## discrete_cdf_test() tests discrete_cdf(), discrete_cdf_inv(), discrete_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  a = 6

  print ( '' )
  print ( 'discrete_cdf_test():' )
  print ( '  discrete_cdf() evaluates the Discrete CDF' )
  print ( '  discrete_cdf_inv() inverts the Discrete CDF.' )
  print ( '  discrete_pdf() evaluates the Discrete PDF' )

  b = np.array ( [ 1.0, 2.0, 6.0, 2.0, 4.0, 1.0 ] )

  check = discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'discrete_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
 
  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )

  r8vec_print ( a, b, '  PDF parameters B:' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = discrete_sample ( a, b, rng )

    pdf = discrete_pdf ( x, a, b )

    cdf = discrete_cdf ( x, a, b )

    x2 = discrete_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def discrete_check ( a, b ):

#*****************************************************************************80
#
## discrete_check() checks the parameters of the Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  import numpy as np

  check = True

  for j in range ( 0, a ):
    if ( b[j] < 0.0 ):
      print ( '' )
      print ( 'discrete_check(): Fatal error!' )
      print ( '  Negative probabilities not allowed.' )
      check = False

  b_sum = np.sum ( b )

  if ( b_sum == 0.0 ):
    print ( '' )
    print ( 'discrete_check(): Fatal error!' )
    print ( '  Total probablity is zero.' )
    check = False

  return check

def discrete_mean ( a, b ):

#*****************************************************************************80
#
## discrete_mean() evaluates the mean of the Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  mean = 0.0
  for j in range ( 0, a ):
    mean = mean + float ( j + 1 ) * b[j]

  mean = mean / b_sum

  return mean

def discrete_pdf ( x, a, b ):

#*****************************************************************************80
#
## discrete_pdf() evaluates the Discrete PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = B(X) if 1 <= X <= A
#                = 0    otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the item whose probability is desired.
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  if ( 1 <= x and x <= a ):
    pdf = b[x-1] / b_sum
  else:
    pdf = 0.0

  return pdf

def discrete_sample ( a, b, rng ):

#*****************************************************************************80
#
## discrete_sample() samples the Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  cdf = rng.random ( )

  x = discrete_cdf_inv ( cdf, a, b )

  return x

def discrete_sample_test ( rng ):

#*****************************************************************************80
#
## discrete_sample_test() tests discrete_mean(), discrete_sample(), discrete_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  a = 6
  nsample = 1000

  print ( '' )
  print ( 'discrete_sample_test():' )
  print ( '  discrete_mean() computes the Discrete mean' )
  print ( '  discrete_sample() samples the Discrete distribution' )
  print ( '  discrete_variance() computes the Discrete variance.' )

  b = np.array ( [ 1.0, 2.0, 6.0, 2.0, 4.0, 1.0 ] )

  check = discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'discrete_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = discrete_mean ( a, b )
  variance = discrete_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )

  r8vec_print ( a, b, '  PDF parameters B:' )

  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )  
  for i in range ( 0,  nsample ):
    x[i] = discrete_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def discrete_variance ( a, b ):

#*****************************************************************************80
#
## discrete_variance() evaluates the variance of the Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of probabilities assigned.
#
#    real B(A), the relative probabilities of
#    outcomes 1 through A.  Each entry must be nonnegative.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  b_sum = np.sum ( b )

  mean = discrete_mean ( a, b )

  variance = 0.0
  for j in range ( 0, a ):
    variance = variance + b[j] * ( j + 1 - mean ) ** 2

  variance = variance / b_sum

  return variance

def disk_mean ( a, b, c ):

#*****************************************************************************80
#
## disk_mean() returns the mean of points in a disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the disk.
#    The disk is centered at (A,B) and has radius C.
#    0.0 < C.
#
#  Output:
#
#    real MEAN(2), the mean.
#
  import numpy as np

  mean = np.array ( [ a, b ] )

  return mean

def disk_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## disk_sample() samples points from a disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the disk.
#    The disk is centered at (A,B) and has radius C.
#    0.0 < C.
#
#  Output:
#
#    real X1, X2, a sampled point of the disk.
#
  import numpy as np

  radius_frac = rng.random ( )
  radius_frac = np.sqrt ( radius_frac )

  angle = rng.random ( )
  angle = 2.0 * np.pi * angle

  x1 = a + c * radius_frac * np.cos ( angle )
  x2 = b + c * radius_frac * np.sin ( angle )

  return x1, x2

def disk_sample_test ( rng ):

#*****************************************************************************80
#
## disk_sample_test() tests disk_mean(), disk_sample(), disk_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'disk_sample_test():' )
  print ( '  disk_mean() returns the Disk mean.' )
  print ( '  disk_sample() samples the Disk distribution.' )
  print ( '  disk_variance() returns the Disk variance.' )

  a = 10.0
  b = 4.0
  c = 5.0

  print ( '' )
  print ( '  X coordinate of center is A = %14g' % ( a ) )
  print ( '  Y coordinate of center is B = %14g' % ( b ) )
  print ( '  Radius is C =                 %14g' % ( c ) )

  mean = disk_mean ( a, b, c )
  v = disk_variance ( a, b, c )

  print ( '' )
  print ( '  Disk mean =     %14g  %14g' % ( mean[0], mean[1] ) )
  print ( '  Disk variance = %14g' % ( v ) )

  x_table = np.zeros ( nsample )
  y_table = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x, y = disk_sample ( a, b, c, rng )
    x_table[i] = x
    y_table[i] = y

  variance = 0.0
  for i in range ( 0, nsample ):
    variance = variance + ( x_table[i] - a ) ** 2 \
                        + ( y_table[i] - b ) ** 2 
  variance = variance / nsample

  xmax = np.zeros ( 2 )
  xmin = np.zeros ( 2 )

  xmean = np.mean ( x_table )
  xmax = np.max ( x_table )
  xmin = np.min ( x_table )

  ymean = np.mean ( y_table )
  ymax = np.max ( y_table )
  ymin = np.min ( y_table )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g  %14g' % ( xmean, ymean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g  %14g' % ( xmax, ymax ) )
  print ( '  Sample minimum =  %14g  %14g' % ( xmin, ymin ) )

  return

def disk_variance ( a, b, c ):

#*****************************************************************************80
#
## disk_variance() returns the variance of points in a disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the disk.
#    The disk is centered at (A,B) and has radius C.
#    0.0 < C.
#
#  Output:
#
#    real VARIANCE, the variance.
#
  variance = 0.5 * c * c

  return variance

def empirical_discrete_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## empirical_discrete_cdf() evaluates the Empirical Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 0.0

  bsum = np.sum ( b )

  for i in range ( 0, a ):

    if ( x < c[i] ):
      break

    cdf = cdf + b[i] / bsum

  return cdf

def empirical_discrete_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## empirical_discrete_cdf_inv() inverts the Empirical Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    real X, the smallest argument whose CDF is greater
#    than or equal to CDF.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'empirical_discrete_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'empirical_discrete_cdf_inv(): Fatal error!' )

  bsum = np.sum ( b )

  x = c[0]
  cdf2 = b[0] / bsum

  for i in range ( 1, a ):

    if ( cdf <= cdf2 ):
      break

    x = c[i]
    cdf2 = cdf2 + b[i] / bsum

  return x

def empirical_discrete_cdf_test ( rng ):

#*****************************************************************************80
#
## empirical_discrete_cdf_test() tests empirical_discrete_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  a = 6

  b = np.array ( [ 1.0, 1.0, 3.0, 2.0, 1.0, 2.0 ] )
  c = np.array ( [ 0.0, 1.0, 2.0, 4.5, 6.0, 10.0 ] )

  print ( '' )
  print ( 'empirical_discrete_cdf_test():' )
  print ( '  empirical_discrete_cdf() evaluates the Empirical Discrete CDF' )
  print ( '  empirical_discrete_cdf_inv() inverts the Empirical Discrete CDF.' )
  print ( '  empirical_discrete_pdf() evaluates the Empirical Discrete PDF' )

  check = empirical_discrete_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'empirical_discrete_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )
  r8vec_print ( a, b, '  PDF parameter B:' )
  r8vec_print ( a, c, '  PDF parameter C:' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = empirical_discrete_sample ( a, b, c, rng )

    pdf = empirical_discrete_pdf ( x, a, b, c )

    cdf = empirical_discrete_cdf ( x, a, b, c )

    x2 = empirical_discrete_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def empirical_discrete_check ( a, b, c ):

#*****************************************************************************80
#
## empirical_discrete_check() checks the parameters of the Empirical Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  import numpy as np

  check = True

  if ( a <= 0 ):
    print ( '' )
    print ( 'empirical_discrete_check(): Fatal error!' )
    print ( '  A must be positive.' )
    print ( '  Input A = %d' % ( a ) )
    print ( '  A is the number of weights.' )
    check = False

  for i in range ( 0, a ):
    if ( ( b[i] < 0.0 ) ):
      print ( '' )
      print ( 'empirical_discrete_check(): Fatal error!' )
      print ( '  Some B(*) < 0.' )
      print ( '  But all B values must be nonnegative.' )
      check = False

  if ( np.sum ( b ) == 0 ):
    print ( '' )
    print ( 'empirical_discrete_check(): Fatal error!' )
    print ( '  All B(*) = 0.' )
    print ( '  But at least one B values must be nonzero.' )
    check = False

  for i in range ( 0, a ):
    for j in range ( i + 1, a ):
      if ( c[i] == c[j] ):
        print ( '' )
        print ( 'empirical_discrete_check(): Fatal error!' )
        print ( '  All values C must be unique.' )
        print ( '  But at least two values are identical.' )
        check = False

  for i in range ( 0, a - 1 ):
    if ( c[i+1] < c[i] ):
      print ( '' )
      print ( 'empirical_discrete_check(): Fatal error!' )
      print ( '  The values in C must be in ascending order.' )
      check = False

  return check

def empirical_discrete_mean ( a, b, c ):

#*****************************************************************************80
#
## empirical_discrete_mean() returns the mean of the Empirical Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = np.dot ( b, c ) / np.sum ( b )

  return mean

def empirical_discrete_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## empirical_discrete_pdf() evaluates the Empirical Discrete PDF.
#
#  Discussion:
#
#    A set of A values C(1:A) are assigned nonnegative weights B(1:A),
#    with at least one B nonzero.  The probability of C(I) is the
#    value of B(I) divided by the sum of the weights.
#
#    The C's must be distinct, and given in ascending order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = 0.0

  for i in range ( 0, a ):
    if ( x == c[i] ):
      pdf = b[i] / np.sum ( b )
      break
 
  return pdf

def empirical_discrete_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## empirical_discrete_sample() samples the Empirical Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = empirical_discrete_cdf_inv ( cdf, a, b, c )

  return x

def empirical_discrete_sample_test ( rng ):

#*****************************************************************************80
#
## empirical_discrete_sample_test() tests empirical_discrete_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  a = 6
  nsample = 1000

  b = np.array ( [ 1.0, 1.0, 3.0, 2.0, 1.0, 2.0 ] )
  c = np.array ( [ 0.0, 1.0, 2.0, 4.5, 6.0, 10.0 ] )

  print ( '' )
  print ( 'empirical_discrete_sample_test():' )
  print ( '  empirical_discrete_mean() computes the Empirical Discrete mean' )
  print ( '  empirical_discrete_sample() samples the Empirical Discrete distribution' )
  print ( '  empirical_discrete_variance() computes the Empirical Discrete variance.' )

  check = empirical_discrete_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'empirical_discrete_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = empirical_discrete_mean ( a, b, c )
  variance = empirical_discrete_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )
  r8vec_print ( a, b, '  PDF parameter B:' )
  r8vec_print ( a, c, '  PDF parameter C:' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = empirical_discrete_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def empirical_discrete_variance ( a, b, c ):

#*****************************************************************************80
#
## empirical_discrete_variance() returns the variance of the Empirical Discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of values.
#    0 < A.
#
#    real B(A), the weights of each value.
#    0 <= B(1:A) and at least one value is nonzero.
#
#    real C(A), the values.
#    The values must be distinct and in ascending order.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  bsum = np.sum ( b )

  mean = empirical_discrete_mean ( a, b, c )

  variance = 0.0

  for i in range ( 0, a ):
    variance = variance + ( b[i] / bsum ) * ( c[i] - mean ) ** 2

  return variance

def english_letter_cdf_inv ( cdf ):

#*****************************************************************************80
#
## english_letter_cdf_inv() inverts the English Letter CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Lewand,
#    Cryptological Mathematics,
#    Mathematics Association of America, 2000,
#    ISBN13: 978-0883857199
#
#  Input:
#
#    real CDF, a cumulative probability between 0 and 1.
#
#  Output:
#
#    character C, the corresponding letter.
#
  import numpy as np

  cdf_vec = np.array ( [ \
    0.00000, \
    0.08167, 0.09659, 0.12441, 0.16694, 0.29396, \
    0.31624, 0.33639, 0.39733, 0.46699, 0.46852, \
    0.47624, 0.51649, 0.54055, 0.60804, 0.68311, \
    0.70240, 0.70335, 0.76322, 0.82649, 0.91705, \
    0.94463, 0.95441, 0.97802, 0.97952, 0.99926, \
    1.00000 ] )

  c = ' '

  for i in range ( 1, 27 ):
    if ( cdf <= cdf_vec[i] ):
      c = chr ( ord ( 'a' ) + i - 1 )
      break

  return c

def english_letter_cdf ( c ):

#*****************************************************************************80
#
## english_letter_cdf() evaluates the English Letter CDF.
#
#  Discussion:
#
#    CDF('c') = 0.12441
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Lewand,
#    Cryptological Mathematics,
#    Mathematics Association of America, 2000,
#    ISBN13: 978-0883857199
#
#  Input:
#
#    character C, the letter whose probability is desired.
#    'a' <= c <= 'z', but case is ignored.
#
#  Output:
#
#    real CDF, the probability that a random letter is less
#    than or equal to C.
#
  import numpy as np

  cdf_vec = np.array ( [ \
    0.00000, \
    0.08167, 0.09659, 0.12441, 0.16694, 0.29396, \
    0.31624, 0.33639, 0.39733, 0.46699, 0.46852, \
    0.47624, 0.51649, 0.54055, 0.60804, 0.68311, \
    0.70240, 0.70335, 0.76322, 0.82649, 0.91705, \
    0.94463, 0.95441, 0.97802, 0.97952, 0.99926, \
    1.00000 ] )

  if ( 'a' <= c and c <= 'z' ):
    i = ord ( c ) - ord ( 'a' ) + 1
    cdf = cdf_vec[i]
  elif ( 'A' <= c and c <= 'Z' ):
    i = ord ( c ) - ord ( 'A' ) + 1
    cdf = cdf_vec[i]
  else:
    cdf = 0.0

  return cdf

def english_letter_cdf_test ( rng ):

#*****************************************************************************80
#
## english_letter_cdf_test() tests english_letter_cdf(), english_letter_cdf_inv(), english_letter_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'english_letter_cdf_test():' )
  print ( '  english_letter_cdf() evaluates the English Letter CDF' )
  print ( '  english_letter_cdf_inv() inverts the English Letter CDF.' )
  print ( '  english_letter_pdf() evaluates the English Letter PDF' )

  print ( '' )
  print ( '   C              PDF             CDF    CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    c = english_letter_sample ( rng )

    pdf = english_letter_pdf ( c )

    cdf = english_letter_cdf ( c )

    c2 = english_letter_cdf_inv ( cdf )

    print ( '  \'%c\'  %14g  %14g        \'%c\'' % ( c, pdf, cdf, c2 ) )

  return

def english_letter_pdf ( c ):

#*****************************************************************************80
#
## english_letter_pdf() evaluates the English Letter PDF.
#
#  Discussion:
#
#    PDF('c') = 0.02782
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Lewand,
#    Cryptological Mathematics,
#    Mathematics Association of America, 2000,
#    ISBN13: 978-0883857199
#
#  Input:
#
#    character C, the letter whose probability is desired.
#    'a' <= c <= 'z', but case is ignored.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf_vec = np.array ( [ \
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, \
    0.02228, 0.02015, 0.06094, 0.06966, 0.00153, \
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507, \
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056, \
    0.02758, 0.00978, 0.02361, 0.00150, 0.01974, \
    0.00074 ] )

  if ( 'a' <= c and c <= 'z' ):
    i = ord ( c ) - ord ( 'a' )
    pdf = pdf_vec[i]
  elif ( 'A' <= c and c <= 'Z' ):
    i = ord ( c ) - ord ( 'A' )
    pdf = pdf_vec[i]
  else:
    pdf = 0.0

  return pdf

def english_letter_sample ( rng ):

#*****************************************************************************80
#
## english_letter_sample() samples the English Letter PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    character C, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  c = english_letter_cdf_inv ( cdf )

  return c

def english_sentence_length_cdf ( x ):

#*****************************************************************************80
#
## english_sentence_length_cdf() evaluates the English Sentence Length CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Input:
#
#    integer X, the word length whose CDF is desired.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  if ( x < 1 ):
    cdf = 0.0
  elif ( x < word_length_max ):
    cdf = np.sum ( pdf_vec[0:x] ) / pdf_sum
  elif ( word_length_max <= x ):
    cdf = 1.0

  return cdf

def english_sentence_length_cdf_inv ( cdf ):

#*****************************************************************************80
#
## english_sentence_length_cdf_inv() inverts the English Sentence Length CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    integer X, the corresponding word length for which
#    CDF(X-1) < CDF <= CDF(X)
#
  import numpy as np

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'english_word_length_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'english_word_length_cdf_inv(): Fatal error!' )

  cum = 0.0

  for j in range ( 0, word_length_max ):

    cum = cum + pdf_vec[j]

    if ( cdf <= cum / pdf_sum ):
      x = j + 1
      return x

  x = word_length_max
  
  return x

def english_sentence_length_cdf_test ( rng ):

#*****************************************************************************80
#
## english_sentence_length_cdf_test() tests english_sentence_length_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'english_sentence_length_cdf_test():' )
  print ( '  english_sentence_length_cdf() evaluates the English Sentence Length CDF' )
  print ( '  english_sentence_length_cdf_inv() inverts the English Sentence Length CDF.' )
  print ( '  english_sentence_length_pdf() evaluates the English Sentence Length PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = english_sentence_length_sample ( rng )

    pdf = english_sentence_length_pdf ( x )

    cdf = english_sentence_length_cdf ( x )

    x2 = english_sentence_length_cdf_inv ( cdf )

    print ( '  %12d  %12g  %12g  %12d' % ( x, pdf, cdf, x2 ) )

  return

def english_sentence_length_mean ( ):

#*****************************************************************************80
#
## english_sentence_length_mean() evaluates the mean of the English Sentence Length PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + float ( j + 1 ) * pdf_vec[j]

  mean = mean / pdf_sum

  return mean

def english_sentence_length_pdf ( x ):

#*****************************************************************************80
#
## english_sentence_length_pdf() evaluates the English Sentence Length PDF.
#
#  Discussion:
#
#    PDF(A,BX) = B(X) if 1 <= X <= A
#                = 0    otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Input:
#
#    integer X, the word length whose probability is desired.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  if ( 1 <= x and x <= word_length_max ):
    pdf = pdf_vec[x-1] / pdf_sum
  else:
    pdf = 0.0

  return pdf

def english_sentence_length_sample ( rng ):

#*****************************************************************************80
#
## english_sentence_length_sample() samples the English Sentence Length PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = english_sentence_length_cdf_inv ( cdf )

  return x

def english_sentence_length_sample_test ( rng ):

#*****************************************************************************80
#
## english_sentence_length_sample_test() tests english_sentence_length_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000

  print ( '' )
  print ( 'english_sentence_length_sample_test():' )
  print ( '  english_sentence_length_mean() computes the English Sentence Length mean' )
  print ( '  english_sentence_length_sample() samples the English Sentence Length distribution' )
  print ( '  english_sentence_length_variance() computes the English Sentence Length variance.' )

  mean = english_sentence_length_mean ( )
  variance = english_sentence_length_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = english_sentence_length_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %12d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def english_sentence_length_variance ( ):

#*****************************************************************************80
#
## english_sentence_length_variance(): variance of the English Sentence Length PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  word_length_max = 79

  pdf_vec = np.array ( [ \
    0.00806, \
    0.01370, \
    0.01862, \
    0.02547, \
    0.03043, \
    0.03189, \
    0.03516, \
    0.03545, \
    0.03286, \
    0.03533, \
    0.03562, \
    0.03788, \
    0.03669, \
    0.03751, \
    0.03518, \
    0.03541, \
    0.03434, \
    0.03305, \
    0.03329, \
    0.03103, \
    0.02867, \
    0.02724, \
    0.02647, \
    0.02526, \
    0.02086, \
    0.02178, \
    0.02128, \
    0.01801, \
    0.01690, \
    0.01556, \
    0.01512, \
    0.01326, \
    0.01277, \
    0.01062, \
    0.01051, \
    0.00901, \
    0.00838, \
    0.00764, \
    0.00683, \
    0.00589, \
    0.00624, \
    0.00488, \
    0.00477, \
    0.00406, \
    0.00390, \
    0.00350, \
    0.00318, \
    0.00241, \
    0.00224, \
    0.00220, \
    0.00262, \
    0.00207, \
    0.00174, \
    0.00174, \
    0.00128, \
    0.00121, \
    0.00103, \
    0.00117, \
    0.00124, \
    0.00082, \
    0.00088, \
    0.00061, \
    0.00061, \
    0.00075, \
    0.00063, \
    0.00056, \
    0.00052, \
    0.00057, \
    0.00031, \
    0.00029, \
    0.00021, \
    0.00017, \
    0.00021, \
    0.00034, \
    0.00031, \
    0.00011, \
    0.00011, \
    0.00008, \
    0.00006 ] )

  pdf_sum = 0.99768

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + ( j + 1 ) * pdf_vec[j]
  mean = mean / pdf_sum

  variance = 0.0
  for j in range ( 0, word_length_max ):
    variance = variance + pdf_vec[j] * ( j + 1 - mean ) ** 2 

  variance = variance / pdf_sum

  return variance

def english_word_length_cdf ( x ):

#*****************************************************************************80
#
## english_word_length_cdf() evaluates the English Word Length CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Input:
#
#    integer X, the word length whose CDF is desired.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  if ( x < 1 ):
    cdf = 0.0
  elif ( x < word_length_max ):
    cdf = np.sum ( pdf_vec[0:x] ) / pdf_sum
  elif ( word_length_max <= x ):
    cdf = 1.0

  return cdf

def english_word_length_cdf_inv ( cdf ):

#*****************************************************************************80
#
## english_word_length_cdf_inv() inverts the English Word Length CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    integer X, the corresponding word length for which
#    CDF(X-1) < CDF <= CDF(X)
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'english_word_length_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'english_word_length_cdf_inv(): Fatal error!' )

  cum = 0.0

  for j in range ( 0, word_length_max ):

    cum = cum + pdf_vec[j]

    if ( cdf <= cum / pdf_sum ):
      x = j + 1
      return x

  x = word_length_max
  
  return x

def english_word_length_cdf_test ( rng ):

#*****************************************************************************80
#
## english_word_length_cdf_test() tests english_word_length_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'english_word_length_cdf_test():' )
  print ( '  english_word_length_cdf() evaluates the English Word Length CDF' )
  print ( '  english_word_length_cdf_inv() inverts the English Word Length CDF.' )
  print ( '  english_word_length_pdf() evaluates the English Word Length PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = english_word_length_sample ( rng )

    pdf = english_word_length_pdf ( x )

    cdf = english_word_length_cdf ( x )

    x2 = english_word_length_cdf_inv ( cdf )

    print ( '  %12d  %12g  %12g  %12d' % ( x, pdf, cdf, x2 ) )

  return

def english_word_length_mean ( ):

#*****************************************************************************80
#
## english_word_length_mean() evaluates the mean of the English Word Length PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + ( j + 1 ) * pdf_vec[j]

  mean = mean / pdf_sum

  return mean

def english_word_length_pdf ( x ):

#*****************************************************************************80
#
## english_word_length_pdf() evaluates the English Word Length PDF.
#
#  Discussion:
#
#    PDF(A,BX) = B(X) if 1 <= X <= A
#                = 0    otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Input:
#
#    integer X, the word length whose probability is desired.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  if ( 1 <= x and x <= word_length_max ):
    pdf = pdf_vec[x-1] / pdf_sum
  else:
    pdf = 0.0

  return pdf

def english_word_length_sample ( rng ):

#*****************************************************************************80
#
## english_word_length_sample() samples the English Word Length PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = english_word_length_cdf_inv ( cdf )

  return x

def english_word_length_sample_test ( rng ):

#*****************************************************************************80
#
## english_word_length_sample_test() tests english_word_length_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000

  print ( '' )
  print ( 'english_word_length_sample_test():' )
  print ( '  english_word_length_mean() computes the English Word Length mean' )
  print ( '  english_word_length_sample() samples the English Word Length distribution' )
  print ( '  english_word_length_variance() computes the English Word Length variance.' )

  mean = english_word_length_mean ( )
  variance = english_word_length_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = english_word_length_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %12d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14d' % ( xmax ) )
  print ( '  Sample minimum =  %14d' % ( xmin ) )

  return

def english_word_length_variance ( ):

#*****************************************************************************80
#
## english_word_length_variance(): variance of the English Word Length PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Henry Kucera, Winthrop Francis,
#    Computational Analysis of Present-Day American English,
#    Brown University Press, 1967.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  word_length_max = 27

  pdf_vec = np.array ( [ \
    0.03160, \
    0.16975, \
    0.21192, \
    0.15678, \
    0.10852, \
    0.08524, \
    0.07724, \
    0.05623, \
    0.04032, \
    0.02766, \
    0.01582, \
    0.00917, \
    0.00483, \
    0.00262, \
    0.00099, \
    0.00050, \
    0.00027, \
    0.00022, \
    0.00011, \
    0.00006, \
    0.00005, \
    0.00002, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001, \
    0.00001 ] )

  pdf_sum = 0.99997

  mean = 0.0
  for j in range ( 0, word_length_max ):
    mean = mean + ( j + 1 ) * pdf_vec[j]

  mean = mean / pdf_sum

  variance = 0.0
  for j in range ( 0, word_length_max ):
    variance = variance + pdf_vec[j] * ( j + 1 - mean ) ** 2 

  variance = variance / pdf_sum

  return variance

def erf_values ( n_data ):

#*****************************************************************************80
#
## erf_values() returns some values of the ERF or "error" function.
#
#  Discussion:
#
#    The error function is defined by:
#
#      ERF(X) = ( 2 / sqrt ( PI ) * integral ( 0 <= T <= X ) exp ( - T^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      Erf[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1124629160182849E+00, \
     0.2227025892104785E+00, \
     0.3286267594591274E+00, \
     0.4283923550466685E+00, \
     0.5204998778130465E+00, \
     0.6038560908479259E+00, \
     0.6778011938374185E+00, \
     0.7421009647076605E+00, \
     0.7969082124228321E+00, \
     0.8427007929497149E+00, \
     0.8802050695740817E+00, \
     0.9103139782296354E+00, \
     0.9340079449406524E+00, \
     0.9522851197626488E+00, \
     0.9661051464753107E+00, \
     0.9763483833446440E+00, \
     0.9837904585907746E+00, \
     0.9890905016357307E+00, \
     0.9927904292352575E+00, \
     0.9953222650189527E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def erf_values_test ( ):

#*****************************************************************************80
#
## erf_values_test() tests erf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'erf_values_test():' )
  print ( '  erf_values() stores values of the error function.' )
  print ( '' )
  print ( '      X         ERF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def erlang_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## erlang_cdf() evaluates the Erlang CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
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
## erlang_cdf_inv() inverts the Erlang CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  it_max = 100
  huge = np.finfo(float).max
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a
    return x
  elif ( 1.0 <= cdf ):
    x = huge
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
      print ( 'erlang_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'erlang_cdf_inv(): Fatal error!' )

    if ( ( cdf3 <= cdf and cdf1 <= cdf ) or ( cdf <= cdf3 and cdf <= cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def erlang_cdf_test ( rng ):

#*****************************************************************************80
#
## erlang_cdf_test() tests erlang_cdf(), erlang_cdf_inv(), erlang_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'erlang_cdf_test():' )
  print ( '  erlang_cdf() evaluates the Erlang CDF.' )
  print ( '  erlang_cdf_inv() inverts the Erlang CDF.' )
  print ( '  erlang_pdf() evaluates the Erlang PDF.' )

  a = 1.0
  b = 2.0
  c = 3

  check = erlang_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'erlang_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = erlang_sample ( a, b, c, rng )

    pdf = erlang_pdf ( x, a, b, c )

    cdf = erlang_cdf ( x, a, b, c )

    x2 = erlang_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def erlang_check ( a, b, c ):

#*****************************************************************************80
#
## erlang_check() checks the parameters of the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'erlang_check(): Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  if ( c <= 0 ):
    print ( '' )
    print ( 'erlang_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def erlang_mean ( a, b, c ):

#*****************************************************************************80
#
## erlang_mean() returns the mean of the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean =  a + b * c

  return mean

def erlang_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## erlang_pdf() evaluates the Erlang PDF.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#    real PDF, the value of the PDF.
#
  from scipy.special import factorial
  import numpy as np

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = y ** ( c - 1 ) / ( b * factorial ( c - 1 ) * np.exp ( y ) )

  return pdf

def erlang_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## erlang_sample() samples the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  a2 = 0.0
  b2 = b
  x = a
  for i in range ( 0, c ):
    x2 = exponential_sample ( a2, b2, rng )
    x = x + x2

  return x

def erlang_sample_test ( rng ):

#*****************************************************************************80
#
## erlang_sample_test() tests erlang_mean(), erlang_sample(), erlang_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'erlang_sample_test():' )
  print ( '  erlang_mean() computes the Erlang mean' )
  print ( '  erlang_sample() samples the Erlang distribution' )
  print ( '  erlang_variance() computes the Erlang variance.' )

  a = 1.0
  b = 2.0
  c = 3

  check = erlang_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'erlang_sample_test(): Fatal error!' )
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
    x[i] = erlang_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def erlang_variance ( a, b, c ):

#*****************************************************************************80
#
## erlang_variance() returns the variance of the Erlang PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, integer C, the parameters of the PDF.
#    0.0 < B.
#    0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance =  b * b * c

  return variance

def exponential_01_cdf ( x ):

#*****************************************************************************80
#
## exponential_01_cdf() evaluates the Exponential 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( - x )

  return cdf

def exponential_01_cdf_inv ( cdf ):

#*****************************************************************************80
#
## exponential_01_cdf_inv() inverts the Exponential 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'exponential_01_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'exponential_01_cdf_inv(): Fatal error!' )

  x = - np.log ( 1.0 - cdf )

  return x

def exponential_01_cdf_test ( rng ):

#*****************************************************************************80
#
## exponential_01_cdf_test() tests exponential_01_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'exponential_01_cdf_test():' )
  print ( '  exponential_01_cdf() evaluates the Exponential 01 CDF.' )
  print ( '  exponential_01_cdf_inv() inverts the Exponential 01 CDF.' )
  print ( '  exponential_01_pdf() evaluates the Exponential 01 PDF.' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = exponential_01_sample ( rng )

    pdf = exponential_01_pdf ( x )

    cdf = exponential_01_cdf ( x )

    x2 = exponential_01_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def exponential_01_mean ( ):

#*****************************************************************************80
#
## exponential_01_mean() returns the mean of the Exponential 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 1.0;

  return mean

def exponential_01_pdf ( x ):

#*****************************************************************************80
#
## exponential_01_pdf() evaluates the Exponential 01 PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - X )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    pdf = np.exp ( - x )

  return pdf

def exponential_01_sample ( rng ):

#*****************************************************************************80
#
## exponential_01_sample() samples the Exponential PDF with parameter 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = - np.log ( 1.0 - cdf )

  return x

def exponential_01_sample_test ( rng ):

#*****************************************************************************80
#
## exponential_01_sample_test() tests exponential_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000
 
  print ( '' )
  print ( 'exponential_01_sample_test():' )
  print ( '  exponential_01_mean() computes the Exponential 01 mean' )
  print ( '  exponential_01_sample() samples the Exponential 01 distribution' )
  print ( '  exponential_01_variance() computes the Exponential 01 variance.' )

  mean = exponential_01_mean ( )
  variance = exponential_01_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = exponential_01_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def exponential_01_variance ( ):

#*****************************************************************************80
#
## exponential_01_variance() returns the variance of the Exponential 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 1.0

  return variance

def exponential_cdf ( x, a, b ):

#*****************************************************************************80
#
## exponential_cdf() evaluates the Exponential CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= a ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( ( a - x ) / b )

  return cdf

def exponential_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## exponential_cdf_inv() inverts the Exponential CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'exponential_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'exponential_cdf_inv(): Fatal error!' )

  x = a - b * np.log ( 1.0 - cdf )

  return x

def exponential_cdf_test ( rng ):

#*****************************************************************************80
#
## exponential_cdf_test() tests exponential_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'exponential_cdf_test():' )
  print ( '  exponential_cdf() evaluates the Exponential CDF.' )
  print ( '  exponential_cdf_inv() inverts the Exponential CDF.' )
  print ( '  exponential_pdf() evaluates the Exponential PDF.' )

  a = 1.0
  b = 2.0

  check = exponential_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'exponential_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = exponential_sample ( a, b, rng )

    pdf = exponential_pdf ( x, a, b )

    cdf = exponential_cdf ( x, a, b )

    x2 = exponential_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def exponential_check ( a, b ):

#*****************************************************************************80
#
## exponential_check() checks the parameters of the Exponential CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'exponential_check(): Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def exponential_mean ( a, b ):

#*****************************************************************************80
#
## exponential_mean() returns the mean of the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a + b

  return mean

def exponential_pdf ( x, a, b ):

#*****************************************************************************80
#
## exponential_pdf() evaluates the Exponential PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = ( 1 / B ) * EXP ( ( A - X ) / B )
#
#    The time interval between two Poisson events is a random
#    variable with the Exponential PDF.  The parameter B is the
#    average interval between events.
#
#    In another context, the Exponential PDF is related to
#    the Boltzmann distribution, which describes the relative
#    probability of finding a system, which is in thermal equilibrium
#    at absolute temperature T, in a given state having energy E.
#    The relative probability is
#
#      Boltzmann_Relative_Probability(E,T) = exp ( - E / ( k * T ) ),
#
#    where k is the Boltzmann constant,
#
#      k = 1.38 * 10^(-23) joules / degree Kelvin
#
#    and normalization requires a determination of the possible
#    energy states of the system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a ):
    pdf = 0.0
  else:
    pdf = ( 1.0 / b ) * np.exp ( ( a - x ) / b )

  return pdf

def exponential_sample ( a, b, rng ):

#*****************************************************************************80
#
## exponential_sample() samples the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = exponential_cdf_inv ( cdf, a, b )

  return x

def exponential_sample_test ( rng ):

#*****************************************************************************80
#
## exponential_sample_test() tests exponential_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'exponential_sample_test():' )
  print ( '  exponential_mean() computes the Exponential mean' )
  print ( '  exponential_sample() samples the Exponential distribution' )
  print ( '  exponential_variance() computes the Exponential variance.' )

  a = 1.0
  b = 10.0

  check = exponential_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'exponential_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = exponential_mean ( a, b )
  variance = exponential_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = exponential_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def exponential_variance ( a, b ):

#*****************************************************************************80
#
## exponential_variance() returns the variance of the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = b * b

  return variance

def extreme_values_cdf_values ( n_data ):

#*****************************************************************************80
#
## extreme_values_cdf_values() returns some values of the Extreme Values CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = ExtremeValuesDistribution [ alpha, beta ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real ALPHA, the first parameter of the distribution.
#
#    real BETA, the second parameter of the distribution.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 12

  alpha_vec = np.array ( (
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.5000000000000000E+01 ))

  beta_vec = np.array ( (
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.5000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01 ))

  f_vec = np.array ( (
     0.3678794411714423E+00, \
     0.8734230184931166E+00, \
     0.9818510730616665E+00, \
     0.9975243173927525E+00, \
     0.5452392118926051E+00, \
     0.4884435800065159E+00, \
     0.4589560693076638E+00, \
     0.4409910259429826E+00, \
     0.5452392118926051E+00, \
     0.3678794411714423E+00, \
     0.1922956455479649E+00, \
     0.6598803584531254E-01 ))

  x_vec = np.array ( (
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    beta = 0.0
    x = 0.0
    f = 0.0
  else:
    alpha = alpha_vec[n_data]
    beta = beta_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, beta, x, f

def extreme_values_cdf_values_test ( ):

#*****************************************************************************80
#
## extreme_values_cdf_values_test() tests extreme_values_cdf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'extreme_values_cdf_values_test():' )
  print ( '  extreme_values_cdf_values() stores values of the Extreme Values CDF.' )
  print ( '' )
  print ( '        Alpha         Beta          X               CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, alpha, beta, x, f = extreme_values_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16g' % ( alpha, beta, x, f ) )

  return

def extreme_values_cdf ( x, a, b ):

#*****************************************************************************80
#
## extreme_values_cdf() evaluates the Extreme Values CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  y = ( x - a ) / b

  cdf = np.exp ( - np.exp ( - y ) )

  return cdf

def extreme_values_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## extreme_values_cdf_inv() inverts the Extreme Values CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'extreme_values_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'extreme_values_cdf_inv(): Fatal error!' )

  x = a - b * np.log ( - np.log ( cdf ) )

  return x

def extreme_values_cdf_test ( rng ):

#*****************************************************************************80
#
## extreme_values_cdf_test() tests extreme_values_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'extreme_values():' )
  print ( '  extreme_values_cdf() evaluates the Extreme Values CDF' )
  print ( '  extreme_values_cdf_inv() inverts the Extreme Values CDF.' )
  print ( '  extreme_values_pdf() evaluates the Extreme Values PDF' )

  a = 2.0
  b = 3.0

  check = extreme_values_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'extreme_values_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = extreme_values_sample ( a, b, rng )

    pdf = extreme_values_pdf ( x, a, b )

    cdf = extreme_values_cdf ( x, a, b )

    x2 = extreme_values_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def extreme_values_check ( a, b ):

#*****************************************************************************80
#
## extreme_values_check() checks the parameters of the Extreme Values CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'extreme_values_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def extreme_values_mean ( a, b ):

#*****************************************************************************80
#
## extreme_values_mean() returns the mean of the Extreme Values PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  euler_constant = 0.5772156649015328

  mean = a + b * euler_constant

  return mean

def extreme_values_pdf ( x, a, b ):

#*****************************************************************************80
#
## extreme_values_pdf() evaluates the Extreme Values PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) =
#      ( 1 / B ) *
#      EXP (
#        ( A - X ) / B - EXP ( ( A - X ) / B  )
#      ).
#
#    The Extreme Values PDF is also known as the Fisher-Tippet PDF
#    and the Log-Weibull PDF.
#
#    The special case A = 0 and B = 1 is the Gumbel PDF.
#
#    The Extreme Values PDF is the limiting distribution for the
#    smallest or largest value in a large sample drawn from
#    any of a great variety of distributions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = ( 1.0 / b ) * np.exp ( ( a - x ) / b - np.exp ( ( a - x ) / b ) )

  return pdf

def extreme_values_sample ( a, b, rng ):

#*****************************************************************************80
#
## extreme_values_sample() samples the Extreme Values PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = extreme_values_cdf_inv ( cdf, a, b )

  return x

def extreme_values_sample_test ( rng ):

#*****************************************************************************80
#
## extreme_values_sample_test() tests extreme_values_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'extreme_values_sample_test():' )
  print ( '  extreme_values_mean() computes the Extreme Values mean' )
  print ( '  extreme_values_sample() samples the Extreme Values distribution' )
  print ( '  extreme_values_variance() computes the Extreme Values variance.' )

  a = 2.0
  b = 3.0

  check = extreme_values_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'extreme_values_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = extreme_values_mean ( a, b )
  variance = extreme_values_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = extreme_values_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def extreme_values_variance ( a, b ):

#*****************************************************************************80
#
## extreme_values_variance() returns the variance of the Extreme Values PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = np.pi * np.pi * b * b / 6.0

  return variance

def fermi_dirac_sample ( u, v, rng ):

#*****************************************************************************80
#
# fermi_dirac_sample samples a (continuous) Fermi-Dirac distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    Original BASIC version by Frederick Ruckdeschel.
#    This version by John Burkardt
#
#  Reference:
#
#    Frederick Ruckdeschel,
#    BASIC Scientific Subroutines,
#    Volume I,
#    McGraw Hill, 1980,
#    ISBN: 0-07-054201-5,
#    LC: QA76.95.R82.
#
#  Input:
#
#    real U, V, the parameters of the distribution.
#    The value of U represents the halfway point for the distribution.
#    Half the probability is to the left, and half to the right, of
#    the value U.  The value of V controls the shape of the distribution.
#    The ratio U/V determines the relative shape of the distribution.
#    Values of U/V in excess of 100 will risk overflow.
#
#  Output:
#
#    real Z, a sample from the Fermi-Dirac distribution.
#    Output values will be nonnegative, and roughly half of them should
#    be less than or equal to U.
#
  import numpy as np

  iter_max = 1000

  x = rng.random ( )
  y = 1.0
  a = np.exp ( 4.0 * u / v )
  b = ( x - 1.0 ) * np.log ( 1.0 + a )

  iter_num = 0

  while ( True ):

    y1 = b + np.log ( a + np.exp ( y ) )

    if ( abs ( y - y1 ) < 0.001 ):
      break

    y = y1

    iter_num = iter_num + 1

    if ( iter_max < iter_num ):
      break

  z = v * y1 / 4.0

  return z

def fermi_dirac_sample_test ( rng ):

#*****************************************************************************80
#
# fermi_dirac_sample_test() tests fermi_dirac_sample.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 10000
  test_num = 7

  u_test = np.array ( [ 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 1.0 ] )
  v_test = np.array ( [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.25 ] )

  print ( '' )
  print ( 'fermi_dirac_sample_test():' )
  print ( '  fermi_dirac_sample() samples the Fermi Dirac distribution.' )

  for test in range ( 0, test_num ):

    u = u_test[test]
    v = v_test[test]

    print ( '' )
    print ( '  U =          %g' % ( u ) )
    print ( '  V =          %g' % ( v ) )

    z = np.zeros ( sample_num  )
    for i in range ( 0, sample_num ):
      z[i] = fermi_dirac_sample ( u, v, rng )

    z_max = np.max ( z )
    z_min = np.min ( z )
    mean = np.mean ( z )
    variance = np.var ( z )

    print ( '' )
    print ( '  SAMPLE_NUM =      %d' % ( sample_num ) )
    print ( '  Sample mean =     %g' % ( mean ) )
    print ( '  Sample variance = %g' % ( variance ) )
    print ( '  Maximum value =   %g' % ( z_max ) )
    print ( '  Minimum value =   %g' % ( z_min ) )

  return

def fisher_pdf ( x, kappa, mu ):

#*****************************************************************************80
#
## fisher_pdf() evaluates the Fisher PDF.
#
#  Discussion:
#
#    The formulat for the PDF is:
#
#      PDF(KAPPA,MUX) = C(KAPPA) * exp ( KAPPA * MU' * X )
#
#    where:
#
#      0 <= KAPPA is the concentration parameter,
#      MU is a point on the unit sphere, the mean direction,
#      X is any point on the unit sphere,
#      and C(KAPPA) is a normalization factor:
#
#      C(KAPPA) = sqrt ( KAPPA ) / ( ( 2 * pi )^(3/2) * I(0.5,KAPPA) )
#
#    where
#
#      I(nu,X) is the Bessel function of order NU and argument X.
#
#    For a fixed value of MU, the value of KAPPA determines the
#    tendency of sample points to tend to be near MU.  In particular,
#    KAPPA = 0 corresponds to a uniform distribution of points on the
#    sphere, but as KAPPA increases, the sample points will tend to
#    cluster more closely to MU.
#
#    The Fisher distribution for points on the unit sphere is
#    analogous to the normal distribution of points on a line,
#    and, more precisely, to the von Mises distribution on a circle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kanti Mardia, Peter Jupp,
#    Directional Statistics,
#    Wiley, 2000,
#    LC: QA276.M335
#
#  Input:
#
#    real X(3), the argument of the PDF.
#    X should have unit Euclidean norm, but this routine will
#    automatically work with a normalized version of X.
#
#    real KAPPA, the concentration parameter.
#    0 <= KAPPA is required.
#
#    real MU(3), the mean direction.
#    MU should have unit Euclidean norm, but this routine will
#    automatically work with a normalized version of MU.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy import special

  if ( kappa < 0.0 ):
    print ( '' )
    print ( 'fisher_pdf(): Fatal error!' )
    print ( '  KAPPA must be nonnegative.' )
    print ( '  Input KAPPA =', kappa )
    raise Exception ( 'fisher_pdf(): Fatal error!' )

  if ( kappa == 0.0 ):
    pdf = 1.0 / ( 4.0 * np.pi )
    return pdf

  alpha = 0.5

  b = special.iv ( alpha, kappa )

  cf = np.sqrt ( kappa ) / ( np.sqrt ( ( 2.0 * np.pi ) ** 3 ) * b )

  mu_norm = np.linalg.norm ( mu )

  if ( mu_norm == 0.0 ):
    pdf = cf
    return pdf

  x_norm = np.linalg.norm ( x )

  if ( x_norm == 0.0 ):
    pdf = cf
    return pdf

  arg = kappa * ( np.dot ( x, mu ) ) / ( x_norm * mu_norm )

  pdf = cf * np.exp ( arg )

  return pdf

def fisher_pdf_test ( rng ):

#*****************************************************************************80
#
## fisher_pdf_test() tests fisher_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 10
  test_num = 3

  print ( '' )
  print ( 'fisher_pdf_test():' )
  print ( '  fisher_pdf() evaluates the Fisher PDF.' )

  for test in range ( 0, test_num ):

    if ( test == 0 ):
      kappa = 0.0
      mu = np.array ( [ 1.0, 0.0, 0.0 ] )
    elif ( test == 1 ):
      kappa = 0.5
      mu = np.array ( [ 1.0, 0.0, 0.0 ] )
    elif ( test == 2 ):
      kappa = 10.0
      mu = np.array ( [ 1.0, 0.0, 0.0 ] )

    print ( '' )
    print ( '  PDF Input:' )
    print ( '    Concentration parameter KAPPA = %g' % ( kappa ) )

    r8vec_transpose_print ( 3, mu, '' )

    print ( '' )
    print ( '      X                         PDF' )
    print ( '' )

    for j in range ( 0, n ):

      x = fisher_sample ( kappa, mu, 1, rng )

      pdf = fisher_pdf ( x[:,0], kappa, mu )

      print ( '  %8g  %8g  %8g    %14g' % ( x[0,0], x[1,0], x[2,0], pdf ) )

  return

def fisher_sample ( kappa, mu, n, rng ):

#*****************************************************************************80
#
## fisher_sample() samples the Fisher distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2008
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Fisher, Toby Lewis, Brian Embleton,
#    Statistical Analysis of Spherical Data,
#    Cambridge, 2003,
#    ISBN13: 978-0521456999,
#    LC: QA276.F489.
#
#  Input:
#
#    real KAPPA, the concentration parameter.
#
#    real MU(3), the mean direction.
#    MU should have unit Euclidean norm, but this routine will
#    automatically work with a normalized version of MU.
#
#    integer N, the number of samples to choose.
#
#  Output:
#
#    real XYZ(3,N), a sample of the Fisher distribution.
#
#  Local:
#
#    real ALPHA, BETA, the colatitude (theta) and 
#    longitude (phi) of the mean direction.  
#
  import numpy as np

  mu_norm = np.linalg.norm ( mu )

  if ( mu_norm == 0.0 ):
    print ( '' )
    print ( 'fisher_sample(): Fatal error!' )
    print ( '  Direction vector MU is zero' )
    raise Exception ( 'fisher_sample(): Fatal error!' )

  alpha = - np.arccos ( mu[2] / mu_norm )
  beta = np.arctan2 ( mu[1], mu[0] )

  lam = np.exp ( - 2.0 * kappa )

  theta = rng.random ( size = n )

  if ( kappa == 0.0 ):
     theta = 2.0 * np.arcsin ( np.sqrt ( 1.0 - theta ) )
  else:
    for i in range ( 0, n ):
      theta = 2.0 * np.arcsin ( np.sqrt \
        ( - np.log ( theta * ( 1.0 - lam ) + lam ) / ( 2.0 * kappa ) ) )

  phi = rng.random ( size = n )
  phi = 2.0 * np.pi * phi

  xyz = np.zeros ( [ 3, n ] )

  for i in range ( 0, n ):
#
#  Compute the unrotated points.
#
    xyz[0,i] = np.sin ( theta[i] ) * np.cos ( phi[i] )
    xyz[1,i] = np.sin ( theta[i] ) * np.sin ( phi[i] )
    xyz[2,i] = np.cos ( theta[i] )
#
#  Compute the rotation matrix.
#
  A = np.zeros ( [ 3, 3 ] )

  A[0,0] =   np.cos ( alpha ) * np.cos ( beta )
  A[1,0] =                    - np.sin ( beta )
  A[2,0] =   np.sin ( alpha ) * np.cos ( beta ) 

  A[0,1] =   np.cos ( alpha ) * np.sin ( beta )
  A[1,1] =                    + np.cos ( beta )
  A[2,1] =   np.sin ( alpha ) * np.sin ( beta )

  A[0,2] = - np.sin ( alpha )
  A[1,2] =   0.0
  A[2,2] =   np.cos ( alpha )
#
#  Rotate the points.
#
  xyz = np.dot ( A, xyz )

  return xyz

def fisk_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## fisk_cdf() evaluates the Fisk CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= a ):
    cdf = 0.0
  else:
    cdf = 1.0 / ( 1.0 + ( b / ( x - a ) ) ** c )

  return cdf

def fisk_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## fisk_cdf_inv() inverts the Fisk CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  huge = np.finfo(float).max

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'fisk_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'fisk_cdf_inv(): Fatal error!' )

  if ( cdf <= 0.0 ):
    x = a
  elif ( cdf < 1.0 ):
    x = a + b * ( cdf / ( 1.0 - cdf ) ) ** ( 1.0 / c )
  elif ( 1.0 <= cdf ):
    x = huge

  return x

def fisk_cdf_test ( rng ):

#*****************************************************************************80
#
## fisk_cdf_test() tests fisk_cdf(), fisk_cdf_inv(), fisk_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'fisk_cdf_test():' )
  print ( '  fisk_cdf() evaluates the Fisk CDF' )
  print ( '  fisk_cdf_inv() inverts the Fisk CDF.' )
  print ( '  fisk_pdf() evaluates the Fisk PDF' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = fisk_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'fisk_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = fisk_sample ( a, b, c, rng )

    pdf = fisk_pdf ( x, a, b, c )

    cdf = fisk_cdf ( x, a, b, c )

    x2 = fisk_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def fisk_check ( a, b, c ):

#*****************************************************************************80
#
## fisk_check() checks the parameters of the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'fisk_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'fisk_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def fisk_mean ( a, b, c ):

#*****************************************************************************80
#
## fisk_mean() returns the mean of the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  if ( c <= 1.0 ):
    print ( '' )
    print ( 'fisk_mean(): Fatal error!' )
    print ( '  No mean defined for C <= 1.0' )
    raise Exception ( 'fisk_mean(): Fatal error!' )

  mean = a + np.pi * ( b / c ) * r8_csc ( np.pi / c )

  return mean

def fisk_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## fisk_pdf() evaluates the Fisk PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) =
#      ( C / B ) * ( ( X - A ) / B )^( C - 1 ) /
#      ( 1 + ( ( X - A ) / B )^C )^2
#
#    The Fisk PDF is also known as the Log Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x <= a ):

    pdf = 0.0 

  else:

    y = ( x - a ) / b

    pdf = ( c / b ) * y ** ( c - 1.0 ) / ( 1.0 + y ** c ) ** 2

  return pdf

def fisk_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## fisk_sample() samples the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = fisk_cdf_inv ( cdf, a, b, c )

  return x

def fisk_sample_test ( rng ):

#*****************************************************************************80
#
## fisk_sample_test() tests fisk_mean(), fisk_sample(), fisk_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'fisk_sample_test():' )
  print ( '  fisk_mean() computes the Fisk mean' )
  print ( '  fisk_sample() samples the Fisk distribution' )
  print ( '  fisk_variance() computes the Fisk variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = fisk_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'fisk_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = fisk_mean ( a, b, c )
  variance = fisk_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = fisk_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def fisk_variance ( a, b, c ):

#*****************************************************************************80
#
## fisk_variance() returns the variance of the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  if ( c <= 2.0 ):
    print ( '' )
    print ( 'fisk_variance(): Fatal error!' )
    print ( '  No variance defined for C <= 2.0' )
    raise Exception ( 'fisk_variance(): Fatal error!' )

  g = np.pi / c

  variance = b ** 2 * ( 2.0 * g * r8_csc ( 2.0 * g ) - ( g * r8_csc ( g ) ) ** 2 )

  return variance

def folded_normal_cdf ( x, a, b ):

#*****************************************************************************80
#
## folded_normal_cdf() evaluates the Folded Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#    0.0 <= X.
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 0.0 ):
    cdf = 0.0
  else:
    x1 = ( x - a ) / b
    cdf1 = normal_01_cdf ( x1 )
    x2 = ( - x - a ) / b
    cdf2 = normal_01_cdf ( x2 )
    cdf = cdf1 - cdf2

  return cdf

def folded_normal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## folded_normal_cdf_inv() inverts the Folded Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    real X, the argument of the CDF.
#    0.0 <= X.
#
  import numpy as np

  it_max = 100
  tol = 0.0001
  huge = np.finfo(float).max

  if ( cdf <= 0.0 ):
    x = 0.0
    return x
  elif ( 1.0 <= cdf ):
    x = huge
    return x
#
#  Find X1, for which the value of CDF will be too small.
#
  if ( 0.0 <= a ):
    x1 = normal_cdf_inv ( cdf, a, b )
  else:
    x1 = normal_cdf_inv ( cdf, -a, b )

  x1 = max ( x1, 0.0 )
  cdf1 = folded_normal_cdf ( x1, a, b )
#
#  Find X2, for which the value of CDF will be too big.
#
  cdf2 = ( 1.0 - cdf ) / 2.0

  xa = normal_cdf_inv ( cdf2, a, b )
  xb = normal_cdf_inv ( cdf2, -a, b )
  x2 = max ( abs ( xa ), abs ( xb ) )
  cdf2 = folded_normal_cdf ( x2, a, b )
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = folded_normal_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'folded_normal_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'folded_normal_cdf_inv(): Fatal error!' )

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def folded_normal_cdf_test ( rng ):

#*****************************************************************************80
#
## folded_normal_cdf_test() tests folded_normal_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'folded_normal_cdf_test():' )
  print ( '  folded_normal_cdf() evaluates the Folded Normal CDF.' )
  print ( '  folded_normal_cdf_inv() inverts the Folded Normal CDF.' )
  print ( '  folded_normal_pdf() evaluates the Folded Normal PDF.' )

  a = 2.0
  b = 3.0

  check = folded_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'folded_normal_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =         %14g' % ( a ) )
  print ( '  PDF parameter B =         %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )
 
  for i in range ( 0, 10 ):

    x = folded_normal_sample ( a, b, rng )

    pdf = folded_normal_pdf ( x, a, b )

    cdf = folded_normal_cdf ( x, a, b )

    x2 = folded_normal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def folded_normal_check ( a, b ):

#*****************************************************************************80
#
## folded_normal_check() checks the parameters of the Folded Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 ):
    print ( '' )
    print ( 'folded_normal_check(): Fatal error!' )
    print ( '  A < 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'folded_normal_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def folded_normal_mean ( a, b ):

#*****************************************************************************80
#
## folded_normal_mean() returns the mean of the Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  a2 = a / b

  cdf = normal_01_cdf ( a2 )

  mean = b * np.sqrt ( 2.0 / np.pi ) * np.exp ( - 0.5 * a2 * a2 ) \
    - a * ( 1.0 - 2.0 * cdf )

  return mean

def folded_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## folded_normal_pdf() evaluates the Folded Normal PDF.
#
#  Discussion:
#
#    PDF(X)(A) = SQRT ( 2 / PI ) * ( 1 / B ) * COSH ( A * X / B^2 )
#      * EXP ( - 0.5 * ( X^2 + A^2 ) / B^2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    pdf = np.sqrt ( 2.0 / np.pi ) * ( 1.0 / b ) * np.cosh ( a * x / ( b * b ) ) \
      * np.exp ( - 0.5 * ( x * x + a * a ) / ( b * b ) )

  return pdf

def folded_normal_sample ( a, b, rng ):

#*****************************************************************************80
#
## folded_normal_sample() samples the Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = folded_normal_cdf_inv ( cdf, a, b )

  return x

def folded_normal_sample_test ( rng ):

#*****************************************************************************80
#
## folded_normal_sample_test() tests folded_normal_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'folded_normal_sample_test():' )
  print ( '  folded_normal_mean() computes the Folded Normal mean' )
  print ( '  folded_normal_sample() samples the Folded Normal distribution' )
  print ( '  folded_normal_variance() computes the Folded Normal variance.' )

  a = 2.0
  b = 3.0

  check = folded_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'folded_normal_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = folded_normal_mean ( a, b )
  variance = folded_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = folded_normal_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def folded_normal_variance ( a, b ):

#*****************************************************************************80
#
## folded_normal_variance() returns the variance of the Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  mean = folded_normal_mean ( a, b )

  variance = a * a + b * b - mean * mean

  return variance

def f_cdf ( x, m, n ):

#*****************************************************************************80
#
## f_cdf() evaluates the F central CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Formula 26.5.28
#    Abramowitz and Stegun,
#    Handbook of Mathematical Functions.
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    arg1 = 0.5 * float ( n )
    arg2 = 0.5 * float ( m )
    arg3 = float ( n ) / float ( n + m * x )

    cdf = beta_inc ( arg1, arg2, arg3 )

  return cdf

def f_cdf_test ( rng ):

#*****************************************************************************80
#
## f_cdf_test() tests f_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'f_cdf_test():' )
  print ( '  f_cdf() evaluates the F CDF.' )
  print ( '  f_pdf() evaluates the F PDF.' )

  m = 1
  n = 1
  
  if ( not f_check ( m, n ) ):
    print ( '' )
    print ( 'f_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal!' )
    return

  print ( '' )
  print ( '  PDF parameter M = %6d' % ( m ) )
  print ( '  PDF parameter N = %6d' % ( n ) )

  print ( '' )
  print ( '      X        M     N        PDF         CDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = f_sample ( m, n, rng )

    pdf = f_pdf ( x, m, n )

    cdf = f_cdf ( x, m, n )

    print ( '  %14g  %6d  %6d  %14g  %14g' % ( x, m, n, pdf, cdf ) )

  return

def f_check ( m, n ):

#*****************************************************************************80
#
## f_check() checks the parameters of the F PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#    0 < M
#    0 < N
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( m <= 0 ):
    print ( '' )
    print ( 'f_check(): Fatal error!' )
    print ( '  M <= 0.' )
    check = False

  if ( n <= 0 ):
    print ( '' )
    print ( 'f_check(): Fatal error!' )
    print ( '  N <= 0.' )
    check = False

  return check

def f_mean ( m, n ):

#*****************************************************************************80
#
## f_mean() returns the mean of the F central PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#    Note, however, that the mean is not defined unless 3 <= N.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  if ( n < 3 ):
    print ( '' )
    print ( 'f_mean(): Fatal error!' )
    print ( '  The mean is not defined for N < 3.' )
    raise Exception ( 'f_mean(): Fatal error!' )

  mean = float ( n ) / float ( n - 2 )

  return mean

def f_pdf ( x, m, n ):

#*****************************************************************************80
#
## f_pdf() evaluates the F central PDF.
#
#  Discussion:
#
#    PDF(X)(M,N) = M^(M/2) * X^((M-2)/2)
#      / ( Beta(M/2,N/2) * N^(M/2) * ( 1 + (M/N) * X )^((M+N)/2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#    integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):

    pdf = 0.0

  else:

    a = m
    b = n

    top = np.sqrt ( float ( m ) ** m * float ( n ) ** n * x ** ( m - 2 ) )
    bot1 = r8_beta ( float ( m ) / 2.0, float ( n ) / 2.0 )
    bot2 = np.sqrt ( ( n + m * x ) ** ( m + n ) )

    pdf = top / ( bot1 * bot2 )

  return pdf

def f_sample ( m, n, rng ):

#*****************************************************************************80
#
## f_sample() samples the F central PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  xm = chi_square_sample ( m, rng )

  xn = chi_square_sample ( n, rng )

  x = float ( n ) * xm / ( float ( m ) * xn )

  return x

def f_sample_test ( rng ):

#*****************************************************************************80
#
## f_sample_test() tests f_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'f_sample_test():' )
  print ( '  f_mean() computes the F mean' )
  print ( '  f_sample() samples the F distribution' )
  print ( '  f_variance() computes the F variance.' )

  m = 8
  n = 6

  if ( not f_check ( m, n ) ):
    print ( '' )
    print ( 'f_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal!' )
    return

  mean = f_mean ( m, n )
  variance = f_variance ( m, n )

  print ( '' )
  print ( '  PDF parameter M =       %6d' % ( m ) )
  print ( '  PDF parameter N =       %6d' % ( n ) )
  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF variance =          %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = f_sample ( m, n, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def f_variance ( m, n ):

#*****************************************************************************80
#
## f_variance() returns the variance of the F central PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#    Note, however, that the variance is not defined unless 5 <= N.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  if ( n < 5 ):
    print ( '' )
    print ( 'f_variance(): Fatal error!' )
    print ( '  The variance is not defined for N < 5.' )
    raise Exception ( 'f_variance(): Fatal error!' )

  variance = float ( 2 * n * n * ( m + n - 2 ) ) \
    / float ( m * ( n - 2 ) ** 2 * ( n - 4 ) )

  return variance

def frechet_cdf ( x, alpha ):

#*****************************************************************************80
#
## frechet_cdf() evaluates the Frechet CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'frechet_cdf(): Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    raise Exception ( 'frechet_cdf(): Fatal error!' )

  if ( x <= 0.0 ):
    cdf = 0.0
  else:
    cdf = np.exp ( - 1.0 / x ** alpha )

  return cdf

def frechet_cdf_inv ( cdf, alpha ):

#*****************************************************************************80
#
## frechet_cdf_inv() inverts the Frechet CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'frechet_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'frechet_cdf_inv(): Fatal error!' )

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'frechet_cdf_inv(): Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    raise Exception ( 'frechet_cdf_inv(): Fatal error!' )

  if ( cdf == 0.0 ):
    x = 0.0
  else:
    x =  ( - 1.0 / np.log ( cdf ) ) ** ( 1.0 / alpha )
 
  return x

def frechet_cdf_test ( rng ):

#*****************************************************************************80
#
## frechet_cdf_test() tests frechet_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'frechet_cdf_test():' )
  print ( '  frechet_cdf() evaluates the Frechet CDF' )
  print ( '  frechet_cdf_inv() inverts the Frechet CDF.' )
  print ( '  frechet_pdf() evaluates the Frechet PDF' )

  alpha = 3.0

  print ( '' )
  print ( '  PDF parameter ALPHA =         %g' % ( alpha ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = frechet_sample ( alpha, rng )

    pdf = frechet_pdf ( x, alpha )

    cdf = frechet_cdf ( x, alpha )

    x2 = frechet_cdf_inv ( cdf, alpha )

    print ( '  %12g  %12g  %12g  %12g' % ( x, pdf, cdf, x2 ) )

  return

def frechet_mean ( alpha ):

#*****************************************************************************80
#
## frechet_mean() returns the mean of the Frechet PDF.
#
#  Discussion:
#
#    The distribution does not have a mean value unless 1 < ALPHA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#    It is required that 1.0 < ALPHA.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  from scipy.special import gamma

  if ( alpha <= 1.0 ):
    print ( '' )
    print ( 'frechet_mean(): Fatal error!' )
    print ( '  Mean does not exist if ALPHA <= 1.' )
    raise Exception ( 'frechet_mean(): Fatal error!' )

  mean = gamma ( ( alpha - 1.0 ) / alpha )

  return mean

def frechet_pdf ( x, alpha ):

#*****************************************************************************80
#
## frechet_pdf() evaluates the Frechet PDF.
#
#  Discussion:
#
#    PDF(X) = ALPHA * exp ( -1 / X^ALPHA ) / X^(ALPHA+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'frechet_pdf(): Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    raise Exception ( 'frechet_pdf(): Fatal error!' )

  pdf = alpha * np.exp ( - 1.0 / x ** alpha ) / x ** ( alpha + 1.0 )

  return pdf

def frechet_sample ( alpha, rng ):

#*****************************************************************************80
#
## frechet_sample() samples the Frechet PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'frechet_sample(): Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    raise Exception ( 'frechet_sample(): Fatal error!' )

  cdf = rng.random ( )

  x = frechet_cdf_inv ( cdf, alpha )

  return x

def frechet_sample_test ( rng ):

#*****************************************************************************80
#
## frechet_sample_test() tests frechet_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'frechet_sample_test():' )
  print ( '  frechet_mean() computes the Frechet mean' )
  print ( '  frechet_sample() samples the Frechet distribution' )
  print ( '  frechet_variance() computes the Frechet variance.' )

  alpha = 3.0

  print ( '' )
  print ( '  PDF parameter ALPHA =         %g' % ( alpha ) )

  mean = frechet_mean ( alpha )
  variance = frechet_variance ( alpha )

  print ( '  PDF mean =                    %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = frechet_sample ( alpha, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %g' % ( nsample ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )

  return

def frechet_variance ( alpha ):

#*****************************************************************************80
#
## frechet_variance() returns the variance of the Frechet PDF.
#
#  Discussion:
#
#    The PDF does not have a variance unless 2 < ALPHA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#    It is required that 2.0 < ALPHA.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  from scipy.special import gamma

  if ( alpha <= 2.0 ):
    print ( '' )
    print ( 'frechet_variance(): Fatal error!' )
    print ( '  Variance does not exist if ALPHA <= 2.' )
    raise Exception ( 'frechet_variance(): Fatal error!' )

  mean = gamma ( ( alpha - 1.0 ) / alpha )

  variance = gamma ( ( alpha - 2.0 ) / alpha ) - mean * mean

  return variance

def gamma_inc_values ( n_data ):

#*****************************************************************************80
#
## gamma_inc_values() returns some values of the incomplete Gamma function.
#
#  Discussion:
#
#    The (normalized) incomplete Gamma function is defined as:
#
#      Integral ( X <= T < oo ) T^(A-1) * exp(-T) dT.
#
#    In Mathematica, the function can be evaluated by:
#
#      Gamma[A,X]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real A, the parameter of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     0.10E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+01, \
     0.10E+01, \
     0.10E+01, \
     0.11E+01, \
     0.11E+01, \
     0.11E+01, \
     0.20E+01, \
     0.20E+01, \
     0.20E+01, \
     0.60E+01, \
     0.60E+01, \
     0.11E+02, \
     0.26E+02, \
     0.41E+02 ))

  f_vec = np.array ( ( \
    2.490302836300570E+00, \
    0.8718369702247978E+00, \
    0.1079213896175866E+00, \
    1.238121685818417E+00, \
    0.3911298052193973E+00, \
    0.01444722098952533E+00, \
    0.9048374180359596E+00, \
    0.3678794411714423E+00, \
    0.006737946999085467E+00, \
    0.8827966752611692E+00, \
    0.3908330082003269E+00, \
    0.008051456628620993E+00, \
    0.9898141728888165E+00, \
    0.5578254003710746E+00, \
    0.007295055724436130E+00, \
    114.9574754165633E+00, \
    2.440923530031405E+00, \
    280854.6620274718E+00, \
    8.576480283455533E+24, \
    2.085031346403364E+47 ))

  x_vec = np.array ( ( \
     0.30E-01, \
     0.30E+00, \
     0.15E+01, \
     0.75E-01, \
     0.75E+00, \
     0.35E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.15E+00, \
     0.15E+01, \
     0.70E+01, \
     0.25E+01, \
     0.12E+02, \
     0.16E+02, \
     0.25E+02, \
     0.45E+02 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def gamma_inc_values_test ( ):

#*****************************************************************************80
#
## gamma_inc_values_test() tests gamma_inc_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gamma_inc_values_test():' )
  print ( '  gamma_inc_values() stores values of the incomplete Gamma function.' )
  print ( '' )
  print ( '      A         X        gamma_inc(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, f = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( a, x, f ) )

  return

def gamma_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## gamma_cdf() evaluates the Gamma CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  x2 = ( x - a ) / b
  p2 = c

  cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def gamma_cdf_test ( rng ):

#*****************************************************************************80
#
## gamma_cdf_test() tests gamma_cdf(), gamma_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
  a = 1.0
  b = 1.5
  c = 3.0

  print ( '' )
  print ( 'gamma_cdf_test():' )
  print ( '  gamma_cdf() evaluates the Gamma CDF.' )
  print ( '  gamma_pdf() evaluates the Gamma PDF.' )
  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )

  check = gamma_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'gamma_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  X  PDF   CDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = gamma_sample ( a, b, c, rng )

    cdf = gamma_cdf ( x, a, b, c )

    pdf = gamma_pdf ( x, a, b, c )

    print ( '  %12g  %12g  %12g' % ( x, pdf, cdf ) )

  return

def gamma_check ( a, b, c ):

#*****************************************************************************80
#
## gamma_check() checks the parameters of the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'gamma_check(): Fatal error!' )
    print ( '  B <= 0.' )
    print ( '  B = %g' % ( b ) )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'gamma_check(): Fatal error!' )
    print ( '  C <= 0.' )
    print ( '  C = %g' % ( c ) )
    check = False

  return check

def gamma_mean ( a, b, c ):

#*****************************************************************************80
#
## gamma_mean() returns the mean of the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a + b * c

  return mean

def gamma_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## gamma_pdf() evaluates the Gamma PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = EXP ( - ( X - A ) / B ) * ( ( X - A ) / B )^(C-1)
#      / ( B * GAMMA ( C ) )
#
#    gamma_pdf(A,B,C), where C is an integer, is the Erlang PDF.
#    gamma_pdf(A,B,1) is the Exponential PDF.
#    gamma_pdf(0,2,C/2) is the Chi Squared PDF with C degrees of freedom.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X.
#
#    real A, B, C, the parameters of the PDF.
#    A controls the location of the peak  A is often chosen to be 0.0.
#    B is the "scale" parameter 0.0 < B, and is often 1.0.
#    C is the "shape" parameter 0.0 < C, and is often 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = y ** ( c - 1.0 ) / ( b * gamma ( c ) * np.exp ( y ) )

  return pdf

def gamma_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## gamma_sample() samples the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 October 2004
#
#  Author:
#
#    This version by John Burkardt.
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
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

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
    return x
#
#  C < 1.
#
  if ( c < 1.0 ):

    while ( True ):

      u = rng.random ( )
      t = 1.0 + c / euler
      p = u * t

      s = exponential_01_sample ( rng )

      if ( p < 1.0 ):
        x = np.exp ( np.log ( p ) / c )
        if ( x <= s ):
          break
      else:
        x = - np.log ( ( t - p ) / c )
        if ( ( 1.0 - c ) * np.log ( x ) <= s ):
          break

    x = a + b * x
    return x
#
#  1 <= C.
#
  else:

    s2 = c - 0.5
    s = np.sqrt ( c - 0.5 )
    d = np.sqrt ( 32.0 ) - 12.0 * np.sqrt ( c - 0.5 )

    t = rng.standard_normal ( )
    x = ( np.sqrt ( c - 0.5 ) + 0.5 * t ) ** 2

    if ( 0.0 <= t ):
      x = a + b * x
      return x

    u = rng.random ( )

    if ( d * u <= t ** 3 ):
      x = a + b * x
      return x

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
        return x

    while ( True ):

      e = exponential_01_sample ( rng )

      u = rng.random ( )

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
            return x

  return x

def gamma_sample_test ( rng ):

#*****************************************************************************80
#
## gamma_sample_test() tests gamma_mean(), gamma_sample(), gamma_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000
  test_num = 2

  print ( '' )
  print ( 'gamma_sample_test():' )
  print ( '  gamma_mean() computes the Gamma mean' )
  print ( '  gamma_sample() samples the Gamma distribution' )
  print ( '  gamma_variance() computes the Gamma variance.' )

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
      print ( 'gamma_sample_test(): Fatal error!' )
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
      x[i] = gamma_sample ( a, b, c, rng )

    mean = np.mean ( x )
    variance = np.var ( x )
    xmax = np.max ( x )
    xmin = np.min ( x )

    print ( '' )
    print ( '  Sample size =     %6d' % ( nsample ) )
    print ( '  Sample mean =     %14g' % ( mean ) )
    print ( '  Sample variance = %14g' % ( variance ) )
    print ( '  Sample maximum =  %14g' % ( xmax ) )
    print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def gamma_variance ( a, b, c ):

#*****************************************************************************80
#
## gamma_variance() returns the variance of the Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = b * b * c

  return variance

def genlogistic_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## genlogistic_cdf() evaluates the Generalized Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  y = ( x - a ) / b

  cdf = 1.0 / ( 1.0 + np.exp ( - y ) ) ** c

  return cdf

def genlogistic_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## genlogistic_cdf_inv() inverts the Generalized Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  huge = np.finfo(float).max

  if ( cdf <= 0.0 ):
    x = - huge
  elif ( cdf < 1.0 ):
    x = a - b * np.log ( cdf ** ( - 1.0 / c ) - 1.0 )
  elif ( 1.0 <= cdf ):
    x = huge

  return x

def genlogistic_cdf_test ( rng ):

#*****************************************************************************80
#
## genlogistic_cdf_test() tests genlogistic_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'genlogistic_cdf_test():' )
  print ( '  genlogistic_pdf() evaluates the Genlogistic PDF.' )
  print ( '  genlogistic_cdf() evaluates the Genlogistic CDF' )
  print ( '  genlogistic_cdf_inv() inverts the Genlogistic CDF.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = genlogistic_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'genlogistic_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = genlogistic_sample ( a, b, c, rng )

    pdf = genlogistic_pdf ( x, a, b, c )

    cdf = genlogistic_cdf ( x, a, b, c )

    x2 = genlogistic_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def genlogistic_check ( a, b, c ):

#*****************************************************************************80
#
## genlogistic_check() checks the parameters of the Generalized Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'genlogistic_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'genlogistic_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def genlogistic_mean ( a, b, c ):

#*****************************************************************************80
#
## genlogistic_mean() returns the mean of the Generalized Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  euler_constant = 0.5772156649015328

  mean = a + b * ( euler_constant + digamma ( c ) )

  return mean

def genlogistic_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## genlogistic_pdf() evaluates the Generalized Logistic PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = ( C / B ) * EXP ( ( A - X ) / B ) /
#      ( ( 1 + EXP ( ( A - X ) / B ) )^(C+1) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  y = ( x - a ) / b

  pdf = ( c / b ) * np.exp ( - y ) / ( 1.0 + np.exp ( - y ) ) ** ( c + 1.0 )

  return pdf

def genlogistic_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## genlogistic_sample() samples the Generalized Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = genlogistic_cdf_inv ( cdf, a, b, c )

  return x

def genlogistic_sample_test ( rng ):

#*****************************************************************************80
#
## genlogistic_sample_test() tests genlogistic_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'genlogistic_sample_test():' )
  print ( '  genlogistic_mean() computes the Genlogistic mean' )
  print ( '  genlogistic_sample() samples the Genlogistic distribution' )
  print ( '  genlogistic_variance() computes the Genlogistic variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = genlogistic_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'genlogistic_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = genlogistic_mean ( a, b, c )
  variance = genlogistic_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = genlogistic_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def genlogistic_variance ( a, b, c ):

#*****************************************************************************80
#
## genlogistic_variance() returns the variance of the Generalized Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = b * b * ( np.pi * np.pi / 6.0 + trigamma ( c ) )

  return variance

def geometric_cdf ( x, a ):

#*****************************************************************************80
#
## geometric_cdf() evaluates the Geometric CDF.
#
#  Discussion:
#
#    CDF(X,P) is the probability that there will be at least one
#    successful trial in the first X Bernoulli trials, given that
#    the probability of success in a single trial is P.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the maximum number of trials.
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= 0 ):
    cdf = 0.0
  elif ( a == 0.0 ):
    cdf = 0.0
  elif ( a == 1.0 ):
    cdf = 1.0
  else:
    cdf = 1.0 - ( 1.0 - a ) ** x

  return cdf

def geometric_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## geometric_cdf_inv() inverts the Geometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    integer X, the corresponding value of X.
#
  import numpy as np

  huge = np.finfo(float).max

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'geometric_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'geometric_cdf_inv(): Fatal error!' )

  if ( a == 1.0 ):
    x = 1
  elif ( a == 0.0 ):
    x = huge
  else:
    x = 1 + ( np.log ( 1.0 - cdf ) // np.log ( 1.0 - a ) )

  return x

def geometric_cdf_test ( rng ):

#*****************************************************************************80
#
## geometric_cdf_test() tests geometric_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#

  print ( '' )
  print ( 'geometric_cdf_test():' )
  print ( '  geometric_cdf() evaluates the Geometric CDF' )
  print ( '  geometric_cdf_inv() inverts the Geometric CDF.' )
  print ( '  geometric_pdf() evaluates the Geometric PDF' )

  a = 0.25

  check = geometric_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'geometric_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = geometric_sample ( a, rng )

    pdf = geometric_pdf ( x, a )

    cdf = geometric_cdf ( x, a )

    x2 = geometric_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def geometric_check ( a ):

#*****************************************************************************80
#
## geometric_check() checks the parameter of the Geometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'geometric_check(): Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False

  return check

def geometric_mean ( a ):

#*****************************************************************************80
#
## geometric_mean() returns the mean of the Geometric PDF.
#
#  Discussion:
#
#    MEAN is the expected value of the number of trials required
#    to obtain a single success.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 1.0 / a

  return mean

def geometric_pdf ( x, a ):

#*****************************************************************************80
#
## geometric_pdf() evaluates the Geometric PDF.
#
#  Discussion:
#
#    PDF(X)(A) = A * ( 1 - A )^(X-1)
#
#    PDF(X)(A) is the probability that exactly X Bernoulli trials, each
#    with probability of success A, will be required to achieve
#    a single success.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the number of trials.
#    0 < X
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#

#
#  Special cases.
#
  if ( x < 1 ):

    pdf = 0.0

  elif ( a == 0.0 ):

    pdf = 0.0

  elif ( a == 1.0 ):

    if ( x == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    pdf = a * ( 1.0 - a ) ** ( x - 1 )

  return pdf

def geometric_sample ( a, rng ):

#*****************************************************************************80
#
## geometric_sample() samples the Geometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = geometric_cdf_inv ( cdf, a )

  return x

def geometric_sample_test ( rng ):

#*****************************************************************************80
#
## geometric_sample_test() tests geometric_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'geometric_sample_test():' )
  print ( '  geometric_mean() computes the Geometric mean' )
  print ( '  geometric_sample() samples the Geometric distribution' )
  print ( '  geometric_variance() computes the Geometric variance.' )

  a = 0.25

  check = geometric_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'geometric_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = geometric_mean ( a )
  variance = geometric_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = geometric_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def geometric_variance ( a ):

#*****************************************************************************80
#
## geometric_variance() returns the variance of the Geometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( 1.0 - a ) / ( a * a )

  return variance

def gompertz_cdf ( x, a, b ):

#*****************************************************************************80
#
## gompertz_cdf() evaluates the Gompertz CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( - b * ( a ** x - 1.0 ) / np.log ( a ) )

  return cdf

def gompertz_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## gompertz_cdf_inv() inverts the Gompertz CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  huge = np.finfo(float).max

  if ( cdf < 0.0 ):
    x = 0.0
  elif ( cdf < 1.0 ):
    x = np.log ( 1.0 - np.log ( 1.0 - cdf ) * np.log ( a ) / b  ) / np.log ( a )
  else:
    x = huge

  return x

def gompertz_cdf_test ( rng ):

#*****************************************************************************80
#
## gompertz_cdf_test() tests gompertz_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gompertz_cdf_test():' )
  print ( '  gompertz_cdf() evaluates the Gompertz CDF' )
  print ( '  gompertz_cdf_inv() inverts the Gompertz CDF.' )
  print ( '  gompertz_pdf() evaluates the Gompertz PDF' )

  a = 2.0
  b = 3.0

  check = gompertz_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'gompertz_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = gompertz_sample ( a, b, rng )

    pdf = gompertz_pdf ( x, a, b )

    cdf = gompertz_cdf ( x, a, b )

    x2 = gompertz_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def gompertz_check ( a, b ):

#*****************************************************************************80
#
## gompertz_check() checks the parameters of the Gompertz PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 1.0 ):
    print ( '' )
    print ( 'gompertz_check(): Fatal error!' )
    print ( '  A <= 1.0!' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'gompertz_check(): Fatal error!' )
    print ( '  B <= 0.0!' )
    check = False

  return check

def gompertz_pdf ( x, a, b ):

#*****************************************************************************80
#
## gompertz_pdf() evaluates the Gompertz PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = B * A^X / exp ( B * ( A^X - 1 ) / log ( A ) )
#
#    for
#
#      0.0 <= X
#      1.0 <  A
#      0.0 <  B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):

    pdf = 0.0

  elif ( 1.0 < a ):

    pdf = np.exp ( np.log ( b ) + x * np.log ( a ) \
      - ( b / np.log ( a ) ) * ( a ** x - 1.0 ) )

  return pdf

def gompertz_sample ( a, b, rng ):

#*****************************************************************************80
#
## gompertz_sample() samples the Gompertz PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = gompertz_cdf_inv ( cdf, a, b )

  return x

def gompertz_sample_test ( rng ):

#*****************************************************************************80
#
## gompertz_sample_test() tests gompertz_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'gompertz_sample_test():' )
  print ( '  gompertz_sample() samples the Gompertz distribution' )

  a = 2.0
  b = 3.0

  check = gompertz_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'gompertz_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = gompertz_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def gumbel_cdf ( x ):

#*****************************************************************************80
#
## gumbel_cdf() evaluates the Gumbel CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  cdf = np.exp ( - np.exp ( - x ) )

  return cdf

def gumbel_cdf_inv ( cdf ):

#*****************************************************************************80
#
## gumbel_cdf_inv() inverts the Gumbel CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'gumbel_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'gumbel_cdf_inv(): Fatal error!' )

  x =  - np.log ( - np.log ( cdf ) )

  return x

def gumbel_cdf_test ( rng ):

#*****************************************************************************80
#
## gumbel_cdf_test() tests gumbel_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gumbel_cdf_test():' )
  print ( '  gumbel_cdf() evaluates the Gumbel CDF.' )
  print ( '  gumbel_cdf_inv() inverts the Gumbel CDF.' )
  print ( '  gumbel_pdf() evaluates the Gumbel PDF.' )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = gumbel_sample ( rng )

    pdf = gumbel_pdf ( x )

    cdf = gumbel_cdf ( x )

    x2 = gumbel_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def gumbel_mean ( ):

#*****************************************************************************80
#
## gumbel_mean() returns the mean of the Gumbel PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  euler_constant = 0.5772156649015328;

  mean = euler_constant

  return mean

def gumbel_pdf ( x ):

#*****************************************************************************80
#
## gumbel_pdf() evaluates the Gumbel PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - X - EXP ( - X  ) ).
#
#    gumbel_pdf(X) = extreme_pdf(X)(0,1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998.
#
#  Input:
#
#    real X, the argument of the PDF.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - x - np.exp ( - x ) )

  return pdf

def gumbel_sample ( rng ):

#*****************************************************************************80
#
## gumbel_sample() samples the Gumbel PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = gumbel_cdf_inv ( cdf )

  return x

def gumbel_sample_test ( rng ):

#*****************************************************************************80
#
## gumbel_sample_test() tests gumbel_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'gumbel_sample_test():' )
  print ( '  gumbel_mean() computes the Gumbel mean' )
  print ( '  gumbel_sample() samples the Gumbel distribution' )
  print ( '  gumbel_variance() computes the Gumbel variance.' )

  mean = gumbel_mean ( )

  variance = gumbel_variance ( )

  print ( '' )
  print ( '  PDF mean      =               %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = gumbel_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def gumbel_variance ( ):

#*****************************************************************************80
#
## gumbel_variance() returns the variance of the Gumbel PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = np.pi * np.pi / 6.0

  return variance

def half_normal_cdf ( x, a, b ):

#*****************************************************************************80
#
## half_normal_cdf() evaluates the Half Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= a ):
    cdf = 0.0
  else:
    cdf2 = normal_cdf ( x, a, b )
    cdf = 2.0 * cdf2 - 1.0

  return cdf

def half_normal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## half_normal_cdf_inv() inverts the Half Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'half_normal_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'half_normal_cdf_inv(): Fatal error!' )

  cdf2 = 0.5 * ( cdf + 1.0 )

  x = normal_cdf_inv ( cdf2, a, b )

  return x

def half_normal_cdf_test ( rng ):

#*****************************************************************************80
#
## half_normal_cdf_test() tests half_normal_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'half_normal_cdf_test():' )
  print ( '  half_normal_cdf() evaluates the Half Normal CDF.' )
  print ( '  half_normal_cdf_inv() inverts the Half Normal CDF.' )
  print ( '  half_normal_pdf() evaluates the Half Normal PDF.' )

  a = 0.0
  b = 2.0

  check = half_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'half_normal_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =         %14g' % ( a ) )
  print ( '  PDF parameter B =         %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = half_normal_sample ( a, b, rng )

    pdf = half_normal_pdf ( x, a, b )

    cdf = half_normal_cdf ( x, a, b )

    x2 = half_normal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def half_normal_check ( a, b ):

#*****************************************************************************80
#
## half_normal_check() checks the parameters of the Half Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'half_normal_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def half_normal_mean ( a, b ):

#*****************************************************************************80
#
## half_normal_mean() returns the mean of the Half Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = a + b * np.sqrt ( 2.0 / np.pi )

  return mean

def half_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## half_normal_pdf() evaluates the Half Normal PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) =
#      SQRT ( 2 / PI ) * ( 1 / B ) * EXP ( - 0.5 * ( ( X - A ) / B )^2 )
#
#    for A <= X
#
#    The Half Normal PDF is a special case of both the Chi PDF and the
#    Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real  A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = np.sqrt ( 2.0 / np.pi ) * ( 1.0 / b ) * np.exp ( - 0.5 * y * y )

  return pdf

def half_normal_sample ( a, b, rng ):

#*****************************************************************************80
#
## half_normal_sample() samples the Half Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = half_normal_cdf_inv ( cdf, a, b )

  return x

def half_normal_sample_test ( rng ):

#*****************************************************************************80
#
## half_normal_sample_test() tests half_normal_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'half_normal_sample_test():' )
  print ( '  half_normal_mean() computes the Half Normal mean' )
  print ( '  half_normal_sample() samples the Half Normal distribution' )
  print ( '  half_normal_variance() computes the Half Normal variance.' )

  a = 0.0
  b = 10.0

  check = half_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'half_normal_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = half_normal_mean ( a, b )
  variance = half_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = half_normal_sample ( a, b, rng )
 
  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def half_normal_variance ( a, b ):

#*****************************************************************************80
#
## half_normal_variance() returns the variance of the Half Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = b * b * ( 1.0 - 2.0 / np.pi )

  return variance

def hypergeometric_cdf ( x, n, m, l ):

#*****************************************************************************80
#
## hypergeometric_cdf() evaluates the Hypergeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the CDF.
#
#    integer N, the number of balls selected.
#    0 <= N <= L.
#
#    integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    integer L, the number of balls to select from.
#    0 <= L.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  from scipy.special import comb
  import numpy as np

  pdf = comb ( l - m, n ) / comb ( l, n )
  cdf = pdf

  for x2 in range ( 0, x ):

    pdf = pdf * float ( ( m - x2 ) * ( n - x2 ) ) \
      / float ( ( x2 + 1 ) * ( l - m - n + x2 + 1 ) )

    cdf = cdf + pdf

  return cdf

def hypergeometric_cdf_test ( rng ):

#*****************************************************************************80
#
## hypergeometric_cdf_test() tests hypergeometric_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hypergeometric_cdf_test():' )
  print ( '  hypergeometric_cdf() evaluates the Hypergeometric CDF.' )
  print ( '  hypergeometric_pdf() evaluates the Hypergeometric PDF.' )

  x = 7

  n = 10
  m = 7
  l = 100

  check = hypergeometric_check ( n, m, l )

  if ( not check ):
    print ( '' )
    print ( 'hypergeometric_cdf_test(): Fatal error!' )
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

  return

def hypergeometric_check ( n, m, l ):

#*****************************************************************************80
#
## hypergeometric_check() checks the parameters of the Hypergeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of balls selected.
#    0 <= N <= L.
#
#    integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    integer L, the number of balls to select from.
#    0 <= L.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( n < 0 or l < n ):
    print ( '' )
    print ( 'hypergeometric_check(): Fatal error!' )
    print ( '  Input N is out of range.' )
    check = False

  if ( m < 0 or l < m ):
    print ( '' )
    print ( 'hypergeometric_check(): Fatal error!' )
    print ( '  Input M is out of range.' )
    check = False

  if ( l < 0 ):
    print ( '' )
    print ( 'hypergeometric_check(): Fatal error!' )
    print ( '  Input L is out of range.' )
    check = False

  return check

def hypergeometric_mean ( n, m, l ):

#*****************************************************************************80
#
## hypergeometric_mean() returns the mean of the Hypergeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of balls selected.
#    0 <= N <= L.
#
#    integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    integer L, the number of balls to select from.
#    0 <= L.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = float ( n * m ) / float ( l )

  return mean

def hypergeometric_pdf ( x, n, m, l ):

#*****************************************************************************80
#
## hypergeometric_pdf() evaluates the Hypergeometric PDF.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the desired number of white balls.
#    0 <= X <= N, usually, although any value of X can be given.
#
#    integer N, the number of balls selected.
#    0 <= N <= L.
#
#    integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    integer L, the number of balls to select from.
#    0 <= L.
#
#  Output:
#
#    real PDF, the probability of exactly K white balls.
#
  from scipy.special import comb
  import numpy as np
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

    pdf = comb ( m, x ) * comb ( l - m, n - x ) / comb ( l, n )

  return pdf

def hypergeometric_sample ( n, m, l, rng ):

#*****************************************************************************80
#
## hypergeometric_sample() samples the Hypergeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of balls selected.
#    0 <= N <= L.
#
#    integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    integer L, the number of balls to select from.
#    0 <= L.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  from scipy.special import comb
  import numpy as np

  a = comb ( l - m, n ) / comb ( l, n )
  b = a

  u = rng.random ( )

  x = 0

  while ( a < u ):

    b = b * float ( ( m - x ) * ( n - x ) ) / float ( ( x + 1 ) * ( l - m - n + x + 1 ) )

    a = a + b

    x = x + 1

  return x

def hypergeometric_sample_test ( rng ):

#*****************************************************************************80
#
## hypergeometric_sample_test() tests hypergeometric_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'hypergeometric_sample_test():' )
  print ( '  hypergeometric_mean() computes the Hypergeometric mean' )
  print ( '  hypergeometric_sample() samples the Hypergeometric distribution' )
  print ( '  hypergeometric_variance() computes the Hypergeometric variance.' )

  n = 10
  m = 7
  l = 100

  check = hypergeometric_check ( n, m, l )

  if ( not check ):
    print ( '' )
    print ( 'hypergeometric_sample_test(): Fatal error!' )
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
    x[i] = hypergeometric_sample ( n, m, l, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def hypergeometric_variance ( n, m, l ):

#*****************************************************************************80
#
## hypergeometric_variance() returns the variance of the Hypergeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of balls selected.
#    0 <= N <= L.
#
#    integer M, the number of white balls in the population.
#    0 <= M <= L.
#
#    integer L, the number of balls to select from.
#    0 <= L.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = float ( n * m * ( l - m ) * ( l - n ) ) / float ( l * l * ( l - 1 ) )

  return variance

def i4_choose ( n, k ):

#*****************************************************************************80
#
## i4_choose() computes the binomial coefficient C(N,K) as an I4.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in integer arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#    Instead of i4_choose(), you could use scipy.special.comb ( n, k ),
#    except that that function uses real arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    ML Wolfson, HV Wright,
#    Algorithm 160:
#    Combinatorial of M Things Taken N at a Time,
#    Communications of the ACM,
#    Volume 6, Number 4, April 1963, page 161.
#
#  Input:
#
#    integer N, K, are the values of N and K.
#
#  Output:
#
#    integer VALUE, the number of combinations of N
#    things taken K at a time.
#
  mn = min ( k, n - k )
  mx = max ( k, n - k )

  if ( mn < 0 ):

    value = 0

  elif ( mn == 0 ):

    value = 1

  else:

    value = mx + 1

    for i in range ( 2, mn + 1 ):
      value = ( value * ( mx + i ) ) // i

  return value

def i4_choose_test ( ):

#*****************************************************************************80
#
## i4_choose_test() tests i4_choose().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_choose_test():' )
  print ( '  i4_choose() evaluates C(N,K).' )
  print ( '' )
  print ( '       N       K     CNK' )

  for n in range ( 0, 5 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = i4_choose ( n, k )

      print ( '  %6d  %6d  %6d' % ( n, k, cnk ) )

  return

def i4_factorial_log ( n ):

#*****************************************************************************80
#
## i4_factorial_log() returns the logarithm of N factorial.
#
#  Discussion:
#
#    N! = Product ( 1 <= I <= N ) I
#
#    N! = Gamma(N+1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the function.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the logarithm of N factorial.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'i4_factorial_log(): Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'i4_factorial_log(): Fatal error!' )

  value = 0.0

  for i in range ( 2, n + 1 ):
    value = value + np.log ( i )

  return value

def i4_factorial_log_test ( ):

#*****************************************************************************80
#
## i4_factorial_log_test() tests i4_factorial_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4_factorial_log_test():' )
  print ( '  i4_factorial_log() evaluates log(N!).' )
  print ( '' )
  print ( '         N           lfact          elfact         fact' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fact = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    lfact = i4_factorial_log ( n )
    elfact = np.exp ( lfact )

    print ( '  %8d  %14.6g  %14.6g  %12d' % ( n, lfact, elfact, fact ) )

  return

def i4_factorial_values ( n_data ):

#*****************************************************************************80
#
## i4_factorial_values() returns values of the factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) I
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    integer FN, the value of the function.
#
  import numpy as np

  n_max = 13

  fn_vec = np.array ( [ \
            1, \
            1, \
            2, \
            6, \
           24, \
          120, \
          720, \
         5040, \
        40320, \
       362880, \
      3628800, \
     39916800, \
    479001600 ] )
  n_vec = np.array ( [ \
     0,  1,  2,  3, \
     4,  5,  6,  7, \
     8,  9, 10, 11, \
    12 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def i4_factorial_values_test ( ):

#*****************************************************************************80
#
## i4_factorial_values_test() tests i4_factorial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_factorial_values_test():' )
  print ( '  i4_factorial_values() returns values of the integer factorial function.' )
  print ( '' )
  print ( '          N          i4_factorial(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %12d' % ( n, fn ) )

  return

def i4_is_power_of_10 ( n ):

#*****************************************************************************80
#
## i4_is_power_of_10() reports whether an integer is a power of 10.
#
#  Discussion:
#
#    The powers of 10 are 1, 10, 100, 1000, 10000, and so on.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be tested.
#
#  Output:
#
#    bool VALUE, is TRUE if N is a power of 10.
#
  value = False

  if ( n <= 0 ):
    return value

  while ( 1 < n ):

    if ( ( n % 10 ) != 0 ):
      return value

    n = n // 10

  value = True

  return value

def i4_is_power_of_10_test ( ):

#*****************************************************************************80
#
## i4_is_power_of_10_test() tests i4_is_power_of_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_is_power_of_10_test():' )
  print ( '  i4_is_power_of_10() reports whether an I4 is a power of 10.' )
  print ( '' )
  print ( '  I     i4_is_power_of_10(I)' )
  print ( '' )

  for i in range ( 97, 104 ):
    print ( '  %6d  %s' % ( i, i4_is_power_of_10 ( i ) ) )

  return

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print() prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## i4mat_print_test() tests i4mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_print_test():' )
  print ( '  i4mat_print() prints an I4MAT.' )

  m = 5
  n = 6
  a = np.array ( ( \
    ( 11, 12, 13, 14, 15, 16 ), \
    ( 21, 22, 23, 24, 25, 26 ), \
    ( 31, 32, 33, 34, 35, 36 ), \
    ( 41, 42, 43, 44, 45, 46 ), \
    ( 51, 52, 53, 54, 55, 56 ) ) )
  title = '  A 5 x 6 integer matrix:'
  i4mat_print ( m, n, a, title )

  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some() prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 10

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_print_some_test() tests i4mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_print_some_test():' )
  print ( '  i4mat_print_some() prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )

  return

def i4row_max ( m, n, x ):

#*****************************************************************************80
#
## i4row_max() returns the maximums of rows of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer X(M,N), the I4ROW.
#
#  Output:
#
#    integer XMAX(M), the maximums of the rows of X.
#
  import numpy as np

  xmax = np.zeros ( m, dtype = np.int32 )

  for i in range ( 0, m ):
    xmax[i] = x[i,0]
    for j in range ( 1, n ):
      xmax[i] = max ( xmax[i], x[i,j] )

  return xmax

def i4row_max_test ( ):

#*****************************************************************************80
#
## i4row_max_test() tests i4row_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_max_test():' )
  print ( '  i4row_max() computes maximums of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  amax = i4row_max ( m, n, a )

  i4vec_print ( m, amax, '  Row maximums:' )

  return

def i4row_mean ( m, n, a ):

#*****************************************************************************80
#
## i4row_mean() returns the means of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the I4ROW
#
#  Output:
#
#    real ROW_mean(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def i4row_mean_test ( ):

#*****************************************************************************80
#
## i4row_mean_test() tests i4row_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_mean_test():' )
  print ( '  i4row_mean() computes row means of an I4ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  means = i4row_mean ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )

  return

def i4row_min ( m, n, x ):

#*****************************************************************************80
#
## i4row_min() returns the minimums of rows of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer X(M,N), the I4ROW.
#
#  Output:
#
#    integer XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m, dtype = np.int32 )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def i4row_min_test ( ):

#*****************************************************************************80
#
## i4row_min_test() tests i4row_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_min_test():' )
  print ( '  i4row_min() computes minimums of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  amin = i4row_min ( m, n, a )

  i4vec_print ( m, amin, '  Row minimums:' )

  return

def i4row_variance ( m, n, x ):

#*****************************************************************************80
#
## i4row_variance() returns the variances of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer X(M,N), the I4ROW whose row means are desired.
#
#  Output:
#
#    real VARIANCE(M), the variances of the rows of X.
#
  import numpy as np

  variance = np.zeros ( m, dtype = np.float32 )

  for i in range ( 0, m ):

    mean = 0.0
    for j in range ( 0, n ):
      mean = mean + x[i,j]
    mean = mean / float ( n )

    for j in range ( 0, n ):
      variance[i] = variance[i] + ( x[i,j] - mean ) ** 2

    if ( 1 < n ):
      variance[i] = variance[i] / float ( n - 1 )
    else:
      variance[i] = 0.0 

  return variance

def i4row_variance_test ( ):

#*****************************************************************************80
#
## i4row_variance_test() tests i4row_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_variance_test():' )
  print ( '  i4row_variance() computes variances of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  variance = i4row_variance ( m, n, a )

  r8vec_print ( m, variance, '  The row variances:' )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  return

def i4vec_run_count ( n, a ):

#*****************************************************************************80
#
## i4vec_run_count() counts runs of equal values in an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of integer values.
#
#    A run is a sequence of equal values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector to be examined.
#
#  Output:
#
#    integer RUN_count, the number of runs.
#
  run_count = 0

  if ( n < 1 ):
    return run_count

  test = -1

  for i in range ( 0, n ):

    if ( i == 0 or a[i] != test ):
      run_count = run_count + 1
      test = a[i]

  return run_count

def i4vec_run_count_test ( rng ):

#*****************************************************************************80
#
## i4vec_run_count_test() tests i4vec_run_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 20

  print ( '' )
  print ( 'i4vec_run_count_test():' )
  print ( '  i4vec_run_count() counts runs in an I4VEC' )
  print ( '' )
  print ( ' Run Count        Sequence' )
  print ( '' )

  for test in range ( 0, 10 ):

    a = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

    run_count = i4vec_run_count ( n, a )

    print ( '  %8d        ' % ( run_count ), end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( a[i] ), end = '' )
    print ( '' )

  return

def i4vec_unique_count ( n, a ):

#*****************************************************************************80
#
## i4vec_unique_count() counts the unique elements in an I4VEC.
#
#  Discussion:
#
#    Because the array is sorted, this algorithm is O(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 April 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    integer A(N), the sorted array to examine.
#
#  Output:
#
#    integer UNIQUE_NUM, the number of unique elements of A.
#
  unique_num = 0

  for i in range ( 0, n ):

    unique_num = unique_num + 1

    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        unique_num = unique_num - 1
        break

  return unique_num

def i4vec_unique_count_test ( rng ):

#*****************************************************************************80
#
## i4vec_unique_count_test() tests i4vec_unique_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 20
  b = 0
  c = n

  print ( '' )
  print ( 'i4vec_unique_count_test():' )
  print ( '  i4vec_unique_count() counts unique entries in an I4VEC.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  a_unique = i4vec_unique_count ( n, a )

  print ( '' )
  print ( '  Number of unique entries is %d' % ( a_unique ) )

  return

def inverse_gaussian_cdf ( x, a, b ):

#*****************************************************************************80
#
## inverse_gaussian_cdf() evaluates the Inverse Gaussian CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#    0.0 < X.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    x1 = np.sqrt ( b / x ) * ( x - a ) / a
    cdf1 = normal_01_cdf ( x1 )

    x2 = - np.sqrt ( b / x ) * ( x + a ) / a
    cdf2 = normal_01_cdf ( x2 )

    cdf = cdf1 + np.exp ( 2.0 * b / a ) * cdf2

  return cdf

def inverse_gaussian_cdf_test ( rng ):

#*****************************************************************************80
#
## inverse_gaussian_cdf_test() tests inverse_gaussian_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'inverse_gaussian_cdf_test():' )
  print ( '  inverse_gaussian_cdf() evaluates the Inverse Gaussian CDF.' )
  print ( '  inverse_gaussian_pdf() evaluates the Inverse Gaussian PDF.' )

  a = 5.0
  b = 2.0

  if ( not inverse_gaussian_check ( a, b ) ):
    print ( '' )
    print ( 'inverse_gaussian_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = inverse_gaussian_sample ( a, b, rng )

    pdf = inverse_gaussian_pdf ( x, a, b )

    cdf = inverse_gaussian_cdf ( x, a, b )

    print ( ' %14g  %14g  %14g' % ( x, pdf, cdf ) )

  return

def inverse_gaussian_check ( a, b ):

#*****************************************************************************80
#
## inverse_gaussian_check() checks the parameters of the Inverse Gaussian CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'inverse_gaussian_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'inverse_gaussian_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def inverse_gaussian_mean ( a, b ):

#*****************************************************************************80
#
## inverse_gaussian_mean() returns the mean of the Inverse Gaussian PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def inverse_gaussian_pdf ( x, a, b ):

#*****************************************************************************80
#
## inverse_gaussian_pdf() evaluates the Inverse Gaussian PDF.
#
#  Discussion:
#
#    The Inverse Gaussian PDF is also known as the Wald PDF
#    and the Inverse Normal PDF.
#
#    PDF(X)(A,B)
#      = SQRT ( B / ( 2 * PI * X^3 ) )
#        * EXP ( - B * ( X - A )^2 / ( 2.0 * A^2 * X ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 < X
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    pdf = 0.0
  else:
    pdf = np.sqrt ( b / ( 2.0 * np.pi * x ** 3 ) ) * \
      np.exp ( - b * ( x - a ) ** 2 / ( 2.0 * a ** 2 * x ) )

  return pdf

def inverse_gaussian_sample ( a, b, rng ):

#*****************************************************************************80
#
## inverse_gaussian_sample() samples the Inverse Gaussian PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  phi = b / a
  z = normal_01_sample ( rng )
  y = z * z

  t = 1.0 + 0.5 * ( y - np.sqrt ( 4.0 * phi * y + y * y ) ) / phi
  u = rng.random ( )

  if ( u * ( 1.0 + t ) <= 1.0 ):
    x = a * t
  else:
    x = a / t

  return x

def inverse_gaussian_sample_test ( rng ):

#*****************************************************************************80
#
## inverse_gaussian_sample_test() tests inverse_gaussian_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'inverse_gaussian_sample_test():' )
  print ( '  inverse_gaussian_mean() computes the Inverse Gaussian mean' )
  print ( '  inverse_gaussian_sample() samples the Inverse Gaussian distribution' )
  print ( '  inverse_gaussian_variance() computes the Inverse Gaussian variance.' )

  a = 2.0
  b = 3.0

  check = inverse_gaussian_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'inverse_gaussian_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = inverse_gaussian_mean ( a, b )
  variance = inverse_gaussian_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = inverse_gaussian_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def inverse_gaussian_variance ( a, b ):

#*****************************************************************************80
#
## inverse_gaussian_variance() returns the variance of the Inverse Gaussian PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a ** 3 / b

  return variance

def laplace_cdf ( x, a, b ):

#*****************************************************************************80
#
## laplace_cdf() evaluates the Laplace CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the PDF.
#
  import numpy as np

  y = ( x - a ) / b

  if ( x <= a ):
    cdf = 0.5 * np.exp ( y )
  else:
    cdf = 1.0 - 0.5 * np.exp ( - y )

  return cdf

def laplace_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## laplace_cdf_inv() inverts the Laplace CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'laplace_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'laplace_cdf_inv(): Fatal error!' )

  if ( cdf <= 0.5 ):
    x = a + b * np.log ( 2.0 * cdf )
  else:
    x = a - b * np.log ( 2.0 * ( 1.0 - cdf ) )

  return x

def laplace_cdf_test ( rng ):

#*****************************************************************************80
#
## laplace_cdf_test() tests laplace_cdf(), laplace_cdf_inv(), laplace_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laplace_cdf_test():' )
  print ( '  laplace_cdf() evaluates the Laplace CDF' )
  print ( '  laplace_cdf_inv() inverts the Laplace CDF.' )
  print ( '  laplace_pdf() evaluates the Laplace PDF' )

  a = 1.0
  b = 2.0

  check = laplace_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'laplace_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = laplace_sample ( a, b, rng )

    pdf = laplace_pdf ( x, a, b )

    cdf = laplace_cdf ( x, a, b )

    x2 = laplace_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def laplace_check ( a, b ):

#*****************************************************************************80
#
## laplace_check() checks the parameters of the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'laplace_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def laplace_mean ( a, b ):

#*****************************************************************************80
#
## laplace_mean() returns the mean of the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def laplace_pdf ( x, a, b ):

#*****************************************************************************80
#
## laplace_pdf() evaluates the Laplace PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = exp ( - abs ( X - A ) / B ) / ( 2 * B )
#
#    The Laplace PDF is also known as the Double Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - abs ( x - a ) / b ) / ( 2.0 * b )

  return pdf

def laplace_sample ( a, b, rng ):

#*****************************************************************************80
#
## laplace_sample() samples the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = laplace_cdf_inv ( cdf, a, b )

  return x

def laplace_sample_test ( rng ):

#*****************************************************************************80
#
## laplace_sample_test() tests laplace_mean(), laplace_sample(), laplace_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'laplace_sample_test():' )
  print ( '  laplace_mean() computes the Laplace mean' )
  print ( '  laplace_sample() samples the Laplace distribution' )
  print ( '  laplace_variance() computes the Laplace variance.' )

  a = 1.0
  b = 2.0

  check = laplace_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'laplace_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = laplace_mean ( a, b )
  variance = laplace_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = laplace_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def laplace_variance ( a, b ):

#*****************************************************************************80
#
## laplace_variance() returns the variance of the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 2.0 * b * b

  return variance

def levy_cdf ( x, a, b ):

#*****************************************************************************80
#
## levy_cdf() evaluates the Levy CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#    Normally, A <= X.
#
#    real A, B, the parameters of the PDF.
#    0 < B.
#
#  Output:
#
#    real CDF, the value of the PDF.
#
  import numpy as np

  if ( b <= 0.0 ):
    print ( '' )
    print ( '  levy_pdf(): Fatal error!' )
    print ( '  Input parameter B <= 0.0' )
    raise Exception ( 'levy_pdf(): Fatal error!' )

  if ( x <= a ):
    cdf = 0.0
  else:
    cdf = 1.0 - r8_erf ( np.sqrt ( b / ( 2.0 * ( x - a ) ) ) )

  return cdf

def levy_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## levy_cdf_inv() inverts the Levy CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'levy_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'levy_cdf_inv(): Fatal error!' )

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'levy_cdf_inv(): Fatal error!' )
    print ( '  Input parameter B <= 0.0' )
    raise Exception ( 'levy_cdf_inv(): Fatal error!' )

  cdf1 = 1.0 - 0.5 * cdf
  x1 = normal_01_cdf_inv ( cdf1 )
  x = a + b / ( x1 * x1 )

  return x

def levy_cdf_test ( rng ):

#*****************************************************************************80
#
## levy_cdf_test() tests levy_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'levy_cdf_test():' )
  print ( '  levy_cdf() evaluates the Levy CDF' )
  print ( '  levy_cdf_inv() inverts the Levy CDF.' )
  print ( '  levy_pdf() evaluates the Levy PDF' )

  a = 1.0
  b = 2.0

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = levy_sample ( a, b, rng )

    pdf = levy_pdf ( x, a, b )

    cdf = levy_cdf ( x, a, b )

    x2 = levy_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def levy_pdf ( x, a, b ):

#*****************************************************************************80
#
## levy_pdf() evaluates the Levy PDF.
#
#  Discussion:
#
#    PDF(A,BX) = sqrt ( B / ( 2 * PI ) )
#               * exp ( - B / ( 2 * ( X - A ) ) 
#               / ( X - A )^(3/2)
#
#    for A <= X.
#
#    Note that the Levy PDF does not have a finite mean or variance.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    Normally, A <= X.
#
#    real A, B, the parameters of the PDF.
#    0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( b <= 0.0 ):
    print ( '' )
    print ( '  levy_pdf(): Fatal error!' )
    print ( '  Input parameter B <= 0.0' )
    raise Exception ( 'levy_pdf(): Fatal error!' )

  if ( x < a ):
    pdf = 0.0
  else:
    pdf = np.sqrt ( b / ( 2.0 * np.pi ) ) \
        * np.exp ( - b / ( 2.0 * ( x - a ) ) ) \
        / np.sqrt ( ( x - a ) ** 3 )

  return pdf

def levy_sample ( a, b, rng ):

#*****************************************************************************80
#
## levy_sample() samples the Levy PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = levy_cdf_inv ( cdf, a, b )

  return x

def logistic_cdf ( x, a, b ):

#*****************************************************************************80
#
## logistic_cdf() evaluates the Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 1.0 / ( 1.0 + np.exp ( ( a - x ) / b ) )

  return cdf

def logistic_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## logistic_cdf_inv() inverts the Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'logistic_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'logistic_cdf_inv(): Fatal error!' )

  x = a - b * np.log ( ( 1.0 - cdf ) / cdf )

  return x

def logistic_cdf_test ( rng ):

#*****************************************************************************80
#
## logistic_cdf_test() tests logistic_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'logistic_cdf_test():' )
  print ( '  logistic_cdf() evaluates the Logistic CDF' )
  print ( '  logistic_cdf_inv() inverts the Logistic CDF.' )
  print ( '  logistic_pdf() evaluates the Logistic PDF' )

  a = 1.0
  b = 2.0

  check = logistic_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'logistic_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = logistic_sample ( a, b, rng )

    pdf = logistic_pdf ( x, a, b )

    cdf = logistic_cdf ( x, a, b )

    x2 = logistic_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def logistic_check ( a, b ):

#*****************************************************************************80
#
## logistic_check() checks the parameters of the Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'logistic_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def logistic_mean ( a, b ):

#*****************************************************************************80
#
## logistic_mean() returns the mean of the Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def logistic_pdf ( x, a, b ):

#*****************************************************************************80
#
## logistic_pdf() evaluates the Logistic PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = EXP ( ( A - X ) / B ) /
#      ( B * ( 1 + EXP ( ( A - X ) / B ) )^2 )
#
#    The Logistic PDF is also known as the Sech-Squared PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  temp = np.exp ( ( a - x ) / b )

  pdf = temp / ( b * ( 1.0 + temp ) ** 2 )

  return pdf

def logistic_sample ( a, b, rng ):

#*****************************************************************************80
#
## logistic_sample() samples the Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = logistic_cdf_inv ( cdf, a, b )

  return x

def logistic_sample_test ( rng ):

#*****************************************************************************80
#
## logistic_sample_test() tests logistic_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'logistic_sample_test():' )
  print ( '  logistic_mean() computes the Logistic mean' )
  print ( '  logistic_sample() samples the Logistic distribution' )
  print ( '  logistic_variance() computes the Logistic variance.' )

  a = 2.0
  b = 3.0

  check = logistic_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'logistic_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = logistic_mean ( a, b )
  variance = logistic_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = logistic_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def logistic_variance ( a, b ):

#*****************************************************************************80
#
## logistic_variance() returns the variance of the Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = ( np.pi * b ) ** 2 / 3.0

  return variance

def log_normal_cdf ( x, a, b ):

#*****************************************************************************80
#
## log_normal_cdf() evaluates the Lognormal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 < X.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    logx = np.log ( x )

    cdf = normal_cdf ( logx, a, b )

  return cdf

def log_normal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## log_normal_cdf_inv() inverts the Lognormal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'log_normal_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'log_normal_cdf_inv(): Fatal error!' )

  logx = normal_cdf_inv ( cdf, a, b )

  x = np.exp ( logx )

  return x

def log_normal_cdf_test ( rng ):

#*****************************************************************************80
#
## log_normal_cdf_test() tests log_normal_cdf(), log_normal_cdf_inv(), log_normal_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'log_normal_cdf_test():' )
  print ( '  log_normal_cdf() evaluates the Log Normal CDF' )
  print ( '  log_normal_cdf_inv() inverts the Log Normal CDF.' )
  print ( '  log_normal_pdf() evaluates the Log Normal PDF' )

  a = 10.0
  b = 2.25

  check = log_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'log_normal_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = log_normal_sample ( a, b, rng )

    pdf = log_normal_pdf ( x, a, b )

    cdf = log_normal_cdf ( x, a, b )

    x2 = log_normal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def log_normal_check ( a, b ):

#*****************************************************************************80
#
## log_normal_check() checks the parameters of the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'log_normal_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def log_normal_mean ( a, b ):

#*****************************************************************************80
#
## log_normal_mean() returns the mean of the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = np.exp ( a + 0.5 * b * b )

  return mean

def log_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## log_normal_pdf() evaluates the Lognormal PDF.
#
#  Discussion:
#
#    PDF(X)(A,B)
#      = EXP ( - 0.5 * ( ( LOG ( X ) - A ) / B )^2 )
#        / ( B * X * SQRT ( 2 * PI ) )
#
#    The Lognormal PDF is also known as the Cobb-Douglas PDF,
#    and as the Antilog_normal PDF.
#
#    The Lognormal PDF describes a variable X whose logarithm
#    is normally distributed.
#
#    The special case A = 0, B = 1 is known as Gilbrat's PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 < X
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    pdf = 0.0
  else:
    pdf = np.exp ( - 0.5 * ( ( np.log ( x ) - a ) / b ) ** 2 ) \
      / ( b * x * np.sqrt ( 2.0 * np.pi ) )

  return pdf

def log_normal_sample ( a, b, rng ):

#*****************************************************************************80
#
## log_normal_sample() samples the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = log_normal_cdf_inv ( cdf, a, b )

  return x

def log_normal_sample_test ( rng ):

#*****************************************************************************80
#
## log_normal_sample_test() tests log_normal_mean(), log_normal_sample(), log_normal_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'log_normal_sample_test():' )
  print ( '  log_normal_mean() computes the Log Normal mean' )
  print ( '  log_normal_sample() samples the Log Normal distribution' )
  print ( '  log_normal_variance() computes the Log Normal variance.' )

  a = 1.0
  b = 2.0

  check = log_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'log_normal_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = log_normal_mean ( a, b )
  variance = log_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = log_normal_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def log_normal_variance ( a, b ):

#*****************************************************************************80
#
## log_normal_variance() returns the variance of the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = np.exp ( 2.0 * a + b * b ) * ( np.exp ( b * b ) - 1.0 )

  return variance

def log_series_cdf ( x, a ):

#*****************************************************************************80
#
## log_series_cdf() evaluates the Logarithmic Series CDF.
#
#  Discussion:
#
#    Simple summation is used, with a recursion to generate successive
#    values of the PDF.
#
#    Thanks to Oscar van Vlijmen.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#    0 < X
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 0.0

  for x2 in range ( 1, x + 1 ):

    if ( x2 == 1 ):
      pdf = - a / np.log ( 1.0 - a )
    else:
      pdf = ( x2 - 1 ) * a * pdf / x2

    cdf = cdf + pdf
 
  return cdf

def log_series_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## log_series_cdf_inv() inverts the Logarithmic Series CDF.
#
#  Discussion:
#
#    Simple summation is used.  The only protection against an
#    infinite loop caused by roundoff is that X cannot be larger
#    than 1000.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    real X, the argument of the CDF for which
#    CDF(X-1) <= CDF <= CDF(X).
#
  import numpy as np

  xmax = 1000

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'log_series_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'log_series_cdf_inv(): Fatal error!' )

  cdf2 = 0.0
  x = 1

  while ( cdf2 < cdf and x < xmax ):

    if ( x == 1 ):
      pdf = - a / np.log ( 1.0 - a )
    else:
      pdf = ( x - 1 ) * a * pdf / x

    cdf2 = cdf2 + pdf

    x = x + 1

  return x

def log_series_cdf_test ( rng ):

#*****************************************************************************80
#
## log_series_cdf_test() tests log_series_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'log_series_cdf_test():' )
  print ( '  log_series_cdf() evaluates the Log Series CDF' )
  print ( '  log_series_cdf_inv() inverts the Log Series CDF.' )
  print ( '  log_series_pdf() evaluates the Log Series PDF' )

  a = 0.25

  check = log_series_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'log_series_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =  %14g' % ( a ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = log_series_sample ( a, rng )

    pdf = log_series_pdf ( x, a )

    cdf = log_series_cdf ( x, a )

    x2 = log_series_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def log_series_check ( a ):

#*****************************************************************************80
#
## log_series_check() checks the parameter of the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 or 1.0 <= a ):
    print ( '' )
    print ( 'log_series_check(): Fatal error!' )
    print ( '  A <= 0.0 or 1.0 <= A' )
    check = False

  return check

def log_series_mean ( a ):

#*****************************************************************************80
#
## log_series_mean() returns the mean of the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = - a / ( ( 1.0 - a ) * np.log ( 1.0 - a ) )

  return mean

def log_series_pdf ( x, a ):

#*****************************************************************************80
#
## log_series_pdf() evaluates the Logarithmic Series PDF.
#
#  Discussion:
#
#    PDF(X)(A) = - A ^ X / ( X * log ( 1 - A ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#    0 < X
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0 ):
    pdf = 0.0
  else:
    pdf = - a ** x / ( x * np.log ( 1.0 - a ) )

  return pdf

def log_series_sample ( a, rng ):

#*****************************************************************************80
#
## log_series_sample() samples the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer-Verlag, New York, 1986, page 547.
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  u = rng.random ( )
  v = rng.random ( )

  x = int ( 1.0 + np.log ( v ) / ( np.log ( 1.0 - ( 1.0 - a ) ** u ) ) )

  return x

def log_series_sample_test ( rng ):

#*****************************************************************************80
#
## log_series_sample_test() tests log_series_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'log_series_sample_test():' )
  print ( '  log_series_mean() computes the Log Series mean' )
  print ( '  log_series_variance() computes the Log Series variance' )
  print ( '  log_series_sample() samples the Log Series distribution.' )

  a = 0.25

  check = log_series_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'log_series_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = log_series_mean ( a )
  variance = log_series_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = log_series_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def log_series_variance ( a ):

#*****************************************************************************80
#
## log_series_variance() returns the variance of the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  alpha = - 1.0 / np.log ( 1.0 - a )

  variance = a * alpha * ( 1.0 - alpha * a ) / ( 1.0 - a ) ** 2

  return variance

def log_uniform_cdf ( x, a, b ):

#*****************************************************************************80
#
## log_uniform_cdf() evaluates the Log Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= a ):
    cdf = 0.0
  elif ( x < b ):
    cdf = ( np.log ( x ) - np.log ( a ) ) / ( np.log ( b ) - np.log ( a ) )
  else:
    cdf = 1.0

  return cdf

def log_uniform_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## log_uniform_cdf_inv() inverts the Log Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'log_uniform_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'log_uniform_cdf_inv(): Fatal error!' )

  x = a * np.exp ( ( np.log ( b ) - np.log ( a ) ) * cdf )

  return x

def log_uniform_cdf_test ( rng ):

#*****************************************************************************80
#
## log_uniform_cdf_test() tests log_uniform_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'log_uniform_cdf_test():' )
  print ( '  log_uniform_cdf() evaluates the Log Uniform CDF' )
  print ( '  log_uniform_cdf_inv() inverts the Log Uniform CDF.' )
  print ( '  log_uniform_pdf() evaluates the Log Uniform PDF' )

  a = 2.0
  b = 20.0

  check = log_uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'log_uniform_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = log_uniform_sample ( a, b, rng )

    pdf = log_uniform_pdf ( x, a, b )

    cdf = log_uniform_cdf ( x, a, b )

    x2 = log_uniform_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def log_uniform_check ( a, b ):

#*****************************************************************************80
#
## log_uniform_check() checks the parameters of the Log Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 1.0 ):
    print ( '' )
    print ( 'log_uniform_check(): Fatal error!' )
    print ( '  A <= 1.' )
    check = False

  if ( b <= a ):
    print ( '' )
    print ( 'log_uniform_check(): Fatal error!' )
    print ( '  B <= A.' )
    check = False

  return check

def log_uniform_mean ( a, b ):

#*****************************************************************************80
#
## log_uniform_mean() returns the mean of the Log Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = ( b - a ) / ( np.log ( b ) - np.log ( a ) )

  return mean

def log_uniform_pdf ( x, a, b ):

#*****************************************************************************80
#
## log_uniform_pdf() evaluates the Log Uniform PDF.
#
#  Discussion:
#
#    PDF(A,BX) = 1 / ( X * ( log ( B ) - log ( A ) ) ) for A <= X <= B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a ):
    pdf = 0.0
  elif ( x <= b ):
    pdf = 1.0 / ( x * ( np.log ( b ) - np.log ( a ) ) )
  else:
    pdf = 0.0

  return pdf

def log_uniform_sample ( a, b, rng ):

#*****************************************************************************80
#
## log_uniform_sample() samples the Log Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = log_uniform_cdf_inv ( cdf, a, b )

  return x

def log_uniform_sample_test ( rng ):

#*****************************************************************************80
#
## log_uniform_sample_test() tests log_uniform_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'log_uniform_sample_test():' )
  print ( '  log_uniform_mean() computes the Log Uniform mean' )
  print ( '  log_uniform_sample() samples the Log Uniform distribution' )
  print ( '  log_uniform_variance() computes the Log Uniform variance' )

  a = 2.0
  b = 20.0

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )

  check = log_uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'log_uniform_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = log_uniform_mean ( a, b )
  variance = log_uniform_variance ( a, b )

  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = log_uniform_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def log_uniform_variance ( a, b ):

#*****************************************************************************80
#
## log_uniform_variance() returns the variance of the Log Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  mean = log_uniform_mean ( a, b )

  variance = \
    ( ( 0.5 * b * b - 2.0 * mean * b + mean * mean * np.log ( b ) ) \
    - ( 0.5 * a * a - 2.0 * mean * a + mean * mean * np.log ( a ) ) ) \
    / ( np.log ( b ) - np.log ( a ) )

  return variance

def lorentz_cdf ( x ):

#*****************************************************************************80
#
## lorentz_cdf() evaluates the Lorentz CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 0.5 + np.arctan ( x ) / np.pi

  return cdf

def lorentz_cdf_inv ( cdf ):

#*****************************************************************************80
#
## lorentz_cdf_inv() inverts the Lorentz CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'lorentz_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'lorentz_cdf_inv(): Fatal error!' )

  x = np.tan ( np.pi * ( cdf - 0.5 ) )

  return x

def lorentz_cdf_test ( rng ):

#*****************************************************************************80
#
## lorentz_cdf_test() tests lorentz_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lorentz_cdf_test():' )
  print ( '  lorentz_cdf() evaluates the Lorentz CDF' )
  print ( '  lorentz_cdf_inv() inverts the Lorentz CDF.' )
  print ( '  lorentz_pdf() evaluates the Lorentz PDF' )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = lorentz_sample ( rng )

    pdf = lorentz_pdf ( x )

    cdf = lorentz_cdf ( x )

    x2 = lorentz_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def lorentz_mean ( ):

#*****************************************************************************80
#
## lorentz_mean() returns the mean of the Lorentz PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def lorentz_pdf ( x ):

#*****************************************************************************80
#
## lorentz_pdf() evaluates the Lorentz PDF.
#
#  Discussion:
#
#    PDF(X) = 1 / ( PI * ( 1 + X^2 ) )
#
#    The chief interest of the Lorentz PDF is that it is easily
#    inverted, and can be used to dominate other PDF's in an
#    acceptance/rejection method.
#
#    lorentz_pdf(X) = cauchy_pdf(X)(0,1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = 1.0 / ( np.pi * ( 1.0 + x * x ) )

  return pdf

def lorentz_sample ( rng ):

#*****************************************************************************80
#
## lorentz_sample() samples the Lorentz PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = lorentz_cdf_inv ( cdf )

  return x

def lorentz_sample_test ( rng ):

#*****************************************************************************80
#
## lorentz_sample_test() tests lorentz_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'lorentz_sample_test():' )
  print ( '  lorentz_mean() computes the Lorentz mean' )
  print ( '  lorentz_variance() computes the Lorentz variance' )
  print ( '  lorentz_sample() samples the Lorentz distribution.' )

  mean = lorentz_mean ( )
  variance = lorentz_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = lorentz_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def lorentz_variance ( ):

#*****************************************************************************80
#
## lorentz_variance() returns the variance of the Lorentz PDF.
#
#  Discussion:
#
#    The variance of the Lorentz PDF is not well defined.  This routine
#    is made available for completeness only, and simply returns
#    a "very large" number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the mean of the PDF.
#
  import numpy as np

  variance = np.finfo(float).max

  return variance

def maxwell_cdf ( x, a ):

#*****************************************************************************80
#
## maxwell_cdf() evaluates the Maxwell CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    x2 = x / a
    p2 = 1.5

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def maxwell_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## maxwell_cdf_inv() inverts the Maxwell CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  it_max = 100
  tol = 0.0001
  huge = np.finfo(float).max

  if ( cdf <= 0.0 ):
    x = 0.0
    return x
  elif ( 1.0 <= cdf ):
    x = huge
    return x

  x1 = 0.0
  cdf1 = 0.0

  x2 = 1.0

  while ( True ):

    cdf2 = maxwell_cdf ( x2, a )

    if ( cdf < cdf2 ):
      break

    x2 = 2.0 * x2

    if ( 1000000.0 < x2 ):
      print ( '' )
      print ( 'maxwell_cdf_inv(): Fatal error!' )
      print ( '  Initial bracketing effort fails.' )
      raise Exception ( 'maxwell_cdf_inv(): Fatal error!' )
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = maxwell_cdf ( x3, a )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'maxwell_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'maxwell_cdf_inv(): Fatal error!' )

    if ( ( cdf3 <= cdf and cdf1 < cdf ) or ( cdf <= cdf3 and cdf <= cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def maxwell_cdf_test ( rng ):

#*****************************************************************************80
#
## maxwell_cdf_test() tests maxwell_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'maxwell_cdf_test():' )
  print ( '  maxwell_cdf() evaluates the Maxwell CDF.' )
  print ( '  maxwell_cdf_inv() inverts the Maxwell CDF.' )
  print ( '  maxwell_pdf() evaluates the Maxwell PDF.' )

  a = 2.0

  if ( not maxwell_check ( a ) ):
    print ( '' )
    print ( 'maxwell_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = maxwell_sample ( a, rng )

    pdf = maxwell_pdf ( x, a )

    cdf = maxwell_cdf ( x, a )

    x2 = maxwell_cdf_inv ( cdf, a )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def maxwell_check ( a ):

#*****************************************************************************80
#
## maxwell_check() checks the parameters of the Maxwell CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'maxwell_check(): Fatal error!' )
    print ( '  A <= 0.0.' )
    check = False

  return check

def maxwell_mean ( a ):

#*****************************************************************************80
#
## maxwell_mean() returns the mean of the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real MEAN, the mean value.
#
  import numpy as np
  from scipy.special import gamma

  mean = np.sqrt ( 2.0 ) * a * gamma ( 2.0 ) / gamma ( 1.5 )

  return mean

def maxwell_pdf ( x, a ):

#*****************************************************************************80
#
## maxwell_pdf() evaluates the Maxwell PDF.
#
#  Discussion:
#
#    PDF(X)(A) = EXP ( - 0.5 * ( X / A )^2 ) * ( X / A )^2 /
#      ( SQRT ( 2 ) * A * GAMMA ( 1.5 ) )
#
#    maxwell_pdf(X)(A) = chi_pdf(0,A,3)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0 < X
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x <= 0.0 ):

    pdf = 0.0

  else:

    y = x / a

    pdf = np.exp ( -0.5 * y * y ) * y * y \
      / ( np.sqrt ( 2.0 ) * a * gamma ( 1.5 ) )

  return pdf

def maxwell_sample ( a, rng ):

#*****************************************************************************80
#
## maxwell_sample() samples the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  a2 = 3.0
  x = chi_square_sample ( a2, rng )

  x = a * np.sqrt ( x )

  return x

def maxwell_sample_test ( rng ):

#*****************************************************************************80
#
## maxwell_sample_test() tests maxwell_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'maxwell_sample_test():' )
  print ( '  maxwell_mean() computes the Maxwell mean' )
  print ( '  maxwell_variance() computes the Maxwell variance' )
  print ( '  maxwell_sample() samples the Maxwell distribution.' )

  a = 2.0

  if ( not maxwell_check ( a ) ):
    print ( '' )
    print ( 'maxwell_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = maxwell_mean ( a )
  variance = maxwell_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF mean =                    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = maxwell_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def maxwell_variance ( a ):

#*****************************************************************************80
#
## maxwell_variance() returns the variance of the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  from scipy.special import gamma

  variance = a * a * ( 3.0 - 2.0 * ( gamma ( 2.0 ) / gamma ( 1.5 ) ) ** 2 )

  return variance

def multinomial_coef_test ( ):

#*****************************************************************************80
#
## multinomial_coef_test() tests multinomial_coef1(), multinomial_coef2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'multinomial_coef_test():' )
  print ( '  multinomial_coef1 computes multinomial coefficients using the Gamma function' )
  print ( '  multinomial_coef2 computes multinomial coefficients directly.' )

  print ( '' )
  print ( '  Line 10 of the BINOMIAL table:' )
  print ( '' )

  n = 10
  nfactor = 2
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i
    factor[1] = n - i

    ncomb1 = multinomial_coef1 ( nfactor, factor )

    ncomb2 = multinomial_coef2 ( nfactor, factor )

    print ( '  %4d  %4d  %5d  %5d' % ( factor[0], factor[1], ncomb1, ncomb2 ) )

  print ( '' )
  print ( '  Level 5 of the TRINOMIAL coefficients:' )

  n = 5
  nfactor = 3
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i

    print ( '' )

    for j in range ( 0, n - factor[0] + 1 ):

      factor[1] = j
      factor[2] = n - factor[0] - factor[1]

      ncomb1 = multinomial_coef1 ( nfactor, factor )

      ncomb2 = multinomial_coef2 ( nfactor, factor )

      print ( '  %4d  %4d  %4d  %5d  %5d' \
        % ( factor[0], factor[1], factor[2], ncomb1, ncomb2 ) )

  return

def multinomial_coef1 ( nfactor, factor ):

#*****************************************************************************80
#
## multinomial_coef1() computes a Multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    The log of the gamma function is used, to avoid overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NFACTOR, the number of factors.
#    1 <= NFACTOR.
#
#    integer FACTOR(NFACTOR), contains the factors.
#    0.0 <= FACTOR(I).
#
#  Output:
#
#    integer NCOMB, the value of the multinomial coefficient.
#
  import numpy as np
  from scipy.special import gammaln
#
#  The factors sum to N.
#
  n = np.sum ( factor )

  facn = gammaln ( float ( n + 1 ) )

  for i in range ( 0, nfactor ):

    facn = facn - gammaln ( float ( factor[i] + 1 ) )

  ncomb = int ( round ( np.exp ( facn ) ) )

  return ncomb

def multinomial_coef2 ( nfactor, factor ):

#*****************************************************************************80
#
## multinomial_coef2() computes a Multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    A direct method is used, which should be exact.  However, there
#    is a possibility of intermediate overflow of the result.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NFACTOR, the number of factors.
#    1 <= NFACTOR.
#
#    integer FACTOR(NFACTOR), contains the factors.
#    0.0 <= FACTOR(I).
#
#  Output:
#
#    integer NCOMB, the value of the multinomial coefficient.
#
  ncomb = 1
  k = 0

  for i in range ( 0, nfactor ):

    for j in range ( 1, factor[i] + 1 ):
      k = k + 1
      ncomb = ( ncomb * k ) / j

  return ncomb

def multinomial_check ( a, b, c ):

#*****************************************************************************80
#
## multinomial_check() checks the parameters of the Multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#
#    integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B ) C(I) = 1.0.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  import numpy as np

  check = True

  if ( b < 1 ):
    print ( '' )
    print ( 'multinomial_check(): Fatal error!' )
    print ( '  B < 1.' )
    check = False

  for i in range ( 0, b ):

    if ( c[i] < 0.0 or 1.0 < c[i] ):
      print ( '' )
      print ( 'multinomial_check(): Fatal error!' )
      print ( '  Input C(I) is out of range.' )
      check = False

  c_sum = np.sum ( c )

  if ( 0.0001 < abs ( 1.0 - c_sum ) ):
    print ( '' )
    print ( 'multinomial_check(): Fatal error!' )
    print ( '  The probabilities do not sum to 1.' )
    check = False

  return check

def multinomial_covariance ( a, b, c ):

#*****************************************************************************80
#
## multinomial_covariance() returns the covariances of the Multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#
#    integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B) C(I) = 1.0.
#
#  Output:
#
#    real COVARIANCE(B,B), the covariance matrix.
#
  import numpy as np

  covariance = np.zeros ( [ b, b ] )

  for i in range ( 0, b ):
    for j in range ( 0, b ):

      if ( i == j ):
        covariance[i,j] = a * c[i] * ( 1.0 - c[i] )
      else:
        covariance[i,j] = - a * c[i] * c[j]

  return covariance

def multinomial_mean ( a, b, c ):

#*****************************************************************************80
#
## multinomial_mean() returns the means of the Multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#
#    integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B) C(I) = 1.0.
#
#  Output:
#
#    real MEAN(B), MEAN(I) is the expected value of the
#    number of outcome I in N trials.
#
  import numpy as np

  mean = np.zeros ( b )

  for i in range ( 0, b ):
    mean[i] = a * c[i]

  return mean

def multinomial_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## multinomial_pdf() computes a Multinomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = Comb(A,B,X) * Product ( 1 <= I <= B ) C(I)^X(I)
#
#    where Comb(A,B,X) is the multinomial coefficient
#      C( A X(1), X(2), ..., X(B) )
#
#    PDF(X)(A,B,C) is the probability that in A trials there
#    will be exactly X(I) occurrences of event I, whose probability
#    on one trial is C(I), for I from 1 to B.
#
#    As soon as A or B gets large, the number of possible X's explodes,
#    and the probability of any particular X can become extremely small.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X(B) X(I) counts the number of occurrences of
#    outcome I, out of the total of A trials.
#
#    integer A, the total number of trials.
#
#    integer B, the number of different possible outcomes on
#    one trial.
#
#    real C(B) C(I) is the probability of outcome I on
#    any one trial.
#
#  Output:
#
#    real PDF, the value of the multinomial PDF.
#
  import numpy as np
  from scipy.special import gammaln
#
#  To try to avoid overflow, do the calculation in terms of logarithms.
#  Note that Gamma(A+1) = A factorial.
#
  pdf_log = gammaln ( float ( a + 1 ) )

  for i in range ( 0, b ):
    pdf_log = pdf_log + x[i] * np.log ( c[i] ) - gammaln ( float ( x[i] + 1 ) )

  pdf = np.exp ( pdf_log )

  return pdf

def multinomial_pdf_test ( ):

#*****************************************************************************80
#
## multinomial_pdf_test() tests multinomial_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  b = 3

  print ( '' )
  print ( 'multinomial_pdf_test():' )
  print ( '  multinomial_pdf() evaluates the Multinomial PDF.' )

  x = np.array ( [ 0, 2, 3 ] )

  a = 5

  c = np.array ( [ 0.10, 0.50, 0.40 ] )

  check = multinomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'multinomial_pdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  i4vec_print ( b, x, '  PDF argument X:' )

  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  r8vec_print ( b, c, '  PDF parameter C:' )

  pdf = multinomial_pdf ( x, a, b, c )

  print ( '' )
  print ( '  PDF value =     %14g' % ( pdf ) )

  return

def multinomial_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## multinomial_sample() samples the Multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer-Verlag, New York, 1986, page 559.
#
#  Input:
#
#    integer A, the total number of trials.
#    0 <= A.
#
#    integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B) C(I) = 1.0.
#
#  Output:
#
#    integer X(B), X(I) is the number of
#    occurrences of event I during the N trials.
#
  import numpy as np

  ntot = a

  sum2 = 1.0

  x = np.zeros ( b, dtype = np.int32 )

  for ifactor in range ( 0, b - 1 ):

    prob = c[ifactor] / sum2
#
#  Generate a binomial random deviate for NTOT trials with
#  single trial success probability PROB.
#
    s = binomial_sample ( ntot, prob, rng )

    x[ifactor] = s

    ntot = ntot - x[ifactor]
    if ( ntot <= 0 ):
      return x

    sum2 = sum2 - c[ifactor]
#
#  The last factor gets what's left.
#
  x[b-1] = ntot

  return x

def multinomial_sample_test ( rng ):

#*****************************************************************************80
#
## multinomial_sample_test() tests multinomial_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  b = 3
  nsample = 1000

  print ( '' )
  print ( 'multinomial_sample_test():' )
  print ( '  multinomial_mean() computes the Multinomial mean' )
  print ( '  multinomial_sample() samples the Multinomial distribution' )
  print ( '  multinomial_variance() computes the Multinomial variance' )

  a = 5

  c = np.array ( [ 0.125, 0.500, 0.375 ] )

  check = multinomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'multinomial_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = multinomial_mean ( a, b, c )
  variance = multinomial_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %6d' % ( b ) )

  r8vec_print ( b, c, '  PDF parameter C:' )

  print ( '' )
  print ( '  PDF means and variances:' )
  print ( '' )
  for i in range ( 0, b ):
    print ( '  %14g  %14g' % ( mean[i], variance[i] ) )
   
  x = np.zeros ( [ b, nsample ] )
  for j in range ( 0, nsample ):
    v = multinomial_sample ( a, b, c, rng )
    for i in range ( 0, b ):
      x[i,j] = v[i]

  xmax = i4row_max ( b, nsample, x )
  xmin = i4row_min ( b, nsample, x )
  mean = i4row_mean ( b, nsample, x )
  variance = i4row_variance ( b, nsample, x )

  print ( '' )
  print ( '  Sample size = %6d' % ( nsample ) )
  print ( '  Component Min, Max, Mean, Variance:' )
  for i in range ( 0, b ):
    print ( '  %6d  %6d  %6d  %14g  %14g' \
      % ( i, xmin[i], xmax[i], mean[i], variance[i] ) )

  return

def multinomial_variance ( a, b, c ):

#*****************************************************************************80
#
## multinomial_variance() returns the variances of the Multinomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the number of trials.
#
#    integer B, the number of outcomes possible on one trial.
#    1 <= B.
#
#    real C(B).  C(I) is the probability of outcome I on
#    any trial.
#    0.0 <= C(I) <= 1.0,
#    Sum ( 1 <= I <= B ) C(I) = 1.0.
#
#  Output:
#
#    real VARIANCE(B), VARIANCE(I) is the variance of the
#    total number of events of type I.
#
  import numpy as np

  variance = np.zeros ( b )
  for i in range ( 0, b ):
    variance[i] = a * c[i] * ( 1.0 - c[i] )

  return variance

def multinoulli_pdf ( x, n, theta ):

#*****************************************************************************80
#
## multinoulli_pdf() evaluates the Multinoulli PDF.
#
#  Discussion:
#
#    PDF(X) = THETA(X) for 0 <= X < N.
#           = 0 otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the index of the outcome.
#    0 <= X < N.
#
#    integer N, the number of legal outcomes.
#
#    real THETA[N], the probability of each outcome.
#
#  Output:
#
#    real VALUE, the probability of outcome X.
#
  if ( 0 <= x and x < n ):
    value = theta[x]
  else:
    value = 0.0

  return value

def multinoulli_pdf_test ( rng ):

#*****************************************************************************80
#
## multinoulli_pdf_test() tests multinoulli_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'multinoulli_pdf_test():' )
  print ( '  multinoulli_pdf() evaluates the Multinoulli PDF.' )

  n = 5
  theta = rng.random ( size = n )
  theta_sum = np.sum ( theta )
  theta[0:n] = theta[0:n] / theta_sum

  print ( '' )
  print ( '   X     pdf(X)' )
  print ( '' )
  for x in range ( -1, n + 1 ):
    pdf = multinoulli_pdf ( x, n, theta )
    print ( '  %2d  %14g' % ( x, pdf ) )

  return

def nakagami_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## nakagami_cdf() evaluates the Nakagami CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= 0.0 ):

    cdf = 0.0

  elif ( 0.0 < x ):

    y = ( x - a ) / b
    x2 = c * y * y
    p2 = c

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def nakagami_cdf_test ( rng ):

#*****************************************************************************80
#
## nakagami_cdf_test() tests nakagami_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'nakagami_cdf_test():' )
  print ( '  nakagami_cdf() evaluates the Nakagami CDF' )
  print ( '  nakagami_pdf() evaluates the Nakagami PDF' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = nakagami_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'nakagami_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 1, 11 ):

    x = a + b + np.sqrt ( float ( i ) / c / 10.0 )

    pdf = nakagami_pdf ( x, a, b, c )

    cdf = nakagami_cdf ( x, a, b, c )

    x2 = nakagami_cdf_inv ( cdf, a, b, c )

    print ( '  %14.6g%14.6g%14.6g%14.6g' % ( x, pdf, cdf, x2 ) )

  return

def nakagami_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## nakagami_cdf_inv() inverts the Nakagami CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  huge = np.finfo(float).max
  it_max = 100
  tol = 0.000001

  if ( cdf <= 0.0 ):
    x = c * a * a
    return x
  elif ( 1.0 <= cdf ):
    x = huge
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
      print ( 'nakagami_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'nakagami_cdf_inv(): Fatal error!' )

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
## nakagami_check() checks the parameters of the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'nakagami_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'nakagami_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def nakagami_mean ( a, b, c ):

#*****************************************************************************80
#
## nakagami_mean() returns the mean of the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  mean = a + b * gamma ( c + 0.5 ) / ( np.sqrt ( c ) * gamma ( c ) )

  return mean

def nakagami_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## nakagami_pdf() evaluates the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x <= 0.0 ):

    pdf = 0.0

  elif ( 0.0 < x ):

    y = ( x - a ) / b

    pdf = 2.0 * c ** c / ( b * gamma ( c ) ) * y ** ( 2.0 * c - 1.0 ) \
    * np.exp ( -c * y * y )

  return pdf

def nakagami_sample_test ( rng ):

#*****************************************************************************80
#
## nakagami_sample_test() tests nakagami_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'nakagami_sample_test():' )
  print ( '  nakagami_mean() computes the Nakagami mean' )
  print ( '  nakagami_variance() computes the Nakagami variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = nakagami_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'nakagami_sample_test(): Fatal error!' )
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

  return

def nakagami_variance ( a, b, c ):

#*****************************************************************************80
#
## nakagami_variance() returns the variance of the Nakagami PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B
#    0.0 < C
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  from scipy.special import gamma

  t1 = gamma ( c + 0.5 )
  t2 = gamma ( c )

  variance = b * b * ( 1.0 - t1 * t1 / ( c * t2 * t2 ) )

  return variance

def negative_binomial_cdf ( x, a, b ):

#*****************************************************************************80
#
## negative_binomial_cdf() evaluates the Negative Binomial CDF.
#
#  Discussion:
#
#    A simple summing approach is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the CDF.
#
#    integer A, a parameter of the PDF.
#    0 <= A.
#
#    real B, a parameter of the PDF.
#    0 < B <= 1.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  from scipy.special import comb

  cdf = 0.0

  for y in range ( a, x + 1 ):

    cnk = comb ( y - 1, a - 1 )

    pdf = cnk * b ** a * ( 1.0 - b ) ** ( y - a )

    cdf = cdf + pdf

  return cdf

def negative_binomial_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## negative_binomial_cdf_inv() inverts the Negative Binomial CDF.
#
#  Discussion:
#
#    A simple discrete approach is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    integer A, real B, parameters of the PDF.
#    0 <= A,
#    0 < B <= 1.
#
#  Output:
#
#    integer X, the smallest X whose cumulative density function
#    is greater than or equal to CDF.
#
  x_max = 1000

  if ( cdf <= 0.0 ):

    x = a

  else:

    cum = 0.0

    x = a

    while ( True ):

      pdf = negative_binomial_pdf ( x, a, b )

      cum = cum + pdf

      if ( cdf <= cum or x_max <= x ):
        break

      x = x + 1

  return x

def negative_binomial_cdf_test ( rng ):

#*****************************************************************************80
#
## negative_binomial_cdf_test() tests negative_binomial_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'negative_binomial_cdf_test():' )
  print ( '  negative_binomial_cdf() evaluates the Negative Binomial CDF.' )
  print ( '  negative_binomial_cdf_inv() inverts the Negative Binomial CDF.' )
  print ( '  negative_binomial_pdf() evaluates the Negative Binomial PDF.' )

  a = 2
  b = 0.25

  if ( not negative_binomial_check ( a, b ) ):
    print ( '' )
    print ( 'negative_binomial_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = negative_binomial_sample ( a, b, rng )

    pdf = negative_binomial_pdf ( x, a, b )

    cdf = negative_binomial_cdf ( x, a, b )

    x2 = negative_binomial_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def negative_binomial_check ( a, b ):

#*****************************************************************************80
#
## negative_binomial_check() checks the parameters of the Negative Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, a parameter of the PDF.
#    0 <= A.
#
#    real B, a parameter of the PDF.
#    0 < B <= 1.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0 ):
    print ( '' )
    print ( 'negative_binomial_check(): Fatal error!' )
    print ( '  A < 0.' )
    check = False

  if ( b <= 0.0 or 1.0 < b ):
    print ( '' )
    print ( 'negative_binomial_check(): Fatal error!' )
    print ( '  B <= 0 or 1 < B.' )
    check = False

  return check

def negative_binomial_mean ( a, b ):

#*****************************************************************************80
#
## negative_binomial_mean() returns the mean of the Negative Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, a parameter of the PDF.
#    0 <= A.
#
#    real B, a parameter of the PDF.
#    0 < B <= 1.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a / b

  return mean

def negative_binomial_pdf ( x, a, b ):

#*****************************************************************************80
#
## negative_binomial_pdf() evaluates the Negative Binomial PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = C(X-1,A-1) * B^A * ( 1 - B )^(X-A)
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability that the A-th success will
#    occur on the X-th trial, given that the probability
#    of a success on a single trial is B.
#
#    The Negative Binomial PDF is also known as the Pascal PDF or
#    the "Polya" PDF.
#
#    negative_binomial_pdf(X)(1,B) = geometric_pdf(X)(B)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the number of trials.
#    A <= X.
#
#    integer A, the number of successes required.
#    0 <= A <= X, normally.
#
#    real B, the probability of a success on a single trial.
#    0.0 < B <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  from scipy.special import comb

  if ( x < a ):

    pdf = 0.0

  else:

    cnk = comb ( x - 1, a - 1 )

    pdf = cnk * b ** a * ( 1.0 - b ) ** ( x - a )

  return pdf

def negative_binomial_sample ( a, b, rng ):

#*****************************************************************************80
#
## negative_binomial_sample() samples the Negative Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, a parameter of the PDF.
#    0 <= A.
#
#    real B, a parameter of the PDF.
#    0 < B <= 1.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  huge = np.finfo(float).max

  if ( b == 1.0 ):
    x = a
    return x
  elif ( b == 0.0 ):
    x = huge
    return x

  x = 0
  num_success = 0

  while ( num_success < a ):

    x = x + 1
    r = rng.random ( )

    if ( r <= b ):
      num_success = num_success + 1

  return x

def negative_binomial_sample_test ( rng ):

#*****************************************************************************80
#
## negative_binomial_sample_test() tests negative_binomial_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'negative_binomial_sample_test():' )
  print ( '  negative_binomial_mean() computes the Negative Binomial mean' )
  print ( '  negative_binomial_sample() samples the Negative Binomial distribution' )
  print ( '  negative_binomial_variance() computes the Negative Binomial variance.' )

  a = 2
  b = 0.75

  if ( not negative_binomial_check ( a, b ) ):
    print ( '' )
    print ( 'negative_binomial_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = negative_binomial_mean ( a, b )
  variance = negative_binomial_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = negative_binomial_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def negative_binomial_variance ( a, b ):

#*****************************************************************************80
#
## negative_binomial_variance() returns the variance of the Negative Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, a parameter of the PDF.
#    0 <= A.
#
#    real B, a parameter of the PDF.
#    0 < B <= 1.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a * ( 1.0 - b ) / ( b * b )

  return variance

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## normal_01_cdf_values() returns some values of the Normal 01 CDF.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real X, the argument of the function.
#
#    real F, the value of the function.
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
## normal_01_cdf_values_test() tests normal_01_cdf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'normal_01_cdf_values_test():' )
  print ( '  normal_01_cdf_values() stores values of the unit normal CDF.' )
  print ( '' )
  print ( '      X         normal_01_cdf(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def normal_01_cdf ( x ):

#*****************************************************************************80
#
## normal_01_cdf() evaluates the Normal 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
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

def normal_01_cdf_test ( rng ):

#*****************************************************************************80
#
## normal_01_cdf_test() tests normal_01_cdf(), normal_01_cdf_inv(), normal_01_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'normal_01_cdf_test():' )
  print ( '  normal_01_cdf() evaluates the Normal 01 CDF' )
  print ( '  normal_01_cdf_inv() inverts the Normal 01 CDF.' )
  print ( '  normal_01_pdf() evaluates the Normal 01 PDF' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = normal_01_sample ( rng )

    pdf = normal_01_pdf ( x )

    cdf = normal_01_cdf ( x )

    x2 = normal_01_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def normal_01_cdf_inv ( p ):

#*****************************************************************************80
#
## normal_01_cdf_inv() inverts the standard normal CDF.
#
#  Discussion:
#
#    The result is accurate to about 1 part in 10^16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by Michael Wichura.
#    This version by John Burkardt.
#
#  Reference:
#
#    Michael Wichura,
#    The Percentage Points of the Normal Distribution,
#    Algorithm AS 241,
#    Applied Statistics,
#    Volume 37, Number 3, pages 477-484, 1988.
#
#  Input:
#
#    real P, the value of the cumulative probability 
#    densitity function.  0 < P < 1.  If P is not in this range, an "infinite"
#    result is returned.
#
#  Output:
#
#    real VALUE, the normal deviate value with the 
#    property that the probability of a standard normal deviate being 
#    less than or equal to the value is P.
#
  import numpy as np

  huge = np.finfo(float).max

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
    value = - huge
    return value

  if ( 1.0 <= p ):
    value = huge
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

      value = huge

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
## normal_01_mean() returns the mean of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def normal_01_pdf ( x ):

#*****************************************************************************80
#
## normal_01_pdf() evaluates the Normal 01 PDF.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return pdf

def normal_01_sample ( rng ):

#*****************************************************************************80
#
## normal_01_sample() samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    X, a sample of the standard normal PDF.
#
  import numpy as np

  x = rng.standard_normal ( )
 
  return x

def normal_01_sample_test ( rng ):

#*****************************************************************************80
#
## normal_01_sample_test() tests normal_01_mean(), normal_01_sample(), normal_01_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'normal_01_sample_test():' )
  print ( '  normal_01_mean() computes the Normal 01 mean' )
  print ( '  normal_01_sample() samples the Normal 01 distribution' )
  print ( '  normal_01_variance() returns the Normal 01 variance.' )

  mean = normal_01_mean ( )
  variance = normal_01_variance ( )

  print ( '' )
  print ( '  PDF mean =      %14g' % ( mean ) )
  print ( '  PDF variance =  %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = normal_01_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def normal_01_samples ( n ):

#*****************************************************************************80
#
## normal_01_samples(): multiple samples of the standard normal PDF.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of samples.
#
#  Output:
#
#    X[N], a sample of the standard normal PDF.
#
  import numpy as np

  x = rng.standard_normal ( size = n )

  return x

def normal_01_samples_test ( ):

#*****************************************************************************80
#
## normal_01_samples_test() tests normal_01_mean(), normal_01_samples(), normal_01_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  nsample = 1000

  print ( '' )
  print ( 'normal_01_samples_test():' )
  print ( '  normal_01_mean() computes the Normal 01 mean' )
  print ( '  normal_01_samplea() samples the Normal 01 distribution' )
  print ( '  normal_01_variance() returns the Normal 01 variance.' )

  mean = normal_01_mean ( )
  variance = normal_01_variance ( )

  print ( '' )
  print ( '  PDF mean =      %14g' % ( mean ) )
  print ( '  PDF variance =  %14g' % ( variance ) )

  x = normal_01_samples ( nsample )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def normal_01_variance ( ):

#*****************************************************************************80
#
## normal_01_variance() returns the variance of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 1.0

  return variance

def normal_cdf ( x, mu, sigma ):

#*****************************************************************************80
#
## normal_cdf() evaluates the Normal CDF.
#
#  Discussion:
#
#    The Normal CDF is related to the Error Function ERF(X) by:
#
#      ERF ( X ) = 2 * normal_cdf ( SQRT ( 2 ) * X ) - 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  y = ( x - mu ) / sigma

  cdf = normal_01_cdf ( y )

  return cdf

def normal_cdf_inv ( cdf, mu, sigma ):

#*****************************************************************************80
#
## normal_cdf_inv() inverts the Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'normal_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'normal_cdf_inv(): Fatal error!' )

  x2 = normal_01_cdf_inv ( cdf )

  x = mu + sigma * x2

  return x

def normal_cdf_test ( rng ):

#*****************************************************************************80
#
## normal_cdf_test() tests normal_cdf(), normal_cdf_inv(), normal_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'normal_cdf_test():' )
  print ( '  normal_cdf() evaluates the Normal CDF' )
  print ( '  normal_cdf_inv() inverts the Normal CDF.' )
  print ( '  normal_pdf() evaluates the Normal PDF' )

  mu = 100.0
  sigma = 15.0

  check = normal_check ( mu, sigma )

  if ( not check ):
    print ( '' )
    print ( 'normal_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter MU =    %14g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %14g' % ( sigma ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = normal_sample ( mu, sigma, rng )

    pdf = normal_pdf ( x, mu, sigma )

    cdf = normal_cdf ( x, mu, sigma )

    x2 = normal_cdf_inv ( cdf, mu, sigma )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def normal_check ( mu, sigma ):

#*****************************************************************************80
#
## normal_check() checks the parameters of the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( sigma == 0.0 ):
    print ( '' )
    print ( 'normal_check(): Fatal error!' )
    print ( '  SIGMA == 0.' )
    check = False

  return check

def normal_mean ( mu, sigma ):

#*****************************************************************************80
#
## normal_mean() returns the mean of the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  return mu

def normal_pdf ( x, mu, sigma ):

#*****************************************************************************80
#
## normal_pdf() evaluates the Normal PDF.
#
#  Discussion:
#
#    The normal PDF is also known as the Gaussian PDF.
#
#  Formula:
#
#    PDF(X;MU,SIGMA) = 
#      EXP ( - 0.5 * ( ( X - MU ) / SIGMA )^2 ) / SQRT ( 2 * PI * SIGMA^2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(), the argument of the PDF.
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real PDF(), the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - 0.5 * ( ( x - mu ) / sigma ) ** 2 ) \
    / np.sqrt ( 2.0 * np.pi * sigma ** 2 )

  return pdf

def normal_sample ( mu, sigma, rng ):

#*****************************************************************************80
#
## normal_sample() samples the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  y = rng.standard_normal ( )

  x = mu + sigma * y

  return x

def normal_sample_test ( rng ):

#*****************************************************************************80
#
## normal_sample_test() tests normal_mean(), normal_sample(), normal_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'normal_sample_test():' )
  print ( '  normal_mean() computes the Normal mean' )
  print ( '  normal_sample samples() the Normal distribution' )
  print ( '  normal_variance() returns the Normal variance.' )

  mu = 100.0
  sigma = 15.0

  check = normal_check ( mu, sigma )

  if ( not check ):
    print ( '' )
    print ( 'normal_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
 
  mean = normal_mean ( mu, sigma )
  variance = normal_variance ( mu, sigma )

  print ( '' )
  print ( '  PDF parameter MU =    %14g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %14g' % ( sigma ) )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = normal_sample ( mu, sigma, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d'  % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def normal_samples ( n, mu, sigma ):

#*****************************************************************************80
#
## normal_samples() returns multiple samples of the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of samples.
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real X[N], samples of the PDF.
#
  import numpy as np

  x = rng.standard_normal ( size = n )

  x = mu + sigma * x

  return x

def normal_samples_test ( ):

#*****************************************************************************80
#
## normal_samples_test() tests normal_mean(), normal_samples(), normal_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'normal_samples_test():' )
  print ( '  normal_mean() computes the Normal mean' )
  print ( '  normal_samples() samples the Normal distribution' )
  print ( '  normal_variance() returns the Normal variance.' )

  mu = 100.0
  sigma = 15.0

  check = normal_check ( mu, sigma )

  if ( not check ):
    print ( '' )
    print ( 'normal_samples_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
 
  mean = normal_mean ( mu, sigma )
  variance = normal_variance ( mu, sigma )

  print ( '' )
  print ( '  PDF parameter MU =    %14g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %14g' % ( sigma ) )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = normal_samples ( nsample, mu, sigma )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d'  % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def normal_variance ( mu, sigma ):

#*****************************************************************************80
#
## normal_variance() returns the variance of the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = sigma * sigma

  return variance

def normal_truncated_ab_cdf ( x, mu, s, a, b ):

#*****************************************************************************80
#
## normal_truncated_ab_cdf() evaluates the truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#  Output:
#
#    real A, B, the lower and upper truncation limits.
#
#    real CDF, the value of the CDF.
#
  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s
  xi = ( x - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )
  xi_cdf = normal_01_cdf ( xi )

  cdf = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  return cdf

def normal_truncated_ab_cdf_inv ( cdf, mu, s, a, b ):

#*****************************************************************************80
#
## normal_truncated_ab_cdf_inv() inverts the truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, B, the lower and upper truncation limits.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'normal_truncated_ab_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'normal_truncated_ab_cdf_inv(): Fatal error!' )

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_ab_cdf_test ( rng ):

#*****************************************************************************80
#
## normal_truncated_ab_cdf_test() tests normal_truncated_ab_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  a = 50.0
  b = 150.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'normal_truncated_ab_cdf_test():' )
  print ( '  normal_truncated_ab_cdf() evaluates the Normal Truncated AB CDF.' )
  print ( '  normal_truncated_ab_cdf_inv() inverts the Normal Truncated AB CDF.' )
  print ( '  normal_truncated_ab_pdf() evaluates the Normal Truncated AB PDF.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = normal_truncated_ab_sample ( mu, s, a, b, rng )

    pdf = normal_truncated_ab_pdf ( x, mu, s, a, b )

    cdf = normal_truncated_ab_cdf ( x, mu, s, a, b )

    x2 = normal_truncated_ab_cdf_inv ( cdf, mu, s, a, b )

    print ( '  %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def normal_truncated_ab_mean ( mu, s, a, b ):

#*****************************************************************************80
#
## normal_truncated_ab_mean() returns the mean of the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviatione of the
#    parent Normal distribution.
#
#    real A, B, the lower and upper truncation limits.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  mean = mu + s * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return mean

def normal_truncated_ab_pdf ( x, mu, s, a, b ):

#*****************************************************************************80
#
## normal_truncated_ab_pdf() evaluates the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, B, the lower and upper truncation limits.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s
  xi = ( x - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )
  xi_pdf = normal_01_pdf ( xi )

  pdf = xi_pdf / ( beta_cdf - alpha_cdf ) / s

  return pdf

def normal_truncated_ab_sample ( mu, s, a, b, rng ):

#*****************************************************************************80
#
## normal_truncated_ab_sample() samples the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, B, the lower and upper truncation limits.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  u = rng.random ( )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_ab_sample_test ( rng ):

#*****************************************************************************80
#
## normal_truncated_ab_sample_test() tests normal_truncated_ab_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000
  a = 50.0
  b = 150.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'normal_truncated_ab_sample_test():' )
  print ( '  normal_truncated_ab_mean() computes the Normal Truncated AB mean' )
  print ( '  normal_truncated_ab_sample() samples the Normal Truncated AB distribution' )
  print ( '  normal_truncated_ab_variance() computes the Normal Truncated AB variance.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  mean = normal_truncated_ab_mean ( mu, s, a, b )

  variance = normal_truncated_ab_variance ( mu, s, a, b )

  print ( '' )
  print ( '  PDF mean      =               %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = normal_truncated_ab_sample ( mu, s, a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %d' % ( sample_num ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )

  return

def normal_truncated_ab_variance ( mu, s, a, b ):

#*****************************************************************************80
#
## normal_truncated_ab_variance() returns the variance of the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, B, the lower and upper truncation limits.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  variance = s * s * ( 1.0 \
    + ( alpha * alpha_pdf - beta * beta_pdf ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return variance

def normal_truncated_a_cdf ( x, mu, s, a ):

#*****************************************************************************80
#
## normal_truncated_a_cdf() evaluates the lower truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  alpha = ( a - mu ) / s
  xi = ( x - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  xi_cdf = normal_01_cdf ( xi )

  cdf = ( xi_cdf - alpha_cdf ) / ( 1.0 - alpha_cdf )

  return cdf

def normal_truncated_a_cdf_inv ( cdf, mu, s, a ):

#*****************************************************************************80
#
## normal_truncated_a_cdf_inv() inverts the lower truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'normal_truncated_a_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'normal_truncated_a_cdf_inv(): Fatal error!' )

  alpha = ( a - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )

  xi_cdf = ( 1.0 - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_a_cdf_test ( rng ):

#*****************************************************************************80
#
## normal_truncated_a_cdf_test() tests normal_truncated_a_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  a = 50.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'normal_truncated_a_cdf_test():' )
  print ( '  normal_truncated_a_cdf() evaluates the Normal Truncated A CDF.' )
  print ( '  normal_truncated_a_cdf_inv() inverts the Normal Truncated A CDF.' )
  print ( '  normal_truncated_a_pdf() evaluates the Normal Truncated A PDF.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,+oo)' % ( a ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( ' ' )

  for i in range ( 0, 10 ):

    x = normal_truncated_a_sample ( mu, s, a, rng )

    pdf = normal_truncated_a_pdf ( x, mu, s, a )

    cdf = normal_truncated_a_cdf ( x, mu, s, a )

    x2 = normal_truncated_a_cdf_inv ( cdf, mu, s, a )

    print ( '  %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def normal_truncated_a_mean ( mu, s, a ):

#*****************************************************************************80
#
## normal_truncated_a_mean() returns the mean of the lower truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviatione of the
#    parent Normal distribution.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  alpha = ( a - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )

  alpha_pdf = normal_01_pdf ( alpha )

  mean = mu + s * alpha_pdf / ( 1.0 - alpha_cdf )

  return mean

def normal_truncated_a_pdf ( x, mu, s, a ):

#*****************************************************************************80
#
## normal_truncated_a_pdf() evaluates the lower truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  alpha = ( a - mu ) / s
  xi = ( x - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  xi_pdf = normal_01_pdf ( xi )

  pdf = xi_pdf / ( 1.0 - alpha_cdf ) / s

  return pdf

def normal_truncated_a_sample ( mu, s, a, rng ):

#*****************************************************************************80
#
## normal_truncated_a_sample() samples the lower truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  alpha = ( a - mu ) / s
# beta = Inf

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  u = rng.random ( )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_a_sample_test ( rng ):

#*****************************************************************************80
#
## normal_truncated_a_sample_test() tests normal_truncated_a_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000
  a = 50.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'normal_truncated_a_sample_test():' )
  print ( '  normal_truncated_a_mean() computes the Normal Truncated A mean' )
  print ( '  normal_truncated_a_sample() samples the Normal Truncated A distribution' )
  print ( '  normal_truncated_a_variance() computes the Normal Truncated A variance.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,+oo]' % ( a ) )

  mean = normal_truncated_a_mean ( mu, s, a )

  variance = normal_truncated_a_variance ( mu, s, a )

  print ( '' )
  print ( '  PDF mean      =               %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = normal_truncated_a_sample ( mu, s, a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %d' % ( sample_num ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )

  return

def normal_truncated_a_variance ( mu, s, a ):

#*****************************************************************************80
#
## normal_truncated_a_variance(): variance of the lower truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  alpha = ( a - mu ) / s
# beta = Inf

  alpha_pdf = normal_01_pdf ( alpha )

  alpha_cdf = normal_01_cdf ( alpha )

  variance = s * s * ( 1.0 \
    + ( alpha * alpha_pdf ) / ( 1.0 - alpha_cdf ) \
    - ( alpha_pdf / ( 1.0 - alpha_cdf ) ) ** 2 )

  return variance

def normal_truncated_b_cdf ( x, mu, s, b ):

#*****************************************************************************80
#
## normal_truncated_b_cdf() evaluates the upper truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  beta = ( b - mu ) / s
  xi = ( x - mu ) / s

  beta_cdf = normal_01_cdf ( beta )
  xi_cdf = normal_01_cdf ( xi )

  cdf = xi_cdf / beta_cdf

  return cdf

def normal_truncated_b_cdf_inv ( cdf, mu, s, b ):

#*****************************************************************************80
#
## normal_truncated_b_cdf_inv() inverts the upper truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'normal_truncated_b_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'normal_truncated_b_cdf_inv(): Fatal error!' )

  beta = ( b - mu ) / s

  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = beta_cdf * cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_b_cdf_test ( rng ):

#*****************************************************************************80
#
## normal_truncated_b_cdf_test() tests normal_truncated_b_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  b = 150.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'normal_truncated_b_cdf_test():' )
  print ( '  normal_truncated_b_cdf() evaluates the Normal Truncated B CDF.' )
  print ( '  normal_truncated_b_cdf_inv() inverts the Normal Truncated B CDF.' )
  print ( '  normal_truncated_b_pdf() evaluates the Normal Truncated B PDF.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [-oo,%g]' % ( b ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = normal_truncated_b_sample ( mu, s, b, rng )

    pdf = normal_truncated_b_pdf ( x, mu, s, b )

    cdf = normal_truncated_b_cdf ( x, mu, s, b )

    x2 = normal_truncated_b_cdf_inv ( cdf, mu, s, b )

    print ( '  %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def normal_truncated_b_mean ( mu, s, b ):

#*****************************************************************************80
#
## normal_truncated_b_mean() returns the mean of the upper truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviatione of the
#    parent Normal distribution.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  beta = ( b - mu ) / s

  beta_cdf = normal_01_cdf ( beta )

  beta_pdf = normal_01_pdf ( beta )

  mean = mu - s * beta_pdf / beta_cdf

  return mean

def normal_truncated_b_pdf ( x, mu, s, b ):

#*****************************************************************************80
#
## normal_truncated_b_pdf() evaluates the upper truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  beta = ( b - mu ) / s
  xi = ( x - mu ) / s

  beta_cdf = normal_01_cdf ( beta )
  xi_pdf = normal_01_pdf ( xi )

  pdf = xi_pdf / beta_cdf / s

  return pdf

def normal_truncated_b_sample ( mu, s, b, rng ):

#*****************************************************************************80
#
## normal_truncated_b_sample() samples the upper truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  beta = ( b - mu ) / s

  beta_cdf = normal_01_cdf ( beta )

  u = rng.random ( )
  xi_cdf =  u * beta_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_b_sample_test ( rng ):

#*****************************************************************************80
#
## normal_truncated_b_sample_test() tests normal_truncated_b_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000
  b = 150.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'normal_truncated_b_sample_test():' )
  print ( '  normal_truncated_b_mean() computes the Normal Truncated B mean' )
  print ( '  normal_truncated_b_sample() samples the Normal Truncated B distribution' )
  print ( '  normal_truncated_b_variance() computes the Normal Truncated B variance.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [-oo,%g]' % ( b ) )

  mean = normal_truncated_b_mean ( mu, s, b )

  variance = normal_truncated_b_variance ( mu, s, b )

  print ( '' )
  print ( '  PDF mean      =               %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = normal_truncated_b_sample ( mu, s, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %d' % ( sample_num ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )

  return

def normal_truncated_b_variance ( mu, s, b ):

#*****************************************************************************80
#
## normal_truncated_b_variance(): variance of the upper truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  beta = ( b - mu ) / s

  beta_pdf = normal_01_pdf ( beta )

  beta_cdf = normal_01_cdf ( beta )

  variance = s * s * ( 1.0 \
    - ( beta * beta_pdf ) / beta_cdf \
    - ( beta_pdf / beta_cdf ) ** 2 )

  return variance

def owen_values ( n_data ):

#*****************************************************************************80
#
## owen_values() returns some values of Owen's T function.
#
#  Discussion:
#
#    Owen's T function is useful for computation of the bivariate normal
#    distribution and the distribution of a skewed normal distribution.
#
#    Although it was originally formulated in terms of the bivariate
#    normal function, the function can be defined more directly as
#
#      T(H,A) = 1 / ( 2 * pi ) *
#        Integral ( 0 <= X <= A ) e^(H^2*(1+X^2)/2) / (1+X^2) dX
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = 1/(2*Pi) * Integrate [ E^(-h^2*(1+x^2)/2)/(1+x^2), {x,0,a} ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Mike Patefield, David Tandy,
#    Fast and Accurate Calculation of Owen's T Function,
#    Journal of Statistical Software,
#    Volume 5, Number 5, 2000, pages 1-25.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real H, a parameter.
#
#    real A, the upper limit of the integral.
#
#    real T, the value of the function.
#
  import numpy as np

  n_max = 28

  a_vec = np.array ( ( \
    0.2500000000000000E+00, \
    0.4375000000000000E+00, \
    0.9687500000000000E+00, \
    0.0625000000000000E+00, \
    0.5000000000000000E+00, \
    0.9999975000000000E+00, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.1000000000000000E+02, \
    0.1000000000000000E+03 ))

  h_vec = np.array ( ( \
    0.0625000000000000E+00, \
    6.5000000000000000E+00, \
    7.0000000000000000E+00, \
    4.7812500000000000E+00, \
    2.0000000000000000E+00, \
    1.0000000000000000E+00, \
    0.1000000000000000E+01, \
    0.1000000000000000E+01, \
    0.1000000000000000E+01, \
    0.1000000000000000E+01, \
    0.5000000000000000E+00, \
    0.5000000000000000E+00, \
    0.5000000000000000E+00, \
    0.5000000000000000E+00, \
    0.2500000000000000E+00, \
    0.2500000000000000E+00, \
    0.2500000000000000E+00, \
    0.2500000000000000E+00, \
    0.1250000000000000E+00, \
    0.1250000000000000E+00, \
    0.1250000000000000E+00, \
    0.1250000000000000E+00, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02 ))

  t_vec = np.array ( ( \
    3.8911930234701366E-02, \
    2.0005773048508315E-11, \
    6.3990627193898685E-13, \
    1.0632974804687463E-07, \
    8.6250779855215071E-03, \
    6.6741808978228592E-02, \
    0.4306469112078537E-01, \
    0.6674188216570097E-01, \
    0.7846818699308410E-01, \
    0.7929950474887259E-01, \
    0.6448860284750376E-01, \
    0.1066710629614485E+00, \
    0.1415806036539784E+00, \
    0.1510840430760184E+00, \
    0.7134663382271778E-01, \
    0.1201285306350883E+00, \
    0.1666128410939293E+00, \
    0.1847501847929859E+00, \
    0.7317273327500385E-01, \
    0.1237630544953746E+00, \
    0.1737438887583106E+00, \
    0.1951190307092811E+00, \
    0.7378938035365546E-01, \
    0.1249951430754052E+00, \
    0.1761984774738108E+00, \
    0.1987772386442824E+00, \
    0.2340886964802671E+00, \
    0.2479460829231492E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    t = 0.0
    h = 0.0
    a = 0.0
  else:
    t = t_vec[n_data]
    h = h_vec[n_data]
    a = a_vec[n_data]
    n_data = n_data + 1

  return n_data, h, a, t

def owen_values_test ( ):

#*****************************************************************************80
#
## owen_values_test() tests owen_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'owen_values_test():' )
  print ( '  owen_values() stores values of the OWEN function.' )
  print ( '' )
  print ( '      H         A          T' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, h, a, t = owen_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f' % ( h, a, t ) )

  return

def pareto_cdf ( x, a, b ):

#*****************************************************************************80
#
## pareto_cdf() evaluates the Pareto CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < a ):
    cdf = 0.0
  else:
    cdf = 1.0 - ( a / x ) ** b

  return cdf

def pareto_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## pareto_cdf_inv() inverts the Pareto CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'pareto_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'pareto_cdf_inv(): Fatal error!' )

  x = a / ( 1.0 - cdf ) ** ( 1.0 / b )

  return x

def pareto_cdf_test ( rng ):

#*****************************************************************************80
#
## pareto_cdf_test() tests pareto_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pareto_cdf_test():' )
  print ( '  pareto_cdf() evaluates the Pareto CDF' )
  print ( '  pareto_cdf_inv() inverts the Pareto CDF.' )
  print ( '  pareto_pdf() evaluates the Pareto PDF' )

  a = 0.5
  b = 5.0

  check = pareto_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'pareto_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    raise Exception ( 'pareto_cdf_test(): Fatal error!' )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = pareto_sample ( a, b, rng )

    pdf = pareto_pdf ( x, a, b )

    cdf = pareto_cdf ( x, a, b )

    x2 = pareto_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def pareto_check ( a, b ):

#*****************************************************************************80
#
## pareto_check() checks the parameters of the Pareto CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'pareto_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'pareto_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def pareto_mean ( a, b ):

#*****************************************************************************80
#
## pareto_mean() returns the mean of the Pareto PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  if ( b <= 1.0 ):

    print ( '' )
    print ( 'pareto_mean(): Fatal error!' )
    print ( '  For B <= 1, the mean does not exist.' )

    mean = 0.0

  else:

    mean = b * a / ( b - 1.0 )

  return mean

def pareto_pdf ( x, a, b ):

#*****************************************************************************80
#
## pareto_pdf() evaluates the Pareto PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = B * A^B / X^(B+1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, the parameters of the PDF.
#    0.0 < A.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < a ):
    pdf = 0.0
  else:
    pdf = b * a ** b / x ** ( b + 1.0 )

  return pdf

def pareto_sample ( a, b, rng ):

#*****************************************************************************80
#
## pareto_sample() samples the Pareto PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = pareto_cdf_inv ( cdf, a, b )

  return x

def pareto_sample_test ( rng ):

#*****************************************************************************80
#
## pareto_sample_test() tests pareto_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'pareto_sample_test():' )
  print ( '  pareto_mean() computes the Pareto mean' )
  print ( '  pareto_sample() samples the Pareto distribution' )
  print ( '  pareto_variance() computes the Pareto variance.' )

  a = 0.5
  b = 5.0

  check = pareto_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'pareto_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = pareto_mean ( a, b )
  variance = pareto_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = pareto_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def pareto_variance ( a, b ):

#*****************************************************************************80
#
## pareto_variance() returns the variance of the Pareto PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  if ( b <= 2.0 ):

    print ( '' )
    print ( 'pareto_variance - Warning!' )
    print ( '  For B <= 2, the variance does not exist.' )
    variance = 0.0

  else:

    variance = a * a * b / ( ( b - 1.0 ) ** 2 * ( b - 2.0 ) )

  return variance

def pearson_05_check ( a, b, c ):

#*****************************************************************************80
#
## pearson_05_check() checks the parameters of the Pearson 5 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'pearson_05_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'pearson_05_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def pearson_05_mean ( a, b, c ):

#*****************************************************************************80
#
## pearson_05_mean() evaluates the mean of the Pearson 5 PDF.
#
#  Discussion:
#
#    The mean is undefined for B <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  if ( b <= 1.0 ):
    print ( '' )
    print ( 'pearson_05_mean(): Fatal error!' )
    print ( '  MEAN undefined for B <= 1.' )
    raise Exception ( 'pearson_05_mean(): Fatal error!' )

  mean = c + a / ( b - 1.0 )

  return mean

def pearson_05_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## pearson_05_pdf() evaluates the Pearson 5 PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = A^B * ( X - C )^(-B-1)
#      * exp ( - A / ( X - C ) ) / Gamma ( B )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    C < X
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x <= c ):
    pdf = 0.0
  else:
    pdf = a ** b * ( x - c ) ** ( - b - 1.0 ) \
      * np.exp ( - a / ( x - c ) ) / gamma ( b )

  return pdf

def pearson_05_pdf_test ( ):

#*****************************************************************************80
#
## pearson_05_pdf_test() tests pearson_05_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pearson_05_pdf_test():' )
  print ( '  pearson_05_pdf() evaluates the Pearson 05 PDF.' )

  x = 5.0

  a = 1.0
  b = 2.0
  c = 3.0

  check = pearson_05_check ( a, b, c )
 
  if ( not check ):
    print ( '' )
    print ( 'pearson_05_pdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  pdf = pearson_05_pdf ( x, a, b, c )

  print ( '' )
  print ( '  PDF argument X =  %14g' % ( x ) )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF value =       %14g' % ( pdf ) )

  return

def pearson_05_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## pearson_05_sample() samples the Pearson 5 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  a2 = 0.0
  b2 = b
  c2 = 1.0 / a

  x2 = gamma_sample ( a2, b2, c2, rng )

  x = c + 1.0 / x2

  return x

def planck_check ( a, b ):

#*****************************************************************************80
#
## planck_check() checks the parameters of the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'planck_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'planck_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def planck_mean ( a, b ):

#*****************************************************************************80
#
## planck_mean() returns the mean of the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = ( b + 1.0 ) * r8_zeta ( b + 2.0 ) / r8_zeta ( b + 1.0 )

  return mean

def planck_pdf ( x, a, b ):

#*****************************************************************************80
#
## planck_pdf() evaluates the Planck PDF.
#
#  Discussion:
#
#    The Planck PDF has the form
#
#      PDF(A,BX) = A^(B+1) * X^B / ( exp ( A * X ) - 1 ) / K
#
#    where K is the normalization constant, and has the value
#
#      K = Gamma ( B + 1 ) * Zeta ( B + 1 ).
#
#    The original Planck distribution governed the frequencies in
#    blackbody radiation at a given temperature T, and has the form
#
#      PDF(AX) = K * X^3 / ( exp ( A * X ) - 1 )
#
#    where 
#
#      K = 15 / PI^4.
#
#    Thus, in terms of the Planck PDF, the original Planck distribution
#    has A = 1, B = 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    k = gamma ( b + 1.0 ) * r8_zeta ( b + 1.0 )
    pdf = a ** ( b + 1.0 ) * x ** b / ( np.exp ( a * x ) - 1.0 ) / k

  return pdf

def planck_pdf_test ( rng ):

#*****************************************************************************80
#
## planck_pdf_test() tests planck_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'planck_pdf_test():' )
  print ( '  planck_pdf() evaluates the Planck PDF.' )

  a = 2.0
  b = 3.0

  if ( not planck_check ( a, b ) ):
    print ( '' )
    print ( 'planck_pdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )
  print ( '' )
  print ( '       X            PDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = planck_sample ( a, b, rng )

    pdf = planck_pdf ( x, a, b )

    print ( '  %12g  %12g' % ( x, pdf ) )

  return

def planck_sample ( a, b, rng ):

#*****************************************************************************80
#
## planck_sample() samples the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer Verlag, 1986, pages 552.
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  a2 = 0.0
  b2 = 1.0
  c2 = b + 1.0

  g = gamma_sample ( a2, b2, c2, rng )

  z = zipf_sample ( c2, rng )

  x = g / ( a * z )

  return x

def planck_sample_test ( rng ):

#*****************************************************************************80
#
## planck_sample_test() tests planck_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'planck_sample_test():' )
  print ( '  planck_mean() returns the mean of the Planck distribution.' )
  print ( '  planck_sample() samples the Planck distribution.' )
  print ( '  planck_variance() returns the variance of the Planck distribution.' )
  print ( '' )
  
  a = 2.0
  b = 3.0

  if ( not planck_check ( a, b ) ):
    print ( '' )
    print ( 'planck_sample_test():' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  mean = planck_mean ( a, b )
  variance = planck_variance ( a, b )

  print ( '' )
  print ( '  PDF mean =     %14g' % ( mean ) )
  print ( '  PDF variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = planck_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def planck_variance ( a, b ):

#*****************************************************************************80
#
## planck_variance() returns the variance of the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 2.0281 ** 2

  return variance

def poisson_cdf ( x, a ):

#*****************************************************************************80
#
## poisson_cdf() evaluates the Poisson CDF.
#
#  Discussion:
#
#    CDF(X,A) is the probability that the number of events observed
#    in a unit time period will be no greater than X, given that the
#    expected number of events in a unit time period is A.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the CDF.
#    0 <= X.
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < 0 ):

    cdf = 0.0

  else:

    next = np.exp ( - a )
    sum2 = next

    for i in range ( 1, x + 1 ):
      last = next
      next = last * a / float ( i )
      sum2 = sum2 + next

    cdf = sum2

  return cdf

def poisson_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## poisson_cdf_inv() inverts the Poisson CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, a value of the CDF.
#    0 <= CDF < 1.
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    integer X, the corresponding argument.
#
  import numpy as np

  xmax = 100
#
#  Now simply start at X = 0, and find the first value for which
#  CDF(X-1) <= CDF <= CDF(X).
#
  sum2 = 0.0

  for i in range ( 0, xmax + 1 ):

    sumold = sum2

    if ( i == 0 ):
      next = np.exp ( - a )
      sum2 = next
    else:
      last = next
      next = last * a / float ( i )
      sum2 = sum2 + next

    if ( sumold <= cdf and cdf <= sum2 ):
      x = i
      return x

  print ( '' )
  print ( 'poisson_cdf_inv(): Warning!' )
  print ( '  Exceeded XMAX = %d' % ( xmax ) )

  x = xmax

  return x

def poisson_cdf_test ( rng ):

#*****************************************************************************80
#
## poisson_cdf_test() tests poisson_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'poisson_cdf_test():' )
  print ( '  poisson_cdf() evaluates the Poisson CDF,' )
  print ( '  poisson_cdf_inv() inverts the Poisson CDF.' )
  print ( '  poisson_pdf() evaluates the Poisson PDF.' )

  a = 10.0

  check = poisson_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'poisson_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =  %14g' % ( a ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = poisson_sample ( a, rng )

    pdf = poisson_pdf ( x, a )

    cdf = poisson_cdf ( x, a )

    x2 = poisson_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def poisson_check ( a ):

#*****************************************************************************80
#
## poisson_check() checks the parameter of the Poisson PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'poisson_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  return check

def poisson_mean ( a ):

#*****************************************************************************80
#
## poisson_mean() returns the mean of the Poisson PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def poisson_pdf ( x, a ):

#*****************************************************************************80
#
## poisson_pdf() evaluates the Poisson PDF.
#
#  Formula:
#
#    PDF(X)(A) = EXP ( - A ) * A^X / X!
#
#  Discussion:
#
#    PDF(X)(A) is the probability that the number of events observed
#    in a unit time period will be X, given the expected number
#    of events in a unit time.
#
#    The parameter A is the expected number of events per unit time.
#
#    The Poisson PDF is a discrete version of the Exponential PDF.
#
#    The time interval between two Poisson events is a random
#    variable with the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#    0 <= X
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  from scipy.special import factorial
  import numpy as np

  if ( x < 0 ):
    pdf = 0.0
  else:
    pdf = np.exp ( - a ) * a ** x / factorial ( x )

  return pdf

def poisson_sample ( a, rng ):

#*****************************************************************************80
#
## poisson_sample() samples the Poisson PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = poisson_cdf_inv ( cdf, a )

  return x

def poisson_sample_test ( rng ):

#*****************************************************************************80
#
## poisson_sample_test() tests poisson_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'poisson_sample_test():' )
  print ( '  poisson_mean() computes the Poisson mean' )
  print ( '  poisson_sample() samples the Poisson distribution' )
  print ( '  poisson_variance() computes the Poisson variance.' )

  a = 10.0

  check = poisson_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'poisson_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = poisson_mean ( a )
  variance = poisson_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = poisson_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def poisson_variance ( a ):

#*****************************************************************************80
#
## poisson_variance() returns the variance of the Poisson PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = a

  return variance

def power_cdf ( x, a, b ):

#*****************************************************************************80
#
## power_cdf() evaluates the Power CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B,
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= 0.0 ):
    cdf = 0.0
  elif ( x <= b ):
    cdf = ( x / b ) ** a
  else:
    cdf = 1.0

  return cdf

def power_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## power_cdf_inv() inverts the Power CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real X, the argument of the CDF.
#
  import numpy as np

  if ( cdf <= 0.0 ):
    x = 0.0
  elif ( cdf < 1.0 ):
    x = b * np.exp ( np.log ( cdf ) / a )
  else:
    x = b

  return x

def power_cdf_test ( rng ):

#*****************************************************************************80
#
## power_cdf_test() tests power_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'power_cdf_test():' )
  print ( '  power_cdf() evaluates the Power CDF' )
  print ( '  power_cdf_inv() inverts the Power CDF.' )
  print ( '  power_pdf() evaluates the Power PDF' )

  a = 2.0
  b = 3.0

  check = power_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'power_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = power_sample ( a, b, rng )

    pdf = power_pdf ( x, a, b )

    cdf = power_cdf ( x, a, b )

    x2 = power_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def power_check ( a, b ):

#*****************************************************************************80
#
## power_check() checks the parameter of the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'power_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'power_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def power_mean ( a, b ):

#*****************************************************************************80
#
## power_mean() returns the mean of the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a * b / ( a + 1.0 )

  return mean

def power_pdf ( x, a, b ):

#*****************************************************************************80
#
## power_pdf() evaluates the Power PDF.
#
#  Formula:
#
#    PDF(X)(A) = (A/B) * (X/B)^(A-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger and Stephen Kokoska,
#    CRC Standard Probability and Statistics Tables and Formulae,
#    Chapman and Hall/CRC, 2000, pages 152-153.
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X <= B.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0.0 or b < x ):
    pdf = 0.0
  else:
    pdf = ( a / b ) * ( x / b ) ** ( a - 1.0 )

  return pdf

def power_sample ( a, b, rng ):

#*****************************************************************************80
#
## power_sample() samples the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = power_cdf_inv ( cdf, a, b )

  return x

def power_sample_test ( rng ):

#*****************************************************************************80
#
## power_sample_test() tests power_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'power_sample_test():' )
  print ( '  power_mean() computes the Power mean' )
  print ( '  power_sample() samples the Power distribution' )
  print ( '  power_variance() computes the Power variance.' )

  a = 2.0
  b = 3.0

  check = power_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'power_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = power_mean ( a, b )
  variance = power_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = power_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def power_variance ( a, b ):

#*****************************************************************************80
#
## power_variance() returns the variance of the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = b * b * a / ( ( a + 1.0 ) ** 2 * ( a + 2.0 ) )

  return variance

def prob_test ( ):

#*****************************************************************************80
#
## prob_test() tests prob().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'prob_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test prob().' )

  rng = default_rng ( )

  angle_cdf_test ( rng )
  angle_mean_test ( )
  angle_pdf_test ( )
  anglit_cdf_test ( rng )
  anglit_sample_test ( rng )
  arcsin_cdf_test ( rng )
  arcsin_sample_test ( rng )
  benford_cdf_test ( rng )
  benford_pdf_test ( )
  benford_sample_test ( rng )
  bernoulli_cdf_test ( rng )
  bernoulli_sample_test ( rng )
  bessel_i0_test ( )
  bessel_i0_values_test ( )
  bessel_i1_test ( )
  bessel_i1_values_test ( )
  beta_binomial_cdf_test ( rng )
  beta_binomial_sample_test ( rng )
  beta_cdf_test ( rng )
  beta_cdf_values_test ( )
  beta_inc_test ( )
  beta_inc_values_test ( )
  beta_sample_test ( rng )
  beta_values_test ( )
  binomial_cdf_test ( rng )
  binomial_sample_test ( rng )
  birthday_cdf_test ( rng )
  birthday_sample_test ( rng )
  bradford_cdf_test ( rng )
  bradford_sample_test ( rng )
  buffon_box_pdf_test ( )
  buffon_box_sample_test ( rng )
  buffon_pdf_test ( )
  buffon_sample_test ( rng )
  burr_cdf_test ( rng )
  burr_sample_test ( rng )
  cardioid_cdf_test ( rng )
  cardioid_sample_test ( rng )
  cauchy_cdf_test ( rng )
  cauchy_sample_test ( rng )
  chebyshev1_cdf_test ( rng )
  chebyshev1_sample_test ( rng )
  chi_cdf_test ( rng )
  chi_sample_test ( rng )
  chi_square_cdf_test ( rng )
  chi_square_sample_test ( rng )
  chi_square_noncentral_sample_test ( rng )
  circular_normal_sample_test ( rng )
  circular_normal_01_sample_test ( rng )
  cosine_cdf_test ( rng )
  cosine_sample_test ( rng )
  coupon_sample_test ( rng )
  coupon_complete_pdf_test ( )
  deranged_cdf_test ( rng )
  deranged_sample_test ( rng )
  digamma_test ( )
  dipole_cdf_test ( rng )
  dipole_sample_test ( rng )
  dirichlet_pdf_test ( )
  dirichlet_sample_test ( rng )
  dirichlet_mix_pdf_test ( )
  dirichlet_mix_sample_test ( rng )
  discrete_cdf_test ( rng )
  discrete_sample_test ( rng )
  disk_sample_test ( rng )
  empirical_discrete_cdf_test ( rng )
  empirical_discrete_sample_test ( rng )
  english_letter_cdf_test ( rng )
  english_sentence_length_cdf_test ( rng )
  english_sentence_length_sample_test ( rng )
  english_word_length_cdf_test ( rng )
  english_word_length_sample_test ( rng )
  erlang_cdf_test ( rng )
  erlang_sample_test ( rng )
  exponential_cdf_test ( rng )
  exponential_sample_test ( rng )
  exponential_01_cdf_test ( rng )
  exponential_01_sample_test ( rng )
  extreme_values_cdf_test ( rng )
  extreme_values_sample_test ( rng )
  f_cdf_test ( rng )
  f_sample_test ( rng )
  fermi_dirac_sample_test ( rng )
  fisher_pdf_test ( rng )
  fisk_cdf_test ( rng )
  fisk_sample_test ( rng )
  folded_normal_cdf_test ( rng )
  folded_normal_sample_test ( rng )
  frechet_cdf_test ( rng )
  frechet_sample_test ( rng )
  gamma_cdf_test ( rng )
  gamma_sample_test ( rng )
  gamma_inc_values_test ( )
  geometric_cdf_test ( rng )
  geometric_sample_test ( rng )
  gompertz_cdf_test ( rng )
  gompertz_sample_test ( rng )
  gumbel_cdf_test ( rng )
  gumbel_sample_test ( rng )
  half_normal_cdf_test ( rng )
  half_normal_sample_test ( rng )
  hypergeometric_cdf_test ( rng )
  hypergeometric_sample_test ( rng )
  i4_choose_test ( )
  i4_factorial_log_test ( )
  i4_is_power_of_10_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4row_max_test ( )
  i4row_mean_test ( )
  i4row_min_test ( )
  i4row_variance_test ( )
  i4vec_print_test ( )
  i4vec_run_count_test ( rng )
  i4vec_unique_count_test ( rng )
  inverse_gaussian_cdf_test ( rng )
  inverse_gaussian_sample_test ( rng )
  laplace_cdf_test ( rng )
  laplace_sample_test ( rng )
  levy_cdf_test ( rng )
  log_normal_cdf_test ( rng )
  log_normal_sample_test ( rng )
  log_series_cdf_test ( rng )
  log_series_sample_test ( rng )
  log_uniform_cdf_test ( rng )
  log_uniform_sample_test ( rng )
  logistic_cdf_test ( rng )
  logistic_sample_test ( rng )
  lorentz_cdf_test ( rng )
  lorentz_sample_test ( rng )
  maxwell_cdf_test ( rng )
  maxwell_sample_test ( rng )
  multinomial_coef_test ( )
  multinomial_pdf_test ( )
  multinomial_sample_test ( rng )
  multinoulli_pdf_test ( rng )
  nakagami_cdf_test ( rng )
  nakagami_sample_test ( rng )
  negative_binomial_cdf_test ( rng )
  negative_binomial_sample_test ( rng )
  normal_01_cdf_test ( rng )
  normal_01_cdf_values_test ( )
  normal_01_sample_test ( rng )
  normal_cdf_test ( rng )
  normal_sample_test ( rng )
  normal_truncated_ab_cdf_test ( rng )
  normal_truncated_ab_sample_test ( rng )
  normal_truncated_a_cdf_test ( rng )
  normal_truncated_a_sample_test ( rng )
  normal_truncated_b_cdf_test ( rng )
  normal_truncated_b_sample_test ( rng )
  owen_values_test ( )
  pareto_cdf_test ( rng )
  pareto_sample_test ( rng )
  pearson_05_pdf_test ( )
  planck_pdf_test ( rng )
  planck_sample_test ( rng )
  poisson_cdf_test ( rng )
  poisson_sample_test ( rng )
  power_cdf_test ( rng )
  power_sample_test ( rng )
  psi_values_test ( )
  quasigeometric_cdf_test ( rng )
  quasigeometric_sample_test ( rng )
  r8_beta_test ( )
  r8_csc_test ( )
  r8_erf_test ( )
  r8_gamma_inc_test ( )
  r8_zeta_test ( )
  r8poly_print_test ( )
  r8poly_value_horner_test ( )
  r8row_max_test ( )
  r8row_mean_test ( )
  r8row_min_test ( )
  r8row_variance_test ( )
  r8vec_transpose_print_test ( )
  r8vec2_print_test ( )
  rayleigh_cdf_test ( rng )
  rayleigh_sample_test ( rng )
  reciprocal_cdf_test ( rng )
  reciprocal_sample_test ( rng )
  sech_cdf_test ( rng )
  sech_sample_test ( rng )
  semicircular_cdf_test ( rng )
  semicircular_sample_test ( rng )
  sin_power_int_test ( )
  sin_power_int_values_test ( )
  stirling2_number_test ( )
  student_cdf_test ( rng )
  student_sample_test ( rng )
  student_noncentral_cdf_test ( rng )
  tfn_test ( )
  triangle_cdf_test ( rng )
  triangle_sample_test ( rng )
  triangular_cdf_test ( rng )
  triangular_sample_test ( rng )
  trigamma_test ( )
  trigamma_values_test ( )
  uniform_01_cdf_test ( rng )
  uniform_01_sample_test ( rng )
  uniform_01_order_sample_test ( rng )
  uniform_cdf_test ( rng )
  uniform_sample_test ( rng )
  uniform_discrete_cdf_test ( rng )
  uniform_discrete_sample_test ( rng )
  uniform_nsphere_sample_test ( rng )
  von_mises_cdf_test ( rng )
  von_mises_sample_test ( rng )
  weibull_cdf_test ( rng )
  weibull_sample_test ( rng )
  weibull_discrete_cdf_test ( rng )
  weibull_discrete_sample_test ( rng )
  zipf_cdf_test ( rng )
  zipf_sample_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'prob_test():' )
  print ( '  Normal end of execution.' )
  return

def psi_values ( n_data ):

#*****************************************************************************80
#
## psi_values() returns some values of the Psi or Digamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[x]
#
#    or
#
#      PolyGamma[0,x]
#
#    PSI(X) = d ln ( Gamma ( X ) ) / d X = Gamma'(X) / Gamma(X)
#
#    PSI(1) = -Euler's constant.
#
#    PSI(X+1) = PSI(X) + 1 / X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -10.42375494041108E+00, \
     -5.289039896592188E+00, \
     -3.502524222200133E+00, \
     -2.561384544585116E+00, \
     -1.963510026021423E+00, \
     -1.540619213893190E+00, \
     -1.220023553697935E+00, \
     -0.9650085667061385E+00, \
     -0.7549269499470514E+00, \
     -0.5772156649015329E+00, \
     -0.4237549404110768E+00, \
     -0.2890398965921883E+00, \
     -0.1691908888667997E+00, \
     -0.6138454458511615E-01, \
      0.3648997397857652E-01, \
      0.1260474527734763E+00, \
      0.2085478748734940E+00, \
      0.2849914332938615E+00, \
      0.3561841611640597E+00, \
      0.4227843350984671E+00 ))

  x_vec = np.array ( ( \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def psi_values_test ( ):

#*****************************************************************************80
#
## psi_values_test() tests psi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'psi_values_test():' )
  print ( '  psi_values() stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def quasigeometric_cdf ( x, a, b ):

#*****************************************************************************80
#
## quasigeometric_cdf() evaluates the Quasigeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the number of trials.
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 0 ):
    cdf = 0.0
  elif ( x == 0 ):
    cdf = a
  elif ( b == 0.0 ):
    cdf = 1.0
  else:
    cdf = a + ( 1.0 - a ) * ( 1.0 - b ** x )

  return cdf

def quasigeometric_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## quasigeometric_cdf_inv() inverts the Quasigeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    integer X, the corresponding value of X.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'quasigeometric_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'quasigeometric_cdf_inv(): Fatal error!' )

  if ( cdf < a ):
    x = 0
  elif ( b == 0.0 ):
    x = 1
  else:
    x = 1 + int ( ( np.log ( 1.0 - cdf ) - np.log ( 1.0 - a ) ) / np.log ( b ) )

  return x

def quasigeometric_cdf_test ( rng ):

#*****************************************************************************80
#
## quasigeometric_cdf_test() tests quasigeometric_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'quasigeometric_cdf_test():' )
  print ( '  quasigeometric_cdf() evaluates the Quasigeometric CDF' )
  print ( '  quasigeometric_cdf_inv() inverts the Quasigeometric CDF.' )
  print ( '  quasigeometric_pdf() evaluates the Quasigeometric PDF' )

  a = 0.4825
  b = 0.5893

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  check = quasigeometric_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'quasigeometric_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    raise Exception ( 'quasigeometric_cdf_test(): Fatal error!' )

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = quasigeometric_sample ( a, b, rng )

    pdf = quasigeometric_pdf ( x, a, b )

    cdf = quasigeometric_cdf ( x, a, b )

    x2 = quasigeometric_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def quasigeometric_check ( a, b ):

#*****************************************************************************80
#
## quasigeometric_check() checks the parameters of the Quasigeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'quasigeometric_check(): Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False

  if ( b < 0.0 or 1.0 <= b ):
    print ( '' )
    print ( 'quasigeometric_check(): Fatal error!' )
    print ( '  B < 0 or 1 <= B.' )
    check = False

  return check

def quasigeometric_mean ( a, b ):

#*****************************************************************************80
#
## quasigeometric_mean() returns the mean of the Quasigeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = ( 1.0 - a  ) / ( 1.0 - b )

  return mean

def quasigeometric_pdf ( x, a, b ):

#*****************************************************************************80
#
## quasigeometric_pdf() evaluates the Quasigeometric PDF.
#
#  Discussion:
#
#    PDF(A,BX) =    A                     if 0  = X
#               = (1-A) * (1-B) * B^(X-1)  if 1 <= X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Darren Glass, Philip Lowry,
#    Quasiquasigeometric Distributions and Extra Inning Baseball Games,
#    Mathematics Magazine,
#    Volume 81, Number 2, April 2008, pages 127-137.
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton University Press, 2008,
#    ISBN13: 978-0-691-12698-2,
#    LC: QA273.25.N34.
#
#  Input:
#
#    integer X, the independent variable.
#    0 <= X
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0 ):

    pdf = 0.0

  elif ( x == 0 ):

    pdf = a

  elif ( b == 0.0 ):

    if ( x == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    pdf = ( 1.0 - a ) * ( 1.0 - b ) * b ** ( x - 1 )

  return pdf

def quasigeometric_sample ( a, b, rng ):

#*****************************************************************************80
#
## quasigeometric_sample() samples the Quasigeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = quasigeometric_cdf_inv ( cdf, a, b )

  return x

def quasigeometric_sample_test ( rng ):

#*****************************************************************************80
#
## quasigeometric_sample_test() tests quasigeometric_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  sample_num = 1000

  print ( '' )
  print ( 'quasigeometric_sample_test():' )
  print ( '  quasigeometric_mean() computes the Quasigeometric mean' )
  print ( '  quasigeometric_sample() samples the Quasigeometric distribution' )
  print ( '  quasigeometric_variance() computes the Quasigeometric variance.' )

  a = 0.4825
  b = 0.5893

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  check = quasigeometric_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'quasigeometric_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = quasigeometric_mean ( a, b )
  variance = quasigeometric_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i] = quasigeometric_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def quasigeometric_variance ( a, b ):

#*****************************************************************************80
#
## quasigeometric_variance() returns the variance of the Quasigeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( 1.0 - a ) * ( a + b ) / ( 1.0 - b ) / ( 1.0 - b )

  return variance

def r8_beta ( a, b ):

#*****************************************************************************80
#
## r8_beta() returns the value of the Beta function.
#
#  Discussion:
#
#    BETA(A,B) = ( GAMMA ( A ) * GAMMA ( B ) ) / GAMMA ( A + B )
#              = Integral ( 0 <= T <= 1 ) T^(A-1) (1-T)^(B-1) dT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the function.
#    0.0 < A,
#    0.0 < B.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
  from scipy.special import gamma

  if ( a <= 0.0 or b <= 0.0 ):
    print ( '' )
    print ( 'r8_beta(): Fatal error!' )
    print ( '  Both A and B must be greater than 0.' )
    raise Exception ( 'r8_beta(): Fatal error!' )

  value = gamma ( a ) * gamma ( b ) / gamma ( a + b )

  return value

def r8_beta_test ( ):

#*****************************************************************************80
#
## r8_beta_test() tests r8_beta().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_beta_test():' )
  print ( '  r8_beta() evaluates the Beta function.' )
  print ( '' )
  print ( '      X         Y         BETA(X,Y)         r8_beta(X,Y)' )
  print ( '                          tabulated         computed.' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f1 = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_beta ( x, y )

    print ( '  %12g  %12g  %24.16g  %24.16g' % ( x, y, f1, f2 ) )

  return

def r8_csc ( theta ):

#*****************************************************************************80
#
## r8_csc() returns the cosecant of X.
#
#  Discussion:
#
#    r8_csc ( THETA ) = 1.0 / SIN ( THETA )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real THETA, the angle, in radians, whose cosecant is desired.
#    It must be the case that SIN ( THETA ) is not zero.
#
#  Output:
#
#    real VALUE, the cosecant of THETA.
#
  import numpy as np

  value = np.sin ( theta )

  if ( value == 0.0 ):
    print ( '' )
    print ( 'r8_csc(): Fatal error!' )
    print ( '  Cosecant undefined for THETA = %g' % ( theta ) )
    raise Exception ( 'r8_csc(): Fatal error!' )

  value = 1.0 / value

  return value

def r8_csc_test ( ):

#*****************************************************************************80
#
## r8_csc_test() tests r8_csc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r8_csc_test():' )
  print ( '  r8_csc() computes the cosecant of an angle.' )
  print ( '' )
  print ( '  ANGLE    r8_csc(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    r = angle / 2.0 / np.pi
    if ( ( i % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_csc ( r ) ) )

  return

def r8_erf ( x ):

#*****************************************************************************80
#
## r8_erf() evaluates the error function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    W J Cody,
#    Mathematics and Computer Science Division,
#    Argonne National Laboratory,
#    Argonne, Illinois, 60439.
#
#  Reference:
#
#    W J Cody,
#    "Rational Chebyshev approximations for the error function",
#    Mathematics of Computation, 
#    1969, pages 631-638.
#
#  Input:
#
#    real X, the argument of the error function.
#
#  Output:
#
#    real VALUE, the value of the error function.
#
  import numpy as np

  a = np.array ( ( \
    3.16112374387056560E+00, \
    1.13864154151050156E+02, \
    3.77485237685302021E+02, \
    3.20937758913846947E+03, \
    1.85777706184603153E-01 ))
  b = np.array ( ( \
    2.36012909523441209E+01, \
    2.44024637934444173E+02, \
    1.28261652607737228E+03, \
    2.84423683343917062E+03 ))
  c = np.array ( ( \
    5.64188496988670089E-01, \
    8.88314979438837594E+00, \
    6.61191906371416295E+01, \
    2.98635138197400131E+02, \
    8.81952221241769090E+02, \
    1.71204761263407058E+03, \
    2.05107837782607147E+03, \
    1.23033935479799725E+03, \
    2.15311535474403846E-08 ))
  d = np.array ( ( \
    1.57449261107098347E+01, \
    1.17693950891312499E+02, \
    5.37181101862009858E+02, \
    1.62138957456669019E+03, \
    3.29079923573345963E+03, \
    4.36261909014324716E+03, \
    3.43936767414372164E+03, \
    1.23033935480374942E+03 ))
  p = np.array ( ( \
    3.05326634961232344E-01, \
    3.60344899949804439E-01, \
    1.25781726111229246E-01, \
    1.60837851487422766E-02, \
    6.58749161529837803E-04, \
    1.63153871373020978E-02 ))
  q = np.array ( ( \
    2.56852019228982242E+00, \
    1.87295284992346047E+00, \
    5.27905102951428412E-01, \
    6.05183413124413191E-02, \
    2.33520497626869185E-03 ))
  sqrpi = 0.56418958354775628695E+00
  thresh = 0.46875E+00
  xbig = 26.543E+00
  xsmall = 1.11E-16

  xabs = abs ( x )
#
#  Evaluate ERF(X) for |X| <= 0.46875.
#
  if ( xabs <= thresh ):

    if ( xsmall < xabs ):
      xsq = xabs * xabs
    else:
      xsq = 0.0

    xnum = a[4] * xsq
    xden = xsq
    for i in range ( 0, 3 ):
      xnum = ( xnum + a[i] ) * xsq
      xden = ( xden + b[i] ) * xsq

    value = x * ( xnum + a[3] ) / ( xden + b[3] )
#
#  Evaluate ERFC(X) for 0.46875 <= |X| <= 4.0.
#
  elif ( xabs <= 4.0 ):

    xnum = c[8] * xabs
    xden = xabs
    for i in range ( 0, 7 ):
      xnum = ( xnum + c[i] ) * xabs
      xden = ( xden + d[i] ) * xabs

    value = ( xnum + c[7] ) / ( xden + d[7] )
    xsq = np.floor ( xabs * 16.0 ) / 16.0
    delt = ( xabs - xsq ) * ( xabs + xsq )
    value = np.exp ( - xsq * xsq ) * np.exp ( - delt ) * value

    value = ( 0.5 - value ) + 0.5

    if ( x < 0.0 ):
      value = -value
#
#  Evaluate ERFC(X) for 4.0 < |X|.
#
  else:

    if ( xbig <= xabs ):

      if ( 0.0 < x ):
        value = 1.0
      else:
        value = -1.0;

    else:

      xsq = 1.0 / ( xabs * xabs )

      xnum = p[5] * xsq
      xden = xsq
      for i in range ( 0, 4 ):
        xnum = ( xnum + p[i] ) * xsq
        xden = ( xden + q[i] ) * xsq

      value = xsq * ( xnum + p[4] ) / ( xden + q[4] )
      value = ( sqrpi -  value ) / xabs
      xsq = np.floor ( xabs * 16.0 ) / 16.0
      delt = ( xabs - xsq ) * ( xabs + xsq )
      value = np.exp ( - xsq * xsq ) * np.exp ( - delt ) * value

      value = ( 0.5 - value ) + 0.5

      if ( x < 0.0 ):
        value = -value;

  return value

def r8_erf_test ( ):

#*****************************************************************************80
#
## r8_erf_test() tests r8_erf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_erf_test():' )
  print ( '  r8_erf() evaluates the error function.' )
  print ( '' )
  print ( '      X            ERF(X)    r8_erf(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_erf ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8_gamma_inc ( p, x ):

#*****************************************************************************80
#
## r8_gamma_inc() computes the incomplete Gamma function.
#
#  Discussion:
#
#    gamma_inc(P,X) = Integral ( 0 <= T <= X ) T^(P-1) EXP(-T) DT / GAMMA(P).
#
#    gamma_inc(P,       0) = 0,
#    gamma_inc(P,Infinity) = 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    B L Shea,
#    Chi-squared and Incomplete Gamma Integral,
#    Algorithm AS239,
#    Applied Statistics,
#    Volume 37, Number 3, 1988, pages 466-473.
#
#  Input:
#
#    real P, the exponent parameter.
#    0.0 < P.
#
#    real X, the integral limit parameter.
#    If X is less than or equal to 0, the value is returned as 0.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
  from scipy.special import gammaln

  exp_arg_min = -88.0
  overflow = 1.0E+37
  plimit = 1000.0
  tol = 1.0E-07
  xbig = 1.0E+08

  value = 0.0

  if ( p <= 0.0 ):
    print ( '' )
    print ( 'r8_gamma_inc(): Fatal error!' )
    print ( '  Parameter P <= 0.' )
    raise Exception ( 'r8_gamma_inc(): Fatal error!' )

  if ( x <= 0.0 ):
    value = 0.0
    return value
#
#  Use a normal approximation if PLIMIT < P.
#
  if ( plimit < p ):
    pn1 = 3.0 * np.sqrt ( p ) * ( ( x / p ) ** ( 1.0 / 3.0 ) + 1.0 / ( 9.0 * p ) - 1.0 )
    cdf = normal_01_cdf ( pn1 )
    value = cdf
    return value
#
#  Is X extremely large compared to P?
#
  if ( xbig < x ):
    value = 1.0
    return value
#
#  Use Pearson's series expansion.
#  (P is not large enough to force overflow in the log of Gamma.
#
  if ( x <= 1.0 or x < p ):

    arg = p * np.log ( x ) - x - gammaln ( p + 1.0 )
    c = 1.0
    value = 1.0
    a = p

    while ( True ):

      a = a + 1.0
      c = c * x / a
      value = value + c

      if ( c <= tol ):
        break

    arg = arg + np.log ( value )

    if ( exp_arg_min <= arg ):
      value = np.exp ( arg )
    else:
      value = 0.0

  else:
#
#  Use a continued fraction expansion.
#
    arg = p * np.log ( x ) - x - gammaln ( p )
    a = 1.0 - p
    b = a + x + 1.0
    c = 0.0
    pn1 = 1.0
    pn2 = x
    pn3 = x + 1.0
    pn4 = x * b
    value = pn3 / pn4

    while ( True ):

      a = a + 1.0
      b = b + 2.0
      c = c + 1.0
      pn5 = b * pn3 - a * c * pn1
      pn6 = b * pn4 - a * c * pn2

      if ( 0.0 < abs ( pn6 ) ):

        rn = pn5 / pn6

        if ( abs ( value - rn ) <= min ( tol, tol * rn ) ):

          arg = arg + np.log ( value )

          if ( exp_arg_min <= arg ):
            value = 1.0 - np.exp ( arg )
          else:
            value = 1.0

          return value

        value = rn

      pn1 = pn3
      pn2 = pn4
      pn3 = pn5
      pn4 = pn6
#
#  Rescale terms in continued fraction if terms are large.
#
      if ( overflow <= abs ( pn5 ) ):
        pn1 = pn1 / overflow
        pn2 = pn2 / overflow
        pn3 = pn3 / overflow
        pn4 = pn4 / overflow

  return value

def r8_gamma_inc_test ( ):

#*****************************************************************************80
#
## r8_gamma_inc_test() tests r8_gamma_inc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_gamma_inc_test():' )
  print ( '  r8_gamma_inc() evaluates the normalized incomplete Gamma' )
  print ( '  function P(A,X).' )
  print ( '' )
  print ( '         A         X         Exact F  r8_gamma_inc(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma_inc ( a, x )

    print ( '  %8g  %8g  %14g  %14g' % ( a, x, fx, fx2 ) )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## r8poly_print() prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of the polynomial.
#
#    real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
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
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8poly_print_test():' )
  print ( '  r8poly_print() prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )

  return

def r8poly_value_horner ( m, c, x ):

#*****************************************************************************80
#
## r8poly_value_horner() evaluates a polynomial using Horner's method.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the polynomial value.
#
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8poly_value_horner_test ( ):

#*****************************************************************************80
#
## r8poly_value_horner_test() tests r8poly_value_horner().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_value_horner_test():' )
  print ( '  r8poly_value_horner() evaluates a polynomial at a point' )
  print ( '  using Horner\'s method.' )

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

  return

def r8row_max ( m, n, x ):

#*****************************************************************************80
#
## r8row_max() returns the maximums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M,N), the R8ROW.
#
#  Output:
#
#    real XMAX(M), the maximums of the rows of X.
#
  import numpy as np

  xmax = np.zeros ( m )

  for i in range ( 0, m ):
    xmax[i] = x[i,0]
    for j in range ( 1, n ):
      xmax[i] = max ( xmax[i], x[i,j] )

  return xmax

def r8row_max_test ( ):

#*****************************************************************************80
#
## r8row_max_test() tests r8row_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_max_test():' )
  print ( '  r8row_max() computes maximums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  amax = r8row_max ( m, n, a )

  r8vec_print ( m, amax, '  Row maximums:' )

  return

def r8row_mean ( m, n, a ):

#*****************************************************************************80
#
## r8row_mean() returns the means of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the R8ROW
#
#  Output:
#
#    real ROW_mean(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def r8row_mean_test ( ):

#*****************************************************************************80
#
## r8row_mean_test() tests r8row_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_mean_test():' )
  print ( '  r8row_mean() computes row means of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  means = r8row_mean ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )

  return

def r8row_min ( m, n, x ):

#*****************************************************************************80
#
## r8row_min() returns the minimums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M,N), the R8ROW.
#
#  Output:
#
#    real XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def r8row_min_test ( ):

#*****************************************************************************80
#
## r8row_min_test() tests r8row_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_min_test():' )
  print ( '  r8row_min() computes minimums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  amin = r8row_min ( m, n, a )

  r8vec_print ( m, amin, '  Row minimums:' )

  return

def r8row_variance ( m, n, x ):

#*****************************************************************************80
#
## r8row_variance() returns the variances of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M,N), the R8ROW whose row means are desired.
#
#  Output:
#
#    real VARIANCE(M), the variances of the rows of X.
#
  import numpy as np

  variance = np.zeros ( m )

  for i in range ( 0, m ):

    mean = 0.0
    for j in range ( 0, n ):
      mean = mean + x[i,j]
    mean = mean / float ( n )

    for j in range ( 0, n ):
      variance[i] = variance[i] + ( x[i,j] - mean ) ** 2

    if ( 1 < n ):
      variance[i] = variance[i] / float ( n - 1 )
    else:
      variance[i] = 0.0 

  return variance

def r8row_variance_test ( ):

#*****************************************************************************80
#
## r8row_variance_test() tests r8row_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_variance_test():' )
  print ( '  r8row_variance() computes variances of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  variance = r8row_variance ( m, n, a )

  r8vec_print ( m, variance, '  The row variances:' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec_circular_variance ( n, x ):

#*****************************************************************************80
#
## r8vec_circular_variance() returns the circular variance of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real X(N), the vector whose variance is desired.
#
#  Output:
#
#    real VALUE, the circular variance of the vector entries.
#
  import numpy as np

  mean = 0.0
  for i in range ( 0, n ):
    mean = mean + x[i]
  mean = mean / float ( n )

  c = 0.0
  s = 0.0
  for i in range ( 0, n ):
    c = c + np.cos ( x[i] - mean )
    s = s + np.sin ( x[i] - mean )

  value = s * s + c * c

  value = np.sqrt ( value ) / float ( n )

  value = 1.0 - value

  return value

def r8vec_circular_variance_test ( ):

#*****************************************************************************80
#
## r8vec_circular_variance_test() tests r8vec_circular_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_circular_variance_test():' )
  print ( '  r8vec_circular_variance() computes the circular variance of an R8VEC.' )

  n = 10
  a = - np.pi
  b = + np.pi
  x = a + ( b - a ) * rng.random ( size = n )

  r8vec_print ( n, x, '  Uniform Vector in [-PI,+PI]:' )
  circular_variance = r8vec_circular_variance ( n, x )

  print ( '' )
  print ( '  Circular variance: %g' % ( circular_variance ) )

  x = rng.standard_normal ( size = n )

  r8vec_print ( n, x, '  Normal vector, mean 0, variance 1' )

  circular_variance = r8vec_circular_variance ( n, x )

  print ( '' )
  print ( '  Circular variance: %g' % ( circular_variance ) )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_transpose_print() prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## r8vec_transpose_print_test() tests r8vec_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  n = 11

  print ( '' )
  print ( 'r8vec_transpose_print_test():' )
  print ( '  r8vec_transpose_print() prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x = np.array ( [ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 ] )

  r8vec_transpose_print ( n, x, '  The vector X:' )

  return

def r8_zeta ( p ):

#*****************************************************************************80
#
## r8_zeta() estimates the Riemann Zeta function.
#
#  Discussion:
#
#    For 1 < P, the Riemann Zeta function is defined as:
#
#      ZETA ( P ) = Sum ( 1 <= N < oo ) 1 / N ^ P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    real P, the power to which the integers are raised.
#    P must be greater than 1.  For integral P up to 20, a
#    precomputed value of ZETA is returned otherwise the infinite
#    sum is approximated.
#
#  Output:
#
#    real VALUE, an approximation to the Riemann
#    Zeta function.
#
  import numpy as np

  if ( p <= 1.0 ):
    value = np.finfo(float).max
  elif ( p == 2.0 ):
    value = np.pi ** 2 / 6.0
  elif ( p == 3.0 ):
    value = 1.2020569032
  elif ( p == 4.0 ):
    value = np.pi ** 4 / 90.0
  elif ( p == 5.0 ):
    value = 1.0369277551
  elif ( p == 6.0 ):
    value = np.pi ** 6 / 945.0
  elif ( p == 7.0 ):
    value = 1.0083492774
  elif ( p == 8.0 ):
    value = np.pi ** 8 / 9450.0
  elif ( p == 9.0 ):
    value = 1.0020083928
  elif ( p == 10.0 ):
    value = np.pi ** 10 / 93555.0
  elif ( p == 11.0 ):
    value = 1.0004941886
  elif ( p == 12.0 ):
    value = 1.0002460866
  elif ( p == 13.0 ):
    value = 1.0001227133
  elif ( p == 14.0 ):
    value = 1.0000612482
  elif ( p == 15.0 ):
    value = 1.0000305882
  elif ( p == 16.0 ):
    value = 1.0000152823
  elif ( p == 17.0 ):
    value = 1.0000076372
  elif ( p == 18.0 ):
    value = 1.0000038173
  elif ( p == 19.0 ):
    value = 1.0000019082
  elif ( p == 20.0 ):
    value = 1.0000009540
  else:

    zsum = 0.0
    n = 0

    while ( True ):

      n = n + 1
      zsum_old = zsum
      zsum = zsum + 1.0 / n ** p

      if ( zsum <= zsum_old ):
        break

    value = zsum

  return value

def r8_zeta_test ( ):

#*****************************************************************************80
#
## r8_zeta_test() tests r8_zeta().
#
#  Discussion:
#
#    Note that SCIPY provides a ZETA function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_zeta_test():' )
  print ( '  r8_zeta() estimates the Zeta function.' )

  print ( '' )
  print ( '       P     r8_zeta(P)' )
  print ( '' )
  for p in range ( 1, 26 ):
    v = r8_zeta ( p )
    print ( '  %6d  %14.6g' % ( p, v ) )

  print ( '' )
  for i in range ( 0, 9 ):
    p = 3.0 + float ( i ) / 8.0
    v = r8_zeta ( p )
    print ( '  %6g  %14.6g' % ( p, v ) )

  return

def rayleigh_cdf ( x, a ):

#*****************************************************************************80
#
## rayleigh_cdf() evaluates the Rayleigh CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#    0.0 <= X.
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < 0.0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( - x * x / ( 2.0 * a * a ) )

  return cdf

def rayleigh_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## rayleigh_cdf_inv() inverts the Rayleigh CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'rayleigh_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'rayleigh_cdf_inv(): Fatal error!' )

  x = np.sqrt ( - 2.0 * a * a * np.log ( 1.0 - cdf ) )

  return x

def rayleigh_cdf_test ( rng ):

#*****************************************************************************80
#
## rayleigh_cdf_test() tests rayleigh_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'rayleigh_cdf_test():' )
  print ( '  rayleigh_cdf() evaluates the Rayleigh CDF' )
  print ( '  rayleigh_cdf_inv() inverts the Rayleigh CDF.' )
  print ( '  rayleigh_pdf() evaluates the Rayleigh PDF' )

  a = 2.0

  check = rayleigh_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'rayleigh_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = rayleigh_sample ( a, rng )

    pdf = rayleigh_pdf ( x, a )

    cdf = rayleigh_cdf ( x, a )

    x2 = rayleigh_cdf_inv ( cdf, a )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def rayleigh_check ( a ):

#*****************************************************************************80
#
## rayleigh_check() checks the parameter of the Rayleigh PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'rayleigh_check(): Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  return check

def rayleigh_mean ( a ):

#*****************************************************************************80
#
## rayleigh_mean() returns the mean of the Rayleigh PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = a * np.sqrt ( 0.5 * np.pi )

  return mean

def rayleigh_pdf ( x, a ):

#*****************************************************************************80
#
## rayleigh_pdf() evaluates the Rayleigh PDF.
#
#  Formula:
#
#    PDF(X)(A) = ( X / A^2 ) * EXP ( - X^2 / ( 2 * A^2 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X
#
#    real A, the parameter of the PDF.
#    0 < A.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    pdf = ( x / ( a * a ) ) * np.exp ( - x * x / ( 2.0 * a * a ) )

  return pdf

def rayleigh_sample ( a, rng ):

#*****************************************************************************80
#
## rayleigh_sample() samples the Rayleigh PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = rayleigh_cdf_inv ( cdf, a )

  return x

def rayleigh_sample_test ( rng ):

#*****************************************************************************80
#
## rayleigh_sample_test() tests rayleigh_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'rayleigh_sample_test():' )
  print ( '  rayleigh_mean() computes the Rayleigh mean' )
  print ( '  rayleigh_sample() samples the Rayleigh distribution' )
  print ( '  rayleigh_variance() computes the Rayleigh variance.' )

  a = 2.0

  check = rayleigh_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'rayleigh_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = rayleigh_mean ( a )
  variance = rayleigh_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = rayleigh_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def rayleigh_variance ( a ):

#*****************************************************************************80
#
## rayleigh_variance() returns the variance of the Rayleigh PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameters of the PDF.
#    0.0 < A.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = 2.0 * a * a * ( 1.0 - 0.25 * np.pi )

  return variance

def reciprocal_cdf ( x, a, b ):

#*****************************************************************************80
#
## reciprocal_cdf() evaluates the Reciprocal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):

    cdf = 0.0

  elif ( 0.0 < x ):

    cdf = np.log ( a / x ) / np.log ( a / b )

  return cdf

def reciprocal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## reciprocal_cdf_inv() inverts the Reciprocal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  if ( cdf <= 0.0 ):
    x = 0.0
  elif ( 0.0 < cdf ):
    x = b ** cdf / a ** ( cdf - 1.0 )

  return x

def reciprocal_cdf_test ( rng ):

#*****************************************************************************80
#
## reciprocal_cdf_test() tests reciprocal_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'reciprocal_cdf_test():' )
  print ( '  reciprocal_cdf() evaluates the Reciprocal CDF.' )
  print ( '  reciprocal_cdf_inv() inverts the Reciprocal CDF.' )
  print ( '  reciprocal_pdf() evaluates the Reciprocal PDF.' )

  a = 1.0
  b = 3.0

  check = reciprocal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'reciprocal_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A =         %14g' % ( a ) )
  print ( '  PDF parameter B =         %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = reciprocal_sample ( a, b, rng )

    pdf = reciprocal_pdf ( x, a, b )

    cdf = reciprocal_cdf ( x, a, b )

    x2 = reciprocal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def reciprocal_check ( a, b ):

#*****************************************************************************80
#
## reciprocal_check() checks the parameters of the Reciprocal CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'reciprocal_check(): Fatal error!' )
    print ( '  A <= 0.0' )
    check = False

  if ( b < a ):
    print ( '' )
    print ( 'reciprocal_check(): Fatal error!' )
    print ( '  B < A' )
    check = False

  return check

def reciprocal_mean ( a, b ):

#*****************************************************************************80
#
## reciprocal_mean() returns the mean of the Reciprocal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = ( a - b ) / np.log ( a / b )

  return mean

def reciprocal_pdf ( x, a, b ):

#*****************************************************************************80
#
## reciprocal_pdf() evaluates the Reciprocal PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 1.0 / ( X * LOG ( B / A ) )
#    for 0.0 <= X
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    pdf = 0.0
  elif ( 0.0 < x ):
    pdf = 1.0 / ( x * np.log ( b / a ) )

  return pdf

def reciprocal_sample ( a, b, rng ):

#*****************************************************************************80
#
## reciprocal_sample() samples the Reciprocal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = b ** cdf / a ** ( cdf - 1.0 )

  return x

def reciprocal_sample_test ( rng ):

#*****************************************************************************80
#
## reciprocal_sample_test() tests reciprocal_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'reciprocal_sample_test():' )
  print ( '  reciprocal_mean() computes the Reciprocal mean' )
  print ( '  reciprocal_sample() samples the Reciprocal distribution' )
  print ( '  reciprocal_variance() computes the Reciprocal variance.' )

  a = 1.0
  b = 3.0

  check = reciprocal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'reciprocal_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = reciprocal_mean ( a, b )
  variance = reciprocal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF variance =          %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = reciprocal_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def reciprocal_variance ( a, b ):

#*****************************************************************************80
#
## reciprocal_variance() returns the variance of the Reciprocal PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  d = np.log ( a / b )

  variance = ( a - b ) * ( a * ( d - 2.0 ) + b * ( d + 2.0 ) ) / ( 2.0 * d * d )

  return variance

def runs_mean ( m, n ):

#*****************************************************************************80
#
## runs_mean() returns the mean of the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = float ( m + 2 * m * n + n ) / float ( m + n )

  return mean

def runs_pdf ( m, n, r ):

#*****************************************************************************80
#
## runs_pdf() evaluates the Runs PDF.
#
#  Discussion:
#
#    Suppose we have M symbols of one type and N of another, and we consider
#    the various possible permutations of these symbols.
#
#    Let "R" be the number of runs in a given permutation.  By a "run", we
#    mean a maximal sequence of identical symbols.  Thus, for instance,
#    the permutation
#
#      ABBBAAAAAAAA
#
#    has three runs.
#
#    The probability that a permutation of M+N symbols, with M of one kind
#    and N of another, will have exactly R runs is:
#
#      PDF(M,N)(R) = 2 * C(M-1,R/2-1) * C(N-1,R/2-1)
#                    / C(M+N,N) for R even
#
#                  = ( C(M-1,(R-1)/2) * C(N-1,(R-3)/2 )
#                    + C(M-1,(R-3)/2) * C(N-1,(R-1)/2 )
#                    ) / C(M+N,N) for R odd.
#
#    Note that the maximum number of runs for a given M and N is:
#
#      M + N,                if M = N
#      2 * min ( M, N ) + 1  otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kalimutha Krishnamoorthy,
#    Handbook of Statistical Distributions with Applications,
#    Chapman and Hall, 2006,
#    ISBN: 1-58488-635-8,
#    LC: QA273.6.K75.
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#
#    integer R, the number of runs.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  from scipy.special import comb

  if ( m < 0 ):
    print ( '' )
    print ( 'RUN_pdf(): Fatal error!' )
    print ( '  M must be at least 0.' )
    print ( '  The input value of M = %d' % ( m ) )
    raise Exception ( 'RUN_pdf(): Fatal error!' )

  if ( n < 0 ):
    print ( '' )
    print ( 'RUN_pdf(): Fatal error!' )
    print ( '  N must be at least 0.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'RUN_pdf(): Fatal error!' )

  if ( n + m <= 0 ):
    print ( '' )
    print ( 'RUN_pdf(): Fatal error!' )
    print ( '  M+N must be at least 1.' )
    print ( '  The input value of M+N = %d' % ( m + n ) )
    raise Exception ( 'RUN_pdf(): Fatal error!' )
#
#  If all the symbols are of one type, there is always 1 run.
#
  if ( m == 0 or n == 0 ):
    if ( r == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0
    return pdf
#
#  Take care of extreme values of R.
#
  if ( r < 2 or m + n < r ):
    pdf = 0.0
    return pdf
#
#  The normal cases.
#
  if ( ( r % 2 ) == 0 ):

    pdf = float ( 2 * comb ( m - 1, ( r // 2 ) - 1 ) \
                    * comb ( n - 1, ( r // 2 ) - 1 ) ) \
        / float (     comb ( m + n, n ) )

  else:

    pdf = float (   comb ( m - 1, ( r - 1 ) // 2 ) \
                  * comb ( n - 1, ( r - 3 ) // 2 ) \
                  + comb ( m - 1, ( r - 3 ) // 2 ) \
                  * comb( n - 1, ( r - 1 ) // 2 ) ) \
        / float (   comb ( m + n, n ) )

  return pdf

def runs_pdf_test ( ):

#*****************************************************************************80
#
## runs_pdf_test() tests runs_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'runs_pdf_test():' )
  print ( '  runs_pdf() evaluates the Runs PDF' )
  print ( '' )
  print ( '  M is the number of symbols of one kind,' )
  print ( '  N is the number of symbols of the other kind,' )
  print ( '  R is the number of runs (sequences of one symbol)' )
  print ( '' )
  print ( '         M         N         R      PDF' )
  print ( '' )

  m = 6

  for n in range ( 0, 9 ):

    print ( '' )
    pdf_total = 0.0

    for r in range ( 1, 2 * min ( m, n ) + 3 ):

      pdf = runs_pdf ( m, n, r )
      print ( '  %8d  %8d  %8d  %14g' % ( m, n, r, pdf ) )
      pdf_total = pdf_total + pdf

    print ( '  %8d                      %14g' % ( m, pdf_total ) )

  return

def runs_sample ( m, n, rng ):

#*****************************************************************************80
#
## runs_sample() samples the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#
#  Output:
#
#    integer R, the number of runs.
#
  a = runs_simulate ( m, n )

  r = i4vec_run_count ( m + n, a )

  return r

def runs_sample_test ( rng ):

#*****************************************************************************80
#
## runs_sample_test() tests runs_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'runs_sample_test():' )
  print ( '  runs_mean() computes the Runs mean' )
  print ( '  runs_sample() samples the Runs distribution.' )
  print ( '  runs_variance() computes the Runs variance' )

  m = 10
  n = 5

  print ( '' )
  print ( '  PDF parameter M = %14g' % ( m ) )
  print ( '  PDF parameter N = %14g' % ( n ) )

  mean = runs_mean ( m, n )
  variance = runs_variance ( m, n )

  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = runs_sample ( m, n, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def runs_simulate ( m, n ):

#*****************************************************************************80
#
## runs_simulate() simulates a case governed by the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#
#  Output:
#
#    integer A(M+N), a sequence of M 0's and N 1's chosen
#    uniformly at random.
#
  import numpy as np

  a = np.zeros ( m + n )

  for i in range ( m, m + n ):
    a[i] = 1

  for i in range ( 0, m + n - 1 ):

    j = rng.integers ( low = i, high = m + n - 1, endpoint = True )

    k    = a[i]
    a[i] = a[j]
    a[j] = k

  return a

def runs_variance ( m, n ):

#*****************************************************************************80
#
## runs_variance() returns the variance of the Runs PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the parameters of the PDF.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = float ( 2 * m * n * ( 2 * m * n - m - n ) ) \
           / float ( ( m + n ) * ( m + n ) * ( m + n - 1 ) )

  return variance

def sech_cdf ( x, a, b ):

#*****************************************************************************80
#
## sech_cdf() evaluates the Hyperbolic Secant CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  y = ( x - a ) / b

  cdf = 2.0 * np.arctan ( np.exp ( y ) ) / np.pi

  return cdf

def sech_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## sech_cdf_inv() inverts the Hyperbolic Secant CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  huge = np.finfo(float).max

  if ( cdf <= 0.0 ):
    x = - huge
  elif ( cdf < 1.0 ):
    x = a + b * np.log ( np.tan ( 0.5 * np.pi * cdf ) )
  elif ( 1.0 <= cdf ):
    x = huge

  return x

def sech_cdf_test ( rng ):

#*****************************************************************************80
#
## sech_cdf_test() tests sech_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'sech_cdf_test():' )
  print ( '  sech_cdf() evaluates the Sech CDF.' )
  print ( '  sech_cdf_inv() inverts the Sech CDF.' )
  print ( '  sech_pdf() evaluates the Sech PDF.' )

  a = 3.0
  b = 2.0

  check = sech_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'sech_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A =         %14g' % ( a ) )
  print ( '  PDF parameter B =         %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = sech_sample ( a, b, rng )

    pdf = sech_pdf ( x, a, b )

    cdf = sech_cdf ( x, a, b )

    x2 = sech_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def sech_check ( a, b ):

#*****************************************************************************80
#
## sech_check() checks the parameters of the Hyperbolic Secant CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'sech_check(): Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def sech_mean ( a, b ):

#*****************************************************************************80
#
## sech_mean() returns the mean of the Hyperbolic Secant PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def sech_pdf ( x, a, b ):

#*****************************************************************************80
#
## sech_pdf() evaluates the Hypebolic Secant PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = sech ( ( X - A ) / B ) / ( PI * B )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  y = ( x - a ) / b

  pdf = 1.0 / np.cosh ( y ) / ( np.pi * b )

  return pdf

def sech_sample ( a, b, rng ):

#*****************************************************************************80
#
## sech_sample() samples the Hyperbolic Secant PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = a + b * np.log ( np.tan ( 0.5 * np.pi * cdf ) )

  return x

def sech_sample_test ( rng ):

#*****************************************************************************80
#
## sech_sample_test() tests sech_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  nsample = 1000

  print ( '' )
  print ( 'sech_sample_test():' )
  print ( '  sech_mean() computes the Sech mean' )
  print ( '  sech_sample() samples the Sech distribution' )
  print ( '  sech_variance() computes the Sech variance.' )

  a = 3.0
  b = 2.0

  check = sech_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'sech_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = sech_mean ( a, b )
  variance = sech_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = sech_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def sech_variance ( a, b ):

#*****************************************************************************80
#
## sech_variance() returns the variance of the Hyperbolic Secant PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = 0.25 * np.pi * np.pi * b * b

  return variance

def semicircular_cdf ( x, a, b ):

#*****************************************************************************80
#
## semicircular_cdf() evaluates the Semicircular CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= a - b ):

    cdf = 0.0

  elif ( x <= a + b ):

    y = ( x - a ) / b

    cdf = 0.5 + ( y * np.sqrt ( 1.0 - y * y ) + np.arcsin ( y ) ) / np.pi

  elif ( a + b < x ):

    cdf = 1.0

  return cdf

def semicircular_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## semicircular_cdf_inv() inverts the Semicircular CDF.
#
#  Discussion:
#
#    A simple bisection method is used on the interval [ A - B, A + B ].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a - b
    return x
  elif ( 1.0 <= cdf ):
    x = a + b
    return x

  x1 = a - b
  cdf1 = 0.0

  x2 = a + b
  cdf2 = 1.0
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = semicircular_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'semicircular_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'semicircular_cdf_inv(): Fatal error!' )

    if ( ( cdf <= cdf3 and cdf <= cdf1 ) or ( cdf3 <= cdf and cdf1 <= cdf ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def semicircular_cdf_test ( rng ):

#*****************************************************************************80
#
## semicircular_cdf_test() tests semicircular_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'semicircular_cdf_test():' )
  print ( '  semicircular_cdf() evaluates the Semicircular CDF.' )
  print ( '  semicircular_cdf_inv() inverts the Semicircular CDF.' )
  print ( '  semicircular_pdf() evaluates the Semicircular PDF.' )

  a = 3.0
  b = 2.0

  check = semicircular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'semicircular_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =         %14g' % ( a ) )
  print ( '  PDF parameter B =         %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = semicircular_sample ( a, b, rng )

    pdf = semicircular_pdf ( x, a, b )

    cdf = semicircular_cdf ( x, a, b )

    x2 = semicircular_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def semicircular_check ( a, b ):

#*****************************************************************************80
#
## semicircular_check() checks the parameters of the Semicircular CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameter of the PDF.
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'semicircular_check(): Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def semicircular_mean ( a, b ):

#*****************************************************************************80
#
## semicircular_mean() returns the mean of the Semicircular PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def semicircular_pdf ( x, a, b ):

#*****************************************************************************80
#
## semicircular_pdf() evaluates the Semicircular PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = ( 2 / ( B * PI ) ) * SQRT ( 1 - ( ( X - A ) / B )^2 )
#    for A - B <= X <= A + B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a - b ):

    pdf = 0.0

  elif ( x <= a + b ):

    y = ( x - a ) / b

    pdf = 2.0 / ( b * np.pi ) * np.sqrt ( 1.0 - y * y )

  elif ( a + b < x ):

    pdf = 0.0

  return pdf

def semicircular_sample ( a, b, rng ):

#*****************************************************************************80
#
## semicircular_sample() samples the Semicircular PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  radius = rng.random ( )
  radius = b * np.sqrt ( radius )
  angle = rng.random ( )
  x = a + radius * np.cos ( np.pi * angle )

  return x

def semicircular_sample_test ( rng ):

#*****************************************************************************80
#
## semicircular_sample_test() tests semicircular_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'semicircular_sample_test():' )
  print ( '  semicircular_mean() computes the Semicircular mean' )
  print ( '  semicircular_sample() samples the Semicircular distribution' )
  print ( '  semicircular_variance() computes the Semicircular variance.' )

  a = 3.0
  b = 2.0

  check = semicircular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'semicircular_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = semicircular_mean ( a, b )
  variance = semicircular_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = semicircular_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def semicircular_variance ( a, b ):

#*****************************************************************************80
#
## semicircular_variance() returns the variance of the Semicircular PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = b * b / 4.0

  return variance

def sin_power_int ( a, b, n ):

#*****************************************************************************80
#
## sin_power_int() evaluates the sine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      sin_power_int(A,B,N) = Integral ( A <= T <= B ) ( sin ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral sin^n ( t ) = (1/n) * (
#        sin^(n-1)(t) * cos(t) + ( n-1 ) * Integral sin^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of integration.
#
#    integer N, the power of the sine function.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'sin_power_int(): Fatal error!' )
    print ( '  Power N < 0.' )
    raise Exception ( 'sin_power_int(): Fatal error!' )

  sa = np.sin ( a );
  sb = np.sin ( b );
  ca = np.cos ( a );
  cb = np.cos ( b );

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = ca - cb
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value \
            + sa ** ( m - 1 ) * ca \
            - sb ** ( m - 1 ) * cb ) / float ( m )

  return value

def sin_power_int_test ( ):

#*****************************************************************************80
#
## sin_power_int_test() tests sin_power_int().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'sin_power_int_test():' )
  print ( '  sin_power_int() returns values of' )
  print ( '  the integral of SIN(X)^N from A to B.' )
  print ( '' )
  print ( '      A         B          N      Exact           Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, fx = sin_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = sin_power_int ( a, b, n )

    print ( '  %8f  %8f  %6d  %14e  %14e' % ( a, b, n, fx, fx2 ) )

  return

def sin_power_int_values ( n_data ):

#*****************************************************************************80
#
## sin_power_int_values() returns some values of the sine power integral.
#
#  Discussion:
#
#    The function has the form
#
#      sin_power_int(A,B,N) = Integral ( A <= T <= B ) ( sin(T) )^N dt
#
#    In Mathematica, the function can be evaluated by:
#
#      Integrate [ ( Sin[x] )^n, { x, a, b } ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real A, B, the limits of integration.
#
#    integer N, the power.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  a_vec = np.array ( ( \
      0.10E+02, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.10E+01, \
      0.00E+00, \
      0.00E+00 ))

  b_vec = np.array ( ( \
      0.20E+02, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.20E+01, \
      0.20E+01, \
      0.10E+01, \
      0.10E+01 ))

  f_vec = np.array ( ( \
     0.10000000000000000000E+02, \
     0.45969769413186028260E+00, \
     0.27267564329357957615E+00, \
     0.17894056254885809051E+00, \
     0.12402556531520681830E+00, \
     0.88974396451575946519E-01, \
     0.90393123848149944133E+00, \
     0.81495684202992349481E+00, \
     0.21887522421729849008E-01, \
     0.17023439374069324596E-01 ))

  n_vec = np.array ( ( \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     5, \
     5, \
    10, \
    11 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    f = 0.0
    n = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n = n_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, n, f

def sin_power_int_values_test ( ):

#*****************************************************************************80
#
## sin_power_int_values_test() tests sin_power_int_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'sin_power_int_values_test():' )
  print ( '  sin_power_int_values() stores values of the sine power integral.' )
  print ( '' )
  print ( '        A             B            N           F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, f = sin_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %6d  %24.16g' % ( a, b, n, f ) )

  return

def stirling2_number ( n, k ):

#*****************************************************************************80
#
## stirling2_number() computes a Stirling number S2(N,K) of the second kind.
#
#  Discussion:
#
#    S2(N,K) represents the number of distinct partitions of N elements
#    into K nonempty sets.  For a fixed N, the sum of the Stirling
#    numbers S2(N,K) is represented by B(N), called "Bell's number",
#    and represents the number of distinct partitions of N elements.
#
#    For example, with 4 objects, there are:
#
#    1 partition into 1 set:
#
#      (A,B,C,D)
#
#    7 partitions into 2 sets:
#
#      (A,B,C) (D)
#      (A,B,D) (C)
#      (A,C,D) (B)
#      (A) (B,C,D)
#      (A,B) (C,D)
#      (A,C) (B,D)
#      (A,D) (B,C)
#
#    6 partitions into 3 sets:
#
#      (A,B) (C) (D)
#      (A) (B,C) (D)
#      (A) (B) (C,D)
#      (A,C) (B) (D)
#      (A,D) (B) (C)
#      (A) (B,D) (C)
#
#    1 partition into 4 sets:
#
#      (A) (B) (C) (D)
#
#    So S2(4,1) = 1, S2(4,2) = 7, S2(4,3) = 6, S2(4,4) = 1, and B(4) = 15.
#
#  First terms:
#
#    N/K: 1    2    3    4    5    6    7    8
#
#    1    1    0    0    0    0    0    0    0
#    2    1    1    0    0    0    0    0    0
#    3    1    3    1    0    0    0    0    0
#    4    1    7    6    1    0    0    0    0
#    5    1   15   25   10    1    0    0    0
#    6    1   31   90   65   15    1    0    0
#    7    1   63  301  350  140   21    1    0
#    8    1  127  966 1701 1050  266   28    1
#
#  Recursion:
#
#    S2(N,1) = 1 for all N.
#    S2(I,I) = 1 for all I.
#    S2(I,J) = 0 if I < J.
#
#    S2(N,K) = K * S2(N-1,K) + S2(N-1,K-1)
#
#  Direct Formula:
#
#    s2(n,k) = 1/k! sum ( 0 <= i <= k ) (-1)^i k-choose-i ( k - i )^n
#
#  Properties:
#
#    sum ( 1 <= K <= M ) S2(I,K) * S1(K,J) = Delta(I,J)
#
#    X^N = sum ( 0 <= K <= N ) S2(N,K) X_K
#    where X_K is the falling factorial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows of the table.
#
#    integer K, the number of columns of the table.
#
#  Output:
#
#    integer S2, the Stirling number of the second kind.
#
  import math
  import numpy as np

  s2 = 0
  for i in range ( 0, k + 1 ):
    s2 = s2 + ( -1 ) ** i * i4_choose ( k, i ) * ( k - i ) ** n

  s2 = s2 / math.factorial ( k )

  return s2

def stirling2_number_test ( ):

#*****************************************************************************80
#
## stirling2_number_test() tests stirling2_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'stirling2_number_test():' )
  print ( '  stirling2_number() calculates a Stirling number S2(n,k)' )
  print ( '  of the second kind.' )
  print ( '' )

  for n in range ( 0, 9 ):
    for k in range ( 0, 9 ):
      s2 = stirling2_number ( n, k )
      print ( '%6d' % ( s2 ), end = '' )
    print ( '' )

  return

def student_noncentral_cdf ( x, idf, d ):

#*****************************************************************************80
#
## student_noncentral_cdf() evaluates the noncentral Student T CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Algorithm AS 5,
#    Applied Statistics,
#    Volume 17, 1968, page 193.
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    integer IDF, the number of degrees of freedom.
#
#    real D, the noncentrality parameter.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np
  from scipy.special import gammaln

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

    a = np.sqrt ( 0.5 * f ) * np.exp ( gammaln ( 0.5 * ( f - 1.0 ) ) \
      - gammaln ( 0.5 * f ) ) * d

    temp = ( x - a ) / np.sqrt ( f * ( 1.0 + d * d ) / ( f - 2.0 ) - a * a )

    cdf2 = normal_01_cdf ( temp )
    cdf = cdf2r8_

  return cdf

def student_noncentral_cdf_test ( rng ):

#*****************************************************************************80
#
## student_noncentral_cdf_test() tests student_noncentral_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'student_noncentral_cdf_test():' )
  print ( '  student_noncentral_cdf() evaluates the Student Noncentral CDF' )

  x = 0.50

  idf = 10
  b = 1.0

  cdf = student_noncentral_cdf ( x, idf, b )

  print ( '' )
  print ( '  PDF argument X =              %14g' % ( x ) )
  print ( '  PDF parameter IDF =           %6d' % ( idf ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  CDF value =                   %14g' % ( cdf ) )

  return

def student_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## student_cdf() evaluates the central Student T CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  y = ( x - a ) / b

  a2 = 0.5 * c
  b2 = 0.5
  c2 = c / ( c + y * y )

  if ( y <= 0.0 ):
    cdf = 0.5 * beta_inc ( a2, b2, c2 )
  else:
    cdf = 1.0 - 0.5 * beta_inc ( a2, b2, c2 )

  return cdf

def student_cdf_test ( rng ):

#*****************************************************************************80
#
## student_cdf_test() tests student_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'student_cdf_test():' )
  print ( '  student_cdf() evaluates the Student CDF.' )
  print ( '  student_pdf() evaluates the Student PDF.' )

  x = 2.447

  a = 0.5
  b = 2.0
  c = 6.0

  check = student_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'student_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  pdf = student_pdf ( x, a, b, c )

  cdf = student_cdf ( x, a, b, c )

  print ( '' )
  print ( '  PDF argument X =    %14g' % ( x ) )
  print ( '  PDF parameter A =   %14g' % ( a ) )
  print ( '  PDF parameter B =   %14g' % ( b ) )
  print ( '  PDF parameter C =   %14g' % ( c ) )
  print ( '  PDF value =         %14g' % ( pdf ) )
  print ( '  CDF value =         %14g' % ( cdf ) )

  return

def student_check ( a, b, c ):

#*****************************************************************************80
#
## student_check() checks the parameter of the central Student T CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b == 0.0 ):
    print ( '' )
    print ( 'student_check(): Fatal error!' )
    print ( '  B must be nonzero.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'student_check(): Fatal error!' )
    print ( '  C must be greater than 0.' )
    check = False

  return check

def student_mean ( a, b, c ):

#*****************************************************************************80
#
## student_mean() returns the mean of the central Student T PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def student_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## student_pdf() evaluates the central Student T PDF.
#
#  Formula:
#
#    PDF(X)(A,B,C) = Gamma ( (C+1)/2 ) /
#      ( Gamma ( C / 2 ) * Sqrt ( PI * C )
#      * ( 1 + ((X-A)/B)^2/C )^(C + 1/2 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy.special import gamma

  y = ( x - a ) / b

  pdf = gamma ( 0.5 * ( c + 1.0 ) ) / ( np.sqrt ( np.pi * c ) \
    * gamma ( 0.5 * c ) * np.sqrt ( ( 1.0 + y * y / c ) \
    ** ( 2 * c + 1.0 ) ) )

  return pdf

def student_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## student_sample() samples the central Student T PDF.
#
#  Discussion:
#
#    For the sampling algorithm, it is necessary that 2 < C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.  
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  if ( c <= 2.0 ):
    print ( '' )
    print ( 'student_sample(): Fatal error!' )
    print ( '  Sampling fails for C <= 2.' )
    raise Exception ( 'student_sample(): Fatal error!' )

  a2 = 0.0
  b2 = c / ( c - 2.0 )

  x2 = normal_sample ( a2, b2, rng )

  a3 = c
  x3 = chi_square_sample ( a3, rng )
  x3 = x3 * c / ( c - 2.0 )

  x = a + b * x2 * np.sqrt ( c ) / x3

  return x

def student_sample_test ( rng ):

#*****************************************************************************80
#
## student_sample_test() tests student_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'student_sample_test():' )
  print ( '  student_mean() computes the Student mean' )
  print ( '  student_sample() samples the Student distribution' )
  print ( '  student_variance() computes the Student variance.' )

  a = 0.5
  b = 2.0
  c = 6.0

  check = student_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'student_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = student_mean ( a, b, c )
  variance = student_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = student_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def student_variance ( a, b, c ):

#*****************************************************************************80
#
## student_variance() returns the variance of the central Student T PDF.
#
#  Discussion:
#
#    For the variance to exist, it is necessary that 2 < C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.  
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  if ( c <= 2.0 ):
    print ( '' )
    print ( 'student_variance(): Fatal error!' )
    print ( '  Variance not defined for C <= 2.' )
    raise Exception ( 'student_variance(): Fatal error!' )

  variance = b * b * c / ( c - 2.0 )

  return variance

def tfn ( h, a ):

#*****************************************************************************80
#
## tfn() calculates the T function of Owen.
#
#  Discussion:
#
#    Owen's T function is useful for computation of the bivariate normal
#    distribution and the distribution of a skewed normal distribution.
#
#    Although it was originally formulated in terms of the bivariate
#    normal function, the function can be defined more directly as
#
#      T(H,A) = 1 / ( 2 * pi ) * 
#        Integral ( 0 <= X <= A ) e^( -H^2 * (1+X^2) / 2) / (1+X^2) dX
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    This version by John Burkardt
#
#  Reference:
#
#    D B Owen,
#    Tables for computing the bivariate normal distribution,
#    Annals of Mathematical Statistics,
#    Volume 27, pages 1075-1090, 1956.
#
#    J C Young and C E Minder,
#    Algorithm AS 76,
#    An Algorithm Useful in Calculating Non-Central T and 
#    Bivariate Normal Distributions,
#    Applied Statistics,
#    Volume 23, Number 3, 1974, pages 455-457.
#
#  Input:
#
#    real H, A, the arguments of the T function.
#
#  Output:
#
#    real VALUE, the value of the T function.
#
  import numpy as np

  ngauss = 10

  two_pi_inverse = 0.1591549430918953
  tv1 = 1.0E-35
  tv2 = 15.0
  tv3 = 15.0
  tv4 = 1.0E-05

  weight = np.array ( [ \
    0.666713443086881375935688098933E-01, \
    0.149451349150580593145776339658E+00, \
    0.219086362515982043995534934228E+00, \
    0.269266719309996355091226921569E+00, \
    0.295524224714752870173892994651E+00, \
    0.295524224714752870173892994651E+00, \
    0.269266719309996355091226921569E+00, \
    0.219086362515982043995534934228E+00, \
    0.149451349150580593145776339658E+00, \
    0.666713443086881375935688098933E-01 ] )

  xtab = np.array ( [ \
   -0.973906528517171720077964012084E+00, \
   -0.865063366688984510732096688423E+00, \
   -0.679409568299024406234327365115E+00, \
   -0.433395394129247190799265943166E+00, \
   -0.148874338981631210884826001130E+00, \
    0.148874338981631210884826001130E+00, \
    0.433395394129247190799265943166E+00, \
    0.679409568299024406234327365115E+00, \
    0.865063366688984510732096688423E+00, \
    0.973906528517171720077964012084E+00 ] )
#
#  Test for H near zero.
#
  if ( abs ( h ) < tv1 ):
    value = np.arctan ( a ) * two_pi_inverse
#
#  Test for large values of abs(H).
#
  elif ( tv2 < abs ( h ) ):
    value = 0.0
#
#  Test for A near zero.
#
  elif ( abs ( a ) < tv1 ):
    value = 0.0
#
#  Test whether abs(A) is so large that it must be truncated.
#  If so, the truncated value of A is H2.
#
  else:

    hs = - 0.5 * h * h
    h2 = a
    asq = a * a
#
#  Computation of truncation point by Newton iteration.
#
    if ( tv3 <= np.log ( 1.0 + asq ) - hs * asq ):

      h1 = 0.5 * a
      asq = 0.25 * asq

      while ( True ):

        rt = asq + 1.0
        h2 = h1 + ( hs * asq + tv3 - np.log ( rt ) ) / ( 2.0 * h1 * ( 1.0 / rt - hs ) )
        asq = h2 * h2

        if ( abs ( h2 - h1 ) < tv4 ):
          break

        h1 = h2
#
#  Gaussian quadrature on the interval [0,H2].
#
    rt = 0.0
    for i in range ( 0, ngauss ):
      x = 0.5 * h2 * ( xtab[i] + 1.0 )
      rt = rt + weight[i] * np.exp ( hs * ( 1.0 + x * x ) ) / ( 1.0 + x * x )

    value = rt * ( 0.5 * h2 ) * two_pi_inverse

  return value

def tfn_test ( ):

#*****************************************************************************80
#
## tfn_test() tests tfn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'tfn_test():' )
  print ( '  tfn() evaluates Owen\'s T function.' )
  print ( '' )
  print ( '      H             A           T(H,A)       Exact' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, h, a, t = owen_values ( n_data )

    if ( n_data <= 0 ):
      break

    t2 = tfn ( h, a )

    print ( '  %14g  %14g  %14g  %14g' % ( h, a, t2, t ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def triangle_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## triangle_cdf() evaluates the Triangle CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= a ):

    cdf = 0.0

  elif ( x <= b ):

    if ( a == b ):
      cdf = 0.0
    else:
      cdf = ( x - a ) * ( x - a ) / ( b - a ) / ( c - a )

  elif ( x <= c ):

    cdf = ( b - a ) / ( c - a ) \
      + ( 2.0 * c - b - x ) * ( x - b ) / ( c - b ) / ( c - a )

  else:

    cdf = 1.0

  return cdf

def triangle_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## triangle_cdf_inv() inverts the Triangle CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'triangle_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'triangle_cdf_inv(): Fatal error!' )

  d = 2.0 / ( c - a )
  cdf_mid = 0.5 * d * ( b - a )

  if ( cdf <= cdf_mid ):
    x = a + np.sqrt ( cdf * ( b - a ) * ( c - a ) )
  else:
    x = c - np.sqrt ( ( c - b ) * ( ( c - b ) - ( cdf - cdf_mid ) * ( c - a ) ) )

  return x

def triangle_cdf_test ( rng ):

#*****************************************************************************80
#
## triangle_cdf_test() tests triangle_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'triangle_cdf_test():' )
  print ( '  triangle_cdf() evaluates the Triangle CDF' )
  print ( '  triangle_cdf_inv() inverts the Triangle CDF.' )
  print ( '  triangle_pdf() evaluates the Triangle PDF' )

  a = 1.0
  b = 3.0
  c = 10.0

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )
  print ( '  PDF parameter C =      %14g' % ( c ) )

  check = triangle_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'triangle_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = triangle_sample ( a, b, c, rng )

    pdf = triangle_pdf ( x, a, b, c )

    cdf = triangle_cdf ( x, a, b, c )

    x2 = triangle_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def triangle_check ( a, b, c ):

#*****************************************************************************80
#
## triangle_check() checks the parameters of the Triangle CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b < a ):
    print ( '' )
    print ( 'triangle_check(): Fatal error!' )
    print ( '  B < A.' )
    check = False

  if ( c < b ):
    print ( '' )
    print ( 'triangle_check(): Fatal error!' )
    print ( '  C < B.' )
    check = False

  if ( a == c ):
    print ( '' )
    print ( 'triangle_check(): Fatal error!' )
    print ( '  A == C.' )
    check = False

  return check

def triangle_mean ( a, b, c ):

#*****************************************************************************80
#
## triangle_mean() returns the mean of the Triangle PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    real MEAN, the mean of the discrete uniform PDF.
#
  mean = a + ( c + b - 2.0 * a ) / 3.0

  return mean

def triangle_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## triangle_pdf() evaluates the Triangle PDF.
#
#  Discussion:
#
#    Given points A <= B <= C, the probability is 0 to the left of A,
#    rises linearly to a maximum of 2/(C-A) at B, drops linearly to zero
#    at C, and is zero for all values greater than C.
#
#  Formula:
#
#    PDF(A,B,CX)
#      = 2 * ( X - A ) / ( B - A ) / ( C - A ) for A <= X <= B
#      = 2 * ( C - X ) / ( C - B ) / ( C - A ) for B <= X <= C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x <= a ):

    pdf = 0.0

  elif ( x <= b ):

    if ( a == b ):
      pdf = 0.0
    else:
      pdf = 2.0 * ( x - a ) / ( b - a ) / ( c - a )

  elif ( x <= c ):

    if ( b == c ):
      pdf = 0.0
    else:
      pdf = 2.0 * ( c - x ) / ( c - b ) / ( c - a )

  else:
    pdf = 0.0

  return pdf

def triangle_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## triangle_sample() samples the Triangle PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = triangle_cdf_inv ( cdf, a, b, c )

  return x

def triangle_sample_test ( rng ):

#*****************************************************************************80
#
## triangle_sample_test() tests triangle_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'triangle_sample_test():' )
  print ( '  triangle_mean() returns the Triangle mean' )
  print ( '  triangle_sample samples the Triangle distribution' )
  print ( '  triangle_variance returns the Triangle variance' )

  a = 1.0
  b = 3.0
  c = 10.0

  check = triangle_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'triangle_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )

  mean = triangle_mean ( a, b, c )
  variance = triangle_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter MEAN =          %14g' % ( mean ) )
  print ( '  PDF parameter VARIANCE =      %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = triangle_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def triangle_variance ( a, b, c ):

#*****************************************************************************80
#
## triangle_variance() returns the variance of the Triangle PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( ( c - a ) * ( c - a ) \
             - ( c - a ) * ( b - a ) \
             + ( b - a ) * ( b - a ) ) / 18.0

  return variance

def triangular_cdf ( x, a, b ):

#*****************************************************************************80
#
## triangular_cdf() evaluates the Triangular CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x <= a ):
    cdf = 0.0
  elif ( x <= 0.5 * ( a + b ) ):
    cdf = 2.0 * ( x * x - 2.0 * a * x + a * a ) / ( b - a ) ** 2
  elif ( x <= b ):
    cdf = 0.5 + ( - 2.0 * x * x + 4.0 * b * x + 0.5 * a * a \
      - a * b - 1.5 * b * b ) / ( b - a ) ** 2
  else:
    cdf = 1.0

  return cdf

def triangular_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## triangular_cdf_inv() inverts the Triangular CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'triangular_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'triangular_cdf_inv(): Fatal error!' )

  if ( cdf <= 0.5 ):
    x = a + 0.5 * ( b - a ) * np.sqrt ( 2.0 * cdf )
  else:
    x = b - 0.5 * ( b - a ) * np.sqrt ( 2.0 * ( 1.0 - cdf ) )

  return x

def triangular_cdf_test ( rng ):

#*****************************************************************************80
#
## triangular_cdf_test() tests triangular_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'triangular_cdf_test():' )
  print ( '  triangular_cdf() evaluates the Triangular CDF' )
  print ( '  triangular_cdf_inv() inverts the Triangular CDF.' )
  print ( '  triangular_pdf() evaluates the Triangular PDF' )

  a = 1.0
  b = 10.0

  check = triangular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'triangular_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = triangular_sample ( a, b, rng )

    pdf = triangular_pdf ( x, a, b )

    cdf = triangular_cdf ( x, a, b )

    x2 = triangular_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def triangular_check ( a, b ):

#*****************************************************************************80
#
## triangular_check() checks the parameters of the Triangular CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= a ):
    print ( '' )
    print ( 'triangular_check(): Fatal error!' )
    print ( '  B <= A.' )
    check = False

  return check

def triangular_mean ( a, b ):

#*****************************************************************************80
#
## triangular_mean() returns the mean of the Triangular PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.5 * ( a + b )

  return mean

def triangular_pdf ( x, a, b ):

#*****************************************************************************80
#
## triangular_pdf() evaluates the Triangular PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 4 * ( X - A ) / ( B - A )^2 for  A <= X <= (A+B)/2
#                = 4 * ( B - X ) / ( B - A )^2 for  (A+B)/2 <= X <= B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x <= a ):
    pdf = 0.0
  elif ( x <= 0.5 * ( a + b ) ):
    pdf = 4.0 * ( x - a ) / ( b - a ) ** 2
  elif ( x <= b ):
    pdf = 4.0 * ( b - x ) / ( b - a ) ** 2
  else:
    pdf = 0.0

  return pdf

def triangular_sample ( a, b, rng ):

#*****************************************************************************80
#
## triangular_sample() samples the Triangular PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = triangular_cdf_inv ( cdf, a, b )

  return x

def triangular_sample_test ( rng ):

#*****************************************************************************80
#
## triangular_sample_test() tests triangular_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'triangular_sample_test():' )
  print ( '  triangular_mean() computes the Triangular mean' )
  print ( '  triangular_sample() samples the Triangular distribution' )
  print ( '  triangular_variance() computes the Triangular variance.' )

  a = 1.0
  b = 10.0

  check = triangular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'triangular_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = triangular_mean ( a, b )
  variance = triangular_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i] = triangular_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def triangular_variance ( a, b ):

#*****************************************************************************80
#
## triangular_variance() returns the variance of the Triangular PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( b - a ) ** 2 / 24.0

  return variance

def trigamma ( x ):

#*****************************************************************************80
#
## trigamma() calculates trigamma(x) = d^2 log(Gamma(x)) / dx^2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    B Schneider,
#    trigamma Function,
#    Algorithm AS 121,
#    Applied Statistics,
#    Volume 27, Number 1, page 97-99, 1978.
#
#  Input:
#
#    X, the argument of the trigamma function.
#    0 < X.
#
#  Output:
#
#    real VALUE, the value of the trigamma function at X.
#
  a = 0.0001
  b = 5.0
  b2 =  1.0 / 6.0
  b4 = -1.0 / 30.0
  b6 =  1.0 / 42.0
  b8 = -1.0 / 30.0
#
#  1): If X is not positive, fail.
#
  if ( x <= 0.0 ):

    value = 0.0
    print ( '' )
    print ( 'trigamma(): Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'trigamma(): Fatal error!' )
#
#  2): If X is smaller than A, use a small value approximation.
#
  elif ( x <= a ):

    value = 1.0 / x ** 2
#
#  3): Otherwise, increase the argument to B <= ( X + I ).
#
  else:

    z = x
    value = 0.0

    while ( z < b ):
      value = value + 1.0 / z ** 2
      z = z + 1.0
#
#  ...and then apply an asymptotic formula.
#
    y = 1.0 / z ** 2

    value = value + 0.5 * \
            y + ( 1.0 \
          + y * ( b2 \
          + y * ( b4 \
          + y * ( b6 \
          + y *   b8 )))) / z

  return value

def trigamma_test ( ):

#*****************************************************************************80
#
## trigamma_test() tests trigamma().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'trigamma_test():' )
  print ( '  trigamma() evaluates the trigamma function.' )
  print ( '' )
  print ( '      X               FX               FX' )
  print ( '                      Tabulated        Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = trigamma_values ( n_data )

    if ( n_data == 0 ):
      break
 
    fx2 = trigamma ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def trigamma_values ( n_data ):

#*****************************************************************************80
#
## trigamma_values() returns some values of the trigamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[1,x]
#
#    trigamma(X) = d^2 ln ( Gamma ( X ) ) / d X^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 11

  f_vec = np.array ( ( \
     0.1644934066848226E+01, \
     0.1433299150792759E+01, \
     0.1267377205423779E+01, \
     0.1134253434996619E+01, \
     0.1025356590529597E+01, \
     0.9348022005446793E+00, \
     0.8584318931245799E+00, \
     0.7932328301639984E+00, \
     0.7369741375017002E+00, \
     0.6879720582426356E+00, \
     0.6449340668482264E+00 ))

  x_vec = np.array ( ( \
    1.0E+00, \
    1.1E+00, \
    1.2E+00, \
    1.3E+00, \
    1.4E+00, \
    1.5E+00, \
    1.6E+00, \
    1.7E+00, \
    1.8E+00, \
    1.9E+00, \
    2.0E+00 ))

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

def trigamma_values_test ( ):

#*****************************************************************************80
#
## trigamma_values_test() tests trigamma_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'trigamma_values_test():' )
  print ( '  trigamma_values() stores values of the trigamma function.' )
  print ( '' )
  print ( '      X         trigamma(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = trigamma_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def uniform_01_order_sample ( n, rng ):

#*****************************************************************************80
#
## uniform_01_order_sample() samples the Uniform 01 Order PDF.
#
#  Discussion:
#
#    In effect, this routine simply generates N samples of the
#    Uniform 01 PDF but it generates them in order.  (Actually,
#    it generates them in descending order, but stores them in
#    the array in ascending order).  This saves the work of
#    sorting the results.  Moreover, if the order statistics
#    for another PDF are desired, and the inverse CDF is available,
#    then the desired values may be generated, presorted, by
#    calling this routine and using the results as input to the
#    inverse CDF routine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 168.
#
#  Input:
#
#    integer N, the number of elements in the sample.
#
#  Output:
#
#    real X(N), N samples of the Uniform 01 PDF, in
#    ascending order.
#
  import numpy as np

  x = np.zeros ( n )
  v = 1.0

  for i in range ( n - 1, -1, -1 ):
    u = rng.random ( )
    v = v * u ** ( 1.0 / float ( i + 1  ) )
    x[i] = v

  return x

def uniform_01_order_sample_test ( rng ):

#*****************************************************************************80
#
## uniform_01_order_sample_test() tests uniform_01_order_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  n = 10

  print ( '' )
  print ( 'uniform_01_order_sample_test():' )
  print ( '  uniform_order_sample() samples the Uniform 01 Order distribution.' )

  x = uniform_01_order_sample ( n, rng )

  r8vec_print ( n, x, '  Ordered sample:' )

  return

def uniform_01_cdf ( x ):

#*****************************************************************************80
#
## uniform_01_cdf() evaluates the Uniform 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 0.0 ):
    cdf = 0.0
  elif ( 1.0 < x ):
    cdf = 1.0
  else:
    cdf = x

  return cdf

def uniform_01_cdf_inv ( cdf ):

#*****************************************************************************80
#
## uniform_01_cdf_inv() inverts the Uniform 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'uniform_01_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'uniform_01_cdf_inv(): Fatal error!' )

  x = cdf

  return x

def uniform_01_cdf_test ( rng ):

#*****************************************************************************80
#
## uniform_01_cdf_test() tests uniform_01_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'uniform_01_cdf_test():' )
  print ( '  uniform_01_cdf() evaluates the Uniform 01 CDF' )
  print ( '  uniform_01_cdf_inv() inverts the Uniform 01 CDF.' )
  print ( '  uniform_01_pdf() evaluates the Uniform 01 PDF' )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = uniform_01_sample ( rng )

    pdf = uniform_01_pdf ( x )

    cdf = uniform_01_cdf ( x )

    x2 = uniform_01_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def uniform_01_mean ( ):

#*****************************************************************************80
#
## uniform_01_mean() returns the mean of the Uniform 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MEAN, the mean of the discrete uniform PDF.
#
  mean = 0.5

  return mean

def uniform_01_pdf ( x ):

#*****************************************************************************80
#
## uniform_01_pdf() evaluates the Uniform 01 PDF.
#
#  Formula:
#
#    PDF(X) = 1 for 0 <= X <= 1
#           = 0 otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    0.0 <= X <= 1.0.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0.0 or 1.0 < x ):
    pdf = 0.0
  else:
    pdf = 1.0

  return pdf

def uniform_01_sample ( rng ):

#*****************************************************************************80
#
## uniform_01_sample() is a portable random number generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Output:
#
#    real VALUE, a random value between 0 and 1.
#
  import numpy as np

  value = rng.random ( )

  return value

def uniform_01_sample_test ( rng ):

#*****************************************************************************80
#
## uniform_01_sample_test() tests uniform_01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'uniform_01_sample_test():' )
  print ( '  uniform_01_mean() computes the Uniform 01 mean' )
  print ( '  uniform_01_sample() samples the Uniform 01 distribution' )
  print ( '  uniform_01_variance() computes the Uniform 01 variance.' )

  mean = uniform_01_mean ( )
  variance = uniform_01_variance ( )

  print ( '' )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = uniform_01_sample ( rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def uniform_01_variance ( ):

#*****************************************************************************80
#
## uniform_01_variance() returns the variance of the Uniform 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = 1.0 / 12.0

  return variance

def uniform_discrete_cdf ( x, a, b ):

#*****************************************************************************80
#
## uniform_discrete_cdf() evaluates the Uniform Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the CDF.
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < a ):
    cdf = 0.0
  elif ( b < x ):
    cdf = 1.0
  else:
    cdf = ( x + 1 - a ) / ( b + 1 - a )

  return cdf

def uniform_discrete_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## uniform_discrete_cdf_inv() inverts the Uniform Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    integer X, the smallest argument whose CDF is greater
#    than or equal to CDF.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'uniform_discrete_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'uniform_discrete_cdf_inv(): Fatal error!' )

  a2 = a - 0.5
  b2 = b + 0.5
  x2 = a + cdf * ( b2 - a2 )

  x = int ( x2 )

  x = max ( x, a )
  x = min ( x, b )

  return x

def uniform_discrete_cdf_test ( rng ):

#*****************************************************************************80
#
## uniform_discrete_cdf_test() tests uniform_discrete_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'uniform_discrete_cdf_test():' )
  print ( '  uniform_discrete_cdf() evaluates the Uniform Discrete CDF' )
  print ( '  uniform_discrete_cdf_inv() inverts the Uniform Discrete CDF.' )
  print ( '  uniform_discrete_pdf() evaluates the Uniform Discrete PDF' )

  a = 1
  b = 6

  check = uniform_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'uniform_discrete_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %6d' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = uniform_discrete_sample ( a, b, rng )

    pdf = uniform_discrete_pdf ( x, a, b )

    cdf = uniform_discrete_cdf ( x, a, b )

    x2 = uniform_discrete_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def uniform_discrete_check ( a, b ):

#*****************************************************************************80
#
## uniform_discrete_check() checks the parameters of the Uniform discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b < a ):
    print ( '' )
    print ( 'uniform_discrete_check(): Fatal error!' )
    print ( '  B < A.' )
    check = False

  return check

def uniform_discrete_mean ( a, b ):

#*****************************************************************************80
#
## uniform_discrete_mean() returns the mean of the Uniform discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = 0.5 * ( a + b )

  return mean

def uniform_discrete_pdf ( x, a, b ):

#*****************************************************************************80
#
## uniform_discrete_pdf() evaluates the Uniform discrete PDF.
#
#  Discussion:
#
#    The Uniform Discrete PDF is also known as the "Rectangular"
#    Discrete PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 1 / ( B + 1 - A ) for A <= X <= B.
#
#    The parameters define the interval of integers
#    for which the PDF is nonzero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < a or b < x ):
    pdf = 0.0
  else:
    pdf = 1.0 / ( b + 1 - a )

  return pdf

def uniform_discrete_sample ( a, b, rng ):

#*****************************************************************************80
#
## uniform_discrete_sample() samples the Uniform discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = uniform_discrete_cdf_inv ( cdf, a, b )

  return x

def uniform_discrete_sample_test ( rng ):

#*****************************************************************************80
#
## uniform_discrete_sample_test() tests uniform_discrete_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'uniform_discrete_sample_test():' )
  print ( '  uniform_discrete_mean() computes the Uniform Discrete mean' )
  print ( '  uniform_discrete_sample() samples the Uniform Discrete distribution' )
  print ( '  uniform_discrete_variance() computes the Uniform Discrete variance.' )

  a = 1
  b = 6

  check = uniform_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'uniform_discrete_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = uniform_discrete_mean ( a, b )
  variance = uniform_discrete_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %6d' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = uniform_discrete_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def uniform_discrete_variance ( a, b ):

#*****************************************************************************80
#
## uniform_discrete_variance() returns the variance of the Uniform discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the parameters of the PDF.
#    A <= B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( ( b + 1.0 - a ) ** 2 - 1.0 ) / 12.0

  return variance

def uniform_nsphere_sample ( n, rng ):

#*****************************************************************************80
#
## uniform_nsphere_sample() samples the Uniform Unit Sphere PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 168.
#
#  Input:
#
#    integer N, the dimension of the sphere.
#
#  Output:
#
#    real X(N), a point on the unit N sphere, chosen
#    with a uniform probability.
#
  import numpy as np

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = normal_01_sample ( rng )

  norm = np.linalg.norm ( x )

  for i in range ( 0, n ):
    x[i] = x[i] / norm

  return x

def uniform_nsphere_sample_test ( rng ):

#*****************************************************************************80
#
## uniform_nsphere_sample_test() tests uniform_nsphere_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  n = 3

  print ( '' )
  print ( 'uniform_nsphere_sample_test():' )
  print ( '  uniform_nsphere_sample() samples the Uniform Nsphere distribution.' )

  print ( '' )
  print ( '  Dimension N of sphere =       %6d' % ( n ) )
  print ( '' )
  print ( '  Points on the sphere:' )
  print ( '' )

  for i in range ( 0, 10 ):
    x = uniform_nsphere_sample ( n, rng )
    r8vec_transpose_print ( n, x, '' )

  return

def uniform_cdf ( x, a, b ):

#*****************************************************************************80
#
## uniform_cdf() evaluates the Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < a ):
    cdf = 0.0
  elif ( b < x ):
    cdf = 1.0
  else:
    cdf = ( x - a ) / ( b - a )

  return cdf

def uniform_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## uniform_cdf_inv() inverts the Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real X, the corresponding argument.
#
  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'uniform_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'uniform_cdf_inv(): Fatal error!' )

  x = a + ( b - a ) * cdf

  return x

def uniform_cdf_test ( rng ):

#*****************************************************************************80
#
## uniform_cdf_test() tests uniform_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  print ( '' )
  print ( 'uniform_cdf_test():' )
  print ( '  uniform_cdf() evaluates the Uniform CDF' )
  print ( '  uniform_cdf_inv() inverts the Uniform CDF.' )
  print ( '  uniform_pdf() evaluates the Uniform PDF' )

  a = 1.0
  b = 10.0

  check = uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'uniform_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = uniform_sample ( a, b, rng )

    pdf = uniform_pdf ( x, a, b )

    cdf = uniform_cdf ( x, a, b )

    x2 = uniform_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def uniform_check ( a, b ):

#*****************************************************************************80
#
## uniform_check() checks the parameters of the Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= a ):
    print ( '' )
    print ( 'uniform_check(): Fatal error!' )
    print ( '  B <= A.' )
    check = False

  return check

def uniform_mean ( a, b ):

#*****************************************************************************80
#
## uniform_mean() returns the mean of the Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real MEAN, the mean of the discrete uniform PDF.
#
  mean = 0.5 * ( a + b )

  return mean

def uniform_pdf ( x, a, b ):

#*****************************************************************************80
#
## uniform_pdf() evaluates the Uniform PDF.
#
#  Discussion:
#
#    The Uniform PDF is also known as the "Rectangular" or "de Moivre" PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 1 / ( B - A ) for A <= X <= B
#               = 0 otherwise
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < a or b < x ):
    pdf = 0.0
  else:
    pdf = 1.0 / ( b - a )

  return pdf

def uniform_sample ( a, b, rng ):

#*****************************************************************************80
#
## uniform_sample() samples the Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = uniform_cdf_inv ( cdf, a, b )

  return x

def uniform_sample_test ( rng ):

#*****************************************************************************80
#
## uniform_sample_test() tests uniform_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'uniform_sample_test():' )
  print ( '  uniform_mean() computes the Uniform mean' )
  print ( '  uniform_sample() samples the Uniform distribution' )
  print ( '  uniform_variance() computes the Uniform variance.' )

  a = 1.0
  b = 10.0

  check = uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'uniform_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = uniform_mean ( a, b )
  variance = uniform_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =     %14g' % ( a ) )
  print ( '  PDF parameter B =     %14g' % ( b ) )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = uniform_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def uniform_variance ( a, b ):

#*****************************************************************************80
#
## uniform_variance() returns the variance of the Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    A < B.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  variance = ( b - a ) ** 2 / 12.0

  return variance

def von_mises_cdf ( x, a, b ):

#*****************************************************************************80
#
## von_mises_cdf() evaluates the von Mises CDF.
#
#  Discussion:
#
#    Thanks to Cameron Huddleston-Holmes for pointing out a discrepancy
#    in the MATLAB version of this routine, caused by overlooking an
#    implicit conversion to integer arithmetic in the original FORTRAN,
#    JVB, 21 September 2005.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    Geoffrey Hill
#    This version by John Burkardt.
#
#  Reference:
#
#    Geoffrey Hill,
#    ACM TOMS Algorithm 518,
#    Incomplete Bessel Function I0: The von Mises Distribution,
#    ACM Transactions on Mathematical Software,
#    Volume 3, Number 3, September 1977, pages 279-284.
#
#    Kanti Mardia, Peter Jupp,
#    Directional Statistics,
#    Wiley, 2000, QA276.M335
#
#  Input:
#
#    real X, the argument of the CDF.
#    A - PI <= X <= A + PI.
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  a1 = 12.0
  a2 = 0.8
  a3 = 8.0
  a4 = 1.0
  c1 = 56.0
  ck = 10.5
#
#  We expect -PI <= X - A <= PI.
#
  if ( x - a <= - np.pi ):
    cdf = 0.0
    return cdf

  if ( np.pi <= x - a ):
    cdf = 1.0
    return cdf
#
#  Convert the angle (X - A) modulo 2 PI to the range ( 0, 2 * PI ).
#
  z = b

  u = ( x - a + np.pi ) % ( 2.0 * np.pi )

  if ( u < 0.0 ):
    u = u + 2.0 * np.pi

  y = u - np.pi
#
#  For small B, sum IP terms by backwards recursion.
#
  if ( z <= ck ):

    v = 0.0

    if ( 0.0 < z ):

      ip = int ( z * a2 - a3 / ( z + a4 ) + a1 )
      p = ip
      s = np.sin ( y )
      c = np.cos ( y )
      y = p * y
      sn = np.sin ( y )
      cn = np.cos ( y )
      r = 0.0
      z = 2.0 / z

      for n in range ( 2, ip + 1 ):
        p = p - 1.0
        y = sn
        sn = sn * c - cn * s
        cn = cn * c + y * s
        r = 1.0 / ( p * z + r )
        v = ( sn / p + v ) * r

    cdf = ( u * 0.5 + v ) / np.pi
#
#  For large B, compute the normal approximation and left tail.
#
  else:

    c = 24.0 * z
    v = c - c1
    r = np.sqrt ( ( 54.0 / ( 347.0 / v + 26.0 - c ) - 6.0 + c ) / 12.0 )
    z = np.sin ( 0.5 * y ) * r
    s = 2.0 * z * z
    v = v - s + 3.0
    y = ( c - s - s - 16.0 ) / 3.0
    y = ( ( s + 1.75 ) * s + 83.5 ) / v - y
    arg = z * ( 1.0 - s / y ** 2 )
    erfx = r8_erf ( arg )
    cdf = 0.5 * erfx + 0.5

  cdf = max ( cdf, 0.0 )
  cdf = min ( cdf, 1.0 )

  return cdf

def von_mises_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## von_mises_cdf_inv() inverts the von Mises CDF.
#
#  Discussion:
#
#    A simple bisection method is used on the interval [ A - PI, A + PI ].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#    A - PI <= X <= A + PI.
#
  import numpy as np

  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a - np.pi
    return x
  elif ( 1.0 <= cdf ):
    x = a + np.pi
    return x

  x1 = a - np.pi
  cdf1 = 0.0

  x2 = a + np.pi
  cdf2 = 1.0
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = von_mises_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break
 
    if ( it_max < it ):
      print ( '' )
      print ( 'von_mises_cdf_inv(): Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      raise Exception ( 'von_mises_cdf_inv(): Fatal error!' )

    if ( ( cdf <= cdf3 and cdf <= cdf1 ) or ( cdf3 <= cdf and cdf1 <= cdf ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def von_mises_cdf_test ( rng ):

#*****************************************************************************80
#
## von_mises_cdf_test() tests von_mises_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  print ( '' )
  print ( 'von_mises_cdf_test():' )
  print ( '  von_mises_cdf() evaluates the Von Mises CDF.' )
  print ( '  von_mises_cdf_inv() inverts the Von Mises CDF.' )
  print ( '  von_mises_pdf() evaluates the Von Mises PDF.' )

  a = 1.0
  b = 2.0

  check = von_mises_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'von_mises_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = von_mises_sample ( a, b, rng )

    pdf = von_mises_pdf ( x, a, b )

    cdf = von_mises_cdf ( x, a, b )

    x2 = von_mises_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def von_mises_check ( a, b ):

#*****************************************************************************80
#
## von_mises_check() checks the parameters of the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  import numpy as np

  check = True

  if ( a < - np.pi or np.pi < a ):
    print ( '' )
    print ( 'von_mises_check(): Fatal error!' )
    print ( '  A < -PI or PI < A.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'von_mises_mean(): Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def von_mises_circular_variance ( a, b ):

#*****************************************************************************80
#
## von_mises_circular_variance() returns the circular variance of the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    real VALUE, the circular variance of the PDF.
#
  from scipy import special

  value = 1.0 - special.iv ( 1.0, b ) / special.iv ( 0.0, b )

  return value

def von_mises_mean ( a, b ):

#*****************************************************************************80
#
## von_mises_mean() returns the mean of the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def von_mises_pdf ( x, a, b ):

#*****************************************************************************80
#
## von_mises_pdf() evaluates the von Mises PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = EXP ( B * COS ( X - A ) ) / ( 2 * PI * I0(B) )
#
#    where:
#
#      I0(*) is the modified Bessel function of the first
#      kind of order 0.
#
#    The von Mises distribution for points on the unit circle is
#    analogous to the normal distribution of points on a line.
#    The variable X is interpreted as a deviation from the angle A,
#    with B controlling the amount of dispersion.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 160.
#
#    D J Best and N I Fisher,
#    Efficient Simulation of the von Mises Distribution,
#    Applied Statistics,
#    Volume 28, Number 2, pages 152-157.
#
#    Kanti Mardia and Peter Jupp,
#    Directional Statistics,
#    Wiley, 2000, QA276.M335
#
#  Input:
#
#    real X, the argument of the PDF.
#    A - PI <= X <= A + PI.
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np
  from scipy import special

  if ( x < a - np.pi ):
    pdf = 0.0
  elif ( x <= a + np.pi ):
    pdf = np.exp ( b * np.cos ( x - a ) ) / ( 2.0 * np.pi * special.iv ( 0.0, b ) )
  else:
    pdf = 0.0

  return pdf

def von_mises_sample ( a, b, rng ):

#*****************************************************************************80
#
## von_mises_sample() samples the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D J Best and N I Fisher,
#    Efficient Simulation of the von Mises Distribution,
#    Applied Statistics,
#    Volume 28, Number 2, pages 152-157.
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  tau = 1.0 + np.sqrt ( 1.0 + 4.0 * b * b )
  rho = ( tau - np.sqrt ( 2.0 * tau ) ) / ( 2.0 * b )
  r = ( 1.0 + rho * rho ) / ( 2.0 * rho )

  while ( True ):

    u1 = rng.random ( )
    z = np.cos ( np.pi * u1 )
    f = ( 1.0 + r * z ) / ( r + z )
    c = b * ( r - f )

    u2 = rng.random ( )

    if ( u2 < c * ( 2.0 - c ) ):
      break

    if ( c <= np.log ( c / u2 ) + 1.0 ):
      break

  u3 = rng.random ( )

  if ( u3 < 0.5 ):
    x = a - np.arccos ( f )
  else:
    x = a + np.arccos ( f )

  return x

def von_mises_sample_test ( rng ):

#*****************************************************************************80
#
## von_mises_sample_test() tests von_mises_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'von_mises_sample_test():' )
  print ( '  von_mises_mean() computes the Von Mises mean' )
  print ( '  von_mises_sample() samples the Von Mises distribution.' )
  print ( '  von_mises_circular_variance() computes the Von Mises circular variance' )

  a = 1.0
  b = 2.0

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )

  check = von_mises_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'von_mises_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = von_mises_mean ( a, b )
  variance = von_mises_circular_variance ( a, b )

  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF circular variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = von_mises_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = r8vec_circular_variance ( nsample, x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =              %6d' % ( nsample ) )
  print ( '  Sample mean =              %14g' % ( mean ) )
  print ( '  Sample circular variance = %14g' % ( variance ) )
  print ( '  Sample maximum =           %14g' % ( xmax ) )
  print ( '  Sample minimum =           %14g' % ( xmin ) )

  return

def weibull_discrete_cdf ( x, a, b ):

#*****************************************************************************80
#
## weibull_discrete_cdf() evaluates the Discrete Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the CDF.
#    0 <= X.
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - ( 1.0 - a ) ** ( ( x + 1 ) ** b )

  return cdf

def weibull_discrete_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## weibull_discrete_cdf_inv() inverts the Discrete Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#  Output:
#
#    integer X, the corresponding argument.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'weibull_discrete_cdf_inv(): Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    raise Exception ( 'weibull_discrete_cdf_inv(): Fatal error!' )

  x = 1 + int ( ( np.log ( 1.0 - cdf ) \
    / np.log ( 1.0 - a ) ) ** ( 1.0 / b ) - 1.0 )

  return x

def weibull_discrete_cdf_test ( rng ):

#*****************************************************************************80
#
## weibull_discrete_cdf_test() tests weibull_discrete_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  print ( '' )
  print ( 'weibull_discrete_cdf_test():' )
  print ( '  weibull_discrete_cdf() evaluates the Weibull Discrete CDF' )
  print ( '  weibull_discrete_cdf_inv() inverts the Weibull Discrete CDF.' )
  print ( '  weibull_discrete_pdf() evaluates the Weibull Discrete PDF' )

  a = 0.50
  b = 1.5

  check = weibull_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'weibull_discrete_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = weibull_discrete_sample ( a, b, rng )

    pdf = weibull_discrete_pdf ( x, a, b )

    cdf = weibull_discrete_cdf ( x, a, b )

    x2 = weibull_discrete_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )

  return

def weibull_discrete_check ( a, b ):

#*****************************************************************************80
#
## weibull_discrete_check() checks the parameters of the discrete Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'weibull_discrete_check(): Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'weibull_discrete_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def weibull_discrete_pdf ( x, a, b ):

#*****************************************************************************80
#
## weibull_discrete_pdf() evaluates the discrete Weibull PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = ( 1 - A )^X^B - ( 1 - A )^(X+1)^B.
#
#    weibull_discrete_pdf(X)(A,1) = geometric_pdf(X)(A)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#    0 <= X
#
#    real A, B, the parameters that define the PDF.
#    0 <= A <= 1,
#    0 < B.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 0 ):
    pdf = 0.0
  else:
    pdf = ( 1.0 - a ) ** ( x ** b ) - ( 1.0 - a ) ** ( ( x + 1 ) ** b )

  return pdf

def weibull_discrete_sample ( a, b, rng ):

#*****************************************************************************80
#
## weibull_discrete_sample() samples the discrete Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = weibull_discrete_cdf_inv ( cdf, a, b )

  return x

def weibull_discrete_sample_test ( rng ):

#*****************************************************************************80
#
## weibull_discrete_sample_test() tests weibull_discrete_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'weibull_discrete_sample_test():' )
  print ( '  weibull_discrete_sample() samples the Weibull Discrete distribution' )

  a = 0.5
  b = 1.5

  check = weibull_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'weibull_discrete_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =     %14g' % ( a ) )
  print ( '  PDF parameter B =     %14g' % ( b ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = weibull_discrete_sample ( a, b, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def weibull_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## weibull_cdf() evaluates the Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the CDF.
#    A <= X.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < a ):
    cdf = 0.0
  else:
    y = ( x - a ) / b
    cdf = 1.0 - 1.0 / np.exp ( y ** c )

  return cdf

def weibull_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## weibull_cdf_inv() inverts the Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#    0.0 < CDF < 1.0.
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, the corresponding argument of the CDF.
#
  import numpy as np

  x = a + b * ( - np.log ( 1.0 - cdf ) ) ** ( 1.0 / c )

  return x

def weibull_cdf_test ( rng ):

#*****************************************************************************80
#
## weibull_cdf_test() tests weibull_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  print ( '' )
  print ( 'weibull_cdf_test():' )
  print ( '  weibull_cdf() evaluates the Weibull CDF' )
  print ( '  weibull_cdf_inv() inverts the Weibull CDF.' )
  print ( '  weibull_pdf() evaluates the Weibull PDF' )

  x = 3.0

  a = 2.0
  b = 3.0
  c = 4.0

  check = weibull_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'weibull_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '' )
  print ( '       X            PDF           CDF            CDf_inv' )
  print ( '' )

  for i in range ( 0, 10 ):

    x = weibull_sample ( a, b, c, rng )

    pdf = weibull_pdf ( x, a, b, c )

    cdf = weibull_cdf ( x, a, b, c )

    x2 = weibull_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )

  return

def weibull_check ( a, b, c ):

#*****************************************************************************80
#
## weibull_check() checks the parameters of the Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'weibull_check(): Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'weibull_check(): Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def weibull_mean ( a, b, c ):

#*****************************************************************************80
#
## weibull_mean() returns the mean of the Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#
  from scipy.special import gamma

  mean = b * gamma ( ( c + 1.0 ) / c ) + a

  return mean

def weibull_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## weibull_pdf() evaluates the Weibull PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = ( C / B ) * ( ( X - A ) / B )^( C - 1 )
#     * EXP ( - ( ( X - A ) / B )^C ).
#
#    The Weibull PDF is also known as the Frechet PDF.
#
#    weibull_pdf(X)(A,B,1) is the Exponential PDF.
#
#    weibull_pdf(X)(0,1,2) is the Rayleigh PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#    A <= X
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = ( c / b ) * y ** ( c - 1.0 )  / np.exp ( y ** c )

  return pdf

def weibull_sample ( a, b, c, rng ):

#*****************************************************************************80
#
## weibull_sample() samples the Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real X, a sample of the PDF.
#
  import numpy as np

  cdf = rng.random ( )

  x = weibull_cdf_inv ( cdf, a, b, c )

  return x

def weibull_sample_test ( rng ):

#*****************************************************************************80
#
## weibull_sample_test() tests weibull_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  import platform

  nsample = 1000

  print ( '' )
  print ( 'weibull_sample_test():' )
  print ( '  weibull_mean() computes the Weibull mean' )
  print ( '  weibull_sample() samples the Weibull distribution' )
  print ( '  weibull_variance() computes the Weibull variance.' )

  a = 2.0
  b = 3.0
  c = 4.0

  check = weibull_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'weibull_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = weibull_mean ( a, b, c )
  variance = weibull_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  print ( '  PDF parameter C =       %14g' % ( c ) )
  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF variance =          %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = weibull_sample ( a, b, c, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )

  return

def weibull_variance ( a, b, c ):

#*****************************************************************************80
#
## weibull_variance() returns the variance of the Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#
  from scipy.special import gamma

  g1 = gamma ( ( c + 2.0 ) / c )
  g2 = gamma ( ( c + 1.0 ) / c )

  variance = b * b * ( g1 - g2 * g2 )

  return variance

def zipf_cdf_inv ( a, cdf ):

#*****************************************************************************80
#
## zipf_cdf_inv() inverts the Zipf CDF.
#
#  Discussion:
#
#    Simple summation is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CDF, the value of the CDF.
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    integer X, the argument such that
#    CDF(X-1) < CDF <= CDF(X)
#    1 <= X <= 1000
#
  if ( cdf <= 0.0 ):

    x = 1

  else:

    c = r8_zeta ( a )
    cdf2 = 0.0

    x = 1000

    for y in range ( 1, 1001 ):
      pdf = ( 1.0 / y ** a ) / c
      cdf2 = cdf2 + pdf
      if ( cdf <= cdf2 ):
        x = y
        break

  return x

def zipf_cdf ( x, a ):

#*****************************************************************************80
#
## zipf_cdf() evaluates the Zipf CDF.
#
#  Discussion:
#
#    Simple summation is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the PDF.
#    1 <= X
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    real CDF, the value of the CDF.
#
  if ( x < 1 ):

    cdf = 0.0

  else:

    c = r8_zeta ( a )
    cdf = 0.0

    for y in range ( 1, x + 1 ):
      pdf = ( 1.0 / y ** a ) / c
      cdf = cdf + pdf

  return cdf

def zipf_cdf_test ( rng ):

#*****************************************************************************80
#
## zipf_cdf_test() tests zipf_cdf(), zipf_cdf_inv(), zipf_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import platform

  print ( '' )
  print ( 'zipf_cdf_test():' )
  print ( '  zipf_pdf() evaluates the Zipf PDF.' )
  print ( '  zipf_cdf() evaluates the Zipf CDF.' )
  print ( '  zipf_cdf_inv() inverts the Zipf CDF.' )

  a = 2.0

  check = zipf_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'zipf_cdf_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '' )
  print ( '       X          PDF(X)          CDF(X)  CDf_inv(CDF)' )
  print ( '' )

  for x in range ( 1, 21 ):

    pdf = zipf_pdf ( x, a )
    cdf = zipf_cdf ( x, a )
    x2 = zipf_cdf_inv ( a, cdf )
    print ( '  %6d  %14g  %14g  %6d' % ( x, pdf, cdf, x2 ) )

  return

def zipf_check ( a ):

#*****************************************************************************80
#
## zipf_check() checks the parameter of the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    bool CHECK, is true if the parameters are legal.
#
  if ( a <= 1.0 ):
    print ( '' )
    print ( 'zipf_check(): Fatal error!' )
    print ( '  A <= 1.' )
    check = False
    return check

  check = True

  return check

def zipf_mean ( a ):

#*****************************************************************************80
#
## zipf_mean() returns the mean of the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    real MEAN, the mean of the PDF.
#    The mean is only defined for 2 < A.
#
  if ( a <= 2.0 ):
    print ( '' )
    print ( 'zipf_mean(): Fatal error!' )
    print ( '  No mean defined for A <= 2.' )
    raise Exception ( 'zipf_mean(): Fatal error!' )

  mean = r8_zeta ( a - 1.0 ) / r8_zeta ( a )

  return mean

def zipf_pdf ( x, a ):

#*****************************************************************************80
#
## zipf_pdf() evaluates the Zipf PDF.
#
#  Discussion:
#
#    PDF(X)(A) = ( 1 / X^A ) / C
#
#    where the normalizing constant is chosen so that
#
#    C = Sum ( 1 <= I < oo ) 1 / I^A.
#
#    From observation, the frequency of different words in long
#    sequences of text seems to follow the Zipf PDF, with
#    parameter A slightly greater than 1.  The Zipf PDF is sometimes
#    known as the "discrete Pareto" PDF.
#
#    Lotka's law is a version of the Zipf PDF in which A is 2 or approximately
#    2.  Lotka's law describes the frequency of publications by authors in a
#    given field, and estimates that the number of authors with X papers is
#    about 1/X^A of the number of authors with 1 paper.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alfred Lotka,
#    The frequency distribution of scientific productivity,
#    Journal of the Washington Academy of Sciences,
#    Volume 16, Number 12, 1926, pages 317-324.
#
#  Input:
#
#    integer X, the argument of the PDF.
#    1 <= N
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    real PDF, the value of the PDF.
#
  if ( x < 1 ):

    pdf = 0.0

  else:

    c = r8_zeta ( a )
    pdf = ( 1.0 / x ** a ) / c

  return pdf

def zipf_sample ( a, rng ):

#*****************************************************************************80
#
## zipf_sample() samples the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer Verlag, 1986, pages 550-551.
#
#  Input:
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    integer X, a sample of the PDF.
#
  import numpy as np

  b = 2.0 ** ( a - 1.0 )

  while ( True ):

    u = rng.random ( )
    v = rng.random ( )
    w = np.floor ( 1.0 / u ** ( 1.0 / ( a - 1.0 ) ) )

    t = ( ( w + 1.0 ) / w ) ** ( a - 1.0 )

    if ( v * w * ( t - 1.0 ) * b <= t * ( b - 1.0 ) ):
      break

  x = np.floor ( w )

  return x

def zipf_sample_test ( rng ):

#*****************************************************************************80
#
## zipf_sample_test() tests zipf_mean(), zipf_sample(), zipf_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  nsample = 1000

  print ( '' )
  print ( 'zipf_sample_test():' )
  print ( '  zipf_mean() returns the mean of the Zipf distribution.' )
  print ( '  zipf_sample() samples the Zipf distribution.' )
  print ( '  zipf_variance() returns the variance of the Zipf distribution.' )

  a = 4.0

  check = zipf_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'zipf_sample_test(): Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = zipf_mean ( a )
  variance = zipf_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i] = zipf_sample ( a, rng )

  mean = np.mean ( x )
  variance = np.var ( x )
  xmax = np.max ( x )
  xmin = np.min ( x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )

  return

def zipf_variance ( a ):

#*****************************************************************************80
#
## zipf_variance() returns the variance of the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the parameter of the PDF.
#    1.0 < A.
#
#  Output:
#
#    real VARIANCE, the variance of the PDF.
#    The variance is only defined for 3 < A.
# 
  if ( a <= 3.0 ):
    print ( '' )
    print ( 'zipf_variance(): Fatal error!' )
    print ( '  No variance defined for A <= 3.0.' )
    raise Exception ( 'zipf_variance(): Fatal error!' )

  mean = zipf_mean ( a )

  variance = r8_zeta ( a - 2.0 ) / r8_zeta ( a ) - mean * mean

  return variance

if ( __name__ == '__main__' ):
  timestamp ( )
  prob_test ( )
  timestamp ( )

