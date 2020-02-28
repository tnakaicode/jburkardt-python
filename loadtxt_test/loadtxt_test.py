#! /usr/bin/env python3
#
def loadtxt_test ( ):

#*****************************************************************************80
#
## LOADTXT_TEST demonstrates the numpy function loadtxt.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'LOADTXT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOADTXT can read selected rows and columns of a text file.' )

  print ( '' )
  filename = 'basketball.txt'
  print ( '  The file "%s" contains some data' % ( filename ) )
  print ( '  Skip the first line, and extract the columns containing numerics.' )

  a = np.loadtxt ( filename, skiprows = 1, usecols = ( 0, 3, 4, 5, 8 ) )

  print ( '' )
  print ( '  Here is the numeric data that was extracted:' )
  print ( '' )

  print ( a )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOADTXT_TEST:' )
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
  timestamp ( )
  loadtxt_test ( )
  timestamp ( )
