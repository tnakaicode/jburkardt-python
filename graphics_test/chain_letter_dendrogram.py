#! /usr/bin/env python3
#
def chain_letter_dendrogram ( ):

#*****************************************************************************80
#
## chain_letter_dendrogram makes a dendrogram from a distance matrix.
#
#  Discussion:
#
#    Students were given 11 chain letters.  Each student was asked to pick
#    a particular chain letter, and then estimate its "distance" from all
#    the chain letters, using a particular scoring system.  
#
#    The results are here assembled into a distance matrix, from which a
#    hierarchical clustering can be made and displayed.
#
#    The distances were based on comparing positions in thw chain letters where
#    a proper name occurred.
#
#    "New England"   0 if the same, 1 otherwise.
#    "R.A.F.Officer" 0 if the same, 1 otherwise.
#    "Gene Welch" 0 if the same, 1 if one name different, 2 if both different.
#    "Saul de Groda" 0 if the same, 1, 2 or 3 if 1, 2 or 3 names different or added.
#    "Constantine Dias" 0 if the same, 1 or 2 if 1 or 2 names different.
#    "Carlos Daddit" 0 if the same, 1 or 2 if 1 or 2 names different.
#    "Dalan Fairchild" 0 if the same, 1 or 2 if 1 or 2 names different.
#    "a young woman in California" 0 if both letters have or don't have this part, 
#      5 if one does and one doesn't.
#
#    The distance between the two chain letters is the sum of the 8 scores.
#
#    From the distance matrix, we can compute a dendrogram that suggests,
#    based on similarity, a sort of genealogy for the chain letters.
#
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2019
#
#  Author:
#
#    John Burkardt
#
  import csv
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  import scipy as sp
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from scipy import spatial
  from scipy import cluster

  print ( '' )
  print ( 'chain_letter_dendrogram:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Construct a dendrogram to analyze the relationship' )
  print ( '  among a set of 11 versions of a chain letter.' )
#
#  Read the distance matrix from a file.
#
  filename = 'chain_letter_data.txt'
  data = np.loadtxt ( filename )

  print ( '' )
  print ( '  Chain letter distance matrix read from "%s"' % ( filename ) )
#
#  Determine pairwise distances.
#
  dv = sp.spatial.distance.pdist ( data )
#
#  Perform hierarchical clustering.
#
  dl = sp.cluster.hierarchy.linkage ( dv, method = 'single' )
#
#  Display the clustering as a dendrogram.
#
  plt.figure ( )
  plt.title ( 'Dendrogram for 11 chain letters A=1 through K=11', fontsize = 16 )

  sp.cluster.hierarchy.dendrogram ( dl, \
    labels = ( 'A','B','C','D','E','F','G','H','I','J','K') )
  filename = 'chain_letter_dendrogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'chain_letter_dendrogram:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chain_letter_dendrogram ( )
  timestamp ( )
 
