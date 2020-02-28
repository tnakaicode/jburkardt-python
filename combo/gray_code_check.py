#! /usr/bin/env python
#
def gray_code_check ( n, t ):

#*****************************************************************************80
#
## GRAY_CODE_CHECK checks a Gray code element.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of digits in each element.
#    N must be positive.
#
#    Input, integer T(N), an element of the Gray code.
#    Each entry T(I) is either 0 or 1.
#
#    Output, bool CHECK, error flag.
#    True, T represents a Gray code.
#    False, T does not represent a Gray code.
#
  check = True

  if ( n < 1 ):
    check = False
    return check

  for i in range ( 0, n ):

    if ( t[i] != 0 and t[i] != 1 ):
      check = False
      return check

  return check

def gray_code_check_test ( ):

#*****************************************************************************80
#
## GRAY_CODE_CHECK_TEST tests GRAY_CODE_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'GRAY_CODE_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRAY_CODE_CHECK checks N and T(1:N).' )
  print ( '' )
  print ( '  Check?      N    T(1:N)' )
  print ( '' )
  
  for test in range ( 1, 4 ):

    n = 5

    if ( test == 1 ):
      t = np.array ( [ 0, 1, 1, 0, 1 ] )
    elif ( test == 2 ):
      t = np.array ( [ 1, 0, 7, 1, 0 ] )
    elif ( test == 3 ):
      t = np.array ( [ 1, 1, 1, 1, 1 ] )

    check = gray_code_check ( n, t )
    print ( '      %5s  %2d:  ' % ( check, n ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( t[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRAY_CODE_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_code_check_test ( )
  timestamp ( )

