#! /usr/bin/env python3
#


def bellman_ford(v_num, e_num, source, e, e_weight):

    # *****************************************************************************80
    #
    #  Purpose:
    #
    #    BELLMAN_FORD finds shortest paths from a given vertex of a weighted directed graph.
    #
    #  Discussion:
    #
    #    The Bellman-Ford algorithm is used.
    #
    #    Each edge of the graph has a weight, which may be negative.  However,
    #    it should not be the case that there is any negative loop, that is,
    #    a circuit whose total weight is negative.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer V_NUM, the number of vertices.
    #
    #    Input, integer E_NUM, the number of edges.
    #
    #    Input, integer SOURCE, the vertex from which distances will
    #    be calculated.
    #
    #    Input, integer E(2,E_NUM), the edges, given as pairs of
    #    vertex indices.
    #
    #    Input, real E_WEIGHT(E_NUM), the weight of each edge.
    #
    #    Output, real V_WEIGHT(V_NUM), the weight of each node,
    #    that is, its minimum distance from SOURCE.
    #
    #    Output, integer PREDECESSOR(V_NUM), a list of predecessors,
    #    which can be used to recover the shortest path from any node back to SOURCE.
    #
    import numpy as np
    from sys import exit

    r8_big = 1.0E+30
#
#  Step 1: initialize the graph.
#
    v_weight = np.zeros(v_num, dtype=np.float64)
    for i in range(0, v_num):
        v_weight[i] = r8_big
    v_weight[source] = 0.0

    predecessor = np.zeros(v_num, dtype=np.int32)
    for i in range(0, v_num):
        predecessor[i] = -1
#
#  Step 2: Relax edges repeatedly.
#
    for i in range(1, v_num):
        for j in range(0, e_num):
            u = e[1][j]
            v = e[0][j]
            t = v_weight[u] + e_weight[j]
            if (t < v_weight[v]):
                v_weight[v] = t
                predecessor[v] = u
#
#  Step 3: check for negative-weight cycles
#
    for j in range(0, e_num):
        u = e[1][j]
        v = e[0][j]
        if (v_weight[u] + e_weight[j] < v_weight[v]):
            print('')
            print('BELLMAN_FORD - Fatal error!')
            print('  Graph contains a cycle with negative weight.')
            exit('BELLMAN_FORD - Fatal error!')

    return v_weight, predecessor


def bellman_ford_test():

    # *****************************************************************************80
    #
    # BELLMAN_FORD_TEST tests BELLMAN_FORD.
    #
    #  Discussion:
    #
    #    The correct distances are { 0, -6, -2, 3, 0, 0 }.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    e_num = 10
    v_num = 6

    e = np.array((
        (1, 4, 1, 2, 4, 2, 5, 3, 5, 3),
        (0, 1, 2, 4, 0, 5, 0, 2, 3, 0)))
    e_weight = np.array((
        -3.0, 6.0, -4.0, -1.0, 4.0, -2.0, 2.0, 8.0, -3.0, 3.0))

    source = 0
#
#  Terminate.
#
    print('')
    print('BELLMAN_FORD_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BELLMAN_FORD implements the Bellman-Ford shortest path algorithm.')

    print('')
    print('  Number of vertices = %d' % (v_num))
    print('  Number of edges = %d' % (e_num))
    print('  The reference vertex is %d' % (source))

    i4mat_transpose_print(2, e_num, e, '  The edge array:')
    r8vec_print(e_num, e_weight, '  The edge weights:')

    [v_weight, predecessor] = bellman_ford(v_num, e_num, source, e, e_weight)

    r8vec_print(v_num, v_weight, '  The shortest distances:')

    i4vec_print(v_num, predecessor,
                '  The vertex predecessor parents for the shortest paths:')
#
#  Terminate.
#
    print('')
    print('BELLMAN_FORD_TEST:')
    print('  Normal end of execution.')
    return


def i4mat_transpose_print(m, n, a, title):

    # *****************************************************************************80
    #
    # I4MAT_TRANSPOSE_PRINT prints an I4MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, integer A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    i4mat_transpose_print_some(m, n, a, 0, 0, m - 1, n - 1, title)


def i4mat_transpose_print_test():

    # *****************************************************************************80
    #
    # I4MAT_TRANSPOSE_PRINT_TEST tests I4MAT_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import sys

    print('')
    print('I4MAT_TRANSPOSE_PRINT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test I4MAT_TRANSPOSE_PRINT, which prints an I4MAT, tranposed.')

    m = 5
    n = 3
    a = np.array((
        (11, 12, 13),
        (21, 22, 23),
        (31, 32, 33),
        (41, 42, 43),
        (51, 52, 53)))
    title = '  A 5 x 3 integer matrix:'
    i4mat_transpose_print(m, n, a, title)
#
#  Terminate.
#
    print('')
    print('I4MAT_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4mat_transpose_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # I4MAT_TRANSPOSE_PRINT_SOME prints a portion of an I4MAT, transposed.
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
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, integer A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for i2lo in range(max(ilo, 0), min(ihi, m - 1), incx):

        i2hi = i2lo + incx - 1
        i2hi = min(i2hi, m - 1)
        i2hi = min(i2hi, ihi)

        print('')
        print('  Row: ', end='')

        for i in range(i2lo, i2hi + 1):
            print('%7d  ' % (i), end='')

        print('')
        print('  Col')

        j2lo = max(jlo, 0)
        j2hi = min(jhi, n - 1)

        for j in range(j2lo, j2hi + 1):

            print(' %4d: ' % (j), end='')

            for i in range(i2lo, i2hi + 1):
                print('%7d  ' % (a[i, j]), end='')

            print('')

    return


def i4mat_transpose_print_some_test():

    # *****************************************************************************80
    #
    # I4MAT_TRANSPOSE_PRINT_SOME_TEST tests I4MAT_TRANSPOSE_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4MAT_TRANSPOSE_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4MAT_TRANSPOSE_PRINT_SOME prints some of an I4MAT, transposed.')

    m = 4
    n = 6
    v = np.array([
        [11, 12, 13, 14, 15, 16],
        [21, 22, 23, 24, 25, 26],
        [31, 32, 33, 34, 35, 36],
        [41, 42, 43, 44, 45, 46]], dtype=np.int32)
    i4mat_transpose_print_some(m, n, v, 0, 3, 2, 5,
                               '  Here is I4MAT, rows 0:2, cols 3:5:')
#
#  Terminate.
#
    print('')
    print('I4MAT_TRANSPOSE_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_PRINT prints an I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i4vec_print_test():

    # *****************************************************************************80
    #
    # I4VEC_PRINT_TEST tests I4VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_PRINT prints an I4VEC.')

    n = 4
    v = np.array([91, 92, 93, 94], dtype=np.int32)
    i4vec_print(n, v, '  Here is an I4VEC:')
#
#  Terminate.
#
    print('')
    print('I4VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
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
    bellman_ford_test()
    timestamp()
