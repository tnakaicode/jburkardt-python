#! /usr/bin/env python
#
def perm0_to_inversion ( n, p ):

#*****************************************************************************80
#
## PERM0_TO_INVERSION: permutation (0,...,N-1) to inversion sequence.
#
#  Discussion:
#
#    For a given permutation P acting on objects 0 through N-1, the inversion
#    sequence INS is defined as:
#
#      INS(1) = 0
#      INS(I) = number of values J < I for which P(I) < P(J).
#
#  Example:
#
#    Input:
#
#      ( 2, 4, 0, 3, 1 )
#
#    Output:
#
#      ( 0, 0, 2, 1, 3 )
#
#    The original permutation can be recovered from the inversion sequence.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton and Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Parameters:
#
#    Input, integer N, the number of objects being permuted.
#
#    Input, integer P(N), the permutation, in standard index form.
#    The I-th item has been mapped to P(I).
#
#    Output, integer INS(N), the inversion sequence of the permutation.
#
  import numpy as np
  from sys import exit
  from perm0_check import perm0_check

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_TO_INVERSION - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    error ( 'PERM0_TO_INVERSION - Fatal error!' )

  ins = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      if ( p[i] < p[j] ):
        ins[i] = ins[i] + 1

  return ins

def perm0_to_inversion_test ( ):

#*****************************************************************************80
#
#% PERM0_TO_INVERSION_TEST tests PERM0_TO_INVERSION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print
  from inversion_to_perm0 import inversion_to_perm0
  from perm0_print import perm0_print

  n = 5

  print ( '' )
  print ( 'PERM0_TO_INVERSION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_TO_INVERSION: permutation (0,...,N-1) => inversion.' )

  perm = np.array ( [ 2, 4, 0, 3, 1 ] )
  perm0_print ( n, perm, '  Permutation:' )

  ins = perm0_to_inversion ( n, perm )
  i4vec_print ( n, ins, '  Inversion:' )

  perm2 = inversion_to_perm0 ( n, ins )
  perm0_print ( n, perm2, '  Recovered permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_TO_INVERSION_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_to_inversion_test ( )
  timestamp ( )

