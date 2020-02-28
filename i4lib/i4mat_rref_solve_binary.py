#! /usr/bin/env python
#
def i4mat_rref_solve_binary ( m, n, a, b ):

#*****************************************************************************80
#
## I4MAT_RREF_SOLVE_BINARY seeks binary solutions of an IRREF system.
#
#  Discussion:
#
#    An MxN linear system A*x = b is considered.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to integer row-reduced echelon form (IRREF).
#
#    In order to solve a particular combinatorial problem, only binary
#    solutions x are of interest that is, each entry of x is either 0 or 1.
#
#    The solution procedure involves two steps:
#    * assign each free variable a value of 0 or 1
#    * solve for the dependent variables.
#
#    We consider every possible assignment of free variables, and we save
#    the solutions in which all the variables take on only 0 or 1 values.
#    
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of
#    the RREF matrix A.
#
#    Input, real A(M,N), the RREF matrix to be analyzed. 
#
#    Input, real B(M), the RREF right hand side.
#
#    Output, integer X_NUM, the number of binary solutions.
#    Note that there may be no binary solutions at all.
#
#    Output, real X(N,X_NUM), the solutions.
#
  import numpy as np
  from i4mat_rref_system import i4mat_rref_system
  from i4mat_u_solve import i4mat_u_solve
  from i4vec_binary_next import i4vec_binary_next
  from i4vec_is_binary import i4vec_is_binary
#
#  Augment the original linear system to the NxN system A2 x = B2.
#
  a2, b2, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a, b )
#
#  Initialize the list of solutions.
#
  x_num = 0
  x = np.zeros ( [ n, x_num ] )
#
#  If FREEDOM_NUM < 0, then the system is overdetermined and cannot be solved.
#
  if ( freedom_num < 0 ):
    return x_num, x
#
#  The indeterminate variables have a simple equation 
#    x(i) = b(i) = 0 or 1
#  Set up and solve every variation of this system.
#  If a solution is binary, accept it.
#
  binary = np.zeros ( freedom_num )

  while ( True ):

    b3 = b2.copy ( )
    for k in range ( 0, freedom_num ):
      i = freedom[k]
      b3[i] = binary[k]

    y = i4mat_u_solve ( n, a2, b3 )

    if ( i4vec_is_binary ( n, y ) ):
      y = np.reshape ( y, ( n, 1 ) )
      x = np.hstack ( ( x, y ) )
      x_num = x_num + 1

    binary = i4vec_binary_next ( freedom_num, binary )

    if ( np.sum ( binary ) == 0 ):
      break

  return x_num, x

def i4mat_rref_solve_binary_test ( ):

#*****************************************************************************80
#
## I4MAT_RREF_SOLVE_BINARY_TEST tests I4MAT_RREF_SOLVE_BINARY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'I4MAT_RREF_SOLVE_BINARY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_RREF_SOLVE_BINARY seeks binary solutions of' )
  print ( '  an Integer Row-Reduced Echelon Form (IRREF) system A*x=b' )
  print ( '  when A and b contain integer values.' )

  m = 9
  n = 10

  a = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 1, 0,-1, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 1, 0, 0, 0, 1, 0,-1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 1, 1 ], \
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ], \
    [ 0, 0, 0, 0, 0, 1,-1, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 1, 0,-1 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ] )

  i4mat_print ( m, n, a, '  The IRREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  i4vec_print ( m, b, '  The right hand side b:' )

  x_num, x = i4mat_rref_solve_binary ( m, n, a, b )

  i4mat_print ( n, x_num, x, '  Binary solution vectors x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_RREF_SOLVE_BINARY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_rref_solve_binary_test ( )
  timestamp ( )


