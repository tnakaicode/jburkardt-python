#! /usr/bin/env python
#
def binomial_pdf_values ( n_data ):

#*****************************************************************************80
#
## BINOMIAL_PDF_VALUES returns some values of the binomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability of X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = BinomialDistribution [ n, p ]
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
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition, CRC Press, 1996, pages 651-652.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer A, a parameter of the function.
#
#    Output, real B, a parameter of the function.
#
#    Output, integer X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  a_vec = np.array ( ( \
     5, 12,  6, 13,  9, \
     1,  2, 17,  6,  8 ))

  b_vec = np.array ( ( \
    0.8295092339327006, \
    0.06611873491603133, \
    0.0438289977791071, \
    0.4495389603071763, \
    0.7972869541062562, \
    0.3507523379805466, \
    0.8590968552798568, \
    0.007512364073964213, \
    0.1136640464424993, \
    0.2671322702601793 ))

  f_vec = np.array ( ( \
    0.3927408939646697, \
    0.0006199968732461383, \
    0.764211224733124, \
    0.0004260353334364943, \
    0.302948289145794, \
    0.3507523379805466, \
    0.01985369619202562, \
    0.006854388879646552, \
    0.000002156446446382985, \
    0.0005691150511772053 ) )

  x_vec = np.array ( ( \
     5, 5, 0, 0, 7, \
     1, 0, 2, 6, 7 ) )

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

def binomial_pdf_values_test ( ):

#*****************************************************************************80
#
## BINOMIAL_PDF_VALUES_TEST demonstrates the use of BINOMIAL_PDF_VALUES.
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
  print ( '' )
  print ( 'BINOMIAL_PDF_VALUES_TEST:' )
  print ( '  BINOMIAL_PDF_VALUES stores values of the BINOMIAL PDF.' )
  print ( '' )
  print ( '   A          B                  X        BINOMIAL_PDF(A,B,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = binomial_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %2d  %24.16g  %2d  %24.16g' % ( a, b, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BINOMIAL_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  binomial_pdf_values_test ( )
  timestamp ( )

