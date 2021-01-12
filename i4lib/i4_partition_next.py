#! /usr/bin/env python
#
def i4_partition_next ( n, npart, a, mult, done ):

#*****************************************************************************80
#
## I4_PARTITION_NEXT generates the partitions of an integer, one at a time.
#
#  Discussion:
#
#    The number of partitions of N is:
#
#      1     1
#      2     2
#      3     3
#      4     5
#      5     7
#      6    11
#      7    15
#      8    22
#      9    30
#     10    42
#     11    56
#     12    77
#     13   101
#     14   135
#     15   176
#     16   231
#     17   297
#     18   385
#     19   490
#     20   627
#     21   792
#     22  1002
#     23  1255
#     24  1575
#     25  1958
#     26  2436
#     27  3010
#     28  3718
#     29  4565
#     30  5604
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
#    Input, integer NPART, the output value of NPART on the previous call.
#
#    Input, integer A(N), the output value of A on the previous call.
#
#    Input, integer MULT(N), the output value of MULT on the previous call.
#
#    Input, logical DONE, is TRUE on the first call, to perform initialization.
#    On an initialization call, the input values of NPART, A and MULT are not
#    needed.
#
#    Output, integer NPART, the number of "parts" in the next partition.
#
#    Output, integer A(N), the parts of the nextpartition.  The value N is
#    represented by sum ( 1 <= I <= NPART ) MULT(I) * A(I).
#
#    Output, integer MULT(N), the multiplicities.
#
#    Output, logical DONE, is FALSE if there are more partitions, or TRUE
#    if there are no more.
#
  from sys import exit

  if ( n <= 0 ):
    print ( '' )
    print ( 'I4_PARTITION_NEXT - Fatal error!' )
    print ( '  N must be positive.' )
    print ( '  The input value of N was %d' % ( n ) )
    exit ( 'I4_PARTITION_NEXT - Fatal error!' )

  if ( done ):

    a[0] = n
    for i in range ( 1, n ):
      a[i] = 0

    mult[0] = 1
    for i in range ( 1, n ):
      mult[i] = 0

    npart = 1
    done = False

  else:

    if ( 1 < a[npart-1] or 1 < npart ):

      done = False

      if ( a[npart-1] == 1 ):
        s = a[npart-2] + mult[npart-1]
        k = npart - 1
      else:
        s = a[npart-1]
        k = npart

      iw = a[k-1] - 1
      iu = ( s // iw )
      iv = ( s % iw )
      mult[k-1] = mult[k-1] - 1

      if ( mult[k-1] == 0 ):
        k1 = k
      else:
        k1 = k + 1

      mult[k1-1] = iu
      a[k1-1] = iw

      if ( iv == 0 ):
        npart = k1
      else:
        mult[k1] = 1
        a[k1] = iv
        npart = k1 + 1

    else:

      done = True

  return npart, a, mult, done

def i4_partition_next_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_NEXT_TEST tests I4_PARTITION_NEXT.
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
  import numpy as np
  import platform
  from i4_partition_print import i4_partition_print

  n = 7
  npart = 0
  a = np.zeros ( n )
  mult = np.zeros ( n )
  done = True

  print ( '' )
  print ( 'I4_PARTITION_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_PARTITION_NEXT generates partitions of an integer.' )
  print ( '  Here N = %d' % ( n ) )
  print ( '' )

  while ( True ):

    npart, a, mult, done = i4_partition_next ( n, npart, a, mult, done )
 
    if ( done ):
      break 

    i4_partition_print ( n, npart, a, mult )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_PARTITION_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_next_test ( )
  timestamp ( )

