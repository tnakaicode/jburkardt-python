#! /usr/bin/env python3
#
def flow_vector ( ):

#*****************************************************************************80
#
## flow_vector() makes a vector plot of the gradient of a function f(x,y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'flow_vector():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a vector plot of the gradient of a function z(x,y).' )
#
#  Evaluate the function at the mesh points.
#
  n = 16
  xmat, ymat, umat, vmat = flow_field ( n )
#
#  Plot 
#
  plt.clf ( )

  plt.quiver ( xmat, ymat, umat, vmat, color = 'c' )
  plt.axis ( 'Equal' )
  plt.title ( 'Velocity flow field', fontsize = 16 )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  filename = 'flow_vector.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'flow_vector():' )
  print ( '  Normal end of execution.' )
  return

def flow_field ( n ):

#*****************************************************************************80
#
## flow_field() returns velocity data for a flow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real N: the number of nodes in the X and Y directions.
#
#  Output:
#
#    real XMAT(N,N), YMAT(N,N): the node coordinates.
#
#    real UMAT(N,N), VMAT(N,N): the velocity components.
#
  import numpy as np

  xvec = np.linspace ( 0.0, 1.0, n )
  yvec = np.linspace ( 0.0, 1.0, n )

  xmat, ymat = np.meshgrid ( xvec, yvec )

  umat = - (       xmat**4 - 2.0 * xmat**3 + xmat**2 ) \
         * ( 2.0 * ymat**3 - 3.0 * ymat**2 + ymat    )

  vmat =   ( 2.0 * xmat**3 - 3.0 * xmat**2 + xmat    ) \
         * (       ymat**4 - 2.0 * ymat**3 + ymat**2 )

  return xmat, ymat, umat, vmat

if ( __name__ == "__main__" ):
  flow_vector ( )

