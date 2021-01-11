#! /usr/bin/env python
#
def r8_besk ( nu, x ):

#*****************************************************************************80
#
## R8_BESK evaluates the Bessel function K of order NU of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 September 2018
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
#    Input, real NU, the order.
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the Bessel function K of order NU at X.
#
  import numpy as np

  xnu = ( nu % 1.0 )

  nin = int ( nu ) + 1

  bke = r8_besks ( xnu, x, nin )

  value = bke[nin-1]

  return value

def r8_besk_test ( ):

#*****************************************************************************80
#
## R8_BESK_TEST tests R8_BESK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from bessel_kx_values import bessel_kx_values

  print ( '' )
  print ( 'R8_BESK_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_BESK evaluates Bessel K functtions K(NU,X).' )
  print ( '' )
  print ( '              NU             X       BESK(X)  R8_BESK(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx1 = bessel_kx_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besk ( nu, x )

    print ( '  %14.4g  %14.4f  %14.6g  %14.6g  %14.6g' \
      % ( nu, x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_BESK_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_besks ( xnu, x, nin ):

#*****************************************************************************80
#
## R8_BESKS evaluates a sequence of K Bessel functions at X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2011
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
#    Input, real XNU, ?
#    |XNU| < 1.
#
#    Input, real X, the argument.
#
#    Input, integer NIN, indicates the number of terms to compute.
#
#    Output, real BK(abs(NIN)), the K Bessel functions.
#
  import numpy as np
  from machine import r8_mach

  xmax = - np.log ( r8_mach ( 1 ) )
  xmax = xmax + 0.5 * np.log ( 3.14 * 0.5 / xmax )

  bk = r8_beskes ( xnu, x, nin )

  expxi = np.exp ( - x )
  n = int ( abs ( nin ) )
  for i in range ( 0, n ):
    bk[i] = expxi * bk[i]

  return bk

def r8_beskes ( xnu, x, nin ):

#*****************************************************************************80
#
## R8_BESKES evaluates a sequence of exponentially scaled K Bessel functions at X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2011
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
#    Input, real XNU, ?
#    |XNU| < 1.
#
#    Input, real X, the argument.
#
#    Input, integer NIN, indicates the number of terms to compute.
#
#    Output, real BKE(abs(NIN)), the exponentially scaled
#    K Bessel functions.
#
  import numpy as np
  from sys import exit

  v = abs ( xnu )
  n = int ( abs ( nin ) )

  if ( 1.0 <= v ):
    print ( '' )
    print ( 'R8_BESKES - Fatal error!' )
    print ( '  |XNU| must be less than 1.' )
    exit ( 'R8_BESKES - Fatal error!' )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'R8_BESKES - Fatal error!' )
    print ( '  X <= 0.' )
    exit ( 'R8_BESKES - Fatal error!' )

  if ( n == 0 ):
    print ( '' )
    print ( 'R8_BESKES - Fatal error!' )
    print ( '  N = 0.' )
    exit ( 'R8_BESKES - Fatal error!' )

  bke = np.zeros ( n )

  value, bknu1, iswtch = r8_knus ( v, x )
  bke[0] = value

  if ( n == 1 ):
    return bke

  if ( nin < 0 ):
    vincr = - 1.0
  else:
    vincr = + 1.0

  if ( xnu < 0.0 ):
    direct = - vincr
  else:
    direct = vincr

  bke[1] = bknu1

  if ( direct < 0.0 ):
    value, bknu1, iswtch = r8_knus ( abs ( xnu + vincr ), x )
    bke[1] = value

  if ( n == 2 ):
    return bke

  vend = abs ( xnu + nin ) - 1.0

  v = xnu
  for i in range ( 2, n ):
    v = v + vincr
    bke[i] = 2.0 * v * bke[i-1] / x + bke[i-2]

  return bke

def r8_knus ( xnu, x ):

#*****************************************************************************80
#
## R8_KNUS computes a sequence of K Bessel functions.
#
#  Discussion:
#
#    This routine computes Bessel functions
#      exp(x) * k-sub-xnu (x)
#    and
#      exp(x) * k-sub-xnu+1 (x)
#    for 0.0 <= xnu < 1.0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 April 2016
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
#    Input, real XNU, the order parameter.
#
#    Input, real X, the argument.
#
#    Output, real BKNU, BKNU1, the two K Bessel functions.
#
#    Output, integer ISWTCH, ?
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_gamma import r8_gamma
  from r8_inits import r8_inits
  from machine import r8_mach

  aln2 = 0.69314718055994530941723212145818
  euler = 0.57721566490153286060651209008240
  sqpi2 = +1.2533141373155002512078826424055

  c0kcs = np.array ( [ \
      +0.60183057242626108387577445180329E-01, \
      -0.15364871433017286092959755943124, \
      -0.11751176008210492040068229226213E-01, \
      -0.85248788891979509827048401550987E-03, \
      -0.61329838767496791874098176922111E-04, \
      -0.44052281245510444562679889548505E-05, \
      -0.31631246728384488192915445892199E-06, \
      -0.22710719382899588330673771793396E-07, \
      -0.16305644608077609552274620515360E-08, \
      -0.11706939299414776568756044043130E-09, \
      -0.84052063786464437174546593413792E-11, \
      -0.60346670118979991487096050737198E-12, \
      -0.43326960335681371952045997366903E-13, \
      -0.31107358030203546214634697772237E-14, \
      -0.22334078226736982254486133409840E-15, \
      -0.16035146716864226300635791528610E-16, \
      -0.11512717363666556196035697705305E-17, \
      -0.82657591746836959105169479089258E-19, \
      -0.59345480806383948172333436695984E-20, \
      -0.42608138196467143926499613023976E-21, \
      -0.30591266864812876299263698370542E-22, \
      -0.21963541426734575224975501815516E-23, \
      -0.15769113261495836071105750684760E-24, \
      -0.11321713935950320948757731048056E-25, \
      -0.81286248834598404082792349714433E-27, \
      -0.58360900893453226552829349315949E-28, \
      -0.41901241623610922519452337780905E-29, \
      -0.30083737960206435069530504212862E-30, \
      -0.21599152067808647728342168089832E-31 ] )

  znu1cs = np.array ( [ \
      +0.203306756994191729674444001216911, \
      +0.140077933413219771062943670790563, \
      +0.791679696100161352840972241972320E-02, \
      +0.339801182532104045352930092205750E-03, \
      +0.117419756889893366664507228352690E-04, \
      +0.339357570612261680333825865475121E-06, \
      +0.842594176976219910194629891264803E-08, \
      +0.183336677024850089184748150900090E-09, \
      +0.354969844704416310863007064469557E-11, \
      +0.619032496469887332205244342078407E-13, \
      +0.981964535680439424960346115456527E-15, \
      +0.142851314396490474211473563005985E-16, \
      +0.191894921887825298966162467488436E-18, \
      +0.239430979739498914162313140597128E-20, \
      +0.278890246815347354835870465474995E-22, \
      +0.304606650633033442582845214092865E-24, \
      +0.313173237042191815771564260932089E-26, \
      +0.304133098987854951645174908005034E-28, \
      +0.279840384636833084343185097659733E-30, \
      +0.244637186274497596485238794922666E-32 ] )

  eta = 0.1 * r8_mach ( 3 )
  ntc0k = r8_inits ( c0kcs, 29, eta )
  ntznu1 = r8_inits ( znu1cs, 20, eta )
  xnusml = np.sqrt ( r8_mach ( 3 ) / 8.0 )
  xsml = 0.1 * r8_mach ( 3 )
  alnsml = np.log ( r8_mach ( 1 ) )
  alnbig = np.log ( r8_mach ( 2 ) )
  alneps = np.log ( 0.1 * r8_mach ( 3 ) )

  if ( xnu < 0.0 or 1.0 <= xnu ):
    print ( '' )
    print ( 'R8_KNUS - Fatal error!' )
    print ( '  XNU < 0 or. 1 <= XNU.' )
    exit ( 'R8_KNUS - Fatal error!' )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'R8_KNUS - Fatal error!' )
    print ( '  X <= 0.' )
    exit ( 'R8_KNUS - Fatal error!' )

  iswtch = 0
#
#  X is small.  Compute k-sub-xnu (x) and the derivative of k-sub-xnu (x)
#  then find k-sub-xnu+1 (x).  xnu is reduced to the interval (-0.5,+0.5)
#  then to (0., .5), because k of negative order (-nu) = k of positive
#  order (+nu).
#
  if ( x <= 2.0 ):

    if ( xnu <= 0.5 ):
      v = xnu
    else:
      v = 1.0 - xnu
#
#  Carefully find (x/2)^xnu and z^xnu where z = x*x/4.
#
    alnz = 2.0 * ( np.log ( x ) - aln2 )

    if ( x <= xnu ):

      if ( alnbig < - 0.5 * xnu * alnz - aln2 - np.log ( xnu ) ):
        print ( '' )
        print ( 'R8_KNUS - Fatal error!' )
        print ( '  Small X causing overflow.' )
        exit ( 'R8_KNUS - Fatal error!' )

    vlnz = v * alnz
    x2tov = np.exp ( 0.5 * vlnz )

    if ( vlnz <= alnsml ):
      ztov = 0.0
    else:
      ztov = x2tov * x2tov

    a0 = 0.5 * r8_gamma ( 1.0 + v )
    b0 = 0.5 * r8_gamma ( 1.0 - v )
    c0 = - euler

    if ( 0.5 <= ztov and xnusml < v ):
      c0 = - 0.75 + r8_csevl ( ( 8.0 * v ) * v - 1.0, c0kcs, ntc0k )

    nterms = max ( 2, int ( r8_aint ( 11.0 + ( 8.0 * alnz - 25.19 - alneps ) \
      / ( 4.28 - alnz ) ) ) )

    alpha = np.zeros ( nterms )
    beta = np.zeros ( nterms )

    if ( ztov <= 0.5 ):
      alpha[0] = ( a0 - ztov * b0 ) / v
    else:
      alpha[0] = c0 - alnz * ( 0.75 + \
        r8_csevl ( vlnz / 0.35 + 1.0, znu1cs, ntznu1 ) ) * b0

    beta[0] = - 0.5 * ( a0 + ztov * b0 )

    if ( x <= xsml ):
      z = 0.0
    else:
      z = 0.25 * x * x

    for i in range ( 1, nterms ):
      xi = float ( i )
      a0 = a0 / ( xi * ( xi - v ) )
      b0 = b0 / ( xi * ( xi + v ) )
      alpha[i] = ( alpha[i-1] + 2.0 * xi * a0 ) / ( xi * ( xi + v ) )
      beta[i] = ( xi - 0.5 * v ) * alpha[i] - ztov * b0

    bknu = alpha[nterms-1]
    bknud = beta[nterms-1]
    for i in range ( nterms - 2, -1, -1 ):
      bknu = alpha[i] + bknu * z
      bknud = beta[i] + bknud * z

    expx = np.exp ( x )
    bknu = expx * bknu / x2tov

    if ( alnbig < - 0.5 * ( xnu + 1.0 ) * alnz - 2.0 * aln2 ):
      iswtch = 1
      return bknu, bknu1, iswtch

    bknud = expx * bknud * 2.0 / ( x2tov * x )

    if ( xnu <= 0.5 ):
      bknu1 = v * bknu / x - bknud
      return bknu, bknu1, iswtch

    bknu0 = bknu
    bknu = - v * bknu / x - bknud
    bknu1 = 2.0 * xnu * bknu / x + bknu0
#
#  x is large.  find k-sub-xnu (x) and k-sub-xnu+1 (x) with y. l. luke-s
#  rational expansion.
#
  else:

    sqrtx = np.sqrt ( x )

    if ( 1.0 / xsml < x ):
      bknu = sqpi2 / sqrtx
      bknu1 = bknu
      return bknu, bknu1, iswtch

    an = - 0.60 - 1.02 / x
    bn = - 0.27 - 0.53 / x

    nterms = min ( 32, max ( 3, int ( r8_aint ( an + bn * alneps ) ) ) )

    alpha = np.zeros ( nterms )
    beta = np.zeros ( nterms )
    a = np.zeros ( nterms )
    b = np.zeros ( nterms )

    for inu in range ( 1, 3 ):

      if ( inu == 1 ):
        if ( xnu <= xnusml ):
          xmu = 0.0
        else:
          xmu = ( 4.0 * xnu ) * xnu
      else:
        xmu = 4.0 * ( abs ( xnu ) + 1.0 ) ** 2

      a[0] = 1.0 - xmu
      a[1] = 9.0 - xmu
      a[2] = 25.0 - xmu

      if ( a[1] == 0.0 ):

        result = sqpi2 * ( 16.0 * x + xmu + 7.0 ) / ( 16.0 * x * sqrtx )

      else:

        alpha[0] = 1.0
        alpha[1] = ( 16.0 * x + a[1] ) / a[1]
        alpha[2] = ( ( 768.0 * x + 48.0 * a[2] ) * x \
          + a[1] * a[2] ) / ( a[1] * a[2] )

        beta[0] = 1.0
        beta[1] = ( 16.0 * x + ( xmu + 7.0 ) ) / a[1]
        beta[2] = ( ( 768.0 * x \
          + 48.0 * ( xmu + 23.0 ) ) * x + \
          ( ( xmu + 62.0 ) * xmu + 129.0 ) ) \
          / ( a[1] * a[2] )

        for i in range ( 3, nterms ):

          n = i
          x2n = float ( 2 * n - 1 )

          a[i] = ( x2n + 2.0 ) ** 2 - xmu
          qq = 16.0 * x2n / a[i]
          p1 = - x2n * ( float ( 12 * n * n - 20 * n ) - a[0] ) \
            / ( ( x2n - 2.0 ) * a[i] ) - qq * x
          p2 = ( float ( 12 * n * n - 28 * n + 8 ) - a[0] ) / a[i] - qq * x
          p3 = - x2n * a[i-3] / ( ( x2n - 2.0 ) * a[i] )

          alpha[i] = - p1 * alpha[i-1] \
                     - p2 * alpha[i-2] \
                     - p3 * alpha[i-3]

          beta[i] =  - p1 * beta[i-1] \
                     - p2 * beta[i-2] \
                     - p3 * beta[i-3]

        result = sqpi2 * beta[nterms-1] / ( sqrtx * alpha[nterms-1] )

      if ( inu == 1 ):
        bknu = result
      else:
        bknu1 = result

  return bknu, bknu1, iswtch

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_besk_test ( )
  timestamp ( )
