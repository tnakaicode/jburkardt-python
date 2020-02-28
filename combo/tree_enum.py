#! /usr/bin/env python
#
def tree_enum ( n ):

#*****************************************************************************80
#
## TREE_ENUM enumerates the trees on N nodes.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of nodes in each tree.
#    N must normally be at least 3, but for this routine,
#    any value of N is allowed.
#
#    Output, integer NTREE, the number of distinct elements.
#
  if ( n < 1 ):
    ntree = 0
  elif ( n == 1 ):
    ntree = 1
  elif ( n == 2 ):
    ntree = 1
  else:
    ntree = n ** ( n - 2 )

  return ntree

def tree_enum_test ( ):

#*****************************************************************************80
#
## TREE_ENUM_TEST tests TREE_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TREE_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TREE_ENUM enumerates trees on N nodes.' )
  print ( '' )
  print ( '   N           #' )
  print ( '' )

  for n in range ( 0, 11 ):
    tree_num = tree_enum ( n )
    print ( '  %2d  %10d' % ( n, tree_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TREE_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tree_enum_test ( )
  timestamp ( )
 
