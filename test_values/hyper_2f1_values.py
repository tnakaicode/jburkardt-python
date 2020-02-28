#! /usr/bin/env python
#
def hyper_2f1_values ( n_data ):

#*****************************************************************************80
#
## HYPER_2F1_VALUES returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2F1 [ a, b, c, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
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
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, C, X, the parameters.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( ( \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
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
    3.3 ))

  b_vec = np.array ( ( \
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

  c_vec = np.array ( ( \
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
    6.7, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5 ))

  f_vec = np.array ( ( \
    0.72356129348997784913, \
    0.97911109345277961340, \
    1.0216578140088564160, \
    1.4051563200112126405, \
    0.46961431639821611095, \
    0.95296194977446325454, \
    1.0512814213947987916, \
    2.3999062904777858999, \
    0.29106095928414718320, \
    0.92536967910373175753, \
    1.0865504094806997287, \
    5.7381565526189046578, \
    15090.669748704606754, \
   -104.31170067364349677, \
    21.175050707768812938, \
    4.1946915819031922850, \
    1.0170777974048815592E+10, \
   -24708.635322489155868, \
    1372.2304548384989560, \
    58.092728706394652211, \
    5.8682087615124176162E+18, \
   -4.4635010147295996680E+08, \
    5.3835057561295731310E+06, \
    20396.913776019659426 ))

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    c = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    c = c_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, c, x, f

def hyper_2f1_values_test ( ):

#*****************************************************************************80
#
## HYPER_2F1_VALUES_TEST demonstrates the use of HYPER_2F1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'HYPER_2F1_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HYPER_2F1_VALUES stores values of the hypergeometric function 2F1' )
  print ( '' )
  print ( '     A     B        C           X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, c, x, f = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %4d  %12f  %12f  %24.16g' % ( a, b, c, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HYPER_2F1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hyper_2f1_values_test ( )
  timestamp ( )
