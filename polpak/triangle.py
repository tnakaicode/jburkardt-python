#! /usr/bin/env python
#
def triangle_num(n):

    # *****************************************************************************80
    #
    # TRIANGLE_NUM returns the N-th triangular  number.
    #
    #  Discussion:
    #
    #    The N-th triangular number T(N) is formed by the sum of the first
    #    N integers:
    #
    #      T(N) = sum ( 1 <= I <= N ) I
    #
    #    By convention, T(0) = 0.
    #
    #    T(N) = ( N * ( N + 1 ) ) / 2
    #
    #  First Values:
    #
    #     0
    #     1
    #     3
    #     6
    #    10
    #    15
    #    21
    #    28
    #    36
    #    45
    #    55
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the index of the desired number, which must be
    #    at least 0.
    #
    #    Output, integer VALUE, the N-th triangleal number.
    #
    value = (n * (n + 1)) / 2

    return value


def triangle_num_test():

    # *****************************************************************************80
    #
    # TRIANGLE_NUM_TEST tests TRIANGLE_NUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TRIANGLE_NUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANGLE_NUM computes the triangular numbers.')
    print('')

    for n in range(1, 11):
        print('  %2d  %6d' % (n, triangle_num(n)))
#
#  Terminate.
#
    print('')
    print('TRIANGLE_NUM_TEST:')
    print('  Normal end of execution.')
    return


def triangle_upper_to_i4(i, j):

    # *****************************************************************************80
    #
    # TRIANGLE_UPPER_TO_I4 converts an upper triangular coordinate to an integer.
    #
    #  Discussion:
    #
    #    Triangular coordinates are handy when storing a naturally triangular
    #    array (such as the upper half of a matrix) in a linear array.
    #
    #    Thus, for example, we might consider storing
    #
    #    (1,1) (1,2) (1,3) (1,4)
    #          (2,2) (2,3) (2,4)
    #                (3,3) (3,4)
    #                      (4,4)
    #
    #    as the linear array
    #
    #    (1,1) (1,2) (2,2) (1,3) (2,3) (3,3) (1,4) (2,4) (3,4) (4,4)
    #
    #    Here, the quantities in parenthesis represent the natural row and
    #    column indices of a single number when stored in a rectangular array.
    #
    #    Thus, our goal is, given the row I and column J of the data,
    #    to produce the value K which indicates its position in the linear
    #    array.
    #
    #    The triangular numbers are the indices associated with the
    #    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
    #    and so on.
    #
    #  Formula:
    #
    #    K = I + ( (J-1) * J ) / 2
    #
    #  First Values:
    #
    #     I  J  K
    #
    #     0  0  0
    #     1  1  1
    #     1  2  2
    #     2  2  3
    #     1  3  4
    #     2  3  5
    #     3  3  6
    #     1  4  7
    #     2  4  8
    #     3  4  9
    #     4  4 10
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, the row and column indices.  I and J must
    #    be nonnegative, and J must not be greater than I.
    #
    #    Output, integer VALUE, the linear index of the (I,J) element.
    #
    from sys import exit

    if (i < 0):
        print('')
        print('TRIANGLE_UPPER_TO_I4 - Fatal error!')
        print('  I < 0.')
        print('  I = %d' % (i))
        exit('TRIANGLE_UPPER_TO_I4 - Fatal error!')

    if (j < 0):
        print('')
        print('TRIANGLE_UPPER_TO_I4 - Fatal error!')
        print('  J < 0.')
        print('  J = %d' % (j))
        exit('TRIANGLE_UPPER_TO_I4 - Fatal error!')

    if (i < j):
        print('')
        print('TRIANGLE_UPPER_TO_I4 - Fatal error!')
        print('  I < J.')
        print('  I = %d' % (i))
        print('  J = %d' % (j))
        exit('TRIANGLE_UPPER_TO_I4 - Fatal error!')

    value = i + ((j - 1) * j) // 2

    return value


def triangle_upper_to_i4_test():

    # *****************************************************************************80
    #
    # TRIANGLE_UPPER_TO_I4_TEST tests TRIANGLE_UPPER_TO_I4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TRIANGLE_UPPER_TO_I4_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANGLE_UPPER_TO_I4 converts an upper triangular index to a linear one.')
    print('')
    print('   ( I,    J ) ==> K')
    print('')

    for i in range(1, 5):
        for j in range(1, i + 1):
            k = triangle_upper_to_i4(i, j)
            print('  %4d  %4d    %4d' % (i, j, k))
#
#  Terminate.
#
    print('')
    print('TRIANGLE_UPPER_TO_I4_TEST:')
    print('  Normal end of execution.')


def triangle_lower_to_i4(i, j):

    # *****************************************************************************80
    #
    # TRIANGLE_LOWER_TO_I4 converts a lower triangular coordinate to an integer.
    #
    #  Discussion:
    #
    #    Triangular coordinates are handy when storing a naturally triangular
    #    array (such as the lower half of a matrix) in a linear array.
    #
    #    Thus, for example, we might consider storing
    #
    #    (1,1)
    #    (2,1) (2,2)
    #    (3,1) (3,2) (3,3)
    #    (4,1) (4,2) (4,3) (4,4)
    #
    #    as the linear array
    #
    #    (1,1) (2,1) (2,2) (3,1) (3,2) (3,3) (4,1) (4,2) (4,3) (4,4)
    #
    #    Here, the quantities in parenthesis represent the natural row and
    #    column indices of a single number when stored in a rectangular array.
    #
    #    Thus, our goal is, given the row I and column J of the data,
    #    to produce the value K which indicates its position in the linear
    #    array.
    #
    #    The triangular numbers are the indices associated with the
    #    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
    #    and so on.
    #
    #  Formula:
    #
    #    K = J + ( (I-1) * I ) / 2
    #
    #  First Values:
    #
    #     I  J  K
    #
    #     0  0  0
    #     1  1  1
    #     2  1  2
    #     2  2  3
    #     3  1  4
    #     3  2  5
    #     3  3  6
    #     4  1  7
    #     4  2  8
    #     4  3  9
    #     4  4 10
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, the row and column indices.  I and J must
    #    be nonnegative, and J must not be greater than I.
    #
    #    Output, integer VALUE, the linear index of the (I,J) element.
    #
    from sys import exit

    if (i < 0):
        print('')
        print('TRIANGLE_LOWER_TO_I4 - Fatal error!')
        print('  I < 0.')
        print('  I = %d' % (i))
        exit('TRIANGLE_LOWER_TO_I4 - Fatal error!')

    if (j < 0):
        print('')
        print('TRIANGLE_LOWER_TO_I4 - Fatal error!')
        print('  J < 0.')
        print('  J = %d' % (j))
        exit('TRIANGLE_LOWER_TO_I4 - Fatal error!')

    if (i < j):
        print('')
        print('TRIANGLE_LOWER_TO_I4 - Fatal error!')
        print('  I < J.')
        print('  I = %d' % (i))
        print('  J = %d' % (j))
        exit('TRIANGLE_LOWER_TO_I4 - Fatal error!')

    value = j + ((i - 1) * i) // 2

    return value


def triangle_lower_to_i4_test():

    # *****************************************************************************80
    #
    # TRIANGLE_LOWER_TO_I4_TEST tests TRIANGLE_LOWER_TO_I4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TRIANGLE_LOWER_TO_I4_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANGLE_LOWER_TO_I4 converts a lower triangular index to a linear one.')
    print('')
    print('   ( I,    J ) ==> K')
    print('')

    for i in range(1, 5):
        for j in range(1, i + 1):
            k = triangle_lower_to_i4(i, j)
            print('  %4d  %4d    %4d' % (i, j, k))
#
#  Terminate.
#
    print('')
    print('TRIANGLE_LOWER_TO_I4_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    triangle_num_test()
    timestamp()
