#! /usr/bin/env python3
#
def airy_ai_prime_values ( n_data ):

#*****************************************************************************80
#
## airy_ai_prime_values() returns some values of the Airy function Ai'(x).
#
#  Discussion:
#
#    The Airy functions Ai(X) and Bi(X) are a pair of linearly independent
#    solutions of the differential equation:
#
#      W'' - X * W = 0
#
#    In Mathematica, the function can be evaluated by:
#
#      AiryAiPrime[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2004
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real AIP, the derivative of the Airy AI function.
#
  import numpy as np

  n_max = 11

  fx_vec = np.array ( ( \
     -0.2588194037928068E+00, \
     -0.2571304219075862E+00, \
     -0.2524054702856195E+00, \
     -0.2451463642190548E+00, \
     -0.2358320344192082E+00, \
     -0.2249105326646839E+00, \
     -0.2127932593891585E+00, \
     -0.1998511915822805E+00, \
     -0.1864128638072717E+00, \
     -0.1727638434616347E+00, \
     -0.1591474412967932E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data =n_data + 1

  return n_data, x, fx

def airy_ai_prime_values_test ( ):

#*****************************************************************************80
#
## airy_ai_prime_values_test() tests airy_ai_prime_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'airy_ai_prime_values_test():' )
  print ( '  airy_ai_prime_values() stores values of' )
  print ( '  the derivative of the Airy Ai function.' )
  print ( '' )
  print ( '      X           FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = airy_ai_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def airy_ai_values ( n_data ):

#*****************************************************************************80
#
## airy_ai_values() returns some values of the Airy Ai(x) function.
#
#  Discussion:
#
#    The Airy functions Ai(X) and Bi(X) are a pair of linearly independent
#    solutions of the differential equation:
#
#      W'' - X * W = 0
#
#    In Mathematica, the function can be evaluated by:
#
#      AiryAi[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2004
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real AI, the value of the Airy AI function.
#
  import numpy as np

  n_max = 11

  ai_vec = np.array ( ( \
     0.3550280538878172E+00, \
     0.3292031299435381E+00, \
     0.3037031542863820E+00, \
     0.2788064819550049E+00, \
     0.2547423542956763E+00, \
     0.2316936064808335E+00, \
     0.2098000616663795E+00, \
     0.1891624003981501E+00, \
     0.1698463174443649E+00, \
     0.1518868036405444E+00, \
     0.1352924163128814E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    ai = 0.0
  else:
    x = x_vec[n_data]
    ai = ai_vec[n_data]
    n_data =n_data + 1

  return n_data, x, ai

def airy_ai_values_test ( ):

#*****************************************************************************80
#
## airy_ai_values_test() tests airy_ai_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2007
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'airy_ai_values_test():' )
  print ( '  airy_ai_values() stores values of' )
  print ( '  the Airy function Ai(x).' )
  print ( '' )
  print ( '      X           Ai(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, ai = airy_ai_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, ai ) )

  return

def airy_bi_prime_values ( n_data ):

#*****************************************************************************80
#
## airy_bi_prime_values() returns some values of the Airy function Bi'(x).
#
#  Discussion:
#
#    The Airy functions Ai(X) and Bi(X) are a pair of linearly independent
#    solutions of the differential equation:
#
#      W'' - X * W = 0
#
#    In Mathematica, the function can be evaluated by:
#
#      AiryBiPrime[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the derivative of the Airy BI function.
#
  import numpy as np

  n_max = 11

  fx_vec = np.array ( ( \
     0.4482883573538264E+00, \
     0.4515126311496465E+00, \
     0.4617892843621509E+00, \
     0.4800490287524480E+00, \
     0.5072816760506224E+00, \
     0.5445725641405923E+00, \
     0.5931444786342857E+00, \
     0.6544059191721400E+00, \
     0.7300069016152518E+00, \
     0.8219038903072090E+00, \
     0.9324359333927756E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data =n_data + 1

  return n_data, x, fx

def airy_bi_prime_values_test ( ):

#*****************************************************************************80
#
## airy_bi_prime_values_test() tests airy_bi_prime_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'airy_bi_prime_values_test():' )
  print ( '  airy_bi_prime_values() stores values of' )
  print ( '  the derivative of the Airy Bi function.' )
  print ( '' )
  print ( '      X           FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = airy_bi_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def airy_bi_values ( n_data ):

#*****************************************************************************80
#
## airy_bi_values() returns some values of the Airy Bi(x) function.
#
#  Discussion:
#
#    The Airy functions Ai(X) and Bi(X) are a pair of linearly independent
#    solutions of the differential equation:
#
#      W'' - X * W = 0
#
#    In Mathematica, the function can be evaluated by:
#
#      AiryBi[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the Airy BI function.
#
  import numpy as np

  n_max = 11

  fx_vec = np.array ( ( \
     0.6149266274460007E+00, \
     0.6598616901941892E+00, \
     0.7054642029186612E+00, \
     0.7524855850873156E+00, \
     0.8017730000135972E+00, \
     0.8542770431031555E+00, \
     0.9110633416949405E+00, \
     0.9733286558781659E+00, \
     0.1042422171231561E+01, \
     0.1119872813134447E+01, \
     0.1207423594952871E+01 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00 ) )

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

def airy_bi_values_test ( ):

#*****************************************************************************80
#
## airy_bi_values_test() tests airy_bi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'airy_bi_values_test():' )
  print ( '  airy_bi_values() stores values of' )
  print ( '  the Airy function Bi(x).' )
  print ( '' )
  print ( '      X           Bi(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, ai = airy_bi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, ai ) )

  return

def arccosh_values ( n_data ):

#*****************************************************************************80
#
## arccosh_values() returns some values of the hyperbolic arc cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      arccosh[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 15

  fx_vec = np.array ( ( \
    0.0000000000000000000, \
    0.14130376948564857735, \
    0.44356825438511518913, \
    0.62236250371477866781, \
    0.75643291085695958624, \
    0.86701472649056510395, \
    0.96242365011920689500, \
    1.3169578969248167086, \
    1.7627471740390860505, \
    1.8115262724608531070, \
    2.0634370688955605467, \
    2.2924316695611776878, \
    2.9932228461263808979, \
    5.2982923656104845907, \
    7.6009022095419886114 ) )

  x_vec = np.array ( ( \
       1.0, \
       1.01, \
       1.1, \
       1.2, \
       1.3, \
       1.4, \
       1.5, \
       2.0, \
       3.0, \
       3.1415926535897932385, \
       4.0, \
       5.0, \
      10.0, \
     100.0, \
    1000.0 ) )

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

def arccosh_values_test ( ):

#*****************************************************************************80
#
## arccosh_values_test() tests arccosh_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'arccosh_values_test():' )
  print ( '  arccosh_values() stores values of' )
  print ( '  the hyperbolic arc cosine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arccosh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def arccos_values ( n_data ):

#*****************************************************************************80
#
## arccos_values() returns some values of the arc cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcCos[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
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
## arccos_values_test() tests arccos_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'arccos_values_test():' )
  print ( '  arccos_values() stores values of' )
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

  return

def arcsinh_values ( n_data ):

#*****************************************************************************80
#
## arcsinh_values() returns some values of the hyperbolic arc sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      arcsinh[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2007
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
    -2.3124383412727526203, \
    -0.88137358701954302523, \
     0.00000000000000000000, \
     0.099834078899207563327, \
     0.19869011034924140647, \
     0.29567304756342243910, \
     0.39003531977071527608, \
     0.48121182505960344750, \
     0.56882489873224753010, \
     0.65266656608235578681, \
     0.73266825604541086415, \
     0.80886693565278246251, \
     0.88137358701954302523, \
     1.4436354751788103425, \
     1.8184464592320668235, \
     2.0947125472611012942, \
     2.3124383412727526203, \
     2.9982229502979697388, \
     5.2983423656105887574, \
     7.6009027095419886115 ) )

  x_vec = np.array ( ( \
       -5.0, \
       -1.0, \
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
        1.0, \
        2.0, \
        3.0, \
        4.0, \
        5.0, \
       10.0, \
      100.0, \
     1000.0 ) )

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

def arcsinh_values_test ( ):

#*****************************************************************************80
#
## arcsinh_values_test() tests arcsinh_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'arcsinh_values_test():' )
  print ( '  arcsinh_values() stores values of' )
  print ( '  the hyperbolic arc sine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arcsinh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def arcsin_values ( n_data ):

#*****************************************************************************80
#
## arcsin_values() returns some values of the arc sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      arcsin[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
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
## arcsin_values_test() tests arcsin_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'arcsin_values_test():' )
  print ( '  arcsin_values() stores values of' )
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

  return

def arctan2_values ( n_data ):

#*****************************************************************************80
#
## arctan2_values(): arc tangent function of two arguments.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      arctan[x,y]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, Y, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 19

  f_vec = np.array ( ( \
   -1.5707963267948966192, \
   -1.0471975511965977462, \
   -0.52359877559829887308, \
    0.00000000000000000000, \
    0.52359877559829887308, \
    1.0471975511965977462, \
    1.5707963267948966192, \
    2.0943951023931954923, \
    2.6179938779914943654, \
    3.1415926535897932385, \
   -2.6179938779914943654, \
   -2.0943951023931954923, \
   -1.5707963267948966192, \
   -1.0471975511965977462, \
   -0.52359877559829887308, \
    0.00000000000000000000, \
    0.52359877559829887308, \
    1.0471975511965977462, \
    1.5707963267948966192 ) )

  x_vec = np.array ( ( \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000, \
    0.86602540378443864676, \
    0.50000000000000000000, \
    0.00000000000000000000, \
   -0.50000000000000000000, \
   -0.86602540378443864676, \
   -1.00000000000000000000, \
   -0.86602540378443864676, \
   -0.50000000000000000000, \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000, \
    0.86602540378443864676, \
    0.50000000000000000000, \
    0.00000000000000000000 ) )

  y_vec = np.array ( ( \
   -1.00000000000000000000, \
   -0.86602540378443864676, \
   -0.50000000000000000000, \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000, \
    0.86602540378443864676, \
    0.50000000000000000000, \
    0.00000000000000000000, \
   -0.50000000000000000000, \
   -0.86602540378443864676, \
   -1.00000000000000000000, \
   -0.86602540378443864676, \
   -0.50000000000000000000, \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, f

def arctan2_values_test ( ):

#*****************************************************************************80
#
## arctan2_values_test() tests arctan2_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'arctan2_values_test():' )
  print ( '  arctan2_values() stores values of' )
  print ( '  the arc tangent function.' )
  print ( '' )
  print ( '        X           Y               F(X,Y)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f = arctan2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( x, y, f ) )

  return

def arctanh_values ( n_data ):

#*****************************************************************************80
#
## arctanh_values() returns some values of the hyperbolic arc tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      arctanh[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 15

  fx_vec = np.array ( ( \
    -0.54930614433405484570, \
     0.00000000000000000000, \
     0.0010000003333335333335, \
     0.10033534773107558064, \
     0.20273255405408219099, \
     0.30951960420311171547, \
     0.42364893019360180686, \
     0.54930614433405484570, \
     0.69314718055994530942, \
     0.86730052769405319443, \
     1.0986122886681096914, \
     1.4722194895832202300, \
     2.6466524123622461977, \
     3.8002011672502000318, \
     7.2543286192620472067 ) )

  x_vec = np.array ( ( \
    -0.5, \
     0.0, \
     0.001, \
     0.1, \
     0.2, \
     0.3, \
     0.4, \
     0.5, \
     0.6, \
     0.7, \
     0.8, \
     0.9, \
     0.99, \
     0.999, \
     0.999999 ) )

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

def arctanh_values_test ( ):

#*****************************************************************************80
#
## arctanh_values_test() tests arctanH_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'arctanh_values_test():' )
  print ( '  arctanh_values() stores values of' )
  print ( '  the hyperbolic arc tangent function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arctanh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def arctan_values ( n_data ):

#*****************************************************************************80
#
## arctan_values() returns some values of the arc tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      arctan[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
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

def arctan_values_test ( ):

#*****************************************************************************80
#
## arctan_values_test() tests arctan_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'arctan_values_test():' )
  print ( '  arctan_values() stores values of' )
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

  return

def bessel_i0_values ( n_data ):

#*****************************************************************************80
#
## bessel_i0_values() returns some values of the I0 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function I0(Z) corresponds to N = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[0,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1010025027795146E+01, \
     0.1040401782229341E+01, \
     0.1092045364317340E+01, \
     0.1166514922869803E+01, \
     0.1266065877752008E+01, \
     0.1393725584134064E+01, \
     0.1553395099731217E+01, \
     0.1749980639738909E+01, \
     0.1989559356618051E+01, \
     0.2279585302336067E+01, \
     0.3289839144050123E+01, \
     0.4880792585865024E+01, \
     0.7378203432225480E+01, \
     0.1130192195213633E+02, \
     0.1748117185560928E+02, \
     0.2723987182360445E+02, \
     0.6723440697647798E+02, \
     0.4275641157218048E+03, \
     0.2815716628466254E+04 ) )

  x_vec = np.array ( ( \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     0.10E+01, \
     0.12E+01, \
     0.14E+01, \
     0.16E+01, \
     0.18E+01, \
     0.20E+01, \
     0.25E+01, \
     0.30E+01, \
     0.35E+01, \
     0.40E+01, \
     0.45E+01, \
     0.50E+01, \
     0.60E+01, \
     0.80E+01, \
     0.10E+02  ) )

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

def bessel_i0_values_test ( ):

#*****************************************************************************80
#
## bessel_i0_values_test() tests bessel_i0_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bessel_i0_values_test():' )
  print ( '  bessel_i0_values() stores values of the Bessel I function. of order 0.' )
  print ( '' )
  print ( '      X           I(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_i1_values ( n_data ):

#*****************************************************************************80
#
## bessel_i1_values() returns some values of the I1 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[1,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1005008340281251E+00, \
     0.2040267557335706E+00, \
     0.3137040256049221E+00, \
     0.4328648026206398E+00, \
     0.5651591039924850E+00, \
     0.7146779415526431E+00, \
     0.8860919814143274E+00, \
     0.1084810635129880E+01, \
     0.1317167230391899E+01, \
     0.1590636854637329E+01, \
     0.2516716245288698E+01, \
     0.3953370217402609E+01, \
     0.6205834922258365E+01, \
     0.9759465153704450E+01, \
     0.1538922275373592E+02, \
     0.2433564214245053E+02, \
     0.6134193677764024E+02, \
     0.3998731367825601E+03, \
     0.2670988303701255E+04 ) )

  x_vec = np.array ( ( \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     0.10E+01, \
     0.12E+01, \
     0.14E+01, \
     0.16E+01, \
     0.18E+01, \
     0.20E+01, \
     0.25E+01, \
     0.30E+01, \
     0.35E+01, \
     0.40E+01, \
     0.45E+01, \
     0.50E+01, \
     0.60E+01, \
     0.80E+01, \
     0.10E+02  ) )

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

def bessel_i1_values_test ( ):

#*****************************************************************************80
#
## bessel_i1_values_test() tests bessel_i1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bessel_i1_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bessel_i1_values stores values of the Bessel I function. of order 1.' )
  print ( '' )
  print ( '      X           I(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_j0_values ( n_data ):

#*****************************************************************************80
#
## bessel_j0_values() returns some values of the J0 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselJ[0,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2004
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  n_max = 21;

  fx_vec = [ \
 ];

  x_vec = [ \
 ];
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     -0.1775967713143383E+00, \
     -0.3971498098638474E+00, \
     -0.2600519549019334E+00, \
      0.2238907791412357E+00, \
      0.7651976865579666E+00, \
      0.1000000000000000E+01, \
      0.7651976865579666E+00, \
      0.2238907791412357E+00, \
     -0.2600519549019334E+00, \
     -0.3971498098638474E+00, \
     -0.1775967713143383E+00, \
      0.1506452572509969E+00, \
      0.3000792705195556E+00, \
      0.1716508071375539E+00, \
     -0.9033361118287613E-01, \
     -0.2459357644513483E+00, \
     -0.1711903004071961E+00, \
      0.4768931079683354E-01, \
      0.2069261023770678E+00, \
      0.1710734761104587E+00, \
     -0.1422447282678077E-01 ) )

  x_vec = np.array ( ( \
     -5.0E+00, \
     -4.0E+00, \
     -3.0E+00, \
     -2.0E+00, \
     -1.0E+00, \
      0.0E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
     11.0E+00, \
     12.0E+00, \
     13.0E+00, \
     14.0E+00, \
     15.0E+00 ) )

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

def bessel_j0_values_test ( ):

#*****************************************************************************80
#
## bessel_j0_values_test() tests bessel_j0_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_j0_values_test():' )
  print ( '  bessel_j0_values stores values of the Bessel J function. of order 0.' )
  print ( '' )
  print ( '      X           J(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_j1_values ( n_data ):

#*****************************************************************************80
#
## bessel_j1_values() returns some values of the J1 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselJ[1,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
      0.3275791375914652E+00, \
      0.6604332802354914E-01, \
     -0.3390589585259365E+00, \
     -0.5767248077568734E+00, \
     -0.4400505857449335E+00, \
      0.0000000000000000E+00, \
      0.4400505857449335E+00, \
      0.5767248077568734E+00, \
      0.3390589585259365E+00, \
     -0.6604332802354914E-01, \
     -0.3275791375914652E+00, \
     -0.2766838581275656E+00, \
     -0.4682823482345833E-02, \
      0.2346363468539146E+00, \
      0.2453117865733253E+00, \
      0.4347274616886144E-01, \
     -0.1767852989567215E+00, \
     -0.2234471044906276E+00, \
     -0.7031805212177837E-01, \
      0.1333751546987933E+00, \
      0.2051040386135228E+00 ) )

  x_vec = np.array ( ( \
     -5.0E+00, \
     -4.0E+00, \
     -3.0E+00, \
     -2.0E+00, \
     -1.0E+00, \
      0.0E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
     11.0E+00, \
     12.0E+00, \
     13.0E+00, \
     14.0E+00, \
     15.0E+00  ) )

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

def bessel_j1_values_test ( ):

#*****************************************************************************80
#
## bessel_j1_values_test() tests bessel_j1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_j1_values_test():' )
  print ( '  bessel_j1_values stores values of the Bessel J function. of order 1.' )
  print ( '' )
  print ( '      X           J(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_k0_values ( n_data ):

#*****************************************************************************80
#
## bessel_k0_values() returns some values of the K0 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function K0(Z) corresponds to N = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselK[0,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.2427069024702017E+01, \
     0.1752703855528146E+01, \
     0.1114529134524434E+01, \
     0.7775220919047293E+00, \
     0.5653471052658957E+00, \
     0.4210244382407083E+00, \
     0.3185082202865936E+00, \
     0.2436550611815419E+00, \
     0.1879547519693323E+00, \
     0.1459314004898280E+00, \
     0.1138938727495334E+00, \
     0.6234755320036619E-01, \
     0.3473950438627925E-01, \
     0.1959889717036849E-01, \
     0.1115967608585302E-01, \
     0.6399857243233975E-02, \
     0.3691098334042594E-02, \
     0.1243994328013123E-02, \
     0.1464707052228154E-03, \
     0.1778006231616765E-04 ) )

  x_vec = np.array ( ( \
      0.1E+00, \
      0.2E+00, \
      0.4E+00, \
      0.6E+00, \
      0.8E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00, \
      5.0E+00, \
      6.0E+00, \
      8.0E+00, \
     10.0E+00 ) )

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

def bessel_k0_values_test ( ):

#*****************************************************************************80
#
## bessel_k0_values_test() tests bessel_k0_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_k0_values_test():' )
  print ( '  bessel_k0_values stores values of the Bessel K function. of order 0.' )
  print ( '' )
  print ( '      X           K(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_k0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_k1_values ( n_data ):

#*****************************************************************************80
#
## bessel_k1_values() returns some values of the K1 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function K1(Z) corresponds to N = 1.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselK[1,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.9853844780870606E+01, \
     0.4775972543220472E+01, \
     0.2184354424732687E+01, \
     0.1302834939763502E+01, \
     0.8617816344721803E+00, \
     0.6019072301972346E+00, \
     0.4345923910607150E+00, \
     0.3208359022298758E+00, \
     0.2406339113576119E+00, \
     0.1826230998017470E+00, \
     0.1398658818165224E+00, \
     0.7389081634774706E-01, \
     0.4015643112819418E-01, \
     0.2223939292592383E-01, \
     0.1248349888726843E-01, \
     0.7078094908968090E-02, \
     0.4044613445452164E-02, \
     0.1343919717735509E-02, \
     0.1553692118050011E-03, \
     0.1864877345382558E-04 ) )

  x_vec = np.array ( ( \
      0.1E+00, \
      0.2E+00, \
      0.4E+00, \
      0.6E+00, \
      0.8E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00, \
      5.0E+00, \
      6.0E+00, \
      8.0E+00, \
     10.0E+00  ) )

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

def bessel_k1_values_test ( ):

#*****************************************************************************80
#
## bessel_k1_values_test() tests bessel_k1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_k1_values_test():' )
  print ( '  bessel_k1_values stores values of the Bessel K function. of order 1.' )
  print ( '' )
  print ( '      X           K(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_k1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_kx_values ( n_data ):

#*****************************************************************************80
#
## bessel_kx_values() returns some values of the Kx Bessel function.
#
#  Discussion:
#
#    This set of data considers the less common case in which the
#    index of the Bessel function Kn is actually not an integer.
#    We may suggest this case by occasionally replacing the symbol
#    "Kn" by "Kx".
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselK[n,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real NU, the order of the function.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 28

  fx_vec = np.array ( ( \
       2.294489339798475E+00, \
       0.4610685044478946E+00, \
       0.1199377719680614E+00, \
       0.06506594315400999E+00, \
       0.03602598513176459E+00, \
       0.003776613374642883E+00, \
       0.00001799347809370518E+00, \
       5.776373974707445E-10, \
       0.9221370088957891E+00, \
       0.1799066579520922E+00, \
       0.004531936049571459E+00, \
       0.00001979282590307570E+00, \
       3.486992497366216E-23, \
       3.227479531135262E+00, \
       0.3897977588961997E+00, \
       0.006495775004385758E+00, \
       0.00002393132586462789E+00, \
       3.627839645299048E-23, \
       0.7311451879202114E+00, \
       0.1567475478393932E+00, \
       0.004257389528177461E+00, \
       0.00001915541065869563E+00, \
       3.463337593569306E-23, \
       4.731184839919541E+00, \
       0.4976876225514758E+00, \
       0.007300864610941163E+00, \
       0.00002546421294106458E+00, \
       3.675275677913656E-23 ) )

  nu_vec = np.array ( ( \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    1.50E+00, \
    1.50E+00, \
    1.50E+00, \
    1.50E+00, \
    1.50E+00, \
    2.50E+00, \
    2.50E+00, \
    2.50E+00, \
    2.50E+00, \
    2.50E+00, \
    1.25E+00, \
    1.25E+00, \
    1.25E+00, \
    1.25E+00, \
    1.25E+00, \
    2.75E+00, \
    2.75E+00, \
    2.75E+00, \
    2.75E+00, \
    2.75E+00 ))

  x_vec = np.array ( ( \
      0.2E+00, \
      1.0E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      5.0E+00, \
     10.0E+00, \
     20.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    nu = 0
    x = 0.0
    fx = 0.0
  else:
    nu = nu_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, nu, x, fx

def bessel_kx_values_test ( ):

#*****************************************************************************80
#
## bessel_kx_values_test() tests bessel_kx_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_kx_values_test():' )
  print ( '  bessel_kx_values stores values of the Bessel K function. of real order NU.' )
  print ( '' )
  print ( '      NU          X           K(NU,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_kx_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( nu, x, fx ) )

  return

def bessel_y0_values ( n_data ):

#*****************************************************************************80
#
## bessel_y0_values() returns some values of the Y0 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselY[0,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
     -0.1534238651350367E+01, \
      0.8825696421567696E-01, \
      0.5103756726497451E+00, \
      0.3768500100127904E+00, \
     -0.1694073932506499E-01, \
     -0.3085176252490338E+00, \
     -0.2881946839815792E+00, \
     -0.2594974396720926E-01, \
      0.2235214893875662E+00, \
      0.2499366982850247E+00, \
      0.5567116728359939E-01, \
     -0.1688473238920795E+00, \
     -0.2252373126343614E+00, \
     -0.7820786452787591E-01, \
      0.1271925685821837E+00, \
      0.2054642960389183E+00 ) )

  x_vec = np.array ( ( \
      0.1E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
     11.0E+00, \
     12.0E+00, \
     13.0E+00, \
     14.0E+00, \
     15.0E+00  ) )

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

def bessel_y0_values_test ( ):

#*****************************************************************************80
#
## bessel_y0_values_test() tests bessel_y0_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_y0_values_test():' )
  print ( '  bessel_y0_values stores values of the Bessel Y function. of order 0.' )
  print ( '' )
  print ( '      X           Y(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_y0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def bessel_y1_values ( n_data ):

#*****************************************************************************80
#
## bessel_y1_values() returns some values of the Y1 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselY[1,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
     -0.6458951094702027E+01, \
     -0.7812128213002887E+00, \
     -0.1070324315409375E+00, \
      0.3246744247918000E+00, \
      0.3979257105571000E+00, \
      0.1478631433912268E+00, \
     -0.1750103443003983E+00, \
     -0.3026672370241849E+00, \
     -0.1580604617312475E+00, \
      0.1043145751967159E+00, \
      0.2490154242069539E+00, \
      0.1637055374149429E+00, \
     -0.5709921826089652E-01, \
     -0.2100814084206935E+00, \
     -0.1666448418561723E+00, \
      0.2107362803687351E-01 ) )

  x_vec = np.array ( ( \
      0.1E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
     11.0E+00, \
     12.0E+00, \
     13.0E+00, \
     14.0E+00, \
     15.0E+00  ) )

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

def bessel_y1_values_test ( ):

#*****************************************************************************80
#
## bessel_y1_values_test() tests bessel_y1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bessel_y1_values_test():' )
  print ( '  bessel_y1_values stores values of the Bessel Y function. of order 1.' )
  print ( '' )
  print ( '      X           Y(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_y1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )

  return

def beta_inc_values ( n_data ):

#*****************************************************************************80
#
## beta_inc_values() returns some values of the incomplete Beta function.
#
#  Discussion:
#
#    The incomplete Beta function may be written
#
#      beta_inc(A,B,X) = Integral (0 to X) T^(A-1) * (1-T)^(B-1) dT
#                      / Integral (0 to 1) T^(A-1) * (1-T)^(B-1) dT
#
#    Thus,
#
#      beta_inc(A,B,0.0) = 0.0;
#      beta_inc(A,B,1.0) = 1.0
#
#    The incomplete Beta function is also sometimes called the
#    "modified" Beta function, or the "normalized" Beta function
#    or the Beta CDF (cumulative density function).
#
#    In Mathematica, the function can be evaluated by:
#
#      BETA[X,A,B] / BETA[A,B]
#
#    The function can also be evaluated by using the Statistics package:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = BetaDistribution [ a, b ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
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
#    Karl Pearson,
#    Tables of the Incomplete Beta Function,
#    Cambridge University Press, 1968.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, the parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 45

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.5E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     30.0E+00, \
     30.0E+00, \
     40.0E+00, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.2E+01, \
      0.3E+01, \
      0.4E+01, \
      0.5E+01, \
      1.30625, \
      1.30625, \
      1.30625 ))

  b_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.0E+00, \
      0.5E+00, \
      5.0E+00, \
      5.0E+00, \
     10.0E+00, \
      5.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.2E+01, \
     0.3E+01, \
     0.4E+01, \
     0.5E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
    11.7562, \
    11.7562, \
    11.7562 ))

  f_vec = np.array ( ( \
     0.6376856085851985E-01, \
     0.2048327646991335E+00, \
     0.1000000000000000E+01, \
     0.0000000000000000E+00, \
     0.5012562893380045E-02, \
     0.5131670194948620E-01, \
     0.2928932188134525E+00, \
     0.5000000000000000E+00, \
     0.2800000000000000E-01, \
     0.1040000000000000E+00, \
     0.2160000000000000E+00, \
     0.3520000000000000E+00, \
     0.5000000000000000E+00, \
     0.6480000000000000E+00, \
     0.7840000000000000E+00, \
     0.8960000000000000E+00, \
     0.9720000000000000E+00, \
     0.4361908850559777E+00, \
     0.1516409096347099E+00, \
     0.8978271484375000E-01, \
     0.1000000000000000E+01, \
     0.5000000000000000E+00, \
     0.4598773297575791E+00, \
     0.2146816102371739E+00, \
     0.9507364826957875E+00, \
     0.5000000000000000E+00, \
     0.8979413687105918E+00, \
     0.2241297491808366E+00, \
     0.7586405487192086E+00, \
     0.7001783247477069E+00, \
     0.5131670194948620E-01, \
     0.1055728090000841E+00, \
     0.1633399734659245E+00, \
     0.2254033307585166E+00, \
     0.3600000000000000E+00, \
     0.4880000000000000E+00, \
     0.5904000000000000E+00, \
     0.6723200000000000E+00, \
     0.2160000000000000E+00, \
     0.8370000000000000E-01, \
     0.3078000000000000E-01, \
     0.1093500000000000E-01, \
     0.918884684620518, \
     0.21052977489419, \
     0.1824130512500673 ) )

  x_vec = np.array ( ( \
     0.01E+00, \
     0.10E+00, \
     1.00E+00, \
     0.00E+00, \
     0.01E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     0.50E+00, \
     0.90E+00, \
     0.50E+00, \
     1.00E+00, \
     0.50E+00, \
     0.80E+00, \
     0.60E+00, \
     0.80E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.70E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.225609, \
     0.0335568, \
     0.0295222  ) )

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

def beta_inc_values_test ( ):

#*****************************************************************************80
#
## beta_inc_values_test() tests beta_inc_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'beta_inc_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  beta_inc_values stores values of the BETA function.' )
  print ( '' )
  print ( '      A         B         X        beta_inc(A,B,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16g' % ( a, b, x, f ) )

  return

def beta_log_values ( n_data ):

#*****************************************************************************80
#
## beta_log_values() returns some values of the logarithm of the Beta function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[Beta[x]]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, Y, the arguments of the function.
#
#    real FXY, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
      0.1609437912434100E+01, \
      0.9162907318741551E+00, \
      0.5108256237659907E+00, \
      0.2231435513142098E+00, \
      0.1609437912434100E+01, \
      0.9162907318741551E+00, \
      0.0000000000000000E+00, \
     -0.1791759469228055E+01, \
     -0.3401197381662155E+01, \
     -0.4941642422609304E+01, \
     -0.6445719819385578E+01, \
     -0.3737669618283368E+01, \
     -0.5123963979403259E+01, \
     -0.6222576268071369E+01, \
     -0.7138866999945524E+01, \
     -0.7927324360309794E+01, \
     -0.9393661429103221E+01 ) )

  x_vec = np.array ( ( \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  y_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.2E+00, \
     0.4E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     7.0E+00   ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, f

def beta_log_values_test ( ):

#*****************************************************************************80
#
## beta_log_values_test() tests beta_log_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'beta_log_values_test():' )
  print ( '  beta_log_values stores values of the Log(BETA) function.' )
  print ( '' )
  print ( '      X         Y         Log(BETA(X,Y))' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f = beta_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( x, y, f ) )

  return

def beta_values ( n_data ):

#*****************************************************************************80
#
## beta_values() returns some values of the Beta function.
#
#  Discussion:
#
#    Beta(X,Y) = ( Gamma(X) * Gamma(Y) ) / Gamma(X+Y)
#
#    Both X and Y must be greater than 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      Beta[X,Y]
#
#  Properties:
#
#    Beta(X,Y) = Beta(Y,X).
#    Beta(X,Y) = Integral ( 0 <= T <= 1 ) T^(X-1) (1-T)^(Y-1) dT.
#    Beta(X,Y) = Gamma(X) * Gamma(Y) / Gamma(X+Y)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, Y, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
     0.5000000000000000E+01, \
     0.2500000000000000E+01, \
     0.1666666666666667E+01, \
     0.1250000000000000E+01, \
     0.5000000000000000E+01, \
     0.2500000000000000E+01, \
     0.1000000000000000E+01, \
     0.1666666666666667E+00, \
     0.3333333333333333E-01, \
     0.7142857142857143E-02, \
     0.1587301587301587E-02, \
     0.2380952380952381E-01, \
     0.5952380952380952E-02, \
     0.1984126984126984E-02, \
     0.7936507936507937E-03, \
     0.3607503607503608E-03, \
     0.8325008325008325E-04 ) )

  x_vec = np.array ( ( \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  y_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.2E+00, \
     0.4E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, f

def beta_values_test ( ):

#*****************************************************************************80
#
## beta_values_test() tests beta_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'beta_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  beta_values stores values of the BETA function.' )
  print ( '' )
  print ( '      X         Y         BETA(X,Y)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( x, y, f ) )

  return

def binomial_values ( n_data ):

#*****************************************************************************80
#
## binomial_values() returns some values of the binomial coefficients.
#
#  Discussion:
#
#    The formula for the binomial coefficient is
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#    In Mathematica, the function can be evaluated by:
#
#      Binomial[n,k]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer A, B, the arguments of the function.
#
#    integer F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     1,  6,  6,  6, 15, \
    15, 15, 15, 15, 15, \
    15, 25, 25, 25, 25, \
    25, 25, 25, 25, 25  ) )

  b_vec = np.array ( ( \
     0,  1,  3,  5,  1, \
     3,  5,  7,  9, 11, \
    13,  1,  3,  5,  7, \
     9, 11, 13, 15, 17  ) )

  f_vec = np.array ( ( \
           1, \
           6, \
          20, \
           6, \
          15, \
         455, \
        3003, \
        6435, \
        5005, \
        1365, \
         105, \
          25, \
        2300, \
       53130, \
      480700, \
     2042975, \
     4457400, \
     5200300, \
     3268760, \
     1081575 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    f = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, f

def binomial_values_test ( ):

#*****************************************************************************80
#
## binomial_values_test() tests binomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'binomial_values_test():' )
  print ( '  binomial_values stores values of the BINOMIAL function.' )
  print ( '' )
  print ( '      A         B         BINOMIAL(A,B)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, f = binomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d  %12d' % ( a, b, f ) )

  return

def cbrt_values ( n_data ):

#*****************************************************************************80
#
## cbrt_values() returns some values of the cube root function.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
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
## cbrt_values_test() tests cbrt_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'cbrt_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cbrt_values stores values of the cube root function.' )
  print ( '' )
  print ( '      X         CBRT(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cbrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def chi_values ( n_data ):

#*****************************************************************************80
#
## chi_values() returns some values of the hyperbolic cosine integral function.
#
#  Discussion:
#
#      CHI(X) = gamma + log ( x ) 
#        + integral ( 0 <= T < X ) ( cosh ( T ) - 1 ) / T  dT
#
#    where gamma is Euler's constant.
#
#    In Mathematica, the function can be evaluated by:
#
#      CoshIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
    -0.05277684495649362, \
     0.1577508933739787, \
     0.3455691756953907, \
     0.5183999848333915, \
     0.6813138871854339, \
     0.8378669409802082, \
     1.141841924170595, \
     1.445494075789644, \
     1.759505807660965, \
     2.092577214062032, \
     2.452666922646915, \
     3.524425488354165, \
     4.960392094765610, \
     6.959191927647393, \
     9.813547558823186, \
    13.96581164859243 ) )

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ) )

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

def chi_values_test ( ):

#*****************************************************************************80
#
## chi_values_test() tests chi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'chi_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  chi_values stores values of the hyperbolic cosine integral function.' )
  print ( '' )
  print ( '      X         CHI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = chi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def cinh_values ( n_data ):

#*****************************************************************************80
#
## cinh_values() returns some values of the alternate hyperbolic cosine integral function.
#
#  Discussion:
#
#    The alternate hyperbolic cosine integral is defined by
#
#      CINH(X) =integral ( 0 <= T < X ) ( cosh ( T ) - 1 ) / T  dT
#
#    In Mathematica, the function can be evaluated by:
#
#      Integrate [ ( Cosh[t] - 1 ) / t, { t, 0, x } ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 17

  fx_vec = np.array ( ( \
     0.00000000000000000, \
     0.06315467070191883, \
     0.09136085223843649, \
     0.1250284547325902, \
     0.1643278712460683, \
     0.2094587379417273, \
     0.2606512760786754, \
     0.3823047024751071, \
     0.5318061742668980, \
     0.7122865135136963, \
     0.9275748842583805, \
     1.182304077185436, \
     2.030919091578478, \
     3.284564141195967, \
     5.129213294250493, \
     7.850037532801762, \
    11.88451858691463 ) )

  x_vec = np.array ( ( \
     0.0, \
     0.5, \
     0.6, \
     0.7, \
     0.8, \
     0.9, \
     1.0, \
     1.2, \
     1.4, \
     1.6, \
     1.8, \
     2.0, \
     2.5, \
     3.0, \
     3.5, \
     4.0, \
     4.5 ) )

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

def cinh_values_test ( ):

#*****************************************************************************80
#
## cinh_values_test() tests cinh_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cinh_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cinh_values: values of the alternate hyperbolic cosine integral function.' )
  print ( '' )
  print ( '      X         CINH(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cinh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def cin_values ( n_data ):

#*****************************************************************************80
#
## cin_values() returns some values of the alternate cosine integral function.
#
#  Discussion:
#
#    The alternate cosine integral is defined by
#
#      CIN(X) = gamma + log(X) + integral ( 0 <= T <= X ) ( cos ( T ) - 1 ) / T  dT
#
#    In Mathematica, the function can be evaluated by:
#
#      EulerGamma + Log[x] - CosIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
     0.6185256314820045E-01, \
     0.8866074809482194E-01, \
     0.1200260139539026E+00, \
     0.1557934976348559E+00, \
     0.1957873187759337E+00, \
     0.2398117420005647E+00, \
     0.3390780388012470E+00, \
     0.4516813164280685E+00, \
     0.5754867772153906E+00, \
     0.7081912003853150E+00, \
     0.8473820166866132E+00, \
     0.1207635200410304E+01, \
     0.1556198167561642E+01, \
     0.1862107181909382E+01, \
     0.2104491723908354E+01, \
     0.2274784183779546E+01 ) )

  x_vec = np.array ( ( \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.2E+00, \
     1.4E+00, \
     1.6E+00, \
     1.8E+00, \
     2.0E+00, \
     2.5E+00, \
     3.0E+00, \
     3.5E+00, \
     4.0E+00, \
     4.5E+00 ) )

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

def cin_values_test ( ):

#*****************************************************************************80
#
## cin_values_test() tests cin_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cin_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cin_values stores values of the alternate cosine integral function.' )
  print ( '' )
  print ( '      X         CIN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def ci_values ( n_data ):

#*****************************************************************************80
#
## ci_values() returns some values of the cosine integral function.
#
#  Discussion:
#
#    The cosine integral is defined by
#
#      CI(X) = - integral ( X <= T < Infinity ) ( cos ( T ) ) / T  dT
#
#    In Mathematica, the function can be evaluated by:
#
#      CosIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
     -0.1777840788066129E+00, \
     -0.2227070695927976E-01, \
      0.1005147070088978E+00, \
      0.1982786159524672E+00, \
      0.2760678304677729E+00, \
      0.3374039229009681E+00, \
      0.4204591828942405E+00, \
      0.4620065850946773E+00, \
      0.4717325169318778E+00, \
      0.4568111294183369E+00, \
      0.4229808287748650E+00, \
      0.2858711963653835E+00, \
      0.1196297860080003E+00, \
     -0.3212854851248112E-01, \
     -0.1409816978869304E+00, \
     -0.1934911221017388E+00 ) )

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ) )

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

def ci_values_test ( ):

#*****************************************************************************80
#
## ci_values_test() tests ci_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ci_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ci_values stores values of the cosine integral function.' )
  print ( '' )
  print ( '      X         CI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = ci_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def cos_degree_values ( n_data ):

#*****************************************************************************80
#
## cos_degree_values(): the cosine function with argument in degrees.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cos[x Degree]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 22

  fx_vec = np.array ( ( \
     0.99619469809174553230, \
     1.0000000000000000000, \
     0.99984769515639123916, \
     0.99939082701909573001, \
     0.99862953475457387378, \
     0.99756405025982424761, \
     0.99619469809174553230, \
     0.98480775301220805937, \
     0.96592582628906828675, \
     0.86602540378443864676, \
     0.70710678118654752440, \
     0.50000000000000000000, \
     0.25881904510252076235, \
     0.087155742747658173558, \
     0.069756473744125300776, \
     0.052335956242943832722, \
     0.034899496702500971646, \
     0.017452406437283512819, \
     0.000000000000000000000, \
    -0.017452406437283512819, \
    -0.25881904510252076235, \
    -1.0000000000000000000 ))

  x_vec = np.array ( ( \
     -5.0, \
      0.0, \
      1.0, \
      2.0, \
      3.0, \
      4.0, \
      5.0, \
     10.0, \
     15.0, \
     30.0, \
     45.0, \
     60.0, \
     75.0, \
     85.0, \
     86.0, \
     87.0, \
     88.0, \
     89.0, \
     90.0, \
     91.0, \
    105.0, \
    180.0 ))

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

def cos_degree_values_test ( ):

#*****************************************************************************80
#
## cos_degree_values_test() tests cos_degree_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'cos_degree_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cos_degree_values stores values of the cosine function.' )
  print ( '' )
  print ( '      X         COS(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cos_degree_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def cosh_values ( n_data ):

#*****************************************************************************80
#
## cosh_values() returns some values of the hyperbolic cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cosh[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  fx_vec = np.array ( ( \
      74.209948524787844444, \
       1.5430806348152437785, \
       1.0000000000000000000, \
       1.0050041680558035990, \
       1.0200667556190758463, \
       1.0453385141288604850, \
       1.0810723718384548093, \
       1.1276259652063807852, \
       1.1854652182422677038, \
       1.2551690056309430182, \
       1.3374349463048445980, \
       1.4330863854487743878, \
       1.5430806348152437785, \
       3.7621956910836314596, \
      10.067661995777765842, \
      27.308232836016486629, \
      74.209948524787844444, \
   11013.232920103323140 ))

  x_vec = np.array ( ( \
   -5.0, \
   -1.0, \
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
    1.0, \
    2.0, \
    3.0, \
    4.0, \
    5.0, \
   10.0 ))

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

def cosh_values_test ( ):

#*****************************************************************************80
#
## cosh_values_test() tests cosh_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'cosh_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cosh_values stores values of the hyperbolic cosine function.' )
  print ( '' )
  print ( '      X         COSH(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cosh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def cos_values ( n_data ):

#*****************************************************************************80
#
## cos_values() returns some values of the cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cos[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
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
## cos_values_test() tests cos_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'cos_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cos_values stores values of the cosine function.' )
  print ( '' )
  print ( '      X         COS(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def cot_values ( n_data ):

#*****************************************************************************80
#
## cot_values() returns some values of the cotangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cot[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 15

  fx_vec = np.array ( ( \
   11.972209353628661620, \
    3.7320508075688772935, \
    1.8304877217124519193, \
    1.7320508075688772935, \
    1.0000000000000000000, \
    0.64209261593433070301, \
    0.57735026918962576451, \
    0.26794919243112270647, \
    0.00000000000000000000, \
    0.13165249758739585347, \
    0.065543462815238228565, \
   -0.45765755436028576375, \
   -7.0152525514345334694, \
    0.86369115445061661395, \
   -0.29581291553274554043 ))

  x_vec = np.array ( ( \
   0.083333333333333333333, \
   0.26179938779914943654, \
   0.50000000000000000000, \
   0.52359877559829887308, \
   0.78539816339744830962, \
   1.0000000000000000000, \
   1.0471975511965977462, \
   1.3089969389957471827, \
   1.5707963267948966192, \
   1.4398966328953219010, \
   1.5053464798451092601, \
   2.0000000000000000000, \
   3.0000000000000000000, \
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

def cot_values_test ( ):

#*****************************************************************************80
#
## cot_values_test() tests cot_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'cot_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cot_values stores values of the cotangent function.' )
  print ( '' )
  print ( '      X         COT(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cot_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def dawson_values ( n_data ):

#*****************************************************************************80
#
## dawson_values() returns some values of Dawson's integral.
#
#  Discussion:
#
#    The definition of Dawson's integral is
#
#      D(X) = exp ( -X * X ) * Integral ( 0 <= Y <= X ) exp ( Y * Y ) dY
#
#    Dawson's integral has a maximum at roughly
#
#      X = 0.9241388730
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi] * Exp[-x^2] * I * Erf[I*x] / 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
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
#    Eric Weisstein,
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.9933599239785286E-01, \
     0.1947510333680280E+00, \
     0.2826316650213119E+00, \
     0.3599434819348881E+00, \
     0.4244363835020223E+00, \
     0.4747632036629779E+00, \
     0.5105040575592318E+00, \
     0.5321017070563654E+00, \
     0.5407243187262987E+00, \
     0.5380795069127684E+00, \
     0.5262066799705525E+00, \
     0.5072734964077396E+00, \
     0.4833975173848241E+00, \
     0.4565072375268973E+00, \
     0.4282490710853986E+00, \
     0.3999398943230814E+00, \
     0.3725593489740788E+00, \
     0.3467727691148722E+00, \
     0.3229743193228178E+00, \
     0.3013403889237920E+00 ))

  x_vec = np.array ( ( \
     0.0E+00, \
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
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def dawson_values_test ( ):

#*****************************************************************************80
#
## dawson_values_test() tests dawson_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dawson_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dawson_values stores values of the Dawson integral function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = dawson_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def dilogarithm_values ( n_data ):

#*****************************************************************************80
#
## dilogarithm_values() returns some values of the dilogarithm function.
#
#  Discussion:
#
#    The dilogarithm is defined as
#
#      Li_2(X) = - Integral ( 0 <= T <= X ) ln ( 1 - T ) / T dT
#
#    The dilogarithm is also known as Spence's integral. 
#
#    In Abramowitz and Stegun form of the function is different,
#    and is equivalent to evaluated Li_2(1-X).
#
#    The dilogarithm is the special case, with N = 2, of the 
#    polylogarithm Li_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyLog[2,X]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( (
     0.0000000000000000E+00, \
     0.5063929246449603E-01, \
     0.1026177910993911E+00, \
     0.1560350339454831E+00, \
     0.2110037754397048E+00, \
     0.2676526390827326E+00, \
     0.3261295100754761E+00, \
     0.3866059411605865E+00, \
     0.4492829744712817E+00, \
     0.5143989891542119E+00, \
     0.5822405264650125E+00, \
     0.6531576315069018E+00, \
     0.7275863077163334E+00, \
     0.8060826895177240E+00, \
     0.8893776242860387E+00, \
     0.9784693929303061E+00, \
     0.1074794600008248E+01, \
     0.1180581123830255E+01, \
     0.1299714723004959E+01, \
     0.1440633796970039E+01, \
     0.1644934066848226E+01 ))

  x_vec = np.array ( (
     0.00E+00, \
     0.05E+00, \
     0.10E+00, \
     0.15E+00, \
     0.20E+00, \
     0.25E+00, \
     0.30E+00, \
     0.35E+00, \
     0.40E+00, \
     0.45E+00, \
     0.50E+00, \
     0.55E+00, \
     0.60E+00, \
     0.65E+00, \
     0.70E+00, \
     0.75E+00, \
     0.80E+00, \
     0.85E+00, \
     0.90E+00, \
     0.95E+00, \
     0.10E+01 ))

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

def dilogarithm_values_test ( ):

#*****************************************************************************80
#
## dilogarithm_values_test() tests dilogarithm_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dilogarithm_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dilogarithm_values stores values of the dilogarithm function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = dilogarithm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def e1_values ( n_data ):

#*****************************************************************************80
#
## e1_values() returns some values of the exponential integral function E1(X).
#
#  Discussion:
#
#    The exponential integral E1(X) is defined by the formula:
#
#      E1(X) = integral ( 1 <= T <= Infinity ) exp ( -X*T ) / T dT
#
#    In Mathematica, the function can be evaluated by:
#
#      ExpIntegralE[1,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( (
     0.5597735947761608E+00, \
     0.4543795031894021E+00, \
     0.3737688432335091E+00, \
     0.3105965785455430E+00, \
     0.2601839393259996E+00, \
     0.2193839343955203E+00, \
     0.1859909045360402E+00, \
     0.1584084368514626E+00, \
     0.1354509578491291E+00, \
     0.1162193125713579E+00, \
     0.1000195824066327E+00, \
     0.8630833369753979E-01, \
     0.7465464440125305E-01, \
     0.6471312936386886E-01, \
     0.5620437817453485E-01, \
     0.4890051070806112E-01 ))

  x_vec = np.array ( (
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def e1_values_test ( ):

#*****************************************************************************80
#
## e1_values_test() tests e1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'e1_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  e1_values stores values of the exponential integral.' )
  print ( '' )
  print ( '      X         E1(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = e1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def ei_values ( n_data ):

#*****************************************************************************80
#
## ei_values() returns some values of the exponential integral function EI(X).
#
#  Definition:
#
#    The exponential integral EI(X) has the formula:
#
#      EI(X) = - integral ( -X <= T <= Infinity ) exp ( -T ) / T dT
#
#    In Mathematica, the function can be evaluated by:
#
#      ExpIntegralEi[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2004
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( (
     0.4542199048631736E+00, \
     0.7698812899373594E+00, \
     0.1064907194624291E+01, \
     0.1347396548212326E+01, \
     0.1622811713696867E+01, \
     0.1895117816355937E+01, \
     0.2167378279563403E+01, \
     0.2442092285192652E+01, \
     0.2721398880232024E+01, \
     0.3007207464150646E+01, \
     0.3301285449129798E+01, \
     0.3605319949019469E+01, \
     0.3920963201354904E+01, \
     0.4249867557487934E+01, \
     0.4593713686953585E+01, \
     0.4954234356001890E+01 ))

  x_vec = np.array ( (
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def ei_values_test ( ):

#*****************************************************************************80
#
## ei_values_test() tests ei_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ei_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ei_values stores values of the exponential integral.' )
  print ( '' )
  print ( '      X         EI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = ei_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def erfc_values ( n_data ):

#*****************************************************************************80
#
## erfc_values() returns some values of the "complementary error" function.
#
#  Discussion:
#
#    The complementary error function is defined by:
#
#      ERFC(X) = 1 - ( 2 / sqrt ( PI ) * integral ( 0 <= T <= X ) exp ( - T^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      Erfc[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
    1.000000000000000E+00, \
    0.7772974107895215E+00, \
    0.5716076449533315E+00, \
    0.3961439091520741E+00, \
    0.2578990352923395E+00, \
    0.1572992070502851E+00, \
    0.08968602177036462E+00, \
    0.04771488023735119E+00, \
    0.02365161665535599E+00, \
    0.01090949836426929E+00, \
    0.004677734981047266E+00, \
    0.001862846297981891E+00, \
    0.0006885138966450786E+00, \
    0.0002360344165293492E+00, \
    0.00007501319466545902E+00, \
    0.00002209049699858544E+00, \
    6.025761151762095E-06, \
    1.521993362862285E-06, \
    3.558629930076853E-07, \
    7.700392745696413E-08, \
    1.541725790028002E-08 ) )

  x_vec = np.array ( ( \
    0.0E+00, \
    0.2E+00, \
    0.4E+00, \
    0.6E+00, \
    0.8E+00, \
    1.0E+00, \
    1.2E+00, \
    1.4E+00, \
    1.6E+00, \
    1.8E+00, \
    2.0E+00, \
    2.2E+00, \
    2.4E+00, \
    2.6E+00, \
    2.8E+00, \
    3.0E+00, \
    3.2E+00, \
    3.4E+00, \
    3.6E+00, \
    3.8E+00, \
    4.0E+00 ) )

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

def erfc_values_test ( ):

#*****************************************************************************80
#
## erfc_values_test() tests erfc_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'erfc_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  erfc_values stores values of the complementary error function.' )
  print ( '' )
  print ( '      X         ERFC(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = erfc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def erf_values ( n_data ):

#*****************************************************************************80
#
## erf_values() returns some values of the ERF or "error" function.
#
#  Discussion:
#
#    The error function is defined by:
#
#      ERF(X) = ( 2 / sqrt ( PI ) * integral ( 0 <= T <= X ) exp ( - T^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      Erf[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2004
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1124629160182849E+00, \
     0.2227025892104785E+00, \
     0.3286267594591274E+00, \
     0.4283923550466685E+00, \
     0.5204998778130465E+00, \
     0.6038560908479259E+00, \
     0.6778011938374185E+00, \
     0.7421009647076605E+00, \
     0.7969082124228321E+00, \
     0.8427007929497149E+00, \
     0.8802050695740817E+00, \
     0.9103139782296354E+00, \
     0.9340079449406524E+00, \
     0.9522851197626488E+00, \
     0.9661051464753107E+00, \
     0.9763483833446440E+00, \
     0.9837904585907746E+00, \
     0.9890905016357307E+00, \
     0.9927904292352575E+00, \
     0.9953222650189527E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
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
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ) )

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

def erf_values_test ( ):

#*****************************************************************************80
#
## erf_values_test() tests erf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'erf_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  erf_values stores values of the error function.' )
  print ( '' )
  print ( '      X         ERF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def exp_values ( n_data ):

#*****************************************************************************80
#
## exp_values() returns some values of the exponential function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Exp[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
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

def exp_values_test ( ):

#*****************************************************************************80
#
## exp_values_test() tests exp_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'exp_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  exp_values stores values of the exponential function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = exp_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def fn_test ( ):

#*****************************************************************************80
#
## fn_test() tests fn().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fn_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test fn().' )
#
#  Utilities.
#
  airy_ai_values_test ( )
  airy_ai_prime_values_test ( )
  airy_bi_values_test ( )
  airy_bi_prime_values_test ( )
  arccos_values_test ( )
  arccosh_values_test ( )
  arcsin_values_test ( )
  arcsinh_values_test ( )
  arctan_values_test ( )
  arctan2_values_test ( )
  arctanh_values_test ( )
  bessel_i0_values_test ( )
  bessel_i1_values_test ( )
  bessel_j0_values_test ( )
  bessel_j1_values_test ( )
  bessel_k0_values_test ( )
  bessel_k1_values_test ( )
  bessel_kx_values_test ( )
  bessel_y0_values_test ( )
  bessel_y1_values_test ( )
  beta_values_test ( )
  beta_inc_values_test ( )
  beta_log_values_test ( )
  binomial_values_test ( )
  cbrt_values_test ( )
  chi_values_test ( )
  ci_values_test ( )
  cin_values_test ( )
  cinh_values_test ( )
  cos_values_test ( )
  cos_degree_values_test ( )
  cosh_values_test ( )
  cot_values_test ( )
  dawson_values_test ( )
  dilogarithm_values_test ( )
  e1_values_test ( )
  ei_values_test ( )
  erf_values_test ( )
  erfc_values_test ( )
  exp_values_test ( )
  gamma_values_test ( )
  gamma_inc_values_test ( )
  gamma_inc_tricomi_values_test ( )
  gamma_log_values_test ( )
  hypergeometric_u_values_test ( )
  int_values_test ( )
  log_values_test ( )
  log10_values_test ( )
  logarithmic_integral_values_test ( )
  psi_values_test ( )
  r8_factorial_values_test ( )
  r8_rise_values_test ( )
  shi_values_test ( )
  si_values_test ( )
  sin_values_test ( )
  sin_degree_values_test ( )
  sinh_values_test ( )
  sqrt_values_test ( )
  tan_values_test ( )
  tanh_values_test ( )

  i4_mach_test ( )

  r8_acos_test ( )
  r8_acosh_test ( )
  r8_ai_test ( )
  r8_aid_test ( )
  r8_aint_test ( )
  r8_asin_test ( )
  r8_asinh_test ( )
  r8_atan_test ( )
  r8_atan2_test ( )
  r8_atanh_test ( )
  r8_besi0_test ( )
  r8_besi1_test ( )
  r8_besj0_test ( )
  r8_besj1_test ( )
  r8_besk0_test ( )
  r8_besk_test ( )
  r8_besk1_test ( )
  r8_besy0_test ( )
  r8_besy1_test ( )
  r8_beta_test ( )
  r8_betai_test ( )
  r8_bi_test ( )
  r8_bid_test ( )
  r8_binom_test ( )
  r8_cbrt_test ( )
  r8_chi_test ( )
  r8_chu_test ( )
  r8_ci_test ( )
  r8_cin_test ( )
  r8_cinh_test ( )
  r8_cos_test ( )
  r8_cos_deg_test ( )
  r8_cosh_test ( )
  r8_cot_test ( )
  r8_csevl_test ( )
  r8_dawson_test ( )
  r8_e1_test ( )
  r8_ei_test ( )
  r8_erf_test ( )
  r8_erfc_test ( )
  r8_exp_test ( )
  r8_fac_test ( )
  r8_gamic_test ( )
  r8_gamit_test ( )
  r8_gaml_test ( )
  r8_gamma_test ( )
  r8_gamr_test ( )
  r8_inits_test ( )
  r8_int_test ( )
  r8_lbeta_test ( )
  r8_lgams_test ( )
  r8_lgmc_test ( )
  r8_li_test ( )
  r8_lngam_test ( )
  r8_lnrel_test ( )
  r8_log_test ( )
  r8_log10_test ( )
  r8_mach_test ( )
  r8_mop_test ( )
  r8_pak_test ( )
  r8_poch_test ( )
  r8_psi_test ( )
  r8_rand_test ( )
  r8_randgs_test ( )
  r8_random_test ( )
  r8_ren_test ( )
  r8_shi_test ( )
  r8_si_test ( )
  r8_sign_test ( )
  r8_sin_test ( )
  r8_sin_deg_test ( )
  r8_sinh_test ( )
  r8_spence_test ( )
  r8_sqrt_test ( )
  r8_tan_test ( )
  r8_tanh_test ( )
  r8_upak_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fn_test():' )
  print ( '  Normal end of execution.' )
  return

def gamma_inc_tricomi_values ( n_data ):

#*****************************************************************************80
#
## gamma_inc_tricomi_values(): values of Tricomi's incomplete Gamma function.
#
#  Discussion:
#
#    Tricomi's incomplete Gamma function is defined as:
#
#      1/Gamma(A) * 1/X^A * Integral ( 0 <= T <= X ) T^(A-1) * exp(-T) dT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, the parameter of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     0.10E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+01, \
     0.10E+01, \
     0.10E+01, \
     0.11E+01, \
     0.11E+01, \
     0.11E+01, \
     0.20E+01, \
     0.20E+01, \
     0.20E+01, \
     0.60E+01, \
     0.60E+01, \
     0.11E+02, \
     0.26E+02, \
     0.41E+02  ))

  f_vec = np.array ( ( \
    1.048292641463504E+00, \
    1.024577737369574E+00, \
    0.9493712443185374E+00, \
    1.100793230316492E+00, \
    0.8998911979655218E+00, \
    0.5301656062431039E+00, \
    0.9516258196404043E+00, \
    0.6321205588285577E+00, \
    0.1986524106001829E+00, \
    0.9071784510537487E+00, \
    0.5891809618706485E+00, \
    0.1688269752193589E+00, \
    0.4527034271637121E+00, \
    0.1965220442795224E+00, \
    0.02025928457705232E+00, \
    0.0001721181724479739E+00, \
    3.280858070850586E-07, \
    5.244396471821590E-14, \
    2.013462926183376E-37, \
    1.230623887499875E-68 ))

  x_vec = np.array ( ( \
     0.30E-01, \
     0.30E+00, \
     0.15E+01, \
     0.75E-01, \
     0.75E+00, \
     0.35E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.15E+00, \
     0.15E+01, \
     0.70E+01, \
     0.25E+01, \
     0.12E+02, \
     0.16E+02, \
     0.25E+02, \
     0.45E+02 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def gamma_inc_tricomi_values_test ( ):

#*****************************************************************************80
#
## gamma_inc_tricomi_values_test() tests gamma_inc_tricomi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gamma_inc_tricomi_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gamma_inc_tricomi_values stores values of an incomplete Gamma function.' )
  print ( '' )
  print ( '      A         X        F(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, f = gamma_inc_tricomi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( a, x, f ) )

  return

def gamma_inc_values ( n_data ):

#*****************************************************************************80
#
## gamma_inc_values() returns some values of the incomplete Gamma function.
#
#  Discussion:
#
#    The (normalized) incomplete Gamma function is defined as:
#
#      Integral ( X <= T < oo ) T^(A-1) * exp(-T) dT.
#
#    In Mathematica, the function can be evaluated by:
#
#      Gamma[A,X]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, the parameter of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     0.10E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+01, \
     0.10E+01, \
     0.10E+01, \
     0.11E+01, \
     0.11E+01, \
     0.11E+01, \
     0.20E+01, \
     0.20E+01, \
     0.20E+01, \
     0.60E+01, \
     0.60E+01, \
     0.11E+02, \
     0.26E+02, \
     0.41E+02 ))

  f_vec = np.array ( ( \
    2.490302836300570E+00, \
    0.8718369702247978E+00, \
    0.1079213896175866E+00, \
    1.238121685818417E+00, \
    0.3911298052193973E+00, \
    0.01444722098952533E+00, \
    0.9048374180359596E+00, \
    0.3678794411714423E+00, \
    0.006737946999085467E+00, \
    0.8827966752611692E+00, \
    0.3908330082003269E+00, \
    0.008051456628620993E+00, \
    0.9898141728888165E+00, \
    0.5578254003710746E+00, \
    0.007295055724436130E+00, \
    114.9574754165633E+00, \
    2.440923530031405E+00, \
    280854.6620274718E+00, \
    8.576480283455533E+24, \
    2.085031346403364E+47 ))

  x_vec = np.array ( ( \
     0.30E-01, \
     0.30E+00, \
     0.15E+01, \
     0.75E-01, \
     0.75E+00, \
     0.35E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.15E+00, \
     0.15E+01, \
     0.70E+01, \
     0.25E+01, \
     0.12E+02, \
     0.16E+02, \
     0.25E+02, \
     0.45E+02 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def gamma_inc_values_test ( ):

#*****************************************************************************80
#
## gamma_inc_values_test() tests gamma_inc_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gamma_inc_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gamma_inc_values stores values of the incomplete Gamma function.' )
  print ( '' )
  print ( '      A         X        gamma_inc(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, f = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( a, x, f ) )

  return

def gamma_log_values ( n_data ):

#*****************************************************************************80
#
## gamma_log_values() returns some values of the Log Gamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[Gamma[x]]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.1524063822430784E+01, \
      0.7966778177017837E+00, \
      0.3982338580692348E+00, \
      0.1520596783998375E+00, \
      0.0000000000000000E+00, \
     -0.4987244125983972E-01, \
     -0.8537409000331584E-01, \
     -0.1081748095078604E+00, \
     -0.1196129141723712E+00, \
     -0.1207822376352452E+00, \
     -0.1125917656967557E+00, \
     -0.9580769740706586E-01, \
     -0.7108387291437216E-01, \
     -0.3898427592308333E-01, \
     0.00000000000000000E+00, \
     0.69314718055994530E+00, \
     0.17917594692280550E+01, \
     0.12801827480081469E+02, \
     0.39339884187199494E+02, \
     0.71257038967168009E+02 ) )

  x_vec = np.array ( ( \
      0.20E+00, \
      0.40E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

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

def gamma_log_values_test ( ):

#*****************************************************************************80
#
## gamma_log_values_test() tests gamma_log_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gamma_log_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gamma_log_values stores values of' )
  print ( '  the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            gamma_log(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def gamma_values ( n_data ):

#*****************************************************************************80
#
## gamma_values() returns some values of the Gamma function.
#
#  Discussion:
#
#    The Gamma function is defined as:
#
#      Gamma(Z) = Integral ( 0 <= T < Infinity) T^(Z-1) exp(-T) dT
#
#    It satisfies the recursion:
#
#      Gamma(X+1) = X * Gamma(X)
#
#    Gamma is undefined for nonpositive integral X.
#    Gamma(0.5) = sqrt(PI)
#    For N a positive integer, Gamma(N+1) = N!, the standard factorial.
#
#    In Mathematica, the function can be evaluated by:
#
#      Gamma[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     -0.3544907701811032E+01, \
     -0.1005871979644108E+03, \
      0.9943258511915060E+02, \
      0.9513507698668732E+01, \
      0.4590843711998803E+01, \
      0.2218159543757688E+01, \
      0.1772453850905516E+01, \
      0.1489192248812817E+01, \
      0.1164229713725303E+01, \
      0.1000000000000000E+01, \
      0.9513507698668732E+00, \
      0.9181687423997606E+00, \
      0.8974706963062772E+00, \
      0.8872638175030753E+00, \
      0.8862269254527580E+00, \
      0.8935153492876903E+00, \
      0.9086387328532904E+00, \
      0.9313837709802427E+00, \
      0.9617658319073874E+00, \
      0.1000000000000000E+01, \
      0.2000000000000000E+01, \
      0.6000000000000000E+01, \
      0.3628800000000000E+06, \
      0.1216451004088320E+18, \
      0.8841761993739702E+31 ) )

  x_vec = np.array ( ( \
     -0.50E+00, \
     -0.01E+00, \
      0.01E+00, \
      0.10E+00, \
      0.20E+00, \
      0.40E+00, \
      0.50E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

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

def gamma_values_test ( ):

#*****************************************************************************80
#
## gamma_values_test() tests gamma_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gamma_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gamma_values stores values of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def hypergeometric_u_values ( n_data ):

#*****************************************************************************80
#
## hypergeometric_u_values(): some values of the hypergeometric function U(a,b,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = HypergeometricU [ a, b, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 February 2015
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, X, the parameters.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( (\
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
     0.825, \
     1.100, \
     1.650, \
     3.300, \
     0.825, \
     1.100, \
     1.650, \
     3.300, \
     0.825, \
     1.100, \
     1.650, \
     3.300 ))

  b_vec = np.array ( (\
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7 ))

  f_vec = np.array ( (\
         -68.693628728078601389E+00, \
          -0.0029710551374761070801E+00, \
           1.5008631742177797301E+00, \
          20.614688244200596134E+00, \
           7.4563815469305551938E+00, \
           1.0155793767749293733E+00, \
           0.73446538936622668912E+00, \
           0.28046404941879399225E+00, \
           3.4508153741446547607E+00, \
           1.5156637368753063495E+00, \
           0.56042118587934993510E+00, \
           0.064897147735134223341E+00, \
      223432.02356977463356E+00, \
      263079.25980740811495E+00, \
      269802.90319351274132E+00, \
       82809.311335606553425E+00, \
          26.465684783131844524E+00, \
          28.093506172516056560E+00, \
          23.889164624518872504E+00, \
           4.5338847857070388229E+00, \
           3.0224469362694842535E+00, \
           2.8040650913713359934E+00, \
           1.9262578111480172682E+00, \
           0.23020518115860909098E+00 ))

  x_vec = np.array ( (\
     0.25, \
     0.25, \
     0.25, \
     0.25, \
     1.55, \
     1.55, \
     1.55, \
     1.55, \
     2.85, \
     2.85, \
     2.85, \
     2.85, \
     0.25, \
     0.25, \
     0.25, \
     0.25, \
     1.55, \
     1.55, \
     1.55, \
     1.55, \
     2.85, \
     2.85, \
     2.85, \
     2.85 ))

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

def hypergeometric_u_values_test ( ):

#*****************************************************************************80
#
## hypergeometric_u_values_test() tests hypergeometric_u_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hypergeometric_u_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hypergeometric_u_values stores values of the Hypergeometric U function.' )
  print ( '' )
  print ( '        A             B             X              F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = hypergeometric_u_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16g' % ( a, b, x, f ) )

  return

def int_values ( n_data ):

#*****************************************************************************80
#
## int_values() returns some values of the "integer part" function.
#
#  Discussion:
#
#    INT(X) = returns the integer part of a real number.
#
#    The result is returned as a real number.
#
#    The result is computed by rounding the absolute value of the
#    input towards 0, and then restoring the sign.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    Output real F, the value of the function.
#
  import numpy as np

  n_max = 25;

  f_vec = np.array ( ( \
     -2.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      2.00E+00 ))

  x_vec = np.array ( ( \
     -2.01E+00, \
     -1.99E+00, \
     -1.50E+00, \
     -1.10E+00, \
     -1.01E+00, \
     -1.00E+00, \
     -0.99E+00, \
     -0.90E+00, \
     -0.51E+00, \
     -0.50E+00, \
     -0.49E+00, \
     -0.01E+00, \
      0.00E+00, \
      0.01E+00, \
      0.49E+00, \
      0.50E+00, \
      0.51E+00, \
      0.90E+00, \
      0.99E+00, \
      1.00E+00, \
      1.01E+00, \
      1.10E+00, \
      1.50E+00, \
      1.99E+00, \
      2.01E+00 ))

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

def int_values_test ( ):

#*****************************************************************************80
#
## int_values_test() tests int_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'int_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  int_values stores values of the integer part function.' )
  print ( '' )
  print ( '      X         INT(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def log10_values ( n_data ):

#*****************************************************************************80
#
## log10_values() returns some values of the logarithm 10 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log10[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
   -5.0000000000000000000, \
   -2.0000000000000000000, \
   -1.0000000000000000000, \
   -0.69897000433601880479, \
   -0.52287874528033756270, \
   -0.39794000867203760957, \
   -0.30102999566398119521, \
   -0.22184874961635636749, \
   -0.15490195998574316929, \
   -0.096910013008056414359, \
   -0.045757490560675125410, \
    0.000000000000000000000, \
    0.30102999566398119521, \
    0.47712125471966243730, \
    0.49714987269413385435, \
    0.69897000433601880479, \
    1.0000000000000000000, \
    1.3010299956639811952, \
    2.0000000000000000000, \
    8.0915149771692704475 ))

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

def log10_values_test ( ):

#*****************************************************************************80
#
## log10_values_test() tests log10_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'log10_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  log10_values stores values of the LOG10 function.' )
  print ( '' )
  print ( '      X         LOG10(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = log10_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def logarithmic_integral_values ( n_data ):

#*****************************************************************************80
#
## logarithmic_integral_values() returns values of the logarithmic integral LI(X).
#
#  Discussion:
#
#    The logarithmic integral is defined as:
#
#      LI(X) = integral ( 0 <= T <= Z ) dT / log ( T )
#
#    The principal value of the integral is taken.  There is a
#    branch cut discontinuity in the complex plane from -infinity
#    to +1.
#
#    Abramowitz and Stegun assume 1 < X.
#
#    In Mathematica, the function can be evaluated by:
#
#      LogIntegral[x]
#
#    There is a simple relationship with the exponential integral EI:
#
#      LI(X) = EI(LN(X))
#
#    The function LI(X) provides a good approximation to PI(X),
#    the number of primes less than or equal to X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 28

  f_vec = np.array ( ( \
      0.0000000000000000E+00, \
     -0.3238978959329102E-01, \
     -0.8512648672879405E-01, \
     -0.1574149028946895E+00, \
     -0.2529494192126213E+00, \
     -0.3786710430610880E+00, \
     -0.5468514142104170E+00, \
     -0.7809468775455607E+00, \
     -0.1134011957382327E+01, \
     -0.1775800683423525E+01, \
     -0.2443622553873225E+01, \
     -0.3124190050507211E+01, \
     -0.2872935510329120E+01, \
     -0.2164282524138207E+01, \
     -0.1440351296279408E+01, \
     -0.6864884538258716E+00, \
      0.1250649863152964E+00, \
      0.1045163780117493E+01, \
      0.2967585095039051E+01, \
      0.5253718299558931E+01, \
      0.8519716463711059E+01, \
      0.1360509217709172E+02, \
      0.2193466832805100E+02, \
      0.3604254831722944E+02, \
      0.6051306533791733E+02, \
      0.1037211171690373E+03, \
      0.1810780396816945E+03, \
      0.3211144156746837E+03 ))

  x_vec = np.array ( ( \
     0.000000E+00, \
     0.100000E+00, \
     0.200000E+00, \
     0.300000E+00, \
     0.400000E+00, \
     0.500000E+00, \
     0.600000E+00, \
     0.700000E+00, \
     0.800000E+00, \
     0.900000E+00, \
     0.950000E+00, \
     0.975000E+00, \
     0.103125E+01, \
     0.106250E+01, \
     0.112500E+01, \
     0.125000E+01, \
     0.150000E+01, \
     0.200000E+01, \
     0.400000E+01, \
     0.800000E+01, \
     0.160000E+02, \
     0.320000E+02, \
     0.640000E+02, \
     0.128000E+03, \
     0.256000E+03, \
     0.512000E+03, \
     0.102400E+04, \
     0.204800E+04 ))

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

def logarithmic_integral_values_test ( ):

#*****************************************************************************80
#
## logarithmic_integral_values_test() tests logarithmic_integral_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'logarithmic_integral_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  logarithmic_integral_values stores values of the logarithmic_integral function.' )
  print ( '' )
  print ( '      X         logarithmic_integral(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = logarithmic_integral_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def log_values ( n_data ):

#*****************************************************************************80
#
## log_values() returns some values of the logarithm function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
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

def log_values_test ( ):

#*****************************************************************************80
#
## log_values_test() tests log_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'log_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  log_values stores values of the LOG function.' )
  print ( '' )
  print ( '      X         LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def r8_mach ( i ):

#*****************************************************************************80
#
## r8_mach() returns double precision real machine constants.
#
#  Discussion:
#
#    Assume that double precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    r8_mach will return the following values:
#
#      r8_mach(1) = B^(EMIN-1), the smallest positive magnitude.
#      r8_mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      r8_mach(3) = B^(-T), the smallest relative spacing.
#      r8_mach(4) = B^(1-T), the largest relative spacing.
#      r8_mach(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    This version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Input:
#
#    integer I, chooses the value to be returned.
#    1 <= I <= 5.
#
#  Output:
#
#    real VALUE, the value of the chosen item.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'r8_mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'r8_mach - Fatal error!' )
  elif ( i == 1 ):
    value = 1.112536929253601E-308
  elif ( i == 2 ):
    value = 4.494232837155789E+307
  elif ( i == 3 ):
    value = 1.110223024625157E-016
  elif ( i == 4 ):
    value = 2.220446049250313E-016
  elif ( i == 5 ):
    value = 0.301029995663981
  elif ( 5 < i ):
    print ( '' )
    print ( 'r8_mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'r8_mach - Fatal error!' )

  return value

def r8_mach_test ( ):

#*****************************************************************************80
#
## r8_mach_test() tests r8_mach().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_mach_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_mach reports the value of constants associated' )
  print ( '  with real double precision computer arithmetic.' )

  print ( '' )
  print ( '  Assume that double precision numbers are stored ' )
  print ( '  with a mantissa of T digits in base B, with an' )
  print ( '  exponent whose value must lie between EMIN and EMAX.' )

  print ( '' )
  print ( '  For input arguments of 1 <= I <= 5,' )
  print ( '  r8_mach will return the following values:' )

  print ( '' )
  print ( '  r8_mach(1) = B^(EMIN-1), the smallest positive magnitude.' )
  print ( '  %26.16e' % ( r8_mach ( 1 ) ) )

  print ( '' )
  print ( '  r8_mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.' )
  print ( '  %26.16e' % ( r8_mach ( 2 ) ) )

  print ( '' )
  print ( '  r8_mach(3) = B^(-T), the smallest relative spacing.' )
  print ( '  %26.16e' % ( r8_mach ( 3 ) ) )

  print ( '' )
  print ( '  r8_mach(4) = B^(1-T), the largest relative spacing.' )
  print ( '  %26.16e' % ( r8_mach ( 4 ) ) )

  print ( '' )
  print ( '  r8_mach(5) = log10(B).' )
  print ( '  %26.16e' % ( r8_mach ( 5 ) ) )

  return

def i4_mach ( i ):

#*****************************************************************************80
#
## i4_mach() returns integer machine constants.
#
#  Discussion:
#
#    Input/output unit numbers.
#
#      i4_mach(1) = the standard input unit.
#      i4_mach(2) = the standard output unit.
#      i4_mach(3) = the standard punch unit.
#      i4_mach(4) = the standard error message unit.
#
#    Words.
#
#      i4_mach(5) = the number of bits per integer storage unit.
#      i4_mach(6) = the number of characters per integer storage unit.
#
#    Integers.
#
#    Assume integers are represented in the S digit base A form:
#
#      Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))
#
#    where 0 <= X(1:S-1) < A.
#
#      i4_mach(7) = A, the base.
#      i4_mach(8) = S, the number of base A digits.
#      i4_mach(9) = A^S-1, the largest integer.
#
#    Floating point numbers
#
#    Assume floating point numbers are represented in the T digit
#    base B form:
#
#      Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )
#
#    where 0 <= X(I) < B for I=1 to T, 0 < X(1) and EMIN <= E <= EMAX.
#
#      i4_mach(10) = B, the base.
#
#    Single precision
#
#      i4_mach(11) = T, the number of base B digits.
#      i4_mach(12) = EMIN, the smallest exponent E.
#      i4_mach(13) = EMAX, the largest exponent E.
#
#    Double precision
#
#      i4_mach(14) = T, the number of base B digits.
#      i4_mach(15) = EMIN, the smallest exponent E.
#      i4_mach(16) = EMAX, the largest exponent E.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    This version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Input:
#
#    integer I, chooses the parameter to be returned.
#    1 <= I <= 16.
#
#  Output:
#
#    integer VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'i4_mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 16.' )
    print ( '  I =   %d' % ( i ) )
    raise Exception ( 'i4_mach - Fatal error!' )
  elif ( i == 1 ):
    value = 5
  elif ( i == 2 ):
    value = 6
  elif ( i == 3 ):
    value = 7
  elif ( i == 4 ):
    value = 6
  elif ( i == 5 ):
    value = 32
  elif ( i == 6 ):
    value = 4
  elif ( i == 7 ):
    value = 2
  elif ( i == 8 ):
    value = 31
  elif ( i == 9 ):
    value = 2147483647
  elif ( i == 10 ):
    value = 2
  elif ( i == 11 ):
    value = 24
  elif ( i == 12 ):
    value = -125
  elif ( i == 13 ):
    value = 128
  elif ( i == 14 ):
    value = 53
  elif ( i == 15 ):
    value = -1021
  elif ( i == 16 ):
    value = 1024
  elif ( 16 < i ):
    print ( '' )
    print ( 'i4_mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 16.' )
    print ( '  I =   %d' % ( i ) )
    raise Exception ( 'i4_mach - Fatal error!' )

  return value

def i4_mach_test ( ):

#*****************************************************************************80
#
## i4_mach_test() tests i4_mach().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_mach_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_mach reports the value of constants associated' )
  print ( '  with integer computer arithmetic.' )

  print ( '' )
  print ( '  Numbers associated with input/output units:' )

  print ( '' )
  print ( '  i4_mach(1) = the standard input unit.' )
  print ( '  %d' % ( i4_mach ( 1 ) ) )

  print ( '' )
  print ( '  i4_mach(2) = the standard output unit.' )
  print ( '  %d' % ( i4_mach ( 2 ) ) )

  print ( '' )
  print ( '  i4_mach(3) = the standard punch unit.' )
  print ( '  %d' % ( i4_mach ( 3 ) ) )

  print ( '' )
  print ( '  i4_mach(4) = the standard error message unit.' )
  print ( '  %d' % ( i4_mach ( 4 ) ) )

  print ( '' )
  print ( '  Numbers associated with words:' )

  print ( '' )
  print ( '  i4_mach(5) = the number of bits per integer.' )
  print ( '  %d' % ( i4_mach ( 5 ) ) )

  print ( '' )
  print ( '  i4_mach(6) = the number of characters per integer.' )
  print ( '  %d' % ( i4_mach ( 6 ) ) )

  print ( '' )
  print ( '  Numbers associated with integer values:' )

  print ( '' )
  print ( '  Assume integers are represented in the S digit' )
  print ( '  base A form:' )
  print ( '' )
  print ( '    Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))' )
  print ( '' )
  print ( '  where the digits X satisfy 0 <= X(1:S-1) < A.' )

  print ( '' )
  print ( '  i4_mach(7) = A, the base.' )
  print ( '  %d' % ( i4_mach ( 7 ) ) )

  print ( '' )
  print ( '  i4_mach(8) = S, the number of base A digits.' )
  print ( '  %d' % ( i4_mach ( 8 ) ) )

  print ( '' )
  print ( '  i4_mach(9) = A^S-1, the largest integer.' )
  print ( '  %d' % ( i4_mach ( 9 ) ) )

  print ( '' )
  print ( '  Numbers associated with floating point values:' )
  print ( '' )
  print ( '  Assume floating point numbers are represented ' )
  print ( '  in the T digit base B form:' )
  print ( '' )
  print ( '    Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )' )
  print ( '' )
  print ( '  where' )
  print ( '' )
  print ( '    0 <= X(1:T) < B,' )
  print ( '    0 < X(1) (unless the value being represented is 0),' )
  print ( '    EMIN <= E <= EMAX.' )

  print ( '' )
  print ( '  i4_mach(10) = B, the base.' )
  print ( '  %d' % ( i4_mach ( 10 ) ) )

  print ( '' )
  print ( '  Numbers associated with single precision values:' )
  print ( '' )
  print ( '  i4_mach(11) = T, the number of base B digits.' )
  print ( '  %d' % ( i4_mach ( 11 ) ) )

  print ( '' )
  print ( '  i4_mach(12) = EMIN, the smallest exponent E.' )
  print ( '  %d' % ( i4_mach ( 12 ) ) )

  print ( '' )
  print ( '  i4_mach(13) = EMAX, the largest exponent E.' )
  print ( '  %d' % ( i4_mach ( 13 ) ) )

  print ( '' )
  print ( '  Numbers associated with double precision values:' )
  print ( '' )
  print ( '  i4_mach(14) = T, the number of base B digits.' )
  print ( '  %d' % ( i4_mach ( 14 ) ) )

  print ( '' )
  print ( '  i4_mach(15) = EMIN, the smallest exponent E.' )
  print ( '  %d' % ( i4_mach ( 15 ) ) )

  print ( '' )
  print ( '  i4_mach(16) = EMAX, the largest exponent E.' )
  print ( '  %d' % ( i4_mach ( 16 ) ) )

  return

def machine_test ( ):

#*****************************************************************************80
#
## machine_test() tests machine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'machine_test():' )
  print ( '  Test machine().' )

  r8_mach_test ( )
  i4_mach_test ( )
  r4_mach_test ( )

  return

def r4_mach ( i ):

#*****************************************************************************80
#
## r4_mach() returns single precision real machine constants.
#
#  Discussion:
#
#    Assume that single precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    r4_mach will return the following values:
#
#      r4_mach(1) = B^(EMIN-1), the smallest positive magnitude.
#      r4_mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      r4_mach(3) = B^(-T), the smallest relative spacing.
#      r4_mach(4) = B^(1-T), the largest relative spacing.
#      r4_mach(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    This version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Input:
#
#    integer I, chooses the parameter to be returned.
#    1 <= I <= 5.
#
#  Output:
#
#    real VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'r4_mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'r4_mach - Fatal error!' )
  elif ( i == 1 ):
    value = 1.1754944E-38
  elif ( i == 2 ):
    value = 3.4028235E+38
  elif ( i == 3 ):
    value = 5.9604645E-08
  elif ( i == 4 ):
    value = 1.1920929E-07
  elif ( i == 5 ):
    value = 0.3010300
  elif ( 5 < i ):
    print ( '' )
    print ( 'r4_mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'r4_mach - Fatal error!' )

  return value

def r4_mach_test ( ):

#*****************************************************************************80
#
## r4_mach_test() tests r4_mach().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r4_mach_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4_mach reports the value of constants associated' )
  print ( '  with real single precision computer arithmetic.' )

  print ( '' )
  print ( '  Assume that single precision numbers are stored ' )
  print ( '  with a mantissa of T digits in base B, with an ' )
  print ( '  exponent whose value must lie between EMIN and EMAX.' )

  print ( '' )
  print ( '  For input arguments of 1 <= I <= 5,' )
  print ( '  r4_mach will return the following values:' )

  print ( '' )
  print ( '  r4_mach(1) = B^(EMIN-1), the smallest positive magnitude.' )
  print ( '  %26.16e' % ( r4_mach ( 1 ) ) )

  print ( '' )
  print ( '  r4_mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.' )
  print ( '  %26.16e' % ( r4_mach ( 2 ) ) )

  print ( '' )
  print ( '  r4_mach(3) = B^(-T), the smallest relative spacing.' )
  print ( '  %26.16e' % ( r4_mach ( 3 ) ) )

  print ( '' )
  print ( '  r4_mach(4) = B^(1-T), the largest relative spacing.' )
  print ( '  %26.16e' % ( r4_mach ( 4 ) ) )

  print ( '' )
  print ( '  r4_mach(5) = log10(B).' )
  print ( '  %26.16e' % ( r4_mach ( 5 ) ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## timestamp_test() tests timestamp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'timestamp_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  timestamp prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  return

def psi_values ( n_data ):

#*****************************************************************************80
#
## psi_values() returns some values of the Psi or Digamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[x]
#
#    or
#
#      PolyGamma[0,x]
#
#    PSI(X) = d ln ( Gamma ( X ) ) / d X = Gamma'(X) / Gamma(X)
#
#    PSI(1) = -Euler's constant.
#
#    PSI(X+1) = PSI(X) + 1 / X.
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -10.42375494041108E+00, \
     -5.289039896592188E+00, \
     -3.502524222200133E+00, \
     -2.561384544585116E+00, \
     -1.963510026021423E+00, \
     -1.540619213893190E+00, \
     -1.220023553697935E+00, \
     -0.9650085667061385E+00, \
     -0.7549269499470514E+00, \
     -0.5772156649015329E+00, \
     -0.4237549404110768E+00, \
     -0.2890398965921883E+00, \
     -0.1691908888667997E+00, \
     -0.6138454458511615E-01, \
      0.3648997397857652E-01, \
      0.1260474527734763E+00, \
      0.2085478748734940E+00, \
      0.2849914332938615E+00, \
      0.3561841611640597E+00, \
      0.4227843350984671E+00 ))

  x_vec = np.array ( ( \
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
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def psi_values_test ( ):

#*****************************************************************************80
#
## psi_values_test() tests psi_values().
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
  import platform

  print ( '' )
  print ( 'psi_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  psi_values stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def r8_acosh ( x ):

#*****************************************************************************80
#
## r8_acosh() evaluates the arc-hyperbolic cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the arc-hyperbolic cosine of X.
#
  import numpy as np

  dln2 = 0.69314718055994530941723212145818
  xmax = 1.0 / np.sqrt ( r8_mach ( 3 ) )

  if ( x < 1.0 ):
    print ( '' )
    print ( 'r8_acosh - Fatal error!' )
    print ( '  X < 1.0' )
    raise Exception ( 'r8_acosh - Fatal error!' )
  elif ( x < xmax ):
    value = np.log ( x + np.sqrt ( x * x - 1.0 ) )
  else:
    value = dln2 + np.log ( x )

  return value

def r8_acosh_test ( ):

#*****************************************************************************80
#
## r8_acosh_test() tests r8_acosh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_acosh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_acosh evaluates the hyperbolic arccosine function' )
  print ( '' )
  print ( '             X      arccosh(X)  r8_acosh(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arccosh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_acosh ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_acos ( x ):

#*****************************************************************************80
#
## r8_acos() evaluates the arc-cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  value = 0.5 * np.pi - r8_asin ( x )

  return value

def r8_acos_test ( ):

#*****************************************************************************80
#
## r8_acos_test() tests r8_acos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'r8_acos_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_acos evaluates the arc-cosine function' )
  print ( '' )
  print ( '             X      ARCCOS(X)  r8_acos(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arccos_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_acos ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_aint ( x ):

#*****************************************************************************80
#
## r8_aint() rounds an R8 argument towards 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  if ( x < 0.0 ):
    value = - np.floor ( abs ( x ) )
  else:
    value =   np.floor ( abs ( x ) )

  return value

def r8_aint_test ( ):

#*****************************************************************************80
#
## r8_aint_test() tests r8_aint().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_aint_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_aint() rounds an R8 towards 0.' )
  print ( '' )
  print ( '             X         AINT(X)  r8_aint(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_aint ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_ai ( x ):

#*****************************************************************************80
#
## r8_ai() evaluates the Airy function Ai of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  aifcs = np.array ( [ \
      -0.37971358496669997496197089469414E-01, \
      +0.59191888537263638574319728013777E-01, \
      +0.98629280577279975365603891044060E-03, \
      +0.68488438190765667554854830182412E-05, \
      +0.25942025962194713019489279081403E-07, \
      +0.61766127740813750329445749697236E-10, \
      +0.10092454172466117901429556224601E-12, \
      +0.12014792511179938141288033225333E-15, \
      +0.10882945588716991878525295466666E-18, \
      +0.77513772196684887039238400000000E-22, \
      +0.44548112037175638391466666666666E-25, \
      +0.21092845231692343466666666666666E-28, \
      +0.83701735910741333333333333333333E-32 ] )

  aigcs = np.array ( [ \
      +0.18152365581161273011556209957864E-01, \
      +0.21572563166010755534030638819968E-01, \
      +0.25678356987483249659052428090133E-03, \
      +0.14265214119792403898829496921721E-05, \
      +0.45721149200180426070434097558191E-08, \
      +0.95251708435647098607392278840592E-11, \
      +0.13925634605771399051150420686190E-13, \
      +0.15070999142762379592306991138666E-16, \
      +0.12559148312567778822703205333333E-19, \
      +0.83063073770821340343829333333333E-23, \
      +0.44657538493718567445333333333333E-26, \
      +0.19900855034518869333333333333333E-29, \
      +0.74702885256533333333333333333333E-33 ] )

  naif = r8_inits ( aifcs, 13, 0.1 * r8_mach ( 3 ) )
  naig = r8_inits ( aigcs, 13, 0.1 * r8_mach ( 3 ) )
  x3sml = r8_mach ( 3 ) ** 0.3334
  xmax = ( - 1.5 * np.log ( r8_mach ( 1 ) ) ) ** 0.6667
  xmax = xmax - xmax * np.log ( xmax ) / ( 4.0 * xmax * np.sqrt ( xmax ) + 1.0 ) - 0.01

  if ( x < - 1.0 ):
    xm, theta = r8_aimp ( x )
    value = xm * np.cos ( theta )
  elif ( abs ( x ) <= x3sml ):
    z = 0.0
    value = 0.375 + ( r8_csevl ( z, aifcs, naif ) \
      - x * ( 0.25 + r8_csevl ( z, aigcs, naig ) ) )
  elif ( x <= 1.0 ):
    z = x * x * x
    value = 0.375 + ( r8_csevl ( z, aifcs, naif ) \
      - x * ( 0.25 + r8_csevl ( z, aigcs, naig ) ) )
  elif ( x <= xmax ):
    value = r8_aie ( x ) * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )
  else:
    value = 0.0

  return value

def r8_ai_test ( ):

#*****************************************************************************80
#
## r8_ai_test() tests r8_ai().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_ai_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_ai() evaluates the Airy function Ai(X)' )
  print ( '' )
  print ( '             X      airy_ai(X)  r8_ai(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = airy_ai_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_ai ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_aid ( x ):

#*****************************************************************************80
#
## r8_aid() evaluates the derivative of the Airy function Ai of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  aifcs = np.array ( [ \
       0.105274612265314088088970057325134114, \
       0.011836136281529978442889292583980840, \
       0.000123281041732256643051689242469164, \
       0.000000622612256381399016825658693579, \
       0.000000001852988878441452950548140821, \
       0.000000000003633288725904357915995625, \
       0.000000000000005046217040440664768330, \
       0.000000000000000005223816555471480985, \
       0.000000000000000000004185745090748989, \
       0.000000000000000000000002672887324883, \
       0.000000000000000000000000001392128006, \
       0.000000000000000000000000000000602653, \
       0.000000000000000000000000000000000220 ] )

  aigcs = np.array ( [ \
       0.0212338781509186668523122276848937, \
       0.0863159303352144067524942809461604, \
       0.0017975947203832313578033963225230, \
       0.0000142654998755506932526620687495, \
       0.0000000594379952836832010488787064, \
       0.0000000001524033664794478945214786, \
       0.0000000000002645876603490435305100, \
       0.0000000000000003315624296815020591, \
       0.0000000000000000003139789757594792, \
       0.0000000000000000000002325767379040, \
       0.0000000000000000000000001384384231, \
       0.0000000000000000000000000000676629, \
       0.0000000000000000000000000000000276 ] )

  eta = 0.1 * r8_mach ( 3 )
  naif = r8_inits ( aifcs, 13, eta )
  naig = r8_inits ( aigcs, 13, eta )
  x3sml = r8_mach ( 3 ) ** 0.3334
  x2sml = np.sqrt ( r8_mach ( 3 ) )

  if ( x < - 1.0 ):
    xn, phi = r8_admp ( x )
    value = xn * np.cos ( phi )
  elif ( abs ( x ) <= x2sml ):
    x2 = 0.0
    x3 = 0.0
    value = ( x2 * ( 0.125 + r8_csevl ( x3, aifcs, naif ) ) \
      - r8_csevl ( x3, aigcs, naig ) ) - 0.25
  elif ( abs ( x ) <= x3sml ):
    x2 = x * x
    x3 = 0.0
    value = ( x2 * ( 0.125 + r8_csevl ( x3, aifcs, naif ) ) \
      - r8_csevl ( x3, aigcs, naig ) ) - 0.25
  elif ( x <= 1.0 ):
    x2 = x * x
    x3 = x * x * x
    value = ( x2 * ( 0.125 + r8_csevl ( x3, aifcs, naif ) ) \
      - r8_csevl ( x3, aigcs, naig ) ) - 0.25
  else:
    value = r8_aide ( x ) \
      * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )

  return value

def r8_aid_test ( ):

#*****************************************************************************80
#
## r8_aid_test() tests r8_aid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_aid_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_aid() evaluates the derivative of the Airy function Ai(x)' )
  print ( '' )
  print ( '             X     airy_aid(X)  r8_aid(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = airy_ai_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_aid ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_aide ( x ):

#*****************************************************************************80
#
## r8_aide(): exponentially scaled derivative, Airy function Ai of an R8 argument.
#
#  Discussion:
#
#    if X <= 0,
#      r8_aide ( X ) = r8_aid ( X )
#    else
#      r8_aide ( X ) = r8_aid ( X ) * np.exp ( 2/3 * X^(3/2) )
#
#    Thanks to Aleksandra Piper for pointing out a correction involving 
#    the computation of Z in the last two cases, 02 February 2012.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  aifcs = np.array ( [ \
       0.105274612265314088088970057325134114, \
        0.011836136281529978442889292583980840, \
        0.000123281041732256643051689242469164, \
        0.000000622612256381399016825658693579, \
        0.000000001852988878441452950548140821, \
        0.000000000003633288725904357915995625, \
        0.000000000000005046217040440664768330, \
        0.000000000000000005223816555471480985, \
        0.000000000000000000004185745090748989, \
        0.000000000000000000000002672887324883, \
        0.000000000000000000000000001392128006, \
        0.000000000000000000000000000000602653, \
        0.000000000000000000000000000000000220 ] )

  aigcs = np.array ( [ \
        0.0212338781509186668523122276848937, \
        0.0863159303352144067524942809461604, \
        0.0017975947203832313578033963225230, \
        0.0000142654998755506932526620687495, \
        0.0000000594379952836832010488787064, \
        0.0000000001524033664794478945214786, \
        0.0000000000002645876603490435305100, \
        0.0000000000000003315624296815020591, \
        0.0000000000000000003139789757594792, \
        0.0000000000000000000002325767379040, \
        0.0000000000000000000000001384384231, \
        0.0000000000000000000000000000676629, \
        0.0000000000000000000000000000000276 ] )

  aip1cs = np.array ( [ \
       0.0358865097808301537956710489261688, \
       0.0114668575627764898572700883121766, \
      -0.0007592073583861400301335647601603, \
       0.0000869517610893841271948619434021, \
      -0.0000128237294298591691789607600486, \
       0.0000022062695681038336934376250420, \
      -0.0000004222295185920749486945988432, \
       0.0000000874686415726348479356130376, \
      -0.0000000192773588418365388625693417, \
       0.0000000044668460054492719699777137, \
      -0.0000000010790108051948168015747466, \
       0.0000000002700029446696248083071434, \
      -0.0000000000696480108007915257318929, \
       0.0000000000184489907003246687076806, \
      -0.0000000000050027817358071698301149, \
       0.0000000000013852243366012168297298, \
      -0.0000000000003908218466657048253473, \
       0.0000000000001121536072524563451273, \
      -0.0000000000000326861522579502522443, \
       0.0000000000000096619179010090805752, \
      -0.0000000000000028934767442698434271, \
       0.0000000000000008770086661150897069, \
      -0.0000000000000002688046261195853754, \
       0.0000000000000000832498823872342992, \
      -0.0000000000000000260343254786947057, \
       0.0000000000000000082159528142686287, \
      -0.0000000000000000026150406704984940, \
       0.0000000000000000008390563463261051, \
      -0.0000000000000000002712685618629660, \
       0.0000000000000000000883333375271942, \
      -0.0000000000000000000289603206822333, \
       0.0000000000000000000095562185928676, \
      -0.0000000000000000000031727463569051, \
       0.0000000000000000000010595576960768, \
      -0.0000000000000000000003558253765402, \
       0.0000000000000000000001201334680517, \
      -0.0000000000000000000000407666883800, \
       0.0000000000000000000000139016944446, \
      -0.0000000000000000000000047628165730, \
       0.0000000000000000000000016391265551, \
      -0.0000000000000000000000005665491354, \
       0.0000000000000000000000001966381969, \
      -0.0000000000000000000000000685230229, \
       0.0000000000000000000000000239706939, \
      -0.0000000000000000000000000084166831, \
       0.0000000000000000000000000029659364, \
      -0.0000000000000000000000000010487947, \
       0.0000000000000000000000000003721150, \
      -0.0000000000000000000000000001324570, \
       0.0000000000000000000000000000472976, \
      -0.0000000000000000000000000000169405, \
       0.0000000000000000000000000000060855, \
      -0.0000000000000000000000000000021924, \
       0.0000000000000000000000000000007920, \
      -0.0000000000000000000000000000002869, \
       0.0000000000000000000000000000001042, \
      -0.0000000000000000000000000000000379 ] )

  aip2cs = np.array ( [ \
       0.0065457691989713756794276979067064, \
       0.0023833724120774591992772552886923, \
      -0.0000430700770220585862775012110584, \
       0.0000015629125858629202330785369063, \
      -0.0000000815417186162706965112501015, \
       0.0000000054103738056935918208008783, \
      -0.0000000004284130882614696528766222, \
       0.0000000000389497962832286424862198, \
      -0.0000000000039623161264979257658071, \
       0.0000000000004428184214405989602353, \
      -0.0000000000000536296527150689675318, \
       0.0000000000000069649872139936028200, \
      -0.0000000000000009619636286095319210, \
       0.0000000000000001403454967784808032, \
      -0.0000000000000000215097136525875715, \
       0.0000000000000000034471230632678283, \
      -0.0000000000000000005753907621819442, \
       0.0000000000000000000997001165824168, \
      -0.0000000000000000000178811436021458, \
       0.0000000000000000000033110307923551, \
      -0.0000000000000000000006315885529506, \
       0.0000000000000000000001238666952364, \
      -0.0000000000000000000000249324053394, \
       0.0000000000000000000000051426030999, \
      -0.0000000000000000000000010854236402, \
       0.0000000000000000000000002341316852, \
      -0.0000000000000000000000000515542099, \
       0.0000000000000000000000000115758841, \
      -0.0000000000000000000000000026479669, \
       0.0000000000000000000000000006165328, \
      -0.0000000000000000000000000001459931, \
       0.0000000000000000000000000000351331, \
      -0.0000000000000000000000000000085863, \
       0.0000000000000000000000000000021297, \
      -0.0000000000000000000000000000005358, \
       0.0000000000000000000000000000001367, \
      -0.0000000000000000000000000000000353 ] )

  eta = 0.1 * r8_mach ( 3 )
  naif = r8_inits ( aifcs, 13, eta )
  naig = r8_inits ( aigcs, 13, eta )
  naip1 = r8_inits ( aip1cs, 57, eta )
  naip2 = r8_inits ( aip2cs, 37, eta )
  x2sml = np.sqrt ( eta )
  x3sml = eta ** 0.3333
  x32sml = 1.3104 * x3sml * x3sml
  xbig = r8_mach ( 2 ) ** 0.6666

  if ( x < - 1.0 ):
    xn, phi = r8_admp ( x )
    value = xn * np.cos ( phi )
  elif ( abs ( x ) < x2sml ):
    x2 = 0.0
    x3 = 0.0
    value = ( x2 * ( 0.125 + r8_csevl ( x3, aifcs, naif ) ) \
      - r8_csevl ( x3, aigcs, naig ) ) - 0.25
    if ( x32sml < x ):
      value = value * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( abs ( x ) < x3sml ):
    x2 = x * x
    x3 = 0.0
    value = ( x2 * ( 0.125 + r8_csevl ( x3, aifcs, naif ) ) \
      - r8_csevl ( x3, aigcs, naig ) ) - 0.25
    if ( x32sml < x ):
      value = value * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )
    end
  elif ( x <= 1.0 ):
    x2 = x * x
    x3 = x * x
    value = ( x2 * ( 0.125 + r8_csevl ( x3, aifcs, naif ) ) \
      - r8_csevl ( x3, aigcs, naig ) ) - 0.25
    if ( x32sml < x ):
      value = value * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 4.0 ):
    sqrtx = np.sqrt ( x )
    z = ( 16.0  / ( x * sqrtx ) - 9.0 ) / 7.0
    value = ( - 0.28125 - r8_csevl ( z, aip1cs, naip1 ) ) * np.sqrt ( sqrtx )
  elif ( x < xbig ):
    sqrtx = np.sqrt ( x )
    z = 16.0  / ( x * sqrtx ) - 1.0
    value = ( - 0.28125 - r8_csevl ( z, aip2cs, naip2 ) ) * np.sqrt ( sqrtx )
  else:
    sqrtx = np.sqrt ( x )
    z = - 1.0
    value = ( - 0.28125 - r8_csevl ( z, aip2cs, naip2 ) ) * np.sqrt ( sqrtx )

  return value

def r8_aie ( x ):

#*****************************************************************************80
#
## r8_aie() evaluates the exponentially scaled Airy function Ai of an R8 argument.
#
#  Discussion:
#
#    if X <= 0,
#      r8_aie ( X ) = r8_ai ( X )
#    else
#      r8_aie ( X ) = r8_ai ( X ) * np.exp ( 2/3 * X^(3/2) )
#
#    Thanks to Aleksandra Piper for pointing out a correction involving a
#    missing assignment to SQRTX, 27 January 2012.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  aifcs = np.array ( [ \
      -0.37971358496669997496197089469414E-01, \
      +0.59191888537263638574319728013777E-01, \
      +0.98629280577279975365603891044060E-03, \
      +0.68488438190765667554854830182412E-05, \
      +0.25942025962194713019489279081403E-07, \
      +0.61766127740813750329445749697236E-10, \
      +0.10092454172466117901429556224601E-12, \
      +0.12014792511179938141288033225333E-15, \
      +0.10882945588716991878525295466666E-18, \
      +0.77513772196684887039238400000000E-22, \
      +0.44548112037175638391466666666666E-25, \
      +0.21092845231692343466666666666666E-28, \
      +0.83701735910741333333333333333333E-32 ] )

  aigcs = np.array ( [ \
      +0.18152365581161273011556209957864E-01, \
      +0.21572563166010755534030638819968E-01, \
      +0.25678356987483249659052428090133E-03, \
      +0.14265214119792403898829496921721E-05, \
      +0.45721149200180426070434097558191E-08, \
      +0.95251708435647098607392278840592E-11, \
      +0.13925634605771399051150420686190E-13, \
      +0.15070999142762379592306991138666E-16, \
      +0.12559148312567778822703205333333E-19, \
      +0.83063073770821340343829333333333E-23, \
      +0.44657538493718567445333333333333E-26, \
      +0.19900855034518869333333333333333E-29, \
      +0.74702885256533333333333333333333E-33 ] )

  aip1cs = np.array ( [ \
      -0.2146951858910538455460863467778E-01, \
      -0.7535382535043301166219720865565E-02, \
      +0.5971527949026380852035388881994E-03, \
      -0.7283251254207610648502368291548E-04, \
      +0.1110297130739299666517381821140E-04, \
      -0.1950386152284405710346930314033E-05, \
      +0.3786973885159515193885319670057E-06, \
      -0.7929675297350978279039072879154E-07, \
      +0.1762247638674256075568420122202E-07, \
      -0.4110767539667195045029896593893E-08, \
      +0.9984770057857892247183414107544E-09, \
      -0.2510093251387122211349867730034E-09, \
      +0.6500501929860695409272038601725E-10, \
      -0.1727818405393616515478877107366E-10, \
      +0.4699378842824512578362292872307E-11, \
      -0.1304675656297743914491241246272E-11, \
      +0.3689698478462678810473948382282E-12, \
      -0.1061087206646806173650359679035E-12, \
      +0.3098414384878187438660210070110E-13, \
      -0.9174908079824139307833423547851E-14, \
      +0.2752049140347210895693579062271E-14, \
      -0.8353750115922046558091393301880E-15, \
      +0.2563931129357934947568636168612E-15, \
      -0.7950633762598854983273747289822E-16, \
      +0.2489283634603069977437281175644E-16, \
      -0.7864326933928735569664626221296E-17, \
      +0.2505687311439975672324470645019E-17, \
      -0.8047420364163909524537958682241E-18, \
      +0.2604097118952053964443401104392E-18, \
      -0.8486954164056412259482488834184E-19, \
      +0.2784706882142337843359429186027E-19, \
      -0.9195858953498612913687224151354E-20, \
      +0.3055304318374238742247668225583E-20, \
      -0.1021035455479477875902177048439E-20, \
      +0.3431118190743757844000555680836E-21, \
      -0.1159129341797749513376922463109E-21, \
      +0.3935772844200255610836268229154E-22, \
      -0.1342880980296717611956718989038E-22, \
      +0.4603287883520002741659190305314E-23, \
      -0.1585043927004064227810772499387E-23, \
      +0.5481275667729675908925523755008E-24, \
      -0.1903349371855047259064017948945E-24, \
      +0.6635682302374008716777612115968E-25, \
      -0.2322311650026314307975200986453E-25, \
      +0.8157640113429179313142743695359E-26, \
      -0.2875824240632900490057489929557E-26, \
      +0.1017329450942901435079714319018E-26, \
      -0.3610879108742216446575703490559E-27, \
      +0.1285788540363993421256640342698E-27, \
      -0.4592901037378547425160693022719E-28, \
      +0.1645597033820713725812102485333E-28, \
      -0.5913421299843501842087920271360E-29, \
      +0.2131057006604993303479369509546E-29, \
      -0.7701158157787598216982761745066E-30, \
      +0.2790533307968930417581783777280E-30, \
      -0.1013807715111284006452241367039E-30, \
      +0.3692580158719624093658286216533E-31 ] )

  aip2cs = np.array ( [ \
      -0.174314496929375513390355844011E-02, \
      -0.167893854325541671632190613480E-02, \
      +0.359653403352166035885983858114E-04, \
      -0.138081860273922835457399383100E-05, \
      +0.741122807731505298848699095233E-07, \
      -0.500238203900133013130422866325E-08, \
      +0.400693917417184240675446866355E-09, \
      -0.367331242795905044199318496207E-10, \
      +0.376034439592373852439592002918E-11, \
      -0.422321332718747538026564938968E-12, \
      +0.513509454033657070919618754120E-13, \
      -0.669095850390477595651681356676E-14, \
      +0.926667545641290648239550724382E-15, \
      -0.135514382416070576333397356591E-15, \
      +0.208115496312830995299006549335E-16, \
      -0.334116499159176856871277570256E-17, \
      +0.558578584585924316868032946585E-18, \
      -0.969219040152365247518658209109E-19, \
      +0.174045700128893206465696557738E-19, \
      -0.322640979731130400247846333098E-20, \
      +0.616074471106625258533259618986E-21, \
      -0.120936347982490059076420676266E-21, \
      +0.243632763310138108261570095786E-22, \
      -0.502914221497457468943403144533E-23, \
      +0.106224175543635689495470626133E-23, \
      -0.229284284895989241509856324266E-24, \
      +0.505181733929503744986884778666E-25, \
      -0.113498123714412404979793920000E-25, \
      +0.259765565985606980698374144000E-26, \
      -0.605124621542939506172231679999E-27, \
      +0.143359777966772800720295253333E-27, \
      -0.345147757060899986280721066666E-28, \
      +0.843875190213646740427025066666E-29, \
      -0.209396142298188169434453333333E-29, \
      +0.527008873478945503182848000000E-30, \
      -0.134457433014553385789030399999E-30, \
      +0.347570964526601147340117333333E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  naif = r8_inits ( aifcs, 13, eta )
  naig = r8_inits ( aigcs, 13, eta )
  naip1 = r8_inits ( aip1cs, 57, eta )
  naip2 = r8_inits ( aip2cs, 37, eta )
  x3sml = eta ** 0.3333
  x32sml = 1.3104 * x3sml * x3sml
  xbig = r8_mach ( 2 ) ** 0.6666

  if ( x < - 1.0 ):
    xm, theta = r8_aimp ( x )
    value = xm * np.cos ( theta )
  elif ( 0.0 <= x and x <= x32sml ):
    z = 0.0
    value = 0.3750 + ( r8_csevl ( z, aifcs, naif ) \
      - x * ( 0.25 + r8_csevl ( z, aigcs, naig ) ) )
  elif ( abs ( x ) <= x3sml ):
    z = 0.0
    value = 0.3750 + ( r8_csevl ( z, aifcs, naif ) \
      - x * ( 0.25 + r8_csevl ( z, aigcs, naig ) ) )
    value = value * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 1.0 ):
    z = x * x * x
    value = 0.3750 + ( r8_csevl ( z, aifcs, naif ) \
      - x * ( 0.25 + r8_csevl ( z, aigcs, naig ) ) )
    value = value * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 4.0 ):
    sqrtx = np.sqrt ( x )
    z = ( 16.0 / ( x * sqrtx ) - 9.0 ) / 7.0
    value = ( 0.28125 + r8_csevl ( z, aip1cs, naip1 ) ) \
      / np.sqrt ( sqrtx )
  elif ( x < xbig ):
    sqrtx = np.sqrt ( x )
    z = 16.0 / ( x * sqrtx ) - 1.0
    value = ( 0.28125 + r8_csevl ( z, aip2cs, naip2 ) ) \
      / np.sqrt ( sqrtx )
  else:
    sqrtx = np.sqrt ( x )
    z = - 1.0
    value = ( 0.28125 + r8_csevl ( z, aip2cs, naip2 ) ) \
      / np.sqrt ( sqrtx )

  return value

def r8_aimp ( x ):

#*****************************************************************************80
#
## r8_aimp() evaluates the modulus and phase of the Airy function.
#
#  Description:
#
#    This function must only be called when X <= -1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real AMPL, PHI, the modulus and phase of the
#    Airy function.
#
  import numpy as np

  am20cs = np.array ( [ \
      +0.108716749086561856615730588125E-01, \
      +0.369489228982663555091728665146E-03, \
      +0.440680100484689563667507001327E-05, \
      +0.143686762361911153929183952833E-06, \
      +0.824275552390078308670628855353E-08, \
      +0.684426758893661606173927278180E-09, \
      +0.739566697282739287731004740213E-10, \
      +0.974595633696825017638702600847E-11, \
      +0.150076885829405775650973119497E-11, \
      +0.262147910221527634206252854802E-12, \
      +0.508354111376487180357278966914E-13, \
      +0.107684753358811440492985997070E-13, \
      +0.246091286618433429335914062617E-14, \
      +0.600786380358656418436110373550E-15, \
      +0.155449156102388071150651388384E-15, \
      +0.423535125035576604426382780182E-16, \
      +0.120862166289299840154401109189E-16, \
      +0.359609651214658240861499706423E-17, \
      +0.111134218386395638261774604677E-17, \
      +0.355559532432366609893680289225E-18, \
      +0.117433021600139309998766947387E-18, \
      +0.399397454661077561389162200966E-19, \
      +0.139576671528916310425606325640E-19, \
      +0.500240055309236041393459280716E-20, \
      +0.183552760958132679184834866457E-20, \
      +0.688490998179202743197790112404E-21, \
      +0.263631035611417012359996885105E-21, \
      +0.102924890237338360287153563785E-21, \
      +0.409246966671594885489762960571E-22, \
      +0.165558573406734651039727903828E-22, \
      +0.680797467063033356116599685727E-23, \
      +0.284326559934079832419751134476E-23, \
      +0.120507398348965255097287818819E-23, \
      +0.517961243287505217976613610424E-24, \
      +0.225622613427562816303268640887E-24, \
      +0.995418801147745168832117078246E-25, \
      +0.444551696397342424308280582053E-25, \
      +0.200865195461501101425916097338E-25, \
      +0.917786344151775165973885645402E-26, \
      +0.423872958105589240661672197948E-26, \
      +0.197789272007846092370846251490E-26, \
      +0.932116351284620665680435253373E-27, \
      +0.443482133249918099955611379722E-27, \
      +0.212945672365573895594589552837E-27, \
      +0.103158569651075977552209344907E-27, \
      +0.504023773022591199157904590029E-28, \
      +0.248301304570155945304046541005E-28, \
      +0.123301783128562196054198238560E-28, \
      +0.617033449920521746121976730507E-29, \
      +0.311092617415918897233869792213E-29, \
      +0.157983085201706173015269071503E-29, \
      +0.807931987538283607678121339092E-30, \
      +0.415997394138667562722951360052E-30, \
      +0.215610934097716900471935862504E-30, \
      +0.112468857265869178296752823613E-30, \
      +0.590331560632838091123040811797E-31, \
      +0.311735667692928562046280505333E-31 ] )

  am21cs = np.array ( [ \
      +0.592790266721309588375717482814E-02, \
      +0.200569405393165186428695217690E-02, \
      +0.911081850262275893553072526291E-04, \
      +0.849894306372047155633172107475E-05, \
      +0.113297908976913076637929215494E-05, \
      +0.187517946100666496180950627804E-06, \
      +0.359306519018245832699035211192E-07, \
      +0.765757714071683864039093517470E-08, \
      +0.176999967168039173925953460744E-08, \
      +0.436259555654598932720546585535E-09, \
      +0.113291641337853230035520085219E-09, \
      +0.307257690982419244137868398126E-10, \
      +0.864482416482201075541200465766E-11, \
      +0.251015250060924402115104562212E-11, \
      +0.749102496764440371601802227751E-12, \
      +0.228996928487994073089565214432E-12, \
      +0.715113658927987694949327491175E-13, \
      +0.227607924959566841946395165061E-13, \
      +0.736942142760886513969953227782E-14, \
      +0.242328675267827490463991742006E-14, \
      +0.808153774548239869283406558403E-15, \
      +0.273008079804356086659174563386E-15, \
      +0.933236070891385318473519474326E-16, \
      +0.322508099681084622213867546973E-16, \
      +0.112581932346444541217757573416E-16, \
      +0.396699463986938821660259459530E-17, \
      +0.141006567944319504660865034527E-17, \
      +0.505302086537851213375537393032E-18, \
      +0.182461523215945141197999102789E-18, \
      +0.663584568262130466928029121642E-19, \
      +0.242963731631276179741747455826E-19, \
      +0.895238915123687802013669922963E-20, \
      +0.331845289350050791260229250755E-20, \
      +0.123706196188658315384437905922E-20, \
      +0.463636677012390840306767734243E-21, \
      +0.174653135947764475469758765989E-21, \
      +0.661116810234991176307910643111E-22, \
      +0.251409918994072486176125666459E-22, \
      +0.960274995571732568694034386998E-23, \
      +0.368324952289296395686436898078E-23, \
      +0.141843138269159136145535939553E-23, \
      +0.548342674276935830106345800990E-24, \
      +0.212761054623118806650372562616E-24, \
      +0.828443700849418591487734760953E-25, \
      +0.323670563926127001421028600927E-25, \
      +0.126868882963286057355055062493E-25, \
      +0.498843818992121626935068934362E-26, \
      +0.196734584467649390967119381790E-26, \
      +0.778135971020326957713212064836E-27, \
      +0.308633941498911152919192968451E-27, \
      +0.122744647045453119789338037234E-27, \
      +0.489431279134292205885241216204E-28, \
      +0.195646879802909821175925099724E-28, \
      +0.783988952922426171166311492266E-29, \
      +0.314896914002484223748298978099E-29, \
      +0.126769763137250681307067842559E-29, \
      +0.511470691906900141641632107724E-30, \
      +0.206801709795538770250900316706E-30, \
      +0.837891344768519001325996867583E-31, \
      +0.340168991971489802052339079577E-31 ] )

  am22cs = np.array ( [ \
      -0.156284448062534112753545828583E-01, \
      +0.778336445239681307018943100334E-02, \
      +0.867057770477189528406072812110E-03, \
      +0.156966273156113719469953482266E-03, \
      +0.356396257143286511324100666302E-04, \
      +0.924598335425043154495080090994E-05, \
      +0.262110161850422389523194982066E-05, \
      +0.791882216516012561489469982263E-06, \
      +0.251041527921011847803162690862E-06, \
      +0.826522320665407734472997712940E-07, \
      +0.280571166281305264396384290014E-07, \
      +0.976821090484680786674631273890E-08, \
      +0.347407923227710343287279035573E-08, \
      +0.125828132169836914219092738164E-08, \
      +0.462988260641895264497330784625E-09, \
      +0.172728258813604072468143128696E-09, \
      +0.652319200131154135148574124970E-10, \
      +0.249047168520982056019881087112E-10, \
      +0.960156820553765948078189890126E-11, \
      +0.373448002067726856974776596757E-11, \
      +0.146417565032053391722216189678E-11, \
      +0.578265471168512825475827881553E-12, \
      +0.229915407244706118560254184494E-12, \
      +0.919780711231997257150883662365E-13, \
      +0.370060068813090065807504045556E-13, \
      +0.149675761698672987823326345205E-13, \
      +0.608361194938461148720451399443E-14, \
      +0.248404087115121397635425326873E-14, \
      +0.101862476526769080727914465339E-14, \
      +0.419383856352753989429640310957E-15, \
      +0.173318901762930756149702493501E-15, \
      +0.718821902388508517820445406811E-16, \
      +0.299123633598403607712470896113E-16, \
      +0.124868990433238627855713110880E-16, \
      +0.522829344609483661928651193632E-17, \
      +0.219532961724713396595998454359E-17, \
      +0.924298325229777281154410024332E-18, \
      +0.390157708236091407825543197309E-18, \
      +0.165093892693863707213759030367E-18, \
      +0.700221815715994367565716554487E-19, \
      +0.297651833616786915573214963506E-19, \
      +0.126796539086902072571134261229E-19, \
      +0.541243400697077628687581725061E-20, \
      +0.231487350218155252296382133283E-20, \
      +0.991920288386566563462623851167E-21, \
      +0.425803015323732357158897608174E-21, \
      +0.183101842973024501678402003088E-21, \
      +0.788678712311075375564526811022E-22, \
      +0.340254607386229874956582997235E-22, \
      +0.147020881405712530791860892535E-22, \
      +0.636211018324916957733348071767E-23, \
      +0.275707050680980721919395987768E-23, \
      +0.119645858090104071356261780457E-23, \
      +0.519912545729242147981768210567E-24, \
      +0.226217674847104475260575286850E-24, \
      +0.985526113754431819448565068283E-25, \
      +0.429870630332508717223681286187E-25, \
      +0.187723641661580639829657670189E-25, \
      +0.820721941772842137268801052115E-26, \
      +0.359214665604615507812767944463E-26, \
      +0.157390594612773315611458940587E-26, \
      +0.690329781039333834965319153586E-27, \
      +0.303092079078968534607859331415E-27, \
      +0.133204934160481219185689121944E-27, \
      +0.585978836851523490117937981442E-28, \
      +0.258016868489487806338425080457E-28, \
      +0.113712433637283667223632182863E-28, \
      +0.501592557226068509236430548549E-29, \
      +0.221445829395509373322569708484E-29, \
      +0.978470283886507289984691416411E-30, \
      +0.432695414934180170112000952983E-30, \
      +0.191497288193994570612929860440E-30, \
      +0.848164622402392354171298331562E-31, \
      +0.375947065173955919947455052934E-31 ] )

  ath0cs = np.array ( [ \
      -0.8172601764161634499840208700543E-01, \
      -0.8004012824788273287596481113068E-03, \
      -0.3186525268782113203795553628242E-05, \
      -0.6688388266477509330741698865033E-07, \
      -0.2931759284994564516506822463184E-08, \
      -0.2011263760883621669049030307186E-09, \
      -0.1877522678055973426074008166652E-10, \
      -0.2199637137704601251899002199848E-11, \
      -0.3071616682592272449025746605586E-12, \
      -0.4936140553673418361025600985389E-13, \
      -0.8902833722583660416935236969866E-14, \
      -0.1768987764615272613656814199467E-14, \
      -0.3817868689032277014678199609600E-15, \
      -0.8851159014819947594156286509984E-16, \
      -0.2184818181414365953149677679568E-16, \
      -0.5700849046986452380599442295119E-17, \
      -0.1563121122177875392516031795495E-17, \
      -0.4481437996768995067906688776353E-18, \
      -0.1337794883736188022044566044098E-18, \
      -0.4143340036874114453776852445442E-19, \
      -0.1327263385718805025080481164652E-19, \
      -0.4385728589128440522215756835955E-20, \
      -0.1491360695952818067686201743956E-20, \
      -0.5208104738630711377154238188773E-21, \
      -0.1864382222390498923872526604979E-21, \
      -0.6830263751167969012975435381881E-22, \
      -0.2557117058029329629296207591347E-22, \
      -0.9770158640254300218246907254046E-23, \
      -0.3805161433416679084068428254886E-23, \
      -0.1509022750737054063493926482995E-23, \
      -0.6087551341242424929005568014525E-24, \
      -0.2495879513809711495425982124058E-24, \
      -0.1039157654581920948909588084274E-24, \
      -0.4390235913976846536974594969051E-25, \
      -0.1880790678447990211675826820582E-25, \
      -0.8165070764199462948863022205753E-26, \
      -0.3589944503749750514266435585041E-26, \
      -0.1597658126632132872981291608708E-26, \
      -0.7193250175703823969113802835305E-27, \
      -0.3274943012727856506209351132721E-27, \
      -0.1507042445783690665816975047272E-27, \
      -0.7006624198319904717843967949140E-28, \
      -0.3289907402983718226528815678356E-28, \
      -0.1559518084365146526445322711496E-28, \
      -0.7460690508208254582833851119721E-29, \
      -0.3600877034824662020563277249431E-29, \
      -0.1752851437473772257350402219197E-29, \
      -0.8603275775188512909623778628724E-30, \
      -0.4256432603226946534668039480105E-30, \
      -0.2122161865044262927723650698206E-30, \
      -0.1065996156704879052472060798561E-30, \
      -0.5393568608816949116410688086892E-31, \
      -0.2748174851043954822278496517870E-31 ] )

  ath1cs = np.array ( [ \
      -0.6972849916208883845888148415037E-01, \
      -0.5108722790650044987073448077961E-02, \
      -0.8644335996989755094525334749512E-04, \
      -0.5604720044235263542188698916125E-05, \
      -0.6045735125623897409156376640077E-06, \
      -0.8639802632488334393219721138499E-07, \
      -0.1480809484309927157147782480780E-07, \
      -0.2885809334577236039999449908712E-08, \
      -0.6191631975665699609309191231800E-09, \
      -0.1431992808860957830931365259879E-09, \
      -0.3518141102137214721504616874321E-10, \
      -0.9084761919955078290070339808051E-11, \
      -0.2446171672688598449343283664767E-11, \
      -0.6826083203213446240828996710264E-12, \
      -0.1964579931194940171278546257802E-12, \
      -0.5808933227139693164009191265856E-13, \
      -0.1759042249527441992795400959024E-13, \
      -0.5440902932714896613632538945319E-14, \
      -0.1715247407486806802622358519451E-14, \
      -0.5500929233576991546871101847161E-15, \
      -0.1791878287739317259495152638754E-15, \
      -0.5920372520086694197778411062231E-16, \
      -0.1981713027876483962470972206590E-16, \
      -0.6713232347016352262049984343790E-17, \
      -0.2299450243658281116122358619832E-17, \
      -0.7957300928236376595304637145634E-18, \
      -0.2779994027291784157172290233739E-18, \
      -0.9798924361326985224406795480814E-19, \
      -0.3482717006061574386702645565849E-19, \
      -0.1247489122558599057173300058084E-19, \
      -0.4501210041478228113487751824452E-20, \
      -0.1635346244013352135596114164667E-20, \
      -0.5980102897780336268098762265941E-21, \
      -0.2200246286286123454028196295475E-21, \
      -0.8142463073515085897408205291519E-22, \
      -0.3029924773660042537432330709674E-22, \
      -0.1133390098574623537722943969689E-22, \
      -0.4260766024749295719283049889791E-23, \
      -0.1609363396278189718797500634453E-23, \
      -0.6106377190825026293045330444287E-24, \
      -0.2326954318021694061836577887573E-24, \
      -0.8903987877472252604474129558186E-25, \
      -0.3420558530005675024117914752341E-25, \
      -0.1319026715257272659017212100607E-25, \
      -0.5104899493612043091316191177386E-26, \
      -0.1982599478474547451242444663466E-26, \
      -0.7725702356880830535636111851519E-27, \
      -0.3020234733664680100815776863573E-27, \
      -0.1184379739074169993712946380800E-27, \
      -0.4658430227922308520573252840106E-28, \
      -0.1837554188100384647157502006613E-28, \
      -0.7268566894427990953321876684800E-29, \
      -0.2882863120391468135527089875626E-29, \
      -0.1146374629459906350417591664639E-29, \
      -0.4570031437748533058179991688533E-30, \
      -0.1826276602045346104809934028799E-30, \
      -0.7315349993385250469111066350933E-31, \
      -0.2936925599971429781637815773866E-31 ] )

  ath2cs = np.array ( [ \
      +0.4405273458718778997061127057775E-02, \
      -0.3042919452318454608483844239873E-01, \
      -0.1385653283771793791602692842653E-02, \
      -0.1804443908954952302670486910952E-03, \
      -0.3380847108327308671057465323618E-04, \
      -0.7678183535229023055257676817765E-05, \
      -0.1967839443716035324690935417077E-05, \
      -0.5483727115877700361586143659281E-06, \
      -0.1625461550532612452712696212258E-06, \
      -0.5053049981268895015277637842078E-07, \
      -0.1631580701124066881183851715617E-07, \
      -0.5434204112348517507963436694817E-08, \
      -0.1857398556409900325763850109630E-08, \
      -0.6489512033326108816213513640676E-09, \
      -0.2310594885800944720482995987079E-09, \
      -0.8363282183204411682819329546745E-10, \
      -0.3071196844890191462660661303891E-10, \
      -0.1142367142432716819409514579892E-10, \
      -0.4298116066345803065822470108971E-11, \
      -0.1633898699596715440601646086632E-11, \
      -0.6269328620016619432123443754076E-12, \
      -0.2426052694816257357356159203991E-12, \
      -0.9461198321624039090742527765052E-13, \
      -0.3716060313411504806847798281269E-13, \
      -0.1469155684097526763170138810309E-13, \
      -0.5843694726140911944556401363094E-14, \
      -0.2337502595591951298832675034934E-14, \
      -0.9399231371171435401160167358411E-15, \
      -0.3798014669372894500076335263715E-15, \
      -0.1541731043984972524883443681775E-15, \
      -0.6285287079535307162925662365202E-16, \
      -0.2572731812811455424755383992774E-16, \
      -0.1057098119354017809340974866555E-16, \
      -0.4359080267402696966695992699964E-17, \
      -0.1803634315959978013953176945540E-17, \
      -0.7486838064380536821719431676914E-18, \
      -0.3117261367347604656799597209985E-18, \
      -0.1301687980927700734792871620696E-18, \
      -0.5450527587519522468973883909909E-19, \
      -0.2288293490114231872268635931903E-19, \
      -0.9631059503829538655655060440088E-20, \
      -0.4063281001524614089092195416434E-20, \
      -0.1718203980908026763900413858510E-20, \
      -0.7281574619892536367415322473328E-21, \
      -0.3092352652680643127960680345790E-21, \
      -0.1315917855965440490383417023254E-21, \
      -0.5610606786087055512664907412668E-22, \
      -0.2396621894086355206020304337895E-22, \
      -0.1025574332390581200832954423924E-22, \
      -0.4396264138143656476403607323663E-23, \
      -0.1887652998372577373342508719450E-23, \
      -0.8118140359576807603579433230445E-24, \
      -0.3496734274366286856375952089214E-24, \
      -0.1508402925156873215171751475867E-24, \
      -0.6516268284778671059787773834341E-25, \
      -0.2818945797529207424505942114583E-25, \
      -0.1221127596512262744598094464505E-25, \
      -0.5296674341169867168620011705073E-26, \
      -0.2300359270773673431358870971744E-26, \
      -0.1000279482355367494781220348930E-26, \
      -0.4354760404180879394806893162179E-27, \
      -0.1898056134741477522515482827030E-27, \
      -0.8282111868712974697554009309315E-28, \
      -0.3617815493066569006586213484374E-28, \
      -0.1582018896178003654858941843636E-28, \
      -0.6925068597802270011772820383247E-29, \
      -0.3034390239778629128908629727335E-29, \
      -0.1330889568166725224761977446509E-29, \
      -0.5842848522173090120487606971706E-30, \
      -0.2567488423238302631121274357678E-30, \
      -0.1129232322268882185791505819151E-30, \
      -0.4970947029753336916550570105023E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  nam20 = r8_inits ( am20cs, 57, eta )
  nath0 = r8_inits ( ath0cs, 53, eta )
  nam21 = r8_inits ( am21cs, 60, eta )
  nath1 = r8_inits ( ath1cs, 58, eta )
  nam22 = r8_inits ( am22cs, 74, eta )
  nath2 = r8_inits ( ath2cs, 72, eta )
  xsml = - ( 128.0 / r8_mach ( 3 ) ) ** 0.3333

  if ( x <= xsml ):
    z = 1.0
    ampl = 0.3125 + r8_csevl ( z, am20cs, nam20 )
    theta = - 0.625 + r8_csevl ( z, ath0cs, nath0 )
  elif ( x < - 4.0 ):
    z = 128.0 / x / x / x + 1.0
    ampl = 0.3125 + r8_csevl ( z, am20cs, nam20 )
    theta = - 0.625 + r8_csevl ( z, ath0cs, nath0 )
  elif ( x < - 2.0 ):
    z = ( 128.0 / x / x / x + 9.0 ) / 7.0
    ampl = 0.3125 + r8_csevl ( z, am21cs, nam21 )
    theta = - 0.625 + r8_csevl ( z, ath1cs, nath1 )
  elif ( x <= - 1.0 ):
    z = ( 16.0 / x / x / x + 9.0 ) / 7.0
    ampl = 0.3125 + r8_csevl ( z, am22cs, nam22 )
    theta = - 0.625 + r8_csevl ( z, ath2cs, nath2 )
  else:
    print ( '' )
    print ( 'r8_aimp - Fatal error!' )
    print ( '  -1.0 < X.' )
    raise Exception ( 'r8_aimp - Fatal error!' )

  sqrtx = np.sqrt ( - x )
  ampl = np.sqrt ( ampl / sqrtx )
  theta = 0.25 * np.pi - x * sqrtx * theta

  return ampl, theta

def r8_bi ( x ):

#*****************************************************************************80
#
## r8_bi() evaluates the Airy function Bi of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  bifcs = np.array ( [ \
    -0.16730216471986649483537423928176E-01, \
    +0.10252335834249445611426362777757, \
    +0.17083092507381516539429650242013E-02, \
    +0.11862545467744681179216459210040E-04, \
    +0.44932907017792133694531887927242E-07, \
    +0.10698207143387889067567767663628E-09, \
    +0.17480643399771824706010517628573E-12, \
    +0.20810231071761711025881891834399E-15, \
    +0.18849814695665416509927971733333E-18, \
    +0.13425779173097804625882666666666E-21, \
    +0.77159593429658887893333333333333E-25, \
    +0.36533879617478566399999999999999E-28, \
    +0.14497565927953066666666666666666E-31 ] )

  bif2cs = np.array ( [ \
    +0.0998457269381604104468284257993, \
    +0.47862497786300553772211467318231, \
    +0.25155211960433011771324415436675E-01, \
    +0.58206938852326456396515697872216E-03, \
    +0.74997659644377865943861457378217E-05, \
    +0.61346028703493836681403010356474E-07, \
    +0.34627538851480632900434268733359E-09, \
    +0.14288910080270254287770846748931E-11, \
    +0.44962704298334641895056472179200E-14, \
    +0.11142323065833011708428300106666E-16, \
    +0.22304791066175002081517866666666E-19, \
    +0.36815778736393142842922666666666E-22, \
    +0.50960868449338261333333333333333E-25, \
    +0.60003386926288554666666666666666E-28, \
    +0.60827497446570666666666666666666E-31 ] )

  bigcs = np.array ( [ \
    +0.22466223248574522283468220139024E-01, \
    +0.37364775453019545441727561666752E-01, \
    +0.44476218957212285696215294326639E-03, \
    +0.24708075636329384245494591948882E-05, \
    +0.79191353395149635134862426285596E-08, \
    +0.16498079851827779880887872402706E-10, \
    +0.24119906664835455909247501122841E-13, \
    +0.26103736236091436985184781269333E-16, \
    +0.21753082977160323853123792000000E-19, \
    +0.14386946400390433219483733333333E-22, \
    +0.77349125612083468629333333333333E-26, \
    +0.34469292033849002666666666666666E-29, \
    +0.12938919273216000000000000000000E-32 ] )

  big2cs = np.array ( [ \
    +0.033305662145514340465176188111647, \
    +0.161309215123197067613287532084943, \
    +0.631900730961342869121615634921173E-02, \
    +0.118790456816251736389780192304567E-03, \
    +0.130453458862002656147116485012843E-05, \
    +0.937412599553521729546809615508936E-08, \
    +0.474580188674725153788510169834595E-10, \
    +0.178310726509481399800065667560946E-12, \
    +0.516759192784958180374276356640000E-15, \
    +0.119004508386827125129496251733333E-17, \
    +0.222982880666403517277063466666666E-20, \
    +0.346551923027689419722666666666666E-23, \
    +0.453926336320504514133333333333333E-26, \
    +0.507884996513522346666666666666666E-29, \
    +0.491020674696533333333333333333333E-32 ] )

  eta = 0.1 * r8_mach ( 3 )
  nbif = r8_inits ( bifcs, 13, eta )
  nbig = r8_inits ( bigcs, 13, eta )
  nbif2 = r8_inits ( bif2cs, 15, eta )
  nbig2 = r8_inits ( big2cs, 15, eta )
  x3sml = eta ** 0.3333
  xmax = ( 1.5 * np.log ( r8_mach ( 2 ) ) ) ** 0.6666

  if ( x < - 1.0 ):
    xm, theta = r8_aimp ( x )
    value = xm * np.sin ( theta )
  elif ( abs ( x ) <= x3sml ):
    z = 0.0
    value = 0.625 + r8_csevl ( z, bifcs, nbif ) \
      + x * ( 0.4375 + r8_csevl ( z, bigcs, nbig ) )
  elif ( x <= 1.0 ):
    z = x * x * x
    value = 0.625 + r8_csevl ( z, bifcs, nbif ) \
      + x * ( 0.4375 + r8_csevl ( z, bigcs, nbig ) )
  elif ( x <= 2.0 ):
    z = ( 2.0 * x * x * x - 9.0 ) / 7.0
    value = 1.125 + r8_csevl ( z, bif2cs, nbif2 ) \
      + x * ( 0.625 + r8_csevl ( z, big2cs, nbig2 ) )
  else:
    value = r8_bie ( x ) * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )

  return value

def r8_bi_test ( ):

#*****************************************************************************80
#
## r8_bi_test() tests r8_bi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_bi_test():' )
  print ( '  r8_bi() evaluates the Airy Bi(X) function' )
  print ( '' )
  print ( '             X      airy_bi(X)  r8_bi(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = airy_bi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_bi ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_bid ( x ):

#*****************************************************************************80
#
## r8_bid() evaluates the derivative of the Airy function Bi of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  bif2cs = np.array ( [ \
       0.32349398760352203352119193596266015, \
       0.08629787153556355913888835323811100, \
       0.00299402555265539742613821050727155, \
       0.00005143052836466163720464316950821, \
       0.00000052584025003681146026033098613, \
       0.00000000356175137395770028102730600, \
       0.00000000001714686400714584830518308, \
       0.00000000000006166351969232555406693, \
       0.00000000000000017191082154315985806, \
       0.00000000000000000038236889518803943, \
       0.00000000000000000000069424173624884, \
       0.00000000000000000000000104833932510, \
       0.00000000000000000000000000133721972, \
       0.00000000000000000000000000000145986, \
       0.00000000000000000000000000000000138 ] )

  bifcs = np.array ( [ \
       0.115353679082857024267474446284908879, \
       0.020500789404919287530357789445940252, \
       0.000213529027890287581892679619451158, \
       0.000001078396061467683042209155523569, \
       0.000000003209470883320666783353670420, \
       0.000000000006293040671833540390213316, \
       0.000000000000008740304300063083340121, \
       0.000000000000000009047915683496049529, \
       0.000000000000000000007249923164709251, \
       0.000000000000000000000004629576649604, \
       0.000000000000000000000000002411236436, \
       0.000000000000000000000000000001043825, \
       0.000000000000000000000000000000000382 ] )

  big2cs = np.array ( [ \
       1.606299946362129457759284537862622883, \
       0.744908881987608865201476685194753972, \
       0.047013873861027737964095177635353019, \
       0.001228442206254823907016188785848091, \
       0.000017322241225662362670987355613727, \
       0.000000152190165236801893711508366563, \
       0.000000000911356024911957704145528786, \
       0.000000000003954791842356644201722554, \
       0.000000000000013001737033862320007309, \
       0.000000000000000033493506858269079763, \
       0.000000000000000000069419094403694057, \
       0.000000000000000000000118248256604581, \
       0.000000000000000000000000168462493472, \
       0.000000000000000000000000000203684674, \
       0.000000000000000000000000000000211619, \
       0.000000000000000000000000000000000191 ] )

  bigcs = np.array ( [ \
      -0.0971964404164435373897790974606802, \
       0.1495035768431670665710843445326264, \
       0.0031135253871213260419419176839631, \
       0.0000247085705798212967777021920569, \
       0.0000001029496277313786081987324295, \
       0.0000000002639703739869432892676778, \
       0.0000000000004582792707803206608181, \
       0.0000000000000005742829740893447321, \
       0.0000000000000000005438275385238549, \
       0.0000000000000000000004028347267083, \
       0.0000000000000000000000002397823826, \
       0.0000000000000000000000000001171956, \
       0.0000000000000000000000000000000479 ] )

  eta = 0.1 * r8_mach ( 3 )
  nbif = r8_inits ( bifcs, 13, eta )
  nbig = r8_inits ( bigcs, 13, eta )
  nbif2 = r8_inits ( bif2cs, 15, eta )
  nbig2 = r8_inits ( big2cs, 16, eta )
  x2sml = np.sqrt ( eta )
  x3sml = eta ** 0.3333
  xmax = ( 1.5 * np.log ( r8_mach ( 2 ) ) ) ** 0.6666

  if ( x < - 1.0 ):
    xn, phi = r8_admp ( x )
    value = xn * np.sin ( phi )
  elif ( abs ( x ) <= x2sml ):
    x2 = 0.0
    x3 = 0.0
    value = x2 * ( r8_csevl ( x3, bifcs, nbif ) + 0.25 ) \
      + r8_csevl ( x3, bigcs, nbig ) + 0.5
  elif ( abs ( x ) <= x3sml ):
    x2 = x * x
    x3 = 0.0
    value = x2 * ( r8_csevl ( x3, bifcs, nbif ) + 0.25 ) \
      + r8_csevl ( x3, bigcs, nbig ) + 0.5
  elif ( x <= 1.0 ):
    x2 = x * x
    x3 = x * x * x
    value = x2 * ( r8_csevl ( x3, bifcs, nbif ) + 0.25 ) \
      + r8_csevl ( x3, bigcs, nbig ) + 0.5
  elif ( x <= 2.0 ):
    z = ( 2.0 * x * x * x - 9.0 ) / 7.0
    value = x * x * ( r8_csevl ( z, bif2cs, nbif2 ) + 0.25 ) \
      + r8_csevl ( z, big2cs, nbig2 ) + 0.5
  else:
    value = r8_bide ( x ) * np.exp ( 2.0 * x * np.sqrt ( x ) / 3.0 )

  return value

def r8_bid_test ( ):

#*****************************************************************************80
#
## r8_bid_test() tests r8_bid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_bid_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_bid evaluates the derivative of the Airy function Bi(X)' )
  print ( '' )
  print ( '             X     airy_bid(X)  r8_bid(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = airy_bi_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_bid ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_bide ( x ):

#*****************************************************************************80
#
## r8_bide(): exponentially scaled derivative, Airy function Bi of an R8 argument.
#
#  Discussion:
#
#    if X < 0,
#      r8_bide ( X ) = r8_bid ( X )
#    else
#      r8_bide ( X ) = r8_bid ( X ) * np.exp ( - 2/3 * X^(3/2) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  atr = 8.75069057084843450880771988210148
  btr = -2.09383632135605431360096498526268

  bif2cs = np.array ( [ \
       0.32349398760352203352119193596266015, \
       0.08629787153556355913888835323811100, \
       0.00299402555265539742613821050727155, \
       0.00005143052836466163720464316950821, \
       0.00000052584025003681146026033098613, \
       0.00000000356175137395770028102730600, \
       0.00000000001714686400714584830518308, \
       0.00000000000006166351969232555406693, \
       0.00000000000000017191082154315985806, \
       0.00000000000000000038236889518803943, \
       0.00000000000000000000069424173624884, \
       0.00000000000000000000000104833932510, \
       0.00000000000000000000000000133721972, \
       0.00000000000000000000000000000145986, \
       0.00000000000000000000000000000000138 ] )

  bifcs = np.array ( [ \
       0.115353679082857024267474446284908879, \
       0.020500789404919287530357789445940252, \
       0.000213529027890287581892679619451158, \
       0.000001078396061467683042209155523569, \
       0.000000003209470883320666783353670420, \
       0.000000000006293040671833540390213316, \
       0.000000000000008740304300063083340121, \
       0.000000000000000009047915683496049529, \
       0.000000000000000000007249923164709251, \
       0.000000000000000000000004629576649604, \
       0.000000000000000000000000002411236436, \
       0.000000000000000000000000000001043825, \
       0.000000000000000000000000000000000382 ] )

  big2cs = np.array ( [ \
       1.606299946362129457759284537862622883, \
       0.744908881987608865201476685194753972, \
       0.047013873861027737964095177635353019, \
       0.001228442206254823907016188785848091, \
       0.000017322241225662362670987355613727, \
       0.000000152190165236801893711508366563, \
       0.000000000911356024911957704145528786, \
       0.000000000003954791842356644201722554, \
       0.000000000000013001737033862320007309, \
       0.000000000000000033493506858269079763, \
       0.000000000000000000069419094403694057, \
       0.000000000000000000000118248256604581, \
       0.000000000000000000000000168462493472, \
       0.000000000000000000000000000203684674, \
       0.000000000000000000000000000000211619, \
       0.000000000000000000000000000000000191 ] )

  bigcs = np.array ( [ \
      -0.0971964404164435373897790974606802, \
       0.1495035768431670665710843445326264, \
       0.0031135253871213260419419176839631, \
       0.0000247085705798212967777021920569, \
       0.0000001029496277313786081987324295, \
       0.0000000002639703739869432892676778, \
       0.0000000000004582792707803206608181, \
       0.0000000000000005742829740893447321, \
       0.0000000000000000005438275385238549, \
       0.0000000000000000000004028347267083, \
       0.0000000000000000000000002397823826, \
       0.0000000000000000000000000001171956, \
       0.0000000000000000000000000000000479 ] )

  bip1cs = np.array ( [ \
      -0.17291873510795537186124679823741003, \
      -0.01493584929846943639486231021818675, \
      -0.00054711049516785663990658697874460, \
       0.00015379662929584083449573727856666, \
       0.00001543534761921794131028948022869, \
      -0.00000654341138519060129226087106765, \
       0.00000037280824078787032232152275240, \
       0.00000020720783881887480080810710514, \
      -0.00000006581733364696191689495883922, \
       0.00000000749267463539288212986048985, \
       0.00000000111013368840707147698890101, \
      -0.00000000072651405529159512323880794, \
       0.00000000017827235598470153962165668, \
      -0.00000000002173463524809506269656807, \
      -0.00000000000203020349653882594017049, \
       0.00000000000193118272294077519319859, \
      -0.00000000000060449525048290296023117, \
       0.00000000000012094496248933664277802, \
      -0.00000000000001251088360074479784619, \
      -0.00000000000000199173832424881344036, \
       0.00000000000000151540816342864303038, \
      -0.00000000000000049768927059816240250, \
       0.00000000000000011545959731810501403, \
      -0.00000000000000001863286862907983871, \
       0.00000000000000000099330392344759104, \
       0.00000000000000000068182083667412417, \
      -0.00000000000000000034854456479650551, \
       0.00000000000000000010860382134235961, \
      -0.00000000000000000002599290185240166, \
       0.00000000000000000000476895370459000, \
      -0.00000000000000000000051946940777177, \
      -0.00000000000000000000005925575044912, \
       0.00000000000000000000005746008970972, \
      -0.00000000000000000000002186119806494, \
       0.00000000000000000000000624124294738, \
      -0.00000000000000000000000146003421785, \
       0.00000000000000000000000027493893904, \
      -0.00000000000000000000000003474678018, \
      -0.00000000000000000000000000109303694, \
       0.00000000000000000000000000261972744, \
      -0.00000000000000000000000000112365018, \
       0.00000000000000000000000000035152059, \
      -0.00000000000000000000000000009167601, \
       0.00000000000000000000000000002040203, \
      -0.00000000000000000000000000000373038, \
       0.00000000000000000000000000000046070, \
       0.00000000000000000000000000000001748 ] )

  bip2cs = np.array ( [ \
      -0.13269705443526630494937031210217135, \
      -0.00568443626045977481306046339037428, \
      -0.00015643601119611609623698471216660, \
      -0.00001136737203679562267336053207940, \
      -0.00000143464350991283669643136951338, \
      -0.00000018098531185164131868746481700, \
       0.00000000926177343610865546229511422, \
       0.00000001710005490720592181887296162, \
       0.00000000476698163503781708252686849, \
      -0.00000000035195022023163141945397159, \
      -0.00000000058890614315886871574147635, \
      -0.00000000006678499607795537597612089, \
       0.00000000006395565101720391190697713, \
       0.00000000001554529427064394106403245, \
      -0.00000000000792396999744612971684001, \
      -0.00000000000258326242689717798947525, \
       0.00000000000121655047787849117978773, \
       0.00000000000038707207172899985942258, \
      -0.00000000000022487045479618229130656, \
      -0.00000000000004953476515684046293493, \
       0.00000000000004563781601526912756017, \
       0.00000000000000332998314345014118494, \
      -0.00000000000000921750185832874202719, \
       0.00000000000000094156670658958205765, \
       0.00000000000000167153952640716157721, \
      -0.00000000000000055134268782182410852, \
      -0.00000000000000022368651572006617795, \
       0.00000000000000017486948976520089209, \
       0.00000000000000000206518666352329750, \
      -0.00000000000000003973060018130712479, \
       0.00000000000000001154836935724892335, \
       0.00000000000000000553906053678276421, \
      -0.00000000000000000457174427396478267, \
       0.00000000000000000026567111858284432, \
       0.00000000000000000101599148154167823, \
      -0.00000000000000000044821231272196246, \
      -0.00000000000000000007959149661617295, \
       0.00000000000000000014583615616165794, \
      -0.00000000000000000004015127893061405, \
      -0.00000000000000000002079152963743616, \
       0.00000000000000000001972630449634388, \
      -0.00000000000000000000336033404001683, \
      -0.00000000000000000000376504832685507, \
       0.00000000000000000000269935508825595, \
      -0.00000000000000000000026985946069808, \
      -0.00000000000000000000061794011788222, \
       0.00000000000000000000038782693311711, \
      -0.00000000000000000000002420094005071, \
      -0.00000000000000000000009844051058925, \
       0.00000000000000000000005954353358494, \
      -0.00000000000000000000000361274446366, \
      -0.00000000000000000000001552634578088, \
       0.00000000000000000000000977819380304, \
      -0.00000000000000000000000092239447509, \
      -0.00000000000000000000000241545903934, \
       0.00000000000000000000000169558652255, \
      -0.00000000000000000000000026762408641, \
      -0.00000000000000000000000036188116265, \
       0.00000000000000000000000030372404951, \
      -0.00000000000000000000000007422876903, \
      -0.00000000000000000000000004930678544, \
       0.00000000000000000000000005468790028, \
      -0.00000000000000000000000001920315188, \
      -0.00000000000000000000000000516335154, \
       0.00000000000000000000000000957723167, \
      -0.00000000000000000000000000463659079, \
      -0.00000000000000000000000000004509226, \
       0.00000000000000000000000000155617519, \
      -0.00000000000000000000000000104156509, \
       0.00000000000000000000000000019565323, \
       0.00000000000000000000000000021335380, \
      -0.00000000000000000000000000021461958, \
       0.00000000000000000000000000007875791, \
       0.00000000000000000000000000001713768, \
      -0.00000000000000000000000000003917137, \
       0.00000000000000000000000000002233559, \
      -0.00000000000000000000000000000269383, \
      -0.00000000000000000000000000000577764, \
       0.00000000000000000000000000000519650, \
      -0.00000000000000000000000000000183361, \
      -0.00000000000000000000000000000045763, \
       0.00000000000000000000000000000099235, \
      -0.00000000000000000000000000000058938, \
       0.00000000000000000000000000000009568, \
       0.00000000000000000000000000000013758, \
      -0.00000000000000000000000000000014066, \
       0.00000000000000000000000000000005964, \
       0.00000000000000000000000000000000437 ] )

  eta = 0.1 * r8_mach ( 3 )
  nbif = r8_inits ( bifcs, 13, eta )
  nbig = r8_inits ( bigcs, 13, eta )
  nbif2 = r8_inits ( bif2cs, 15, eta )
  nbig2 = r8_inits ( big2cs, 16, eta )
  nbip1 = r8_inits ( bip1cs, 47, eta )
  nbip2 = r8_inits ( bip2cs, 88, eta )
  x2sml = np.sqrt ( eta )
  x3sml = eta ** 0.3333
  x32sml = 1.3104 * x3sml * x3sml
  xbig = r8_mach ( 2 ) ** 0.6666

  if ( x < -1.0 ):
    xn, phi = r8_admp ( x )
    value = xn * np.sin ( phi )
  elif ( abs ( x ) <= x2sml ):
    x2 = 0.0
    x3 = 0.0
    value = x2 * ( r8_csevl ( x3, bifcs, nbif ) \
      + 0.25 ) + r8_csevl ( x3, bigcs, nbig ) + 0.5
    if ( x32sml < x ):
      value = value * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( abs ( x ) <= x3sml ):
    x2 = x * x
    x3 = 0.0
    value = x2 * ( r8_csevl ( x3, bifcs, nbif ) \
      + 0.25 ) + r8_csevl ( x3, bigcs, nbig ) + 0.5
    if ( x32sml < x ):
      value = value * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 1.0 ):
    x2 = x * x
    x3 = x * x * x
    value = x2 * ( r8_csevl ( x3, bifcs, nbif ) \
      + 0.25 ) + r8_csevl ( x3, bigcs, nbig ) + 0.5
    if ( x32sml < x ):
      value = value * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 2.0 ):
    z = ( 2.0 * x * x * x - 9.0 ) / 7.0
    value = np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 ) \
      * ( x * x * ( 0.25 + r8_csevl ( z, bif2cs, nbif2 ) ) \
      + 0.5 + r8_csevl ( z, big2cs, nbig2 ) )
  elif ( x <= 4.0 ):
    sqrtx = np.sqrt ( x )
    z = atr / x / sqrtx + btr
    value = ( 0.625 + r8_csevl ( z, bip1cs, nbip1 ) ) * np.sqrt ( sqrtx )
  elif ( x <= xbig ):
    sqrtx = np.sqrt ( x )
    z = 16.0 / x / sqrtx - 1.0
    value = ( 0.625 + r8_csevl ( z, bip2cs, nbip2 ) ) * np.sqrt ( sqrtx )
  else:
    sqrtx = np.sqrt ( x )
    z = -1.0
    value = ( 0.625 + r8_csevl ( z, bip2cs, nbip2 ) ) * np.sqrt ( sqrtx )

  return value

def r8_bie ( x ):

#*****************************************************************************80
#
## r8_bie() evaluates the exponentially scaled Airy function Bi of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the exponentially scaled Airy function Bi of X.
#
  import numpy as np

  atr = 8.75069057084843450880771988210148
  btr = -2.09383632135605431360096498526268

  bif2cs = np.array ( [ \
      +0.0998457269381604104468284257993, \
      +0.47862497786300553772211467318231, \
      +0.25155211960433011771324415436675E-01, \
      +0.58206938852326456396515697872216E-03, \
      +0.74997659644377865943861457378217E-05, \
      +0.61346028703493836681403010356474E-07, \
      +0.34627538851480632900434268733359E-09, \
      +0.14288910080270254287770846748931E-11, \
      +0.44962704298334641895056472179200E-14, \
      +0.11142323065833011708428300106666E-16, \
      +0.22304791066175002081517866666666E-19, \
      +0.36815778736393142842922666666666E-22, \
      +0.50960868449338261333333333333333E-25, \
      +0.60003386926288554666666666666666E-28, \
      +0.60827497446570666666666666666666E-31 ] )

  bifcs = np.array ( [ \
      -0.16730216471986649483537423928176E-01, \
      +0.10252335834249445611426362777757, \
      +0.17083092507381516539429650242013E-02, \
      +0.11862545467744681179216459210040E-04, \
      +0.44932907017792133694531887927242E-07, \
      +0.10698207143387889067567767663628E-09, \
      +0.17480643399771824706010517628573E-12, \
      +0.20810231071761711025881891834399E-15, \
      +0.18849814695665416509927971733333E-18, \
      +0.13425779173097804625882666666666E-21, \
      +0.77159593429658887893333333333333E-25, \
      +0.36533879617478566399999999999999E-28, \
      +0.14497565927953066666666666666666E-31 ] )

  big2cs = np.array ( [ \
      +0.033305662145514340465176188111647, \
      +0.161309215123197067613287532084943, \
      +0.631900730961342869121615634921173E-02, \
      +0.118790456816251736389780192304567E-03, \
      +0.130453458862002656147116485012843E-05, \
      +0.937412599553521729546809615508936E-08, \
      +0.474580188674725153788510169834595E-10, \
      +0.178310726509481399800065667560946E-12, \
      +0.516759192784958180374276356640000E-15, \
      +0.119004508386827125129496251733333E-17, \
      +0.222982880666403517277063466666666E-20, \
      +0.346551923027689419722666666666666E-23, \
      +0.453926336320504514133333333333333E-26, \
      +0.507884996513522346666666666666666E-29, \
      +0.491020674696533333333333333333333E-32 ] )

  bigcs = np.array ( [ \
      +0.22466223248574522283468220139024E-01, \
      +0.37364775453019545441727561666752E-01, \
      +0.44476218957212285696215294326639E-03, \
      +0.24708075636329384245494591948882E-05, \
      +0.79191353395149635134862426285596E-08, \
      +0.16498079851827779880887872402706E-10, \
      +0.24119906664835455909247501122841E-13, \
      +0.26103736236091436985184781269333E-16, \
      +0.21753082977160323853123792000000E-19, \
      +0.14386946400390433219483733333333E-22, \
      +0.77349125612083468629333333333333E-26, \
      +0.34469292033849002666666666666666E-29, \
      +0.12938919273216000000000000000000E-32 ] )

  bip1cs = np.array ( [ \
      -0.83220474779434474687471864707973E-01, \
      +0.11461189273711742889920226128031E-01, \
      +0.42896440718911509494134472566635E-03, \
      -0.14906639379950514017847677732954E-03, \
      -0.13076597267876290663136340998881E-04, \
      +0.63275983961030344754535716032494E-05, \
      -0.42226696982681924884778515889433E-06, \
      -0.19147186298654689632835494181277E-06, \
      +0.64531062845583173611038157880934E-07, \
      -0.78448546771397719289748310448628E-08, \
      -0.96077216623785085879198533565432E-09, \
      +0.70004713316443966339006074402068E-09, \
      -0.17731789132814932022083128056698E-09, \
      +0.22720894783465236347282126389311E-10, \
      +0.16540456313972049847032860681891E-11, \
      -0.18517125559292316390755369896693E-11, \
      +0.59576312477117290165680715534277E-12, \
      -0.12194348147346564781055769498986E-12, \
      +0.13347869253513048815386347813597E-13, \
      +0.17278311524339746664384792889731E-14, \
      -0.14590732013016720735268871713166E-14, \
      +0.49010319927115819978994989520104E-15, \
      -0.11556545519261548129262972762521E-15, \
      +0.19098807367072411430671732441524E-16, \
      -0.11768966854492179886913995957862E-17, \
      -0.63271925149530064474537459677047E-18, \
      +0.33861838880715361614130191322316E-18, \
      -0.10725825321758625254992162219622E-18, \
      +0.25995709605617169284786933115562E-19, \
      -0.48477583571081193660962309494101E-20, \
      +0.55298913982121625361505513198933E-21, \
      +0.49421660826069471371748197444266E-22, \
      -0.55162121924145707458069720814933E-22, \
      +0.21437560417632550086631884499626E-22, \
      -0.61910313387655605798785061137066E-23, \
      +0.14629362707391245659830967336959E-23, \
      -0.27918484471059005576177866069333E-24, \
      +0.36455703168570246150906795349333E-25, \
      +0.58511821906188711839382459733333E-27, \
      -0.24946950487566510969745047551999E-26, \
      +0.10979323980338380977919579477333E-26, \
      -0.34743388345961115015034088106666E-27, \
      +0.91373402635349697363171082240000E-28, \
      -0.20510352728210629186247720959999E-28, \
      +0.37976985698546461748651622399999E-29, \
      -0.48479458497755565887848448000000E-30, \
      -0.10558306941230714314205866666666E-31 ] )

  bip2cs = np.array ( [ \
      -0.11359673758598867913797310895527, \
      +0.41381473947881595760052081171444E-02, \
      +0.13534706221193329857696921727508E-03, \
      +0.10427316653015353405887183456780E-04, \
      +0.13474954767849907889589911958925E-05, \
      +0.16965374054383983356062511163756E-06, \
      -0.10096500865641624301366228396373E-07, \
      -0.16729119493778475127836973095943E-07, \
      -0.45815364485068383217152795613391E-08, \
      +0.37366813665655477274064749384284E-09, \
      +0.57669303201452448119584643502111E-09, \
      +0.62181265087850324095393408792371E-10, \
      -0.63294120282743068241589177281354E-10, \
      -0.14915047908598767633999091989487E-10, \
      +0.78896213942486771938172394294891E-11, \
      +0.24960513721857797984888064000127E-11, \
      -0.12130075287291659477746664734814E-11, \
      -0.37404939108727277887343460402716E-12, \
      +0.22377278140321476798783446931091E-12, \
      +0.47490296312192466341986077472514E-13, \
      -0.45261607991821224810605655831294E-13, \
      -0.30172271841986072645112245876020E-14, \
      +0.91058603558754058327592683478908E-14, \
      -0.98149238033807062926643864207709E-15, \
      -0.16429400647889465253601245251589E-14, \
      +0.55334834214274215451182114635164E-15, \
      +0.21750479864482655984374381998156E-15, \
      -0.17379236200220656971287029558087E-15, \
      -0.10470023471443714959283909313604E-17, \
      +0.39219145986056386925441403311462E-16, \
      -0.11621293686345196925824005665910E-16, \
      -0.54027474491754245533735411307773E-17, \
      +0.45441582123884610882675428553304E-17, \
      -0.28775599625221075729427585480086E-18, \
      -0.10017340927225341243596162960440E-17, \
      +0.44823931215068369856332561906313E-18, \
      +0.76135968654908942328948982366775E-19, \
      -0.14448324094881347238956060145422E-18, \
      +0.40460859449205362251624847392112E-19, \
      +0.20321085700338446891325190707277E-19, \
      -0.19602795471446798718272758041962E-19, \
      +0.34273038443944824263518958211738E-20, \
      +0.37023705853905135480024651593154E-20, \
      -0.26879595172041591131400332966712E-20, \
      +0.28121678463531712209714454683364E-21, \
      +0.60933963636177797173271119680329E-21, \
      -0.38666621897150844994172977893413E-21, \
      +0.25989331253566943450895651927228E-22, \
      +0.97194393622938503767281175216084E-22, \
      -0.59392817834375098415630478204591E-22, \
      +0.38864949977113015409591960439444E-23, \
      +0.15334307393617272869721512868769E-22, \
      -0.97513555209762624036336521409724E-23, \
      +0.96340644440489471424741339383726E-24, \
      +0.23841999400208880109946748792454E-23, \
      -0.16896986315019706184848044205207E-23, \
      +0.27352715888928361222578444801478E-24, \
      +0.35660016185409578960111685025730E-24, \
      -0.30234026608258827249534280666954E-24, \
      +0.75002041605973930653144204823232E-25, \
      +0.48403287575851388827455319838748E-25, \
      -0.54364137654447888432698010297766E-25, \
      +0.19281214470820962653345978809756E-25, \
      +0.50116355020532656659611814172172E-26, \
      -0.95040744582693253786034620869972E-26, \
      +0.46372646157101975948696332245611E-26, \
      +0.21177170704466954163768170577046E-28, \
      -0.15404850268168594303692204548726E-26, \
      +0.10387944293201213662047889194441E-26, \
      -0.19890078156915416751316728235153E-27, \
      -0.21022173878658495471177044522532E-27, \
      +0.21353099724525793150633356670491E-27, \
      -0.79040810747961342319023537632627E-28, \
      -0.16575359960435585049973741763592E-28, \
      +0.38868342850124112587625586496537E-28, \
      -0.22309237330896866182621562424717E-28, \
      +0.27777244420176260265625977404382E-29, \
      +0.57078543472657725368712433782772E-29, \
      -0.51743084445303852800173371555280E-29, \
      +0.18413280751095837198450927071569E-29, \
      +0.44422562390957094598544071068647E-30, \
      -0.98504142639629801547464958226943E-30, \
      +0.58857201353585104884754198881995E-30, \
      -0.97636075440429787961402312628595E-31, \
      -0.13581011996074695047063597884122E-30, \
      +0.13999743518492413270568048380345E-30, \
      -0.59754904545248477620884562981118E-31, \
      -0.40391653875428313641045327529856E-32 ] )

  eta = 0.1  * r8_mach ( 3 )
  nbif = r8_inits ( bifcs, 13, eta )
  nbig = r8_inits ( bigcs, 13, eta )
  nbif2 = r8_inits ( bif2cs, 15, eta )
  nbig2 = r8_inits ( big2cs, 15, eta )
  nbip1 = r8_inits ( bip1cs, 47, eta )
  nbip2 = r8_inits ( bip2cs, 88, eta )
  x3sml = eta ** 0.3333
  x32sml = 1.3104 * x3sml * x3sml
  xbig = r8_mach ( 2 ) ** 0.6666

  if ( x < - 1.0 ):
    xm, theta = r8_aimp ( x )
    value = xm * np.sin ( theta )
  elif ( abs ( x ) <= x3sml ):
    z = 0.0
    value = 0.625 + r8_csevl ( z, bifcs, nbif ) \
      + x * ( 0.4375 + r8_csevl ( z, bigcs, nbig ) )
    if (  x32sml <= x ):
      value = value * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 1.0 ):
    z = x * x * x
    value = 0.625 + r8_csevl ( z, bifcs, nbif ) \
      + x * ( 0.4375 + r8_csevl ( z, bigcs, nbig ) )
    if (  x32sml <= x ):
      value = value * np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 )
  elif ( x <= 2.0 ):
    z = ( 2.0 * x * x * x - 9.0 ) / 7.0
    value = np.exp ( - 2.0 * x * np.sqrt ( x ) / 3.0 ) \
      * ( 1.125 + r8_csevl ( z, bif2cs, nbif2 ) \
      + x * ( 0.625 + r8_csevl ( z, big2cs, nbig2 ) ) )
  elif ( x <= 4.0 ):
    sqrtx = np.sqrt ( x )
    z = atr / x / sqrtx + btr
    value = ( 0.625 + r8_csevl ( z, bip1cs, nbip1 ) ) / np.sqrt ( sqrtx )
  elif ( x < xbig ):
    sqrtx = np.sqrt ( x )
    z = 16.0 / ( x * sqrtx ) - 1.0
    value = ( 0.625 + r8_csevl ( z, bip2cs, nbip2 ) ) / np.sqrt ( sqrtx )
  else:
    sqrtx = np.sqrt ( x )
    z = - 1.0
    value = ( 0.625 + r8_csevl ( z, bip2cs, nbip2 ) ) / np.sqrt ( sqrtx )

  return value

def r8_asinh ( x ):

#*****************************************************************************80
#
## r8_asinh() evaluates the arc-sine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  asnhcs = np.array ( [ \
      -0.12820039911738186343372127359268E+00, \
      -0.58811761189951767565211757138362E-01, \
      +0.47274654322124815640725249756029E-02, \
      -0.49383631626536172101360174790273E-03, \
      +0.58506207058557412287494835259321E-04, \
      -0.74669983289313681354755069217188E-05, \
      +0.10011693583558199265966192015812E-05, \
      -0.13903543858708333608616472258886E-06, \
      +0.19823169483172793547317360237148E-07, \
      -0.28847468417848843612747272800317E-08, \
      +0.42672965467159937953457514995907E-09, \
      -0.63976084654366357868752632309681E-10, \
      +0.96991686089064704147878293131179E-11, \
      -0.14844276972043770830246658365696E-11, \
      +0.22903737939027447988040184378983E-12, \
      -0.35588395132732645159978942651310E-13, \
      +0.55639694080056789953374539088554E-14, \
      -0.87462509599624678045666593520162E-15, \
      +0.13815248844526692155868802298129E-15, \
      -0.21916688282900363984955142264149E-16, \
      +0.34904658524827565638313923706880E-17, \
      -0.55785788400895742439630157032106E-18, \
      +0.89445146617134012551050882798933E-19, \
      -0.14383426346571317305551845239466E-19, \
      +0.23191811872169963036326144682666E-20, \
      -0.37487007953314343674570604543999E-21, \
      +0.60732109822064279404549242880000E-22, \
      -0.98599402764633583177370173440000E-23, \
      +0.16039217452788496315232638293333E-23, \
      -0.26138847350287686596716134399999E-24, \
      +0.42670849606857390833358165333333E-25, \
      -0.69770217039185243299730773333333E-26, \
      +0.11425088336806858659812693333333E-26, \
      -0.18735292078860968933021013333333E-27, \
      +0.30763584414464922794065920000000E-28, \
      -0.50577364031639824787046399999999E-29, \
      +0.83250754712689142224213333333333E-30, \
      -0.13718457282501044163925333333333E-30, \
      +0.22629868426552784104106666666666E-31 ] )

  nterms = r8_inits ( asnhcs, 39, 0.1 * r8_mach ( 3 ) )
  aln2 = 0.69314718055994530941723212145818
  sqeps = np.sqrt ( r8_mach ( 3 ) )
  xmax = 1.0 / sqeps
 
  y = abs ( x )

  if ( y <= sqeps ):
    value = x
  elif ( y <= 1.0 ):
    value = x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, asnhcs, nterms ) )
  elif ( y < xmax ):
    value = np.log ( y + np.sqrt ( y * y + 1.0 ) )
    if ( x < 0.0 ):
      value = - value
  else:
    value = aln2 + np.log ( y )
    if ( x < 0.0 ):
      value = - value

  return value

def r8_asinh_test ( ):

#*****************************************************************************80
#
## r8_asinh_test() tests r8_asinh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_asinh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_asinh evaluates the arc hyperbolic sine function' )
  print ( '' )
  print ( '             X     arcsinH(X)  r8_asinh(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arcsinh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_asinh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_asin ( x ):

#*****************************************************************************80
#
## r8_asin() evaluates the arc-sine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  asincs = np.array ( [ \
    +0.10246391753227159336573148305785E+00, \
    +0.54946487221245833306011195902924E-01, \
    +0.40806303925449692851307056149246E-02, \
    +0.40789006854604435455598823905612E-03, \
    +0.46985367432203691616048530136218E-04, \
    +0.58809758139708058986454385552074E-05, \
    +0.77732312462777632750557528163795E-06, \
    +0.10677423340082039235047504956587E-06, \
    +0.15092399536022808262386434401064E-07, \
    +0.21809724080055385496609614713930E-08, \
    +0.32075984262789614433261959667376E-09, \
    +0.47855369646781034461493133918953E-10, \
    +0.72251287362910432263848754537112E-11, \
    +0.11018334742255783705372701334987E-11, \
    +0.16947632539203354877423745651078E-12, \
    +0.26261558667348224162283241502416E-13, \
    +0.40958299813281178408828069291110E-14, \
    +0.64244793108803655891727944887091E-15, \
    +0.10128142198228221693973361222041E-15, \
    +0.16039221897380787560050597464746E-16, \
    +0.25503501355807141715298789676373E-17, \
    +0.40701403797862382855487165672106E-18, \
    +0.65172671712881144437889267575466E-19, \
    +0.10467453037096796954244891716266E-19, \
    +0.16858725563380328094989095185066E-20, \
    +0.27221936305040227625164341247999E-21, \
    +0.44059293900347550617126830079999E-22, \
    +0.71466685243375937853063168000000E-23, \
    +0.11615793343859516051798971733333E-23, \
    +0.18915234552354685801184187733333E-24, \
    +0.30855772044244342399827968000000E-25, \
    +0.50416366022162453412970495999999E-26, \
    +0.82502725502400865081753600000000E-27, \
    +0.13520032631020947208055466666666E-27, \
    +0.22184326876541720216644266666666E-28, \
    +0.36442494054085079212578133333333E-29, \
    +0.59920218558643813307733333333333E-30, \
    +0.98584812059573785810261333333333E-31, \
    +0.16222501166399014393173333333333E-31 ] )

  nterms = r8_inits ( asincs, 39, 0.1 * r8_mach ( 3 ) )

  sqeps = np.sqrt ( 6.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( x < - 1.0 - sqeps ):

    print ( '' )
    print ( 'r8_asin - Fatal error!' )
    print ( '  X < - 1.0' )
    raise Exception ( 'r8_asin - Fatal error!' )

  elif ( x < - 1.0 ):

    value = - 0.5 * np.pi

  elif ( x < 1.0 ):

    z = 0.0
    if ( sqeps < y ):
      z = y * y

    if ( z <= 0.5 ):
      value = x * ( 1.0 + r8_csevl ( 4.0 * z - 1.0, asincs, nterms ) )
    else:
      value = 0.5 * np.pi - np.sqrt ( 1.0 - z ) * ( 1.0 + \
        r8_csevl ( 3.0 - 4.0 * z, asincs, nterms ) )

    if ( x < 0.0 ):
      value = - abs ( value )
    elif ( 0.0 < x ):
      value = + abs ( value )

  elif ( x < 1.0 + sqeps ):

    value = 0.5 * np.pi

  else:

    print ( '' )
    print ( 'r8_asin - Fatal error!' )
    print ( '  1.0 < X' )
    raise Exception ( 'r8_asin - Fatal error!' )

  return value

def r8_asin_test ( ):

#*****************************************************************************80
#
## r8_asin_test() tests r8_asin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_asin_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_asin evaluates the arc-sine function' )
  print ( '' )
  print ( '             X      arcsin(X)  r8_asin(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arcsin_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_asin ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_atan2 ( sn, cs ):

#*****************************************************************************80
#
## r8_atan2() evaluates the arc-tangent of two R8 arguments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real SN, CS, the Y and X coordinates of a
#    point on the angle.
#
#  Output:
#
#    real VALUE, the arc-tangent of the angle.
#
  import numpy as np

  sml = r8_mach ( 1 )
  big = r8_mach ( 2 )
#
#  We now make sure SN can be divided by CS.  It is painful.
#
  abssn = abs ( sn )
  abscs = abs ( cs )

  if ( abscs <= abssn ):

    if ( abscs < 1.0 and abscs * big <= abssn ):

      if ( sn < 0.0 ):
        value = - 0.5 * np.pi
      elif ( sn == 0.0 ):
        print ( '' )
        print ( 'r8_atan2 - Fatal error!' )
        print ( '  Both arguments are 0.' )
        raise Exception ( 'r8_atan2 - Fatal error!' )
      else:
        value = 0.5 * np.pi

      return value

  else:

    if ( 1.0 < abscs and abssn <= abscs * sml ):

      if ( 0.0 <= cs ):
        value = 0.0
      else:
        value = np.pi

      return value

  value = r8_atan ( sn / cs )

  if ( cs < 0.0 ):
    value = value + np.pi

  if ( np.pi < value ):
    value = value - 2.0 * np.pi

  return value

def r8_atan2_test ( ):

#*****************************************************************************80
#
## r8_atan2_test() tests r8_atan2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_atan2_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_atan2 evaluates the arctangent function' )
  print ( '' )
  print ( '             X               Y   arctan2(Y,X)  r8_atan2(Y,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, fx1 = arctan2_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_atan2 ( y, x )

    print ( '  %14.4g  %14.4f  %14.6g  %14.6g  %14.6g' \
      % ( x, y, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_atanh ( x ):

#*****************************************************************************80
#
## r8_atanh() evaluates the arc-hyperbolic tangent of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  atnhcs = np.array ( [ \
    +0.9439510239319549230842892218633E-01, \
    +0.4919843705578615947200034576668E-01, \
    +0.2102593522455432763479327331752E-02, \
    +0.1073554449776116584640731045276E-03, \
    +0.5978267249293031478642787517872E-05, \
    +0.3505062030889134845966834886200E-06, \
    +0.2126374343765340350896219314431E-07, \
    +0.1321694535715527192129801723055E-08, \
    +0.8365875501178070364623604052959E-10, \
    +0.5370503749311002163881434587772E-11, \
    +0.3486659470157107922971245784290E-12, \
    +0.2284549509603433015524024119722E-13, \
    +0.1508407105944793044874229067558E-14, \
    +0.1002418816804109126136995722837E-15, \
    +0.6698674738165069539715526882986E-17, \
    +0.4497954546494931083083327624533E-18, \
    +0.3032954474279453541682367146666E-19, \
    +0.2052702064190936826463861418666E-20, \
    +0.1393848977053837713193014613333E-21, \
    +0.9492580637224576971958954666666E-23, \
    +0.6481915448242307604982442666666E-24, \
    +0.4436730205723615272632320000000E-25, \
    +0.3043465618543161638912000000000E-26, \
    +0.2091881298792393474047999999999E-27, \
    +0.1440445411234050561365333333333E-28, \
    +0.9935374683141640465066666666666E-30, \
    +0.6863462444358260053333333333333E-31 ] )

  nterms = r8_inits ( atnhcs, 27, 0.1 * r8_mach ( 3 ) )
  dxrel = np.sqrt ( r8_mach ( 4 ) )
  sqeps = np.sqrt ( 3.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= sqeps ):
    value = x
  elif ( y <= 0.5 ):
    value = x * ( 1.0 + r8_csevl ( 8.0 * x * x - 1.0, atnhcs, nterms ) )
  elif ( y < 1.0 ):
    value = 0.5 * np.log ( ( 1.0 + x ) / ( 1.0 - x ) )
    if ( 1.0 - y < dxrel ):
      print ( '' )
      print ( 'r8_atanH - Warning:' )
      print ( '  Answer lt half precision because |X| too near 1.' )
  else:
    print ( '' )
    print ( 'r8_atanH - Fatal error!' )
    print ( '  1 <= |X|.' )
    raise Exception ( 'r8_atanH - Fatal error!' )

  return value

def r8_atanh_test ( ):

#*****************************************************************************80
#
## r8_atanh_test() tests r8_atanh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_atanh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_atanh evaluates the hyperbolic arctangent function.' )
  print ( '' )
  print ( '             X     arctanH(X)  r8_atanh(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arctanh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_atanh ( x )

    print ( '  %14f  %14g  %14g  %14g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_atan ( x ):

#*****************************************************************************80
#
## r8_atan() evaluates the arc-tangent of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  atancs = np.array ( [ \
    +0.48690110349241406474636915902891E+00, \
    -0.65108316367174641818869794945974E-02, \
    +0.38345828265245177653569992430456E-04, \
    -0.26872212876223146539595410518788E-06, \
    +0.20500930985824269846636514686688E-08, \
    -0.16450717395484269455734135285348E-10, \
    +0.13650975274390773423813528484428E-12, \
    -0.11601779591998246322891309834666E-14, \
    +0.10038333943866273835797657402666E-16, \
    -0.88072747152163859327073696000000E-19, \
    +0.78136321005661722180580266666666E-21, \
    -0.69954535148267456086613333333333E-23, \
    +0.63105905713702136004266666666666E-25, \
    -0.57296075370213874346666666666666E-27, \
    +0.52274796280602282666666666666666E-29, \
    -0.48327903911608320000000000000000E-31 ] )

  conpi8 = np.array ( [ \
    0.375, \
    0.75, \
    1.125, \
    1.5 ] )

  pi8 = np.array ( [ \
    +0.17699081698724154807830422909937E-01, \
    +0.35398163397448309615660845819875E-01, \
    +0.53097245096172464423491268729813E-01, \
    +0.70796326794896619231321691639751E-01 ] )

  tanp8 = np.array ( [ \
    +0.41421356237309504880168872420969, \
    +1.0, \
    +2.4142135623730950488016887242096 ] )

  xbnd1 = +0.19891236737965800691159762264467
  xbnd2 = +0.66817863791929891999775768652308
  xbnd3 = +1.4966057626654890176011351349424
  xbnd4 = +5.0273394921258481045149750710640
  nterms = r8_inits ( atancs, 16, 0.1 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( 6.0 * r8_mach ( 3 ) )
  xbig = 1.0 / r8_mach ( 3 )

  y = abs ( x )

  if ( y <= xbnd1 ):

    value = x
    if ( sqeps < y ):
      value = x * ( 0.75 + r8_csevl ( 50.0 * y * y - 1.0, atancs, nterms ) )

  elif ( y <= xbnd4 ):

    if ( xbnd3 < y ):
      n = 3
    elif ( xbnd2 < y ):
      n = 2
    else:
      n = 1

    t = ( y - tanp8[n-1] ) / ( 1.0 + y * tanp8[n-1] )

    value = conpi8[n-1] + ( pi8[n-1] + t * ( 0.75 + \
      r8_csevl ( 50.0 * t * t - 1.0, atancs, nterms ) ) )

  else:

    value = conpi8[3] + pi8[3]

    if ( y < xbig ):
      value = conpi8[3] + ( pi8[3] - ( 0.75 + \
        r8_csevl ( 50.0 / y / y - 1.0, atancs, nterms ) ) / y )

  if ( x < 0.0 ):
    value = - abs ( value )
  else:
    value = + abs ( value )

  return value

def r8_atan_test ( ):

#*****************************************************************************80
#
## r8_atan_test() tests r8_atan().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_atan_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_atan evaluates the arc tangent function.' )
  print ( '' )
  print ( '             X      arctan(X)  r8_atan(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arctan_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_atan ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besi0 ( x ):

#*****************************************************************************80
#
## r8_besi0() evaluates the Bessel function I of order 0 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  bi0cs = np.array ( [ \
      -0.7660547252839144951081894976243285E-01, \
      +0.1927337953993808269952408750881196E+01, \
      +0.2282644586920301338937029292330415, \
      +0.1304891466707290428079334210691888E-01, \
      +0.4344270900816487451378682681026107E-03, \
      +0.9422657686001934663923171744118766E-05, \
      +0.1434006289510691079962091878179957E-06, \
      +0.1613849069661749069915419719994611E-08, \
      +0.1396650044535669699495092708142522E-10, \
      +0.9579451725505445344627523171893333E-13, \
      +0.5333981859862502131015107744000000E-15, \
      +0.2458716088437470774696785919999999E-17, \
      +0.9535680890248770026944341333333333E-20, \
      +0.3154382039721427336789333333333333E-22, \
      +0.9004564101094637431466666666666666E-25, \
      +0.2240647369123670016000000000000000E-27, \
      +0.4903034603242837333333333333333333E-30, \
      +0.9508172606122666666666666666666666E-33 ] )

  nti0 = r8_inits ( bi0cs, 18, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 8.0 * r8_mach ( 3 ) )
  xmax = np.log ( r8_mach ( 2 ) )

  y = abs ( x )

  if ( y <= xsml ):
    value = 1.0
  elif ( y <= 3.0 ):
    value = 2.75 + r8_csevl ( y * y / 4.5 - 1.0, bi0cs, nti0 )
  elif ( y <= xmax ):
    value = np.exp ( y ) * r8_besi0e ( x )
  else:
    print ( '' )
    print ( 'r8_besi0 - Fatal error!' )
    print ( '  |X| too large.' )
    raise Exception ( 'r8_besi0 - Fatal error!' )

  return value

def r8_besi0_test ( ):

#*****************************************************************************80
#
## r8_besi0_test() tests r8_besi0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_besi0_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besi0 evaluates the Bessel I0(x) function.' )
  print ( '' )
  print ( '             X       BESI0(X)  r8_besi0(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_i0_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besi0 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besi0e ( x ):

#*****************************************************************************80
#
## r8_besi0e() evaluates the exponentially scaled Bessel function I0(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ai02cs = np.array ( [ \
      +0.5449041101410883160789609622680E-01, \
      +0.3369116478255694089897856629799E-02, \
      +0.6889758346916823984262639143011E-04, \
      +0.2891370520834756482966924023232E-05, \
      +0.2048918589469063741827605340931E-06, \
      +0.2266668990498178064593277431361E-07, \
      +0.3396232025708386345150843969523E-08, \
      +0.4940602388224969589104824497835E-09, \
      +0.1188914710784643834240845251963E-10, \
      -0.3149916527963241364538648629619E-10, \
      -0.1321581184044771311875407399267E-10, \
      -0.1794178531506806117779435740269E-11, \
      +0.7180124451383666233671064293469E-12, \
      +0.3852778382742142701140898017776E-12, \
      +0.1540086217521409826913258233397E-13, \
      -0.4150569347287222086626899720156E-13, \
      -0.9554846698828307648702144943125E-14, \
      +0.3811680669352622420746055355118E-14, \
      +0.1772560133056526383604932666758E-14, \
      -0.3425485619677219134619247903282E-15, \
      -0.2827623980516583484942055937594E-15, \
      +0.3461222867697461093097062508134E-16, \
      +0.4465621420296759999010420542843E-16, \
      -0.4830504485944182071255254037954E-17, \
      -0.7233180487874753954562272409245E-17, \
      +0.9921475412173698598880460939810E-18, \
      +0.1193650890845982085504399499242E-17, \
      -0.2488709837150807235720544916602E-18, \
      -0.1938426454160905928984697811326E-18, \
      +0.6444656697373443868783019493949E-19, \
      +0.2886051596289224326481713830734E-19, \
      -0.1601954907174971807061671562007E-19, \
      -0.3270815010592314720891935674859E-20, \
      +0.3686932283826409181146007239393E-20, \
      +0.1268297648030950153013595297109E-22, \
      -0.7549825019377273907696366644101E-21, \
      +0.1502133571377835349637127890534E-21, \
      +0.1265195883509648534932087992483E-21, \
      -0.6100998370083680708629408916002E-22, \
      -0.1268809629260128264368720959242E-22, \
      +0.1661016099890741457840384874905E-22, \
      -0.1585194335765885579379705048814E-23, \
      -0.3302645405968217800953817667556E-23, \
      +0.1313580902839239781740396231174E-23, \
      +0.3689040246671156793314256372804E-24, \
      -0.4210141910461689149219782472499E-24, \
      +0.4791954591082865780631714013730E-25, \
      +0.8459470390221821795299717074124E-25, \
      -0.4039800940872832493146079371810E-25, \
      -0.6434714653650431347301008504695E-26, \
      +0.1225743398875665990344647369905E-25, \
      -0.2934391316025708923198798211754E-26, \
      -0.1961311309194982926203712057289E-26, \
      +0.1503520374822193424162299003098E-26, \
      -0.9588720515744826552033863882069E-28, \
      -0.3483339380817045486394411085114E-27, \
      +0.1690903610263043673062449607256E-27, \
      +0.1982866538735603043894001157188E-28, \
      -0.5317498081491816214575830025284E-28, \
      +0.1803306629888392946235014503901E-28, \
      +0.6213093341454893175884053112422E-29, \
      -0.7692189292772161863200728066730E-29, \
      +0.1858252826111702542625560165963E-29, \
      +0.1237585142281395724899271545541E-29, \
      -0.1102259120409223803217794787792E-29, \
      +0.1886287118039704490077874479431E-30, \
      +0.2160196872243658913149031414060E-30, \
      -0.1605454124919743200584465949655E-30, \
      +0.1965352984594290603938848073318E-31 ] )

  ai0cs = np.array ( [ \
      +0.7575994494023795942729872037438E-01, \
      +0.7591380810823345507292978733204E-02, \
      +0.4153131338923750501863197491382E-03, \
      +0.1070076463439073073582429702170E-04, \
      -0.7901179979212894660750319485730E-05, \
      -0.7826143501438752269788989806909E-06, \
      +0.2783849942948870806381185389857E-06, \
      +0.8252472600612027191966829133198E-08, \
      -0.1204463945520199179054960891103E-07, \
      +0.1559648598506076443612287527928E-08, \
      +0.2292556367103316543477254802857E-09, \
      -0.1191622884279064603677774234478E-09, \
      +0.1757854916032409830218331247743E-10, \
      +0.1128224463218900517144411356824E-11, \
      -0.1146848625927298877729633876982E-11, \
      +0.2715592054803662872643651921606E-12, \
      -0.2415874666562687838442475720281E-13, \
      -0.6084469888255125064606099639224E-14, \
      +0.3145705077175477293708360267303E-14, \
      -0.7172212924871187717962175059176E-15, \
      +0.7874493403454103396083909603327E-16, \
      +0.1004802753009462402345244571839E-16, \
      -0.7566895365350534853428435888810E-17, \
      +0.2150380106876119887812051287845E-17, \
      -0.3754858341830874429151584452608E-18, \
      +0.2354065842226992576900757105322E-19, \
      +0.1114667612047928530226373355110E-19, \
      -0.5398891884396990378696779322709E-20, \
      +0.1439598792240752677042858404522E-20, \
      -0.2591916360111093406460818401962E-21, \
      +0.2238133183998583907434092298240E-22, \
      +0.5250672575364771172772216831999E-23, \
      -0.3249904138533230784173432285866E-23, \
      +0.9924214103205037927857284710400E-24, \
      -0.2164992254244669523146554299733E-24, \
      +0.3233609471943594083973332991999E-25, \
      -0.1184620207396742489824733866666E-26, \
      -0.1281671853950498650548338687999E-26, \
      +0.5827015182279390511605568853333E-27, \
      -0.1668222326026109719364501503999E-27, \
      +0.3625309510541569975700684800000E-28, \
      -0.5733627999055713589945958399999E-29, \
      +0.3736796722063098229642581333333E-30, \
      +0.1602073983156851963365512533333E-30, \
      -0.8700424864057229884522495999999E-31, \
      +0.2741320937937481145603413333333E-31 ] )

  bi0cs = np.array ( [ \
      -0.7660547252839144951081894976243285E-01, \
      +0.1927337953993808269952408750881196E+01, \
      +0.2282644586920301338937029292330415, \
      +0.1304891466707290428079334210691888E-01, \
      +0.4344270900816487451378682681026107E-03, \
      +0.9422657686001934663923171744118766E-05, \
      +0.1434006289510691079962091878179957E-06, \
      +0.1613849069661749069915419719994611E-08, \
      +0.1396650044535669699495092708142522E-10, \
      +0.9579451725505445344627523171893333E-13, \
      +0.5333981859862502131015107744000000E-15, \
      +0.2458716088437470774696785919999999E-17, \
      +0.9535680890248770026944341333333333E-20, \
      +0.3154382039721427336789333333333333E-22, \
      +0.9004564101094637431466666666666666E-25, \
      +0.2240647369123670016000000000000000E-27, \
      +0.4903034603242837333333333333333333E-30, \
      +0.9508172606122666666666666666666666E-33 ] )

  eta = 0.1 * r8_mach ( 3 )
  nti0 = r8_inits ( bi0cs, 18, eta )
  ntai0 = r8_inits ( ai0cs, 46, eta )
  ntai02 = r8_inits ( ai02cs, 69, eta )
  xsml = np.sqrt ( 8.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= xsml ):
    value = 1.0
  elif ( y <= 3.0 ):
    value = np.exp ( - y ) * ( 2.75 \
      + r8_csevl ( y * y / 4.5 - 1.0, bi0cs, nti0 ) )
  elif ( y <= 8.0 ):
    value = ( 0.375 + r8_csevl ( ( 48.0 / y - 11.0 ) / 5.0, \
      ai0cs, ntai0 ) ) / np.sqrt ( y )
  else:
    value = ( 0.375 + r8_csevl ( 16.0 / y - 1.0, ai02cs, ntai02 ) ) \
      / np.sqrt ( y )

  return value

def r8_besk0 ( x ):

#*****************************************************************************80
#
## r8_besk0() evaluates the Bessel function K of order 0 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  bk0cs = np.array ( [ \
      -0.353273932339027687201140060063153E-01, \
      +0.344289899924628486886344927529213, \
      +0.359799365153615016265721303687231E-01, \
      +0.126461541144692592338479508673447E-02, \
      +0.228621210311945178608269830297585E-04, \
      +0.253479107902614945730790013428354E-06, \
      +0.190451637722020885897214059381366E-08, \
      +0.103496952576336245851008317853089E-10, \
      +0.425981614279108257652445327170133E-13, \
      +0.137446543588075089694238325440000E-15, \
      +0.357089652850837359099688597333333E-18, \
      +0.763164366011643737667498666666666E-21, \
      +0.136542498844078185908053333333333E-23, \
      +0.207527526690666808319999999999999E-26, \
      +0.271281421807298560000000000000000E-29, \
      +0.308259388791466666666666666666666E-32 ] )

  ntk0 = r8_inits ( bk0cs, 16, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )
  xmax = - np.log ( r8_mach ( 1 ) )
  xmax = xmax - 0.5 * xmax * np.log ( xmax ) / ( xmax + 0.5 )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_besk0 = Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_besk0 = Fatal error!' )
  elif ( x <= xsml ):
    y = 0.0
    value = - np.log ( 0.5 * x ) * r8_besi0 ( x ) \
      - 0.25 + r8_csevl ( 0.5 * y - 1.0, bk0cs, ntk0 )
  elif ( x <= 2.0 ):
    y = x * x
    value = - np.log ( 0.5 * x ) * r8_besi0 ( x ) \
      - 0.25 + r8_csevl ( 0.5 * y - 1.0, bk0cs, ntk0 )
  elif ( x <= xmax ):
    value = np.exp ( - x ) * r8_besk0e ( x )
  else:
    value = 0.0

  return value

def r8_besk0_test ( ):

#*****************************************************************************80
#
## r8_besk0_test() tests r8_besk0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_besk0_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besk0 evaluates Bessel functions K0(X)' )
  print ( '' )
  print ( '             X       BESK0(X)  r8_besk0(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_k0_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besk0 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besk0e ( x ):

#*****************************************************************************80
#
## r8_besk0e() evaluates the exponentially scaled Bessel function K0(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ak02cs = np.array ( [ \
      -0.1201869826307592239839346212452E-01, \
      -0.9174852691025695310652561075713E-02, \
      +0.1444550931775005821048843878057E-03, \
      -0.4013614175435709728671021077879E-05, \
      +0.1567831810852310672590348990333E-06, \
      -0.7770110438521737710315799754460E-08, \
      +0.4611182576179717882533130529586E-09, \
      -0.3158592997860565770526665803309E-10, \
      +0.2435018039365041127835887814329E-11, \
      -0.2074331387398347897709853373506E-12, \
      +0.1925787280589917084742736504693E-13, \
      -0.1927554805838956103600347182218E-14, \
      +0.2062198029197818278285237869644E-15, \
      -0.2341685117579242402603640195071E-16, \
      +0.2805902810643042246815178828458E-17, \
      -0.3530507631161807945815482463573E-18, \
      +0.4645295422935108267424216337066E-19, \
      -0.6368625941344266473922053461333E-20, \
      +0.9069521310986515567622348800000E-21, \
      -0.1337974785423690739845005311999E-21, \
      +0.2039836021859952315522088960000E-22, \
      -0.3207027481367840500060869973333E-23, \
      +0.5189744413662309963626359466666E-24, \
      -0.8629501497540572192964607999999E-25, \
      +0.1472161183102559855208038400000E-25, \
      -0.2573069023867011283812351999999E-26, \
      +0.4601774086643516587376640000000E-27, \
      -0.8411555324201093737130666666666E-28, \
      +0.1569806306635368939301546666666E-28, \
      -0.2988226453005757788979199999999E-29, \
      +0.5796831375216836520618666666666E-30, \
      -0.1145035994347681332155733333333E-30, \
      +0.2301266594249682802005333333333E-31 ] )

  ak0cs = np.array ( [ \
      -0.7643947903327941424082978270088E-01, \
      -0.2235652605699819052023095550791E-01, \
      +0.7734181154693858235300618174047E-03, \
      -0.4281006688886099464452146435416E-04, \
      +0.3081700173862974743650014826660E-05, \
      -0.2639367222009664974067448892723E-06, \
      +0.2563713036403469206294088265742E-07, \
      -0.2742705549900201263857211915244E-08, \
      +0.3169429658097499592080832873403E-09, \
      -0.3902353286962184141601065717962E-10, \
      +0.5068040698188575402050092127286E-11, \
      -0.6889574741007870679541713557984E-12, \
      +0.9744978497825917691388201336831E-13, \
      -0.1427332841884548505389855340122E-13, \
      +0.2156412571021463039558062976527E-14, \
      -0.3349654255149562772188782058530E-15, \
      +0.5335260216952911692145280392601E-16, \
      -0.8693669980890753807639622378837E-17, \
      +0.1446404347862212227887763442346E-17, \
      -0.2452889825500129682404678751573E-18, \
      +0.4233754526232171572821706342400E-19, \
      -0.7427946526454464195695341294933E-20, \
      +0.1323150529392666866277967462400E-20, \
      -0.2390587164739649451335981465599E-21, \
      +0.4376827585923226140165712554666E-22, \
      -0.8113700607345118059339011413333E-23, \
      +0.1521819913832172958310378154666E-23, \
      -0.2886041941483397770235958613333E-24, \
      +0.5530620667054717979992610133333E-25, \
      -0.1070377329249898728591633066666E-25, \
      +0.2091086893142384300296328533333E-26, \
      -0.4121713723646203827410261333333E-27, \
      +0.8193483971121307640135680000000E-28, \
      -0.1642000275459297726780757333333E-28, \
      +0.3316143281480227195890346666666E-29, \
      -0.6746863644145295941085866666666E-30, \
      +0.1382429146318424677635413333333E-30, \
      -0.2851874167359832570811733333333E-31 ] )

  bk0cs = np.array ( [ \
      -0.353273932339027687201140060063153E-01, \
      +0.344289899924628486886344927529213, \
      +0.359799365153615016265721303687231E-01, \
      +0.126461541144692592338479508673447E-02, \
      +0.228621210311945178608269830297585E-04, \
      +0.253479107902614945730790013428354E-06, \
      +0.190451637722020885897214059381366E-08, \
      +0.103496952576336245851008317853089E-10, \
      +0.425981614279108257652445327170133E-13, \
      +0.137446543588075089694238325440000E-15, \
      +0.357089652850837359099688597333333E-18, \
      +0.763164366011643737667498666666666E-21, \
      +0.136542498844078185908053333333333E-23, \
      +0.207527526690666808319999999999999E-26, \
      +0.271281421807298560000000000000000E-29, \
      +0.308259388791466666666666666666666E-32 ] )

  eta = 0.1 * r8_mach ( 3 )
  ntk0 = r8_inits ( bk0cs, 16, eta )
  ntak0 = r8_inits ( ak0cs, 38, eta )
  ntak02 = r8_inits ( ak02cs, 33, eta )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_besk0e = Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_besk0e = Fatal error!' )
  elif ( x <= xsml ):
    y = 0.0
    value = np.exp ( x ) * ( - np.log ( 0.5 * x ) * r8_besi0 ( x ) - 0.25 \
      + r8_csevl ( 0.5 * y - 1.0, bk0cs, ntk0 ) )
  elif ( x <= 2.0 ):
    y = x * x
    value = np.exp ( x ) * ( - np.log ( 0.5 * x ) * r8_besi0 ( x ) - 0.25 \
      + r8_csevl ( 0.5 * y - 1.0, bk0cs, ntk0 ) )
  elif ( x <= 8.0 ):
    value = ( 1.25 \
      + r8_csevl ( ( 16.0 / x - 5.0 ) / 3.0, ak0cs, ntak0 ) ) / np.sqrt ( x )
  else:
    value = ( 1.25 + r8_csevl ( 16.0 / x - 1.0, ak02cs, ntak02 ) ) \
      / np.sqrt ( x )

  return value

def r8_besi1 ( x ):

#*****************************************************************************80
#
## r8_besi1() evaluates the Bessel function I of order 1 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, function value at X.
#
  import numpy as np

  bi1cs = np.array ( [ \
      -0.19717132610998597316138503218149E-02, \
      +0.40734887667546480608155393652014, \
      +0.34838994299959455866245037783787E-01, \
      +0.15453945563001236038598401058489E-02, \
      +0.41888521098377784129458832004120E-04, \
      +0.76490267648362114741959703966069E-06, \
      +0.10042493924741178689179808037238E-07, \
      +0.99322077919238106481371298054863E-10, \
      +0.76638017918447637275200171681349E-12, \
      +0.47414189238167394980388091948160E-14, \
      +0.24041144040745181799863172032000E-16, \
      +0.10171505007093713649121100799999E-18, \
      +0.36450935657866949458491733333333E-21, \
      +0.11205749502562039344810666666666E-23, \
      +0.29875441934468088832000000000000E-26, \
      +0.69732310939194709333333333333333E-29, \
      +0.14367948220620800000000000000000E-31 ] )

  nti1 = r8_inits ( bi1cs, 17, 0.1 * r8_mach ( 3 ) )
  xmin = 2.0 * r8_mach ( 1 )
  xsml = np.sqrt ( 8.0 * r8_mach ( 3 ) )
  xmax = np.log ( r8_mach ( 2 ) )

  y = abs ( x )

  if ( y <= xmin ):
    value = 0.0
  elif ( y <= xsml ):
    value = 0.5 * x
  elif ( y <= 3.0 ):
    value = x * ( 0.875 + r8_csevl ( y * y / 4.5 - 1.0, bi1cs, nti1 ) )
  elif ( y <= xmax ):
    value = np.exp ( y ) * r8_besi1e ( x )
  else:
    print ( '' )
    print ( 'r8_besi1 - Fatal error!' )
    print ( '  Result overflows.' )
    raise Exception ( 'r8_besi1 - Fatal error!' )

  return value

def r8_besi1_test ( ):

#*****************************************************************************80
#
## r8_besi1_test() tests r8_besi1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_besi1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besi1 evaluates the Bessel I1(x) function' )
  print ( '' )
  print ( '             X       BESI1(X)  r8_besi1(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_i1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besi1 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besi1e ( x ):

#*****************************************************************************80
#
## r8_besi1e() evaluates the exponentially scaled Bessel function I1(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ai12cs = np.array ( [ \
    +0.2857623501828012047449845948469E-01, \
    -0.9761097491361468407765164457302E-02, \
    -0.1105889387626237162912569212775E-03, \
    -0.3882564808877690393456544776274E-05, \
    -0.2512236237870208925294520022121E-06, \
    -0.2631468846889519506837052365232E-07, \
    -0.3835380385964237022045006787968E-08, \
    -0.5589743462196583806868112522229E-09, \
    -0.1897495812350541234498925033238E-10, \
    +0.3252603583015488238555080679949E-10, \
    +0.1412580743661378133163366332846E-10, \
    +0.2035628544147089507224526136840E-11, \
    -0.7198551776245908512092589890446E-12, \
    -0.4083551111092197318228499639691E-12, \
    -0.2101541842772664313019845727462E-13, \
    +0.4272440016711951354297788336997E-13, \
    +0.1042027698412880276417414499948E-13, \
    -0.3814403072437007804767072535396E-14, \
    -0.1880354775510782448512734533963E-14, \
    +0.3308202310920928282731903352405E-15, \
    +0.2962628997645950139068546542052E-15, \
    -0.3209525921993423958778373532887E-16, \
    -0.4650305368489358325571282818979E-16, \
    +0.4414348323071707949946113759641E-17, \
    +0.7517296310842104805425458080295E-17, \
    -0.9314178867326883375684847845157E-18, \
    -0.1242193275194890956116784488697E-17, \
    +0.2414276719454848469005153902176E-18, \
    +0.2026944384053285178971922860692E-18, \
    -0.6394267188269097787043919886811E-19, \
    -0.3049812452373095896084884503571E-19, \
    +0.1612841851651480225134622307691E-19, \
    +0.3560913964309925054510270904620E-20, \
    -0.3752017947936439079666828003246E-20, \
    -0.5787037427074799345951982310741E-22, \
    +0.7759997511648161961982369632092E-21, \
    -0.1452790897202233394064459874085E-21, \
    -0.1318225286739036702121922753374E-21, \
    +0.6116654862903070701879991331717E-22, \
    +0.1376279762427126427730243383634E-22, \
    -0.1690837689959347884919839382306E-22, \
    +0.1430596088595433153987201085385E-23, \
    +0.3409557828090594020405367729902E-23, \
    -0.1309457666270760227845738726424E-23, \
    -0.3940706411240257436093521417557E-24, \
    +0.4277137426980876580806166797352E-24, \
    -0.4424634830982606881900283123029E-25, \
    -0.8734113196230714972115309788747E-25, \
    +0.4045401335683533392143404142428E-25, \
    +0.7067100658094689465651607717806E-26, \
    -0.1249463344565105223002864518605E-25, \
    +0.2867392244403437032979483391426E-26, \
    +0.2044292892504292670281779574210E-26, \
    -0.1518636633820462568371346802911E-26, \
    +0.8110181098187575886132279107037E-28, \
    +0.3580379354773586091127173703270E-27, \
    -0.1692929018927902509593057175448E-27, \
    -0.2222902499702427639067758527774E-28, \
    +0.5424535127145969655048600401128E-28, \
    -0.1787068401578018688764912993304E-28, \
    -0.6565479068722814938823929437880E-29, \
    +0.7807013165061145280922067706839E-29, \
    -0.1816595260668979717379333152221E-29, \
    -0.1287704952660084820376875598959E-29, \
    +0.1114548172988164547413709273694E-29, \
    -0.1808343145039336939159368876687E-30, \
    -0.2231677718203771952232448228939E-30, \
    +0.1619029596080341510617909803614E-30, \
    -0.1834079908804941413901308439210E-31 ] )

  ai1cs = np.array ( [ \
    -0.2846744181881478674100372468307E-01, \
    -0.1922953231443220651044448774979E-01, \
    -0.6115185857943788982256249917785E-03, \
    -0.2069971253350227708882823777979E-04, \
    +0.8585619145810725565536944673138E-05, \
    +0.1049498246711590862517453997860E-05, \
    -0.2918338918447902202093432326697E-06, \
    -0.1559378146631739000160680969077E-07, \
    +0.1318012367144944705525302873909E-07, \
    -0.1448423418183078317639134467815E-08, \
    -0.2908512243993142094825040993010E-09, \
    +0.1266388917875382387311159690403E-09, \
    -0.1664947772919220670624178398580E-10, \
    -0.1666653644609432976095937154999E-11, \
    +0.1242602414290768265232168472017E-11, \
    -0.2731549379672432397251461428633E-12, \
    +0.2023947881645803780700262688981E-13, \
    +0.7307950018116883636198698126123E-14, \
    -0.3332905634404674943813778617133E-14, \
    +0.7175346558512953743542254665670E-15, \
    -0.6982530324796256355850629223656E-16, \
    -0.1299944201562760760060446080587E-16, \
    +0.8120942864242798892054678342860E-17, \
    -0.2194016207410736898156266643783E-17, \
    +0.3630516170029654848279860932334E-18, \
    -0.1695139772439104166306866790399E-19, \
    -0.1288184829897907807116882538222E-19, \
    +0.5694428604967052780109991073109E-20, \
    -0.1459597009090480056545509900287E-20, \
    +0.2514546010675717314084691334485E-21, \
    -0.1844758883139124818160400029013E-22, \
    -0.6339760596227948641928609791999E-23, \
    +0.3461441102031011111108146626560E-23, \
    -0.1017062335371393547596541023573E-23, \
    +0.2149877147090431445962500778666E-24, \
    -0.3045252425238676401746206173866E-25, \
    +0.5238082144721285982177634986666E-27, \
    +0.1443583107089382446416789503999E-26, \
    -0.6121302074890042733200670719999E-27, \
    +0.1700011117467818418349189802666E-27, \
    -0.3596589107984244158535215786666E-28, \
    +0.5448178578948418576650513066666E-29, \
    -0.2731831789689084989162564266666E-30, \
    -0.1858905021708600715771903999999E-30, \
    +0.9212682974513933441127765333333E-31, \
    -0.2813835155653561106370833066666E-31 ] )

  bi1cs = np.array ( [ \
    -0.19717132610998597316138503218149E-02, \
    +0.40734887667546480608155393652014E+00, \
    +0.34838994299959455866245037783787E-01, \
    +0.15453945563001236038598401058489E-02, \
    +0.41888521098377784129458832004120E-04, \
    +0.76490267648362114741959703966069E-06, \
    +0.10042493924741178689179808037238E-07, \
    +0.99322077919238106481371298054863E-10, \
    +0.76638017918447637275200171681349E-12, \
    +0.47414189238167394980388091948160E-14, \
    +0.24041144040745181799863172032000E-16, \
    +0.10171505007093713649121100799999E-18, \
    +0.36450935657866949458491733333333E-21, \
    +0.11205749502562039344810666666666E-23, \
    +0.29875441934468088832000000000000E-26, \
    +0.69732310939194709333333333333333E-29, \
    +0.14367948220620800000000000000000E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  nti1 = r8_inits ( bi1cs, 17, eta )
  ntai1 = r8_inits ( ai1cs, 46, eta )
  ntai12 = r8_inits ( ai12cs, 69, eta )
  xmin = 2.0 * r8_mach ( 1 )
  xsml = np.sqrt ( 8.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= xmin ):
    value = 0.0
  elif ( y <= xsml ):
    value = 0.5 * x * np.exp ( - y )
  elif ( y <= 3.0 ):
    value = x * ( 0.875 + r8_csevl ( y * y / 4.5 - 1.0, bi1cs, nti1 ) ) \
      * np.exp ( - y )
  elif ( y <= 8.0 ):
    value = ( 0.375 + r8_csevl ( ( 48.0 / y - 11.0) / 5.0, \
      ai1cs, ntai1 ) ) / np.sqrt ( y )
    if ( x < 0.0 ):
      value = - value
  else:
    value = ( 0.375 + r8_csevl ( 16.0 / y - 1.0, ai12cs, ntai12 ) ) \
      / np.sqrt ( y )
    if ( x < 0.0 ):
      value = - value

  return value

def r8_besk1 ( x ):

#*****************************************************************************80
#
## r8_besk1() evaluates the Bessel function K of order 1 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  bk1cs = np.array ( [ \
      +0.25300227338947770532531120868533E-01, \
      -0.35315596077654487566723831691801, \
      -0.12261118082265714823479067930042, \
      -0.69757238596398643501812920296083E-02, \
      -0.17302889575130520630176507368979E-03, \
      -0.24334061415659682349600735030164E-05, \
      -0.22133876307347258558315252545126E-07, \
      -0.14114883926335277610958330212608E-09, \
      -0.66669016941993290060853751264373E-12, \
      -0.24274498505193659339263196864853E-14, \
      -0.70238634793862875971783797120000E-17, \
      -0.16543275155100994675491029333333E-19, \
      -0.32338347459944491991893333333333E-22, \
      -0.53312750529265274999466666666666E-25, \
      -0.75130407162157226666666666666666E-28, \
      -0.91550857176541866666666666666666E-31 ] )

  ntk1 = r8_inits ( bk1cs, 16, 0.1 * r8_mach ( 3 ) )
  xmin = np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) ) + 0.01 )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )
  xmax = - np.log ( r8_mach ( 1 ) )
  xmax = xmax - 0.5 * xmax * np.log ( xmax ) / ( xmax + 0.5 ) - 0.01

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_besk1 = Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_besk1 - Fatal error!' )
  elif ( x <= xsml ):
    y = 0.0
    value = np.log ( 0.5 * x ) * r8_besi1 ( x ) + ( 0.75 \
      + r8_csevl ( 0.5 * y - 1.0, bk1cs, ntk1 ) ) / x
  elif ( x <= 2.0 ):
    y = x * x
    value = np.log ( 0.5 * x ) * r8_besi1 ( x ) + ( 0.75 \
      + r8_csevl ( 0.5 * y - 1.0, bk1cs, ntk1 ) ) / x
  elif ( x <= xmax ):
    value = np.exp ( - x ) * r8_besk1e ( x )
  else:
    value = 0.0

  return value

def r8_besk1_test ( ):

#*****************************************************************************80
#
## r8_besk1_test() tests r8_besk1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_besk1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besk1 evaluates Bessel functions K1(x)' )
  print ( '' )
  print ( '             X       BESK1(X)  r8_besk1(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_k1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besk1 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besk1e ( x ):

#*****************************************************************************80
#
## r8_besk1e() evaluates the exponentially scaled Bessel function K1(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ak12cs = np.array ( [ \
      +0.6379308343739001036600488534102E-01, \
      +0.2832887813049720935835030284708E-01, \
      -0.2475370673905250345414545566732E-03, \
      +0.5771972451607248820470976625763E-05, \
      -0.2068939219536548302745533196552E-06, \
      +0.9739983441381804180309213097887E-08, \
      -0.5585336140380624984688895511129E-09, \
      +0.3732996634046185240221212854731E-10, \
      -0.2825051961023225445135065754928E-11, \
      +0.2372019002484144173643496955486E-12, \
      -0.2176677387991753979268301667938E-13, \
      +0.2157914161616032453939562689706E-14, \
      -0.2290196930718269275991551338154E-15, \
      +0.2582885729823274961919939565226E-16, \
      -0.3076752641268463187621098173440E-17, \
      +0.3851487721280491597094896844799E-18, \
      -0.5044794897641528977117282508800E-19, \
      +0.6888673850418544237018292223999E-20, \
      -0.9775041541950118303002132480000E-21, \
      +0.1437416218523836461001659733333E-21, \
      -0.2185059497344347373499733333333E-22, \
      +0.3426245621809220631645388800000E-23, \
      -0.5531064394246408232501248000000E-24, \
      +0.9176601505685995403782826666666E-25, \
      -0.1562287203618024911448746666666E-25, \
      +0.2725419375484333132349439999999E-26, \
      -0.4865674910074827992378026666666E-27, \
      +0.8879388552723502587357866666666E-28, \
      -0.1654585918039257548936533333333E-28, \
      +0.3145111321357848674303999999999E-29, \
      -0.6092998312193127612416000000000E-30, \
      +0.1202021939369815834623999999999E-30, \
      -0.2412930801459408841386666666666E-31 ] )

  ak1cs = np.array ( [ \
      +0.27443134069738829695257666227266, \
      +0.75719899531993678170892378149290E-01, \
      -0.14410515564754061229853116175625E-02, \
      +0.66501169551257479394251385477036E-04, \
      -0.43699847095201407660580845089167E-05, \
      +0.35402774997630526799417139008534E-06, \
      -0.33111637792932920208982688245704E-07, \
      +0.34459775819010534532311499770992E-08, \
      -0.38989323474754271048981937492758E-09, \
      +0.47208197504658356400947449339005E-10, \
      -0.60478356628753562345373591562890E-11, \
      +0.81284948748658747888193837985663E-12, \
      -0.11386945747147891428923915951042E-12, \
      +0.16540358408462282325972948205090E-13, \
      -0.24809025677068848221516010440533E-14, \
      +0.38292378907024096948429227299157E-15, \
      -0.60647341040012418187768210377386E-16, \
      +0.98324256232648616038194004650666E-17, \
      -0.16284168738284380035666620115626E-17, \
      +0.27501536496752623718284120337066E-18, \
      -0.47289666463953250924281069568000E-19, \
      +0.82681500028109932722392050346666E-20, \
      -0.14681405136624956337193964885333E-20, \
      +0.26447639269208245978085894826666E-21, \
      -0.48290157564856387897969868800000E-22, \
      +0.89293020743610130180656332799999E-23, \
      -0.16708397168972517176997751466666E-23, \
      +0.31616456034040694931368618666666E-24, \
      -0.60462055312274989106506410666666E-25, \
      +0.11678798942042732700718421333333E-25, \
      -0.22773741582653996232867840000000E-26, \
      +0.44811097300773675795305813333333E-27, \
      -0.88932884769020194062336000000000E-28, \
      +0.17794680018850275131392000000000E-28, \
      -0.35884555967329095821994666666666E-29, \
      +0.72906290492694257991679999999999E-30, \
      -0.14918449845546227073024000000000E-30, \
      +0.30736573872934276300799999999999E-31 ] )

  bk1cs = np.array ( [ \
      +0.25300227338947770532531120868533E-01, \
      -0.35315596077654487566723831691801, \
      -0.12261118082265714823479067930042, \
      -0.69757238596398643501812920296083E-02, \
      -0.17302889575130520630176507368979E-03, \
      -0.24334061415659682349600735030164E-05, \
      -0.22133876307347258558315252545126E-07, \
      -0.14114883926335277610958330212608E-09, \
      -0.66669016941993290060853751264373E-12, \
      -0.24274498505193659339263196864853E-14, \
      -0.70238634793862875971783797120000E-17, \
      -0.16543275155100994675491029333333E-19, \
      -0.32338347459944491991893333333333E-22, \
      -0.53312750529265274999466666666666E-25, \
      -0.75130407162157226666666666666666E-28, \
      -0.91550857176541866666666666666666E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  ntk1 = r8_inits ( bk1cs, 16, eta )
  ntak1 = r8_inits ( ak1cs, 38, eta )
  ntak12 = r8_inits ( ak12cs, 33, eta )
  xmin = np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) ) + 0.01 )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_besk1e = Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_besk1e - Fatal error!' )
  elif ( x <= xsml ):
    y = 0.0
    value = np.exp ( x ) * ( np.log ( 0.5 * x ) * r8_besi1 ( x ) \
      + ( 0.75 + r8_csevl ( 0.5 * y - 1.0, bk1cs, ntk1 ) ) / x )
  elif ( x <= 2.0 ):
    y = x * x
    value = np.exp ( x ) * ( np.log ( 0.5 * x ) * r8_besi1 ( x ) \
      + ( 0.75 + r8_csevl ( 0.5 * y - 1.0, bk1cs, ntk1 ) ) / x )
  elif ( x <= 8.0 ):
    value = ( 1.25 + r8_csevl ( ( 16.0 / x - 5.0 ) / 3.0, ak1cs, \
      ntak1 ) ) / np.sqrt ( x )
  else:
    value = ( 1.25 + r8_csevl ( 16.0 / x - 1.0, ak12cs, ntak12 ) ) / np.sqrt ( x )

  return value

def r8_b0mp ( x ):

#*****************************************************************************80
#
## r8_b0mp() evaluates the modulus and phase for the Bessel J0 and Y0 functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real AMPL, THETA, the modulus and phase.
#
  import numpy as np

  bm0cs = np.array ( [ \
      +0.9211656246827742712573767730182E-01, \
      -0.1050590997271905102480716371755E-02, \
      +0.1470159840768759754056392850952E-04, \
      -0.5058557606038554223347929327702E-06, \
      +0.2787254538632444176630356137881E-07, \
      -0.2062363611780914802618841018973E-08, \
      +0.1870214313138879675138172596261E-09, \
      -0.1969330971135636200241730777825E-10, \
      +0.2325973793999275444012508818052E-11, \
      -0.3009520344938250272851224734482E-12, \
      +0.4194521333850669181471206768646E-13, \
      -0.6219449312188445825973267429564E-14, \
      +0.9718260411336068469601765885269E-15, \
      -0.1588478585701075207366635966937E-15, \
      +0.2700072193671308890086217324458E-16, \
      -0.4750092365234008992477504786773E-17, \
      +0.8615128162604370873191703746560E-18, \
      -0.1605608686956144815745602703359E-18, \
      +0.3066513987314482975188539801599E-19, \
      -0.5987764223193956430696505617066E-20, \
      +0.1192971253748248306489069841066E-20, \
      -0.2420969142044805489484682581333E-21, \
      +0.4996751760510616453371002879999E-22, \
      -0.1047493639351158510095040511999E-22, \
      +0.2227786843797468101048183466666E-23, \
      -0.4801813239398162862370542933333E-24, \
      +0.1047962723470959956476996266666E-24, \
      -0.2313858165678615325101260800000E-25, \
      +0.5164823088462674211635199999999E-26, \
      -0.1164691191850065389525401599999E-26, \
      +0.2651788486043319282958336000000E-27, \
      -0.6092559503825728497691306666666E-28, \
      +0.1411804686144259308038826666666E-28, \
      -0.3298094961231737245750613333333E-29, \
      +0.7763931143074065031714133333333E-30, \
      -0.1841031343661458478421333333333E-30, \
      +0.4395880138594310737100799999999E-31 ] )

  bm02cs = np.array ( [ \
      +0.9500415145228381369330861335560E-01, \
      -0.3801864682365670991748081566851E-03, \
      +0.2258339301031481192951829927224E-05, \
      -0.3895725802372228764730621412605E-07, \
      +0.1246886416512081697930990529725E-08, \
      -0.6065949022102503779803835058387E-10, \
      +0.4008461651421746991015275971045E-11, \
      -0.3350998183398094218467298794574E-12, \
      +0.3377119716517417367063264341996E-13, \
      -0.3964585901635012700569356295823E-14, \
      +0.5286111503883857217387939744735E-15, \
      -0.7852519083450852313654640243493E-16, \
      +0.1280300573386682201011634073449E-16, \
      -0.2263996296391429776287099244884E-17, \
      +0.4300496929656790388646410290477E-18, \
      -0.8705749805132587079747535451455E-19, \
      +0.1865862713962095141181442772050E-19, \
      -0.4210482486093065457345086972301E-20, \
      +0.9956676964228400991581627417842E-21, \
      -0.2457357442805313359605921478547E-21, \
      +0.6307692160762031568087353707059E-22, \
      -0.1678773691440740142693331172388E-22, \
      +0.4620259064673904433770878136087E-23, \
      -0.1311782266860308732237693402496E-23, \
      +0.3834087564116302827747922440276E-24, \
      -0.1151459324077741271072613293576E-24, \
      +0.3547210007523338523076971345213E-25, \
      -0.1119218385815004646264355942176E-25, \
      +0.3611879427629837831698404994257E-26, \
      -0.1190687765913333150092641762463E-26, \
      +0.4005094059403968131802476449536E-27, \
      -0.1373169422452212390595193916017E-27, \
      +0.4794199088742531585996491526437E-28, \
      -0.1702965627624109584006994476452E-28, \
      +0.6149512428936330071503575161324E-29, \
      -0.2255766896581828349944300237242E-29, \
      +0.8399707509294299486061658353200E-30, \
      -0.3172997595562602355567423936152E-30, \
      +0.1215205298881298554583333026514E-30, \
      -0.4715852749754438693013210568045E-31 ] )

  bt02cs = np.array ( [ \
      -0.24548295213424597462050467249324, \
      +0.12544121039084615780785331778299E-02, \
      -0.31253950414871522854973446709571E-04, \
      +0.14709778249940831164453426969314E-05, \
      -0.99543488937950033643468850351158E-07, \
      +0.85493166733203041247578711397751E-08, \
      -0.86989759526554334557985512179192E-09, \
      +0.10052099533559791084540101082153E-09, \
      -0.12828230601708892903483623685544E-10, \
      +0.17731700781805131705655750451023E-11, \
      -0.26174574569485577488636284180925E-12, \
      +0.40828351389972059621966481221103E-13, \
      -0.66751668239742720054606749554261E-14, \
      +0.11365761393071629448392469549951E-14, \
      -0.20051189620647160250559266412117E-15, \
      +0.36497978794766269635720591464106E-16, \
      -0.68309637564582303169355843788800E-17, \
      +0.13107583145670756620057104267946E-17, \
      -0.25723363101850607778757130649599E-18, \
      +0.51521657441863959925267780949333E-19, \
      -0.10513017563758802637940741461333E-19, \
      +0.21820381991194813847301084501333E-20, \
      -0.46004701210362160577225905493333E-21, \
      +0.98407006925466818520953651199999E-22, \
      -0.21334038035728375844735986346666E-22, \
      +0.46831036423973365296066286933333E-23, \
      -0.10400213691985747236513382399999E-23, \
      +0.23349105677301510051777740800000E-24, \
      -0.52956825323318615788049749333333E-25, \
      +0.12126341952959756829196287999999E-25, \
      -0.28018897082289428760275626666666E-26, \
      +0.65292678987012873342593706666666E-27, \
      -0.15337980061873346427835733333333E-27, \
      +0.36305884306364536682359466666666E-28, \
      -0.86560755713629122479172266666666E-29, \
      +0.20779909972536284571238399999999E-29, \
      -0.50211170221417221674325333333333E-30, \
      +0.12208360279441714184191999999999E-30, \
      -0.29860056267039913454250666666666E-31 ] )

  bth0cs = np.array ( [ \
      -0.24901780862128936717709793789967, \
      +0.48550299609623749241048615535485E-03, \
      -0.54511837345017204950656273563505E-05, \
      +0.13558673059405964054377445929903E-06, \
      -0.55691398902227626227583218414920E-08, \
      +0.32609031824994335304004205719468E-09, \
      -0.24918807862461341125237903877993E-10, \
      +0.23449377420882520554352413564891E-11, \
      -0.26096534444310387762177574766136E-12, \
      +0.33353140420097395105869955014923E-13, \
      -0.47890000440572684646750770557409E-14, \
      +0.75956178436192215972642568545248E-15, \
      -0.13131556016891440382773397487633E-15, \
      +0.24483618345240857495426820738355E-16, \
      -0.48805729810618777683256761918331E-17, \
      +0.10327285029786316149223756361204E-17, \
      -0.23057633815057217157004744527025E-18, \
      +0.54044443001892693993017108483765E-19, \
      -0.13240695194366572724155032882385E-19, \
      +0.33780795621371970203424792124722E-20, \
      -0.89457629157111779003026926292299E-21, \
      +0.24519906889219317090899908651405E-21, \
      -0.69388422876866318680139933157657E-22, \
      +0.20228278714890138392946303337791E-22, \
      -0.60628500002335483105794195371764E-23, \
      +0.18649748964037635381823788396270E-23, \
      -0.58783732384849894560245036530867E-24, \
      +0.18958591447999563485531179503513E-24, \
      -0.62481979372258858959291620728565E-25, \
      +0.21017901684551024686638633529074E-25, \
      -0.72084300935209253690813933992446E-26, \
      +0.25181363892474240867156405976746E-26, \
      -0.89518042258785778806143945953643E-27, \
      +0.32357237479762298533256235868587E-27, \
      -0.11883010519855353657047144113796E-27, \
      +0.44306286907358104820579231941731E-28, \
      -0.16761009648834829495792010135681E-28, \
      +0.64292946921207466972532393966088E-29, \
      -0.24992261166978652421207213682763E-29, \
      +0.98399794299521955672828260355318E-30, \
      -0.39220375242408016397989131626158E-30, \
      +0.15818107030056522138590618845692E-30, \
      -0.64525506144890715944344098365426E-31, \
      +0.26611111369199356137177018346367E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  nbm0 = r8_inits ( bm0cs, 37, eta )
  nbt02 = r8_inits ( bt02cs, 39, eta )
  nbm02 = r8_inits ( bm02cs, 40, eta )
  nbth0 = r8_inits ( bth0cs, 44, eta )
  xmax = 1.0 / r8_mach ( 4 )

  if ( x < 4.0 ):
    print ( '' )
    print ( 'r8_b0mp - Fatal error!' )
    print ( '  X < 4.' )
    raise Exception ( 'r8_b0mp - Fatal error!' )
  elif ( x <= 8.0 ):
    z = ( 128.0 / x / x - 5.0 ) / 3.0
    ampl = ( 0.75 + r8_csevl ( z, bm0cs, nbm0 ) ) / np.sqrt ( x )
    theta = x - 0.25 * np.pi + r8_csevl ( z, bt02cs, nbt02 ) / x
  else:
    z = 128.0 / x / x - 1.0
    ampl = ( 0.75 + r8_csevl ( z, bm02cs, nbm02) ) / np.sqrt ( x )
    theta = x - 0.25 * np.pi + r8_csevl ( z, bth0cs, nbth0 ) / x

  return ampl, theta

def r8_besj0 ( x ):

#*****************************************************************************80
#
## r8_besj0() evaluates the Bessel function J of order 0 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  bj0cs = np.array ( [ \
      +0.10025416196893913701073127264074, \
      -0.66522300776440513177678757831124, \
      +0.24898370349828131370460468726680, \
      -0.33252723170035769653884341503854E-01, \
      +0.23114179304694015462904924117729E-02, \
      -0.99112774199508092339048519336549E-04, \
      +0.28916708643998808884733903747078E-05, \
      -0.61210858663032635057818407481516E-07, \
      +0.98386507938567841324768748636415E-09, \
      -0.12423551597301765145515897006836E-10, \
      +0.12654336302559045797915827210363E-12, \
      -0.10619456495287244546914817512959E-14, \
      +0.74706210758024567437098915584000E-17, \
      -0.44697032274412780547627007999999E-19, \
      +0.23024281584337436200523093333333E-21, \
      -0.10319144794166698148522666666666E-23, \
      +0.40608178274873322700800000000000E-26, \
      -0.14143836005240913919999999999999E-28, \
      +0.43910905496698880000000000000000E-31 ] )

  ntj0 = r8_inits ( bj0cs, 19, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= xsml ):
    value = 1.0
  elif ( y <= 4.0 ):
    value = r8_csevl ( 0.125 * y * y - 1.0, bj0cs, ntj0 )
  else:
    ampl, theta = r8_b0mp ( y )
    value = ampl * np.cos ( theta )

  return value

def r8_besj0_test ( ):

#*****************************************************************************80
#
## r8_besj0_test() tests r8_besj0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_besj0_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besj0 evaluates the Bessel J0(x) function' )
  print ( '' )
  print ( '             X       BESJ0(X)  r8_besj0(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_j0_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besj0 ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besy0 ( x ):

#*****************************************************************************80
#
## r8_besy0() evaluates the Bessel function Y of order 0 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  alnhaf = -0.69314718055994530941723212145818
  twodpi = 0.636619772367581343075535053490057

  by0cs = np.array ( [ \
      -0.1127783939286557321793980546028E-01, \
      -0.1283452375604203460480884531838, \
      -0.1043788479979424936581762276618, \
      +0.2366274918396969540924159264613E-01, \
      -0.2090391647700486239196223950342E-02, \
      +0.1039754539390572520999246576381E-03, \
      -0.3369747162423972096718775345037E-05, \
      +0.7729384267670667158521367216371E-07, \
      -0.1324976772664259591443476068964E-08, \
      +0.1764823261540452792100389363158E-10, \
      -0.1881055071580196200602823012069E-12, \
      +0.1641865485366149502792237185749E-14, \
      -0.1195659438604606085745991006720E-16, \
      +0.7377296297440185842494112426666E-19, \
      -0.3906843476710437330740906666666E-21, \
      +0.1795503664436157949829120000000E-23, \
      -0.7229627125448010478933333333333E-26, \
      +0.2571727931635168597333333333333E-28, \
      -0.8141268814163694933333333333333E-31 ] )

  nty0 = r8_inits ( by0cs, 19, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_besy0 - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_besy0 - Fatal error!' )
  elif ( x <= xsml ):
    y = 0.0
    value = twodpi * ( alnhaf + np.log ( x ) ) * r8_besj0 ( x ) \
      + 0.375 + r8_csevl ( 0.125 * y - 1.0, by0cs, nty0 )
  elif ( x <= 4.0 ):
    y = x * x
    value = twodpi * ( alnhaf + np.log ( x ) ) * r8_besj0 ( x ) \
      + 0.375 + r8_csevl ( 0.125 * y - 1.0, by0cs, nty0 )
  else:
    ampl, theta = r8_b0mp ( x )
    value = ampl * np.sin ( theta )

  return value

def r8_besy0_test ( ):

#*****************************************************************************80
#
## r8_besy0_test() tests r8_besy0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
 
  print ( '' )
  print ( 'r8_besy0_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besy0 evaluates the Bessel Y0(X) function.' )
  print ( '' )
  print ( '             X       BESY0(X)  r8_besy0(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_y0_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besy0 ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_b1mp ( x ):

#*****************************************************************************80
#
## r8_b1mp() evaluates the modulus and phase for the Bessel J1 and Y1 functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real AMPL, THETA, the modulus and phase.
#
  import numpy as np

  bm12cs = np.array ( [ \
      +0.9807979156233050027272093546937E-01, \
      +0.1150961189504685306175483484602E-02, \
      -0.4312482164338205409889358097732E-05, \
      +0.5951839610088816307813029801832E-07, \
      -0.1704844019826909857400701586478E-08, \
      +0.7798265413611109508658173827401E-10, \
      -0.4958986126766415809491754951865E-11, \
      +0.4038432416421141516838202265144E-12, \
      -0.3993046163725175445765483846645E-13, \
      +0.4619886183118966494313342432775E-14, \
      -0.6089208019095383301345472619333E-15, \
      +0.8960930916433876482157048041249E-16, \
      -0.1449629423942023122916518918925E-16, \
      +0.2546463158537776056165149648068E-17, \
      -0.4809472874647836444259263718620E-18, \
      +0.9687684668292599049087275839124E-19, \
      -0.2067213372277966023245038117551E-19, \
      +0.4646651559150384731802767809590E-20, \
      -0.1094966128848334138241351328339E-20, \
      +0.2693892797288682860905707612785E-21, \
      -0.6894992910930374477818970026857E-22, \
      +0.1830268262752062909890668554740E-22, \
      -0.5025064246351916428156113553224E-23, \
      +0.1423545194454806039631693634194E-23, \
      -0.4152191203616450388068886769801E-24, \
      +0.1244609201503979325882330076547E-24, \
      -0.3827336370569304299431918661286E-25, \
      +0.1205591357815617535374723981835E-25, \
      -0.3884536246376488076431859361124E-26, \
      +0.1278689528720409721904895283461E-26, \
      -0.4295146689447946272061936915912E-27, \
      +0.1470689117829070886456802707983E-27, \
      -0.5128315665106073128180374017796E-28, \
      +0.1819509585471169385481437373286E-28, \
      -0.6563031314841980867618635050373E-29, \
      +0.2404898976919960653198914875834E-29, \
      -0.8945966744690612473234958242979E-30, \
      +0.3376085160657231026637148978240E-30, \
      -0.1291791454620656360913099916966E-30, \
      +0.5008634462958810520684951501254E-31 ] )

  bm1cs = np.array ( [ \
      +0.1069845452618063014969985308538, \
      +0.3274915039715964900729055143445E-02, \
      -0.2987783266831698592030445777938E-04, \
      +0.8331237177991974531393222669023E-06, \
      -0.4112665690302007304896381725498E-07, \
      +0.2855344228789215220719757663161E-08, \
      -0.2485408305415623878060026596055E-09, \
      +0.2543393338072582442742484397174E-10, \
      -0.2941045772822967523489750827909E-11, \
      +0.3743392025493903309265056153626E-12, \
      -0.5149118293821167218720548243527E-13, \
      +0.7552535949865143908034040764199E-14, \
      -0.1169409706828846444166290622464E-14, \
      +0.1896562449434791571721824605060E-15, \
      -0.3201955368693286420664775316394E-16, \
      +0.5599548399316204114484169905493E-17, \
      -0.1010215894730432443119390444544E-17, \
      +0.1873844985727562983302042719573E-18, \
      -0.3563537470328580219274301439999E-19, \
      +0.6931283819971238330422763519999E-20, \
      -0.1376059453406500152251408930133E-20, \
      +0.2783430784107080220599779327999E-21, \
      -0.5727595364320561689348669439999E-22, \
      +0.1197361445918892672535756799999E-22, \
      -0.2539928509891871976641440426666E-23, \
      +0.5461378289657295973069619199999E-24, \
      -0.1189211341773320288986289493333E-24, \
      +0.2620150977340081594957824000000E-25, \
      -0.5836810774255685901920938666666E-26, \
      +0.1313743500080595773423615999999E-26, \
      -0.2985814622510380355332778666666E-27, \
      +0.6848390471334604937625599999999E-28, \
      -0.1584401568222476721192960000000E-28, \
      +0.3695641006570938054301013333333E-29, \
      -0.8687115921144668243012266666666E-30, \
      +0.2057080846158763462929066666666E-30, \
      -0.4905225761116225518523733333333E-31 ] )

  bt12cs = np.array ( [ \
      +0.73823860128742974662620839792764, \
      -0.33361113174483906384470147681189E-02, \
      +0.61463454888046964698514899420186E-04, \
      -0.24024585161602374264977635469568E-05, \
      +0.14663555577509746153210591997204E-06, \
      -0.11841917305589180567005147504983E-07, \
      +0.11574198963919197052125466303055E-08, \
      -0.13001161129439187449366007794571E-09, \
      +0.16245391141361731937742166273667E-10, \
      -0.22089636821403188752155441770128E-11, \
      +0.32180304258553177090474358653778E-12, \
      -0.49653147932768480785552021135381E-13, \
      +0.80438900432847825985558882639317E-14, \
      -0.13589121310161291384694712682282E-14, \
      +0.23810504397147214869676529605973E-15, \
      -0.43081466363849106724471241420799E-16, \
      +0.80202544032771002434993512550400E-17, \
      -0.15316310642462311864230027468799E-17, \
      +0.29928606352715568924073040554666E-18, \
      -0.59709964658085443393815636650666E-19, \
      +0.12140289669415185024160852650666E-19, \
      -0.25115114696612948901006977706666E-20, \
      +0.52790567170328744850738380799999E-21, \
      -0.11260509227550498324361161386666E-21, \
      +0.24348277359576326659663462400000E-22, \
      -0.53317261236931800130038442666666E-23, \
      +0.11813615059707121039205990399999E-23, \
      -0.26465368283353523514856789333333E-24, \
      +0.59903394041361503945577813333333E-25, \
      -0.13690854630829503109136383999999E-25, \
      +0.31576790154380228326413653333333E-26, \
      -0.73457915082084356491400533333333E-27, \
      +0.17228081480722747930705920000000E-27, \
      -0.40716907961286507941068800000000E-28, \
      +0.96934745136779622700373333333333E-29, \
      -0.23237636337765716765354666666666E-29, \
      +0.56074510673522029406890666666666E-30, \
      -0.13616465391539005860522666666666E-30, \
      +0.33263109233894654388906666666666E-31 ] )

  bth1cs = np.array ( [ \
      +0.74749957203587276055443483969695, \
      -0.12400777144651711252545777541384E-02, \
      +0.99252442404424527376641497689592E-05, \
      -0.20303690737159711052419375375608E-06, \
      +0.75359617705690885712184017583629E-08, \
      -0.41661612715343550107630023856228E-09, \
      +0.30701618070834890481245102091216E-10, \
      -0.28178499637605213992324008883924E-11, \
      +0.30790696739040295476028146821647E-12, \
      -0.38803300262803434112787347554781E-13, \
      +0.55096039608630904934561726208562E-14, \
      -0.86590060768383779940103398953994E-15, \
      +0.14856049141536749003423689060683E-15, \
      -0.27519529815904085805371212125009E-16, \
      +0.54550796090481089625036223640923E-17, \
      -0.11486534501983642749543631027177E-17, \
      +0.25535213377973900223199052533522E-18, \
      -0.59621490197413450395768287907849E-19, \
      +0.14556622902372718620288302005833E-19, \
      -0.37022185422450538201579776019593E-20, \
      +0.97763074125345357664168434517924E-21, \
      -0.26726821639668488468723775393052E-21, \
      +0.75453300384983271794038190655764E-22, \
      -0.21947899919802744897892383371647E-22, \
      +0.65648394623955262178906999817493E-23, \
      -0.20155604298370207570784076869519E-23, \
      +0.63417768556776143492144667185670E-24, \
      -0.20419277885337895634813769955591E-24, \
      +0.67191464220720567486658980018551E-25, \
      -0.22569079110207573595709003687336E-25, \
      +0.77297719892989706370926959871929E-26, \
      -0.26967444512294640913211424080920E-26, \
      +0.95749344518502698072295521933627E-27, \
      -0.34569168448890113000175680827627E-27, \
      +0.12681234817398436504211986238374E-27, \
      -0.47232536630722639860464993713445E-28, \
      +0.17850008478186376177858619796417E-28, \
      -0.68404361004510395406215223566746E-29, \
      +0.26566028671720419358293422672212E-29, \
      -0.10450402527914452917714161484670E-29, \
      +0.41618290825377144306861917197064E-30, \
      -0.16771639203643714856501347882887E-30, \
      +0.68361997776664389173535928028528E-31, \
      -0.28172247861233641166739574622810E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  nbm1 = r8_inits ( bm1cs, 37, eta )
  nbt12 = r8_inits ( bt12cs, 39, eta )
  nbm12 = r8_inits ( bm12cs, 40, eta )
  nbth1 = r8_inits ( bth1cs, 44, eta )
  xmax = 1.0 / r8_mach ( 4 )

  if ( x < 4.0 ):
    print ( '' )
    print ( 'r8_b1mp - Fatal error!' )
    print ( '  X < 4.' )
    raise Exception ( 'r8_b1mp - Fatal error!' )
  elif ( x <= 8.0 ):
    z = ( 128.0 / x / x - 5.0 ) / 3.0
    ampl = ( 0.75 + r8_csevl ( z, bm1cs, nbm1 ) ) / np.sqrt ( x )
    theta = x - 0.75 * np.pi + r8_csevl ( z, bt12cs, nbt12 ) / x
  else:
    z = 128.0 / x / x - 1.0
    ampl = ( 0.75 + r8_csevl ( z, bm12cs, nbm12 ) ) / np.sqrt ( x )
    theta = x - 0.75 * np.pi + r8_csevl ( z, bth1cs, nbth1 ) / x

  return ampl, theta

def r8_besj1 ( x ):

#*****************************************************************************80
#
## r8_besj1() evaluates the Bessel function J of order 1 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  bj1cs = np.array ( [ \
      -0.117261415133327865606240574524003, \
      -0.253615218307906395623030884554698, \
      +0.501270809844695685053656363203743E-01, \
      -0.463151480962508191842619728789772E-02, \
      +0.247996229415914024539124064592364E-03, \
      -0.867894868627882584521246435176416E-05, \
      +0.214293917143793691502766250991292E-06, \
      -0.393609307918317979229322764073061E-08, \
      +0.559118231794688004018248059864032E-10, \
      -0.632761640466139302477695274014880E-12, \
      +0.584099161085724700326945563268266E-14, \
      -0.448253381870125819039135059199999E-16, \
      +0.290538449262502466306018688000000E-18, \
      -0.161173219784144165412118186666666E-20, \
      +0.773947881939274637298346666666666E-23, \
      -0.324869378211199841143466666666666E-25, \
      +0.120223767722741022720000000000000E-27, \
      -0.395201221265134933333333333333333E-30, \
      +0.116167808226645333333333333333333E-32 ] )

  ntj1 = r8_inits ( bj1cs, 19, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )
  xmin = 2.0 * r8_mach ( 1 )

  y = abs ( x )

  if ( y <= xmin ):
    value = 0.0
  elif ( y <= xsml ):
    value = 0.5 * x
  elif ( y <= 4.0 ):
    value = x * ( 0.25 + r8_csevl ( 0.125 * y * y - 1.0, bj1cs, ntj1 ) )
  else:
    ampl, theta = r8_b1mp ( y )
    if ( x < 0.0 ):
      value = - ampl * np.cos ( theta )
    else:
      value = + ampl * np.cos ( theta )

  return value

def r8_besj1_test ( ):

#*****************************************************************************80
#
## r8_besj1_test() tests r8_besj1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_besj1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besj1 evaluates the Bessel J1(x) function' )
  print ( '' )
  print ( '             X       BESJ1(X)  r8_besj1(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_j1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besj1 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besy1 ( x ):

#*****************************************************************************80
#
## r8_besy1() evaluates the Bessel function Y of order 1 of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  twodpi = 0.636619772367581343075535053490057

  by1cs = np.array ( [ \
      +0.320804710061190862932352018628015E-01, \
      +0.126270789743350044953431725999727E+01, \
      +0.649996189992317500097490637314144E-02, \
      -0.893616452886050411653144160009712E-01, \
      +0.132508812217570954512375510370043E-01, \
      -0.897905911964835237753039508298105E-03, \
      +0.364736148795830678242287368165349E-04, \
      -0.100137438166600055549075523845295E-05, \
      +0.199453965739017397031159372421243E-07, \
      -0.302306560180338167284799332520743E-09, \
      +0.360987815694781196116252914242474E-11, \
      -0.348748829728758242414552947409066E-13, \
      +0.278387897155917665813507698517333E-15, \
      -0.186787096861948768766825352533333E-17, \
      +0.106853153391168259757070336000000E-19, \
      -0.527472195668448228943872000000000E-22, \
      +0.227019940315566414370133333333333E-24, \
      -0.859539035394523108693333333333333E-27, \
      +0.288540437983379456000000000000000E-29, \
      -0.864754113893717333333333333333333E-32 ] )

  nty1 = r8_inits ( by1cs, 20, 0.1 * r8_mach ( 3 ) )
  xmin = 1.571 * np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) ) + 0.01 )
  xsml = np.sqrt ( 4.0 * r8_mach ( 3 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_besy1 - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_besy1 - Fatal error!' )
  elif ( x <= xmin ):
    y = 0.0
    value = twodpi * np.log ( 0.5 * x ) * r8_besj1 ( x ) \
      + ( 0.5 + r8_csevl ( 0.125 * y - 1.0, by1cs, nty1 ) ) / x
  elif ( x <= 4.0 ):
    y = x * x
    value = twodpi * np.log ( 0.5 * x ) * r8_besj1 ( x ) \
      + ( 0.5 + r8_csevl ( 0.125 * y - 1.0, by1cs, nty1 ) ) / x
  else:
    ampl, theta = r8_b1mp ( x )
    value = ampl * np.sin ( theta )

  return value

def r8_besy1_test ( ):

#*****************************************************************************80
#
## r8_besy1_test() tests r8_besy1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_besy1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besy1 evaluates the Bessel Y1(x) function' )
  print ( '' )
  print ( '             X       BESY1(X)  r8_besy1(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = bessel_y1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besy1 ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besk ( nu, x ):

#*****************************************************************************80
#
## r8_besk() evaluates the Bessel function K of order NU of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real NU, the order.
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the Bessel function K of order NU at X.
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
## r8_besk_test() tests r8_besk().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_besk_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_besk evaluates Bessel K functtions K(NU,X).' )
  print ( '' )
  print ( '              NU             X       BESK(X)  r8_besk(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx1 = bessel_kx_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_besk ( nu, x )

    print ( '  %14.4g  %14.4f  %14.6g  %14.6g  %14.6g' \
      % ( nu, x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_besks ( xnu, x, nin ):

#*****************************************************************************80
#
## r8_besks() evaluates a sequence of K Bessel functions at X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    Input, real XNU, the fractional order.
#    |XNU| < 1.
#
#    real X, the argument.
#
#    integer NIN, indicates the number of terms to compute.
#
#  Output:
#
#    real BK(abs(NIN)), the K Bessel functions.
#
  import numpy as np

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
## r8_beskes() evaluates a sequence of exponentially scaled K Bessel functions at X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real XNU, ?
#    |XNU| < 1.
#
#    real X, the argument.
#
#    integer NIN, indicates the number of terms to compute.
#
#  Output:
#
#    real BKE(abs(NIN)), the exponentially scaled
#    K Bessel functions.
#
  import numpy as np

  v = abs ( xnu )
  n = int ( abs ( nin ) )

  if ( 1.0 <= v ):
    print ( '' )
    print ( 'r8_beskes - Fatal error!' )
    print ( '  |XNU| must be less than 1.' )
    raise Exception ( 'r8_beskes - Fatal error!' )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_beskes - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_beskes - Fatal error!' )

  if ( n == 0 ):
    print ( '' )
    print ( 'r8_beskes - Fatal error!' )
    print ( '  N = 0.' )
    raise Exception ( 'r8_beskes - Fatal error!' )

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
## r8_knus() computes a sequence of K Bessel functions.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real XNU, the order parameter.
#
#    real X, the argument.
#
#  Output:
#
#    real BKNU, BKNU1, the two K Bessel functions.
#
#    integer ISWTCH, ?
#
  import numpy as np

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
    print ( 'r8_knus - Fatal error!' )
    print ( '  XNU < 0 or. 1 <= XNU.' )
    raise Exception ( 'r8_knus - Fatal error!' )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_knus - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_knus - Fatal error!' )

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
        print ( 'r8_knus - Fatal error!' )
        print ( '  Small X causing overflow.' )
        raise Exception ( 'r8_knus - Fatal error!' )

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

def r8_betai ( x, pin, qin ):

#*****************************************************************************80
#
## r8_betai() evaluates the incomplete beta ratio of R8 arguments.
#
#  Discussion:
#
#    The incomplete Beta function ratio is the probability that a
#    random variable from a beta distribution having parameters
#    P and Q will be less than or equal to X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
#
#  Reference:
#
#    Nancy Bosten, EL Battiste,
#    Remark on Algorithm 179:
#    Incomplete Beta Ratio,
#    Communications of the ACM,
#    Volume 17, Number 3, March 1974, pages 156-157.
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
#  Input:
#
#    real X, the upper limit of integration.
#    0.0 <= X <= 1.0.
#
#    real PIN, the first distribution parameter.
#    0.0 < PIN.
#
#    real QIN, the second distribution parameter.
#    0.0 < QIN.
#
#  Output:
#
#    real VALUE, the incomplete beta function ratio.
#
  import numpy as np

  eps = r8_mach ( 3 )
  alneps = np.log ( eps )
  sml = r8_mach ( 1 )
  alnsml = np.log ( sml )

  if ( x < 0.0 or 1.0 < x ):
    print ( '' )
    print ( 'r8_betai - Fatal error!' )
    print ( '  0 <= X <= 1 is required.' )
    raise Exception ( 'r8_betai - Fatal error!' )

  if ( pin <= 0.0 or qin <= 0.0 ):
    print ( '' )
    print ( 'r8_betai - Fatal error!' )
    print ( '  P or Q <= 0.0.' )
    raise Exception ( 'r8_betai - Fatal error!' )

  y = x
  p = pin
  q = qin

  if ( p < q or 0.8 <= x ):

    if ( 0.2 <= x ):
      y = 1.0 - y
      p = qin
      q = pin

  if ( ( p + q ) * y / ( p + 1.0 ) < eps ):

    value = 0.0

    xb = p * np.log ( max ( y, sml ) ) - np.log ( p ) - r8_lbeta ( p, q )

    if ( alnsml < xb and y != 0.0 ):
      value = np.exp ( xb )

    if ( y != x or p != pin ):
      value = 1.0 - value

    return value

  ps = q - r8_aint ( q )
  if ( ps == 0.0 ):
    ps = 1.0

  xb = p * np.log ( y ) - r8_lbeta ( ps, p ) - np.log ( p )

  if ( xb < alnsml ):

    value = 0.0

  else:

    value = np.exp ( xb )
    term = value * p

    if ( ps != 1.0 ):

      n = int ( r8_aint ( max ( alneps / np.log ( y ), 4.0 ) ) )
      for i in range ( 1, n + 1 ):
        term = term * ( i - ps ) * y / float ( i )
        value = value + term / ( p + i )
#
#  Now evaluate the finite sum.
#
  if ( 1.0 < q ):

    xb = p * np.log ( y ) + q * np.log ( 1.0 - y ) - r8_lbeta ( p, q ) - np.log ( q )
    ib = r8_aint ( max ( xb / alnsml, 0.0 ) )
    term = np.exp ( xb - ib * alnsml )
    c = 1.0 / ( 1.0 - y )
    p1 = q * c / ( p + q - 1.0 )

    finsum = 0.0
    n = int ( r8_aint ( q ) )
    if ( q == n ):
      n = n - 1

    for i in range ( 1, n + 1 ):

      if ( p1 <= 1.0 and term / eps <= finsum ):
        break

      term = ( q - i + 1.0 ) * c * term / ( p + q - i )

      if ( 1.0 < term ):
        ib = ib - 1
        term = term * sml

      if ( ib == 0 ):
        finsum = finsum + term

    value = value + finsum

  if ( y != x or p != pin ):
    value = 1.0 - value

  if ( value < 0.0 ):
    value =  0.0

  if ( 1.0 < value ):
    value = 1.0

  return value

def r8_betai_test ( ):

#*****************************************************************************80
#
## r8_betai_test() tests r8_betai().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_betai_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_betai evaluates the incomplete Beta function.' )
  print ( '' )
  print ( '             X               A               B     BETAI(A,B)  r8_betai(A,B)  Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx1 = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_betai ( x, a, b )

    print ( '  %14.4f  %14.4f  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( x, a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_beta ( a, b ):

#*****************************************************************************80
#
## r8_beta() evaluates the beta function of R8 arguments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, B, the arguments.
#
#  Output:
#
#    real VALUE, the beta function of A and B.
#
  import numpy as np

  xmin, xmax = r8_gaml ( )
  alnsml = np.log ( r8_mach ( 1 ) )

  if ( a <= 0.0 or b <= 0.0 ):
    print ( '' )
    print ( 'r8_beta - Fatal error!' )
    print ( '  A and B must be greater than 0.' )
    raise Exception ( 'r8_beta - Fatal error!' )

  if ( a + b < xmax ):
    value = r8_gamma ( a ) * r8_gamma ( b ) / r8_gamma ( a + b )
  else:
    value = r8_lbeta ( a, b )
    value = np.exp ( value )

  return value

def r8_beta_test ( ):

#*****************************************************************************80
#
## r8_beta_test() tests r8_beta().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
 
  print ( '' )
  print ( 'r8_beta_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_beta evaluates the Beta function.' )
  print ( '' )
  print ( '             A               B      BETA(A,B)  r8_beta(A,B)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx1 = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_beta ( a, b )

    print ( '  %14.6g  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_binom ( n, m ):

#*****************************************************************************80
#
## r8_binom() evaluates the binomial coefficient using R8 arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    integer N, M, the arguments.
#
#  Output:
#
#    real VALUE, the binomial coefficient.
#
  import numpy as np

  sq2pil = 0.91893853320467274178032973640562

  bilnmx = np.log ( r8_mach ( 2 ) ) - 0.0001
  fintmx = 0.9 / r8_mach ( 3 )

  if ( n < 0 ):
    value = 0.0
    return value

  if ( m < 0 ):
    value = 0.0
    return value

  if ( n < m ):
    value = 0.0
    return value

  k = min ( m, n - m )

  if ( k <= 20 and k * np.log ( max ( n, 1 ) ) <= bilnmx ):

    value = 1.0

    for i in range ( 1, k + 1 ):
      value = value * float ( n - i + 1 ) / float ( i )

  else:

    if ( k < 9 ):
      print ( '' )
      print ( 'r8_binom - Fatal error!' )
      print ( '  Result overflows.' )
      print ( '  N or M is too big.' )
      raise Exception ( 'r8_binom - Fatal error!' )

    xn = float ( n + 1 )
    xk = float ( k + 1 )
    xnk = float ( n - k + 1 )

    corr = r8_lgmc ( xn ) - r8_lgmc ( xk ) - r8_lgmc ( xnk )

    value = xk * np.log ( xnk / xk ) \
      - xn * r8_lnrel ( - ( xk - 1.0 ) / xn ) \
      - 0.5 * np.log ( xn * xnk / xk ) + 1.0 - sq2pil + corr

    if ( bilnmx < value ):
      print ( '' )
      print ( 'r8_binom - Fatal error!' )
      print ( '  Result overflows.' )
      print ( '  N or M is too big.' )
      raise Exception ( 'r8_binom - Fatal error!' )

    value = np.exp ( value )

  if ( value < fintmx ):
    value = r8_aint ( value + 0.5 )

  return value

def r8_binom_test ( ):

#*****************************************************************************80
#
## r8_binom_test() tests r8_binom().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_binom_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_binom evaluates the binomial coefficient.' )
  print ( '' )
  print ( '             A               B     BINOM(A,B)  r8_binom(A,B)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx1 = binomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_binom ( a, b )

    print ( '  %14d  %14d  %14d  %14d  %14.6g' \
      % ( a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_cbrt ( x ):

#*****************************************************************************80
#
## r8_cbrt() computes the cube root of an R8.
#
#  Discussion:
#
#    The approximation is a generalized Chebyshev series converted
#    to polynomial form.  The approximation is nearly best in the
#    sense of relative error with 4.085 digits accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  cbrt2 = np.array ( [ \
      0.62996052494743658238360530363911, \
      0.79370052598409973737585281963615, \
      1.0, \
      1.25992104989487316476721060727823, \
      1.58740105196819947475170563927231 ] )

  niter = int ( r8_aint ( 1.443 * np.log ( - 0.106 \
      * np.log ( 0.1 * r8_mach ( 3 ) ) ) + 1.0 ) )

  value = 0.0

  if ( x != 0.0 ):

    y, n = r8_upak ( abs ( x ) )
    ixpnt = ( n // 3 )
    irem = n - 3 * ixpnt + 3

    value = 0.439581 + y * ( \
            0.928549 + y * ( \
          - 0.512653 + y * \
            0.144586 ) )

    for iter in range ( 0, niter ):
      vsq = value * value
      value = value + ( y - value * vsq ) / ( 3.0 * vsq )

    if ( x < 0.0 ):
      value = - abs ( value )
    else:
      value = + abs ( value )

    value = r8_pak ( cbrt2[irem-1] * value, ixpnt )

  return value

def r8_cbrt_test ( ):

#*****************************************************************************80
#
## r8_cbrt_test() tests r8_cbrt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_cbrt_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cbrt evaluates the cube root function.' )
  print ( '' )
  print ( '             X        CBRT(X)  r8_cbrt(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cbrt_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cbrt ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_chi ( x ):

#*****************************************************************************80
#
## r8_chi() evaluates the hyperbolic cosine integral of an R8 argument.
#
#  Discussion:
#
#    The hyperbolic cosine integral is defined by
#
#      CHI(X) = gamma + log ( x )
#        + integral ( 0 <= T < X ) ( cosh ( T ) - 1 ) / T  dT
#
#    where gamma is Euler's constant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  value = 0.5 * ( r8_ei ( x ) - r8_e1 ( x ) )

  return value

def r8_chi_test ( ):

#*****************************************************************************80
#
## r8_chi_test() tests r8_chi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_chi_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_chi evaluates the hyperbolic cosine integral.' )
  print ( '' )
  print ( '             X          CHI(X)  r8_chi(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = chi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_chi ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_chu ( a, b, x ):

#*****************************************************************************80
#
## r8_chu() evaluates the confluent hypergeometric function of R8 arguments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, B, the parameters.
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  eps = r8_mach ( 3 )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'r8_chu - Fatal error!' )
    print ( '  X < 0.' )
    raise Exception ( 'r8_chu - Fatal error!' )

  if ( x == 0.0 ):
    if ( 1.0 <= b ):
      print ( '' )
      print ( 'r8_chu - Fatal error!' )
      print ( '  X = 0 and 1 <= B.' )
      raise Exception ( 'r8_chu - Fatal error!' )

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
    print ( 'r8_chu - Fatal error!' )
    print ( '  No convergence in 1000 terms.' )
    raise Exception ( 'r8_chu - Fatal error!' )
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
  print ( 'r8_chu - Fatal error!' )
  print ( '  No convergence in 1000 terms.' )
  raise Exception ( 'r8_chu - Fatal error!' )

def r8_chu_test ( ):

#*****************************************************************************80
#
## r8_chu_test() tests r8_chu().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_chu_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_chu evaluates the hypergeometric U function.' )
  print ( '' )
  print ( '             A               B               X     CHU(A,B,X)  r8_chu(A,B,X)  Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx1 = hypergeometric_u_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_chu ( a, b, x )

    print ( '  %14.4f  %14.4f  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, b, x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_chu_scaled ( a, b, z ):

#*****************************************************************************80
#
## r8_chu_scaled(): scaled confluent hypergeometric function of R8 arguments.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, B, the parameters.
#
#    real Z, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

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
  print ( 'r8_chu_scaled - Fatal error!' )
  print ( '  No convergence after 300 terms.' )
  raise Exception ( 'r8_chu_scaled - Fatal error!' )

def r8_exprel ( x ):

#*****************************************************************************80
#
## r8_exprel() evaluates the exponential relative error term of an R8 argument.
#
#  Discussion:
#
#    The relative error term is ( exp ( x ) - 1 ) / x.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Inpur:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

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
## r8_poch1() evaluates a quantity related to Pochhammer's symbol.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, the parameter.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

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
      print ( 'r8_poch1 - Fatal error!' )
      print ( ' 20 < NTERMS.' )
      raise Exception ( 'r8_poch1 - Fatal error!' )

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

def r8_cinh ( x ):

#*****************************************************************************80
#
## r8_cinh(): alternate hyperbolic cosine integral Cinh of an R8 argument.
#
#  Discussion:
#
#    Cinh ( x ) = Integral ( 0 <= t <= x ) ( cosh ( t ) - 1 ) dt / t
#
#    The original text of this program had a mistake:
#      y = x * x / 9.0 - 1.0
#    has been corrected to
#      y = x * x / 4.5 - 1.0
#    JVB, 27 March 2010
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  eul = 0.57721566490153286060651209008240

  cinhcs = np.array ( [ \
      0.1093291636520734431407425199795917, \
      0.0573928847550379676445323429825108, \
      0.0028095756978830353416404208940774, \
      0.0000828780840721356655731765069792, \
      0.0000016278596173914185577726018815, \
      0.0000000227809519255856619859083591, \
      0.0000000002384484842463059257284002, \
      0.0000000000019360829780781957471028, \
      0.0000000000000125453698328172559683, \
      0.0000000000000000663637449497262300, \
      0.0000000000000000002919639263594744, \
      0.0000000000000000000010849123956107, \
      0.0000000000000000000000034499080805, \
      0.0000000000000000000000000094936664, \
      0.0000000000000000000000000000228291, \
      0.0000000000000000000000000000000484 ] )

  ncinh = r8_inits ( cinhcs, 16, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( r8_mach ( 3 ) )
  xmin = 2.0 * np.sqrt ( r8_mach ( 1 ) )

  absx = abs ( x )

  if ( x == 0.0 ):
    value = 0.0
  elif ( absx <= xmin ):
    value = 0.0
  elif ( x <= xsml ):
    y = - 1.0
    value = x * x * ( 0.25 + r8_csevl ( y, cinhcs, ncinh ) )
  elif ( x <= 3.0 ):
    y = x * x / 4.5 - 1.0
    value = x * x * ( 0.25 + r8_csevl ( y, cinhcs, ncinh ) )
  else:
    value = r8_chi ( absx ) - eul - np.log ( absx )

  return value

def r8_cinh_test ( ):

#*****************************************************************************80
#
## r8_cinh_test() tests r8_cinh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_cinh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cinh evaluates the alternate hyperbolic cosine integral.' )
  print ( '' )
  print ( '             X         CINH(X)  r8_cinh(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cinh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cinh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_ci ( x ):

#*****************************************************************************80
#
## r8_ci() evaluates the cosine integral Ci of an R8 argument.
#
#  Discussion:
#
#    The cosine integral is defined by
#
#      CI(X) = - integral ( X <= T < Infinity ) ( cos ( T ) ) / T  dT
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  cics = np.array ( [ \
      -0.34004281856055363156281076633129873, \
      -1.03302166401177456807159271040163751, \
       0.19388222659917082876715874606081709, \
      -0.01918260436019865893946346270175301, \
       0.00110789252584784967184098099266118, \
      -0.00004157234558247208803840231814601, \
       0.00000109278524300228715295578966285, \
      -0.00000002123285954183465219601280329, \
       0.00000000031733482164348544865129873, \
      -0.00000000000376141547987683699381798, \
       0.00000000000003622653488483964336956, \
      -0.00000000000000028911528493651852433, \
       0.00000000000000000194327860676494420, \
      -0.00000000000000000001115183182650184, \
       0.00000000000000000000005527858887706, \
      -0.00000000000000000000000023907013943, \
       0.00000000000000000000000000091001612, \
      -0.00000000000000000000000000000307233, \
       0.00000000000000000000000000000000926 ] )

  nci = r8_inits ( cics, 19, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( r8_mach ( 3 ) )

  if ( x <= 0.0 ):

    print ( '' )
    print ( 'r8_ci - Fatal error!' )
    print ( '  X <= 0.0.' )
    raise Exception ( 'r8_ci - Fatal error!' )

  elif ( x <= xsml ):
    y = - 1.0
    value = np.log ( x ) - 0.5 + r8_csevl ( y, cics, nci )
  elif ( x <= 4.0 ):
    y = ( x * x - 8.0 ) * 0.125
    value = np.log ( x ) - 0.5 + r8_csevl ( y, cics, nci )
  else:
    f, g = r8_sifg ( x )
    sinx = np.sin ( x )
    value = f * sinx - g * np.cos ( x )

  return value

def r8_ci_test ( ):

#*****************************************************************************80
#
## r8_ci_test() tests r8_ci().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_ci_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_ci evaluates the cosine integral.' )
  print ( '' )
  print ( '             X           CI(X)  r8_ci(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = ci_values ( n_data ) 

    if ( n_data == 0 ):
      break

    fx2 = r8_ci ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_cin ( x ):

#*****************************************************************************80
#
## r8_cin() evaluates the alternate cosine integral Cin of an R8 argument.
#
#  Discussion:
#
#    CIN(X) = gamma + log(X)
#      + integral ( 0 <= T <= X ) ( cos ( T ) - 1 ) / T  dT
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the cosine integral Cin evaluated at X.
#
  import numpy as np

  eul = 0.57721566490153286060651209008240

  cincs = np.array ( [ \
      0.37074501750909688741654801228564992, \
     -0.05893574896364446831956864397363697, \
      0.00538189642113569124048745326203340, \
     -0.00029860052841962135319594906563410, \
      0.00001095572575321620077031054467306, \
     -0.00000028405454877346630491727187731, \
      0.00000000546973994875384912457861806, \
     -0.00000000008124187461318157083277452, \
      0.00000000000095868593117706609013181, \
     -0.00000000000000920266004392351031377, \
      0.00000000000000007325887999017895024, \
     -0.00000000000000000049143726675842909, \
      0.00000000000000000000281577746753902, \
     -0.00000000000000000000001393986788501, \
      0.00000000000000000000000006022485646, \
     -0.00000000000000000000000000022904717, \
      0.00000000000000000000000000000077273, \
     -0.00000000000000000000000000000000233 ] )

  ncin = r8_inits ( cincs, 18, 0.1 * r8_mach ( 3 ) )
  xmin = np.sqrt ( r8_mach ( 1 ) )

  absx = abs ( x )

  if ( absx <= xmin ):
    value = 0.0
  elif ( absx <= 4.0 ):
    value = r8_csevl ( ( x * x - 8.0 ) * 0.125, cincs, ncin ) * x * x
  else:
    f, g = r8_sifg ( absx )
    sinx = np.sin ( absx )
    value = - f * sinx + g * np.cos ( absx ) + np.log ( absx ) + eul

  return value

def r8_cin_test ( ):

#*****************************************************************************80
#
## r8_cin_test() tests r8_cin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_cin_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cin evaluates the alternate hyperbolic cosine integral.' )
  print ( '' )
  print ( '             X          CIN(X)  r8_cin(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cin_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cin ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_si ( x ):

#*****************************************************************************80
#
## r8_si() evaluates the sine integral Si of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sics = np.array ( [ \
      -0.1315646598184841928904275173000457, \
      -0.2776578526973601892048287660157299, \
       0.0354414054866659179749135464710086, \
      -0.0025631631447933977658752788361530, \
       0.0001162365390497009281264921482985, \
      -0.0000035904327241606042670004347148, \
       0.0000000802342123705710162308652976, \
      -0.0000000013562997692540250649931846, \
       0.0000000000179440721599736775567759, \
      -0.0000000000001908387343087145490737, \
       0.0000000000000016669989586824330853, \
      -0.0000000000000000121730988368503042, \
       0.0000000000000000000754181866993865, \
      -0.0000000000000000000004014178842446, \
       0.0000000000000000000000018553690716, \
      -0.0000000000000000000000000075166966, \
       0.0000000000000000000000000000269113, \
      -0.0000000000000000000000000000000858 ] )

  nsi = r8_inits ( sics, 18, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( r8_mach ( 3 ) )

  absx = abs ( x )

  if ( absx < xsml ):
    value = x
  elif ( absx <= 4.0 ):
    value = x * ( 0.75 + r8_csevl ( ( x * x - 8.0 ) * 0.125, sics, nsi ) )
  else:
    f, g = r8_sifg ( absx )
    cosx = np.cos ( absx )
    value = 0.5 * np.pi - f * cosx - g * np.sin ( x )
    if ( x < 0.0 ):
      value = - value

  return value

def r8_si_test ( ):

#*****************************************************************************80
#
## r8_si_test() tests r8_si().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_si_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_si evaluates the sine integral.' )
  print ( '' )
  print ( '             X           SI(X)  r8_si(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = si_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_si ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_sifg ( x ):

#*****************************************************************************80
#
## r8_sifg() is a utility routine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real F, G.
#
  import numpy as np

  f1cs = np.array ( [ \
      -0.1191081969051363610348201965828918, \
      -0.0247823144996236247590074150823133, \
       0.0011910281453357821268120363054457, \
      -0.0000927027714388561748308600360706, \
       0.0000093373141568270996868204582766, \
      -0.0000011058287820557143938979426306, \
       0.0000001464772071460162169336550799, \
      -0.0000000210694496287689532601227548, \
       0.0000000032293492366848236382857374, \
      -0.0000000005206529617529375828014986, \
       0.0000000000874878884570278750268316, \
      -0.0000000000152176187056123668294574, \
       0.0000000000027257192405419573900583, \
      -0.0000000000005007053075968556290255, \
       0.0000000000000940240902726068511779, \
      -0.0000000000000180014444791803678336, \
       0.0000000000000035062621432741785826, \
      -0.0000000000000006935282926769149709, \
       0.0000000000000001390925136454216568, \
      -0.0000000000000000282486885074170585, \
       0.0000000000000000058031305693579081, \
      -0.0000000000000000012046901573375820, \
       0.0000000000000000002525052443655940, \
      -0.0000000000000000000533980268805594, \
       0.0000000000000000000113855786274122, \
      -0.0000000000000000000024462861505259, \
       0.0000000000000000000005293659320439, \
      -0.0000000000000000000001153184940277, \
       0.0000000000000000000000252786568318, \
      -0.0000000000000000000000055738645378, \
       0.0000000000000000000000012358245621, \
      -0.0000000000000000000000002754350842, \
       0.0000000000000000000000000616906808, \
      -0.0000000000000000000000000138817443, \
       0.0000000000000000000000000031375329, \
      -0.0000000000000000000000000007121249, \
       0.0000000000000000000000000001622778, \
      -0.0000000000000000000000000000371206, \
       0.0000000000000000000000000000085221, \
      -0.0000000000000000000000000000019633, \
       0.0000000000000000000000000000004538, \
      -0.0000000000000000000000000000001052, \
       0.0000000000000000000000000000000245 ] )

  f2cs = np.array ( [ \
      -0.03484092538970132330836049733745577, \
      -0.01668422056779596873246786312278676, \
       0.00067529012412377385045207859239727, \
      -0.00005350666225447013628785577557429, \
       0.00000626934217790075267050759431626, \
      -0.00000095266388019916680677790414293, \
       0.00000017456292242509880425504427666, \
      -0.00000003687954030653093307097646628, \
       0.00000000872026777051395264075816938, \
      -0.00000000226019703919738748530423167, \
       0.00000000063246249765250612520444877, \
      -0.00000000018889118884717869240911480, \
       0.00000000005967746729997813372620472, \
      -0.00000000001980443117372239011196007, \
       0.00000000000686413954772103383713264, \
      -0.00000000000247310193070199106074890, \
       0.00000000000092263594549941404196042, \
      -0.00000000000035523634999261784497297, \
       0.00000000000014076049625351591461820, \
      -0.00000000000005726228499747652794311, \
       0.00000000000002386537545413171810106, \
      -0.00000000000001017141890764597142232, \
       0.00000000000000442594531078364424968, \
      -0.00000000000000196344933049189761979, \
       0.00000000000000088688748314810461024, \
      -0.00000000000000040743345027311546948, \
       0.00000000000000019016837215675339859, \
      -0.00000000000000009009707297478042442, \
       0.00000000000000004329211274095668667, \
      -0.00000000000000002108144465322479526, \
       0.00000000000000001039637907026452274, \
      -0.00000000000000000518891007948931936, \
       0.00000000000000000261955324869899371, \
      -0.00000000000000000133690399951301570, \
       0.00000000000000000068941057702931664, \
      -0.00000000000000000035905362610437250, \
       0.00000000000000000018878077255791706, \
      -0.00000000000000000010016125265594380, \
       0.00000000000000000005360725691578228, \
      -0.00000000000000000002893198974944827, \
       0.00000000000000000001574065100202625, \
      -0.00000000000000000000863027106431206, \
       0.00000000000000000000476715602862288, \
      -0.00000000000000000000265222739998504, \
       0.00000000000000000000148582865063866, \
      -0.00000000000000000000083797235923135, \
       0.00000000000000000000047565916422711, \
      -0.00000000000000000000027169073353112, \
       0.00000000000000000000015612738881686, \
      -0.00000000000000000000009024555078347, \
       0.00000000000000000000005246097049119, \
      -0.00000000000000000000003066450818697, \
       0.00000000000000000000001801996250957, \
      -0.00000000000000000000001064443050752, \
       0.00000000000000000000000631942158881, \
      -0.00000000000000000000000377013812246, \
       0.00000000000000000000000225997542918, \
      -0.00000000000000000000000136100844814, \
       0.00000000000000000000000082333232003, \
      -0.00000000000000000000000050025986091, \
       0.00000000000000000000000030526245684, \
      -0.00000000000000000000000018705164021, \
       0.00000000000000000000000011508404393, \
      -0.00000000000000000000000007108714611, \
       0.00000000000000000000000004408065533, \
      -0.00000000000000000000000002743760867, \
       0.00000000000000000000000001714144851, \
      -0.00000000000000000000000001074768860, \
       0.00000000000000000000000000676259777, \
      -0.00000000000000000000000000426981348, \
       0.00000000000000000000000000270500637, \
      -0.00000000000000000000000000171933331, \
       0.00000000000000000000000000109636138, \
      -0.00000000000000000000000000070132573, \
       0.00000000000000000000000000045001784, \
      -0.00000000000000000000000000028963835, \
       0.00000000000000000000000000018697009, \
      -0.00000000000000000000000000012104646, \
       0.00000000000000000000000000007859065, \
      -0.00000000000000000000000000005116867, \
       0.00000000000000000000000000003340627, \
      -0.00000000000000000000000000002186851, \
       0.00000000000000000000000000001435340, \
      -0.00000000000000000000000000000944523, \
       0.00000000000000000000000000000623117, \
      -0.00000000000000000000000000000412101, \
       0.00000000000000000000000000000273208, \
      -0.00000000000000000000000000000181558, \
       0.00000000000000000000000000000120934, \
      -0.00000000000000000000000000000080737, \
       0.00000000000000000000000000000054022, \
      -0.00000000000000000000000000000036227, \
       0.00000000000000000000000000000024348, \
      -0.00000000000000000000000000000016401, \
       0.00000000000000000000000000000011074, \
      -0.00000000000000000000000000000007497, \
       0.00000000000000000000000000000005091, \
      -0.00000000000000000000000000000003470, \
       0.00000000000000000000000000000002377 ] )

  g1cs = np.array ( [ \
      -0.3040578798253495954499726682091083, \
      -0.0566890984597120587731339156118269, \
       0.0039046158173275643919984071554082, \
      -0.0003746075959202260618619339867489, \
       0.0000435431556559843679552220840065, \
      -0.0000057417294453025046561970723475, \
       0.0000008282552104502629741937616492, \
      -0.0000001278245892594642727883913223, \
       0.0000000207978352948687884439257529, \
      -0.0000000035313205921990798042032682, \
       0.0000000006210824236308951068631449, \
      -0.0000000001125215474446292649336987, \
       0.0000000000209088917684421605267019, \
      -0.0000000000039715831737681727689158, \
       0.0000000000007690431314272089939005, \
      -0.0000000000001514696742731613519826, \
       0.0000000000000302892146552359684119, \
      -0.0000000000000061399703834708825400, \
       0.0000000000000012600605829510933553, \
      -0.0000000000000002615029250939483683, \
       0.0000000000000000548278844891796821, \
      -0.0000000000000000116038182129526571, \
       0.0000000000000000024771654107129795, \
      -0.0000000000000000005330672753223389, \
       0.0000000000000000001155666075598465, \
      -0.0000000000000000000252280547744957, \
       0.0000000000000000000055429038550786, \
      -0.0000000000000000000012252208421297, \
       0.0000000000000000000002723664318684, \
      -0.0000000000000000000000608707831422, \
       0.0000000000000000000000136724874476, \
      -0.0000000000000000000000030856626806, \
       0.0000000000000000000000006995212319, \
      -0.0000000000000000000000001592587569, \
       0.0000000000000000000000000364051056, \
      -0.0000000000000000000000000083539465, \
       0.0000000000000000000000000019240303, \
      -0.0000000000000000000000000004446816, \
       0.0000000000000000000000000001031182, \
      -0.0000000000000000000000000000239887, \
       0.0000000000000000000000000000055976, \
      -0.0000000000000000000000000000013100, \
       0.0000000000000000000000000000003074, \
      -0.0000000000000000000000000000000723 ] )

  g2cs = np.array ( [ \
      -0.1211802894731646263541834046858267, \
      -0.0316761386394950286701407923505610, \
       0.0013383199778862680163819429492182, \
      -0.0000895511011392252425531905069518, \
       0.0000079155562961718213115249467924, \
      -0.0000008438793322241520181418982080, \
       0.0000001029980425677530146647227274, \
      -0.0000000139295750605183835795834444, \
       0.0000000020422703959875980400677594, \
      -0.0000000003196534694206427035434752, \
       0.0000000000528147832657267698615312, \
      -0.0000000000091339554672671033735289, \
       0.0000000000016426251238967760444819, \
      -0.0000000000003055897039322660002410, \
       0.0000000000000585655825785779717892, \
      -0.0000000000000115229197730940120563, \
       0.0000000000000023209469119988537310, \
      -0.0000000000000004774355834177535025, \
       0.0000000000000001000996765800180573, \
      -0.0000000000000000213533778082256704, \
       0.0000000000000000046277190777367671, \
      -0.0000000000000000010175807410227657, \
       0.0000000000000000002267657399884672, \
      -0.0000000000000000000511630776076426, \
       0.0000000000000000000116767014913108, \
      -0.0000000000000000000026935427672470, \
       0.0000000000000000000006275665841146, \
      -0.0000000000000000000001475880557531, \
       0.0000000000000000000000350145314739, \
      -0.0000000000000000000000083757732152, \
       0.0000000000000000000000020191815152, \
      -0.0000000000000000000000004903567705, \
       0.0000000000000000000000001199123348, \
      -0.0000000000000000000000000295170610, \
       0.0000000000000000000000000073113112, \
      -0.0000000000000000000000000018217843, \
       0.0000000000000000000000000004565148, \
      -0.0000000000000000000000000001150151, \
       0.0000000000000000000000000000291267, \
      -0.0000000000000000000000000000074125, \
       0.0000000000000000000000000000018953, \
      -0.0000000000000000000000000000004868, \
       0.0000000000000000000000000000001256, \
      -0.0000000000000000000000000000000325 ] )

  g3cs = np.array ( [ \
      -0.0280574367809472928402815264335299, \
      -0.0137271597162236975409100508089556, \
       0.0002894032638760296027448941273751, \
      -0.0000114129239391197145908743622517, \
       0.0000006813965590726242997720207302, \
      -0.0000000547952289604652363669058052, \
       0.0000000055207429918212529109406521, \
      -0.0000000006641464199322920022491428, \
       0.0000000000922373663487041108564960, \
      -0.0000000000144299088886682862611718, \
       0.0000000000024963904892030710248705, \
      -0.0000000000004708240675875244722971, \
       0.0000000000000957217659216759988140, \
      -0.0000000000000207889966095809030537, \
       0.0000000000000047875099970877431627, \
      -0.0000000000000011619070583377173759, \
       0.0000000000000002956508969267836974, \
      -0.0000000000000000785294988256492025, \
       0.0000000000000000216922264368256612, \
      -0.0000000000000000062113515831676342, \
       0.0000000000000000018384568838450977, \
      -0.0000000000000000005610887482137276, \
       0.0000000000000000001761862805280062, \
      -0.0000000000000000000568111050541451, \
       0.0000000000000000000187786279582313, \
      -0.0000000000000000000063531694151124, \
       0.0000000000000000000021968802368238, \
      -0.0000000000000000000007754666550395, \
       0.0000000000000000000002791018356581, \
      -0.0000000000000000000001023178525247, \
       0.0000000000000000000000381693403919, \
      -0.0000000000000000000000144767895606, \
       0.0000000000000000000000055779512634, \
      -0.0000000000000000000000021817239071, \
       0.0000000000000000000000008656646309, \
      -0.0000000000000000000000003482157895, \
       0.0000000000000000000000001419188130, \
      -0.0000000000000000000000000585714314, \
       0.0000000000000000000000000244660482, \
      -0.0000000000000000000000000103387099, \
       0.0000000000000000000000000044177299, \
      -0.0000000000000000000000000019080079, \
       0.0000000000000000000000000008326038, \
      -0.0000000000000000000000000003669553, \
       0.0000000000000000000000000001632875, \
      -0.0000000000000000000000000000733357, \
       0.0000000000000000000000000000332327, \
      -0.0000000000000000000000000000151906, \
       0.0000000000000000000000000000070020, \
      -0.0000000000000000000000000000032539, \
       0.0000000000000000000000000000015240, \
      -0.0000000000000000000000000000007193, \
       0.0000000000000000000000000000003420, \
      -0.0000000000000000000000000000001638, \
       0.0000000000000000000000000000000790, \
      -0.0000000000000000000000000000000383 ] )

  tol = 0.1 * r8_mach ( 3 )
  nf1 = r8_inits ( f1cs, 43, tol )
  nf2 = r8_inits ( f2cs, 99, tol )
  ng1 = r8_inits ( g1cs, 44, tol )
  ng2 = r8_inits ( g2cs, 44, tol )
  ng3 = r8_inits ( g3cs, 56, tol )
  xbig = np.sqrt ( 1.0 / r8_mach ( 3 ) )
  xmaxf = np.exp ( min ( - np.log ( r8_mach ( 1 ) ), \
    np.log ( r8_mach ( 2 ) ) ) - 0.01 )
  xmaxg = 1.0 / np.sqrt ( r8_mach ( 1 ) )
  xbnd = np.sqrt ( 50.0 )
  xbndg = np.sqrt ( 200.0 )

  if ( x < 4.0 ):
    print ( '' )
    print ( 'r8_sifg - Fatal error!' )
    print ( '  Approximation invalid for X < 4.' )
    raise Exception ( 'r8_sifg - Fatal error!' )
  elif ( x <= xbnd ):
    f = ( 1.0 + r8_csevl ( ( 1.0 / x / x - 0.04125 ) / 0.02125, f1cs, nf1 ) ) / x
    g = ( 1.0 + r8_csevl ( ( 1.0 / x / x - 0.04125 ) / 0.02125, g1cs, ng1 ) ) / x / x
  elif ( x <= xbig ):
    f = ( 1.0 + r8_csevl ( 100. / x / x - 1.0, f2cs, nf2 ) ) / x
    if ( x <= xbndg ):
      g = ( 1.0 + r8_csevl ( ( 10000.0 / x / x - 125.0 ) / 75.0, g2cs, ng2 ) ) / x / x
    else:
      g = ( 1.0 + r8_csevl ( 400.0 / x / x - 1.0, g3cs, ng3 ) ) / x / x
  else:
    if ( x < xmaxf ):
      f = 1.0 / x
    else:
      f = 0.0
    if ( x < xmaxg ):
      g = 1.0 / x / x
    else:
      g = 0.0

  return f, g

def r8_cos_deg ( x ):

#*****************************************************************************80
#
## r8_cos_deg() evaluates the cosine of an R8 argument in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  raddeg = 0.017453292519943295769236907684886

  value = r8_cos ( raddeg * x )

  if ( ( x % 90.0 ) == 0.0 ):

    n = np.floor ( abs ( x ) / 90.0 + 0.5 )
    n = ( n % 2 )

    if ( n == 1 ):
      value = 0.0
    elif ( value < 0.0 ):
      value = - 1.0
    else:
      value = + 1.0

  return value

def r8_cos_deg_test ( ):

#*****************************************************************************80
#
## r8_cos_deg_test() tests r8_cos_deg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_cos_deg_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cos_deg evaluates the cosine of an argument in degrees.' )
  print ( '' )
  print ( '             X     cos_deg(X)  r8_cos_deg(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cos_degree_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cos_deg ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_cosh ( x ):

#*****************************************************************************80
#
## r8_cosh() evaluates the hyperbolic cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ymax = 1.0 / np.sqrt ( r8_mach ( 3 ) )

  y = r8_exp ( abs ( x ) )

  if ( y < ymax ):
    value = 0.5 * ( y + 1.0 / y )
  else:
    value = 0.5 * y

  return value

def r8_cosh_test ( ):

#*****************************************************************************80
#
## r8_cosh_test() tests r8_cosh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_cosh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cosh evaluates the hyperbolic cosine function.' )
  print ( '' )
  print ( '             X         COSH(X)  r8_cosh(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cosh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cosh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_cos ( x ):

#*****************************************************************************80
#
## r8_cos() evaluates the cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np
#
#  pihi + pilo = pi.  pihi is exactly representable on all machines
#  with at least 8 bits of precision.  whether it is exactly
#  represented depends on the compiler.  this routine is more
#  accurate if it is exactly represented.
#
  pi2 = 1.57079632679489661923132169163975
  pi2rec = 0.63661977236758134307553505349006
  pihi = 3.140625
  pilo = 9.6765358979323846264338327950288E-04
  pirec = 0.31830988618379067153776752674503

  sincs = np.array ( [ \
      -0.374991154955873175839919279977323464, \
      -0.181603155237250201863830316158004754, \
      +0.005804709274598633559427341722857921, \
      -0.000086954311779340757113212316353178, \
      +0.000000754370148088851481006839927030, \
      -0.000000004267129665055961107126829906, \
      +0.000000000016980422945488168181824792, \
      -0.000000000000050120578889961870929524, \
      +0.000000000000000114101026680010675628, \
      -0.000000000000000000206437504424783134, \
      +0.000000000000000000000303969595918706, \
      -0.000000000000000000000000371357734157, \
      +0.000000000000000000000000000382486123, \
      -0.000000000000000000000000000000336623, \
      +0.000000000000000000000000000000000256 ] )

  ntsn = r8_inits ( sincs, 15, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 2.0 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xwarn = np.sqrt ( xmax )

  absx = abs ( x )
  y = absx + pi2

  if ( xmax < y ):
    print ( '' )
    print ( 'r8_cos - Warning!' )
    print ( '  No precision because |X| is big.' )
    value = 0.0
    return value

  if ( xwarn < y ):
    print ( '' )
    print ( 'r8_cos - Warning!' )
    print ( '  Answer < half precision because |X| is big.' )

  value = 1.0

  if ( absx < xsml ):
    return value

  xn = r8_aint ( y * pirec + 0.5 )
  n2 = r8_aint ( ( xn % 2.0 ) + 0.5 )
  xn = xn - 0.5
  f = ( absx - xn * pihi ) - xn * pilo

  xn = 2.0 * ( f * pi2rec ) * ( f * pi2rec ) - 1.0

  value = f + f * r8_csevl ( xn, sincs, ntsn )

  if ( n2 != 0 ):
    value = - value

  if ( value < -1.0 ):
    value = -1.0
  elif ( 1.0 < value ):
    value = 1.0

  return value

def r8_cos_test ( ):

#*****************************************************************************80
#
## r8_cos_test() tests r8_cos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_cos_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cos evaluates the cosine function.' )
  print ( '' )
  print ( '             X         COS(X)  r8_cos(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cos_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cos ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_cot ( x ):

#*****************************************************************************80
#
## r8_cot() evaluates the cotangent of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  pi2rec = 0.011619772367581343075535053490057

  cotcs = np.array ( [ \
      +0.240259160982956302509553617744970, \
      -0.165330316015002278454746025255758E-01, \
      -0.429983919317240189356476228239895E-04, \
      -0.159283223327541046023490851122445E-06, \
      -0.619109313512934872588620579343187E-09, \
      -0.243019741507264604331702590579575E-11, \
      -0.956093675880008098427062083100000E-14, \
      -0.376353798194580580416291539706666E-16, \
      -0.148166574646746578852176794666666E-18, \
      -0.583335658903666579477984000000000E-21, \
      -0.229662646964645773928533333333333E-23, \
      -0.904197057307483326719999999999999E-26, \
      -0.355988551920600064000000000000000E-28, \
      -0.140155139824298666666666666666666E-30, \
      -0.551800436872533333333333333333333E-33 ] )

  nterms = r8_inits ( cotcs, 15, 0.1 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xsml = np.sqrt ( 3.0 * r8_mach ( 3 ) )
  xmin = np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) )  + 0.01 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( y < xmin ):
    print ( '' )
    print ( 'r8_cot - Fatal error!' )
    print ( '  |X| is too small.' )
    raise Exception ( 'r8_cot - Fatal error!' )

  if ( xmax < y ):
    print ( '' )
    print ( 'r8_cot - Fatal error!' )
    print ( '  |X| is too big.' )
    raise Exception ( 'r8_cot - Fatal error!' )

  ainty = r8_aint ( y )
  yrem = y - ainty
  prodbg = 0.625 * ainty
  ainty = r8_aint ( prodbg )
  y = ( prodbg - ainty ) + 0.625 * yrem + y * pi2rec
  ainty2 = r8_aint ( y )
  ainty = ainty + ainty2
  y = y - ainty2

  ifn = r8_aint ( ( ainty % 2.0 ) )

  if ( ifn == 1 ):
    y = 1.0 - y

  if ( 0.5 < abs ( x ) and y < abs ( x ) * sqeps ):
    print ( '' )
    print ( 'r8_cot - Warning!' )
    print ( '  Answer less than half precision.' )
    print ( '  |X| too big, or X nearly a nonzero multiple of pi.' )

  if ( y == 0.0 ):
    print ( '' )
    print ( 'r8_cot - Fatal error!' )
    print ( '  X is a multiple of pi.' )
    raise Exception ( 'r8_cot - Fatal error!' )

  elif ( y <= xsml ):

    value = 1.0 / y

  elif ( y <= 0.25 ):

    value = ( 0.5 + r8_csevl ( 32.0 * y * y - 1.0, cotcs, nterms ) ) / y

  elif ( y <= 0.5 ):

    value = ( 0.5 + r8_csevl ( 8.0 * y * y - 1.0, \
      cotcs, nterms ) ) / ( 0.5 * y )

    value = ( value * value - 1.0 ) * 0.5 / value

  else:

    value = ( 0.5 + r8_csevl ( 2.0 * y * y - 1.0, \
      cotcs, nterms ) ) / ( 0.25 * y )
    value = ( value * value - 1.0 ) * 0.5 / value
    value = ( value * value - 1.0 ) * 0.5 / value

  if ( x < 0.0 ):
    value = - abs ( value )
  else:
    value = + abs ( value )

  if ( ifn == 1 ):
    value = - value

  return value

def r8_cot_test ( ):

#*****************************************************************************80
#
## r8_cot_test() tests r8_cot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_cot_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cot evaluates the cotangent function.' )
  print ( '' )
  print ( '             X         COT(X)  r8_cot(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cot_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cot ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_csevl ( x, a, n ):

#*****************************************************************************80
#
## r8_csevl() evaluates a Chebyshev series.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Input:
#
#    real X, the evaluation point.
#
#    real CS(N), the Chebyshev coefficients.
#
#    integer N, the number of Chebyshev coefficients.
#
#  Output:
#
#    real VALUE, the Chebyshev series evaluated at X.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'r8_csevl - Fatal error!' )
    print ( '  Number of terms <= 0.' )
    raise Exception ( 'r8_csevl - Fatal error!' )

  if ( 1000 < n ):
    print ( '' )
    print ( 'r8_csevl - Fatal error!' )
    print ( '  Number of terms > 1000.' )
    raise Exception ( 'r8_csevl - Fatal error!' )

  if ( x < -1.1 or 1.1 < x ):
    print ( '' )
    print ( 'r8_csevl - Fatal error!' )
    print ( '  X outside (-1,+1)' )
    print ( '  X = %g' % ( x ) )
    raise Exception ( 'r8_csevl - Fatal error!' )

  b1 = 0.0
  b0 = 0.0

  for i in range ( n - 1, -1, -1 ):
    b2 = b1
    b1 = b0
    b0 = 2.0 * x * b1 - b2 + a[i]

  value = 0.5 * ( b0 - b2 )

  return value

def r8_csevl_test ( ):

#*****************************************************************************80
#
## r8_csevl_test() tests r8_csevl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  expcs = np.array ( [ \
   2.532131755504016E+00, \
   1.130318207984970E+00, \
   0.271495339534077E+00, \
   0.044336849848664E+00, \
   0.005474240442094E+00, \
   0.000542926311914E+00, \
   0.000044977322954E+00, \
   0.000003198436462E+00, \
   0.000000199212481E+00, \
   0.000000011036772E+00, \
   0.000000000550590E+00, \
   0.000000000024980E+00, \
   0.000000000001039E+00, \
   0.000000000000040E+00, \
   0.000000000000001E+00 ] )

  print ( '' )
  print ( 'r8_csevl_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_csevl evaluates a Chebyshev approximant' )
  print ( '  of N terms at a point X.' )
  print ( '' )
  print ( '  Here we use an approximant to the exponential function' )
  print ( '  and average the absolute error at 21 points.' )
  print ( '' )
  print ( '   N    error' )
  print ( '' )

  for n in range ( 1, 13 ):
    err = 0.0
    for i in range ( -10, 11 ):
      x = float ( i ) / 10.0
      s = r8_csevl ( x, expcs, n )
      err = err + abs ( s - np.exp ( x ) )
    err = err / 21.0
    print ( '  %2d  %14.6g' % ( n, err ) )

  return

def r8_dawson ( x ):

#*****************************************************************************80
#
## r8_dawson() evaluates Dawson's integral of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  daw2cs = np.array ( [ \
      -0.56886544105215527114160533733674E-01, \
      -0.31811346996168131279322878048822, \
      +0.20873845413642236789741580198858, \
      -0.12475409913779131214073498314784, \
      +0.67869305186676777092847516423676E-01, \
      -0.33659144895270939503068230966587E-01, \
      +0.15260781271987971743682460381640E-01, \
      -0.63483709625962148230586094788535E-02, \
      +0.24326740920748520596865966109343E-02, \
      -0.86219541491065032038526983549637E-03, \
      +0.28376573336321625302857636538295E-03, \
      -0.87057549874170423699396581464335E-04, \
      +0.24986849985481658331800044137276E-04, \
      -0.67319286764160294344603050339520E-05, \
      +0.17078578785573543710504524047844E-05, \
      -0.40917551226475381271896592490038E-06, \
      +0.92828292216755773260751785312273E-07, \
      -0.19991403610147617829845096332198E-07, \
      +0.40963490644082195241210487868917E-08, \
      -0.80032409540993168075706781753561E-09, \
      +0.14938503128761465059143225550110E-09, \
      -0.26687999885622329284924651063339E-10, \
      +0.45712216985159458151405617724103E-11, \
      -0.75187305222043565872243727326771E-12, \
      +0.11893100052629681879029828987302E-12, \
      -0.18116907933852346973490318263084E-13, \
      +0.26611733684358969193001612199626E-14, \
      -0.37738863052129419795444109905930E-15, \
      +0.51727953789087172679680082229329E-16, \
      -0.68603684084077500979419564670102E-17, \
      +0.88123751354161071806469337321745E-18, \
      -0.10974248249996606292106299624652E-18, \
      +0.13261199326367178513595545891635E-19, \
      -0.15562732768137380785488776571562E-20, \
      +0.17751425583655720607833415570773E-21, \
      -0.19695006967006578384953608765439E-22, \
      +0.21270074896998699661924010120533E-23, \
      -0.22375398124627973794182113962666E-24, \
      +0.22942768578582348946971383125333E-25, \
      -0.22943788846552928693329592319999E-26, \
      +0.22391702100592453618342297600000E-27, \
      -0.21338230616608897703678225066666E-28, \
      +0.19866196585123531518028458666666E-29, \
      -0.18079295866694391771955199999999E-30, \
      +0.16090686015283030305450666666666E-31 ] )

  dawacs = np.array ( [ \
      +0.1690485637765703755422637438849E-01, \
      +0.8683252278406957990536107850768E-02, \
      +0.2424864042417715453277703459889E-03, \
      +0.1261182399572690001651949240377E-04, \
      +0.1066453314636176955705691125906E-05, \
      +0.1358159794790727611348424505728E-06, \
      +0.2171042356577298398904312744743E-07, \
      +0.2867010501805295270343676804813E-08, \
      -0.1901336393035820112282492378024E-09, \
      -0.3097780484395201125532065774268E-09, \
      -0.1029414876057509247398132286413E-09, \
      -0.6260356459459576150417587283121E-11, \
      +0.8563132497446451216262303166276E-11, \
      +0.3033045148075659292976266276257E-11, \
      -0.2523618306809291372630886938826E-12, \
      -0.4210604795440664513175461934510E-12, \
      -0.4431140826646238312143429452036E-13, \
      +0.4911210272841205205940037065117E-13, \
      +0.1235856242283903407076477954739E-13, \
      -0.5788733199016569246955765071069E-14, \
      -0.2282723294807358620978183957030E-14, \
      +0.7637149411014126476312362917590E-15, \
      +0.3851546883566811728777594002095E-15, \
      -0.1199932056928290592803237283045E-15, \
      -0.6313439150094572347334270285250E-16, \
      +0.2239559965972975375254912790237E-16, \
      +0.9987925830076495995132891200749E-17, \
      -0.4681068274322495334536246507252E-17, \
      -0.1436303644349721337241628751534E-17, \
      +0.1020822731410541112977908032130E-17, \
      +0.1538908873136092072837389822372E-18, \
      -0.2189157877645793888894790926056E-18, \
      +0.2156879197938651750392359152517E-20, \
      +0.4370219827442449851134792557395E-19, \
      -0.8234581460977207241098927905177E-20, \
      -0.7498648721256466222903202835420E-20, \
      +0.3282536720735671610957612930039E-20, \
      +0.8858064309503921116076561515151E-21, \
      -0.9185087111727002988094460531485E-21, \
      +0.2978962223788748988314166045791E-22, \
      +0.1972132136618471883159505468041E-21, \
      -0.5974775596362906638089584995117E-22, \
      -0.2834410031503850965443825182441E-22, \
      +0.2209560791131554514777150489012E-22, \
      -0.5439955741897144300079480307711E-25, \
      -0.5213549243294848668017136696470E-23, \
      +0.1702350556813114199065671499076E-23, \
      +0.6917400860836148343022185660197E-24, \
      -0.6540941793002752512239445125802E-24, \
      +0.6093576580439328960371824654636E-25, \
      +0.1408070432905187461501945080272E-24, \
      -0.6785886121054846331167674943755E-25, \
      -0.9799732036214295711741583102225E-26, \
      +0.2121244903099041332598960939160E-25, \
      -0.5954455022548790938238802154487E-26, \
      -0.3093088861875470177838847232049E-26, \
      +0.2854389216344524682400691986104E-26, \
      -0.3951289447379305566023477271811E-27, \
      -0.5906000648607628478116840894453E-27, \
      +0.3670236964668687003647889980609E-27, \
      -0.4839958238042276256598303038941E-29, \
      -0.9799265984210443869597404017022E-28, \
      +0.4684773732612130606158908804300E-28, \
      +0.5030877696993461051647667603155E-29, \
      -0.1547395051706028239247552068295E-28, \
      +0.6112180185086419243976005662714E-29, \
      +0.1357913399124811650343602736158E-29, \
      -0.2417687752768673088385304299044E-29, \
      +0.8369074582074298945292887587291E-30, \
      +0.2665413042788979165838319401566E-30, \
      -0.3811653692354890336935691003712E-30, \
      +0.1230054721884951464371706872585E-30, \
      +0.4622506399041493508805536929983E-31, \
      -0.6120087296881677722911435593001E-31, \
      +0.1966024640193164686956230217896E-31 ] )

  dawcs = np.array ( [ \
      -0.6351734375145949201065127736293E-02, \
      -0.2294071479677386939899824125866, \
      +0.2213050093908476441683979161786E-01, \
      -0.1549265453892985046743057753375E-02, \
      +0.8497327715684917456777542948066E-04, \
      -0.3828266270972014924994099521309E-05, \
      +0.1462854806250163197757148949539E-06, \
      -0.4851982381825991798846715425114E-08, \
      +0.1421463577759139790347568183304E-09, \
      -0.3728836087920596525335493054088E-11, \
      +0.8854942961778203370194565231369E-13, \
      -0.1920757131350206355421648417493E-14, \
      +0.3834325867246327588241074439253E-16, \
      -0.7089154168175881633584099327999E-18, \
      +0.1220552135889457674416901120000E-19, \
      -0.1966204826605348760299451733333E-21, \
      +0.2975845541376597189113173333333E-23, \
      -0.4247069514800596951039999999999E-25, \
      +0.5734270767391742798506666666666E-27, \
      -0.7345836823178450261333333333333E-29, \
      +0.8951937667516552533333333333333E-31 ] )

  eps = r8_mach ( 3 )
  ntdaw  = r8_inits ( dawcs,  21, 0.1 * eps )
  ntdaw2 = r8_inits ( daw2cs, 45, 0.1 * eps )
  ntdawa = r8_inits ( dawacs, 75, 0.1 * eps )
  xsml = np.sqrt ( 1.5 * eps )
  xbig = np.sqrt ( 0.5 / eps )
  xmax = np.exp ( min ( - np.log ( 2.0 * r8_mach ( 1 ) ), \
      np.log ( r8_mach ( 2 ) ) ) - 0.01 )

  y = abs ( x )

  if ( y <= xsml ):
    value = x
  elif ( y <= 1.0 ):
    value = x * ( 0.75 + r8_csevl ( 2.0 * y * y - 1.0, dawcs, ntdaw ) )
  elif ( y <= 4.0 ):
    value = x * ( 0.25 + r8_csevl ( 0.125 * y * y - 1.0, daw2cs, ntdaw2 ) )
  elif ( y < xbig ):
    value = ( 0.5 + r8_csevl ( 32.0 / y / y - 1.0, dawacs, ntdawa ) ) / x
  elif ( y <= xmax ):
    value = 0.5 / x
  else:
    value = 0.0

  return value

def r8_dawson_test ( ):

#*****************************************************************************80
#
## r8_dawson_test() tests r8_dawson().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_dawson_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_dawson evaluates Dawson\'s integral.' )
  print ( '' )
  print ( '             X      DAWSON(X)  r8_dawson(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = dawson_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_dawson ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_e1 ( x ):

#*****************************************************************************80
#
## r8_e1() evaluates the exponential integral E1 for an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ae10cs = np.array ( [ \
      +0.3284394579616699087873844201881E-01, \
      -0.1669920452031362851476184343387E-01, \
      +0.2845284724361346807424899853252E-03, \
      -0.7563944358516206489487866938533E-05, \
      +0.2798971289450859157504843180879E-06, \
      -0.1357901828534531069525563926255E-07, \
      +0.8343596202040469255856102904906E-09, \
      -0.6370971727640248438275242988532E-10, \
      +0.6007247608811861235760831561584E-11, \
      -0.7022876174679773590750626150088E-12, \
      +0.1018302673703687693096652346883E-12, \
      -0.1761812903430880040406309966422E-13, \
      +0.3250828614235360694244030353877E-14, \
      -0.5071770025505818678824872259044E-15, \
      +0.1665177387043294298172486084156E-16, \
      +0.3166753890797514400677003536555E-16, \
      -0.1588403763664141515133118343538E-16, \
      +0.4175513256138018833003034618484E-17, \
      -0.2892347749707141906710714478852E-18, \
      -0.2800625903396608103506340589669E-18, \
      +0.1322938639539270903707580023781E-18, \
      -0.1804447444177301627283887833557E-19, \
      -0.7905384086522616076291644817604E-20, \
      +0.4435711366369570103946235838027E-20, \
      -0.4264103994978120868865309206555E-21, \
      -0.3920101766937117541553713162048E-21, \
      +0.1527378051343994266343752326971E-21, \
      +0.1024849527049372339310308783117E-22, \
      -0.2134907874771433576262711405882E-22, \
      +0.3239139475160028267061694700366E-23, \
      +0.2142183762299889954762643168296E-23, \
      -0.8234609419601018414700348082312E-24, \
      -0.1524652829645809479613694401140E-24, \
      +0.1378208282460639134668480364325E-24, \
      +0.2131311202833947879523224999253E-26, \
      -0.2012649651526484121817466763127E-25, \
      +0.1995535662263358016106311782673E-26, \
      +0.2798995808984003464948686520319E-26, \
      -0.5534511845389626637640819277823E-27, \
      -0.3884995396159968861682544026146E-27, \
      +0.1121304434507359382850680354679E-27, \
      +0.5566568152423740948256563833514E-28, \
      -0.2045482929810499700448533938176E-28, \
      -0.8453813992712336233411457493674E-29, \
      +0.3565758433431291562816111116287E-29, \
      +0.1383653872125634705539949098871E-29, \
      -0.6062167864451372436584533764778E-30, \
      -0.2447198043989313267437655119189E-30, \
      +0.1006850640933998348011548180480E-30, \
      +0.4623685555014869015664341461674E-31 ] )

  ae11cs = np.array ( [ \
      +0.20263150647078889499401236517381, \
      -0.73655140991203130439536898728034E-01, \
      +0.63909349118361915862753283840020E-02, \
      -0.60797252705247911780653153363999E-03, \
      -0.73706498620176629330681411493484E-04, \
      +0.48732857449450183453464992488076E-04, \
      -0.23837064840448290766588489460235E-05, \
      -0.30518612628561521027027332246121E-05, \
      +0.17050331572564559009688032992907E-06, \
      +0.23834204527487747258601598136403E-06, \
      +0.10781772556163166562596872364020E-07, \
      -0.17955692847399102653642691446599E-07, \
      -0.41284072341950457727912394640436E-08, \
      +0.68622148588631968618346844526664E-09, \
      +0.53130183120506356147602009675961E-09, \
      +0.78796880261490694831305022893515E-10, \
      -0.26261762329356522290341675271232E-10, \
      -0.15483687636308261963125756294100E-10, \
      -0.25818962377261390492802405122591E-11, \
      +0.59542879191591072658903529959352E-12, \
      +0.46451400387681525833784919321405E-12, \
      +0.11557855023255861496288006203731E-12, \
      -0.10475236870835799012317547189670E-14, \
      -0.11896653502709004368104489260929E-13, \
      -0.47749077490261778752643019349950E-14, \
      -0.81077649615772777976249734754135E-15, \
      +0.13435569250031554199376987998178E-15, \
      +0.14134530022913106260248873881287E-15, \
      +0.49451592573953173115520663232883E-16, \
      +0.79884048480080665648858587399367E-17, \
      -0.14008632188089809829248711935393E-17, \
      -0.14814246958417372107722804001680E-17, \
      -0.55826173646025601904010693937113E-18, \
      -0.11442074542191647264783072544598E-18, \
      +0.25371823879566853500524018479923E-20, \
      +0.13205328154805359813278863389097E-19, \
      +0.62930261081586809166287426789485E-20, \
      +0.17688270424882713734999261332548E-20, \
      +0.23266187985146045209674296887432E-21, \
      -0.67803060811125233043773831844113E-22, \
      -0.59440876959676373802874150531891E-22, \
      -0.23618214531184415968532592503466E-22, \
      -0.60214499724601478214168478744576E-23, \
      -0.65517906474348299071370444144639E-24, \
      +0.29388755297497724587042038699349E-24, \
      +0.22601606200642115173215728758510E-24, \
      +0.89534369245958628745091206873087E-25, \
      +0.24015923471098457555772067457706E-25, \
      +0.34118376888907172955666423043413E-26, \
      -0.71617071694630342052355013345279E-27, \
      -0.75620390659281725157928651980799E-27, \
      -0.33774612157467324637952920780800E-27, \
      -0.10479325703300941711526430332245E-27, \
      -0.21654550252170342240854880201386E-28, \
      -0.75297125745288269994689298432000E-30, \
      +0.19103179392798935768638084000426E-29, \
      +0.11492104966530338547790728833706E-29, \
      +0.43896970582661751514410359193600E-30, \
      +0.12320883239205686471647157725866E-30, \
      +0.22220174457553175317538581162666E-31 ] )

  ae12cs = np.array ( [ \
      +0.63629589796747038767129887806803, \
      -0.13081168675067634385812671121135, \
      -0.84367410213053930014487662129752E-02, \
      +0.26568491531006685413029428068906E-02, \
      +0.32822721781658133778792170142517E-03, \
      -0.23783447771430248269579807851050E-04, \
      -0.11439804308100055514447076797047E-04, \
      -0.14405943433238338455239717699323E-05, \
      +0.52415956651148829963772818061664E-08, \
      +0.38407306407844323480979203059716E-07, \
      +0.85880244860267195879660515759344E-08, \
      +0.10219226625855003286339969553911E-08, \
      +0.21749132323289724542821339805992E-10, \
      -0.22090238142623144809523503811741E-10, \
      -0.63457533544928753294383622208801E-11, \
      -0.10837746566857661115340539732919E-11, \
      -0.11909822872222586730262200440277E-12, \
      -0.28438682389265590299508766008661E-14, \
      +0.25080327026686769668587195487546E-14, \
      +0.78729641528559842431597726421265E-15, \
      +0.15475066347785217148484334637329E-15, \
      +0.22575322831665075055272608197290E-16, \
      +0.22233352867266608760281380836693E-17, \
      +0.16967819563544153513464194662399E-19, \
      -0.57608316255947682105310087304533E-19, \
      -0.17591235774646878055625369408853E-19, \
      -0.36286056375103174394755328682666E-20, \
      -0.59235569797328991652558143488000E-21, \
      -0.76030380926310191114429136895999E-22, \
      -0.62547843521711763842641428479999E-23, \
      +0.25483360759307648606037606400000E-24, \
      +0.25598615731739857020168874666666E-24, \
      +0.71376239357899318800207052800000E-25, \
      +0.14703759939567568181578956800000E-25, \
      +0.25105524765386733555198634666666E-26, \
      +0.35886666387790890886583637333333E-27, \
      +0.39886035156771301763317759999999E-28, \
      +0.21763676947356220478805333333333E-29, \
      -0.46146998487618942367607466666666E-30, \
      -0.20713517877481987707153066666666E-30, \
      -0.51890378563534371596970666666666E-31 ] )

  ae13cs = np.array ( [ \
      -0.60577324664060345999319382737747, \
      -0.11253524348366090030649768852718, \
      +0.13432266247902779492487859329414E-01, \
      -0.19268451873811457249246838991303E-02, \
      +0.30911833772060318335586737475368E-03, \
      -0.53564132129618418776393559795147E-04, \
      +0.98278128802474923952491882717237E-05, \
      -0.18853689849165182826902891938910E-05, \
      +0.37494319356894735406964042190531E-06, \
      -0.76823455870552639273733465680556E-07, \
      +0.16143270567198777552956300060868E-07, \
      -0.34668022114907354566309060226027E-08, \
      +0.75875420919036277572889747054114E-09, \
      -0.16886433329881412573514526636703E-09, \
      +0.38145706749552265682804250927272E-10, \
      -0.87330266324446292706851718272334E-11, \
      +0.20236728645867960961794311064330E-11, \
      -0.47413283039555834655210340820160E-12, \
      +0.11221172048389864324731799928920E-12, \
      -0.26804225434840309912826809093395E-13, \
      +0.64578514417716530343580369067212E-14, \
      -0.15682760501666478830305702849194E-14, \
      +0.38367865399315404861821516441408E-15, \
      -0.94517173027579130478871048932556E-16, \
      +0.23434812288949573293896666439133E-16, \
      -0.58458661580214714576123194419882E-17, \
      +0.14666229867947778605873617419195E-17, \
      -0.36993923476444472706592538274474E-18, \
      +0.93790159936721242136014291817813E-19, \
      -0.23893673221937873136308224087381E-19, \
      +0.61150624629497608051934223837866E-20, \
      -0.15718585327554025507719853288106E-20, \
      +0.40572387285585397769519294491306E-21, \
      -0.10514026554738034990566367122773E-21, \
      +0.27349664930638667785806003131733E-22, \
      -0.71401604080205796099355574271999E-23, \
      +0.18705552432235079986756924211199E-23, \
      -0.49167468166870480520478020949333E-24, \
      +0.12964988119684031730916087125333E-24, \
      -0.34292515688362864461623940437333E-25, \
      +0.90972241643887034329104820906666E-26, \
      -0.24202112314316856489934847999999E-26, \
      +0.64563612934639510757670475093333E-27, \
      -0.17269132735340541122315987626666E-27, \
      +0.46308611659151500715194231466666E-28, \
      -0.12448703637214131241755170133333E-28, \
      +0.33544574090520678532907007999999E-29, \
      -0.90598868521070774437543935999999E-30, \
      +0.24524147051474238587273216000000E-30, \
      -0.66528178733552062817107967999999E-31 ] )

  ae14cs = np.array ( [ \
      -0.1892918000753016825495679942820, \
      -0.8648117855259871489968817056824E-01, \
      +0.7224101543746594747021514839184E-02, \
      -0.8097559457557386197159655610181E-03, \
      +0.1099913443266138867179251157002E-03, \
      -0.1717332998937767371495358814487E-04, \
      +0.2985627514479283322825342495003E-05, \
      -0.5659649145771930056560167267155E-06, \
      +0.1152680839714140019226583501663E-06, \
      -0.2495030440269338228842128765065E-07, \
      +0.5692324201833754367039370368140E-08, \
      -0.1359957664805600338490030939176E-08, \
      +0.3384662888760884590184512925859E-09, \
      -0.8737853904474681952350849316580E-10, \
      +0.2331588663222659718612613400470E-10, \
      -0.6411481049213785969753165196326E-11, \
      +0.1812246980204816433384359484682E-11, \
      -0.5253831761558460688819403840466E-12, \
      +0.1559218272591925698855028609825E-12, \
      -0.4729168297080398718476429369466E-13, \
      +0.1463761864393243502076199493808E-13, \
      -0.4617388988712924102232173623604E-14, \
      +0.1482710348289369323789239660371E-14, \
      -0.4841672496239229146973165734417E-15, \
      +0.1606215575700290408116571966188E-15, \
      -0.5408917538957170947895023784252E-16, \
      +0.1847470159346897881370231402310E-16, \
      -0.6395830792759094470500610425050E-17, \
      +0.2242780721699759457250233276170E-17, \
      -0.7961369173983947552744555308646E-18, \
      +0.2859308111540197459808619929272E-18, \
      -0.1038450244701137145900697137446E-18, \
      +0.3812040607097975780866841008319E-19, \
      -0.1413795417717200768717562723696E-19, \
      +0.5295367865182740958305442594815E-20, \
      -0.2002264245026825902137211131439E-20, \
      +0.7640262751275196014736848610918E-21, \
      -0.2941119006868787883311263523362E-21, \
      +0.1141823539078927193037691483586E-21, \
      -0.4469308475955298425247020718489E-22, \
      +0.1763262410571750770630491408520E-22, \
      -0.7009968187925902356351518262340E-23, \
      +0.2807573556558378922287757507515E-23, \
      -0.1132560944981086432141888891562E-23, \
      +0.4600574684375017946156764233727E-24, \
      -0.1881448598976133459864609148108E-24, \
      +0.7744916111507730845444328478037E-25, \
      -0.3208512760585368926702703826261E-25, \
      +0.1337445542910839760619930421384E-25, \
      -0.5608671881802217048894771735210E-26, \
      +0.2365839716528537483710069473279E-26, \
      -0.1003656195025305334065834526856E-26, \
      +0.4281490878094161131286642556927E-27, \
      -0.1836345261815318199691326958250E-27, \
      +0.7917798231349540000097468678144E-28, \
      -0.3431542358742220361025015775231E-28, \
      +0.1494705493897103237475066008917E-28, \
      -0.6542620279865705439739042420053E-29, \
      +0.2877581395199171114340487353685E-29, \
      -0.1271557211796024711027981200042E-29, \
      +0.5644615555648722522388044622506E-30, \
      -0.2516994994284095106080616830293E-30, \
      +0.1127259818927510206370368804181E-30, \
      -0.5069814875800460855562584719360E-31 ] )

  e11cs = np.array ( [ \
      -0.16113461655571494025720663927566180E+02, \
      +0.77940727787426802769272245891741497E+01, \
      -0.19554058188631419507127283812814491E+01, \
      +0.37337293866277945611517190865690209, \
      -0.56925031910929019385263892220051166E-01, \
      +0.72110777696600918537847724812635813E-02, \
      -0.78104901449841593997715184089064148E-03, \
      +0.73880933562621681878974881366177858E-04, \
      -0.62028618758082045134358133607909712E-05, \
      +0.46816002303176735524405823868362657E-06, \
      -0.32092888533298649524072553027228719E-07, \
      +0.20151997487404533394826262213019548E-08, \
      -0.11673686816697793105356271695015419E-09, \
      +0.62762706672039943397788748379615573E-11, \
      -0.31481541672275441045246781802393600E-12, \
      +0.14799041744493474210894472251733333E-13, \
      -0.65457091583979673774263401588053333E-15, \
      +0.27336872223137291142508012748799999E-16, \
      -0.10813524349754406876721727624533333E-17, \
      +0.40628328040434303295300348586666666E-19, \
      -0.14535539358960455858914372266666666E-20, \
      +0.49632746181648636830198442666666666E-22, \
      -0.16208612696636044604866560000000000E-23, \
      +0.50721448038607422226431999999999999E-25, \
      -0.15235811133372207813973333333333333E-26, \
      +0.44001511256103618696533333333333333E-28, \
      -0.12236141945416231594666666666666666E-29, \
      +0.32809216661066001066666666666666666E-31, \
      -0.84933452268306432000000000000000000E-33 ] )

  e12cs = np.array ( [ \
      -0.3739021479220279511668698204827E-01, \
      +0.4272398606220957726049179176528E-01, \
      -0.130318207984970054415392055219726, \
      +0.144191240246988907341095893982137E-01, \
      -0.134617078051068022116121527983553E-02, \
      +0.107310292530637799976115850970073E-03, \
      -0.742999951611943649610283062223163E-05, \
      +0.453773256907537139386383211511827E-06, \
      -0.247641721139060131846547423802912E-07, \
      +0.122076581374590953700228167846102E-08, \
      -0.548514148064092393821357398028261E-10, \
      +0.226362142130078799293688162377002E-11, \
      -0.863589727169800979404172916282240E-13, \
      +0.306291553669332997581032894881279E-14, \
      -0.101485718855944147557128906734933E-15, \
      +0.315482174034069877546855328426666E-17, \
      -0.923604240769240954484015923200000E-19, \
      +0.255504267970814002440435029333333E-20, \
      -0.669912805684566847217882453333333E-22, \
      +0.166925405435387319431987199999999E-23, \
      -0.396254925184379641856000000000000E-25, \
      +0.898135896598511332010666666666666E-27, \
      -0.194763366993016433322666666666666E-28, \
      +0.404836019024630033066666666666666E-30, \
      -0.807981567699845120000000000000000E-32 ] )

  eta = 0.1 * r8_mach ( 3 )
  ntae10 = r8_inits ( ae10cs, 50, eta )
  ntae11 = r8_inits ( ae11cs, 60, eta )
  ntae12 = r8_inits ( ae12cs, 41, eta )
  nte11 = r8_inits ( e11cs, 29, eta )
  nte12 = r8_inits ( e12cs, 25, eta )
  ntae13 = r8_inits ( ae13cs, 50, eta )
  ntae14 = r8_inits ( ae14cs, 64, eta )
  xmax = - np.log ( r8_mach ( 1 ) )
  xmax = xmax - np.log ( xmax )

  if ( x <= - 32.0 ):
    value = np.exp ( - x ) / x * ( 1.0 \
      + r8_csevl ( 64.0 / x + 1.0, ae10cs, ntae10 ) )
  elif ( x <= - 8.0 ):
    value = np.exp ( - x ) / x * ( 1.0 \
      + r8_csevl ( ( 64.0 / x + 5.0 ) / 3.0, ae11cs, ntae11 ) )
  elif ( x <= - 4.0 ):
    value = np.exp ( - x ) / x * (1.0 \
      + r8_csevl ( 16.0 / x + 3.0, ae12cs, ntae12 ) )
  elif ( x <= - 1.0 ):
    value = - np.log ( - x ) \
      + r8_csevl ( ( 2.0 * x + 5.0 ) / 3.0, e11cs, nte11 )
  elif ( x == 0.0 ):
    print ( '' )
    print ( 'r8_e1 - Fatal error!' )
    print ( '  X is zero.' )
    raise Exception ( 'r8_e1 - Fatal error!' )
  elif ( x <= 1.0 ):
    value = ( - np.log ( abs ( x ) ) - 0.6875 + x ) \
      + r8_csevl ( x, e12cs, nte12 )
  elif ( x <= 4.0 ):
    value = np.exp ( - x ) / x * ( 1.0 \
      + r8_csevl ( ( 8.0 / x - 5.0 ) / 3.0, ae13cs, ntae13 ) )
  elif ( x <= xmax ):
    value = np.exp ( - x ) / x * ( 1.0 \
      + r8_csevl ( 8.0 / x - 1.0, ae14cs, ntae14 ) )
  else:
    value = 0.0

  return value

def r8_e1_test ( ):

#*****************************************************************************80
#
## r8_e1_test() tests r8_e1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_e1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_e1 evaluates the E1(x) exponential function.' )
  print ( '' )
  print ( '             X           E1(X)  r8_e1(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = e1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_e1 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_ei ( x ):

#*****************************************************************************80
#
## r8_ei() evaluates the exponential integral Ei for an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  value = - r8_e1 ( - x )

  return value

def r8_ei_test ( ):

#*****************************************************************************80
#
## r8_ei_test() tests r8_ei().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_ei_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_ei evaluates the exponential integral Ei(X).' )
  print ( '' )
  print ( '             X           EI(X)  r8_ei(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = ei_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_ei ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_erf ( x ):

#*****************************************************************************80
#
## r8_erf() evaluates the error function of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sqrtpi = 1.77245385090551602729816748334115

  erfcs = np.array ( [ \
      -0.49046121234691808039984544033376E-01, \
      -0.14226120510371364237824741899631E+00, \
      +0.10035582187599795575754676712933E-01, \
      -0.57687646997674847650827025509167E-03, \
      +0.27419931252196061034422160791471E-04, \
      -0.11043175507344507604135381295905E-05, \
      +0.38488755420345036949961311498174E-07, \
      -0.11808582533875466969631751801581E-08, \
      +0.32334215826050909646402930953354E-10, \
      -0.79910159470045487581607374708595E-12, \
      +0.17990725113961455611967245486634E-13, \
      -0.37186354878186926382316828209493E-15, \
      +0.71035990037142529711689908394666E-17, \
      -0.12612455119155225832495424853333E-18, \
      +0.20916406941769294369170500266666E-20, \
      -0.32539731029314072982364160000000E-22, \
      +0.47668672097976748332373333333333E-24, \
      -0.65980120782851343155199999999999E-26, \
      +0.86550114699637626197333333333333E-28, \
      -0.10788925177498064213333333333333E-29, \
      +0.12811883993017002666666666666666E-31 ] )

  nterf = r8_inits ( erfcs, 21, 0.1 * r8_mach ( 3 ) )
  xbig = np.sqrt ( - np.log ( sqrtpi * r8_mach ( 3 ) ) )
  sqeps = np.sqrt ( 2.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= sqeps ):
    value = 2.0 * x / sqrtpi
  elif ( y <= 1.0 ):
    value = x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, erfcs, nterf ) )
  elif ( y <= xbig ):
    value = 1.0 - r8_erfc ( y )
    if ( x < 0.0 ):
      value = - value
  else:
    value = 1.0
    if ( x < 0.0 ):
      value = - value

  return value

def r8_erf_test ( ):

#*****************************************************************************80
#
## r8_erf_test() tests r8_erf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_erf_test():' )
  print ( '  r8_erf evaluates the error function.' )
  print ( '' )
  print ( '             X          ERF(X)  r8_erf(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_erf ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_erfc ( x ):

#*****************************************************************************80
#
## r8_erfc() evaluates the co-error function of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    Ireal X, the argument.
#
#  Output:
#
#    real VALUE, the co-error function of X.
#
  import numpy as np

  sqrtpi = 1.77245385090551602729816748334115

  erc2cs = np.array ( [ \
    -0.6960134660230950112739150826197E-01, \
    -0.4110133936262089348982212084666E-01, \
    +0.3914495866689626881561143705244E-02, \
    -0.4906395650548979161280935450774E-03, \
    +0.7157479001377036380760894141825E-04, \
    -0.1153071634131232833808232847912E-04, \
    +0.1994670590201997635052314867709E-05, \
    -0.3642666471599222873936118430711E-06, \
    +0.6944372610005012589931277214633E-07, \
    -0.1371220902104366019534605141210E-07, \
    +0.2788389661007137131963860348087E-08, \
    -0.5814164724331161551864791050316E-09, \
    +0.1238920491752753181180168817950E-09, \
    -0.2690639145306743432390424937889E-10, \
    +0.5942614350847910982444709683840E-11, \
    -0.1332386735758119579287754420570E-11, \
    +0.3028046806177132017173697243304E-12, \
    -0.6966648814941032588795867588954E-13, \
    +0.1620854541053922969812893227628E-13, \
    -0.3809934465250491999876913057729E-14, \
    +0.9040487815978831149368971012975E-15, \
    -0.2164006195089607347809812047003E-15, \
    +0.5222102233995854984607980244172E-16, \
    -0.1269729602364555336372415527780E-16, \
    +0.3109145504276197583836227412951E-17, \
    -0.7663762920320385524009566714811E-18, \
    +0.1900819251362745202536929733290E-18, \
    -0.4742207279069039545225655999965E-19, \
    +0.1189649200076528382880683078451E-19, \
    -0.3000035590325780256845271313066E-20, \
    +0.7602993453043246173019385277098E-21, \
    -0.1935909447606872881569811049130E-21, \
    +0.4951399124773337881000042386773E-22, \
    -0.1271807481336371879608621989888E-22, \
    +0.3280049600469513043315841652053E-23, \
    -0.8492320176822896568924792422399E-24, \
    +0.2206917892807560223519879987199E-24, \
    -0.5755617245696528498312819507199E-25, \
    +0.1506191533639234250354144051199E-25, \
    -0.3954502959018796953104285695999E-26, \
    +0.1041529704151500979984645051733E-26, \
    -0.2751487795278765079450178901333E-27, \
    +0.7290058205497557408997703680000E-28, \
    -0.1936939645915947804077501098666E-28, \
    +0.5160357112051487298370054826666E-29, \
    -0.1378419322193094099389644800000E-29, \
    +0.3691326793107069042251093333333E-30, \
    -0.9909389590624365420653226666666E-31, \
    +0.2666491705195388413323946666666E-31 ] )

  erfccs = np.array ( [ \
    +0.715179310202924774503697709496E-01, \
    -0.265324343376067157558893386681E-01, \
    +0.171115397792085588332699194606E-02, \
    -0.163751663458517884163746404749E-03, \
    +0.198712935005520364995974806758E-04, \
    -0.284371241276655508750175183152E-05, \
    +0.460616130896313036969379968464E-06, \
    -0.822775302587920842057766536366E-07, \
    +0.159214187277090112989358340826E-07, \
    -0.329507136225284321486631665072E-08, \
    +0.722343976040055546581261153890E-09, \
    -0.166485581339872959344695966886E-09, \
    +0.401039258823766482077671768814E-10, \
    -0.100481621442573113272170176283E-10, \
    +0.260827591330033380859341009439E-11, \
    -0.699111056040402486557697812476E-12, \
    +0.192949233326170708624205749803E-12, \
    -0.547013118875433106490125085271E-13, \
    +0.158966330976269744839084032762E-13, \
    -0.472689398019755483920369584290E-14, \
    +0.143587337678498478672873997840E-14, \
    -0.444951056181735839417250062829E-15, \
    +0.140481088476823343737305537466E-15, \
    -0.451381838776421089625963281623E-16, \
    +0.147452154104513307787018713262E-16, \
    -0.489262140694577615436841552532E-17, \
    +0.164761214141064673895301522827E-17, \
    -0.562681717632940809299928521323E-18, \
    +0.194744338223207851429197867821E-18, \
    -0.682630564294842072956664144723E-19, \
    +0.242198888729864924018301125438E-19, \
    -0.869341413350307042563800861857E-20, \
    +0.315518034622808557122363401262E-20, \
    -0.115737232404960874261239486742E-20, \
    +0.428894716160565394623737097442E-21, \
    -0.160503074205761685005737770964E-21, \
    +0.606329875745380264495069923027E-22, \
    -0.231140425169795849098840801367E-22, \
    +0.888877854066188552554702955697E-23, \
    -0.344726057665137652230718495566E-23, \
    +0.134786546020696506827582774181E-23, \
    -0.531179407112502173645873201807E-24, \
    +0.210934105861978316828954734537E-24, \
    -0.843836558792378911598133256738E-25, \
    +0.339998252494520890627359576337E-25, \
    -0.137945238807324209002238377110E-25, \
    +0.563449031183325261513392634811E-26, \
    -0.231649043447706544823427752700E-26, \
    +0.958446284460181015263158381226E-27, \
    -0.399072288033010972624224850193E-27, \
    +0.167212922594447736017228709669E-27, \
    -0.704599152276601385638803782587E-28, \
    +0.297976840286420635412357989444E-28, \
    -0.126252246646061929722422632994E-28, \
    +0.539543870454248793985299653154E-29, \
    -0.238099288253145918675346190062E-29, \
    +0.109905283010276157359726683750E-29, \
    -0.486771374164496572732518677435E-30, \
    +0.152587726411035756763200828211E-30 ] )

  erfcs = np.array ( [ \
    -0.49046121234691808039984544033376E-01, \
    -0.14226120510371364237824741899631E+00, \
    +0.10035582187599795575754676712933E-01, \
    -0.57687646997674847650827025509167E-03, \
    +0.27419931252196061034422160791471E-04, \
    -0.11043175507344507604135381295905E-05, \
    +0.38488755420345036949961311498174E-07, \
    -0.11808582533875466969631751801581E-08, \
    +0.32334215826050909646402930953354E-10, \
    -0.79910159470045487581607374708595E-12, \
    +0.17990725113961455611967245486634E-13, \
    -0.37186354878186926382316828209493E-15, \
    +0.71035990037142529711689908394666E-17, \
    -0.12612455119155225832495424853333E-18, \
    +0.20916406941769294369170500266666E-20, \
    -0.32539731029314072982364160000000E-22, \
    +0.47668672097976748332373333333333E-24, \
    -0.65980120782851343155199999999999E-26, \
    +0.86550114699637626197333333333333E-28, \
    -0.10788925177498064213333333333333E-29, \
    +0.12811883993017002666666666666666E-31 ] )

  eta = 0.1 * r8_mach ( 3 )
  nterf = r8_inits ( erfcs, 21, eta )
  nterfc = r8_inits ( erfccs, 59, eta )
  nterc2 = r8_inits ( erc2cs, 49, eta )

  xsml = - np.sqrt ( - np.log ( sqrtpi * r8_mach ( 3 ) ) )
  xmax = np.sqrt (- np.log ( sqrtpi * r8_mach ( 1 ) ) )
  xmax = xmax - 0.5 * np.log ( xmax ) / xmax - 0.01
  sqeps = np.sqrt ( 2.0 * r8_mach ( 3 ) )

  if ( x <= xsml ):

    value = 2.0
    return value

  if ( xmax < x ):
    print ( '' )
    print ( 'r8_erfc - Warning!' )
    print ( '  X so big that ERFC underflows.' )
    value = 0.0
    return value

  y = abs ( x )

  if ( y < sqeps ):
    value = 1.0 - 2.0 * x / sqrtpi
    return value
  elif ( y <= 1.0 ):
    value = 1.0 - x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, erfcs, nterf ) )
    return value

  y = y * y

  if ( y <= 4.0 ):
    value = np.exp ( - y ) / abs ( x ) * ( 0.5 \
      + r8_csevl ( ( 8.0 / y - 5.0 ) / 3.0, erc2cs, nterc2 ) )
  else:
    value = np.exp ( - y ) / abs ( x ) * ( 0.5 \
      + r8_csevl ( 8.0 / y - 1.0, erfccs, nterfc ) )

  if ( x < 0.0 ):
    value = 2.0 - value

  return value

def r8_erfc_test ( ):

#*****************************************************************************80
#
## r8_erfc_test() tests r8_erfc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_erfc_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_erfc evaluates the complementary error function.' )
  print ( '' )
  print ( '             X         ERFC(X)  r8_erfc(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = erfc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_erfc ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_exp ( x ):

#*****************************************************************************80
#
## r8_exp() evaluates the exponential of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  aln216 = +0.83120654223414517758794896030274E-01

  expcs = np.array ( [ \
      +0.866569493314985712733404647266231E-01, \
      +0.938494869299839561896336579701203E-03, \
      +0.677603970998168264074353014653601E-05, \
      +0.366931200393805927801891250687610E-07, \
      +0.158959053617461844641928517821508E-09, \
      +0.573859878630206601252990815262106E-12, \
      +0.177574448591421511802306980226000E-14, \
      +0.480799166842372422675950244533333E-17, \
      +0.115716376881828572809260000000000E-19, \
      +0.250650610255497719932458666666666E-22, \
      +0.493571708140495828480000000000000E-25, \
      +0.890929572740634240000000000000000E-28, \
      +0.148448062907997866666666666666666E-30, \
      +0.229678916630186666666666666666666E-33 ] )

  twon16 = np.array ( [ \
      +0.0, \
      +0.44273782427413840321966478739929E-01, \
      +0.90507732665257659207010655760707E-01, \
      +0.13878863475669165370383028384151, \
      +0.18920711500272106671749997056047, \
      +0.24185781207348404859367746872659, \
      +0.29683955465100966593375411779245, \
      +0.35425554693689272829801474014070, \
      +0.41421356237309504880168872420969, \
      +0.47682614593949931138690748037404, \
      +0.54221082540794082361229186209073, \
      +0.61049033194925430817952066735740, \
      +0.68179283050742908606225095246642, \
      +0.75625216037329948311216061937531, \
      +0.83400808640934246348708318958828, \
      +0.91520656139714729387261127029583, \
      +1.0 ] )

  nterms = int ( r8_inits ( expcs, 14, 0.1 * r8_mach ( 3 ) ) )
  xmin = np.log ( r8_mach ( 1 ) ) + 0.01
  xmax = np.log ( r8_mach ( 2 ) ) - 0.001

  if ( x < xmin ):

    print ( '' )
    print ( 'r8_exp - Warning!' )
    print ( '  X so small that exp(X) underflows.' )
    value = 0.0

  elif ( x <= xmax ):

    xint = int ( np.fix ( x ) )
 
    y = x - xint

    y = 23.0 * y + x * aln216

    n = int ( np.fix ( y ) )

    f = y - n

    n = int ( np.fix ( 23.0 * xint + n ) )

    n16 = int ( np.fix ( n / 16 ) )
    if ( n < 0 ):
      n16 = n16 - 1
    ndx = n - 16 * n16 + 1
    if ( 17 < ndx ):
      ndx = 17

    value = 1.0 + ( twon16[ndx-1] + f * ( 1.0 + twon16[ndx-1] ) \
      * r8_csevl ( f, expcs, nterms ) )

    value = r8_pak ( value, n16 )

  else:

    print ( '' )
    print ( 'r8_exp - Fatal error!' )
    print ( '  X so large that exp(X) overflows.' )
    raise Exception ( 'r8_exp - Fatal error!' )

  return value

def r8_exp_test ( ):

#*****************************************************************************80
#
## r8_exp_test() tests r8_exp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_exp_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_exp evaluates the exponential function.' )
  print ( '' )
  print ( '             X          EXP(X)  r8_exp(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = exp_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_exp ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_fac ( n ):

#*****************************************************************************80
#
## r8_fac() evaluates the factorial of an I4 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    integer N, the argument.
#
#  Output:
#
#    real VALUE, the factorial of N.
#
  import numpy as np

  sq2pil = 0.91893853320467274178032973640562

  facn = np.array ( [ \
      +0.100000000000000000000000000000000E+01, \
      +0.100000000000000000000000000000000E+01, \
      +0.200000000000000000000000000000000E+01, \
      +0.600000000000000000000000000000000E+01, \
      +0.240000000000000000000000000000000E+02, \
      +0.120000000000000000000000000000000E+03, \
      +0.720000000000000000000000000000000E+03, \
      +0.504000000000000000000000000000000E+04, \
      +0.403200000000000000000000000000000E+05, \
      +0.362880000000000000000000000000000E+06, \
      +0.362880000000000000000000000000000E+07, \
      +0.399168000000000000000000000000000E+08, \
      +0.479001600000000000000000000000000E+09, \
      +0.622702080000000000000000000000000E+10, \
      +0.871782912000000000000000000000000E+11, \
      +0.130767436800000000000000000000000E+13, \
      +0.209227898880000000000000000000000E+14, \
      +0.355687428096000000000000000000000E+15, \
      +0.640237370572800000000000000000000E+16, \
      +0.121645100408832000000000000000000E+18, \
      +0.243290200817664000000000000000000E+19, \
      +0.510909421717094400000000000000000E+20, \
      +0.112400072777760768000000000000000E+22, \
      +0.258520167388849766400000000000000E+23, \
      +0.620448401733239439360000000000000E+24, \
      +0.155112100433309859840000000000000E+26, \
      +0.403291461126605635584000000000000E+27, \
      +0.108888694504183521607680000000000E+29, \
      +0.304888344611713860501504000000000E+30, \
      +0.884176199373970195454361600000000E+31, \
      +0.265252859812191058636308480000000E+33 ] )

  xmin, xmax = r8_gaml ( )
  nmax = int ( r8_aint ( xmax - 1.0 ) )

  if ( n < 0 ):

    print ( '' )
    print ( 'r8_fac - Fatal error!' )
    print ( '  Input argument is negative.' )
    raise Exception ( 'r8_fac - Fatal error!' )

  elif ( n <= 30 ):

    value = facn[n]

  elif ( n <= nmax ):

    x = float ( n + 1 )
    value = np.exp ( ( x - 0.5 ) * np.log ( x ) - x + sq2pil + r8_lgmc ( x ) )

  else:

    print ( '' )
    print ( 'r8_fac - Fatal error!' )
    print ( '  Factorial overflows.' )
    raise Exception ( 'r8_fac - Fatal error!' )

  return value

def r8_fac_test ( ):

#*****************************************************************************80
#
## r8_fac_test() tests r8_fac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_fac_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_fac evaluates the factorial function.' )
  print ( '' )
  print ( '             N          FAC(N)  r8_fac(N)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fx1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_fac ( n )

    print ( '  %14d  %14.6g  %14.6g  %14.6g' % ( n, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_factorial_values ( n_data ):

#*****************************************************************************80
#
## r8_factorial_values() returns values of the real factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) J
#
#    Although the factorial is an integer valued function, it quickly
#    becomes too large for an integer to hold.  This routine still accepts
#    an integer as the input argument, but returns the function value
#    as a real number.
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    real FN, the value of the function.
#
  import numpy as np

  n_max = 25

  fn_vec = np.array ( [ \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.6000000000000000E+01, \
     0.2400000000000000E+02, \
     0.1200000000000000E+03, \
     0.7200000000000000E+03, \
     0.5040000000000000E+04, \
     0.4032000000000000E+05, \
     0.3628800000000000E+06, \
     0.3628800000000000E+07, \
     0.3991680000000000E+08, \
     0.4790016000000000E+09, \
     0.6227020800000000E+10, \
     0.8717829120000000E+11, \
     0.1307674368000000E+13, \
     0.2092278988800000E+14, \
     0.3556874280960000E+15, \
     0.6402373705728000E+16, \
     0.1216451004088320E+18, \
     0.2432902008176640E+19, \
     0.1551121004333099E+26, \
     0.3041409320171338E+65, \
     0.9332621544394415E+158, \
     0.5713383956445855E+263 ] )

  n_vec = np.array ( [ \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def r8_factorial_values_test ( ):

#*****************************************************************************80
#
## r8_factorial_values_test() tests r8_factorial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_factorial_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_factorial_values() returns values of the real factorial function.' )
  print ( '' )
  print ( '          N          r8_factorial(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %14.6g' % ( n, fn ) )

  return

def r8_gamic ( a, x ):

#*****************************************************************************80
#
## r8_gamic() evaluates the complementary incomplete gamma function.
#
#  Discussion:
#
#    GAMIC = integral ( x <= t < oo ) exp(-t) * t^(a-1) dt
#
#    GAMIC is evaluated for arbitrary real values of A and non-negative
#    values X (even though GAMIC is defined for X < 0.0), except that
#    for X = 0 and A <= 0.0, GAMIC is undefined.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#    Walter Gautschi,
#    A Computational Procedure for Incomplete Gamma Functions,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 4, December 1979, pages 466-481.
#
#  Input:
#
#    real A, the parameter.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the value of the incomplete gamma function.
#
  import numpy as np

  eps = 0.5 * r8_mach ( 3 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )
  alneps = - np.log ( r8_mach ( 3 ) )
  bot = np.log ( r8_mach ( 1 ) )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'r8_gamic - Fatal error!' )
    print ( '  X < 0.' )
    raise Exception ( 'r8_gamic - Fatal error!' )

  if ( x == 0.0 ):

    if ( a <= 0.0 ):
      print ( '' )
      print ( 'r8_gamic - Fatal error!' )
      print ( '  X = 0 and A <= 0.' )
      raise Exception ( 'r8_gamic - Fatal error!' )

    value = np.exp ( r8_lngam ( a + 1.0 ) - np.log ( a ) )

    return value

  alx = np.log ( x )

  if ( a < 0.0 ):
    sga = - 1.0
  else:
    sga = + 1.0

  ainta = r8_aint ( a + 0.5 * sga )
  aeps = a - ainta

  izero = 0

  if ( x < 1.0 ):

    if ( a <= 0.5 and abs ( aeps ) <= 0.001 ):

      if ( - ainta <= 1.0 ):
        e = 2.0
      else:
        e = 2.0 * ( - ainta + 2.0 ) / ( ainta * ainta - 1.0 )

      e = e - alx * x ** ( - 0.001 )

      if ( e * abs ( aeps ) <= eps ):
        value = r8_gmic ( a, x, alx )
        return value

    algap1, sgngam = r8_lgams ( a + 1.0 )
    gstar = r8_gmit ( a, x, algap1, sgngam, alx )

    if ( gstar == 0.0 ):
      izero = 1
    else:
      alngs = np.log ( abs ( gstar ) )
      sgngs = r8_sign ( gstar )

  else:

    if ( a < x ):
      value = np.exp ( r8_lgic ( a, x, alx ) )
      return value

    sgngam = 1.0
    algap1 = r8_lngam ( a + 1.0 )
    sgngs = 1.0
    alngs = r8_lgit ( a, x, algap1 )

  h = 1.0

  if ( izero != 1 ):

    t = a * alx + alngs

    if ( alneps < t ):
      sgng = - sgngs * sga * sgngam
      t = t + algap1 - np.log ( abs ( a ) )
      value = sgng * np.exp ( t )
      return value

    if ( - alneps < t ):
      h = 1.0 - sgngs * np.exp ( t )

  sgng = r8_sign ( h ) * sga * sgngam
  t = np.log ( abs ( h ) ) + algap1 - np.log ( abs ( a ) )
  value = sgng * np.exp ( t )

  return value

def r8_gamic_test ( ):

#*****************************************************************************80
#
## r8_gamic_test() tests r8_gamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_gamic_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_gamic evaluates the incomplete Gamma function.' )
  print ( '' )
  print ( '             A               X     GAMIC(A,X)  r8_gamic(A,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx1 = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamic ( a, x )

    print ( '  %14.4g  %14.4f  %14.6g  %14.6g  %14.6g' \
      % ( a, x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_gmic ( a, x, alx ):

#*****************************************************************************80
#
## r8_gmic(): complementary incomplete gamma, small X, A near negative integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, the parameter.
#
#    real X, the argument.
#
#    real ALX, the logarithm of X.
#
#  Output:
#
#    real VALUE, the complementary incomplete gamma function.
#
  import numpy as np

  euler = 0.57721566490153286060651209008240

  eps = 0.5 * r8_mach ( 3 )
  bot = np.log ( r8_mach ( 1 ) )

  if ( 0.0 < a ):
    print ( '' )
    print ( 'r8_gmic - Fatal error!' )
    print ( '  A must be near a negative integer.' )
    raise Exception ( 'r8_gmic - Fatal error!' )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_gmic - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_gmic - Fatal error!' )

  m = - int ( r8_aint ( a - 0.5 ) )
  fm = float ( m )

  te = 1.0
  t = 1.0
  s = t
  converged = False

  for k in range ( 1, 201 ):

    fkp1 = float ( k + 1 )
    te = - x * te / ( fm + fkp1 )
    t = te / fkp1
    s = s + t

    if ( abs ( t ) < eps * s ):
      converged = True
      break

  if ( not converged ):
    print ( '' )
    print ( 'r8_gmic - Fatal error!' )
    print ( '  No convergence after 200 iterations.' )
    raise Exception ( 'r8_gmic - Fatal error!' )

  value = - alx - euler + x * s / ( fm + 1.0 )

  if ( m == 0 ):
    return value
  elif ( m == 1 ):
    value = - value - 1.0 + 1.0 / x
    return value

  te = fm
  t = 1.0
  s = t
  mm1 = m - 1

  for k in range ( 1, mm1 + 1 ):

    fk = float ( k )
    te = - x * te / fk
    t = te / ( fm - fk )
    s = s + t

    if ( abs ( t ) < eps * abs ( s ) ):
      break

  for k in range ( 1, m + 1 ):
    value = value + 1.0 / float ( k )

  if ( ( m % 2 ) == 1 ):
    sgng = - 1.0
  else:
    sgng = + 1.0

  alng = np.log ( value ) - r8_lngam ( fm + 1.0 )

  if ( bot < alng ):
    value = sgng * np.exp ( alng )
  else:
    value = 0.0

  if ( s != 0.0 ):
    value = value + abs ( np.exp ( - fm * alx + np.log ( abs ( s ) / fm ) ) ) * r8_sign ( s )

  return value

def r8_lgic ( a, x, alx ):

#*****************************************************************************80
#
## r8_lgic() evaluates the log complementary incomplete gamma function for large X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, the parameter.
#
#    real X, the argument.
#
#    real ALX, the logarithm of X.
#
#  Output:
#
#    real VALUE, the log complementary incomplete
#    gamma function.
#
  import numpy as np

  eps = 0.5 * r8_mach ( 3 )

  xpa = x + 1.0 - a
  xma = x - 1.0 - a

  r = 0.0
  p = 1.0
  s = p

  for k in range ( 1, 301 ):

    fk = float ( k )
    t = fk * ( a - fk ) * ( 1.0 + r )
    r = - t / ( ( xma + 2.0 * fk ) * ( xpa + 2.0 * fk ) + t )
    p = r * p
    s = s + p

    if ( abs ( p ) < eps * s ):
      value = a * alx - x + np.log ( s / xpa )
      return value

  print ( '' )
  print ( 'r8_lgic - Fatal error!' )
  print ( '  No convergence in 300 iterations.' )

  raise Exception ( 'r8_lgic - Fatal error!' )

def r8_lgit ( a, x, algap1 ):

#*****************************************************************************80
#
## r8_lgit() evaluates the log of Tricomi's incomplete gamma function.
#
#  Discussion:
#
#    Perron's continued fraction is used for large X and X <= A.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, the parameter.
#
#    real X, the argument.
#
#    real ALGAP1, the logarithm of the gamma function of A+1.
#
#  Output:
#
#    real VALUE, the log of Tricomi's incomplete gamma function.
#
  import numpy as np

  eps = 0.5 * r8_mach ( 3 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_lgit - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_lgit - Fatal error!' )

  if ( a < x ):
    print ( '' )
    print ( 'r8_lgit - Fatal error!' )
    print ( '  A < X.' )
    raise Exception ( 'r8_lgit - Fatal error!' )

  ax = a + x
  a1x = ax + 1.0
  r = 0.0
  p = 1.0
  s = p

  for k in range ( 1, 201 ):

    fk = float ( k )
    t = ( a + fk ) * x * ( 1.0 + r )
    r = t / ( ( ax + fk ) * ( a1x + fk ) - t )
    p = r * p
    s = s + p

    if ( abs ( p ) < eps * s ):
      hstar = 1.0 - x * s / a1x
      value = - x - algap1 - np.log ( hstar )
      return value

  print ( '' )
  print ( 'r8_lgit - Fatal error!' )
  print ( '  No convergence after 200 iterations.' )
  raise Exception ( 'r8_lgit - Fatal error!' )

def r8_gamit ( a, x ):

#*****************************************************************************80
#
## r8_gamit() evaluates Tricomi's incomplete gamma function for an R8 argument.
#
#  Discussion:
#
#      GAMIT = x^(-a) / gamma(a)
#        * Integral ( 0 <= t <= x ) exp(-t) * t^(a-1) dt
#
#    with analytic continuation for a <= 0.0.  Gamma(x) is the complete
#    gamma function of X.  GAMIT is evaluated for arbitrary real values of
#    A and for non-negative values of X (even though GAMIT is defined for
#    X < 0.0).
#
#    A slight deterioration of 2 or 3 digits accuracy will occur when
#    gamit is very large or very small in absolute value, because log-
#    arithmic variables are used.  Also, if the parameter A is very close
#    to a negative integer (but not a negative integer), there is a loss
#    of accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#    Walter Gautschi,
#    A Computational Procedure for Incomplete Gamma Functions,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 4, December 1979, pages 466-481.
#
#  Input:
#
#    real A, the parameter.
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  alneps = - np.log ( r8_mach ( 3 ) )
  sqeps = np.sqrt ( r8_mach ( 4 ) )
  bot = np.log ( r8_mach ( 1 ) )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'r8_gamit - Fatal error!' )
    print ( '  X is negative.' )
    raise Exception ( 'r8_gamit - Fatal error!' )
  elif ( x == 0.0 ):
    alx = 0.0
  else:
    alx = np.log ( x )

  if ( a < 0.0 ):
    sga = - 1.0
  else:
    sga = + 1.0

  ainta = r8_aint ( a + 0.5 * sga )
  aeps = a - ainta

  if ( x == 0.0 ):
    if ( 0.0 < ainta or aeps != 0.0 ):
      value = r8_gamr ( a + 1.0 )
    else:
      value = 0.0
    return value

  if ( x <= 1.0 ):
    if ( - 0.5 <= a or aeps != 0.0 ):
      algap1, sgngam = r8_lgams ( a + 1.0 )
    value = r8_gmit ( a, x, algap1, sgngam, alx )
    return value

  if ( x <= a ):
    t = r8_lgit ( a, x, r8_lngam ( a + 1.0 ) )
    value = np.exp ( t )
    return value

  alng = r8_lgic ( a, x, alx )
#
#  Evaluate in terms of log (r8_gamic (a, x))
#
  h = 1.0

  if ( aeps != 0.0 or 0.0 < ainta ):

    algap1, sgngam = r8_lgams ( a + 1.0 )
    t = np.log ( abs ( a ) ) + alng - algap1

    if ( alneps < t ):
      t = t - a * alx
      value = - sga * sgngam * np.exp ( t )
      return value

    if ( - alneps < t ):
      h = 1.0 - sga * sgngam * np.exp ( t )

  t = - a * alx + np.log ( abs ( h ) )

  if ( h < 0.0 ):
    value = - np.exp ( t )
  else:
    value = + np.exp ( t )

  return value

def r8_gamit_test ( ):

#*****************************************************************************80
#
## r8_gamit_test() tests r8_gamit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_gamit_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_gamit evaluates Tricomi\'s incomplete Gamma function' )
  print ( '' )
  print ( '             A               X     GAMIT(A,X)  r8_gamit(A,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx1 = gamma_inc_tricomi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamit ( a, x )

    print ( '  %14.4g  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_gmit ( a, x, algap1, sgngam, alx ):

#*****************************************************************************80
#
## r8_gmit(): Tricomi's incomplete gamma function for small X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, the parameter.
#
#    real X, the argument.
#
#    real ALGAP1, the logarithm of Gamma ( A + 1 ).
#
#    real SGNGAM, the sign of Gamma ( A + 1 ).
#
#    real ALX, the logarithm of X.
#
#  Output:
#
#    real VALUE, the Tricomi incomplete gamma function.
#
  import numpy as np

  eps = 0.5 * r8_mach ( 3 )
  bot = np.log ( r8_mach ( 1 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_gmit - Fatal error!' )
    print ( '  X <= 0.' )
    raise Exception ( 'r8_gmit - Fatal error!' )

  if ( a < 0.0 ):
    ma = int ( r8_aint ( a - 0.5 ) )
  else:
    ma = int ( r8_aint ( a + 0.5 ) )

  aeps = a - ma

  if ( a < - 0.5 ):
    ae = aeps
  else:
    ae = a

  t = 1.0
  te = ae
  s = t
  converged = False
  for k in range ( 1, 201 ):
    fk = float ( k )
    te = - x * te / fk
    t = te / ( ae + fk )
    s = s + t
    if ( abs ( t ) < eps * abs ( s ) ):
      converged = True
      break

  if ( not converged ):
    print ( '' )
    print ( 'r8_gmit - Fatal error!' )
    print ( '  No convergence in 200 iterations.' )
    raise Exception ( 'r8_gmit - Fatal error!' )

  if ( - 0.5 <= a ):
    algs = - algap1 + np.log ( s )
    value = np.exp ( algs )
    return value

  algs = - r8_lngam ( 1.0 + aeps ) + np.log ( s )
  s = 1.0
  m = - ma - 1
  t = 1.0
  for k in range ( 1, m + 1 ):
    t = x * t / ( aeps - ( m + 1 - k ) )
    s = s + t
    if ( abs ( t ) < eps * abs ( s ) ):
      break

  value = 0.0
  algs = - ma * np.log ( x ) + algs

  if ( s == 0.0 or aeps == 0.0 ):
    value = np.exp ( algs )
    return value

  sgng2 = sgngam * r8_sign ( s )
  alg2 = - x - algap1 + np.log ( abs ( s ) )

  if ( bot < alg2 ):
    value = sgng2 * np.exp ( alg2 )

  if ( bot < algs ):
    value = value + np.exp ( algs )

  return value

def r8_gaml ( ):

#*****************************************************************************80
#
## r8_gaml() evaluates bounds for an R8 argument of the gamma function.
#
#  Discussion:
#
#    This function calculates the minimum and maximum legal bounds
#    for X in the evaluation of GAMMA ( X ).
#
#    XMIN and XMAX are not the only bounds, but they are the only
#    non-trivial ones to calculate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Output:
#
#    real XMIN, XMAX, the bounds.
#
  import numpy as np
 
  alnsml = np.log ( r8_mach ( 1 ) )
  xmin = - alnsml

  for i in range ( 0, 10 ):

    xold = xmin
    xln = np.log ( xmin )
    xmin = xmin - xmin * ( ( xmin + 0.5 ) * xln - xmin \
      - 0.2258 + alnsml ) / ( xmin * xln + 0.5 )

    if ( abs ( xmin - xold ) < 0.005 ):

      xmin = - xmin + 0.01

      alnbig = np.log ( r8_mach ( 2 ) )
      xmax = alnbig

      for j in range ( 0, 10 ):

        xold = xmax
        xln = np.log ( xmax )
        xmax = xmax - xmax * ( ( xmax - 0.5 ) * xln - xmax \
          + 0.9189 - alnbig ) / ( xmax * xln - 0.5 )

        if ( abs ( xmax - xold ) < 0.005 ):
          xmax = xmax - 0.01
          xmin = max ( xmin, - xmax + 1.0 )
          return xmin, xmax

      print ( '' )
      print ( 'r8_gaml - Fatal error!' )
      print ( '  Unable to find XMAX.' )
      raise Exception ( 'r8_gaml - Fatal error!' )

  print ( '' )
  print ( 'r8_gaml - Fatal error!' )
  print ( '  Unable to find XMIN.' )
  raise Exception ( 'r8_gaml - Fatal error!' )

def r8_gaml_test ( ):

#*****************************************************************************80
#
## r8_gaml_test() tests r8_gaml().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_gaml_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_gaml returns bounds for the argument of the gamma function.' )

  xmin, xmax = r8_gaml ( )

  print ( '' )
  print ( '  Lower limit XMIN = %g' % ( xmin ) )
  print ( '  Upper limit XMAX = %g' % ( xmax ) )

  return

def r8_gamma ( x ):

#*****************************************************************************80
#
## r8_gamma() evaluates the gamma function of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sq2pil = 0.91893853320467274178032973640562

  gcs = np.array ( [ \
      +0.8571195590989331421920062399942E-02, \
      +0.4415381324841006757191315771652E-02, \
      +0.5685043681599363378632664588789E-01, \
      -0.4219835396418560501012500186624E-02, \
      +0.1326808181212460220584006796352E-02, \
      -0.1893024529798880432523947023886E-03, \
      +0.3606925327441245256578082217225E-04, \
      -0.6056761904460864218485548290365E-05, \
      +0.1055829546302283344731823509093E-05, \
      -0.1811967365542384048291855891166E-06, \
      +0.3117724964715322277790254593169E-07, \
      -0.5354219639019687140874081024347E-08, \
      +0.9193275519859588946887786825940E-09, \
      -0.1577941280288339761767423273953E-09, \
      +0.2707980622934954543266540433089E-10, \
      -0.4646818653825730144081661058933E-11, \
      +0.7973350192007419656460767175359E-12, \
      -0.1368078209830916025799499172309E-12, \
      +0.2347319486563800657233471771688E-13, \
      -0.4027432614949066932766570534699E-14, \
      +0.6910051747372100912138336975257E-15, \
      -0.1185584500221992907052387126192E-15, \
      +0.2034148542496373955201026051932E-16, \
      -0.3490054341717405849274012949108E-17, \
      +0.5987993856485305567135051066026E-18, \
      -0.1027378057872228074490069778431E-18, \
      +0.1762702816060529824942759660748E-19, \
      -0.3024320653735306260958772112042E-20, \
      +0.5188914660218397839717833550506E-21, \
      -0.8902770842456576692449251601066E-22, \
      +0.1527474068493342602274596891306E-22, \
      -0.2620731256187362900257328332799E-23, \
      +0.4496464047830538670331046570666E-24, \
      -0.7714712731336877911703901525333E-25, \
      +0.1323635453126044036486572714666E-25, \
      -0.2270999412942928816702313813333E-26, \
      +0.3896418998003991449320816639999E-27, \
      -0.6685198115125953327792127999999E-28, \
      +0.1146998663140024384347613866666E-28, \
      -0.1967938586345134677295103999999E-29, \
      +0.3376448816585338090334890666666E-30, \
      -0.5793070335782135784625493333333E-31 ] )

  ngcs = r8_inits ( gcs, 42, 0.1 * r8_mach ( 3 ) )
  xmin, xmax = r8_gaml ( )
  xsml = np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) ) + 0.01 )
  dxrel = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( y <= 10.0 ):

    n = int ( r8_aint ( x ) )

    if ( x < 0.0 ):
      n = n - 1

    y = x - n
    n = n - 1
    value = 0.9375 + r8_csevl ( 2.0 * y - 1.0, gcs, ngcs )

    if ( n == 0 ):

      return value

    elif ( n < 0 ):

      n = - n

      if ( x == 0.0 ):
        print ( '' )
        print ( 'r8_gamma - Fatal error!' )
        print ( '  X is 0.' )
        raise Exception ( 'r8_gamma - Fatal error!' )

      if ( x < 0.0 and x + n - 2 == 0.0 ):
        print ( '' )
        print ( 'r8_gamma - Fatal error!' )
        print ( '  X is a negative integer.' )
        raise Exception ( 'r8_gamma - Fatal error!' )


      if ( x < - 0.5 and abs ( ( x - r8_aint ( x - 0.5 ) ) / x ) < dxrel ):
        print ( '' )
        print ( 'r8_gamma - Warning!' )
        print ( '  X too near a negative integer,' )
        print ( '  answer is half precision.' )

      if ( y < xsml ):
        print ( '' )
        print ( 'r8_gamma - Fatal error!' )
        print ( '  X is so close to zero that Gamma overflows.' )
        raise Exception ( 'r8_gamma - Fatal error!' )

      for i in range ( 1, n + 1 ):
        value = value / ( x + i - 1 )

    elif ( n == 0 ):

      pass

    else:

      for i in range ( 1, n + 1 ):
        value = ( y + i ) * value

  else:

    if ( xmax < x ):
      print ( '' )
      print ( 'r8_gamma - Fatal error!' )
      print ( '  X so big that Gamma overflows.' )
      raise Exception ( 'r8_gamma - Fatal error!' )
#
#  Underflow.
#
    if ( x < xmin ):
      value = 0.0
      return value

    value = np.exp ( ( y - 0.5 ) * np.log ( y ) - y + sq2pil + r8_lgmc ( y ) )

    if ( 0.0 < x ):
      return value

    if ( abs ( ( x - r8_aint ( x - 0.5 ) ) / x ) < dxrel ):
      print ( '' )
      print ( 'r8_gamma - Warning!' )
      print ( '  X too near a negative integer,' )
      print ( '  answer is half precision.' )

    sinpiy = sin ( np.pi * y )

    if ( sinpiy == 0.0 ):
      print ( '' )
      print ( 'r8_gamma - Fatal error!' )
      print ( '  X is a negative integer.' )
      raise Exception ( 'r8_gamma - Fatal error!' )

    value = - np.pi / ( y * sinpiy * value )

  return value

def r8_gamma_test ( ):

#*****************************************************************************80
#
## r8_gamma_test() tests r8_gamma().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_gamma_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_gamma computes the Gamma function.' )
  print ( '' )
  print ( '             X        GAMMA(X)  r8_gamma(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_gamr ( x ):

#*****************************************************************************80
#
## r8_gamr() evaluates the reciprocal gamma function of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  if ( x <= 0.0 and r8_aint ( x ) == x ):

    value = 0.0

  elif ( abs ( x ) <= 10.0 ):

    value = 1.0 / r8_gamma ( x )

  else:

    alngx, sgngx = r8_lgams ( x )
    value = sgngx * np.exp ( - alngx )

  return value

def r8_gamr_test ( ):

#*****************************************************************************80
#
## r8_gamr_test() tests r8_gamr().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_gamr_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_gamr computes the 1/Gamma(x).' )
  print ( '' )
  print ( '             X      1/GAMMA(X)  r8_gamr(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, gx = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx1 = 1.0 / gx
    fx2 = r8_gamr ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_inits ( dos, nos, eta ):

#*****************************************************************************80
#
## r8_inits() initializes a Chebyshev series.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Input:
#
#    real DOS(NOS), the Chebyshev coefficients.
#
#    integer NOS, the number of coefficients.
#
#    real ETA, the desired accuracy.
#
#  Output:
#
#    integer VALUE, the number of terms of the series needed
#    to ensure the requested accuracy.
#
  if ( nos < 1 ):
    print ( '' )
    print ( 'r8_inits - Fatal error!' )
    print ( '  Number of coefficients < 1.' )
    raise Exception ( 'r8_inits - Fatal error!' )

  if ( eta < dos[nos-1] ):

    print ( '' )
    print ( 'r8_inits - Warning!' )
    print ( '  ETA may be too small.' )
    print ( '  The requested accuracy cannot be guaranteed' )
    print ( '  even if all available coefficients are used.' )
    value = nos

  else:

    err = 0.0

    for i in range ( nos - 1, -1, -1 ):
      value = i
      err = err + abs ( dos[value] )
      if ( eta < err ):
        break

  return value

def r8_inits_test ( ):

#*****************************************************************************80
#
## r8_inits_test() tests r8_inits().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  sincs = np.array ( [ \
    -0.374991154955873175839919279977323464E+00, \
    -0.181603155237250201863830316158004754E+00, \
    +0.005804709274598633559427341722857921E+00, \
    -0.000086954311779340757113212316353178E+00, \
    +0.000000754370148088851481006839927030E+00, \
    -0.000000004267129665055961107126829906E+00, \
    +0.000000000016980422945488168181824792E+00, \
    -0.000000000000050120578889961870929524E+00, \
    +0.000000000000000114101026680010675628E+00, \
    -0.000000000000000000206437504424783134E+00, \
    +0.000000000000000000000303969595918706E+00, \
    -0.000000000000000000000000371357734157E+00, \
    +0.000000000000000000000000000382486123E+00, \
    -0.000000000000000000000000000000336623E+00, \
    +0.000000000000000000000000000000000256E+00 ] )

  print ( '' )
  print ( 'r8_inits_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_inits determines the Chebyshev interpolant degree' )
  print ( '  necessary to guarantee a desired accuracy level.' )
  print ( '' )
  print ( '  Here, we use a 15 term Chebyshev expansion for the' )
  print ( '  sine function.' )
  print ( '' )
  print ( '  Accuracy    Terms Needed' )
  print ( '' )

  tol = 1.0
  for i in range ( 1, 19 ):
    n = r8_inits ( sincs, 15, tol )
    print ( '  %14.6g  %4d' % ( tol, n ) )
    tol = tol / 10.0

  return

def r8_int ( x ):

#*****************************************************************************80
#
## r8_int() returns the integer part of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  ibase = i4_mach ( 10 )
  xmax = 1.0 / r8_mach ( 4 )
  xbig = min ( i4_mach ( 9 ), xmax )
  expo = np.floor ( np.log ( xbig ) / np.log ( ibase ) - 0.5 )
  scale = ibase ** expo
  npart = np.floor ( np.log ( xmax ) / np.log ( scale ) + 1.0 )

  if ( x < - xmax ):

    value = x

  elif ( x < - xbig ):

    xscl = - x

    for i in range ( 0, npart ):
      xscl = xscl / scale

    value = 0.0
    for i in range ( 0, npart ):
      xscl = xscl * scale
      ipart = np.ceil ( xscl )
      part = ipart
      xscl = xscl - part
      value = value * scale + part

    value = - value

  elif ( x < 0 ):

    value = np.ceil ( x )

  elif ( x < + xbig ):

    value = np.floor ( x )

  elif ( x < + xmax ):

    xscl = x

    for i in range ( 0, npart ):
      xscl = xscl / scale

    value = 0.0
    for i in range ( 0, npart ):
      xscl = xscl * scale
      ipart = np.floor ( xscl )
      part = ipart
      xscl = xscl - part
      value = value * scale + part

  else:

    value = x

  return value

def r8_int_test ( ):

#*****************************************************************************80
#
## r8_int_test() tests r8_int().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_int_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_int computes the integer part of an R8.' )
  print ( '' )
  print ( '             X         INT(X)  r8_int(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_int ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_lbeta ( a, b ):

#*****************************************************************************80
#
## r8_lbeta() evaluates the logarithm of the beta function of R8 arguments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, B, the arguments.
#
#  Output:
#
#    real VALUE, the logarithm of the beta function of A
#    and B.
#
  import numpy as np

  sq2pil = 0.91893853320467274178032973640562

  p = min ( a, b )
  q = max ( a, b )

  if ( p <= 0.0 ):

    print ( '' )
    print ( 'r8_lbeta - Fatal error!' )
    print ( '  Both arguments must be greater than 0.' )
    raise Exception ( 'r8_lbeta - Fatal error!' )

  elif ( p < 10.0 and q <= 10.0 ):

    value = np.log ( r8_gamma ( p ) * ( r8_gamma ( q ) / r8_gamma ( p + q ) ) )

  elif ( p < 10.0 ):

    corr = r8_lgmc ( q ) - r8_lgmc ( p + q )

    value = r8_lngam ( p ) + corr + p - p * np.log ( p + q ) + \
      ( q - 0.5 ) * r8_lnrel ( - p / ( p + q ) )

  else:

    corr = r8_lgmc ( p ) + r8_lgmc ( q ) - r8_lgmc ( p + q )

    value = - 0.5 * np.log ( q ) + sq2pil + corr \
      + ( p - 0.5 ) * np.log ( p / ( p + q ) ) \
      + q * r8_lnrel ( - p / ( p + q ) )

  return value

def r8_lbeta_test ( ):

#*****************************************************************************80
#
## r8_lbeta_test() tests r8_lbeta().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_lbeta_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_lbeta evaluates the logarithm of the Beta function.' )
  print ( '' )
  print ( '             A               B     LBETA(A,B)  r8_lbeta(A,B)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx1 = beta_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_lbeta ( a, b )

    print ( '  %14.4f  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_lgams ( x ):

#*****************************************************************************80
#
## r8_lgams() evaluates the log of |gamma(x)| and sign, for an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real ALGAM, the logarithm of the absolute value of gamma ( X ).
#
#    real SGNGAM, the sign (+1 or -1 ) of gamma ( X ).
#
  import numpy as np

  algam = r8_lngam ( x )
  sgngam = 1.0

  if ( x <= 0.0 ):

    k = np.floor ( ( ( - r8_aint ( x ) ) % 2.0 ) + 0.1 )

    if ( k == 0 ):
      sgngam = - 1.0

  return algam, sgngam

def r8_lgams_test ( ):

#*****************************************************************************80
#
## r8_lgams_test() tests r8_lgams().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_lgams_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_lgams evaluates the sign of Gamma(x) and ' )
  print ( '  the logarithm of the absolute value of Gamma(x).' )
  print ( '' )
  print ( '             X        LNGAM(X)  Sign(Gamma(x))   Log(|Gamma(x)|)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, slngam = r8_lgams ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g' \
      % ( x, fx1, slngam, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_lgmc ( x ):

#*****************************************************************************80
#
## r8_lgmc() evaluates the log gamma correction factor for an R8 argument.
#
#  Discussion:
#
#    For 10 <= X, compute the log gamma correction factor so that
#
#      log ( gamma ( x ) ) = log ( sqrt ( 2 * pi ) )
#                          + ( x - 0.5 ) * log ( x ) - x
#                          + r8_lgmc ( x )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  algmcs = np.array ( [ \
      +0.1666389480451863247205729650822, \
      -0.1384948176067563840732986059135E-04, \
      +0.9810825646924729426157171547487E-08, \
      -0.1809129475572494194263306266719E-10, \
      +0.6221098041892605227126015543416E-13, \
      -0.3399615005417721944303330599666E-15, \
      +0.2683181998482698748957538846666E-17, \
      -0.2868042435334643284144622399999E-19, \
      +0.3962837061046434803679306666666E-21, \
      -0.6831888753985766870111999999999E-23, \
      +0.1429227355942498147573333333333E-24, \
      -0.3547598158101070547199999999999E-26, \
      +0.1025680058010470912000000000000E-27, \
      -0.3401102254316748799999999999999E-29, \
      +0.1276642195630062933333333333333E-30 ] )

  nalgm = r8_inits ( algmcs, 15, r8_mach ( 3 ) )
  xbig = 1.0 / np.sqrt ( r8_mach ( 3 ) )
  xmax = np.exp ( min ( np.log ( r8_mach ( 2 ) / 12.0 ), \
    - np.log ( 12.0 * r8_mach ( 1 ) ) ) )

  if ( x < 10.0 ):

    print ( '' )
    print ( 'r8_lgmc - Fatal error!' )
    print ( '  X must be at least 10.' )
    raise Exception ( 'r8_lgmc - Fatal error!' )

  elif ( x < xbig ):

    value = r8_csevl ( 2.0 * ( 10.0 / x ) * ( 10.0 / x ) - 1.0, algmcs, nalgm ) / x

  elif ( x < xmax ):

    value = 1.0 / ( 12.0 * x )

  else:

    value = 0.0

  return value

def r8_lgmc_test ( ):

#*****************************************************************************80
#
## r8_lgmc_test() tests r8_lgmc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_lgmc_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_lgmc evaluates the correction log gamma factor.' )
  print ( '  r8_lgmc(x) = log ( gamma ( x ) ) - log ( sqrt ( 2 * pi )' )
  print ( '    - ( x - 0.5 ) * log ( x ) + x' )
  print ( '' )
  print ( '             X        LGMC(X)  r8_lgmc(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, gamma_log = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break
#
#  Function requires 10 <= x.
#
    if ( 10.0 <= x ):
      fx1 = gamma_log - np.log ( np.sqrt ( 2.0 * np.pi ) ) \
        - ( x - 0.5 ) * np.log ( x ) + x
      fx2 = r8_lgmc ( x )
      print ( '  %14.4f  %14.6g  %14.6g  %14.6g' \
        % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_li ( x ):

#*****************************************************************************80
#
## r8_li() evaluates the logarithmic integral for an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sqeps = np.sqrt ( r8_mach ( 3 ) )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'r8_li - Fatal error!' )
    print ( '  Function undefined for X <= 0.' )
    raise Exception ( 'r8_li - Fatal error!' )

  if ( x == 0.0 ):
    value = 0.0
    return value

  if ( x == 1.0 ):
    print ( '' )
    print ( 'r8_li - Fatal error!' )
    print ( '  Function undefined for X = 1.' )
    raise Exception ( 'r8_li - Fatal error!' )

  if ( abs ( 1.0 - x ) < sqeps ):
    print ( '' )
    print ( 'r8_li - Warning!' )
    print ( '  Answer less than half precision.' )
    print ( '  X is too close to 1.' )

  value = r8_ei ( r8_log ( x ) )

  return value

def r8_li_test ( ):

#*****************************************************************************80
#
## r8_li_test() tests r8_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_li_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_li evaluates the logarithmic integral.' )
  print ( '' )
  print ( '             X           LI(X)  r8_li(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = logarithmic_integral_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_li ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_lngam ( x ):

#*****************************************************************************80
#
## r8_lngam() evaluates the log of the absolute value of gamma of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sq2pil = 0.91893853320467274178032973640562
  sqpi2l = +0.225791352644727432363097614947441

  xmax = r8_mach ( 2 ) / np.log ( r8_mach ( 2 ) )
  dxrel = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( y <= 10.0 ):
    value = np.log ( abs ( r8_gamma ( x ) ) )
    return value

  if ( xmax < y ):
    print ( '' )
    print ( 'r8_lngam - Fatal error!' )
    print ( '  Result overflows, |X| too big.' )
    raise Exception ( 'r8_lngam - Fatal error!' )

  if ( 0.0 < x ):
    value = sq2pil + ( x - 0.5 ) * np.log ( x ) - x + r8_lgmc ( y )
    return value

  sinpiy = abs ( np.sin ( np.pi * y ) )

  if ( sinpiy == 0.0 ):
    print ( '' )
    print ( 'r8_lngam - Fatal error!' )
    print ( '  X is a negative integer.' )
    raise Exception ( 'r8_lngam - Fatal error!' )

  value = sqpi2l + ( x - 0.5 ) * np.log ( y ) - x - np.log ( sinpiy ) - r8_lgmc ( y )

  if ( abs ( ( x - r8_aint ( x - 0.5 ) ) * value / x ) < dxrel ):
    print ( '' )
    print ( 'r8_lngam - Warning!' )
    print ( '  Result is half precision because' )
    print ( '  X is too near a negative integer.' )

  return value

def r8_lngam_test ( ):

#*****************************************************************************80
#
## r8_lngam_test() tests r8_lngam().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_lngam_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_lngam evaluates the logarithm of the Gamma function.' )
  print ( '' )
  print ( '             X        LNGAM(X)  r8_lngam(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_lngam ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_lnrel ( x ):

#*****************************************************************************80
#
## r8_lnrel() evaluates log ( 1 + X ) for an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  alnrcs = np.array ( [ \
      +0.10378693562743769800686267719098E+01, \
      -0.13364301504908918098766041553133, \
      +0.19408249135520563357926199374750E-01, \
      -0.30107551127535777690376537776592E-02, \
      +0.48694614797154850090456366509137E-03, \
      -0.81054881893175356066809943008622E-04, \
      +0.13778847799559524782938251496059E-04, \
      -0.23802210894358970251369992914935E-05, \
      +0.41640416213865183476391859901989E-06, \
      -0.73595828378075994984266837031998E-07, \
      +0.13117611876241674949152294345011E-07, \
      -0.23546709317742425136696092330175E-08, \
      +0.42522773276034997775638052962567E-09, \
      -0.77190894134840796826108107493300E-10, \
      +0.14075746481359069909215356472191E-10, \
      -0.25769072058024680627537078627584E-11, \
      +0.47342406666294421849154395005938E-12, \
      -0.87249012674742641745301263292675E-13, \
      +0.16124614902740551465739833119115E-13, \
      -0.29875652015665773006710792416815E-14, \
      +0.55480701209082887983041321697279E-15, \
      -0.10324619158271569595141333961932E-15, \
      +0.19250239203049851177878503244868E-16, \
      -0.35955073465265150011189707844266E-17, \
      +0.67264542537876857892194574226773E-18, \
      -0.12602624168735219252082425637546E-18, \
      +0.23644884408606210044916158955519E-19, \
      -0.44419377050807936898878389179733E-20, \
      +0.83546594464034259016241293994666E-21, \
      -0.15731559416479562574899253521066E-21, \
      +0.29653128740247422686154369706666E-22, \
      -0.55949583481815947292156013226666E-23, \
      +0.10566354268835681048187284138666E-23, \
      -0.19972483680670204548314999466666E-24, \
      +0.37782977818839361421049855999999E-25, \
      -0.71531586889081740345038165333333E-26, \
      +0.13552488463674213646502024533333E-26, \
      -0.25694673048487567430079829333333E-27, \
      +0.48747756066216949076459519999999E-28, \
      -0.92542112530849715321132373333333E-29, \
      +0.17578597841760239233269760000000E-29, \
      -0.33410026677731010351377066666666E-30, \
      +0.63533936180236187354180266666666E-31 ] )
  
  nlnrel = r8_inits ( alnrcs, 43, 0.1 * r8_mach ( 3 ) )
  xmin = - 1.0 + np.sqrt ( r8_mach ( 4 ) )

  if ( x <= - 1.0 ):
    print ( '' )
    print ( 'r8_lnrel - Fatal error!' )
    print ( '  X <= -1.' )
    raise Exception ( 'r8_lnrel - Fatal error!' )
  elif ( x < xmin ):
    print ( '' )
    print ( 'r8_lnrel - Warning!' )
    print ( '  Result is less than half precision.' )
    print ( '  X is too close to - 1.' )

  if ( abs ( x ) <= 0.375 ):
    value = x * ( 1.0 - x * r8_csevl ( x / 0.375, alnrcs, nlnrel ) )
  else:
    value = r8_log ( 1.0 + x )

  return value

def r8_lnrel_test ( ):

#*****************************************************************************80
#
## r8_lnrel_test() tests r8_lnrel().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_lnrel_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_lnrel evaluates  ln(1+X).' )
  print ( '' )
  print ( '             X          LN(1+X)  r8_lnrel(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = log_values ( n_data )

    if ( n_data == 0 ):
      break

    x = x - 1.0
    fx2 = r8_lnrel ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_log10 ( x ):

#*****************************************************************************80
#
## r8_log10() evaluates the logarithm, base 10, of an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  aloge = 0.43429448190325182765112891891661

  value = aloge * r8_log ( x )

  return value

def r8_log10_test ( ):

#*****************************************************************************80
#
## r8_log10_test() tests r8_log10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_log10_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_log10 evaluates the logarithm base 10.' )
  print ( '' )
  print ( '             X        LOG10(X)  r8_log10(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = log10_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_log10 ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_log ( x ):

#*****************************************************************************80
#
## r8_log() evaluates the logarithm of an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  aln2 = 0.06814718055994530941723212145818

  alncs = np.array ( [ \
      +0.13347199877973881561689386047187E+01, \
      +0.69375628328411286281372438354225E-03, \
      +0.42934039020450834506559210803662E-06, \
      +0.28933847795432594580466440387587E-09, \
      +0.20512517530340580901741813447726E-12, \
      +0.15039717055497386574615153319999E-15, \
      +0.11294540695636464284521613333333E-18, \
      +0.86355788671171868881946666666666E-22, \
      +0.66952990534350370613333333333333E-25, \
      +0.52491557448151466666666666666666E-28, \
      +0.41530540680362666666666666666666E-31 ] )

  center = np.array ( [ 1.0, 1.25, 1.50, 1.75 ] )

  alncen = np.array ( [ \
      +0.0, \
      +0.22314355131420975576629509030983, \
      +0.40546510810816438197801311546434, \
      +0.55961578793542268627088850052682, \
      +0.69314718055994530941723212145817 ] )

  nterms = r8_inits ( alncs, 11, 28.9 * r8_mach ( 3 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'r8_log - Fatal error!' )
    print ( '  X <= 0.0' )
    raise Exception ( 'r8_log - Fatal error!' )

  y, n = r8_upak ( x )

  xn = n - 1
  y = 2.0 * y
  ntrval = int ( r8_aint ( 4.0 * y - 2.5 ) )

  if ( ntrval == 5 ):
    t = ( ( y - 1.0 ) - 1.0 ) / ( y + 2.0 )
  elif ( ntrval < 5 ):
    t = ( y - center[ntrval-1] ) / ( y + center[ntrval-1] )

  t2 = t * t
  value = 0.625 * xn + ( aln2 * xn + alncen[ntrval-1] \
    + 2.0 * t + t * t2 \
    * r8_csevl ( 578.0 * t2 - 1.0, alncs, nterms ) )

  return value

def r8_log_test ( ):

#*****************************************************************************80
#
## r8_log_test() tests r8_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_log_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_log evaluates the logarithm.' )
  print ( '' )
  print ( '             X          LOG(X)  r8_log(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_log ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real r8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'r8_mop_test():' )
  print ( '  r8_mop() evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_MOP(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = +100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

  return

def r8_pak ( y, n ):

#*****************************************************************************80
#
## r8_pak() packs a base 2 exponent into an R8.
#
#  Discussion:
#
#    This routine is almost the inverse of r8_upak.  It is not exactly
#    the inverse, because abs ( x ) need not be between 0.5 and 1.0.
#    If both r8_pak and 2.0^n were known to be in range, we could compute
#    r8_pak = x * 2.0^n.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 216
#
#  Author:
#
#    This version by John Burkardt.
#
#  Input:
#
#    real Y, the mantissa.
#
#    integer N, the exponent.
#
#  Output:
#
#    real VALUE, the packed value.
#
  aln210 = 3.321928094887362347870319429489

  aln2b = 1.0
  if ( i4_mach ( 10 ) != 2 ):
    aln2b = r8_mach ( 5 ) * aln210
  nmin = aln2b * i4_mach ( 15 )
  nmax = aln2b * i4_mach ( 16 )

  value, ny = r8_upak ( y )

  nsum = n + ny

  if ( nsum < nmin ):
    print ( '' )
    print ( 'r8_pak - Warning!' )
    print ( '  Packed number underflows.' )
    value = 0.0
    return value

  if ( nmax < nsum ):
    print ( '' )
    print ( 'r8_pak - Fatal error!' )
    print ( '  Packed number overflows.' )
    raise Exception ( 'r8_pak - Fatal error!' )

  while ( nsum < 0 ):
    value = 0.5 * value
    nsum = nsum + 1

  while ( 0 < nsum ):
    value = 2.0 * value
    nsum = nsum - 1

  return value

def r8_pak_test ( ):

#*****************************************************************************80
#
## r8_pak_test() tests r8_pak().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_test = np.array ( [ 7, 8, 7, 7, 4, 0, -1, 0, 7, 2, 0 ] )

  y_test = np.array ( [ \
    0.5, \
    0.5, \
   -0.5, \
    0.75, \
    0.9375, \
    0.5, \
    0.5, \
    0.625, \
    0.5048828125, \
    0.7853981633974483, \
    0.0 ] )

  print ( '' )
  print ( 'r8_pak_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_pak converts a mantissa and base 2 exponent to an R8.' )
  print ( '' )
  print ( '    Mantissa     Exponent         R8' )
  print ( '' )

  for i in range ( 0, 11 ):

    y = y_test[i];
    n = n_test[i]

    x = r8_pak ( y, n )

    print ( '  %24.16g  %8d  %14.16g' % ( y, n, x ) )

  return

def r8_upak ( x ):

#*****************************************************************************80
#
## r8_upak() unpacks an R8 into a mantissa and exponent.
#
#  Discussion:
#
#    This function unpacks a floating point number x so that
#
#      x = y * 2.0^n
#
#    where
#
#      0.5 <= abs ( y ) < 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Input:
#
#    real X, the number to be unpacked.
#
#  Output:
#
#    real Y, the mantissa.
#
#    integer N, the exponent.
#
  absx = abs ( x )
  n = 0
  y = 0.0

  if ( x == 0.0 ):
    return y, n

  while ( absx < 0.5 ):
    n = n - 1
    absx = absx * 2.0

  while ( 1.0 <= absx ):
    n = n + 1
    absx = absx * 0.5

  if ( x < 0.0 ):
    y = - absx
  else:
    y = + absx

  return y, n

def r8_upak_test ( ):

#*****************************************************************************80
#
## r8_upak_test() tests r8_upak().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  x_test = np.array ( [ \
    64.0, \
   128.0, \
   -64.0, \
    96.0, \
    15.0, \
    0.5, \
    0.25, \
    0.625, \
   64.625, \
    3.141592653589793, \
    0.0 ] )

  print ( '' )
  print ( 'r8_upak_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_upak converts an R8 to a mantissa and base 2 exponent.' )
  print ( '' )
  print ( '             X         Mantissa     Exponent' )
  print ( '' )

  for i in range ( 0, 11 ):

    x = x_test[i];

    y, n = r8_upak ( x )

    print ( '  %24.16g  %24.16g  %8d' % ( x, y, n ) )

  return

def r8_poch ( a, x ):

#*****************************************************************************80
#
## r8_poch() evaluates Pochhammer's function of R8 arguments.
#
#  Discussion:
#
#    POCH ( A, X ) = Gamma ( A + X ) / Gamma ( A ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real A, X, the arguments.
#
#  Output:
#
#    real VALUE, the Pochhammer function of A and X.
#
  import numpy as np

  eps = r8_mach ( 4 )
  sqeps = np.sqrt ( eps )

  ax = a + x

  if ( ax <= 0.0 and r8_aint ( ax ) == ax ):

    if ( 0.0 < a or r8_aint ( a ) != a ):
      print ( '' )
      print ( 'r8_poch - Fatal error!' )
      print ( '  A + X is nonpositive integer,' )
      print ( '  but A is not.' )
      raise Exception ( 'r8_poch - Fatal error!' )
#
#  We know here that both A+X and A are non-positive integers.
#
    if ( x == 0.0 ):
      value = 1.0
    elif ( - 20.0 < min ( a + x, a ) ):
      n = int ( r8_aint ( x ) )
      ia = int ( r8_aint ( a ) )
      value = r8_mop ( n ) * r8_fac ( - ia ) / r8_fac ( - ia - n )
    else:
      n = int ( r8_aint ( x ) )
      value = r8_mop ( n ) * np.exp ( ( a - 0.5 ) \
        * r8_lnrel ( x / ( a - 1.0 ) ) \
        + x * np.log ( - a + 1.0 - x ) - x \
        + r8_lgmc ( - a + 1.0 ) \
        - r8_lgmc ( - a - x + 1.0 ) )

    return value
#
#  A + X is not zero or a negative integer.
#
  if ( a <= 0.0 and r8_aint ( a ) == a ):
    value = 0.0
    return value

  n = int ( abs ( r8_aint ( x ) ) )
#
#  X is a small non-positive integer, presummably a common case.
#
  if ( n == x and n <= 20 ):
    value = 1.0
    for i in range ( 0, n ):
      value = value * ( a + i )
    return value

  absax = abs ( a + x )
  absa = abs ( a )

  if ( max ( absax, absa ) <= 20.0 ):
    value = r8_gamma ( a + x ) * r8_gamr ( a )
    return value

  if ( 0.5 * absa < abs ( x ) ):
    alngax, sgngax = r8_lgams ( a + x )
    alnga, sgnga = r8_lgams ( a )
    value = sgngax * sgnga * np.exp ( alngax - alnga )
    return value
#
#  abs(x) is small and both abs(a+x) and abs(a) are large.  thus,
#  a+x and a must have the same sign.  for negative a, we use
#  gamma(a+x)/gamma(a) = gamma(-a+1)/gamma(-a-x+1) *
#  sin(pi*a)/sin(pi*(a+x))
#
  if ( a < 0.0 ):
    b = - a - x + 1.0
  else:
    b = a

  value = np.exp ( ( b - 0.5 ) * r8_lnrel ( x / b ) \
    + x * np.log ( b + x ) - x + r8_lgmc ( b + x ) - r8_lgmc ( b ) )

  if ( 0.0 <= a or value == 0.0 ):
    return value

  cospix = np.cos ( np.pi * x )
  sinpix = np.sin ( np.pi * x )
  cospia = np.cos ( np.pi * a )
  sinpia = np.sin ( np.pi * a )

  errpch = abs ( x ) * ( 1.0 + np.log ( b ) )
  den = cospix + cospia * sinpix / sinpia
  err = ( abs ( x ) * ( abs ( sinpix ) \
    + abs ( cospia * cospix / sinpia ) ) \
    + abs ( a * sinpix ) / sinpia / sinpia ) * pi
  err = errpch + err / abs ( den )

  value = value / den

  return value

def r8_poch_test ( ):

#*****************************************************************************80
#
## r8_poch_test() tests r8_poch().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_poch_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_poch evaluates the Pochhammer symbol.' )
  print ( '' )
  print ( '             A               X      POCH(A,X)  r8_poch(A,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, n, fx1 = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    x = n
    fx2 = r8_poch ( a, x )

    print ( '  %14.4g  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

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
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
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

def r8_psi_test ( ):

#*****************************************************************************80
#
## r8_psi_test() tests r8_psi().
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
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_psi_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_psi evaluates the PSI function.' )
  print ( '' )
  print ( '      X            PSI(X)    r8_psi(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_psi ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8_randgs ( xmean, sd, seed ):

#*****************************************************************************80
#
## r8_randgs() generates a normally distributed random number.
#
#  Discussion:
#
#    This function generate a normally distributed random number, that is,
#    it generates random numbers with a Gaussian distribution.  These
#    random numbers are not exceptionally good, especially in the tails
#    of the distribution, but this implementation is simple and suitable
#    for most applications.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Richard Hamming,
#    Numerical Methods for Scientists and Engineers,
#    Dover, 1986,
#    ISBN: 0486652416,
#    LC: QA297.H28.
#
#  Input:
#
#    real XMEAN, the mean of the Gaussian distribution.
#
#    real SD, the standard deviation of the
#    Gaussian function.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real VALUE, a normally distributed random number.
#
#    integer SEED, an updated seed.
#
  value = - 6.0
  for i in range ( 0, 12 ):
    r, seed = r8_ren ( seed )
    value = value + r

  value = xmean + sd * value

  return value, seed

def r8_randgs_test ( ):

#*****************************************************************************80
#
## r8_randgs_test() tests r8_randgs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3.0
  sd = 2.0
  seed = 123456789

  print ( '' )
  print ( 'r8_randgs_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_randgs is a normal random number generator.' )
  print ( '  Mean = %g' % ( m ) )
  print ( '  Standard Deviation = %g' % ( sd ) )
  print ( '' )
  print ( '             I         r8_randgs' )
  print ( '' )

  m2 = 0.0
  sd2 = 0.0

  for i in range ( 0, 1000 ):

    r, seed = r8_randgs ( m, sd, seed )
    m2 = m2 + r
    sd2 = sd2 + ( r - m ) ** 2
    if ( i <= 10 ):
      print ( '  %14d  %14g' % ( i, r ) )

  m2 = m2 / 1000.0
  sd2 = np.sqrt ( sd2 / 1000.0 )

  print ( '' )
  print ( '  Sequence mean =  %g' % ( m2 ) )
  print ( '  Sequence standard deviation = %g' % ( sd2 ) )

  return

def r8_random ( n, t, ix0, ix1 ):

#*****************************************************************************80
#
## r8_random() is a portable pseudorandom number generator.
#
#  Discussion:
#
#    This random number generator is portable amoung a wide variety of
#    computers.  It generates a random number between 0.0 and 1.0
#    according to the algorithm presented by Bays and Durham.
#
#    The motivation for using this scheme, which resembles the
#    Maclaren-Marsaglia method, is to greatly increase the period of the
#    random sequence.  If the period of the basic generator is P,
#    then the expected mean period of the sequence generated by this
#    generator is given by
#
#      new mean P = sqrt ( pi * factorial ( N ) / ( 8 * P ) ),
#
#    where factorial ( N ) must be much greater than P in this
#    asymptotic formula.  Generally, N should be 16 to maybe 32.
#
#  Modified:
#
#    09 May 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Carter Bays, Stephen Durham,
#    Improving a Poor Random Number Generator,
#    ACM Transactions on Mathematical Software,
#    Volume 2, Number 1, March 1976, pages 59-64.
#
#  Input:
#
#    integer N, the number of random numbers in an auxiliary table.  
#
#    real T(N+1), an array of random numbers, initialized
#    before first call by r8_random_init.
#
#    integer IX0, IX1, two parameters used
#    as seeds for the random number generator.
#
#  Output:
#
#    real T(N+1), an updated array of random numbers.
#
#    integer IX0, IX1, updated seeds for the random number generator.
#
#    real VALUE, a random number between 0.0 and 1.0.
#

#
#  Pick J, a random index between 1 and N, and return T(J).
#
  j = int ( t[n] * abs ( n ) )
  t[n] = t[j]
  value = t[j]
#
#  Put a new value into T(J).
#
  r = 0.0
  t[j], ix0, ix1 = r8_rand ( r, ix0, ix1 )

  return value, t, ix0, ix1

def r8_random_init ( n, t, ix0, ix1 ):

#*****************************************************************************80
#
## r8_random_init() initializes data for r8_random().
#
#  Discussion:
#
#    Before calling r8_random the first time, call r8_random_init
#    in order to initialize the T array.
#
#  Modified:
#
#    09 May 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Carter Bays, Stephen Durham,
#    Improving a Poor Random Number Generator,
#    ACM Transactions on Mathematical Software,
#    Volume 2, Number 1, March 1976, pages 59-64.
#
#  Input:
#
#    integer N, the number of random numbers in an auxiliary table.
#
#    real T(N+1), an array whose contents are unimportant.
#
#    integer IX0, IX1, two parameters used as seeds.  
#    On first call, these might both be set to 0.
#
#  Output:
#
#    real T(N+1), an updated array of random numbers.
#
#    integer IX0, IX1, updated seeds. 
#
  import numpy as np

  r = 0.0

  t = np.zeros ( n + 1 )

  for i in range ( 0, n + 1 ):
    t[i], ix0, ix1 = r8_rand ( r, ix0, ix1 )

  return t, ix0, ix1

def r8_random_test ( ):

#*****************************************************************************80
#
## r8_random_test() tests r8_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 32
  t = np.zeros ( n + 1 )
  i_value = np.array ( [ 1, 2, 3, 4, 10, 100, 1000 ] )

  print ( '' )
  print ( 'r8_random_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_random is a random number generator.' )
  print ( '' )
  print ( '             I         r8_random' )
  print ( '' )
#
#  Start the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  t, ix0, ix1 = r8_random_init ( n, t, ix0, ix1 )

  k = 0

  for i in range ( 1, 1001 ):

    r, t, ix0, ix1 = r8_random ( n, t, ix0, ix1 )

    if ( i == i_value[k] ):
      print ( '  %14d  %14.6g' % ( i, r ) )
      k = k + 1
#
#  Restart the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  t, ix0, ix1 = r8_random_init ( n, t, ix0, ix1 )

  average = 0.0
  for i in range ( 0, 1000001 ):
    r, t, ix0, ix1 = r8_random ( n, t, ix0, ix1 )
    average = average + r
  average = average / 1000000.0
  print ( '' )
  print ( '       Average =  %14g  %14g' % ( average, 0.5 ) )
#
#  Restart the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  [ t, ix0, ix1 ] = r8_random_init ( n, t, ix0, ix1 )

  variance = 0.0
  for i in range ( 0, 1000001 ):
    r, t, ix0, ix1 = r8_random ( n, t, ix0, ix1 )
    variance = variance + ( r - average ) ** 2
  variance = variance / 1000000.0
  print ( '       Variance = %14g  %14g' % ( variance, 1.0 / 12.0 ) )

  return

def r8_rand ( r, ix0, ix1 ):

#*****************************************************************************80
#
## r8_rand() is a portable pseudorandom number generator.
#
#  Discussion:
#
#    This pseudo-random number generator is portable amoung a wide
#    variety of computers.  It is undoubtedly not as good as many
#    readily available installation dependent versions, and so this
#    routine is not recommended for widespread usage.  Its redeeming
#    feature is that the exact same random numbers (to within final round-
#    off error) can be generated from machine to machine.  Thus, programs
#    that make use of random numbers can be easily transported to and
#    checked in a new environment.
#
#    The random numbers are generated by the linear congruential
#    method described by Knuth in seminumerical methods (p.9),
#    addison-wesley, 1969.  Given the i-th number of a pseudo-random
#    sequence, the i+1 -st number is generated from
#      x(i+1) = (a*x(i) + c) mod m,
#    where here m = 2^22 = 4194304, c = 1731 and several suitable values
#    of the multiplier a are discussed below.  Both the multiplier a and
#    random number x are represented in real as two 11-bit
#    words.  The constants are chosen so that the period is the maximum
#    possible, 4194304.
#
#    In order that the same numbers be generated from machine to
#    machine, it is necessary that 23-bit integers be reducible modulo
#    2^11 exactly, that 23-bit integers be added exactly, and that 11-bit
#    integers be multiplied exactly.  Furthermore, if the restart option
#    is used (where r is between 0 and 1), then the product r*2^22 =
#    r*4194304 must be correct to the nearest integer.
#
#    The first four random numbers should be
#
#      0.0004127026,
#      0.6750836372,
#      0.1614754200,
#      0.9086198807.
#
#    The tenth random number is
#
#      0.5527787209.
#
#    The hundredth random number is
#
#      0.3600893021.
#
#    The thousandth number should be
#
#      0.2176990509.
#
#    In order to generate several effectively independent sequences
#    with the same generator, it is necessary to know the random number
#    for several widely spaced calls.  The I-th random number times 2^22,
#    where I=K*P/8 and P is the period of the sequence (P = 2^22), is
#    still of the form L*P/8.  In particular we find the I-th random
#    number multiplied by 2^22 is given by
#      I   =  0  1*p/8  2*p/8  3*p/8  4*p/8  5*p/8  6*p/8  7*p/8  8*p/8
#      RAND=  0  5*p/8  2*p/8  7*p/8  4*p/8  1*p/8  6*p/8  3*p/8  0
#    thus the 4*P/8 = 2097152 random number is 2097152/2**22.
#
#    Several multipliers have been subjected to the spectral test
#    (see Knuth, p. 82).  Four suitable multipliers roughly in order of
#    goodness according to the spectral test are
#      3146757 = 1536*2048 + 1029 = 2^21 + 2^20 + 2^10 + 5
#      2098181 = 1024*2048 + 1029 = 2^21 + 2^10 + 5
#      3146245 = 1536*2048 +  517 = 2^21 + 2^20 + 2^9 + 5
#      2776669 = 1355*2048 + 1629 = 5^9 + 7^7 + 1
#
#    In the table below log10(NU(I)) gives roughly the number of
#    random decimal digits in the random numbers considered I at a time.
#    C is the primary measure of goodness.  In both cases bigger is better.
#
#                     log10 nu(i)              c(i)
#         a       i=2  i=3  i=4  i=5    i=2  i=3  i=4  i=5
#
#      3146757    3.3  2.0  1.6  1.3    3.1  1.3  4.6  2.6
#      2098181    3.3  2.0  1.6  1.2    3.2  1.3  4.6  1.7
#      3146245    3.3  2.2  1.5  1.1    3.2  4.2  1.1  0.4
#      2776669    3.3  2.1  1.6  1.3    2.5  2.0  1.9  2.6
#     best
#      possible   3.3  2.3  1.7  1.4    3.6  5.9  9.7  14.9
#
#    Note that the original version of this routine used local static
#    variables IX0 and IX1.  In this revised version, IX0 and IX1 are
#    routine arguments.  To duplicate the behavior of the original code,
#    IX0 and IX1 should be set to zero before the first call.  
#    JVB, 04 May 2016.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 May 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Input:
#
#    real R, determines the action.
#    * R = 0.0, the next random number of the sequence is generated.
#    * R < 0.0, the last generated number will be returned for
#    possible use in a restart procedure.
#    * R > 0.0, the sequence of random numbers will start with the
#    seed ( R mod 1 ).  This seed is also returned as the value of
#    r8_rand provided the arithmetic is done exactly.
#
#    integer IX0, IX1, two parameters used
#    as seeds for the random number generator.  On first call, these
#    might both be set to 0.
#
#  Output:
#
#    real VALUE, a pseudo-random number between
#    0.0 and 1.0.
#
#    integer IX0, IX1, updated seed values.
#
  ia0 = 1029
  ia1 = 1536
  ia1ma0 = 507
  ic = 1731

  if ( r == 0.0 ):
    iy0 = ia0 * ix0
    iy1 = ia1 * ix1 + ia1ma0 * ( ix0 - ix1 ) + iy0
    iy0 = iy0 + ic
    ix0 = ( iy0 % 2048 )
    iy1 = iy1 + ( iy0 - ix0 ) // 2048
    ix1 = ( iy1 % 2048 )

  if ( 0.0 < r ):
    ix1 = int ( ( r % 1.0 ) * 4194304.0 + 0.5 )
    ix0 = ( ix1 % 2048 )
    ix1 = ( ix1 - ix0 ) // 2048

  value = float ( ix1 * 2048 + ix0 )
  value = value / 4194304.0

  return value, ix0, ix1

def r8_rand_test ( ):

#*****************************************************************************80
#
## r8_rand_test() tests r8_rand().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i_value = np.array ( [ 1, 2, 3, 4, 10, 100, 1000 ] )

  r_value = np.array ( [ \
    0.0004127026, \
    0.6750836372, \
    0.1614754200, \
    0.9086198807, \
    0.5527787209, \
    0.3600893021, \
    0.2176990509 ] )

  print ( '' )
  print ( 'r8_rand_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_rand is a random number generator.' )
  print ( '' )
  print ( '             I         r8_rand        Expected' )
  print ( '' )
#
#  Start the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  s = 0.0

  k = 0

  for i in range ( 0, 1000 ):

    r, ix0, ix1 = r8_rand ( s, ix0, ix1 )

    if ( i + 1 == i_value[k] ):
      print ( '  %14d  %14.6g  %14.6g' % ( i + 1, r, r_value[k] ) )
      k = k + 1
#
#  Restart the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  s = 0.0

  average = 0.0
  for i in range ( 0, 1000000 ):
    r, ix0, ix1 = r8_rand ( s, ix0, ix1 )
    average = average + r
  average = average / 1000000.0
  print ( '' )
  print ( '       Average =  %14g  %14g' % ( average, 0.5 ) )
#
#  Restart the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  s = 0.0

  variance = 0.0
  for i in range ( 0, 1000000 ):
    r, ix0, ix1 = r8_rand ( s, ix0, ix1 )
    variance = variance + ( r - average ) ** 2
  variance = variance / 1000000.0
  print ( '       Variance = %14g  %14g' % ( variance, 1.0 / 12.0 ) )

  return

def r8_ren ( seed ):

#*****************************************************************************80
#
## r8_ren() is a simple random number generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    This version by John Burkardt.
#
#  Reference:
#
#    Malcolm Pike, David Hill,
#    Algorithm 266:
#    Pseudo-Random Numbers,
#    Communications of the ACM,
#    Volume 8, Number 10, October 1965, page 605.
#
#  Input:
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real VALUE, the random value.
#
#    integer SEED, an updated seed.
#
  i4_huge = 2147483647
  seed = ( seed % ( i4_huge // 125 ) )
  seed = seed * 125
  seed = seed - ( seed // 2796203 ) * 2796203
  value = seed / 2796203.0

  return value, seed

def r8_ren_test ( ):

#*****************************************************************************80
#
## r8_ren_test() tests r8_ren().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i_value = np.array ( [ 1, 2, 3, 4, 10, 100, 1000 ] )

  r_value = np.array ( [ \
    0.470393E+00, \
    0.799066E+00, \
    0.883261E+00, \
    0.407667E+00, \
    0.955566E+00, \
    0.173576E+00, \
    0.121733E-01 ] )

  print ( '' )
  print ( 'r8_ren_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_ren is a random number generator.' )
  print ( '' )
  print ( '             I         r8_ren         Expected' )
  print ( '' )

  seed = 100001
  k = 0
  for i in range ( 1, 1001 ):

    r, seed = r8_ren ( seed )

    if ( i == i_value[k] ):
      print ( '  %14d  %14.6g  %14.6g' % ( i, r, r_value[k] ) )
      k = k + 1

  seed = 100001
  average = 0.0
  for i in range ( 1, 1000000 ):
    r, seed = r8_ren ( seed )
    average = average + r
  average = average / 1000000.0
  print ( '' )
  print ( '       Average =  %14.6g  %14.6g' % ( average, 0.5 ) )

  seed = 100001
  variance = 0.0
  for i in range ( 1, 1000000 ):
    r, seed = r8_ren ( seed )
    variance = variance + ( r - average ) ** 2
  variance = variance / 1000000.0
  print ( '       Variance = %14.6g  %14.6g' % ( variance, 1.0 / 12.0 ) )

  return

def r8_rise_values ( n_data ):

#*****************************************************************************80
#
## r8_rise_values() returns values of the rising factorial function.
#
#  Discussion:
#
#    The rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) \ * ( m - 1 + n )
#            = Gamma ( m + n ) / Gamma ( m )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      Pochhammer[m,n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 December 2014
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, integer N, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( [ 
       1680.000000000000, \
       1962.597656250000, \
       2279.062500000000, \
       2631.972656250000, \
       3024.000000000000, \
       1.000000000000000, \
       7.500000000000000, \
       63.75000000000000, \
       605.6250000000000, \
       6359.062500000000, \
       73129.21875000000, \
       914115.2343750000, \
       1.234055566406250E+07, \
       1.789380571289063E+08, \
       2.773539885498047E+09 ] )

  n_vec = np.array ( [ 
       4, \
       4, \
       4, \
       4, \
       4, \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9 ] )

  x_vec = np.array ( [ 
       5.00, \
       5.25, \
       5.50, \
       5.75, \
       6.00, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    n = 0
    f = 0.0
  else:
    x = x_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, n, f

def r8_rise_values_test ( ):

#*****************************************************************************80
#
## r8_rise_values_test() tests r8_rise_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_rise_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_rise_values() returns values of the rising factorial.' )
  print ( '' )
  print ( '          X         N          r8_rise(X,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, n, f = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8.4f  %8d  %24.16g' % ( x, n, f ) )

  return

def r8_shi ( x ):

#*****************************************************************************80
#
## r8_shi() evaluates the hyperbolic sine integral Shi of an R8 argument.
#
#  Discussion:
#
#    Shi ( x ) = Integral ( 0 <= t <= x ) sinh ( t ) dt / t
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  shics = np.array ( [ \
      0.0078372685688900950695200984317332, \
      0.0039227664934234563972697574427225, \
      0.0000041346787887617266746747908275, \
      0.0000000024707480372882742135145302, \
      0.0000000000009379295590763630457157, \
      0.0000000000000002451817019520867353, \
      0.0000000000000000000467416155257592, \
      0.0000000000000000000000067803072389, \
      0.0000000000000000000000000007731289, \
      0.0000000000000000000000000000000711 ] )

  nshi = r8_inits ( shics, 10, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( r8_mach ( 3 ) )

  absx = abs ( x )

  if ( absx <= xsml ):
    value = x
  elif ( absx <= 0.375 ):
    value = x * ( 1.0 + r8_csevl ( 128.0 * x * x / 9.0 - 1.0, shics, nshi ) )
  else:
    value = 0.5 * ( r8_ei ( x ) + r8_e1 ( x ) )

  return value

def r8_shi_test ( ):

#*****************************************************************************80
#
## r8_shi_test() tests r8_shi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8_shi_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_shi evaluates the hyperbolic sine integral.' )
  print ( '' )
  print ( '             X          SHI(X)  r8_shi(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = shi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_shi ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sign returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )

  return

def r8_sin_deg ( x ):

#*****************************************************************************80
#
## r8_sin_deg() evaluates the sine of an R8 argument in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  raddeg = 0.017453292519943295769236907684886

  value = r8_sin ( raddeg * x )

  if ( ( x % 90.0 ) == 0.0 ):

    n = np.floor ( abs ( x ) / 90.0 + 0.5 )
    n = ( n % 2 )

    if ( n == 0 ):
      value = 0.0
    elif ( value < 0.0 ):
      value = - 1.0
    else:
      value = + 1.0

  return value

def r8_sin_deg_test ( ):

#*****************************************************************************80
#
## r8_sin_deg_test() tests r8_sin_deg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_sin_deg_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sin_deg evaluates the sine of an argument in degrees.' )
  print ( '' )
  print ( '             X     sin_deg(X)  r8_sin_deg(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = sin_degree_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_sin_deg ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_sinh ( x ):

#*****************************************************************************80
#
## r8_sinh() evaluates the hyperbolic sine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sinhcs = np.array ( [ \
      +0.17304219404717963167588384698501, \
      +0.87594221922760477154900263454440E-01, \
      +0.10794777745671327502427270651579E-02, \
      +0.63748492607547504815685554571850E-05, \
      +0.22023664049230530159190496019502E-07, \
      +0.49879401804158493149425807203661E-10, \
      +0.79730535541157304814411480441186E-13, \
      +0.94731587130725443342927317226666E-16, \
      +0.86934920504480078871023098666666E-19, \
      +0.63469394403318040457397333333333E-22, \
      +0.37740337870858485738666666666666E-25, \
      +0.18630213719570056533333333333333E-28, \
      +0.77568437166506666666666666666666E-32 ] )

  nterms = r8_inits ( sinhcs, 13, 0.1 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( 6.0 * r8_mach ( 3 ) )
  ymax = 1.0 / np.sqrt ( r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= sqeps ):

    value = x

  elif ( y <= 1.0 ):

    value = x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, sinhcs, nterms ) )

  else:

    y = np.exp ( y )

    if ( ymax <= y ):
      value = 0.5 * y
    else:
      value = 0.5 * ( y - 1.0 / y )

    if ( x < 0.0 ):
      value = - value

  return value

def r8_sinh_test ( ):

#*****************************************************************************80
#
## r8_sinh_test() tests r8_sinh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_sinh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sinh evaluates the hyperbolic sine function.' )
  print ( '' )
  print ( '             X         SINH(X)  r8_sinh(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = sinh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_sinh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_sin ( x ):

#*****************************************************************************80
#
## r8_sin() evaluates the sine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  pi2rec = 0.63661977236758134307553505349006
  pihi = 3.140625
  pilo = 9.6765358979323846264338327950288E-04
  pirec = 0.31830988618379067153776752674503

  sincs = np.array ( [ \
     -0.374991154955873175839919279977323464, \
     -0.181603155237250201863830316158004754, \
     +0.005804709274598633559427341722857921, \
     -0.000086954311779340757113212316353178, \
     +0.000000754370148088851481006839927030, \
     -0.000000004267129665055961107126829906, \
     +0.000000000016980422945488168181824792, \
     -0.000000000000050120578889961870929524, \
     +0.000000000000000114101026680010675628, \
     -0.000000000000000000206437504424783134, \
     +0.000000000000000000000303969595918706, \
     -0.000000000000000000000000371357734157, \
     +0.000000000000000000000000000382486123, \
     -0.000000000000000000000000000000336623, \
     +0.000000000000000000000000000000000256 ] )

  ntsn = r8_inits ( sincs, 15, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 2.0 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xwarn = np.sqrt ( xmax )

  y = abs ( x )

  if ( xmax < y ):
    print ( '' )
    print ( 'r8_sin - Warning!' )
    print ( '  No precision because |X| is big.' )
    value = 0.0
    return value

  if ( xwarn < y ):
    print ( '' )
    print ( 'r8_sin - Warning!' )
    print ( '  Answer < half precision because |X| is big.' )

  value = x

  if ( y < xsml ):
    return value

  xn = r8_aint ( y * pirec + 0.5 )
  n2 = r8_aint ( ( xn % 2.0 ) + 0.5 )

  sgn = x

  if ( n2 != 0 ):
    sgn = - sgn

  f = ( y - xn * pihi ) - xn * pilo

  xn = 2.0 * ( f * pi2rec ) * ( f * pi2rec ) - 1.0

  value = f + f * r8_csevl ( xn, sincs, ntsn )

  if ( sgn < 0.0 ):
    value = - value

  if ( value < - 1.0 ):
    value = - 1.0
  elif ( 1.0 < value ):
    value = + 1.0

  return value

def r8_sin_test ( ):

#*****************************************************************************80
#
## r8_sin_test() tests r8_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_sin_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sin evaluates the sine function.' )
  print ( '' )
  print ( '             X         SIN(X)  r8_sin(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = sin_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_sin ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_spence ( x ):

#*****************************************************************************80
#
## r8_spence() evaluates a form of Spence's function for an R8 argument.
#
#  Discussion:
#
#    This function evaluates a form of Spence's function defined by
#
#      f(x) = Integral ( 0 <= y <= x ) - log ( abs ( 1 - y ) ) / y dy
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions, page 1004,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
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
#    K Mitchell,
#    Tables of the function Integral ( 0 < y < x ) - log | 1 - y | dy / y
#    with an account of some properties of this and related functions,
#    Philosophical Magazine,
#    Volume 40, pages 351-368, 1949.
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  pi26 = +1.644934066848226436472415166646025189219

  spencs = np.array ( [ \
      +0.1527365598892405872946684910028, \
      +0.8169658058051014403501838185271E-01, \
      +0.5814157140778730872977350641182E-02, \
      +0.5371619814541527542247889005319E-03, \
      +0.5724704675185826233210603054782E-04, \
      +0.6674546121649336343607835438589E-05, \
      +0.8276467339715676981584391689011E-06, \
      +0.1073315673030678951270005873354E-06, \
      +0.1440077294303239402334590331513E-07, \
      +0.1984442029965906367898877139608E-08, \
      +0.2794005822163638720201994821615E-09, \
      +0.4003991310883311823072580445908E-10, \
      +0.5823462892044638471368135835757E-11, \
      +0.8576708692638689278097914771224E-12, \
      +0.1276862586280193045989483033433E-12, \
      +0.1918826209042517081162380416062E-13, \
      +0.2907319206977138177795799719673E-14, \
      +0.4437112685276780462557473641745E-15, \
      +0.6815727787414599527867359135607E-16, \
      +0.1053017386015574429547019416644E-16, \
      +0.1635389806752377100051821734570E-17, \
      +0.2551852874940463932310901642581E-18, \
      +0.3999020621999360112770470379519E-19, \
      +0.6291501645216811876514149171199E-20, \
      +0.9933827435675677643803887752533E-21, \
      +0.1573679570749964816721763805866E-21, \
      +0.2500595316849476129369270954666E-22, \
      +0.3984740918383811139210663253333E-23, \
      +0.6366473210082843892691326293333E-24, \
      +0.1019674287239678367077061973333E-24, \
      +0.1636881058913518841111074133333E-25, \
      +0.2633310439417650117345279999999E-26, \
      +0.4244811560123976817224362666666E-27, \
      +0.6855411983680052916824746666666E-28, \
      +0.1109122433438056434018986666666E-28, \
      +0.1797431304999891457365333333333E-29, \
      +0.2917505845976095173290666666666E-30, \
      +0.4742646808928671061333333333333E-31 ] )

  nspenc = r8_inits ( spencs, 38, 0.1 * r8_mach ( 3 ) )
  xbig = 1.0 / r8_mach ( 3 )

  if ( x <= - xbig ):

    aln = np.log ( 1.0 - x )
    value = - pi26  - 0.5 * aln * ( 2.0 * np.log ( - x ) - aln )

  elif ( x <= - 1.0 ):

    aln = np.log ( 1.0 - x )

    value = - pi26 - 0.5 * aln * ( 2.0 \
      * np.log ( - x ) - aln ) + ( 1.0 + r8_csevl ( \
      4.0 / ( 1.0 - x ) - 1.0, spencs, nspenc ) ) / ( 1.0 - x )

  elif ( x <= 0.0 ):

    value = - 0.5 * np.log ( 1.0 - x ) \
      * np.log ( 1.0 - x ) - x * ( 1.0 + r8_csevl ( \
      4.0 * x / ( x - 1.0 ) - 1.0, spencs, nspenc ) ) \
      / ( x - 1.0 )

  elif ( x <= 0.5 ):

    value = x * ( 1.0 + r8_csevl ( 4.0 * x - 1.0, spencs, nspenc ) )

  elif ( x < 1.0 ):

    value = pi26 - np.log ( x ) * np.log ( 1.0 - x ) \
      - ( 1.0 - x ) * ( 1.0 + r8_csevl ( 4.0 \
      * ( 1.0 - x ) - 1.0, spencs, nspenc ) )

  elif ( x == 1.0 ):

    value = pi26

  elif ( x <= 2.0 ):

    value = pi26 - 0.5 * np.log ( x ) \
      * np.log ( ( x - 1.0 ) * ( x - 1.0 ) / x ) \
      + ( x - 1.0 ) * ( 1.0 + r8_csevl ( 4.0 \
      * ( x - 1.0 ) / x - 1.0, spencs, nspenc ) ) / x

  elif ( x < xbig ):

    value = 2.0 * pi26 - 0.5 * np.log ( x ) * np.log ( x ) \
      - ( 1.0 + r8_csevl ( 4.0 / x - 1.0, spencs, \
      nspenc ) ) / x

  else:

    value = 2.0 * pi26 - 0.5 * np.log ( x ) * np.log ( x )

  return value

def r8_spence_test ( ):

#*****************************************************************************80
#
## r8_spence_test() tests r8_spence().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_spence_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_spence evaluates Spence\'s integral.' )
  print ( '' )
  print ( '             X       SPENCE(X)  r8_spence(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = dilogarithm_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_spence ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_sqrt ( x ):

#*****************************************************************************80
#
## r8_sqrt() computes the square root of an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  sqrt2 = np.array ( [ \
    0.70710678118654752440084436210485, \
    1.0, \
    1.41421356237309504880168872420970 ] )

  niter = int ( 1.443 * r8_log ( - 0.104 * r8_log ( 0.1 * r8_mach ( 3 ) ) ) + 1.0 )

  if ( x < 0.0 ):

    print ( '' )
    print ( 'r8_sqrt - Fatal error!' )
    print ( '  X < 0.0' )
    raise Exception ( 'r8_sqrt - Fatal error!' )

  elif ( x == 0.0 ):

    value = 0.0

  else:

    y, n = r8_upak ( x )
    ixpnt = ( n // 2 )
    irem = int ( np.fix ( n - 2 * ixpnt + 2 ) )
    value = 0.261599 + y * ( 1.114292 + y * ( -0.516888 + y * 0.141067 ) )

    for iter in range ( 0, niter ):
      value = value + 0.5 * ( y - value * value ) / value

    value = r8_pak ( sqrt2[irem-1] * value, ixpnt )

  return value

def r8_sqrt_test ( ):

#*****************************************************************************80
#
## r8_sqrt_test() tests r8_sqrt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_sqrt_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sqrt evaluates the square root function.' )
  print ( '' )
  print ( '             X         SQRT(X)  r8_sqrt(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = sqrt_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_sqrt ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_tanh ( x ):

#*****************************************************************************80
#
## r8_tanh() evaluates the hyperbolic tangent of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  tanhcs = np.array ( [ \
      -0.25828756643634710438338151450605, \
      -0.11836106330053496535383671940204, \
      +0.98694426480063988762827307999681E-02, \
      -0.83579866234458257836163690398638E-03, \
      +0.70904321198943582626778034363413E-04, \
      -0.60164243181207040390743479001010E-05, \
      +0.51052419080064402965136297723411E-06, \
      -0.43320729077584087216545467387192E-07, \
      +0.36759990553445306144930076233714E-08, \
      -0.31192849612492011117215651480953E-09, \
      +0.26468828199718962579377758445381E-10, \
      -0.22460239307504140621870997006196E-11, \
      +0.19058733768288196054319468396139E-12, \
      -0.16172371446432292391330769279701E-13, \
      +0.13723136142294289632897761289386E-14, \
      -0.11644826870554194634439647293781E-15, \
      +0.98812684971669738285540514338133E-17, \
      -0.83847933677744865122269229055999E-18, \
      +0.71149528869124351310723506176000E-19, \
      -0.60374242229442045413288837119999E-20, \
      +0.51230825877768084883404663466666E-21, \
      -0.43472140157782110106047829333333E-22, \
      +0.36888473639031328479423146666666E-23, \
      -0.31301874774939399883325439999999E-24, \
      +0.26561342006551994468488533333333E-25, \
      -0.22538742304145029883494399999999E-26, \
      +0.19125347827973995102208000000000E-27, \
      -0.16228897096543663117653333333333E-28, \
      +0.13771101229854738786986666666666E-29, \
      -0.11685527840188950118399999999999E-30, \
      +0.99158055384640389120000000000000E-32 ] )

  nterms = r8_inits ( tanhcs, 31, 0.1 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( 3.0 * r8_mach ( 3 ) )
  xmax = - 0.5 * np.log ( r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= sqeps ):

    value = x

  elif ( y <= 1.0 ):

    value = x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, tanhcs, nterms ) )

  elif ( y <= xmax ):

    y = np.exp ( y )
    yrec = 1.0 / y
    value = ( y - yrec ) / ( y + yrec )

    if ( x < 0.0 ):
      value = - value

  else:

    if ( x < 0.0 ):
      value = - 1.0
    else:
      value = + 1.0

  return value

def r8_tanh_test ( ):

#*****************************************************************************80
#
## r8_tanh_test() tests r8_tanh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_tanh_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_tanH evaluates the hyperbolic tangent function.' )
  print ( '  tanh_values() returns some exact values.' )
  print ( '' )
  print ( '             X         TANH(X)  r8_tanH(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = tanh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_tanh ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def r8_tan ( x ):

#*****************************************************************************80
#
## r8_tan() evaluates the tangent of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
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
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  pi2rec = 0.011619772367581343075535053490057

  tancs = np.array ( [ \
      +0.22627932763129357846578636531752, \
      +0.43017913146548961775583410748067E-01, \
      +0.68544610682565088756929473623461E-03, \
      +0.11045326947597098383578849369696E-04, \
      +0.17817477903926312943238512588940E-06, \
      +0.28744968582365265947529646832471E-08, \
      +0.46374854195902995494137478234363E-10, \
      +0.74817609041556138502341633308215E-12, \
      +0.12070497002957544801644516947824E-13, \
      +0.19473610812823019305513858584533E-15, \
      +0.31417224874732446504614586026666E-17, \
      +0.50686132555800153941904891733333E-19, \
      +0.81773105159836540043979946666666E-21, \
      +0.13192643412147384408951466666666E-22, \
      +0.21283995497042377309866666666666E-24, \
      +0.34337960192345945292800000000000E-26, \
      +0.55398222121173811200000000000000E-28, \
      +0.89375227794352810666666666666666E-30, \
      +0.14419111371369130666666666666666E-31 ] )

  nterms = r8_inits ( tancs, 19, 0.1 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xsml = np.sqrt ( 3.0 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( xmax < y ):
    print ( '' )
    print ( 'r8_tan - Warning!' )
    print ( '  No precision because |X| is big.' )
    value = 0.0
    return value

  ainty = r8_aint ( y )
  yrem = y - ainty
  prodbg = 0.625 * ainty
  ainty = r8_aint ( prodbg )
  y = ( prodbg - ainty ) + 0.625 * yrem + pi2rec * y
  ainty2 = r8_aint ( y )
  ainty = ainty + ainty2
  y = y - ainty2

  ifn = r8_aint ( ainty % 2.0 )

  if ( ifn == 1 ):
    y = 1.0 - y

  if ( 1.0 - y < abs ( x ) * sqeps ):
    print ( '' )
    print ( 'r8_tan - Warning!' )
    print ( '  Answer < half precision.' )
    print ( '  |X| big or X near pi/2 or 3*pi/2.' )

  if ( y == 1.0 ):
    print ( '' )
    print ( 'r8_tan - Fatal error!' )
    print ( '  X is pi/2 or 3*pi/2.' )
    value = 0.0
    raise Exception ( 'r8_tan - Fatal error!' )

  if ( y <= 0.25 ):

    value = y
    if ( xsml < y ):
      value = y * ( 1.5 + r8_csevl ( 32.0 * y * y - 1.0, tancs, nterms ) )

  elif ( y <= 0.5 ):

    value = 0.5 * y * ( 1.5 + r8_csevl ( \
      8.0 * y * y - 1.0, tancs, nterms ) )
    value = 2.0 * value / ( 1.0 - value * value )

  else:

    value = 0.25 * y * ( 1.5 + r8_csevl ( \
      2.0 * y * y - 1.0, tancs, nterms ) )
    value = 2.0 * value / ( 1.0 - value * value )
    value = 2.0 * value / ( 1.0 - value * value )

  if ( x < 0.0 ):
    value = - abs ( value )
  elif ( 0.0 < x ):
    value = + abs ( value )

  if ( ifn == 1 ):
    value = - value

  return value

def r8_tan_test ( ):

#*****************************************************************************80
#
## r8_tan_test() tests r8_tan().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_tan_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_tan evaluates the tangent function.' )
  print ( '' )
  print ( '             X         TAN(X)  r8_tan(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = tan_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_tan ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )

  return

def shi_values ( n_data ):

#*****************************************************************************80
#
## shi_values() returns some values of the hyperbolic sine integral function.
#
#  Discussion:
#
#    SHI(X) = integral ( 0 <= T <= X ) sinh ( T ) / T dt
#
#    In Mathematica, the function can be evaluated by:
#
#      SinhIntegral[x]
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( \
    0.5069967498196672, \
    0.6121303965633808, \
    0.7193380189288998, \
    0.8289965633789345, \
    0.9414978265114335, \
    1.057250875375729, \
    1.300250361022057, \
    1.561713388361002, \
    1.845814141358504, \
    2.157290343425901, \
    2.501567433354976, \
    3.549340406224435, \
    4.973440475859807, \
    6.966162067504942, \
    9.817326911233034, \
    13.96788504934715  ))

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ))

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

def shi_values_test ( ):

#*****************************************************************************80
#
## shi_values_test() tests shi_values().
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
  import platform

  print ( '' )
  print ( 'shi_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  shi_values stores values of the SHI function.' )
  print ( '' )
  print ( '      X         SHI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = shi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def sin_degree_values ( n_data ):

#*****************************************************************************80
#
## sin_degree_values(): the sine function with argument in degrees.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sin[x Degree]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
    -0.087155742747658173558, \
     0.000000000000000000000, \
     0.017452406437283512819, \
     0.034899496702500971646, \
     0.052335956242943832722, \
     0.069756473744125300776, \
     0.087155742747658173558, \
     0.17364817766693034885, \
     0.25881904510252076235, \
     0.50000000000000000000, \
     0.70710678118654752440, \
     0.86602540378443864676, \
     0.96592582628906828675, \
     0.99619469809174553230, \
     0.99756405025982424761, \
     0.99862953475457387378, \
     0.99939082701909573001, \
     0.99984769515639123916, \
     1.0000000000000000000, \
     0.99984769515639123916, \
     0.96592582628906828675, \
     0.00000000000000000000 ))
  x_vec = np.array ( ( \
     -5.0, \
      0.0, \
      1.0, \
      2.0, \
      3.0, \
      4.0, \
      5.0, \
     10.0, \
     15.0, \
     30.0, \
     45.0, \
     60.0, \
     75.0, \
     85.0, \
     86.0, \
     87.0, \
     88.0, \
     89.0, \
     90.0, \
     91.0, \
    105.0, \
    180.0 ))


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

def sin_degree_values_test ( ):

#*****************************************************************************80
#
## sin_degree_values_test() tests sin_degree_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sin_degree_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sin_degree_values stores values of the SIN function.' )
  print ( '' )
  print ( '      X         SIN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sin_degree_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def sinh_values ( n_data ):

#*****************************************************************************80
#
## sinh_values() returns some values of the hyperbolic sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sinh[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
      -74.203210577788758977, \
       -1.1752011936438014569, \
        0.00000000000000000000, \
        0.10016675001984402582, \
        0.20133600254109398763, \
        0.30452029344714261896, \
        0.41075232580281550854, \
        0.52109530549374736162, \
        0.63665358214824127112, \
        0.75858370183953350346, \
        0.88810598218762300657, \
        1.0265167257081752760, \
        1.1752011936438014569, \
        3.6268604078470187677, \
       10.017874927409901899, \
       27.289917197127752449, \
       74.203210577788758977, \
    11013.232874703393377 ))

  x_vec = np.array ( ( \
   -5.0, \
   -1.0, \
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
    1.0, \
    2.0, \
    3.0, \
    4.0, \
    5.0, \
   10.0 ))

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

def sinh_values_test ( ):

#*****************************************************************************80
#
## sinh_values_test() tests sinh_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sinh_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sinh_values stores values of the SINH function.' )
  print ( '' )
  print ( '      X         SINH(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sinh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def sin_values ( n_data ):

#*****************************************************************************80
#
## sin_values() returns some values of the sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sin[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
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
## sin_values_test() tests sin_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'sin_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sin_values stores values of the SIN function.' )
  print ( '' )
  print ( '      X         SIN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def si_values ( n_data ):

#*****************************************************************************80
#
## si_values() returns some values of the sine integral function.
#
#  Discussion:
#
#    SI(X) = integral ( 0 <= T <= X ) sin ( T ) / T dt
#
#    In Mathematica, the function can be evaluated by:
#
#      SinIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( \
     0.4931074180430667E+00, \
     0.5881288096080801E+00, \
     0.6812222391166113E+00, \
     0.7720957854819966E+00, \
     0.8604707107452929E+00, \
     0.9460830703671830E+00, \
     0.1108047199013719E+01, \
     0.1256226732779218E+01, \
     0.1389180485870438E+01, \
     0.1505816780255579E+01, \
     0.1605412976802695E+01, \
     0.1778520173443827E+01, \
     0.1848652527999468E+01, \
     0.1833125398665997E+01, \
     0.1758203138949053E+01, \
     0.1654140414379244E+01 ))

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ))

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

def si_values_test ( ):

#*****************************************************************************80
#
## si_values_test() tests si_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'si_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  si_values stores values of the SI function.' )
  print ( '' )
  print ( '      X         SI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = si_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def sqrt_values ( n_data ):

#*****************************************************************************80
#
## sqrt_values() returns some values of the square root function.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
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

def sqrt_values_test ( ):

#*****************************************************************************80
#
## sqrt_values_test() tests sqrt_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'sqrt_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sqrt_values stores values of the SQRT function.' )
  print ( '' )
  print ( '      X         SQRT(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sqrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def tanh_values ( n_data ):

#*****************************************************************************80
#
## tanh_values() returns some values of the hyperbolic tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Tanh[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
   -0.99990920426259513121, \
   -0.76159415595576488812, \
    0.00000000000000000000, \
    0.099667994624955817118, \
    0.19737532022490400074, \
    0.29131261245159090582, \
    0.37994896225522488527, \
    0.46211715726000975850, \
    0.53704956699803528586, \
    0.60436777711716349631, \
    0.66403677026784896368, \
    0.71629787019902442081, \
    0.76159415595576488812, \
    0.96402758007581688395, \
    0.99505475368673045133, \
    0.99932929973906704379, \
    0.99990920426259513121, \
    0.99999999587769276362 ))

  x_vec = np.array ( ( \
   -5.0, \
   -1.0, \
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
    1.0, \
    2.0, \
    3.0, \
    4.0, \
    5.0, \
   10.0 ))

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

def tanh_values_test ( ):

#*****************************************************************************80
#
## tanh_values_test() tests tanh_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'tanh_values_test():' )
  print ( '  tanh_values() stores values of the TANH function.' )
  print ( '' )
  print ( '      X         TANH(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tanh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )

  return

def tan_values ( n_data ):

#*****************************************************************************80
#
## tan_values() returns some values of the tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Tan[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
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

def tan_values_test ( ):

#*****************************************************************************80
#
## tan_values_test() tests tan_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'tan_values_test)_:' )
  print ( '  tan_values() stores values of the TAN function.' )
  print ( '' )
  print ( '      X         TAN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tan_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## timestamp_test() tests timestamp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'timestamp_test)_:' )
  print ( '  timestamp() prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  fn_test ( )
  timestamp ( )

