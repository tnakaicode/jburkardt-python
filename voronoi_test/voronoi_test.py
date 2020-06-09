#! /usr/bin/env python3
#


def voronoi_test():

    # *****************************************************************************80
    #
    # VORONOI_TEST tests VORONOI and VORONOI_PLOT_2D.
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
    import matplotlib.pyplot as plt
    import platform
    import numpy as np
    from scipy.spatial import Voronoi
    from scipy.spatial import voronoi_plot_2d

    print('')
    print('VORONOI_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  scipy.spatial.Voronoi computes the Voronoi diagram of a set of points.')
    print('  scipy.spatial.voronoi_plot_2d will plot it.')
#
#  Select the points.
#
    nc = 25
    xy = np.random.random([nc, 2])
#
#  Compute the diagram.
#
    diagram = Voronoi(xy)
#
#  Plot the diagram.
#
    voronoi_plot_2d(diagram)
#
#  Save the plot.
#
    filename = 'voronoi_test.png'
    plt.savefig(filename)
    print('')
    print('  Saved graphics in file "%s"' % (filename))
#
#  Display the plot.
#
    plt.show(block=False)
#
#  Terminate.
#
    print('')
    print('VORONOI_TEST:')
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
    voronoi_test()
    timestamp()
