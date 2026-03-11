#! /usr/bin/env python3
#
def sortrows_test ( ):

#*****************************************************************************80
#
## sortrows_test() tests sortrows().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'sortrows_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  sortrows() lexically sorts the rows of an array.' )
  print ( '' )
  x = rng.integers ( low = 1, high = 10, size = [ 10, 3 ], endpoint = True )
  print ( '' )
  print ( '  Initial array:' )
  print ( x )

  x = sortrows ( x )

  print ( '' )
  print ( '  Array after sortrows() was applied:' )
  print ( x )
#
#  Terminate.
#
  print ( '' )
  print ( 'sortrows_test():' )
  print ( '  Normal end of execution.' )
  return

def sortrows ( x ):

#*****************************************************************************80
#
## sortrows() lexically sorts the rows of an array.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    array x[]: the array to be sorted.
#
#  Output:
#
#    array x[]: the sorted array.
#
  import numpy as np

  x = x[ np.lexsort ( x.T[::-1] ) ]

  return x

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
  sortrows_test ( )
  timestamp ( )

