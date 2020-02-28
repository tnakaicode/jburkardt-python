#! /usr/bin/env python
#
def perm0_free ( npart, ipart, nfree ):

#*****************************************************************************80
#
## PERM0_FREE reports unused items in a partial permutation of (0,...,N-1).
#
#  Discussion:
#
#    It is assumed that the N objects being permuted are the integers
#    from 0 to N-1, and that IPART contains a "partial" permutation, that
#    is, the NPART entries of IPART represent the beginning of a
#    permutation of all N items.
#
#    The routine returns in IFREE the items that have not been used yet.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NPART, the number of entries in IPART.  NPART may be 0.
#
#    Input, integer IPART(NPART), the partial permutation, which should
#    contain, at most once, some of the integers between 1 and
#    NPART+NFREE.
#
#    Input, integer NFREE, the number of integers that have not been
#    used in IPART.  This is simply N - NPART.  NFREE may be zero.
#
#    Output, integer IFREE(NFREE), the integers between 1 and NPART+NFREE
#    that were not used in IPART.
#
  import numpy as np
  from sys import exit
  from i4vec_indicator0 import i4vec_indicator0

  n = npart + nfree

  if ( npart < 0 ):

    print ( '' )
    print ( 'PERM0_FREE - Fatal error!' )
    print ( '  NPART < 0.' )
    exit ( 'PERM0_FREE - Fatal error!' )

  elif ( npart == 0 ):

    ifree = i4vec_indicator0 ( n )

  elif ( nfree < 0 ):

    print ( '' )
    print ( 'PERM0_FREE - Fatal error!' )
    print ( '  NFREE < 0.' )
    exit ( 'PERM0_FREE - Fatal error!' )

  elif ( nfree == 0 ):

    ifree = np.zeros ( 0 )
    return ifree

  else:

    ifree = np.zeros ( nfree )

    k = 0

    for i in range ( 0, n ):

      match = False

      for j in range ( 0, npart ):

        if ( ipart[j] == i ):
          match = True
          break

      if ( not match ):

        if ( nfree < k ):
          print ( '' )
          print ( 'PERM0_FREE - Fatal error!' )
          print ( '  The partial permutation is illegal.' )
          exit ( 'PERM0_FREE - Fatal error!' )

        ifree[k] = i
        k = k + 1

  return ifree

def perm0_free_test ( ):

#*****************************************************************************80
#
## PERM0_FREE_TEST tests PERM0_FREE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5
  p = np.array ( [ 4, 1, 2, 3, 0 ] )

  print ( '' )
  print ( 'PERM0_FREE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_FREE returns the unused values in a partial permutation.' )

  for npart in range ( 1, n + 1 ):
    ipart = np.zeros ( npart )
    for j in range ( 0, npart ):
      ipart[j] = p[j]
    nfree = n - npart
    ifree = perm0_free ( npart, ipart, nfree )
    i4vec_transpose_print ( npart, ipart, '  Partial permutation:' )
    i4vec_transpose_print ( nfree, ifree, '  Values not yet used:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_FREE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_free_test ( )
  timestamp ( )

