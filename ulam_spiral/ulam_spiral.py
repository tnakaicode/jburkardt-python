#! /usr/bin/env python3
#
def ulam_spiral_test ( ):

#*****************************************************************************80
#
## ulam_spiral_test() tests ulam_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ulam_spiral_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ulam_spiral()' )

  spiral_array_test ( )
  prime_spiral_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ulam_spiral_test():' )
  print ( '  Normal end of execution.' )

  return

def i4_is_prime ( n ) :

#*****************************************************************************80
#
## i4_is_prime() reports whether an I4 is prime.
#
#  Discussion:
#
#    A simple, unoptimized sieve of Eratosthenes is used to
#    check whether N can be divided by any integer between 2
#    and SQRT(N).
#
#    Note that negative numbers, 0 and 1 are not considered prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be tested.
#
#  Output:
#
#    boolean VALUE, is TRUE if N is prime, and FALSE otherwise.
#
  import numpy as np

  if ( n <= 0 ):
    value = False
    return value

  if ( n == 1 ):
    value = False
    return value

  if ( n <= 3 ):
    value = True
    return value

  nhi = int ( np.sqrt ( float ( n ) ) )

  for i in range ( 2, nhi + 1 ):
    if ( ( n % i ) == 0 ):
      value = False
      return value

  value = True

  return value

def prime_spiral ( thick, base ):

#*****************************************************************************80
#
## prime_spiral() produces a spiral array with 1's representing prime numbers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer thick: the "radius" of the array, which can be 0 or more.
#
#    integer base: the starting value at the center of the spiral.
#    This is usually 1.
#
#  Output:
#
#    integer P[2*thick+1,2*thick+1]: an array of sequential integers, 
#    spiraling out from a central value of base.
#
  import numpy as np

  S = spiral_array ( thick, base )

  m, n = S.shape
  P = np.zeros ( [ m, n ], dtype = int )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      P[i,j] = i4_is_prime ( S[i,j] )

  return P

def prime_spiral_test ( ):

#*****************************************************************************80
#
## prime_spiral_test() tests prime_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'prime_spiral_test():' )
  print ( '  prime_spiral(thick,k) makes a 2*thick+1 order array P' )
  print ( '  of 1\'s for primes and 0\'s otherwise,' )
  print ( '  spiralling out from a central value of k.' )
#
#  Print a small version of P.
#
  thick = 3
  k = 1
  P = prime_spiral ( thick, k )

  print ( '' )
  print ( '  thick =', thick )
  print ( '  k =', k )
  print ( '  P:' )
  print ( P )
#
#  Creat a larger version, and display it with spy().
#
  thick = 30
  k = 1
  P = prime_spiral ( thick, k )
  print ( '' )
  print ( '  thick =', thick )
  print ( '  k =', k )
  print ( '  P:' )

  plt.clf ( )
  plt.spy ( P )
  plt.axis ( False )
  filename = 'prime_spiral.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
  
  return

def spiral_array ( thick, base ):

#*****************************************************************************80
#
## spiral_array() produces a 2*thick+1 x 2*thick+1 spiral array of integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer thick: the "radius" of the array, which can be 0 or more.
#
#    integer base: the starting value at the center of the spiral.
#    This is usually 1.
#
#  Output:
#
#    integer S[2*thick+1,2*thick+1]: an array of sequential integers, 
#    spiraling out from a central value of base.
#
  import numpy as np

  n = 2 * thick + 1
  S = np.zeros ( [ n, n ], dtype = int )

  row = thick + 1
  col = thick
  k = base - 1

  for t in range ( 0, thick + 1 ):

    col = col + 1
    k = k + 1
    S[row-1,col-1] = k
    done = False

    while ( not done ):

      if ( row == t + thick + 1 and col == t + thick + 1 ):
        done = True
        break
      elif ( col == t + thick + 1 and - t + thick + 1 < row ):
        row = row - 1
      elif ( row == - t + thick + 1 and - t + thick + 1 < col ):
        col = col - 1
      elif ( col == - t + thick + 1 and row < t + thick + 1 ):
        row = row + 1
      elif ( row == t + thick + 1 and col < t + thick + 1 ):
        col = col + 1

      k = k + 1
      S[row-1,col-1] = k

  return S

def spiral_array_test ( ):

#*****************************************************************************80
#
## spiral_array_test() tests spiral_array().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'spiral_array_test():' )
  print ( '  spiral_array(thick,k) makes a 2*thick+1 order array S' )
  print ( '  of integers, spiralling out from a central value of k.' )

  thick = 3
  k = 1
  S = spiral_array ( thick, k )

  print ( '' )
  print ( '  thick = ', thick )
  print ( '  k = ', k )
  print ( '  S:' )
  print ( S )
  
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
  ulam_spiral_test ( )
  timestamp ( )


