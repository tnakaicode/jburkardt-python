#! /usr/bin/env python
#
def perm_to_cycle ( n, p ):

#*****************************************************************************80
#
## PERM_TO_CYCLE converts a permutation from array to cycle form.
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
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), describes the permutation using a
#    single array.  For each index I, I -> P(I).
#
#    Output, integer NCYCLE, the number of cycles.
#    1 <= NCYCLE <= N.
#
#    Output, integer T(N), INDEX(N), describes the permutation
#    as a collection of NCYCLE cycles.  The first cycle is
#    T(1) -> T(2) -> ... -> T(INDEX(1)) -> T(1).
#
  import numpy as np
  from perm_check import perm_check
  from sys import exit
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_TO_CYCLE - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PERM_TO_CYCLE - Fatal error!' )
#
#  Initialize.
#
  ncycle = 0

  index = np.zeros ( n, dtype = np.int32 )
  t = np.zeros ( n, dtype = np.int32 )
  nset = 0
#
#  Find the next unused entry.      
#
  for i in range ( 1, n + 1 ):

    if ( 0 < p[i-1] ):

      ncycle = ncycle + 1
      index[ncycle-1] = 1

      nset = nset + 1
      t[nset-1] = p[i-1]
      p[i-1] = - p[i-1]

      while ( True ):

        j = t[nset-1]

        if ( p[j-1] < 0 ):
          break

        index[ncycle-1] = index[ncycle-1] + 1

        nset = nset + 1
        t[nset-1] = p[j-1]
        p[j-1] = - p[j-1]

  return ncycle, t, index

def perm_to_cycle_test ( ):

#*****************************************************************************80
#
## PERM_TO_CYCLE_TEST tests PERM_TO_CYCLE.
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
  import numpy as np
  import platform
  from perm_print import perm_print

  print ( '' )
  print ( 'PERM_TO_CYCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_TO_CYCLE converts a permutation from' )
  print ( '  array to cycle form.' )

  n = 7
  p = np.array ( [ 4, 5, 1, 2, 3, 6, 7 ], dtype = np.int32 )
  perm_print ( n, p, '  Permutation:' )

  ncycle, t, index = perm_to_cycle ( n, p )

  print ( '' )
  print ( '  Corresponding cycle form:' )
  print ( '  Number of cycles is %d' % ( ncycle ) )
  print ( '' )
  jlo = 0
  for i in range ( 0, ncycle ):
    print ( '    ', end = '' )
    for j in range ( jlo, jlo + index[i] ):
      print ( '%4d' % ( t[j] ), end = '' )
    print ( '' )
    jlo = jlo + index[i]
#
#  Terminate.
# )
  print ( '' )
  print ( 'PERM_TO_CYCLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_to_cycle_test ( )
  timestamp ( )
 
