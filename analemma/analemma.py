#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def analemma(ecc, lon, obliq):

    # *****************************************************************************80
    #
    # ANALEMMA computes the analemma.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2017
    #
    #  Author:
    #
    #    Original C version by Brian Tung.
    #    Python version by John Burkardt.
    #
    #  Parameters:
    #
    #    Optional input, double ECC, the orbital eccentricity.
    #
    #    Optinal input, double LON, the longitude of the perihelion in degrees.
    #
    #    Optional input, double OBLIQ, the obliquity in degrees.
    #

    days = 365.242

    #  Internally, longitude and obliquity are in radians.
    lon = lon * np.pi / 180.0
    obliq = obliq * np.pi / 180.0

    #  Compute the data using vector operations.
    n = 1001

    t01 = np.zeros(n)
    eot = np.zeros(n)
    dec = np.zeros(n)

    f = np.linspace(0.0, 1.0, n)
    tau = 2.0 * np.pi * f

    #  Set theta to the current longitude.
    theta = np.arctan2(np.sqrt(1.0 - ecc * ecc) *
                       np.sin(tau), np.cos(tau) - ecc)

    #  Rotate clockwise in XY plane by theta, corrected by lon.
    x1 = np.cos(theta - (lon - np.pi / 2.0))
    y1 = np.sin(theta - (lon - np.pi / 2.0))
    z1 = 0.0

    #  Rotate counter-clockwise in XZ plane by obliq.
    x2 = np.cos(obliq) * x1 + np.sin(obliq) * z1
    y2 = y1
    z2 = - np.sin(obliq) * x1 + np.cos(obliq) * z1

    #  Set t equal to real time from tau and
    #  rotate counter-clockwise by t, corrected by lon
    t = tau - ecc * np.sin(tau)
    x3 = np.cos(t - (lon - np.pi / 2.0)) * x2 + \
        np.sin(t - (lon - np.pi / 2.0)) * y2
    y3 = - np.sin(t - (lon - np.pi / 2.0)) * x2 + \
        np.cos(t - (lon - np.pi / 2.0)) * y2
    z3 = z2

    t01 = t / 2.0 / np.pi
    eot = - np.arctan2(y3, x3) * 4.0 * 180 / np.pi * days / (days + 1.0)
    dec = np.arcsin(z3) * 180.0 / np.pi

    #  Plot the equation of time.
    plt.plot(t01, eot, 'b-')
    plt.grid(True)
    plt.xlabel('<---Normalized Date--->')
    plt.ylabel('<---Minutes Early/Late--->')
    plt.title('Equation of Time')
    plt.savefig('eot.png')

    #  Plot the declination.
    plt.plot(t01, dec, 'b-')
    plt.grid(True)
    plt.xlabel('<---Normalized Date--->')
    plt.ylabel('<---Degrees North/South--->')
    plt.title('Declination')
    plt.savefig('declination.png')

    #  Plot the analemma.
    plt.plot(eot, dec, 'b-')
    plt.grid(True)
    plt.xlabel('<---Minutes Early/Late--->')
    plt.ylabel('<---Degrees North/South--->')
    plt.title('Analemma')
    plt.savefig('analemma.png')


class AnalemaCurve(plot2d):

    #
    # ANALEMMA computes the analemma.
    #
    #  Parameters:
    #
    #    Optional input, double ECC, the orbital eccentricity.
    #    Optinall input, double LON, the longitude of the perihelion in degrees.
    #    Optional input, double OBLIQ, the obliquity in degrees.
    #

    def __init__(self, ecc, lon, obliq):
        plot2d.__init__(self, aspect="equal")

        days = 365.242

        #  Internally, longitude and obliquity are in radians.
        lon = lon * np.pi / 180.0
        obliq = obliq * np.pi / 180.0

        #  Compute the data using vector operations.
        n = 1001

        t01 = np.zeros(n)
        eot = np.zeros(n)
        dec = np.zeros(n)

        f = np.linspace(0.0, 1.0, n)
        tau = 2.0 * np.pi * f

        #  Set theta to the current longitude.
        theta = np.arctan2(np.sqrt(1.0 - ecc * ecc) *
                           np.sin(tau), np.cos(tau) - ecc)

        #  Rotate clockwise in XY plane by theta, corrected by lon.
        x1 = np.cos(theta - (lon - np.pi / 2.0))
        y1 = np.sin(theta - (lon - np.pi / 2.0))
        z1 = 0.0

        #  Rotate counter-clockwise in XZ plane by obliq.
        x2 = np.cos(obliq) * x1 + np.sin(obliq) * z1
        y2 = y1
        z2 = - np.sin(obliq) * x1 + np.cos(obliq) * z1

        #  Set t equal to real time from tau and
        #  rotate counter-clockwise by t, corrected by lon
        t = tau - ecc * np.sin(tau)
        x3 = np.cos(t - (lon - np.pi / 2.0)) * x2 + \
            np.sin(t - (lon - np.pi / 2.0)) * y2
        y3 = - np.sin(t - (lon - np.pi / 2.0)) * x2 + \
            np.cos(t - (lon - np.pi / 2.0)) * y2
        z3 = z2

        t01 = t / 2.0 / np.pi
        eot = - np.arctan2(y3, x3) * 4.0 * 180 / np.pi * days / (days + 1.0)
        dec = np.arcsin(z3) * 180.0 / np.pi

        #  Plot the equation of time.
        self.new_2Dfig(aspect="auto")
        self.axs.plot(t01, eot, 'b-')
        self.axs.set_xlabel('<---Normalized Date--->')
        self.axs.set_ylabel('<---Minutes Early/Late--->')
        self.axs.set_title('Equation of Time')
        self.SavePng('eot.png')

        #  Plot the declination.
        self.new_2Dfig(aspect="auto")
        self.axs.plot(t01, dec, 'b-')
        self.axs.set_xlabel('<---Normalized Date--->')
        self.axs.set_ylabel('<---Degrees North/South--->')
        self.axs.set_title('Declination')
        self.SavePng('declination.png')

        #  Plot the analemma.
        self.new_2Dfig(aspect="equal")
        self.axs.plot(eot, dec, 'b-')
        self.axs.set_xlabel('<---Minutes Early/Late--->')
        self.axs.set_ylabel('<---Degrees North/South--->')
        self.axs.set_title('Analemma')
        self.SavePng('analemma.png')


def analemma_test():

    # *****************************************************************************80
    #
    # ANALEMMA_TEST tests ANALEMMA.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2017
    #
    #  Author:
    #
    #    Original C version by Brian Tung.
    #    Python version by John Burkardt.
    #

    print('')
    print('ANALEMMA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ANALEMMA computes the analemma curve for given values of')
    print('  eccentricity, longitude, and obliquity.')

    ecc = 0.01671
    lon = 1.347 * 180.0 / np.pi
    obliq = 0.4091 * 180.0 / np.pi

    analemma(ecc, lon, obliq)
    print('')
    print('ANALEMMA_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    # analemma_test()

    ecc = 0.01671
    lon = 1.347 * 180.0 / np.pi
    obliq = 0.4091 * 180.0 / np.pi

    AnalemaCurve(ecc, lon, obliq)
    timestamp()
