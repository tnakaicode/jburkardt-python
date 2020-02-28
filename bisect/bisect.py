#! /usr/bin/env python3
#
class bisect ( ):

  def __init__ ( self, a, b, f ):

    self.a = a
    self.fa = f ( a )
    self.b = b
    self.fb = f ( b )
    self.f = f

  def x ( self ):
    value = ( self.a + self.b ) / 2.0
    return value

  def bisect ( self ):
    c = ( self.a + self.b ) / 2.0
    fc = self.f ( c )
    if ( fc <= 0.0 and self.fa <= 0.0 ):
      self.a = c
      self.fa = fc
    else:
      self.b = c
      self.fb = fc
    return

def bisect_test ( ):

#*****************************************************************************80
#
## BISECT_TEST tests BISECT
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2016
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
  print ( 'BISECT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BISECT seeks a root of a nonlinear equation using bisection.' )

  a = 2.0
  b = 3.0
  f = lambda x : x ** 3 - 2.0 * x - 5
  wallis = bisect ( a, b, f )

  print ('  Wallis.x = %g' % ( wallis.x ( ) ) )

  for test in range ( 0, 20 ):
    wallis.bisect ( )
    print ( '  Wallis.a = %g, Wallis.b = %g' % ( wallis.a, wallis.b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BISECT_TEST:' )
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
  bisect_test ( )
  timestamp ( )

