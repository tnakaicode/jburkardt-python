#! /usr/bin/env python3
#
def california_migration_test ( ):

#*****************************************************************************80
#
## california_migration_test() tests california_migration().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'california_migration_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Suppose that every year, 30% of California moves out' )
  print ( '  and 10% of the US moves into California.' )
  print ( '  Suppose in 1960 California had 16,000,000 residents,' )
  print ( '  and the rest of the US had 164,000,000 residents.' )
  print ( '  Predict the California population for the next 20 years.' )

  california_migration_scalar_test ( )
  california_migration_matrix_test ( )
  california_migration_matrix_backwards ( )
  california_migration_matrix_eigenvalues ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'california_migration_test():' )
  print ( '  Normal end of execution.' )

  return

def california_migration_scalar_test ( ):

#*****************************************************************************80
#
## california_migration_scalar_test() tests california_migration_scalar().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'california_migration_scalar_test():' )
  print ( '  Test california_migration_scalar().' )

  print ( '' )
  print ( '  Year     CA Pop     US pop      Total' )
  print ( '' )

  m = 21
  ca = np.zeros ( m )
  us = np.zeros ( m )

  year = np.linspace ( 1960, 1960 + m - 1, m )

  for i in range ( 0, 21 ):

    if ( i == 0 ):
      ca[i] =  16000000
      us[i] = 164000000
    else:
      ca[i], us[i] = california_migration_scalar ( ca[i-1], us[i-1] )

    print ( '  %4d  %9.0f  %9.0f  %9.0f' \
      % ( year[i], ca[i], us[i], ca[i] + us[i] ) )

  plt.clf ( )
  plt.plot ( year, ca, linewidth = 3 )
  plt.plot ( year, us, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Year -->' )
  plt.ylabel ( '<-- Population -->' )
  plt.title ( 'California population scalar' )
  plt.legend ( [ 'CA', 'US' ] )
  filename = 'california_migration_scalar.png'
  plt.savefig ( filename )     
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def california_migration_scalar ( ca, us ):

#*****************************************************************************80
#
## california_migration_scalar() approximates next year's California population.
#
#  Discussion:
#
#    For a while in the 1960's, the following statement was approximately true:
#
#   "Every year, 30% of the population of California leaves the state, and
#    every year, 10% of the population of the other states moves to California."
#
#    1) The statement sounds nonsensical.  Can we write down some equations
#       that give us numbers we can think about?
#
#    2) If 30% move out, and 10% move it, does this mean California is
#       gradually going to have no population at all?
#
#    3) If this behavior lasts long enough, does the population curve
#       of California look chaotic, go towards infinity, become negative, 
#       or oscillatory, or does it settle down?
#
#    We can make some simplifying assumptions:
#
#    * Assume that the 30% and 10% values are exact and don't change.
#
#    * The population estimates will be real numbers with fractional parts,
#      but we'll just accept figures like a population of 10,000.73
#
#    * Find the populations of California and the US in 1960, and assume
#      that the total population never changes after that, but just
#      moves back and forth.
#
#    Our goal will be simply to compute the populations of California and
#    the US (minus California), for each year, from 1960 onwards, and to
#    plot the California population, and to compute it long enough that
#    we feel we understand the pattern, if any.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CA, US: the populations of California and the rest of the US
#    at the end of this year.
#
#  Output:
#
#    real CA_NEXT, US_NEXT: the populations next year.
#
  ca_next = 0.70 * ca + 0.10 * us
  us_next = 0.30 * ca + 0.90 * us

  return ca_next, us_next

def california_migration_matrix_test ( ):

#*****************************************************************************80
#
## california_migration_matrix_test() tests california_migration_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'california_migration_matrix_test():' )
  print ( '  Test california_migration_matrix().' )

  print ( '' )
  print ( '  Year     CA Pop     US pop      Total' )
  print ( '' )

  m = 21
  pop = np.zeros ( [ m, 2 ] )
  year = np.linspace ( 1960, 1960 + m - 1, m )

  for i in range ( 0, 21 ):

    if ( i == 0 ):
      pop[0,0] =  16000000
      pop[0,1] = 164000000
    else:
      pop[i,0:2] = california_migration_matrix ( pop[i-1,0:2] )

    print ( '  %4d  %9.0f  %9.0f  %9.0f' \
      % ( year[i], pop[i,0], pop[i,1], pop[i,0] + pop[i,1] ) )

  plt.clf ( )
  plt.plot ( year, pop[:,0], linewidth = 3 )
  plt.plot ( year, pop[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Year -->' )
  plt.ylabel ( '<-- Population -->' )
  plt.title ( 'California population matrix' )
  plt.legend ( [ 'CA', 'US' ] )
  filename = 'california_migration_matrix.png'
  plt.savefig ( filename )     
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def california_migration_matrix ( pop ):

#*****************************************************************************80
#
## california_migration_matrix() approximates next year's California population.
#
#  Discussion:
#
#    This function reformulates the scalar code as a matrix operation
#    pop = A * pop.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real pop[2]: the populations of California and the rest of the US
#    at the end of this year.
#
#  Output:
#
#    real pop[2]: the populations next year.
#
  import numpy as np

  A = np.array ( [ \
    [ 0.70, 0.10 ], \
    [ 0.30, 0.90 ] ] )

  pop = np.matmul ( A, pop )

  return pop

def california_migration_matrix_backwards ( ):

#*****************************************************************************80
#
## california_migration_matrix_backwards() goes "backward" in time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'california_migration_matrix_backwards():' )
  print ( '  Go "backwards" in time using np.linalg.solve()' )

  A = np.array ( [ \
    [ 0.70, 0.10 ], \
    [ 0.30, 0.90 ] ] )

  pop = np.zeros ( [ 2, 2 ] )

  i = 1
  pop[i,:] = np.array ( [ 27600000, 152400000 ] )
  print ( '' )
  print ( '  Population data for 1961:' )
  print ( '  %4d  %9.0f  %9.0f  %9.0f' \
    % ( 1961, pop[i,0], pop[i,1], pop[i,0] + pop[i,1] ) )
#
#  np.linalg.solve solves A*x=b.
#  Use this to compute previous year 1960 from current year 1961.
#
  pop[i-1,:] = np.linalg.solve ( A, pop[i,:] )

  print ( '' )
  print ( '  Population data for 1960:' )
  print ( '  %4d  %9.0f  %9.0f  %9.0f' \
    % ( 1960, pop[i-1,0], pop[i-1,1], pop[i-1,0] + pop[i-1,1] ) )

  return

def california_migration_matrix_eigenvalues ( ):

#*****************************************************************************80
#
## california_migration_matrix_eigenvalues() determines the eigen information.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real L[2]: the eigenvalues.
#
#    real V[2,2]: the eigenvectors.
#
  import numpy as np

  print ( '' )
  print ( 'california_migration_matrix_eigenvalues():' )
  print ( '  Compute eigen information for matrix A' )

  A = np.array ( [ \
    [ 0.70, 0.10 ], \
    [ 0.30, 0.90 ] ] )

  L, V = np.linalg.eig ( A )

  print ( '' )
  print ( '  eigenvalues L: ')
  print ( L )

  print ( '' )
  print ( '  eigenvectors V:')
  print ( V )

  AV = np.matmul ( A, V )
  print ( '' )
  print ( '  A*V:')
  print ( AV )

  VL = np.matmul ( V, np.diag ( L ) )
  print ( '' )
  print ( '  V*np.diag(L):' )
  print ( VL )

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
  california_migration_test ( )
  timestamp ( )

