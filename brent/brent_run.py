#! /usr/bin/env python3
#

import platform
import time
import sys
import os

sys.path.append(os.path.join("../"))
from brent.glomin import glomin_test
from brent.local_min import local_min_test
from brent.local_min_rc import local_min_rc_test
from brent.zero import zero_test
from brent.zero_rc import zero_rc_test


def brent_test():

    # *****************************************************************************80
    #
    # BRENT_TEST tests the BRENT library.
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

    print('')
    print('BRENT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the components of the BRENT library.')

    glomin_test()
    local_min_test()
    local_min_rc_test()
    zero_test()
    zero_rc_test()

    print('')
    print('BRENT_TEST:')
    print('  Normal end of execution.')


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

    return None


if (__name__ == '__main__'):
    timestamp()
    brent_test()
    timestamp()
