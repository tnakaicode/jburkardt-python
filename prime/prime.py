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


def prime():

    # *****************************************************************************80
    #
    # MAIN is the main program for prime.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('prime')
    print('  Python version: %s' % (platform.python_version()))
    print('  Count the primes between N_LO and N_HI.')

    n_lo = 1
    # n_hi = 131072
    n_hi = 10000
    n_factor = 2
    prime_number_sweep(n_lo, n_hi, n_factor)

    print('')
    print('prime')
    print('  Normal end of execution.')


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


def prime_number_sweep(n_lo, n_hi, n_factor):

    # *****************************************************************************80
    #
    # PRIME_NUMBER_SWEEP does repeated timed calls to PRIME_NUMBER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N_LO, the first value of N.
    #
    #    Input, integer N_HI, the last value of N.
    #
    #    Input, integer N_FACTOR, the factor by which to increase N
    #    after each iteration.
    #

    print('')
    print('PRIME_NUMBER_SWEEP')
    print('  Call PRIME_NUMBER to count the primes from 1 to N.')
    print('')
    print('         N         Pi       Time')
    print('')

    n = n_lo

    while n <= n_hi:
        wtime = time.time()
        primes = prime_number(n)
        wtime = time.time() - wtime
        print('{0:10d} {1:10d} {2:10.5f}'.format(n, primes, wtime))
        n = n * n_factor


def prime_number(n):

    # *****************************************************************************80
    #
    # PRIME_NUMBER returns the number of primes between 1 and N.
    #
    #  Discussion:
    #
    #    A naive algorithm is used.
    #
    #    Mathematica can return the number of primes less than or equal to N
    #    by the command PrimePi[N].
    #
    #                N  PRIME_NUMBER
    #
    #                1           0
    #               10           4
    #              100          25
    #            1,000         168
    #           10,000       1,229
    #          100,000       9,592
    #        1,000,000      78,498
    #       10,000,000     664,579
    #      100,000,000   5,761,455
    #    1,000,000,000  50,847,534
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the maximum number to check.
    #
    #    Output, integer TOTAL, the number of prime numbers up to N.
    #
    total = 0

    for i in range(2, n + 1):

        prime = 1

        for j in range(2, i):
            if (i % j) == 0:
                prime = 0
                break

        total = total + prime

    return total


if (__name__ == '__main__'):
    timestamp()
    prime()
    prime_mpi()
    timestamp()
