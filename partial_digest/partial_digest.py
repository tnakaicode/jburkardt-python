#! /usr/bin/env python3
#


def find_distances(l_length, l, x_length, x, y):

    # *****************************************************************************80
    #
    # FIND_DISTANCES determines if the "free" distances include every ||X(I)-Y||.
    #
    #  Discussion:
    #
    #    This routine is given a candidate point Y, a set of placed points
    #    X(1:X_LENGTH), and a list of unused or "free" distances in
    #    L(1:L_LENGTH).  The routine seeks to find in L a copy of the
    #    distance from Y to each X.
    #
    #    If so, then the L array is reordered so that entries
    #    L(L_LENGTH-X_LENGTH+1:L_LENGTH) contain theses distances.
    #
    #    In other words, Y can be added into X, and L_LENGTH reduced to
    #    L_LENGTH-X_LENGTH.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Pavel Pevzner,
    #    Computational Molecular Biology,
    #    MIT Press, 2000,
    #    ISBN: 0-262-16197-4,
    #    LC: QH506.P47.
    #
    #  Parameters:
    #
    #    Input, integer L_LENGTH, the length of the array.
    #
    #    Input/output, integer L(L_LENGTH), the array.  On output,
    #    some entries have been shuffled.  In particular, if SUCCESS is TRUE,
    #    the entries L(L_LENGTH-X_LENGTH+1:L_LENGTH) contain the distances
    #    of X(1:X_LENGTH) to Y.
    #
    #    Input, integer X_LENGTH, the number of entries in X.
    #
    #    Input, integer X(X_LENGTH), the number of points
    #    already accepted.
    #
    #    Input, integer Y, a new point that we are considering.
    #
    #    Output, logical SUCCESS, is TRUE if the entries of L included
    #    the values of the distance of Y to each entry of X.
    #
    l2_length = l_length

    for i in range(0, x_length):

        d = abs(x[i] - y)

        success = False

        for j in range(0, l2_length):

            if (l[j] == d):
                l[j] = l[l2_length - 1]
                l[l2_length - 1] = d
                l2_length = l2_length - 1
                success = True
                break

        if (not success):
            return success, l

    success = True

    return success, l


def find_distances_test():

    # *****************************************************************************80
    #
    # FIND_DISTANCES_TEST tests FIND_DISTANCES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('FIND_DISTANCES_TEST:')
    print('  FIND_DISTANCES takes a candidate location Y')
    print('  and determines whether its distance to each point')
    print('  in the X array is listed in the L array.')

    n = 5
    l_length = n * (n - 1) // 2
    l = np.array([13, 15, 38, 90, 2, 25, 77, 23, 75, 52], dtype=np.int32)
    i4vec_print(l_length, l, '  Initial L array:')

    l, l_max = i4vec_max_last(l_length, l)
    l_length = l_length - 1

    x = np.zeros(n)
    x[0] = 0
    x[1] = l_max
    x_length = 2
#
#  Solution is X = (/ 0, 13, 15, 38, 90 /) or (/ 0, 52, 75, 77, 90 /)
#  So Y = 13, 15, 38, 52, 75 or 77 will be acceptable.
#
    l, y = i4vec_max_last(l_length, l)
    success, l = find_distances(l_length, l, x_length, x, y)

    print('')
    print('  Consider Y = %d' % (y))
    print('')
    if (success):
        print('  This Y is acceptable.')
        l_length = l_length - x_length
        x_length = x_length + 1
        x[x_length - 1] = y
        i4vec_print(x_length, x, '  New X array:')
        i4vec_print(l_length, l, '  New L array:')
    else:
        print('  This Y is not acceptable.')

    y = 35
    success, l = find_distances(l_length, l, x_length, x, y)

    print('')
    print('  Consider Y = %d' % (y))
    print('')
    if (success):
        print('  This Y is acceptable.')
        l_length = l_length - x_length
        x_length = x_length + 1
        x[x_length - 1] = y
        i4vec_print(x_length, x, '  New X array:')
        i4vec_print(l_length, l, '  New L array:')
    else:
        print('  This Y is not acceptable.')

    return


def i4_uniform_ab(a, b, seed):

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB returns a scaled pseudorandom I4.
    #
    #  Discussion:
    #
    #    The pseudorandom number will be scaled to be uniformly distributed
    #    between A and B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C, the randomly chosen integer.
    #
    #    Output, integer SEED, the updated seed.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4_UNIFORM_AB - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    a = round(a)
    b = round(b)

    r = (1.0 - r) * (min(a, b) - 0.5) \
        + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round(r)

    value = max(value, min(a, b))
    value = min(value, max(a, b))
    value = int(value)

    return value, seed


def i4_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    for i in range(1, 21):
        j, seed = i4_uniform_ab(a, b, seed)
        print('  %8d  %8d' % (i, j))
#
#  Terminate.
#
    print('')
    print('I4_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_max_last(l_length, l):

    # *****************************************************************************80
    #
    # I4VEC_MAX_LAST moves the maximum entry of an I4VEC to the last position.
    #
    #  Discussion:
    #
    #    This routine finds the largest entry in an array and moves
    #    it to the end of the array.
    #
    #    If we ignore this last array entry, then the effect is the same
    #    as "deleting" the maximum entry from the array.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Pavel Pevzner,
    #    Computational Molecular Biology,
    #    MIT Press, 2000,
    #    ISBN: 0-262-16197-4,
    #    LC: QH506.P47.
    #
    #  Parameters:
    #
    #    Input, integer L_LENGTH, the length of the array.
    #
    #    Input/output, integer L(L_LENGTH), the array.  On output,
    #    the maximum entry has been shifted to the end.
    #
    #    Output, integer VALUE, the maximum entry in the
    #    input array.
    #
    for i in range(1, l_length):
        if (l[i] < l[i - 1]):
            t = l[i]
            l[i] = l[i - 1]
            l[i - 1] = t

    value = l[l_length - 1]

    return l, value


def i4vec_max_last_test():

    # *****************************************************************************80
    #
    # I4VEC_MAX_LAST_TEST tests I4VEC_MAX_LAST.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 January 2018
    #
    #  Author:
    #
    #   John Burkardt
    #
    import numpy as np

    n = 10

    print('')
    print('I4VEC_MAX_LAST_TEST')
    print('  I4VEC_MAX_LAST identifies the largest element in an')
    print('  I4VEC, and moves it to the final entry.')

    seed = 123456789

    x = np.zeros(n)
    for i in range(0, n):
        x[i], seed = i4_uniform_ab(1, 30, seed)

    i4vec_print(n, x, '  Input vector:')

    x, x_max = i4vec_max_last(n, x)

    print('')
    print('  Maximum: %d' % (x_max))

    i4vec_print(n, x, '  Output vector:')

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


def partial_digest_recur(n, l):

    # *****************************************************************************80
    #
    # PARTIAL_DIGEST_RECUR uses recursion on the partial digest problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Pavel Pevzner,
    #    Computational Molecular Biology,
    #    MIT Press, 2000,
    #    ISBN: 0-262-16197-4,
    #    LC: QH506.P47.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of nodes.
    #
    #    Input, integer L((N*(N-1))/2), the distances between all pairs
    #    of distinct nodes.
    #
    import numpy as np
#
#  How long is L?
#
    l_length = (n * (n - 1)) // 2
#
#  Find WIDTH, the largest element of L, and move it to the last position.
#
    l, width = i4vec_max_last(l_length, l)
#
#  Think of L as being 1 entry shorter.
#
    l_length = l_length - 1
#
#  Using WIDTH, set the first two entries of X.
#
    x = np.zeros(n)
    x[0] = 0
    x[1] = width
    x_length = 2
#
#  Begin recursive operation.
#
    l_length, l, x_length, x = place(l_length, l, x_length, x)

    return


def partial_digest_recur_test01():

    # *****************************************************************************80
    #
    # PARTIAL_DIGEST_RECUR_TEST01 tests PARTIAL_DIGEST_RECUR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 5
    nn2 = (n * (n - 1)) // 2
#
#  Set the distance array.
#
    dist = np.array([2, 2, 3, 3, 4, 5, 6, 7, 8, 10], dtype=np.int32)

    print('')
    print('PARTIAL_DIGEST_RECUR_TEST01')
    print('  PARTIAL_DIGEST_RECUR generates solutions to the partial')
    print('  digest problem, using recursion.')

    print('')
    print('  The number of objects to place is N = %d' % (n))
    print('')
    print('  The original placement was 0,3,6,8,10.')
    print('  These placements generate the following distances:')

    i4vec_print(nn2, dist, '  Distance array:')

    print('')
    print('  PARTIAL_DIGEST_RECUR may recover the original placements')
    print('  from the pairwise distances.  It may also find other')
    print('  placements that have the same distance array.')

    partial_digest_recur(n, dist)

    return


def partial_digest_recur_test02():

    # *****************************************************************************80
    #
    # PARTIAL_DIGEST_RECUR_TEST02 considers tests from a library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('PARTIAL_DIGEST_RECUR_TEST02:')
    print('  PARTIAL_DIGEST_RECUR generates solutions to the partial')
    print('  digest problem, using recursion.')
    print('  TEST_PARTIAL_DIGEST creates test problems for the')
    print('  partial digest problem.')
#
#  Request a sample problem.
#
    k = 6
    dmax = 20
    seed = 123456789

    print('')
    print('  Number of nodes = %d' % (k))
    print('  Maximum distance = %d' % (dmax))

    locate, d, seed = test_partial_digest(k, dmax, seed)
#
#  Sort the data.
#
    locate = np.sort(locate)
    d = np.sort(d)
#
#  Print the data.
#
    i4vec_print(k, locate, '  Locations:')
    i4vec_print(k * (k - 1) / 2, d, '  Distances:')
#
#  Solve the problem.
#
    partial_digest_recur(k, d)

    return


def test_partial_digest(k, dmax, seed):

    # *****************************************************************************80
    #
    # TEST_PARTIAL_DIGEST returns a partial digest test problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer K, the number of objects.
    #    K must be at least 2.
    #
    #    Input, integer DMAX, the maximum possible distance.
    #    DMAX must be at least K-1.
    #
    #    Input/output, integer SEED, a seed for the random number
    #    generator.
    #
    #    Output, integer LOCATE(K), the obect locations.
    #
    #    Output, integer D(K*(K-1)/2), the pairwise distances.
    #
    import numpy as np
    from sys import exit
#
#  Check input.
#
    if (k < 2):
        print('\n')
        print('TEST_PARTIAL_DIGEST - Fatal error!\n')
        print('  Input K < 2.\n')
        exit('TEST_PARTIAL_DIGEST - Fatal error!')

    if (dmax < k - 1):
        print('\n')
        print('TEST_PARTIAL_DIGEST - Fatal error!\n')
        print('  DMAX < K - 1.\n')
        exit('TEST_PARTIAL_DIGEST - Fatal error!')
#
#  Select LOCATE, which is a random subset of the integers 0 through DMAX.
#
    locate, seed = ksub_random(dmax - 1, k - 2, seed)
    locate = np.insert(locate, 0, 0)
    locate = np.append(locate, dmax)
#
#  Compute K*(K+1)/2 pairwise distances.
#
    d = i4vec_distances(k, locate)

    return locate, d, seed


def ksub_random(n, k, seed):

    # *****************************************************************************80
    #
    # KSUB_RANDOM selects a random subset of size K from a set of size N.
    #
    #  Discussion:
    #
    #    Consider the set A(1:N) = 1, 2, 3, ... N.
    #    Choose a random index I1 between 1 and N, and swap items A(1) and A(I1).
    #    Choose a random index I2 between 2 and N, and swap items A(2) and A(I2).
    #    repeat K times.
    #    A(1:K) is your random K-subset.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 June 2011
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the size of the set from which subsets
    #    are drawn.
    #
    #    Input, integer K, number of elements in desired subsets.
    #    1 <= K <= N.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, integer A(K), the indices of the randomly
    #    chosen elements.
    #
    import numpy as np
#
#  Let B index the set.
#
    b = np.zeros(n, dtype=np.int32)
    for i in range(0, n):
        b[i] = i
#
#  Choose item 1 from N things,
#  choose item 2 from N-1 things,
#  choose item K from N-K+1 things.
#
    for i in range(0, k):

        j, seed = i4_uniform_ab(i, n - 1, seed)

        t = b[i]
        b[i] = b[j]
        b[j] = t
#
#  Copy the first K elements.
#
    a = np.zeros(k, dtype=np.int32)
    for i in range(0, k):
        a[i] = b[i]

    return a, seed


def i4vec_distances(k, locate):

    # *****************************************************************************80
    #
    # I4VEC_DISTANCES computes a pairwise distance table.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer K, the number of objects.
    #
    #    Input, integer LOCATE(K), the obect locations.
    #
    #    Output, integer D(K*(K-1)/2), the pairwise distances.
    #
    import numpy as np

    d = np.zeros(k * (k - 1) // 2)

    l = 0
    for i in range(0, k):
        for j in range(i + 1, k):
            d[l] = abs(locate[i] - locate[j])
            l = l + 1

    return d


def place(l_length, l, x_length, x):

    # *****************************************************************************80
    #
    # PLACE tries to place the next point for the partial digest problem.
    #
    #  Discussion:
    #
    #    Note that this is a recursive subroutine.  A solution to the
    #    partial digest problem is sought by calling this routine repeatedly.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Pavel Pevzner,
    #    Computational Molecular Biology,
    #    MIT Press, 2000,
    #    ISBN: 0-262-16197-4,
    #    LC: QH506.P47.
    #
    #  Parameters:
    #
    #    Input/output, integer L_LENGTH, the number of entries in L.
    #
    #    Input/output, integer L(L_LENGTH), the array of distances.
    #
    #    Input/output, integer X_LENGTH, the number of entries in X.
    #
    #    Input/output, integer X(X_LENGTH), the current partial solution.
    #

    #
    #  Are we done?
    #
    if (l_length <= 0):
        i4vec_print(x_length, x, '  Solution:')
        return l_length, l, x_length, x
#
#  Find the maximum remaining distance.
#
    l, y = i4vec_max_last(l_length, l)
#
#  We can add a point at Y if L contains all the distances from Y to
#  the current X's.
#
    success, l = find_distances(l_length, l, x_length, x, y)

    if (success):
        l_length2 = l_length - x_length
        x_length = x_length + 1
        x[x_length - 1] = y
        l_length2, l, x_length, x = place(l_length2, l, x_length, x)
        x_length = x_length - 1
#
#  We must also consider the case where Y represents the distance
#  to X[1], not X[0].
#
    y = x[1] - y

    success, l = find_distances(l_length, l, x_length, x, y)

    if (success):
        l_length2 = l_length - x_length
        x_length = x_length + 1
        x[x_length - 1] = y
        l_length2, l, x_length, x = place(l_length2, l, x_length, x)
        x_length = x_length - 1

    return l_length, l, x_length, x


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
    find_distances_test()
    i4_uniform_ab_test()
    i4vec_max_last_test()
    i4vec_print_test()
    partial_digest_recur_test01()
#
#  Test02 requires access to the TEST_PARTIAL_DIGEST library.
#
# partial_digest_recur_test02 ( )
    timestamp()
