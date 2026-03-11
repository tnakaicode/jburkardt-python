#! /usr/bin/env python3

def plasma_matrix ( n = 101 ):

#*****************************************************************************80
#
## plasma_matrix() computes jacobian and residual for a plasma problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2020
#
#  Author:
#
#    Original Python code by James Cheung.
#    This version by John Burkardt.
#
#  Input:
#
#    integer N: the number of nodes in the X and Y directions.
#
#  Output:
#
#    real sparse A(n*n,n*n): the Jacobian matrix.
#
#    real b(n*n,1): the residual vector.
#
#  Local:
#
#    real XLEFT, XRIGHT: the left and right endpoints of the X and Y intervals.
#
#    real H: the spacing between nodes.
#
#    real RHO(n,n): the density. 
#
#    integer NUMNODES: the number of nodes.
#
#    real X(n): the X coordinates of the grid.
#
#    real Y(n): the Y coordinates of the grid.
#
  from scipy.sparse import lil_matrix
  import numpy as np
  import scipy as sp

  xleft = -10.0
  xright = +10.0

  x = np.linspace ( xleft, xright, n )
  y = np.linspace ( xleft, xright, n )
  h = ( xright - xleft ) / float ( n - 1 )
  hsq = h**2
#
#  Set up the plasma density as a step function, which is 1 
#  in a central square, and 0.25 outside of the square.
#
  numnodes = n * n
  rho = np.zeros ( numnodes, dtype = float )
  phi = np.zeros ( numnodes, dtype = float )

  nr = 0.25
  k = 0

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( np.abs ( x[i] ) < 5.0 and np.abs ( y[j] ) < 5.0 ):
        rho[k] = 1.0
      else:
        rho[k] = nr

      phi[k] = np.log ( rho[k] )

      k = k + 1
#
#  Allocate A initially as a row-based "list of lists" sparse matrix.
#
  A = lil_matrix ( ( numnodes, numnodes ) )
  b = np.zeros ( numnodes )
#
#  Bottom
#
  b[0] = \
    - 4.0 * phi[0] \
    + 2.0 * phi[1] \
    + 2.0 * phi[n] \
    - hsq * np.exp ( phi[0] ) \
    + hsq * rho[0]

  A[0,0] = - 4.0 - hsq * np.exp ( phi[0] )
  A[0,1] = 2.0
  A[0,n] = 2.0

  for i in range ( 1, n - 1 ):

    b[i] = \
              phi[i-1] \
      - 4.0 * phi[i] \
      +       phi[i+1] \
      + 2.0 * phi[i+n] \
      - hsq * np.exp ( phi[i] ) \
      + hsq * rho[i]

    A[i,i-1] = 1.0
    A[i,i] = - 4.0 - hsq * np.exp ( phi[i] )
    A[i,i+1] = 1.0
    A[i,n+i] = 2.0

  b[n-1] = \
      2.0 * phi[n-2] \
    - 4.0 * phi[n-1] \
    + 2.0 * phi[2*n-1] \
    - hsq * np.exp ( phi[n-1] ) \
    + hsq * rho[n-1]

  A[n-1,n-2] =   2.0
  A[n-1,n-1] = - 4.0 - hsq * np.exp ( phi[n-1] )
  A[n-1,n+n-1] = 2.0
#
#  Middle
#
  for i in range ( 1, n - 1 ):

    z = i * n

    b[z] = \
              phi[z-n] \
      - 4.0 * phi[z] \
      + 2.0 * phi[z+1] \
      +       phi[z+n] \
      - hsq * np.exp ( phi[z] ) \
      + hsq * rho[z]

    A[z,z-n] = 1.0
    A[z,z] = - 4.0 - hsq * np.exp ( phi[z] )
    A[z,z+1] = 2.0
    A[z,z+n] = 1.0

    for j in range ( 1, n - 1 ):

      b[z+j] = \
                phi[z+j-1] \
        +       phi[z+j-n] \
        - 4.0 * phi[z+j] \
        +       phi[z+j+1] \
        +       phi[z+n+j] \
        - hsq * np.exp ( phi[z+j] ) \
        + hsq * rho[z+j]

      A[z+j,z-n+j] = 1.0
      A[z+j,z+j-1] = 1.0
      A[z+j,z+j] = - 4.0 - hsq * np.exp ( phi[z+j] )
      A[z+j,z+j+1] = 1.0
      A[z+j,z+n+j] = 1.0

    b[z+n-1] = \
        2.0 * phi[z+n-2] \
      +       phi[z-1] \
      - 4.0 * phi[z+n-1] \
      +       phi[z+2*n-1] \
      - hsq * np.exp ( phi[z+n-1] ) \
      + hsq * rho[z+n-1]

    A[z+n-1,z-1] = 1.0
    A[z+n-1,z+n-2] = 2.0
    A[z+n-1,z+n-1] = - 4.0 - hsq * np.exp ( phi[z+n-1] )
    A[z+n-1,z+2*n-1] = 1.0
#
#  Top
#
  z = ( n - 1 ) * n

  b[z] = \
      2.0 * phi[z-n] \
    - 4.0 * phi[z] \
    + 2.0 * phi[z+1] \
    - hsq * np.exp ( phi[z] ) \
    + hsq * rho[z]

  A[z,z-n] = 2.0
  A[z,z] = - 4.0 - hsq * np.exp ( phi[z] )
  A[z,z+1] = 2.0

  for i in range ( 1, n - 1 ):

    b[z+i] = \
              phi[z+i-1] \
      + 2.0 * phi[z+i-n] \
      - 4.0 * phi[z+i] \
      +       phi[z+i+1] \
      - hsq * np.exp ( phi[z+i] ) \
      + hsq * rho[z+i]

    A[z+i,z-n+i] = 2.0
    A[z+i,z+i-1] = 1.0
    A[z+i,z+i] = - 4.0 - hsq * np.exp ( phi[z+i] )
    A[z+i,z+i+1] = 1.0

  b[z+n-1] = \
      2.0 * phi[z+n-2] \
    + 2.0 * phi[z-1] \
    - 4.0 * phi[z+n-1] \
    - hsq * np.exp ( phi[z+n-1] ) \
    + hsq * rho[z+n-1]

  A[z+n-1,z-1] = 2.0
  A[z+n-1,z+n-2] = 2.0
  A[z+n-1,z+n-2] = - 4.0 - hsq * np.exp ( phi[z+n-1] )
#
#  In order to use the scipy sparse solver, convert the LIL matrix to CSR form.
#
  A = A.tocsr ( )

  return A, b
 
def plasma_matrix_test01 ( n ):

#*****************************************************************************80
#
## plasma_matrix_test01() creates a plasma matrix and solves a linear system.
#
#  Discussion:
#
#    The use specifies a linear grid dimension of N, corresponding to N^2
#    grid points and N^4 matrix entries.  However, the actual matrix is
#    sparse, to only about 5*N^2 entries are nonzero.  
#
#    Sparse storage is used for the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the linear order of the spatial grid.
#
  from scipy.sparse.linalg import spsolve
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy as sp

  print ( '' )
  print ( 'plasma_matrix_test01():' )
  print ( '  Linear order of spatial grid = ', n )
  print ( '  Number of grid points is ', n * n )
  print ( '  Approximate number of nonzero matrix entries is ', 5 * n * n )
  print ( '  Full storage matrix would require', n**4, 'entries.' )

  A, b = plasma_matrix ( n )

  b_norm = np.linalg.norm ( b )
  print ( '' )
  print ( '  Norm of right hand side b is', b_norm )

  plt.spy ( A )
  filename =  'plasma_' + str ( n ) + '_sparsity.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Solve the system A * x = - b.
#
  x = spsolve ( A, -b )
  x_norm = np.linalg.norm ( x )
  print ( '' )
  print ( '  Norm of solution is', x_norm )

  return

def plasma_matrix_test02 ( n ):

#*****************************************************************************80
#
## plasma_matrix_test02() solves a plasma matrix linear system using bicg.
#
#  Discussion:
#
#    The use specifies a linear grid dimension of N, corresponding to N^2
#    grid points and N^4 matrix entries.  However, the actual matrix is
#    sparse, to only about 5*N^2 entries are nonzero.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the linear order of the spatial grid.
#
  from scipy.sparse.linalg import spilu
  import numpy as np
  import scipy as sp

  print ( '' )
  print ( 'plasma_matrix_test02():' )
  print ( '  Linear order of spatial grid =', n )
  print ( '  Number of grid points is', n * n )
  print ( '  Approximate number of nonzero matrix entries is ', 5 * n * n )
  print ( '  Full storage matrix would require', n**4, 'entries.' )

  A, b = plasma_matrix ( n )

  b_norm = np.linalg.norm ( b )
  print ( '' )
  print ( '  Norm of right hand side b is', b_norm )
#
#  Use backslash to solve the system A * x = b.
#
  x1 = sp.sparse.linalg.spsolve ( A, b )
  x1_norm = np.linalg.norm ( x1 )
  print ( '' )
  print ( '  Norm of backslash solution x is', x1_norm )
#
#  Use bicg to solve the system A * x = b.
#
  x2, info = sp.sparse.linalg.bicg ( A, b )
  x2_norm = np.linalg.norm ( x2 )
  print ( '' )
  print ( '  Norm of bicg solution x is', x2_norm )
#
#  Use ILU approximate inverse to solve the system A * x = b.
#
  A = A.tocsc ( )
  Ailu = spilu ( A )
  x3 = Ailu.solve ( b )
  x3_norm = np.linalg.norm ( x3 )
  print ( '' )
  print ( '  Norm of ilu solution x is', x3_norm )

  return

def plasma_matrix_test ( ):

#*****************************************************************************80
#
## plasma_matrix_test() tests plasma_matrix().
#
#  Discussion:
#
#    This program shows how a sparse matrix (and possibly a right
#    hand side vector) can be stored into a Harwell-Boeing file,
#    and later retrieved.
#
#    Harwell-Boeing files are useful as a means of storing sparse matrices,
#    especially when data is created with one program and needed by another.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'plasma_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test plasma_matrix()' )

  plasma_matrix_test01 ( 5 )
  plasma_matrix_test01 ( 101 )
  plasma_matrix_test02 ( 101 )
#
#  Terminate.
#
  print ( '' )
  print ( 'plasma_matrix_test():' )
  print ( '  Normal end of execution.' )

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
  plasma_matrix_test ( )
  timestamp ( )
