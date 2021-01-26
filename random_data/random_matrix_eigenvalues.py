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

obj = plot2d()


def laplace_matrix():

    # *****************************************************************************80
    #
    # LAPLACE_MATRIX analyzes a matrix sampled from the Laplace distribution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2017
    #
    #  Author:
    #
    #    Original code by John D Cook.
    #    Modifications by John Burkardt.
    #
    #  Reference:
    #
    #    John D Cook,
    #    Heavy-tailed random matrices,
    #    https://www.johndcook.com/blog/
    #

    N = 5000

    print('')
    print('LAPLACE_MATRIX')
    print('  Python version: %s' % (platform.python_version()))
    print('  Examine eigenvalue distribution of %dx%d matrix' % (N, N))
    print('  with entries from Laplace distribution.')

    A = np.random.laplace(0, np.sqrt(0.5), (N, N))
    for i in range(0, N):
        A[i, 0:i] = A[0:i, i]
    eigenvalues = np.linalg.eigvalsh(A)

    print('')
    print('  Eigenvalue range: [%g, %g]' %
          (min(eigenvalues), max(eigenvalues)))

    obj.new_2Dfig(aspect="auto")
    obj.axs.hist(eigenvalues, bins=70)
    obj.axs.set_title('Laplace matrix')
    obj.SavePng(obj.tempname + "_laplace.png")


def normal_matrix():

    # *****************************************************************************80
    #
    # NORMAL_MATRIX analyzes a matrix sampled from the normal distribution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2017
    #
    #  Author:
    #
    #    Original code by John D Cook.
    #    Modifications by John Burkardt.
    #
    #  Reference:
    #
    #    John D Cook,
    #    Heavy-tailed random matrices,
    #    https://www.johndcook.com/blog/
    #

    N = 5000

    print('')
    print('NORMAL_MATRIX')
    print('  Python version: %s' % (platform.python_version()))
    print('  Examine eigenvalue distribution of %dx%d matrix' % (N, N))
    print('  with entries from normal distribution.')

    A = np.random.normal(0, 1, (N, N))
    for i in range(0, N):
        A[i, 0:i] = A[0:i, i]
    eigenvalues = np.linalg.eigvalsh(A)

    print('')
    print('  Eigenvalue range: [%g, %g]' %
          (min(eigenvalues), max(eigenvalues)))

    obj.new_2Dfig(aspect="auto")
    obj.axs.hist(eigenvalues, bins=70)
    obj.axs.set_title('Normal matrix')
    obj.SavePng(obj.tempname + "_normal.png")


def student_matrix():

    # *****************************************************************************80
    #
    # STUDENT_MATRIX analyzes a matrix sampled from the Student T distribution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2017
    #
    #  Author:
    #
    #    Original code by John D Cook.
    #    Modifications by John Burkardt.
    #
    #  Reference:
    #
    #    John D Cook,
    #    Heavy-tailed random matrices,
    #    https://www.johndcook.com/blog/
    #

    N = 5000

    print('')
    print('STUDENT_MATRIX')
    print('  Python version: %s' % (platform.python_version()))
    print('  Examine eigenvalue distribution of %dx%d matrix' % (N, N))
    print('  with entries from the Student t distribution.')

    A = np.random.standard_t(1.8, (N, N))
    for i in range(0, N):
        A[i, 0:i] = A[0:i, i]
    eigenvalues = np.linalg.eigvalsh(A)

    print('')
    print('  Eigenvalue range: [%g, %g]' %
          (min(eigenvalues), max(eigenvalues)))

    obj.new_2Dfig(aspect="auto")
    obj.axs.hist(eigenvalues, bins=70)
    obj.axs.set_title('Student t matrix')
    obj.SavePng(obj.tempname + "_student.png")


def uniform_matrix():

    # *****************************************************************************80
    #
    # UNIFORM_MATRIX analyzes a matrix sampled from the uniform distribution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2017
    #
    #  Author:
    #
    #    Original code by John D Cook.
    #    Modifications by John Burkardt.
    #
    #  Reference:
    #
    #    John D Cook,
    #    Heavy-tailed random matrices,
    #    https://www.johndcook.com/blog/
    #

    N = 5000

    print('')
    print('UNIFORM_MATRIX')
    print('  Python version: %s' % (platform.python_version()))
    print('  Examine eigenvalue distribution of %dx%d matrix' % (N, N))
    print('  with entries from uniform distribution.')

    A = np.random.random([N, N])
    for i in range(0, N):
        A[i, 0:i] = A[0:i, i]
    eigenvalues = np.linalg.eigvalsh(A)
    print('')
    print('  Eigenvalue range: [%g, %g]' %
          (min(eigenvalues), max(eigenvalues)))

    obj.new_2Dfig(aspect="auto")
    obj.axs.hist(eigenvalues, bins=70)
    obj.axs.set_title('Uniform matrix')
    obj.SavePng(obj.tempname + "_uniform.png")


if (__name__ == '__main__'):
    timestamp()
    laplace_matrix()
    normal_matrix()
    student_matrix()
    uniform_matrix()
    timestamp()
