#! /usr/bin/env python
#
def perm_enum ( n ):

#*****************************************************************************80
#
## PERM_ENUM enumerates the permutations on N digits.
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
#    Input, integer N, the number of values being permuted.
#    N must be nonnegative.
#
#    Output, integer NPERM, the number of distinct elements.
#
  from i4_factorial import i4_factorial

  nperm = i4_factorial ( n );

  return nperm

def perm_enum_test ( ):

#*****************************************************************************80
#
## PERM_ENUM_TEST tests PERM_ENUM.
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
  print ( 'PERM_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_ENUM enumerates permutations of N items.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    perm_num = perm_enum ( n )
    print ( '  %2d  %6d' % ( n, perm_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_enum_test ( )
  timestamp ( )
 
