#! /usr/bin/env python
#
def fisher_pdf ( x, kappa, mu ):

#*****************************************************************************80
#
## FISHER_PDF evaluates the Fisher PDF.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, real X(3), the argument of the PDF.
#    X should have unit Euclidean norm, but this routine will
#    automatically work with a normalized version of X.
#
#    Input, real KAPPA, the concentration parameter.
#    0 <= KAPPA is required.
#
#    Input, real MU(3), the mean direction.
#    MU should have unit Euclidean norm, but this routine will
#    automatically work with a normalized version of MU.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8vec_dot_product import r8vec_dot_product
  from r8vec_norm import r8vec_norm
  from scipy import special
  from sys import exit
#
#  Force column-vector shape.
#
  if ( kappa < 0.0 ):
    print ( '' )
    print ( 'FISHER_PDF - Fatal error!' )
    print ( '  KAPPA must be nonnegative.' )
    print ( '  Input KAPPA = %g' % ( kappa ) )
    exit ( 'FISHER_PDF - Fatal error!' )

  if ( kappa == 0.0 ):
    pdf = 1.0 / ( 4.0 * np.pi )
    return pdf

  alpha = 0.5

  b = special.iv ( alpha, kappa )

  cf = np.sqrt ( kappa ) / ( np.sqrt ( ( 2.0 * np.pi ) ** 3 ) * b )

  mu_norm = r8vec_norm ( 3, mu )

  if ( mu_norm == 0.0 ):
    pdf = cf
    return pdf

  x_norm = r8vec_norm ( 3, x )

  if ( x_norm == 0.0 ):
    pdf = cf
    return pdf

  arg = kappa * ( r8vec_dot_product ( 3, x, mu ) ) / ( x_norm * mu_norm )

  pdf = cf * np.exp ( arg )

  return pdf

def fisher_pdf_test ( ):

#*****************************************************************************80
#
## FISHER_PDF_TEST tests FISHER_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  n = 10
  test_num = 3

  print ( '' )
  print ( 'FISHER_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FISHER_PDF evaluates the Fisher PDF.' )

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
    print ( '  PDF parameters:' )
    print ( '    Concentration parameter KAPPA = %g' % ( kappa ) )

    r8vec_transpose_print ( 3, mu, '' )

    print ( '' )
    print ( '      X                         PDF' )
    print ( '' )

    seed = 123456789

    for j in range ( 0, n ):

      x, seed = fisher_sample ( kappa, mu, 1, seed )

      pdf = fisher_pdf ( x, kappa, mu )

      print ( '  %8g  %8g  %8g    %14g' % ( x[0,0], x[1,0], x[2,0], pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FISHER_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def fisher_sample ( kappa, mu, n, seed ):

#*****************************************************************************80
#
## FISHER_SAMPLE samples the Fisher distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, real KAPPA, the concentration parameter.
#
#    Input, real MU(3), the mean direction.
#    MU should have unit Euclidean norm, but this routine will
#    automatically work with a normalized version of MU.
#
#    Input, integer N, the number of samples to choose.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real XYZ(3,N), a sample of the Fisher distribution.
#
#    Output, integer SEED, a seed for the random number generator.
#
#  Local Parameters:
#
#    Input, real ALPHA, BETA, the colatitude (theta) and 
#    longitude (phi) of the mean direction.  
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01
  from r8vec_norm import r8vec_norm
  from r8vec_uniform_01 import r8vec_uniform_01
  from sys import exit

  mu_norm = r8vec_norm ( 3, mu )

  if ( mu_norm == 0.0 ):
    print ( '' )
    print ( 'FISHER_SAMPLE - Fatal error!' )
    print ( '  Direction vector MU is zero' )
    exit ( 'FISHER_SAMPLE - Fatal error!' )

  alpha = - np.arccos ( mu[2] / mu_norm )
  beta = np.arctan2 ( mu[1], mu[0] )

  lam = np.exp ( - 2.0 * kappa )

  theta, seed = r8vec_uniform_01 ( n, seed )

  if ( kappa == 0.0 ):
    for i in range ( 0, n ):
      theta[i] = 2.0 * np.arcsin ( np.sqrt ( 1.0 - theta[i] ) )
  else:
    for i in range ( 0, n ):
      theta[i] = 2.0 * np.arcsin ( np.sqrt ( - np.log ( theta[i] * ( 1.0 - lam ) + lam ) \
        / ( 2.0 * kappa ) ) )

  phi, seed = r8vec_uniform_01 ( n, seed )
  for i in range ( 0, n ):
    phi[i] = 2.0 * np.pi * phi[i]

  a = np.zeros ( [ 3, 3 ] )
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
  a[0,0] =   np.cos ( alpha ) * np.cos ( beta )
  a[1,0] =                    - np.sin ( beta )
  a[2,0] =   np.sin ( alpha ) * np.cos ( beta ) 

  a[0,1] =   np.cos ( alpha ) * np.sin ( beta )
  a[1,1] =                    + np.cos ( beta )
  a[2,1] =   np.sin ( alpha ) * np.sin ( beta )

  a[0,2] = - np.sin ( alpha )
  a[1,2] =   0.0
  a[2,2] =   np.cos ( alpha )
#
#  Rotate the points.
#
  xyz = np.dot ( a, xyz )

  return xyz, seed

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  fisher_pdf_test ( )
  timestamp ( )
 
