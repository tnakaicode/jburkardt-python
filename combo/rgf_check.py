#! /usr/bin/env python
#
def rgf_check ( m, f ):

#*****************************************************************************80
#
## RGF_CHECK checks a restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
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
#    from 1 to M.  M must be positive.
#
#    Input, integer F(M), the restricted growth function.
#
#    Output, bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( m <= 0 ):
    check = False
    return check

  fmax = 0
  for i in range ( 0, m ):
    if ( f[i] <= 0 or fmax + 1 < f[i] ):
      check = False
      return check
    fmax = max ( fmax, f[i] )

  return check

def rgf_check_test ( ):

#*****************************************************************************80
#
## RGF_CHECK_TEST tests RGF_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'RGF_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_CHECK checks a restricted growth function.' )
  
  for test in range ( 1, 5 ):

    if ( test == 1 ):
      m = -1
      f = np.array ( [] )
    elif ( test == 2 ):
      m = 7
      f = np.array ( [ 0, 1, 2, 3, 4, 5, 6 ] )
    elif ( test == 3 ):
      m = 7
      f = np.array ( [ 1, 3, 5, 8, 9, 10, 12 ] )
    elif ( test == 4 ):
      m = 7
      f = np.array ( [ 1, 2, 3, 1, 4, 5, 4 ] )

    check = rgf_check ( m, f )
    i4vec_transpose_print ( m, f, '  RGF:' )
    print ( '  Check = %s' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_check_test ( )
  timestamp ( )
