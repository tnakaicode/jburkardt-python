#! /usr/bin/env python
#
def perm0_inverse2 ( n, p ):

#*****************************************************************************80
#
## PERM0_INVERSE2 inverts a permutation of (0,...,N-1).
#
#  Discussion:
#
#    The routine needs no extra vector storage in order to compute the
#    inverse of a permutation.
#
#    This feature might be useful if the permutation is large.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the number of objects in the permutation.
#
#    Input, integer P(N), the permutation.
#
#    Output, integer P_INV(N), the inverse permutation.
#
  import numpy as np
  from perm0_check import perm0_check
  from sys import exit

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_INVERSE2 - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_INVERSE2 - Fatal error!' )

  p_inv = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p_inv[i] = p[i]

  tag = np.ones ( n, dtype = np.int32 )

  for m in range ( n - 1, -1, -1 ):

    i = p_inv[m]
    ti = tag[m]

    if ( ti < 0 ):

      tag[m] = +1

    elif ( i != m ):

      k = m

      while ( True ):

        j = p_inv[i]

        tag[i] = -1
        p_inv[i] = k

        if ( j == m ):
          p_inv[m] = i
          break

        k = i
        i = j

  return p_inv

def perm0_inverse2_test ( ):

#*****************************************************************************80
#
## PERM0_INVERSE2_TEST tests PERM0_INVERSE2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm0_print import perm0_print

  n = 7
  p = np.array ( [ 3, 2, 4, 0, 6, 5, 1 ] )

  print ( '' )
  print ( 'PERM0_INVERSE2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_INVERSE2 inverts a permutation in place.' )

  perm0_print ( n, p, '  The original permutation:' )
 
  p_inv = perm0_inverse2 ( n, p )
 
  perm0_print ( n, p_inv, '  The inverted permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_INVERSE2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_inverse2_test ( )
  timestamp ( )

