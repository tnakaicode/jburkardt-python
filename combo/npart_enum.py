#! /usr/bin/env python
#
def npart_enum ( n, npart ):

#*****************************************************************************80
#
## NPART_ENUM enumerates the number of partitions of N with NPART parts.
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
#    Input, integer NPART, the number of parts of the partition.
#    Normally, 1 <= NPART <= N is required,
#    but for this routine any value of NPART is allowed.
#
#    Output, integer NPARTITIONS is the number of partitions of N
#    with NPART parts.
#
  from npart_table import npart_table

  if ( n <= 0 ):

    npartitions = 0

  elif ( npart <= 0 or n < npart ):

    npartitions = 0

  else:

    p = npart_table ( n, npart )

    npartitions = p[n,npart]

  return npartitions

def npart_enum_test ( ):

#*****************************************************************************80
#
## NPART_ENUM_TEST tests NPART_ENUM.
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
  print ( 'NPART_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_ENUM enumerates partitions of N into PART_NUM parts.' )
  print ( '' )
  print ( '   PART_NUM:  1       2       3       4       5       6' )
  print ( '   N' )
  for n in range ( 0, 11 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for part_num in range ( 1, min ( n, 6 ) + 1 ):
      npart_num = npart_enum ( n, part_num )
      print ( '  %6d' % ( npart_num ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_enum_test ( )
  timestamp ( )
 
