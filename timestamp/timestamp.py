#! /usr/bin/env python3
#
import time


def timestamp():

    # *****************************************************************************80
    #
    # timestamp prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    t = time.time()
    print(time.ctime(t))
    return t


if (__name__ == '__main__'):
    timestamp()
