#! /usr/bin/env python
#
def i4vec_backtrack ( n, maxstack, x, indx, k, nstack, stacks, ncan ):

#*****************************************************************************80
#
## I4VEC_BACKTRACK supervises a backtrack search for a vector.
#
#  Discussion:
#
#    The routine tries to construct a vector one index at a time,
#    using possible candidates as supplied by the user.
#
#    At any time, the partially constructed vector may be discovered to be
#    unsatisfactory, but the routine records information about where the
#    last arbitrary choice was made, so that the search can be
#    carried out efficiently, rather than starting out all over again.
#
#    First, call the routine with INDX = 0 so it can initialize itself.
#
#    Now, on each return from the routine, if INDX is:
#      1, you've just been handed a complete candidate vector
#         Admire it, analyze it, do what you like.
#      2, please determine suitable candidates for position X(K).
#         Return the number of candidates in NCAN(K), adding each
#         candidate to the end of STACKS, and increasing NSTACK.
#      3, you're done.  Stop calling the routine
#
#    At one time, the variable "stacks" was called "stack", but MATLAB
#    now seems to have taken "stack" as a keyword that is no longer
#    acceptable as a variable name.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of positions to be filled in the vector.
#
#    Input, integer MAXSTACK, the maximum length of the stack.
#
#    Input, integer X(N), the partially filled in candidate vector.
#
#    Input, integer INDX, a communication flag.
#    * 0, to begin a backtracking search.
#    * 2, the requested candidates for position K have been added to
#      STACKS, and NCAN(K) was updated.
#
#    Input, integer K, the index in X that we are trying to fill.
#
#    Input, integer NSTACK, the current length of the stack.
#
#    Input, integer STACKS(MAXSTACK), a list of all current candidates for
#    all positions 1 through K.
#
#    Input, integer NCAN(N), lists the current number of candidates for
#    all positions 1 through K.
#
#    Output, integer X(N), the partially filled in candidate vector.
#
#    Output, integer INDX, a communication flag.
#    * 1, a complete output vector has been determined and returned in X(1:N)
#    * 2, candidates are needed for position X(K)
#    * 3, no more possible vectors exist.
#
#    Output, integer K, the index in X that we are trying to fill.
#
#    Output, integer NSTACK, the current length of the stack.
#
#    Output, integer STACKS(MAXSTACK), a list of all current candidates for
#    all positions 1 through K.
#
#    Output, integer NCAN(N), lists the current number of candidates for
#    all positions 1 through K.
#

#
#  If this is the first call, request a candidate for position 1.
#
  if ( indx == 0 ):
    k = 1
    nstack = 0
    indx = 2
    return x, indx, k, nstack, stacks, ncan
#
#  Examine the stack.
#
  while ( True ):
#
#  If there are candidates for position K, take the first available
#  one off the stack, and increment K.
#
#  This may cause K to reach the desired value of N, in which case
#  we need to signal the user that a complete set of candidates
#  is being returned.
#
    if ( 0 < ncan[k-1] ):
      x[k-1] = stacks[nstack-1]
      nstack = nstack - 1

      ncan[k-1] = ncan[k-1] - 1

      if ( k != n ):
        k = k + 1
        indx = 2
      else:
        indx = 1

      break
#
#  If there are no candidates for position K, then decrement K.
#  If K is still positive, repeat the examination of the stack.
#
    else:

      k = k - 1

      if ( k <= 0 ):
        indx = 3
        break

  return x, indx, k, nstack, stacks, ncan

def i4vec_backtrack_test ( ):

#*****************************************************************************80
#
## I4VEC_BACKTRACK_TEST tests I4VEC_BACKTRACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_BACKTRACK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_BACKTRACK uses backtracking, seeking a vector X of' )
  print ( '  N values which satisfies some condition.' )

  print ( '' )
  print ( '  In this demonstration, we have 8 integers W(I).' )
  print ( '  We seek all subsets that sum to 53.' )
  print ( '  X(I) is 0 or 1 if the entry is skipped or used.' )
  print ( '' )

  n = 8
  maxstack = 100
  stacks = np.zeros ( maxstack )
  x = np.zeros ( n )
  indx = 0
  k = 1
  nstack = 0
  ncan = np.zeros ( n )

  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ], dtype = np.int32 )
  t = 53

  found_num = 0

  while ( True ):

    x, indx, k, nstack, stacks, ncan = i4vec_backtrack ( n, maxstack, \
    x, indx, k, nstack, stacks, ncan )

    if ( indx == 1 ):

      found_num = found_num + 1
      print ( '  %2d   ' % ( found_num ), end = '' )

      total = 0
      for i in range ( 0, n ):
        if ( x[i] == 1 ):
          total = total + w[i]
      print ( '  %2d:  ' % ( total ), end = '' )

      for i in range ( 0, n ):
        if ( x[i] == 1 ):
          print ( '  %d' % ( w[i] ), end = '' )
      print ( '' )
#
#  Given that we've chose X(1:K-1), what are our choices for X(K)?
#
#    if T < TOTAL, 
#      no choices
#    if T = TOTAL, 
#      X(K) = 0
#    if T > TOTAL and K < N, 
#      X(k) = 0
#      If ( W(K)+TOTAL <= T ) X(K) = 1
#    If T > TOTAL and K = N,
#      If ( W(K) + TOTAL) = T ) X(K) = 1
#
    elif ( indx == 2 ):

      total = 0
      for i in range ( 0, k - 1 ):
        if ( x[i] == 1 ):
          total = total + w[i]

      if ( t < total ):

        ncan[k-1] = 0

      elif ( t == total ):

        ncan[k-1] = ncan[k-1] + 1
        nstack = nstack + 1
        stacks[nstack-1] = 0

      elif ( total < t and k < n ):

        ncan[k-1] = ncan[k-1] + 1
        nstack = nstack + 1
        stacks[nstack-1] = 0

        if ( total + w[k-1] <= t ):
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1

      elif ( total < t and k == n ):

        if ( total + w[k-1] == t ):
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1

    else:

      print ( '' )
      print ( '  Done!' )
      break

#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_BACKTRACK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_backtrack_test ( )
  timestamp ( )

