#! /usr/bin/env python
#
def elliptic_inc_pik_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIK_VALUES: values of incomplete elliptic integral Pi(PHI,N,K).
#
#  Discussion:
#
#    This is the incomplete elliptic integral of the third kind.
#
#      Pi(PHI,N,K) = integral ( 0 <= T <= PHI ) 
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - K^2 * sin ( T )^2 )
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
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real PHI, N, K, the arguments of the function.
#
#    Output, real PIK, the value of the function.
#
  import numpy as np

  n_max = 20

  k_vec = np.array ( [ \
       1.959036804709882, \
      -1.123741823223131, \
      -2.317629084640271, \
     -0.1202582658444815, \
       1.008702896970963, \
      -103.3677494756118, \
       4.853800240677973, \
      -1.016577251056124, \
       -1.94341484065839, \
     -0.8876593284500023, \
      0.8160487832898813, \
      0.2994546721661018, \
     -0.7044232294525243, \
     -0.9266523277404759, \
     -0.6962608926846425, \
     -0.4453932031991797, \
     -0.9104582513322106, \
      0.6187501419936026, \
      0.8672305032589989, \
     -0.1996772638241632 ] )

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

  pik_vec = np.array ( [ \
      0.7982975462595892, \
       1.024022134726036, \
        0.40158120852642, \
      0.7772649487439858, \
      0.8737159913132074, \
    0.004733334297691273, \
      0.1280656893638068, \
       1.594376037512564, \
      0.8521145133671923, \
      0.8154325229803082, \
        1.31594514075427, \
        1.25394623148424, \
      0.3796503567258643, \
      0.3111034454739552, \
      0.9442477901112342, \
      0.9153111661980959, \
       2.842080644328393, \
      0.9263253777034376, \
       1.212396018757624, \
       1.628083572710471 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    k = 0.0
    n = 0.0
    phi = 0.0
    pik = 0.0
  else:
    k = k_vec[n_data]
    n = n_vec[n_data]
    phi = phi_vec[n_data]
    pik = pik_vec[n_data]
    n_data = n_data + 1

  return n_data, phi, n, k, pik

def elliptic_inc_pik_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIK_VALUES_TEST tests ELLIPTIC_INC_PIK_VALUES.
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
  print ( 'ELLIPTIC_INC_PIK_VALUES_TEST:' )
  print ( '  ELLIPTIC_INC_PIK_VALUES stores values of' )
  print ( '  the incomplete elliptic integral of the third' )
  print ( '  kind, with parameters PHI, N and K.' )
  print ( '' )
  print ( '    PHI           N             K            Pi(PHI,N,K)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, n, k, pik = elliptic_inc_pik_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16f' % ( phi, n, k, pik ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_pik_values_test ( )
  timestamp ( )
