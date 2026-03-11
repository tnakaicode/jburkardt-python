#! /usr/bin/env python3
#
def linalg_test ( ):

#*****************************************************************************80
#
## linalg_test() tests some scipy() linear algebra functions
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'linalg_test():' )
  print ( '  Set up and solve a linear system A*x=b.' )

  n = 5
  A = np.random.randint ( low = 1, high = 9, size = [ n, n ] )
  A = A.reshape ( n, n )
#
#  Solve linear system.
#
  print ( '  Matrix A:' )
  print ( A )
  x = np.arange ( 1, n + 1 )
  b = np.dot ( A, x )
  print ( '  Right hand side b:' )
  print ( b )
  x2 = np.linalg.solve ( A, b )
  print ( '  Computed solution x:' )
  print ( x2 )
  e = np.linalg.norm ( np.dot ( A, x2 ) - b )
  print ( '  ||error|| =', e )

  return

if ( __name__ == "__main__" ):
  linalg_test ( )

