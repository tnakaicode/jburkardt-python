#! /usr/bin/env python
#
def sphere01_area_values ( n_data ):

#*****************************************************************************80
#
## SPHERE01_AREA_VALUES returns some areas of the unit sphere in ND.
#
#  Discussion:
#
#    The formula for the surface area of the unit sphere in N dimensions is:
#
#      Sphere_Unit_Area ( N ) = 2 * PI^(N/2) / Gamma ( N / 2 )
#
#    Some values of the function include:
#
#       N   Area
#
#       2    2        * PI
#       3  ( 4 /    ) * PI
#       4  ( 2 /   1) * PI^2
#       5  ( 8 /   3) * PI^2
#       6  ( 1 /   1) * PI^3
#       7  (16 /  15) * PI^3
#       8  ( 1 /   3) * PI^4
#       9  (32 / 105) * PI^4
#      10  ( 1 /  12) * PI^5
#
#    For the unit sphere, Area(N) = N * Volume(N)
#
#    In Mathematica, the function can be evaluated by:
#
#      2 * Pi^(n/2) / Gamma[n/2]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.
#    On input, if N_DATA is 0, the first test data is returned, and
#    N_DATA is set to the index of the test data.  On each subsequent
#    call, N_DATA is incremented and that test data is returned.  When
#    there is no more test data, N_DATA is set to 0.
#
#    Output, integer N, the spatial dimension.
#
#    Output, real AREA, the area of the unit sphere 
#    in that dimension.
#
  import numpy as np

  n_max = 20

  area_vec = np.array ( ( \
     0.2000000000000000E+01, \
     0.6283185307179586E+01, \
     0.1256637061435917E+02, \
     0.1973920880217872E+02, \
     0.2631894506957162E+02, \
     0.3100627668029982E+02, \
     0.3307336179231981E+02, \
     0.3246969701133415E+02, \
     0.2968658012464836E+02, \
     0.2550164039877345E+02, \
     0.2072514267328890E+02, \
     0.1602315322625507E+02, \
     0.1183817381218268E+02, \
     0.8389703410491089E+01, \
     0.5721649212349567E+01, \
     0.3765290085742291E+01, \
     0.2396678817591364E+01, \
     0.1478625959000308E+01, \
     0.8858104195716824E+00, \
     0.5161378278002812E+00 ))

  n_vec = np.array ( ( \
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
    20 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0.0
    area = 0.0
  else:
    n = n_vec[n_data]
    area = area_vec[n_data]
    n_data = n_data + 1

  return n_data, n, area

def sphere01_area_values_test ( ):

#*****************************************************************************80
#
## SPHERE01_AREA_VALUES_TEST demonstrates the use of SPHERE01_AREA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPHERE01_AREA_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SPHERE01_AREA_VALUES stores areas of the unit sphere in N dimensions.' )
  print ( '' )
  print ( '      N         SPHERE01_AREA(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, area = sphere01_area_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %24.16f' % ( n, area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPHERE01_AREA_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere01_area_values_test ( )
  timestamp ( )

