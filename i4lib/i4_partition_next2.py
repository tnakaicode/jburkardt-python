#! /usr/bin/env python
#
def i4_partition_next2 ( n, npart, a, mult, more ):

#*****************************************************************************80
#
## I4_PARTITION_NEXT2 computes the partitions of the integer N one at a time.
#
#  Discussion:
#
#    Unlike compositions, order is not important in a partition.  Thus
#    the sequences 3+2+1 and 1+2+3 represent distinct compositions, but
#    not distinct partitions.  Also 0 is never returned as one of the
#    elements of the partition.
#
#    Initialize the program by calling with MORE = FALSE.  On an initialization
#    call, the input values of A, MULT and NPART are not needed.  Thereafter,
#    they should be set to the output values of A, MULT and NPART
#    from the previous call.
#
#  Example:
#
#    Sample partitions of 6 include:
#
#      6 = 4+1+1 = 3+2+1 = 2+2+2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the integer whose partitions are desired.
#
#    Input, integer NPART, the output value of NPART on the previous call.
#
#    Input, integer A(N), the output value of A on the previous call.
#
#    Input, integer MULT(N), the output value of MULT on the previous call.
#
#    Input, logical MORE, is FALSE on the first call, which causes
#    initialization.  Thereafter, it should be TRUE.
#
#    Output, integer NPART, the number of distinct, nonzero parts in the
#    output partition.
#
#    Output, integer A(N).  A(1:NPART) the distinct parts
#    of the partition.
#
#    Output, integer MULT(1:NPART), the multiplicity of the parts.
#
#    Output, logical MORE is TRUE if there are more partitions available.
#
  if ( not more ):
    npart = 1
    a[npart-1] = n
    mult[npart-1] = 1
    more = ( mult[npart-1] != n )
    return npart, a, mult, more

  isum = 1

  if ( a[npart-1] <= 1 ):
    isum = mult[npart-1] + 1
    npart = npart - 1

  iff = a[npart-1] - 1

  if ( mult[npart-1] != 1 ):
    mult[npart-1] = mult[npart-1] - 1
    npart = npart + 1

  a[npart-1] = iff
  mult[npart-1] = 1 + ( isum // iff )
  s = ( isum % iff )

  if ( 0 < s ):
    npart = npart + 1
    a[npart-1] = s
    mult[npart-1] = 1
#
#  There are more partitions, as long as we haven't just computed
#  the last one, which is N copies of 1.
#
  more = ( mult[npart-1] != n )

  return npart, a, mult, more

def i4_partition_next2_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_NEXT2_TEST tests I4_PARTITION_NEXT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4_partition_print import i4_partition_print

  n = 7

  print ( '' )
  print ( 'I4_PARTITION_NEXT2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_PARTITION_NEXT2 produces partitions of an integer.' )
  print ( '' )

  npart = 0
  a = np.zeros ( n )
  mult = np.zeros ( n )
  more = False

  while ( True ):

    npart, a, mult, more = i4_partition_next2 ( n, npart, a, mult, more )

    i4_partition_print ( n, npart, a, mult )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_PARTITION_NEXT2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_next2_test ( )
  timestamp ( )

