#! /usr/bin/env python
#
def i4_binomial_pdf ( n, p, k ):

#*****************************************************************************80
#
## I4_BINOMIAL_PDF evaluates the binomial PDF.
#
#  Discussion:
#
#    pdf(n,p,k) = C(n,k) p^k (1-p)^(n-k)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the number of binomial trials.
#    0 < N.
#
#    Input, real P, the probability of a success in one trial.
#
#    Input, integer K, the number of successes.
#
#    Output, real VALUE, the probability of K successes
#    in N trials with a per-trial success probability of P.
#
  from r8_choose import r8_choose

  if ( k < 0 ):
    value = 0.0
  elif ( k <= n ):
    value = r8_choose ( n, k ) * ( p ** k ) * ( 1.0 - p ) ** ( n - k )
  else:
    value = 0.0

  return value

def i4_binomial_pdf_values ( n_data ):

#*****************************************************************************80
#
## I4_BINOMIAL_PDF_VALUES returns some values of the binomial PDF.
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

def i4_binomial_pdf_test ( ):

#*****************************************************************************80
#
## I4_BINOMIAL_PDF_TEST tests I4_BINOMIAL_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'I4_BINOMIAL_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BINOMIAL_PDF evaluates the binomial pdf' )
  print ( '  pdf(n,p,k) = probability, in n trials, of k successes,' )
  print ( '  if a single success has probability p.' )
  print ( '' )
  print ( '     N          P        K       PDF(N,P,K)       PDF(N,P,K)' )
  print ( '                                 tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, n, p, k, pdf1 = i4_binomial_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = i4_binomial_pdf ( n, p, k )
    print ( '  %4d  %14.6g  %2d  %14.6g  %14.6g' % ( n, p, k, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BINOMIAL_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_binomial_pdf_test ( )
  timestamp ( )
 
