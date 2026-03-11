#! /usr/bin/env python3
#
def laplace_matrix ( rng ):

#*****************************************************************************80
#
## laplace_matrix() analyzes a matrix sampled from the Laplace distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  N = 5000

  print ( '' )
  print ( 'laplace_matrix()' )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from Laplace distribution.' )

  A = rng.laplace ( 0, np.sqrt(0.5), (N, N) )
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 

  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Laplace matrix' )
  filename = 'laplace_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

  return

def normal_matrix ( rng ):

#*****************************************************************************80
#
## normal_matrix() analyzes a matrix sampled from the normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  N = 5000

  print ( '' )
  print ( 'normal_matrix():' )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from normal distribution.' )

  A = rng.standard_normal ( size = (N, N) )    
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 

  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Normal matrix' )
  filename = 'normal_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

  return

def random_matrix_eigenvalues_test ( ):

#*****************************************************************************80
#
## random_matrix_eigenvalues_test() tests random_matrix_eigenvalues().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 January 2024
#
#  Author:
#
#    John Burkardt.
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'random_matrix_eigenvalues_test:' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test random_matrix_eigenvalues()' )

  rng = default_rng ( )

  laplace_matrix ( rng )
  normal_matrix ( rng )
  student_matrix ( rng )
  uniform_matrix ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_matrix_eigenvalues_test():' )
  print ( '  Normal end of execution.' )
  return

def student_matrix ( rng ):

#*****************************************************************************80
#
## student_matrix() analyzes a matrix sampled from the Student T distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original code by John D Cook.
#    Modifications by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  N = 5000

  print ( '' )
  print ( 'student_matrix():' )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from the Student t distribution.' )

  df = 1.8
  A = rng.standard_t ( df, size = ( N, N ) )
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 

  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Student t matrix' )
  filename = 'student_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def uniform_matrix ( rng ):

#*****************************************************************************80
#
## uniform_matrix() analyzes a matrix sampled from the uniform distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  N = 5000

  print ( '' )
  print ( 'uniform_matrix():' )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from uniform distribution.' )

  A = 2.0 * rng.random ( size = [ N, N ] ) - 1.0
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 
  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Uniform matrix' )
  filename = 'uniform_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  random_matrix_eigenvalues_test ( )
  timestamp ( )

