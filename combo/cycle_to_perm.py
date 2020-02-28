#! /usr/bin/env python
#
def cycle_to_perm ( n, ncycle, t, index ):

#*****************************************************************************80
#
## CYCLE_TO_PERM converts a permutation from cycle to array form.
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
#    Input, integer N, the number of items permuted.
#    N must be positive.
#
#    Input, integer NCYCLE, the number of cycles.
#    1 <= NCYCLE <= N.
#
#    Input, integer T(N), INDEX(NCYCLE), describes the permutation
#    as a collection of NCYCLE cycles.  The first cycle is
#    T(1) -> T(2) -> ... -> T(INDEX(1)) -> T(1).
#
#    Output, integer P(N), describes the permutation using a
#    single array.  For each index I, I -> P(I).
#
  import numpy as np
  from cycle_check import cycle_check
  from sys import exit
#
#  Check.
#
  check = cycle_check ( n, ncycle, t, index )

  if ( not check ):
    print ( '' )
    print ( 'CYCLE_TO_PERM - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'CYCLE_TO_PERM - Fatal error!' )

  p = np.zeros ( n )

  jhi = 0

  for  i in range ( 0, ncycle  ):

    jlo = jhi + 1
    jhi = jhi + index[i]

    for j in range ( jlo, jhi + 1 ):

      if ( j < jhi ):
        p[t[j-1]-1] = t[j]
      else:
        p[t[j-1]-1] = t[jlo-1]

  return p

def cycle_to_perm_test ( ):

#*****************************************************************************80
#
## CYCLE_TO_PERM_TEST tests CYCLE_TO_PERM.
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
  from perm_print import perm_print

  print ( '' )
  print ( 'CYCLE_TO_PERM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version (  ) ) )
  print ( '  CYCLE_TO_PERM converts a permutation from' )
  print ( '  cycle to array form.' )

  n = 7
  ncycle = 3
  t = np.array ( [ 4, 2, 5, 3, 1, 6, 7 ] )
  index = np.array ( [ 5, 1, 1 ] )

  print ( '' )
  print ( '  Permutation in cycle form:' )
  print ( '  Number of cycles is %d' % ( ncycle ) )
  print ( '' )
  jlo = 0
  for i in range ( 0, ncycle ):
    print ( '    ', end = '' )
    for j in range ( jlo, jlo + index[i] ):
      print ( '%4d'% ( t[j] ), end = '' )
    print ( '' )
    jlo = jlo + index[i]

  p = cycle_to_perm ( n, ncycle, t, index )

  perm_print ( n, p, '  Corresponding permutation form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_TO_PERM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cycle_to_perm_test ( )
  timestamp ( )
 
