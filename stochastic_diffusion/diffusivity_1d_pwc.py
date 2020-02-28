#! /usr/bin/env python3
#
def diffusivity_1d_pwc ( mc, xc, vc, mp, xp ):

#*****************************************************************************80
#
## DIFFUSIVITY_1D_PWC: piecewise constant diffusivity function in 1D.
#
#  Discussion:
#
#    A piecewise constant function is defined over NC intervals, 
#    with interval IC associated with constant value VC(I),
#    separated by NC-1 ascending sorted breakpoints.
#
#    The function is to be evaluated at NP points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MC, the number of function values.
#
#    Input, real XC(MC-1), the breakpoints, in ascending order.
#
#    Input, real VC(MC), the function values over each interval.
#
#    Input, integer MP, the number of evaluation points.
#
#    Input, real XP(MP), the evaluation points.
#
#    Output, real VP(MP), the function value at the evaluation points.
#
  import numpy as np

  vp = np.zeros ( mp )

  for ip in range ( 0, mp ):
    kc = 0
    for ic in range ( 0, mc - 1 ):
      if ( xp[ip] < xc[ic] ):
        break
      kc = kc + 1
    vp[ip] = vc[kc]

  return vp

def diffusivity_1d_pwc_test ( ):

#*****************************************************************************80
#
## diffusivity_1d_pwc_test tests diffusivity_1d_pwc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'diffusivity_1d_xk_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_1d_pwc.' )

  mc = 10
  xc = np.array ( [ -0.9, -0.5, -0.45, -0.1, 0.2, 0.3, 0.32, 0.7, 0.85 ] )
  vc = np.array ( [  1.0,  1.5,  3.0,   1.2, 1.0, 0.8, 0.2,  0.4, 0.8, 1.0 ] )
#
#  Set the spatial grid.
#
  mp = 100
  x_min = -1.0
  x_max = +1.0
  xp = np.linspace ( x_min, x_max, mp )
  vp = diffusivity_1d_pwc ( mc, xc, vc, mp, xp )
#
#  Plot the diffusivity field.
#
  plt.plot ( xp, vp, linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( 'rho(X)' )
  plt.title ( 'PWC 1D Stochastic diffusivity function' )
  filename = 'diffusivity_1d_pwc.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_1d_pwc_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_1d_pwc_test ( )
  timestamp ( )
