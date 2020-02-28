#! /usr/bin/env python3
#
def polyomino_lp_write ( filename, label, m, n, a, b ):

#*****************************************************************************80
#
## POLYOMINO_LP_WRITE writes an LP file for the polyomino problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the output filename.
#
#    Input, string LABEL, the problem title.
#
#    Input, integer M, the number of equations
#
#    Input, integer N, the number of variables.
#
#    Input, integer A(M,N), the coefficients.
#
#    Input, integer B(M), the right hand sides.
#

#
#  Open the file.
#
  output = open ( filename, 'w' )

  output.write ( '%s\n' % ( label ) )
  output.write ( '\n' )
 
  output.write ( 'Maximize\n' )
  output.write ( '  Obj: 0\n' )

  output.write ( 'Subject to\n' )

  for i in range ( 0, m ):

    first = True

    for j in range ( 0, n ):

      if ( a[i,j] != 0 ):

        if ( a[i,j] < 0 ):
          output.write ( ' -' )
        elif ( not first ):
          output.write ( ' +' )

        if ( abs ( a[i,j] ) == 1 ):
          s = ' x%d' % j
          output.write ( s )
        else:
          s = ' %d x%d' % ( abs ( a[i,j] ), j )
          output.write ( s )

        first = False

    s = ' = %d\n' % ( b[i] )
    output.write ( s )

  output.write ( 'Binary\n' )
  output.write ( ' ' )
  for j in range ( 0, n ):
    s = ' x%d' % ( j )
    output.write ( s )
  output.write ( '\n' )

  output.write ( 'End\n' )
#
#  Close the file.
#
  output.close ( )

  return

def polyomino_lp_write_test ( ):

#*****************************************************************************80
#
## POLYOMINO_LP_WRITE_TEST tests POLYOMINO_LP_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'POLYOMINO_LP_WRITE_TEST:' )
  print ( '  Python version' )
  print ( '  POLYOMINO_LP_WRITE writes an LP file associated' )
  print ( '  with a binary programming problem for tiling a region' )
  print ( '  with copies of a single polyomino.' )
#
#  Get the coefficients and right hand side for the Reid system.
#
  a, b = polyomino_monohedral_example_reid_system ( )
#
#  Create the LP file.
#
  filename = 'reid.lp'
  label = '\ LP file for the Reid example.'
  shape = a.shape
  m = shape[0]
  n = shape[1]

  polyomino_lp_write ( filename, label, m, n, a, b )

  print ( '' )
  print ( '  POLYOMINO_LP_WRITE created the LP file "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYOMINO_LP_WRITE_TEST:' )
  print ( '  Normal end of execution.' )

  return

def polyomino_monohedral_example_reid_system ( ):

#*****************************************************************************80
#
## POLYOMINO_MONOHEDRAL_EXAMPLE_REID_SYSTEM sets up the Reid linear system.
#
#  Discussion:
#
#    This function sets up the linear system A*x=b associated with
#    the Reid polyomino tiling problem.
#
#    While it is desirable to have a general procedure that can automatically
#    deduce the linear system from the problem specification, for simplicity
#    in this example, we simply provide the linear system directly.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer A(9,10), the system matrix.
#
#    Output, integer B(9), the right hand side.
#
  import numpy as np

  a = np.array ( [ \
    [1,0,0,0,0,1,0,0,0,0], \
    [1,0,0,0,0,0,1,0,0,0], \
    [0,1,0,0,0,1,0,1,0,0], \
    [0,1,1,0,0,0,1,0,1,0], \
    [0,0,1,0,0,0,0,0,0,1], \
    [0,0,0,1,0,0,0,1,0,0], \
    [0,0,0,1,1,0,0,0,1,0], \
    [0,0,0,0,1,0,0,0,0,1], \
    [2,2,2,2,2,2,2,2,2,2] ] )

  b = np.array ( [ 1,1,1,1,1,1,1,1,8] )

  return a, b

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  polyomino_lp_write_test ( )
  timestamp ( )


