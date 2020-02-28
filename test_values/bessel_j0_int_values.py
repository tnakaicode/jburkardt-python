#! /usr/bin/env python
#
def bessel_j0_int_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_J0_INT_VALUES returns some values of the Bessel J0 integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      J0_INT(x) = Integral ( 0 <= t <= x ) J0(t) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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

  n_max = 20

  fx_vec = np.array ( ( \
      0.97656242238978822427E-03, \
      0.39062450329491108875E-02, \
     -0.62479657927917933620E-01, \
      0.12483733492120479139E+00, \
     -0.48968050664604505505E+00, \
      0.91973041008976023931E+00, \
     -0.14257702931970265690E+01, \
      0.10247341594606064818E+01, \
     -0.12107468348304501655E+01, \
      0.11008652032736190799E+01, \
     -0.10060334829904124192E+01, \
      0.81330572662485953519E+00, \
     -0.10583788214211277585E+01, \
      0.87101492116545875169E+00, \
     -0.88424908882547488420E+00, \
      0.11257761503599914603E+01, \
     -0.90141212258183461184E+00, \
      0.91441344369647797803E+00, \
     -0.94482281938334394886E+00, \
      0.92266255696016607257E+00 ) )

  x_vec = np.array ( ( \
       0.0009765625E+00, \
       0.0039062500E+00, \
      -0.0625000000E+00, \
       0.1250000000E+00, \
      -0.5000000000E+00, \
       1.0000000000E+00, \
      -2.0000000000E+00, \
       4.0000000000E+00, \
      -8.0000000000E+00, \
      16.0000000000E+00, \
     -16.5000000000E+00, \
      18.0000000000E+00, \
     -20.0000000000E+00, \
      25.0000000000E+00, \
     -30.0000000000E+00, \
      40.0000000000E+00, \
     -50.0000000000E+00, \
      75.0000000000E+00, \
     -80.0000000000E+00, \
     100.0000000000E+00 ) )

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

def bessel_j0_int_values_test ( ):

#*****************************************************************************80
#
## BESSEL_J0_INT_VALUES_TEST demonstrates the use of BESSEL_J0_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_J0_INT_VALUES_TEST:' )
  print ( '  BESSEL_J0_INT_VALUES stores values of the Bessel J integral. of order 0.' )
  print ( '' )
  print ( '      X           Int_J(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j0_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_J0_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_j0_int_values_test ( )
  timestamp ( )
