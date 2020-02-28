#! /usr/bin/env python3
#
def elliptic_inc_fm_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FM_VALUES: values of the incomplete elliptic integral F(PHI,M).
#
#  Discussion:
#
#    This is the incomplete elliptic integral of the first kind.
#
#      F(PHI,M) = integral ( 0 <= T <= PHI ) 
#        dT / sqrt ( 1 - M * sin ( T )^2 )
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
#    Output, real PHI, M, the arguments.
#
#    Output, real FM, the value of the function.
#
  import numpy as np

  n_max = 20

  fm_vec = np.array ( [ \
        0.4804314075855023, \
         1.535634981092025, \
        0.6602285297476601, \
        0.4125884303785135, \
       0.07964566007155376, \
        0.1062834070535258, \
        0.7733990864393913, \
         1.252862499892228, \
         1.549988686611532, \
        0.1488506735822822, \
         1.892229900799662, \
        0.1936153327753556, \
        0.5481932935424454, \
        0.1911795073571756, \
         1.379225069349756, \
         1.261282453331402, \
         1.535239838525378, \
         1.739782418156071, \
        0.3616930047198503, \
        0.6458627645916422 ] )

  m_vec = np.array ( [ \
         8.450689756874594, \
        0.6039878267930615, \
        0.1794126658351454, \
        0.7095689301026752, \
         133.9643389059188, \
         47.96621393936416, \
         2.172070586163255, \
      0.002038130569431913, \
        0.3600036705339421, \
        0.6219544540067304, \
        0.8834215943508453, \
        0.2034290670379481, \
         5.772526076430922, \
         11.14853902343298, \
        0.2889238477277305, \
        0.7166617182589116, \
        0.4760623731559658, \
        0.6094948502068943, \
         8.902276887883076, \
        0.5434439226321253 ] )

  phi_vec = np.array ( [ \
        0.3430906586047127, \
         1.302990057703935, \
        0.6523628380743488, \
        0.4046022501376546, \
       0.06884642871852312, \
        0.0969609046794745, \
         0.630370432896175, \
         1.252375418911598, \
         1.409796082144801, \
        0.1485105463502483, \
         1.349466184634646, \
        0.1933711786970301, \
        0.4088829927466769, \
        0.1785430666405224, \
         1.292588374416351, \
         1.087095515757691, \
         1.352794600489329, \
         1.432530166308616, \
        0.2968093345769761, \
        0.6235880396594726  ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    fm = 0.0
    m = 0.0
    phi = 0.0
  else:
    fm = fm_vec[n_data]
    m = m_vec[n_data]
    phi = phi_vec[n_data]
    n_data = n_data + 1

  return n_data, phi, m, fm

def elliptic_inc_fm_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FM_VALUES_TEST tests ELLIPTIC_INC_FM_VALUES.
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
  print ( 'ELLIPTIC_INC_FM_VALUES_TEST:' )
  print ( '  ELLIPTIC_INC_FM_VALUES stores values of' )
  print ( '  the incomplete elliptic integral of the first' )
  print ( '  kind, with parameters PHI, M.' )
  print ( '' )
  print ( '    PHI        M            F(PHI,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, m, fm = elliptic_inc_fm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( phi, m, fm ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_fm_values_test ( )
  timestamp ( )

