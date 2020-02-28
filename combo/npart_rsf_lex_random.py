#! /usr/bin/env python
#
def npart_rsf_lex_random ( n, npart, seed ):

#*****************************************************************************80
#
## NPART_RSF_LEX_RANDOM returns a random RSF NPART partition.
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
#    Input, integer N, the integer to be partitioned.
#    N must be positive.
#
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Input/output, integer SEED, a seed for the random number
#    generator.
#
#    Output, integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
  from i4_uniform_ab import i4_uniform_ab
  from npart_enum import npart_enum
  from npart_rsf_lex_unrank import npart_rsf_lex_unrank

  npartitions = npart_enum ( n, npart );

  rank, seed = i4_uniform_ab ( 1, npartitions, seed )

  a = npart_rsf_lex_unrank ( rank, n, npart )

  return a, seed

def npart_rsf_lex_random_test ( ):

#*****************************************************************************80
#
## NPART_RSF_LEX_RANDOM_TEST tests NPART_RSF_LEX_RANDOM;
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

  npart = 3
  n = 12
  seed = 123456789

  print ( '' )
  print ( 'NPART_RSF_LEX_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_RSF_LEX_RANDOM produces random examples' )
  print ( '  of partitions of N = %d' % ( n ) )
  print ( '  with NPART = %d parts' % ( npart ) )
  print ( '  in reverse standard form.' )
  print ( '' )

  for i in range ( 0, 10 ):

    t, seed = npart_rsf_lex_random ( n, npart, seed )

    for i in range ( 0, npart ):
      print ( '%5d' % ( t[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_RSF_LEX_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_rsf_lex_random_test ( )
  timestamp ( )
 
