#! /usr/bin/env python
#
def elliptic_inc_pia_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIA_VALUES: values of incomplete elliptic integral Pi(PHI,N,A).
#
#  Discussion:
#
#    This is the incomplete elliptic integral of the third kind.
#
#      Pi(PHI,N,A) = integral ( 0 <= T <= PHI ) 
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - sin^2(A) * sin ( T )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2018
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real PHI, N, A, the arguments of the function.
#
#    Output, real PIA, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( [ \
         88.87822485052908, \
        -86.55208740039521, \
        -116.6195703112117, \
        -9.742878017582015, \
         65.73480919446207, \
        -115.0387719677141, \
         124.9421177735846, \
        -89.78704401263703, \
        -98.42673771271734, \
        -53.74936192418378, \
         68.28047574440727, \
         20.82174673810708, \
         -29.1042364797769, \
        -37.80176710944693, \
        -55.81173355852393, \
        -37.66594589748672, \
        -80.09408170610219, \
         52.23806528467412, \
         74.30945212430545, \
        -17.22920703094039 ] )

  n_vec = np.array ( [ \
         8.064681366127422, \
       -0.2840588974558835, \
        -5.034023488967104, \
        -1.244606253942751, \
         1.465981775919188, \
         95338.12857321106, \
        -44.43130633436311, \
       -0.8029374966926196, \
         5.218883222649502, \
         2.345821782626782, \
         0.157358332363011, \
         1.926593468907062, \
         6.113982855261652, \
         1.805710621498681, \
       -0.4072847419780592, \
       -0.9416404038595624, \
        0.7009655305226739, \
        -1.019830985340273, \
       -0.4510798219577842, \
        0.6028821390092596  ] )

  phi_vec = np.array ( [ \
        0.3430906586047127, \
        0.8823091382756705, \
        0.4046022501376546, \
        0.9958310121985398, \
         0.630370432896175, \
      0.002887706662908567, \
        0.1485105463502483, \
         1.320800086884777, \
        0.4088829927466769, \
         0.552337007372852, \
         1.087095515757691, \
        0.7128175949111615, \
        0.2968093345769761, \
        0.2910907344062498, \
        0.9695030752034163, \
         1.122288759723523, \
         1.295911610809573, \
         1.116491437736542, \
         1.170719322533712, \
         1.199360682338851 ] )

  pia_vec = np.array ( [ \
        0.7099335174334724, \
        0.9601963779142505, \
        0.3362852532098376, \
        0.7785343427543768, \
         0.857889755214478, \
      0.004630772344931844, \
        0.1173842687902911, \
         1.505788070660267, \
        0.7213264194624553, \
        0.8073261799642218, \
         1.402853811110838, \
         1.259245331474513, \
        0.3779079263971614, \
        0.3088493910496766, \
        0.9782829177005183, \
        0.9430491574504173, \
         3.320796277384155, \
        0.9730988737054799, \
         1.301988094953789, \
          1.64558360445259 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    n = 0.0
    phi = 0.0
    pia = 0.0
  else:
    a = a_vec[n_data]
    n = n_vec[n_data]
    phi = phi_vec[n_data]
    pia = pia_vec[n_data]
    n_data = n_data + 1

  return n_data, phi, n, a, pia

def elliptic_inc_pia_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIA_VALUES_TEST tests ELLIPTIC_INC_PIA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ELLIPTIC_INC_PIA_VALUES_TEST:' )
  print ( '  ELLIPTIC_INC_PIA_VALUES stores values of' )
  print ( '  the incomplete elliptic integral of the third' )
  print ( '  kind, with parameters PHI, N and A.' )
  print ( '' )
  print ( '    PHI           N             A            Pi(PHI,N,A)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, n, a, pia = elliptic_inc_pia_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16f' % ( phi, n, a, pia ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_pia_values_test ( )
  timestamp ( )

