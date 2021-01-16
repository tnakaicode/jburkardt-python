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


def hello():

    # *****************************************************************************80
    #
    # HELLO is a simple 'Hello, world!' program..
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print("Hello, world!")


def hello_mpi():

    # *****************************************************************************80
    #
    # HELLO_MPI is a simple 'Hello, world!' test of MPI4PY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    comm = MPI.COMM_WORLD

    id = comm.Get_rank()

    p = comm.Get_size()

    if (id == 0):
        print('')
        print('HELLO_MPI:')
        print('  P', id, ':  There are ', p, ' MPI processes running.')

    print('  P', id, ':  Hello, world!')


if (__name__ == '__main__'):
    timestamp()
    hello()
    hello_mpi()
    timestamp()
