#! /usr/bin/env python
#
def i4mat_rref_solve_binary_nz ( m, n, nz, a, b ):

#*****************************************************************************80
#
## I4MAT_RREF_SOLVE_BINARY_NZ seeks binary solutions of an IRREF system.
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
#    Moreover, we know that exactly NZ of the variables are 1.
#
#    The solution procedure involves two steps:
#    * assign each free variable a value of 0 or 1, but never assign more
#      that NZ nonzeroes
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer NZ, the number of nonzeros required in any binary
#    solution.
#
#    Input, real A(M,N), the IRREF matrix to be analyzed. 
#
#    Input, real B(M), the right hand side.
#
#    Output, integer X_NUM, the number of binary solutions discovered.
#    Note that there may be no binary solutions at all.
#
#    Output, real X(N,X_NUM), the solutions.
#
  import numpy as np
  from i4mat_rref_system import i4mat_rref_system
  from i4mat_u_solve import i4mat_u_solve
  from i4vec_binary_next import i4vec_binary_next
  from i4vec_is_binary import i4vec_is_binary
  from ksub_next4 import ksub_next4
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
#  There are FREEDOM_NUM degrees of freedom, each of which could be set to 1.
#  There must be NZ variables set to 1.
#  Consider setting NZ2 degrees of freedom to 1, where NZ2 is between 0
#  and the minimum of NZ and FREEDOM_NUM.
#
#  Choose every possible selection of NZ2 degrees of freedom, and solve
#  the system.
#
#  If the resulting solution is binary, then add it to the list.
#
  b_num = 0

  for nz2 in range ( 0, min ( nz, freedom_num ) + 1 ):

    done = True
    free_sub = []

    while ( True ):

      free_sub, done = ksub_next4 ( freedom_num, nz2, free_sub, done )

      if ( done ):
        break

      b3 = b2.copy ( )
#
#  Moron error:
#  only integer scalar arrays can be converted to a scalar index
#     b2[freedom[free_sub[0:nz2]]] = 1
#
      for k in range ( 0, nz2 ):
        j = free_sub[k] - 1
        i = freedom[j]
        b3[i] = 1

      b_num = b_num + 1

      y = i4mat_u_solve ( n, a2, b3 )

      if ( i4vec_is_binary ( n, y ) ):
        y = np.reshape ( y, ( n, 1 ) )
        x = np.hstack ( ( x, y ) )
        x_num = x_num + 1

  return x_num, x

def i4mat_rref_solve_binary_nz_test ( ):

#*****************************************************************************80
#
## I4MAT_RREF_SOLVE_BINARY_NZ_TEST tests I4MAT_RREF_SOLVE_BINARY_NZ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2018
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
  print ( 'I4MAT_RREF_SOLVE_BINARY_NZ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_RREF_SOLVE_BINARY_NZ seeks binary solutions of' )
  print ( '  an Integer Row-Reduced Echelon Form (IRREF) system A*x=b' )
  print ( '  which have exactly NZ nonzeros.' )

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

  nz = 4
  print ( '' )
  print ( '  Only consider binary solutions with exactly %d nonzeros.' % ( nz ) )

  x_num, x = i4mat_rref_solve_binary_nz ( m, n, nz, a, b )

  i4mat_print ( n, x_num, x, '  Binary solution vectors x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_RREF_SOLVE_BINARY_NZ_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_rref_solve_binary_nz_test ( )
  timestamp ( )

