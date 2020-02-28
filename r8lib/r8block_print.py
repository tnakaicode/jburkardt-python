#! /usr/bin/env python
#
def r8block_print ( l, m, n, a, title ):

#*****************************************************************************80
#
## R8BLOCK_PRINT prints an R8BLOCK
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer L, M, N, the dimensions of the block.
#
#    Input, real A(L,M,N), the array to be printed.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( '%s' % ( title ) )

  for k in range ( 0, n ):

    print ( '' )
    print ( '  K = %d' % ( k ) )

    for jlo in range ( 0, m, 5 ):
      jhi = min ( jlo + 5, m )
      print ( '' )
      print ( '      ', end = '' )
      for j in range ( jlo, jhi ):
        print ( '       %7d' % ( j ), end = '' )
      print ( '' )
      print ( '' )
      for i in range ( 0, l ):
        print ( '%5d:' % ( i ), end = '' )
        for j in range ( jlo, jhi ):
          print ( '  %12g' % ( a[i,j,k] ), end = '' )
        print ( '' )

  return

def r8block_print_test ( ):

#*****************************************************************************80
#
## R8BLOCK_PRINT_TEST tests R8BLOCK_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  l = 4
  m = 3
  n = 2

  x = np.array ( [ \
        [  [  1.0,   2.0 ], [  1.0,  2.0 ], [  1.0,   2.0 ] ], \
        [  [  2.0,   4.0 ], [  4.0,  8.0 ], [  8.0,  16.0 ] ], \
        [  [  3.0,   6.0 ], [  9.0, 18.0 ], [ 27.0,  54.0 ] ], \
        [  [  4.0,   8.0 ], [ 16.0, 32.0 ], [ 64.0, 128.0 ] ] ] )

  print ( '' )
  print ( 'R8BLOCK_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8BLOCK_PRINT prints an R8BLOCK.' )

  r8block_print ( l, m, n, x, '  The 3D array:' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8block_print_test ( )
  timestamp ( )

