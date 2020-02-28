#! /usr/bin/env python
#
def rgf_successor ( m, f, rank ):

#*****************************************************************************80
#
## RGF_SUCCESSOR generates the next restricted growth function.
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
#    Input/output, integer F(M), the restricted growth function.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  from rgf_check import rgf_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, m ):
      f[i] = 1
    rank = 0
    return f, rank
#
#  Check.
#
  check = rgf_check ( m, f )

  if ( not check ):
    print ( '' )
    print ( 'RGF_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal!' )
    exit ( 'RGF_SUCCESSOR - Fatal error!' )
#
#  Find the first position from the right which can be incremented.
#
  for i in range ( m, 1, -1 ):
    fmax = 1
    for j in range ( 2, i ):
      fmax = max ( fmax, f[j-1] )
#
#  Increment the function at this position, and set later entries to 1.
#
    if ( f[i-1] != fmax + 1 ):
      f[i-1] = f[i-1] + 1
      for j in range ( i + 1, m + 1 ):
        f[j-1] = 1
      rank = rank + 1
      return f, rank
#
#  The final element was input.
#  Return the first element.
#
  for i in range ( 0, m ):
    f[i] = 1
  rank = 0

  return f, rank

def rgf_successor_test ( ):

#*****************************************************************************80
#
## RGF_SUCCESSOR_TEST tests RGF_SUCCESSOR.
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

  m = 4

  print ( '' )
  print ( 'RGF_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_SUCCESSOR lists restricted growth functions.' )
  print ( '' )

  f = np.zeros ( m )
  rank = -1

  while ( True ):

    rank_old = rank

    f, rank = rgf_successor ( m, f, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( m, f, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_successor_test ( )
  timestamp ( )
 
