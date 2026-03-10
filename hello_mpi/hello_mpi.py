#! /usr/bin/env python3
#
def hello_mpi ( ):

#*****************************************************************************80
#
## hello_mpi() is a simple 'Hello, world!' test of MPI4PY.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
  import sys
  from mpi4py import MPI

  comm = MPI.COMM_WORLD

  id = comm.Get_rank()

  p = comm.Get_size()

  if ( id == 0 ):
    print ( '' )
    print ( 'hello_mpi():' )
    print ( '  P', id, ':  There are ', p, ' MPI processes running.' )

  print ( '  P', id, ':  Hello, world!' )

  return

if ( __name__ == '__main__' ):
  hello_mpi ( )

