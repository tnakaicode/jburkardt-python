#! /usr/bin/env python
#
def i0ml0_values ( n_data ):

#*****************************************************************************80
#
## I0ML0_VALUES returns some values of the I0ML0 function.
#
#  Discussion:
#
#    The function is defined by:
#
#      I0ML0(x) = I0(x) - L0(x)
#
#    I0(x) is the modified Bessel function of the first kind of order 0,
#    L0(x) is the modified Struve function of order 0.
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#      special functions,
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

  f_vec = np.array ( (\
     0.99875755515461749793E+00, \
     0.99011358230706643807E+00, \
     0.92419435310023947018E+00, \
     0.73624267134714273902E+00, \
     0.55582269181411744686E+00, \
     0.34215154434462160628E+00, \
     0.17087174888774706539E+00, \
     0.81081008709219208918E-01, \
     0.53449421441089580702E-01, \
     0.39950321008923244846E-01, \
     0.39330637437584921392E-01, \
     0.37582274342808670750E-01, \
     0.31912486554480390343E-01, \
     0.25506146883504738403E-01, \
     0.21244480317825292412E-01, \
     0.15925498348551684335E-01, \
     0.12737506927242585015E-01, \
     0.84897750814784916847E-02, \
     0.63668349178454469153E-02, \
     0.50932843163122551114E-02 ))

  x_vec = np.array ( (\
       0.0019531250E+00, \
       0.0156250000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       2.0000000000E+00, \
       4.0000000000E+00, \
       8.0000000000E+00, \
      12.0000000000E+00, \
      16.0000000000E+00, \
      16.2500000000E+00, \
      17.0000000000E+00, \
      20.0000000000E+00, \
      25.0000000000E+00, \
      30.0000000000E+00, \
      40.0000000000E+00, \
      50.0000000000E+00, \
      75.0000000000E+00, \
     100.0000000000E+00, \
     125.0000000000E+00 ))

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

def i0ml0_values_test ( ):

#*****************************************************************************80
#
## I0ML0_VALUES_TEST demonstrates the use of I0ML0_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'I0ML0_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I0ML0_VALUES stores values of the I0ML0 function.' )
  print ( '' )
  print ( '      X         I0ML0(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = i0ml0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I0ML0_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i0ml0_values_test ( )
  timestamp ( )

