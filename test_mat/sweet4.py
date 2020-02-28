#! /usr/bin/env python
#
def sweet4 ( ):

#*****************************************************************************80
#
## SWEET4 returns the SWEET4 matrix.
#
#  Example:
#
#    5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0   1.0  10.0 -15.0
#    1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0   1.0  10.0
#   -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0   1.0
#   12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0
#  -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0
#   28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0
#   -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0
#   -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8
#    2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6
#    1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0
#   -6.0   1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0
#    1.0  -6.0   1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0
#   -0.5   1.0  -6.0   1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  n = 13

  v = np.array ( [ \
  -0.5,  1.0,  -6.0,     1.0,    2.0, \
  -1.0, -7.0,  28.361, -19.656, 12.755, \
  -3.0,  1.0,   5.0,    -1.0,    6.0, \
   2.0,  5.697, 5.850,   3.0,   -5.0, \
  -2.0, -7.0,   1.0,    10.0,  -15.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = v[j-i+12]

  return a

def sweet4_condition ( ):

#*****************************************************************************80
#
## SWEET4_CONDITION returns the L1 condition of the SWEET4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 100.3190000000000
  b_norm = 0.510081684645161
  value = a_norm * b_norm

  return value

def sweet4_condition_test ( ):

#*****************************************************************************80
#
## SWEET4_CONDITION_TEST tests SWEET4_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from sweet4 import sweet4
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'SWEET4_CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SWEET4_CONDITION computes the condition of the SWEET4 matrix.' )

  n = 13
  a = sweet4 ( )
  r8mat_print ( n, n, a, '  SWEET4 matrix:' )

  value = sweet4_condition ( )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SWEET4_CONDITION_TEST' )
  print ( '  Normal end of execution.' )
  return

def sweet4_determinant ( ):

#*****************************************************************************80
#
## SWEET4_DETERMINANT returns the determinant of the SWEET4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = - 6.463481763930611E+16

  return value

def sweet4_determinant_test ( ):

#*****************************************************************************80
#
## SWEET4_DETERMINANT_TEST tests SWEET4_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from sweet4 import sweet4
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'SWEET4_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SWEET4_DETERMINANT computes the determinant of the SWEET4 matrix.' )

  n = 13
  a = sweet4 ( )
  r8mat_print ( n, n, a, '  SWEET4 matrix:' )

  value = sweet4_determinant ( )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SWEET4_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def sweet4_inverse ( ):

#*****************************************************************************80
#
## SWEET4_INVERSE returns the inverse of the SWEET4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(13,13), the matrix.
#
  import numpy as np
#
#  Note that matrix entries are given by row.
#
  a = np.array ( [ \
  [ -0.006395453515049,   0.030690839549686, \
    -0.002288997065175,  -0.008539260151857, \
    -0.001015137652004,   0.040513470913244, \
     0.017598472282428,  -0.008312925397734, \
    -0.015546543686421,  -0.010969455314610, \
    -0.017014452081345,  -0.017669033095207, \
    -0.013805699365025 ], \
  [  0.004338135763774,   0.039852868508471, \
    -0.006409462970417,  -0.010789166315387, \
     0.023605183638394,   0.023524498024753, \
     0.032221111978773,   0.010175588114759, \
    -0.018129776994110,  -0.028500341074603, \
    -0.029318921760199,  -0.030615698849391, \
    -0.017669033095207 ], \
  [  0.011852844358462,   0.033292080046396, \
    -0.005374341111703,  -0.008875487063420, \
     0.031350558988152,   0.015098401236510, \
    -0.004426214105193,   0.030910853378811, \
     0.012927937004693,  -0.023901509668313, \
    -0.035222171390576,  -0.029318921760199, \
    -0.017014452081345 ], \
  [  0.013846756886370,   0.028058421670586, \
    -0.009388803334490,  -0.004500416153857, \
     0.032089285374445,   0.007746385727172, \
    -0.018511813509106,  -0.002525445590655, \
     0.039475608232317,   0.011543138436698, \
    -0.023901509668313,  -0.028500341074603, \
    -0.010969455314610 ], \
  [  0.009447720973799,   0.021796805754657, \
     0.000727759422194,  -0.008130365160809, \
     0.021992767390463,   0.013573971521042, \
    -0.015354921685074,  -0.016609776210723, \
     0.004261697864111,   0.039475608232316, \
     0.012927937004693,  -0.018129776994110, \
    -0.015546543686421 ], \
  [  0.009432787993907,   0.039704365747118, \
    -0.018354056201609,  -0.002772215599655, \
     0.028789202755591,   0.020818744033636, \
    -0.008277808905384,  -0.017802710611741, \
    -0.016609776210723,  -0.002525445590655, \
     0.030910853378811,   0.010175588114759, \
    -0.008312925397734 ], \
  [  0.006050784346575,   0.020779138484695, \
     0.018595613535238,  -0.018881036665831, \
     0.017128957468121,   0.021782629702447, \
     0.006363468918819,  -0.008277808905384, \
    -0.015354921685074,  -0.018511813509106, \
    -0.004426214105193,   0.032221111978773, \
     0.017598472282428 ], \
  [ -0.001688517566864,  -0.071337491505107, \
     0.069446707802933,   0.034560078451674, \
    -0.059246627902032,  -0.038486648845696, \
     0.021782629702447,   0.020818744033636, \
     0.013573971521042,   0.007746385727172, \
     0.015098401236510,   0.023524498024753, \
     0.040513470913244 ], \
  [ -0.024098383394697,  -0.082853404494777, \
     0.033466389466084,   0.079212314240954, \
    -0.061573703805162,  -0.059246627902032, \
     0.017128957468121,   0.028789202755591, \
     0.021992767390463,   0.032089285374445, \
     0.031350558988152,   0.023605183638394, \
    -0.001015137652004 ], \
  [ -0.014571843537603,   0.050761162107706, \
    -0.090910979018549,   0.012959017667649, \
     0.079212314240954,   0.034560078451674, \
    -0.018881036665831,  -0.002772215599655, \
    -0.008130365160809,  -0.004500416153857, \
    -0.008875487063420,  -0.010789166315387, \
    -0.008539260151857 ], \
  [  0.006620954487991,  -0.004862149070269, \
     0.029222791279654,  -0.090910979018549, \
     0.033466389466084,   0.069446707802933, \
     0.018595613535238,  -0.018354056201609, \
     0.000727759422194,  -0.009388803334490, \
    -0.005374341111703,  -0.006409462970417, \
    -0.002288997065175 ], \
  [  0.017905883190490,  -0.068187074515203, \
    -0.004862149070269,   0.050761162107706, \
    -0.082853404494777,  -0.071337491505107, \
     0.020779138484695,   0.039704365747118, \
     0.021796805754657,   0.028058421670586, \
     0.033292080046396,   0.039852868508471, \
     0.030690839549686 ], \
  [ -0.031068329896258,   0.017905883190490, \
     0.006620954487991,  -0.014571843537603, \
    -0.024098383394697,  -0.001688517566864, \
     0.006050784346575,   0.009432787993907, \
     0.009447720973799,   0.013846756886370, \
     0.011852844358462,   0.004338135763774, \
    -0.006395453515049 ] ] )

  return a

def sweet4_test ( ):

#*****************************************************************************80
#
## SWEET4_TEST tests SWEET4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'SWEET4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SWEET4 computes the SWEET4 matrix.' )

  n = 13
  a = sweet4 ( )
  r8mat_print ( n, n, a, '  SWEET4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SWEET4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sweet4_test ( )
  timestamp ( )
 
