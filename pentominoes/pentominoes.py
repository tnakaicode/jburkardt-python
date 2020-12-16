#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import time
import platform


def cell_ij_fill(m, i, j, color):

    # *****************************************************************************80
    #
    # CELL_IJ_FILL plots a filled (I,J) cell.
    #
    #  Discussion:
    #
    #    We assume the data is represented in a matrix.
    #
    #    In order to convert between the matrix coordinates and picture
    #    coordinates, the (I,J) cell will be drawn with the following corners:
    #
    #    (j-1,m-i+1), (j,m-i+1), (j,m-i), (j-1,m-1).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the maximum row index.
    #
    #    Input, integer I, J, the index of the cell.
    #
    #    Input, MATLAB color COLOR, can be any of the 8 abbreviated color terms
    #    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as
    #    [1.0,0.4,0.0].  The square is filled with this color.
    #

    a = j - 1
    b = j
    c = m - (i - 1)
    d = m - i

    plt.fill([a, b, b, a], [c, c, d, d], color)


def cell_ij_fill_test():

    # *****************************************************************************80
    #
    # CELL_IJ_FILL_TEST tests CELL_IJ_FILL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('CELL_IJ_FILL_TEST:')
    print('  CELL_IJ_FILL fills in unit cells indexed by (I,J)')
    print('  using matrix coordinate system.')

    mario = np.array([
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 6, 6, 6, 5, 5, 5, 1, 5, 0, 0, 0],
        [0, 6, 5, 6, 5, 5, 5, 5, 1, 5, 5, 5, 0],
        [0, 6, 5, 6, 6, 5, 5, 5, 5, 1, 5, 5, 5],
        [0, 6, 6, 5, 5, 5, 5, 5, 1, 1, 1, 1, 0],
        [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0],
        [0, 0, 2, 2, 3, 2, 2, 2, 2, 0, 0, 0, 0],
        [0, 2, 2, 2, 3, 2, 2, 3, 2, 2, 2, 0, 0],
        [2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0],
        [5, 5, 2, 3, 4, 3, 3, 4, 3, 2, 5, 5, 0],
        [5, 5, 5, 3, 3, 3, 3, 3, 3, 5, 5, 5, 0],
        [5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 0],
        [0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 0],
        [0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0],
        [6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0]])

    dims = mario.shape
    m = dims[0]
    n = dims[1]

    #  0: white
    #  1: black
    #  2: red
    #  3: blue
    #  4: yellow
    #  5: beige
    #  6: brown
    plt.axis('equal')
    plt.axis('off')

    for i in range(0, m):
        for j in range(0, n):
            k = mario[i, j]

            #  Despite documentation assuring me it was possible, I could not seem to use
            #  numeric RGB triples for colors.
            if (k == 0):
                color = 'white'
            elif (k == 1):
                color = 'black'
            elif (k == 2):
                color = 'red'
            elif (k == 3):
                color = 'blue'
            elif (k == 4):
                color = 'yellow'
            elif (k == 5):
                color = 'bisque'
            elif (k == 6):
                color = 'brown'

            cell_ij_fill(m, i, j, color)

    plt.savefig('cell_ij_fill_test.png')
    plt.show(block=False)
    plt.clf()


def pentomino_display(p, label):

    # *****************************************************************************80
    #
    # PENTOMINO_DISPLAY displays a particular pentomino in a 5x5 grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer P(P_M,P_N), a matrix of 0's and 1's.
    #    1 <= P_M, P_N <= 5.  There should be exactly 5 values of one.
    #
    #    Input, string LABEL, a title for the plot.
    #

    #  The background grid.
    grid_m = 5
    grid_n = 5
    grid = np.zeros([grid_m, grid_n])

    #  Place the pentomino on the grid, so that it is "snug" in the upper left corner.
    dims = p.shape
    p_m = dims[0]
    p_n = dims[1]

    grid[0:p_m, 0:p_n] = p[0:p_m, 0:p_n]

    #  Display each square of the grid.
    plt.axis('equal')
    plt.axis('off')

    for i in range(0, grid_m):
        for j in range(0, grid_n):
            k = grid[i, j]
            if (k == 0):
                color = 'white'
            elif (k == 1):
                color = 'black'
            cell_ij_fill(grid_m, i, j, color)

    filename = label + '.png'
    plt.savefig(filename)
    plt.show(block=False)
    plt.clf()

    print('  PENTOMINO_DISPLAY created "%s"' % (filename))


def pentomino_display_test():

    # *****************************************************************************80
    #
    # PENTOMINO_DISPLAY_TEST tests PENTOMINO_DISPLAY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PENTOMINO_DISPLAY_TEST')
    print('  PENTOMINO_DISPLAY displays a picture of a pentomino.')

    pentominos = np.array(
        ['F', 'I', 'L', 'N', 'P', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    for i in range(0, 12):
        name = pentominos[i]
        p = pentomino_matrix(name)
        pentomino_display(p, name)


def pentominoes_test():

    # *****************************************************************************80
    #
    # PENTOMINOES_TEST tests the PENTOMINOES library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PENTOMINOES_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the PENTOMINOES library.')

    cell_ij_fill_test()
    pentomino_matrix_test()
    pentomino_display_test()

    print('')
    print('PENTOMINOES_TEST')
    print('  Normal end of execution.')
    return


def pentomino_matrix(name):

    # *****************************************************************************80
    #
    # PENTOMINO_MATRIX returns a 0/1 matrix defining a particular pentomino.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, character NAME, is f, i, l, n, p, t, u, v, w, x, y or z.
    #
    #    Output, integer P(P_M,P_N), a matrix of 0's and 1's that indicates
    #    the shape of the pentomino.
    #
    from sys import exit

    if (name.lower() == 'f'):
        p = np.array([
            [0, 1, 1],
            [1, 1, 0],
            [0, 1, 0]])

    elif (name.lower() == 'i'):
        p = np.array([
            [1],
            [1],
            [1],
            [1],
            [1]])

    elif (name.lower() == 'l'):
        p = np.array([
            [1, 0],
            [1, 0],
            [1, 0],
            [1, 1]])

    elif (name.lower() == 'n'):
        p = np.array([
            [1, 1, 0, 0],
            [0, 1, 1, 1]])

    elif (name.lower() == 'p'):
        p = np.array([
            [1, 1],
            [1, 1],
            [1, 0]])

    elif (name.lower() == 't'):
        p = np.array([
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0]])

    elif (name.lower() == 'u'):
        p = np.array([
            [1, 0, 1],
            [1, 1, 1]])

    elif (name.lower() == 'v'):
        p = np.array([
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]])

    elif (name.lower() == 'w'):
        p = np.array([
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 1]])

    elif (name.lower() == 'x'):
        p = np.array([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]])

    elif (name.lower() == 'y'):
        p = np.array([
            [0, 0, 1, 0],
            [1, 1, 1, 1]])

    elif (name.lower() == 'z'):
        p = np.array([
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 1]])

    else:
        print('')
        print('PENTOMINO_MATRIX - Fatal error!')
        print('  Illegal name = "%s"' % (name))
        print('  Legal names: f, i, l, n, p, t, u, v, w, x, y, z.')
        exit('PENTOMINO_MATRIX - Fatal error!')

    return p


def pentomino_matrix_test():

    # *****************************************************************************80
    #
    # PENTOMINO_MATRIX_TEST tests PENTOMINO_MATRIX.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PENTOMINO_MATRIX_TEST')
    print('  PENTOMINO_MATRIX returns a 0/1 matrix representing a pentomino.')

    pentominos = np.array(
        ['F', 'I', 'L', 'N', 'P', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    for i in range(0, 12):
        name = pentominos[i]
        p = pentomino_matrix(name)
        dims = p.shape
        m = dims[0]
        n = dims[1]
        print('')
        print('  %s pentomino (%d,%d):' % (name, m, n))
        print('')
        for i in range(0, m):
            print('    '),
            for j in range(0, n):
                print(' %d' % (p[i, j])),
            print('')


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
    t = time.time()
    print(time.ctime(t))


if (__name__ == '__main__'):
    timestamp()
    pentominoes_test()
    timestamp()
