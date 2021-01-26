#! /usr/bin/env python
#
def c8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## C8MAT_UNIFORM_01 returns a unit pseudorandom C8MAT.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, complex C(M,N), the pseudorandom complex matrix.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647;

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'C8MAT_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'C8MAT_UNIFORM_01 - Fatal error!' )

  c = np.zeros ( ( m, n ), 'complex' )

  for i2 in range ( 0, n ): 
    for i1 in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836;

      if ( seed < 0 ):
        seed = seed + i4_huge

      r = np.sqrt ( seed * 4.656612875E-10 )

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      theta = 2.0 * np.pi * seed * 4.656612875E-10

      c[i1][i2] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## C8MAT_UNIFORM_01_TEST tests C8MAT_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from c8mat_print import c8mat_print

  m = 5
  n = 3
  seed = 123456789

  print ( '' )
  print ( 'C8MAT_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8MAT_UNIFORM_01 computes a random C8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = c8mat_uniform_01 ( m, n, seed )

  c8mat_print ( m, n, v, '  Random C8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8MAT_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_uniform_01_test ( )
  timestamp ( )
 
