#! /usr/bin/env python3
#
def tic ():

#*****************************************************************************80
#
## tic() records the beginning of a time interval.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 July 2021
#
#  Output:
#
#    real startTime_for_tictoc, the starting time.
#
  import time
  global startTime_for_tictoc

  startTime_for_tictoc = time.time()

  return startTime_for_tictoc

def toc ():

#*****************************************************************************80
#
## toc() prints the time difference yielded by generator instance TicToc.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 July 2021
#
#  Output:
#
#    real s, the time since toc() was called.
#
  import time

  if ( 'startTime_for_tictoc' in globals () ):
    s = time.time() - startTime_for_tictoc
    print ( "Elapsed time is", s, "seconds." )
  else:
    s = 0.0
    print ( "toc: start time not set." )

  return s

def tictoc_test():

#*****************************************************************************80
#
## tictoc_test() tests tictoc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import time

  print ( '' )
  print ( 'tictoc_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  tictoc() provides tic() and toc() for timing.' )

  tic ( )
  time.sleep ( 5 )
  toc ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'tictoc_test():' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  tictoc_test ( )
  timestamp ( )

