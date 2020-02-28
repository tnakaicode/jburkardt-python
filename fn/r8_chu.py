#! /usr/bin/env python
#
def r8_chu ( a, b, x ):

#*****************************************************************************80
#
## R8_CHU evaluates the confluent hypergeometric function of R8 arguments.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real A, B, the parameters.
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_gamma import r8_gamma
  from r8_gamr import r8_gamr
  from machine import r8_mach
  from r8_mop import r8_mop
  from r8_poch import r8_poch
  from sys import exit

  eps = r8_mach ( 3 )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'R8_CHU - Fatal error!' )
    print ( '  X < 0.' )
    exit ( 'R8_CHU - Fatal error!' )

  if ( x == 0.0 ):
    if ( 1.0 <= b ):
      print ( '' )
      print ( 'R8_CHU - Fatal error!' )
      print ( '  X = 0 and 1 <= B.' )
      exit ( 'R8_CHU - Fatal error!' )

    value = r8_gamma ( 1.0 - b ) / r8_gamma ( 1.0 + a - b )
    return value

  if ( max ( abs ( a ), 1.0 ) * max ( abs ( 1.0 + a - b ), 1.0 ) < 0.99 * abs ( x ) ):
    value = x ** ( - a ) * r8_chu_scaled ( a, b, x )
    return value
#
#  The ascending series will be used, because the descending rational
#  approximation (which is based on the asymptotic series) is unstable.
#
  if ( 0.0 <= b ):
    aintb = r8_aint ( b + 0.5 )
  else:
    aintb = r8_aint ( b - 0.5 )

  beps = b - aintb
  n = int ( aintb )
  alnx = np.log ( x )
  xtoeps = np.exp ( - beps * alnx )
#
#  Evaluate the finite sum.
#
#  Consider the case b < 1.0 first.
#
  if ( n < 1 ):

    sum = 1.0

    t = 1.0
    m = - n
    for i in range ( 0, m ):
      xi1 = float ( i )
      t = t * ( a + xi1 ) * x / ( ( b + xi1 ) * ( xi1 + 1.0 ) )
      sum = sum + t

    sum = r8_poch ( 1.0 + a - b, - a ) * sum
#
#  Now consider the case 1 <= b.
#
  else:

    sum = 0.0
    m = n - 2

    if ( 0 <= m ):

      t = 1.0
      sum = 1.0

      for i in range ( 1, m + 1 ):
        xi = float ( i )
        t = t * ( a - b + xi ) * x / ( ( 1.0 - b + xi ) * xi )
        sum = sum + t

      sum = r8_gamma ( b - 1.0 ) * r8_gamr ( a ) * x ** ( 1 - n ) * xtoeps * sum
#
#  Next evaluate the infinite sum.
#
  if ( n < 1 ):
    istrt = 1 - n
  else:
    istrt = 0

  xi = float ( istrt )

  factor = r8_mop ( n ) * r8_gamr ( 1.0 + a - b ) * x ** istrt

  if ( beps != 0.0 ):
    factor = factor * beps * np.pi / np.sin ( beps * np.pi )

  pochai = r8_poch ( a, xi )
  gamri1 = r8_gamr ( xi + 1.0 )
  gamrni = r8_gamr ( aintb + xi )
  b0 = factor * r8_poch ( a, xi - beps ) * gamrni \
    * r8_gamr ( xi + 1.0 - beps )
#
#  x^(-beps) is close to 1.0, so we must be careful in evaluating 
#  the differences.
#
  if ( abs ( xtoeps - 1.0 ) <= 0.5 ):

    pch1ai = r8_poch1 ( a + xi, - beps )
    pch1i = r8_poch1 ( xi + 1.0 - beps, beps )
    c0 = factor * pochai * gamrni * gamri1 * ( \
      - r8_poch1 ( b + xi,- beps ) + pch1ai \
      - pch1i + beps * pch1ai * pch1i )
#
#  xeps1 = (1.0 - x^(-beps))/beps = (x^(-beps) - 1.0)/(-beps)
#
    xeps1 = alnx * r8_exprel ( - beps * alnx )

    value = sum + c0 + xeps1 * b0
    xn = float ( n )

    for i in range ( 1, 1001 ):
      xi = float ( istrt + i )
      xi1 = float ( istrt + i - 1 )
      b0 = ( a + xi1 - beps ) * b0 * x \
        / ( ( xn + xi1 ) * ( xi - beps ) )
      c0 = ( a + xi1 ) * c0 * x / ( ( b + xi1) * xi ) \
        - ( ( a - 1.0 ) * ( xn + 2.0 * xi - 1.0 ) \
        + xi * ( xi - beps ) ) * b0 \
        / ( xi * ( b + xi1 ) * ( a + xi1 - beps ) )
      t = c0 + xeps1 * b0
      value = value + t

      if ( abs ( t ) < eps * abs ( value ) ):
        return value

    print ( '' )
    print ( 'R8_CHU - Fatal error!' )
    print ( '  No convergence in 1000 terms.' )
    exit ( 'R8_CHU - Fatal error!' )
#
#  x^(-beps) is very different from 1.0, so the straightforward
#  formulation is stable.
#
  a0 = factor * pochai * r8_gamr ( b + xi ) * gamri1 / beps
  b0 = xtoeps * b0 / beps

  value = sum + a0 - b0

  for i in range ( 1, 1001 ):

    xi = float ( istrt + i )
    xi1 = float ( istrt + i - 1 )
    a0 = ( a + xi1 ) * a0 * x / ( ( b + xi1 ) * xi )
    b0 = ( a + xi1 - beps ) * b0 * x / ( ( aintb + xi1 ) * ( xi - beps ) )
    t = a0 - b0
    value = value + t

    if ( abs ( t ) < eps * abs ( value ) ):
      return value

  print ( '' )
  print ( 'R8_CHU - Fatal error!' )
  print ( '  No convergence in 1000 terms.' )
  exit ( 'R8_CHU - Fatal error!' )

def r8_chu_test ( ):

#*****************************************************************************80
#
## R8_CHU_TEST tests R8_CHU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from hypergeometric_u_values import hypergeometric_u_values

  print ( '' )
  print ( 'R8_CHU_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHU evaluates the hypergeometric U function.' )
  print ( '' )
  print ( '             A               B               X     CHU(A,B,X)  R8_CHU(A,B,X)  Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx1 = hypergeometric_u_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_chu ( a, b, x )

    print ( '  %14.4f  %14.4f  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, b, x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHU_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_chu_scaled ( a, b, z ):

#*****************************************************************************80
#
## R8_CHU_SCALED: scaled confluent hypergeometric function of R8 arguments.
#
#  Discussion:
#
#    Evaluate, for large z, z^a * u(a,b,z)  where U is the logarithmic
#    confluent hypergeometric function.  A rational approximation due to
#    Y L Luke is used.  When U is not in the asymptotic region, that is, when A
#    or B is large compared with Z, considerable significance loss occurs.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real A, B, the parameters.
#
#    Input, real Z, the argument.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  from machine import r8_mach
  from sys import exit

  eps = 4.0 * r8_mach ( 4 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  bp = 1.0 + a - b
  ab = a * bp
  ct2 = 2.0 * ( z - ab )
  sab = a + bp

  aa = np.zeros ( 4 )
  bb = np.zeros ( 4 )

  bb[0] = 1.0
  aa[0] = 1.0

  ct3 = sab + 1.0 + ab
  bb[1] = 1.0 + 2.0 * z / ct3
  aa[1] = 1.0 + ct2 / ct3

  anbn = ct3 + sab + 3.0
  ct1 = 1.0 + 2.0 * z / anbn
  bb[2] = 1.0 + 6.0 * ct1 * z / ct3
  aa[2] = 1.0 + 6.0 * ab / anbn + 3.0 * ct1 * ct2 / ct3

  for i in range ( 4, 301 ):

    x2i1 = float ( 2 * i - 3 )
    ct1 = x2i1 / ( x2i1 - 2.0 )
    anbn = anbn + x2i1 + sab
    ct2 = ( x2i1 - 1.0 ) / anbn
    c2 = x2i1 * ct2 - 1.0
    d1z = x2i1 * 2.0 * z / anbn

    ct3 = sab * ct2
    g1 = d1z + ct1 * ( c2 + ct3 )
    g2 = d1z - c2
    g3 = ct1 * ( 1.0 - ct3 - 2.0 * ct2 )

    bb[3] = g1 * bb[2] + g2 * bb[1] + g3 * bb[0]
    aa[3] = g1 * aa[2] + g2 * aa[1] + g3 * aa[0]

    value = aa[3] / bb[3]

    if ( abs ( value - aa[0] / bb[0] ) < eps * abs ( value ) ):
      return value

    for j in range ( 0, 3 ):
      aa[j] = aa[j+1]
      bb[j] = bb[j+1]

  print ( '' )
  print ( 'R8_CHU_SCALED - Fatal error!' )
  print ( '  No convergence after 300 terms.' )
  exit ( 'R8_CHU_SCALED - Fatal error!' )

def r8_exprel ( x ):

#*****************************************************************************80
#
## R8_EXPREL evaluates the exponential relative error term of an R8 argument.
#
#  Discussion:
#
#    The relative error term is ( exp ( x ) - 1 ) / x.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the exponential relative error term
#    at X.
#
  import numpy as np
  from r8_aint import r8_aint
  from machine import r8_mach

  alneps = np.log ( r8_mach ( 3 ) )
  xn = 3.72 - 0.3 * alneps
  xln = np.log ( ( xn + 1.0 ) / 1.36 )
  nterms = int ( r8_aint ( xn - ( xn * xln + alneps ) / ( xln + 1.36 ) + 1.5 ) )
  xbnd = r8_mach ( 3 )

  absx = abs ( x )

  if ( absx < xbnd ):
    value = 1.0
  elif ( absx <= 0.5 ):
    value = 0.0
    for i in range ( 1, nterms + 1 ):
      value = 1.0 + value * x / float ( nterms + 2 - i )
  else:
    value = ( np.exp ( x ) - 1.0 ) / x

  return value

def r8_poch1 ( a, x ):

#*****************************************************************************80
#
## R8_POCH1 evaluates a quantity related to Pochhammer's symbol.
#
#  Discussion:
#
#    Evaluate a generalization of Pochhammer's symbol for special
#    situations that require especially accurate values when x is small in
#      poch1(a,x) = (poch(a,x)-1)/x
#                 = (gamma(a+x)/gamma(a) - 1.0)/x .
#    This specification is particularly suited for stably computing
#    expressions such as
#      (gamma(a+x)/gamma(a) - gamma(b+x)/gamma(b))/x
#           = poch1(a,x) - poch1(b,x)
#    Note that poch1(a,0.0) = psi(a)
#
#    When abs ( x ) is so small that substantial cancellation will occur if
#    the straightforward formula is used, we  use an expansion due
#    to fields and discussed by y. l. luke, the special functions and their
#    approximations, vol. 1, academic press, 1969, page 34.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real A, the parameter.
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the value of the function.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_cot import r8_cot
  from machine import r8_mach
  from r8_poch import r8_poch
  from r8_psi import r8_psi

  bern = np.array ( [ \
      +0.833333333333333333333333333333333E-01, \
      -0.138888888888888888888888888888888E-02, \
      +0.330687830687830687830687830687830E-04, \
      -0.826719576719576719576719576719576E-06, \
      +0.208767569878680989792100903212014E-07, \
      -0.528419013868749318484768220217955E-09, \
      +0.133825365306846788328269809751291E-10, \
      -0.338968029632258286683019539124944E-12, \
      +0.858606205627784456413590545042562E-14, \
      -0.217486869855806187304151642386591E-15, \
      +0.550900282836022951520265260890225E-17, \
      -0.139544646858125233407076862640635E-18, \
      +0.353470703962946747169322997780379E-20, \
      -0.895351742703754685040261131811274E-22, \
      +0.226795245233768306031095073886816E-23, \
      -0.574472439520264523834847971943400E-24, \
      +0.145517247561486490186626486727132E-26, \
      -0.368599494066531017818178247990866E-28, \
      +0.933673425709504467203255515278562E-30, \
      -0.236502241570062993455963519636983E-31 ] )

  sqtbig = 1.0 / np.sqrt ( 24.0 * r8_mach ( 1 ) )
  alneps = np.log ( r8_mach ( 3 ) )

  if ( x == 0.0 ):
    value = r8_psi ( a )
    return value

  absx = abs ( x )
  absa = abs ( a )

  if ( 0.1 * absa < absx or 0.1 < absx * np.log ( max ( absa, 2.0 ) ) ):
    value = r8_poch ( a, x )
    value = ( value - 1.0 ) / x
    return value

  if ( a < - 0.5 ):
    bp = 1.0 - a - x
  else:
    bp = a

  if ( bp < 10.0 ):
    incr = int ( r8_aint ( 11.0 - bp ) )
  else:
    incr = 0

  b = bp + float ( incr )

  var = b + 0.5 * ( x - 1.0 )
  alnvar = np.log ( var )
  q = x * alnvar

  poly1 = 0.0

  gbern = np.zeros ( 10 )

  if ( var < sqtbig ):

    var2 = 1.0 / var / var

    rho = 0.5 * ( x + 1.0 )
    gbern[0] = 1.0
    gbern[1] = - rho / 12.0
    term = var2
    poly1 = gbern[1] * term

    nterms = int ( r8_aint ( - 0.5 * alneps / alnvar + 1.0 ) )

    if ( 20 < nterms ):
      print ( '' )
      print ( 'R8_POCH1 - Fatal error!' )
      print ( ' 20 < NTERMS.' )
      exit ( 'R8_POCH1 - Fatal error!' )

    for k in range ( 2, nterms + 1 ):
      gbk = 0.0
      for j in range ( 1, k + 1 ):
        ndx = k - j + 1
        gbk = gbk + bern[ndx-1] * gbern[j-1]
      gbern[k] = - rho * gbk / float ( k )
      term = term * ( 2 * k - 2 - x ) * ( 2 * k - 1 - x ) * var2
      poly1 = poly1 + gbern[k] * term

  poly1 = ( x - 1.0 ) * poly1
  value = r8_exprel ( q ) * ( alnvar + q * poly1 ) + poly1
#
#  we have value(b,x), but bp is small, so we use backwards recursion
#  to obtain value(bp,x).
#
  for ii in range ( 1, incr + 1 ):
    i = incr - ii
    binv = 1.0 / ( bp + i )
    value = ( value - binv ) / ( 1.0 + x * binv )

  if ( bp == a ):
    return value
#
#  we have value(bp,x), but a is lt -0.5.  We therefore use a reflection
#  formula to obtain value(a,x).
#
  sinpxx = np.sin ( np.pi * x ) / x
  sinpx2 = np.sin ( 0.5 * np.pi * x )
  trig = sinpxx * r8_cot ( np.pi * b ) - 2.0 * sinpx2 * ( sinpx2 / x )

  value = trig + ( 1.0 + x * trig ) * value

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_chu_test ( )
  timestamp ( )
