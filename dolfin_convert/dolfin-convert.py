#! /usr/bin/env python3
#
# Copyright (C) 2006 Anders Logg
# Licensed under the GNU LGPL Version 2.1
#
# Modified by Garth N. Wells (gmsh function)
# Modified by Alexander H. Jarosch (gmsh fix)
# Modified by Angelo Simone (Gmsh and Medit fix)
# Modified by Andy R. Terrel (gmsh fix)
# Modified by Magnus Vikstrom (metis and scotch function)
#
# Script for converting between various data formats

import getopt
import sys


def main(argv):

    # *****************************************************************************80
    #
    # MAIN is the main function for DOLFIN-CONVERT.
    #
    #  Usage:
    #
    #    dolfin-convert input_filename output_filename
    #
    "Main function"

    #
    #  Get the command-line arguments.
    #
    try:
        opts, args = getopt.getopt(
            argv, "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    #
    #  Get options
    #
    input_format = ""
    output_format = ""

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            input_format = arg
        elif opt in ("-o", "--output"):
            output_format = arg

    #
    #  Check that we got two filenames.
    #
    if not len(args) == 2:
        usage()
        sys.exit(2)

    #
    #  Get filenames and suffixes
    #
    ifilename = args[0]
    ofilename = args[1]
    isuffix = ifilename.split(".")[-1]
    osuffix = ofilename.split(".")[-1]

    #
    # Choose format based on suffixes if not specified
    #
    if input_format == "":
        input_format = format_from_suffix(isuffix)
    if output_format == "":
        output_format = format_from_suffix(osuffix)

    #
    #  Choose conversion:
    #    MESH          => XML
    #    GMSH          => XML
    #    XML-OLD       => XML
    #    METIS Graph   => DOLFIN Graph XML
    #    SCOTCH Graph  => DOLFIN Graph XML
    #
    if input_format == "mesh" and output_format == "xml":
        mesh2xml(ifilename, ofilename)
    elif input_format == "gmsh" and output_format == "xml":
        gmsh2xml(ifilename, ofilename)
    elif input_format == "xml-old" and output_format == "xml":
        xml_old2xml(ifilename, ofilename)
    elif input_format == "metis" and output_format == "xml":
        metis_graph2graph_xml(ifilename, ofilename)
    elif input_format == "scotch" and output_format == "xml":
        scotch_graph2graph_xml(ifilename, ofilename)
    else:
        error("Cannot convert between .%s and .%s formats." %
              (isuffix, osuffix))


def usage():

    # *****************************************************************************80
    #
    # USAGE prints the program usage statement.
    #
    print("Display usage")
    print("")
    print("Usage: dolfin-convert [OPTIONS] ... input.x output.y")
    print("")
    print("Options:")
    print("")
    print("  -h         display this help text and exit")
    print("  -i format  specify input format")
    print("  -o format  specify output format")
    print("")
    print("Alternatively, the following long options may be used:")
    print("")
    print("  --help     same as -h")
    print("  --input    same as -i")
    print("  --output   same as -o")
    print("")
    print("Supported formats:")
    print("")
    print("  xml     - DOLFIN XML mesh format (current)")
    print("  xml-old - DOLFIN XML mesh format (DOLFIN 0.6.2 and earlier)")
    print("  mesh    - Medit, generated by tetgen with option -g")
    print("  gmsh    - Gmsh, version 2.0 file format")
    print("  metis   - Metis graph file format")
    print("  scotch  - Scotch graph file format")
    print("")
    print("If --input or --output are not specified, the format will")
    print("be deduced from the suffix:")
    print("")
    print("  .xml  - xml")
    print("  .mesh - mesh")
    print("  .gmsh - gmsh")
    print("  .msh  - gmsh")
    print("  .gra  - metis")
    print("  .grf  - scotch")


def format_from_suffix(suffix):

    # *****************************************************************************80
    #
    # FORMAT_FROM_SUFFIX determines the format from the file suffix.
    #
    "Return format for given suffix"

    if suffix == "xml":
        return "xml"
    elif suffix == "mesh":
        return "mesh"
    elif suffix == "gmsh":
        return "gmsh"
    elif suffix == "msh":
        return "gmsh"
    elif suffix == "gra":
        return "metis"
    elif suffix == "grf":
        return "scotch"
    else:
        error("Sorry, unknown suffix %s." % suffix)


def error(message):

    # *****************************************************************************80
    #
    # ERROR prints an error message and exits.
    #
    "Write an error message"

    for line in message.split("\n"):
        print("*** %s" % line)

    sys.exit(2)


def mesh2xml(ifilename, ofilename):

    # *****************************************************************************80
    #
    # MESH2XML converts from MESH to XML format.
    #
    #  Modified:
    #
    #    18 October 2014
    #
    """
    Convert between .mesh and .xml, parser implemented as a
    state machine:

        0 = read 'Dimension'
        1 = read dimension
        2 = read 'Vertices'
        3 = read number of vertices
        4 = read next vertex
        5 = read 'Triangles' or 'Tetrahedra'
        6 = read number of cells
        7 = read next cell
        8 = done

    """

    print("Converting from Medit format (.mesh) to DOLFIN XML format")
    ifile = open(ifilename, "r")
    ofile = open(ofilename, "w")

    #
    # Scan file for cell type
    #
    cell_type = None
    dim = 0
    while 1:
        #
        # Read next line
        #
        line = ifile.readline()
        if not line:
            break

        #
        # Remove newline
        #
        if line[-1] == "\n":
            line = line[:-1]

        #
        # Read dimension
        #
        if line == "Dimension":
            line = ifile.readline()
            num_dims = int(line)
            if num_dims == 1:
                cell_type = "interval"
                dim = 1
            elif num_dims == 2:
                cell_type = "triangle"
                dim = 2
            elif num_dims == 3:
                cell_type = "tetrahedron"
                dim = 3
            break

    #
    # Check that we got the cell type
    #
    if cell_type == None:
        error("Unable to find cell type.")

    #
    # Step to beginning of file
    #
    ifile.seek(0)

    #
    # Write header
    #
    write_header_mesh(ofile, cell_type, dim)

    #
    # Current state
    #
    state = 0

    #
    # Write data
    #
    num_vertices_read = 0
    num_cells_read = 0

    while 1:

        # Read next line
        line = ifile.readline()
        if not line:
            break

        # Skip comments
        if line[0] == '#':
            continue

        # Remove newline
        if line[-1] == "\n":
            line = line[:-1]

        if state == 0:
            if line == "Dimension":
                state += 1
        elif state == 1:
            num_dims = int(line)
            state += 1
        elif state == 2:
            if line == "Vertices":
                state += 1
        elif state == 3:
            num_vertices = int(line)
            write_header_vertices(ofile, num_vertices)
            state += 1
        elif state == 4:
            if num_dims == 1:
                (x, tmp1, tmp2) = line.split()
                x = float(x)
                y = 0.0
                z = 0.0
            elif num_dims == 2:
                (x, y, tmp) = line.split()
                x = float(x)
                y = float(y)
                z = 0.0
            elif num_dims == 3:
                (x, y, z, tmp) = line.split()
                x = float(x)
                y = float(y)
                z = float(z)
            write_vertex(ofile, num_vertices_read, x, y, z)
            num_vertices_read += 1
            if num_vertices == num_vertices_read:
                write_footer_vertices(ofile)
                state += 1
        elif state == 5:
            if line == "Intervals" and num_dims == 1:
                state += 1
            if line == "Triangles" and num_dims == 2:
                state += 1
            if line == "Tetrahedra" and num_dims == 3:
                state += 1
        elif state == 6:
            num_cells = int(line)
            write_header_cells(ofile, num_cells)
            state += 1
        elif state == 7:
            if num_dims == 1:
                (n0, n1, tmp1, tmp2) = line.split()
                n0 = int(n0) - 1
                n1 = int(n1) - 1
                write_cell_interval(ofile, num_cells_read, n0, n1)
            elif num_dims == 2:
                (n0, n1, n2, tmp) = line.split()
                n0 = int(n0) - 1
                n1 = int(n1) - 1
                n2 = int(n2) - 1
                write_cell_triangle(ofile, num_cells_read, n0, n1, n2)
            elif num_dims == 3:
                (n0, n1, n2, n3, tmp) = line.split()
                n0 = int(n0) - 1
                n1 = int(n1) - 1
                n2 = int(n2) - 1
                n3 = int(n3) - 1
                write_cell_tetrahedron(ofile, num_cells_read, n0, n1, n2, n3)
            num_cells_read += 1
            if num_cells == num_cells_read:
                write_footer_cells(ofile)
                state += 1
        elif state == 8:
            break

    #
    # Check that we got all data
    #
    if state == 8:
        print("Conversion done")
    else:
        error("Missing data, unable to convert")

    #
    # Write footer
    #
    write_footer_mesh(ofile)
    ifile.close()
    ofile.close()


def gmsh2xml(ifilename, ofilename):
    #
    # GMSH2XML converts a Gmsh msh file to Dolfin XML format.
    #
    #  Discussion:
    #
    #    This function can only handle triangles and tetrahedrons.
    #
    #  Modified:
    #
    #    18 October 2014
    #
    """
    Convert between .gmsh v2.0 format (http://www.geuz.org/gmsh/) and .xml, 
    parser implemented as a state machine:

        0 = read 'MeshFormat'
        1 = read  mesh format data
        2 = read 'EndMeshFormat'
        3 = read 'Nodes'
        4 = read  number of vertices
        5 = read  vertices
        6 = read 'EndNodes'
        7 = read 'Elements'
        8 = read  number of cells
        9 = read  cells
        10 = done

    """

    print("Converting from Gmsh format (.msh, .gmsh) to DOLFIN XML format")
    print("Hello")

    ifile = open(ifilename, "r")
    ofile = open(ofilename, "w")

    #
    #  Scan file for cell type
    #
    cell_type = None
    dim = 0
    line = ifile.readline()
    while line:

        # Remove newline
        if line[-1] == "\n":
            line = line[:-1]

        # Read dimension
        if line.find("$Elements") == 0:

            line = ifile.readline()
            num_cells = int(line)
            num_cells_counted = 0
            if num_cells == 0:
                error("No cells found in gmsh file.")
            line = ifile.readline()

            #
            #  Now iterate through elements to find largest dimension.
            #
            #  Gmsh format might include elements of lower dimensions in the element list.
            #
            #  We also need to count number of elements of correct dimensions.
            #
            #  Also determine which vertices are not used.
            #
            dim_2_count = 0
            dim_3_count = 0
            vertices_2_used = []
            vertices_3_used = []
            while line.find("$EndElements") == -1:
                element = line.split()
                elem_type = int(element[1])
                num_tags = int(element[2])
                if elem_type == 2:
                    if dim < 2:
                        cell_type = "triangle"
                        dim = 2
                    node_num_list = [int(node)
                                     for node in element[3 + num_tags:]]
                    vertices_2_used.extend(node_num_list)
                    dim_2_count += 1
                elif elem_type == 4:
                    if dim < 3:
                        cell_type = "tetrahedron"
                        dim = 3
                        vertices_2_used = None
                    node_num_list = [int(node)
                                     for node in element[3 + num_tags:]]
                    vertices_3_used.extend(node_num_list)
                    dim_3_count += 1
                line = ifile.readline()
        else:
            # Read next line
            line = ifile.readline()

    #
    #  Check that we got the cell type and set num_cells_counted
    #
    # if cell_type == None:
    #     error("Unable to find cell type.")

    if dim == 3:
        num_cells_counted = dim_3_count
        vertex_set = set(vertices_3_used)
        vertices_3_used = None
    elif dim == 2:
        num_cells_counted = dim_2_count
        vertex_set = set(vertices_2_used)
        vertices_2_used = None
    else:
        num_cells_counted = dim_2_count
        vertex_set = set(vertices_2_used)
        vertices_2_used = None

    vertex_dict = {}

    for n, v in enumerate(vertex_set):
        vertex_dict[v] = n
    #
    # Step to beginning of file
    #
    ifile.seek(0)
    #
    # Write header
    #
    write_header_mesh(ofile, cell_type, dim)
    #
    # Initialize node list (gmsh does not export all vertexes in order)
    #
    nodelist = {}
    #
    # Current state
    #
    state = 0
    #
    # Write data
    #
    num_vertices_read = 0
    num_cells_read = 0

    while state != 10:

        # Read next line
        line = ifile.readline()
        if not line:
            break

        # Skip comments
        if line[0] == '#':
            continue

        # Remove newline
        if line[-1] == "\n":
            line = line[:-1]

        if state == 0:
            if line == "$MeshFormat":
                state = 1
        elif state == 1:
            (version, file_type, data_size) = line.split()
            state = 2
        elif state == 2:
            if line == "$EndMeshFormat":
                state = 3
        elif state == 3:
            if line == "$Nodes":
                state = 4
        elif state == 4:
            #num_vertices = int(line)
            num_vertices = len(vertex_dict)
            write_header_vertices(ofile, num_vertices)
            state = 5
        elif state == 5:
            (node_no, x, y, z) = line.split()
            # if vertex_dict.keys(int(node_no)):
            #    node_no = vertex_dict[int(node_no)]
            # else:
            #    continue
            node_no = vertex_dict[int(node_no)]
            nodelist[int(node_no)] = num_vertices_read
            x = float(x)
            y = float(y)
            z = float(z)
            write_vertex(ofile, num_vertices_read, x, y, z)
            num_vertices_read += 1

            if num_vertices == num_vertices_read:
                write_footer_vertices(ofile)
                state = 6
        elif state == 6:
            if line == "$EndNodes":
                state = 7
        elif state == 7:
            if line == "$Elements":
                state = 8
        elif state == 8:
            write_header_cells(ofile, num_cells_counted)
            state = 9
        elif state == 9:
            element = line.split()
            elem_type = int(element[1])
            num_tags = int(element[2])
            if elem_type == 2 and dim == 2:
                node_num_list = [vertex_dict[int(node)]
                                 for node in element[3 + num_tags:]]
                for node in node_num_list:
                    if not node in nodelist:
                        error("Vertex %d of triangle %d not previously defined." %
                              (node, num_cells_read))
                n0 = nodelist[node_num_list[0]]
                n1 = nodelist[node_num_list[1]]
                n2 = nodelist[node_num_list[2]]
                write_cell_triangle(ofile, num_cells_read, n0, n1, n2)
                num_cells_read += 1
            elif elem_type == 4 and dim == 3:
                node_num_list = [vertex_dict[int(node)]
                                 for node in element[3 + num_tags:9]]
                for node in node_num_list:
                    if not node in nodelist:
                        error("Vertex %d of tetrahedron %d not previously defined." %
                              (node, num_cells_read))
                n0 = nodelist[node_num_list[0]]
                n1 = nodelist[node_num_list[1]]
                n2 = nodelist[node_num_list[2]]
                n3 = nodelist[node_num_list[3]]
                write_cell_tetrahedron(ofile, num_cells_read, n0, n1, n2, n3)
                num_cells_read += 1

            if num_cells_counted == num_cells_read:
                write_footer_cells(ofile)
                state = 10
        elif state == 10:
            break

    #
    # Check that we got all data
    #
    if state == 10:
        print("Conversion done")
    else:
        error("Missing data, unable to convert \n\ Did you use version 2.0 of the gmsh file format?")

    write_footer_mesh(ofile)
    ifile.close()
    ofile.close()


def xml_old2xml(ifilename, ofilename):

    #
    # XML_OLD2XML converts from the old to the new DOLFIN XML format.
    #
    "Convert from old DOLFIN XML format to new."

    print("Converting from old (pre DOLFIN 0.6.2) to new DOLFIN XML format...")
    ifile = open(ifilename, "r")
    ofile = open(ofilename, "w")

    #
    # Scan file for cell type (assuming there is just one)
    #
    cell_type = None
    dim = 0
    while 1:

        # Read next line
        line = ifile.readline()
        if not line:
            break

        # Read dimension
        if "<triangle" in line:
            cell_type = "triangle"
            dim = 2
            break
        elif "<tetrahedron" in line:
            cell_type = "tetrahedron"
            dim = 3
            break

    # Step to beginning of file
    ifile.seek(0)

    # Read lines and make changes
    while 1:

        # Read next line
        line = ifile.readline()
        if not line:
            break

        # Modify line
        if "xmlns" in line:
            line = "<dolfin xmlns:dolfin=\"http://www.fenics.org/dolfin/\">\n"
        if "<mesh>" in line:
            line = "  <mesh celltype=\"%s\" dim=\"%d\">\n" % (cell_type, dim)
        if dim == 2 and " z=\"0.0\"" in line:
            line = line.replace(" z=\"0.0\"", "")
        if " name=" in line:
            line = line.replace(" name=", " index=")
        if " name =" in line:
            line = line.replace(" name =", " index=")
        if "n0" in line:
            line = line.replace("n0", "v0")
        if "n1" in line:
            line = line.replace("n1", "v1")
        if "n2" in line:
            line = line.replace("n2", "v2")
        if "n3" in line:
            line = line.replace("n3", "v3")

        ofile.write(line)

    ifile.close()
    ofile.close()
    print("Conversion done")


def metis_graph2graph_xml(ifilename, ofilename):

    # *****************************************************************************80
    #
    # METIS_GRAPH2GRAPH_XML converts from METIS graph to DOLFIN XML graph format.
    #
    "Convert from Metis graph format to DOLFIN Graph XML."

    print("Converting from Metis graph format to DOLFIN Graph XML.")

    #
    # Open files
    #
    ifile = open(ifilename, "r")
    ofile = open(ofilename, "w")

    #
    # Read number of vertices and edges
    #
    line = ifile.readline()
    if not line:
        error("Empty file")

    (num_vertices, num_edges) = line.split()

    write_header_graph(ofile, "undirected")
    write_header_vertices(ofile, int(num_vertices))

    for i in range(int(num_vertices)):
        line = ifile.readline()
        edges = line.split()
        write_graph_vertex(ofile, i, len(edges))

    write_footer_vertices(ofile)
    write_header_edges(ofile, int(num_edges))

    #
    # Step to beginning of file and skip header info
    #
    ifile.seek(0)
    ifile.readline()
    for i in range(int(num_vertices)):
        line = ifile.readline()
        edges = line.split()
        for e in edges:
            if i < int(e):
                write_graph_edge(ofile, i, int(e))

    write_footer_edges(ofile)
    write_footer_graph(ofile)

    ifile.close()
    ofile.close()


def scotch_graph2graph_xml(ifilename, ofilename):

    # *****************************************************************************80
    #
    # SCOTCH_GRAPH2GRAPH_XML converts from Scotch graph to DOLFIN XML graph.
    #
    "Convert from Scotch graph format to DOLFIN Graph XML."

    print("Converting from Scotch graph format to DOLFIN Graph XML.")

    ifile = open(ifilename, "r")
    ofile = open(ofilename, "w")

    #
    # Skip graph file version number
    #
    ifile.readline()

    #
    # Read number of vertices and edges
    #
    line = ifile.readline()
    if not line:
        error("Empty file")

    (num_vertices, num_edges) = line.split()
    #
    # Read start index and numeric flag
    # Start index is 0 or 1 (C/Fortran)
    # Numeric flag is 3 bits where bit 1 enables vertex labels
    # bit 2 enables edge weights and bit 3 enables vertex weights
    #
    line = ifile.readline()
    (start_index, numeric_flag) = line.split()

    #
    # Handling not implemented
    #
    if not numeric_flag == "000":
        error("Handling of scotch vertex labels, edge- and vertex weights not implemented")

    write_header_graph(ofile, "undirected")
    write_header_vertices(ofile, int(num_vertices))

    # Read vertices and edges, first number gives number of edges from this vertex (not used)
    for i in range(int(num_vertices)):
        line = ifile.readline()
        edges = line.split()
        write_graph_vertex(ofile, i, len(edges) - 1)

    write_footer_vertices(ofile)
    write_header_edges(ofile, int(num_edges) / 2)

    # Step to beginning of file and skip header info
    ifile.seek(0)
    ifile.readline()
    ifile.readline()
    ifile.readline()
    for i in range(int(num_vertices)):
        line = ifile.readline()

        edges = line.split()
        for j in range(1, len(edges)):
            if i < int(edges[j]):
                write_graph_edge(ofile, i, int(edges[j]))

    write_footer_edges(ofile)
    write_footer_graph(ofile)

    ifile.close()
    ofile.close()


def write_header_mesh(ofile, cell_type, dim):

    # *****************************************************************************80
    #
    # WRITE_HEADER_MESH writes the mesh header.

    ofile.write("""\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>

<dolfin xmlns:dolfin=\"http://www.fenics.org/dolfin/\">
  <mesh celltype="%s" dim="%d">
""" % (cell_type, dim))


def write_header_graph(ofile, graph_type):

    # *****************************************************************************80
    #
    # WRITE_HEADER_GRAPH writes the graph header.
    #
    ofile.write("""\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>

<dolfin xmlns:dolfin=\"http://www.fenics.org/dolfin/\">
  <graph type="%s">
""" % (graph_type))


def write_footer_mesh(ofile):

    # *****************************************************************************80
    #
    # WRITE_FOOTER_MESH writes the mesh footer.
    #
    ofile.write("""\
  </mesh>
</dolfin>
""")


def write_footer_graph(ofile):

    # *****************************************************************************80
    #
    # WRITE_FOOTER_GRAPH writes the graph footer.
    #
    ofile.write("""\
  </graph>
</dolfin>
""")


def write_header_vertices(ofile, num_vertices):

    # *****************************************************************************80
    #
    # WRITE_HEADER_VERTICES ???
    #
    "Write vertices header"
    print("Expecting %d vertices" % num_vertices)
    ofile.write("    <vertices size=\"%d\">\n" % num_vertices)


def write_footer_vertices(ofile):

    # *****************************************************************************80
    #
    # WRITE_FOOTER_VERTICES ???
    #
    "Write vertices footer"
    ofile.write("    </vertices>\n")
    print("Found all vertices")


def write_header_edges(ofile, num_edges):

    # *****************************************************************************80
    #
    # WRITE_HEADER_EDGES ???
    #
    "Write edges header"
    print("Expecting %d edges" % num_edges)
    ofile.write("    <edges size=\"%d\">\n" % num_edges)


def write_footer_edges(ofile):

    # *****************************************************************************80
    #
    # WRITE_FOOTER_EDGES ???
    #
    "Write edges footer"
    ofile.write("    </edges>\n")
    print("Found all edges")


def write_vertex(ofile, vertex, x, y, z):

    # *****************************************************************************80
    #
    # WRITE_VERTEX ???
    #
    "Write vertex"
    ofile.write("      <vertex index=\"%d\" x=\"%g\" y=\"%g\" z=\"%g\"/>\n" %
                (vertex, x, y, z))


def write_graph_vertex(ofile, vertex, num_edges, weight=1):

    # *****************************************************************************80
    "Write graph vertex"
    ofile.write("      <vertex index=\"%d\" num_edges=\"%d\" weight=\"%d\"/>\n" %
                (vertex, num_edges, weight))


def write_graph_edge(ofile, v1, v2, weight=1):

    # *****************************************************************************80
    "Write graph edge"
    ofile.write("      <edge v1=\"%d\" v2=\"%d\" weight=\"%d\"/>\n" %
                (v1, v2, weight))


def write_header_cells(ofile, num_cells):

    # *****************************************************************************80
    "Write cells header"
    ofile.write("    <cells size=\"%d\">\n" % num_cells)
    print("Expecting %d cells" % num_cells)


def write_footer_cells(ofile):

    # *****************************************************************************80
    "Write cells footer"
    ofile.write("    </cells>\n")
    print("Found all cells")


def write_cell_interval(ofile, cell, n0, n1):
    # *****************************************************************************80
    "Write cell (interval)"
    ofile.write("      <interval index=\"%d\" v0=\"%d\" v1=\"%d\"/>\n" %
                (cell, n0, n1))


def write_cell_triangle(ofile, cell, n0, n1, n2):
    # *****************************************************************************80
    "Write cell (triangle)"
    ofile.write("      <triangle index=\"%d\" v0=\"%d\" v1=\"%d\" v2=\"%d\"/>\n" %
                (cell, n0, n1, n2))


def write_cell_tetrahedron(ofile, cell, n0, n1, n2, n3):

    # *****************************************************************************80
    "Write cell (tetrahedron)"
    ofile.write("      <tetrahedron index=\"%d\" v0=\"%d\" v1=\"%d\" v2=\"%d\" v3=\"%d\"/>\n" %
                (cell, n0, n1, n2, n3))


if __name__ == "__main__":
    main(["cylinder_2d.msh", "cylinder_2d.xml"])
    main(["cylinder_2d.msh", "cylinder_2d.xml"])
    main(["cylinder_3d.msh", "cylinder_3d.xml"])
    main(["ell_2d.msh", "ell_2d.xml"])
    main(["pinch.msh", "pinch.xml"])
    main(["step_2d.msh", "step_2d.xml"])
    main(["step_3d.msh", "step_3d.xml"])
    main(["test02.msh", "test02.xml"])
    main(["test03.msh", "test03.xml"])
