#! /usr/bin/env python3
#
def four_fifths(n):

    # *****************************************************************************80
    #
    # four_fifths searches for a solution to the four fifths problem.
    #
    #  Discussion:
    #
    #    Euler conjectured that a fifth power cannot be represented as
    #    the sum of less than 5 fifth powers.
    #
    #    The correct equation is:
    #
    #      27^5 + 84^5 + 110^5 + 133^5 = 144^5 = 61917364224
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 September 2018
    #
    #  Author:
    #
    #    Brian Hayes
    #
    #  Reference:
    #
    #    Brian Hayes,
    #    Four Fifths = A Fifth
    #    http://bit-player.org/
    #    Posted on 03 December 2014.
    #
    #  Input:
    #
    #    integer N, the upper limit for the range of integers to search.
    #
    import itertools as it

    """Return smallest positive integers ((a,b,c,d),e) such that
     a^5 + b^5 + c^5 + d^5 = e^5; if no such tuple exists
     with e < n, return the string 'Failed'."""

    fifths = [x ** 5 for x in range(n)]

    combos = it.combinations_with_replacement(range(1, n), 4)

    count = 0

    while True:

        try:
            count = count + 1
            cc = next(combos)
            cc_sum = sum([fifths[i] for i in cc])
            if cc_sum in fifths:
                return (cc, fifths.index(cc_sum), count)

        except StopIteration:
            return ('Failed')


def four_fifths_test():

    # *****************************************************************************80
    #
    # four_fifths_test tests four_fifths().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('four_fifths_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  four_fifths() seeks a solution of the four fifths problem:')
    print('  Find integers a, b, c, d and e such that')
    print('    a^5 + b^5 + c^5 + d^5 = e^5.')

    n = 150
    cc, index, count = four_fifths(n)

    print('')
    print('  Result:')
    print('    %d^5  + %d^5  + %d^5  + %d^5  = %d^5' %
          (cc[0], cc[1], cc[2], cc[3], index))
    print('  A solution was found after ',
          count, ' combinations were checked.')
#
#  Terminate.
#
    print('')
    print('four_fifths_test:')
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

    return


if (__name__ == '__main__'):
    timestamp()
    four_fifths_test()
    timestamp()
