#! /usr/bin/env python3
#
def function_args ( *args ):

#*****************************************************************************80
#
## FUNCTION_ARGS accepts and prints an arbitrary number of arguments.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, *ARGS, an arbitrary number of arguments.
#
  print ( '' )
  print ( 'FUNCTION_ARGS:' )
  print ( '  Number of arguments on this call was %d' % ( len ( args ) ) )
  print ( '' )

  for count, thing in enumerate ( args ):
    print ( '  {0}. {1}'.format ( count, thing ) )

  return

def function_args_test ( ):

#*****************************************************************************80
#
## FUNCTION_ARGS_TEST tests FUNCTION_ARGS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'FUNCTION_ARGS_TEST:' )
  print ( '  FUNCTION_ARGS demonstrates how to count and print function arguments' )
  print ( '  when the number of arguments may vary.' )

  function_args ( )
  function_args ( 1.1, - 2.2, 3.3 )
  function_args ( 1, 'two', 3.3, ( 4, 5 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FUNCTION_ARGS_TEST:' )
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

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):

  import platform
  import sys

  print ( '' )
  print ( 'ARGS' )
  print ( '  Python version %s' % ( platform.python_version ( )  ))
  print ( '  Count and print the arguments.' )
  print ( '' )
  print ( '  The number of arguments was ' + repr ( len ( sys.argv ) ) + '.' )
  print ( '' )
  print ( '  Arg[0] = the program name = ' + sys.argv[0] + '' )

  i = 1

  while 1 < len ( sys.argv ):
    print ( '  Arg[' + repr ( i ) + '] = ' + sys.argv[1] + '' )
    del sys.argv[1]
    i = i + 1

  timestamp ( )
  function_args_test ( )
  timestamp ( )

