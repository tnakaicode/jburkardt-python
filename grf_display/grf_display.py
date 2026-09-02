#! /usr/bin/env python3
#
def grf_display_test ( ):

#*****************************************************************************80
#
## grf_display_test() tests grf_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'grf_display_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test grf_display.' )

  grf_display ( )

  grf_display ( 'simple' )

  grf_display ( 'coxeter' )
#
#  Terminate.
#
  print ( '' )
  print ( 'grf_display_test():' )
  print ( '  Normal end of execution.' )

  return

def grf_display ( prefix = None ):

#*****************************************************************************80
#
## grf_display() displays a mathematical graph stored in a GRF file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Usage:
#
#    grf_display ( 'prefix' )
#
#    where
#
#    'prefix'.grf is the name of the GRF file to display.
#
#  Input:
#
#    string PREFIX, the prefix of the input files.
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  import pprint

  print ( '' )
  print ( 'grf_display():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Read a GRF file describing an abstract graph, and plot it.' )
#
#  Read the GRF data.
#
  if ( prefix == None ):

    prefix = 'grf_display'

    grf_filename = prefix + '.grf'

    print ( '' )
    print ( '  No GRF file specified.  Will display default example.' )

    node_num, edge_num = grf_example_size ( )

    grf_header_print ( node_num, edge_num )

    edge_pointer, edge_data, xy = grf_example ( node_num, edge_num )

  else:

    grf_filename = prefix + '.grf'

    print ( '' )
    print ( '  Processing GRF file "' + grf_filename + '".' )

    node_num, edge_num = grf_header_read ( grf_filename )

    grf_header_print ( node_num, edge_num )

    edge_pointer, edge_data, xy = grf_data_read ( grf_filename, node_num, \
      edge_num )
#
#  Convert the GRF data to XY, XYL data.
#
  line_num = 0
  line_data_num = 0
  line_pointer = []
  line_pointer.append ( 1 )
  line_data = []

  for node_i in range ( 0, node_num ):
    for edge in range ( edge_pointer[node_i], edge_pointer[node_i+1] ):

      node_j = edge_data[edge]

      line_data_num = line_data_num + 1
      line_data.append ( node_i )
      line_data_num = line_data_num + 1
      line_data.append ( node_j )

      line_num = line_num + 1
      line_pointer.append ( line_data_num + 1 )
#
#  Draw the picture.
#
  plt.clf ( )
#
#  Draw the lines first.
#
  for i in range ( 0, line_num ):
    for index in range ( line_pointer[i], line_pointer[i+1] - 1 ):
      p = [ line_data[index-1], line_data[index] ]
      plt.plot ( xy[p,0], xy[p,1], linewidth = 2.0, color = 'red' )
#
#  Display the nodes.
#
  plt.scatter ( xy[:,0], xy[:,1], s = 80, color = 'blue' )
#
#  Annotate the graph.
#
#  The TITLE function will interpret underscores in the title.
#  We need to unescape such escape sequences!
#
  plt.title ( prefix )

  plt.axis ( 'equal' )
#
#  Suppress the axis markings, axis lines, and, unfortunately,
#  the white background.
#
  plt.axis ( 'off' )
#
#  End of plot commands.
#
  filename = prefix + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

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

def s_escape_tex ( s1 ):

#*****************************************************************************80
#
## s_escape_tex() de-escapes TeX escape sequences.
#
#  Discussion:
#
#    In particular, every occurrence of the characters '\', '_',
#    '^', '{' and '}' will be replaced by '\\', '\_', '\^',
#    '\{' and '\}'.  A TeX interpreter, on seeing these character
#    strings, is then likely to return the original characters.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S1, the string to be de-escaped.
#
#  Output:
#
#    string S2, a copy of the string, modified to avoid TeX escapes.
#
  s1_length = len ( s1 )

  s1_pos = 0
  s2_pos = 0
  s2 = ''

  while ( s1_pos < s1_length ):

    if ( s1[s1_pos] == '\\' or \
         s1[s1_pos] == '_' or \
         s1[s1_pos] == '^' or \
         s1[s1_pos] == '{' or \
         s1[s1_pos] == '}' ):
      s2_pos = s2_pos + 1
      s2 = s2 + '\\'

    s2_pos = s2_pos + 1
    s2 = s2 + s1[s1_pos]

    s1_pos = s1_pos + 1

  return s2

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
  grf_display_test ( )
  timestamp ( )

