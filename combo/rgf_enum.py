#! /usr/bin/env python
#
def rgf_enum ( m ):

#*****************************************************************************80
#
## RGF_ENUM enumerates the restricted growth functions on M.
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
#    Input, integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.  However, for the enumeration routine
#    only, it is legal to call with any value of M.
#
#    Output, integer VALUE, the number of restricted growth
#    functions.
#
  import numpy as np
  from i4_choose import i4_choose

  if ( m < 0 ):

    value = 0

  elif ( m == 0 ):

    value = 1

  else:

    b = np.zeros ( m + 1 )
    b[0] = 1
    for j in range ( 1, m + 1 ):
      for i in range ( 0, j ):
        b[j] = b[j] + i4_choose ( j - 1, i ) * b[i]

    value = b[m]

  return value

def rgf_enum_test ( ):

#*****************************************************************************80
#
## RGF_ENUM_TEST tests RGF_ENUM.
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
  print ( 'RGF_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_ENUM enumerates restricted growth functions.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    rgf_num = rgf_enum ( n )
    print ( '  %2d  %6d' % ( n, rgf_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_enum_test ( )
  timestamp ( )
