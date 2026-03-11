#! /usr/bin/env python3
#
def scipy_test ( ):

#*****************************************************************************80
#
## scipy_test() tests scipy().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  from bessel_j_test import bessel_j_test
  from brentq_test import brentq_test
  from contour_himmelblau_test import contour_himmelblau_test
  from ConvexHull_test import ConvexHull_test
  from drum_normal_modes_test import drum_normal_modes_test
  from fft_co2_test import fft_co2_test
  from fft_el_nino_test import fft_el_nino_test
  from fft_test import fft_test
  from interp1d_test import interp1d_test
  from linalg_test import linalg_test
  from minimize_himmelblau_test import minimize_himmelblau_test
  from minimize_scalar_test import minimize_scalar_test
  from ndimage_test import ndimage_test
  from quad_test import quad_test
  from solve_ivp_test import solve_ivp_test
  from stats_test import stats_test
  import numpy as np
  import platform
  import scipy as sp

  print ( '' )
  print ( 'scipy_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + sp.version.version )
  print ( '  scipy() is an package of advanced mathematical functions.' )

  bessel_j_test ( )
  brentq_test ( )
  ConvexHull_test ( )
  contour_himmelblau_test ( )
  drum_normal_modes_test ( )
  fft_co2_test ( )
  fft_el_nino_test ( )
  fft_test ( )
  interp1d_test ( )
  linalg_test ( )
  minimize_himmelblau_test ( )
  minimize_scalar_test ( )
  ndimage_test ( )
  quad_test ( )
  solve_ivp_test ( )
  stats_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'scipy_test():' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  scipy_test ( )
  timestamp ( )

