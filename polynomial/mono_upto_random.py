#! /usr/bin/env python
#
def mono_upto_random ( m, n, seed  ):

#*****************************************************************************80
#
## MONO_UPTO_RANDOM: random monomial with total degree less than or equal to N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the degree.
#    0 <= N.
#
#    Input, integer SEED, the random number seed.
#
#    Output, integer X[M], the random monomial.
#
#    Output, integer RANK, the rank of the monomial.
#
#    Output, integer SEED, the random number seed.
#
  from i4_uniform_ab import i4_uniform_ab
  from mono_unrank_grlex import mono_unrank_grlex
  from mono_upto_enum import mono_upto_enum

  rank_min = 1
  rank_max = mono_upto_enum ( m, n )
  rank, seed = i4_uniform_ab ( rank_min, rank_max, seed )
  x = mono_unrank_grlex ( m, rank )

  return x, rank, seed

def mono_upto_random_test ( ):

#*****************************************************************************80
#
## MONO_UPTO_RANDOM_TEST tests MONO_UPTO_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 3

  print ( '' )
  print ( 'MONO_UPTO_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MONO_UPTO_RANDOM selects at random a monomial' )
  print ( '  in M dimensions of total degree no greater than N.' )

  n = 4

  print ( '' )
  print ( '  Let M = %d' % ( m ) )
  print ( '      N = %d' % ( n ) )
  print ( '' )

  seed = 123456789
  test_num = 5

  for test in range ( 0, test_num ):
    x, rank, seed = mono_upto_random ( m, n, seed )
    print ( '  %2d    ' % ( rank ) ),
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'MONO_UPTO_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  mono_upto_random_test ( )
  timestamp ( )
 
