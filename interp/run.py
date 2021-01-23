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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose_print import r8vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from i4lib.i4_normal_ab import i4_normal_ab
from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from i4lib.i4mat_uniform_ab import i4mat_uniform_ab

from r8lib.r8_uniform_01 import r8_uniform_01, r8_uniform_ab
from r8lib.r8vec_uniform_01 import r8vec_uniform_01, r8vec_uniform_ab
from r8lib.r8vec_normal_01 import r8vec_normal_01
from r8lib.r8vec_normal_ab import r8vec_normal_ab
from r8lib.r8mat_uniform_01 import r8mat_uniform_01
from r8lib.r8mat_uniform_ab import r8mat_uniform_ab
from r8lib.r8mat_normal_01 import r8mat_normal_01
from r8lib.r8mat_normal_ab import r8mat_normal_ab
from r8lib.r8vec_uniform_unit import r8vec_uniform_unit
from r8lib.r8vec_uniform_abvec import r8vec_uniform_abvec
from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec

from interp.prob_data import p00_data, p00_data_num, p00_dim_num


def lagrange_basis_1d(nd, xd, ni, xi):

    # *****************************************************************************80
    #
    # LAGRANGE_BASIS_1D evaluates a 1D Lagrange basis.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #
    #    Input, real XD(ND,1), the interpolation nodes.
    #
    #    Input, integer NI, the number of evaluation points.
    #
    #    Input, real XI(NI,1), the evaluation points.
    #
    #    Output, real LB(NI,ND), the value, at the I-th point XI, of the
    #    Jth basis function.
    #
    lb = np.zeros([ni, nd])
    for i in range(0, ni):
        for j in range(0, nd):
            lb[i, j] = 1.0
            for k in range(0, nd):
                if (k != j):
                    lb[i, j] = lb[i, j] * (xi[i] - xd[k]) / (xd[j] - xd[k])

    return lb


def lagrange_value_1d(nd, xd, yd, ni, xi):

    # *****************************************************************************80
    #
    # LAGRANGE_VALUE_1D evaluates the Lagrange interpolant.
    #
    #  Discussion:
    #
    #    The Lagrange interpolant L(ND,XD,YD)(X) is the unique polynomial of
    #    degree ND-1 which interpolates the points (XD(I),YD(I)) for I = 1
    #    to ND.
    #
    #    The Lagrange interpolant can be constructed from the Lagrange basis
    #    polynomials.  Given ND distinct abscissas, XD(1:ND), the I-th Lagrange
    #    basis polynomial LB(ND,XD,I)(X) is defined as the polynomial of degree
    #    ND - 1 which is 1 at  XD(I) and 0 at the ND - 1 other abscissas.
    #
    #    Given data values YD at each of the abscissas, the value of the
    #    Lagrange interpolant may be written as
    #
    #      L(ND,XD,YD)(X) = sum ( 1 <= I <= ND ) LB(ND,XD,I)(X) * YD(I)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #    ND must be at least 1.
    #
    #    Input, real XD(ND,1), the data points.
    #
    #    Input, real YD(ND,1), the data values.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI,1), the interpolation points.
    #
    #    Output, real YI(NI,1), the interpolated values.
    #
    lb = lagrange_basis_1d(nd, xd, ni, xi)
    yi = np.dot(lb, yd)
    return yi


def nearest_interp_1d(nd, xd, yd, ni, xi):

    # *****************************************************************************80
    #
    # NEAREST_INTERP_1D evaluates the nearest neighbor interpolant.
    #
    #  Discussion:
    #
    #    The nearest neighbor interpolant L(ND,XD,YD)(X) is the piecewise
    #    constant function which interpolates the data (XD(I),YD(I)) for I = 1
    #    to ND.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #    ND must be at least 1.
    #
    #    Input, real XD(ND), the data points.
    #
    #    Input, real YD(ND), the data values.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI), the interpolation points.
    #
    #    Output, real YI(NI), the interpolated values.
    #

    yi = np.zeros(ni)
    for i in range(0, ni):
        d = float('Inf')
        k = -1
        for k2 in range(0, nd):
            d2 = abs(xi[i] - xd[k2])
            if (d2 < d):
                k = k2
                d = d2
        yi[i] = yd[k]
    return yi


def shepard_value_1d(nd, xd, yd, p, ni, xi):

    # *****************************************************************************80
    #
    # SHEPARD_VALUE_1D evaluates a 1D Shepard interpolant.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Donald Shepard,
    #    A two-dimensional interpolation function for irregularly spaced data,
    #    ACM '68: Proceedings of the 1968 23rd ACM National Conference,
    #    ACM, pages 517-524, 1969.
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #    Input, real XD(ND), the data points.
    #    Input, real YD(ND), the data values.
    #    Input, real P, the power.
    #    Input, integer NI, the number of interpolation points.
    #    Input, real XI(NI), the interpolation points.
    #
    #    Output, real YI(NI), the interpolated values.
    #

    yi = np.zeros(ni)
    w = np.zeros(nd)
    for i in range(0, ni):
        if (p == 0.0):
            for j in range(0, nd):
                w[j] = 1.0 / float(nd)
        else:
            z = -1
            for j in range(0, nd):
                w[j] = abs(xi[i] - xd[j])
                if (w[j] == 0.0):
                    z = j

            if (z != -1):
                for j in range(0, nd):
                    w[j] = 0.0
                w[z] = 1.0
            else:
                for j in range(0, nd):
                    w[j] = 1.0 / w[j] ** p
                s = np.sum(w)
                for j in range(0, nd):
                    w[j] = w[j] / s

        for j in range(0, nd):
            yi[i] = yi[i] + w[j] * yd[j]

    return yi


class BaseInterp(plot2d):

    def __init__(self):
        plot2d.__init__(self)

        self.p = 10.0
        self.prob = 6
        self.dim_num = p00_dim_num(self.prob)
        self.nd = p00_data_num(self.prob)
        self.xy = p00_data(self.prob, self.dim_num, self.nd)
        print('  Number of data points = %d' % (self.nd))

    def shepard_interp_1d_test01(self):
        self.interp_name = "shepard"

        xd = self.xy[0, :]
        yd = self.xy[1, :]
        xmin, xmax = np.min(xd), np.max(xd)
        ymin, ymax = np.min(yd), np.max(yd)
        xrng = (xmax - xmin) * 0.05

        ni = 501
        xi = np.linspace(xmin - xrng / 2, xmax + xrng / 2, ni)
        yi = shepard_value_1d(self.nd, xd, yd, self.p, ni, xi)
        self.plot_interp_1d(xd, yd, xi, yi)

    def nearest_interp_1d_test01(self):
        self.interp_name = "nearest"

        xd = self.xy[0, :]
        yd = self.xy[1, :]
        xmin, xmax = np.min(xd), np.max(xd)
        ymin, ymax = np.min(yd), np.max(yd)
        xrng = (xmax - xmin) * 0.05

        ni = 501
        xi = np.linspace(xmin - xrng / 2, xmax + xrng / 2, ni)
        yi = nearest_interp_1d(self.nd, xd, yd, ni, xi)
        self.plot_interp_1d(xd, yd, xi, yi)

    def lagrange_interp_1d_test01(self):
        self.interp_name = "lagrange"

        xd = self.xy[0, :]
        yd = self.xy[1, :]
        xmin, xmax = np.min(xd), np.max(xd)
        ymin, ymax = np.min(yd), np.max(yd)
        xrng = (xmax - xmin) * 0.05

        ni = 501
        xi = np.linspace(xmin + xrng / 2, xmax - xrng / 2, ni)
        yi = lagrange_value_1d(self.nd, xd, yd, ni, xi)
        self.plot_interp_1d(xd, yd, xi, yi)

    def plot_interp_1d(self, xd, yd, xi, yi):
        t0 = "prob{:03d} Piecewise Linear Interpolant".format(self.prob)
        p0 = "prob{:03d}_data.png".format(self.prob)
        t1 = "prob{:03d} {} interpolate".format(self.prob, self.interp_name)
        p1 = "prob{:03d}_{}.png".format(self.prob, self.interp_name)

        self.new_2Dfig(aspect="auto")
        self.axs.plot(xd, yd, 'b-', linewidth=3.0)
        self.axs.plot(xd, yd, 'k.', markersize=10)
        self.axs.set_title(t0)
        self.axs.set_xlabel('<---X--->')
        self.axs.set_ylabel('<---Y--->')
        self.SavePng(self.tmpdir + p0)

        self.new_2Dfig(aspect="auto")
        self.axs.plot(xd, yd, 'b-', linewidth=3.0)
        self.axs.plot(xi, yi, 'r-', linewidth=4.0)
        self.axs.plot(xd, yd, 'k.', markersize=10)
        self.axs.set_title(t1)
        self.axs.set_xlabel('<---X--->')
        self.axs.set_ylabel('<---Y--->')
        self.SavePng(self.tmpdir + p1)
        plt.clf()


if (__name__ == '__main__'):
    obj = BaseInterp()
    obj.shepard_interp_1d_test01()
    obj.nearest_interp_1d_test01()
    obj.lagrange_interp_1d_test01()
