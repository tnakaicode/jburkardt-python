#! /usr/bin/env python
#
def setpart_to_rgf ( m, nsub, s, index ):

#*****************************************************************************80
#
## SETPART_TO_RGF converts a set partition to a restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer M, the number of elements of the set.
#    M must be positive.
#
#    Input, integer NSUB, the number of nonempty subsets into
#    which the set is partitioned.  1 <= NSUB <= M.
#
#    Input, integer INDEX(NSUB), lists the location in S of the
#    last element of each subset.  Thus, the elements of subset 1
#    are S(1) through S(INDEX(1)), the elements of subset 2
#    are S(INDEX(1)+1) through S(INDEX(2)) and so on.
#
#    Input, integer S(M), contains the integers from 1 to M,
#    grouped into subsets as described by INDEX.
#
#    Output, integer F(M), the restricted growth function from
#    M to NSUB.
#
  import numpy as np
  from setpart_check import setpart_check
  from sys import exit
#
#  Check.
#
  check = setpart_check ( m, nsub, s, index )

  if ( not check ):
    print ( '' )
    print ( 'SETPART_TO_RGF - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'SETPART_TO_RGF - Fatal error!' )

  f = np.zeros ( m )

  khi = 0
  for i in range ( 0, nsub ):
    klo = khi + 1
    khi = index[i]
    for k in range ( klo, khi + 1 ):
      f[s[k-1]-1] = i + 1

  return f

def setpart_to_rgf_test ( ):

#*****************************************************************************80
#
## SETPART_TO_RGF_TEST tests SETPART_TO_RGF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  m = 8

  print ( '' )
  print ( 'SETPART_TO_RGF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SETPART_TO_RGF converts a set partition' )
  print ( '  to a restricted growth function.' )

  nsub = 3
  s = np.array ( [ 1, 2, 3, 4, 5, 6, 7, 8 ] )
  index = np.array ( [ 6, 7, 8 ] )

  print ( '' )
  print ( '  The set partition' )
  print ( '  M = %d' % ( m ) )
  print ( '  NSUB = %d' % ( nsub ) )
  print ( '' )
  jlo = 0
  for i in range ( 0, nsub ):
    for j in range ( jlo, index[i] ):
      print ( '%4d' % ( s[j] ), end = '' )
    print ( '' )
    jlo = index[i]
#
#  Convert the set partition back to an RGF.
#
  f = setpart_to_rgf ( m, nsub, s, index )

  i4vec_transpose_print ( m, f,  '  Recovered restricted growth function:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SETPART_TO_RGF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  setpart_to_rgf_test ( )
  timestamp ( )
 
