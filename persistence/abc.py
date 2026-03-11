#! /usr/bin/env python3
#
def abc ( a_in = None, b_in = None, c_in = None ):

#*****************************************************************************80
#
## abc() stores, saves, and returns variables "a", "b" and "c".
#
#  Discussion:
#
#    Calling abc() with no input arguments returns the current
#    values of A, B, and C.
#
#    Calling abc(a_in,b_in,c_in) supplies new values for A, B,
#    and C which overwrite the current values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_IN: a new value for A or None
#
#    real B_IN: a new value for B or None.
#
#    real C_IN: a new value for C or None.
#
#  Persistent:
#
#    real ABC.A_DEFAULT: the current value of A.
#
#    real ABC.B_DEFAULT: the current value of B.
#
#    real ABC.C_DEFAULT: the current value of C.
#
#  Output:
#
#    real A_OUT: the current value of A.
#
#    real B_OUT: the current value of B.
#
#    real C_OUT: the current value or C.
#
  if not hasattr ( abc, "a_default" ):
    abc.a_default = 1.0

  if not hasattr ( abc, "b_default" ):
    abc.b_default = 2.0

  if not hasattr ( abc, "c_default" ):
    abc.c_default = 3.0
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( a_in is not None ):
    abc.a_default = a_in

  if ( b_in is not None ):
    abc.b_default = b_in

  if ( c_in is not None ):
    abc.c_default = c_in
#
#  The current values are copied to the output.
#
  a_out = abc.a_default
  b_out = abc.b_default
  c_out = abc.c_default

  return a_out, b_out, c_out

def abc_test ( ):

#*****************************************************************************80
#
## abc_test() tests abc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'abc_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test abc(), with the interface:' )
  print ( '    [a,b,c] = abc(a,b,c)' )
  print ( '' )

  a_out, b_out, c_out = abc ( None, None, None )
  print ( '    ', a_out, ',', b_out, ',', c_out, ' = abc ( )' )

  a_in = a_out
  b_in = 19
  c_in = c_out
  abc ( a_in, b_in, c_in )
  print ( '    abc ( ', a_in, ',', b_in, ',', c_in, ')' )

  a_in = a_out
  b_in = 19
  c_in = c_out
  a_out, b_out, c_out = abc ( None, None, None )
  print ( '    ', a_out, ',', b_out, ',', c_out, ' = abc ( )' )

  a_in = 50
  b_in = 60
  c_in = 70
  a_out, b_out, c_out = abc ( a_in, b_in, c_in )
  print ( '    ', a_out, ',', b_out, ',', c_out, \
    ' = abc ( ', a_in, ',', b_in, ',', c_in, ')' )

  a_out, b_out, c_out = abc ( None, None, None )
  print ( '    ', a_out, ',', b_out, ',', c_out, ' = abc ( )' )
#
#  Terminate.
#
  print ( '' )
  print ( 'abc_test():' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  abc_test ( )
  timestamp ( )

