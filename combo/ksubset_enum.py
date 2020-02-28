#! /usr/bin/env python
#
def ksubset_enum ( k, n ):

#*****************************************************************************80
#
## KSUBSET_ENUM enumerates the K element subsets of an N set.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the number of elements each K subset must
#    have. 0 <= K <= N.
#
#    Input, integer N, the number of elements in the master set.
#    0 <= N.
#
#    Output, integer NKSUB, the number of distinct elements.
#
  from i4_choose import i4_choose

  nksub = i4_choose ( n, k )

  return nksub

def ksubset_enum_test ( ):

#*****************************************************************************80
#
## KSUBSET_ENUM_TEST tests KSUBSET_COLEX_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUBSET_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_ENUM enumerates K-subsets of an N set.' )
#
#  Enumerate.
#
  print ( '' )
  print ( '      K:   0    1    2    3    4    5' )
  print ( '   N' )
  print ( '' )
  for n in range ( 0, 6 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      nksub = ksubset_enum ( k, n )
      print ( '  %2d' % ( nksub ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_enum_test ( )
  timestamp ( )

