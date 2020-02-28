#! /usr/bin/env python
#
def r8_normal_pdf ( av, sd, x ):

#*****************************************************************************80
#
## R8_NORMAL_PDF evaluates the PDF of a normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    Original FORTRAN90 version by Guannan Zhang.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real AV, the mean value.
#
#    Input, real SD, the standard deviation.
#    0.0 < SD.
#
#    Input, real X, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  from sys import exit
  import numpy as np

  if ( sd <= 0.0 ):
    print ( '' )
    print ( 'R8_NORMAL_PDF - Fatal error!' )
    print ( '  Standard deviation must be positive.' )
    exit ( 'R8_NORMAL_PDF - Fatal error!' )

  rtemp = 0.5 * ( ( x - av ) / sd ) ** 2

  value = np.exp ( - rtemp ) / sd / np.sqrt ( 2.0 * np.pi )

  return value

def r8_normal_pdf_values ( n_data ):

#*****************************************************************************80
#
## R8_NORMAL_PDF_VALUES returns some values of the Normal PDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ mu, sigma ]
#      PDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2015
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
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( ( \
    0.01180775937213258, \
    0.006307849174478944, \
    0.0147514774470322, \
    0.9468437743011001, \
    0.02140312299941794, \
    0.05939959967353488, \
    0.2348929157422787, \
    0.007207515678571277, \
    0.005944396897656727, \
    0.03637663165771322 ))

  mu_vec = np.array ( ( \
   -56.31634060352484, \
     12.33908855337884, \
    -48.48444152359102, \
      26.7931424604825, \
    -19.73874370047668, \
    -99.63232576831896, \
    -81.09104995766396, \
     68.16949013113364, \
    -47.93940044652702, \
    -29.67426801922078 ))

  sigma_vec = np.array ( ( \
    4.785956124893755, \
    2.13500469923221, \
    0.6387882883091059, \
    0.4024634224214489, \
    3.79790008346491, \
    4.497769898408682, \
    0.1667227687589636, \
    0.7032091872463158, \
    4.57117016420902, \
    4.132147851761006 ))

  x_vec = np.array ( ( \
  -46.85424018542929, \
    6.781057314200307, \
  -50.23282168570062, \
   26.67129012408019, \
  -12.9643468135976, \
 -103.6600156181528, \
  -80.73183222587458, \
   66.09155915000321, \
  -58.53544475210675, \
  -35.44773135435396 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, x, f

def r8_normal_pdf_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_PDF_TEST tests R8_NORMAL_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'R8_NORMAL_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NORMAL_PDF evaluates the normal pdf' )
  print ( '  pdf(mu,sigma) is the normal pdf with' )
  print ( '  mu = mean, sigma = standard deviation.' )
  print ( '' )
  print ( '            MU                       SIGMA                      X' ),
  print ( '                     PDF(MU,SIGMA)             PDF(MU,SIGMA)' )
  print ( '                                                                 ' ),
  print ( '                     tabulated                 computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, mu, sigma, x, pdf1 = r8_normal_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_normal_pdf ( mu, sigma, x )
    print ( '  %24.16g  %24.16g  %24.16g  %24.16g  %24.16g' % ( mu, sigma, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NORMAL_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_normal_pdf_test ( )
  timestamp ( )
 
