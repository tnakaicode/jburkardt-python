#! /usr/bin/env python
#
def i4_partition_random ( n, table, seed ):

#*****************************************************************************80
#
## I4_PARTITION_RANDOM selects a random partition of the integer N.
#
#  Discussion:
#
#    Note that some elements of the partition may be 0.  The partition is
#    returned as (MULT(I),I), with NPART nonzero entries in MULT, and
#
#      N = sum ( 1 <= I <= N ) MULT(I) * I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the integer to be partitioned.
#
#    Input, integer TABLE(N), the number of partitions of the integers 1 through N.
#    This table may be computed by I4_PARTITION_COUNT2.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(N), contains in A(1:NPART) the parts of the partition.
#
#    Output, integer MULT(N), contains in MULT(1:NPART) the multiplicity
#    of the parts.
#
#    Output, integer NPART, the number of parts in the partition chosen,
#    that is, the number of integers I with nonzero multiplicity MULT(I).
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  m = n
  npart = 0

  a = np.zeros ( n, dtype = np.int32 )
  mult = np.zeros ( n, dtype = np.int32 )

  while ( 0 < m ):

    z, seed = r8_uniform_01 ( seed )
    z = m * table[m-1] * z
    id = 1
    i1 = m
    j = 0

    while ( True ):

      j = j + 1
      i1 = i1 - id

      if ( i1 < 0 ):
        id = id + 1
        i1 = m
        j = 0
        continue

      if ( i1 == 0 ):
        z = z - id
        if ( 0.0 < z ):
          id = id + 1
          i1 = m
          j = 0
          continue
        else:
          break

      if ( 0 < i1 ):
        z = z - id * table[i1-1]
        if ( z <= 0.0 ):
          break

    mult[id-1] = mult[id-1] + j
    npart = npart + j
    m = i1
#
#  Reformulate the partition in the standard form.
#  NPART is the number of distinct parts.
#
  npart = 0

  for i in range ( 1, n + 1 ):
    if ( mult[i-1] != 0 ):
      npart = npart + 1
      a[npart-1] = i
      mult[npart-1] = mult[i-1]

  for i in range ( npart, n ):
    mult[i] = 0

  return a, mult, npart, seed

def i4_partition_random_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_RANDOM_TEST tests I4_PARTITION_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_partition_count2 import i4_partition_count2
  from i4_partition_print import i4_partition_print

  n = 8

  print ( '' )
  print ( 'I4_PARTITION_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_PARTITION_RANDOM generates a random partition.' )
  print ( '' )

  seed = 123456789
#
#  Get the partition table.
#
  table = i4_partition_count2 ( n )

  print ( '' )
  print ( '  The number of partitions of N' )
  print ( '' )
  print ( '     N    Number of partitions' )
  print ( '' )

  for j in range ( 0, n ):
    print ( '  %4d    %6d' % ( j, table[j] ) )

  print ( '' )

  for i in range ( 0, 5 ):

    a, mult, npart, seed = i4_partition_random ( n, table, seed )

    i4_partition_print ( n, npart, a, mult )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_PARTITION_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_random_test ( )
  timestamp ( )
