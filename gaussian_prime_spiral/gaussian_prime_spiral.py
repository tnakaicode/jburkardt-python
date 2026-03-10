#! /usr/bin/env python3
#
def gaussian_prime_spiral_test ( ):

#*****************************************************************************80
#
## gaussian_prime_spiral_test() tests gaussian_prime_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'gaussian_prime_spiral_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gaussian_prime_spiral()' )
#
#  Display Gaussian primes in a rectangular region.
#
  print ( '' )
  print ( '  gaussian_prime_display() displays Gaussian primes.' )

  clo = - 15 - 15j
  chi = + 15 + 15j
  gaussian_prime_display ( clo, chi )
#
#  Compute Gaussian prime spiral from given starting point.
#
  print ( '' )
  print ( '  gaussian_prime_spiral_trajectory() computes a spiral path.' )

  cstart = - 12 - 7j
  d = +1

  avec, bvec = gaussian_prime_spiral_trajectory ( cstart, d )

  plt.clf ( )
  
  plt.plot ( avec, bvec, 'b-' )

  for i in range ( 0, len ( avec ) ):
    if ( is_gaussian_prime ( avec[i] + bvec[i] * 1j ) ):
      plt.plot ( avec[i], bvec[i], 'r.', markersize = 6 )
    else:
      plt.plot ( avec[i], bvec[i], 'k.', markersize = 3 )
  plt.plot ( cstart.real, cstart.imag, 'g.', markersize = 10 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Gaussian prime spiral' )
  filename = 'gaussian_prime_spiral.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gaussian_prime_spiral_test():' )
  print ( '  Normal end of execution.' )

  return

def gaussian_prime_display ( clo, chi ):

#*****************************************************************************80
#
## gaussian_prime_display() displays Gaussian primes in a rectangular range.
#
#  Discussion:
#
#    Let c be a Gaussian integer, a complex number of the form c = a + bi,
#    where a and b are integers.
#
#    Then c is a Gaussian prime if 
#      * a and b are integers 
#    and
#      * a is 0 and |b| is prime and |b| mod 4 is 3 or
#      * b is 0 and |a| is prime and |a| mod 4 is 3 or
#      * neither a nor b is zero, and a^2+b^2 is prime.
#
#    A Gaussian prime spiral begins at an initial Gaussian integer c, 
#    and an initial step direction d, which is 1, i, -1, or -i.
#
#    A step involves incrementing c by d.  If the new value of c
#    is a Gaussian prime, then the old direction is multiplied by i.
#
#    The spiral consists of a series of steps that eventually return
#    to the starting point.
#    
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex clo, chi: defines the lower left and upper right corners of the range.
#    Both clo and chi should be Gaussian integers.
#
  import matplotlib.pyplot as plt

  alo = int ( clo.real )
  blo = int ( clo.imag )
  ahi = int ( chi.real )
  bhi = int ( chi.imag )

  plt.clf ( )

  for a in range ( alo, ahi + 1 ):
    for b in range ( blo, bhi + 1 ):
      c = complex ( a, b )
      if ( is_gaussian_prime ( c ) ):
        plt.plot ( a, b, 'r.', markersize = 10 )
      else:
        plt.plot ( a, b, 'ko', markersize = 2 )

  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Gaussian primes (red dots)' )
  filename = 'gaussian_prime_display.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def gaussian_prime_spiral_step ( c, d ):

#*****************************************************************************80
#
## gaussian_prime_spiral_step() takes one step along a Gaussian prime spiral.
#
#  Discussion:
#
#    Let c be a Gaussian integer, a complex number of the form c = a + bi,
#    where a and b are integers.
#
#    Then c is a Gaussian prime if 
#      * a and b are integers 
#    and
#      * a is 0 and |b| is prime and |b| mod 4 is 3 or
#      * b is 0 and |a| is prime and |a| mod 4 is 3 or
#      * neither a nor b is zero, and a^2+b^2 is prime.
#
#    A Gaussian prime spiral begins at an initial Gaussian integer c, 
#    and an initial step direction d, which is 1, i, -1, or -i.
#
#    A step involves incrementing c by d.  If the new value of c
#    is a Gaussian prime, then the old direction is multiplied by i.
#
#    The spiral consists of a series of steps that eventually return
#    to the starting point.
#    
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex c: the current location.
#
#    complex d: the current step increment, which should be 1, i, -1, or -i.
#
#  Output:
#
#    complex c: the next location.
#
#    complex d: the next step increment, which should be 1, i, -1, or -i.
#
  c = c + d
  if ( is_gaussian_prime ( c ) ):
    d = d * 1j

  return c, d

def gaussian_prime_spiral_trajectory ( cstart, d ):

#*****************************************************************************80
#
## gaussian_prime_spiral_trajectory() computes a Gaussian prime spiral trajectory.
#
#  Discussion:
#
#    Let c be a Gaussian integer, a complex number of the form c = a + bi,
#    where a and b are integers.
#
#    Then c is a Gaussian prime if 
#      * a and b are integers 
#    and
#      * a is 0 and |b| is prime and |b| mod 4 is 3 or
#      * b is 0 and |a| is prime and |a| mod 4 is 3 or
#      * neither a nor b is zero, and a^2+b^2 is prime.
#
#    A Gaussian prime spiral begins at an initial Gaussian integer c, 
#    and an initial step direction d, which is 1, i, -1, or -i.
#
#    A step involves incrementing c by d.  If the new value of c
#    is a Gaussian prime, then the old direction is multiplied by i.
#
#    The spiral consists of a series of steps that eventually return
#    to the starting point.
#    
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex cstart: the starting location.
#
#    complex d: the starting step increment, which should be 1, i, -1, or -i.
#
#  Output:
#
#    integer avec(*), bvec(*): the trajectory.
#
  i = 0
  avec = []
  bvec = []

  while ( True ):

    if ( i == 0 ):
      c = cstart
    else:
      c, d = gaussian_prime_spiral_step ( c, d )

    avec.append ( c.real )
    bvec.append ( c.imag )

    if ( 0 < i and c == cstart ):
      break

    i = i + 1

  return avec, bvec

def is_gaussian_prime ( c ):

#*****************************************************************************80
#
## is_gaussian_prime() reports whether a complex number is a Gaussian prime.
#
#  Discussion:
#
#    Let c be a complex number of the form c = a + bi.
#
#    Then c is a Gaussian prime if 
#      * a and b are integers 
#    and
#      * a is 0 and |b| is prime and |b| mod 4 is 3 or
#      * b is 0 and |a| is prime and |a| mod 4 is 3 or
#      * neither a nor b is zero, and a^2+b^2 is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex c: the number to be tested.
#
#  Output:
#
#    logical value: true if c is a Gaussian prime.
#
  from sympy import isprime

  a = int ( abs ( c.real ) )
  b = int ( abs ( c.imag ) )
#
#  A and B must be integers.
#
  if ( c.real != round ( c.real ) ):
    value = False

  elif ( c.imag != round ( c.imag ) ):
    value = False
#
#  If one is zero, the other must be a prime with remainder 3 mod 4.
#
  elif ( a == 0 ):
    value = ( isprime ( b ) and ( ( b % 4 ) == 3 ) )

  elif ( b == 0 ):
    value = ( isprime ( a ) and ( ( a % 4 ) == 3 ) )
#
#  If both are nonzero, then a^2+b^2 must be prime.
#
  else:
    value = isprime ( a * a + b * b )

  return value

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
  gaussian_prime_spiral_test ( )
  timestamp ( )

