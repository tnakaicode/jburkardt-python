#! /usr/bin/env python
#
def perm0_to_equiv ( n, p ):

#*****************************************************************************80
#
## PERM0_TO_EQUIV computes the partition induced by a permutation of (0,...,N-1).
#
#  Example:
#
#    Input:
#
#      N = 9
#      P = 1, 2, 8, 5, 6, 7, 4, 3, 0
#
#    Output:
#
#      NPART = 3
#      JARRAY = 4, 3, 2
#      IARRAY = 1, 1, 1, 2  3  2  3  2, 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects being permuted.
#
#    Input, integer P(N), a permutation, in standard index form.
#
#    Output, integer NPART, number of subsets in the partition.
#
#    Output, integer JARRAY(N).  JARRAY(I) is the number of elements
#    in the I-th subset of the partition.
#
#    Output, integer IARRAY(N).  IARRAY(I) is the class to which
#    element I belongs.
#
  import numpy as np
  from perm0_check import perm0_check
  from sys import exit

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_TO_EQUIV - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_TO_EQUIV - Fatal error!' )
#
#  Initialize.
#
  iarray = np.zeros ( n, dtype = np.int32 )
  jarray = np.zeros ( n, dtype = np.int32 )

  npart = 0
#
#  Search for the next item J which has not been assigned a subset/orbit.
#
  for j in range ( 1, n + 1 ):

    if ( iarray[j-1] != 0 ):
      continue
#
#  Begin a new subset/orbit.
#
    npart = npart + 1
    k = j
#
#  Add the item to the subset/orbit.
#
    while ( True ):

      jarray[npart-1] = jarray[npart-1] + 1
      iarray[k-1] = npart
#
#  Apply the permutation.  If the permuted object isn't already in the
#  subset/orbit, add it.
#
      k = p[k-1] + 1

      if ( iarray[k-1] != 0 ):
        break

  return npart, jarray, iarray

def perm0_to_equiv_test ( ):

#*****************************************************************************80
#
## PERM0_TO_EQUIV_TEST tests PERM0_TO_EQUIV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from equiv_print import equiv_print
  from perm0_print import perm0_print

  n = 9
  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ] )

  print ( '' )
  print ( 'PERM0_TO_EQUIV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_TO_EQUIV returns the set partition' )
  print ( '  or equivalence classes determined by a' )
  print ( '  permutation.' )

  perm0_print ( n, p, '  The input permutation:' )
 
  npart, jarray, a = perm0_to_equiv ( n, p )

  equiv_print ( n, a, '  The partition:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_TO_EQUIV_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_to_equiv_test ( )
  timestamp ( )
