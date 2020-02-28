#! /usr/bin/env python
#
def dist_enum ( m, n ):

#*****************************************************************************80
#
## DIST_ENUM returns the number of distributions of indistinguishable objects.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of distinguishable "slots".
#
#    Input, integer N, the number of indistinguishable objects.
#
#    Output, integer DIST_NUM, the number of distributions of N
#    indistinguishable objects about M distinguishable slots.
#
  from i4_choose import i4_choose

  dist_num = i4_choose ( m + n - 1, n )

  return dist_num

def dist_enum_test ( ):

#*****************************************************************************80
#
## DIST_ENUM_TEST tests DIST_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DIST_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIST_ENUM enumerates distributions of N indistinguishable' )
  print ( '  objects among M distinguishable slots:' )
  print ( '' )
  print ( '      N:      0       1       2       3       4       5' )
  print ( '   M' )
  for m in range ( 0, 11 ):
    print ( '  %2d:  ' % ( m ), end = '' )
    for n in range ( 0, 6 ):
      print ( '  %5d' % ( dist_enum ( m, n ) ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIST_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dist_enum_test ( )
  timestamp ( )
 
