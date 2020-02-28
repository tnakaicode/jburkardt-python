#! /usr/bin/env python
#
def tableau_enum ( n ):

#*****************************************************************************80
#
## TABLEAU_ENUM enumerates tableaus on N nodes.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
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
#    Output, integer BALUE, the number of 2 by N standard tableaus.
#
  from i4_choose import i4_choose

  value = i4_choose ( 2 * n, n ) / ( n + 1 )

  return value

def tableau_enum_test ( ):

#*****************************************************************************80
#
## TABLEAU_ENUM_TEST tests TABLEAU_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TABLEAU_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TABLEAU_ENUM enumerates tableaus on N nodes.' )
  print ( '' )
  print ( '   N           #' )
  print ( '' )

  for n in range ( 0, 11 ):
    tableau_num = tableau_enum ( n )
    print ( '  %2d  %10d' % ( n, tableau_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TABLEAU_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tableau_enum_test ( )
  timestamp ( )
 
