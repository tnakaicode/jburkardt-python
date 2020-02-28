#! /usr/bin/env python
#
def inversion_to_perm0 ( n, ins ):

#*****************************************************************************80
#
## INVERSION_TO_PERM0: inversion sequence to permutation of (0,...,N-1).
#
#  Discussion:
#
#    For a given permutation P acting on objects 0 through N-1, the
#    inversion sequence INS is defined as:
#
#      INS(1) = 0
#      INS(I) = number of values J < I for which P(I) < P(J).
#
#  Example:
#
#    Input:
#
#      ( 0, 0, 2, 1, 3 )
#
#    Output:
#
#      ( 2, 4, 0, 3, 1 )
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
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Parameters:
#
#    Input, integer N, the number of objects being permuted.
#
#    Input, integer INS(N), the inversion sequence of a permutation.
#    It must be the case that 0 <= INS(I) < I for I = 1 to N.
#
#    Output, integer P(N), the permutation.
#
  from i4vec_indicator0 import i4vec_indicator0

  p = i4vec_indicator0 ( n )

  for i in range ( n, 1, -1 ):

    itemp = p[i-1-ins[i-1]]

    for j in range ( i - ins[i-1], i ):
      p[j-1] = p[j]

    p[i-1] = itemp

  return p

def inversion_to_perm0_test ( ):

#*****************************************************************************80
#
## INVERSION_TO_PERM0_TEST tests INVERSION_TO_PERM0.
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
  from perm0_to_inversion import perm0_to_inversion

  n = 5

  print ( '' )
  print ( 'INVERSION_TO_PERM0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INVERSION_TO_PERM0: inversion => permutation (0,...,N-1).' )

  perm = np.array ( [ 2, 4, 0, 3, 1 ] )
  i4vec_print ( n, perm, '  Permutation:' )

  ins = perm0_to_inversion ( n, perm )
  i4vec_print ( n, ins, '  Inversion:' )

  perm2 = inversion_to_perm0 ( n, ins )
  i4vec_print ( n, perm2, '  Recovered permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'INVERSION_TO_PERM0_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  inversion_to_perm0_test ( )
  timestamp ( )
