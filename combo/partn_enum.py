#! /usr/bin/env python
#
def partn_enum ( n, nmax ):

#*****************************************************************************80
#
## PARTN_ENUM enumerates the partitions of N with maximum element NMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
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
#    Input, integer NMAX, the maximum element in the partition.
#    Normally, 1 <= NMAX <= N is required,
#    but for this routine any value of NMAX is allowed.
#
#    Output, integer NPARTITIONS is the number of partitions of N
#    with maximum element NMAX.
#
  from npart_table import npart_table

  if ( n <= 0 ):

    value = 0

  elif ( nmax <= 0 or n < nmax ):

    value = 0

  else:

    p = npart_table ( n, nmax )

    value = p[n,nmax]

  return value

def partn_enum_test ( ):

#*****************************************************************************80
#
## PARTN_ENUM_TEST tests PARTN_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PARTN_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARTN_ENUM enumerates partitions of N with maximum part NMAX.' )
  print ( '' )
  print ( '   NMAX:      1       2       3       4       5       6' )
  print ( '   N' )

  for n in range ( 0, 11 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for nmax in range ( 1, min ( n, 6 ) + 1 ):
      partn_num = partn_enum ( n, nmax )
      print ( '  %6d' % ( partn_num ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PARTN_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  partn_enum_test ( )
  timestamp ( )
 
