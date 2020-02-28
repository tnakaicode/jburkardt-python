#! /usr/bin/env python
#
def bessel_j0_zero_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_J0_VALUES returns some zeros of the J0 Bessel function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer K, the index of the zero.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 30

  fx_vec = np.array ( [ \
    2.40482555769577276862163187933E+00, \
    5.52007811028631064959660411281E+00, \
    8.65372791291101221695419871266E+00, \
    11.7915344390142816137430449119E+00, \
    14.9309177084877859477625939974E+00, \
    18.0710639679109225431478829756E+00, \
    21.2116366298792589590783933505E+00, \
    24.3524715307493027370579447632E+00, \
    27.4934791320402547958772882346E+00, \
    30.6346064684319751175495789269E+00, \
    33.7758202135735686842385463467E+00, \
    36.9170983536640439797694930633E+00, \
    40.0584257646282392947993073740E+00, \
    43.1997917131767303575240727287E+00, \
    46.3411883716618140186857888791E+00, \
    49.4826098973978171736027615332E+00, \
    52.6240518411149960292512853804E+00, \
    55.7655107550199793116834927735E+00, \
    58.9069839260809421328344066346E+00, \
    62.0484691902271698828525002646E+00, \
    65.1899648002068604406360337425E+00, \
    68.3314693298567982709923038400E+00, \
    71.4729816035937328250630738561E+00, \
    74.6145006437018378838205404693E+00, \
    77.7560256303880550377393718912E+00, \
    80.8975558711376278637721434909E+00, \
    84.0390907769381901578796383480E+00, \
    87.1806298436411536512618050690E+00, \
    90.3221726372104800557177667775E+00, \
    93.4637187819447741711905915439E+00 ] )

  k_vec = np.array ( [ \
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
    21, \
    22, \
    23, \
    24, \
    25, \
    26, \
    27, \
    28, \
    29, \
    30  ] )

  if ( n_data < 0 ):
    n_data = 0

  n_data = n_data + 1

  if ( n_max < n_data ):
    n_data = 0
    k = 0
    fx = 0.0
  else:
    k = k_vec[n_data-1]
    fx = fx_vec[n_data-1]

  return n_data, k, fx

def bessel_j0_zero_values_test ( ):

#*****************************************************************************80
#
## BESSEL_J0_ZERO_VALUES_TEST demonstrates the use of BESSEL_J0_ZERO_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_J0_ZERO_VALUES_TEST:' )
  print ( '  BESSEL_J0_ZERO_VALUES stores zeros of' )
  print ( '  the Bessel J0 function.' )
  print ( '' )
  print ( '      K            X(K)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, k, fx = bessel_j0_zero_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %24.16g' % ( k, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_J0_ZERO_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_j0_zero_values_test ( )
  timestamp ( )
