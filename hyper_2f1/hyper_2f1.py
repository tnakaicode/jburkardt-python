#! /usr/bin/env python3
#
def hyper_2f1_test ( ):

#*****************************************************************************80
#
## hyper_2f1_test() tests hyper_2f1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hyper_2f1_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hyper_2f1().' )

  hyper_2f1_real_test ( )
  hyper_2f1_complex_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hyper_2f1_test():' )
  print ( '  Normal end of execution.' )
  return

def hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## hyper_2f1() evaluates the hypergeometric 2F1 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C: the parameters.
#
#    real or complex X: the argument.
#
#  Output:
#
#    real or complex F: the value of the function.
#
  from scipy.special import hyp2f1

  f = hyp2f1 ( a, b, c, x )

  return f

def hyper_2f1_real_values ( n_data ):

#*****************************************************************************80
#
## hyper_2f1_real_values() returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2F1 [ a, b, c, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real A, B, C, X, the parameters.
#
#    real F, the value of the function.
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

def hyper_2f1_real_test ( ):

#*****************************************************************************80
#
## hyper_2f1_real_test() tests hyper_2f1() for real arguments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hyper_2f1_real_test():' )
  print ( '  hyper_2f1() evaluates the hypergeometric function 2F1(A,B,C;X)' )
  print ( '  Check the computation for real arguments X.' )

  n_data = 0

  while ( True ):

    n_data, a, b, c, x, f1 = hyper_2f1_real_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = hyper_2f1 ( a, b, c, x )

    print ( '' )
    print ( '  (a,b,c,x):   %4d  %4d  %12f  %12f' % ( a, b, c, x ) )
    print ( '  (exact):     %24.16g' % ( f1 ) )
    print ( '  (computed):  %24.16g' % ( f2 ) )
    print ( '  (error):     %24.16g' % ( abs ( f1 - f2 ) ) )

  return

def hyper_2f1_complex_values ( n_data ):

#*****************************************************************************80
#
## hyper_2f1_complex_values() returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fz = Hypergeometric2F1 [ a, b, c, z ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2023
#
#  Author:
#
#    John Burkardt
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
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real A, B, C: the parameters.
#
#    complex Z: the argument.
#
#    complex FZ: the value of the function.
#
  import numpy as np

  n_max = 15

  a_vec = np.array ( ( \
    3.2, \
    3.2, \
   -5.0, \
    3.3, \
   -7.0, \
    4.3, \
    3.3, \
    3.5, \
    3.3, \
    7.0, \
    5.0, \
    3.5, \
    2.1, \
    8.7, \
    8.7 ))

  b_vec = np.array ( ( \
   1.8, \
  -1.8, \
   3.3, \
  -6.0, \
   3.3, \
  -8.0, \
   5.8, \
  -2.4, \
   4.3, \
   5.0, \
   7.0, \
   1.2, \
   5.4, \
   3.2, \
   2.7 ))

  c_vec = np.array ( ( \
   6.7, \
   6.7, \
   6.7, \
   3.7, \
  -3.7, \
  -3.7, \
   6.7, \
   6.7, \
   6.7, \
   4.1, \
   4.1, \
   9.7, \
   9.7, \
   6.7, \
   6.7 ))

  fz_vec = np.array ( ( \
    5.468999154361234+0.00000000j, \
    0.3375063477462785+0.00000000j, \
    116.8274991533609+603.8909562709345j, \
    17620.41819334182+38293.80901310932j, \
   -11772775115.27448-14382285977.20268j, \
    1316118577866.058-101298889382.4362j, \
    1.733055678355656+0.6340102904953357j, \
    0.6476224071999852-0.5211050690999773j, \
   -1.483008322270093+8.374426179451589j, \
   -0.004037609523971226-0.002956632645480181j, \
   -0.004037609523971226-0.002956632645480181j, \
    1.034313610729953+0.5447389238499308j, \
    0.6885043978280027+1.227418679098749j, \
   -0.9004649679297319-1.11988994714304j, \
   -0.4608388640599718-0.5457569650549665j ))

  z_vec = np.array ( ( \
   1.0+0.0j, \
   1.0+0.0j, \
   5.2+4.8j, \
   5.2-4.8j, \
   5.2-4.8j, \
   5.2+4.8j, \
   0.2+0.1j, \
   0.2+0.5j, \
   0.8+0.3j, \
   3.0-1.0j, \
   3.0-1.0j, \
   0.6+0.9j, \
   0.5+0.7j, \
   0.5+0.7j, \
   0.6+0.9j ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    c = 0.0
    z = 0.0
    fz = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    c = c_vec[n_data]
    z = z_vec[n_data]
    fz = fz_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, c, z, fz

def hyper_2f1_complex_test ( ):

#*****************************************************************************80
#
## hyper_2f1_complex_test() tests hyper_2f1() for complex arguments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hyper_2f1_complex_test():' )
  print ( '  Test hyper_2f1() for complex arguments.' )

  n_data = 0

  while ( True ):

    n_data, a, b, c, z, f1 = hyper_2f1_complex_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = hyper_2f1 ( a, b, c, z )

    print ( '' )
    print ( '  (a,b,c,z):   %4d  %4d  %8f  (%8f,%8f)' % ( a, b, c, z.real, z.imag ) )
    print ( '  (exact):     (%24.16g,%24.16g)' % ( f1.real, f1.imag ) )
    print ( '  (computed):  (%24.16g,%24.16g)' % ( f2.real, f2.imag ) )
    print ( '  (error):     %24.16g' % ( abs ( f1 - f2 ) ) )

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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hyper_2f1_test ( )
  timestamp ( )
 
