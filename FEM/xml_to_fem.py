#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d


def xml_read(filename):

    # *****************************************************************************80
    #
    # XML_READ reads mesh information from a DOLFIN or FENICS mesh XML file.
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
    #    Input, string FILENAME, the name of the XML file.
    #
    import numpy as np
    import xml.etree.ElementTree as ET

    tree = ET.parse(filename)

    root = tree.getroot()

    for alice in root:

        if alice.tag == 'mesh':

            celltype = alice.get('celltype')
            dim = int(alice.get('dim'))

            for bob in alice:

                if (bob.tag == 'vertices'):

                    node_num = int(bob.get('size'))

                    node_x = np.zeros((node_num, dim))

                    for carol in bob:

                        for dave in carol.attrib:
                            if (dave == 'index'):
                                index = int(carol.get('index'))

                        for dave in carol.attrib:
                            if (dave == 'x'):
                                x = float(carol.get('x'))
                                node_x[index, 0] = x
                            elif (dave == 'y'):
                                y = float(carol.get('y'))
                                node_x[index, 1] = y
                            elif (dave == 'z'):
                                z = float(carol.get('z'))
                                node_x[index, 2] = z

                elif (bob.tag == 'cells'):

                    elem_num = int(bob.get('size'))

                    if (celltype == 'interval'):
                        elem_order = 2
                    elif (celltype == 'triangle'):
                        elem_order = 3
                    elif (celltype == 'tetrahedron'):
                        elem_order = 4

                    elem_node = np.zeros((elem_num, elem_order))

                    for carol in bob:

                        for dave in carol.attrib:
                            if (dave == 'index'):
                                index = int(carol.get('index'))

                        for dave in carol.attrib:
                            if (dave == 'v0'):
                                v0 = int(carol.get('v0'))
                                elem_node[index, 0] = v0
                            elif (dave == 'v1'):
                                v1 = int(carol.get('v1'))
                                elem_node[index, 1] = v1
                            elif (dave == 'v2'):
                                v2 = int(carol.get('v2'))
                                elem_node[index, 2] = v2
                            elif (dave == 'v3'):
                                v3 = int(carol.get('v3'))
                                elem_node[index, 3] = v3

    return node_x, elem_node


def xml_to_fem(prefix):

    # *****************************************************************************80
    #
    # XML_TO_FEM converts XML data to FEM format.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string PREFIX, the common filename prefix.
    #
    filename_xml = prefix + '.xml'

    print('')
    print('  Read the XML file "%s"' % (filename_xml))

    node_x, elem_node = xml_read(filename_xml)

    node_x_shape = node_x.shape
    node_num = node_x_shape[0]
    dim_num = node_x_shape[1]
    print('  Spatial dimension = %d' % (dim_num))
    print('  Number of nodes = %d' % (node_num))

    elem_node_shape = elem_node.shape
    elem_num = elem_node_shape[0]
    elem_order = elem_node_shape[1]
    print('  Element order = %d' % (elem_order))
    print('  Number of elements = %d' % (elem_num))

    print('')
    print('  NODE_X array of node coordinates:')
    print('')
    for i in range(0, node_num):
        for j in range(0, dim_num):
            print('  %g' % (node_x[i][j]), end='')
        print('')

    print('')
    print('  ELEM_NODE array of node indices:')
    print('')
    for i in range(0, elem_num):
        for j in range(0, elem_order):
            print('  %d' % (elem_node[i][j]), end='')
        print('')

    filename_elements = prefix + '_elements.txt'
    i4mat_write(filename_elements, elem_num, elem_order, elem_node)

    filename_nodes = prefix + '_nodes.txt'
    r8mat_write(filename_nodes, node_num, dim_num, node_x)

    return


def xml_to_fem_test():

    # *****************************************************************************80
    #
    # XML_TO_FEM_TEST tests XML_TO_FEM.
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

    print('')
    print('XML_TO_FEM_TEST.')
    print('  Python version: %s' % (platform.python_version()))
    print('  Read a DOLFIN/FENICS XML mesh file.')
    print('  Extract the coordinate and element information.')

    xml_to_fem('cheby9')
    xml_to_fem('rectangle')
    xml_to_fem('tet_mesh')
#
#  Terminate.
#
    print('')
    print('XML_TO_FEM_TEST.')
    print('  Normal end of execution')
    return


def i4mat_write(filename, m, n, a):

    # *****************************************************************************80
    #
    # I4MAT_WRITE writes an I4MAT to a file.
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
    #    Input, string FILENAME, the name of the output file.
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, integer A(M,N), the matrix.
    #
    output = open(filename, 'w')

    for i in range(0, m):
        for j in range(0, n):
            s = '  %d' % (a[i, j])
            output.write(s)
        output.write('\n')

    output.close()

    return


def i4mat_write_test():

    # *****************************************************************************80
    #
    # I4MAT_WRITE_TEST tests I4MAT_WRITE.
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
    import numpy as np
    import platform

    print('')
    print('I4MAT_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4MAT_WRITE writes an I4MAT to a file.')

    filename = 'i4mat_write_test.txt'
    m = 5
    n = 3
    a = np.array((
        (11, 12, 13),
        (21, 22, 23),
        (31, 32, 33),
        (41, 42, 43),
        (51, 52, 53)))
    i4mat_write(filename, m, n, a)

    print('')
    print('  Created file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('I4MAT_WRITE_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_write(filename, m, n, a):

    # *****************************************************************************80
    #
    # R8MAT_WRITE writes an R8MAT to a file.
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
    #    Input, string FILENAME, the name of the output file.
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    output = open(filename, 'w')

    for i in range(0, m):
        for j in range(0, n):
            s = '  %g' % (a[i, j])
            output.write(s)
        output.write('\n')

    output.close()

    return


def r8mat_write_test():

    # *****************************************************************************80
    #
    # R8MAT_WRITE_TEST tests R8MAT_WRITE.
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
    import numpy as np
    import platform

    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test R8MAT_WRITE, which writes an R8MAT to a file.')

    filename = 'r8mat_write_test.txt'
    m = 5
    n = 3
    a = np.array((
        (1.1, 1.2, 1.3),
        (2.1, 2.2, 2.3),
        (3.1, 3.2, 3.3),
        (4.1, 4.2, 4.3),
        (5.1, 5.2, 5.3)))
    r8mat_write(filename, m, n, a)

    print('')
    print('  Created file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Normal end of execution.')
    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
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

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
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

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    xml_to_fem_test()
    timestamp()
