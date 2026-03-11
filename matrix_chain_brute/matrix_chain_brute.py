#! /usr/bin/env python3
#
def matrix_chain_brute_test ( ):

#*****************************************************************************80
#
## matrix_chain_brute_test() tests matrix_chain_brute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2024
#
#  Author:
#
#    John Burkardt
#
  from math import factorial
  import numpy as np
  import platform

  print ( '' )
  print ( 'matrix_chain_brute_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test matrix_chain_brute().' )

  for test in range ( 1, 11 ):

    if ( test == 1 ):
      dims = np.array ( [ 40, 20, 30, 10, 30 ], dtype = int )
    elif ( test == 2 ):
      dims = np.array ( [ 1, 2, 3, 4, 3 ], dtype = int )
    elif ( test == 3 ):
      dims = np.array ( [ 10, 20, 30 ], dtype = int )
    elif ( test == 4 ):
      dims = np.array ( [ 10, 30, 5, 60 ], dtype = int )
    elif ( test == 5 ):
      dims = np.array ( [ 10, 20 ], dtype = int )
    elif ( test == 6 ):
      dims = np.array ( [ 40, 20, 0, 10, 30 ], dtype = int )
    elif ( test == 7 ):
      dims = np.array ( [ 1, 100, 1, 100, 1 ], dtype = int )
    elif ( test == 8 ):
      dims = np.array ( [ 100, 50, 1, 50, 100 ], dtype = int )
    elif ( test == 9 ):
      dims = np.array ( [ 1, 50, 100, 50, 1 ], dtype = int )
    elif ( test == 10 ):
      dims = np.array ( [ 4, 10, 3, 12, 20, 7 ], dtype = int )

    n_dims = len ( dims )
    n_mats = n_dims - 1
    n_mults = n_mats - 1

    print ( '' )
    print ( '  Test #', test )
    print ( '  Number of matrix dimensions =', n_dims )
    print ( '  Number of matrices          =', n_mats )
    print ( '  Number of multiplications   =', n_mults )
    print ( '  Matrix dimensions' )
    for i in range ( 0, n_dims ):
      print ( '  ', dims[i], end = '' )
    print ( '' )
    parens = catalan_number ( n_mults )
    print ( '  Number of possible parenthesizations is', parens )
    perms = factorial ( n_mults )
    print ( '  Number of possible permutations is', perms )
    cost, p = matrix_chain_brute ( dims )
    print ( '  Minimal cost is', cost )
    print ( '  Ordering: ', end = '' )
    for i in range ( 0, n_mults ):
      print ( '  ', p[i], end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'matrix_chain_brute_test():' )
  print ( '  Normal end of execution.' )

  return

def catalan_number ( n ):

#*****************************************************************************80
#
## catalan_number() computes the N-th Catalan number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the Catalan number.
#
#  Output:
#
#    integer C: the value of the Catalan number.
#
  import numpy as np

  if ( n < 0 ):
    c = 0
    return c
 
  c = 1
#
#  The extra parentheses ensure that the integer division is
#  done AFTER the integer multiplication.
#
  for i in range ( 1, n + 1 ):
    c = ( c * 2 * ( 2 * i - 1 ) ) // ( i + 1 )

  return c

def matrix_chain_brute ( dims ):

#*****************************************************************************80
#
## matrix_chain_brute() finds the lowest cost to form a multiple matrix product.
#
#  Discussion:
#
#    This code represents a brute force approach.
#
#    An "efficient" brute force approach would only go through every
#    possible parenthesization of the multiplication, and a cost of
#    catalan(n_mats-1).  But it's not clear to me how to generate a sequence
#    of parentheses and properly interpret them as a multiplication ordering.
#
#    Instead, we rely on the fact that, to multiply N matrices, there are
#    N-1 multiplications to carry out, in any order.  This means that,
#    if we do some careful bookkeeping, we have N-1 choices for the first
#    multiplication, N-2 for the second, and a total of factorial(N-1)    
#    distinct cases to consider.  Some of these cases collapse to the
#    same paretheses representation, but we don't care.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer dims(n_mats+1): matrix dimension information.  Matrix A(i)
#    has dimensions dims(i) x dims(i+1).  All entries must be positive.
#
#  Output:
#
#    integer cost: the minimal cost, in terms of scalar multiplications,
#    for the optimal ordering of the matrix multiplications.
#
#    integer p(n_mats-1): the multiplication ordering.
#
  import numpy as np
#
#  n_mats is the number of matrices in the product.
#
  n_dims = len ( dims )
  n_mats = n_dims - 1
  n_mults = n_mats - 1
#
#  Deal with stupidity.
#
  if ( n_mats == 1 ):
    cost = 0
    p = np.array ( [ ] )
    return cost, p

  if ( np.any ( dims <= 0 ) ):
    cost = 0
    p = np.linspace ( n_mults, 1, n_mults, dtype = int )
    return cost, p
#
#  Initialize the output.
#
  cost = np.inf
  p = np.linspace ( n_mults, 1, n_mults, dtype = int )
#
#  Prepare to loop over all orderings.
#
  this_p = p.copy()
  pivot_sequence_num = pivot_sequence_enum ( n_mults )

  for i in range ( 0, pivot_sequence_num ):

    this_p = pivot_sequence_successor ( this_p )
    this_cost = pivot_sequence_to_matrix_chain_cost ( n_mats, this_p, dims )

    if ( this_cost < cost ):
      cost = this_cost
      p = this_p.copy()

  return cost, p

def pivot_sequence_check ( t ):

#*****************************************************************************80
#
## pivot_sequence_check() checks a pivot sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer t(n): a pivot sequence.
#
#  Output:
#
#    logical CHECK, error flag.
#    true, T is a pivot sequence.
#    false, T is not a legal pivot sequence.
#
  verbose = False
  check = True

  n = len ( t )

  for i in range ( 0, n ):

    if ( t[i] <= 0 ):

      if ( verbose ):
        print ( '' )
        print ( 'pivot_sequence_check(): Fatal error!' )
        print ( '  t(', i, ') =', t[i], ' <= 0' )

      check = False
      return check

    elif ( n - i < t[i] ):

      if ( verbose ):
        print ( '' )
        print ( 'pivot_seq_check(): Fatal error!' )
        print ( '  n - i = ', n - i, ' < t(', i, ') = ', t[i] )

      check = False
      return check

  return check

def pivot_sequence_enum ( n ):

#*****************************************************************************80
#
## pivot_sequence_enum() enumerates pivot sequences.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of pivot steps.
#
#  Output:
#
#    integer pivot_sequence_num: the number of pivot sequences of n steps.
#
  from math import factorial

  pivot_sequence_num = factorial ( n )

  return pivot_sequence_num

def pivot_sequence_successor ( t ):

#*****************************************************************************80
#
## pivot_sequence_successor() computes the pivot sequence successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer t(n): the previous pivot sequence.
#    To initiate the routine, call with t=linspace(n,1,n).
#
#  Output:
#
#    integer t(n): the lexical successor of the input.
#
  import numpy as np
#
#  Check.
#
  check = pivot_sequence_check ( t )

  if ( not check ):
    print ( '' )
    print ( 'pivot_sequence_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'pivot_sequence_successor(): Fatal error!' )
#
#  Find last entry that is less than its maximum value.
#
  n = len ( t )

  last = -1
  for i in range ( n - 1, -1, -1 ):
    if ( t[i] < n - i ):
      last = i
      break

  if ( last == -1 ):
    t = np.ones ( n, dtype = int )
  else:
    t[last] = t[last] + 1
    t[last+1:n] = 1

  return t

def pivot_sequence_to_matrix_chain_cost ( n_mats, p, dims ):

#*****************************************************************************80
#
## pivot_sequence_to_matrix_chain_cost() evaluates a matrix chain product.
#
#  Discussion:
#
#    There are n_mats matrices to multiply.
#    There are n_dims = n_mats+1 dimensions to consider.
#    There are n_mults = n_mats-1 matrix multiplications to carry out.
#
#    The cost, in terms of multiplications of pairs of real numbers,
#    of a multiplying a single pair of matrices A and B,
#    of dimensions LxM and MxN, is L*M*N.
#
#    The cost of multiplying a sequence of N matrices A*B*C*...*Z
#    will in general vary, depending on the order in which the N-1
#    multiplications are carried out.
#
#    This function assumes that a particular multiplication ordering 
#    has been specified in the pivot sequence p(), and returns the
#    corresponding cost.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n_mats: the number of matrices to multiply.
#
#    integer p(n_mats-1): the pivot sequence.
#
#    integer dims(n_mats+1): the matrix dimensions.
#    For 1 <= i <= n_mats, the i-th matrix has dimension dims(i) x dims(i+1).
#
#  Output:
#
#    integer cost: the matrix multiplication cost.
#
  cost = 0
  n_dims = n_mats + 1
  n_mults = n_mats - 1

  dims2 = dims.copy()
  n_dims2 = n_dims
#
#  Carry out n_mults multiplications.
#  On step I, we carry out multiplication J.
#  Multiplication J involves 
#    dims(j)dims(j+1) * dims(j+1)dims(j+2) => dims(j)dims(j+2)
#  at an additional cost of dims(j) * dims(j+1) * dims(j+2),
#  while removing dims(j+1) from the list of dimensions.
#
  for i in range ( 0, n_mults ):
    j = p[i] - 1
    d1 = dims2[j]
    d2 = dims2[j+1]
    d3 = dims2[j+2]
    cost = cost + d1 * d2 * d3
    for k in range ( j + 1, n_dims2 - 1 ):
      dims2[k] = dims2[k+1]
    n_dims2 = n_dims2 - 1

  return cost

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
  matrix_chain_brute_test ( )
  timestamp ( )

