#! /usr/bin/env python
#
def normal_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## NORMAL_01_PDF_VALUES returns some values of the Normal 01 PDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0, 1 ]
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
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( ( \
    0.03155059887555709, \
    0.0005094586261557538, \
    0.01235886992552887, \
    0.353192862601275, \
    0.3171212685764107, \
    0.0009653372813755943, \
    0.06083856556197816, \
    0.003066504313116445, \
    0.0005116437388114821, \
    0.2246444116615346 ))

  x_vec = np.array ( ( \
    -2.252653624140994, \
     3.650540612071437, \
     2.636073871461605, \
     0.4935635421351536, \
    -0.6775433481923101, \
    -3.471050120671749, \
    -1.939377660943641, \
    -3.120345651740235, \
    -3.649368017767143, \
     1.0717256984193 ))

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

def normal_01_pdf_values_test ( ):

#*****************************************************************************80
#
## NORMAL_01_PDF_VALUES_TEST demonstrates the use of NORMAL_01_PDF_VALUES.
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
  import platform

  print ( '' )
  print ( 'NORMAL_01_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_PDF_VALUES stores values of the unit normal PDF.' )
  print ( '' )
  print ( '      X         NORMAL_01_PDF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = normal_01_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_pdf_values_test ( )
  timestamp ( )

