#! /usr/bin/env python
#
def tfn ( h, a ):

#*****************************************************************************80
#
## TFN calculates the T function of Owen.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    Python version by John Burkardt
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
#  Parameters:
#
#    Input, real H, A, the arguments of the T function.
#
#    Output, real VALUE, the value of the T function.
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
## TFN_TEST tests TFN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  from owen_values import owen_values

  print ( '' )
  print ( 'TFN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TFN evaluates Owen\'s T function.' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'TFN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  tfn_test ( )
  timestamp ( )
 
