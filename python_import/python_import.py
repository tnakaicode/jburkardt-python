#! /usr/bin/env python3
#
def python_import_test ( ):

#*****************************************************************************80
#
## python_import_test() tests importing a "remote" Python library.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
#
#  The following commands allow us to access information in another
#  directory, using commands like
#    from test_partial_digest import test_partial_digest
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_partial_digest' )

  from test_partial_digest import test_partial_digest

  print ( '' )
  print ( 'python_import_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  This program demonstrates how a Python function can' )
  print ( '  import information from a Python library that is' )
  print ( '  in another directory.' )
  print ( '' )
  print ( '  Here, we want to request a sample problem from the' )
  print ( '  library "test_partial_digest.py", which is in another' )
  print ( '  directory, and then apply partial_digest_recur().' )
  print ( '' )
  print ( '  partial_digest_recur() generates solutions to the partial' )
  print ( '  digest problem, using recursion.' )
  print ( '  test_partial_digest() creates test problems for the' )
  print ( '  partial digest problem.' )
#
#  Request a sample problem from the test_partial_digest library.
#
  k = 6
  dmax = 20

  print ( '' )
  print ( '  Number of nodes = %d' % ( k ) )
  print ( '  Maximum distance = %d' % ( dmax ) )

  locate, d = test_partial_digest ( k, dmax )
#
#  Sort the data.
#
  locate = np.sort ( locate )
  d = np.sort ( d )
#
#  Print the data.
#
  i4vec_print ( k, locate, '  Locations:' )
  i4vec_print ( k * ( k - 1 ) // 2, d, '  Distances:' )
#
#  Solve the problem.
#
  partial_digest_recur ( k, d )
#
#  Terminate.
#
  print ( '' )
  print ( 'python_import_test():' )
  print ( '  Normal end of execution.' )
  return

def find_distances ( l_length, l, x_length, x, y ):

#*****************************************************************************80
#
## find_distances() determines if the "free" distances include every ||X(I)-Y||.
#
#  Discussion:
#
#    This routine is given a candidate point Y, a set of placed points
#    X(1:X_LENGTH), and a list of unused or "free" distances in
#    L(1:L_LENGTH).  The routine seeks to find in L a copy of the
#    distance from Y to each X.
#
#    If so, then the L array is reordered so that entries
#    L(L_LENGTH-X_LENGTH+1:L_LENGTH) contain theses distances.
#
#    In other words, Y can be added into X, and L_LENGTH reduced to
#    L_LENGTH-X_LENGTH.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_LENGTH, the length of the array.
#
#    Input/integer L(L_LENGTH), the array.  On output,
#    some entries have been shuffled.  In particular, if SUCCESS is TRUE,
#    the entries L(L_LENGTH-X_LENGTH+1:L_LENGTH) contain the distances
#    of X(1:X_LENGTH) to Y.
#
#    integer X_LENGTH, the number of entries in X.
#
#    integer X(X_LENGTH), the number of points
#    already accepted.
#
#    integer Y, a new point that we are considering.
#
#  Output:
#
#    logical SUCCESS, is TRUE if the entries of L included
#    the values of the distance of Y to each entry of X.
#
  l2_length = l_length

  for i in range ( 0, x_length ):

    d = abs ( x[i] - y )

    success = False

    for j in range ( 0, l2_length ):

      if ( l[j] == d ):
        l[j] = l[l2_length-1]
        l[l2_length-1] = d
        l2_length = l2_length - 1
        success = True
        break

    if ( not success ):
      return success, l

  success = True

  return success, l

def i4vec_max_last ( l_length, l ):

#*****************************************************************************80
#
## i4vec_max_last() moves the maximum entry of an I4VEC to the last position.
#
#  Discussion:
#
#    This routine finds the largest entry in an array and moves
#    it to the end of the array.
#
#    If we ignore this last array entry, then the effect is the same
#    as "deleting" the maximum entry from the array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_LENGTH, the length of the array.
#
#    integer L(L_LENGTH), the array.
#
#  Output:
#
#    integer VALUE, the maximum entry in the
#    input array.
#
#    integer L(L_LENGTH), the maximum entry has been shifted to the end.
#
  for i in range ( 1, l_length ):
    if ( l[i] < l[i-1] ):
      t = l[i]
      l[i] = l[i-1]
      l[i-1] = t
 
  value = l[l_length-1];

  return l, value

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def partial_digest_recur ( n, l ):

#*****************************************************************************80
#
## partial_digest_recur() uses recursion on the partial digest problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer N, the number of nodes.
#
#    integer L((N*(N-1))/2), the distances between all pairs
#    of distinct nodes.
#
  import numpy as np
#
#  How long is L?
#
  l_length = ( n * ( n - 1 ) ) // 2
#
#  Find WIDTH, the largest element of L, and move it to the last position.
#
  l, width = i4vec_max_last ( l_length, l )
#
#  Think of L as being 1 entry shorter.
#
  l_length = l_length - 1
#
#  Using WIDTH, set the first two entries of X.
#
  x = np.zeros ( n )
  x[0] = 0
  x[1] = width
  x_length = 2
#
#  Begin recursive operation.
#
  l_length, l, x_length, x = place ( l_length, l, x_length, x )

  return

def place ( l_length, l, x_length, x ):

#*****************************************************************************80
#
## place() tries to place the next point for the partial digest problem.
#
#  Discussion:
#
#    Note that this is a recursive function.  A solution to the
#    partial digest problem is sought by calling this routine repeatedly.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_LENGTH, the number of entries in L.
#
#    integer L(L_LENGTH), the array of distances.
#
#    integer X_LENGTH, the number of entries in X.
#
#    integer X(X_LENGTH), the current partial solution.
#
#  Output:
#
#    integer L_LENGTH, the updated number of entries in L.
#
#    integer L(L_LENGTH), the update array of distances.
#
#    integer X_LENGTH, the updated number of entries in X.
#
#    integer X(X_LENGTH), the updated partial solution.
#

#
#  Are we done?
#
  if ( l_length <= 0 ):
    i4vec_print ( x_length, x, '  Solution:' )
    return l_length, l, x_length, x
#
#  Find the maximum remaining distance.
#
  l, y = i4vec_max_last ( l_length, l )
#
#  We can add a point at Y if L contains all the distances from Y to
#  the current X's.
#
  success, l = find_distances ( l_length, l, x_length, x, y )

  if ( success ):
    l_length2 = l_length - x_length
    x_length = x_length + 1
    x[x_length-1] = y
    l_length2, l, x_length, x = place ( l_length2, l, x_length, x )
    x_length = x_length - 1
#
#  We must also consider the case where Y represents the distance
#  to X[1], not X[0].
#
  y = x[1] - y

  success, l = find_distances ( l_length, l, x_length, x, y )

  if ( success ):
    l_length2 = l_length - x_length
    x_length = x_length + 1
    x[x_length-1] = y
    l_length2, l, x_length, x = place ( l_length2, l, x_length, x )
    x_length = x_length - 1

  return l_length, l, x_length, x

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  python_import_test ( )
  timestamp ( )
 
