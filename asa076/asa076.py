#! /usr/bin/env python3
#
def asa076_test ( ):

#*****************************************************************************80
#
## asa076_test() tests asa076().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa076_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa076().' )

  tfn_test ( )
  tha_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa076_test():' )
  print ( '  Normal end of execution.' )

  return

def alnorm ( x, upper ):

#*****************************************************************************80
#
## alnorm() computes the cumulative density of the standard normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    Original FORTRAN77 version by David Hill.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Hill,
#    Algorithm AS 66:
#    The Normal Integral,
#    Applied Statistics,
#    Volume 22, Number 3, 1973, pages 424-427.
#
#  Input:
#
#    real X, is one endpoint of the semi-infinite interval
#    over which the integration takes place.
#
#    logical UPPER, determines whether the upper or lower
#    interval is to be integrated:
#    1 => integrate from X to + Infinity
#    0 => integrate from - Infinity to X.
#
#  Output:
#
#    real VALUE, the integral of the standard normal
#    distribution over the desired interval.
#
  import numpy as np

  a1 = 5.75885480458 
  a2 = 2.62433121679 
  a3 = 5.92885724438 
  b1 = -29.8213557807 
  b2 = 48.6959930692 
  c1 = -0.000000038052 
  c2 = 0.000398064794 
  c3 = -0.151679116635 
  c4 = 4.8385912808 
  c5 = 0.742380924027 
  c6 = 3.99019417011
  con = 1.28
  d1 = 1.00000615302
  d2 = 1.98615381364
  d3 = 5.29330324926
  d4 = -15.1508972451
  d5 = 30.789933034
  ltone = 7.0
  p = 0.39894228044 
  q = 0.39990348504
  r = 0.398942280385
  utzero = 18.66

  up = upper
  z = x

  if ( z < 0.0 ):
    if ( up ):
      up = 0
    else:
      up = 1
    z = - z

  if ( ltone < z and ( ( not up ) or utzero < z ) ):

    if ( up ):
      value = 0.0
    else:
      value = 1.0
 
    return value

  y = 0.5 * z * z

  if ( z <= con ):

    value = 0.5  - z * ( p - q * y \
      / ( y + a1 + b1 \
      / ( y + a2 + b2 \
      / ( y + a3 ))))

  else:

    value = r * np.exp ( - y ) \
      / ( z + c1 + d1 \
      / ( z + c2 + d2 \
      / ( z + c3 + d3 \
      / ( z + c4 + d4 \
      / ( z + c5 + d5 \
      / ( z + c6 ))))))

  if ( not up ):
    value = 1.0  - value

  return value

def owen_values ( n_data ):

#*****************************************************************************80
#
## owen_values() returns some values of Owen's T function.
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
#        Integral ( 0 <= X <= A ) e^(H^2*(1+X^2)/2) / (1+X^2) dX
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = 1/(2*Pi) * Integrate [ E^(-h^2*(1+x^2)/2)/(1+x^2), {x,0,a} ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Mike Patefield, David Tandy,
#    Fast and Accurate Calculation of Owen's T Function,
#    Journal of Statistical Software,
#    Volume 5, Number 5, 2000, pages 1-25.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    real H, a parameter.
#
#    real A, the upper limit of the integral.
#
#    real T, the value of the function.
#
  import numpy as np

  n_max = 28

  a_vec = np.array ( ( \
    0.2500000000000000E+00, \
    0.4375000000000000E+00, \
    0.9687500000000000E+00, \
    0.0625000000000000E+00, \
    0.5000000000000000E+00, \
    0.9999975000000000E+00, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.2000000000000000E+01, \
    0.3000000000000000E+01, \
    0.1000000000000000E+02, \
    0.1000000000000000E+03 ))

  h_vec = np.array ( ( \
    0.0625000000000000E+00, \
    6.5000000000000000E+00, \
    7.0000000000000000E+00, \
    4.7812500000000000E+00, \
    2.0000000000000000E+00, \
    1.0000000000000000E+00, \
    0.1000000000000000E+01, \
    0.1000000000000000E+01, \
    0.1000000000000000E+01, \
    0.1000000000000000E+01, \
    0.5000000000000000E+00, \
    0.5000000000000000E+00, \
    0.5000000000000000E+00, \
    0.5000000000000000E+00, \
    0.2500000000000000E+00, \
    0.2500000000000000E+00, \
    0.2500000000000000E+00, \
    0.2500000000000000E+00, \
    0.1250000000000000E+00, \
    0.1250000000000000E+00, \
    0.1250000000000000E+00, \
    0.1250000000000000E+00, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02, \
    0.7812500000000000E-02 ))

  t_vec = np.array ( ( \
    3.8911930234701366E-02, \
    2.0005773048508315E-11, \
    6.3990627193898685E-13, \
    1.0632974804687463E-07, \
    8.6250779855215071E-03, \
    6.6741808978228592E-02, \
    0.4306469112078537E-01, \
    0.6674188216570097E-01, \
    0.7846818699308410E-01, \
    0.7929950474887259E-01, \
    0.6448860284750376E-01, \
    0.1066710629614485E+00, \
    0.1415806036539784E+00, \
    0.1510840430760184E+00, \
    0.7134663382271778E-01, \
    0.1201285306350883E+00, \
    0.1666128410939293E+00, \
    0.1847501847929859E+00, \
    0.7317273327500385E-01, \
    0.1237630544953746E+00, \
    0.1737438887583106E+00, \
    0.1951190307092811E+00, \
    0.7378938035365546E-01, \
    0.1249951430754052E+00, \
    0.1761984774738108E+00, \
    0.1987772386442824E+00, \
    0.2340886964802671E+00, \
    0.2479460829231492E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    t = 0.0
    h = 0.0
    a = 0.0
  else:
    t = t_vec[n_data]
    h = h_vec[n_data]
    a = a_vec[n_data]
    n_data = n_data + 1

  return n_data, h, a, t

def tfn ( x, fx ):

#*****************************************************************************80
#
## TFN calculates the T-function of Owen.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2008
#
#  Author:
#
#    Original FORTRAN77 version by JC Young, Christoph Minder.
#    This version by John Burkardt.
#
#  Reference:
#
#    MA Porter, DJ Winstanley,
#    Remark AS R30:
#    A Remark on Algorithm AS76:
#    An Integral Useful in Calculating Noncentral T and Bivariate
#    Normal Probabilities,
#    Applied Statistics,
#    Volume 28, Number 1, 1979, page 113.
#
#    JC Young, Christoph Minder,
#    Algorithm AS 76:
#    An Algorithm Useful in Calculating Non-Central T and
#    Bivariate Normal Distributions,
#    Applied Statistics,
#    Volume 23, Number 3, 1974, pages 455-457.
#
#  Input:
#
#    real X, FX, the parameters of the function.
#
#  Output:
#
#    real VALUE, the value of the T-function.
#
  import numpy as np

  ng = 5

  r = np.array ( [ \
    0.1477621, \
    0.1346334, \
    0.1095432, \
    0.0747257, \
    0.0333357 ] )

  tp = 0.159155
  tv1 = 1.0E-35
  tv2 = 15.0
  tv3 = 15.0
  tv4 = 1.0E-05

  u = np.array ( [ \
    0.0744372, \
    0.2166977, \
    0.3397048, \
    0.4325317, \
    0.4869533 ] )
#
#  Test for X near zero.
#
  if ( np.abs ( x ) < tv1 ):
    value = tp * np.arctan ( fx )
    return value
#
#  Test for large values of abs(X).
#
  if ( tv2 < np.abs ( x ) ):
    value = 0.0
    return value
#
#  Test for FX near zero.
#
  if ( np.abs ( fx ) < tv1 ):
    value = 0.0
    return value
#
#  Test whether abs ( FX ) is so large that it must be truncated.
#
  xs = - 0.5 * x * x
  x2 = fx
  fxs = fx * fx
#
#  Computation of truncation point by Newton iteration.
#
  if ( tv3 <= np.log ( 1.0 + fxs ) - xs * fxs ):

    x1 = 0.5 * fx
    fxs = 0.25 * fxs

    while ( True ):

      rt = fxs + 1.0

      x2 = x1 + ( xs * fxs + tv3 - np.log ( rt ) ) \
        / ( 2.0 * x1 * ( 1.0 / rt - xs ) )

      fxs = x2 * x2

      if ( np.abs ( x2 - x1 ) < tv4 ):
        break
 
      x1 = x2
#
#  Gaussian quadrature.
#
  rt = 0.0

  for i in range ( 0, ng ):

    r1 = 1.0 + fxs * ( 0.5 + u[i] )**2
    r2 = 1.0 + fxs * ( 0.5 - u[i] )**2

    rt = rt + r[i] * ( np.exp ( xs * r1 ) / r1 + np.exp ( xs * r2 ) / r2 )

  value = rt * x2 * tp

  return value

def tfn_test ( ):

#*****************************************************************************80
#
## tfn_test() tests tfn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'tfn_test():' )
  print ( '  tfn() evaluates Owen''s T function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '          H            A        ', end = '' )
  print ( '  T                       T' )
  print ( '                                ', end = '' )
  print ( '  (Tabulated)             (TFN)                   DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, h, a, t1 = owen_values ( n_data )

    if ( n_data == 0 ):
      break

    t2 = tfn ( h, a )

    print ( '  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' \
      % ( h, a, t1, t2, np.abs ( t1 - t2 ) ) )

  return

def tha ( h1, h2, a1, a2 ):

#*****************************************************************************80
#
## tha() computes Owen's T function.
#
#  Discussion:
#
#    This function computes T(H1/H2, A1/A2) for any real numbers H1, H2,
#    A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by JC Young, Christoph Minder.
#    This version by John Burkardt.
#
#  Reference:
#
#    Richard Boys,
#    Remark AS R80:
#    A Remark on Algorithm AS76:
#    An Integral Useful in Calculating Noncentral T and Bivariate
#    Normal Probabilities,
#    Applied Statistics,
#    Volume 38, Number 3, 1989, pages 580-582.
#
#    Youn-Min Chou,
#    Remark AS R55:
#    A Remark on Algorithm AS76:
#    An Integral Useful in Calculating Noncentral T and Bivariate
#    Normal Probabilities,
#    Applied Statistics,
#    Volume 34, Number 1, 1985, pages 100-101.
#
#    PW Goedhart, MJW Jansen,
#    Remark AS R89:
#    A Remark on Algorithm AS76:
#    An Integral Useful in Calculating Noncentral T and Bivariate
#    Normal Probabilities,
#    Applied Statistics,
#    Volume 41, Number 2, 1992, pages 496-497.
#
#    JC Young, Christoph Minder,
#    Algorithm AS 76:
#    An Algorithm Useful in Calculating Noncentral T and
#    Bivariate Normal Distributions,
#    Applied Statistics,
#    Volume 23, Number 3, 1974, pages 455-457.
#
#  Input:
#
#    real H1, H2, A1, A2, define the arguments of the T function.
#
#  Output:
#
#    real VALUE, the value of Owen's T function.
#
  import numpy as np

  if ( h2 == 0.0 ):
    value = 0.0
    return value

  h = h1 / h2

  if ( a2 == 0.0 ):

    g = alnorm ( h, 0 )

    if ( h < 0.0 ):
      value = g / 2.0
    else:
      value = ( 1.0 - g ) / 2.0

    if ( a1 < 0.0 ):
      value = - value

    return value

  a = a1 / a2

  if ( np.abs ( h ) < 0.3 and 7.0 < np.abs ( a ) ):

    lam = np.abs ( a * h )
    ex = np.exp ( - lam * lam / 2.0 )
    g = alnorm ( lam, 0 )
    c1 = ( ex / lam + np.sqrt ( 2.0 * np.pi ) * ( g - 0.5 ) ) / 2.0 / np.pi
    c2 = ( ( lam * lam + 2.0 ) * ex / lam / lam / lam \
      + np.sqrt ( 2.0 * np.pi ) * ( g - 0.5 ) ) / ( 6.0 * 2.0 * np.pi )
    ah = np.abs ( h )
    value = 0.25 - c1 * ah + c2 * ah * ah * ah
    if ( a < 0.0 ):
      value = - np.abs ( value )
    else:
       value = np.abs ( value )

  else:

    absa = np.abs ( a )

    if ( absa <= 1.0 ):
      value = tfn ( h, a )
      return value

    ah = absa * h
    gh = alnorm ( h, 0 )
    gah = alnorm ( ah, 0 )
    value = 0.5 * ( gh + gah ) - gh * gah - tfn ( ah, 1.0 / absa )

    if ( a < 0.0 ):
      value = - value

  return value

def tha_test ( ):

#*****************************************************************************80
#
## tha_test() tests tha().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'tha_test():' )
  print ( '  tha() evaluates Owen''s T function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '          H            A        ', end = '' )
  print ( 'T                         T' )
  print ( '                                ', end = '' )
  print ( '(Tabulated)               (THA)                   DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, h, a, t1 = owen_values ( n_data )

    if ( n_data == 0 ):
      break

    t2 = tha ( h, 1.0, a, 1.0 )

    print ( '  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' \
      % ( h, a, t1, t2, np.abs ( t1 - t2 ) ) )

  return

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
  asa076_test ( )
  timestamp ( )


