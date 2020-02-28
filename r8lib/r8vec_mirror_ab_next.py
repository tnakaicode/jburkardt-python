#! /usr/bin/env python
#
def r8vec_mirror_ab_next ( m, a, b, x, done ):

#*****************************************************************************80
#
## R8VEC_MIRROR_AB_NEXT steps through "mirrored" versions of vector X.
#
#  Discussion:
#
#    X is an M component vector contained in a rectangle described by A and B,
#    that is, for each index I, we have
#      A(I) <= X(I) <= B(I).
#
#    "Mirrored" versions of the vector X have one or more components
#    reflected about the A or B limit.  
#
#    As long as each component of X is strictly between the limits A and B,
#    this means there will be 3^M possible versions of the vector.
#
#    If one component of X is equal to one limit or the other, this 
#    suppresses mirroring across that limit.  If one component of
#    X, A and B are equal, then no mirroring is done at all in that component.
# 
#  Example:
#
#      A = 0, 0, 0
#      X = 1, 1, 1
#      B = 2, 2, 2
#      results in the following sequence of 3x3x3 values:
#
#      0  0  0
#      0  0  1
#      0  0  2
#      0  1  0
#      0  1  1
#      .......
#      2  1  1
#      2  1  2
#      2  2  0
#      2  2  1
#      2  2  2
#
#    A = 0 1 0
#    X = 1 1 1
#    B = 2 2 2
#    results in the following sequence of 3x2x3 values:
#
#      0 1 0
#      0 1 1
#      0 1 2
#      0 2 0
#      0 2 1
#      0 2 2
#      1 1 0
#      1 1 1
#      1 1 2
#      1 2 0
#      1 2 1
#      1 2 2
#      2 1 0
#      2 1 1
#      2 1 2
#      2 2 0
#      2 2 1
#      2 2 2
#
#    A = 0 1 0
#    X = 1 1 1
#    B = 2 1 2
#    results in the following sequence of 3x1x3 values:
#
#      0 1 0
#      0 1 1
#      0 1 2
#      1 1 0
#      1 1 1
#      1 1 2
#      2 1 0
#      2 1 1
#      2 1 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of entries in the vector.
#
#    Input, real A(M), B(M), the lower and upper limits.
#
#    Input/output, real X(M), a vector being manipulated.
#
#    Input/output, logical DONE.  On first call, DONE should be TRUE, and
#    A(I) <= X(I) <= B(I) for each index I.  On output, if DONE is TRUE,
#    then the returned value is the last entry in the sequence.
#

#
#  First call:
#
  if ( done ):
#
#  Ensure all A(I) <= X(I) <= B(I).
#
    for i in range ( 0, m ):

      if ( x[i] < a[i] ):
        print ( '' )
        print ( 'R8VEC_MIRROR_AB_NEXT - Fatal error!' )
        print ( '  Not every A(I) <= X(I).' )
        exit ( 'R8VEC_MIRROR_AB_NEXT - Fatal error!' )

      if ( b[i] < x[i] ):
        print ( '' )
        print ( 'R8VEC_MIRROR_AB_NEXT - Fatal error!' )
        print ( '  Not every X(I) <= B(I).' )
        exit ( 'R8VEC_MIRROR_AB_NEXT - Fatal error!' )
#
#  Set first element of sequence.
#
    x[0:m] = 2.0 * a[0:m] - x[0:m]
#
#  Unless A = B, our sequence is not done.
#
    done = True
    for i in range ( 0, m ):
      if ( a[i] != b[i] ):
        done = False
        break
#
#  Subsequent calls.
#
  else:
#
#  Initialize index to last.
#  loop
#    if index < 1, set DONE = true and return.
#    if the index-th value is below B, increment it and return
#    otherwise reset index-th value to A.
#    decrement the index.
#
    i = m - 1

    while ( 0 <= i ):

      if ( x[i] < a[i] ):
        x[i] = 2.0 * a[i] - x[i]
        return x, done
      elif ( x[i] < b[i] ):
        x[i] = 2.0 * b[i] - x[i]
        return x, done
      else:
        x[i] = x[i] - 2.0 * ( b[i] - a[i] )

      i = i - 1

    done = True

  return x, done

def r8vec_mirror_ab_next_test ( ):

#*****************************************************************************80
#
## R8VEC_MIRROR_AB_NEXT_TEST tests R8VEC_MIRROR_AB_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  m = 3

  print ( '' )
  print ( 'R8VEC_MIRROR_AB_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MIRROR_AB_NEXT generates all versions of' )
  print ( '  of a real vector X mirrored by A and B.' )

  a = np.array ( [ -0.5, -0.5, -0.5 ] )
  x = np.array ( [  0.0,  0.0,  0.0 ] )
  b = np.array ( [  0.5,  0.5,  0.5 ] )

  print ( '' )
  print ( '  Case 1: 3x3x3 possibilities:'  )
  print ( '' )

  r8vec_transpose_print ( m, a, '   A:' )
  r8vec_transpose_print ( m, x, '   X:' )
  r8vec_transpose_print ( m, b, '   B:' )

  print ( '' )

  i = 0
  done = True

  while ( True ):

    x, done = r8vec_mirror_ab_next ( m, a, b, x, done )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

    i = i + 1
    s = str ( i )

    r8vec_transpose_print ( m, x, s )

  a = np.array ( [ -0.5, -0.5, -0.5 ] )
  x = np.array ( [  0.0,  0.5,  0.0 ] )
  b = np.array ( [  0.5,  0.5,  0.5 ] )

  print ( '' )
  print ( '  Case 2: 3x2x3 possibilities:'  )
  print ( '' )

  r8vec_transpose_print ( m, a, '   A:' )
  r8vec_transpose_print ( m, x, '   X:' )
  r8vec_transpose_print ( m, b, '   B:' )

  print ( '' )

  i = 0
  done = True

  while ( True ):

    x, done = r8vec_mirror_ab_next ( m, a, b, x, done )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

    i = i + 1
    s = str ( i )

    r8vec_transpose_print ( m, x, s )

  a = np.array ( [  0.0, -0.5, -0.5 ] )
  x = np.array ( [  0.0,  0.0,  0.0 ] )
  b = np.array ( [  0.0,  0.5,  0.5 ] )

  print ( '' )
  print ( '  Case 3: 1x3x3 possibilities:'  )
  print ( '' )

  r8vec_transpose_print ( m, a, '   A:' )
  r8vec_transpose_print ( m, x, '   X:' )
  r8vec_transpose_print ( m, b, '   B:' )

  print ( '' )

  i = 0
  done = True

  while ( True ):

    x, done = r8vec_mirror_ab_next ( m, a, b, x, done )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

    i = i + 1
    s = str ( i )

    r8vec_transpose_print ( m, x, s )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MIRROR_AB_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_mirror_ab_next_test ( )
  timestamp ( )

