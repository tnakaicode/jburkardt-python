#! /usr/bin/env python
#
def perm_random ( n, seed ):

#*****************************************************************************80
#
## PERM_RANDOM selects a random permutation of 1, ..., N.
#
#  Discussion:
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of objects to be permuted.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer P(N), a permutation of ( 1, 2, ..., N ), in standard
#    index form.
#
#    Output, integer SEED, the updated random number seed.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  p = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p[i] = i + 1

  for i in range ( 0, n - 1 ):

    j, seed = i4_uniform_ab ( i, n - 1, seed )

    temp = p[i]
    p[i] = p[j]
    p[j] = temp

  return p, seed

def perm_random_test ( ):

#*****************************************************************************80
#
## PERM_RANDOM_TEST tests PERM_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5

  print ( '' )
  print ( 'PERM_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_RANDOM randomly selects a permutation of 1, ..., N.' )
  print ( '' )

  seed = 123456789

  for test in range ( 0, 5 ):

    p, seed = perm_random ( n, seed )

    i4vec_transpose_print ( n, p, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_random_test ( )
  timestamp ( )
 
