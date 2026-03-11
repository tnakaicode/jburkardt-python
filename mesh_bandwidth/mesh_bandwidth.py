#! /usr/bin/env python3
#
def mesh_bandwidth_test ( ):

#*****************************************************************************80
#
## mesh_bandwidth_test() tests mesh_bandwidth().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mesh_bandwidth_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mesh_bandwidth().' )

  mesh_bandwidth ( 'sphere_q4_elements.txt' )
#
#  Terminate.
#
  print ( '' )
  print ( 'mesh_bandwidth_test():' )
  print ( '  Normal end of execution.' )

  return

def mesh_bandwidth ( element_filename ):

#*****************************************************************************80
#
## mesh_bandwidth() determines the geometric bandwidth of a mesh of elements.
#
#  Discussion:
#
#    The user supplies an element file, listing the indices of the nodes that
#    make up each element.
#
#    The code computes the geometric bandwidth associated with the mesh.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string element_filename, the file containing the element definitions.
#
  import numpy as np

  print ( '' )
  print ( 'mesh_bandwidth():' )
  print ( '  Read a file which defines a mesh in 2D, 3D, or ND,' )
  print ( '  made up of elements of uniform order.' )
  print ( '  Determine the geometric mesh bandwidth.' )
  print ( '' )
  print ( '    M = ML + 1 + MU.' )
  print ( '' )
  print ( '  which is the bandwidth of the vertex connectivity' )
  print ( '  matrix.' )
  print ( '' )
  print ( '  Note that a matrix associated with variables defined' )
  print ( '  at the nodes could have a greater bandwidth than M,' )
  print ( '  since you might have multiple variables at a vertex,' )
  print ( '  or the variable might be a vector quantity,' )
  print ( '  or physical effects might link two variables that are' )
  print ( '  not associated with vertices that are connected.' )
#
#  Read the triangulation data.
#
  element_node = np.loadtxt ( element_filename, dtype = int )

  element_num, element_order = element_node.shape

  print ( '' )
  print ( '  Read element node data from "' + element_filename + '"' )
  print ( '  Element number ELEMENT_NUM  =', element_num )
  print ( '  Element order ELEMENT_ORDER =', element_order )
#
#  Compute the bandwidth.
#
  ml, mu, m = bandwidth_mesh ( element_num, element_order, element_node )

  print ( '' )
  print ( '  Lower bandwidth ML =', ml )
  print ( '  Upper bandwidth MU =', mu )
  print ( '  Total bandwidth M  =', m )

  return

def bandwidth_mesh ( element_num, element_order, element_node ):

#*****************************************************************************80
#
## bandwidth_mesh() determines the bandwidth of the coefficient matrix.
#
#  Discussion:
#
#    The quantity computed here is the "geometric" bandwidth determined
#    by the finite element mesh alone.
#
#    If a single finite element variable is associated with each node
#    of the mesh, and if the nodes and variables are numbered in the
#    same way, then the geometric bandwidth is the same as the bandwidth
#    of a typical finite element matrix.
#
#    The bandwidth M is defined in terms of the lower and upper bandwidths:
#
#      M = ML + 1 + MU
#
#    where 
#
#      ML = maximum distance from any diagonal entry to a nonzero
#      entry in the same row, but earlier column,
#
#      MU = maximum distance from any diagonal entry to a nonzero
#      entry in the same row, but later column.
#
#    Because the finite element node adjacency relationship is symmetric,
#    we are guaranteed that ML = MU.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ELEMENT_NUM, the number of elements.
#
#    integer ELEMENT_ORDER, the order of the elements.
#
#    integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#    ELEMENT_NODE(I,J) is the global index of local node J in element I.
#
#  Output:
#
#    integer ML, MU, the lower and upper bandwidths of the matrix.
#
#    integer M, the bandwidth of the matrix.
#
  ml = 0
  mu = 0

  for element in range ( 0, element_num ):

    for local_i in range ( 0, element_order ):
      global_i = element_node[element,local_i]

      for local_j in range ( 0, element_order ):
        global_j = element_node[element,local_j]

        mu = max ( mu, global_j - global_i )
        ml = max ( ml, global_i - global_j )

  m = ml + 1 + mu

  return ml, mu, m

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
  mesh_bandwidth_test ( )
  timestamp ( )

