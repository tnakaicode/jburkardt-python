#! /usr/bin/env python3
#
def lbm_obstacle_test ( ):

#*****************************************************************************80
#
## lbm_obstacle_test() reads a boolean text file for use by lbm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lbm_obstacle_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Read a file of boolean values defining an obstacle' )
  print ( '  for use by the lbm() Lattice Boltzmann Method code.' )
#
#  The file contains 400 lines of 400 0/1 values. 
#
  filename = 'lbm_obstacle_map.txt'
  print ( '  Reading data from "' + filename + '"' )
#
#  Read the data at Nx strings, each of length Ny.
#
  s = np.loadtxt ( filename, dtype = str )
#
#  Determine Nx, Ny
#
  Nx = s.shape[0]
  Ny = len ( s[0] )
#
#  Report shape.
#
  print ( '' )
  print ( '  Shape corresponds to Nx = ', Nx, ', Ny = ', Ny )
#
#  Prepare a boolean array in which to store the converted values.
#
  solid = np.zeros ( [ Nx, Ny ], dtype = bool )
#
#  Convert each character to boolean 0/1.
#
  for i in range ( 0, Nx ):
    for j in range ( 0, Ny ):
      solid[i,j] = ( s[i][j] == '1' )
#
#  Print the results.
#
  print ( '' )
  print ( '  Partial display of data:' )
  print ( '' )
  print ( solid )
#
#  Create an ASCII PBM version.
#
  pbm_filename = 'lbm_obstacle_map.pbm'
  pbm = open ( pbm_filename, 'wt' )
  pbm.write ( 'P1\n' )
  pbm.write ( '# ' + pbm_filename + '\n' )
  pbm.write ( '%d  %d\n' % ( Nx, Ny ) )
  for i in range ( 0, Nx ):
    for j in range ( 0, Ny ):
      s = ( ' %d' % ( solid[i,j] ) )
      pbm.write ( s )
    pbm.write ( '\n' )
  pbm.close ( )
  print ( '  Created portable bit map image as "' + pbm_filename + '"' )

#
#  Terminate.
#
  print ( '' )
  print ( 'lbm_obstacle_test():' )
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

if ( __name__ == "__main__" ):
  timestamp ( )
  lbm_obstacle_test ( )
  timestamp ( )
