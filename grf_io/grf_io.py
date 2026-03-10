#! /usr/bin/env python3
#
def grf_io_test ( ):

#*****************************************************************************80
#
## grf_io_test() tests grf_io().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'grf_io_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test grf_io().' )

  grf_io_write_test ( )
  grf_io_read_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'grf_io_test():' )
  print ( '  Normal end of execution.' )

  return

def grf_io_write_test ( ):

#*****************************************************************************80
#
## grf_io_write_test() tests grf_header_write() and grf_data_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
  filename = 'coxeter.grf'

  print ( '' )
  print ( 'grf_io_write_test():' )
  print ( '  grf_header_write() writes the header of a GRF file.' )
  print ( '  grf_write() writes the data of a GRF file.' )

  node_num, edge_num = grf_example_size ( )

  grf_header_print ( node_num, edge_num )

  edge_pointer, edge_data, xy = grf_example ( node_num, edge_num )

  grf_write ( filename, node_num, edge_num, edge_pointer, edge_data, xy )

  print ( '' )
  print ( '  Write the GRF file "' + filename + '"' )

  return

def grf_io_read_test ( ):

#*****************************************************************************80
#
## grf_io_read_test() tests grf_header_read() and grf_data_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
  filename = 'coxeter.grf'

  print ( '' )
  print ( 'grf_io_read_test():' )
  print ( '  grf_header_read() reads the header of a GRF file.' )
  print ( '  grf_data_read() reads the data of a GRF file.' )

  print ( '' )
  print ( '  Read the GRF file "' + filename + '"' )

  node_num, edge_num = grf_header_read ( filename )

  grf_header_print ( node_num, edge_num )

  edge_pointer, edge_data, xy = grf_data_read ( filename, node_num, edge_num )

  grf_data_print ( node_num, edge_num, edge_pointer, edge_data, xy )

  return

def grf_data_print ( node_num, edge_num, edge_pointer, edge_data, xy ):

#*****************************************************************************80
#
## grf_data_print() prints the data of a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Input:
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
#    integer EDGE_POINTER(NODE_NUM+1), pointers to
#    the beginning of edge data for each node.
#
#    integer EDGE_DATA(EDGE_NUM), the edge data.
#
#    real XY(NODE_NUM,2), the node coordinates.
#
  print ( '' )
  print ( '  Edge pointers:' )
  print ( '' )
  print ( '  Node     First      Last' )
  print ( '' )
  for node in range ( 0, node_num ):
    print ( '  %4d  %8d  %8d'
      % ( node, edge_pointer[node], edge_pointer[node+1]-1 ) )

  print ( '' )
  print ( '  Edge data:' )
  print ( '' )
  print ( '  Node     Adjacent nodes' )
  print ( '' )

  for node in range ( 0, node_num ):
    print ( '  %4d' % ( node ), end = '' )
    for edge in range ( edge_pointer[node], edge_pointer[node+1] ):
      print ( '  %8d' % ( edge_data[edge] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  Node        X          Y' )
  print ( '' )

  for node in range ( 0, node_num ):
    print ( ' %4d  %10f  %10f' % ( node, xy[node,0], xy[node,1] ) )

  return

def grf_data_read ( filename, node_num, edge_num ):

#*****************************************************************************80
#
## grf_data_read() reads the data of a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
#  Output:
#
#    integer EDGE_POINTER(NODE_NUM+1), pointers to
#    the beginning of edge data for each node.
#
#    integer EDGE_DATA(EDGE_NUM), the edge data.
#
#    real XY(NODE_NUM,2), the node coordinates.
#
  import numpy as np

  edge_data = -1 * np.ones ( edge_num, dtype = int )
  edge_pointer = -1 * np.ones ( node_num + 1, dtype = int )
  xy = np.inf * np.ones ( [ node_num, 2 ], dtype = float )
#
#  Open the file.
#
  try:
    input_unit = open ( filename, 'rt' )
  except:
    print ( '' )
    print ( 'grf_data_read(): Fatal error!' )
    print ( '  Could not open the input file "' + filename + '"' )
    raise Exception ( 'grf_data_read(): Fatal error!' )
#
#  Read information about each node.
#
  edge = 0
  edge_pointer[0] = 0

  while ( True ):

    line = input_unit.readline ( )

    if ( len ( line ) == 0 ):
      break

    if ( line[0] == '#' ):
      continue

    word = line.strip().split()

    word_num = len ( word )

    if ( word_num < 3 ):
      print ( '' )
      print ( 'grf_data_read(): Fatal error!' )
      print ( '  Less than 3 items on an input line.' )
      raise Exception ( 'grf_data_read(): Fatal error!' )

    node_i = int ( word[0] )

    edge_pointer[node_i+1] = edge_pointer[node_i]
#
#  Extract the X, Y coordinates of the node.
#
    xy[node_i,0] = float ( word[1] )
    xy[node_i,1] = float ( word[2] )
#
#  Read the indices of the nodes to which the node is connected.
#
    for i in range ( 3, word_num ):

      node_j = int ( word[i] )
      edge_data[edge] = node_j
      edge_pointer[node_i+1] = edge_pointer[node_i+1] + 1
      edge = edge + 1

  input_unit.close ( )

  return edge_pointer, edge_data, xy

def grf_data_write ( output, node_num, edge_num, edge_pointer, edge_data, xy ):

#*****************************************************************************80
#
## grf_data_write() prints the data to a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Input:
#
#    file_object OUTPUT, the output device.
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
#    integer EDGE_POINTER(NODE_NUM+1), pointers to
#    the beginning of edge data for each node.
#
#    integer EDGE_DATA(EDGE_NUM), the edge data.
#
#    real XY(NODE_NUM,2), the node coordinates.
#
  for node in range ( 0, node_num ):
    output.write ( '  %4d  %10f  %10f' % ( node, xy[node,0], xy[node,1] ) )
    for edge in range ( edge_pointer[node], edge_pointer[node+1] ):
      output.write ( '  %4d' % ( edge_data[edge] ) )
    output.write ( '\n' )

  return

def grf_example ( node_num, edge_num ):

#*****************************************************************************80
#
## grf_example() sets up a GRF example.
#
#  Discussion:
#
#    The example is known as the Coxeter graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Input:
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
#  Output:
#
#    integer EDGE_POINTER(NODE_NUM+1), pointers to
#    the beginning of edge data for each node.
#
#    integer EDGE_DATA(EDGE_NUM), the edge data.
#
#    real XY(NODE_NUM,2), the node coordinates.
#
  import numpy as np

  edge_pointer = np.array ( [ \
    0,  3,  6,  9, 12, 15, 18, 21, 24, 27, \
   30, 33, 36, 39, 42, 45, 48, 51, 54, 57, \
   60, 63, 66, 69, 72, 75, 78, 81, 84 ] )

  edge_data = np.array ( [ \
     7,   1,   2, \
    13,   0,   4, \
     8,   3,   0, \
     9,   6,   2, \
    12,   1,   5, \
    11,   4,   6, \
    10,   5,   3, \
    24,  19,   0, \
    23,  20,   2, \
    22,  14,   3, \
    21,  15,   6, \
    27,  16,   5, \
    26,  17,   4, \
    25,  18,   1, \
     9,  17,  18, \
    10,  18,  19, \
    11,  20,  19, \
    12,  14,  20, \
    13,  15,  14, \
     7,  16,  15, \
     8,  17,  16, \
    10,  26,  23, \
     9,  27,  24, \
     8,  25,  21, \
     7,  22,  26, \
    13,  23,  27, \
    12,  24,  21, \
    11,  25,  22 ] )

  xy = np.array ( [ \
    [ 0.412,   0.984 ], \
    [ 0.494,   0.984 ], \
    [ 0.366,   0.926 ], \
    [ 0.388,   0.862 ], \
    [ 0.546,   0.926 ], \
    [ 0.518,   0.860 ], \
    [ 0.458,   0.818 ], \
    [ 0.152,   0.684 ], \
    [ 0.264,   0.682 ], \
    [ 0.354,   0.680 ], \
    [ 0.458,   0.670 ], \
    [ 0.554,   0.672 ], \
    [ 0.658,   0.668 ], \
    [ 0.774,   0.692 ], \
    [ 0.164,   0.450 ], \
    [ 0.228,   0.448 ], \
    [ 0.274,   0.390 ], \
    [ 0.242,   0.330 ], \
    [ 0.194,   0.278 ], \
    [ 0.146,   0.328 ], \
    [ 0.102,   0.390 ], \
    [ 0.668,   0.472 ], \
    [ 0.638,   0.416 ], \
    [ 0.656,   0.334 ], \
    [ 0.714,   0.270 ], \
    [ 0.798,   0.326 ], \
    [ 0.830,   0.408 ], \
    [ 0.754,   0.466] ] )

  return edge_pointer, edge_data, xy

def grf_example_size ( ):

#*****************************************************************************80
#
## grf_example_size() sizes a GRF example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Output:
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
  node_num = 28
  edge_num = 84

  return node_num, edge_num

def grf_header_print ( node_num, edge_num ):

#*****************************************************************************80
#
## grf_header_print() prints the header of a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Input:
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
  print ( '' )
  print ( '  The number of nodes NODE_NUM = ', node_num )
  print ( '  The number of edges EDGE_NUM = ', edge_num )

  return

def grf_header_read ( filename ):

#*****************************************************************************80
#
## grf_header_read() reads the header of a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Skiena,
#    Implementing Discrete Mathematics,
#    Combinatorics and Graph Theory with Mathematica,
#    Addison-Wesley, 1990.
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
  edge_num = -1
  node_num = -1
#
#  Open the file.
#
  try:
    input_unit = open ( filename, 'r' )
  except:
    print ( '' )
    print ( 'grf_header_read(): Fatal error!' )
    print ( '  Could not open the input file "' + filename + '"' )
    raise Exception ( 'grf_header_read(): Fatal error!' )
#
#  Read information about each node.
#
  node_num = 0
  edge_num = 0

  while ( True ):

    line = input_unit.readline ( )

    if ( len ( line ) == 0 ):
      break

    if ( line[0] == '#' ):
      continue

    words = line.strip().split()

    word_num = len ( words )

    if ( word_num < 3 ):
      print ( '' )
      print ( 'grf_header_read(): Fatal error!' )
      print ( '  Less than 3 items on an input line.' )
      raise Exception ( 'grf_header_read(): Fatal error!' )

    node_num = node_num + 1
    edge_num = edge_num + word_num - 3

  input_unit.close ( )

  return node_num, edge_num

def grf_header_write ( filename, output, node_num, edge_num ):

#*****************************************************************************80
#
## grf_header_write() writes the header of a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    file object OUTPUT, the output device.
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
  import time
#
#  Write the header.
#
  output.write ( '# ' + filename + '\n' )
  output.write ( '#  created by grf_io::grf_header_write.py\n' )
  output.write ( '#  on ' + time.ctime ( time.time ( ) ) )
  output.write ( '#\n' )
  output.write ( '#  Number of nodes  = ', node_num, '\n' )
  output.write ( '#  Number of edges =  ', edge_num, '\n' )
  output.write ( '#\n' )

  return

def grf_write ( filename, node_num, edge_num, edge_pointer, edge_data, xy ):

#*****************************************************************************80
#
## grf_write() writes a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer NODE_NUM, the number of nodes.
#
#    integer EDGE_NUM, the number of edges.
#
#    integer EDGE_POINTER(NODE_NUM+1), pointers to the
#    first edge item for each node.
#
#    integer EDGE_DATA(EDGE_NUM), indices of adjacent nodes.
#
#    real XY(NODE_NUM,2), the node coordinates.
#

#
#  Open the file.
#
  try:
    output = open ( filename, 'wt' )
  except:
    print ( '' )
    print ( 'grf_write(): Fatal error!' )
    print ( '  Could not open the output file "' + filename + '"' )
    raise Exception ( 'grf_write(): Fatal error!' )
#
#  Write the header.
#
  if ( False ):
    grf_header_write ( filename, output, node_num, edge_num )
#
#  Write the data.
#
  grf_data_write ( output, node_num, edge_num, edge_pointer, edge_data, xy )
#
#  Close the file.
#
  output.close ( )

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
  grf_io_test ( )
  timestamp ( )

