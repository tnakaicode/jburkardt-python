#! /usr/bin/env python3
#


def voronoi_plot(xy=[], m=200, n=200, p=2):

    # *****************************************************************************80
    #
    # VORONOI_PLOT computes a pixel plot of a Voronoi diagram.
    #
    #  Discussion:
    #
    #    Rather than doing the difficult geometry, we simply discretize the
    #    region into pixels, assign a color to each generator, and color a pixel
    #    with the color of the nearest generator.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real XY(2,NC), coordinates of center points.
    #
    #    Input, integer M, the number of rows of pixels
    #    to use in the plot.  M = 100 might be reasonable for a start.
    #
    #    Input, integer N, the number of columns of pixels
    #    to use in the plot.  N = 100 might be reasonable for a start.
    #
    #    Input, real P, the norm to be used.
    #    P = 2, the default Euclidean or L2 norm.
    #    P = Inf, the max or L-Infinity norm.
    #    P = 1, the L1 norm.
    #    Otherwise Norm(X,Y) = ( |X|^P + |Y|^P ) ^ (1/P)
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform

    print('')
    print('VORONOI_PLOT:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Display a Voronoi diagram using a pixel computation.')

    if (not len(xy)):
        nc = 15
        xy = np.random([2, nc])
#
#  How many points did we get?
#
    nc = xy.shape[1]
#
#  Compute the range of the points.
#
    xmin = min(xy[0, :])
    xmax = max(xy[0, :])
    if (xmin == xmax):
        xmin = xmin - 0.5
        xmax = xmax + 0.5
    ymin = min(xy[1, :])
    ymax = max(xy[1, :])
    if (ymin == ymax):
        ymin = ymin - 0.5
        ymax = ymax + 0.5
#
#  Compute a margin, so the extreme points are not on the boundary.
#
    margin = 0.05 * max(xmax - xmin, ymax - ymin)
#
#  Extend the region by the margin.
#
    xmin = xmin - margin
    xmax = xmax + margin
    ymin = ymin - margin
    ymax = ymax + margin
#
#  Randomly choose NC + 1 sets of RGB values.
#  Our extra color is black, just in case something goes wrong.
#
    rgb = np.zeros([nc + 1, 3], dtype=np.uint8)
    rgb = np.random.random_integers(0, 255, [nc + 1, 3])
    rgb[nc, :] = 0
#
#  Our picture A will be stored as an M x N array of RGB values
#  which are a special MATLAB data type of unsignted 8 bit integers.
#
    a = np.zeros([m, n, 3], dtype=np.uint8)
#
#  For each pixel in A, we calculate its corresponding XY position,
#  find the nearest center, and color the pixel with the corresponding
#  RGB color.  A vectorized calculation would be much faster.
#
    for i in range(0, m):

        y = (float(m - i - 1) * ymax
             + float(i) * ymin) \
            / float(m - 1)

        for j in range(0, n):

            x = (float(n - j) * xmax
                 + float(j - 1) * xmin) \
                / float(n - 1)

            nearest = nc
            distsq_min = float('Inf')

            for k in range(0, nc):

                if (np.isinf(p)):
                    distsq = max(abs(x - xy[0, k]), abs(y - xy[1, k]))
                elif (p == 2):
                    distsq = (x - xy[0, k]) ** 2 + (y - xy[1, k]) ** 2
                elif (p == 1):
                    distsq = abs(x - xy[0, k]) + abs(y - xy[1, k])
                else:
                    dx = abs(x - xy[0, k])
                    dy = abs(y - xy[1, k])
                    distsq = (dx ** p + dy ** p) ** (1.0 / p)

                if (distsq < distsq_min):
                    distsq_min = distsq
                    nearest = k

            a[i, j, :] = rgb[nearest, :]
#
#  Mark the generators as black squares.
#
    for k in range(0, nc):
        i = int((n * ymax - 1 * ymin - (n - 1) * xy[1, k]) / (ymax - ymin)) - 1
        j = int((n * xmax - 1 * xmin - (n - 1) * xy[0, k]) / (xmax - xmin)) - 1
        a[i - 1:i + 1, j - 1:j + 1, :] = 0
#
#  Display the image.
#
    plt.imshow(a)

    filename = 'voronoi.png'
    plt.savefig(filename)
    print('')
    print('  Saved graphics in file "%s"' % (filename))

    plt.show(block=False)

    return


def voronoi_plot_test():

    # *****************************************************************************80
    #
    # VORONOI_PLOT_TEST tests VORONOI_PLOT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 October 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('VORONOI_PLOT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  VORONOI_PLOT makes a simple pixel plot of a Voronoi diagram.')

    nc = 25
    xy = np.random.random([2, nc])
    voronoi_plot(xy, 200, 200, 2)
#
#  Terminate.
#
    print('')
    print('VORONOI_PLOT_TEST:')
    print('  Normal end of execution.')
    return


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
    import time

    t = time.time()
    print(time.ctime(t))

    return None


if (__name__ == '__main__'):
    import numpy as np
    timestamp()
    voronoi_plot_test()
    timestamp()
