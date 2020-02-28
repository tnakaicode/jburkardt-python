#! /usr/bin/env python
#
def vector_constrained_next5 ( n, x, sum_min, sum_max, base, more ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT5 returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider all positive integer vectors of dimension N whose
#    components satisfy SUM_MIN <= X(1:N) <= SUM_MAX.
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    SUM_MIN = 5
#    SUM_MAX = 6
#
#    #  X(1)  X(2)  X(3)     SUM
#
#    1    3     1     1        5
#    2    2     2     1        5
#    3    2     1     2        5
#    4    1     3     1        5
#    5    1     2     2        5
#    6    1     1     3        5
#
#    7    4     1     1        6
#    8    3     2     1        6
#    9    3     1     2        6
#   10    2     3     1        6
#   11    2     2     2        6
#   12    2     1     3        6
#   13    1     4     1        6
#   14    1     3     2        6
#   15    1     2     3        6
#   16    1     1     4        6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components in the vector.
#
#    Input, integer SUM_MIN, SUM_MAX, the minimum and maximum sums..
#
#    Input/output, integer X(N).   On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On output with MORE = TRUE, the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    Input/output, integer BASE, a variable which is used only by
#    this function, but which must be declared by the calling program.
#    The output value from the previous call must be used as the input
#    value for the next call.
#
#    Input/output, logical MORE.  On input, if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On output, if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#

#
#  Initialization.
#
  if ( not more ):

    if ( sum_max < n ):
      more = False
      return x, base, more

    if ( sum_max < sum_min ):
      more = False
      return x, base, more

    more = True

    base = max ( sum_min, n )

    x[0] = base - n + 1
    for i in range ( 1, n ):
      x[i] = 1

    return x, base, more
#
#  Next element.
#
  else:
#
#  Search from the right, seeking an index I < N for which 1 < X(I).
#
    for i in range ( n - 2, -1, -1 ):
#
#  If you find such an I, decrease X(I) by 1, and add that to X(I+1).
#
      if ( 1 < x[i] ):

        x[i]   = x[i]   - 1
        x[i+1] = x[i+1] + 1
#
#  Now grab all the "excess" 1's from the entries to the right of X(I+1).
#
        for j in range ( i + 2, n ):
          if ( 1 < x[j] ):
            x[i+1] = x[i+1] + x[j] - 1
            x[j] = 1

        return x, base, more
#
#  The current vector is (1,1,1,...,BASE-N+1).
#  If BASE < SUM_MAX, then increase BASE by 1, and start the new series.
#
    if ( base < sum_max ):
      base = base + 1
      x[0] = base - n + 1
      for i in range ( 1, n ):
        x[i] = 1
      return x, base, more
#
#  We returned the last legal vector on the previous call.
#  The calculation is done.
#
    more = False

  return x, base, more

def vector_constrained_next5_test ( ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT5_TEST tests VECTOR_CONSTRAINED_NEXT5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'VECTOR_CONSTRAINED_NEXT5_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VECTOR_CONSTRAINED_NEXT5:' )
  print ( '  Generate integer vectors X such that:' )
  print ( '    SUM_MIN <= sum ( X(1:N) ) <= SUM_MAX,' )
  print ( '  We require every X(I) to be at least 1.' )

  n = 3
  sum_min = 5
  sum_max = 7
  base = 0
  more = False

  print ( '' )
  print ( '  N =       %d' % ( n ) )
  print ( '  SUM_MIN = %d' % ( sum_min ) )
  print ( '  SUM_MAX = %d' % ( sum_max ) )
  print ( '' )
  print ( '         #        X(1)      X(2)      X(3)' )
  print ( '' )

  i = 0
  x = np.zeros ( n )
  
  while ( True ):

    x, base, more = vector_constrained_next5 ( n, x, sum_min, sum_max, base, more )

    if ( not more ):
      break

    i = i + 1
    print ( '  %8d:' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '  %8d' % ( x[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VECTOR_CONSTRAINED_NEXT5_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  vector_constrained_next5_test ( )
  timestamp ( )

