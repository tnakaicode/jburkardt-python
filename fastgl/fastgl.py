#! /usr/bin/env python3
#
def besselj1squared ( k ):

#*****************************************************************************80
#
## BESSELJ1SQUARED computes the square of BesselJ(1, BesselZero(0,k))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer K, the index of the desired zero.
#
#    Output, real Z, the value of the square of the Bessel
#    J1 function at the K-th zero of the Bessel J0 function.
#
  import numpy as np

  j1 = np.array ( [ \
    0.269514123941916926139021992911E+00, \
    0.115780138582203695807812836182E+00, \
    0.0736863511364082151406476811985E+00, \
    0.0540375731981162820417749182758E+00, \
    0.0426614290172430912655106063495E+00, \
    0.0352421034909961013587473033648E+00, \
    0.0300210701030546726750888157688E+00, \
    0.0261473914953080885904584675399E+00, \
    0.0231591218246913922652676382178E+00, \
    0.0207838291222678576039808057297E+00, \
    0.0188504506693176678161056800214E+00, \
    0.0172461575696650082995240053542E+00, \
    0.0158935181059235978027065594287E+00, \
    0.0147376260964721895895742982592E+00, \
    0.0137384651453871179182880484134E+00, \
    0.0128661817376151328791406637228E+00, \
    0.0120980515486267975471075438497E+00, \
    0.0114164712244916085168627222986E+00, \
    0.0108075927911802040115547286830E+00, \
    0.0102603729262807628110423992790E+00, \
    0.00976589713979105054059846736696E+00 ] )

  if ( 21 < k ):

    x = 1.0E+00 / ( k - 0.25E+00 )
    x2 = x * x
    z = \
        x *       (  0.202642367284675542887758926420E+00 \
      + x2 * x2 * ( -0.303380429711290253026202643516E-03 \
      + x2 *      (  0.198924364245969295201137972743E-03 \
      + x2 *      ( -0.228969902772111653038747229723E-03 \
      + x2 *      (  0.433710719130746277915572905025E-03 \
      + x2 *      ( -0.123632349727175414724737657367E-02 \
      + x2 *      (  0.496101423268883102872271417616E-02 \
      + x2 *      ( -0.266837393702323757700998557826E-01 \
      + x2 *      (  0.185395398206345628711318848386E+00 ) ))))))))
  else:
    z = j1[k-1]

  return z

def besselj1squared_test ( ):

#*****************************************************************************80
#
## BESSELJ1SQUARED_TEST tests BESSELJ1SQUARED.
#
#  Discussion:
#
#    SCIPY.SPECIAL provides the built in function J1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import platform
  import scipy.special as sp

  print ( '' )
  print ( 'BESSELJ1SQUARED_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BESSELJ1SQUARED returns the square of the Bessel J1(X) function' )
  print ( '  at the K-th zero of J0(X).' )
  print ( '' )
  print ( '   K           X(K)                    J1(X(K))^2                 BESSELJ1SQUARED' )
  print ( '' )

  for k in range ( 1, 31 ):
    x = besseljzero ( k )
    f1 = sp.j1 ( x ) ** 2
    f2 = besselj1squared ( k )
    print ( '  %2d  %24.16g  %24.16g  %24.16g' % ( k, x, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSELJ1SQUARED_TEST:' )
  print ( '  Normal end of execution.' )
  return

def besseljzero ( k ):

#*****************************************************************************80
#
## BESSELJZERO computes the kth zero of the J0(X) Bessel function.
#
#  Discussion:
#
#    Note that the first 20 zeros are tabulated.  After that, they are
#    computed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer K, the index of the desired zero.
#    1 <= K.
#
#    Output, real X, the value of the zero.
#
  import numpy as np

  jz = np.array ( [ \
    2.40482555769577276862163187933E+00, \
    5.52007811028631064959660411281E+00, \
    8.65372791291101221695419871266E+00, \
    11.7915344390142816137430449119E+00, \
    14.9309177084877859477625939974E+00, \
    18.0710639679109225431478829756E+00, \
    21.2116366298792589590783933505E+00, \
    24.3524715307493027370579447632E+00, \
    27.4934791320402547958772882346E+00, \
    30.6346064684319751175495789269E+00, \
    33.7758202135735686842385463467E+00, \
    36.9170983536640439797694930633E+00, \
    40.0584257646282392947993073740E+00, \
    43.1997917131767303575240727287E+00, \
    46.3411883716618140186857888791E+00, \
    49.4826098973978171736027615332E+00, \
    52.6240518411149960292512853804E+00, \
    55.7655107550199793116834927735E+00, \
    58.9069839260809421328344066346E+00, \
    62.0484691902271698828525002646E+00 ] )

  if ( 20 < k ):
    x = np.pi * ( k - 0.25E+00 )
    r = 1.0E+00 / x
    r2 = r * r
    x = x \
      + r  * (  0.125E+00 \
      + r2 * ( -0.807291666666666666666666666667E-01 \
      + r2 * (  0.246028645833333333333333333333E+00 \
      + r2 * ( -0.182443876720610119047619047619E+01 \
      + r2 * (  0.253364147973439050099206349206E+02 \
      + r2 * ( -0.567644412135183381139802038240E+03 \
      + r2 * (  0.186904765282320653831636345064E+05 \
      + r2 * ( -0.849353580299148769921876983660E+06 \
      + r2 *    0.509225462402226769498681286758E+08 ))))))))
  else:
    x = jz[k-1]

  return x

def besseljzero_test ( ):

#*****************************************************************************80
#
## BESSELJZERO_TEST tests BESSELJZERO.
#
#  Discussion:
#
#    SCIPY.SPECIAL provides the built in J0(X) function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import platform
  import scipy.special as sp

  print ( '' )
  print ( 'BESSELJZERO_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BESSELJZERO returns the K-th zero of J0(X).' )
  print ( '' )
  print ( '   K           X(K)                  J0(X(K))' )
  print ( '' )

  for k in range ( 1, 31 ):
    x = besseljzero ( k )
    j0x = sp.j0 ( x )
    print ( '  %2d  %24.16g  %24.16g' % ( k, x, j0x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSELJZERO_TEST:' )
  print ( '  Normal end of execution.' )
  return

def fastgl_test ( ):

#*****************************************************************************80
#
## FASTGL_TEST tests the FASTGL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FASTGL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the FASTGL library.' )

  besseljzero_test ( )
  besselj1squared_test ( )
  glpair_test ( )
  glpairs_test ( )
  glpairtabulated_test ( )
  legendre_theta_test ( )
  legendre_weight_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'FASTGL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def glpair ( n, k ):

#*****************************************************************************80
#
## GLPAIR computes the K-th pair of an N-point Gauss-Legendre rule.
#
#  Discussion:
#
#    If N <= 100, GLPAIRTABULATED is called, otherwise GLPAIR is called.
#
#    Theta values of the zeros are in [0,pi], and monotonically increasing. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer N, the number of points in the given rule.
#    0 < N.
#
#    Input, integer K, the index of the point to be returned.
#    1 <= K <= N.
#
#    Output, real THETA, WEIGHT, X, the theta coordinate, weight, 
#    and x coordinate of the point.
#
  from sys import exit

  if ( n < 1 ):
    print ( '' )
    print ( 'GLPAIR - Fatal error!' )
    print ( '  Illegal value of N.' )
    exit ( 'GLPAIR - Fatal error!' )

  if ( k < 1 or n < k ):
    print ( '' )
    print ( 'GLPAIR - Fatal error!' )
    print ( '  Illegal value of K.' )
    exit ( 'GLPAIR - Fatal error!' )

  if ( n < 101 ):
    theta, weight, x = glpairtabulated ( n, k )
  else:
    theta, weight, x = glpairs ( n, k )

  return theta, weight, x

def glpair_test ( ):

#*****************************************************************************80
#
## GLPAIR_TEST tests GLPAIR.
#
#  Discussion:
#
#    Test the numerical integration of ln(x) over the range [0,1]
#    Normally, one would not use Gauss-Legendre quadrature for this,
#    but for the sake of having an example with l > 100, this is included.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'GLPAIR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Estimate integral ( 0 <= x <= 1 ) ln(x) dx.' )
  print ( '' )
  print ( '    Nodes           Estimate' )
  print ( '' )

  l = 1
  for p in range ( 0, 7 ):
    q = 0.0
    for k in range ( 1, l + 1 ):
      theta, weight, x = glpair ( l, k )
      q = q + 0.5 * weight * np.log ( 0.5 * ( x + 1.0 ) )
    print ( '  %7d       %24.16g' % ( l, q ) )
    l = l * 10
  print ( '' )
  print ( '    Exact        -1.0' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GLPAIR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def glpairs ( n, k ):

#*****************************************************************************80
#
## GLPAIRS computes the K-th pair of an N-point Gauss-Legendre rule.
#
#  Discussion:
#
#    This routine is intended for cases were 100 < N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer N, the number of points in the given rule.
#    1 <= N.
#
#    Input, integer K, the index of the point to be returned.
#    1 <= K <= N.
#
#    Output, real THETA, WEIGHT, X, the theta coordinate, weight, 
#    and x coordinate of the point.
#
  import numpy as np
  from sys import exit

  if ( n < 1 ):
    print ( '' )
    print ( 'GLPAIRS - Fatal error!' )
    print ( '  Illegal value of N.' )
    exit ( 'GLPAIRS - Fatal error!' )

  if ( k < 1 or n < k ):
    print ( '' )
    print ( 'GLPAIRS - Fatal error!' )
    print ( '  Illegal value of K.' )
    exit ( 'GLPAIRS - Fatal error!' )

  if ( n < ( 2 * k - 1 ) ):
    kcopy = n - k + 1
  else:
    kcopy = k
#
#  Get the Bessel zero.
#
  w = 1.0E+00 / ( float ( n ) + 0.5E+00 )
  nu = besseljzero ( kcopy )
  theta = w * nu
  y = theta ** 2
#
#  Get the asymptotic BesselJ(1,nu) squared.
#
  b = besselj1squared ( kcopy )
#
#  Get the Chebyshev interpolants for the nodes.
#
  sf1t = ((((( \
    - 1.29052996274280508473467968379E-12 * y \
    + 2.40724685864330121825976175184E-10 ) * y \
    - 3.13148654635992041468855740012E-08 ) * y \
    + 0.275573168962061235623801563453E-05 ) * y \
    - 0.148809523713909147898955880165E-03 ) * y \
    + 0.416666666665193394525296923981E-02 ) * y \
    - 0.416666666666662959639712457549E-01

  sf2t = ((((( \
    + 2.20639421781871003734786884322E-09 * y \
    - 7.53036771373769326811030753538E-08 ) * y \
    + 0.161969259453836261731700382098E-05 ) * y \
    - 0.253300326008232025914059965302E-04 ) * y \
    + 0.282116886057560434805998583817E-03 ) * y \
    - 0.209022248387852902722635654229E-02 ) * y \
    + 0.815972221772932265640401128517E-02

  sf3t = ((((( \
    - 2.97058225375526229899781956673E-08 * y \
    + 5.55845330223796209655886325712E-07 ) * y \
    - 0.567797841356833081642185432056E-05 ) * y \
    + 0.418498100329504574443885193835E-04 ) * y \
    - 0.251395293283965914823026348764E-03 ) * y \
    + 0.128654198542845137196151147483E-02 ) * y \
    - 0.416012165620204364833694266818E-02
#
#  Get the Chebyshev interpolants for the weights.
#
  wsf1t = (((((((( \
    - 2.20902861044616638398573427475E-14 * y \
    + 2.30365726860377376873232578871E-12 ) * y \
    - 1.75257700735423807659851042318E-10 ) * y \
    + 1.03756066927916795821098009353E-08 ) * y \
    - 4.63968647553221331251529631098E-07 ) * y \
    + 0.149644593625028648361395938176E-04 ) * y \
    - 0.326278659594412170300449074873E-03 ) * y \
    + 0.436507936507598105249726413120E-02 ) * y \
    - 0.305555555555553028279487898503E-01 ) * y \
    + 0.833333333333333302184063103900E-01

  wsf2t = ((((((( \
    + 3.63117412152654783455929483029E-12 * y \
    + 7.67643545069893130779501844323E-11 ) * y \
    - 7.12912857233642220650643150625E-09 ) * y \
    + 2.11483880685947151466370130277E-07 ) * y \
    - 0.381817918680045468483009307090E-05 ) * y \
    + 0.465969530694968391417927388162E-04 ) * y \
    - 0.407297185611335764191683161117E-03 ) * y \
    + 0.268959435694729660779984493795E-02 ) * y \
    - 0.111111111111214923138249347172E-01

  wsf3t = ((((((( \
    + 2.01826791256703301806643264922E-09 * y \
    - 4.38647122520206649251063212545E-08 ) * y \
    + 5.08898347288671653137451093208E-07 ) * y \
    - 0.397933316519135275712977531366E-05 ) * y \
    + 0.200559326396458326778521795392E-04 ) * y \
    - 0.422888059282921161626339411388E-04 ) * y \
    - 0.105646050254076140548678457002E-03 ) * y \
    - 0.947969308958577323145923317955E-04 ) * y \
    + 0.656966489926484797412985260842E-02
#
#  Refine with the paper expansions.
#
  nuosin = nu / np.sin ( theta )
  bnuosin = b * nuosin
  winvsinc = w * w * nuosin
  wis2 = winvsinc * winvsinc
# 
#  Finally compute the node and the weight.
#
  theta = w * ( nu + theta * winvsinc \
    * ( sf1t + wis2 * ( sf2t + wis2 * sf3t ) ) )
  deno = bnuosin + bnuosin * wis2 * ( wsf1t + wis2 * ( wsf2t + wis2 * wsf3t ) )
  weight = ( 2.0E+00 * w ) / deno

  if ( n < ( 2 * k - 1 ) ):
    theta = np.pi - theta

  x = np.cos ( theta )

  return theta, weight, x

def glpairs_test ( ):

#*****************************************************************************80
#
## GLPAIRS_TEST tests GLPAIRS.
#
#  Discussion:
#
#    Test the numerical integration of cos(1000 x) over the range [-1,1]
#    for varying number of Gauss-Legendre quadrature nodes l.
#    The fact that only twelve digits of accuracy are obtained is due to the 
#    condition number of the summation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'GLPAIRS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  integral ( -1 <= x <= 1 ) cos(1000 x) dx' )
  print ( '' )
  print ( '    Nodes           Estimate' )
  print ( '' )

  for l in range ( 500, 620, 20 ):

    q = 0.0

    for k in range ( 1, l + 1 ):
      theta, weight, x = glpairs ( l, k )
      q = q + weight * np.cos ( 1000.0 * x )

    print ( '  %7d  %24.16g' % ( l, q ) )

  print ( '' )
  print ( '    Exact  %24.16g' % ( 0.002 * np.sin ( 1000.0 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GLPAIRS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def glpairtabulated ( l, k ):

#*****************************************************************************80
#
## GLPAIRTABULATED computes the K-th pair of an N-point Gauss-Legendre rule.
#
#  Discussion:
#
#    Data is tabulated for 1 <= L <= 100.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer L, the number of points in the given rule.
#    1 <= L <= 100.
#
#    Input, integer K, the index of the point to be returned.
#    1 <= K <= L.
#
#    Output, real THETA, WEIGHT, X, the theta coordinate, weight, 
#    and x coordinate of the point.
#
  import numpy as np
  from sys import exit

  if ( l < 1 or 100 < l ):
    print ( '' )
    print ( 'GLPAIRTABULATED - Fatal error!' )
    print ( '  Illegal value of L.' )
    exit ( 'GLPAIRTABULATED - Fatal error!' )

  if ( k < 1 or l < k ):
    print ( '' )
    print ( 'GLPAIRTABULATED - Fatal error!' )
    print ( '  Illegal value of K.' )
    exit ( 'GLPAIRTABULATED - Fatal error!' )

  theta = legendre_theta ( l, k )
  weight = legendre_weight ( l, k )

  x = np.cos ( theta )   

  return theta, weight, x

def glpairtabulated_test ( ):

#*****************************************************************************80
#
## GLPAIRTABULATED_TEST tests GLPAIRTABULATED.
#
#  Discussion:
#
#    Test the numerical integration of exp(x) over the range [-1,1]
#    for varying number of Gauss-Legendre quadrature nodes l.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'GLPAIRTABULATED_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  integral ( -1 <= x <= 1 ) exp(x) dx' )
  print ( '' )
  print ( '    Nodes           Estimate' )
  print ( '' )

  for l in range ( 1, 10 ):
    q = 0.0
    for k in range ( 1, l + 1 ):
      theta, weight, x = glpairtabulated ( l, k )
      q = q + weight * np.exp ( x )
    print ( '  %7d  %24.16g' % ( l, q ) )

  print ( '' )
  print ( '    Exact  %24.16g' % ( np.exp ( 1.0E+00 ) - np.exp ( -1.0E+00 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GLPAIRTABULATED_TEST:' )
  print ( '  Normal end of execution.' )
  return

def legendre_theta ( l, k ):

#*****************************************************************************80
#
## LEGENDRE_THETA returns the K-th theta coordinate in an L point rule.
#
#  Discussion:
#
#    The X coordinate is simply cos ( THETA ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer L, the number of points in the given rule.
#    1 <= L.
#
#    Input, integer K, the index of the point to be returned.
#    1 <= K <= L.
#
#    Output, real THETA, the theta coordinate of the point.
#
  import numpy as np
  from sys import exit

  EvenThetaZero1 = np.array ( [ \
    0.9553166181245092781638573E+00 ] )
  EvenThetaZero2 = np.array ( [ \
    0.1223899586470372591854100E+01, \
    0.5332956802491269896325121E+00 ] )
  EvenThetaZero3 = np.array ( [ \
    0.1329852612388110166006182E+01, \
    0.8483666264874876548310910E+00, \
    0.3696066519448289481138796E+00 ] )
  EvenThetaZero4 = np.array ( [ \
    0.1386317078892131346282665E+01, \
    0.1017455539490153431016397E+01, \
    0.6490365804607796100719162E+00, \
    0.2827570635937967783987981E+00 ] )
  EvenThetaZero5 = np.array ( [ \
    0.1421366498439524924081833E+01, \
    0.1122539327631709474018620E+01, \
    0.8238386589997556048023640E+00, \
    0.5255196555285001171749362E+00, \
    0.2289442988470260178701589E+00 ] )
  EvenThetaZero6 = np.array ( [ \
    0.1445233238471440081118261E+01, \
    0.1194120375947706635968399E+01, \
    0.9430552870605735796668951E+00, \
    0.6921076988818410126677201E+00, \
    0.4414870814893317611922530E+00, \
    0.1923346793046672033050762E+00 ] )
  EvenThetaZero7 = np.array ( [ \
    0.1462529992921481833498746E+01, \
    0.1246003586776677662375070E+01, \
    0.1029498592525136749641068E+01, \
    0.8130407055389454598609888E+00, \
    0.5966877608172733931509619E+00, \
    0.3806189306666775272453522E+00, \
    0.1658171411523664030454318E+00 ] )
  EvenThetaZero8 = np.array ( [ \
    0.1475640280808194256470687E+01, \
    0.1285331444322965257106517E+01, \
    0.1095033401803444343034890E+01, \
    0.9047575323895165085030778E+00, \
    0.7145252532340252146626998E+00, \
    0.5243866409035941583262629E+00, \
    0.3344986386876292124968005E+00, \
    0.1457246820036738335698855E+00 ] )
  EvenThetaZero9 = np.array ( [ \
    0.1485919440392653014379727E+01, \
    0.1316167494718022699851110E+01, \
    0.1146421481056642228295923E+01, \
    0.9766871104439832694094465E+00, \
    0.8069738930788195349918620E+00, \
    0.6373005058706191519531139E+00, \
    0.4677113145328286263205134E+00, \
    0.2983460782092324727528346E+00, \
    0.1299747364196768405406564E+00 ] )
  EvenThetaZero10 = np.array ( [ \
    0.1494194914310399553510039E+01, \
    0.1340993178589955138305166E+01, \
    0.1187794926634098887711586E+01, \
    0.1034603297590104231043189E+01, \
    0.8814230742890135843662021E+00, \
    0.7282625848696072912405713E+00, \
    0.5751385026314284688366450E+00, \
    0.4220907301111166004529037E+00, \
    0.2692452880289302424376614E+00, \
    0.1172969277059561308491253E+00 ] )
  EvenThetaZero11 = np.array ( [ \
    0.1501000399130816063282492E+01, \
    0.1361409225664372117193308E+01, \
    0.1221820208990359866348145E+01, \
    0.1082235198111836788818162E+01, \
    0.9426568273796608630446470E+00, \
    0.8030892957063359443650460E+00, \
    0.6635400754448062852164288E+00, \
    0.5240242709487281141128643E+00, \
    0.3845781703583910933413978E+00, \
    0.2453165389983612942439953E+00, \
    0.1068723357985259945018899E+00 ] )
  EvenThetaZero12 = np.array ( [ \
    0.1506695545558101030878728E+01, \
    0.1378494427506219143960887E+01, \
    0.1250294703417272987066314E+01, \
    0.1122097523267250692925104E+01, \
    0.9939044422989454674968570E+00, \
    0.8657177770401081355080608E+00, \
    0.7375413075437535618804594E+00, \
    0.6093818382449565759195927E+00, \
    0.4812531951313686873528891E+00, \
    0.3531886675690780704072227E+00, \
    0.2252936226353075734690198E+00, \
    0.9814932949793685067733311E-01 ] )
  EvenThetaZero13 = np.array ( [ \
    0.1511531546703289231944719E+01, \
    0.1393002286179807923400254E+01, \
    0.1274473959424494104852958E+01, \
    0.1155947313793812040125722E+01, \
    0.1037423319077439147088755E+01, \
    0.9189033445598992550553862E+00, \
    0.8003894803353296871788647E+00, \
    0.6818851814129298518332401E+00, \
    0.5633967073169293284500428E+00, \
    0.4449368152119130526034289E+00, \
    0.3265362611165358134766736E+00, \
    0.2082924425598466358987549E+00, \
    0.9074274842993199730441784E-01 ] )
  EvenThetaZero14 = np.array ( [ \
    0.1515689149557281132993364E+01, \
    0.1405475003062348722192382E+01, \
    0.1295261501292316172835393E+01, \
    0.1185049147889021579229406E+01, \
    0.1074838574917869281769567E+01, \
    0.9646306371285440922680794E+00, \
    0.8544265718392254369377945E+00, \
    0.7442282945111358297916378E+00, \
    0.6340389954584301734412433E+00, \
    0.5238644768825679339859620E+00, \
    0.4137165857369637683488098E+00, \
    0.3036239070914333637971179E+00, \
    0.1936769929947376175341314E+00, \
    0.8437551461511597225722252E-01 ] )
  EvenThetaZero15 = np.array ( [ \
    0.1519301729274526620713294E+01, \
    0.1416312682230741743401738E+01, \
    0.1313324092045794720169874E+01, \
    0.1210336308624476413072722E+01, \
    0.1107349759228459143499061E+01, \
    0.1004365001539081003659288E+01, \
    0.9013828087667156388167226E+00, \
    0.7984043170121235411718744E+00, \
    0.6954313000299367256853883E+00, \
    0.5924667257887385542924194E+00, \
    0.4895160050896970092628705E+00, \
    0.3865901987860504829542802E+00, \
    0.2837160095793466884313556E+00, \
    0.1809780449917272162574031E+00, \
    0.7884320726554945051322849E-01 ] )
  EvenThetaZero16 = np.array ( [ \
    0.1522469852641529230282387E+01, \
    0.1425817011963825344615095E+01, \
    0.1329164502391080681347666E+01, \
    0.1232512573416362994802398E+01, \
    0.1135861522840293704616614E+01, \
    0.1039211728068951568003361E+01, \
    0.9425636940046777101926515E+00, \
    0.8459181315837993237739032E+00, \
    0.7492760951181414487254243E+00, \
    0.6526392394594561548023681E+00, \
    0.5560103418005302722406995E+00, \
    0.4593944730762095704649700E+00, \
    0.3628020075350028174968692E+00, \
    0.2662579994723859636910796E+00, \
    0.1698418454282150179319973E+00, \
    0.7399171309970959768773072E-01 ] )
  EvenThetaZero17 = np.array ( [ \
    0.1525270780617194430047563E+01, \
    0.1434219768045409606267345E+01, \
    0.1343169000217435981125683E+01, \
    0.1252118659062444379491066E+01, \
    0.1161068957629157748792749E+01, \
    0.1070020159291475075961444E+01, \
    0.9789726059789103169325141E+00, \
    0.8879267623988119819560021E+00, \
    0.7968832893748414870413015E+00, \
    0.7058431727509840105946884E+00, \
    0.6148079652926100198490992E+00, \
    0.5237802779694730663856110E+00, \
    0.4327648832448234459097574E+00, \
    0.3417715500266717765568488E+00, \
    0.2508238767288223767569849E+00, \
    0.1599966542668327644694431E+00, \
    0.6970264809814094464033170E-01 ] )
  EvenThetaZero18 = np.array ( [ \
    0.1527764849261740485876940E+01, \
    0.1441701954349064743573367E+01, \
    0.1355639243522655042028688E+01, \
    0.1269576852063768424508476E+01, \
    0.1183514935851550608323947E+01, \
    0.1097453683555812711123880E+01, \
    0.1011393333949027021740881E+01, \
    0.9253342019812867059380523E+00, \
    0.8392767201322475821509486E+00, \
    0.7532215073977623159515351E+00, \
    0.6671694908788198522546767E+00, \
    0.5811221342350705406265672E+00, \
    0.4950819018993074588093747E+00, \
    0.4090533017972007314666814E+00, \
    0.3230455648729987995657071E+00, \
    0.2370809940997936908335290E+00, \
    0.1512302802537625099602687E+00, \
    0.6588357082399222649528476E-01 ] )
  EvenThetaZero19 = np.array ( [ \
    0.1529999863223206659623262E+01, \
    0.1448406982124841835685420E+01, \
    0.1366814241651488684482888E+01, \
    0.1285221744143731581870833E+01, \
    0.1203629605904952775544878E+01, \
    0.1122037965173751996510051E+01, \
    0.1040446993107623345153211E+01, \
    0.9588569097730895525404200E+00, \
    0.8772680085516152329147030E+00, \
    0.7956806951062012653043722E+00, \
    0.7140955526031660805347356E+00, \
    0.6325134568448222221560326E+00, \
    0.5509357927460004487348532E+00, \
    0.4693648943475422765864580E+00, \
    0.3878050333015201414955289E+00, \
    0.3062649591511896679168503E+00, \
    0.2247658146033686460963295E+00, \
    0.1433746167818849555570557E+00, \
    0.6246124541276674097388211E-01 ] )
  EvenThetaZero20 = np.array ( [ \
    0.1532014188279762793560699E+01, \
    0.1454449946977268522285131E+01, \
    0.1376885814601482670609845E+01, \
    0.1299321869764876494939757E+01, \
    0.1221758200747475205847413E+01, \
    0.1144194910846247537582396E+01, \
    0.1066632125552939823863593E+01, \
    0.9890700026972186303565530E+00, \
    0.9115087474225932692070479E+00, \
    0.8339486352158799520695092E+00, \
    0.7563900488174808348719219E+00, \
    0.6788335401193977027577509E+00, \
    0.6012799395312684623216685E+00, \
    0.5237305617022755897200291E+00, \
    0.4461876237541810478131970E+00, \
    0.3686551849119556335824055E+00, \
    0.2911415613085158758589405E+00, \
    0.2136668503694680525340165E+00, \
    0.1362947587312224822844743E+00, \
    0.5937690028966411906487257E-01 ] )
  EvenThetaZero21 = np.array ( [ \
    0.1533838971193864306068338E+01, \
    0.1459924288056445029654271E+01, \
    0.1386009690354996919044862E+01, \
    0.1312095239305276612560739E+01, \
    0.1238181002944535867235042E+01, \
    0.1164267059803796726229370E+01, \
    0.1090353503721897748980095E+01, \
    0.1016440450472067349837507E+01, \
    0.9425280472651469176638349E+00, \
    0.8686164868955467866176243E+00, \
    0.7947060295895204342519786E+00, \
    0.7207970381018823842440224E+00, \
    0.6468900366403721167107352E+00, \
    0.5729858150363658839291287E+00, \
    0.4990856247464946058899833E+00, \
    0.4251915773724379089467945E+00, \
    0.3513075400485981451355368E+00, \
    0.2774414365914335857735201E+00, \
    0.2036124177925793565507033E+00, \
    0.1298811916061515892914930E+00, \
    0.5658282534660210272754152E-01 ] )
  EvenThetaZero22 = np.array ( [ \
    0.1535499761264077326499892E+01, \
    0.1464906652494521470377318E+01, \
    0.1394313611500109323616335E+01, \
    0.1323720686538524176057236E+01, \
    0.1253127930763390908996314E+01, \
    0.1182535404796980113294400E+01, \
    0.1111943180033868679273393E+01, \
    0.1041351343083674290731439E+01, \
    0.9707600019805773720746280E+00, \
    0.9001692951667510715040632E+00, \
    0.8295794049297955988640329E+00, \
    0.7589905782114329186155957E+00, \
    0.6884031600807736268672129E+00, \
    0.6178176499732537480601935E+00, \
    0.5472348011493452159473826E+00, \
    0.4766558078624760377875119E+00, \
    0.4060826859477620301047824E+00, \
    0.3355191279517093844978473E+00, \
    0.2649727008485465487101933E+00, \
    0.1944616940738156405895778E+00, \
    0.1240440866043499301839465E+00, \
    0.5403988657613871827831605E-01 ] )
  EvenThetaZero23 = np.array ( [ \
    0.1537017713608809830855653E+01, \
    0.1469460505124226636602925E+01, \
    0.1401903350962364703169699E+01, \
    0.1334346289590505369693957E+01, \
    0.1266789363044399933941254E+01, \
    0.1199232618763735058848455E+01, \
    0.1131676111906105521856066E+01, \
    0.1064119908394702657537061E+01, \
    0.9965640890815034701957497E+00, \
    0.9290087556203499065939494E+00, \
    0.8614540390091103102510609E+00, \
    0.7939001124053586164046432E+00, \
    0.7263472110048245091518914E+00, \
    0.6587956640463586742461796E+00, \
    0.5912459486086227271608064E+00, \
    0.5236987847717837556177452E+00, \
    0.4561553147193391989386660E+00, \
    0.3886174669444433167860783E+00, \
    0.3210887745896478259115420E+00, \
    0.2535764786314617292100029E+00, \
    0.1860980813776342452540915E+00, \
    0.1187090676924131329841811E+00, \
    0.5171568198966901682810573E-01 ] )
  EvenThetaZero24 = np.array ( [ \
    0.1538410494858190444190279E+01, \
    0.1473638845472165977392911E+01, \
    0.1408867240039222913928858E+01, \
    0.1344095709533508756473909E+01, \
    0.1279324287566779722061664E+01, \
    0.1214553011719528935181709E+01, \
    0.1149781925191718586091000E+01, \
    0.1085011078936665906275419E+01, \
    0.1020240534516704208782618E+01, \
    0.9554703680422404498752066E+00, \
    0.8907006757608306209160649E+00, \
    0.8259315822134856671969566E+00, \
    0.7611632524946588128425351E+00, \
    0.6963959112887657683892237E+00, \
    0.6316298735371143844913976E+00, \
    0.5668655960010826255149266E+00, \
    0.5021037684870694065589284E+00, \
    0.4373454855522296089897130E+00, \
    0.3725925956833896735786860E+00, \
    0.3078484858841616878136371E+00, \
    0.2431200981264999375962973E+00, \
    0.1784242126043536701754986E+00, \
    0.1138140258514833068653307E+00, \
    0.4958315373802413441075340E-01 ] )
  EvenThetaZero25 = np.array ( [ \
    0.1539692973716708504412697E+01, \
    0.1477486279394502338589519E+01, \
    0.1415279620944410339318226E+01, \
    0.1353073023537942666830874E+01, \
    0.1290866514321280958405103E+01, \
    0.1228660123395079609266898E+01, \
    0.1166453885011658611362850E+01, \
    0.1104247839096738022319035E+01, \
    0.1042042033248543055386770E+01, \
    0.9798365254403234947595400E+00, \
    0.9176313877712591840677176E+00, \
    0.8554267118081827231209625E+00, \
    0.7932226163976800550406599E+00, \
    0.7310192594231560707888939E+00, \
    0.6688168560730805146438886E+00, \
    0.6066157082814543103941755E+00, \
    0.5444162542389049922529553E+00, \
    0.4822191559963931133878621E+00, \
    0.4200254643636986308379697E+00, \
    0.3578369542536859435571624E+00, \
    0.2956568781922605524959448E+00, \
    0.2334919029083292837123583E+00, \
    0.1713581437497397360313735E+00, \
    0.1093066902335822942650053E+00, \
    0.4761952998197036029817629E-01 ] )
  EvenThetaZero26 = np.array ( [ \
    0.1540877753740080417345045E+01, \
    0.1481040617373741365390254E+01, \
    0.1421203510518656600018143E+01, \
    0.1361366453804322852131292E+01, \
    0.1301529469356044341206877E+01, \
    0.1241692581525935716830402E+01, \
    0.1181855817774264617619371E+01, \
    0.1122019209772750368801179E+01, \
    0.1062182794829879659341536E+01, \
    0.1002346617783007482854908E+01, \
    0.9425107335729934538419206E+00, \
    0.8826752108319277463183701E+00, \
    0.8228401370047382776784725E+00, \
    0.7630056258499810562932058E+00, \
    0.7031718287376427885875898E+00, \
    0.6433389522119553277924537E+00, \
    0.5835072863023426715977658E+00, \
    0.5236772521416453354847559E+00, \
    0.4638494862268433259444639E+00, \
    0.4040249990308909882616381E+00, \
    0.3442054975680110060507306E+00, \
    0.2843941101955779333389742E+00, \
    0.2245972494281051799602510E+00, \
    0.1648304164747050021714385E+00, \
    0.1051427544146599992432949E+00, \
    0.4580550859172367960799915E-01 ] )
  EvenThetaZero27 = np.array ( [ \
    0.1541975588842621898865181E+01, \
    0.1484334121018556567335167E+01, \
    0.1426692677652358867201800E+01, \
    0.1369051275783071487471360E+01, \
    0.1311409933595114953831618E+01, \
    0.1253768670970438091691833E+01, \
    0.1196127510146226323327062E+01, \
    0.1138486476526912406867032E+01, \
    0.1080845599717322003702293E+01, \
    0.1023204914871722785830020E+01, \
    0.9655644644970043364617272E+00, \
    0.9079243009168822510582606E+00, \
    0.8502844897148263889326479E+00, \
    0.7926451146568312828354346E+00, \
    0.7350062849078710810840430E+00, \
    0.6773681459074923011631400E+00, \
    0.6197308962817025162722438E+00, \
    0.5620948151095422609589585E+00, \
    0.5044603077892199488064657E+00, \
    0.4468279872027509013135997E+00, \
    0.3891988265038338944044115E+00, \
    0.3315744698431505326770711E+00, \
    0.2739579305700525818998611E+00, \
    0.2163553856859193758294342E+00, \
    0.1587817673749480300092784E+00, \
    0.1012844151694839452028589E+00, \
    0.4412462056235422293371300E-01 ] )
  EvenThetaZero28 = np.array ( [ \
    0.1542995710582548837472073E+01, \
    0.1487394484904746766220933E+01, \
    0.1431793279635669382208875E+01, \
    0.1376192108950239363921811E+01, \
    0.1320590987909222553912422E+01, \
    0.1264989932881031519687125E+01, \
    0.1209388962038683919740547E+01, \
    0.1153788095965648154683658E+01, \
    0.1098187358416032947576489E+01, \
    0.1042586777292402877200408E+01, \
    0.9869863859317282394719449E+00, \
    0.9313862248321055503829503E+00, \
    0.8757863440192765677772914E+00, \
    0.8201868063589761051746975E+00, \
    0.7645876922981545448147078E+00, \
    0.7089891068198449136125464E+00, \
    0.6533911899285832425290628E+00, \
    0.5977941329592257586198087E+00, \
    0.5421982048745539015834188E+00, \
    0.4866037965045890355211229E+00, \
    0.4310114988353693539492225E+00, \
    0.3754222503860499120445385E+00, \
    0.3198376369331602148544626E+00, \
    0.2642605649958747239907310E+00, \
    0.2086969927688100977274751E+00, \
    0.1531613237261629042774314E+00, \
    0.9769922156300582041279299E-01, \
    0.4256272861907242306694832E-01 ] )
  EvenThetaZero29 = np.array ( [ \
    0.1543946088331101630230404E+01, \
    0.1490245617072432741470241E+01, \
    0.1436545162952171175361532E+01, \
    0.1382844737841275627385236E+01, \
    0.1329144354302189376680665E+01, \
    0.1275444025914442882448630E+01, \
    0.1221743767654456436125309E+01, \
    0.1168043596353244531685999E+01, \
    0.1114343531263457295536939E+01, \
    0.1060643594778787047442989E+01, \
    0.1006943813366184678568021E+01, \
    0.9532442187977767941200107E+00, \
    0.8995448498101763729640445E+00, \
    0.8458457543830885615091264E+00, \
    0.7921469929325243736682034E+00, \
    0.7384486428849507503612470E+00, \
    0.6847508053901545384892447E+00, \
    0.6310536154445759741044291E+00, \
    0.5773572576394624029563656E+00, \
    0.5236619915567428835581025E+00, \
    0.4699681944935857341529219E+00, \
    0.4162764370726533962791279E+00, \
    0.3625876255789859906927245E+00, \
    0.3089032914359211154562848E+00, \
    0.2552262416643531728802047E+00, \
    0.2015622306384971766058615E+00, \
    0.1479251692966707827334002E+00, \
    0.9435916010280739398532997E-01, \
    0.4110762866287674188292735E-01 ] )
  EvenThetaZero30 = np.array ( [ \
    0.1544833637851665335244669E+01, \
    0.1492908264756388370493025E+01, \
    0.1440982906138650837480037E+01, \
    0.1389057572001580364167786E+01, \
    0.1337132272892735072773304E+01, \
    0.1285207020157876647295968E+01, \
    0.1233281826234298389291217E+01, \
    0.1181356705000596722238457E+01, \
    0.1129431672204958843918638E+01, \
    0.1077506746001711267258715E+01, \
    0.1025581947637229234301640E+01, \
    0.9736573023432582093437126E+00, \
    0.9217328405213548692702866E+00, \
    0.8698085993416727107979968E+00, \
    0.8178846249414537373941032E+00, \
    0.7659609755086193214466010E+00, \
    0.7140377257012462393241274E+00, \
    0.6621149731355525426273686E+00, \
    0.6101928481720243483360470E+00, \
    0.5582715291407654489802101E+00, \
    0.5063512668959282414914789E+00, \
    0.4544324261262307197237056E+00, \
    0.4025155584642650335664553E+00, \
    0.3506015401168133792671488E+00, \
    0.2986918517703509333332016E+00, \
    0.2467892075469457255751440E+00, \
    0.1948991714956708008247732E+00, \
    0.1430351946011564171352354E+00, \
    0.9123992133264713232350199E-01, \
    0.3974873026126591246235829E-01 ] )
  EvenThetaZero31 = np.array ( [ \
    0.1545664389841685834178882E+01, \
    0.1495400520006868605194165E+01, \
    0.1445136662469633349524466E+01, \
    0.1394872825707861196682996E+01, \
    0.1344609018631531661347402E+01, \
    0.1294345250782284139500904E+01, \
    0.1244081532562166402923175E+01, \
    0.1193817875503760392032898E+01, \
    0.1143554292597402872188167E+01, \
    0.1093290798696377946301336E+01, \
    0.1043027411028491785799717E+01, \
    0.9927641498535133311947588E+00, \
    0.9425010393224361375194941E+00, \
    0.8922381086194002226900769E+00, \
    0.8419753935054036625982058E+00, \
    0.7917129384431112475049142E+00, \
    0.7414507995789214800057706E+00, \
    0.6911890490185720721582180E+00, \
    0.6409277811053987947460976E+00, \
    0.5906671218914768219060599E+00, \
    0.5404072438741681591850965E+00, \
    0.4901483897634232956856935E+00, \
    0.4398909124691513811974471E+00, \
    0.3896353458699818240468259E+00, \
    0.3393825380385224469051922E+00, \
    0.2891339221891949677776928E+00, \
    0.2388921255071779766209942E+00, \
    0.1886625339124777570188312E+00, \
    0.1384581678870181657476050E+00, \
    0.8832030722827102577102185E-01, \
    0.3847679847963676404657822E-01 ] )
  EvenThetaZero32 = np.array ( [ \
    0.1546443627125265521960044E+01, \
    0.1497738231263909315513507E+01, \
    0.1449032845902631477147772E+01, \
    0.1400327478265391242178337E+01, \
    0.1351622135921668846451224E+01, \
    0.1302916826944702448727527E+01, \
    0.1254211560091483702838765E+01, \
    0.1205506345013417018443405E+01, \
    0.1156801192508980685500292E+01, \
    0.1108096114833249453312212E+01, \
    0.1059391126084216587933501E+01, \
    0.1010686242693213908544820E+01, \
    0.9619814840575052973573711E+00, \
    0.9132768733691264344256970E+00, \
    0.8645724387181842642305406E+00, \
    0.8158682145859558652971026E+00, \
    0.7671642439014559105969752E+00, \
    0.7184605809290069459742089E+00, \
    0.6697572954095121564500879E+00, \
    0.6210544786425143220264938E+00, \
    0.5723522526623283741373995E+00, \
    0.5236507845164779831804685E+00, \
    0.4749503092950064087413842E+00, \
    0.4262511688770346357064771E+00, \
    0.3775538805043668894422883E+00, \
    0.3288592658750793954850446E+00, \
    0.2801687136893753887834348E+00, \
    0.2314847695998852605184853E+00, \
    0.1828126524563463299986617E+00, \
    0.1341649789468091132459783E+00, \
    0.8558174883654483804697753E-01, \
    0.3728374374031613183399036E-01 ] )
  EvenThetaZero33 = np.array ( [ \
    0.1547175997094614757138430E+01, \
    0.1499935340679181525271649E+01, \
    0.1452694693272706215568985E+01, \
    0.1405454061061768876728643E+01, \
    0.1358213450511184239883293E+01, \
    0.1310972868490444296079765E+01, \
    0.1263732322416537730871712E+01, \
    0.1216491820419724046503073E+01, \
    0.1169251371540540180758674E+01, \
    0.1122010985968754004469355E+01, \
    0.1074770675338453464761893E+01, \
    0.1027530453098431393666936E+01, \
    0.9802903349842005856557204E+00, \
    0.9330503396284544173873149E+00, \
    0.8858104893623263267477775E+00, \
    0.8385708112832335506864354E+00, \
    0.7913313387011139500976360E+00, \
    0.7440921131314510897906335E+00, \
    0.6968531870945337206139839E+00, \
    0.6496146281309018959581539E+00, \
    0.6023765246993705639765525E+00, \
    0.5551389950762090311242875E+00, \
    0.5079022012032895030848024E+00, \
    0.4606663710240282967569630E+00, \
    0.4134318360639670775957014E+00, \
    0.3661990979414348851212686E+00, \
    0.3189689535781378596191439E+00, \
    0.2717427498485401725509746E+00, \
    0.2245229557871702595200694E+00, \
    0.1773146332323969343091350E+00, \
    0.1301300193754780766338959E+00, \
    0.8300791095077070533235660E-01, \
    0.3616244959900389221395842E-01 ] )
  EvenThetaZero34 = np.array ( [ \
    0.1547865604457777747119921E+01, \
    0.1502004162357357213441384E+01, \
    0.1456142728021903760325049E+01, \
    0.1410281306774684706589738E+01, \
    0.1364419904164498130803254E+01, \
    0.1318558526067441138200403E+01, \
    0.1272697178801115154796514E+01, \
    0.1226835869256177571730448E+01, \
    0.1180974605051351016009903E+01, \
    0.1135113394719709026888693E+01, \
    0.1089252247936466574864114E+01, \
    0.1043391175801911243726755E+01, \
    0.9975301911979639874925565E+00, \
    0.9516693092438447484954432E+00, \
    0.9058085478865097428655118E+00, \
    0.8599479286766250282572181E+00, \
    0.8140874778035996603018790E+00, \
    0.7682272274981820559251592E+00, \
    0.7223672179660643783333797E+00, \
    0.6765075001043380283085699E+00, \
    0.6306481393987597674748178E+00, \
    0.5847892216487432573582268E+00, \
    0.5389308616059791284685642E+00, \
    0.4930732164176132508179420E+00, \
    0.4472165073094733435432890E+00, \
    0.4013610560689043520551232E+00, \
    0.3555073496130768130758891E+00, \
    0.3096561615434305328219637E+00, \
    0.2638087993597793691714182E+00, \
    0.2179676599607749036552390E+00, \
    0.1721376573496165890967450E+00, \
    0.1263306713881449555499955E+00, \
    0.8058436603519718986295825E-01, \
    0.3510663068970053260227480E-01 ] )
  EvenThetaZero35 = np.array ( [ \
    0.1548516088202564202943238E+01, \
    0.1503955613246577879586994E+01, \
    0.1459395145012190281751360E+01, \
    0.1414834688100222735099866E+01, \
    0.1370274247295441414922756E+01, \
    0.1325713827649021532002630E+01, \
    0.1281153434570536124285912E+01, \
    0.1236593073933169034954499E+01, \
    0.1192032752196710979323473E+01, \
    0.1147472476554108430135576E+01, \
    0.1102912255109027578275434E+01, \
    0.1058352097094263144928973E+01, \
    0.1013792013144153206047048E+01, \
    0.9692320156388929821870602E+00, \
    0.9246721191454417746654622E+00, \
    0.8801123409896300773149632E+00, \
    0.8355527020087518049947413E+00, \
    0.7909932275560464363973909E+00, \
    0.7464339488624693592395086E+00, \
    0.7018749049145358048463504E+00, \
    0.6573161450929179933243905E+00, \
    0.6127577329584494909986789E+00, \
    0.5681997518140860838771656E+00, \
    0.5236423130979094957496400E+00, \
    0.4790855694444512920982626E+00, \
    0.4345297357523596151738496E+00, \
    0.3899751246318782591316393E+00, \
    0.3454222091410984787772492E+00, \
    0.3008717408917773811461237E+00, \
    0.2563249902500918978614004E+00, \
    0.2117842860782107775954396E+00, \
    0.1672544029381415755198150E+00, \
    0.1227468836419337342946123E+00, \
    0.7829832364814667171382217E-01, \
    0.3411071484766340151578357E-01 ] )
  EvenThetaZero36 = np.array ( [ \
    0.1549130685823945998342524E+01, \
    0.1505799405819664254557106E+01, \
    0.1462468131657470292685966E+01, \
    0.1419136867330461353369368E+01, \
    0.1375805616982638895139986E+01, \
    0.1332474384976155365522566E+01, \
    0.1289143175965912901391449E+01, \
    0.1245811994984327181800398E+01, \
    0.1202480847539690438616688E+01, \
    0.1159149739732435788417226E+01, \
    0.1115818678394807971862305E+01, \
    0.1072487671261111519215409E+01, \
    0.1029156727178025494814510E+01, \
    0.9858258563677261466814511E+00, \
    0.9424950707611702085500992E+00, \
    0.8991643844255133860018485E+00, \
    0.8558338141192845596532563E+00, \
    0.8125033800232146117493243E+00, \
    0.7691731067161328174004981E+00, \
    0.7258430244984030733808537E+00, \
    0.6825131712172895509836733E+00, \
    0.6391835948321685576634513E+00, \
    0.5958543570955633038336902E+00, \
    0.5525255389612023677479152E+00, \
    0.5091972487450747080139606E+00, \
    0.4658696348260689008126722E+00, \
    0.4225429061321313393543928E+00, \
    0.3792173666095906812269559E+00, \
    0.3358934762285008809293807E+00, \
    0.2925719658301625547639832E+00, \
    0.2492540707015179370724365E+00, \
    0.2059420554273186332219697E+00, \
    0.1626405628266886976038507E+00, \
    0.1193608172622853851645011E+00, \
    0.7613840464754681957544313E-01, \
    0.3316974474186058622824911E-01 ] )
  EvenThetaZero37 = np.array ( [ \
    0.1549712287207882890839045E+01, \
    0.1507544209724862511636878E+01, \
    0.1465376137339015815734558E+01, \
    0.1423208073529702865859582E+01, \
    0.1381040021900765225468989E+01, \
    0.1338871986235691269778498E+01, \
    0.1296703970558498635765633E+01, \
    0.1254535979202491212629656E+01, \
    0.1212368016889500927716256E+01, \
    0.1170200088822853513468851E+01, \
    0.1128032200798161849314963E+01, \
    0.1085864359337236600941540E+01, \
    0.1043696571852037437540940E+01, \
    0.1001528846847853898635169E+01, \
    0.9593611941780778060127795E+00, \
    0.9171936253674231737318512E+00, \
    0.8750261540268988114426643E+00, \
    0.8328587963932301252176965E+00, \
    0.7906915720393251716472997E+00, \
    0.7485245048233193695739358E+00, \
    0.7063576241759074809548715E+00, \
    0.6641909668761970070284373E+00, \
    0.6220245795476036586681135E+00, \
    0.5798585222396645710869275E+00, \
    0.5376928736905555113005422E+00, \
    0.4955277392687366749125653E+00, \
    0.4533632633323484070376718E+00, \
    0.4111996491651493998151895E+00, \
    0.3690371925202636251212886E+00, \
    0.3268763409876008462653069E+00, \
    0.2847178057580674399826003E+00, \
    0.2425627889274157106498810E+00, \
    0.2004134942584602007834507E+00, \
    0.1582744399049656648660257E+00, \
    0.1161565488818554609430574E+00, \
    0.7409445176394481360104851E-01, \
    0.3227929535095246410912398E-01 ] )
  EvenThetaZero38 = np.array ( [ \
    0.1550263480064160377720298E+01, \
    0.1509197788083808185665328E+01, \
    0.1468132100566875710992083E+01, \
    0.1427066420556418463513913E+01, \
    0.1386000751198712817289420E+01, \
    0.1344935095788765217267069E+01, \
    0.1303869457820298477498722E+01, \
    0.1262803841041882838326682E+01, \
    0.1221738249521212843639205E+01, \
    0.1180672687719991159061894E+01, \
    0.1139607160582508034089119E+01, \
    0.1098541673641858946868449E+01, \
    0.1057476233148907719560749E+01, \
    0.1016410846230700992453501E+01, \
    0.9753455210872527645472818E+00, \
    0.9342802672387126698703291E+00, \
    0.8932150958393123732306518E+00, \
    0.8521500200807685012223049E+00, \
    0.8110850557169691024167180E+00, \
    0.7700202217553081279468270E+00, \
    0.7289555413804262510029339E+00, \
    0.6878910432074509889956044E+00, \
    0.6468267630110350344178276E+00, \
    0.6057627461556542068727688E+00, \
    0.5646990510834698732732127E+00, \
    0.5236357544389875315454201E+00, \
    0.4825729588028297682338108E+00, \
    0.4415108047277878179738561E+00, \
    0.4004494901533595099830119E+00, \
    0.3593893030723592157150581E+00, \
    0.3183306793460978083354355E+00, \
    0.2772743115465352362860883E+00, \
    0.2362213703174823832436869E+00, \
    0.1951740017836102296584907E+00, \
    0.1541366059551230775894261E+00, \
    0.1131198202589878992052369E+00, \
    0.7215736988593890187079586E-01, \
    0.3143540438351454384152236E-01 ] )
  EvenThetaZero39 = np.array ( [ \
    0.1550786588415152297375587E+01, \
    0.1510767112957397367780716E+01, \
    0.1470747641421582916022579E+01, \
    0.1430728176478592843861361E+01, \
    0.1390708720885325111445925E+01, \
    0.1350689277522434511387126E+01, \
    0.1310669849435604714836514E+01, \
    0.1270650439881648370588402E+01, \
    0.1230631052380981613091250E+01, \
    0.1190611690778358944744052E+01, \
    0.1150592359314214516523625E+01, \
    0.1110573062709576809284752E+01, \
    0.1070553806268363352417161E+01, \
    0.1030534596002003296175373E+01, \
    0.9905154387828984834423913E+00, \
    0.9504963425353941517573974E+00, \
    0.9104773164759498161192732E+00, \
    0.8704583714184727086854142E+00, \
    0.8304395201669023270865304E+00, \
    0.7904207780260519973626051E+00, \
    0.7504021634749074983118715E+00, \
    0.7103836990664583264642972E+00, \
    0.6703654126486745769832673E+00, \
    0.6303473390491956215820085E+00, \
    0.5903295224434431765765323E+00, \
    0.5503120197533818815098408E+00, \
    0.5102949056413983084126817E+00, \
    0.4702782800468414863285692E+00, \
    0.4302622799152491769326599E+00, \
    0.3902470981180917254123191E+00, \
    0.3502330152869736207185960E+00, \
    0.3102204561556976356809728E+00, \
    0.2702100956292792195263915E+00, \
    0.2302030745053307298726703E+00, \
    0.1902014842102915167005070E+00, \
    0.1502096126336221315300686E+00, \
    0.1102378261690820867329259E+00, \
    0.7031899075931525095025389E-01, \
    0.3063451333411226493032265E-01 ] )
  EvenThetaZero40 = np.array ( [ \
    0.1551283705347968314195100E+01, \
    0.1512258463601911009913297E+01, \
    0.1473233225313284690780287E+01, \
    0.1434207992834186122366616E+01, \
    0.1395182768588723275108301E+01, \
    0.1356157555104474252423723E+01, \
    0.1317132355046745793679891E+01, \
    0.1278107171256650000336432E+01, \
    0.1239082006794203284097135E+01, \
    0.1200056864987904389011051E+01, \
    0.1161031749492588664002624E+01, \
    0.1122006664357811755961100E+01, \
    0.1082981614109627397900573E+01, \
    0.1043956603849447575483550E+01, \
    0.1004931639374790125389322E+01, \
    0.9659067273282460489273148E+00, \
    0.9268818753831082867718635E+00, \
    0.8878570924770502938457708E+00, \
    0.8488323891094102606331406E+00, \
    0.8098077777236123075833052E+00, \
    0.7707832732049530424809748E+00, \
    0.7317588935368492604710264E+00, \
    0.6927346606780251833003950E+00, \
    0.6537106017528970872810663E+00, \
    0.6146867506941756306797580E+00, \
    0.5756631505519364744300804E+00, \
    0.5366398568077528417370132E+00, \
    0.4976169422443344500752625E+00, \
    0.4585945042946725387136724E+00, \
    0.4195726764797194195007418E+00, \
    0.3805516468579533335376469E+00, \
    0.3415316890685593880011997E+00, \
    0.3025132172735989410463832E+00, \
    0.2634968895917008761291809E+00, \
    0.2244838184598823563259898E+00, \
    0.1854760433267094750424413E+00, \
    0.1464777455344068532549101E+00, \
    0.1074990339130794792907032E+00, \
    0.6857195785426972961368108E-01, \
    0.2987341732561906608807860E-01 ] )
  EvenThetaZero41 = np.array ( [ \
    0.1551756721003315464043007E+01, \
    0.1513677510435354867644006E+01, \
    0.1475598302924814895692182E+01, \
    0.1437519100549654116408972E+01, \
    0.1399439905448387106945081E+01, \
    0.1361360719846430407096351E+01, \
    0.1323281546084682430842605E+01, \
    0.1285202386651141609385598E+01, \
    0.1247123244216506877361870E+01, \
    0.1209044121674894401873626E+01, \
    0.1170965022191058363946285E+01, \
    0.1132885949255841486220662E+01, \
    0.1094806906752030657845562E+01, \
    0.1056727899033393535018723E+01, \
    0.1018648931020478788570327E+01, \
    0.9805700083178549567966928E+00, \
    0.9424911373589552049711100E+00, \
    0.9044123255867553868253384E+00, \
    0.8663335816813894348633149E+00, \
    0.8282549158498738099497389E+00, \
    0.7901763401989443875774432E+00, \
    0.7520978692204962458482329E+00, \
    0.7140195204316730003387055E+00, \
    0.6759413152305656820841666E+00, \
    0.6378632800575392064866756E+00, \
    0.5997854479978337579981629E+00, \
    0.5617078610344953281799357E+00, \
    0.5236305732820186728652802E+00, \
    0.4855536557378012985520074E+00, \
    0.4474772034530068342865487E+00, \
    0.4094013466928584958758982E+00, \
    0.3713262689388439070717808E+00, \
    0.3332522371792479009733062E+00, \
    0.2951796555193184134657530E+00, \
    0.2571091661074227554417865E+00, \
    0.2190418543971735546480404E+00, \
    0.1809797103814301725822348E+00, \
    0.1429268140230164119614409E+00, \
    0.1048930290780323497410212E+00, \
    0.6690962797843649866645769E-01, \
    0.2914922224685900914817542E-01 ] )
  EvenThetaZero42 = np.array ( [ \
    0.1552207346590136182648920E+01, \
    0.1515029387081184115266415E+01, \
    0.1477851430283927973458023E+01, \
    0.1440673478039699629370259E+01, \
    0.1403495532240969264030648E+01, \
    0.1366317594853508812224152E+01, \
    0.1329139667940348087929429E+01, \
    0.1291961753688162615428688E+01, \
    0.1254783854436838464182091E+01, \
    0.1217605972713102930414639E+01, \
    0.1180428111269300876868432E+01, \
    0.1143250273128649048802100E+01, \
    0.1106072461638634327789036E+01, \
    0.1068894680534663975270023E+01, \
    0.1031716934016664760314029E+01, \
    0.9945392268421176498894610E+00, \
    0.9573615644400829018748874E+00, \
    0.9201839530522288586731642E+00, \
    0.8830063999088902711516820E+00, \
    0.8458289134509915302518266E+00, \
    0.8086515036126424512848147E+00, \
    0.7714741821849085841225787E+00, \
    0.7342969632895448309937051E+00, \
    0.6971198640037406540069491E+00, \
    0.6599429051953912854163132E+00, \
    0.6227661126567800124770610E+00, \
    0.5855895186691062254659102E+00, \
    0.5484131642019636734351025E+00, \
    0.5112371020703309674589504E+00, \
    0.4740614015734592960802666E+00, \
    0.4368861554959151187817336E+00, \
    0.3997114910036376358365916E+00, \
    0.3625375872199777754435892E+00, \
    0.3253647047992267079974806E+00, \
    0.2881932382678453273830096E+00, \
    0.2510238145617968753500674E+00, \
    0.2138574934303919974438356E+00, \
    0.1766962177535783269128215E+00, \
    0.1395439709154010255199071E+00, \
    0.1024103832005221866954023E+00, \
    0.6532598686141261097119747E-01, \
    0.2845930797694291389393445E-01 ] )
  EvenThetaZero43 = np.array ( [ \
    0.1552637135069155811491072E+01, \
    0.1516318752418798211357541E+01, \
    0.1480000372180291690418989E+01, \
    0.1443681995989991700140976E+01, \
    0.1407363625527612735973164E+01, \
    0.1371045262534953065860219E+01, \
    0.1334726908836065747097909E+01, \
    0.1298408566359386697763653E+01, \
    0.1262090237162411913706886E+01, \
    0.1225771923459625279363960E+01, \
    0.1189453627654523146514386E+01, \
    0.1153135352376772077918208E+01, \
    0.1116817100525785826106551E+01, \
    0.1080498875322336017099434E+01, \
    0.1044180680370244915946738E+01, \
    0.1007862519730785566833872E+01, \
    0.9715443980131875264637689E+00, \
    0.9352263204856910439167915E+00, \
    0.8989082932130182550456316E+00, \
    0.8625903232280967802521182E+00, \
    0.8262724187486163930514201E+00, \
    0.7899545894528804342126058E+00, \
    0.7536368468349768085155075E+00, \
    0.7173192046673890278545072E+00, \
    0.6810016796111441673128480E+00, \
    0.6446842920316340773745262E+00, \
    0.6083670671059611518530899E+00, \
    0.5720500363511797523369558E+00, \
    0.5357332397728172506411618E+00, \
    0.4994167289487775362163415E+00, \
    0.4631005715608865274454686E+00, \
    0.4267848582339839676363509E+00, \
    0.3904697131799790288672503E+00, \
    0.3541553113674441557740819E+00, \
    0.3178419074113077198829473E+00, \
    0.2815298867038369044519273E+00, \
    0.2452198616736214006194288E+00, \
    0.2089128675558041239775998E+00, \
    0.1726108022974787183994402E+00, \
    0.1363175571713249458600521E+00, \
    0.1000425397881322914313825E+00, \
    0.6381557644960651200944222E-01, \
    0.2780129671121636039734655E-01 ] )
  EvenThetaZero44 = np.array ( [ \
    0.1553047499032218401181962E+01, \
    0.1517549844221432542461907E+01, \
    0.1482052191561582448658478E+01, \
    0.1446554542510861055782865E+01, \
    0.1411056898564365493121105E+01, \
    0.1375559261269981001734724E+01, \
    0.1340061632245437638964436E+01, \
    0.1304564013196950335363525E+01, \
    0.1269066405939915513649123E+01, \
    0.1233568812422221364483924E+01, \
    0.1198071234750839346739124E+01, \
    0.1162573675222508872274463E+01, \
    0.1127076136359515473862368E+01, \
    0.1091578620951808778363231E+01, \
    0.1056081132107029235444226E+01, \
    0.1020583673310438024843461E+01, \
    0.9850862484973095869616622E+00, \
    0.9495888621411026369897815E+00, \
    0.9140915193617473526041913E+00, \
    0.8785942260597805964360395E+00, \
    0.8430969890839839780181254E+00, \
    0.8075998164428632814935249E+00, \
    0.7721027175741014967901450E+00, \
    0.7366057036915554827257553E+00, \
    0.7011087882372792641869964E+00, \
    0.6656119874777629720186974E+00, \
    0.6301153213012084608241887E+00, \
    0.5946188142997514629085459E+00, \
    0.5591224972630766104664894E+00, \
    0.5236264092783024624074546E+00, \
    0.4881306007441175888503326E+00, \
    0.4526351377998500905914452E+00, \
    0.4171401090099414677462070E+00, \
    0.3816456357674021470057899E+00, \
    0.3461518890753412856675063E+00, \
    0.3106591177837409768492156E+00, \
    0.2751676985649013361686770E+00, \
    0.2396782299970584002479842E+00, \
    0.2041917239104339765549482E+00, \
    0.1687100353513348647833163E+00, \
    0.1332369676454340307348264E+00, \
    0.9778171579501174586520881E-01, \
    0.6237343205901608270979365E-01, \
    0.2717302558182235133513210E-01 ] )
  EvenThetaZero45 = np.array ( [ \
    0.1553439726211153891540573E+01, \
    0.1518726525682668668950427E+01, \
    0.1484013327077361052080319E+01, \
    0.1449300131698066374929113E+01, \
    0.1414586940879145218883617E+01, \
    0.1379873756000009717714844E+01, \
    0.1345160578499605494109603E+01, \
    0.1310447409892181029407508E+01, \
    0.1275734251784724823396464E+01, \
    0.1241021105896515467487132E+01, \
    0.1206307974081314658309029E+01, \
    0.1171594858352843571506531E+01, \
    0.1136881760914326165420300E+01, \
    0.1102168684193068774494217E+01, \
    0.1067455630881287279906518E+01, \
    0.1032742603984709761582283E+01, \
    0.9980296068808995413713835E+00, \
    0.9633166433897968474836258E+00, \
    0.9286037178597176902839922E+00, \
    0.8938908352730483454962679E+00, \
    0.8591780013772376740585140E+00, \
    0.8244652228485703565016715E+00, \
    0.7897525074988288740747291E+00, \
    0.7550398645386622329842600E+00, \
    0.7203273049167972965433221E+00, \
    0.6856148417619669061621766E+00, \
    0.6509024909658764678789680E+00, \
    0.6161902719627732109904446E+00, \
    0.5814782087876726421060849E+00, \
    0.5467663315368932859708410E+00, \
    0.5120546784214694424751802E+00, \
    0.4773432987146161851453875E+00, \
    0.4426322570828636775769209E+00, \
    0.4079216401227574252826633E+00, \
    0.3732115665343573673240355E+00, \
    0.3385022035318641142927744E+00, \
    0.3037937944563405612019789E+00, \
    0.2690867076466992914990193E+00, \
    0.2343815284441088285495466E+00, \
    0.1996792463094099012688324E+00, \
    0.1649816752853099621072722E+00, \
    0.1302925346385956500837770E+00, \
    0.9562081616094948269905207E-01, \
    0.6099502786102040135198395E-01, \
    0.2657252290854776665952679E-01 ] )
  EvenThetaZero46 = np.array ( [ \
    0.1553814992974904767594241E+01, \
    0.1519852325907741898557817E+01, \
    0.1485889660564341242674032E+01, \
    0.1451926998111647785152899E+01, \
    0.1417964339743630985906479E+01, \
    0.1384001686692845945859686E+01, \
    0.1350039040242776872946770E+01, \
    0.1316076401741232369348729E+01, \
    0.1282113772615099921371445E+01, \
    0.1248151154386817288949698E+01, \
    0.1214188548692984168143550E+01, \
    0.1180225957305622474388020E+01, \
    0.1146263382156703179022046E+01, \
    0.1112300825366698998613230E+01, \
    0.1078338289278105103916832E+01, \
    0.1044375776495107627552926E+01, \
    0.1010413289930890288650173E+01, \
    0.9764508328644780886953041E+00, \
    0.9424884090095589354132202E+00, \
    0.9085260225984488659490189E+00, \
    0.8745636784853451215455853E+00, \
    0.8406013822743460048537475E+00, \
    0.8066391404795569177534715E+00, \
    0.7726769607271702244889884E+00, \
    0.7387148520130367387469271E+00, \
    0.7047528250344497011443004E+00, \
    0.6707908926224332706815892E+00, \
    0.6368290703120276715090693E+00, \
    0.6028673771049329733376093E+00, \
    0.5689058365047911420524623E+00, \
    0.5349444779460832748774921E+00, \
    0.5009833388030907720537138E+00, \
    0.4670224672735823328060142E+00, \
    0.4330619266162571710985599E+00, \
    0.3991018015460700850326972E+00, \
    0.3651422081877256344485503E+00, \
    0.3311833101314466311103548E+00, \
    0.2972253454486352538763297E+00, \
    0.2632686745061683534910424E+00, \
    0.2293138699815081215985284E+00, \
    0.1953618999343470689252174E+00, \
    0.1614145391777897730914718E+00, \
    0.1274754265555317105245073E+00, \
    0.9355335943686297111639257E-01, \
    0.5967622944002585907962555E-01, \
    0.2599798753052849047032580E-01 ] )
  EvenThetaZero47 = np.array ( [ \
    0.1554174376112911655131098E+01, \
    0.1520930475263640362170511E+01, \
    0.1487686575963027013435604E+01, \
    0.1454442679258803180913942E+01, \
    0.1421198786221944168258440E+01, \
    0.1387954897956585365296993E+01, \
    0.1354711015610581847809736E+01, \
    0.1321467140386931222410853E+01, \
    0.1288223273556309404505081E+01, \
    0.1254979416471008337267759E+01, \
    0.1221735570580615776412743E+01, \
    0.1188491737449843097435062E+01, \
    0.1155247918778991542491874E+01, \
    0.1122004116427655660730083E+01, \
    0.1088760332442401967089102E+01, \
    0.1055516569089340593777585E+01, \
    0.1022272828892740925095715E+01, \
    0.9890291146811467076264609E+00, \
    0.9557854296428465678959260E+00, \
    0.9225417773930866874628226E+00, \
    0.8892981620561221868061383E+00, \
    0.8560545883661619186153440E+00, \
    0.8228110617925680415850631E+00, \
    0.7895675886964734656602191E+00, \
    0.7563241765284943282959446E+00, \
    0.7230808340807681383862155E+00, \
    0.6898375718116413059811978E+00, \
    0.6565944022687408111136058E+00, \
    0.6233513406471279431598408E+00, \
    0.5901084055357449335782332E+00, \
    0.5568656199307345199294838E+00, \
    0.5236230126340485109018232E+00, \
    0.4903806202198476810807501E+00, \
    0.4571384898571183050552302E+00, \
    0.4238966834573972483152713E+00, \
    0.3906552839347125500730013E+00, \
    0.3574144049483910279156003E+00, \
    0.3241742066189948531421192E+00, \
    0.2909349219721993995636414E+00, \
    0.2576969037411283384416169E+00, \
    0.2244607124763750082606152E+00, \
    0.1912272957431274569912962E+00, \
    0.1579983907861406744991899E+00, \
    0.1247775594308675650267811E+00, \
    0.9157341285433675818728635E-01, \
    0.5841325237532701385812948E-01, \
    0.2544777076240816313972829E-01 ] )
  EvenThetaZero48 = np.array ( [ \
    0.1554518863153354618809409E+01, \
    0.1521963936333782670214978E+01, \
    0.1489409010908686292228052E+01, \
    0.1456854087820918568482631E+01, \
    0.1424299168033388494075931E+01, \
    0.1391744252537595165009714E+01, \
    0.1359189342362693116905575E+01, \
    0.1326634438585269225516707E+01, \
    0.1294079542340034988016159E+01, \
    0.1261524654831668904330407E+01, \
    0.1228969777348083696352705E+01, \
    0.1196414911275444418157033E+01, \
    0.1163860058115329026827193E+01, \
    0.1131305219504506571098859E+01, \
    0.1098750397237914982841550E+01, \
    0.1066195593295557461150055E+01, \
    0.1033640809874212986016967E+01, \
    0.1001086049425085324651032E+01, \
    0.9685313146988134601280153E+00, \
    0.9359766087996588330547245E+00, \
    0.9034219352512048766203636E+00, \
    0.8708672980765996496647291E+00, \
    0.8383127018973108640833295E+00, \
    0.8057581520556423644789438E+00, \
    0.7732036547680256450048242E+00, \
    0.7406492173185620802637676E+00, \
    0.7080948483057714882525616E+00, \
    0.6755405579604902654406567E+00, \
    0.6429863585601198571817691E+00, \
    0.6104322649751623629236805E+00, \
    0.5778782954001507969801437E+00, \
    0.5453244723459250134170285E+00, \
    0.5127708240092147734858477E+00, \
    0.4802173861982495342372455E+00, \
    0.4476642050968422792532389E+00, \
    0.4151113413261211455132671E+00, \
    0.3825588760747025757978563E+00, \
    0.3500069206395502661556462E+00, \
    0.3174556318161704671189642E+00, \
    0.2849052377944113082878058E+00, \
    0.2523560839907875626097181E+00, \
    0.2198087193323827316322426E+00, \
    0.1872640717400572601243546E+00, \
    0.1547238424480887172335593E+00, \
    0.1221915194567498709631299E+00, \
    0.8967553546914315204781840E-01, \
    0.5720262597323678474637133E-01, \
    0.2492036059421555107245208E-01 ] )
  EvenThetaZero49 = np.array ( [ \
    0.1554849361424470843090118E+01, \
    0.1522955431101933730645303E+01, \
    0.1491061502037751976297424E+01, \
    0.1459167575082261894770634E+01, \
    0.1427273651103158170602525E+01, \
    0.1395379730992862183093282E+01, \
    0.1363485815676330697886480E+01, \
    0.1331591906119453530640248E+01, \
    0.1299698003338207337770238E+01, \
    0.1267804108408757103237650E+01, \
    0.1235910222478728395590872E+01, \
    0.1204016346779913703159712E+01, \
    0.1172122482642727288439229E+01, \
    0.1140228631512787910483320E+01, \
    0.1108334794970091261912531E+01, \
    0.1076440974751339138680154E+01, \
    0.1044547172776127017814204E+01, \
    0.1012653391177865049408482E+01, \
    0.9807596323405319627306720E+00, \
    0.9488658989426541583823449E+00, \
    0.9169721940102869797082899E+00, \
    0.8850785209812848825432963E+00, \
    0.8531848837838285971960304E+00, \
    0.8212912869330969580404013E+00, \
    0.7893977356512249782795147E+00, \
    0.7575042360174185552669765E+00, \
    0.7256107951575083863622461E+00, \
    0.6937174214856350398887716E+00, \
    0.6618241250156435481462849E+00, \
    0.6299309177668761147121611E+00, \
    0.5980378142995696297245189E+00, \
    0.5661448324309071185385071E+00, \
    0.5342519942071113461815355E+00, \
    0.5023593272451872220760104E+00, \
    0.4704668666194035162003700E+00, \
    0.4385746575692260390945883E+00, \
    0.4066827594785525726660483E+00, \
    0.3747912518813925812276922E+00, \
    0.3429002438089823350625543E+00, \
    0.3110098888674705209106637E+00, \
    0.2791204106078991711912441E+00, \
    0.2472321474279120600810915E+00, \
    0.2153456371036966567922014E+00, \
    0.1834617887100953140198272E+00, \
    0.1515822689338083535939382E+00, \
    0.1197104949484175660714864E+00, \
    0.8785472823121690639967810E-01, \
    0.5604116141749524467628553E-01, \
    0.2441436781606819510490200E-01 ] )
  EvenThetaZero50 = np.array ( [ \
    0.1555166706034023842787706E+01, \
    0.1523907464890582273398300E+01, \
    0.1492648224885016483409279E+01, \
    0.1461388986785839210767990E+01, \
    0.1430129751376631035251350E+01, \
    0.1398870519462421720845393E+01, \
    0.1367611291876438076975682E+01, \
    0.1336352069487341263827064E+01, \
    0.1305092853207091240256110E+01, \
    0.1273833643999595441027728E+01, \
    0.1242574442890323705495464E+01, \
    0.1211315250977103200801981E+01, \
    0.1180056069442347222927677E+01, \
    0.1148796899567022469820701E+01, \
    0.1117537742746723499546780E+01, \
    0.1086278600510304367969825E+01, \
    0.1055019474541620880304106E+01, \
    0.1023760366705069175705639E+01, \
    0.9925012790757765081567637E+00, \
    0.9612422139755203374385844E+00, \
    0.9299831740157389822411293E+00, \
    0.8987241621493743180375722E+00, \
    0.8674651817337867269827651E+00, \
    0.8362062366076504452859926E+00, \
    0.8049473311856388413561914E+00, \
    0.7736884705759381993127359E+00, \
    0.7424296607273230664538510E+00, \
    0.7111709086148904840060001E+00, \
    0.6799122224768919982385331E+00, \
    0.6486536121198915829209739E+00, \
    0.6173950893164463798129595E+00, \
    0.5861366683298159921278400E+00, \
    0.5548783666157332634604655E+00, \
    0.5236202057751242467455922E+00, \
    0.4923622128691229579358494E+00, \
    0.4611044222679868504944176E+00, \
    0.4298468783051183048132298E+00, \
    0.3985896391770900735176252E+00, \
    0.3673327828297899556279530E+00, \
    0.3360764161195064368209114E+00, \
    0.3048206895905456571224703E+00, \
    0.2735658223403245791263072E+00, \
    0.2423121460275046288225596E+00, \
    0.2110601877217048587999889E+00, \
    0.1798108384023314561549010E+00, \
    0.1485657315840060835766576E+00, \
    0.1173282164330337207824850E+00, \
    0.8610639001623934211634967E-01, \
    0.5492592372249737419414775E-01, \
    0.2392851379957687254895331E-01 ] )
  
  OddThetaZero1 = np.array ( [ \
    0.6847192030022829138880982E+00 ] )
  OddThetaZero2 = np.array ( [ \
    0.1002176803643121641749915E+01, \
    0.4366349492255221620374655E+00 ] )
  OddThetaZero3 = np.array ( [ \
    0.1152892953722227341986065E+01, \
    0.7354466143229520469385622E+00, \
    0.3204050902900619825355950E+00 ] )
  OddThetaZero4 = np.array ( [ \
    0.1240573923404363422789550E+01, \
    0.9104740292261473250358755E+00, \
    0.5807869795060065580284919E+00, \
    0.2530224166119306882187233E+00 ] )
  OddThetaZero5 = np.array ( [ \
    0.1297877729331450368298142E+01, \
    0.1025003226369574843297844E+01, \
    0.7522519395990821317003373E+00, \
    0.4798534223256743217333579E+00, \
    0.2090492874137409414071522E+00 ] )
  OddThetaZero6 = np.array ( [ \
    0.1338247676100454369194835E+01, \
    0.1105718066248490075175419E+01, \
    0.8732366099401630367220948E+00, \
    0.6408663264733867770811230E+00, \
    0.4088002373420211722955679E+00, \
    0.1780944581262765470585931E+00 ] )
  OddThetaZero7 = np.array ( [ \
    0.1368219536992351783359098E+01, \
    0.1165652065603030148723847E+01, \
    0.9631067821301481995711685E+00, \
    0.7606069572889918619145483E+00, \
    0.5582062109125313357140248E+00, \
    0.3560718303314725022788878E+00, \
    0.1551231069747375098418591E+00 ] )
  OddThetaZero8 = np.array ( [ \
    0.1391350647015287461874435E+01, \
    0.1211909966211469688151240E+01, \
    0.1032480728417239563449772E+01, \
    0.8530732514258505686069670E+00, \
    0.6737074594242522259878462E+00, \
    0.4944303818194983217354808E+00, \
    0.3153898594929282395996014E+00, \
    0.1373998952992547671039022E+00 ] )
  OddThetaZero9 = np.array ( [ \
    0.1409742336767428999667236E+01, \
    0.1248691224331339221187704E+01, \
    0.1087646521650454938943641E+01, \
    0.9266134127998189551499083E+00, \
    0.7656007620508340547558669E+00, \
    0.6046261769405451549818494E+00, \
    0.4437316659960951760051408E+00, \
    0.2830497588453068048261493E+00, \
    0.1233108673082312764916251E+00 ] )
  OddThetaZero10 = np.array ( [ \
    0.1424715475176742734932665E+01, \
    0.1278636375242898727771561E+01, \
    0.1132561101012537613667002E+01, \
    0.9864925055883793730483278E+00, \
    0.8404350520135058972624775E+00, \
    0.6943966110110701016065380E+00, \
    0.5483930281810389839680525E+00, \
    0.4024623099018152227701990E+00, \
    0.2567245837448891192759858E+00, \
    0.1118422651428890834760883E+00 ] )
  OddThetaZero11 = np.array ( [ \
    0.1437141935303526306632113E+01, \
    0.1303488659735581140681362E+01, \
    0.1169837785762829821262819E+01, \
    0.1036190996404462300207004E+01, \
    0.9025507517347875930425807E+00, \
    0.7689210263823624893974324E+00, \
    0.6353089402976822861185532E+00, \
    0.5017289283414202278167583E+00, \
    0.3682157131008289798868520E+00, \
    0.2348791589702580223688923E+00, \
    0.1023252788872632487579640E+00 ] )
  OddThetaZero12 = np.array ( [ \
    0.1447620393135667144403507E+01, \
    0.1324445197736386798102445E+01, \
    0.1201271573324181312770120E+01, \
    0.1078100568411879956441542E+01, \
    0.9549336362382321811515336E+00, \
    0.8317729718814276781352878E+00, \
    0.7086221837538611370849622E+00, \
    0.5854877911108011727748238E+00, \
    0.4623830630132757357909198E+00, \
    0.3393399712563371486343129E+00, \
    0.2164597408964339264361902E+00, \
    0.9430083986305519349231898E-01 ] )
  OddThetaZero13 = np.array ( [ \
    0.1456575541704195839944967E+01, \
    0.1342355260834552126304154E+01, \
    0.1228136043468909663499174E+01, \
    0.1113918572282611841378549E+01, \
    0.9997037539874953933323299E+00, \
    0.8854928869950799998575862E+00, \
    0.7712879690777516856072467E+00, \
    0.6570923167092416238233585E+00, \
    0.5429119513798658239789812E+00, \
    0.4287591577660783587509129E+00, \
    0.3146635662674373982102762E+00, \
    0.2007190266590380629766487E+00, \
    0.8744338280630300217927750E-01 ] )
  OddThetaZero14 = np.array ( [ \
    0.1464317002991565219979113E+01, \
    0.1357838033080061766980173E+01, \
    0.1251359804334884770836945E+01, \
    0.1144882777708662655968171E+01, \
    0.1038407544520296695714932E+01, \
    0.9319349156915986836657782E+00, \
    0.8254660749671546663859351E+00, \
    0.7190028636037068047812305E+00, \
    0.6125483562383020473196681E+00, \
    0.5061081521562999836102547E+00, \
    0.3996936914666951732317457E+00, \
    0.2933325857619472952507468E+00, \
    0.1871123137498061864373407E+00, \
    0.8151560650977882057817999E-01 ] )
  OddThetaZero15 = np.array ( [ \
    0.1471075823713997440657641E+01, \
    0.1371355574944658989649887E+01, \
    0.1271635855736122280723838E+01, \
    0.1171916986981363820797100E+01, \
    0.1072199368669106404814915E+01, \
    0.9724835301003496870596165E+00, \
    0.8727702114891848603047954E+00, \
    0.7730605060747958359120755E+00, \
    0.6733561257504194406005404E+00, \
    0.5736599396529727772420934E+00, \
    0.4739771829190733570809765E+00, \
    0.3743185619229329461021810E+00, \
    0.2747099287638327553949437E+00, \
    0.1752332025619508475799133E+00, \
    0.7634046205384429302353073E-01 ] )
  OddThetaZero16 = np.array ( [ \
    0.1477027911291552393547878E+01, \
    0.1383259682348271685979143E+01, \
    0.1289491840051302622319481E+01, \
    0.1195724613675799550484673E+01, \
    0.1101958282220461402990667E+01, \
    0.1008193204014774090964219E+01, \
    0.9144298626454031699590564E+00, \
    0.8206689427646120483710056E+00, \
    0.7269114630504563073034288E+00, \
    0.6331590254855162126233733E+00, \
    0.5394143214244183829842424E+00, \
    0.4456822679082866369288652E+00, \
    0.3519729273095236644049666E+00, \
    0.2583106041071417718760275E+00, \
    0.1647723231643112502628240E+00, \
    0.7178317184275122449502857E-01 ] )
  OddThetaZero17 = np.array ( [ \
    0.1482309554825692463999299E+01, \
    0.1393822922226542123661077E+01, \
    0.1305336577335833571381699E+01, \
    0.1216850687682353365944624E+01, \
    0.1128365453024608460982204E+01, \
    0.1039881123511957522668140E+01, \
    0.9513980267579228357946521E+00, \
    0.8629166105524045911461307E+00, \
    0.7744375139383604902604254E+00, \
    0.6859616923374368587817328E+00, \
    0.5974906525247623278123711E+00, \
    0.5090269299866796725116786E+00, \
    0.4205751610647263669405267E+00, \
    0.3321448379994943116084719E+00, \
    0.2437588931448048912587688E+00, \
    0.1554900095178924564386865E+00, \
    0.6773932498157585698088354E-01 ] )
  OddThetaZero18 = np.array ( [ \
    0.1487027983239550912222135E+01, \
    0.1403259745496922270264564E+01, \
    0.1319491725464661433609663E+01, \
    0.1235724047968681189212364E+01, \
    0.1151956859289811446164825E+01, \
    0.1068190338689553494802072E+01, \
    0.9844247150109837231349622E+00, \
    0.9006602918737365182850484E+00, \
    0.8168974877846821404275069E+00, \
    0.7331369031796229223580227E+00, \
    0.6493794386888650054486281E+00, \
    0.5656265174356596757139537E+00, \
    0.4818805368222631487731579E+00, \
    0.3981458834052590173509113E+00, \
    0.3144315409387123154212535E+00, \
    0.2307592167302372059759857E+00, \
    0.1471977156945989772472748E+00, \
    0.6412678117309944052403703E-01 ] )
  OddThetaZero19 = np.array ( [ \
    0.1491268718102344688271411E+01, \
    0.1411741190914640487505771E+01, \
    0.1332213830951015404441941E+01, \
    0.1252686732830809999680267E+01, \
    0.1173160005794509313174730E+01, \
    0.1093633781237958896879965E+01, \
    0.1014108223243148393065201E+01, \
    0.9345835440325075907377330E+00, \
    0.8550600276575269107773349E+00, \
    0.7755380679025248517258532E+00, \
    0.6960182317959841585145109E+00, \
    0.6165013717819833504477346E+00, \
    0.5369888366794912945318079E+00, \
    0.4574829005269902932408889E+00, \
    0.3779877260196973978940863E+00, \
    0.2985118404618624984946326E+00, \
    0.2190758506462427957069113E+00, \
    0.1397450765119767349146353E+00, \
    0.6088003363863534825005464E-01 ] )
  OddThetaZero20 = np.array ( [ \
    0.1495100801651051409999732E+01, \
    0.1419405340110198552778393E+01, \
    0.1343710008748627892724810E+01, \
    0.1268014880389353000310414E+01, \
    0.1192320038028903827079750E+01, \
    0.1116625579891689469044026E+01, \
    0.1040931626310454794079799E+01, \
    0.9652383295306942866661884E+00, \
    0.8895458882533946571137358E+00, \
    0.8138545700535261740447950E+00, \
    0.7381647473570304814395029E+00, \
    0.6624769578126105498149624E+00, \
    0.5867920109947446493391737E+00, \
    0.5111111891461744489290992E+00, \
    0.4354366553151050147918632E+00, \
    0.3597723703299625354660452E+00, \
    0.2841264494060559943920389E+00, \
    0.2085185052177154996230005E+00, \
    0.1330107089065635461375419E+00, \
    0.5794620170990797798650123E-01 ] )
  OddThetaZero21 = np.array ( [ \
    0.1498580583401444174317386E+01, \
    0.1426364890228584522673414E+01, \
    0.1354149299629923281192036E+01, \
    0.1281933868420423988034246E+01, \
    0.1209718660626713399048551E+01, \
    0.1137503750956414845248481E+01, \
    0.1065289229411733880607916E+01, \
    0.9930752076949068878557126E+00, \
    0.9208618284397049456535757E+00, \
    0.8486492789905562098591586E+00, \
    0.7764378127156926158031943E+00, \
    0.7042277832708635930867344E+00, \
    0.6320197021480767602848178E+00, \
    0.5598143404345395912377042E+00, \
    0.4876129202946139420188428E+00, \
    0.4154175043169533365541148E+00, \
    0.3432318703096418027524597E+00, \
    0.2710637595435203246492797E+00, \
    0.1989318822110657561806962E+00, \
    0.1268955503926593166308254E+00, \
    0.5528212871240371048241379E-01 ] )
  OddThetaZero22 = np.array ( [ \
    0.1501754508594837337089856E+01, \
    0.1432712730475143340404518E+01, \
    0.1363671034069754274950592E+01, \
    0.1294629464249430679064317E+01, \
    0.1225588071083248538559259E+01, \
    0.1156546912269029268686830E+01, \
    0.1087506056298747798071893E+01, \
    0.1018465586752840651469411E+01, \
    0.9494256083335850798964741E+00, \
    0.8803862556198167553278643E+00, \
    0.8113477061841624760598814E+00, \
    0.7423102009244498727845341E+00, \
    0.6732740767851639064676858E+00, \
    0.6042398217472142478598295E+00, \
    0.5352081720899522889584566E+00, \
    0.4661802954366277026594659E+00, \
    0.3971581629712621730826920E+00, \
    0.3281453857685808451825081E+00, \
    0.2591493642052661979197670E+00, \
    0.1901879854885491785792565E+00, \
    0.1213179541186130699071317E+00, \
    0.5285224511635143601147552E-01 ] )
  OddThetaZero23 = np.array ( [ \
    0.1504661202517196460191540E+01, \
    0.1438526110541037227495230E+01, \
    0.1372391084315255737540026E+01, \
    0.1306256159670931796771616E+01, \
    0.1240121376243315949825014E+01, \
    0.1173986779205849344923421E+01, \
    0.1107852421486856229076325E+01, \
    0.1041718366715156747157745E+01, \
    0.9755846932657442605621389E+00, \
    0.9094514999854931965227238E+00, \
    0.8433189145364798253029042E+00, \
    0.7771871059265138564989363E+00, \
    0.7110563039566125173946002E+00, \
    0.6449268305419475123120585E+00, \
    0.5787991523675322133651034E+00, \
    0.5126739740395088296453592E+00, \
    0.4465524134105889084933393E+00, \
    0.3804363581140941600870992E+00, \
    0.3143292666717729726674543E+00, \
    0.2482382273986418438740754E+00, \
    0.1821803739336923550363257E+00, \
    0.1162100228791666307841708E+00, \
    0.5062697144246344520692308E-01 ] )
  OddThetaZero24 = np.array ( [ \
    0.1507333049739684406957329E+01, \
    0.1443869798951040686809862E+01, \
    0.1380406601553595646811530E+01, \
    0.1316943486448336467960940E+01, \
    0.1253480485358734060913055E+01, \
    0.1190017634088428795118215E+01, \
    0.1126554974102287077081806E+01, \
    0.1063092554588577221978254E+01, \
    0.9996304352342330000643921E+00, \
    0.9361686900661624628632729E+00, \
    0.8727074129127595264965883E+00, \
    0.8092467253835331800652228E+00, \
    0.7457867888716805068068402E+00, \
    0.6823278231980088937854296E+00, \
    0.6188701366516795329577182E+00, \
    0.5554141765061554178407906E+00, \
    0.4919606183965743300387332E+00, \
    0.4285105345527885639657014E+00, \
    0.3650657359209552112046854E+00, \
    0.3016295408979540017854803E+00, \
    0.2382087510453128743250072E+00, \
    0.1748198074104535338147956E+00, \
    0.1115148317291502081079519E+00, \
    0.4858150828905663931389750E-01 ] )
  OddThetaZero25 = np.array ( [ \
    0.1509797405521643600800862E+01, \
    0.1448798505784201776188819E+01, \
    0.1387799649767640868379247E+01, \
    0.1326800860997572277878513E+01, \
    0.1265802165120213614545418E+01, \
    0.1204803590828283748583827E+01, \
    0.1143805171007496028164312E+01, \
    0.1082806944206958485218487E+01, \
    0.1021808956582037259849130E+01, \
    0.9608112645303606832220554E+00, \
    0.8998139383584991342974664E+00, \
    0.8388170675106567024157190E+00, \
    0.7778207682214244793380700E+00, \
    0.7168251950382156442798800E+00, \
    0.6558305587295081487906238E+00, \
    0.5948371551492265376377962E+00, \
    0.5338454137827292925154468E+00, \
    0.4728559836463229599006206E+00, \
    0.4118698949811841042358258E+00, \
    0.3508888880839026413717319E+00, \
    0.2899161521835467942607342E+00, \
    0.2289582244272697168835150E+00, \
    0.1680309071251709912058722E+00, \
    0.1071842976730454709494914E+00, \
    0.4669490825917857848258897E-01 ] )
  OddThetaZero26 = np.array ( [ \
    0.1512077535592702651885542E+01, \
    0.1453358762182399391553360E+01, \
    0.1394640024852448295479492E+01, \
    0.1335921342914185177270306E+01, \
    0.1277202737290683500323248E+01, \
    0.1218484231207691826029908E+01, \
    0.1159765851037557179133987E+01, \
    0.1101047627365156083369632E+01, \
    0.1042329596373083545617043E+01, \
    0.9836118016874520301049009E+00, \
    0.9248942968954766185908511E+00, \
    0.8661771490588063053774554E+00, \
    0.8074604437333368789787031E+00, \
    0.7487442923247565105494255E+00, \
    0.6900288431709550365296138E+00, \
    0.6313142987730108226833704E+00, \
    0.5726009435739572428629866E+00, \
    0.5138891906843943809444838E+00, \
    0.4551796645660731149033106E+00, \
    0.3964733566771858874923011E+00, \
    0.3377719420068963817561906E+00, \
    0.2790784903284342592940125E+00, \
    0.2203992941938221111139898E+00, \
    0.1617495649772923108686624E+00, \
    0.1031775271253784724197264E+00, \
    0.4494935602951385601335598E-01 ] )
  OddThetaZero27 = np.array ( [ \
    0.1514193352804819997509006E+01, \
    0.1457590393617468793209691E+01, \
    0.1400987464419153080392546E+01, \
    0.1344384581184662080889348E+01, \
    0.1287781761126833878758488E+01, \
    0.1231179023218584237510462E+01, \
    0.1174576388822640925688125E+01, \
    0.1117973882475943676285829E+01, \
    0.1061371532893653466992815E+01, \
    0.1004769374285310770780417E+01, \
    0.9481674481184788854172919E+00, \
    0.8915658055327279211293483E+00, \
    0.8349645107156934027761499E+00, \
    0.7783636457331086848148917E+00, \
    0.7217633176118399859733190E+00, \
    0.6651636690166557413471029E+00, \
    0.6085648948549621671933311E+00, \
    0.5519672690500084950513985E+00, \
    0.4953711895788266953367288E+00, \
    0.4387772581729219934583483E+00, \
    0.3821864303519236078766179E+00, \
    0.3256003205491779498477363E+00, \
    0.2690218877324958059454348E+00, \
    0.2124571975249336244841297E+00, \
    0.1559209129891515317090843E+00, \
    0.9945952063842375053227931E-01, \
    0.4332960406341033436157524E-01 ] )
  OddThetaZero28 = np.array ( [ \
    0.1516162000094549207021851E+01, \
    0.1461527685790782385188426E+01, \
    0.1406893396579229558427657E+01, \
    0.1352259145769086826235918E+01, \
    0.1297624947629923059740243E+01, \
    0.1242990817790597917328601E+01, \
    0.1188356773715062198539162E+01, \
    0.1133722835287525783953663E+01, \
    0.1079089025551156002698850E+01, \
    0.1024455371662101389801169E+01, \
    0.9698219061474760364582928E+00, \
    0.9151886685974009713577537E+00, \
    0.8605557079864861100238346E+00, \
    0.8059230859253162466918892E+00, \
    0.7512908813164713594661588E+00, \
    0.6966591971861112012613682E+00, \
    0.6420281709850565965229799E+00, \
    0.5873979906122764301937499E+00, \
    0.5327689202536826556885353E+00, \
    0.4781413438508069051295597E+00, \
    0.4235158420269503798571552E+00, \
    0.3688933369002844229314675E+00, \
    0.3142753865947702189467806E+00, \
    0.2596648470121556361200229E+00, \
    0.2050675726616484232653526E+00, \
    0.1504977164639767777858359E+00, \
    0.9600014792058154736462106E-01, \
    0.4182252607645932321862773E-01 ] )
  OddThetaZero29 = np.array ( [ \
    0.1517998315905975681819213E+01, \
    0.1465200315462026532129551E+01, \
    0.1412402336143180968579639E+01, \
    0.1359604389111228213837104E+01, \
    0.1306806486279734731351497E+01, \
    0.1254008640622089183072742E+01, \
    0.1201210866535131048800458E+01, \
    0.1148413180281179970113571E+01, \
    0.1095615600538999408768381E+01, \
    0.1042818149105710558651372E+01, \
    0.9900208518088600875617620E+00, \
    0.9372237397138955502862203E+00, \
    0.8844268507524555199840381E+00, \
    0.8316302319600398731649744E+00, \
    0.7788339426133210890795576E+00, \
    0.7260380587255163256281298E+00, \
    0.6732426796448045921910045E+00, \
    0.6204479380061240544867289E+00, \
    0.5676540152134466427854705E+00, \
    0.5148611664077887834613451E+00, \
    0.4620697624728053757183766E+00, \
    0.4092803643735033357684553E+00, \
    0.3564938631002461237979451E+00, \
    0.3037117642790043703921396E+00, \
    0.2509368276982060978106092E+00, \
    0.1981747109679032915697317E+00, \
    0.1454390911823840643137232E+00, \
    0.9277332955453467429763451E-01, \
    0.4041676055113025684436480E-01 ] )
  OddThetaZero30 = np.array ( [ \
    0.1519715208823086817411929E+01, \
    0.1468634099702062550682430E+01, \
    0.1417553008469014674939490E+01, \
    0.1366471944542347269659860E+01, \
    0.1315390917933946912760115E+01, \
    0.1264309939489363760018555E+01, \
    0.1213229021168654147755139E+01, \
    0.1162148176384137345494752E+01, \
    0.1111067420416500738111992E+01, \
    0.1059986770938296676746064E+01, \
    0.1008906248685091746434581E+01, \
    0.9578258783312407255956784E+00, \
    0.9067456896525242756445150E+00, \
    0.8556657190967860708153477E+00, \
    0.8045860119448479090873824E+00, \
    0.7535066253423996943740445E+00, \
    0.7024276326462752642452137E+00, \
    0.6513491298057893513225544E+00, \
    0.6002712449887427739045163E+00, \
    0.5491941535583390603837715E+00, \
    0.4981181022276018128369963E+00, \
    0.4470434496975185070560821E+00, \
    0.3959707385770101868486847E+00, \
    0.3449008307748737032772825E+00, \
    0.2938351828535981363494671E+00, \
    0.2427764647581323719392653E+00, \
    0.1917301500230701193408602E+00, \
    0.1407094708800750523796875E+00, \
    0.8975637836633630394302762E-01, \
    0.3910242380354419363081899E-01 ] )
  OddThetaZero31 = np.array ( [ \
    0.1521323961422700444944464E+01, \
    0.1471851603590422118622546E+01, \
    0.1422379260986849454727777E+01, \
    0.1372906941604798453293218E+01, \
    0.1323434653909307929892118E+01, \
    0.1273962407026590487708892E+01, \
    0.1224490210963055761921526E+01, \
    0.1175018076866133593082748E+01, \
    0.1125546017342156230227131E+01, \
    0.1076074046851682267877939E+01, \
    0.1026602182210094558879809E+01, \
    0.9771304432322302018639612E+00, \
    0.9276588535760335871906045E+00, \
    0.8781874418647315968408864E+00, \
    0.8287162432047307488040550E+00, \
    0.7792453012756761070555010E+00, \
    0.7297746712644485550469075E+00, \
    0.6803044240724808212528033E+00, \
    0.6308346524943159683026367E+00, \
    0.5813654805388740483542438E+00, \
    0.5318970779332963132260134E+00, \
    0.4824296835154055410257004E+00, \
    0.4329636445908698102350729E+00, \
    0.3834994865870752458854056E+00, \
    0.3340380441799942088370002E+00, \
    0.2845807279748544733570760E+00, \
    0.2351301237470960623526672E+00, \
    0.1856915325646991222655151E+00, \
    0.1362777698319134965765757E+00, \
    0.8692946525012054120187353E-01, \
    0.3787087726949234365520114E-01 ] )
  OddThetaZero32 = np.array ( [ \
    0.1522834478472358672931947E+01, \
    0.1474872636605138418026177E+01, \
    0.1426910807768284322082436E+01, \
    0.1378948998781055367310047E+01, \
    0.1330987216841224680164684E+01, \
    0.1283025469674968454386883E+01, \
    0.1235063765709222885799986E+01, \
    0.1187102114275073728898860E+01, \
    0.1139140525853183114841234E+01, \
    0.1091179012375759666645271E+01, \
    0.1043217587604604879578741E+01, \
    0.9952562676120370548458597E+00, \
    0.9472950714021223337048082E+00, \
    0.8993340217254078241758816E+00, \
    0.8513731461641338285808219E+00, \
    0.8034124786014693431693904E+00, \
    0.7554520612457602368887930E+00, \
    0.7074919474732165281510693E+00, \
    0.6595322059052657580628641E+00, \
    0.6115729263971504325174172E+00, \
    0.5636142290734363894767612E+00, \
    0.5156562783879918167717991E+00, \
    0.4676993058012953469089537E+00, \
    0.4197436479350834076514896E+00, \
    0.3717898140987174444032373E+00, \
    0.3238386134116156886828960E+00, \
    0.2758914133405791810724762E+00, \
    0.2279507206431424610498769E+00, \
    0.1800216744637006612298520E+00, \
    0.1321166988439841543825694E+00, \
    0.8427518284958235696897899E-01, \
    0.3671453742186897322954009E-01 ] )
  OddThetaZero33 = np.array ( [ \
    0.1524255491013576804195881E+01, \
    0.1477714660784952783237945E+01, \
    0.1431173841758652772349485E+01, \
    0.1384633039781787069436630E+01, \
    0.1338092261006965672253841E+01, \
    0.1291551512012124788593875E+01, \
    0.1245010799937299944123195E+01, \
    0.1198470132644670409416924E+01, \
    0.1151929518909907204916554E+01, \
    0.1105388968655282680015213E+01, \
    0.1058848493238442193822372E+01, \
    0.1012308105815651361079674E+01, \
    0.9657678218054126734684090E+00, \
    0.9192276594886802366068293E+00, \
    0.8726876407972167893294764E+00, \
    0.8261477923647281669131478E+00, \
    0.7796081469509049827753598E+00, \
    0.7330687454042532567721262E+00, \
    0.6865296394193009886613469E+00, \
    0.6399908954920466591029822E+00, \
    0.5934526007301573325059582E+00, \
    0.5469148716199143611697357E+00, \
    0.5003778676688561814362271E+00, \
    0.4538418134105091550464446E+00, \
    0.4073070354279485829740435E+00, \
    0.3607740278788822846227453E+00, \
    0.3142435758510728338330843E+00, \
    0.2677170062389944640113953E+00, \
    0.2211967514739567668334169E+00, \
    0.1746877983807874325844051E+00, \
    0.1282022028383479964348629E+00, \
    0.8177818680168764430245080E-01, \
    0.3562671947817428176226631E-01 ] )
  OddThetaZero34 = np.array ( [ \
    0.1525594725214770881206476E+01, \
    0.1480393128432045740356817E+01, \
    0.1435191541323085582529217E+01, \
    0.1389989968924959812091252E+01, \
    0.1344788416522907866060817E+01, \
    0.1299586889746827997174554E+01, \
    0.1254385394680661996389736E+01, \
    0.1209183937989395175829969E+01, \
    0.1163982527069600127515982E+01, \
    0.1118781170231154762473596E+01, \
    0.1073579876920155012130433E+01, \
    0.1028378657996412636748477E+01, \
    0.9831775260837211038023103E+00, \
    0.9379764960179657076015136E+00, \
    0.8927755854282048597997986E+00, \
    0.8475748155007347757967789E+00, \
    0.8023742119985848209905761E+00, \
    0.7571738066433708695662393E+00, \
    0.7119736390205872251796930E+00, \
    0.6667737592565460745639184E+00, \
    0.6215742318591892056934095E+00, \
    0.5763751413603713322640298E+00, \
    0.5311766008298875656047892E+00, \
    0.4859787651249621588538330E+00, \
    0.4407818522612533891543536E+00, \
    0.3955861793705505114602136E+00, \
    0.3503922263398633798966312E+00, \
    0.3052007556167344348049303E+00, \
    0.2600130558662051177480644E+00, \
    0.2148314894784555841956251E+00, \
    0.1696608997322034095150907E+00, \
    0.1245129955389270002683579E+00, \
    0.7942489891978153749097006E-01, \
    0.3460150809198016850782325E-01 ] )
  OddThetaZero35 = np.array ( [ \
    0.1526859042890589526378487E+01, \
    0.1482921763148403842276533E+01, \
    0.1438984491795164536567108E+01, \
    0.1395047233189252525231459E+01, \
    0.1351109991891878034957302E+01, \
    0.1307172772745304669260382E+01, \
    0.1263235580960968906699379E+01, \
    0.1219298422221050703835127E+01, \
    0.1175361302797916700875697E+01, \
    0.1131424229697065895207730E+01, \
    0.1087487210830887883186060E+01, \
    0.1043550255232887174273672E+01, \
    0.9996133733253190253881393E+00, \
    0.9556765772578535710715874E+00, \
    0.9117398813415957196221754E+00, \
    0.8678033026125661948850687E+00, \
    0.8238668615732247310812836E+00, \
    0.7799305831824293601507400E+00, \
    0.7359944981977457886183921E+00, \
    0.6920586450266629333858465E+00, \
    0.6481230723279649663476697E+00, \
    0.6041878427445000852182582E+00, \
    0.5602530383870993537615272E+00, \
    0.5163187691099712879003757E+00, \
    0.4723851853891499571797438E+00, \
    0.4284524990953311047063058E+00, \
    0.3845210184454249891341793E+00, \
    0.3405912098612419399584605E+00, \
    0.2966638144233703899038032E+00, \
    0.2527400847124078576715667E+00, \
    0.2088223170017057788708674E+00, \
    0.1649152190599722827308055E+00, \
    0.1210301722471160155498167E+00, \
    0.7720326018898817828206987E-01, \
    0.3363364974516995102167462E-01 ] )
  OddThetaZero36 = np.array ( [ \
    0.1528054559083405137047563E+01, \
    0.1485312794997097705446883E+01, \
    0.1442571038214470776579613E+01, \
    0.1399829292522320013570493E+01, \
    0.1357087561874166765548658E+01, \
    0.1314345850454078759228779E+01, \
    0.1271604162748143389685638E+01, \
    0.1228862503626296926524085E+01, \
    0.1186120878437839368895715E+01, \
    0.1143379293124832099340074E+01, \
    0.1100637754358770795248912E+01, \
    0.1057896269707576280860569E+01, \
    0.1015154847842238156769126E+01, \
    0.9724134987956584339974640E+00, \
    0.9296722342907946818431047E+00, \
    0.8869310681617368097575324E+00, \
    0.8441900169008687429295884E+00, \
    0.8014491003793523040286325E+00, \
    0.7587083428093935362576859E+00, \
    0.7159677740493625646700975E+00, \
    0.6732274314040501413860867E+00, \
    0.6304873621547357085895928E+00, \
    0.5877476271899241333221832E+00, \
    0.5450083063396327078463020E+00, \
    0.5022695064252395155059223E+00, \
    0.4595313737871711838065652E+00, \
    0.4167941144922007176438387E+00, \
    0.3740580283336802289311736E+00, \
    0.3313235690067746553700419E+00, \
    0.2885914573933480330041531E+00, \
    0.2458629119584249278750153E+00, \
    0.2031401664615301668533461E+00, \
    0.1604278005405711652039491E+00, \
    0.1177368858339244458607172E+00, \
    0.7510252408650086658441596E-01, \
    0.3271846270775478856070884E-01 ] )
  OddThetaZero37 = np.array ( [ \
    0.1529186740959505109653289E+01, \
    0.1487577158293388707508111E+01, \
    0.1445967582009979387718202E+01, \
    0.1404358015412336440816745E+01, \
    0.1362748461941311565399969E+01, \
    0.1321138925227929972823825E+01, \
    0.1279529409151733277951100E+01, \
    0.1237919917907156982173977E+01, \
    0.1196310456080472987418488E+01, \
    0.1154701028740456700905269E+01, \
    0.1113091641546798022997704E+01, \
    0.1071482300881451340842721E+01, \
    0.1029873014009735917989475E+01, \
    0.9882637892802373569245916E+00, \
    0.9466546363756944528310758E+00, \
    0.9050455666314926033869497E+00, \
    0.8634365934447506520344540E+00, \
    0.8218277328062565148449433E+00, \
    0.7802190040012226850703573E+00, \
    0.7386104305454957746359112E+00, \
    0.6970020414556031913861513E+00, \
    0.6553938730008771105113861E+00, \
    0.6137859711661063914322283E+00, \
    0.5721783951857430999179669E+00, \
    0.5305712227365694155165922E+00, \
    0.4889645577740232855661796E+00, \
    0.4473585427277744403333139E+00, \
    0.4057533781735039172217875E+00, \
    0.3641493559322687127223795E+00, \
    0.3225469176515179389138545E+00, \
    0.2809467650889194227770571E+00, \
    0.2393500844055270891104500E+00, \
    0.1977590501629603151642330E+00, \
    0.1561781206604067112364815E+00, \
    0.1146180742271483316267615E+00, \
    0.7311308274978660184520447E-01, \
    0.3185176130791400787169333E-01 ] )
  OddThetaZero38 = np.array ( [ \
    0.1530260491394766313570510E+01, \
    0.1489724658775115137266557E+01, \
    0.1449188831753177403184250E+01, \
    0.1408653013220734918131897E+01, \
    0.1368117206184034069757975E+01, \
    0.1327581413807020172726043E+01, \
    0.1287045639459248683416470E+01, \
    0.1246509886770075360771330E+01, \
    0.1205974159691064843702080E+01, \
    0.1165438462569017837684371E+01, \
    0.1124902800232641860108690E+01, \
    0.1084367178096737546333982E+01, \
    0.1043831602288925654461738E+01, \
    0.1003296079805520648394589E+01, \
    0.9627606187053432591598275E+00, \
    0.9222252283533212928777294E+00, \
    0.8816899197300536544215117E+00, \
    0.8411547058297167490229198E+00, \
    0.8006196021777239861105672E+00, \
    0.7600846275129127849719743E+00, \
    0.7195498046991648764002008E+00, \
    0.6790151619622966197448464E+00, \
    0.6384807345966275863946969E+00, \
    0.5979465673637771458800754E+00, \
    0.5574127179353942966481713E+00, \
    0.5168792619515766918187819E+00, \
    0.4763463006547495614450433E+00, \
    0.4358139727703203523144583E+00, \
    0.3952824736706231680817472E+00, \
    0.3547520876199503791717895E+00, \
    0.3142232448436673832093046E+00, \
    0.2736966289659020439688229E+00, \
    0.2331733955144496369946707E+00, \
    0.1926556629116315949109922E+00, \
    0.1521477743835989472840536E+00, \
    0.1116602300918232453371161E+00, \
    0.7122632005925390425640031E-01, \
    0.3102979192734513847869512E-01 ] )
  OddThetaZero39 = np.array ( [ \
    0.1531280219945530918862887E+01, \
    0.1491764115543711582608611E+01, \
    0.1452248016067723206269747E+01, \
    0.1412731924058150689920340E+01, \
    0.1373215842151127100608219E+01, \
    0.1333699773114208203180680E+01, \
    0.1294183719885939986844436E+01, \
    0.1254667685620366764206205E+01, \
    0.1215151673737978313041594E+01, \
    0.1175635687984935008823566E+01, \
    0.1136119732502868295328130E+01, \
    0.1096603811912170337964094E+01, \
    0.1057087931412518476253055E+01, \
    0.1017572096905509113863513E+01, \
    0.9780563151458206514020694E+00, \
    0.9385405939294598498464432E+00, \
    0.8990249423306286659734381E+00, \
    0.8595093710029676968794279E+00, \
    0.8199938925669823205931282E+00, \
    0.7804785221142635001130339E+00, \
    0.7409632778721439753645470E+00, \
    0.7014481820920565808095373E+00, \
    0.6619332622550151160558599E+00, \
    0.6224185527349885679868616E+00, \
    0.5829040971371158016902326E+00, \
    0.5433899516536147244946347E+00, \
    0.5038761899947552937603140E+00, \
    0.4643629108305196256509391E+00, \
    0.4248502493722176391609139E+00, \
    0.3853383960541810555628366E+00, \
    0.3458276279674767760058527E+00, \
    0.3063183644932167228808922E+00, \
    0.2668112720373341483108662E+00, \
    0.2273074770384765519559169E+00, \
    0.1878090446069578429818381E+00, \
    0.1483202086882449059764783E+00, \
    0.1088512052741322662621244E+00, \
    0.6943448689600673838300180E-01, \
    0.3024917865720923179577363E-01 ] )
  OddThetaZero40 = np.array ( [ \
    0.1532249903371281818085917E+01, \
    0.1493703482108998740614827E+01, \
    0.1455157065195200346809599E+01, \
    0.1416610654869340270223431E+01, \
    0.1378064253450997606022340E+01, \
    0.1339517863369794055919890E+01, \
    0.1300971487198245305453001E+01, \
    0.1262425127688525048786896E+01, \
    0.1223878787814308166546501E+01, \
    0.1185332470819113339105535E+01, \
    0.1146786180272904774996439E+01, \
    0.1108239920139165765487189E+01, \
    0.1069693694855262920629379E+01, \
    0.1031147509429735196850587E+01, \
    0.9926013695612463310882198E+00, \
    0.9540552817854489715123326E+00, \
    0.9155092536580933534978986E+00, \
    0.8769632939856246206308699E+00, \
    0.8384174131186299393233148E+00, \
    0.7998716233293992826192237E+00, \
    0.7613259393034545837300323E+00, \
    0.7227803787876118667749166E+00, \
    0.6842349634562860931661901E+00, \
    0.6456897200871628101751519E+00, \
    0.6071446821835496233813653E+00, \
    0.5685998922550279415939221E+00, \
    0.5300554050908430047380815E+00, \
    0.4915112925697217767572364E+00, \
    0.4529676509187802579380104E+00, \
    0.4144246120108054286121629E+00, \
    0.3758823615873930314093573E+00, \
    0.3373411699211847213003570E+00, \
    0.2988014460838619282843952E+00, \
    0.2602638401106843145315994E+00, \
    0.2217294507811754336425535E+00, \
    0.1832002925124018168986342E+00, \
    0.1446804953347050655563166E+00, \
    0.1061800440374660771048480E+00, \
    0.6773059476567831336488402E-01, \
    0.2950687695527422224851832E-01 ] )
  OddThetaZero41 = np.array ( [ \
    0.1533173137460634461235066E+01, \
    0.1495549950040734249895393E+01, \
    0.1457926766471340970762709E+01, \
    0.1420303588732694442267846E+01, \
    0.1382680418872520759663065E+01, \
    0.1345057259031099988676433E+01, \
    0.1307434111468678960501903E+01, \
    0.1269810978596001635506341E+01, \
    0.1232187863008871596257323E+01, \
    0.1194564767527851916244615E+01, \
    0.1156941695244461089553108E+01, \
    0.1119318649575559636172662E+01, \
    0.1081695634328067979412755E+01, \
    0.1044072653776750930510111E+01, \
    0.1006449712758602402124214E+01, \
    0.9688268167884441336521039E+00, \
    0.9312039722018274751677424E+00, \
    0.8935811863333633591901354E+00, \
    0.8559584677414483220357356E+00, \
    0.8183358264943738874932307E+00, \
    0.7807132745385688213392421E+00, \
    0.7430908261781095392995681E+00, \
    0.7054684987070400358784448E+00, \
    0.6678463132547297820965882E+00, \
    0.6302242959332082940279826E+00, \
    0.5926024794204980683238426E+00, \
    0.5549809051864955237054951E+00, \
    0.5173596266878257139037738E+00, \
    0.4797387140623364241772428E+00, \
    0.4421182612140318859822955E+00, \
    0.4044983968396638104610711E+00, \
    0.3668793022152994411560368E+00, \
    0.3292612411240570212440856E+00, \
    0.2916446128242035199998930E+00, \
    0.2540300517665934607689814E+00, \
    0.2164186303985620085027010E+00, \
    0.1788123148742007754778852E+00, \
    0.1412151362884411752920148E+00, \
    0.1036368402634645114775150E+00, \
    0.6610832470916409695729856E-01, \
    0.2880013396280840229218334E-01 ] )
  OddThetaZero42 = np.array ( [ \
    0.1534053181584449084854269E+01, \
    0.1497310038074501005766978E+01, \
    0.1460566897984002644464183E+01, \
    0.1423823763069232867789940E+01, \
    0.1387080635143547965139117E+01, \
    0.1350337516098480646600889E+01, \
    0.1313594407926723776707731E+01, \
    0.1276851312747612578778902E+01, \
    0.1240108232835827171448969E+01, \
    0.1203365170654181674634873E+01, \
    0.1166622128891556900019450E+01, \
    0.1129879110507284864268762E+01, \
    0.1093136118783624474731954E+01, \
    0.1056393157388405786003046E+01, \
    0.1019650230450503114577901E+01, \
    0.9829073426515786199715451E+00, \
    0.9461644993385942743541994E+00, \
    0.9094217066630320811486021E+00, \
    0.8726789717547518480094350E+00, \
    0.8359363029411928866147184E+00, \
    0.7991937100265521402467844E+00, \
    0.7624512046511992388808212E+00, \
    0.7257088007597790982554974E+00, \
    0.6889665152185689899094400E+00, \
    0.6522243686409073299342467E+00, \
    0.6154823865075504175164916E+00, \
    0.5787406007128420496638175E+00, \
    0.5419990517384125648087865E+00, \
    0.5052577917731960988645056E+00, \
    0.4685168892980173635234519E+00, \
    0.4317764360047099160222576E+00, \
    0.3950365575646972937604113E+00, \
    0.3582974309994310205507555E+00, \
    0.3215593139080007759227897E+00, \
    0.2848225961961619069649047E+00, \
    0.2480878974611689122432227E+00, \
    0.2113562650517154915467591E+00, \
    0.1746296191183898065201571E+00, \
    0.1379118964507339113271975E+00, \
    0.1012126146941469342401701E+00, \
    0.6456194899726137278760257E-01, \
    0.2812645439079299219187419E-01 ] )
  OddThetaZero43 = np.array ( [ \
    0.1534892997139557227614279E+01, \
    0.1498989668998897501276994E+01, \
    0.1463086343903285773505644E+01, \
    0.1427183023414814244376429E+01, \
    0.1391279709144040438287602E+01, \
    0.1355376402767821814937864E+01, \
    0.1319473106048673173924451E+01, \
    0.1283569820856137399848247E+01, \
    0.1247666549190742942502495E+01, \
    0.1211763293211231530413995E+01, \
    0.1175860055265884319525693E+01, \
    0.1139956837928964066704190E+01, \
    0.1104053644043538840797350E+01, \
    0.1068150476772278342447444E+01, \
    0.1032247339658243608912598E+01, \
    0.9963442366982618328585493E+00, \
    0.9604411724322426430586723E+00, \
    0.9245381520528253319358567E+00, \
    0.8886351815411563067305273E+00, \
    0.8527322678365406966379400E+00, \
    0.8168294190504262166761188E+00, \
    0.7809266447390142664026016E+00, \
    0.7450239562542930157586944E+00, \
    0.7091213672012904985883029E+00, \
    0.6732188940411854039055226E+00, \
    0.6373165568977466866717861E+00, \
    0.6014143806519714388063208E+00, \
    0.5655123964528129857845238E+00, \
    0.5296106438411039715966193E+00, \
    0.4937091737981756577948229E+00, \
    0.4578080532255782153525438E+00, \
    0.4219073717059785387344039E+00, \
    0.3860072520255396095683859E+00, \
    0.3501078671472635990145335E+00, \
    0.3142094687704932495909488E+00, \
    0.2783124378775218384923333E+00, \
    0.2424173798924625361874772E+00, \
    0.2065253182141071551836492E+00, \
    0.1706381290938671641708352E+00, \
    0.1347596593282315198612592E+00, \
    0.9889920900871122533586553E-01, \
    0.6308626356388784057588631E-01, \
    0.2748357108440508277394892E-01 ] )
  OddThetaZero44 = np.array ( [ \
    0.1535695280838629983064694E+01, \
    0.1500594236235067817656313E+01, \
    0.1465493194350303789230585E+01, \
    0.1430392156577492526495371E+01, \
    0.1395291124351096810858349E+01, \
    0.1360190099162024176252063E+01, \
    0.1325089082574000089379322E+01, \
    0.1289988076241572027256558E+01, \
    0.1254887081930202663795858E+01, \
    0.1219786101538994920367859E+01, \
    0.1184685137126702182946916E+01, \
    0.1149584190941820846004092E+01, \
    0.1114483265457749469332035E+01, \
    0.1079382363414242848588494E+01, \
    0.1044281487866708939888712E+01, \
    0.1009180642245317812316634E+01, \
    0.9740798304264509422659935E+00, \
    0.9389790568197674899837757E+00, \
    0.9038783264751749171405213E+00, \
    0.8687776452153701566068907E+00, \
    0.8336770198015192229270720E+00, \
    0.7985764581422970742698971E+00, \
    0.7634759695602610192254430E+00, \
    0.7283755651349081311799055E+00, \
    0.6932752581495918103871962E+00, \
    0.6581750646810479477537782E+00, \
    0.6230750043877162525265513E+00, \
    0.5879751015798285374141491E+00, \
    0.5528753866962970290878822E+00, \
    0.5177758983811020490994086E+00, \
    0.4826766864637186565865902E+00, \
    0.4475778163386701445336738E+00, \
    0.4124793755752883735361361E+00, \
    0.3773814842049053432591527E+00, \
    0.3422843113148581639684411E+00, \
    0.3071881029697497767338606E+00, \
    0.2720932316284942932084102E+00, \
    0.2370002891767127567222407E+00, \
    0.2019102761348421810146637E+00, \
    0.1668250268181992892198073E+00, \
    0.1317483020532982541977987E+00, \
    0.9668919410176593344830717E-01, \
    0.6167652949817792358742135E-01, \
    0.2686941953400762687915995E-01 ] )
  OddThetaZero45 = np.array ( [ \
    0.1536462493634653558154673E+01, \
    0.1502128661685489464262068E+01, \
    0.1467794832169950298839286E+01, \
    0.1433461006333747476463744E+01, \
    0.1399127185457927306909792E+01, \
    0.1364793370871767472755746E+01, \
    0.1330459563966682507229700E+01, \
    0.1296125766211456950047804E+01, \
    0.1261791979169174443914592E+01, \
    0.1227458204516276373551266E+01, \
    0.1193124444064268679881601E+01, \
    0.1158790699784705540565424E+01, \
    0.1124456973838220917338613E+01, \
    0.1090123268608563332983681E+01, \
    0.1055789586742829027889885E+01, \
    0.1021455931199402224481903E+01, \
    0.9871223053055240306873772E+00, \
    0.9527887128269590857605072E+00, \
    0.9184551580529615732874848E+00, \
    0.8841216459007313197085517E+00, \
    0.8497881820448998068986446E+00, \
    0.8154547730794463756650640E+00, \
    0.7811214267220410983907210E+00, \
    0.7467881520744805288579630E+00, \
    0.7124549599581423848996086E+00, \
    0.6781218633510390484774053E+00, \
    0.6437888779643722276961833E+00, \
    0.6094560230135452763170614E+00, \
    0.5751233222647905281576305E+00, \
    0.5407908054797110156395425E+00, \
    0.5064585104462232763044121E+00, \
    0.4721264858937837018545325E+00, \
    0.4377947957771643018072936E+00, \
    0.4034635257416918872885646E+00, \
    0.3691327931855416440777167E+00, \
    0.3348027634909946151567752E+00, \
    0.3004736773353657517478163E+00, \
    0.2661458990278703974149616E+00, \
    0.2318200075085118064771005E+00, \
    0.1974969814205034596217949E+00, \
    0.1631786149772797106698111E+00, \
    0.1288685867945150272796250E+00, \
    0.9457579039019365184018477E-01, \
    0.6032842220945916819748797E-01, \
    0.2628211572883546008386342E-01 ] )
  OddThetaZero46 = np.array ( [ \
    0.1537196885933572311910085E+01, \
    0.1503597446159129663218426E+01, \
    0.1469998008568304160871417E+01, \
    0.1436398574277729377094190E+01, \
    0.1402799144434368418084898E+01, \
    0.1369199720226542342210552E+01, \
    0.1335600302895785666466344E+01, \
    0.1302000893749787833197270E+01, \
    0.1268401494176718217187838E+01, \
    0.1234802105661283063077015E+01, \
    0.1201202729802928570677208E+01, \
    0.1167603368336689119731474E+01, \
    0.1134004023157288628212183E+01, \
    0.1100404696347243386055709E+01, \
    0.1066805390209896030700280E+01, \
    0.1033206107308545748870827E+01, \
    0.9996068505131472996246808E+00, \
    0.9660076230564559666956844E+00, \
    0.9324084286020318648375284E+00, \
    0.8988092713272342656758064E+00, \
    0.8652101560253048754543914E+00, \
    0.8316110882319595313175680E+00, \
    0.7980120743837286767240920E+00, \
    0.7644131220178278512956878E+00, \
    0.7308142400269308414762795E+00, \
    0.6972154389873656296775555E+00, \
    0.6636167315867435235683334E+00, \
    0.6300181331881122315700717E+00, \
    0.5964196625844131090385918E+00, \
    0.5628213430226633060114218E+00, \
    0.5292232036175455988770345E+00, \
    0.4956252813388603291268380E+00, \
    0.4620276238643496856689332E+00, \
    0.4284302937718012609061760E+00, \
    0.3948333748659561479104270E+00, \
    0.3612369820255324850503899E+00, \
    0.3276412770872600895283016E+00, \
    0.2940464955725917238672137E+00, \
    0.2604529939906062681054034E+00, \
    0.2268613388903867245835696E+00, \
    0.1932724879746856807613294E+00, \
    0.1596881970714452359218090E+00, \
    0.1261120661032951679792394E+00, \
    0.9255279834764232165670211E-01, \
    0.5903798711627596210077655E-01, \
    0.2571993685288741305807485E-01 ] )
  OddThetaZero47 = np.array ( [ \
    0.1537900519639177351485509E+01, \
    0.1505004713461118831562885E+01, \
    0.1472108909246876714959093E+01, \
    0.1439213107999753788389740E+01, \
    0.1406317310749171844429399E+01, \
    0.1373421518560135827011261E+01, \
    0.1340525732543378926238078E+01, \
    0.1307629953866399941713193E+01, \
    0.1274734183765634621652739E+01, \
    0.1241838423560042429086765E+01, \
    0.1208942674666441461574345E+01, \
    0.1176046938616989970936899E+01, \
    0.1143151217079296988032361E+01, \
    0.1110255511879752164142939E+01, \
    0.1077359825030803093319347E+01, \
    0.1044464158763086533573607E+01, \
    0.1011568515563550961534623E+01, \
    0.9786728982210094134846821E+00, \
    0.9457773098809579873452675E+00, \
    0.9128817541120207886160886E+00, \
    0.8799862349870845994262022E+00, \
    0.8470907571831347751008168E+00, \
    0.8141953261050969543263697E+00, \
    0.7812999480407721032432037E+00, \
    0.7484046303564402266425896E+00, \
    0.7155093817462244075628281E+00, \
    0.6826142125533466396520346E+00, \
    0.6497191351887403950357432E+00, \
    0.6168241646833332909207560E+00, \
    0.5839293194266532352434130E+00, \
    0.5510346221695150324949297E+00, \
    0.5181401014079633610544426E+00, \
    0.4852457933290632607369490E+00, \
    0.4523517446039431388003505E+00, \
    0.4194580164920722423612656E+00, \
    0.3865646910356375140534892E+00, \
    0.3536718807003189971969294E+00, \
    0.3207797439266498255416416E+00, \
    0.2878885112969848452450724E+00, \
    0.2549985318477515756044100E+00, \
    0.2221103602568508117102717E+00, \
    0.1892249341643785313168465E+00, \
    0.1563439726212394862316010E+00, \
    0.1234710001537068179882843E+00, \
    0.9061453776736619019094845E-01, \
    0.5780160090309369034797044E-01, \
    0.2518130440638251656980999E-01 ] )
  OddThetaZero48 = np.array ( [ \
    0.1538575287485045780713568E+01, \
    0.1506354249056545799167351E+01, \
    0.1474133212398093554231315E+01, \
    0.1441912178413208451704314E+01, \
    0.1409691148027973881079186E+01, \
    0.1377470122199186272616473E+01, \
    0.1345249101923067139210221E+01, \
    0.1313028088244711409410919E+01, \
    0.1280807082268469343020428E+01, \
    0.1248586085169490583375238E+01, \
    0.1216365098206699074213627E+01, \
    0.1184144122737518830558069E+01, \
    0.1151923160234735793613503E+01, \
    0.1119702212305964062886069E+01, \
    0.1087481280716290811591462E+01, \
    0.1055260367414810028339009E+01, \
    0.1023039474565930165787482E+01, \
    0.9908186045865674272211987E+00, \
    0.9585977601906320722299056E+00, \
    0.9263769444426036830464570E+00, \
    0.8941561608225061952846411E+00, \
    0.8619354133052817812042663E+00, \
    0.8297147064584916186566054E+00, \
    0.7974940455635382827549679E+00, \
    0.7652734367673509855003551E+00, \
    0.7330528872739117793257283E+00, \
    0.7008324055884451343305450E+00, \
    0.6686120018320298047193041E+00, \
    0.6363916881515750209117372E+00, \
    0.6041714792607289968809847E+00, \
    0.5719513931632926368357825E+00, \
    0.5397314521353000325496229E+00, \
    0.5075116840805377280486923E+00, \
    0.4752921244363891783961832E+00, \
    0.4430728189095547215892704E+00, \
    0.4108538274961112658763390E+00, \
    0.3786352305487998074788803E+00, \
    0.3464171382200184643128623E+00, \
    0.3141997056941599156198233E+00, \
    0.2819831588178046655599196E+00, \
    0.2497678394619649260592757E+00, \
    0.2175542909210219972765731E+00, \
    0.1853434315961135904158300E+00, \
    0.1531369452704970394027659E+00, \
    0.1209382841678252589048669E+00, \
    0.8875579450016283173293810E-01, \
    0.5661593754525190873771522E-01, \
    0.2466476940450737058975552E-01 ] )
  OddThetaZero49 = np.array ( [ \
    0.1539222930035210331902410E+01, \
    0.1507649534071729882214386E+01, \
    0.1476076139707032453353232E+01, \
    0.1444502747756546556830706E+01, \
    0.1412929359055252480197337E+01, \
    0.1381355974464721552102928E+01, \
    0.1349782594880622732927647E+01, \
    0.1318209221240839295255046E+01, \
    0.1286635854534357387243172E+01, \
    0.1255062495811112994872428E+01, \
    0.1223489146193015470717893E+01, \
    0.1191915806886406014313715E+01, \
    0.1160342479196260434661502E+01, \
    0.1128769164542510055952304E+01, \
    0.1097195864478936528824546E+01, \
    0.1065622580715200621234508E+01, \
    0.1034049315142698534418744E+01, \
    0.1002476069865111021377467E+01, \
    0.9709028472347329448081481E+00, \
    0.9393296498959608456620406E+00, \
    0.9077564808376970380335442E+00, \
    0.8761833434569334264096395E+00, \
    0.8446102416364528348063321E+00, \
    0.8130371798404960344077378E+00, \
    0.7814641632334840064334645E+00, \
    0.7498911978285964532098456E+00, \
    0.7183182906753955596314298E+00, \
    0.6867454500990591398232408E+00, \
    0.6551726860086246453663390E+00, \
    0.6236000102986843027011345E+00, \
    0.5920274373793840619034224E+00, \
    0.5604549848852622707385612E+00, \
    0.5288826746375584896948472E+00, \
    0.4973105339724571989307663E+00, \
    0.4657385976085971045914307E+00, \
    0.4341669103277770901346174E+00, \
    0.4025955309141879357899857E+00, \
    0.3710245380997234377015025E+00, \
    0.3394540398171456073906403E+00, \
    0.3078841881262277508367562E+00, \
    0.2763152043287541015913350E+00, \
    0.2447474234189502677044064E+00, \
    0.2131813777658572006989977E+00, \
    0.1816179673056091210434906E+00, \
    0.1500588419721174291665790E+00, \
    0.1185073845935281602210493E+00, \
    0.8697177361567243680812898E-01, \
    0.5547793843128156580348541E-01, \
    0.2416899936118312040170588E-01 ] )
 
  if ( l < 1 or 100 < l ):
    print ( '' )
    print ( 'LEGENDRE_THETA - Fatal error!' )
    print ( '  1 <= L <= 100 is required.' )
    exit ( 'LEGENDRE_THETA - Fatal error!' )

  lhalf = ( ( l + 1 ) // 2 )

  if ( ( l % 2 ) == 1 ):
    if ( lhalf < k ):
      kcopy = k - lhalf
    elif ( lhalf == k ):
      kcopy = lhalf
    else:
      kcopy = lhalf - k
  else:
    if ( lhalf < k ):
      kcopy = k - lhalf
    else:
      kcopy = lhalf + 1 - k
  
  if ( kcopy < 1 or lhalf < kcopy ):
    print ( '' )
    print ( 'LEGENDRE_THETA - Fatal error!' )
    print ( '  1 <= K <= (L+1)/2 is required.' )
    exit ( 'LEGENDRE_THETA - Fatal error!' )
#
#  If L is odd, and K = ( L - 1 ) / 2, then it's easy.
#
  if ( ( l % 2 ) == 1 and kcopy == lhalf ):
    theta = np.pi / 2.0
  elif ( l == 2 ):
    theta = EvenThetaZero1[kcopy-1]
  elif ( l == 3 ):
    theta = OddThetaZero1[kcopy-1]
  elif ( l == 4 ):
    theta = EvenThetaZero2[kcopy-1]
  elif ( l == 5 ):
    theta = OddThetaZero2[kcopy-1]
  elif ( l == 6 ):
    theta = EvenThetaZero3[kcopy-1]
  elif ( l == 7 ):
    theta = OddThetaZero3[kcopy-1]
  elif ( l == 8 ):
    theta = EvenThetaZero4[kcopy-1]
  elif ( l == 9 ):
    theta = OddThetaZero4[kcopy-1]
  elif ( l == 10 ):
    theta = EvenThetaZero5[kcopy-1]
  elif ( l == 11 ):
    theta = OddThetaZero5[kcopy-1]
  elif ( l == 12 ):
    theta = EvenThetaZero6[kcopy-1]
  elif ( l == 13 ):
    theta = OddThetaZero6[kcopy-1]
  elif ( l == 14 ):
    theta = EvenThetaZero7[kcopy-1]
  elif ( l == 15 ):
    theta = OddThetaZero7[kcopy-1]
  elif ( l == 16 ):
    theta = EvenThetaZero8[kcopy-1]
  elif ( l == 17 ):
    theta = OddThetaZero8[kcopy-1]
  elif ( l == 18 ):
    theta = EvenThetaZero9[kcopy-1]
  elif ( l == 19 ):
    theta = OddThetaZero9[kcopy-1]
  elif ( l == 20 ):
    theta = EvenThetaZero10[kcopy-1]
  elif ( l == 21 ):
    theta = OddThetaZero10[kcopy-1]
  elif ( l == 22 ):
    theta = EvenThetaZero11[kcopy-1]
  elif ( l == 23 ):
    theta = OddThetaZero11[kcopy-1]
  elif ( l == 24 ):
    theta = EvenThetaZero12[kcopy-1]
  elif ( l == 25 ):
    theta = OddThetaZero12[kcopy-1]
  elif ( l == 26 ):
    theta = EvenThetaZero13[kcopy-1]
  elif ( l == 27 ):
    theta = OddThetaZero13[kcopy-1]
  elif ( l == 28 ):
    theta = EvenThetaZero14[kcopy-1]
  elif ( l == 29 ):
    theta = OddThetaZero14[kcopy-1]
  elif ( l == 30 ):
    theta = EvenThetaZero15[kcopy-1]
  elif ( l == 31 ):
    theta = OddThetaZero15[kcopy-1]
  elif ( l == 32 ):
    theta = EvenThetaZero16[kcopy-1]
  elif ( l == 33 ):
    theta = OddThetaZero16[kcopy-1]
  elif ( l == 34 ):
    theta = EvenThetaZero17[kcopy-1]
  elif ( l == 35 ):
    theta = OddThetaZero17[kcopy-1]
  elif ( l == 36 ):
    theta = EvenThetaZero18[kcopy-1]
  elif ( l == 37 ):
    theta = OddThetaZero18[kcopy-1]
  elif ( l == 38 ):
    theta = EvenThetaZero19[kcopy-1]
  elif ( l == 39 ):
    theta = OddThetaZero19[kcopy-1]
  elif ( l == 40 ):
    theta = EvenThetaZero20[kcopy-1]
  elif ( l == 41 ):
    theta = OddThetaZero20[kcopy-1]
  elif ( l == 42 ):
    theta = EvenThetaZero21[kcopy-1]
  elif ( l == 43 ):
    theta = OddThetaZero21[kcopy-1]
  elif ( l == 44 ):
    theta = EvenThetaZero22[kcopy-1]
  elif ( l == 45 ):
    theta = OddThetaZero22[kcopy-1]
  elif ( l == 46 ):
    theta = EvenThetaZero23[kcopy-1]
  elif ( l == 47 ):
    theta = OddThetaZero23[kcopy-1]
  elif ( l == 48 ):
    theta = EvenThetaZero24[kcopy-1]
  elif ( l == 49 ):
    theta = OddThetaZero24[kcopy-1]
  elif ( l == 50 ):
    theta = EvenThetaZero25[kcopy-1]
  elif ( l == 51 ):
    theta = OddThetaZero25[kcopy-1]
  elif ( l == 52 ):
    theta = EvenThetaZero26[kcopy-1]
  elif ( l == 53 ):
    theta = OddThetaZero26[kcopy-1]
  elif ( l == 54 ):
    theta = EvenThetaZero27[kcopy-1]
  elif ( l == 55 ):
    theta = OddThetaZero27[kcopy-1]
  elif ( l == 56 ):
    theta = EvenThetaZero28[kcopy-1]
  elif ( l == 57 ):
    theta = OddThetaZero28[kcopy-1]
  elif ( l == 58 ):
    theta = EvenThetaZero29[kcopy-1]
  elif ( l == 59 ):
    theta = OddThetaZero29[kcopy-1]
  elif ( l == 60 ):
    theta = EvenThetaZero30[kcopy-1]
  elif ( l == 61 ):
    theta = OddThetaZero30[kcopy-1]
  elif ( l == 62 ):
    theta = EvenThetaZero31[kcopy-1]
  elif ( l == 63 ):
    theta = OddThetaZero31[kcopy-1]
  elif ( l == 64 ):
    theta = EvenThetaZero32[kcopy-1]
  elif ( l == 65 ):
    theta = OddThetaZero32[kcopy-1]
  elif ( l == 66 ):
    theta = EvenThetaZero33[kcopy-1]
  elif ( l == 67 ):
    theta = OddThetaZero33[kcopy-1]
  elif ( l == 68 ):
    theta = EvenThetaZero34[kcopy-1]
  elif ( l == 69 ):
    theta = OddThetaZero34[kcopy-1]
  elif ( l == 70 ):
    theta = EvenThetaZero35[kcopy-1]
  elif ( l == 71 ):
    theta = OddThetaZero35[kcopy-1]
  elif ( l == 72 ):
    theta = EvenThetaZero36[kcopy-1]
  elif ( l == 73 ):
    theta = OddThetaZero36[kcopy-1]
  elif ( l == 74 ):
    theta = EvenThetaZero37[kcopy-1]
  elif ( l == 75 ):
    theta = OddThetaZero37[kcopy-1]
  elif ( l == 76 ):
    theta = EvenThetaZero38[kcopy-1]
  elif ( l == 77 ):
    theta = OddThetaZero38[kcopy-1]
  elif ( l == 78 ):
    theta = EvenThetaZero39[kcopy-1]
  elif ( l == 79 ):
    theta = OddThetaZero39[kcopy-1]
  elif ( l == 80 ):
    theta = EvenThetaZero40[kcopy-1]
  elif ( l == 81 ):
    theta = OddThetaZero40[kcopy-1]
  elif ( l == 82 ):
    theta = EvenThetaZero41[kcopy-1]
  elif ( l == 83 ):
    theta = OddThetaZero41[kcopy-1]
  elif ( l == 84 ):
    theta = EvenThetaZero42[kcopy-1]
  elif ( l == 85 ):
    theta = OddThetaZero42[kcopy-1]
  elif ( l == 86 ):
    theta = EvenThetaZero43[kcopy-1]
  elif ( l == 87 ):
    theta = OddThetaZero43[kcopy-1]
  elif ( l == 88 ):
    theta = EvenThetaZero44[kcopy-1]
  elif ( l == 89 ):
    theta = OddThetaZero44[kcopy-1]
  elif ( l == 90 ):
    theta = EvenThetaZero45[kcopy-1]
  elif ( l == 91 ):
    theta = OddThetaZero45[kcopy-1]
  elif ( l == 92 ):
    theta = EvenThetaZero46[kcopy-1]
  elif ( l == 93 ):
    theta = OddThetaZero46[kcopy-1]
  elif ( l == 94 ):
    theta = EvenThetaZero47[kcopy-1]
  elif ( l == 95 ):
    theta = OddThetaZero47[kcopy-1]
  elif ( l == 96 ):
    theta = EvenThetaZero48[kcopy-1]
  elif ( l == 97 ):
    theta = OddThetaZero48[kcopy-1]
  elif ( l == 98 ):
    theta = EvenThetaZero49[kcopy-1]
  elif ( l == 99 ):
    theta = OddThetaZero49[kcopy-1]
  elif ( l == 100 ):
    theta = EvenThetaZero50[kcopy-1]

  if ( ( 2 * k - 1 ) <= l ):
    theta = np.pi - theta

  return theta

def legendre_theta_test ( ):

#*****************************************************************************80
#
## LEGENDRE_THETA_TEST tests LEGENDRE_THETA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'LEGENDRE_THETA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LEGENDRE_THETA returns the K-th theta value for' )
  print ( '  a Gauss Legendre rule of order L.' )

  for l in range ( 1, 11 ):
    print ( '' )
    print ( '  Gauss Legendre rule of order %d' % ( l ) )
    print ( '' )
    print ( '   K       Theta      Cos(Theta)' )
    print ( '' )
    for k in range ( 1, l + 1 ):
      theta = legendre_theta ( l, k )
      print ( '  %2d  %14.6g  %14.6g' % ( k, theta, np.cos ( theta ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_THETA_TEST:' )
  print ( '  Normal end of execution.' )
  return

def legendre_weight ( l, k ):

#*****************************************************************************80
#
## LEGENDRE_WEIGHT returns the K-th weight in an L-point Legendre rule.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    Original C++ version by Ignace Bogaert.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
#  Parameters:
#
#    Input, integer L, the number of points in the given rule.
#    1 <= L.
#
#    Input, integer K, the index of the point to be returned.
#    1 <= K <= L.
#
#    Output, real WEIGHT, the weight of the point.
#
  import numpy as np
  from sys import exit

  cl = np.array ( [ \
    1.0E+00, \
    1.0E+00, \
   -0.5000000000000000000000000E+00, \
   -0.1500000000000000000000000E+01, \
    0.3750000000000000000000000E+00, \
    0.1875000000000000000000000E+01, \
   -0.3125000000000000000000000E+00, \
   -0.2187500000000000000000000E+01, \
    0.2734375000000000000000000E+00, \
    0.2460937500000000000000000E+01, \
   -0.2460937500000000000000000E+00, \
   -0.2707031250000000000000000E+01, \
    0.2255859375000000000000000E+00, \
    0.2932617187500000000000000E+01, \
   -0.2094726562500000000000000E+00, \
   -0.3142089843750000000000000E+01, \
    0.1963806152343750000000000E+00, \
    0.3338470458984375000000000E+01, \
   -0.1854705810546875000000000E+00, \
   -0.3523941040039062500000000E+01, \
    0.1761970520019531250000000E+00, \
    0.3700138092041015625000000E+01, \
   -0.1681880950927734375000000E+00, \
   -0.3868326187133789062500000E+01, \
    0.1611802577972412109375000E+00, \
    0.4029506444931030273437500E+01, \
   -0.1549810171127319335937500E+00, \
   -0.4184487462043762207031250E+01, \
    0.1494459807872772216796875E+00, \
    0.4333933442831039428710938E+01, \
   -0.1444644480943679809570312E+00, \
   -0.4478397890925407409667969E+01, \
    0.1399499340914189815521240E+00, \
    0.4618347825016826391220093E+01, \
   -0.1358337595593184232711792E+00, \
   -0.4754181584576144814491272E+01, \
    0.1320605995715595781803131E+00, \
    0.4886242184147704392671585E+01, \
   -0.1285853206354659050703049E+00, \
   -0.5014827504783170297741890E+01, \
    0.1253706876195792574435472E+00, \
    0.5140198192402749555185437E+01, \
   -0.1223856712476845132187009E+00, \
   -0.5262583863650434068404138E+01, \
    0.1196041787193280470091850E+00, \
    0.5382188042369762115413323E+01, \
   -0.1170040878776035242481157E+00, \
   -0.5499192130247365639661439E+01, \
    0.1145665027134867841596133E+00, \
    0.5613758632960852423821052E+01, \
   -0.1122751726592170484764210E+00, \
   -0.5726033805620069472297473E+01, \
    0.1101160347234628744672591E+00, \
    0.5836149840343532346764732E+01, \
   -0.1080768488952505990141617E+00, \
   -0.5944226689238782945778894E+01, \
    0.1061469051649782668889088E+00, \
    0.6050373594403761212667803E+01, \
   -0.1043167861104096760804794E+00, \
   -0.6154690380514170888748282E+01, \
    0.1025781730085695148124714E+00, \
    0.6257268553522740403560753E+01, \
   -0.1009236863471409742509799E+00, \
   -0.6358192239869881377811733E+01, \
    0.9934675374796689652830833E-01, \
    0.6457538993617848274340042E+01, \
   -0.9784149990330073142939457E-01, \
   -0.6555380493521149005769436E+01, \
    0.9640265431648748537896230E-01, \
    0.6651783147837636491148399E+01, \
   -0.9502547354053766415926284E-01, \
   -0.6746808621378174155307661E+01, \
    0.9370567529691908549038419E-01, \
    0.6840514296675093240798046E+01, \
   -0.9243938238750126001078440E-01, \
   -0.6932953679062594500808830E+01, \
    0.9122307472450782237906355E-01, \
    0.7024176753787102323187894E+01, \
   -0.9005354812547567081010120E-01, \
   -0.7114230301912577993997995E+01, \
    0.8892787877390722492497493E-01, \
    0.7203158180686485218922970E+01, \
   -0.8784339244739616120637768E-01, \
   -0.7291001573133881380129347E+01, \
    0.8679763777540334976344461E-01, \
    0.7377799210909284729892792E+01, \
   -0.8578836291754982244061386E-01, \
   -0.7463587573826834552333406E+01, \
    0.8481349515712311991287961E-01, \
    0.7548401068983957672246285E+01, \
   -0.8387112298871064080273650E-01, \
   -0.7632272191972668313049022E+01, \
    0.8295948034752900340270676E-01, \
    0.7715231672320197316451729E+01, \
   -0.8207693268425741826012477E-01, \
   -0.7797308605004454734711853E+01, \
    0.8122196463546307015324847E-01, \
    0.7878530569639917804865102E+01, \
   -0.8039316907795834494760308E-01, \
   -0.7958923738717876149812705E+01, \
    0.7958923738717876149812705E-01 ] )
  EvenW1 = np.array ( [ \
    1.0E+00 ] )
  EvenW2 = np.array ( [ \
    0.6521451548625461426269364E+00, \
    0.3478548451374538573730642E+00 ] )
  EvenW3 = np.array ( [ \
    0.4679139345726910473898704E+00, \
    0.3607615730481386075698336E+00, \
    0.1713244923791703450402969E+00 ] )
  EvenW4 = np.array ( [ \
    0.3626837833783619829651504E+00, \
    0.3137066458778872873379622E+00, \
    0.2223810344533744705443556E+00, \
    0.1012285362903762591525320E+00 ] )
  EvenW5 = np.array ( [ \
    0.2955242247147528701738930E+00, \
    0.2692667193099963550912268E+00, \
    0.2190863625159820439955350E+00, \
    0.1494513491505805931457764E+00, \
    0.6667134430868813759356850E-01 ] )
  EvenW6 = np.array ( [ \
    0.2491470458134027850005624E+00, \
    0.2334925365383548087608498E+00, \
    0.2031674267230659217490644E+00, \
    0.1600783285433462263346522E+00, \
    0.1069393259953184309602552E+00, \
    0.4717533638651182719461626E-01 ] )
  EvenW7 = np.array ( [ \
    0.2152638534631577901958766E+00, \
    0.2051984637212956039659240E+00, \
    0.1855383974779378137417164E+00, \
    0.1572031671581935345696019E+00, \
    0.1215185706879031846894145E+00, \
    0.8015808715976020980563266E-01, \
    0.3511946033175186303183410E-01 ] )
  EvenW8 = np.array ( [ \
    0.1894506104550684962853967E+00, \
    0.1826034150449235888667636E+00, \
    0.1691565193950025381893119E+00, \
    0.1495959888165767320815019E+00, \
    0.1246289712555338720524763E+00, \
    0.9515851168249278480992520E-01, \
    0.6225352393864789286284360E-01, \
    0.2715245941175409485178166E-01 ] )
  EvenW9 = np.array ( [ \
    0.1691423829631435918406565E+00, \
    0.1642764837458327229860538E+00, \
    0.1546846751262652449254180E+00, \
    0.1406429146706506512047311E+00, \
    0.1225552067114784601845192E+00, \
    0.1009420441062871655628144E+00, \
    0.7642573025488905652912984E-01, \
    0.4971454889496979645333512E-01, \
    0.2161601352648331031334248E-01 ] )
  EvenW10 = np.array ( [ \
    0.1527533871307258506980843E+00, \
    0.1491729864726037467878288E+00, \
    0.1420961093183820513292985E+00, \
    0.1316886384491766268984948E+00, \
    0.1181945319615184173123774E+00, \
    0.1019301198172404350367504E+00, \
    0.8327674157670474872475850E-01, \
    0.6267204833410906356950596E-01, \
    0.4060142980038694133103928E-01, \
    0.1761400713915211831186249E-01 ] )
  EvenW11 = np.array ( [ \
    0.1392518728556319933754102E+00, \
    0.1365414983460151713525738E+00, \
    0.1311735047870623707329649E+00, \
    0.1232523768105124242855609E+00, \
    0.1129322960805392183934005E+00, \
    0.1004141444428809649320786E+00, \
    0.8594160621706772741444398E-01, \
    0.6979646842452048809496104E-01, \
    0.5229333515268328594031142E-01, \
    0.3377490158481415479330258E-01, \
    0.1462799529827220068498987E-01 ] )
  EvenW12 = np.array ( [ \
    0.1279381953467521569740562E+00, \
    0.1258374563468282961213754E+00, \
    0.1216704729278033912044631E+00, \
    0.1155056680537256013533445E+00, \
    0.1074442701159656347825772E+00, \
    0.9761865210411388826988072E-01, \
    0.8619016153195327591718514E-01, \
    0.7334648141108030573403386E-01, \
    0.5929858491543678074636724E-01, \
    0.4427743881741980616860272E-01, \
    0.2853138862893366318130802E-01, \
    0.1234122979998719954680507E-01 ] )
  EvenW13 = np.array ( [ \
    0.1183214152792622765163711E+00, \
    0.1166604434852965820446624E+00, \
    0.1133618165463196665494407E+00, \
    0.1084718405285765906565795E+00, \
    0.1020591610944254232384142E+00, \
    0.9421380035591414846366474E-01, \
    0.8504589431348523921044770E-01, \
    0.7468414976565974588707538E-01, \
    0.6327404632957483553945402E-01, \
    0.5097582529714781199831990E-01, \
    0.3796238329436276395030342E-01, \
    0.2441785109263190878961718E-01, \
    0.1055137261734300715565387E-01 ] )
  EvenW14 = np.array ( [ \
    0.1100470130164751962823763E+00, \
    0.1087111922582941352535716E+00, \
    0.1060557659228464179104165E+00, \
    0.1021129675780607698142166E+00, \
    0.9693065799792991585048880E-01, \
    0.9057174439303284094218612E-01, \
    0.8311341722890121839039666E-01, \
    0.7464621423456877902393178E-01, \
    0.6527292396699959579339794E-01, \
    0.5510734567571674543148330E-01, \
    0.4427293475900422783958756E-01, \
    0.3290142778230437997763004E-01, \
    0.2113211259277125975149896E-01, \
    0.9124282593094517738816778E-02 ] )
  EvenW15 = np.array ( [ \
    0.1028526528935588403412856E+00, \
    0.1017623897484055045964290E+00, \
    0.9959342058679526706278018E-01, \
    0.9636873717464425963946864E-01, \
    0.9212252223778612871763266E-01, \
    0.8689978720108297980238752E-01, \
    0.8075589522942021535469516E-01, \
    0.7375597473770520626824384E-01, \
    0.6597422988218049512812820E-01, \
    0.5749315621761906648172152E-01, \
    0.4840267283059405290293858E-01, \
    0.3879919256962704959680230E-01, \
    0.2878470788332336934971862E-01, \
    0.1846646831109095914230276E-01, \
    0.7968192496166605615469690E-02 ] )
  EvenW16 = np.array ( [ \
    0.9654008851472780056676488E-01, \
    0.9563872007927485941908208E-01, \
    0.9384439908080456563918026E-01, \
    0.9117387869576388471286854E-01, \
    0.8765209300440381114277140E-01, \
    0.8331192422694675522219922E-01, \
    0.7819389578707030647174106E-01, \
    0.7234579410884850622539954E-01, \
    0.6582222277636184683765034E-01, \
    0.5868409347853554714528360E-01, \
    0.5099805926237617619616316E-01, \
    0.4283589802222668065687810E-01, \
    0.3427386291302143310268716E-01, \
    0.2539206530926205945575196E-01, \
    0.1627439473090567060516896E-01, \
    0.7018610009470096600404748E-02 ] )
  EvenW17 = np.array ( [ \
    0.9095674033025987361533764E-01, \
    0.9020304437064072957394216E-01, \
    0.8870189783569386928707642E-01, \
    0.8646573974703574978424688E-01, \
    0.8351309969984565518702044E-01, \
    0.7986844433977184473881888E-01, \
    0.7556197466003193127083398E-01, \
    0.7062937581425572499903896E-01, \
    0.6511152155407641137854442E-01, \
    0.5905413582752449319396124E-01, \
    0.5250741457267810616824590E-01, \
    0.4552561152335327245382266E-01, \
    0.3816659379638751632176606E-01, \
    0.3049138063844613180944194E-01, \
    0.2256372198549497008409476E-01, \
    0.1445016274859503541520101E-01, \
    0.6229140555908684718603220E-02 ] )
  EvenW18 = np.array ( [ \
    0.8598327567039474749008516E-01, \
    0.8534668573933862749185052E-01, \
    0.8407821897966193493345756E-01, \
    0.8218726670433970951722338E-01, \
    0.7968782891207160190872470E-01, \
    0.7659841064587067452875784E-01, \
    0.7294188500565306135387342E-01, \
    0.6874532383573644261368974E-01, \
    0.6403979735501548955638454E-01, \
    0.5886014424532481730967550E-01, \
    0.5324471397775991909202590E-01, \
    0.4723508349026597841661708E-01, \
    0.4087575092364489547411412E-01, \
    0.3421381077030722992124474E-01, \
    0.2729862149856877909441690E-01, \
    0.2018151529773547153209770E-01, \
    0.1291594728406557440450307E-01, \
    0.5565719664245045361251818E-02 ] )
  EvenW19 = np.array ( [ \
    0.8152502928038578669921876E-01, \
    0.8098249377059710062326952E-01, \
    0.7990103324352782158602774E-01, \
    0.7828784465821094807537540E-01, \
    0.7615366354844639606599344E-01, \
    0.7351269258474345714520658E-01, \
    0.7038250706689895473928292E-01, \
    0.6678393797914041193504612E-01, \
    0.6274093339213305405296984E-01, \
    0.5828039914699720602230556E-01, \
    0.5343201991033231997375704E-01, \
    0.4822806186075868337435238E-01, \
    0.4270315850467443423587832E-01, \
    0.3689408159402473816493978E-01, \
    0.3083950054517505465873166E-01, \
    0.2457973973823237589520214E-01, \
    0.1815657770961323689887502E-01, \
    0.1161344471646867417766868E-01, \
    0.5002880749639345675901886E-02 ] )
  EvenW20 = np.array ( [ \
    0.7750594797842481126372404E-01, \
    0.7703981816424796558830758E-01, \
    0.7611036190062624237155810E-01, \
    0.7472316905796826420018930E-01, \
    0.7288658239580405906051074E-01, \
    0.7061164739128677969548346E-01, \
    0.6791204581523390382569024E-01, \
    0.6480401345660103807455446E-01, \
    0.6130624249292893916653822E-01, \
    0.5743976909939155136661768E-01, \
    0.5322784698393682435499678E-01, \
    0.4869580763507223206143380E-01, \
    0.4387090818567327199167442E-01, \
    0.3878216797447201763997196E-01, \
    0.3346019528254784739267780E-01, \
    0.2793700698002340109848970E-01, \
    0.2224584919416695726150432E-01, \
    0.1642105838190788871286396E-01, \
    0.1049828453115281361474434E-01, \
    0.4521277098533191258471490E-02 ] )
  EvenW21 = np.array ( [ \
    0.7386423423217287999638556E-01, \
    0.7346081345346752826402828E-01, \
    0.7265617524380410488790570E-01, \
    0.7145471426517098292181042E-01, \
    0.6986299249259415976615480E-01, \
    0.6788970337652194485536350E-01, \
    0.6554562436490897892700504E-01, \
    0.6284355804500257640931846E-01, \
    0.5979826222758665431283142E-01, \
    0.5642636935801838164642686E-01, \
    0.5274629569917407034394234E-01, \
    0.4877814079280324502744954E-01, \
    0.4454357777196587787431674E-01, \
    0.4006573518069226176059618E-01, \
    0.3536907109759211083266214E-01, \
    0.3047924069960346836290502E-01, \
    0.2542295952611304788674188E-01, \
    0.2022786956905264475705664E-01, \
    0.1492244369735749414467869E-01, \
    0.9536220301748502411822340E-02, \
    0.4105998604649084610599928E-02 ] )
  EvenW22 = np.array ( [ \
    0.7054915778935406881133824E-01, \
    0.7019768547355821258714200E-01, \
    0.6949649186157257803708402E-01, \
    0.6844907026936666098545864E-01, \
    0.6706063890629365239570506E-01, \
    0.6533811487918143498424096E-01, \
    0.6329007973320385495013890E-01, \
    0.6092673670156196803855800E-01, \
    0.5825985987759549533421064E-01, \
    0.5530273556372805254874660E-01, \
    0.5207009609170446188123162E-01, \
    0.4857804644835203752763920E-01, \
    0.4484398408197003144624282E-01, \
    0.4088651231034621890844686E-01, \
    0.3672534781380887364290888E-01, \
    0.3238122281206982088084682E-01, \
    0.2787578282128101008111450E-01, \
    0.2323148190201921062895910E-01, \
    0.1847148173681474917204335E-01, \
    0.1361958675557998552020491E-01, \
    0.8700481367524844122565470E-02, \
    0.3745404803112777515171456E-02 ] )
  EvenW23 = np.array ( [ \
    0.6751868584903645882021418E-01, \
    0.6721061360067817586237416E-01, \
    0.6659587476845488737576196E-01, \
    0.6567727426778120737875756E-01, \
    0.6445900346713906958827948E-01, \
    0.6294662106439450817895206E-01, \
    0.6114702772465048101535670E-01, \
    0.5906843459554631480755080E-01, \
    0.5672032584399123581687444E-01, \
    0.5411341538585675449163752E-01, \
    0.5125959800714302133536554E-01, \
    0.4817189510171220053046892E-01, \
    0.4486439527731812676709458E-01, \
    0.4135219010967872970421980E-01, \
    0.3765130535738607132766076E-01, \
    0.3377862799910689652060416E-01, \
    0.2975182955220275579905234E-01, \
    0.2558928639713001063470016E-01, \
    0.2130999875413650105447862E-01, \
    0.1693351400783623804623151E-01, \
    0.1247988377098868420673525E-01, \
    0.7969898229724622451610710E-02, \
    0.3430300868107048286016700E-02 ] )
  EvenW24 = np.array ( [ \
    0.6473769681268392250302496E-01, \
    0.6446616443595008220650418E-01, \
    0.6392423858464818662390622E-01, \
    0.6311419228625402565712596E-01, \
    0.6203942315989266390419786E-01, \
    0.6070443916589388005296916E-01, \
    0.5911483969839563574647484E-01, \
    0.5727729210040321570515042E-01, \
    0.5519950369998416286820356E-01, \
    0.5289018948519366709550490E-01, \
    0.5035903555385447495780746E-01, \
    0.4761665849249047482590674E-01, \
    0.4467456085669428041944838E-01, \
    0.4154508294346474921405856E-01, \
    0.3824135106583070631721688E-01, \
    0.3477722256477043889254814E-01, \
    0.3116722783279808890206628E-01, \
    0.2742650970835694820007336E-01, \
    0.2357076083932437914051962E-01, \
    0.1961616045735552781446139E-01, \
    0.1557931572294384872817736E-01, \
    0.1147723457923453948959265E-01, \
    0.7327553901276262102386656E-02, \
    0.3153346052305838632678320E-02 ] )
  EvenW25 = np.array ( [ \
    0.6217661665534726232103316E-01, \
    0.6193606742068324338408750E-01, \
    0.6145589959031666375640678E-01, \
    0.6073797084177021603175000E-01, \
    0.5978505870426545750957640E-01, \
    0.5860084981322244583512250E-01, \
    0.5718992564772838372302946E-01, \
    0.5555774480621251762356746E-01, \
    0.5371062188899624652345868E-01, \
    0.5165570306958113848990528E-01, \
    0.4940093844946631492124360E-01, \
    0.4695505130394843296563322E-01, \
    0.4432750433880327549202254E-01, \
    0.4152846309014769742241230E-01, \
    0.3856875661258767524477018E-01, \
    0.3545983561514615416073452E-01, \
    0.3221372822357801664816538E-01, \
    0.2884299358053519802990658E-01, \
    0.2536067357001239044019428E-01, \
    0.2178024317012479298159128E-01, \
    0.1811556071348939035125903E-01, \
    0.1438082276148557441937880E-01, \
    0.1059054838365096926356876E-01, \
    0.6759799195745401502778824E-02, \
    0.2908622553155140958394976E-02 ] )
  EvenW26 = np.array ( [ \
    0.5981036574529186024778538E-01, \
    0.5959626017124815825831088E-01, \
    0.5916881546604297036933200E-01, \
    0.5852956177181386855029062E-01, \
    0.5768078745252682765393200E-01, \
    0.5662553090236859719080832E-01, \
    0.5536756966930265254904124E-01, \
    0.5391140693275726475083694E-01, \
    0.5226225538390699303439404E-01, \
    0.5042601856634237721821144E-01, \
    0.4840926974407489685396032E-01, \
    0.4621922837278479350764582E-01, \
    0.4386373425900040799512978E-01, \
    0.4135121950056027167904044E-01, \
    0.3869067831042397898510146E-01, \
    0.3589163483509723294194276E-01, \
    0.3296410908971879791501014E-01, \
    0.2991858114714394664128188E-01, \
    0.2676595374650401344949324E-01, \
    0.2351751355398446159032286E-01, \
    0.2018489150798079220298930E-01, \
    0.1678002339630073567792252E-01, \
    0.1331511498234096065660116E-01, \
    0.9802634579462752061952706E-02, \
    0.6255523962973276899717754E-02, \
    0.2691316950047111118946698E-02 ] )
  EvenW27 = np.array ( [ \
    0.5761753670714702467237616E-01, \
    0.5742613705411211485929010E-01, \
    0.5704397355879459856782852E-01, \
    0.5647231573062596503104434E-01, \
    0.5571306256058998768336982E-01, \
    0.5476873621305798630622270E-01, \
    0.5364247364755361127210060E-01, \
    0.5233801619829874466558872E-01, \
    0.5085969714618814431970910E-01, \
    0.4921242732452888606879048E-01, \
    0.4740167880644499105857626E-01, \
    0.4543346672827671397485208E-01, \
    0.4331432930959701544192564E-01, \
    0.4105130613664497422171834E-01, \
    0.3865191478210251683685736E-01, \
    0.3612412584038355258288694E-01, \
    0.3347633646437264571604038E-01, \
    0.3071734249787067605400450E-01, \
    0.2785630931059587028700164E-01, \
    0.2490274146720877305005456E-01, \
    0.2186645142285308594551102E-01, \
    0.1875752762146937791200757E-01, \
    0.1558630303592413170296832E-01, \
    0.1236332812884764416646861E-01, \
    0.9099369455509396948032734E-02, \
    0.5805611015239984878826112E-02, \
    0.2497481835761585775945054E-02 ] )
  EvenW28 = np.array ( [ \
    0.5557974630651439584627342E-01, \
    0.5540795250324512321779340E-01, \
    0.5506489590176242579630464E-01, \
    0.5455163687088942106175058E-01, \
    0.5386976186571448570895448E-01, \
    0.5302137852401076396799152E-01, \
    0.5200910915174139984305222E-01, \
    0.5083608261779848056012412E-01, \
    0.4950592468304757891996610E-01, \
    0.4802274679360025812073550E-01, \
    0.4639113337300189676219012E-01, \
    0.4461612765269228321341510E-01, \
    0.4270321608466708651103858E-01, \
    0.4065831138474451788012514E-01, \
    0.3848773425924766248682568E-01, \
    0.3619819387231518603588452E-01, \
    0.3379676711561176129542654E-01, \
    0.3129087674731044786783572E-01, \
    0.2868826847382274172988602E-01, \
    0.2599698705839195219181960E-01, \
    0.2322535156256531693725830E-01, \
    0.2038192988240257263480560E-01, \
    0.1747551291140094650495930E-01, \
    0.1451508927802147180777130E-01, \
    0.1150982434038338217377419E-01, \
    0.8469063163307887661628584E-02, \
    0.5402522246015337761313780E-02, \
    0.2323855375773215501098716E-02 ] )
  EvenW29 = np.array ( [ \
    0.5368111986333484886390600E-01, \
    0.5352634330405825210061082E-01, \
    0.5321723644657901410348096E-01, \
    0.5275469052637083342964580E-01, \
    0.5214003918366981897126058E-01, \
    0.5137505461828572547451486E-01, \
    0.5046194247995312529765992E-01, \
    0.4940333550896239286651076E-01, \
    0.4820228594541774840657052E-01, \
    0.4686225672902634691841818E-01, \
    0.4538711151481980250398048E-01, \
    0.4378110353364025103902560E-01, \
    0.4204886332958212599457020E-01, \
    0.4019538540986779688807676E-01, \
    0.3822601384585843322945902E-01, \
    0.3614642686708727054078062E-01, \
    0.3396262049341601079772722E-01, \
    0.3168089125380932732029244E-01, \
    0.2930781804416049071839382E-01, \
    0.2685024318198186847590714E-01, \
    0.2431525272496395254025850E-01, \
    0.2171015614014623576691612E-01, \
    0.1904246546189340865578709E-01, \
    0.1631987423497096505212063E-01, \
    0.1355023711298881214517933E-01, \
    0.1074155353287877411685532E-01, \
    0.7901973849998674754018608E-02, \
    0.5039981612650243085015810E-02, \
    0.2167723249627449943047768E-02 ] )
  EvenW30 = np.array ( [ \
    0.5190787763122063973286496E-01, \
    0.5176794317491018754380368E-01, \
    0.5148845150098093399504444E-01, \
    0.5107015606985562740454910E-01, \
    0.5051418453250937459823872E-01, \
    0.4982203569055018101115930E-01, \
    0.4899557545575683538947578E-01, \
    0.4803703181997118096366674E-01, \
    0.4694898884891220484701330E-01, \
    0.4573437971611448664719662E-01, \
    0.4439647879578711332778398E-01, \
    0.4293889283593564195423128E-01, \
    0.4136555123558475561316394E-01, \
    0.3968069545238079947012286E-01, \
    0.3788886756924344403094056E-01, \
    0.3599489805108450306657888E-01, \
    0.3400389272494642283491466E-01, \
    0.3192121901929632894945890E-01, \
    0.2975249150078894524083642E-01, \
    0.2750355674992479163522324E-01, \
    0.2518047762152124837957096E-01, \
    0.2278951694399781986378308E-01, \
    0.2033712072945728677503268E-01, \
    0.1782990101420772026039605E-01, \
    0.1527461859678479930672510E-01, \
    0.1267816647681596013149540E-01, \
    0.1004755718228798435788578E-01, \
    0.7389931163345455531517530E-02, \
    0.4712729926953568640893942E-02, \
    0.2026811968873758496433874E-02 ] )
  EvenW31 = np.array ( [ \
    0.5024800037525628168840300E-01, \
    0.5012106956904328807480410E-01, \
    0.4986752859495239424476130E-01, \
    0.4948801791969929252786578E-01, \
    0.4898349622051783710485112E-01, \
    0.4835523796347767283480314E-01, \
    0.4760483018410123227045008E-01, \
    0.4673416847841552480220700E-01, \
    0.4574545221457018077723242E-01, \
    0.4464117897712441429364478E-01, \
    0.4342413825804741958006920E-01, \
    0.4209740441038509664302268E-01, \
    0.4066432888241744096828524E-01, \
    0.3912853175196308412331100E-01, \
    0.3749389258228002998561838E-01, \
    0.3576454062276814128558760E-01, \
    0.3394484437941054509111762E-01, \
    0.3203940058162467810633926E-01, \
    0.3005302257398987007700934E-01, \
    0.2799072816331463754123820E-01, \
    0.2585772695402469802709536E-01, \
    0.2365940720868279257451652E-01, \
    0.2140132227766996884117906E-01, \
    0.1908917665857319873250324E-01, \
    0.1672881179017731628855027E-01, \
    0.1432619182380651776740340E-01, \
    0.1188739011701050194481938E-01, \
    0.9418579428420387637936636E-02, \
    0.6926041901830960871704530E-02, \
    0.4416333456930904813271960E-02, \
    0.1899205679513690480402948E-02 ] )
  EvenW32 = np.array ( [ \
    0.4869095700913972038336538E-01, \
    0.4857546744150342693479908E-01, \
    0.4834476223480295716976954E-01, \
    0.4799938859645830772812614E-01, \
    0.4754016571483030866228214E-01, \
    0.4696818281621001732532634E-01, \
    0.4628479658131441729595326E-01, \
    0.4549162792741814447977098E-01, \
    0.4459055816375656306013478E-01, \
    0.4358372452932345337682780E-01, \
    0.4247351512365358900733972E-01, \
    0.4126256324262352861015628E-01, \
    0.3995374113272034138665686E-01, \
    0.3855015317861562912896262E-01, \
    0.3705512854024004604041492E-01, \
    0.3547221325688238381069330E-01, \
    0.3380516183714160939156536E-01, \
    0.3205792835485155358546770E-01, \
    0.3023465707240247886797386E-01, \
    0.2833967261425948322751098E-01, \
    0.2637746971505465867169136E-01, \
    0.2435270256871087333817770E-01, \
    0.2227017380838325415929788E-01, \
    0.2013482315353020937234076E-01, \
    0.1795171577569734308504602E-01, \
    0.1572603047602471932196614E-01, \
    0.1346304789671864259806029E-01, \
    0.1116813946013112881859029E-01, \
    0.8846759826363947723030856E-02, \
    0.6504457968978362856118112E-02, \
    0.4147033260562467635287472E-02, \
    0.1783280721696432947292054E-02 ] )
  EvenW33 = np.array ( [ \
    0.4722748126299855484563332E-01, \
    0.4712209828764473218544518E-01, \
    0.4691156748762082774625404E-01, \
    0.4659635863958410362582412E-01, \
    0.4617717509791597547166640E-01, \
    0.4565495222527305612043888E-01, \
    0.4503085530544150021519278E-01, \
    0.4430627694315316190460328E-01, \
    0.4348283395666747864757528E-01, \
    0.4256236377005571631890662E-01, \
    0.4154692031324188131773448E-01, \
    0.4043876943895497912586836E-01, \
    0.3924038386682833018781280E-01, \
    0.3795443766594162094913028E-01, \
    0.3658380028813909441368980E-01, \
    0.3513153016547255590064132E-01, \
    0.3360086788611223267034862E-01, \
    0.3199522896404688727128174E-01, \
    0.3031819621886851919364104E-01, \
    0.2857351178293187118282268E-01, \
    0.2676506875425000190879332E-01, \
    0.2489690251475737263773110E-01, \
    0.2297318173532665591809836E-01, \
    0.2099819909186462577733052E-01, \
    0.1897636172277132593486659E-01, \
    0.1691218147224521718035102E-01, \
    0.1481026500273396017364296E-01, \
    0.1267530398126168187644599E-01, \
    0.1051206598770575465737803E-01, \
    0.8325388765990901416725080E-02, \
    0.6120192018447936365568516E-02, \
    0.3901625641744248259228942E-02, \
    0.1677653744007238599334225E-02 ] )
  EvenW34 = np.array ( [ \
    0.4584938738725097468656398E-01, \
    0.4575296541606795051900614E-01, \
    0.4556032425064828598070770E-01, \
    0.4527186901844377786941174E-01, \
    0.4488820634542666782635216E-01, \
    0.4441014308035275590934876E-01, \
    0.4383868459795605201060492E-01, \
    0.4317503268464422322584344E-01, \
    0.4242058301114249930061428E-01, \
    0.4157692219740291648457550E-01, \
    0.4064582447595407614088174E-01, \
    0.3962924796071230802540652E-01, \
    0.3852933052910671449325372E-01, \
    0.3734838532618666771607896E-01, \
    0.3608889590017987071497568E-01, \
    0.3475351097975151316679320E-01, \
    0.3334503890398068790314300E-01, \
    0.3186644171682106493934736E-01, \
    0.3032082893855398034157906E-01, \
    0.2871145102748499071080394E-01, \
    0.2704169254590396155797848E-01, \
    0.2531506504517639832390244E-01, \
    0.2353519968587633336129308E-01, \
    0.2170583961037807980146532E-01, \
    0.1983083208795549829102926E-01, \
    0.1791412045792315248940600E-01, \
    0.1595973590961380007213420E-01, \
    0.1397178917445765581596455E-01, \
    0.1195446231976944210322336E-01, \
    0.9912001251585937209131520E-02, \
    0.7848711393177167415052160E-02, \
    0.5768969918729952021468320E-02, \
    0.3677366595011730633570254E-02, \
    0.1581140256372912939103728E-02 ] )
  EvenW35 = np.array ( [ \
    0.4454941715975466720216750E-01, \
    0.4446096841724637082355728E-01, \
    0.4428424653905540677579966E-01, \
    0.4401960239018345875735580E-01, \
    0.4366756139720144025254848E-01, \
    0.4322882250506869978939520E-01, \
    0.4270425678944977776996576E-01, \
    0.4209490572728440602098398E-01, \
    0.4140197912904520863822652E-01, \
    0.4062685273678961635122600E-01, \
    0.3977106549277656747784952E-01, \
    0.3883631648407340397900292E-01, \
    0.3782446156922281719727230E-01, \
    0.3673750969367269534804046E-01, \
    0.3557761890129238053276980E-01, \
    0.3434709204990653756854510E-01, \
    0.3304837223937242047087430E-01, \
    0.3168403796130848173465310E-01, \
    0.3025679798015423781653688E-01, \
    0.2876948595580828066131070E-01, \
    0.2722505481866441715910742E-01, \
    0.2562657090846848279898494E-01, \
    0.2397720788910029227868640E-01, \
    0.2228024045225659583389064E-01, \
    0.2053903782432645338449270E-01, \
    0.1875705709313342341545081E-01, \
    0.1693783637630293253183738E-01, \
    0.1508498786544312768229492E-01, \
    0.1320219081467674762507440E-01, \
    0.1129318464993153764963015E-01, \
    0.9361762769699026811498692E-02, \
    0.7411769363190210362109460E-02, \
    0.5447111874217218312821680E-02, \
    0.3471894893078143254999524E-02, \
    0.1492721288844515731042666E-02 ] )
  EvenW36 = np.array ( [ \
    0.4332111216548653707639384E-01, \
    0.4323978130522261748526514E-01, \
    0.4307727227491369974525036E-01, \
    0.4283389016833881366683982E-01, \
    0.4251009191005772007780078E-01, \
    0.4210648539758646414658732E-01, \
    0.4162382836013859820760788E-01, \
    0.4106302693607506110193610E-01, \
    0.4042513397173397004332898E-01, \
    0.3971134704483490178239872E-01, \
    0.3892300621616966379996300E-01, \
    0.3806159151380216383437540E-01, \
    0.3712872015450289946055536E-01, \
    0.3612614350763799298563092E-01, \
    0.3505574380721787043413848E-01, \
    0.3391953061828605949719618E-01, \
    0.3271963706429384670431246E-01, \
    0.3145831582256181397777608E-01, \
    0.3013793489537547929298290E-01, \
    0.2876097316470176109512506E-01, \
    0.2733001573895093443379638E-01, \
    0.2584774910065589028389804E-01, \
    0.2431695606441916432634724E-01, \
    0.2274051055503575445593134E-01, \
    0.2112137221644055350981986E-01, \
    0.1946258086329427804301667E-01, \
    0.1776725078920065359435915E-01, \
    0.1603856495028515521816122E-01, \
    0.1427976905455419326655572E-01, \
    0.1249416561987375776778277E-01, \
    0.1068510816535189715895734E-01, \
    0.8855996073706153383956510E-02, \
    0.7010272321861863296081600E-02, \
    0.5151436018790886908248502E-02, \
    0.3283169774667495801897558E-02, \
    0.1411516393973434135715864E-02 ] )
  EvenW37 = np.array ( [ \
    0.4215870660994342212223066E-01, \
    0.4208374996915697247489576E-01, \
    0.4193396995777702146995522E-01, \
    0.4170963287924075437870998E-01, \
    0.4141113759675351082006810E-01, \
    0.4103901482412726684741876E-01, \
    0.4059392618219472805807676E-01, \
    0.4007666302247696675915112E-01, \
    0.3948814502019646832363280E-01, \
    0.3882941853913770775808220E-01, \
    0.3810165477126324889635168E-01, \
    0.3730614765439415573370658E-01, \
    0.3644431157165856448181076E-01, \
    0.3551767883680095992585374E-01, \
    0.3452789696982646100333388E-01, \
    0.3347672576782876626372244E-01, \
    0.3236603417621699952527994E-01, \
    0.3119779696591542603337254E-01, \
    0.2997409122246118733996502E-01, \
    0.2869709265326987534209508E-01, \
    0.2736907171967935230243778E-01, \
    0.2599238960072378786677346E-01, \
    0.2456949399594276724564910E-01, \
    0.2310291477491582303093246E-01, \
    0.2159525948167588896969968E-01, \
    0.2004920870279494425273506E-01, \
    0.1846751130897987978285368E-01, \
    0.1685297958202485358484807E-01, \
    0.1520848424340123480887426E-01, \
    0.1353694941178749434105245E-01, \
    0.1184134754749966732316814E-01, \
    0.1012469453828730542112095E-01, \
    0.8390045433971397064089364E-02, \
    0.6640492909114357634760192E-02, \
    0.4879179758594144584288316E-02, \
    0.3109420149896754678673688E-02, \
    0.1336761650069883550325931E-02 ] )
  EvenW38 = np.array ( [ \
    0.4105703691622942259325972E-01, \
    0.4098780546479395154130842E-01, \
    0.4084945930182849228039176E-01, \
    0.4064223171029473877745496E-01, \
    0.4036647212284402315409558E-01, \
    0.4002264553259682611646172E-01, \
    0.3961133170906205842314674E-01, \
    0.3913322422051844076750754E-01, \
    0.3858912926450673834292118E-01, \
    0.3797996430840528319523540E-01, \
    0.3730675654238160982756716E-01, \
    0.3657064114732961700724404E-01, \
    0.3577285938071394752777924E-01, \
    0.3491475648355076744412550E-01, \
    0.3399777941205638084674262E-01, \
    0.3302347439779174100654158E-01, \
    0.3199348434042160006853510E-01, \
    0.3090954603749159538993714E-01, \
    0.2977348725590504095670750E-01, \
    0.2858722365005400377397500E-01, \
    0.2735275553182752167415270E-01, \
    0.2607216449798598352427480E-01, \
    0.2474760992065967164326474E-01, \
    0.2338132530701118662247962E-01, \
    0.2197561453441624916801320E-01, \
    0.2053284796790802109297466E-01, \
    0.1905545846719058280680223E-01, \
    0.1754593729147423095419928E-01, \
    0.1600682991224857088850986E-01, \
    0.1444073174827667993988980E-01, \
    0.1285028384751014494492467E-01, \
    0.1123816856966768723967455E-01, \
    0.9607105414713754082404616E-02, \
    0.7959847477239734621118374E-02, \
    0.6299180497328445866575096E-02, \
    0.4627935228037421326126844E-02, \
    0.2949102953642474900394994E-02, \
    0.1267791634085359663272804E-02 ] )
  EvenW39 = np.array ( [ \
    0.4001146511842048298877858E-01, \
    0.3994739036908802487930490E-01, \
    0.3981934348036408922503176E-01, \
    0.3962752950781054295639346E-01, \
    0.3937225562423312193722022E-01, \
    0.3905393062777341314731136E-01, \
    0.3867306428725767400389548E-01, \
    0.3823026652585098764962036E-01, \
    0.3772624644432424786429014E-01, \
    0.3716181118549838685067108E-01, \
    0.3653786464168470064819248E-01, \
    0.3585540600719169544500572E-01, \
    0.3511552817821718947488010E-01, \
    0.3431941600268909029029166E-01, \
    0.3346834438285897797298150E-01, \
    0.3256367623368904440805548E-01, \
    0.3160686030030479773888294E-01, \
    0.3059942883801304528943330E-01, \
    0.2954299515860694641162030E-01, \
    0.2843925104689751626239046E-01, \
    0.2728996405162436486456432E-01, \
    0.2609697465510883502983394E-01, \
    0.2486219332622245076144308E-01, \
    0.2358759746145747209645146E-01, \
    0.2227522821911388676305032E-01, \
    0.2092718725187772678537816E-01, \
    0.1954563334339992337791787E-01, \
    0.1813277895498232864440684E-01, \
    0.1669088668934389186621294E-01, \
    0.1522226568017845169331591E-01, \
    0.1372926792014414839372596E-01, \
    0.1221428454978988639768250E-01, \
    0.1067974215748111335351669E-01, \
    0.9128099227255087276943326E-02, \
    0.7561843189439718826977318E-02, \
    0.5983489944440407989648850E-02, \
    0.4395596039460346742737866E-02, \
    0.2800868811838630411609396E-02, \
    0.1204024566067353280336448E-02 ] )
  EvenW40 = np.array ( [ \
    0.3901781365630665481128044E-01, \
    0.3895839596276953119862554E-01, \
    0.3883965105905196893177418E-01, \
    0.3866175977407646332707712E-01, \
    0.3842499300695942318521238E-01, \
    0.3812971131447763834420674E-01, \
    0.3777636436200139748977496E-01, \
    0.3736549023873049002670538E-01, \
    0.3689771463827600883915092E-01, \
    0.3637374990583597804396502E-01, \
    0.3579439395341605460286146E-01, \
    0.3516052904474759349552658E-01, \
    0.3447312045175392879436434E-01, \
    0.3373321498461152281667534E-01, \
    0.3294193939764540138283636E-01, \
    0.3210049867348777314805654E-01, \
    0.3121017418811470164244288E-01, \
    0.3027232175955798066122008E-01, \
    0.2928836958326784769276746E-01, \
    0.2825981605727686239675312E-01, \
    0.2718822750048638067441898E-01, \
    0.2607523576756511790296854E-01, \
    0.2492253576411549110511808E-01, \
    0.2373188286593010129319242E-01, \
    0.2250509024633246192622164E-01, \
    0.2124402611578200638871032E-01, \
    0.1995061087814199892889169E-01, \
    0.1862681420829903142873492E-01, \
    0.1727465205626930635858456E-01, \
    0.1589618358372568804490352E-01, \
    0.1449350804050907611696272E-01, \
    0.1306876159240133929378674E-01, \
    0.1162411412079782691646643E-01, \
    0.1016176604110306452083288E-01, \
    0.8683945269260858426408640E-02, \
    0.7192904768117312752674654E-02, \
    0.5690922451403198649270494E-02, \
    0.4180313124694895236739096E-02, \
    0.2663533589512681669292770E-02, \
    0.1144950003186941534544369E-02 ] )
  EvenW41 = np.array ( [ \
    0.3807230964014187120769602E-01, \
    0.3801710843143526990530278E-01, \
    0.3790678605050578477946422E-01, \
    0.3774150245427586967153708E-01, \
    0.3752149728818502087157412E-01, \
    0.3724708953872766418784006E-01, \
    0.3691867707095445699853162E-01, \
    0.3653673605160765284219780E-01, \
    0.3610182025872702307569544E-01, \
    0.3561456027872747268049598E-01, \
    0.3507566259211269038478042E-01, \
    0.3448590854915070550737888E-01, \
    0.3384615323699685874463648E-01, \
    0.3315732423990721132775848E-01, \
    0.3242042029434060507783656E-01, \
    0.3163650984090024553762352E-01, \
    0.3080672947521562981366802E-01, \
    0.2993228230001272463508596E-01, \
    0.2901443618076440396145302E-01, \
    0.2805452190745423047171398E-01, \
    0.2705393126512477151978662E-01, \
    0.2601411501601702375386842E-01, \
    0.2493658079624075515577230E-01, \
    0.2382289093004782634222678E-01, \
    0.2267466016491410310244200E-01, \
    0.2149355333077484404348958E-01, \
    0.2028128292691215890157032E-01, \
    0.1903960664017892507303976E-01, \
    0.1777032479849840714698234E-01, \
    0.1647527776398370889101217E-01, \
    0.1515634327076256178846848E-01, \
    0.1381543371412645938772740E-01, \
    0.1245449340114210467973318E-01, \
    0.1107549578175989632022419E-01, \
    0.9680440704371073736965104E-02, \
    0.8271351818383685604431294E-02, \
    0.6850274534183526184325356E-02, \
    0.5419276232446765090703842E-02, \
    0.3980457937856074619030326E-02, \
    0.2536054696856106109823094E-02, \
    0.1090118595275830866109234E-02 ] )
  EvenW42 = np.array ( [ \
    0.3717153701903406760328362E-01, \
    0.3712016261260209427372758E-01, \
    0.3701748480379452058524442E-01, \
    0.3686364550259030771845208E-01, \
    0.3665885732875907563657692E-01, \
    0.3640340331800212248862624E-01, \
    0.3609763653077256670175260E-01, \
    0.3574197956431530727788894E-01, \
    0.3533692396860127616038866E-01, \
    0.3488302956696330845641672E-01, \
    0.3438092368237270062133504E-01, \
    0.3383130027042598480372494E-01, \
    0.3323491896024044407471552E-01, \
    0.3259260400458425718361322E-01, \
    0.3190524314069272748402282E-01, \
    0.3117378636334566129196750E-01, \
    0.3039924461190246977311372E-01, \
    0.2958268837311084528960516E-01, \
    0.2872524620162180221266452E-01, \
    0.2782810316025840603576668E-01, \
    0.2689249918219763751581640E-01, \
    0.2591972735733464772516052E-01, \
    0.2491113214520642888439108E-01, \
    0.2386810751695823938471552E-01, \
    0.2279209502894212933888898E-01, \
    0.2168458183064482298924430E-01, \
    0.2054709860975627861152400E-01, \
    0.1938121747731880864780669E-01, \
    0.1818854979605654992760044E-01, \
    0.1697074395521161134308213E-01, \
    0.1572948309558359820159970E-01, \
    0.1446648278916118624227443E-01, \
    0.1318348867918234598679997E-01, \
    0.1188227408980122349505120E-01, \
    0.1056463762300824526484878E-01, \
    0.9232400784190247014382770E-02, \
    0.7887405752648146382107148E-02, \
    0.6531513687713654601121566E-02, \
    0.5166605182746808329881136E-02, \
    0.3794591650452349696393000E-02, \
    0.2417511265443122855238466E-02, \
    0.1039133516451971889197062E-02 ] )
  EvenW43 = np.array ( [ \
    0.3631239537581333828231516E-01, \
    0.3626450208420238743149194E-01, \
    0.3616877866860063758274494E-01, \
    0.3602535138093525771008956E-01, \
    0.3583440939092405578977942E-01, \
    0.3559620453657549559069116E-01, \
    0.3531105099203420508058466E-01, \
    0.3497932485321009937141316E-01, \
    0.3460146364173769225993442E-01, \
    0.3417796572791990463423808E-01, \
    0.3370938967341755486497158E-01, \
    0.3319635349455159712009034E-01, \
    0.3263953384718992195609868E-01, \
    0.3203966513429401611022852E-01, \
    0.3139753853730286555853332E-01, \
    0.3071400097263205318303994E-01, \
    0.2998995397466493249133840E-01, \
    0.2922635250670994458366154E-01, \
    0.2842420370149349475731242E-01, \
    0.2758456553285124838738412E-01, \
    0.2670854542037220957530654E-01, \
    0.2579729876883953540777106E-01, \
    0.2485202744439983591832606E-01, \
    0.2387397818947900497321768E-01, \
    0.2286444097854800644577274E-01, \
    0.2182474731692762780068420E-01, \
    0.2075626848490914279058154E-01, \
    0.1966041372956217980740210E-01, \
    0.1853862840670985920631482E-01, \
    0.1739239207569054238672012E-01, \
    0.1622321654972902258808405E-01, \
    0.1503264390508137868494523E-01, \
    0.1382224445276667086664874E-01, \
    0.1259361467806969781040954E-01, \
    0.1134837515617770397716730E-01, \
    0.1008816846038610565467284E-01, \
    0.8814657101954815703782366E-02, \
    0.7529521612194562606844596E-02, \
    0.6234459139140123463885784E-02, \
    0.4931184096960103696423408E-02, \
    0.3621439249610901437553882E-02, \
    0.2307087488809902925963262E-02, \
    0.9916432666203635255681510E-03 ] )
  EvenW44 = np.array ( [ \
    0.3549206430171454529606746E-01, \
    0.3544734460447076970614316E-01, \
    0.3535796155642384379366902E-01, \
    0.3522402777945910853287866E-01, \
    0.3504571202900426139658624E-01, \
    0.3482323898139935499312912E-01, \
    0.3455688895080708413486530E-01, \
    0.3424699753602007873736958E-01, \
    0.3389395519761025923989258E-01, \
    0.3349820676595309252806520E-01, \
    0.3306025088074670014528066E-01, \
    0.3258063936273210868623942E-01, \
    0.3205997651840638806926700E-01, \
    0.3149891837860489232004182E-01, \
    0.3089817187191219763370292E-01, \
    0.3025849393394352533513752E-01, \
    0.2958069055361934911335230E-01, \
    0.2886561575763542924647688E-01, \
    0.2811417053440861349157908E-01, \
    0.2732730169885533083562360E-01, \
    0.2650600069943473772140906E-01, \
    0.2565130236896194788477952E-01, \
    0.2476428362076873302532156E-01, \
    0.2384606209185966126357838E-01, \
    0.2289779473478114232724788E-01, \
    0.2192067635998985359563460E-01, \
    0.2091593813057662423225406E-01, \
    0.1988484601127411324360109E-01, \
    0.1882869917375545139470985E-01, \
    0.1774882836032407455649534E-01, \
    0.1664659420821765604511323E-01, \
    0.1552338553693355384016474E-01, \
    0.1438061760129994423593466E-01, \
    0.1321973031362791170818164E-01, \
    0.1204218643958121230973900E-01, \
    0.1084946977542927125940107E-01, \
    0.9643083322053204400769368E-02, \
    0.8424547492702473015098308E-02, \
    0.7195398459796372059759572E-02, \
    0.5957186996138046583131162E-02, \
    0.4711479279598661743021848E-02, \
    0.3459867667862796423976646E-02, \
    0.2204058563143696628535344E-02, \
    0.9473355981619272667700360E-03 ] )
  EvenW45 = np.array ( [ \
    0.3470797248895005792046014E-01, \
    0.3466615208568824018827232E-01, \
    0.3458256166949689141805380E-01, \
    0.3445730196032425617459566E-01, \
    0.3429052388637504193169728E-01, \
    0.3408242840225399546360508E-01, \
    0.3383326624683168725792750E-01, \
    0.3354333764112427668293316E-01, \
    0.3321299192655131651404080E-01, \
    0.3284262714400750457863018E-01, \
    0.3243268955425561691178950E-01, \
    0.3198367310021857603945600E-01, \
    0.3149611881181863607695780E-01, \
    0.3097061415408092094593650E-01, \
    0.3040779231928695269039426E-01, \
    0.2980833146403127548714788E-01, \
    0.2917295389210074248655798E-01, \
    0.2850242518416141631875546E-01, \
    0.2779755327530227515803874E-01, \
    0.2705918748154795852161408E-01, \
    0.2628821747651458736159580E-01, \
    0.2548557221944322848446706E-01, \
    0.2465221883590485293596628E-01, \
    0.2378916145252872321010090E-01, \
    0.2289743998716318463498862E-01, \
    0.2197812889593413383869188E-01, \
    0.2103233587872256311706242E-01, \
    0.2006120054463959596453232E-01, \
    0.1906589303913731842532399E-01, \
    0.1804761263446023616404962E-01, \
    0.1700758628522267570939747E-01, \
    0.1594706715100663901320649E-01, \
    0.1486733308804332405038481E-01, \
    0.1376968511233709343075118E-01, \
    0.1265544583716812886887583E-01, \
    0.1152595788914805885059348E-01, \
    0.1038258230989321461380844E-01, \
    0.9226696957741990940319884E-02, \
    0.8059694944620015658670990E-02, \
    0.6882983208463284314729370E-02, \
    0.5697981560747352600849438E-02, \
    0.4506123613674977864136850E-02, \
    0.3308867243336018195431340E-02, \
    0.2107778774526329891473788E-02, \
    0.9059323712148330937360098E-03 ] )
  EvenW46 = np.array ( [ \
    0.3395777082810234796700260E-01, \
    0.3391860442372254949502722E-01, \
    0.3384031678893360189141840E-01, \
    0.3372299821957387169380074E-01, \
    0.3356678402920367631007550E-01, \
    0.3337185439303681030780114E-01, \
    0.3313843414012938182262046E-01, \
    0.3286679249406566032646806E-01, \
    0.3255724276244004524316198E-01, \
    0.3221014197549332953574452E-01, \
    0.3182589047432008582597260E-01, \
    0.3140493144912217791614030E-01, \
    0.3094775042804103166804096E-01, \
    0.3045487471715832098063528E-01, \
    0.2992687279231107330786762E-01, \
    0.2936435364342281261274650E-01, \
    0.2876796607210717582237958E-01, \
    0.2813839794335440451445112E-01, \
    0.2747637539216417339517938E-01, \
    0.2678266198604032330048838E-01, \
    0.2605805784431417922245786E-01, \
    0.2530339871531322569754810E-01, \
    0.2451955501244097425717108E-01, \
    0.2370743081028191239353720E-01, \
    0.2286796280189254240434106E-01, \
    0.2200211921848585739874382E-01, \
    0.2111089871276246180997612E-01, \
    0.2019532920718748374956428E-01, \
    0.1925646670855947471237209E-01, \
    0.1829539409026755729118717E-01, \
    0.1731321984368977636114053E-01, \
    0.1631107680025595800481463E-01, \
    0.1529012082579650150690625E-01, \
    0.1425152948895392526580707E-01, \
    0.1319650070571113802911160E-01, \
    0.1212625136263771052929676E-01, \
    0.1104201592263539422398575E-01, \
    0.9945045019726082041770092E-02, \
    0.8836604056467877374547944E-02, \
    0.7717971837373568504533128E-02, \
    0.6590439334214895223179124E-02, \
    0.5455308908000870987158870E-02, \
    0.4313895331861700472339122E-02, \
    0.3167535943396097874261610E-02, \
    0.2017671366262838591883234E-02, \
    0.8671851787671421353540866E-03 ] )
  EvenW47 = np.array ( [ \
    0.3323930891781532080070524E-01, \
    0.3320257661860686379876634E-01, \
    0.3312915261254696321600516E-01, \
    0.3301911803949165507667076E-01, \
    0.3287259449712959072614770E-01, \
    0.3268974390660630715252838E-01, \
    0.3247076833358767948450850E-01, \
    0.3221590976496030711281812E-01, \
    0.3192544984141561392584074E-01, \
    0.3159970954621320046477392E-01, \
    0.3123904885046741788219108E-01, \
    0.3084386631534918741110674E-01, \
    0.3041459865164271220328128E-01, \
    0.2995172023714386920008800E-01, \
    0.2945574259243367639719146E-01, \
    0.2892721381560625584227516E-01, \
    0.2836671797657610681272962E-01, \
    0.2777487447163422062065088E-01, \
    0.2715233733896656472388262E-01, \
    0.2649979453589169919669406E-01, \
    0.2581796717861672816440260E-01, \
    0.2510760874535240512858038E-01, \
    0.2436950424366898830634656E-01, \
    0.2360446934301438228050796E-01, \
    0.2281334947335523641001192E-01, \
    0.2199701889094007717339700E-01, \
    0.2115637971222138981504522E-01, \
    0.2029236091701113217988866E-01, \
    0.1940591732198200488605189E-01, \
    0.1849802852566591095380957E-01, \
    0.1756969782614325199872555E-01, \
    0.1662195111266549663832874E-01, \
    0.1565583573251555786002188E-01, \
    0.1467241933449946420426407E-01, \
    0.1367278869060687850644038E-01, \
    0.1265804849763899444482439E-01, \
    0.1162932016112241459607371E-01, \
    0.1058774056495412223672440E-01, \
    0.9534460832865158250063918E-02, \
    0.8470645094534635999910406E-02, \
    0.7397469288142356200862272E-02, \
    0.6316120091036448223107804E-02, \
    0.5227794289507767545307002E-02, \
    0.4133699875407776483295790E-02, \
    0.3035065891038628027389626E-02, \
    0.1933219888725418943121000E-02, \
    0.8308716126821624946495838E-03 ] )
  EvenW48 = np.array ( [ \
    0.3255061449236316624196142E-01, \
    0.3251611871386883598720548E-01, \
    0.3244716371406426936401278E-01, \
    0.3234382256857592842877486E-01, \
    0.3220620479403025066866710E-01, \
    0.3203445623199266321813896E-01, \
    0.3182875889441100653475374E-01, \
    0.3158933077072716855802074E-01, \
    0.3131642559686135581278434E-01, \
    0.3101033258631383742324982E-01, \
    0.3067137612366914901422878E-01, \
    0.3029991542082759379408878E-01, \
    0.2989634413632838598438796E-01, \
    0.2946108995816790597043632E-01, \
    0.2899461415055523654267862E-01, \
    0.2849741106508538564559948E-01, \
    0.2797000761684833443981840E-01, \
    0.2741296272602924282342110E-01, \
    0.2682686672559176219805676E-01, \
    0.2621234073567241391345816E-01, \
    0.2557003600534936149879724E-01, \
    0.2490063322248361028838244E-01, \
    0.2420484179236469128226730E-01, \
    0.2348339908592621984223612E-01, \
    0.2273706965832937400134754E-01, \
    0.2196664443874434919475618E-01, \
    0.2117293989219129898767356E-01, \
    0.2035679715433332459524556E-01, \
    0.1951908114014502241008485E-01, \
    0.1866067962741146738515655E-01, \
    0.1778250231604526083761406E-01, \
    0.1688547986424517245047785E-01, \
    0.1597056290256229138061685E-01, \
    0.1503872102699493800587588E-01, \
    0.1409094177231486091586166E-01, \
    0.1312822956696157263706415E-01, \
    0.1215160467108831963518178E-01, \
    0.1116210209983849859121361E-01, \
    0.1016077053500841575758671E-01, \
    0.9148671230783386632584044E-02, \
    0.8126876925698759217383246E-02, \
    0.7096470791153865269143206E-02, \
    0.6058545504235961683315686E-02, \
    0.5014202742927517692471308E-02, \
    0.3964554338444686673733524E-02, \
    0.2910731817934946408411678E-02, \
    0.1853960788946921732331620E-02, \
    0.7967920655520124294367096E-03 ] )
  EvenW49 = np.array ( [ \
    0.3188987535287646727794502E-01, \
    0.3185743815812401071309920E-01, \
    0.3179259676252863019831786E-01, \
    0.3169541712034925160907410E-01, \
    0.3156599807910805290145092E-01, \
    0.3140447127904656151748860E-01, \
    0.3121100101922626441684056E-01, \
    0.3098578409040993463104290E-01, \
    0.3072904957489366992001356E-01, \
    0.3044105861349325839490764E-01, \
    0.3012210413992189884853100E-01, \
    0.2977251058282947626617570E-01, \
    0.2939263353580649216776328E-01, \
    0.2898285939568834204744914E-01, \
    0.2854360496952788570349054E-01, \
    0.2807531705063613875324586E-01, \
    0.2757847196412239390009986E-01, \
    0.2705357508239612827767608E-01, \
    0.2650116031112363935248738E-01, \
    0.2592178954616244891846836E-01, \
    0.2531605210202609734314644E-01, \
    0.2468456411246099618197954E-01, \
    0.2402796790374549880324124E-01, \
    0.2334693134134927471268304E-01, \
    0.2264214715061843311126274E-01, \
    0.2191433221217865041901888E-01, \
    0.2116422683277485691127980E-01, \
    0.2039259399229191457948346E-01, \
    0.1960021856772633077323700E-01, \
    0.1878790653490468656148738E-01, \
    0.1795648414877062812244296E-01, \
    0.1710679710308990026235402E-01, \
    0.1623970967045369565272614E-01, \
    0.1535610382349775576849818E-01, \
    0.1445687833830440197756895E-01, \
    0.1354294788102946514364726E-01, \
    0.1261524207892195285778215E-01, \
    0.1167470457713812428742924E-01, \
    0.1072229208322431712024324E-01, \
    0.9758973402174096835348026E-02, \
    0.8785728467392263202699392E-02, \
    0.7803547379100754890979542E-02, \
    0.6813429479165215998771186E-02, \
    0.5816382546439639112764538E-02, \
    0.4813422398586770918478190E-02, \
    0.3805574085352359565512666E-02, \
    0.2793881135722130870629084E-02, \
    0.1779477041014528741695358E-02, \
    0.7647669822743134580383448E-03 ] )
  EvenW50 = np.array ( [ \
    0.3125542345386335694764248E-01, \
    0.3122488425484935773237650E-01, \
    0.3116383569620990678381832E-01, \
    0.3107233742756651658781016E-01, \
    0.3095047885049098823406346E-01, \
    0.3079837903115259042771392E-01, \
    0.3061618658398044849645950E-01, \
    0.3040407952645482001650792E-01, \
    0.3016226510516914491906862E-01, \
    0.2989097959333283091683684E-01, \
    0.2959048805991264251175454E-01, \
    0.2926108411063827662011896E-01, \
    0.2890308960112520313487610E-01, \
    0.2851685432239509799093676E-01, \
    0.2810275565910117331764820E-01, \
    0.2766119822079238829420408E-01, \
    0.2719261344657688013649158E-01, \
    0.2669745918357096266038448E-01, \
    0.2617621923954567634230892E-01, \
    0.2562940291020811607564182E-01, \
    0.2505754448157958970376402E-01, \
    0.2446120270795705271997480E-01, \
    0.2384096026596820596256040E-01, \
    0.2319742318525412162248878E-01, \
    0.2253122025633627270179672E-01, \
    0.2184300241624738631395360E-01, \
    0.2113344211252764154267220E-01, \
    0.2040323264620943276683910E-01, \
    0.1965308749443530586538157E-01, \
    0.1888373961337490455294131E-01, \
    0.1809594072212811666439111E-01, \
    0.1729046056832358243934388E-01, \
    0.1646808617614521264310506E-01, \
    0.1562962107754600272393719E-01, \
    0.1477588452744130176887969E-01, \
    0.1390771070371877268795387E-01, \
    0.1302594789297154228555807E-01, \
    0.1213145766297949740774437E-01, \
    0.1122511402318597711722209E-01, \
    0.1030780257486896958578198E-01, \
    0.9380419653694457951417628E-02, \
    0.8443871469668971402620252E-02, \
    0.7499073255464711578829804E-02, \
    0.6546948450845322764152444E-02, \
    0.5588428003865515157213478E-02, \
    0.4624450063422119351093868E-02, \
    0.3655961201326375182342828E-02, \
    0.2683925371553482419437272E-02, \
    0.1709392653518105239533969E-02, \
    0.7346344905056717304142370E-03 ] )
  
  OddW1 = np.array ( [ \
    0.5555555555555555555555555E+00  ] )
  OddW2 = np.array ( [ \
    0.4786286704993664680412916E+00, \
    0.2369268850561890875142644E+00 ] )
  OddW3 = np.array ( [ \
    0.3818300505051189449503698E+00, \
    0.2797053914892766679014680E+00, \
    0.1294849661688696932706118E+00 ] )
  OddW4 = np.array ( [ \
    0.3123470770400028400686304E+00, \
    0.2606106964029354623187428E+00, \
    0.1806481606948574040584721E+00, \
    0.8127438836157441197189206E-01 ] )
  OddW5 = np.array ( [ \
    0.2628045445102466621806890E+00, \
    0.2331937645919904799185238E+00, \
    0.1862902109277342514260979E+00, \
    0.1255803694649046246346947E+00, \
    0.5566856711617366648275374E-01 ] )
  OddW6 = np.array ( [ \
    0.2262831802628972384120902E+00, \
    0.2078160475368885023125234E+00, \
    0.1781459807619457382800468E+00, \
    0.1388735102197872384636019E+00, \
    0.9212149983772844791442126E-01, \
    0.4048400476531587952001996E-01 ] )
  OddW7 = np.array ( [ \
    0.1984314853271115764561182E+00, \
    0.1861610000155622110268006E+00, \
    0.1662692058169939335532006E+00, \
    0.1395706779261543144478051E+00, \
    0.1071592204671719350118693E+00, \
    0.7036604748810812470926662E-01, \
    0.3075324199611726835462762E-01 ] )
  OddW8 = np.array ( [ \
    0.1765627053669926463252710E+00, \
    0.1680041021564500445099705E+00, \
    0.1540457610768102880814317E+00, \
    0.1351363684685254732863199E+00, \
    0.1118838471934039710947887E+00, \
    0.8503614831717918088353538E-01, \
    0.5545952937398720112944102E-01, \
    0.2414830286854793196010920E-01 ] )
  OddW9 = np.array ( [ \
    0.1589688433939543476499565E+00, \
    0.1527660420658596667788553E+00, \
    0.1426067021736066117757460E+00, \
    0.1287539625393362276755159E+00, \
    0.1115666455473339947160242E+00, \
    0.9149002162244999946446222E-01, \
    0.6904454273764122658070790E-01, \
    0.4481422676569960033283728E-01, \
    0.1946178822972647703631351E-01 ] )
  OddW10 = np.array ( [ \
    0.1445244039899700590638271E+00, \
    0.1398873947910731547221335E+00, \
    0.1322689386333374617810526E+00, \
    0.1218314160537285341953671E+00, \
    0.1087972991671483776634747E+00, \
    0.9344442345603386155329010E-01, \
    0.7610011362837930201705132E-01, \
    0.5713442542685720828363528E-01, \
    0.3695378977085249379995034E-01, \
    0.1601722825777433332422273E-01 ] )
  OddW11 = np.array ( [ \
    0.1324620394046966173716425E+00, \
    0.1289057221880821499785954E+00, \
    0.1230490843067295304675784E+00, \
    0.1149966402224113649416434E+00, \
    0.1048920914645414100740861E+00, \
    0.9291576606003514747701876E-01, \
    0.7928141177671895492289248E-01, \
    0.6423242140852585212716980E-01, \
    0.4803767173108466857164124E-01, \
    0.3098800585697944431069484E-01, \
    0.1341185948714177208130864E-01 ] )
  OddW12 = np.array ( [ \
    0.1222424429903100416889594E+00, \
    0.1194557635357847722281782E+00, \
    0.1148582591457116483393255E+00, \
    0.1085196244742636531160939E+00, \
    0.1005359490670506442022068E+00, \
    0.9102826198296364981149704E-01, \
    0.8014070033500101801323524E-01, \
    0.6803833381235691720718712E-01, \
    0.5490469597583519192593686E-01, \
    0.4093915670130631265562402E-01, \
    0.2635498661503213726190216E-01, \
    0.1139379850102628794789998E-01 ] )
  OddW13 = np.array ( [ \
    0.1134763461089651486203700E+00, \
    0.1112524883568451926721632E+00, \
    0.1075782857885331872121629E+00, \
    0.1025016378177457986712478E+00, \
    0.9608872737002850756565252E-01, \
    0.8842315854375695019432262E-01, \
    0.7960486777305777126307488E-01, \
    0.6974882376624559298432254E-01, \
    0.5898353685983359911030058E-01, \
    0.4744941252061506270409646E-01, \
    0.3529705375741971102257772E-01, \
    0.2268623159618062319603554E-01, \
    0.9798996051294360261149438E-02 ] )
  OddW14 = np.array ( [ \
    0.1058761550973209414065914E+00, \
    0.1040733100777293739133284E+00, \
    0.1010912737599149661218204E+00, \
    0.9696383409440860630190016E-01, \
    0.9173775713925876334796636E-01, \
    0.8547225736617252754534480E-01, \
    0.7823832713576378382814484E-01, \
    0.7011793325505127856958160E-01, \
    0.6120309065707913854210970E-01, \
    0.5159482690249792391259412E-01, \
    0.4140206251868283610482948E-01, \
    0.3074049220209362264440778E-01, \
    0.1973208505612270598385931E-01, \
    0.8516903878746409654261436E-02 ] )
  OddW15 = np.array ( [ \
    0.9922501122667230787487546E-01, \
    0.9774333538632872509347402E-01, \
    0.9529024291231951280720412E-01, \
    0.9189011389364147821536290E-01, \
    0.8757674060847787612619794E-01, \
    0.8239299176158926390382334E-01, \
    0.7639038659877661642635764E-01, \
    0.6962858323541036616775632E-01, \
    0.6217478656102842691034334E-01, \
    0.5410308242491685371166596E-01, \
    0.4549370752720110290231576E-01, \
    0.3643227391238546402439264E-01, \
    0.2700901918497942180060860E-01, \
    0.1731862079031058246315918E-01, \
    0.7470831579248775858700554E-02 ] )
  OddW16 = np.array ( [ \
    0.9335642606559611616099912E-01, \
    0.9212398664331684621324104E-01, \
    0.9008195866063857723974370E-01, \
    0.8724828761884433760728158E-01, \
    0.8364787606703870761392808E-01, \
    0.7931236479488673836390848E-01, \
    0.7427985484395414934247216E-01, \
    0.6859457281865671280595482E-01, \
    0.6230648253031748003162750E-01, \
    0.5547084663166356128494468E-01, \
    0.4814774281871169567014706E-01, \
    0.4040154133166959156340938E-01, \
    0.3230035863232895328156104E-01, \
    0.2391554810174948035053310E-01, \
    0.1532170151293467612794584E-01, \
    0.6606227847587378058647800E-02 ] )
  OddW17 = np.array ( [ \
    0.8814053043027546297073886E-01, \
    0.8710444699718353424332214E-01, \
    0.8538665339209912522594402E-01, \
    0.8300059372885658837992644E-01, \
    0.7996494224232426293266204E-01, \
    0.7630345715544205353865872E-01, \
    0.7204479477256006466546180E-01, \
    0.6722228526908690396430546E-01, \
    0.6187367196608018888701398E-01, \
    0.5604081621237012857832772E-01, \
    0.4976937040135352980519956E-01, \
    0.4310842232617021878230592E-01, \
    0.3611011586346338053271748E-01, \
    0.2882926010889425404871630E-01, \
    0.2132297991148358088343844E-01, \
    0.1365082834836149226640441E-01, \
    0.5883433420443084975750336E-02 ] )
  OddW18 = np.array ( [ \
    0.8347457362586278725225302E-01, \
    0.8259527223643725089123018E-01, \
    0.8113662450846503050987774E-01, \
    0.7910886183752938076721222E-01, \
    0.7652620757052923788588804E-01, \
    0.7340677724848817272462668E-01, \
    0.6977245155570034488508154E-01, \
    0.6564872287275124948402376E-01, \
    0.6106451652322598613098804E-01, \
    0.5605198799827491780853916E-01, \
    0.5064629765482460160387558E-01, \
    0.4488536466243716665741054E-01, \
    0.3880960250193454448896226E-01, \
    0.3246163984752148106723444E-01, \
    0.2588603699055893352275954E-01, \
    0.1912904448908396604350259E-01, \
    0.1223878010030755652630649E-01, \
    0.5273057279497939351724544E-02 ] )
  OddW19 = np.array ( [ \
    0.7927622256836847101015574E-01, \
    0.7852361328737117672506330E-01, \
    0.7727455254468201672851160E-01, \
    0.7553693732283605770478448E-01, \
    0.7332175341426861738115402E-01, \
    0.7064300597060876077011486E-01, \
    0.6751763096623126536302120E-01, \
    0.6396538813868238898670650E-01, \
    0.6000873608859614957494160E-01, \
    0.5567269034091629990739094E-01, \
    0.5098466529212940521402098E-01, \
    0.4597430110891663188417682E-01, \
    0.4067327684793384393905618E-01, \
    0.3511511149813133076106530E-01, \
    0.2933495598390337859215654E-01, \
    0.2336938483217816459471240E-01, \
    0.1725622909372491904080491E-01, \
    0.1103478893916459424267603E-01, \
    0.4752944691635101370775866E-02 ] )
  OddW20 = np.array ( [ \
    0.7547874709271582402724706E-01, \
    0.7482962317622155189130518E-01, \
    0.7375188202722346993928094E-01, \
    0.7225169686102307339634646E-01, \
    0.7033766062081749748165896E-01, \
    0.6802073676087676673553342E-01, \
    0.6531419645352741043616384E-01, \
    0.6223354258096631647157330E-01, \
    0.5879642094987194499118590E-01, \
    0.5502251924257874188014710E-01, \
    0.5093345429461749478117008E-01, \
    0.4655264836901434206075674E-01, \
    0.4190519519590968942934048E-01, \
    0.3701771670350798843526154E-01, \
    0.3191821173169928178706676E-01, \
    0.2663589920711044546754900E-01, \
    0.2120106336877955307569710E-01, \
    0.1564493840781858853082666E-01, \
    0.9999938773905945338496546E-02, \
    0.4306140358164887684003630E-02 ] )
  OddW21 = np.array ( [ \
    0.7202750197142197434530754E-01, \
    0.7146373425251414129758106E-01, \
    0.7052738776508502812628636E-01, \
    0.6922334419365668428229950E-01, \
    0.6755840222936516919240796E-01, \
    0.6554124212632279749123378E-01, \
    0.6318238044939611232562970E-01, \
    0.6049411524999129451967862E-01, \
    0.5749046195691051942760910E-01, \
    0.5418708031888178686337342E-01, \
    0.5060119278439015652385048E-01, \
    0.4675149475434658001064704E-01, \
    0.4265805719798208376380686E-01, \
    0.3834222219413265757212856E-01, \
    0.3382649208686029234496834E-01, \
    0.2913441326149849491594084E-01, \
    0.2429045661383881590201850E-01, \
    0.1931990142368390039612543E-01, \
    0.1424875643157648610854214E-01, \
    0.9103996637401403318866628E-02, \
    0.3919490253844127282968528E-02 ] )
  OddW22 = np.array ( [ \
    0.6887731697766132288200278E-01, \
    0.6838457737866967453169206E-01, \
    0.6756595416360753627091012E-01, \
    0.6642534844984252808291474E-01, \
    0.6496819575072343085382664E-01, \
    0.6320144007381993774996374E-01, \
    0.6113350083106652250188634E-01, \
    0.5877423271884173857436156E-01, \
    0.5613487875978647664392382E-01, \
    0.5322801673126895194590376E-01, \
    0.5006749923795202979913194E-01, \
    0.4666838771837336526776814E-01, \
    0.4304688070916497115169120E-01, \
    0.3922023672930244756418756E-01, \
    0.3520669220160901624770010E-01, \
    0.3102537493451546716250854E-01, \
    0.2669621396757766480567536E-01, \
    0.2223984755057873239395080E-01, \
    0.1767753525793759061709347E-01, \
    0.1303110499158278432063191E-01, \
    0.8323189296218241645734836E-02, \
    0.3582663155283558931145652E-02 ] )
  OddW23 = np.array ( [ \
    0.6599053358881047453357062E-01, \
    0.6555737776654974025114294E-01, \
    0.6483755623894572670260402E-01, \
    0.6383421660571703063129384E-01, \
    0.6255174622092166264056434E-01, \
    0.6099575300873964533071060E-01, \
    0.5917304094233887597615438E-01, \
    0.5709158029323154022201646E-01, \
    0.5476047278153022595712512E-01, \
    0.5218991178005714487221170E-01, \
    0.4939113774736116960457022E-01, \
    0.4637638908650591120440168E-01, \
    0.4315884864847953826830162E-01, \
    0.3975258612253100378090162E-01, \
    0.3617249658417495161345948E-01, \
    0.3243423551518475676761786E-01, \
    0.2855415070064338650473990E-01, \
    0.2454921165965881853783378E-01, \
    0.2043693814766842764203432E-01, \
    0.1623533314643305967072624E-01, \
    0.1196284846431232096394232E-01, \
    0.7638616295848833614105174E-02, \
    0.3287453842528014883248206E-02 ] )
  OddW24 = np.array ( [ \
    0.6333550929649174859083696E-01, \
    0.6295270746519569947439960E-01, \
    0.6231641732005726740107682E-01, \
    0.6142920097919293629682652E-01, \
    0.6029463095315201730310616E-01, \
    0.5891727576002726602452756E-01, \
    0.5730268153018747548516450E-01, \
    0.5545734967480358869043158E-01, \
    0.5338871070825896852794302E-01, \
    0.5110509433014459067462262E-01, \
    0.4861569588782824027765094E-01, \
    0.4593053935559585354249958E-01, \
    0.4306043698125959798834538E-01, \
    0.4001694576637302136860494E-01, \
    0.3681232096300068981946734E-01, \
    0.3345946679162217434248744E-01, \
    0.2997188462058382535069014E-01, \
    0.2636361892706601696094518E-01, \
    0.2264920158744667649877160E-01, \
    0.1884359585308945844445106E-01, \
    0.1496214493562465102958377E-01, \
    0.1102055103159358049750846E-01, \
    0.7035099590086451473452956E-02, \
    0.3027278988922905077484090E-02 ] )
  OddW25 = np.array ( [ \
    0.6088546484485634388119860E-01, \
    0.6054550693473779513812526E-01, \
    0.5998031577750325209006396E-01, \
    0.5919199392296154378353896E-01, \
    0.5818347398259214059843780E-01, \
    0.5695850772025866210007778E-01, \
    0.5552165209573869301673704E-01, \
    0.5387825231304556143409938E-01, \
    0.5203442193669708756413650E-01, \
    0.4999702015005740977954886E-01, \
    0.4777362624062310199999514E-01, \
    0.4537251140765006874816670E-01, \
    0.4280260799788008665360980E-01, \
    0.4007347628549645318680892E-01, \
    0.3719526892326029284290846E-01, \
    0.3417869320418833623620910E-01, \
    0.3103497129016000845442504E-01, \
    0.2777579859416247719599602E-01, \
    0.2441330057378143427314164E-01, \
    0.2095998840170321057979252E-01, \
    0.1742871472340105225950284E-01, \
    0.1383263400647782229668883E-01, \
    0.1018519129782172993923731E-01, \
    0.6500337783252600292109494E-02, \
    0.2796807171089895575547228E-02 ] )
  OddW26 = np.array ( [ \
    0.5861758623272026331807196E-01, \
    0.5831431136225600755627570E-01, \
    0.5781001499171319631968304E-01, \
    0.5710643553626719177338328E-01, \
    0.5620599838173970980865512E-01, \
    0.5511180752393359900234954E-01, \
    0.5382763486873102904208140E-01, \
    0.5235790722987271819970160E-01, \
    0.5070769106929271529648556E-01, \
    0.4888267503269914042044844E-01, \
    0.4688915034075031402187278E-01, \
    0.4473398910367281021276570E-01, \
    0.4242462063452001359228150E-01, \
    0.3996900584354038212709364E-01, \
    0.3737560980348291567417214E-01, \
    0.3465337258353423795838740E-01, \
    0.3181167845901932306323576E-01, \
    0.2886032361782373626279970E-01, \
    0.2580948251075751771396152E-01, \
    0.2266967305707020839878928E-01, \
    0.1945172110763689538804750E-01, \
    0.1616672525668746392806095E-01, \
    0.1282602614424037917915135E-01, \
    0.9441202284940344386662890E-02, \
    0.6024276226948673281242120E-02, \
    0.2591683720567031811603734E-02 ] )
  OddW27 = np.array ( [ \
    0.5651231824977200140065834E-01, \
    0.5624063407108436802827906E-01, \
    0.5578879419528408710293598E-01, \
    0.5515824600250868759665114E-01, \
    0.5435100932991110207032224E-01, \
    0.5336967000160547272357054E-01, \
    0.5221737154563208456439348E-01, \
    0.5089780512449397922477522E-01, \
    0.4941519771155173948075862E-01, \
    0.4777429855120069555003682E-01, \
    0.4598036394628383810390480E-01, \
    0.4403914042160658989516800E-01, \
    0.4195684631771876239520718E-01, \
    0.3974015187433717960946388E-01, \
    0.3739615786796554528291572E-01, \
    0.3493237287358988740726862E-01, \
    0.3235668922618583168470572E-01, \
    0.2967735776516104122129630E-01, \
    0.2690296145639627066711996E-01, \
    0.2404238800972562200779126E-01, \
    0.2110480166801645412020978E-01, \
    0.1809961452072906240796732E-01, \
    0.1503645833351178821315019E-01, \
    0.1192516071984861217075236E-01, \
    0.8775746107058528177390204E-02, \
    0.5598632266560767354082364E-02, \
    0.2408323619979788819164582E-02 ] )
  OddW28 = np.array ( [ \
    0.5455280360476188648013898E-01, \
    0.5430847145249864313874678E-01, \
    0.5390206148329857464280950E-01, \
    0.5333478658481915842657698E-01, \
    0.5260833972917743244023134E-01, \
    0.5172488892051782472062386E-01, \
    0.5068707072492740865664050E-01, \
    0.4949798240201967899383808E-01, \
    0.4816117266168775126885110E-01, \
    0.4668063107364150378384082E-01, \
    0.4506077616138115779721374E-01, \
    0.4330644221621519659643210E-01, \
    0.4142286487080111036319668E-01, \
    0.3941566547548011408995280E-01, \
    0.3729083432441731735473546E-01, \
    0.3505471278231261750575064E-01, \
    0.3271397436637156854248994E-01, \
    0.3027560484269399945849064E-01, \
    0.2774688140218019232125814E-01, \
    0.2513535099091812264727322E-01, \
    0.2244880789077643807968978E-01, \
    0.1969527069948852038242318E-01, \
    0.1688295902344154903500062E-01, \
    0.1402027079075355617024753E-01, \
    0.1111576373233599014567619E-01, \
    0.8178160067821232626211086E-02, \
    0.5216533474718779390504886E-02, \
    0.2243753872250662909727492E-02 ] )
  OddW29 = np.array ( [ \
    0.5272443385912793196130422E-01, \
    0.5250390264782873905094128E-01, \
    0.5213703364837539138398724E-01, \
    0.5162484939089148214644000E-01, \
    0.5096877742539391685024800E-01, \
    0.5017064634299690281072034E-01, \
    0.4923268067936198577969374E-01, \
    0.4815749471460644038814684E-01, \
    0.4694808518696201919315986E-01, \
    0.4560782294050976983186828E-01, \
    0.4414044353029738069079808E-01, \
    0.4255003681106763866730838E-01, \
    0.4084103553868670766020196E-01, \
    0.3901820301616000950303072E-01, \
    0.3708661981887092269183778E-01, \
    0.3505166963640010878371850E-01, \
    0.3291902427104527775751116E-01, \
    0.3069462783611168323975056E-01, \
    0.2838468020053479790515332E-01, \
    0.2599561973129850018665014E-01, \
    0.2353410539371336342527500E-01, \
    0.2100699828843718735046168E-01, \
    0.1842134275361002936061624E-01, \
    0.1578434731308146614732024E-01, \
    0.1310336630634519101831859E-01, \
    0.1038588550099586219379846E-01, \
    0.7639529453487575142699186E-02, \
    0.4872239168265284768580414E-02, \
    0.2095492284541223402697724E-02 ] )
  OddW30 = np.array ( [ \
    0.5101448703869726354373512E-01, \
    0.5081476366881834320770052E-01, \
    0.5048247038679740464814450E-01, \
    0.5001847410817825342505160E-01, \
    0.4942398534673558993996884E-01, \
    0.4870055505641152608753004E-01, \
    0.4785007058509560716183348E-01, \
    0.4687475075080906597642932E-01, \
    0.4577714005314595937133982E-01, \
    0.4456010203508348827154136E-01, \
    0.4322681181249609790104358E-01, \
    0.4178074779088849206667564E-01, \
    0.4022568259099824736764020E-01, \
    0.3856567320700817274615216E-01, \
    0.3680505042315481738432126E-01, \
    0.3494840751653335109085198E-01, \
    0.3300058827590741063272390E-01, \
    0.3096667436839739482469792E-01, \
    0.2885197208818340150434184E-01, \
    0.2666199852415088966281066E-01, \
    0.2440246718754420291534050E-01, \
    0.2207927314831904400247522E-01, \
    0.1969847774610118133051782E-01, \
    0.1726629298761374359443389E-01, \
    0.1478906588493791454617878E-01, \
    0.1227326350781210462927897E-01, \
    0.9725461830356133736135366E-02, \
    0.7152354991749089585834616E-02, \
    0.4560924006012417184541648E-02, \
    0.1961453361670282671779431E-02 ] )
  OddW31 = np.array ( [ \
    0.4941183303991817896703964E-01, \
    0.4923038042374756078504314E-01, \
    0.4892845282051198994470936E-01, \
    0.4850678909788384786409014E-01, \
    0.4796642113799513141105276E-01, \
    0.4730867131226891908060508E-01, \
    0.4653514924538369651039536E-01, \
    0.4564774787629260868588592E-01, \
    0.4464863882594139537033256E-01, \
    0.4354026708302759079896428E-01, \
    0.4232534502081582298250554E-01, \
    0.4100684575966639863511004E-01, \
    0.3958799589154409398480778E-01, \
    0.3807226758434955676363856E-01, \
    0.3646337008545728963045232E-01, \
    0.3476524064535587769718026E-01, \
    0.3298203488377934176568344E-01, \
    0.3111811662221981750821608E-01, \
    0.2917804720828052694555162E-01, \
    0.2716657435909793322519012E-01, \
    0.2508862055334498661862972E-01, \
    0.2294927100488993314894282E-01, \
    0.2075376125803909077534152E-01, \
    0.1850746446016127040926083E-01, \
    0.1621587841033833888228333E-01, \
    0.1388461261611561082486681E-01, \
    0.1151937607688004175075116E-01, \
    0.9125968676326656354058462E-02, \
    0.6710291765960136251908410E-02, \
    0.4278508346863761866081200E-02, \
    0.1839874595577084117085868E-02 ] )
  OddW32 = np.array ( [ \
    0.4790669250049586203134730E-01, \
    0.4774134868124062155903898E-01, \
    0.4746619823288550315264446E-01, \
    0.4708187401045452224600686E-01, \
    0.4658925997223349830225508E-01, \
    0.4598948914665169696389334E-01, \
    0.4528394102630023065712822E-01, \
    0.4447423839508297442732352E-01, \
    0.4356224359580048653228480E-01, \
    0.4255005424675580271921714E-01, \
    0.4143999841724029302268646E-01, \
    0.4023462927300553381544642E-01, \
    0.3893671920405119761667398E-01, \
    0.3754925344825770980977246E-01, \
    0.3607542322556527393216642E-01, \
    0.3451861839854905862522142E-01, \
    0.3288241967636857498404946E-01, \
    0.3117059038018914246443218E-01, \
    0.2938706778931066806264472E-01, \
    0.2753595408845034394249940E-01, \
    0.2562150693803775821408458E-01, \
    0.2364812969128723669878144E-01, \
    0.2162036128493406284165378E-01, \
    0.1954286583675006282683714E-01, \
    0.1742042199767024849536596E-01, \
    0.1525791214644831034926464E-01, \
    0.1306031163999484633616732E-01, \
    0.1083267878959796862151440E-01, \
    0.8580148266881459893636434E-02, \
    0.6307942578971754550189764E-02, \
    0.4021524172003736347075858E-02, \
    0.1729258251300250898337759E-02 ] )
  OddW33 = np.array ( [ \
    0.4649043816026462820831466E-01, \
    0.4633935168241562110844706E-01, \
    0.4608790448976157619721740E-01, \
    0.4573664116106369093689412E-01, \
    0.4528632245466953156805004E-01, \
    0.4473792366088982547214182E-01, \
    0.4409263248975101830783160E-01, \
    0.4335184649869951735915584E-01, \
    0.4251717006583049147154770E-01, \
    0.4159041091519924309854838E-01, \
    0.4057357620174452522725164E-01, \
    0.3946886816430888264288692E-01, \
    0.3827867935617948064763712E-01, \
    0.3700558746349258202313488E-01, \
    0.3565234972274500666133270E-01, \
    0.3422189694953664673983902E-01, \
    0.3271732719153120542712204E-01, \
    0.3114189901947282393742616E-01, \
    0.2949902447094566969584718E-01, \
    0.2779226166243676998720012E-01, \
    0.2602530708621323880370460E-01, \
    0.2420198760967316472069180E-01, \
    0.2232625219645207692279754E-01, \
    0.2040216337134354044925720E-01, \
    0.1843388845680457387216616E-01, \
    0.1642569062253087920472674E-01, \
    0.1438191982720055093097663E-01, \
    0.1230700384928815052195302E-01, \
    0.1020544003410244098666155E-01, \
    0.8081790299023136215346300E-02, \
    0.5940693177582235216514606E-02, \
    0.3787008301825508445960626E-02, \
    0.1628325035240012866460003E-02 ] )
  OddW34 = np.array ( [ \
    0.4515543023614546051651704E-01, \
    0.4501700814039980219871620E-01, \
    0.4478661887831255754213528E-01, \
    0.4446473312204713809623108E-01, \
    0.4405200846590928438098588E-01, \
    0.4354928808292674103357578E-01, \
    0.4295759900230521387841984E-01, \
    0.4227815001128051285158270E-01, \
    0.4151232918565450208287406E-01, \
    0.4066170105406160053752604E-01, \
    0.3972800340176164120645862E-01, \
    0.3871314372049251393273936E-01, \
    0.3761919531164090650815840E-01, \
    0.3644839305070051405664348E-01, \
    0.3520312882168348614775456E-01, \
    0.3388594663083228949780964E-01, \
    0.3249953740964611124473418E-01, \
    0.3104673351789053903268552E-01, \
    0.2953050295790671177981110E-01, \
    0.2795394331218770599086132E-01, \
    0.2632027541686948379176090E-01, \
    0.2463283678454245536433616E-01, \
    0.2289507479074078565552120E-01, \
    0.2111053963987189462789068E-01, \
    0.1928287712884940278924393E-01, \
    0.1741582123196982913207401E-01, \
    0.1551318654340616473976910E-01, \
    0.1357886064907567099981112E-01, \
    0.1161679661067196554873961E-01, \
    0.9631006150415575588660562E-02, \
    0.7625555931201510611459992E-02, \
    0.5604579927870594828535346E-02, \
    0.3572416739397372609702552E-02, \
    0.1535976952792084075135094E-02 ] )
  OddW35 = np.array ( [ \
    0.4389487921178858632125256E-01, \
    0.4376774491340214497230982E-01, \
    0.4355612710410853337113396E-01, \
    0.4326043426324126659885626E-01, \
    0.4288123715758043502060704E-01, \
    0.4241926773962459303533940E-01, \
    0.4187541773473300618954268E-01, \
    0.4125073691986602424910896E-01, \
    0.4054643109724689643492514E-01, \
    0.3976385976685758167433708E-01, \
    0.3890453350226294749240264E-01, \
    0.3797011103483115621441804E-01, \
    0.3696239605198203185608278E-01, \
    0.3588333371564891077796844E-01, \
    0.3473500690768218837536532E-01, \
    0.3351963220945403083440624E-01, \
    0.3223955562344352694190700E-01, \
    0.3089724804509072169860608E-01, \
    0.2949530049370881246493644E-01, \
    0.2803641911174149061798030E-01, \
    0.2652341994215790800810512E-01, \
    0.2495922349431387305527612E-01, \
    0.2334684910922325263171504E-01, \
    0.2168940913598536796183230E-01, \
    0.1999010293235011128748561E-01, \
    0.1825221070467867050232934E-01, \
    0.1647908720746239655059230E-01, \
    0.1467415533461152920040808E-01, \
    0.1284089966808780607041846E-01, \
    0.1098286015429855170627475E-01, \
    0.9103626461992005851317578E-02, \
    0.7206835281831493387342912E-02, \
    0.5296182844025892632677844E-02, \
    0.3375555496730675865126842E-02, \
    0.1451267330029397268489446E-02 ] )
  OddW36 = np.array ( [ \
    0.4270273086485722207660098E-01, \
    0.4258568982601838702576300E-01, \
    0.4239085899223159440537396E-01, \
    0.4211859425425563626894556E-01, \
    0.4176939294869285375410172E-01, \
    0.4134389294952549452688336E-01, \
    0.4084287150293886154936056E-01, \
    0.4026724380756003336494178E-01, \
    0.3961806134270614331650800E-01, \
    0.3889650994769673952047552E-01, \
    0.3810390765573980059550798E-01, \
    0.3724170228634977315689404E-01, \
    0.3631146880069778469034650E-01, \
    0.3531490642472828750906318E-01, \
    0.3425383554530221541412972E-01, \
    0.3313019438504384067706900E-01, \
    0.3194603546197670648650132E-01, \
    0.3070352184043350493812614E-01, \
    0.2940492318011656010545704E-01, \
    0.2805261159057206032380240E-01, \
    0.2664905729872748295223048E-01, \
    0.2519682413753831281333190E-01, \
    0.2369856486421897462660896E-01, \
    0.2215701631704007205676952E-01, \
    0.2057499442036116916601972E-01, \
    0.1895538904867002168973610E-01, \
    0.1730115876248908300560664E-01, \
    0.1561532543359142299553300E-01, \
    0.1390096878831465086752053E-01, \
    0.1216122092928111272776412E-01, \
    0.1039926099500053220130511E-01, \
    0.8618310479532247613912182E-02, \
    0.6821631349174792362208078E-02, \
    0.5012538571606190263812266E-02, \
    0.3194524377289034522078870E-02, \
    0.1373376462759619223985654E-02 ] )
  OddW37 = np.array ( [ \
    0.4157356944178127878299940E-01, \
    0.4146558103261909213524834E-01, \
    0.4128580808246718908346088E-01, \
    0.4103456181139210667622250E-01, \
    0.4071227717293733029875788E-01, \
    0.4031951210114157755817430E-01, \
    0.3985694654465635257596536E-01, \
    0.3932538128963516252076754E-01, \
    0.3872573657343257584146640E-01, \
    0.3805905049151360313563098E-01, \
    0.3732647720033209016730652E-01, \
    0.3652928491929033900685118E-01, \
    0.3566885373524045308911856E-01, \
    0.3474667321333040653509838E-01, \
    0.3376433981833409264695562E-01, \
    0.3272355415093422052152286E-01, \
    0.3162611800374964805603220E-01, \
    0.3047393124221453920313760E-01, \
    0.2926898851572598680503318E-01, \
    0.2801337580478054082525924E-01, \
    0.2670926681012085177235442E-01, \
    0.2535891919021637909420806E-01, \
    0.2396467065371695917476570E-01, \
    0.2252893491386577645054636E-01, \
    0.2105419751228284223644546E-01, \
    0.1954301152012788937957076E-01, \
    0.1799799312564505063794604E-01, \
    0.1642181711902464004359937E-01, \
    0.1481721228981446852013731E-01, \
    0.1318695676282480211961300E-01, \
    0.1153387332830449596681366E-01, \
    0.9860824916114018392051822E-02, \
    0.8170710707327826403717118E-02, \
    0.6466464907037538401963982E-02, \
    0.4751069185015273965898868E-02, \
    0.3027671014606041291230134E-02, \
    0.1301591717375855993899257E-02 ] )
  OddW38 = np.array ( [ \
    0.4050253572678803195524960E-01, \
    0.4040269003221775617032620E-01, \
    0.4023646282485108419526524E-01, \
    0.4000412721559123741035150E-01, \
    0.3970606493128931068103760E-01, \
    0.3934276568757015193713232E-01, \
    0.3891482638423378562103292E-01, \
    0.3842295012455452367368120E-01, \
    0.3786794506008932026166678E-01, \
    0.3725072306289371887876038E-01, \
    0.3657229822732745453345840E-01, \
    0.3583378520391196260264276E-01, \
    0.3503639736797827845487748E-01, \
    0.3418144482611567926531782E-01, \
    0.3327033226369854530283962E-01, \
    0.3230455663703097559357210E-01, \
    0.3128570471390543339395640E-01, \
    0.3021545046662299869139892E-01, \
    0.2909555232176876134870268E-01, \
    0.2792785027127696854150716E-01, \
    0.2671426284955789083200264E-01, \
    0.2545678398169440375263742E-01, \
    0.2415747970795584494059388E-01, \
    0.2281848479012952051290956E-01, \
    0.2144199920545613550512462E-01, \
    0.2003028453431617639624646E-01, \
    0.1858566024834148550917969E-01, \
    0.1711049990653110417623953E-01, \
    0.1560722726874913129508073E-01, \
    0.1407831234002700405016720E-01, \
    0.1252626736922736518735940E-01, \
    0.1095364285391135423859170E-01, \
    0.9363023692386430769260798E-02, \
    0.7757025950083070731841176E-02, \
    0.6138296159756341839268696E-02, \
    0.4509523600205835333238688E-02, \
    0.2873553083652691657275240E-02, \
    0.1235291177139409614163874E-02 ] )
  OddW39 = np.array ( [ \
    0.3948525740129116475372166E-01, \
    0.3939275600474300393426418E-01, \
    0.3923874749659464355491890E-01, \
    0.3902347234287979602650502E-01, \
    0.3874726667023996706818530E-01, \
    0.3841056174110417740541666E-01, \
    0.3801388328032604954551756E-01, \
    0.3755785065432977047790708E-01, \
    0.3704317590404678415983790E-01, \
    0.3647066263315342752925638E-01, \
    0.3584120475334575228920704E-01, \
    0.3515578508861113112825058E-01, \
    0.3441547384067660088259166E-01, \
    0.3362142691803093004992252E-01, \
    0.3277488413113081785342150E-01, \
    0.3187716725661117036051890E-01, \
    0.3092967797352483528829388E-01, \
    0.2993389567483836289564858E-01, \
    0.2889137515760726678163634E-01, \
    0.2780374419544705894443552E-01, \
    0.2667270099710555653788310E-01, \
    0.2550001155512877394733978E-01, \
    0.2428750688879949263942200E-01, \
    0.2303708018571902627697914E-01, \
    0.2175068384660807976864198E-01, \
    0.2043032643814085987844290E-01, \
    0.1907806955893748858478357E-01, \
    0.1769602462431041786466318E-01, \
    0.1628634957619168209183741E-01, \
    0.1485124552635006931857919E-01, \
    0.1339295334482567619730830E-01, \
    0.1191375021511699869960077E-01, \
    0.1041594620451338257918368E-01, \
    0.8901880982652486253740074E-02, \
    0.7373921131330176830391914E-02, \
    0.5834459868763465589211910E-02, \
    0.4285929113126531218219446E-02, \
    0.2730907065754855918535274E-02, \
    0.1173930129956613021207112E-02 ] )
  OddW40 = np.array ( [ \
    0.3851778959688469523783810E-01, \
    0.3843192958037517210025656E-01, \
    0.3828897129558352443032002E-01, \
    0.3808912713547560183102332E-01, \
    0.3783269400830055924757518E-01, \
    0.3752005289647583785923924E-01, \
    0.3715166829056371214474266E-01, \
    0.3672808749918043951690600E-01, \
    0.3624993983586341279832570E-01, \
    0.3571793568410456853072614E-01, \
    0.3513286544193937941597898E-01, \
    0.3449559834765979589474544E-01, \
    0.3380708118839624555119598E-01, \
    0.3306833689348800442087536E-01, \
    0.3228046301473268887240310E-01, \
    0.3144463009577406641803652E-01, \
    0.3056207993305266189565968E-01, \
    0.2963412373090559765847516E-01, \
    0.2866214015356067622579182E-01, \
    0.2764757327692492691108618E-01, \
    0.2659193044321992109092004E-01, \
    0.2549678002166567706947970E-01, \
    0.2436374907856309733249090E-01, \
    0.2319452096027391988145570E-01, \
    0.2199083279275163277050144E-01, \
    0.2075447290144560853952252E-01, \
    0.1948727815560191821592671E-01, \
    0.1819113124125576115176324E-01, \
    0.1686795786763513947433495E-01, \
    0.1551972391246436293824549E-01, \
    0.1414843251323606554825229E-01, \
    0.1275612111513442100025550E-01, \
    0.1134485849541625576200880E-01, \
    0.9916741809595875499750926E-02, \
    0.8473893785345565449616918E-02, \
    0.7018460484931625511609624E-02, \
    0.5552611370256278902273182E-02, \
    0.4078551113421395586018386E-02, \
    0.2598622299928953013499446E-02, \
    0.1117029847124606606122469E-02 ] )
  OddW41 = np.array ( [ \
    0.3759656394395517759196934E-01, \
    0.3751672450373727271505762E-01, \
    0.3738378433575740441091762E-01, \
    0.3719793160197673054400130E-01, \
    0.3695942935618497107975802E-01, \
    0.3666861517167809004390068E-01, \
    0.3632590066346228889989584E-01, \
    0.3593177090566064734733082E-01, \
    0.3548678374494710264584324E-01, \
    0.3499156901097965473152462E-01, \
    0.3444682762495051683252180E-01, \
    0.3385333060751519869931002E-01, \
    0.3321191798750501518117324E-01, \
    0.3252349761296806599129116E-01, \
    0.3178904386622215064354856E-01, \
    0.3100959628473919484306724E-01, \
    0.3018625808981441705410184E-01, \
    0.2932019462510452791804122E-01, \
    0.2841263170724764156375054E-01, \
    0.2746485389090326123892810E-01, \
    0.2647820265067376248510830E-01, \
    0.2545407448248949675081806E-01, \
    0.2439391892715855749743432E-01, \
    0.2329923651890054937016126E-01, \
    0.2217157666180362262199056E-01, \
    0.2101253543726991787400918E-01, \
    0.1982375334565493904931242E-01, \
    0.1860691298547847284166721E-01, \
    0.1736373667382462235016547E-01, \
    0.1609598401193537091543832E-01, \
    0.1480544940071787768084914E-01, \
    0.1349395951237523498069998E-01, \
    0.1216337072779861206303406E-01, \
    0.1081556655803715872036043E-01, \
    0.9452455092479699888244178E-02, \
    0.8075966593123452283593892E-02, \
    0.6688051635243685741358420E-02, \
    0.5290681445859865555240374E-02, \
    0.3885859435353202192003776E-02, \
    0.2475719322545939743331242E-02, \
    0.1064168219666567756385077E-02 ] )
  OddW42 = np.array ( [ \
    0.3671834473341961622215226E-01, \
    0.3664397593378570248640692E-01, \
    0.3652013948874488485747660E-01, \
    0.3634700257169520376675674E-01, \
    0.3612479890936246037475190E-01, \
    0.3585382846628081255691520E-01, \
    0.3553445703985569908199156E-01, \
    0.3516711576655578824981280E-01, \
    0.3475230053990063752924744E-01, \
    0.3429057134102984670822224E-01, \
    0.3378255148275753033131186E-01, \
    0.3322892676813276976252854E-01, \
    0.3263044456464217818903764E-01, \
    0.3198791279530467445976990E-01, \
    0.3130219884802087044839684E-01, \
    0.3057422840464999572392432E-01, \
    0.2980498419139588737561256E-01, \
    0.2899550465219015208986610E-01, \
    0.2814688254686507584638292E-01, \
    0.2726026347601116478577010E-01, \
    0.2633684433451435982173160E-01, \
    0.2537787169586608847736972E-01, \
    0.2438464012943568314241580E-01, \
    0.2335849045298989189769872E-01, \
    0.2230080792283937418945736E-01, \
    0.2121302036408937967241628E-01, \
    0.2009659624357542174179408E-01, \
    0.1895304268818284044680496E-01, \
    0.1778390345139817090774314E-01, \
    0.1659075683115467007520452E-01, \
    0.1537521354238962687440865E-01, \
    0.1413891454840083293055609E-01, \
    0.1288352885649808429050626E-01, \
    0.1161075128670389800962475E-01, \
    0.1032230023052424589381722E-01, \
    0.9019915439993631278967098E-02, \
    0.7705355960382757079897960E-02, \
    0.6380398587897515098686098E-02, \
    0.5046838426924442725450432E-02, \
    0.3706500125759316706868292E-02, \
    0.2361331704285020896763904E-02, \
    0.1014971908967743695374167E-02 ] )
  OddW43 = np.array ( [ \
    0.3588019106018701587773518E-01, \
    0.3581080434383374175662560E-01, \
    0.3569525919440943377647946E-01, \
    0.3553370454416059391133478E-01, \
    0.3532634862941021369843054E-01, \
    0.3507345872215153655662536E-01, \
    0.3477536078554782924871120E-01, \
    0.3443243905378224376593820E-01, \
    0.3404513553679937345518354E-01, \
    0.3361394945057693558422230E-01, \
    0.3313943657366202353628890E-01, \
    0.3262220853080144392580048E-01, \
    0.3206293200458966777765818E-01, \
    0.3146232787615076393796228E-01, \
    0.3082117029596223415371898E-01, \
    0.3014028568601882474395096E-01, \
    0.2942055167462304824922484E-01, \
    0.2866289596517621838858744E-01, \
    0.2786829514042920598963448E-01, \
    0.2703777340373580728397710E-01, \
    0.2617240125893355894972542E-01, \
    0.2527329413055707316411874E-01, \
    0.2434161092616763233921348E-01, \
    0.2337855254266017225782364E-01, \
    0.2238536031848547821419758E-01, \
    0.2136331443380253159361604E-01, \
    0.2031373226065556952656956E-01, \
    0.1923796666535655878505047E-01, \
    0.1813740426535425205021816E-01, \
    0.1701346364300153443364516E-01, \
    0.1586759351882631900292224E-01, \
    0.1470127088723984222989451E-01, \
    0.1351599911824565808188095E-01, \
    0.1231330603004803654228712E-01, \
    0.1109474194056071927972064E-01, \
    0.9861877713701826716584494E-02, \
    0.8616302838488951832949878E-02, \
    0.7359623648818063660769462E-02, \
    0.6093462047634872130101964E-02, \
    0.4819456238501885899307624E-02, \
    0.3539271655388628540179688E-02, \
    0.2254690753752853092482060E-02, \
    0.9691097381770753376096654E-03 ] )
  OddW44 = np.array ( [ \
    0.3507942401790202531716760E-01, \
    0.3501458416619644336915306E-01, \
    0.3490660650856070989101148E-01, \
    0.3475562407298142092081152E-01, \
    0.3456182286913780813643384E-01, \
    0.3432544165923908781796544E-01, \
    0.3404677166387108716735582E-01, \
    0.3372615620321457070630952E-01, \
    0.3336399027407732093971928E-01, \
    0.3296072006326111707429234E-01, \
    0.3251684239786320696758578E-01, \
    0.3203290413318958550703170E-01, \
    0.3150950147903428365879858E-01, \
    0.3094727926515484478947892E-01, \
    0.3034693014684912934340756E-01, \
    0.2970919375161245962730194E-01, \
    0.2903485576792681183001942E-01, \
    0.2832474697730520722803496E-01, \
    0.2757974223078458253347716E-01, \
    0.2680075937112917771256550E-01, \
    0.2598875810207383625148160E-01, \
    0.2514473880600256862281534E-01, \
    0.2426974131152233927366188E-01, \
    0.2336484361245544582716880E-01, \
    0.2243116053983636712835892E-01, \
    0.2146984238856114084341254E-01, \
    0.2048207350040027021224486E-01, \
    0.1946907080515187313867415E-01, \
    0.1843208232178411567584622E-01, \
    0.1737238562150240166964102E-01, \
    0.1629128625479238457754130E-01, \
    0.1519011614466612339747308E-01, \
    0.1407023194864448281388687E-01, \
    0.1293301339260267729158710E-01, \
    0.1177986158087489217661933E-01, \
    0.1061219728997218803268093E-01, \
    0.9431459260797890539711922E-02, \
    0.8239102525389078730572362E-02, \
    0.7036596870989114137389446E-02, \
    0.5825425788770107459644064E-02, \
    0.4607087343463241433054622E-02, \
    0.3383104792407455132632698E-02, \
    0.2155112582219113764637582E-02, \
    0.9262871051934728155239026E-03 ] )
  OddW45 = np.array ( [ \
    0.3431359817623139857242020E-01, \
    0.3425291647165106006719224E-01, \
    0.3415185977541012618567448E-01, \
    0.3401054720622907866548866E-01, \
    0.3382914533369793579365620E-01, \
    0.3360786798193575310982430E-01, \
    0.3334697597754983863697838E-01, \
    0.3304677684219179120016898E-01, \
    0.3270762443007278294842040E-01, \
    0.3232991851086539448409380E-01, \
    0.3191410429848369728859888E-01, \
    0.3146067192629708854519032E-01, \
    0.3097015586939654421561894E-01, \
    0.3044313431459439490344712E-01, \
    0.2988022847890037493277136E-01, \
    0.2928210187727747971826382E-01, \
    0.2864945954054102439649608E-01, \
    0.2798304718432316638118606E-01, \
    0.2728365033008298027898986E-01, \
    0.2655209337919890810307922E-01, \
    0.2578923864123601618879028E-01, \
    0.2499598531753495743256148E-01, \
    0.2417326844132287942221788E-01, \
    0.2332205777559880283599600E-01, \
    0.2244335667009737337332098E-01, \
    0.2153820087868566629622426E-01, \
    0.2060765733859846074045938E-01, \
    0.1965282291296914660474199E-01, \
    0.1867482309816812542178599E-01, \
    0.1767481069752190506037194E-01, \
    0.1665396446306124017225753E-01, \
    0.1561348770705005975095101E-01, \
    0.1455460688520869608484063E-01, \
    0.1347857015383097919431856E-01, \
    0.1238664590355674305453526E-01, \
    0.1128012127376968298340906E-01, \
    0.1016030065441547672889225E-01, \
    0.9028504189234487748913298E-02, \
    0.7886066314628901599629988E-02, \
    0.6734334432268884665261132E-02, \
    0.5574668047479788997832340E-02, \
    0.4408439747302676819065170E-02, \
    0.3237045507972104977098260E-02, \
    0.2061987122032229660677942E-02, \
    0.8862412406694141765769646E-03 ] )
  OddW46 = np.array ( [ \
    0.3358047670273290820423322E-01, \
    0.3352360509236689973246714E-01, \
    0.3342889041048296629425518E-01, \
    0.3329643957561578934524218E-01, \
    0.3312640210470322597293962E-01, \
    0.3291896994430459113247722E-01, \
    0.3267437725392241575486392E-01, \
    0.3239290014167229270630344E-01, \
    0.3207485635259921958171598E-01, \
    0.3172060490999230883258760E-01, \
    0.3133054571010280192591498E-01, \
    0.3090511907072293590876800E-01, \
    0.3044480523413530949647580E-01, \
    0.2995012382499392416587776E-01, \
    0.2942163326374897748551588E-01, \
    0.2885993013627770636290672E-01, \
    0.2826564852043306435742870E-01, \
    0.2763945927027071971311622E-01, \
    0.2698206925876273304878794E-01, \
    0.2629422057985327475229788E-01, \
    0.2557668971075783892217594E-01, \
    0.2483028663545258189183534E-01, \
    0.2405585393034465615306556E-01, \
    0.2325426581315775168991978E-01, \
    0.2242642715610957188910656E-01, \
    0.2157327246449981801505782E-01, \
    0.2069576482186873448858912E-01, \
    0.1979489480292792866805571E-01, \
    0.1887167935550803461442971E-01, \
    0.1792716065281371317885285E-01, \
    0.1696240491732901090122756E-01, \
    0.1597850121778211678831695E-01, \
    0.1497656024067188095391932E-01, \
    0.1395771303800797072406999E-01, \
    0.1292310975318535045602668E-01, \
    0.1187391832744712509861298E-01, \
    0.1081132319054248938202577E-01, \
    0.9736523941887687826947068E-02, \
    0.8650734035428648314139846E-02, \
    0.7555179500769820751618632E-02, \
    0.6451097794311275889059324E-02, \
    0.5339737098169214613757504E-02, \
    0.4222357382406607998634106E-02, \
    0.3100240403099316775464478E-02, \
    0.1974768768686808388940061E-02, \
    0.8487371680679110048896640E-03 ] )
  OddW47 = np.array ( [ \
    0.3287800959763194823557646E-01, \
    0.3282463569369918669308888E-01, \
    0.3273574336068393226919658E-01, \
    0.3261142878598215425670652E-01, \
    0.3245182648620325926685946E-01, \
    0.3225710916161441434734840E-01, \
    0.3202748750926769529295728E-01, \
    0.3176320999501228029097900E-01, \
    0.3146456258463840201321734E-01, \
    0.3113186843444399825682258E-01, \
    0.3076548754155891475295788E-01, \
    0.3036581635440506677724356E-01, \
    0.2993328734371411225240016E-01, \
    0.2946836853456688237515152E-01, \
    0.2897156299996101153484194E-01, \
    0.2844340831645486261311894E-01, \
    0.2788447598247691424309350E-01, \
    0.2729537079993022266578380E-01, \
    0.2667673021976135431896846E-01, \
    0.2602922365220227153290076E-01, \
    0.2535355174243201293660006E-01, \
    0.2465044561244261997612948E-01, \
    0.2392066606993061007707546E-01, \
    0.2316500278507139174920030E-01, \
    0.2238427343606939184041926E-01, \
    0.2157932282441140120676856E-01, \
    0.2075102196078490181790884E-01, \
    0.1990026712265721124487174E-01, \
    0.1902797888454570639306994E-01, \
    0.1813510112204514410759734E-01, \
    0.1722259999071698441334003E-01, \
    0.1629146288099104326591566E-01, \
    0.1534269735028835663459242E-01, \
    0.1437733003365908208357459E-01, \
    0.1339640553436828544136536E-01, \
    0.1240098529611606104018197E-01, \
    0.1139214645908584403924275E-01, \
    0.1037098070311609684083942E-01, \
    0.9338593083876397086740596E-02, \
    0.8296100874530990238145090E-02, \
    0.7244632443933199672626606E-02, \
    0.6185326261033323769312750E-02, \
    0.5119330329927718280032034E-02, \
    0.4047803316371759906879922E-02, \
    0.2971924240818190718436604E-02, \
    0.1892968377922935762776147E-02, \
    0.8135642494541165010544716E-03 ] )
  OddW48 = np.array ( [ \
    0.3220431459661350533475748E-01, \
    0.3215415737958550153577998E-01, \
    0.3207061987527279934927952E-01, \
    0.3195378880670864194528382E-01, \
    0.3180378546007149044495368E-01, \
    0.3162076555877401604294910E-01, \
    0.3140491910180172362457798E-01, \
    0.3115647016646904145775102E-01, \
    0.3087567667579765382432642E-01, \
    0.3056283013075858386135104E-01, \
    0.3021825530765601453452082E-01, \
    0.2984230992096702903457814E-01, \
    0.2943538425198732086424294E-01, \
    0.2899790074366843187205222E-01, \
    0.2853031356206718751823808E-01, \
    0.2803310812486267752680532E-01, \
    0.2750680059743034256009616E-01, \
    0.2695193735699644067363378E-01, \
    0.2636909442542934975707846E-01, \
    0.2575887687125678489535242E-01, \
    0.2512191818153004673565192E-01, \
    0.2445887960418784729059960E-01, \
    0.2377044946160306882104198E-01, \
    0.2305734243602599579639616E-01, \
    0.2232029882766713237862322E-01, \
    0.2156008378619171827843500E-01, \
    0.2077748651642656849799008E-01, \
    0.1997331945910804688818908E-01, \
    0.1914841744752812933525703E-01, \
    0.1830363684096414082229124E-01, \
    0.1743985463580780463940516E-01, \
    0.1655796755534245662902801E-01, \
    0.1565889111915692052020687E-01, \
    0.1474355869323695017635984E-01, \
    0.1381292052185304327114855E-01, \
    0.1286794274249338667571135E-01, \
    0.1190960638533075683273654E-01, \
    0.1093890635919594895396767E-01, \
    0.9956850427084044948237490E-02, \
    0.8964458176697999432566250E-02, \
    0.7962759997865495595598110E-02, \
    0.6952796096469405526464256E-02, \
    0.5935615630788222954183688E-02, \
    0.4912276262166028130833504E-02, \
    0.3883845329489294421733034E-02, \
    0.2851409243213055771419126E-02, \
    0.1816146398210039609502983E-02, \
    0.7805332219425612457264822E-03 ] )
  OddW49 = np.array ( [ \
    0.3155766036791122885809208E-01, \
    0.3151046648162834771323796E-01, \
    0.3143186227722154616152128E-01, \
    0.3132192610907518012817474E-01, \
    0.3118076756395815837033438E-01, \
    0.3100852735178559535833486E-01, \
    0.3080537716535627949917920E-01, \
    0.3057151950920577999218210E-01, \
    0.3030718749774580397961262E-01, \
    0.3001264462289103447190280E-01, \
    0.2968818449140509844801766E-01, \
    0.2933413053222750347643324E-01, \
    0.2895083567407331040373860E-01, \
    0.2853868199362694972663692E-01, \
    0.2809808033468091126593440E-01, \
    0.2762946989859901232207604E-01, \
    0.2713331780651255092639320E-01, \
    0.2661011863368585130179228E-01, \
    0.2606039391651548254092866E-01, \
    0.2548469163265475465058230E-01, \
    0.2488358565478194644598738E-01, \
    0.2425767517855707823164026E-01, \
    0.2360758412533789404661778E-01, \
    0.2293396052025105528408320E-01, \
    0.2223747584623937158435550E-01, \
    0.2151882437473022381824646E-01, \
    0.2077872247359421120742490E-01, \
    0.2001790789308656620794778E-01, \
    0.1923713903048718479867380E-01, \
    0.1843719417417849927098560E-01, \
    0.1761887072792438050675710E-01, \
    0.1678298441613870708950299E-01, \
    0.1593036847096084971103802E-01, \
    0.1506187280199023331295260E-01, \
    0.1417836314957944606614279E-01, \
    0.1328072022265728347995425E-01, \
    0.1236983882217516210343368E-01, \
    0.1144662695149825376113323E-01, \
    0.1051200491552474540574917E-01, \
    0.9566904411326136356898158E-02, \
    0.8612267615478888991732218E-02, \
    0.7649046279335257935390770E-02, \
    0.6678200860575098165183170E-02, \
    0.5700699773395926875152328E-02, \
    0.4717519037520830079689318E-02, \
    0.3729643487243034749198276E-02, \
    0.2738075873626878091327392E-02, \
    0.1743906958219244938639563E-02, \
    0.7494736467374053633626714E-03 ] )

  if ( l < 1 or 100 < l ):
    print ( '' )
    print ( 'LEGENDRE_WEIGHT - Fatal error!' )
    print ( '  1 <= L <= 100 is required.' )
    exit ( 'LEGENDRE_WEIGHT - Fatal error!' )

  lhalf = ( ( l + 1 ) // 2 )

  if ( ( l % 2 ) == 1 ):
    if ( lhalf < k ):
      kcopy = k - lhalf
    elif ( lhalf == k ):
      kcopy = lhalf
    else:
      kcopy = lhalf - k
  else:
    if ( lhalf < k ):
      kcopy = k - lhalf
    else:
      kcopy = lhalf + 1 - k
  
  if ( kcopy < 1 or lhalf < kcopy ):
    print ( '' )
    print ( 'LEGENDRE_WEIGHT - Fatal error!' )
    print ( '  1 <= K <= (L+1)/2 is required.' )
    exit ( 'LEGENDRE_WEIGHT - Fatal error!' )
#
#  If L is odd, and K = ( L - 1 ) / 2, then it's easy.
#
  if ( ( l % 2 ) == 1 and kcopy == lhalf ):
    weight = 2.0E+00 / cl[l] ** 2
  elif ( l == 2 ):
    weight = EvenW1[kcopy-1]
  elif ( l == 3 ):
    weight = OddW1[kcopy-1]
  elif ( l == 4 ):
    weight = EvenW2[kcopy-1]
  elif ( l == 5 ):
    weight = OddW2[kcopy-1]
  elif ( l == 6 ):
    weight = EvenW3[kcopy-1]
  elif ( l == 7 ):
    weight = OddW3[kcopy-1]
  elif ( l == 8 ):
    weight = EvenW4[kcopy-1]
  elif ( l == 9 ):
    weight = OddW4[kcopy-1]
  elif ( l == 10 ):
    weight = EvenW5[kcopy-1]
  elif ( l == 11 ):
    weight = OddW5[kcopy-1]
  elif ( l == 12 ):
    weight = EvenW6[kcopy-1]
  elif ( l == 13 ):
    weight = OddW6[kcopy-1]
  elif ( l == 14 ):
    weight = EvenW7[kcopy-1]
  elif ( l == 15 ):
    weight = OddW7[kcopy-1]
  elif ( l == 16 ):
    weight = EvenW8[kcopy-1]
  elif ( l == 17 ):
    weight = OddW8[kcopy-1]
  elif ( l == 18 ):
    weight = EvenW9[kcopy-1]
  elif ( l == 19 ):
    weight = OddW9[kcopy-1]
  elif ( l == 20 ):
    weight = EvenW10[kcopy-1]
  elif ( l == 21 ):
    weight = OddW10[kcopy-1]
  elif ( l == 22 ):
    weight = EvenW11[kcopy-1]
  elif ( l == 23 ):
    weight = OddW11[kcopy-1]
  elif ( l == 24 ):
    weight = EvenW12[kcopy-1]
  elif ( l == 25 ):
    weight = OddW12[kcopy-1]
  elif ( l == 26 ):
    weight = EvenW13[kcopy-1]
  elif ( l == 27 ):
    weight = OddW13[kcopy-1]
  elif ( l == 28 ):
    weight = EvenW14[kcopy-1]
  elif ( l == 29 ):
    weight = OddW14[kcopy-1]
  elif ( l == 30 ):
    weight = EvenW15[kcopy-1]
  elif ( l == 31 ):
    weight = OddW15[kcopy-1]
  elif ( l == 32 ):
    weight = EvenW16[kcopy-1]
  elif ( l == 33 ):
    weight = OddW16[kcopy-1]
  elif ( l == 34 ):
    weight = EvenW17[kcopy-1]
  elif ( l == 35 ):
    weight = OddW17[kcopy-1]
  elif ( l == 36 ):
    weight = EvenW18[kcopy-1]
  elif ( l == 37 ):
    weight = OddW18[kcopy-1]
  elif ( l == 38 ):
    weight = EvenW19[kcopy-1]
  elif ( l == 39 ):
    weight = OddW19[kcopy-1]
  elif ( l == 40 ):
    weight = EvenW20[kcopy-1]
  elif ( l == 41 ):
    weight = OddW20[kcopy-1]
  elif ( l == 42 ):
    weight = EvenW21[kcopy-1]
  elif ( l == 43 ):
    weight = OddW21[kcopy-1]
  elif ( l == 44 ):
    weight = EvenW22[kcopy-1]
  elif ( l == 45 ):
    weight = OddW22[kcopy-1]
  elif ( l == 46 ):
    weight = EvenW23[kcopy-1]
  elif ( l == 47 ):
    weight = OddW23[kcopy-1]
  elif ( l == 48 ):
    weight = EvenW24[kcopy-1]
  elif ( l == 49 ):
    weight = OddW24[kcopy-1]
  elif ( l == 50 ):
    weight = EvenW25[kcopy-1]
  elif ( l == 51 ):
    weight = OddW25[kcopy-1]
  elif ( l == 52 ):
    weight = EvenW26[kcopy-1]
  elif ( l == 53 ):
    weight = OddW26[kcopy-1]
  elif ( l == 54 ):
    weight = EvenW27[kcopy-1]
  elif ( l == 55 ):
    weight = OddW27[kcopy-1]
  elif ( l == 56 ):
    weight = EvenW28[kcopy-1]
  elif ( l == 57 ):
    weight = OddW28[kcopy-1]
  elif ( l == 58 ):
    weight = EvenW29[kcopy-1]
  elif ( l == 59 ):
    weight = OddW29[kcopy-1]
  elif ( l == 60 ):
    weight = EvenW30[kcopy-1]
  elif ( l == 61 ):
    weight = OddW30[kcopy-1]
  elif ( l == 62 ):
    weight = EvenW31[kcopy-1]
  elif ( l == 63 ):
    weight = OddW31[kcopy-1]
  elif ( l == 64 ):
    weight = EvenW32[kcopy-1]
  elif ( l == 65 ):
    weight = OddW32[kcopy-1]
  elif ( l == 66 ):
    weight = EvenW33[kcopy-1]
  elif ( l == 67 ):
    weight = OddW33[kcopy-1]
  elif ( l == 68 ):
    weight = EvenW34[kcopy-1]
  elif ( l == 69 ):
    weight = OddW34[kcopy-1]
  elif ( l == 70 ):
    weight = EvenW35[kcopy-1]
  elif ( l == 71 ):
    weight = OddW35[kcopy-1]
  elif ( l == 72 ):
    weight = EvenW36[kcopy-1]
  elif ( l == 73 ):
    weight = OddW36[kcopy-1]
  elif ( l == 74 ):
    weight = EvenW37[kcopy-1]
  elif ( l == 75 ):
    weight = OddW37[kcopy-1]
  elif ( l == 76 ):
    weight = EvenW38[kcopy-1]
  elif ( l == 77 ):
    weight = OddW38[kcopy-1]
  elif ( l == 78 ):
    weight = EvenW39[kcopy-1]
  elif ( l == 79 ):
    weight = OddW39[kcopy-1]
  elif ( l == 80 ):
    weight = EvenW40[kcopy-1]
  elif ( l == 81 ):
    weight = OddW40[kcopy-1]
  elif ( l == 82 ):
    weight = EvenW41[kcopy-1]
  elif ( l == 83 ):
    weight = OddW41[kcopy-1]
  elif ( l == 84 ):
    weight = EvenW42[kcopy-1]
  elif ( l == 85 ):
    weight = OddW42[kcopy-1]
  elif ( l == 86 ):
    weight = EvenW43[kcopy-1]
  elif ( l == 87 ):
    weight = OddW43[kcopy-1]
  elif ( l == 88 ):
    weight = EvenW44[kcopy-1]
  elif ( l == 89 ):
    weight = OddW44[kcopy-1]
  elif ( l == 90 ):
    weight = EvenW45[kcopy-1]
  elif ( l == 91 ):
    weight = OddW45[kcopy-1]
  elif ( l == 92 ):
    weight = EvenW46[kcopy-1]
  elif ( l == 93 ):
    weight = OddW46[kcopy-1]
  elif ( l == 94 ):
    weight = EvenW47[kcopy-1]
  elif ( l == 95 ):
    weight = OddW47[kcopy-1]
  elif ( l == 96 ):
    weight = EvenW48[kcopy-1]
  elif ( l == 97 ):
    weight = OddW48[kcopy-1]
  elif ( l == 98 ):
    weight = EvenW49[kcopy-1]
  elif ( l == 99 ):
    weight = OddW49[kcopy-1]
  elif ( l == 100 ):
    weight = EvenW50[kcopy-1]

  return weight

def legendre_weight_test ( ):

#*****************************************************************************80
#
## LEGENDRE_WEIGHT_TEST tests LEGENDRE_WEIGHT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ignace Bogaert,
#    Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
#    SIAM Journal on Scientific Computing,
#    Volume 36, Number 3, 2014, pages A1008-1026.
#
  import platform

  print ( '' )
  print ( 'LEGENDRE_WEIGHT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LEGENDRE_WEIGHT returns the K-th weight for' )
  print ( '  a Gauss Legendre rule of order L.' )

  for l in range ( 1, 11 ):
    print ( '' )
    print ( '  Gauss Legendre rule of order %d' % ( l ) )
    print ( '' )
    print ( '   K      Weight' )
    print ( '' )
    for k in range ( 1, l + 1 ):
      weight = legendre_weight ( l, k )
      print ( '  %2d  %14.6g' % ( k, weight ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_WEIGHT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  fastgl_test ( )
  timestamp ( )

