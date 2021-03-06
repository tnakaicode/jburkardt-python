#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpi4py import MPI
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def prime_mpi():

    # *****************************************************************************80
    #
    # PRIME_MPI counts the primes between N_LO and N_HI.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 October 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    comm = MPI.COMM_WORLD

    id = comm.Get_rank()

    p = comm.Get_size()

    n_lo = 1
    n_hi = 131072
    n_factor = 2

    if id == 0:
        wtime = MPI.Wtime()
        print('')
        print('PRIME_MPI')
        print('  Python version: %s' % (platform.python_version()))
        print('')
        print('  Use MPI to divide the computation among')
        print('  multiple processes.')

    n = n_lo
    while n <= n_hi:
        #
        #  The PRIMES array starts out as an empty list of integers.
        #
        primes = np.array(0, dtype=np.int32)
        wtime = MPI.Wtime()

        #
        #  T counts the primes that process ID finds.
        #
        t = 0

        #
        #  Process 0 checks   2+0,   2+0  +P, 2+0  +2P  ...
        #  Process 1 checks   2+1,   2+1  +P, 2+1  +2P, ...
        #  Process P-1 checks 2+P-1, 2+P-1+P, 2+P-1+2P, ...
        #
        for i in range(2 + id, n + 1, p):
            isprime = 1
            for j in range(2, i):
                if (i % j) == 0:
                    isprime = 0
                    break
            t = t + isprime

            comm.Reduce(
                [t.to_bytes(2, 'big'), MPI.DOUBLE],
                [primes.tobytes(), MPI.INT],
                op=MPI.SUM, root=0
            )

        wtime = MPI.Wtime() - wtime

        n = n * n_factor

    if id == 0:
        print('')
        print('PRIME_MPI:')
        print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    prime_mpi()
    timestamp()
