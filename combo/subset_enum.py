#! /usr/bin/env python
#
def subset_enum ( n ):

#*****************************************************************************80
#
## SUBSET_ENUM enumerates the subsets of a set with N elements.
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
#  Parameters:
#
#    Input, integer N, the number of elements in the set.
#    N must be at least 0.
#
#    Output, integer NSUB, the number of distinct elements.
#
  nsub = 2 ** n

  return nsub

def subset_enum_test ( ):

#*****************************************************************************80
#
## SUBSET_ENUM_TEST tests SUBSET_ENUM.
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
  print ( 'SUBSET_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_ENUM enumerates subsets of a set of N items.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    subset_num = subset_enum ( n )
    print ( '  %2d  %6d' % ( n, subset_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_enum_test ( )
  timestamp ( )
 
