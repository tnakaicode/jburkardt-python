#! /usr/bin/env python
#
def subset_random ( n, seed ):

#*****************************************************************************80
#
## SUBSET_RANDOM returns a random subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the set.
#
#    Input/output, integer SEED, a seed for the random number
#    generator.
#
#    Output, integer S(N), defines the subset using 0 and 1 values.
#
  from i4vec_uniform_ab import i4vec_uniform_ab

  s, seed = i4vec_uniform_ab ( n, 0, 1, seed )

  return s, seed

def subset_random_test ( ):

#*****************************************************************************80
#
## SUBSET_RANDOM_TEST tests SUBSET_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'SUBSET_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_RANDOM returns a random subset.' )

  n = 5;
  seed = 123456789;

  for i in range ( 0, 10 ):
    s, seed = subset_random ( n, seed )
    i4vec_transpose_print ( n, s, '  Subset:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_random_test ( )
  timestamp ( )
 
