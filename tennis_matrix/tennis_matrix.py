#! /usr/bin/env python3
#
def tennis_labels ( ):

#*****************************************************************************80
#
## tennis_labels() returns labels for the tennis game states.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    cell array labels{17}: labels for the tennis game states.
#    Most of these are pairs of server/opponent scores.
#
  labels = [ \
    '0-0', \
    '15-0', \
    '0-15', \
    '30-0', \
    '15-15', \
    '0-30', \
    '40:0', \
    '30:15', \
    '15:30', \
    '0:40', \
    'Win', \
    '40:15', \
    'Deuce', \
    '15:40', \
    'Loss', \
    'Ahead 1', \
    'Behind 1' ]

  return labels

def tennis_matrix ( p ):

#*****************************************************************************80
#
## tennis_matrix() returns a tennis transition matrix.
#
#  Discussion:
#
#    The peculiar tennis scoring system goes 0, 15, 30, 40, Win.
#
#    However, to win, a player must be ahead by two points.  
#
#    There are three "peculiar" states: Deuce, Ahead 1, Behind 1,
#    which arise when one player is near to winning.  
#    'Ahead 1' means the player is 1 point away from winning.
#    'Behind 1' means the player is 1 point away from losing.
#    'Deuce' means either player will win with two unopposed points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real p: the probability that the server will make the next point.
#
#  Output:
#
#    real A[17,17): the transition matrix.
#
  import numpy as np

  q = 1.0 - p

  A = np.zeros ( [ 17, 17 ] )
#
#  1: 0-0
#
  A[0,1] = p
  A[0,3] = q
#
#  2: 15-0
#  3: 0-15
#
  A[1,3] = p
  A[1,4] = q
  A[2,4] = p
  A[2,5] = q
#
#  4: 30-0
#  5: 15-15
#  6: 0-30
#
  A[3,6] = p
  A[3,7] = q
  A[4,7] = p
  A[4,8] = q
  A[5,8] = p
  A[5,9] = q
#
#  7: 40:0
#  8: 30:15
#  9: 15:30
#  10: 0:40
#
  A[6,10] = p
  A[6,11] = q
  A[7,11] = p
  A[7,12] = q
  A[8,12] = p
  A[8,13] = q
  A[9,13] = p
  A[9,14] = q
#
#  11: Win
#  12: 40:15
#  13: Deuce
#  14: 15:40
#  15: Loss
#
  A[10,10] = 1.0
  A[11,10] = p
  A[11,15] = q
  A[12,15] = p
  A[12,16] = q
  A[13,10] = p
  A[13,16] = q
  A[14,14] = 1.0
#
#  16: Ahead 1
#  17: Behind 1
#
  A[15,10] = p
  A[15,13] = q
  A[16,13] = p
  A[16,14] = q

  return A

def tennis_matrix_test ( ):

#*****************************************************************************80
#
## tennis_matrix_test() tests tennis_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tennis_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tennis_matrix().' )

  tennis_matrix_spy_test ( )
  tennis_matrix_eigen_test ( )
  tennis_labels_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'tennis_matrix_test()' )
  print ( '  Normal end of execution.' )

  return

def tennis_labels_test ( ):

#*****************************************************************************80
#
## tennis_labels_test() tests tennis_labels().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tennis_labels_test():' )
  print ( '  tennis_labels() provides labels for the tennis states.' )
  print ( '' )

  labels = tennis_labels ( )
  for i in range ( 0, len ( labels ) ):
    print ( '  %2d: %s' % ( i, labels[i] ) )

  return

def tennis_matrix_eigen_test ( ):

#*****************************************************************************80
#
## tennis_matrix_eigen_test() does an eigenanalysis of a tennis matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  p = 0.60

  print ( '' )
  print ( 'tennis_matrix_eigen_test():' )
  print ( '  tennis_matrix() is evaluated with probability' )
  print ( '  of server winning a single serve p = ', p )
  print ( '  eigen() computes eigenvalues and eigenvectors.' )

  A = tennis_matrix ( p )
  w, V = np.linalg.eig ( A )
  
  print ( '' )
  print ( '  Eigenvalues:' )
  print ( w )

  print ( '' )
  print ( '  Eigenvectors:' )
  print ( V )

  return

def tennis_matrix_spy_test ( ):

#*****************************************************************************80
#
## tennis_matrix_spy_test() uses spy() to display a tennis matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'tennis_matrix_spy_test():' )
  print ( '  tennis_matrix() is evaluated for p=0.5.' )
  print ( '  spy() displays the nonzero elements of the resulting matrix.' )

  p = 0.5
  A = tennis_matrix ( p )
  plt.spy ( A )
  filename = 'tennis_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  tennis_matrix_test ( )
  timestamp ( )



