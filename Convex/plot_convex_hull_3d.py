import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import sys
import os
import time
from scipy.spatial import ConvexHull

sys.path.append(os.path.join('../'))
from base import plot3d

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


class ConvexArea3D (plot3d):

    def __init__(self, num=30, idx=2):
        plot3d.__init__(self)
        self.pnt = np.random.rand(num, 3)
        self.cov = ConvexHull(self.pnt)
        self.axs.plot(self.pnt[:, 0], self.pnt[:, 1], self.pnt[:, 2], 'o')

        print(self.cov)
        for idx in self.cov.simplices:
            x = self.pnt[idx, 0]
            y = self.pnt[idx, 1]
            z = self.pnt[idx, 2]
            print(idx, x, y, z)
            self.axs.plot_trisurf(x, y, z, linewidth=0.2, alpha=0.3)

        print(self.cov.vertices)

        self.axs.plot(self.pnt[self.cov.vertices, 0],
                      self.pnt[self.cov.vertices, 1], 'r--', lw=2)


if __name__ == '__main__':
    obj = ConvexArea3D(num=30)
    obj.SavePng()
