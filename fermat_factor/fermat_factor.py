#! /usr/bin/env python3
#
def fermat_factor_test ( ):

#*****************************************************************************80
#
## fermat_factor_test() tests fermat_factor().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from primePy import primes

  print ( '' )
  print ( 'fermat_factor_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  fermat_factor() factors an integer using the Fermat method.' )

  for n in [ 39, 25951, 2025090001, 2027651281 ]:

    f1, f2 = fermat_factor ( n )

    print ( '' )
    print ( '  Seeking factors of n = ', n )
    print ( '  ', f1, ' * ', f2, ' = ', f1 * f2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'fermat_factor_test():' )
  print ( '  Normal end of execution.' )

  return

def fermat_factor ( n ):

#*****************************************************************************80
#
## fermat_factor() uses Fermat factorization on an integer.
#
#  Discussion:
#
#    The method determines values A and B such that 
#      N = A^2 - B^2  = ( A + B ) * ( A - B ).
#
#    The method is most efficient when B is small, that is, the two
#    factors are close.  For encryption, the key N is often generated
#    by two primes that are roughly the same size, and this make this
#    method complete more quickly.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 April 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Manon Bischoff,
#    This more than 380-year-old trick can crack some modern encryption,
#    Spektrum der Wissenschaft,
#    09 April 2025.
#
#  Input:
#
#    integer n: the number to be factored.
#
#  Output:
#
#    integer f1, f2: factors of n.
#
  from math import ceil
  from math import floor
  from math import sqrt

  n2 = sqrt ( n )
  n2 = ceil ( n2 )
  steps = 0

  while ( n2 <= n ):

    n3 = n2 * n2 - n
    n4 = floor ( sqrt ( n3 ) )
    if ( n4 * n4 == n3 ):
      if ( False ):
        print ( '' )
        print ( 'steps = ', steps )
        print ( 'n2 = ', n2 )
        print ( 'n4 = ', n4 )
      f1 = n2 + n4
      f2 = n2 - n4
      break
    n2 = n2 + 1
    steps = steps + 1

  return f1, f2

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

if ( __name__ == "__main__" ):
  timestamp ( )
  fermat_factor_test ( )
  timestamp ( )

