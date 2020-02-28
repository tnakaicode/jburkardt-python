#! /usr/bin/env python
#
def genprm ( a, n ):

#*****************************************************************************80
#
## GENPRM generates and applies a random permutation to an array.
#
#  Discussion:
#
#    To see the permutation explicitly, let the input array be
#    1, 2, ..., N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, integer A(N), an array to be permuted.
#
#    Input, integer N, the number of entries in the array.
#
#    Output, integer A2(N), a permuted copy of the array.
#
  from ignuin import ignuin

  a2 = a.copy ( )
  for i in range ( 0, n ):
    j = ignuin ( i, n - 1 )
    itmp  = a2[j]
    a2[j] = a2[i]
    a2[i] = itmp

  return a2

def genprm_test ( phrase ):

#*****************************************************************************80
#
## GENPRM_TEST tests GENPRM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from initialize import initialize
  from phrtsd import phrtsd
  from set_initial_seed import set_initial_seed

  print ( '' )
  print ( 'GENPRM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GENPRM generates a random permutation.' )
#
#  Initialize the generators.
#
  initialize ( )
#
#  Set the seeds based on the phrase.
#
  seed1, seed2 = phrtsd ( phrase )
#
#  Initialize all generators.
#
  set_initial_seed ( seed1, seed2 )

  n = 10

  p1 = np.array ( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
  p2 = genprm ( p1, n )

  print ( '' )
  print ( '  Array:   ' ),
  for i in range ( 0, n ):
    print ( '%d' % p1[i] ),
  print ( '' )
  print ( '  Permuted:' ),
  for i in range ( 0, n ):
    print ( '%d' % p2[i] ),
  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENPRM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomize'
  genprm_test ( phrase )
  timestamp ( )

