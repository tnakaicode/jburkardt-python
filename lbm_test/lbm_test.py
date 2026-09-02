#! /usr/bin/env python3
#
import sys
sys.path.insert ( 0, "../lbm" )
from lbm import *

def lbm_test ( ):

#*****************************************************************************80
#
## lbm_test() tests lbm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 August 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'lbm_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  lbm() demonstrates the Lattice Boltzmann Method.' )

  bounce_test ( )
  boundaries_test ( )
  collide_test ( )
  equilibrium_test ( )
  initialize_test ( )
  macros_test ( )
  obstacle_test ( )
  stream_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lbm_test():' )
  print ( '  Normal end of execution.' )

  return

def bounce_test ( ):

#*****************************************************************************80
#
## bounce_test() tests bounce().
#
#  Discussion:
#
#    It seems like bounce() does nothing except preserve the
#    zero entries inside the solid.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 August 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import pprint

  rng = default_rng ( )
  print ( '' )
  print ( 'bounce_test():' )
  print ( '  bounce() applies the bounce back boundary' )
  print ( '  condition to the particle density field f(9,Nx,Ny).' )

  Nx = 7
  Ny = 6
  cx = 4
  cy = 3
  r = 2

  solid = obstacle ( Nx, Ny, cx, cy, r )
#
#  Compute a hokey old f function that is zero inside the solid.
#
  f_before = rng.random ( [ 9, Nx, Ny ] )
  f_before[:,solid] = 0.0

  print ( '' )
  print ( '  f_before():' )
  for i in range ( 0, 9 ):
    bob = f_before[i,:,:]
    pprint.pprint ( bob )
#
#  Make a hokey current f function that is nonzero everywhere.
#
  f = rng.random ( [ 9, Nx, Ny ] ) + 5.0

  print ( '' )
  print ( '  f():' )
  for i in range ( 0, 9 ):
    bob = f[i,:,:]
    pprint.pprint ( bob )
#
#  Apply the bounce back condition.
#
  f = bounce ( Nx, Ny, f, f_before, solid )

  print ( '' )
  print ( '  f() after bounce():' )
  for i in range ( 0, 9 ):
    bob = f[i,:,:]
    pprint.pprint ( bob )

  return

def boundaries_test ( ):

#*****************************************************************************80
#
## boundaries_test() tests boundaries().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import pprint

  rng = default_rng ( )
  print ( '' )
  print ( 'boundaries_test():' )
  print ( '  boundaries() applies the boundary conditions' )
  print ( '  to the particle density field f(9,Nx,Ny).' )

  Nx = 7
  Ny = 6
  cx = 4
  cy = 3
  r = 2

  solid = obstacle ( Nx, Ny, cx, cy, r )
#
#  Compute a hokey old f function that is zero inside the solid.
#
  f = rng.random ( [ 9, Nx, Ny ] )
  f[:,solid] = 0.0

  print ( '' )
  print ( '  f():' )
  for i in range ( 0, 9 ):
    bob = f[i,:,:]
    pprint.pprint ( bob )
#
#  Apply the boundary condition condition.
#
  uw = 0.1
  f = boundaries ( f, Nx, Ny, uw )

  print ( '' )
  print ( '  f() after apply_boundaries():' )
  for i in range ( 0, 9 ):
    bob = f[i,:,:]
    pprint.pprint ( bob )

  return

def collide_test ( ):

#*****************************************************************************80
#
## collide_test() tests collide().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 August 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import pprint

  rng = default_rng ( )

  print ( '' )
  print ( 'collide_test():' )
  print ( '  collide() relaxes the particle density function f()' )
  print ( '  toward equilibrium.' )

  Nx = 3
  Ny = 3
  cs2 = 1.0 / 3.0
  rho = np.array ( [ [  1,  2,  3 ], [  4,  5,  6 ], [  7,  8,  9 ] ] )
  ux  = np.array ( [ [ 11, 12, 13 ], [ 14, 15, 16 ], [ 17, 18, 19 ] ] )
  uy  = np.array ( [ [ 21, 22, 23 ], [ 24, 25, 26 ], [ 27, 28, 29 ] ] )
  cx = 4
  cy = 3
  r = 2
  solid = obstacle ( Nx, Ny, cx, cy, r )

  f = rng.random ( [ 9, Nx, Ny ] )
  f[:,solid] = 0.0

  tau = 0.55

  f_out = collide ( Nx, Ny, f, cs2, rho, ux, uy, solid, tau )

  print ( '' )
  print ( '  f_out():' )
  for i in range ( 0, 9 ):
    bob = f_out[i,:,:]
    pprint.pprint ( bob )

  return

def equilibrium_test ( ):

#*****************************************************************************80
#
## equilibrium_test() tests equilibrium().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'equilibrium_test():' )
  print ( '  equilibrium() sets the equilibrium value for' )
  print ( '  the particle density field f(9,Nx,Ny).' )

  Nx = 3
  Ny = 3
  cs2 = 1.0 / 3.0
  rho = np.array ( [ [  1,  2,  3 ], [  4,  5,  6 ], [  7,  8,  9 ] ] )
  ux  = np.array ( [ [ 11, 12, 13 ], [ 14, 15, 16 ], [ 17, 18, 19 ] ] )
  uy  = np.array ( [ [ 21, 22, 23 ], [ 24, 25, 26 ], [ 27, 28, 29 ] ] )

  print ( '' )
  print ( '  rho():' )
  pprint.pprint ( rho )
  print ( '' )
  print ( '  ux():' )
  pprint.pprint ( ux )
  print ( '' )
  print ( '  uy():' )
  pprint.pprint ( uy )
#
#  Compute the equilibrium particle density function.
#
  f_eq = equilibrium ( Nx, Ny, cs2, rho, ux, uy )

  print ( '' )
  print ( '  f_eq():' )
  for i in range ( 0, 9 ):
    bob = f_eq[i,:,:]
    pprint.pprint ( bob )

  return

def f_3x3 ( ):

#*****************************************************************************80
#
## f_3x3() defines a particle density function over a 3x3 grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real f(9,Nx,Ny): the particle density function.
#
  import numpy as np

  f = np.array ( [ \
    [ [  1,  2,  3 ], [   4,  5,  6 ], [   7,  8,  9 ] ], \
    [ [ 11, 12, 13 ], [  14, 15, 16 ], [  17, 18, 19 ] ], \
    [ [ 21, 22, 23 ], [  24, 25, 26 ], [  27, 28, 29 ] ], \
    [ [ 31, 32, 33 ], [  34, 35, 36 ], [  37, 38, 39 ] ], \
    [ [ 41, 42, 43 ], [  44, 45, 46 ], [  47, 48, 49 ] ], \
    [ [ 51, 52, 53 ], [  54, 55, 56 ], [  57, 58, 59 ] ], \
    [ [ 61, 62, 63 ], [  64, 65, 66 ], [  67, 68, 69 ] ], \
    [ [ 71, 72, 73 ], [  74, 75, 76 ], [  77, 78, 79 ] ], \
    [ [ 81, 82, 83 ], [  84, 85, 86 ], [  87, 88, 89 ] ] ] )

  return f

def initialize_test ( ):

#*****************************************************************************80
#
## initialize_test() tests initialize().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'initialize_test()' )
  print ( '  initialize() initializes the' )
  print ( '  particle density field f(9,Nx,Ny).' )

  Nx = 3
  Ny = 3
  cs2 = 1.0 / 3.0
  rho0 = 1.0
  uw = 0.1
  cx = 3
  cy = 2
  r = 2

  solid = obstacle ( Nx, Ny, cx, cy, r )

  f_init = initialize ( Nx, Ny, cs2, rho0, uw, solid )

  print ( '' )
  print ( '  f_init():' )
  for i in range ( 0, 9 ):
    bob = f_init[i,:,:]
    pprint.pprint ( bob )

  return

def macros_test ( ):

#*****************************************************************************80
#
## macros_test() tests macros().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'macros_test():' )
  print ( '  macros() recovers macroscopic density and velocity' )
  print ( '  from particle density field f(9,Nx,Ny).' )

  Nx = 3
  Ny = 3
  f = f_3x3 ( )

  cx = 1
  cy = 1
  r = 0.5

  solid = obstacle ( Nx, Ny, cx, cy, r )
#
#  Determine macroscopic quantities.
#
  rho, ux, uy = macros ( Nx, Ny, f, solid )

  print ( '' )
  print ( '  Density(Nx,Ny):' )
  pprint.pprint ( rho )

  print ( '' )
  print ( '  Velocity(Nx,Ny):' )
  velocity = np.sqrt ( ux**2 + uy**2 )
  pprint.pprint ( velocity )

  return

def obstacle_test ( ):

#*****************************************************************************80
#
## obstacle_test() tests obstacle().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'obstacle_test()' )
  print ( '  obstacle() defines a logical array that' )
  print ( '  represents a circular obstacle to the flow.' )

  Nx = 7
  Ny = 6
  cx = 3
  cy = 2
  r = 2

  solid = obstacle ( Nx, Ny, cx, cy, r )

  print ( '' )
  print ( '  solid(:,:):' )
  pprint.pprint ( solid )

  return

def stream_test ( ):

#*****************************************************************************80
#
## stream_test() tests stream().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'stream_test():' )
  print ( '  stream() propagates the particle density function.' )

  f = np.zeros ( [ 9, 3, 3 ] );
  f[0,:,:] = np.array ( [ [  1,  2,  3 ], [  4,  5,  6 ], [  7,  8,  9 ] ] )
  f[1,:,:] = np.array ( [ [ 11, 12, 13 ], [ 14, 15, 16 ], [ 17, 18, 19 ] ] )
  f[2,:,:] = np.array ( [ [ 21, 22, 23 ], [ 24, 25, 26 ], [ 27, 28, 29 ] ] )
  f[3,:,:] = np.array ( [ [ 31, 32, 33 ], [ 34, 35, 36 ], [ 37, 38, 39 ] ] )
  f[4,:,:] = np.array ( [ [ 41, 42, 43 ], [ 44, 45, 46 ], [ 47, 48, 49 ] ] )
  f[5,:,:] = np.array ( [ [ 51, 52, 53 ], [ 54, 55, 56 ], [ 57, 58, 59 ] ] )
  f[6,:,:] = np.array ( [ [ 61, 62, 63 ], [ 64, 65, 66 ], [ 67, 68, 69 ] ] )
  f[7,:,:] = np.array ( [ [ 71, 72, 73 ], [ 74, 75, 76 ], [ 77, 78, 79 ] ] )
  f[8,:,:] = np.array ( [ [ 81, 82, 83 ], [ 84, 85, 86 ], [ 87, 88, 89 ] ] )

  print ( '' )
  print ( '  f():' )
  pprint.pprint ( f )

  f2 = stream ( f )
  print ( '' )
  print ( '  f() after streaming:' )
  pprint.pprint ( f2 )

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

if __name__ == '__main__':
  timestamp ( )
  lbm_test ( )
  timestamp ( )

