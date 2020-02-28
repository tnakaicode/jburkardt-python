#! /usr/bin/env python3
#
def angle_shift ( alpha, beta ):

#*****************************************************************************80
#
## ANGLE_SHIFT shifts angle ALPHA to lie between BETA and BETA+2PI.
#
#  Discussion:
#
#    The input angle ALPHA is shifted by multiples of 2 * PI to lie
#    between BETA and BETA+2*PI.
#
#    The resulting angle GAMMA has all the same trigonometric function
#    values as ALPHA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the angle to be shifted.
#
#    Input, real BETA, defines the lower endpoint of
#    the angle range.
#
#    Output, real GAMMA, the shifted angle.
#
  import numpy as np
  
  if ( alpha < beta ):
    gamma = beta - np.mod ( beta - alpha, 2.0 * np.pi ) + 2.0 * np.pi
  else:
    gamma = beta + np.mod ( alpha - beta, 2.0 * np.pi )

  return gamma

def angle_shift_test ( ):

#*****************************************************************************80
#
## ANGLE_SHIFT_TEST demonstrates the use of ANGLE_SHIFT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  
  print ( '' )
  print ( 'ANGLE_SHIFT_TEST:' )
  print ( '  ANGLE_SHIFT shifts angle ALPHA to lie between' )
  print ( '  BETA and BETA+2 PI.' )
  print ( '' )
  print ( '           ALPHA          BETA   ALPHA_SHIFT     BETA+2 PI' )
  print ( '' )

  seed = 123456789
  beta, seed  = r8_uniform_01 ( seed )
  beta = 10.0 * beta
  
  for i in range ( 0, 10 ):
    alpha, seed = r8_uniform_01 ( seed )
    alpha = 20.0 * alpha - 10.0
    alpha2 = angle_shift ( alpha, beta )
    print ( '  %12f  %12f  %12f  %12f' \
      % ( alpha, beta, alpha2, beta + 2.0 * np.pi ) )

  return

def arccos_cordic ( t, n ):

#*****************************************************************************80
#
## ARCCOS_CORDIC returns the arccosine of an angle using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Michel Muller,
#    Elementary Functions: Algorithms and Implementation,
#    Second Edition,
#    Birkhaeuser, 2006,
#    ISBN13: 978-0-8176-4372-0,
#    LC: QA331.M866.
#
#  Parameters:
#
#    Input, real T, the cosine of an angle.  -1 <= T <= 1.
#
#    Input, integer N, the number of iterations to take.
#    A value of 10 is low.  Good accuracy is achieved with 20 or more
#    iterations.
#
#    Output, real THETA, an angle whose cosine is T.
#
#  Local Parameters:
#
#    Local, real ANGLES(60) = arctan ( (1/2)^(0:59) )
#
  import numpy as np
  from sys import exit
  
  angles = np.array ( [  \
    7.8539816339744830962E-01, \
    4.6364760900080611621E-01, \
    2.4497866312686415417E-01, \
    1.2435499454676143503E-01, \
    6.2418809995957348474E-02, \
    3.1239833430268276254E-02, \
    1.5623728620476830803E-02, \
    7.8123410601011112965E-03, \
    3.9062301319669718276E-03, \
    1.9531225164788186851E-03, \
    9.7656218955931943040E-04, \
    4.8828121119489827547E-04, \
    2.4414062014936176402E-04, \
    1.2207031189367020424E-04, \
    6.1035156174208775022E-05, \
    3.0517578115526096862E-05, \
    1.5258789061315762107E-05, \
    7.6293945311019702634E-06, \
    3.8146972656064962829E-06, \
    1.9073486328101870354E-06, \
    9.5367431640596087942E-07, \
    4.7683715820308885993E-07, \
    2.3841857910155798249E-07, \
    1.1920928955078068531E-07, \
    5.9604644775390554414E-08, \
    2.9802322387695303677E-08, \
    1.4901161193847655147E-08, \
    7.4505805969238279871E-09, \
    3.7252902984619140453E-09, \
    1.8626451492309570291E-09, \
    9.3132257461547851536E-10, \
    4.6566128730773925778E-10, \
    2.3283064365386962890E-10, \
    1.1641532182693481445E-10, \
    5.8207660913467407226E-11, \
    2.9103830456733703613E-11, \
    1.4551915228366851807E-11, \
    7.2759576141834259033E-12, \
    3.6379788070917129517E-12, \
    1.8189894035458564758E-12, \
    9.0949470177292823792E-13, \
    4.5474735088646411896E-13, \
    2.2737367544323205948E-13, \
    1.1368683772161602974E-13, \
    5.6843418860808014870E-14, \
    2.8421709430404007435E-14, \
    1.4210854715202003717E-14, \
    7.1054273576010018587E-15, \
    3.5527136788005009294E-15, \
    1.7763568394002504647E-15, \
    8.8817841970012523234E-16, \
    4.4408920985006261617E-16, \
    2.2204460492503130808E-16, \
    1.1102230246251565404E-16, \
    5.5511151231257827021E-17, \
    2.7755575615628913511E-17, \
    1.3877787807814456755E-17, \
    6.9388939039072283776E-18, \
    3.4694469519536141888E-18, \
    1.7347234759768070944E-18 ] )

  if ( 1.0 < abs ( t ) ):
    print ( '' )
    print ( 'ARCCOS_CORDIC - Fatal error!' )
    print ( '  Input argument 1 < |T|.' )
    exit ( 'ARCCOS_CORDIC - Fatal error!' )

  theta = 0.0
  z = np.array ( [ 1.0, 0.0 ] )

  poweroftwo = 1.0

  for j in range ( 0, n ):

    if ( z[1] < 0.0 ):
      sign_z2 = -1.0
    else:
      sign_z2 = +1.0
  
    if ( t <= z[0] ):
      sigma = + sign_z2
    else:
      sigma = - sign_z2

    if ( j < angles.size ):
      angle = angles[j]
    else:
      angle = angle / 2.0

    r = np.array ( [\
      [ 1.0,               - sigma * poweroftwo ], \
      [ sigma * poweroftwo, 1.0 ] ] )

    z = np.dot ( r, np.dot ( r, z ) )
    
    theta = theta + 2.0 * sigma * angle

    t = t + t * poweroftwo * poweroftwo

    poweroftwo = poweroftwo / 2.0

  return theta

def arccos_cordic_test ( ):

#*****************************************************************************80
#
## ARCCOS_CORDIC_TEST demonstrates the use of ARCCOS_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ARCCOS_CORDIC_TEST:' )
  print ( '  ARCCOS_CORDIC computes the arccosine of T' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      T    N         ArcCos(T)   ArcCos(T)      Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, t, a1 = arccos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      a2 = arccos_cordic ( t, n )
      d = a1 - a2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( t, n, a1, a2, d ) )

  return
  
def arccos_values ( n_data ):

#*****************************************************************************80
#
## ARCCOS_VALUES returns some values of the arc cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcCos[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 12

  fx_vec = np.array ( ( \
    1.6709637479564564156, \
    1.5707963267948966192, \
    1.4706289056333368229, \
    1.3694384060045658278, \
    1.2661036727794991113, \
    1.1592794807274085998, \
    1.0471975511965977462, \
    0.92729521800161223243, \
    0.79539883018414355549, \
    0.64350110879328438680, \
    0.45102681179626243254, \
    0.00000000000000000000 ) )

  x_vec = np.array ( ( \
    -0.1, \
     0.0, \
     0.1, \
     0.2, \
     0.3, \
     0.4, \
     0.5, \
     0.6, \
     0.7, \
     0.8, \
     0.9, \
     1.0 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def arccos_values_test ( ):

#*****************************************************************************80
#
## ARCCOS_VALUES_TEST tests ARCCOS VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCCOS_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCCOS_VALUES stores values of' )
  print ( '  the arc cosine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arccos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCCOS_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def arcsin_cordic ( t, n ):

#*****************************************************************************80
#
## ARCSIN_CORDIC returns the arcsine of an angle using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Michel Muller,
#    Elementary Functions: Algorithms and Implementation,
#    Second Edition,
#    Birkhaeuser, 2006,
#    ISBN13: 978-0-8176-4372-0,
#    LC: QA331.M866.
#
#  Parameters:
#
#    Input, real T, the sine of an angle.  -1 <= T <= 1.
#
#    Input, integer N, the number of iterations to take.
#    A value of 10 is low.  Good accuracy is achieved with 20 or more
#    iterations.
#
#    Output, real THETA, an angle whose sine is T.
#
#  Local Parameters:
#
#    Local, real ANGLES(60) = arctan ( (1/2)^(0:59) )
#
  import numpy as np
  from sys import exit
  
  angles = np.array ( [ \
    7.8539816339744830962E-01, \
    4.6364760900080611621E-01, \
    2.4497866312686415417E-01, \
    1.2435499454676143503E-01, \
    6.2418809995957348474E-02, \
    3.1239833430268276254E-02, \
    1.5623728620476830803E-02, \
    7.8123410601011112965E-03, \
    3.9062301319669718276E-03, \
    1.9531225164788186851E-03, \
    9.7656218955931943040E-04, \
    4.8828121119489827547E-04, \
    2.4414062014936176402E-04, \
    1.2207031189367020424E-04, \
    6.1035156174208775022E-05, \
    3.0517578115526096862E-05, \
    1.5258789061315762107E-05, \
    7.6293945311019702634E-06, \
    3.8146972656064962829E-06, \
    1.9073486328101870354E-06, \
    9.5367431640596087942E-07, \
    4.7683715820308885993E-07, \
    2.3841857910155798249E-07, \
    1.1920928955078068531E-07, \
    5.9604644775390554414E-08, \
    2.9802322387695303677E-08, \
    1.4901161193847655147E-08, \
    7.4505805969238279871E-09, \
    3.7252902984619140453E-09, \
    1.8626451492309570291E-09, \
    9.3132257461547851536E-10, \
    4.6566128730773925778E-10, \
    2.3283064365386962890E-10, \
    1.1641532182693481445E-10, \
    5.8207660913467407226E-11, \
    2.9103830456733703613E-11, \
    1.4551915228366851807E-11, \
    7.2759576141834259033E-12, \
    3.6379788070917129517E-12, \
    1.8189894035458564758E-12, \
    9.0949470177292823792E-13, \
    4.5474735088646411896E-13, \
    2.2737367544323205948E-13, \
    1.1368683772161602974E-13, \
    5.6843418860808014870E-14, \
    2.8421709430404007435E-14, \
    1.4210854715202003717E-14, \
    7.1054273576010018587E-15, \
    3.5527136788005009294E-15, \
    1.7763568394002504647E-15, \
    8.8817841970012523234E-16, \
    4.4408920985006261617E-16, \
    2.2204460492503130808E-16, \
    1.1102230246251565404E-16, \
    5.5511151231257827021E-17, \
    2.7755575615628913511E-17, \
    1.3877787807814456755E-17, \
    6.9388939039072283776E-18, \
    3.4694469519536141888E-18, \
    1.7347234759768070944E-18 ] )

  if ( 1.0 < abs ( t ) ):
    print ( '' )
    print ( 'ARCSIN_CORDIC - Fatal error!' )
    print ( '  Input argument 1 < |T|.' )
    exit ( 'ARCSIN_CORDIC - Fatal error!' )

  theta = 0.0
  z = np.array ( [ 1.0, 0.0 ] )
  poweroftwo = 1.0

  for j in range ( 0, n ):

    if ( z[0] < 0.0 ):
      sign_z1 = -1.0
    else:
      sign_z1 = +1.0
  
    if ( z[1] <= t ):
      sigma = + sign_z1
    else:
      sigma = - sign_z1

    if ( j < angles.size ):
      angle = angles[j]
    else:
      angle = angle / 2.0

    r = np.array ( [ \
      [ 1.0,               - sigma * poweroftwo ], \
      [ sigma * poweroftwo, 1.0 ] ] )

    z = np.dot ( r, np.dot ( r, z ) )
    
    theta = theta + 2.0 * sigma * angle

    t = t + t * poweroftwo * poweroftwo

    poweroftwo = poweroftwo / 2.0

  return theta

def arcsin_cordic_test ( ):

#*****************************************************************************80
#
## ARCSIN_CORDIC_TEST demonstrates the use of ARCSIN_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ARCSIN_CORDIC_TEST:' )
  print ( '  ARCSIN_CORDIC computes the arcsine of T' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      T    N         ArcSin(T)   ArcSin(T)      Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, t, a1 = arcsin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
     
      a2 = arcsin_cordic ( t, n )
      d = a1 - a2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( t, n, a1, a2, d ) )

  return

def arcsin_values ( n_data ):

#*****************************************************************************80
#
## ARCSIN_VALUES returns some values of the arc sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcSin[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 12

  fx_vec = np.array ( ( \
    -0.10016742116155979635, \
     0.00000000000000000000, \
     0.10016742116155979635, \
     0.20135792079033079146, \
     0.30469265401539750797, \
     0.41151684606748801938, \
     0.52359877559829887308, \
     0.64350110879328438680, \
     0.77539749661075306374, \
     0.92729521800161223243, \
     1.1197695149986341867, \
     1.5707963267948966192 ) )

  x_vec = np.array ( ( \
    -0.1, \
     0.0, \
     0.1, \
     0.2, \
     0.3, \
     0.4, \
     0.5, \
     0.6, \
     0.7, \
     0.8, \
     0.9, \
     1.0 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def arcsin_values_test ( ):

#*****************************************************************************80
#
## ARCSIN_VALUES_TEST tests ARCSIN VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCSIN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCSIN_VALUES stores values of' )
  print ( '  the arc sine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arcsin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCSIN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def arctan_values ( n_data ):

#*****************************************************************************80
#
## ARCTAN_VALUES returns some values of the arc tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcTan[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 11

  fx_vec = np.array ( ( \
    0.00000000000000000000, \
    0.24497866312686415417, \
    0.32175055439664219340, \
    0.46364760900080611621, \
    0.78539816339744830962, \
    1.1071487177940905030, \
    1.2490457723982544258, \
    1.3258176636680324651, \
    1.3734007669450158609, \
    1.4711276743037345919, \
    1.5208379310729538578 ) )

  x_vec = np.array ( ( \
    0.00000000000000000000, \
    0.25000000000000000000, \
    0.33333333333333333333, \
    0.50000000000000000000, \
    1.0000000000000000000, \
    2.0000000000000000000, \
    3.0000000000000000000, \
    4.0000000000000000000, \
    5.0000000000000000000, \
    10.000000000000000000, \
    20.000000000000000000 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def arctan_cordic ( x, y, n ):

#*****************************************************************************80
#
## ARCTAN_CORDIC returns the arctangent of an angle using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Michel Muller,
#    Elementary Functions: Algorithms and Implementation,
#    Second Edition,
#    Birkhaeuser, 2006,
#    ISBN13: 978-0-8176-4372-0,
#    LC: QA331.M866.
#
#  Parameters:
#
#    Input, real X, Y, define the tangent of an angle as Y/X.
#
#    Input, integer N, the number of iterations to take.
#    A value of 10 is low.  Good accuracy is achieved with 20 or more
#    iterations.
#
#    Output, real THETA, the angle whose tangent is Y/X.
#
#  Local Parameters:
#
#    Local, real ANGLES(60) = arctan ( (1/2)^(0:59) )
#
  import numpy as np
  
  angles = np.array ( [ \
    7.8539816339744830962E-01, \
    4.6364760900080611621E-01, \
    2.4497866312686415417E-01, \
    1.2435499454676143503E-01, \
    6.2418809995957348474E-02, \
    3.1239833430268276254E-02, \
    1.5623728620476830803E-02, \
    7.8123410601011112965E-03, \
    3.9062301319669718276E-03, \
    1.9531225164788186851E-03, \
    9.7656218955931943040E-04, \
    4.8828121119489827547E-04, \
    2.4414062014936176402E-04, \
    1.2207031189367020424E-04, \
    6.1035156174208775022E-05, \
    3.0517578115526096862E-05, \
    1.5258789061315762107E-05, \
    7.6293945311019702634E-06, \
    3.8146972656064962829E-06, \
    1.9073486328101870354E-06, \
    9.5367431640596087942E-07, \
    4.7683715820308885993E-07, \
    2.3841857910155798249E-07, \
    1.1920928955078068531E-07, \
    5.9604644775390554414E-08, \
    2.9802322387695303677E-08, \
    1.4901161193847655147E-08, \
    7.4505805969238279871E-09, \
    3.7252902984619140453E-09, \
    1.8626451492309570291E-09, \
    9.3132257461547851536E-10, \
    4.6566128730773925778E-10, \
    2.3283064365386962890E-10, \
    1.1641532182693481445E-10, \
    5.8207660913467407226E-11, \
    2.9103830456733703613E-11, \
    1.4551915228366851807E-11, \
    7.2759576141834259033E-12, \
    3.6379788070917129517E-12, \
    1.8189894035458564758E-12, \
    9.0949470177292823792E-13, \
    4.5474735088646411896E-13, \
    2.2737367544323205948E-13, \
    1.1368683772161602974E-13, \
    5.6843418860808014870E-14, \
    2.8421709430404007435E-14, \
    1.4210854715202003717E-14, \
    7.1054273576010018587E-15, \
    3.5527136788005009294E-15, \
    1.7763568394002504647E-15, \
    8.8817841970012523234E-16, \
    4.4408920985006261617E-16, \
    2.2204460492503130808E-16, \
    1.1102230246251565404E-16, \
    5.5511151231257827021E-17, \
    2.7755575615628913511E-17, \
    1.3877787807814456755E-17, \
    6.9388939039072283776E-18, \
    3.4694469519536141888E-18, \
    1.7347234759768070944E-18 ] )

  x1 = x
  y1 = y
#
#  Account for signs.
#
  if ( x1 < 0.0 and y1 < 0.0 ):
    x1 = - x1
    y1 = - y1

  if ( x1 < 0.0 ):
    x1 = - x1
    sign_factor = -1.0
  elif ( y1 < 0.0 ):
    y1 = -y1
    sign_factor = -1.0
  else:
    sign_factor = +1.0

  theta = 0.0
  poweroftwo = 1.0

  for j in range ( 0, n ):

    if ( y1 <= 0.0 ):
      sigma = +1.0
    else:
      sigma = -1.0

    if ( j < angles.size ):
      angle = angles[j]
    else:
      angle = angle / 2.0

    x2 =                      x1 - sigma * poweroftwo * y1
    y2 = sigma * poweroftwo * x1 +                      y1
    
    theta = theta - sigma * angle

    x1 = x2
    y1 = y2

    poweroftwo = poweroftwo / 2.0

  theta = sign_factor * theta

  return theta

def arctan_cordic_test ( ):

#*****************************************************************************80
#
## ARCTAN_CORDIC_TEST demonstrates the use of ARCTAN_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2007
#
#  Author:
#
#    John Burkardt
#
  seed = 123456789

  print ( '' )
  print ( 'ARCTAN_CORDIC_TEST:' )
  print ( '  ARCTAN_CORDIC computes the arctangent of Y/X' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      X      Y    N       ArcTan(Y/X) ArcTan(Y/X)      Difference' )
  print ( '                          Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, z, a1 = arctan_values ( n_data )

    if ( n_data == 0 ):
      break

    r, seed = r8_uniform_01 ( seed )

    x = r
    y = r * z

    s, seed = r8_uniform_01 ( seed )

    if ( s < 0.5 ):
      x = - x
      y = - y

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      a2 = arctan_cordic ( x, y, n )
      d = a1 - a2

      print ( '  %12f  %12f  %4d  %16.8f  %16.8f  %9e' % ( x, y, n, a1, a2, d ) )

  return
  
def arctan_values_test ( ):

#*****************************************************************************80
#
## ARCTAN_VALUES_TEST tests ARCTAN VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCTAN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCTAN_VALUES stores values of' )
  print ( '  the arc tangent function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arctan_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCTAN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def cbrt_cordic ( x, n ):

#*****************************************************************************80
#
## CBRT_CORDIC returns the cube root of a value using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose cube root is desired.
#
#    Input, integer N, the number of iterations to take.
#    This is essentially the number of binary digits of accuracy.
#
#    Output, real Y, the approximate cube root of X.
#
  x_mag = abs ( x )

  if ( x == 0.0 ):
    y = 0.0
    return y

  if ( x_mag == 1.0 ):
    y = x
    return y

  poweroftwo = 1.0

  if ( x_mag < 1.0 ):

    while ( x_mag <= poweroftwo * poweroftwo * poweroftwo ):
      poweroftwo = poweroftwo / 2.0

    y = poweroftwo

  elif ( 1.0 < x_mag ):

    while ( poweroftwo * poweroftwo * poweroftwo <= x_mag ):
      poweroftwo = 2.0 * poweroftwo

    y = poweroftwo / 2.0


  for i in range ( 0, n ):
    poweroftwo = poweroftwo / 2.0
    if ( ( y + poweroftwo ) * ( y + poweroftwo ) * ( y + poweroftwo ) <= x_mag ):
      y = y + poweroftwo

  if ( x < 0.0 ):
    y = - y

  return y

def cbrt_cordic_test ( ):

#*****************************************************************************80
#
## CBRT_CORDIC_TEST demonstrates the use of CBRT_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'CBRT_CORDIC_TEST:' )
  print ( '  CBRT_CORDIC computes the cube root ' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      X    N        Cbrt(X)     Cbrt(X)          Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, theta, t1 = cbrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      t2 = cbrt_cordic ( theta, n )
      d = t1 - t2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( theta, n, t1, t2, d ) )

  return

def cbrt_values ( n_data ):

#*****************************************************************************80
#
## CBRT_VALUES returns some values of the cube root function.
#
#  Discussion:
#
#    CBRT(X) = real number Y such that Y * Y * Y = X.
#
#    In Mathematica, the function can be evaluated by:
#
#      Sign[x] * ( Abs[x] )^(1/3)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  fx_vec = np.array ( ( \
    0.0000000000000000E+00, \
   -0.0020082988563383484484E+00, \
    0.44814047465571647087E+00, \
   -0.46415888336127788924E+00, \
    0.73680629972807732116E+00, \
   -1.0000000000000000000E+00, \
    1.2599210498948731648E+00, \
   -1.4422495703074083823E+00, \
    1.4645918875615232630E+00, \
   -2.6684016487219448673E+00, \
    3.0723168256858472933E+00, \
   -4.1408177494228532500E+00, \
    4.5947008922070398061E+00, \
   -497.93385921817447440E+00 ) )

  x_vec = np.array ( ( \
     0.0000000000000000E+00, \
    -0.8100000073710001E-08, \
     0.9000000000000000E-01, \
    -0.1000000000000000E+00, \
     0.4000000000000000E+00, \
    -0.1000000000000000E+01, \
     0.2000000000000000E+01, \
    -0.3000000000000000E+01, \
     0.3141592653589793E+01, \
    -0.1900000000000000E+02, \
     0.2900000000000000E+02, \
    -0.7100000000000000E+02, \
     0.9700000000000000E+02, \
    -0.1234567890000000E+09 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def cbrt_values_test ( ):

#*****************************************************************************80
#
## CBRT_VALUES_TEST demonstrates the use of CBRT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CBRT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CBRT_VALUES stores values of the cube root function.' )
  print ( '' )
  print ( '      X         CBRT(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cbrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CBRT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def cos_cordic_test ( ):

#*****************************************************************************80
#
## COS_CORDIC_TEST demonstrates the use of COSSIN_CORDIC for the cosine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'COS_CORDIC_TEST:' )
  print ( '  COSSIN_CORDIC computes the cosine and sine of an angle' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      A    N           Cos(A)     Cos(A)      Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, a, c1 = cos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      v = cossin_cordic ( a, n )
      c2 = v[0]
      d = c1 - c2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( a, n, c1, c2, d ) )

  return

def cos_values ( n_data ):

#*****************************************************************************80
#
## COS_VALUES returns some values of the cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cos[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 13

  fx_vec = np.array ( ( \
     1.0000000000000000000, \
     0.96592582628906828675, \
     0.87758256189037271612, \
     0.86602540378443864676, \
     0.70710678118654752440, \
     0.54030230586813971740, \
     0.50000000000000000000, \
     0.00000000000000000000, \
    -0.41614683654714238700, \
    -0.98999249660044545727, \
    -1.0000000000000000000, \
    -0.65364362086361191464, \
     0.28366218546322626447 ))

  x_vec = np.array ( ( \
    0.0000000000000000000, \
    0.26179938779914943654, \
    0.50000000000000000000, \
    0.52359877559829887308, \
    0.78539816339744830962, \
    1.0000000000000000000, \
    1.0471975511965977462, \
    1.5707963267948966192, \
    2.0000000000000000000, \
    3.0000000000000000000, \
    3.1415926535897932385, \
    4.0000000000000000000, \
    5.0000000000000000000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def cos_values_test ( ):

#*****************************************************************************80
#
## COS_VALUES_TEST demonstrates the use of COS_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COS_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COS_VALUES stores values of the cosine function.' )
  print ( '' )
  print ( '      X         COS(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COS_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def cossin_cordic ( beta, n ):

#*****************************************************************************80
#
## COSSIN_CORDIC returns the sine and cosine using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    Based on MATLAB code in a Wikipedia article.
#
#    Modifications by John Burkardt
#
#  Parameters:
#
#    Input, real BETA, the angle (in radians).
#
#    Input, integer N, the number of iterations to take.
#    A value of 10 is low.  Good accuracy is achieved with 20 or more
#    iterations.
#
#    Output, real V(2), the cosine and sine of the angle.
#
#  Local Parameters:
#
#    Local, real ANGLES(60) = arctan ( (1/2)^(0:59) )
#
#    Local, real KPROD(33), KPROD(j) = product ( 0 <= i <= j ) K(i),
#    K(i) = 1 / sqrt ( 1 + (1/2)^(2i) ).
#
  import numpy as np
  
  angles = np.array ( [ \
    7.8539816339744830962E-01, \
    4.6364760900080611621E-01, \
    2.4497866312686415417E-01, \
    1.2435499454676143503E-01, \
    6.2418809995957348474E-02, \
    3.1239833430268276254E-02, \
    1.5623728620476830803E-02, \
    7.8123410601011112965E-03, \
    3.9062301319669718276E-03, \
    1.9531225164788186851E-03, \
    9.7656218955931943040E-04, \
    4.8828121119489827547E-04, \
    2.4414062014936176402E-04, \
    1.2207031189367020424E-04, \
    6.1035156174208775022E-05, \
    3.0517578115526096862E-05, \
    1.5258789061315762107E-05, \
    7.6293945311019702634E-06, \
    3.8146972656064962829E-06, \
    1.9073486328101870354E-06, \
    9.5367431640596087942E-07, \
    4.7683715820308885993E-07, \
    2.3841857910155798249E-07, \
    1.1920928955078068531E-07, \
    5.9604644775390554414E-08, \
    2.9802322387695303677E-08, \
    1.4901161193847655147E-08, \
    7.4505805969238279871E-09, \
    3.7252902984619140453E-09, \
    1.8626451492309570291E-09, \
    9.3132257461547851536E-10, \
    4.6566128730773925778E-10, \
    2.3283064365386962890E-10, \
    1.1641532182693481445E-10, \
    5.8207660913467407226E-11, \
    2.9103830456733703613E-11, \
    1.4551915228366851807E-11, \
    7.2759576141834259033E-12, \
    3.6379788070917129517E-12, \
    1.8189894035458564758E-12, \
    9.0949470177292823792E-13, \
    4.5474735088646411896E-13, \
    2.2737367544323205948E-13, \
    1.1368683772161602974E-13, \
    5.6843418860808014870E-14, \
    2.8421709430404007435E-14, \
    1.4210854715202003717E-14, \
    7.1054273576010018587E-15, \
    3.5527136788005009294E-15, \
    1.7763568394002504647E-15, \
    8.8817841970012523234E-16, \
    4.4408920985006261617E-16, \
    2.2204460492503130808E-16, \
    1.1102230246251565404E-16, \
    5.5511151231257827021E-17, \
    2.7755575615628913511E-17, \
    1.3877787807814456755E-17, \
    6.9388939039072283776E-18, \
    3.4694469519536141888E-18, \
    1.7347234759768070944E-18 ] )

  kprod = np.array ( [ \
    0.70710678118654752440, \
    0.63245553203367586640, \
    0.61357199107789634961, \
    0.60883391251775242102, \
    0.60764825625616820093, \
    0.60735177014129595905, \
    0.60727764409352599905, \
    0.60725911229889273006, \
    0.60725447933256232972, \
    0.60725332108987516334, \
    0.60725303152913433540, \
    0.60725295913894481363, \
    0.60725294104139716351, \
    0.60725293651701023413, \
    0.60725293538591350073, \
    0.60725293510313931731, \
    0.60725293503244577146, \
    0.60725293501477238499, \
    0.60725293501035403837, \
    0.60725293500924945172, \
    0.60725293500897330506, \
    0.60725293500890426839, \
    0.60725293500888700922, \
    0.60725293500888269443, \
    0.60725293500888161574, \
    0.60725293500888134606, \
    0.60725293500888127864, \
    0.60725293500888126179, \
    0.60725293500888125757, \
    0.60725293500888125652, \
    0.60725293500888125626, \
    0.60725293500888125619, \
    0.60725293500888125617 ] )
#
#  Shift angle to interval [-pi,pi].
#
  theta = angle_shift ( beta, - np.pi )
#
#  Shift angle to interval [-pi/2,pi/2] and account for signs.
#
  if ( theta < - 0.5 * np.pi ):
    theta = theta + np.pi
    sign_factor = -1.0
  elif ( 0.5 * np.pi < theta ):
    theta = theta - np.pi
    sign_factor = -1.0
  else:
    sign_factor = +1.0

  v = np.array ( [ 1.0, 0.0 ] )
  poweroftwo = 1.0
  angle = angles[0]

  for j in range ( 0, n ):

    if ( theta < 0.0 ):
      sigma = -1.0
    else:
      sigma = 1.0

    factor = sigma * poweroftwo

    r = np.array ( [ \
      [ 1.0,   -factor ], \
      [ factor, 1.0    ] ] )

    v = np.dot ( r, v )
#
#  Update the remaining angle.
#
    theta = theta - sigma * angle

    poweroftwo = poweroftwo / 2.0
#
#  Update the angle from table, or eventually by just dividing by two.
#
    if ( angles.size <= ( j + 1 ) ):
      angle = angle / 2.0
    else:
      angle = angles[j+1]
#
#  Adjust length of output vector to be [cos(beta), sin(beta)]:
#
#  KPROD is essentially constant after a certain point, so if N is
#  large, just take the last available value.
#
  if ( 0 < n ):
    v = v * kprod [ min ( n, kprod.size ) - 1 ]
#
#  Adjust for possible sign change because angle was originally
#  not in quadrant 1 or 4.
#
  v = sign_factor * v

  return v

def exp_values ( n_data ):

#*****************************************************************************80
#
## EXP_VALUES returns some values of the exponential function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Exp[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 24

  fx_vec = np.array ( (
    0.000045399929762484851536E+00, \
    0.0067379469990854670966E+00, \
    0.36787944117144232160E+00, \
    1.0000000000000000000E+00, \
    1.0000000100000000500E+00, \
    1.0001000050001666708E+00, \
    1.0010005001667083417E+00, \
    1.0100501670841680575E+00, \
    1.1051709180756476248E+00, \
    1.2214027581601698339E+00, \
    1.3498588075760031040E+00, \
    1.4918246976412703178E+00, \
    1.6487212707001281468E+00, \
    1.8221188003905089749E+00, \
    2.0137527074704765216E+00, \
    2.2255409284924676046E+00, \
    2.4596031111569496638E+00, \
    2.7182818284590452354E+00, \
    7.3890560989306502272E+00, \
    23.140692632779269006E+00, \
     148.41315910257660342E+00, \
    22026.465794806716517E+00, \
    4.8516519540979027797E+08, \
    2.3538526683701998541E+17 ))

  x_vec = np.array ( (
     -10.0E+00, \
      -5.0E+00, \
      -1.0E+00, \
       0.0E+00, \
       0.00000001E+00, \
       0.0001E+00, \
       0.001E+00, \
       0.01E+00, \
       0.1E+00, \
       0.2E+00, \
       0.3E+00, \
       0.4E+00, \
       0.5E+00, \
       0.6E+00, \
       0.7E+00, \
       0.8E+00, \
       0.9E+00, \
       1.0E+00, \
       2.0E+00, \
       3.1415926535897932385E+00, \
       5.0E+00, \
      10.0E+00, \
      20.0E+00, \
      40.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def exp_cordic ( x, n ):

#*****************************************************************************80
#
## EXP_CORDIC evaluates the exponential function using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frederick Ruckdeschel,
#    BASIC Scientific Subroutines,
#    Volume II,
#    McGraw-Hill, 1980,
#    ISBN: 0-07-054202-3,
#    LC: QA76.95.R82.
#
#    Pitts Jarvis,
#    Implementing CORDIC Algorithms,
#    Dr Dobb's Journal,
#    October 1990.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Input, integer N, the number of steps to take.
#
#    Output, real FX, the exponential of X.
#
#  Local Parameters:
#
#    Local, real A(1:25) = exp ( (1/2)^(1:25) )
#
  import numpy as np
  
  a_length = 25

  a = np.array ( [ \
    1.648721270700128, \
    1.284025416687742, \
    1.133148453066826, \
    1.064494458917859, \
    1.031743407499103, \
    1.015747708586686, \
    1.007843097206488, \
    1.003913889338348, \
    1.001955033591003, \
    1.000977039492417, \
    1.000488400478694, \
    1.000244170429748, \
    1.000122077763384, \
    1.000061037018933, \
    1.000030518043791, \
    1.0000152589054785, \
    1.0000076294236351, \
    1.0000038147045416, \
    1.0000019073504518, \
    1.0000009536747712, \
    1.0000004768372719, \
    1.0000002384186075, \
    1.0000001192092967, \
    1.0000000596046466, \
    1.0000000298023228 ] )
    
  e = 2.718281828459045

  x_int = int ( np.floor ( x ) )
#
#  Determine the weights.
#
  poweroftwo = 0.5
  z = x - x_int
  w = np.zeros ( n )
  
  for i in range ( 0, n ):
    if ( poweroftwo < z ):
      w[i] = 1.0
      z = z - poweroftwo
    poweroftwo = poweroftwo / 2.0
#
#  Calculate products.
#
  fx = 1.0

  for i in range ( 0, n ):

    if ( i < a.size ):
      ai = a[i]
    else:
      ai = 1.0 + ( ai - 1.0 ) / 2.0

    if ( 0.0 < w[i] ):
      fx = fx * ai
#
#  Perform residual multiplication.
#
  fx = fx             \
    * ( 1.0 + z       \
    * ( 1.0 + z / 2.0 \
    * ( 1.0 + z / 3.0 \
    * ( 1.0 + z / 4.0 ))))
#
#  Account for factor EXP(X_INT).
#
  if ( x_int < 0 ):

    for i in range ( 0, - x_int ):
      fx = fx / e

  else:

    for i in range ( 0, x_int ):
      fx = fx * e

  return fx

def exp_cordic_test ( ):

#*****************************************************************************80
#
## EXP_CORDIC_TEST demonstrates the use of EXP_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'EXP_CORDIC_TEST:' )
  print ( '  EXP_CORDIC computes the exponential function' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      X    N         Exp(X)      Exp(X)          Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, theta, t1 = exp_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      t2 = exp_cordic ( theta, n )
      d = t1 - t2

      print ( '  %12f  %4d  %16.8e  %16.8e  %9e' % ( theta, n, t1, t2, d ) )

  return

def exp_values_test ( ):

#*****************************************************************************80
#
## EXP_VALUES_TEST demonstrates the use of EXP_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EXP_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXP_VALUES stores values of the exponential function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = exp_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXP_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def log_values ( n_data ):

#*****************************************************************************80
#
## LOG_VALUES returns some values of the logarithm function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -11.512925464970228420E+00, \
     -4.6051701859880913680E+00, \
     -2.3025850929940456840E+00, \
     -1.6094379124341003746E+00, \
     -1.2039728043259359926E+00, \
     -0.91629073187415506518E+00, \
     -0.69314718055994530942E+00, \
     -0.51082562376599068321E+00, \
     -0.35667494393873237891E+00, \
     -0.22314355131420975577E+00, \
     -0.10536051565782630123E+00, \
      0.00000000000000000000E+00, \
      0.69314718055994530942E+00, \
      1.0986122886681096914E+00, \
      1.1447298858494001741E+00, \
      1.6094379124341003746E+00, \
      2.3025850929940456840E+00, \
      2.9957322735539909934E+00, \
      4.6051701859880913680E+00, \
      18.631401766168018033E+00 ))

  x_vec = np.array ( ( \
   1.0E-05,  \
   1.0E-02,  \
   0.1,  \
   0.2,  \
   0.3,  \
   0.4,  \
   0.5,  \
   0.6,  \
   0.7,  \
   0.8,  \
   0.9,  \
   1.0,  \
   2.0,  \
   3.0,  \
   3.1415926535897932385,  \
   5.0,  \
   10.0,  \
   20.0, \
   100.0, \
   123456789.0 ))

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

def log_cordic ( x, n ):

#*****************************************************************************80
#
## LOG_CORDIC evaluates the natural logarithm function using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frederick Ruckdeschel,
#    BASIC Scientific Subroutines,
#    Volume II,
#    McGraw-Hill, 1980,
#    ISBN: 0-07-054202-3,
#    LC: QA76.95.R82.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Input, integer N, the number of steps to take.
#
#    Output, real FX, the logarithm of X.
#
#  Local Parameters:
#
#    Local, real A(1:25) = exp ( (1/2)^(1:25) )
#
  import numpy as np
  from sys import exit
  
  a_length = 25

  a = np.array ( [ \
    1.648721270700128, \
    1.284025416687742, \
    1.133148453066826, \
    1.064494458917859, \
    1.031743407499103, \
    1.015747708586686, \
    1.007843097206488, \
    1.003913889338348, \
    1.001955033591003, \
    1.000977039492417, \
    1.000488400478694, \
    1.000244170429748, \
    1.000122077763384, \
    1.000061037018933, \
    1.000030518043791, \
    1.0000152589054785, \
    1.0000076294236351, \
    1.0000038147045416, \
    1.0000019073504518, \
    1.0000009536747712, \
    1.0000004768372719, \
    1.0000002384186075, \
    1.0000001192092967, \
    1.0000000596046466, \
    1.0000000298023228 ] )
    
  e = 2.718281828459045

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'LOG_CORDIC - Fatal error!' )
    print ( '  Input argument X <= 0.0' )
    exit ( 'LOG_CORDIC - Fatal error!' )

  k = 0

  while ( e <= x ):
    k = k + 1
    x = x / e

  while ( x < 1.0 ):
    k = k - 1
    x = x * e
#
#  Determine the weights.
#
  w = np.zeros ( n )
  
  for i in range ( 0, n ):

    if ( i < a_length ):
      ai = a[i]
    else:
      ai = 1.0 + ( ai - 1.0 ) / 2.0

    if ( ai < x ):
      w[i] = 1.0
      x = x / ai
      
  x = x - 1.0
  x = x \
    * ( 1.0 - ( x / 2.0 ) \
    * ( 1.0 + ( x / 3.0 ) \
    * ( 1.0 -   x / 4.0 )))
#
#  Assemble.
#
  poweroftwo = 0.5
  
  for i in range ( 0, n ):
    x = x + w[i] * poweroftwo
    poweroftwo = poweroftwo / 2.0

  fx = k + x

  return fx

def log_cordic_test ( ):

#*****************************************************************************80
#
## LOG_CORDIC_TEST demonstrates the use of LOG_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'LOG_CORDIC_TEST:' )
  print ( '  LOG_CORDIC computes the natural logarithm function' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      X    N         Log(X)      Log(X)          Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, theta, t1 = log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      t2 = log_cordic ( theta, n )
      d = t1 - t2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( theta, n, t1, t2, d ) )

  return

def log_values_test ( ):

#*****************************************************************************80
#
## LOG_VALUES_TEST demonstrates the use of LOG_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOG_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_VALUES stores values of the LOG function.' )
  print ( '' )
  print ( '      X         LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOG_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def multiply_cordic ( x, y ):

#*****************************************************************************80
#
## MULTIPLY_CORDIC computes Z=X*Y the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Michel Muller,
#    Elementary Functions: Algorithms and Implementation,
#    Second Edition,
#    Birkhaeuser, 2006,
#    ISBN13: 978-0-8176-4372-0,
#    LC: QA331.M866.
#
#  Parameters:
#
#    Input, real X, Y, the factors.
#
#    Output, real Z, the product.
#
  z = 0.0
#
#  Easy result if X or Y is zero.
#
  if ( x == 0.0 ):
    return z

  if ( y == 0.0 ):
    return z
#
#  X = X_SIGN * X_ABS.
#
  if ( x < 0.0 ):
    x_sign = -1.0
    x_abs = - x
  else:
    x_sign = +1.0
    x_abs = x
#
#  X = X_SIGN * X_ABS * 2^X_LOG2
#
  x_log2 = 0
  while ( 2.0 <= x_abs ):
    x_abs = x_abs / 2.0
    x_log2 = x_log2 + 1

  while ( x_abs < 1.0 ):
    x_abs = x_abs * 2.0
    x_log2 = x_log2 - 1
#
#  X*Y = X_SIGN * sum ( 0 <= i) X_ABS(i) * 2^(-i) * Y ) * 2^X_LOG2
#  where X_ABS(I) is the I-th binary digit in expansion of X_ABS.
#
  two_power = 1.0
  while ( 0.0 < x_abs ):
    if ( 1.0 <= x_abs ):
      x_abs = x_abs - 1.0
      z = z + y * two_power
    x_abs = x_abs * 2.0
    two_power = two_power / 2.0
#
#  Account for X_SIGN and X_LOG2.
#
  z = z * x_sign

  while ( 0 < x_log2 ):
    z = z * 2.0
    x_log2 = x_log2 - 1

  while ( x_log2 < 0 ):
    z = z / 2.0
    x_log2 = x_log2 + 1
 
  return z

def multiply_cordic_test ( ):

#*****************************************************************************80
#
## MULTIPLY_CORDIC_TEST tests MULTIPLY_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'MULTIPLY_CORDIC_TEST:' )
  print ( '  MULTIPLY_CORDIC computes Z = X * Y' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '        X             Y               Z                 Z' )
  print ( '                                      (X*Y)             (CORDIC)' )
  print ( '' )

  for i in range ( 0, 20 ):

    x = - 100.0 + 200.0 * np.random.rand ( )
    y = - 100.0 + 200.0 * np.random.rand ( )
    z1 = x * y
    z2 = multiply_cordic ( x, y )

    print ( '  %12f  %12f  %16.8f  %16.8f' % ( x, y, z1, z2 ) )

  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def sin_cordic_test ( ):

#*****************************************************************************80
#
## SIN_CORDIC_TEST demonstrates the use of COSSIN_CORDIC for the sine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'SIN_CORDIC_TEST:' )
  print ( '  COSSIN_CORDIC computes the cosine and sine of an angle' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      A    N           Sin(A)     Sin(A)      Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, a, s1 = sin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      v = cossin_cordic ( a, n )
      s2 = v[1]
      d = s1 - s2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( a, n, s1, s2, d ) )

  return

def sin_values ( n_data ):

#*****************************************************************************80
#
## SIN_VALUES returns some values of the sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sin[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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

  n_max = 13

  f_vec = np.array ( ( \
     0.00000000000000000000, \
     0.25881904510252076235, \
     0.47942553860420300027, \
     0.50000000000000000000, \
     0.70710678118654752440, \
     0.84147098480789650665, \
     0.86602540378443864676, \
     1.00000000000000000000, \
     0.90929742682568169540, \
     0.14112000805986722210, \
     0.00000000000000000000, \
    -0.75680249530792825137, \
    -0.95892427466313846889 ))

  x_vec = np.array ( ( \
    0.0000000000000000000, \
    0.26179938779914943654, \
    0.50000000000000000000, \
    0.52359877559829887308, \
    0.78539816339744830962, \
    1.0000000000000000000, \
    1.0471975511965977462, \
    1.5707963267948966192, \
    2.0000000000000000000, \
    3.0000000000000000000, \
    3.1415926535897932385, \
    4.0000000000000000000, \
    5.0000000000000000000  ))

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

def sin_values_test ( ):

#*****************************************************************************80
#
## SIN_VALUES_TEST demonstrates the use of SIN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SIN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIN_VALUES stores values of the SIN function.' )
  print ( '' )
  print ( '      X         SIN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def sqrt_values ( n_data ):

#*****************************************************************************80
#
## SQRT_VALUES returns some values of the square root function.
#
#  Discussion:
#
#    SQRT(X) = positive real number Y such that Y * Y = X.
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
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
#    Output real F, the value of the function.
#
  import numpy as np

  n_max = 14

  f_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.9000000040950000E-04, \
     0.3000000000000000E+00, \
     0.3162277660168379E+00, \
     0.6324555320336759E+00, \
     0.1000000000000000E+01, \
     0.1414213562373095E+01, \
     0.1732050807568877E+01, \
     0.1772453850905516E+01, \
     0.4358898943540674E+01, \
     0.5385164807134504E+01, \
     0.8426149773176359E+01, \
     0.9848857801796105E+01, \
     0.1111111106055556E+05 ) )

  x_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.8100000073710001E-08, \
     0.9000000000000000E-01, \
     0.1000000000000000E+00, \
     0.4000000000000000E+00, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3141592653589793E+01, \
     0.1900000000000000E+02, \
     0.2900000000000000E+02, \
     0.7100000000000000E+02, \
     0.9700000000000000E+02, \
     0.1234567890000000E+09 ) )

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

def sqrt_cordic ( x, n ):

#*****************************************************************************80
#
## SQRT_CORDIC returns the square root of a value using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose square root is desired.
#
#    Input, integer N, the number of iterations to take.
#    This is essentially the number of binary digits of accuracy.
#
#    Output, real Y, the approximate square root of X.
#
  from sys import exit

  if ( x < 0.0 ):
    print ( '' )
    print ( 'SQRT_CORDIC - Fatal error!' )
    print ( '  X < 0.' )
    exit ( 'SQRT_CORDIC - Fatal error!' )

  if ( x == 0.0 ):
    y = 0.0
    return y

  if ( x == 1.0 ):
    y = 1.0
    return y

  poweroftwo = 1.0

  if ( x < 1.0 ):

    while ( x <= poweroftwo * poweroftwo ):
      poweroftwo = poweroftwo / 2.0

    y = poweroftwo

  elif ( 1.0 < x ):

    while ( poweroftwo * poweroftwo <= x ):
      poweroftwo = 2.0 * poweroftwo

    y = poweroftwo / 2.0

  for i in range ( 0, n ):
    poweroftwo = poweroftwo / 2.0
    if ( ( y + poweroftwo ) * ( y + poweroftwo ) <= x ):
      y = y + poweroftwo

  return y

def sqrt_cordic_test ( ):

#*****************************************************************************80
#
## SQRT_CORDIC_TEST demonstrates the use of SQRT_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'SQRT_CORDIC_TEST:' )
  print ( '  SQRT_CORDIC computes the square root ' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '      X    N        Sqrt(X)     Sqrt(X)          Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, theta, t1 = sqrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      t2 = sqrt_cordic ( theta, n )
      d = t1 - t2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( theta, n, t1, t2, d ) )

  return

def sqrt_values_test ( ):

#*****************************************************************************80
#
## SQRT_VALUES_TEST demonstrates the use of SQRT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SQRT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SQRT_VALUES stores values of the SQRT function.' )
  print ( '' )
  print ( '      X         SQRT(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sqrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SQRT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def tan_values ( n_data ):

#*****************************************************************************80
#
## TAN_VALUES returns some values of the tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Tan[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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

  n_max = 15

  f_vec = np.array ( ( \
     0.00000000000000000000, \
     0.26794919243112270647, \
     0.54630248984379051326, \
     0.57735026918962576451, \
     1.0000000000000000000, \
     1.5574077246549022305, \
     1.7320508075688772935, \
     3.7320508075688772935, \
     7.5957541127251504405, \
    15.257051688265539110, \
    -2.1850398632615189916, \
    -0.14254654307427780530, \
     0.0000000000000000000, \
     1.1578212823495775831, \
    -3.3805150062465856370 ))

  x_vec = np.array ( ( \
    0.00000000000000000000, \
    0.26179938779914943654, \
    0.50000000000000000000, \
    0.52359877559829887308, \
    0.78539816339744830962, \
    1.0000000000000000000, \
    1.0471975511965977462, \
    1.3089969389957471827, \
    1.4398966328953219010, \
    1.5053464798451092601, \
    2.0000000000000000000, \
    3.0000000000000000000, \
    3.1415926535897932385, \
    4.0000000000000000000, \
    5.0000000000000000000 ))

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

def tan_cordic ( beta, n ):

#*****************************************************************************80
#
## TAN_CORDIC returns the tangent of an angle using the CORDIC method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    Based on MATLAB code in a Wikipedia article.
#
#    Modifications by John Burkardt
#
#  Parameters:
#
#    Input, real BETA, the angle (in radians).
#
#    Input, integer N, the number of iterations to take.
#    A value of 10 is low.  Good accuracy is achieved with 20 or more
#    iterations.
#
#    Output, real VALUE, the tangent of the angle.
#
#  Local Parameters:
#
#    Local, real ANGLES(60) = arctan ( (1/2)^(0:59) )
#
  import numpy as np

  angles = np.array ( [ \
    7.8539816339744830962E-01, \
    4.6364760900080611621E-01, \
    2.4497866312686415417E-01, \
    1.2435499454676143503E-01, \
    6.2418809995957348474E-02, \
    3.1239833430268276254E-02, \
    1.5623728620476830803E-02, \
    7.8123410601011112965E-03, \
    3.9062301319669718276E-03, \
    1.9531225164788186851E-03, \
    9.7656218955931943040E-04, \
    4.8828121119489827547E-04, \
    2.4414062014936176402E-04, \
    1.2207031189367020424E-04, \
    6.1035156174208775022E-05, \
    3.0517578115526096862E-05, \
    1.5258789061315762107E-05, \
    7.6293945311019702634E-06, \
    3.8146972656064962829E-06, \
    1.9073486328101870354E-06, \
    9.5367431640596087942E-07, \
    4.7683715820308885993E-07, \
    2.3841857910155798249E-07, \
    1.1920928955078068531E-07, \
    5.9604644775390554414E-08, \
    2.9802322387695303677E-08, \
    1.4901161193847655147E-08, \
    7.4505805969238279871E-09, \
    3.7252902984619140453E-09, \
    1.8626451492309570291E-09, \
    9.3132257461547851536E-10, \
    4.6566128730773925778E-10, \
    2.3283064365386962890E-10, \
    1.1641532182693481445E-10, \
    5.8207660913467407226E-11, \
    2.9103830456733703613E-11, \
    1.4551915228366851807E-11, \
    7.2759576141834259033E-12, \
    3.6379788070917129517E-12, \
    1.8189894035458564758E-12, \
    9.0949470177292823792E-13, \
    4.5474735088646411896E-13, \
    2.2737367544323205948E-13, \
    1.1368683772161602974E-13, \
    5.6843418860808014870E-14, \
    2.8421709430404007435E-14, \
    1.4210854715202003717E-14, \
    7.1054273576010018587E-15, \
    3.5527136788005009294E-15, \
    1.7763568394002504647E-15, \
    8.8817841970012523234E-16, \
    4.4408920985006261617E-16, \
    2.2204460492503130808E-16, \
    1.1102230246251565404E-16, \
    5.5511151231257827021E-17, \
    2.7755575615628913511E-17, \
    1.3877787807814456755E-17, \
    6.9388939039072283776E-18, \
    3.4694469519536141888E-18, \
    1.7347234759768070944E-18 ] )
#
#  Shift angle to interval [-pi,pi].
#
  theta = angle_shift ( beta, - np.pi )
#
#  Shift angle to interval [-pi/2,pi/2] and account for signs.
#
  if ( theta < - 0.5 * np.pi ):
    theta = theta + np.pi
  elif ( 0.5 * np.pi < theta ):
    theta = theta - np.pi

  v = np.array ( [ 1.0, 0.0 ] )
  poweroftwo = 1.0
  angle = angles[0]

  for j in range ( 0, n ):

    if ( theta < 0.0 ):
      sigma = -1.0
    else:
      sigma = +1.0

    factor = sigma * poweroftwo

    r = np.array ( [ \
      [ 1.0,   -factor ], \
      [ factor, 1.0 ] ] )

    v = np.dot ( r, v )
#
#  Update the remaining angle.
#
    theta = theta - sigma * angle

    poweroftwo = poweroftwo / 2.0
#
#  Update the angle from table, or eventually by just dividing by two.
#
    if ( angles.size <= ( j + 1 ) ):
      angle = angle / 2.0
    else:
      angle = angles[j+1]

  value = v[1] / v[0]

  return value

def tan_cordic_test ( ):

#*****************************************************************************80
#
## TAN_CORDIC_TEST demonstrates the use of TAN_CORDIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'TAN_CORDIC_TEST:' )
  print ( '  TAN_CORDIC computes the tangent of an angle THETA' )
  print ( '  using the CORDIC algorithm.' )
  print ( '' )
  print ( '  THETA    N         Tan(THETA)  Tan(THETA)      Difference' )
  print ( '                     Tabulated   CORDIC' )

  n_data = 0

  while ( True ):

    n_data, theta, t1 = tan_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '' )
    
    for n in range ( 0, 30, 5 ):
        
      t2 = tan_cordic ( theta, n )
      d = t1 - t2

      print ( '  %12f  %4d  %16.8f  %16.8f  %9e' % ( theta, n, t1, t2, d ) )

  return

def tan_values_test ( ):

#*****************************************************************************80
#
## TAN_VALUES_TEST demonstrates the use of TAN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TAN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TAN_VALUES stores values of the TAN function.' )
  print ( '' )
  print ( '      X         TAN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tan_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TAN_VALUES_TEST:' )
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

def cordic_test ( ):

#*****************************************************************************80
#
## CORDIC_TEST tests the CORDIC library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 June 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CORDIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CORDIC library.' )

  angle_shift_test ( )
  arccos_cordic_test ( )
  arcsin_cordic_test ( )
  arctan_cordic_test ( )
  cbrt_cordic_test ( )
  cos_cordic_test ( )
  exp_cordic_test ( )
  log_cordic_test ( )
  multiply_cordic_test ( )
  r8_uniform_01_test ( )
  sin_cordic_test ( )
  sqrt_cordic_test ( )
  tan_cordic_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CORDIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  cordic_test ( )
  timestamp ( )
