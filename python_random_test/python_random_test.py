#! /usr/bin/env python3
#
def python_random_test ( ):

#*****************************************************************************80
#
## python_random_test() tests Python random number generation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'python_random_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test random number generation.' )

  seed_test ( )
  normal_test ( )
  chi_test ( )
  rng_share_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'python_random_test():' )
  print ( '  Normal end of execution.' )

  return

def seed_test ( ):

#*****************************************************************************80
#
## seed_test() tests use of random number seed.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 December 2023
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'seed_test():' )
  print ( '  Set seed to get or recover a specific sequence.' )

  for i in range ( 0, 3 ):
    if ( i == 1 ):
      seed = 987654321
    else:
      seed = 123456789
    rng = default_rng ( seed )
    print ( '' )
    print ( '  Initializing with seed = ', seed )
    for j in range ( 0, 5 ):
      r = rng.random ( )
      print ( '  ', j, ':  ', r )
   
  return

def normal_test ( ):

#*****************************************************************************80
#
## normal_test() tests generation of random standard normal values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 December 2023
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'normal_test():' )
  print ( '  Generate normal random values with standard_normal().' )

  for i in range ( 0, 3 ):

    if ( i == 1 ):
      seed = 987654321
    else:
      seed = 123456789

    rng = default_rng ( seed )

    n = 1000
    r = rng.standard_normal ( size = n )
    mx = np.max ( r )
    mn = np.min ( r )
    mu = np.mean ( r )
    sg = np.std ( r )
    vr = np.var ( r )
   
    print ( '' )
    print ( '  Seed     = ', seed )
    print ( '  Values   = ', n )
    print ( '  Minimum  = ', mn )
    print ( '  Mean     = ', mu )
    print ( '  Maximum  = ', mx )
    print ( '  STD      = ', sg )
    print ( '  Variance = ', vr )

  return

def chi_test ( ):

#*****************************************************************************80
#
## chi_test() tests generation of random chi values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 December 2023
#
#  Author:
#
#    John Burkardt
#
  from scipy.stats import chi
  import numpy as np

  print ( '' )
  print ( 'chi_test():' )
  print ( '  Generate random chi values.' )

  for i in range ( 0, 3 ):

    if ( i == 1 ):
      seed = 987654321
    else:
      seed = 123456789

    df = 5
    n = 1000
    r = chi.rvs ( df, size = n, random_state = seed )
    mx = np.max ( r )
    mn = np.min ( r )
    mu = np.mean ( r )
    sigma = np.std ( r )
   
    print ( '' )
    print ( '  Seed = ', seed )
    print ( '  Chi values generated = ', n )
    print ( '  Minimum = ', mn )
    print ( '  Mean    = ', mu )
    print ( '  Maximum = ', mx )
    print ( '  STD =     ', sigma )

  return

def rng_share_test ( ):

#*****************************************************************************80
#
## rng_share_test() shows how the random number generator can be "shared".
#
#  Discussion:
#
#    When a program depends on random values, and rng() is used to generate
#    them, and this happens within more than one function, then it is 
#    advisable to "share" the definition of a single pointer to rng().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'rng_shared_test():' )
  print ( '  Share the rng with a lower level function.' )

  for i in range ( 0, 3 ):

    seed = 123456789
    rng = default_rng ( seed )

    if ( i == 0 ):
      
      print ( '' )
      print ( '  Initializing with seed = ', seed )
      print ( '  Executing rng only in main function.' )
      for j in range ( 0, 5 ):
        r = rng.random ( )
        print ( '  ', j, ' (main):     ', r )

    elif ( i == 1 ):

      print ( '' )
      print ( '  Initializing with seed = ', seed )
      print ( '  Executing shared rng in main and lower function.' )
      for j in range ( 0, 3 ):
        r = rng.random ( )
        print ( '  ', j, ' (main):     ', r )
      rng_shared ( rng )

    elif ( i == 2 ):

      print ( '' )
      print ( '  Initializing with seed = ', seed )
      print ( '  Executing rng in main and separate rng in lower function.' )
      for j in range ( 0, 3 ):
        r = rng.random ( )
        print ( '  ', j, ' (main):     ', r )
      rng_unshared ( )

  return

def rng_shared ( rng ):

#*****************************************************************************80
#
## rng_shared() uses a shared copy of rng() to generate random values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  for j in range ( 3, 5 ):
    r = rng.random ( )
    print ( '  ', j, ' (shared):   ', r )
  return

def rng_unshared ( ):

#*****************************************************************************80
#
## rng_unshared() creates a new version of rng() to generate random values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  rng = default_rng ( )
  for j in range ( 3, 5 ):
    r = rng.random ( )
    print ( '  ', j, ' (unshared): ', r )
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
  python_random_test ( )
  timestamp ( )

