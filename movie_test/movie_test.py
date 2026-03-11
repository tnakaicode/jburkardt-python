#! /usr/bin/env python3
#
def movie_test ( ):

#*****************************************************************************80
#
## movie_test() tests Python movie making.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2023
#
#  Author:
#
#    John Burkardt
#
  from allen_cahn_movie import allen_cahn_movie
  from sine_movie import sine_movie
  import numpy as np
  import platform

  print ( '' )
  print ( 'movie_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test movie making in Python.' )

  allen_cahn_movie ( )
  sine_movie
#
#  Terminate.
#
  print ( '' )
  print ( 'movie_test():' )
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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  movie_test ( )
  timestamp ( )
