#! /usr/bin/env python
#
def vector_constrained_next7 ( n, level_weight, x_max, x, q_min, q_max, more ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT7 returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider vectors X of dimension N satisfying:
#
#      0 <= X(1:N) <= X_MAX(1:N).
#
#    and the following constraint:
#
#      Q_MIN < sum ( 1 <= I <= N ) LEVEL_WEIGHT(I) * X(I) <= Q_MAX
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    LEVEL_WEIGHT    4.0  3.0  5.0
#    Q_MIN   16.0
#    Q_MAX   20.0
#    X_MAX:   5   6   4
#
#    #  X(1)  X(2)  X(3)     Total
#
#    1    3     1     1       20.0
#    2    2     2     1       19.0
#    3    1     3     1       18.0
#    4    1     1     2       17.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components in the vector.
#
#    Input, real LEVEL_WEIGHT(N), the coefficient vector.
#
#    Input, integer X_MAX(N), the maximum
#    values allowed in each component.
#
#    Input, integer X(N).  On first call, with
#    MORE = FALSE, the input value of X is not important.  On subsequent calls,
#    the input value of X should be the output value from the previous call.
#
#    Input, real Q_MIN, Q_MAX, the lower and upper
#    limits on the sum.
#
#    Input, logical MORE.  If the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  
#
#    Output, integer X(N), (with MORE = TRUE), the value of X will be 
#    the "next" vector in the reverse lexicographical list of vectors 
#    that satisfy the condition.  However, on output with MORE = FALSE, 
#    the vector X is meaningless, because there are no more vectors 
#    in the list.
#
#    Output, logical MORE is TRUE if the next value of X was found, and
#    FALSE if there were no more values of X to compute.  
#
  if ( not more ):

    more = True

    for i in range ( 0, n ):
      x[i] = 0

    total = 0.0
    for i in range ( 0, n ):
      total = total + level_weight[i] * x[i]

    if ( q_min < total and total <= q_max ):
      return x, more

  while ( True ):

    j = n - 1

    while ( True ):

      if ( x[j] < x_max[j] ):
        break

      if ( j <= 0 ):
        more = False
        return x, more

      j = j - 1

    x[j] = x[j] + 1
    for i in range ( j + 1, n ):
      x[i] = 0

    total = 0.0
    for i in range ( 0, n ):
      total = total + level_weight[i] * x[i]

    if ( q_min < total and total <= q_max ):
      break

  return x, more

def vector_constrained_next7_test ( ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT7_TEST tests VECTOR_CONSTRAINED_NEXT7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'VECTOR_CONSTRAINED_NEXT7_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VECTOR_CONSTRAINED_NEXT7:' )
  print ( '  Consider vectors:' )
  print ( '    0 <= X(1:N) <= X_MAX(1:N),' )
  print ( '  Set' )
  print ( '    TOTAL = sum ( ALPHA(1:N) * X(1:N) )' )
  print ( '  Accept only vectors for which:' )
  print ( '    Q_MIN <= TOTAL <= Q_MAX' )

  for n in range ( 2, 4 ):

    if ( n == 2 ):
      alpha = np.array ( [ 4.0, 3.0 ] )
      x_max = np.array ( [ 2, 6 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False
    elif ( n == 3 ):
      alpha = np.array ( [ 4.0, 3.0, 5.0 ] )
      x_max = np.array ( [ 2, 6, 4 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False

    print ( '' )
    print ( '  ALPHA:', end = '' )
    for i in range ( 0, n ):
      print ( '  %14f' % ( alpha[i] ), end = '' )
    print ( '' )
    print ( '' )
    print ( '  Q_MIN:%14f' % ( q_min ) )
    print ( '  Q_MAX:%14f' % ( q_max ) )
    print ( '  X_MAX:', end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x_max[i] ), end = '' )
    print ( '' )
    print ( '' )

    rank = 0

    while ( True ):

      x, more = vector_constrained_next7 ( n, alpha, x_max, x, q_min, q_max, more )

      if ( not more ):
        break
 
      total = 0.0
      for i in range ( 0, n ):
        total = total + alpha[i] * x[i]

      rank = rank + 1
      print ( '  %8d  %14f' % ( rank, total ), end = '' )
      for i in range ( 0, n ):
        print ( '  %8d' % ( x[i] ), end = '' )
      print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VECTOR_CONSTRAINED_NEXT7_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  vector_constrained_next7_test ( )
  timestamp ( )

