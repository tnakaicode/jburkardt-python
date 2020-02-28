#! /usr/bin/env python
#
def part_enum ( n ):

#*****************************************************************************80
#
## PART_ENUM enumerates the number of partitions of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the integer to be partitioned.
#    Normally N must be positive, but for this routine any
#    N is allowed.
#
#    Output, integer NPARTITIONS is the number of partitions of N.
#
  from part_table import part_table

  if ( n < 0 ):

    npartitions = 0

  else:

    p = part_table ( n )

    npartitions = p[n]

  return npartitions

def part_enum_test ( ):

#*****************************************************************************80
#
## PART_ENUM_TEST tests PART_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PART_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PART_ENUM enumerates partitions of N.' )
  print ( '' )
  print ( '   N     #' )
  print ( '' )

  for n in range ( 0, 11 ):
    part_num = part_enum ( n )
    print ( '  %2d  %6d' % ( n, part_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PART_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  part_enum_test ( )
  timestamp ( )
 
