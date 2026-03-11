#! /usr/bin/env python3
#
def jaccard_distance_test ( ):

#*****************************************************************************80
#
## jaccard_distance_test() tests jaccard_distance().
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
  print ( 'jaccard_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  jaccard_distance() computes the jaccard distance' )
  print ( '  between two sets.' )

  A = set ( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )
  B = set ( [ 'a', 'l', 'i', 'g', 't', 'o', 'r' ] )
  d = jaccard_distance ( A, B )
  print ( '' )
  print ( '  A:', end = '' )
  print ( A )
  print ( '  B:', end = '' )
  print ( B )
  print ( '  Computed distance = ', d )
#
#  Repeated elements are ignored.
#
  A = set ( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )
  B = set ( [ 'a', 'l', 'l', 'i', 'g', 'a', 't', 'o', 'r' ] )
  d = jaccard_distance ( A, B )
  print ( '' )
  print ( '  A:', end = '' )
  print ( A )
  print ( '  B:', end = '' )
  print ( B )
  print ( '  Computed distance = ', d )
#
#  No intersection.
#
  A = set ( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )
  B = set ( [ 'c', 'r', 'w', 't', 'h' ] )
  d = jaccard_distance ( A, B )
  print ( '' )
  print ( '  A:', end = '' )
  print ( A )
  print ( '  B:', end = '' )
  print ( B )
  print ( '  Computed distance = ', d )
#
#  Can specify sets as strings.
#
  A = set ( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )
  B = set ( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )
  d = jaccard_distance ( A, B )
  print ( '' )
  print ( '  A:', end = '' )
  print ( A )
  print ( '  B:', end = '' )
  print ( B )
  print ( '  Computed distance = ', d )
#
#  Can specify sets as strings.
#
  A = set ( [ 'a', 'e', 'i', 'o', 'u', 'y' ] )
  B = set ( [ 'a', 'd', 'i', 'e', 'u' ] )
  d = jaccard_distance ( A, B )
  print ( '' )
  print ( '  A:', end = '' )
  print ( A )
  print ( '  B:', end = '' )
  print ( B )
  print ( '  Computed distance = ', d )
#
#  Terminate.
#
  print ( '' )
  print ( 'jaccard_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def jaccard_distance ( A, B ):

#*****************************************************************************80
#
## jaccard_distance() computes the Jaccard distance between two sets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Jaccard index and jazz albums,
#    https://www.johndcook.com/blog/2023/07/26/jaccard-jazz/
#    Posted 26 July 2023.
#
#  Input:
#
#    set A(*), B(*): two sets.
#
#  Output:
#
#    real d: the Jaccard distance between the sets.
#
  d = 1.0 - jaccard_index ( A, B )

  return d

def jaccard_index ( A, B ):

#*****************************************************************************80
#
## jaccard_index() computes the Jaccard index of two sets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Jaccard index and jazz albums,
#    https://www.johndcook.com/blog/2023/07/26/jaccard-jazz/
#    Posted 26 July 2023.
#
#  Input:
#
#    set A(*), B(*): two sets.
#
#  Output:
#
#    real j: the Jaccard index of the two sets.
#
  j = len ( A & B ) / len ( A | B )

  return j

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
  jaccard_distance_test ( )
  timestamp ( )

