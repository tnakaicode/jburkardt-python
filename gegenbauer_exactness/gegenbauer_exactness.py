#! /usr/bin/env python3
#
def gegenbauer_exactness_test ( ):

#*****************************************************************************80
#
## gegenbauer_exactness_test() tests gegenbauer_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gegenbauer_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gegenbauer_exactness().' )

  gegenbauer_exactness ( 'gegen_o8_a0.5', 8, 0.5 )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def gegenbauer_exactness ( quad_filename, degree_max, alpha ):

#*****************************************************************************80
#
## gegenbauer_exactness() determines the exactness of a Gegenbauer quadrature rule.
#
#  Discussion:
#
#    This program investigates a standard Gauss-Gegenbauer quadrature rule
#    by using it to integrate monomials over [-1,+1], and comparing the
#    approximate result to the known exact value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character QUAD_FILENAME, the "root" name of the R, W and X files 
#    that specify the rule
#
#    integer DEGREE_MAX, the maximum monomial degree to be checked
#
#    integer ALPHA, the exponent of the (1-X^2) factor
#
  import numpy as np

  print ( '' )
  print ( 'gegenbauer_exactness():' )
  print ( '  Investigate the polynomial exactness of a Gauss-Gegenbauer' )
  print ( '  quadrature rule by integrating weighted' )
  print ( '  monomials up to a given degree over the [-1,+1] interval.' )
#
#  Create the names of:
#    the quadrature X file
#    the quadrature W file
#    the quadrature R file
#
  quad_x_filename = quad_filename + '_x.txt'
  quad_w_filename = quad_filename + '_w.txt'
  quad_r_filename = quad_filename + '_r.txt'
#
#  Summarize the input.
#
  print ( '' )
  print ( 'gegenbauer_exactness(): User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".', quad_w_filename )
  print ( '  Quadrature rule R file = "' + quad_r_filename + '".', quad_r_filename )
  print ( '  Maximum degree to check = ', degree_max )
  print ( '  Exponent of (1-x^2), ALPHA = ', alpha )
#
#  Read the X file.
#
  x = np.loadtxt ( quad_x_filename )
  order = x.shape[0]

  print ( '' )
  print ( '  Number of points  = ', order )
#
#  Read the W file.
#
  w = np.loadtxt ( quad_w_filename )
#
#  Read the R file.
#
  r = np.loadtxt ( quad_r_filename )
#
#  Print the input quadrature rule.
#
  print ( '' )
  print ( '  Testing a Gauss-Gegenbauer rule' )
  print ( '  ORDER = ', order )
  print ( '  ALPHA = ', alpha )
  print ( '' )
  print ( '  Standard rule:' )
  print ( '    Integral ( -1 <= x <= +1 ) (1-x^2)^alpha f(x) dx' )
  print ( '    is to be approximated by' )
  print ( '    sum ( 1 <= I <= ORDER ) w(i) * f(x(i)).' )
  print ( '' )
  print ( '  Weights W:' )
  print ( '' )
  print ( w )
  print ( '' )
  print ( '  Abscissas X:' )
  print ( '' )
  print ( x )
  print ( '' )
  print ( '  Region R:' )
  print ( '' )
  print ( r )
#
#  Explore the monomials.
#
  print ( '' )
  print ( '  A Gauss-Gegenbauer rule would be able to exactly' )
  print ( '  integrate monomials up to and including ' )
  print ( '  degree = ', 2 * order - 1 )
  print ( '' )
  print ( '      Error    Degree' )
  print ( '' )

  for degree in range ( 0, degree_max + 1 ):

    quad_error = monomial_quadrature_gegenbauer ( degree, alpha, order, w, x )

    print ( '  %24.16f   %2d' % ( quad_error, degree ) )
#
#  Terminate.
#
  return

def gegenbauer_integral ( expon, alpha ):

#*****************************************************************************80
#
## gegenbauer_integral() evaluates the integral of a monomial with Gegenbauer weight.
#
#  Discussion:
#
#    VALUE = Integral ( -1 <= X <= +1 ) x^EXPON (1-x^2)^ALPHA dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of (1-X^2)
#    in the weight factor.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  if ( ( expon % 2 ) == 1 ):
    value = 0.0
    return value

  c = expon

  arg1 = - alpha
  arg2 =   1.0 + c
  arg3 =   2.0 + alpha + c
  arg4 = - 1.0

  value1 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  value = 2.0 * gamma ( 1.0 + c ) * gamma ( 1.0 + alpha ) \
    * value1 / gamma ( 2.0 + alpha + c )

  return value

def monomial_quadrature_gegenbauer ( expon, alpha, order, w, x ):

#*****************************************************************************80
#
## monomial_quadrature_gegenbauer() applies a quadrature rule to a monomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of (1-X^2) in the weight factor.
#
#    intege ORDER, the number of points in the rule.
#
#    real W(ORDER), the quadrature weights.
#
#    real X(ORDER), the quadrature points.
#
#  Output:
#
#    real QUAD_ERROR, the quadrature error.
#
  import numpy as np
#
#  Get the exact value of the integral.
#
  exact = gegenbauer_integral ( expon, alpha )
#
#  Evaluate the monomial at the quadrature points.
#
  value = x ** expon
#
#  Compute the weighted sum.
#
  quad = np.dot ( w, value )
#
#  Error:
#
  if ( exact == 0.0 ):
    quad_error = np.abs ( quad - exact )
  else:
    quad_error = np.abs ( ( quad - exact ) / exact )

  return quad_error

def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## r8_hyper_2f1() evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
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
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Input:
#
#    real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
  from scipy.special import gamma

  el = 0.5772156649015329

  l0 = ( c == int ( c ) ) and ( c < 0.0 )
  l1 = ( 1.0 - x < 1.0E-15 ) and ( c - a - b <= 0.0 )
  l2 = ( a == int ( a ) ) and ( a < 0.0 )
  l3 = ( b == int ( b ) ) and ( b < 0.0 )
  l4 = ( c - a == int ( c - a ) ) and ( c - a <= 0.0 )
  l5 = ( c - b == int ( c - b ) ) and ( c - b <= 0.0 )

  if ( l0 ):
    print ( '' )
    print ( 'r8_hyper_2f1(): Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )

  if ( l1 ):
    print ( '' )
    print ( 'r8_hyper_2f1(): Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  1 = X < 0, C - A - B <= 0.' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  X = %f' % ( x ) )

  if ( 0.95 < x ):
    eps = 1.0E-08
  else:
    eps = 1.0E-15

  if ( x == 0.0 or a == 0.0 or b == 0.0 ):

    value = 1.0
    return value

  elif ( 1.0 - x == eps and 0.0 < c - a - b ):

    gc = gamma ( c )
    gcab = gamma ( c - a - b )
    gca = gamma ( c - a )
    gcb = gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = gamma ( c )
    g2 = gamma ( 1.0 + a / 2.0 - b )
    g3 = gamma ( 0.5 + 0.5 * a )
    value = g0 * g1 / ( g2 * g3 )
    return value

  elif ( l2 or l3 ):

    if ( l2 ):
      nm = int ( abs ( a ) )

    if ( l3 ):
      nm = int ( abs ( b ) )

    value = 1.0
    r = 1.0

    for k in range ( 1, nm + 1 ):
      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r

    return value

  elif ( l4 or l5 ):

    if ( l4 ):
      nm = int ( abs ( c - a ) )
 
    if ( l5 ):
      nm = int ( abs ( c - b ) )

    value = 1.0
    r  = 1.0
    for k in range ( 1, nm + 1 ):
      r = r * ( c - a + float ( k ) - 1.0 ) * ( c - b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r
    value = ( 1.0 - x ) ** ( c - a - b ) * hf
    return value

  aa = a
  bb = b
  x1 = x

  if ( x < 0.0 ):
    x = x / ( x - 1.0 )
    if ( a < c and b < a and 0.0 < b ):
      a = bb
      b = aa
    b = c - b

  if ( 0.75 <= x ):

    gm = 0.0

    if ( abs ( c - a - b - int ( c - a - b ) ) < 1.0E-15 ):

      m = int ( c - a - b )
      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gam = gamma ( a + float ( m ) )
      gbm = gamma ( b + float ( m ) )

      pa = r8_psi ( a )
      pb = r8_psi ( b )

      if ( m != 0 ):
        gm = 1.0

      for j in range ( 1, abs ( m ) ):
        gm = gm * float ( j )

      rm = 1.0
      for j in range ( 1, abs ( m ) + 1 ):
        rm = rm * float ( j )
 
      f0 = 1.0
      r0 = 1.0
      r1 = 1.0
      sp0 = 0.0
      sp = 0.0

      if ( 0 <= m ):

        c0 = gm * gc / ( gam * gbm )
        c1 = - gc * ( x - 1.0 ) ** m / ( ga * gb * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0
 
        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / ( a + float ( k ) - 1.0 ) \
            + 1.0 / ( b + float ( k ) - 1.0 ) - 1.0 / float ( k )

        f1 = pa + pb + sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + ( 1.0 - a ) \
              / ( float ( j + k ) * ( a + float ( j + k ) - 1.0 ) ) \
              + 1.0 / ( b + float ( j + k ) - 1.0 )

          rp = pa + pb + 2.0 * el + sp + sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + m + float ( k ) - 1.0 ) * ( b + m + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break
 
          hw = f1

        value = f0 * c0 + f1 * c1

      elif ( m < 0 ):

        m = - m
        c0 = gm * gc / ( ga * gb * ( 1.0 - x ) ** m )
        c1 = - ( - 1 ) ** m * gc / ( gam * gbm * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a - float ( m ) + float ( k ) - 1.0 ) \
            * ( b - float ( m ) + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0

        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / float ( k )

        f1 = pa + pb - sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) \
            / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + 1.0 / float ( j + k )

          rp = pa + pb + 2.0 * el + sp - sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break

          hw = f1

        value = f0 * c0 + f1 * c1

    else:

      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gca = gamma ( c - a )
      gcb = gamma ( c - b )
      gcab = gamma ( c - a - b )
      gabc = gamma ( a + b - c )
      c0 = gc * gcab / ( gca * gcb )
      c1 = gc * gabc / ( ga * gb ) * ( 1.0 - x ) ** ( c - a - b )
      value = 0.0
      hw = value
      r0 = c0
      r1 = c1

      for k in range ( 1, 251 ):

        r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( a + b - c + float ( k ) ) ) * ( 1.0 - x )

        r1 = r1 * ( c - a + float ( k ) - 1.0 ) \
          * ( c - b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( c - a - b + float ( k ) ) ) * ( 1.0 - x )

        value = value + r0 + r1

        if ( abs ( value - hw ) < abs ( value ) * eps ):
          break

        hw = value

      value = value + c0 + c1

  else:

    a0 = 1.0

    if ( a < c and c < 2.0 * a and b < c and c < 2.0 * b ):

      a0 = ( 1.0 - x ) ** ( c - a - b )
      a = c - a
      b = c - b

    value = 1.0
    hw = value
    r = 1.0

    for k in range ( 1, 251 ):

      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( k * ( c + float ( k ) - 1.0 ) ) * x

      value = value + r

      if ( abs ( value - hw ) <= abs ( value ) * eps ):
        break

      hw = value

    value = a0 * value

  if ( x1 < 0.0 ):
    x = x1
    c0 = 1.0 / ( 1.0 - x ) ** aa
    value = c0 * value

  if ( 120 < k ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Warning!' )
    print ( '  A large number of iterations were needed.' )
    print ( '  The accuracy of the results should be checked.' )

  return value

def r8_psi ( x ):

#*****************************************************************************80
#
## r8_psi() evaluates the function Psi(X).
#
#  Discussion:
#
#    This routine evaluates the logarithmic derivative of the
#    Gamma function,
#
#      PSI(X) = d/dX ( GAMMA(X) ) / GAMMA(X)
#             = d/dX LN ( GAMMA(X) )
#
#    for real X, where either
#
#      - XMAX1 < X < - XMIN, and X is not a negative integer,
#
#    or
#
#      XMIN < X.
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
#    Original FORTRAN77 version by William Cody.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Cody, Anthony Strecok, Henry Thacher,
#    Chebyshev Approximations for the Psi Function,
#    Mathematics of Computation,
#    Volume 27, Number 121, January 1973, pages 123-127.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

  p1 = np.array ( ( \
   4.5104681245762934160E-03, \
   5.4932855833000385356, \
   3.7646693175929276856E+02, \
   7.9525490849151998065E+03, \
   7.1451595818951933210E+04, \
   3.0655976301987365674E+05, \
   6.3606997788964458797E+05, \
   5.8041312783537569993E+05, \
   1.6585695029761022321E+05 ))

  p2 = np.array ( ( \
  -2.7103228277757834192, \
  -1.5166271776896121383E+01, \
  -1.9784554148719218667E+01, \
  -8.8100958828312219821, \
  -1.4479614616899842986, \
  -7.3689600332394549911E-02, \
  -6.5135387732718171306E-21 ))

  piov4 = 0.78539816339744830962

  q1 = np.array ( ( \
   9.6141654774222358525E+01, \
   2.6287715790581193330E+03, \
   2.9862497022250277920E+04, \
   1.6206566091533671639E+05, \
   4.3487880712768329037E+05, \
   5.4256384537269993733E+05, \
   2.4242185002017985252E+05, \
   6.4155223783576225996E-08 ))

  q2 = np.array ( ( \
   4.4992760373789365846E+01, \
   2.0240955312679931159E+02, \
   2.4736979003315290057E+02, \
   1.0742543875702278326E+02, \
   1.7463965060678569906E+01, \
   8.8427520398873480342E-01 ))

  x01 = 187.0
  x01d = 128.0
  x02 = 6.9464496836234126266E-04
  xinf = 1.70E+38
  xlarge = 2.04E+15
  xmax1 = 3.60E+16
  xmin1 = 5.89E-39
  xsmall = 2.05E-09

  w = abs ( x )
  aug = 0.0
#
#  Check for valid arguments, then branch to appropriate algorithm.
#
  if ( xmax1 <= - x or w < xmin1 ):

    if ( 0.0 < x ):
      value = - xinf
    else:
      value = xinf;

    return value

  if ( x < 0.5 ):
#
#  X < 0.5, use reflection formula: psi(1-x) = psi(x) + pi * cot(pi*x)
#  Use 1/X for PI*COTAN(PI*X)  when  XMIN1 < |X| <= XSMALL.
#
    if ( w <= xsmall ):

      aug = - 1.0 / x
#
#  Argument reduction for cotangent.
#
    else:

      if ( x < 0.0 ):
        sgn = piov4
      else:
        sgn = - piov4

      w = w - int ( w )
      nq = int ( w * 4.0 )
      w = 4.0 * ( w - float ( nq ) * 0.25 )
#
#  W is now related to the fractional part of 4.0 * X.
#  Adjust argument to correspond to values in the first
#  quadrant and determine the sign.
#
      n = ( nq // 2 )

      if ( n + n != nq ):
        w = 1.0 - w

      z = piov4 * w

      if ( ( n % 2 ) != 0 ):
        sgn = - sgn
#
#  Determine the final value for  -pi * cotan(pi*x).
#
      n = ( ( nq + 1 ) // 2 )
      if ( ( n % 2 ) == 0 ):
#
#  Check for singularity.
#
        if ( z == 0.0 ):

          if ( 0.0 < x ):
            value = - xinf
          else:
            value = xinf

          return value

        aug = sgn * ( 4.0 / np.tan ( z ) )

      else:

        aug = sgn * ( 4.0 * np.tan ( z ) )

    x = 1.0 - x
#
#  0.5 <= X <= 3.0.
#
  if ( x <= 3.0 ):

    den = x
    upper = p1[0] * x
    for i in range ( 0, 7 ):
      den = ( den + q1[i] ) * x
      upper = ( upper + p1[i+1] ) * x

    den = ( upper + p1[8] ) / ( den + q1[7] )
    x = ( x - x01 / x01d ) - x02
    value = den * x + aug
    return value
#
#  3.0 < X.
#
  if ( x < xlarge ):
    w = 1.0 / ( x * x )
    den = w
    upper = p2[0] * w
    for i in range ( 0, 5 ):
      den = ( den + q2[i] ) * w
      upper = ( upper + p2[i+1] ) * w
    aug = ( upper + p2[6] ) / ( den + q2[5] ) - 0.5 / x + aug

  value = aug + np.log ( x )

  return value

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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  gegenbauer_exactness_test ( )
  timestamp ( )


