#! /usr/bin/env python3
#
def tran06_values ( n_data ):

#*****************************************************************************80
#
## TRAN06_VALUES returns some values of the order 6 transportation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      TRAN06(x) = Integral ( 0 <= t <= x ) t^6 exp(t) / ( exp(t) - 1 )^2 dt
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.56843405953641209574E-14, \
     0.59601180165247401484E-08, \
     0.60978424397580572815E-05, \
     0.61578909866319494394E-02, \
     0.18854360275680840514E+00, \
     0.13319251347921659134E+01, \
     0.50857202271697616755E+01, \
     0.13729222365466557122E+02, \
     0.29579592481641441292E+02, \
     0.88600835706899853768E+02, \
     0.10916037113373004909E+03, \
     0.18224323749575359518E+03, \
     0.23765383125586756031E+03, \
     0.29543246745959381136E+03, \
     0.50681244381280455592E+03, \
     0.63878231134946125623E+03, \
     0.72699203556994876111E+03, \
     0.73230331643146851717E+03, \
     0.73248692015882096369E+03, \
     0.73248700462879996604E+03 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
       5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00 ))

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

def tran06_values_test ( ):

#*****************************************************************************80
#
## TRAN06_VALUES_TEST demonstrates the use of TRAN06_VALUES.
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
  print ( 'TRAN06_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRAN06_VALUES stores values of the TRAN06 function.' )
  print ( '' )
  print ( '      X         TRAN06(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tran06_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRAN06_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tran06_values_test ( )
  timestamp ( )

