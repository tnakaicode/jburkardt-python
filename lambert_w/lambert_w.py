#! /usr/bin/env python3
#
def lambert_w_test ( ):

#*****************************************************************************80
#
## lambert_w_test() tests lambert_w().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lambert_w_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lambert_w().' )

  lambert_w_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lambert_w_test():' )
  print ( '  Normal end of execution.' )

  return

def lambert_w_test01 ( ):

#*****************************************************************************80
#
## lambert_w_test01() compares lambert_w() to stored values, and a built in function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2023
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import lambertw

  print ( '' )
  print ( 'lambert_w_test01():' )
  print ( '  Compare stored, computed, and system values for LambertW(x).' )
  print ( '' )
  print ( '      X           Stored value       lambert_w(x)       lambertw(x)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1, b = lambert_w_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = lambert_w ( x, b, 0 )

    fx3 = lambertw ( x, b )

    print ( '  %12f  %24.16f  %24.16f  %24.16f' % ( x, fx1, fx2, fx3.real ) )

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

def lambert_w ( x, nb, l ):

#*****************************************************************************80
#
## lambert_w() approximates the Lambert W function.
#
#  Discussion:
#
#    The call will fail if the input value X is out of range.
#    The range requirement for the upper branch is:
#      -exp(-1) <= X.
#    The range requirement for the lower branch is:
#      -exp(-1) < X < 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    This version by John Burkardt.
#
#  Reference:
#
#    Andrew Barry, S. J. Barry, Patricia Culligan-Hensley,
#    Algorithm 743: WAPR - A Fortran routine for calculating real 
#    values of the W-function,
#    ACM Transactions on Mathematical Software,
#    Volume 21, Number 2, June 1995, pages 172-181.
#
#  Input:
#
#    real x: the argument.
#
#    integer nb: indicates the desired branch.
#    * 0, the upper branch
#    * nonzero, the lower branch.
#
#    integer l: indicates the interpretation of X.
#    * 1, X is actually the offset from -(exp-1), so compute W(X-exp(-1)).
#    * not 1, X is the argument compute W(X)
#
#  Output:
#
#    real value: the approximate value of W(X).
#
  import numpy as np

  value = float ( "NaN" )

  nbits = 52
  niter = 1

  em = - np.exp ( -1.0 )
  em9 = - np.exp ( -9.0 )
  c13 = 1.0 / 3.0
  c23 = 2.0 * c13
  em2 = 2.0 / em
  d12 = - em2
  tb = 0.5 ** nbits
  tb2 = np.sqrt ( tb )
  x0 = tb ** ( 1.0 / 6.0 ) * 0.5
  x1 = ( 1.0 - 17.0 * tb ** ( 2.0 / 7.0 ) ) * em
  an3 = 8.0 / 3.0
  an4 = 135.0 / 83.0
  an5 = 166.0 / 39.0
  an6 = 3167.0 / 3549.0
  s2 = np.sqrt ( 2.0 )
  s21 = 2.0 * s2 - 3.0
  s22 = 4.0 - 3.0 * s2
  s23 = s2 - 2.0

  if ( l == 1 ):

    delx = x

    if ( delx < 0.0 ):
      raise Exception ( 'WAPR - Fatal error!' )

    xx = x + em

  else:

    if ( x < em ):
      return value
    elif ( x == em ):
      value = -1.0
      return value

    xx = x
    delx = xx - em

  if ( nb == 0 ):
#
#  Calculations for Wp.
#
    if ( abs ( xx ) <= x0 ):
      value = xx / ( 1.0 + xx / ( 1.0 + xx \
        / ( 2.0 + xx / ( 0.6 + 0.34 * xx ))))
      return value
    elif ( xx <= x1 ):
      reta = np.sqrt ( d12 * delx )
      value = reta / ( 1.0 + reta / ( 3.0 + reta / ( reta \
        / ( an4 + reta / ( reta * an6 + an5 ) ) + an3 ) ) ) - 1.0
      return value
    elif ( xx <= 20.0 ):
      reta = s2 * np.sqrt ( 1.0 - xx / em )
      an2 = 4.612634277343749 * np.sqrt ( np.sqrt ( reta + 1.09556884765625 ))
      value = reta / ( 1.0 + reta / ( 3.0 + ( s21 * an2 \
        + s22 ) * reta / ( s23 * ( an2 + reta )))) - 1.0
    else:
      zl = np.log ( xx )
      value = np.log ( xx / np.log ( xx \
        / zl ** np.exp ( -1.124491989777808 / \
        ( 0.4225028202459761 + zl ))))
#
#  Calculations for Wm.
#
  else:

    if ( 0.0 <= xx ):
      return value
    elif ( xx <= x1 ):
      reta = np.sqrt ( d12 * delx )
      value = reta / ( reta / ( 3.0 + reta / ( reta / ( an4 \
        + reta / ( reta * an6 - an5 ) ) - an3 ) ) - 1.0 ) - 1.0
      return value
    elif ( xx <= em9 ):
      zl = np.log ( - xx )
      t = -1.0 - zl
      ts = np.sqrt ( t )
      value = zl - ( 2.0 * ts ) / ( s2 + ( c13 - t \
        / ( 270.0 + ts * 127.0471381349219 )) * ts )
    else:
      zl = np.log ( - xx )
      eta = 2.0 - em2 * xx
      value = np.log ( xx / np.log ( -xx / ( ( 1.0 \
        - 0.5043921323068457 * ( zl + 1.0 ) ) \
        * ( np.sqrt ( eta ) + eta / 3.0 ) + 1.0 )))

  for i in range ( 0, niter ):
    zn = np.log ( xx / value ) - value
    temp = 1.0 + value
    temp2 = temp + c23 * zn
    temp2 = 2.0 * temp * temp2
    value = value * ( 1.0 + ( zn / temp ) * ( temp2 - zn ) \
      / ( temp2 - 2.0 * zn ) )

  return value

def lambert_w_values ( n_data ):

#*****************************************************************************80
#
## lambert_w_values() returns some values of the Lambert W function.
#
#  Discussion:
#
#    The function W(X) is defined implicitly by:
#
#      W(X) * e^W(X) = X
#
#    The function is defined for -1/e <= x.
#
#    There are two branches, joining at -1/e = x.
#    The lower branch extends from -1/e <= x < 0
#    The upper branch extends from -1/e <= x
#
#    The function is also known as the "Omega" function.
#
#    In Mathematica, the function can be evaluated by:
#      W = ProductLog [ X ]
#
#    In MATLAB,
#      W = lambertw ( b, x )
#    where b = -1 for lower branch, 0 for upper branch.
#
#    In Python,
#      W = scipy.special.lambertw ( x, b )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    "Why W?",
#    The American Scientist,
#    Volume 93, March-April 2005, pages 104-108.
#
#    Eric Weisstein,
#    "Lambert's W-Function",
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data: The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data: On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real x: the argument of the function.
#
#    real f: the value of the function.
#
#    integer b: -1 (lower branch) or 0 (upper branch).
#
  import numpy as np

  n_max = 41

  f_vec = np.array ( [ \
   -4.889720169867429, \
   -3.994308347002122, \
   -3.439216483280204, \
   -3.022313245324657, \
   -2.678346990016661, \
   -2.376421342062887, \
   -2.097349210703492, \
   -1.824388309032984, \
   -1.531811608389612, \
   -1.000000000000000, \
   -0.608341284733432, \
   -0.471671909743522, \
   -0.374493134019498, \
   -0.297083462446424, \
   -0.231960952986534, \
   -0.175356500529299, \
   -0.125066982982524, \
   -0.079678160511477, \
   -0.038221241746799, \
    0.0000000000000000E+00, \
    0.3517337112491958E+00, \
    0.5671432904097839E+00, \
    0.7258613577662263E+00, \
    0.8526055020137255E+00, \
    0.9585863567287029E+00, \
    0.1000000000000000E+01, \
    0.1049908894964040E+01, \
    0.1130289326974136E+01, \
    0.1202167873197043E+01, \
    0.1267237814307435E+01, \
    0.1326724665242200E+01, \
    0.1381545379445041E+01, \
    0.1432404775898300E+01, \
    0.1479856830173851E+01, \
    0.1524345204984144E+01, \
    0.1566230953782388E+01, \
    0.1605811996320178E+01, \
    0.1745528002740699E+01, \
    0.3385630140290050E+01, \
    0.5249602852401596E+01, \
    0.1138335808614005E+02 ] )

  x_vec = np.array ( [ \
   -0.036787944117144, \
   -0.073575888234288, \
   -0.110363832351433, \
   -0.147151776468577, \
   -0.183939720585721, \
   -0.220727664702865, \
   -0.257515608820010, \
   -0.294303552937154, \
   -0.331091497054298, \
   -0.367879441171442, \
   -0.331091497054298, \
   -0.294303552937154, \
   -0.257515608820010, \
   -0.220727664702865, \
   -0.183939720585721, \
   -0.147151776468577, \
   -0.110363832351433, \
   -0.073575888234288, \
   -0.036787944117144, \
    0.0000000000000000E+00, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.1500000000000000E+01, \
    0.2000000000000000E+01, \
    0.2500000000000000E+01, \
    0.2718281828459045E+01, \
    0.3000000000000000E+01, \
    0.3500000000000000E+01, \
    0.4000000000000000E+01, \
    0.4500000000000000E+01, \
    0.5000000000000000E+01, \
    0.5500000000000000E+01, \
    0.6000000000000000E+01, \
    0.6500000000000000E+01, \
    0.7000000000000000E+01, \
    0.7500000000000000E+01, \
    0.8000000000000000E+01, \
    0.1000000000000000E+02, \
    0.1000000000000000E+03, \
    0.1000000000000000E+04, \
    0.1000000000000000E+07 ] )

  branch_vec =  np.array ( [ \
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, \
     0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
     0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
     0,  0,  0,  0,  0,  0,  0,  0,  0,  0, \
     0 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
    b = 0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    b = branch_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f, b

if ( __name__ == '__main__' ):
  timestamp ( )
  lambert_w_test ( )
  timestamp ( )

