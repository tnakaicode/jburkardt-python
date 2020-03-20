import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import sys
import os
import time
from scipy.spatial import ConvexHull

sys.path.append(os.path.join('../'))
from base import plot2d

""" Spatial Transformations
.. autosummary::
   :toctree: generated/

   KDTree      -- class for efficient nearest-neighbor queries
   cKDTree     -- class for efficient nearest-neighbor queries (faster impl.)
   Rectangle
"""

""" Delaunay Triangulation, Convex Hulls and Voronoi Diagrams
.. autosummary::
   :toctree: generated/

   Delaunay    -- compute Delaunay triangulation of input points
   ConvexHull  -- compute a convex hull for input points
   Voronoi     -- compute a Voronoi diagram hull from input points
   SphericalVoronoi -- compute a Voronoi diagram from input points on the surface of a sphere
   HalfspaceIntersection -- compute the intersection points of input halfspaces
"""


class ConvexArea (plot2d):

    def __init__(self, num=30, idx=2):
        plot2d.__init__(self)
        self.pnt = np.random.rand(num, 3)
        self.cov = ConvexHull(self.pnt[:, 0:2])
        self.axs.plot(self.pnt[:, 0], self.pnt[:, 1], 'o')

        print(self.cov)
        for idx in self.cov.simplices:
            x = self.pnt[idx, 0]
            y = self.pnt[idx, 1]
            print(idx, x, y)
            self.axs.plot(x, y, 'k-')

        print(self.cov.vertices)

        self.axs.plot(self.pnt[self.cov.vertices, 0],
                      self.pnt[self.cov.vertices, 1], 'r--', lw=2)
        self.axs.plot(self.pnt[self.cov.vertices[0], 0],
                      self.pnt[self.cov.vertices[0], 1], 'ro')


if __name__ == '__main__':
    obj = ConvexArea(num=50)
    obj.SavePng()
