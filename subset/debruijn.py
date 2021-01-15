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

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from subset.index_unrank0 import index_unrank0
from subset.index_rank0 import index_rank0
from subset.digraph_arc_euler import digraph_arc_euler
from subset.digit_to_ch import digit_to_ch


def debruijn(m, n):

    # *****************************************************************************80
    #
    # DEBRUIJN constructs a de Bruijn sequence.
    #
    #  Discussion:
    #
    #    Suppose we have an alphabet of M letters, and we are interested in
    #    all possible strings of length N.  If M = 2 and N = 3, then we are
    #    interested in the M^N strings:
    #
    #      000
    #      001
    #      010
    #      011
    #      100
    #      101
    #      110
    #      111
    #
    #    Now, instead of making a list like this, we prefer, if possible, to
    #    write a string of letters, such that every consecutive sequence of
    #    N letters is one of the strings, and every string occurs once, if
    #    we allow wraparound.
    #
    #    For the above example, a suitable sequence would be the 8 characters:
    #
    #      00011101(00...
    #
    #    where we have suggested the wraparound feature by repeating the first
    #    two characters at the end.
    #
    #    Such a sequence is called a de Bruijn sequence.  It can easily be
    #    constructed by considering a directed graph, whose nodes are all
    #    M^(N-1) strings of length N-1.  A node I has a directed edge to
    #    node J (labeled with character K) if the string at node J can
    #    be constructed by beheading the string at node I and adding character K.
    #
    #    In this setting, a de Bruijn sequence is simply an Eulerian circuit
    #    of the directed graph, with the edge labels being the entries of the
    #    sequence.  In general, there are many distinct de Bruijn sequences
    #    for the same parameter M and N.  This program will only find one
    #    of them.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of letters in the alphabet.
    #
    #    Input, integer N, the number of letters in a codeword.
    #
    #    Output, integer STRING(M^N), a deBruijn string.
    #

    #
    #  Construct the adjacency information.
    #
    nnode = m ** (n - 1)
    nedge = m ** n

    iedge = 0

    inode = np.zeros(nedge, dtype=np.int32)
    jnode = np.zeros(nedge, dtype=np.int32)
    knode = np.zeros(nedge, dtype=np.int32)
    jvec = np.zeros(n - 1, dtype=np.int32)

    for i in range(1, nnode + 1):

        ivec = index_unrank0(n - 1, m, i)

        for k in range(0, m):

            for l in range(0, n - 2):
                jvec[l] = ivec[l + 1]
            jvec[n - 2] = k + 1

            j = index_rank0(n - 1, m, jvec)

            inode[iedge] = i
            jnode[iedge] = j
            knode[iedge] = k + 1
            iedge = iedge + 1
    
    #
    #  Determine a circuit.
    #
    success, trail = digraph_arc_euler(nnode, nedge, inode, jnode)
    
    #
    #  The string is constructed from the labels of the edges in the circuit.
    #
    s = ''
    for i in range(0, nedge):
        s = s + digit_to_ch(knode[trail[i] - 1])

    return s


def debruijn_test():

    # *****************************************************************************80
    #
    # DEBRUIJN_TEST tests DEBRUIJN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    mtest = np.array([2, 3, 2])
    ntest = np.array([3, 3, 4])

    print('')
    print('DEBRUIJN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DEBRUIJN computes a de Bruijn string.')

    for itest in range(0, 3):

        m = mtest[itest]
        n = ntest[itest]

        print('')
        print('  The alphabet size is M = %d' % (m))
        print('  The string length is N = %d' % (n))

        s = debruijn(m, n)

        print('')
        print('    %s' % (s))

    print('')
    print('DEBRUIJN_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    debruijn_test()
    timestamp()
