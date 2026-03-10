#! /usr/bin/env python3
#
def gurobi_solution_read_demo ( filename ):

#*****************************************************************************80
#
## gurobi_solution_read_demo() analyzes a gurobi() solution read from a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import os

  print ( '' )
  print ( 'gurobi_solution_read_demo():' )
  print ( '  gurobi_solution_read() reads a gurobi() solution file.' )
  print ( '  This demo will read ' + filename + '"' )

  x = gurobi_solution_read ( filename )
#
#  Report the solutions.
#
  x_dim = len ( x )

  if ( x_dim <= 100 ):
    print ( x )
  else:
    print ( '' )
    print ( '  Data is rather large, so will not be printed out.' )
#
#  Save X as a text file.
#
  head, tail = os.path.splitext ( filename )
  filename2 = head + '.txt'
  np.savetxt ( filename2, x, fmt = '%d' )

  print ( '' )
  print ( '  Saved data as "' + filename2 + '"' )

  return

def gurobi_solution_read ( filename ):

#*****************************************************************************80
#
## gurobi_solution_read() reads solution vectors from a gurobi() solution file.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer X(X_DIM), a vector of solution information.
#
  import numpy as np

  print ( '' )
  print ( 'gurobi_solution_read():' )
  print ( '  Reading gurobi() solution file "' + filename + '"' )

  data = np.loadtxt ( filename, dtype = str )

  x_num, n = np.shape ( data )
  print ( '  ' + filename + 'contains', x_num, 'lines.' )

  x = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    sindex = data[i,0]
    sindex = sindex[1:]
    svalue = data[i,1]
    index = int ( sindex )
    value = int ( svalue )
    x[index-1] = value

  return x

def gurobi_solution_read_test ( ):

#*****************************************************************************80
#
## gurobi_solution_read_test() tests gurobi_solution_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gurobi_solution_read_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  gurobi_solution_read() extracts a solution vector X' )
  print ( '  returned by gurobi() for a polyomino tiling problem.' )

  filename = 'reid_gurobi.sol'
  gurobi_solution_read_demo ( filename )

  filename = 'pent5x6_gurobi.sol'
  gurobi_solution_read_demo ( filename )

  filename = 'pent18x30_gurobi.sol'
  gurobi_solution_read_demo ( filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'gurobi_solution_read_test():' )
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
  gurobi_solution_read_test ( )
  timestamp ( )

