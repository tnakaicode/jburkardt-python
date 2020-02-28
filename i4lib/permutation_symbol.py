#! /usr/bin/env python3
#
def permutation_symbol ( n, ivec ):

#*****************************************************************************80
#
## PERMUTATION_SYMBOL evaluates the Levi-Civita permutation symbol.
#
#  Discussion:
#
#    Given a vector of N values I(), 
#
#      epsilon = product ( q < p ) ( i(p) - i(q) ) / abs ( i(p) - i(q) )
#
#    where epsilon is 0 if any pair of values are equal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, integer IVEC(N), the vector of values.
#
#    Output, integer VALUE, the value of the Levi-Civita permutation symbol,
#    which will be -1, 0, or 1.
#
  value = 1

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      if ( ivec[i] == ivec[j] ):
        value = 0
        return value
      elif ( ivec[i] < ivec[j] ):
        value = - value

  return value

def permutation_symbol_test ( ):

#*****************************************************************************80
#
## PERMUTATION_SYMBOL_TEST tests PERMUTATION_SYMBOL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'PERMUTATION_SYMBOL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERMUTATION_SYMBOL evaluates the Levi-Civita permutation symbol.' )

  n = 5
  a = np.array ( [ 1, 2, 3, 4, 5 ] )
  i4vec_transpose_print ( n, a, '  Input vector:' )
  value = permutation_symbol ( n, a )
  print ( '  Levi-Civita permutation symbol = %d' % ( value ) )

  n = 5
  a = np.array ( [ 4, 2, 3, 1, 5 ] )
  i4vec_transpose_print ( n, a, '  Input vector:' )
  value = permutation_symbol ( n, a )
  print ( '  Levi-Civita permutation symbol = %d' % ( value ) )

  n = 5
  a = np.array ( [ 1, 2, 3, 4, 2 ] )
  i4vec_transpose_print ( n, a, '  Input vector:' )
  value = permutation_symbol ( n, a )
  print ( '  Levi-Civita permutation symbol = %d' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERMUTATION_SYMBOL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  permutation_symbol_test ( )
  timestamp ( )

