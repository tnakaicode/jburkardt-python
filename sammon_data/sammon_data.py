#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def data_circle(n):

    # *****************************************************************************80
    #
    # DATA_CIRCLE writes the circle test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(2,N), the points.
    #

    m = 2
    c = 5.0 * np.random.rand(2)
    r = 2.5 * np.random.rand(1)
    theta0 = 2.0 * np.pi * np.random.rand(1)

    print('')
    print('DATA_CIRCLE')
    print('  Generate %d data points around a circle' % (n - 1))
    print('  of radius R = %f' % (r))
    print('  and center C = ( %f, %f )' % (c[0], c[1]))
    print('  with initial angle THETA0 = %f' % (theta0))
    print('  plus the center point.')

    x = np.zeros([m, n])
    for j in range(0, n - 1):
        theta = theta0 + float(j) * 2.0 * np.pi / float(n - 1)
        x[0, j] = c[0] + r * np.cos(theta)
        x[1, j] = c[1] + r * np.sin(theta)

    x[0, n - 1] = c[0]
    x[1, n - 1] = c[1]

    filename = 'sammon_circle.txt'
    r8mat_write(filename, m, n, x)

    print('')
    print('  Test data written to "%s".' % (filename))
    return x


def data_helix(n):

    # *****************************************************************************80
    #
    # DATA_HELIX writes the helix test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(3,N), the points.
    #

    m = 3

    print('')
    print('DATA_HELIX')
    print('  Generate %d data points along a helix.' % (n))

    x = np.zeros([m, n])

    for j in range(0, n):
        z = float(j) / np.sqrt(2.0)
        x[0, j] = np.cos(z)
        x[1, j] = np.sin(z)
        x[2, j] = z

    filename = 'sammon_helix.txt'
    r8mat_write(filename, m, n, x)

    print('')
    print('  Test data written to "%s".' % (filename))

    return x


def data_iris():

    # *****************************************************************************80
    #
    # DATA_IRIS writes the Iris test data.
    #
    #  Discussion:
    #
    #    This is Fisher's Iris data.
    #
    #    1 - sepal length in cm
    #    2 - sepal width in cm
    #    3 - petal length in cm
    #    4 - petal width in cm
    #    5 - class: 1 for Iris setosa, 2 for Iris Versicolour, 3 for Iris Virginica.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Ronald Fisher,
    #    The use of multiple measurements in taxonomic problems,
    #    Annual Eugenics,
    #    Volume 7, part II, 1936, pages 179-188.
    #
    #  Parameters:
    #
    #    Input, real X(147,5), the points.
    #

    m = 147
    n = 5

    print('')
    print('DATA_IRIS')
    print('  Fisher\'s iris data.')
    print('  Number of points M = %d' % (m))
    print('  Spatial dimension N = %d' % (n))

    x = np.array([
        [5.1, 3.5, 1.4, 0.2, 1],
        [4.9, 3.0, 1.4, 0.2, 1],
        [4.7, 3.2, 1.3, 0.2, 1],
        [4.6, 3.1, 1.5, 0.2, 1],
        [5.0, 3.6, 1.4, 0.2, 1],
        [5.4, 3.9, 1.7, 0.4, 1],
        [4.6, 3.4, 1.4, 0.3, 1],
        [5.0, 3.4, 1.5, 0.2, 1],
        [4.4, 2.9, 1.4, 0.2, 1],
        [4.9, 3.1, 1.5, 0.1, 1],
        [5.4, 3.7, 1.5, 0.2, 1],
        [4.8, 3.4, 1.6, 0.2, 1],
        [4.8, 3.0, 1.4, 0.1, 1],
        [4.3, 3.0, 1.1, 0.1, 1],
        [5.8, 4.0, 1.2, 0.2, 1],
        [5.7, 4.4, 1.5, 0.4, 1],
        [5.4, 3.9, 1.3, 0.4, 1],
        [5.1, 3.5, 1.4, 0.3, 1],
        [5.7, 3.8, 1.7, 0.3, 1],
        [5.1, 3.8, 1.5, 0.3, 1],
        [5.4, 3.4, 1.7, 0.2, 1],
        [5.1, 3.7, 1.5, 0.4, 1],
        [4.6, 3.6, 1.0, 0.2, 1],
        [5.1, 3.3, 1.7, 0.5, 1],
        [4.8, 3.4, 1.9, 0.2, 1],
        [5.0, 3.0, 1.6, 0.2, 1],
        [5.0, 3.4, 1.6, 0.4, 1],
        [5.2, 3.5, 1.5, 0.2, 1],
        [5.2, 3.4, 1.4, 0.2, 1],
        [4.7, 3.2, 1.6, 0.2, 1],
        [4.8, 3.1, 1.6, 0.2, 1],
        [5.4, 3.4, 1.5, 0.4, 1],
        [5.2, 4.1, 1.5, 0.1, 1],
        [5.5, 4.2, 1.4, 0.2, 1],
        [4.9, 3.1, 1.5, 0.1, 1],
        [5.0, 3.2, 1.2, 0.2, 1],
        [5.5, 3.5, 1.3, 0.2, 1],
        [4.9, 3.1, 1.5, 0.1, 1],
        [4.4, 3.0, 1.3, 0.2, 1],
        [5.1, 3.4, 1.5, 0.2, 1],
        [5.0, 3.5, 1.3, 0.3, 1],
        [4.5, 2.3, 1.3, 0.3, 1],
        [4.4, 3.2, 1.3, 0.2, 1],
        [5.0, 3.5, 1.6, 0.6, 1],
        [5.1, 3.8, 1.9, 0.4, 1],
        [4.8, 3.0, 1.4, 0.3, 1],
        [5.1, 3.8, 1.6, 0.2, 1],
        [4.6, 3.2, 1.4, 0.2, 1],
        [5.3, 3.7, 1.5, 0.2, 1],
        [5.0, 3.3, 1.4, 0.2, 1],
        [7.0, 3.2, 4.7, 1.4, 2],
        [6.4, 3.2, 4.5, 1.5, 2],
        [6.9, 3.1, 4.9, 1.5, 2],
        [5.5, 2.3, 4.0, 1.3, 2],
        [6.5, 2.8, 4.6, 1.5, 2],
        [5.7, 2.8, 4.5, 1.3, 2],
        [6.3, 3.3, 4.7, 1.6, 2],
        [4.9, 2.4, 3.3, 1.0, 2],
        [6.6, 2.9, 4.6, 1.3, 2],
        [5.2, 2.7, 3.9, 1.4, 2],
        [5.0, 2.0, 3.5, 1.0, 2],
        [5.9, 3.0, 4.2, 1.5, 2],
        [6.0, 2.2, 4.0, 1.0, 2],
        [6.1, 2.9, 4.7, 1.4, 2],
        [5.6, 2.9, 3.6, 1.3, 2],
        [6.7, 3.1, 4.4, 1.4, 2],
        [5.6, 3.0, 4.5, 1.5, 2],
        [5.8, 2.7, 4.1, 1.0, 2],
        [6.2, 2.2, 4.5, 1.5, 2],
        [5.6, 2.5, 3.9, 1.1, 2],
        [5.9, 3.2, 4.8, 1.8, 2],
        [6.1, 2.8, 4.0, 1.3, 2],
        [6.3, 2.5, 4.9, 1.5, 2],
        [6.1, 2.8, 4.7, 1.2, 2],
        [6.4, 2.9, 4.3, 1.3, 2],
        [6.6, 3.0, 4.4, 1.4, 2],
        [6.8, 2.8, 4.8, 1.4, 2],
        [6.7, 3.0, 5.0, 1.7, 2],
        [6.0, 2.9, 4.5, 1.5, 2],
        [5.7, 2.6, 3.5, 1.0, 2],
        [5.5, 2.4, 3.8, 1.1, 2],
        [5.5, 2.4, 3.7, 1.0, 2],
        [5.8, 2.7, 3.9, 1.2, 2],
        [6.0, 2.7, 5.1, 1.6, 2],
        [5.4, 3.0, 4.5, 1.5, 2],
        [6.0, 3.4, 4.5, 1.6, 2],
        [6.7, 3.1, 4.7, 1.5, 2],
        [6.3, 2.3, 4.4, 1.3, 2],
        [5.6, 3.0, 4.1, 1.3, 2],
        [5.5, 2.5, 4.0, 1.3, 2],
        [5.5, 2.6, 4.4, 1.2, 2],
        [6.1, 3.0, 4.6, 1.4, 2],
        [5.8, 2.6, 4.0, 1.2, 2],
        [5.0, 2.3, 3.3, 1.0, 2],
        [5.6, 2.7, 4.2, 1.3, 2],
        [5.7, 3.0, 4.2, 1.2, 2],
        [5.7, 2.9, 4.2, 1.3, 2],
        [6.2, 2.9, 4.3, 1.3, 2],
        [5.1, 2.5, 3.0, 1.1, 2],
        [5.7, 2.8, 4.1, 1.3, 2],
        [6.3, 3.3, 6.0, 2.5, 3],
        [5.8, 2.7, 5.1, 1.9, 3],
        [7.1, 3.0, 5.9, 2.1, 3],
        [6.3, 2.9, 5.6, 1.8, 3],
        [6.5, 3.0, 5.8, 2.2, 3],
        [7.6, 3.0, 6.6, 2.1, 3],
        [4.9, 2.5, 4.5, 1.7, 3],
        [7.3, 2.9, 6.3, 1.8, 3],
        [6.7, 2.5, 5.8, 1.8, 3],
        [7.2, 3.6, 6.1, 2.5, 3],
        [6.5, 3.2, 5.1, 2.0, 3],
        [6.4, 2.7, 5.3, 1.9, 3],
        [6.8, 3.0, 5.5, 2.1, 3],
        [5.7, 2.5, 5.0, 2.0, 3],
        [5.8, 2.8, 5.1, 2.4, 3],
        [6.4, 3.2, 5.3, 2.3, 3],
        [6.5, 3.0, 5.5, 1.8, 3],
        [7.7, 3.8, 6.7, 2.2, 3],
        [7.7, 2.6, 6.9, 2.3, 3],
        [6.0, 2.2, 5.0, 1.5, 3],
        [6.9, 3.2, 5.7, 2.3, 3],
        [5.6, 2.8, 4.9, 2.0, 3],
        [7.7, 2.8, 6.7, 2.0, 3],
        [6.3, 2.7, 4.9, 1.8, 3],
        [6.7, 3.3, 5.7, 2.1, 3],
        [7.2, 3.2, 6.0, 1.8, 3],
        [6.2, 2.8, 4.8, 1.8, 3],
        [6.1, 3.0, 4.9, 1.8, 3],
        [6.4, 2.8, 5.6, 2.1, 3],
        [7.2, 3.0, 5.8, 1.6, 3],
        [7.4, 2.8, 6.1, 1.9, 3],
        [7.9, 3.8, 6.4, 2.0, 3],
        [6.4, 2.8, 5.6, 2.2, 3],
        [6.3, 2.8, 5.1, 1.5, 3],
        [6.1, 2.6, 5.6, 1.4, 3],
        [7.7, 3.0, 6.1, 2.3, 3],
        [6.3, 3.4, 5.6, 2.4, 3],
        [6.4, 3.1, 5.5, 1.8, 3],
        [6.0, 3.0, 4.8, 1.8, 3],
        [6.9, 3.1, 5.4, 2.1, 3],
        [6.7, 3.1, 5.6, 2.4, 3],
        [6.9, 3.1, 5.1, 2.3, 3],
        [5.8, 2.7, 5.1, 1.9, 3],
        [6.8, 3.2, 5.9, 2.3, 3],
        [6.7, 3.3, 5.7, 2.5, 3],
        [6.7, 3.0, 5.2, 2.3, 3],
        [6.3, 2.5, 5.0, 1.9, 3],
        [6.5, 3.0, 5.2, 2.0, 3],
        [6.2, 3.4, 5.4, 2.3, 3],
        [5.9, 3.0, 5.1, 1.8, 3]])

    filename = 'sammon_iris.txt'
    r8mat_write(filename, m, n, x)

    print('')
    print('  Test data written to "%s".' % (filename))

    return x


def data_linear(m, n):

    # *****************************************************************************80
    #
    # DATA_LINEAR writes the straight line test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(M,N), the points.
    #

    print('')
    print('DATA_LINEAR')
    print('  Generate %d data points along a straight line' % (n))
    print('  in %d-dimensional space.' % (m))

    a = np.random.rand(m)
    b = np.random.rand(m)
    x = np.zeros([m, n])
    for j in range(0, n):
        for i in range(0, m):
            x[i, j] = (float(n - j - 1) * a[i]
                       + float(j) * b[i]) \
                / float(n - 1)

    filename = 'sammon_linear.txt'
    r8mat_write(filename, m, n, x)

    print('')
    print('  Test data written to "%s".' % (filename))

    return x


def data_nonlinear(n):

    # *****************************************************************************80
    #
    # DATA_NONLINEAR writes the nonlinear test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(5,N), the points.
    #

    m = 5

    print('')
    print('DATA_NONLINEAR')
    print('  Generate %d data points along a nonlinear curve.' % (n))
    print('  Spatial dimension M = %d' % (m))

    x = np.zeros([m, n])

    for j in range(0, n):
        z = float(j) / np.sqrt(2.0)
        x[0, j] = np.cos(z)
        x[1, j] = np.sin(z)
        x[2, j] = 0.5 * np.cos(2.0 * z)
        x[3, j] = 0.5 * np.sin(2.0 * z)
        x[4, j] = z

    filename = 'sammon_nonlinear.txt'
    r8mat_write(filename, m, n, x)

    print('')
    print('  Test data written to %s".' % (filename))

    return x


def data_simplex(m, n, s):

    # *****************************************************************************80
    #
    # DATA_SIMPLEX writes the nonlinear test data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real S, the standard deviation of sample points from a vertex.
    #
    #    Input, real X(M,N), the points.
    #

    print('')
    print('DATA_SIMPLEX')
    print('  Generate %d data points at vertices of a simplex' % (n))
    print('  with a standard deviation of %f' % (s))
    print('  Spatial dimension M = %d' % (m))

    x = np.zeros([m + 1, n])
    v = simplex_coordinates2(m)
    #
    #  Rescale so intervertex distance is sqrt (5/4).
    #
    s = 0.0
    for i in range(0, m):
        s = s + (v[i, 0] - v[i, 1]) ** 2
    s = np.sqrt(s)

    v = (np.sqrt(5.0 / 4.0) / s) * v
    #
    #  For point J of N points, choose one of M+1 vertices.
    #  Evaluate a Gaussian distribution centered at that vertex
    #  with a standard deviation of 0.2 units in each dimension.
    #
    #  Add an M+1-th coordinate that remembers the associated vertex.
    #
    for j in range(0, n):
        k = np.random.randint(0, m, 1)
        for i in range(0, m):
            x[i, j] = v[i, k] + s * np.random.randn(1)
        x[m, j] = float(k + 1)

    filename = 'sammon_simplex.txt'
    r8mat_write(filename, m + 1, n, x)

    print('')
    print('  Test data written to "%s".' % (filename))

    return x


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


def simplex_coordinates2(n):

    # *****************************************************************************80
    #
    # SIMPLEX_COORDINATES2 computes the Cartesian coordinates of simplex vertices.
    #
    #  Discussion:
    #
    #    This routine uses a simple approach to determining the coordinates of
    #    the vertices of a regular simplex in n dimensions.
    #
    #    We want the vertices of the simplex to satisfy the following conditions:
    #
    #    1) The centroid, or average of the vertices, is 0.
    #    2) The distance of each vertex from the centroid is 1.
    #       By 1), this is equivalent to requiring that the sum of the squares
    #       of the coordinates of any vertex be 1.
    #    3) The distance between any pair of vertices is equal (and is not zero.)
    #    4) The dot product of any two coordinate vectors for distinct vertices
    #       is -1/N equivalently, the angle subtended by two distinct vertices
    #       from the centroid is arccos ( -1/N).
    #
    #    Note that if we choose the first N vertices to be the columns of the
    #    NxN identity matrix, we are almost there.  By symmetry, the last column
    #    must have all entries equal to some value A.  Because the square of the
    #    distance between the last column and any other column must be 2 (because
    #    that's the distance between any pair of columns), we deduce that
    #    (A-1)^2 + (N-1)*A^2 = 2, hence A = (1-sqrt(1+N))/N.  Now compute the
    #    centroid C of the vertices, and subtract that, to center the simplex
    #    around the origin.  Finally, compute the norm of one column, and rescale
    #    the matrix of coordinates so each vertex has unit distance from the origin.
    #
    #    This approach devised by John Burkardt, 19 September 2010.  What,
    #    I'm not the first?
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the spatial dimension.
    #
    #    Output, real X(N,N+1), the coordinates of the vertices
    #    of a simplex in N dimensions.
    #

    x = np.zeros([n, n + 1])
    for j in range(0, n):
        x[j, j] = 1.0

    a = (1.0 - np.sqrt(1.0 + float(n))) / float(n)
    for i in range(0, n):
        x[i, n] = a

    #
    #  Now adjust coordinates so the centroid is at zero.
    #
    c = np.zeros(n)
    for i in range(0, n):
        for j in range(0, n + 1):
            c[i] = c[i] + x[i, j]
        c[i] = c[i] / float(n + 1)

    for j in range(0, n + 1):
        for i in range(0, n):
            x[i, j] = x[i, j] - c[i]

    #
    #  Now scale so each column has norm 1.
    #
    s = 0.0
    for i in range(0, n):
        s = s + x[i, 0] ** 2
    s = np.sqrt(s)

    for i in range(0, n):
        for j in range(0, n + 1):
            x[i, j] = x[i, j] / s

    return x


def sammon_data_test():

    # *****************************************************************************80
    #
    # SAMMON_DATA_TEST generates data for SAMMON tests.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SAMMON_DATA_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate data for SAMMON tests.')

    n = 9
    x = data_circle(n)

    n = 20
    x = data_helix(n)

    x = data_iris()

    m = 9
    n = 9
    x = data_linear(m, n)

    n = 29
    x = data_nonlinear(n)

    m = 4
    n = 75
    s = 0.2
    x = data_simplex(m, n, s)

    print('')
    print('SAMMON_DATA_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    sammon_data_test()
    timestamp()
