#! /usr/bin/env python3
#
def python_mistake ( ):

#*****************************************************************************80
#
## python_mistake displays some mistakes in python.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  import numpy as np
  import platform

  print ( '' )
  print ( 'python_mistake:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Demonstrate some python mistakes.' )

  python_mistake01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'python_mistake:' )
  print ( '  Normal end of execution.' )

  return

def python_mistake01 ( ):

#*****************************************************************************80
#
## python_mistake01 tries to copy an array using the notation a = b.
#
#  Discussion:
#
#    Given arrays a and b, the statement "b = a" does not copy the entries
#    of a into b.  Instead, it allows b to be a second name for the information
#    in a.  A programmer who is unaware of this issue can set up disastrous
#    and mysterious errors.
#
#    By contrast, the correct procedure "b = a.copy()" does copy the entries
#    of a into b, creating two separate sets of memory.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'python_mistake01:' )
  print ( '  Show that A=B is not the right way to copy arrays.' )

  print ( '' )
  print ( '  Use "=" to copy an array' )
  print ( '' )
  a = np.linspace ( 1, 10, 10 )
  print ( '  a =                        ', a )
  b = a
  print ( '  (Bad) b = a =              ', b )
  i1 = np.where ( b < 5 )
  b[i1] = -1
  i2 = np.where ( 5 <= b )
  b[i2] = +1
  print ( '  Do stuff to b, but do not touch a...')
  print ( '  a =                        ', a );
  print ( '  b =                        ', b );

  print ( '' )
  print ( '  Repeat, but use COPY rather than "="' )
  print ( '' )
  a = np.linspace ( 1, 10, 10 )
  print ( '  a =                        ', a )
  b = a.copy ( )
  print ( '  (Correct) b = a.copy() =   ', b )
  i1 = np.where ( b < 5 )
  b[i1] = -1
  i2 = np.where ( 5 <= b )
  b[i2] = +1
  print ( '  Do stuff to b, but do not touch a...')
  print ( '  a =                        ', a );
  print ( '  b =                        ', b );

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
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
  python_mistake ( )
  timestamp ( )

