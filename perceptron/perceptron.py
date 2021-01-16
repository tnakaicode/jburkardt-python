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


def perceptron():

    # *****************************************************************************80
    #
    # perceptron demonstrates the perceptron algorithm.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('perceptron')
    print('  Python version: %s' % (platform.python_version()))
    print('  The Perceptron.')
    print('  Data file: index, rpm, vibration, rating')
    print('  Rating is 0 for bad, 1 for good.')
    print('  Use the perceptron algorithm to determine a')
    print('  classifier f(rpm,vibration) -> {0, 1}')

    #
    #  Read the data file.
    #
    print('')
    print('  Generator Ratings')
    data = np.loadtxt('generators.txt')
    rpm = data[:, 1]
    vib = data[:, 2]
    grade = data[:, 3]
    n = len(rpm)

    #  Part 1.
    print('')
    print('  Number of generators = %d' % (n))
    rpm_min = np.min(rpm)
    rpm_max = np.max(rpm)
    vib_min = np.min(vib)
    vib_max = np.max(vib)
    good = (grade == +1.0)
    bad = (grade == 0.0)
    n_good = len(good)
    n_bad = len(bad)
    bad_rpm_mean = np.mean(rpm[bad])
    bad_vib_mean = np.mean(vib[bad])
    good_rpm_mean = np.mean(rpm[good])
    good_vib_mean = np.mean(vib[good])

    print('  %d good generators, and %d bad generators' % (n_good, n_bad))
    print('  %g <= RPM <= %g' % (rpm_min, rpm_max))
    print('  %g <= VIB <= %g' % (vib_min, vib_max))
    print('  GOOD: mean RPM = %g, mean VIB = %g' %
          (good_rpm_mean, good_vib_mean))
    print('  BAD:  mean RPM = %g, mean VIB = %g' %
          (bad_rpm_mean, bad_vib_mean))
    print('  %g <= VIB <= %g' % (vib_min, vib_max))

    filename = 'perceptron_data.png'
    obj.new_2Dfig()
    obj.axs.plot(rpm[good], vib[good], 'b+', rpm[bad], vib[bad], 'ro')
    obj.axs.set_xlabel('<-- RPM -->')
    obj.axs.set_ylabel('<-- VIB -->')
    obj.axs.set_title('Generator Ratings')
    obj.SavePng(filename)
    print('  Graphics saved as "%s"' % (filename))

    #  Part 2.
    #  Work with normalized data.
    r = (rpm - np.min(rpm)) / (np.max(rpm) - np.min(rpm))
    v = (vib - np.min(vib)) / (np.max(vib) - np.min(vib))
    #  Perceptron algorithm.
    alpha = 0.01
    m = 3
    w = np.ones(m) / m
    x = np.zeros([n, 3])
    x[:, 0] = 1.0
    x[:, 1] = np.copy(r)
    x[:, 2] = np.copy(v)

    e = 1
    step = 0

    while (e != 0 and step < 100):
        e = 0
        step = step + 1
        for i in range(0, n):
            f = (0 < np.dot(x[i, :], w[:]))
            e = e + (grade[i] != f)
            w = w + alpha * np.dot(x[i, :], (grade[i] - f))
        w = w / np.linalg.norm(w)

    if (e == 0):
        print('  All training data classified on step %d' % (step))
    else:
        print('  Iteration terminated without convergence on step %d' % (step))

    print('')
    print('  Perceptron weights:')
    print('  f(x) = %g + %g * r + %g * v' % (w[0], w[1], w[2]))
    print('')
    print('')
    print('  Index    x*w  (0<x*w)  Rating')
    print('')
    c = np.dot(x, w)
    f = (0 < c)
    for j in range(0, n):
        print('     %2d  %6.2f      %g      %g' % (j, c[j], f[j], grade[j]))

    px = np.zeros(0)
    py = np.zeros(0)

    rv = 0.0
    vv = (- w[0] - w[1] * rv) / w[2]
    if (0.0 <= vv and vv <= +1.0):
        px = np.append(px, rv)
        py = np.append(py, vv)

    vv = 0.0
    rv = (- w[0] - w[2] * vv) / w[1]
    if (0.0 <= rv and rv <= +1.0):
        px = np.append(px, rv)
        py = np.append(py, vv)

    vv = +1.0
    rv = (- w[0] - w[2] * vv) / w[1]
    if (0.0 <= rv and rv <= +1.0):
        px = np.append(px, rv)
        py = np.append(py, vv)

    rv = +1.0
    vv = (- w[0] - w[1] * rv) / w[2]
    if (0.0 <= vv and vv <= +1.0):
        px = np.append(px, rv)
        py = np.append(py, vv)

    filename = 'perceptron_classifier.png'
    obj.new_2Dfig()
    obj.axs.plot(r[good], v[good], 'b+', r[bad], v[bad], 'ro')
    obj.axs.plot(px, py, 'k-', linewidth=3)
    obj.axs.set_xlabel('<-- RPM -->')
    obj.axs.set_ylabel('<-- VIB -->')
    obj.axs.set_title('Generator Ratings Classifier')
    obj.SavePng(filename)
    print('  Graphics saved as "%s"' % (filename))
    print('')
    print('perceptron')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    perceptron()
    timestamp()
