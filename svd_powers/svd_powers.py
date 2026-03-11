#! /usr/bin/env python3
#
def powers_data ( xmin, xmax, xnum, pnum ):

#*****************************************************************************80
#
## powers_data() generates A[I,J] = X(I)^J.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XMIN, XMAX, the range of the X data.
#
#    integer XNUM, the number of X values to generate.
#
#    integer PNUM, the number of powers to consider, between 0 and PNUM-1.
#
#  Output:
#
#    real A(XNUM,PNUM):  A(I,J) = X(I)^J.
#
  import numpy as np

  x = np.linspace ( xmin, xmax, xnum )

  A = np.zeros ( [ xnum, pnum ] )

  for j in range ( 0, pnum ):
    A[:,j] = x ** j

  return A

def powers_data_test ( ):

#*****************************************************************************80
#
## powers_data_test() tests powers_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'powers_data_test():' )
  print ( '  powers_data() generates a dataset A[i,j] = x[i]^j.' )

  xmin = -1.0
  xmax = +1.0
  pnum = 4
  xnum = 11

  A = powers_data ( xmin, xmax, xnum, pnum )

  print ( '' )
  print ( '  powers_data() generated this data' )
  print ( '  for xnum = ' + str ( xnum ) + ' pnum = ' + str ( pnum ) )
  print ( '' )
  print ( A )

  return

def svd_powers_test ( ):

#*****************************************************************************80
#
## svd_powers_test() tests svd_powers().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'svd_powers_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test svd_powers().' )

  powers_data_test ( )
  svd_vectors_test ( )
  svd_project_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_powers_test():' )
  print ( '  Normal end of execution.' )

  return

def svd_project_test ( ):

#*****************************************************************************80
#
## svd_project_test() demonstrates projection using SVD vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'svd_project_test():' )
  print ( '  Compute singular vectors for x(i)^j.' )
  print ( '  Then take an arbitrary vector.' )
  print ( '  Approximate it with 0, 1, 2, ... singular vectors.' )
#
#  Get the data array.
#
  xmin = -1.0
  xmax = +1.0
  xnum = 51
  pnum = 8

  x = np.linspace ( xmin, xmax, xnum )
  A = powers_data ( xmin, xmax, xnum, pnum )
#
#  Compute some SVD vectors.
#
  svd_vec, svd_val, avg = svd_vectors ( A, pnum )

  avg = avg / np.linalg.norm ( avg )
#
#  Get a data vector SE.
#
  se = np.sin ( x ) + 1.0 / ( x**2 + 0.25 )
#
#  Break the data vector into:
#  SE0: constant + multiple of average
#  SE1: remainder.
#
  beta = ( se[xnum-1] - se[0] ) / ( avg[xnum-1] - avg[0] )
  alpha = se[0] - beta * avg[0]
  se0 = alpha + beta * avg
  se1 = se - se0
#
#  Construct approximation SA = SE0 + (SE1,V0) * V0 + (SE1,V1) * V1 + ...
#
  for j in range ( 0, pnum + 1 ):

    if ( j == 0 ):
      sa = se0.copy( )
    else:
      c = np.dot ( se1, svd_vec[:,j-1] )
      sa = sa + c * svd_vec[:,j-1]

    plt.clf ( )
    plt.plot ( x, se, 'b-', linewidth = 3 )
    plt.plot ( x, sa, 'r-', linewidth = 3 )   
    plt.grid ( True )
    label = 'SVD projection using ' + str ( j ) + ' vectors.'
    plt.title ( label )
    filename = 'svd_project_test_' + str ( j ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.show ( block = False )
    plt.close ( )

  return

def svd_vectors ( A, numvecs ):

#*****************************************************************************80
#
## svd_vectors() gets some SVD vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(XNUM,PNUM), an array of data.
#
#    integer NUMVECS, the number of vectors requested.
#    NUMVECS <= N.
#
#  Output:
#
#    real U(XNUM,NUMVECS), the requested vectors.
#
#    real VALUES(PNUM), the singular values.
#
#    real AVG(XNUM), the average vector for each row.
#
  import numpy as np

  xnum, pnum = A.shape
#
#  Compute the average of each row.
#
  avg = np.mean ( A, axis = 1 )
#
#  Subtract the row average from each column of A.
#
  for j in range ( 0, pnum ):
    A[:,j] = A[:,j] - avg
#
#  Compute the economic SVD:
#
  U, svec, V = np.linalg.svd ( A, full_matrices = False )
#
#  Cut U down to length NUMVECS.
#
  U = U[:,0:numvecs]
#
#  Return singular values as a vector.
#
  return U, svec, avg

def svd_vectors_test ( ):

#*****************************************************************************80
#
## svd_vectors_test() tests svd_vectors().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 December 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'svd_vectors_test():' )
  print ( '  svd_vectors() computes SVD vectors.' )
  print ( '  Data is a set of power vectors.' )
  print ( '  Do SVD analysis.' )
  print ( '  Display the SVD vectors.' )
#
#  Get the data array.
#
  xmin = -1.0
  xmax = +1.0
  xnum = 51
  pnum = 8

  x = np.linspace ( xmin, xmax, xnum )
  A = powers_data ( xmin, xmax, xnum, pnum )
#
#  Compute N SVD vectors.
#
  svd_vec, svd_val, avg = svd_vectors ( A, pnum )
#
#  Display the average and the SVD vectors.
#
  for j in range ( 0, pnum ):
    plt.clf ( )
    if ( j == 0 ):
      plt.plot ( x, avg, linewidth = 3 )
      label = 'SVD average'
    else:
      plt.plot ( x, svd_vec[:,j], linewidth = 3 )
      label = 'SVD vector ' + str ( j ) + ' SVD value = ' + str ( svd_val[j] )
    plt.title ( label )
    plt.ylim ( np.array ( [ -1.0, +1.0 ] ) )
    plt.grid ( True )
    filename = 'svd_vectors_' + str ( j ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.show ( block = False )
    plt.close ( )
#
#  Display the singular values.
#
  plt.clf ( )
  plt.plot ( svd_val, 'ob-', linewidth = 3 )
  plt.title ( 'Singular values' )
  plt.grid ( True )
  filename = 'svd_values.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

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
  svd_powers_test ( )
  timestamp ( )

