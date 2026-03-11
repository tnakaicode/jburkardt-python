#! /usr/bin/env python3
#
def search_mpi ( a, b, c ):

#*****************************************************************************80
#
## search_mpi() searches for a solution to an integer equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the lower limit of the search.
#
#    integer B, the upper limit of the search.
#
#    integer C, the desired value.
#
#  Output:
#
#    integer J, is:
#    -1, if no solution could be found.
#    otherwise, F(J) = C and A <= J <= B.
#
  import numpy
  import sys
  from mpi4py import MPI

  comm = MPI.COMM_WORLD

  id = comm.Get_rank()

  p = comm.Get_size()

  if ( id == 0 ):
    print ( '' )
    print ( 'search_mpi():' )
    print ( '  Python/MPI version' )
    print ( '  Search the integers from A to B' )
    print ( '  for a value J such that F(J) = C.' )
    print ( '' )
    print ( '  Use MPI to divide the computation among', p, 'processes.' )
    print ( '' )
    print ( '  A        = ', a )
    print ( '  B        = ', b )
    print ( '  C        = ', c )
    wtime = MPI.Wtime ( )

  j = search_partial ( a, b, c, id, p )

  if ( j != -1 ):
    print ( '  Process ', id, ' found J = ', j )
    print ( '  Verify F(J) = ', f ( j ) )

  if ( id == 0 ):
    wtime = MPI.Wtime ( ) - wtime
    print ( '  Time     = ', wtime )

  return j

def search_mpi_test ( ):

#*****************************************************************************80
#
## search_mpi_test() tests search_mpi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'search_mpi_test:' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test search_mpi()' )

  search_mpi ( 1,               10000, 45 )
  search_mpi ( 1,              100000, 45 )
  search_mpi ( 1,             1000000, 45 )
  search_mpi ( 1674924000, 1674924999, 45 )
#
#  Terminate.
#
  print ( '' )
  print ( 'search_mpi_test:' )
  print ( '  Normal end of execution.' )
  return

def search_partial ( a, b, c, id, p ):

#*****************************************************************************80
#
## search_partial() searches 'partially' through [A,B] for a J so that F(J) = C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the search range.
#
#    integer C, the desired function value.
#
#    integer ID, the increment between successive values that
#    are to be checked.
#
#    integer P, the number of processes.
#
#  Output:
#
#    integer J, the computed solution, or -1
#    if no solution was found.
#
  for i in range ( a + id, b + 1, p ):

    if ( f ( i ) == c ):
      return i

  return ( - 1 )

def f ( i ):

#*****************************************************************************80
#
## f() is the function we are analyzing.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the argument.
#
#  Output:
#
#    integer VALUE, the value.
#
  i4_huge = 2147483647

  value = i

  for j in range ( 0, 5 ):

    k = ( value // 127773 )

    value = 16807 * ( value - k * 127773 ) - k * 2836

    if ( value <= 0 ):
      value = value + i4_huge

  return value

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  search_mpi_test ( )
  timestamp ( )

