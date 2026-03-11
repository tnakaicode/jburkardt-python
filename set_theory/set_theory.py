#! /usr/bin/env python3
#
def set_theory_test ( ):

#*****************************************************************************80
#
## set_theory_test() tests set_theory().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'set_theory_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  set_theory() demonstrates some set theory operations.' )

  set_theory_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'set_theory_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def set_theory_test01 ( ):

#*****************************************************************************80
#
## set_theory_test01() demonstrates some set theory operations.
#
#  Discussion:
#
#    For most applications, I imagine it is enough to represent the sets
#    as numeric indices between 1 and N.  In this example, a universal
#    set U is defined as the integers from 1 to 50, a few subsets are
#    created, and set operations are carried out.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
#
#  Define a universal set U.
#
  print ( '' )
  print ( '  Let U be the "universal" set.' )
  U = set ( np.arange ( 1, 51 ) )
  print ( U )

  print ( '' )
  print ( '  len(U) counts the elements.' )
  print ( len ( U ) )
#
#  Define set A by an arithmetic property that elements of U
#  might have.  FIND will index those values (and, accidentally,
#  since U is the sequence 1:50, I and A will be identical.)
#
  print ( '' )
  print ( '  Find A: x in u with mod(x,5)=2.' )
  A = set()
  for x in U:
    if ( x % 5 == 2 ):
      A.add ( x )
  print ( A )
#
#  Define B by listing its elements.
#  These happen to be elements of U divisible by 3.
#
  print ( '' )
  print ( '  Define B as 3, 6, 9, 12, ..., 48.' )
  B = set ( [ 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48 ] )
  print ( B )
#
#  C is the complement of B with respect to the universal set U.
#
  print ( '' )
  print ( '  Define C as complement of B relative to U.' )
  C = U - B
  print ( C )
#
#  D is the intersection of A and B.
#
  print ( '' )
  print ( '  Define D is intersection of A and B.' )
  D = ( A & B )
  print ( D )
#
#  E is the union of A and B.
#
  print ( '' )
  print ( '  Define E is union of A and B.' )
  E = ( A | B )
  print ( E )
#
#  F is the symmetric difference of A and B.
#
  print ( '' )
  print ( '  Define F is symmetric difference of A and B.' )
  F = ( A ^ B )
  print ( F )
#
#  G is the complement of B with respect to A.
#  H is the complement of A with respect to B.
#
  print ( '' )
  print ( '  Define G is the complement of B with respect to A.' )
  print ( '         H is the complement of A with respect to B.' )
  G = A - B
  print ( G )

  H = B - A
  print ( H )
#
#  ISMEMBER checks if an element is in a set.
#
  print ( '' )
  print ( '  x in A reports whether x is a member of A' )
  print ( '' )

  for x in range ( 10, 21 ):
    if ( x in A ):
      print ( '  ', x, ' is a member of A.' )
    else:
      print ( '  ', x, ' is not a member of A.' )
#
#  <, <=, >, => are subset comparisons.
#
  print ( '' )
  print ( '  ( I < A ) reports whether I is a proper subset of A' )
  print ( '' )

  I = ( A & B )
  print ( I )

  if ( I < A ):
    print ( '  I is a proper subset of A.' )
  else:
    print ( '  I is not a proper subset of A.' )
#
#  To add an item.
#
  print ( '' )
  print ( '  J is set to numbers ending in 1.' )
  J = set ( [ 1, 11, 21, 31, 41 ] )
  print ( J )
  print ( '  J.add(x) adds an item to the set.' )
  x = 6
  J.add ( x )
  print ( J )
  print ( '  J.remove(x) removes an item from the set.' )
  x = 21
  J.remove ( x )
  print ( J )
#
#  pop selects an entry at random.
#
  print ( '' )
  print ( '  J.pop() returns an entry at random.' )

  for i in range ( 0, 5 ):
    print ( J.pop() )

  return

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
#    21 August 2019
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
  set_theory_test ( )
  timestamp ( )
