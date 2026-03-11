#! /usr/bin/env python3
#
def rng_cliff_test ( ):

#*****************************************************************************80
#
## rng_cliff_test() tests rng_cliff().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rng_cliff_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rng_cliff().' )

  rng_cliff_test01 ( )
  rng_cliff_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rng_cliff_test():' )
  print ( '  Normal end of execution.' )

  return

def rng_cliff_test01 ( ):

#*****************************************************************************80
#
## rng_cliff_test01() tests rng_cliff_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 August 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'rng_cliff_test01():' )
  print ( '  rng_cliff_next() computes the next entry in the' )
  print ( '  Cliff pseudorandom number generator sequence.' )
  print ( '' )
  print ( '       i         r(i)' )
  print ( '' )

  for i in range ( 0, 11 ):
    if ( i == 0 ):
      r = 0.5
    else:
      r = rng_cliff_next ( r )
    print ( '  %6d  %16.8f' % ( i, r ) )

  return

def rng_cliff_test02 ( ):

#*****************************************************************************80
#
## rng_cliff_test02() tests rng_cliff_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rng_cliff_test02():' )
  print ( '  rng_cliff_next() computes the next entry in the' )
  print ( '  Cliff pseudorandom number generator sequence.' )
  print ( '' )
  print ( '  Generate a sequence of length n.' )
  print ( '  Compute mean and standard deviation.' )
  print ( '' )
  print ( '       n        mean         std' )
  print ( '' )

  n = 10

  for n_log in range ( 1, 8 ):

    rvec = np.zeros ( n )

    rvec[0] = 0.5

    for i in range ( 1, n ):
      rvec[i] = rng_cliff_next ( rvec[i-1] )

    print ( '  %8d  %10.6f  %10.6f' % ( n, np.mean ( rvec ), np.std ( rvec ) ) )

    n = n * 10

  return

def rng_cliff_next ( x ):

#*****************************************************************************80
#
## rng_cliff_next() returns the next entry for the Cliff random number generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the current entry.
#    0 < x < 1.
#
#  Output:
#
#    real x: the next entry.
#
  import numpy as np

  if ( x <= 0.0 or 1.0 <= x ):
    raise Exception ( 'rng_cliff_next: 0 < x < 1 fails for input.' )
  
  x = ( - 100.0 * np.log ( x ) ) % 1.0

  return x

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
  rng_cliff_test ( )
  timestamp ( )

