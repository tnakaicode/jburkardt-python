#! /usr/bin/env python
#
def sort_heap_external ( n, indx,isgn, i1, j1, k0, k1, n1 ):

#*****************************************************************************80
#
## SORT_HEAP_EXTERNAL externally sorts a list of items into ascending order.
#
#  Discussion:
#
#    The actual list of data is not passed to the routine.  Hence this
#    routine may be used to sort integers, reals, numbers, names,
#    dates, shoe sizes, and so on.  After each call, the routine asks
#    the user to compare or interchange two items, until a special
#    return value signals that the sorting is completed.
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
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf.
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of items to be sorted.
#
#    Input, integer INDX, the main communication signal.
#    The user must set INDX to 0 before the first call.
#    Thereafter, the user should set the input value of INDX
#    to the output value from the previous call.
#
#    Input, integer ISGN, results of comparison of elements I and J.
#    (Used only when the previous call returned INDX less than 0).
#    ISGN <= 0 means I is less than or equal to J
#    0 <= ISGN means I is greater than or equal to J.
#
#    Output, integer INDX, the main communication signal.
#    If INDX is
#
#      greater than 0, the user should:
#      * interchange items I and J
#      * call again.
#
#      less than 0, the user should:
#      * compare items I and J
#      * set ISGN = -1 if I < J, ISGN = +1 if J < I
#      * call again.
#
#      equal to 0, the sorting is done.
#
#    Output, integer I, J, the indices of two items.
#    On return with INDX positive, elements I and J should be interchanged.
#    On return with INDX negative, elements I and J should be compared, and
#    the result reported in ISGN on the next call.
#
#    Input/output, integer I1, J1, K0, K1, N1, variables that
#    are used for bookkeeping.  The user should declare them, and pass the
#    output values from one call as input values on the next call.  The user
#    should not change these variables.
#

#
#  INDX = 0: This is the first call.
#
  if ( indx == 0 ):
      
    k0 = ( n // 2 )
    k1 = ( n // 2 )
    n1 = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
  elif ( indx < 0 ):

    if ( indx == -2 ):

      if ( isgn < 0 ):
        i1 = i1 + 1

      j1 = k1
      k1 = i1
      indx = -1
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( 0 < isgn ):
      indx = 2
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( k0 <= 1 ):

      if ( n1 == 1 ):
        i1 = 0
        j1 = 0
        indx = 0
      else:
        i1 = n1
        n1 = n1 - 1
        j1 = 1
        indx = 1

      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    k0 = k0 - 1
    k1 = k0
#
#  0 < INDX, the user was asked to make an interchange.
#
  elif ( indx == 1 ):

    k1 = k0

  while ( True ):

    i1 = 2 * k1

    if ( i1 == n1 ):
      j1 = k1
      k1 = i1
      indx = -1
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1
    elif ( i1 < n1 ):
      j1 = i1 + 1
      indx = -2
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( k0 <= 1 ):
      break

    k0 = k0 - 1
    k1 = k0

  if ( n1 == 1 ):
    i1 = 0
    j1 = 0
    indx = 0
    i = i1 - 1
    j = j1 - 1
  else:
    i1 = n1
    n1 = n1 - 1
    j1 = 1
    indx = 1
    i = i1 - 1
    j = j1 - 1

  return indx, i, j, i1, j1, k0, k1, n1

def sort_heap_external_test ( ):

#*****************************************************************************80
#
## SORT_HEAP_EXTERNAL_TEST tests SORT_HEAP_EXTERNAL.
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
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 20

  print (  '' )
  print (  'SORT_HEAP_EXTERNAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print (  '  SORT_HEAP_EXTERNAL sorts objects externally.' )

  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, 1, n, seed )

  i4vec_print ( n, a, '  Unsorted array:' )

  indx = 0
  isgn = 0
  i1 = 0
  j1 = 0
  k0 = 0
  k1 = 0
  n1 = 0

  while ( True ):

    indx, i, j, i1, j1, k0, k1, n1 = sort_heap_external ( n, indx, \
      isgn, i1, j1, k0, k1, n1 )

    if ( indx < 0 ):
      isgn = 1
      if ( a[i] <= a[j] ):
        isgn = -1
    elif ( 0 < indx ):
      t    = a[i]
      a[i] = a[j]
      a[j] = t
    else:
      break

  i4vec_print ( n, a, '  Sorted array:' )
#
#  Terminate.
#
  print (  '' )
  print (  'SORT_HEAP_EXTERNAL_TEST:' )
  print (  '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sort_heap_external_test ( )
  timestamp ( )

