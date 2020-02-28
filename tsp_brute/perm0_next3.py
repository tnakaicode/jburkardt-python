#! /usr/bin/env python
#
def perm0_next3 ( n, p, more, rank ):

#*****************************************************************************80
#
## PERM0_NEXT3 computes permutations of (0,...,N-1).
#
#  Discussion:
#
#    The routine is initialized by calling with MORE = TRUE, in which case
#    it returns the identity permutation.
#
#    If the routine is called with MORE = FALSE, then the successor of the
#    input permutation is computed.
#
#    Trotter's algorithm is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hale Trotter,
#    PERM, Algorithm 115,
#    Communications of the Association for Computing Machinery,
#    Volume 5, 1962, pages 434-435.
#
#  Parameters:
#
#    Input, integer N, the number of objects being permuted.
#
#    Input/output, integer P(N).  On input, this is the previous permutation, 
#    if MORE is TRUE.  But on a startup call, with MORE FALSE, the input value 
#    of P is not needed.  On output, the next permutation if MORE is FALSE, 
#    then P is the first permutation in the sequence.
#
#    Input/output, logical MORE.  On input, should be set to FALSE on an
#    initialization call, and on subsequent inputs should have its output
#    value from the previous call.  On output, is TRUE if there was a next
#    permutation to produce, or FALSE if there are no more permutations 
#    to produce.
#
#    Input/output, integer RANK, the rank of the current permutation.  
#
  if ( not more ):

    for i in range ( 0, n ):
      p[i] = i
    more = True
    rank = 1

  else:

    n2 = n
    m2 = rank
    s = n

    while ( True ):

      q = ( m2 % n2 )
      t = ( m2 % ( 2 * n2 ) )

      if ( q != 0 ):
        break

      if ( t == 0 ):
        s = s - 1

      m2 = ( m2 // n2 )
      n2 = n2 - 1

      if ( n2 == 0 ):
        for i in range ( 0, n ):
          p[i] = i
        more = False
        rank = 1
        break

    if ( n2 != 0 ):

      if ( q == t ):
        s = s - q
      else:
        s = s + q - n2

      t      = p[s-1]
      p[s-1] = p[s]
      p[s]   = t

      rank = rank + 1

  return p, more, rank

def perm0_next3_test ( ):

#*****************************************************************************80
#
## PERM0_NEXT3_TEST tests PERM0_NEXT3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PERM0_NEXT3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_NEXT3 generates permutations in order.' )
  print ( '' )

  n = 4
  p = np.zeros ( n )
  more = False
  rank = 0
 
  while ( True ):

    p, more, rank = perm0_next3 ( n, p, more, rank )

    if ( not more ):
      break

    print ( '  %3d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_NEXT3_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_next3_test ( )
  timestamp ( )


