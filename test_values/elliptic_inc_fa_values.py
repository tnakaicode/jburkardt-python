#! /usr/bin/env python
#
def elliptic_inc_fa_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FA_VALUES: values of the incomplete elliptic integral F(PHI,A).
#
#  Discussion:
#
#    This is the incomplete elliptic integral of the first kind.
#
#      F(PHI,A) = integral ( 0 <= T <= PHI ) 
#        dT / sqrt ( 1 - sin^2 ( A ) * sin^2 ( T ) )
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
#    Output, real PHI, A, the arguments.
#
#    Output, real FA, the function value.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( [ \
         123.0821233267548, \
         11.26931745051486, \
        -94.88806452075445, \
        -99.71407853545323, \
         57.05881039324191, \
        -19.71363287074183, \
         56.31230299738043, \
        -91.55605346417718, \
        -27.00654574696468, \
        -169.2293728595904, \
         61.96859564803047, \
        -158.7324398933148, \
         105.0883958999383, \
        -48.95883872360177, \
        -42.58568835110901, \
         11.65603284687828, \
        -8.398113719173338, \
         17.69362213019626, \
          73.8803420626852, \
        -69.82492339645128 ] )

  fa_vec = np.array ( [ \
        0.3478806460316299, \
         1.313180577009584, \
        0.7037956689264326, \
        0.4157626844675118, \
       0.06888475483285136, \
       0.09697816754845832, \
        0.6605394722518515, \
          1.82758346036751, \
         1.482258783392487, \
        0.1485295339221232, \
         1.753800062701494, \
         0.193528896465351, \
        0.4199100508706138, \
        0.1790836490491233, \
         1.446048832279763, \
         1.094097652100984, \
         1.358947908427035, \
          1.46400078231538, \
        0.3009092014525799, \
        0.6621341112075102 ] )

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
        0.6235880396594726 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    fa = 0.0
    phi = 0.0
  else:
    a = a_vec[n_data]
    fa = fa_vec[n_data]
    phi = phi_vec[n_data]
    n_data = n_data + 1

  return n_data, phi, a, fa

def elliptic_inc_fa_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FA_VALUES_TEST tests ELLIPTIC_INC_FA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ELLIPTIC_INC_FA_VALUES_TEST:' )
  print ( '  ELLIPTIC_INC_FA_VALUES stores values of' )
  print ( '  the incomplete elliptic integral of the first' )
  print ( '  kind, with parameters PHI, A.' )
  print ( '' )
  print ( '    PHI        A            F(PHI,A)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, a, fa = elliptic_inc_fa_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( phi, a, fa ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_fa_values_test ( )
  timestamp ( )