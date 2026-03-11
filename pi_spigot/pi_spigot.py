#! /usr/bin/env python3
#
def pi_101 ( ):

#*****************************************************************************80
#
## pi_101() prints the first 101 decimal digits of pi.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2021
#
#  Author:
#
#    John Burkardt
#
  print ( '3.', end = '' )
  print ( '1415926535', end = '' )
  print ( '8979323846', end = '' )
  print ( '2643383279', end = '' )
  print ( '5028841971', end = '' )
  print ( '6939937510', end = '' )
  print ( '5820974944', end = '' )
  print ( '5923078164', end = '' )
  print ( '0628620899', end = '' )
  print ( '8628034825', end = '' )
  print ( '3421170679' )

  return

def pi_spigot ( n ):

#*****************************************************************************80
#
## pi_spigot() implements the "pi spigot" algorithm for decimal digits of pi.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stanley Rabinowitz, Stan Wagon,
#    A spigot algorithm for the digits of pi,
#    American Mathematical Monthly,
#    Volume 102, Number 3, pages 195-203, March 1995.
#
#  Input:
#
#    integer N, the number of digits to compute.
#
  import numpy as np

  len = ( ( 10 * n ) // 3 )

  a = 2 * np.ones ( len, dtype = np.int32 )
  nines = 0
  predigit = 0

  for j in range ( 1, n + 1 ):

    q = 0
    for i in range ( len - 1, -1, -1 ):
      x = 10 * a[i] + q * ( i + 1 )
      a[i] = ( x % ( 2 * i + 1 ) )
      q = ( x // ( 2 * i + 1 ) )

    a[0] = ( q % 10 )
    q = ( q // 10 )

    if ( q == 9 ):
      nines = nines + 1
    elif ( q == 10 ):
      print ( predigit + 1, end = '' )
      for k in range ( 0, nines ):
        print ( 0, end = '' )
        predigit = 0
        nines = 0
    else:
      if ( 1 < j ):
        print ( predigit, end = '' )
      if ( j == 2 ):
        print ( '.', end = '' )
      predigit = q
      if ( nines != 0 ):
        for k in range ( 0, nines ):
          print ( 9, end = '' )
        nines = 0

  print ( predigit )

  return

def pi_spigot_test ( ):

#*****************************************************************************80
#
## pi_spigot_test() tests pi_spigot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pi_spigot_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pi_spigot()' )

  n = 101
  print ( '' )
  print ( '  Compute and print the first', n, 'decimal digits of pi:' )
  print ( '' )
  pi_spigot ( n )

  print ( '' )
  print ( '  Correct first 101 digits of pi:' )
  print ( '' )
  pi_101 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pi_spigot_test():' )
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
  pi_spigot_test ( )
  timestamp ( )

