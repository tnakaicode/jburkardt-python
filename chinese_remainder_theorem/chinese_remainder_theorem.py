#! /usr/bin/env python3
#
def chinese_remainder_theorem_test ( ):

#*****************************************************************************80
#
## chinese_remainder_theorem_test() tests chinese_remainder_theorem().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 December 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'chinese_remainder_theorem_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test chinese_remainder_theorem().' )

  crt_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'chinese_remainder_theorem_test():' )
  print ( '  Normal end of execution.' )
  return

def crt_test ( ):

#*****************************************************************************80
#
## crt_test() tests crt().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 December 2020
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt
#
  from random import randrange
  from sympy import prod
  from sympy.ntheory.modular import crt

  print ( '' )
  print ( 'crt_test():' )
  print ( '  crt() reconstructs a value f which satisfies' )
  print ( '    mod(f,m(i)) = r(i), 0 <= i < n' )

  moduli = [ 199, 233, 194, 239 ]
  M = prod ( moduli )
  print ( '  Modulus product is ', M )
#
#  Choose a test value between 0 and M-1.
#
  print ( '  Random test value x will satisfy 0 <= x < ', M )
  x = randrange ( M )
  print ( '  Random test value is ', x )

  rx = [ x % m for m in moduli ]

  y = crt ( moduli, rx, symmetric = False )[0]
  print ( '  Recovered value is y = ', y )

  ry = [ y % m for m in moduli ]

  print ( '' )
  print ( '  #i   m[i]  r[i]  mod(f,m[i])' )
  print ( '' )

  for i in range ( 0, 4 ):
    print ( ' %3d   %3d   %3d      %3d' % ( i, moduli[i], rx[i], ry[i] ) )

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
  chinese_remainder_theorem_test ( )
  timestamp ( )

