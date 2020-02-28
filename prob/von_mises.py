#! /usr/bin/env python
#
def von_mises_cdf ( x, a, b ):

#*****************************************************************************80
#
## VON_MISES_CDF evaluates the von Mises CDF.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    Geoffrey Hill
#    Python version by John Burkardt.
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
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#    A - PI <= X <= A + PI.
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from r8_erf import r8_erf

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
## VON_MISES_CDF_INV inverts the von Mises CDF.
#
#  Discussion:
#
#    A simple bisection method is used on the interval [ A - PI, A + PI ].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Output, real X, the corresponding argument of the CDF.
#    A - PI <= X <= A + PI.
#
  import numpy as np
  from sys import exit

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
      print ( 'VON_MISES_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'VON_MISES_CDF_INV - Fatal error!' )

    if ( ( cdf <= cdf3 and cdf <= cdf1 ) or ( cdf3 <= cdf and cdf1 <= cdf ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def von_mises_cdf_test ( ):

#*****************************************************************************80
#
## VON_MISES_CDF_TEST tests VON_MISES_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'VON_MISES_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VON_MISES_CDF evaluates the Von Mises CDF.' )
  print ( '  VON_MISES_CDF_INV inverts the Von Mises CDF.' )
  print ( '  VON_MISES_PDF evaluates the Von Mises PDF.' )

  a = 1.0
  b = 2.0

  check = von_mises_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'VON_MISES_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = von_mises_sample ( a, b, seed )

    pdf = von_mises_pdf ( x, a, b )

    cdf = von_mises_cdf ( x, a, b )

    x2 = von_mises_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'VON_MISES_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def von_mises_check ( a, b ):

#*****************************************************************************80
#
## VON_MISES_CHECK checks the parameters of the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  import numpy as np

  check = True

  if ( a < - np.pi or np.pi < a ):
    print ( '' )
    print ( 'VON_MISES_CHECK - Fatal error!' )
    print ( '  A < -PI or PI < A.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'VON_MISES_MEAN - Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def von_mises_circular_variance ( a, b ):

#*****************************************************************************80
#
## VON_MISES_CIRCULAR_VARIANCE returns the circular variance of the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Output, real VALUE, the circular variance of the PDF.
#
  from scipy import special

  value = 1.0 - special.iv ( 1.0, b ) / special.iv ( 0.0, b )

  return value

def von_mises_mean ( a, b ):

#*****************************************************************************80
#
## VON_MISES_MEAN returns the mean of the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def von_mises_pdf ( x, a, b ):

#*****************************************************************************80
#
## VON_MISES_PDF evaluates the von Mises PDF.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    A - PI <= X <= A + PI.
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
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

def von_mises_sample ( a, b, seed ):

#*****************************************************************************80
#
## VON_MISES_SAMPLE samples the von Mises PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    -PI <= A <= PI,
#    0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  tau = 1.0 + np.sqrt ( 1.0 + 4.0 * b * b )
  rho = ( tau - np.sqrt ( 2.0 * tau ) ) / ( 2.0 * b )
  r = ( 1.0 + rho * rho ) / ( 2.0 * rho )

  while ( True ):

    u1, seed = r8_uniform_01 ( seed )
    z = np.cos ( np.pi * u1 )
    f = ( 1.0 + r * z ) / ( r + z )
    c = b * ( r - f )

    u2, seed = r8_uniform_01 ( seed )

    if ( u2 < c * ( 2.0 - c ) ):
      break

    if ( c <= np.log ( c / u2 ) + 1.0 ):
      break

  u3, seed = r8_uniform_01 ( seed )

  if ( u3 < 0.5 ):
    x = a - np.arccos ( f )
  else:
    x = a + np.arccos ( f )

  return x, seed

def von_mises_sample_test ( ):

#*****************************************************************************80
#
## VON_MISES_SAMPLE_TEST tests VON_MISES_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_circular_variance import r8vec_circular_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'VON_MISES_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VON_MISES_MEAN computes the Von Mises mean' )
  print ( '  VON_MISES_SAMPLE samples the Von Mises distribution.' )
  print ( '  VON_MISES_CIRCULAR_VARIANCE computes the Von Mises circular variance' )

  a = 1.0
  b = 2.0

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )

  check = von_mises_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'VON_MISES_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = von_mises_mean ( a, b )
  variance = von_mises_circular_variance ( a, b )

  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF circular variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = von_mises_sample ( a, b, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_circular_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =              %6d' % ( nsample ) )
  print ( '  Sample mean =              %14g' % ( mean ) )
  print ( '  Sample circular variance = %14g' % ( variance ) )
  print ( '  Sample maximum =           %14g' % ( xmax ) )
  print ( '  Sample minimum =           %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'VON_MISES_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  von_mises_cdf_test ( )
  von_mises_sample_test ( )
  timestamp ( )
 
