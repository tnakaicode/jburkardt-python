#! /usr/bin/env python3
#
def cycle_floyd ( f, x0 ):

#*****************************************************************************80
#
## CYCLE_FLOYD finds a cycle in an iterated mapping using Floyd's method.
#
#  Discussion:
#
#    Suppose we a repeatedly apply a function f(), starting with the argument
#    x0, then f(x0), f(f(x0)) and so on.  Suppose that the range of f is finite.
#    Then eventually the iteration must reach a cycle.  Once the cycle is reached,
#    succeeding values stay within that cycle.
#
#    Starting at x0, there is a "nearest element" of the cycle, which is
#    reached after MU applications of f.
#
#    Once the cycle is entered, the cycle has a length LAM, which is the number
#    of steps required to first return to a given value.
#
#    This function uses Floyd's method to determine the values of MU and LAM,
#    given F and X0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2013
#
#  Author:
#
#    An anonymous Wikipedia article
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 2, Seminumerical Algorithms,
#    Third Edition,
#    Addison Wesley, 1997,
#    ISBN: 0201896842,
#    LC: QA76.6.K64.
#
#  Parameters:
#
#    Input, integer F( integer I ), the name of the function 
#    to be analyzed.
#
#    Input, integer X0, the starting point.
#
#    Output, integer LAM, the length of the cycle.
#
#    Output, integer MU, the index in the sequence starting
#    at X0, of the first appearance of an element of the cycle.
#
  tortoise = f ( x0 )
  hare = f ( tortoise )

  while ( tortoise != hare ):
    tortoise = f ( tortoise )
    hare = f ( f ( hare ) )

  mu = 0
  tortoise = x0

  while ( tortoise != hare ):
    tortoise = f ( tortoise )
    hare = f ( hare )
    mu = mu + 1

  lam = 1
  hare = f ( tortoise )
  while ( tortoise != hare ):
    hare = f ( hare )
    lam = lam + 1

  return lam, mu

def cycle_floyd_test01 ( ):

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST01 tests CYCLE_FLOYD for a tiny example.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CYCLE_FLOYD_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test CYCLE_FLOYD on F1().' )
  print ( '  f1(0) = 6.' )
  print ( '  f1(1) = 6.' )
  print ( '  f1(2) = 0.' )
  print ( '  f1(3) = 1.' )
  print ( '  f1(4) = 4.' )
  print ( '  f1(5) = 3.' )
  print ( '  f1(6) = 3.' )
  print ( '  f1(7) = 4.' )
  print ( '  f1(8) = 0.' )

  x0 = 2
  print ( '' )
  print ( '  Starting argument X0 = %d' % ( x0 ) )

  lam, mu = cycle_floyd ( f1, x0 )

  print ( '' )
  print ( '  Reported cycle length is %d' % ( lam ) )
  print ( '  Expected value is 3' )
  print ( '' )
  print ( '  Reported distance to first cycle element is %d' % ( mu ) )
  print ( '  Expected value is  2' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_FLOYD_TEST01' )
  print ( '  Normal end of execution.' )
  return

def cycle_floyd_test02 ( ) :

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST02 tests CYCLE_FLOYD for F2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CYCLE_FLOYD_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test CYCLE_FLOYD for F2().' )
  print ( '  f2(i) = mod ( 22 * i + 1, 72 ).' )

  x0 = 0
  print ( '' )
  print ( '  Starting argument X0 = %d' % ( x0 ) )

  lam, mu = cycle_floyd ( f2, x0 )

  print ( '' )
  print ( '  Reported cycle length is %d' % ( lam ) )
  print ( '  Expected value is 9' )
  print ( '' )
  print ( '  Reported distance to first cycle element is %d' % ( mu ) )
  print ( '  Expected value is 3' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_FLOYD_TEST02' )
  print ( '  Normal end of execution.' )
  return

def cycle_floyd_test03 ( ) :

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST03 tests CYCLE_FLOYD for F3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CYCLE_FLOYD_TEST03' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test CYCLE_FLOYD for F3().' )
  print ( '  f3(i) = mod ( 123 * i + 456, 100000 ).' )

  x0 = 789
  print ( '' )
  print ( '  Starting argument X0 = %d' % ( x0 ) )

  lam, mu = cycle_floyd ( f3, x0 )

  print ( '' )
  print ( '  Reported cycle length is %d' % ( lam ) )
  print ( '  Expected value is 50000' )
  print ( '' )
  print ( '  Reported distance to first cycle element is %d' % ( mu ) )
  print ( '  Expected value is 0' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_FLOYD_TEST03' )
  print ( '  Normal end of execution.' )
  return

def cycle_floyd_test04 ( ) :

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST04 tests CYCLE_FLOYD for F4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CYCLE_FLOYD_TEST04' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test CYCLE_FLOYD for F4().' )
  print ( '  f4(i) = mod ( 31421 * i + 6927, 65536 ).' )

  x0 = 1
  print ( '' )
  print ( '  Starting argument X0 = %d' % ( x0 ) )

  lam, mu = cycle_floyd ( f4, x0 )

  print ( '' )
  print ( '  Reported cycle length is %d' % ( lam ) )
  print ( '  Expected value is 65536' )
  print ( '' )
  print ( '  Reported distance to first cycle element is %d' % ( mu ) )
  print ( '  Expected value is 0' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_FLOYD_TEST04' )
  print ( '  Normal end of execution.' )
  return

def cycle_floyd_test05 ( ) :

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST05 tests CYCLE_FLOYD for F5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CYCLE_FLOYD_TEST05' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test CYCLE_FLOYD for F5().' )
  print ( '  f5(i) = mod ( 16383 * i + 1, 65536 ).' )

  x0 = 1
  print ( '' )
  print ( '  Starting argument X0 = %d' % ( x0 ) )

  lam, mu = cycle_floyd ( f5, x0 )

  print ( '' )
  print ( '  Reported cycle length is %d' % ( lam ) )
  print ( '  Expected value is 8' )
  print ( '' )
  print ( '  Reported distance to first cycle element is %d' % ( mu ) )
  print ( '  Expected value is 0' )

  i = 0
  x0 = 1
  print ( '' )
  print ( '  %d  %d' % ( i, x0 ) )
  for i in range ( 1, 11 ):
    x0 = f5 ( x0 )
    print ( '  %d  %d' % ( i, x0 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_FLOYD_TEST05' )
  print ( '  Normal end of execution.' )
  return

def cycle_floyd_test ( ):

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST tests the CYCLE_FLOYD library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CYCLE_FLOYD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CYCLE_FLOYD library.' )

  cycle_floyd_test01 ( )
  cycle_floyd_test02 ( )
  cycle_floyd_test03 ( )
  cycle_floyd_test04 ( )
  cycle_floyd_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_FLOYD_TEST' )
  print ( '  Normal end of execution.' )

  return

def f1 ( i ) :

#*****************************************************************************80
#
## F1 is the iteration function for example 1.
#
#  Discussion:
#
#    This function has two cycles:
#
#    6, 3, 1, of length 3
#    4, of length 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#    0 <= I <= 9.
#
#    Output, integer VALUE, the value of the function.
#
  f_table = [ 6, 6, 0, 1, 4, 3, 3, 4, 0 ]

  value = f_table [i]

  return value

def f2 ( i ) :

#*****************************************************************************80
#
## F2 is the iteration function for example 2.
#
#  Discussion:
#
#    This function has a cycle
#
#    3, 67, 35, 51, 43, 11, 27, 19, 59, of length 9
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  value = ( ( 22 * i + 1 ) % 72 )

  return value

def f3 ( i ) :

#*****************************************************************************80
#
## F3 is the iteration function for example 3.
#
#  Discussion:
#
#    This function has a cycle of length 50000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  value = ( ( 123 * i + 456 ) % 1000000 )

  return value

def f4 ( i ) :

#*****************************************************************************80
#
## F4 is the iteration function for example 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  value = ( ( 31421 * i + 6927 ) % 65536 );

  return value

def f5 ( i ) :

#*****************************************************************************80
#
## F5 is the iteration function for example 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  value = ( ( 16383 * i + 1 ) % 65536 )

  return value

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
  cycle_floyd_test ( )
  timestamp ( )

