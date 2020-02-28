#! /usr/bin/env python
#
def setpart_enum ( m ):

#*****************************************************************************80
#
## SETPART_ENUM enumerates the partitions of a set of M elements.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2011
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
#    Input, integer M, the number of elements in the set.
#    M must be positive.  However, for the enumeration routine only,
#    it is legal to call with any value of M.
#
#    Output, integer NPART, the number of partitions of the set.
#
  import numpy as np
  from i4_choose import i4_choose

  if ( m < 0 ):

    npart = 0

  elif ( m == 0 ):

    npart = 1

  else:

    b = np.zeros ( m + 1 )

    b[0] = 1
    for j in range ( 1, m + 1 ):
      b[j] = 0
      for i in range ( 0, j ):
        b[j] = b[j] + i4_choose ( j - 1, i ) * b[i]

    npart = b[m]

  return npart

def setpart_enum_test ( ):

#*****************************************************************************80
#
## SETPART_ENUM_TEST tests SETPART_ENUM.
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
  print ( 'SETPART_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SETPART_ENUM enumerates set partitions.' )
  print ( '' )
#
#  Enumerate.
#
  for n in range ( 1, 7 ):
    npart = setpart_enum ( n )
    print ( '  %4d  %4d' % ( n, npart ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SETPART_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  setpart_enum_test ( )
  timestamp ( )
 
