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

from i4lib.i4vec_reverse import i4vec_reverse
from subset.digraph_arc_print import digraph_arc_print


def digraph_arc_euler(nnode, nedge, inode, jnode):

    # *****************************************************************************80
    #
    # DIGRAPH_ARC_EULER returns an Euler circuit in a digraph.
    #
    #  Description:
    #
    #    An Euler circuit of a digraph is a path which starts and ends at
    #    the same node and uses each directed edge exactly once.  A digraph is
    #    eulerian if it has an Euler circuit.  The problem is to decide whether
    #    a given digraph is eulerian and to find an Euler circuit if the
    #    answer is affirmative.
    #
    #    A digraph has an Euler circuit if and only if the number of incoming
    #    edges is equal to the number of outgoing edges at each node.
    #
    #    This characterization gives a straightforward procedure to decide whether
    #    a digraph is eulerian.  Furthermore, an Euler circuit in an eulerian
    #    digraph G of NEDGE edges can be determined by the following method:
    #
    #      STEP 1: Choose any node U as the starting node, and traverse any edge
    #      ( U, V ) incident to node U, and than traverse any unused edge incident
    #      to node U.  Repeat this process of traversing unused edges until the
    #      starting node U is reached.  Let P be the resulting walk consisting of
    #      all used edges.  If all edges of G are in P, than stop.
    #
    #      STEP 2: Choose any unused edge ( X,  Y) in G such that X is
    #      in P and Y is not in P.  Use node X as the starting node and
    #      find another walk Q using all unused edges as in step 1.
    #
    #      STEP 3: Walk P and walk Q share a common node X, they can be merged
    #      to form a walk R by starting at any node S of P and to traverse P
    #      until node X is reached than, detour and traverse all edges of Q
    #      until node X is reached and continue to traverse the edges of P until
    #      the starting node S is reached.  Set P = R.
    #
    #      STEP 4: Repeat steps 2 and 3 until all edges are used.
    #
    #    The running time of the algorithm is O ( NEDGE ).
    #
    #    The digraph is assumed to be connected.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 July 2004
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Hang Tong Lau,
    #    Algorithms on Graphs,
    #    Tab Books, 1989.
    #
    #  Parameters:
    #
    #    Input, integer NNODE, the number of nodes.
    #
    #    Input, integer NEDGE, the number of edges.
    #
    #    Input, integer INODE(NEDGE), JNODE(NEDGE) the I-th edge starts at node
    #    INODE(I) and ends at node JNODE(I).
    #
    #    Output, logical SUCCESS, is TRUE if an Euler circuit was found,
    #    and FALSE otherwise.
    #
    #    Output, integer TRAIL(NEDGE).  TRAIL(I) is the edge number of the I-th
    #    edge in the Euler circuit.
    #

#
#  Check if the digraph is eulerian.
#
    trail = np.zeros(nedge, dtype=np.int32)
    endnod = np.zeros(nedge, dtype=np.int32)

    for i in range(1, nedge + 1):
        j = inode[i - 1]
        trail[j - 1] = trail[j - 1] + 1
        j = jnode[i - 1]
        endnod[j - 1] = endnod[j - 1] + 1

    for i in range(1, nnode + 1):
        if (trail[i - 1] != endnod[i - 1]):
            success = False
            return success, trail
#
#  The digraph is eulerian find an Euler circuit.
#
    success = 1
    lensol = 1
    lenstk = 0
#
#  Find the next edge.
#
    stacks = np.zeros(2 * nedge, dtype=np.int32)
    candid = np.zeros(nedge, dtype=np.int32)

    while (True):

        if (lensol == 1):

            endnod[0] = inode[0]
            stacks[0] = 1
            stacks[1] = 1
            lenstk = 2

        else:

            l = lensol - 1

            if (lensol != 2):
                endnod[l - 1] = inode[trail[l - 1] - 1] + \
                    jnode[trail[l - 1] - 1] - endnod[l - 2]

            k = endnod[l - 1]

            for i in range(1, nedge + 1):
                candid[i - 1] = (k == jnode[i - 1])

            for i in range(1, l + 1):
                candid[trail[i - 1] - 1] = False

            lens = lenstk

            for i in range(1, nedge + 1):

                if (candid[i - 1]):
                    lens = lens + 1
                    stacks[lens - 1] = i

            stacks[lens] = lens - lenstk
            lenstk = lens + 1

        while (True):

            istak = stacks[lenstk - 1]
            lenstk = lenstk - 1

            if (istak != 0):
                break

            lensol = lensol - 1

            if (lensol == 0):
                trail = i4vec_reverse(nedge, trail)
                return success, trail

        trail[lensol - 1] = stacks[lenstk - 1]
        stacks[lenstk - 1] = istak - 1

        if (lensol == nedge):
            break

        lensol = lensol + 1

    trail = i4vec_reverse(nedge, trail)

    return success, trail


def digraph_arc_euler_test():

    # *****************************************************************************80
    #
    # DIGRAPH_ARC_EULER_TEST calls DIGRAPH_ARC_EULER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    nedge = 7
    nnode = 5

    inode = np.array([2, 1, 2, 1, 3, 5, 4], dtype=np.int32)
    jnode = np.array([5, 4, 3, 2, 1, 1, 2], dtype=np.int32)

    print('')
    print('DIGRAPH_ARC_EULER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DIGRAPH_ARC_EULER finds an Euler circuit of a digraph.')

    digraph_arc_print(nedge, inode, jnode, '  The arc list of the digraph:')

    success, trail = digraph_arc_euler(nnode, nedge, inode, jnode)

    if (success):

        i4vec_print(nedge, trail, '  The edge list of the Euler circuit:')

        print('')
        print('  The node list of the Euler circuit:')
        print('')
        print('    I  Edge  Node')
        print('')

        for i in range(1, nedge + 1):

            j = trail[i - 1]

            if (i == nedge):
                jp1 = trail[0]
            else:
                jp1 = trail[i]

            if (jnode[j - 1] == inode[jp1 - 1]):
                inn = jnode[j - 1]
            else:
                print('')
                print('The circuit has failed!')
                break

            print('  %4d  %4d  %4d' % (i, j, inn))

    else:

        print('')
        print('  The digraph is not eulerian.')
        print('')
#
#  Terminate.
#
    print('')
    print('DIGRAPH_ARC_EULER_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    digraph_arc_euler_test()
    timestamp()
