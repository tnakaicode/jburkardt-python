#! /usr/bin/env python3
#
def collatz_path ( n ):

#*****************************************************************************80
#
## COLLATZ_PATH uses recursion to print the path of a Collatz sequence.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the current member of the path.
#
  from sys import exit
  
  print ( '  %d' % ( n ) )

  if ( n < 1 ):

    print ( '' )
    print ( 'COLLATZ_PATH - Fatal error!' )
    print ( '  Path member N = %d is not positive.' % ( n ) )
    exit ( 'COLLATZ_PATH - Fatal error!' )

  elif ( n == 1 ):
    pass
  elif ( ( n % 2 ) == 0 ):
    collatz_path ( int ( n / 2 ) )
  else:
    collatz_path ( 3 * n + 1 )

  return

def collatz_path_test ( ):

#*****************************************************************************80
#
## COLLATZ_PATH_TEST tests COLLATZ_PATH
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'COLLATZ_PATH_TEST' )
  print ( '  COLLATZ_PATH prints the members of a Collatz path.' )

  for n in [ 7, 8, 9, 10, 600 ]:
    print ( '' )
    print ( '  %d is the starting point.' % ( n ) )
    collatz_path ( n )

  return

def collatz_recursive_test ( ):

#*****************************************************************************80
#
## COLLATZ_RECURSIVE_TEST tests the COLLATZ_RECURSIVE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'COLLATZ_RECURSIVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the COLLATZ_RECURSIVE library.' )

  collatz_path_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'COLLATZ_RECURSIVE_TEST' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )
  
  return None
  
if ( __name__ == '__main__' ):
  timestamp ( )
  collatz_recursive_test ( )
  timestamp ( )
