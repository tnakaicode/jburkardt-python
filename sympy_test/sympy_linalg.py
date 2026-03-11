#! /usr/bin/env python3
#
def sympy_linalg ( ):

#*****************************************************************************80
#
## sympy_linalg() uses sympy() to perform linear algebra.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  from sympy import det
  from sympy import Matrix
  from sympy import solve_linear_system
  from sympy import symbols

  print ( '' )
  print ( 'sympy_linalg():' )
  print ( '  Demonstrate sympy linear algebra operations.' )
  print ( '' )
#
#  Matrix multiplication.
#
  A = Matrix ( [ \
    [ 2,-1, 0, 0], \
    [-1, 2,-1, 0], \
    [ 0,-1, 2,-1], \
    [ 0, 0,-1, 2] ] )
  x = Matrix ( [ 1, 2, 3, 4 ] )
  b = A * x

  print ( '  A = ', A )
  print ( '  x = ', x )
  print ( '  b = A*x = ', b )
#
#  Solve linear system.
#  Awkward.  We have to define the augmented matrix A2=[A,b],
#  and define n scalar variables to hold the solution.
#
  x1, x2, x3, x4 = symbols ( 'x1 x2 x3 x4' )

  A2 = Matrix ( [ \
    [ 2, -1, 0, 0, b[0] ], \
    [ -1, 2, -1, 0, b[1] ], \
    [  0, -1, 2, -1, b[2] ], \
    [  0,  0, -1, 2, b[3] ] ] )

  solution = solve_linear_system ( A2, x1, x2, x3, x4 )
  print ( '  Solved A*x=b = ', solution )
#
#  Determinant.
#
  A_determinant = A.det()
  print ( '  det(A) = ', A_determinant )
#
#  Compute matrix inverse.
#
  A_inverse = A**(-1)
  print ( '  A inverse = ', A_inverse )
#
#  A * A_inverse?
#
  I = A * A_inverse
  print ( '  A * A_inverse = ', I )
#
#  Compute eigenvalues.
#
  A_eigen = A.eigenvals()
  print ( '  A eigenvalues : multiplicity = ', A_eigen )

  return

if ( __name__ == "__main__" ):
  sympy_linalg ( )

