#! /usr/bin/env python3
#
class Y:

#*****************************************************************************80
#
## Y is a class with associated variables V0 and G.
#
#  Discussion:
#
#    __INIT__ associates values of V0 and G with an instance of Y.
#
#    RESULT returns the position at time T.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real V0, the initial velocity at time 0.
#
#    Input, real G, the gravitational acceleration.
#
  def __init__ ( self, v0, g ):
    self.v0 = v0
    self.g = g

  def result ( self, t ):
    value = self.v0 * t - 0.5 * self.g * t ** 2
    return value

def Y_test ( ):

#*****************************************************************************80
#
## Y_TEST invokes the Y class three times, generating three curves Y(V0,G)(T)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real V0, the initial velocity at time 0.
#
#    Input, real G, the gravitational acceleration.
#
  import platform

  print ( '' )
  print ( 'Y_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Y(V0,G)(T) is a function defining the height of a ball' )
  print ( '  at time T, with initial velocity V0 and gravity force G.' )

  y = Y ( 3.0, 9.81 )
  print ( '' )
  print ( '  First case:' )
  print ( '  Initial velocity = %g' % ( y.v0 ) )
  print ( '  Gravity = %g' % ( y.g ) )

  for t in range ( 0, 11 ):
    print ( '  %g  %g' % ( t, y.result ( t ) ) )

  y = Y ( -3.0, 9.81 )

  print ( '' )
  print ( '  Second case:' )
  print ( '  Initial velocity = %g' % ( y.v0 ) )
  print ( '  Gravity = %g' % ( y.g ) )

  for t in range ( 0, 11 ):
    print ( '  %g  %g' % ( t, y.result ( t ) ) )

  y = Y ( 96.0, 32.0 )

  print ( '' )
  print ( '  Third case:' )
  print ( '  Initial velocity = %g' % ( y.v0 ) )
  print ( '  Gravity = %g' % ( y.g ) )

  for t in range ( 0, 11 ):
    print ( '  %g  %g' % ( t, y.result ( t ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'Y_TEST:' )
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
  from timestamp import timestamp
  timestamp ( )
  Y_test ( )
  timestamp ( )

