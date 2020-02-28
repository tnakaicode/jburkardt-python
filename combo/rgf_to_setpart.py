#! /usr/bin/env python
#
def rgf_to_setpart ( m, f ):

#*****************************************************************************80
#
## RGF_TO_SETPART converts a restricted growth function to a set partition.
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
#    Input, integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    Input, integer F(M), the restricted growth function.
#
#    Output, integer NSUB, the number of nonempty subsets into
#    which the set is partitioned.
#
#    Output, integer S(M), describes the partition of a set of
#    M objects into NSUB nonempty subsets.  If element I of the
#    superset belongs to subset J, then S(I) = J.
#
#    Output, integer INDEX(M), lists the location in S of the last
#    element of each subset.  Thus, the elements of subset 1
#    are S(1) through S(INDEX(1)), the elements of subset 2
#    are S(INDEX(1)+1) through S(INDEX(2)) and so on.
#
  import numpy as np
  from rgf_check import rgf_check
  from sys import exit
#
#  Check.
#
  check = rgf_check ( m, f )

  if ( not check ):
    print ( '' )
    print ( 'RGF_TO_SETPART - Fatal error!' )
    print ( '  The input array is illegal!' )
    exit ( 'RGF_TO_SETPART - Fatal error!' )
#
#  Determine the number of subsets.
#
  nsub = max ( f )
#
#  Initialize.
#
  s = np.zeros ( m, dtype = np.int32 )
  index = np.zeros ( nsub, dtype = np.int32 )
#
#  For each subset I, collect the indices of F which have value I.
#  These are the elements of the I-th subset.
#
  k = 0
  for i in range ( 1, nsub + 1 ):
    for j in range ( 0, m ):
      if ( f[j] == i ):
        s[k] = j + 1
        k = k + 1
    index[i-1] = k

  return nsub, s, index

def rgf_to_setpart_test ( ):

#*****************************************************************************80
#
## RGF_TO_SETPART_TEST tests RGF_TO_SETPART.
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
  print ( 'RGF_TO_SETPART_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_TO_SETPART converts a balanced' )
  print ( '  sequence to a restricted growth function' )

  f = np.array ( [ 1, 1, 1, 1, 1, 2, 1, 3 ] )

  i4vec_transpose_print ( m, f,  '  Restricted growth function:' )
#
#  Convert the RGF to a set partition.
#
  nsub, s, index = rgf_to_setpart ( m, f )

  print ( '' )
  print ( '  Corresponding set partition:' )
  print ( '' )
  jlo = 0
  for i in range ( 0, nsub ):
    for j in range ( jlo, index[i] ):
      print ( '%4d' % ( s[j] ), end = '' )
    print ( '' )
    jlo = index[i]
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_TO_SETPART_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_to_setpart_test ( )
  timestamp ( )
 
