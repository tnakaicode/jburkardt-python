#! /usr/bin/env python
#
def elliptic_inc_ek_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_INC_EK_VALUES: values of the incomplete elliptic integral E(PHI,K).
#
#  Discussion:
#
#    This is the incomplete elliptic integral of the second kind.
#
#      E(PHI,K) = integral ( 0 <= T <= PHI ) 
#        sqrt ( 1 - K^2 * sin ( T )^2 ) dT
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
#    Milton Abramowitz and Irene Stegun,
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
#    Output, real PHI, K, the arguments.
#
#    Output, real EK, the function value.
#
  import numpy as np

  n_max = 20

  ek_vec = np.array ( [ \
        0.2852345328295404, \
         1.298690225567921, \
        0.5508100202571943, \
        0.3575401358115371, \
       0.06801307805507453, \
       0.09679584980231837, \
        0.6003112504412838, \
        0.8996717721794724, \
         1.380715261453875, \
        0.1191644625202453, \
         1.196994838171557, \
        0.1536260979667945, \
        0.3546768920544152, \
        0.1758756066650882, \
         1.229819109410569, \
          1.08381066114337, \
          1.35023378157378, \
         1.419775884709218, \
        0.2824895528020034, \
        0.5770427720982867 ] )

  k_vec = np.array ( [ \
         2.712952582080266, \
        0.1279518954120547, \
        -1.429437513650137, \
        -1.981659235625333, \
         3.894801879555818, \
        -1.042486024983672, \
        0.8641142168759754, \
        -1.049058412826877, \
       -0.3024062128402472, \
        -6.574288841527263, \
        0.6987397421988888, \
         -5.12558591600033, \
         2.074947853793764, \
        -1.670886158426681, \
       -0.4843595000931672, \
        0.1393061679635559, \
       -0.0946527302537008, \
        0.1977207111754007, \
         1.788159919089993, \
        -1.077780624681256 ] )

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
    ek = 0.0
    k = 0.0
    phi = 0.0
  else:
    ek = ek_vec[n_data]
    k = k_vec[n_data]
    phi = phi_vec[n_data]
    n_data = n_data + 1

  return n_data, phi, k, ek

def elliptic_inc_ek_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_EK_VALUES_TEST tests ELLIPTIC_INC_EK_VALUES.
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
  print ( 'ELLIPTIC_INC_EK_VALUES_TEST:' )
  print ( '  ELLIPTIC_INC_EK_VALUES stores values of' )
  print ( '  the incomplete elliptic integral of the second' )
  print ( '  kind, with parameters PHI, K.\n' )
  print ( '' )
  print ( '    PHI        K            E(PHI,K)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, k, ek = elliptic_inc_ek_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( phi, k, ek ) )


  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_ek_values_test ( )
  timestamp ( )
