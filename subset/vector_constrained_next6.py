#! /usr/bin/env python
#
def vector_constrained_next6 ( n, alpha, x_min, x_max, x, q_min, q_max, more ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT6 returns the "next" constrained vector.
#
#  Discussion:
#
#    This routine is similar to VECTOR_CONSTRAINED_NEXT2,
#    VECTOR_CONSTRAINED_NEXT3, and VECTOR_CONSTRAINED_NEXT4.
#
#    We consider all vectors X of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_MAX(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      Q_MIN <= sum ( 1 <= I <= N ) ALPHA(I) * X(I) <= Q_MAX
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    ALPHA    4.0  3.0  5.0
#    Q_MIN   16.0
#    Q_MAX   20.0
#    X_MIN:   1   1   1
#    X_MAX:   5   6   4
#
#    #  X(1)  X(2)  X(3)     Total
#
#    1    2     1     1       20.0
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
#    Input, real ALPHA(N), the coefficient vector.
#
#    Input, integer X_MIN(N), X_MAX(N), the minimum and maximum
#    values allowed in each component.
#
#    Input, integer X(N), the output value of X from the previous call.
#    On first call, the user must set X = []
#
#    Input, real Q_MIN, Q_MAX, the lower and upper
#    limits on the sum.
#
#    Input, logical MORE, should be FALSE on the first call, and
#    TRUE thereafter.
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
      x[i] = x_min[i]

    total = 0.0
    for i in range ( 0, n ):
      total = total + alpha[i] * x[i]

    if ( q_min <= total and total <= q_max ):
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
      x[i] = x_min[i]

    total = 0.0
    for i in range ( 0, n ):
      total = total + alpha[i] * x[i]

    if ( q_min <= total and total <= q_max ):
      break

  return x, more

def vector_constrained_next6_test ( ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT6_TEST tests VECTOR_CONSTRAINED_NEXT6.
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
  print ( 'VECTOR_CONSTRAINED_NEXT6_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VECTOR_CONSTRAINED_NEXT6:' )
  print ( '  Consider vectors:' )
  print ( '    X_MIN(1:N) <= X(1:N) <= X_MAX(1:N),' )
  print ( '  Set' )
  print ( '    TOTAL = sum ( ALPHA(1:N) * X(1:N) )' )
  print ( '  Accept only vectors for which:' )
  print ( '    Q_MIN <= TOTAL <= Q_MAX' )

  for n in range ( 2, 4 ):

    if ( n == 2 ):
      alpha = np.array ( [ 4.0, 3.0 ] )
      x_min = np.array ( [ 1, 0 ] )
      x_max = np.array ( [ 2, 6 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False
    elif ( n == 3 ):
      alpha = np.array ( [ 4.0, 3.0, 5.0 ] )
      x_min = np.array ( [ 1, 0, 1 ] )
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
    print ( '  X_MIN:', end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x_min[i] ), end = '' )
    print ( '' )
    print ( '  X_MAX:', end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x_max[i] ), end = '' )
    print ( '' )
    print ( '' )

    rank = 0

    while ( True ):

      x, more = vector_constrained_next6 ( n, alpha, x_min, x_max, x, \
        q_min, q_max, more )

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
  print ( 'VECTOR_CONSTRAINED_NEXT6_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  vector_constrained_next6_test ( )
  timestamp ( )

