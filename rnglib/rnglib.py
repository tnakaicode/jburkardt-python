#! /usr/bin/env python3
#
def rnglib_test ( ):

#*****************************************************************************80
#
## RNGLIB_TEST tests the RNGLIB library.
#
#  Discussion:
#
#    RNGLIB_TEST calls sample problems for the RNGLIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uni         import i4_uni_test
  from initialize     import initialize
  from r8_uni_01      import r8_uni_01_test
  from rnglib_test03  import rnglib_test03
  from rnglib_test04  import rnglib_test04

  print ( '' )
  print ( 'RNGLIB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the RNGLIB library.' )
#
#  Initialize RNGLIB.
#
  initialize ( )
#
#  Call tests.
#
  i4_uni_test ( )
  r8_uni_01_test ( )

  rnglib_test03 ( )
  rnglib_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RNGLIB_TEST:' )
  print ( '  Normal end of execution.' )

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rnglib_test ( )
  timestamp ( )

