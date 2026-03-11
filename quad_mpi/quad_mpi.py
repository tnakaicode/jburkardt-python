#! /usr/bin/env python3
#
def quad_mpi ( ):

#*****************************************************************************80
#
## quad_mpi() estimates an integral using a quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2011
#
#  Author:
#
#    John Burkardt
#
  from mpi4py import MPI
  import numpy as np
  import platform
  import sys
 
  comm = MPI.COMM_WORLD

  id = comm.Get_rank()

  p = comm.Get_size()

  a =  0.0
  b = 10.0
  exact = 0.49936338107645674464
#
#  Assume process 0 decides on the value of N, and sends it to others.
#
  if id == 0:
    n = np.array ( 10000, dtype = 'i' )
    wtime = MPI.Wtime ( )
    print ( '' )
    print ( 'quad_mpi():' )
    print ( '  python version: ' + platform.python_version ( ) )
    print ( '  numpy version:  ' + np.version.version )
    print ( '  Estimate an integral of f(x) from A to B.' )
    print ( '  f(x) = 50 / (pi * ( 2500 * x * x + 1 ) )' )
    print ( '' )
    print ( '  A        = ', a )
    print ( '  B        = ', b )
    print ( '  N        = ', n )
    print ( '  Exact    = ', exact )
    print ( '' )
    print ( '  Use MPI to divide the computation among' )
    print ( '  multiple processes.' )
  else:
    n = np.array ( 0, dtype = 'i' )

  comm.Bcast ( [ n, MPI.INT ], root = 0 )

  t = np.array ( 0.0, dtype = 'd' )

  for i in range ( id, n, p ):
    x = ( float ( n - i - 1 ) * a + float ( i ) * b ) / float ( n - 1 )
    t = t + f ( x )

  print ( '  Sum for process ', id, ' is ', t )
 
  total = np.array ( 0.0, dtype = 'd' )

  comm.Reduce ( [ t, MPI.DOUBLE ], [ total, MPI.DOUBLE ], op = MPI.SUM, root = 0 )

  if id == 0:
    wtime = MPI.Wtime ( ) - wtime

    total = ( b - a ) * total / float ( n )
    error = np.abs ( total - exact )
 
    print ( '' )
    print ( '  Estimate = ', total )
    print ( '  Error    = ', error )
    print ( '  Time     = ', wtime )
#
#  Terminate.
#
  print ( '' )
  print ( 'quad_mpi():' )
  print ( '  Normal end of execution.' )
  return

def f ( x ):

#*****************************************************************************80
#
## f() evaluates the function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = 50.0 / ( np.pi * ( 2500.0 * x * x + 1.0 ) );

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
  quad_mpi ( )
  timestamp ( )

