#! /usr/bin/env python
#
def pruefer_enum ( n ):

#*****************************************************************************80
#
## PRUEFER_ENUM enumerates the Pruefer codes on N-2 digits.
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
#  Parameters:
#
#    Input, integer N, the number of digits in the code, plus 2.
#    N must be at least 3.
#
#    Output, integer NCODE, the number of distinct elements.
#
  if ( n < 3 ):
    ncode = 1
  else:
    ncode = n ** ( n - 2 )

  return ncode

def pruefer_enum_test ( ):

#*****************************************************************************80
#
## PRUEFER_ENUM_TEST tests PRUEFER_ENUM.
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
  print ( 'PRUEFER_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PRUEFER_ENUM enumerates trees on N nodes, using the Pruefer code' )
  print ( '' )
  print ( '   N           #' )
  print ( '' )

  for n in range ( 0, 11 ):
    pruefer_num = pruefer_enum ( n )
    print ( '  %2d  %10d' % ( n, pruefer_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRUEFER_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pruefer_enum_test ( )
  timestamp ( )
 
