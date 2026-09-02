#! /usr/bin/env python3
#
def einsum_test ( ):

#*****************************************************************************80
#
## einsum_test() tests Einstein summation implemented by einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'einsum_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  einsum() carries out Einstein summation.' )

  matrix_column_sum_test ( )
  matrix_diagonal_test ( )
  matrix_matrix_multiplication_test ( )
  matrix_matrix_multiplication_hadamard_test ( )
  matrix_row_sum_test ( )
  matrix_trace_test ( )
  matrix_transpose_test ( )
  matrix_vector_multiplication_test ( )
  vector_inner_product_test ( )
  vector_norm_test ( )
  vector_outer_product_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'einsum_test():' )
  print ( '  Normal end of execution.' )

  return

def matrix_column_sum_test ( ):

#*****************************************************************************80
#
## matrix_column_sum_test() computes matrix column sums using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint
  
  print ( '' )
  print ( '  matrix_column_sum_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ], \
    [ 31, 32, 33 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  Ac = np.einsum ( 'ij -> j', A )
  print ( '  Ac = np.einsum ( \'ij -> j\', A ):' )
  pprint.pprint ( Ac )

  return

def matrix_diagonal_test ( ):

#*****************************************************************************80
#
## matrix_diagonal_test() computes a matrix diagonal using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint
  
  print ( '' )
  print ( '  matrix_diagonal_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ], \
    [ 31, 32, 33 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  D = np.einsum ( 'ii -> i', A )
  print ( '  D = np.einsum ( \'ii -> i\', A ):' )
  pprint.pprint ( D )

  return

def matrix_matrix_multiplication_test ( ):

#*****************************************************************************80
#
## matrix_matrix_multiplication_test() computes a matrix-matrix product().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  matrix_matrix_multiplication_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  B = np.array ( [ \
    [ 1, 2 ], \
    [ 3, 4 ], \
    [ 5, 6 ] ] )
  print ( '  B:' )
  pprint.pprint ( B )

  AB = np.einsum ( 'ij,jk -> ik', A, B )
  print ( '  AB = np.einsum ( \'ij -> jk\', A, B ):' )
  pprint.pprint ( AB )

  return

def matrix_matrix_multiplication_hadamard_test ( ):

#*****************************************************************************80
#
## matrix_matrix_multiplication_hadamard_test() computes Hadamard matrix product.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  matrix_matrix_multiplication_hadamard_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  B = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ] ] )
  print ( '  B:' )
  pprint.pprint ( B )

  AB = np.einsum ( 'ij,ij -> ij', A, B )
  print ( '  AB = np.einsum ( \'ij,ij -> ij\', A, B ):' )
  pprint.pprint ( AB )

  return

def matrix_row_sum_test ( ):

#*****************************************************************************80
#
## matrix_row_sum_test() computes a matrix row sum using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint
  
  print ( '' )
  print ( '  matrix_row_sum_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ], \
    [ 31, 32, 33 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  Ar = np.einsum ( 'ij -> i', A )
  print ( '  Ar = np.einsum ( \'ij -> i\', A ):' )
  pprint.pprint ( Ar )

  return

def matrix_trace_test ( ):

#*****************************************************************************80
#
## matrix_trace_test() computes a matrix trace using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#

  import numpy as np
  import pprint

  print ( '' )
  print ( '  matrix_trace_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ], \
    [ 31, 32, 33 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  D = np.einsum ( 'ii ->', A )
  print ( '  D = np.einsum ( \'ii ->\', A ):' )
  pprint.pprint ( D )

  return

def matrix_transpose_test ( ):

#*****************************************************************************80
#
## matrix_transpose_test() computes a matrix transpose using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  matrix_transpose_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  AT = np.einsum ( 'ij -> ji', A )
  print ( '  AT = np.einsum ( \'ij -> ji\', A ):' )
  pprint.pprint ( AT )

  return

def matrix_vector_multiplication_test ( ):

#*****************************************************************************80
#
## matrix_vector_multiplication_test() computes a matrix vector product using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  matrix_vector_multiplication_test():' )

  A = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ] ] )
  print ( '  A:' )
  pprint.pprint ( A )

  v = np.array ( [ 1, 2 ] )
  print ( '  v:' )
  pprint.pprint ( v )

  Av = np.einsum ( 'ij,i -> j', A, v )
  print ( '  Av = np.einsum ( \'ij -> j\', A, v ):')
  pprint.pprint ( Av )

  return

def vector_inner_product_test ( ):

#*****************************************************************************80
#
## vector_inner_product_test() computes a vector inner product using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  vector_inner_product_test():' )

  u = np.array ( [ 1, 2, 3 ] )
  print ( '  u:' )
  pprint.pprint ( u )

  v = np.array ( [ 4, 5, 6 ] )
  print ( '  v:' )
  pprint.pprint ( v )

  w = np.einsum ( 'i,i ->', u, v )
  print ( '  w = np.einsum ( \'i,i ->\', u, v ):')
  pprint.pprint ( w )

  return

def vector_norm_test ( ):

#*****************************************************************************80
#
## vector_norm_test() computes a vector norm using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  vector_norm_test():' )

  u = np.array ( [ 1, 2, 3 ] )
  print ( '  u:' )
  pprint.pprint ( u )

  s = np.sqrt ( np.einsum ( 'i,i ->', u, u ) )
  print ( '  s = np.sqrt ( np.einsum ( \'i,i ->\', u, u ) )')
  pprint.pprint ( s )

  return

def vector_outer_product_test ( ):

#*****************************************************************************80
#
## vector_outer_product_test() computes a vector outer product using einsum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 August 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( '  vector_outer_product_test():' )

  u = np.array ( [ 1, 2, 3 ] )
  print ( '  u:' )
  pprint.pprint ( u )

  v = np.array ( [ 4, 5, 6 ] )
  print ( '  v:' )
  pprint.pprint ( v )

  w = np.einsum ( 'i,j ->', u, v )
  print ( '  w = np.einsum ( \'i,j ->\', u, v )')
  pprint.pprint ( w )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  einsum_test ( )
  timestamp ( )

    
