#! /usr/bin/env python3
#
def fem_to_xml ( prefix ):

#*****************************************************************************80
#
## FEM_TO_XML converts mesh data from FEM to DOLFIN XML format.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem_to_xml/fem_to_xml.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string PREFIX, the common filename prefix.
#
  import numpy as np

  filename_elements = prefix + '_elements.txt'
  filename_nodes = prefix + '_nodes.txt'
  filename_xml = prefix + '.xml'

  node_num, dim_num = r8mat_header_read ( filename_nodes )
  print ( '' )
  print ( '  Number of nodes = ', node_num )
  print ( '  Spatial dimension = ', dim_num )

  node_x = r8mat_data_read ( filename_nodes, node_num, dim_num )

  element_num, element_order = i4mat_header_read ( filename_elements )

  print ( '' )
  print ( '  Number of elements = ', element_num )
  print ( '  Element order = ', element_order )

  element_node = i4mat_data_read ( filename_elements, element_num, element_order )

  if ( dim_num == 1 ):
    xml_mesh1d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node )
  elif ( dim_num == 2 ):
    xml_mesh2d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node )
  elif ( dim_num == 3 ):
    xml_mesh3d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node )
  else:
    print ( '' )
    print ( 'fem_to_xml: Fatal error!' )
    print ( '  dim_num is not 1, 2 or 3.' )

  return

def mesh_base_zero ( node_num, element_order, element_num, element_node ):

#*****************************************************************************80
#
## MESH_BASE_ZERO ensures that the element definition is zero-based.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input/output, integer ELEMENT_NODE[ELEMENT_NUM,ELEMENT_ORDER], the element
#    definitions.
#
  i4_huge = 2147483647
  node_min = + i4_huge
  node_max = - i4_huge
  for j in range ( 0, element_order ):
    for i in range ( 0, element_num ):
      node_min = min ( node_min, element_node[i,j] )
      node_max = max ( node_max, element_node[i,j] )

  if ( node_min == 0 and node_max == node_num - 1 ):
    print ( '' )
    print ( 'MESH_BASE_ZERO:' )
    print ( '  The element indexing appears to be 0-based!' )
    print ( '  No conversion is necessary.' )
  elif ( node_min == 1 and node_max == node_num ):
    print ( '' )
    print ( 'MESH_BASE_ZERO:' )
    print ( '  The element indexing appears to be 1-based!' )
    print ( '  This will be converted to 0-based.' )
    for j in range ( 0, element_order ):
      for i in range ( 0, element_num ):
        element_node[i,j] = element_node[i,j] - 1
  else:
    print ( '' )
    print ( 'MESH_BASE_ZERO - Warning!' )
    print ( '  The element indexing is not of a recognized type.' )
    print ( '  NODE_MIN = %d' % ( node_min ) )
    print ( '  NODE_MAX = %d' % ( node_max ) )
    print ( '  NODE_NUM = %d' % ( node_num ) )

  return element_node

def xml_mesh1d_write ( filename_xml, node_num, dim_num, element_num, \
  element_order, node_x, element_node ):

#*****************************************************************************80
#
## XML_MESH1D_WRITE writes 1D mesh data to a DOLFIN XML file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME_XML, the name of the XML file.
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, real NODE_X(NODE_NUM,DIM_NUM), the node coordinates.
#
#    Input, integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#

#
#  Enforce 0-based indexing.
#
  element_node = mesh_base_zero ( node_num, element_order, element_num, element_node );

  output = open ( filename_xml, 'w' )

  output.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
  output.write ( '<dolfin xmlns:dolfin="http://www.fenics.org/dolfin/">\n' )
  output.write ( '  <mesh celltype="interval" dim="1">\n' );

  output.write ( '    <vertices size="' + repr ( node_num ) + '">\n' )
  for i in range ( 0, node_num ):
    output.write ( '      <vertex index="' + repr ( i ) + '"')
    output.write ( ' x="' + repr ( node_x[i,0] ) + '"/>\n' )

  output.write ( '    </vertices>\n' )

  output.write ( '    <cells size="' + repr ( element_num ) + '">\n' )
  for i in range ( 0, element_num ):
    output.write ( '      <interval index="' + repr ( i ) + '"' )
    for j in range ( 0, element_order ):
      output.write ( ' v' + repr ( j ) + '="' + repr ( element_node[i,j] ) + '"' )
    output.write ( '/>\n' );
  output.write ( '    </cells>\n' )
  output.write ( '  </mesh>\n' )
  output.write ( '</dolfin>\n' )

  output.close ( )

  return

def xml_mesh2d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node ):

#*****************************************************************************80
#
## XML_MESH2D_WRITE writes 2D mesh data to a DOLFIN XML file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME_XML, the name of the XML file.
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, real NODE_X(NODE_NUM,DIM_NUM), the node coordinates.
#
#    Input, integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#

#
#  Enforce 0-based indexing.
#
  element_node = mesh_base_zero ( node_num, element_order, element_num, element_node );

  output = open ( filename_xml, 'w' )

  output.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
  output.write ( '<dolfin xmlns:dolfin="http://www.fenics.org/dolfin/">\n' )
  output.write ( '  <mesh celltype="triangle" dim="2">\n' );

  output.write ( '    <vertices size="' + repr ( node_num ) + '">\n' )
  for i in range ( 0, node_num ):
    output.write ( '      <vertex index="' + repr ( i ) + '"')
    output.write ( ' x="' + repr ( node_x[i,0] ) + '"' )
    output.write ( ' y="' + repr ( node_x[i,1] ) + '"/>\n' )

  output.write ( '    </vertices>\n' )

  output.write ( '    <cells size="' + repr ( element_num ) + '">\n' )
  for i in range ( 0, element_num ):
    output.write ( '      <triangle index="' + repr ( i ) + '"' )
    for j in range ( 0, element_order ):
      output.write ( ' v' + repr ( j ) + '="' + repr ( element_node[i,j] ) + '"' )
    output.write ( '/>\n' );
  output.write ( '    </cells>\n' )
  output.write ( '  </mesh>\n' )
  output.write ( '</dolfin>\n' )

  output.close ( )

  return

def xml_mesh3d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node ):

#*****************************************************************************80
#
## XML_MESH3D_WRITE writes 3D mesh data to a DOLFIN XML file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME_XML, the name of the XML file.
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, real NODE_X(NODE_NUM,DIM_NUM), the node coordinates.
#
#    Input, integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#

#
#  Enforce 0-based indexing.
#
  element_node = mesh_base_zero ( node_num, element_order, element_num, element_node );

  output = open ( filename_xml, 'w' )

  output.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
  output.write ( '<dolfin xmlns:dolfin="http://www.fenics.org/dolfin/">\n' )
  output.write ( '  <mesh celltype="tetrahedron" dim="3">\n' );

  output.write ( '    <vertices size="' + repr ( node_num ) + '">\n' )
  for i in range ( 0, node_num ):
    output.write ( '      <vertex index="' + repr ( i ) + '"')
    output.write ( ' x="' + repr ( node_x[i,0] ) + '"' )
    output.write ( ' y="' + repr ( node_x[i,1] ) + '"' )
    output.write ( ' z="' + repr ( node_x[i,2] ) + '"/>\n' )

  output.write ( '    </vertices>\n' )

  output.write ( '    <cells size="' + repr ( element_num ) + '">\n' )
  for i in range ( 0, element_num ):
    output.write ( '      <tetrahedron index="' + repr ( i ) + '"' )
    for j in range ( 0, element_order ):
      output.write ( ' v' + repr ( j ) + '="' + repr ( element_node[i,j] ) + '"' )
    output.write ( '/>\n' );
  output.write ( '    </cells>\n' )
  output.write ( '  </mesh>\n' )
  output.write ( '</dolfin>\n' )

  output.close ( )

  return

def fem_to_xml_test ( ):

#*****************************************************************************80
#
## FEM_TO_XML_TEST tests a 1D, 2D and 3D mesh.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FEM_TO_XML_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read mesh data from FEM files.' )
  print ( '  Write mesh data to equivalent XML file.' )
  print ( '' )

  prefix = 'cheby9'
  print ( '  Using common file prefix "%s"' % ( prefix ) )
  fem_to_xml ( prefix )

  prefix = 'rectangle'
  print ( '  Using common file prefix "%s"' % ( prefix ) )
  fem_to_xml ( prefix )

  prefix = 'tet_mesh'
  print ( '  Using common file prefix "%s"' % ( prefix ) )
  fem_to_xml ( prefix )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM_TO_XML_TEST:' )
  print ( '  Normal end of execution.' )
  return

def file_column_count ( filename ):

#*****************************************************************************80
#
## FILE_COLUMN_COUNT counts the number of words in a typical column of a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the file.
#
#    Output, integer COLUMN_COUNT, the number of words in a typical column.
#
  column_count = -1

  input = open ( filename, 'r' )

  column_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      elif ( column_count == 0 ):
        column_count = wc
        break

  input.close ( )

  return column_count

def file_column_count_test ( ):

#*****************************************************************************80
#
## FILE_COLUMN_COUNT_TEST tests FILE_COLUMN_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FILE_COLUMN_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of columns in a typical text file line.' )

  filename = 'r8mat_write_test.txt'
  column_count = file_column_count ( filename )

  print ( '' )
  print ( '  Number of columns in "%s" is %d' % ( filename, column_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_COLUMN_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def file_row_count ( filename ):

#*****************************************************************************80
#
## FILE_ROW_COUNT counts the number of rows (lines) in a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the file.
#
#    Output, integer ROW_COUNT, the number of rows in the file.
#
  row_count = -1

  input = open ( filename, 'r' )

  row_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      else:
        row_count = row_count + 1

  input.close ( )

  return row_count

def file_row_count_test ( ):

#*****************************************************************************80
#
## FILE_ROW_COUNT_TEST tests FILE_ROW_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FILE_ROW_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of rows in a text file.' )

  filename = 'i4mat_write_test.txt'
  row_count = file_row_count ( filename )

  print ( '' )
  print ( '  Number of rows in "%s" is %d' % ( filename, row_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_ROW_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_data_read ( filename, m, n ):

#*****************************************************************************80
#
## I4MAT_DATA_READ reads the data from an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Input, integer M, the number of rows in the file.
#
#    Input, integer N, the number of columns in the file.
#
#    Output, integer TABLE(M,N), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( ( m, n ), dtype=np.int )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      j = 0
      for word in line.strip().split():
        table[i,j] = int ( word )
        j = j + 1
      i = i + 1

  input.close ( )

  return table

def i4mat_data_read_test ( ):

#*****************************************************************************80
#
## I4MAT_DATA_READ_TEST tests I4MAT_DATA_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4MAT_DATA_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test I4MAT_DATA_READ, which reads data from an I4MAT.' )

  m = 5
  n = 3
  filename = 'i4mat_write_test.txt'
  a = i4mat_data_read ( filename, m, n )
  i4mat_print ( m, n, a, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_DATA_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_header_read ( filename ):

#*****************************************************************************80
#
## I4MAT_HEADER_READ reads the header from an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Output, integer M, the number of rows in the file.
#
#    Output, integer N, the number of columns in the file.
#
  m = file_row_count ( filename )
  n = file_column_count ( filename )

  return m, n

def i4mat_header_read_test ( ):

#*****************************************************************************80
#
## I4MAT_HEADER_READ_TEST tests I4MAT_HEADER_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4MAT_HEADER_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_HEADER_READ counts rows and columns in a file' )
  print ( '  containing an I4MAT.' )

  filename = 'i4mat_write_test.txt'
  m, n = i4mat_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows and %d columns.' % ( filename, m, n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_HEADER_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_data_read ( filename, m, n ):

#*****************************************************************************80
#
## R8MAT_DATA_READ reads the data from an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Input, integer M, the number of rows in the file.
#
#    Input, integer N, the number of columns in the file.
#
#    Output, real TABLE(M,N), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( ( m, n ) )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      j = 0
      for word in line.strip().split():
        table[i,j] = float ( word )
        j = j + 1
      i = i + 1

  input.close ( )

  return table

def r8mat_data_read_test ( ):

#*****************************************************************************80
#
## R8MAT_DATA_READ_TEST tests R8MAT_DATA_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8MAT_DATA_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DATA_READ reads data from an R8MAT.' )

  m = 5
  n = 3
  filename = 'r8mat_write_test.txt'
  a = r8mat_data_read ( filename, m, n )
  r8mat_print ( m, n, a, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_DATA_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_header_read ( filename ):

#*****************************************************************************80
#
## R8MAT_HEADER_READ reads the header from an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Output, integer M, the number of columns in the file.
#
#    Output, integer N, the number of rows in the file.
#
  m = file_row_count ( filename )
  n = file_column_count ( filename )

  return m, n

def r8mat_header_read_test ( ):

#*****************************************************************************80
#
## R8MAT_HEADER_READ_TEST tests R8MAT_HEADER_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_HEADER_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HEADER_READ counts rows and columns in a file' )
  print ( '  containing an R8MAT.' )

  filename = 'r8mat_write_test.txt'
  m, n = r8mat_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows and %d columns.' % ( filename, m, n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HEADER_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  fem_to_xml_test ( )
  timestamp ( )

