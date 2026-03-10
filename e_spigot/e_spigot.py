#! /usr/bin/env python3
#
def e_101 ( ):

#*****************************************************************************80
#
## e_101() prints the first 101 decimal digits of e.
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
  print ( '2.', end = '' )
  print ( '7182818284', end = '' )
  print ( '5904523536', end = '' )
  print ( '0287471352', end = '' )
  print ( '6624977572', end = '' )
  print ( '4709369995', end = '' )
  print ( '9574966967', end = '' )
  print ( '6277240766', end = '' )
  print ( '3035354759', end = '' )
  print ( '4571382178', end = '' )
  print ( '5251664274' )

  return

def e_spigot ( n ):

#*****************************************************************************80
#
## e_spigot() implements the "e spigot" algorithm for decimal digits of e.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2019
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

  a = np.ones ( n + 1, dtype = np.int32 )

  print ( '2.', end = '' )
  for j in range ( 1, n ):
    a = a * 10
    q = 0
    for i in range ( n - 1, -1, -1 ):
      a[i] = a[i] + q
      q = ( a[i] // ( i + 2 ) )
      a[i] = ( a[i] % ( i + 2 ) )
    print ( q, end = '' )
 
  print ( '' )

  return

def e_spigot_test ( ):

#*****************************************************************************80
#
## e_spigot_test() tests e_spigot().
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
  print ( 'e_spigot_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test e_spigot()' )

  n = 101
  print ( '' )
  print ( '  Compute and print the first ', n, 'decimal digits of e:.' )
  print ( '' )
  e_spigot ( n )

  print ( '' )
  print ( '  Correct first 101 digits of e:' )
  print ( '' )
  e_101 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'e_spigot_test():' )
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
  e_spigot_test ( )
  timestamp ( )


