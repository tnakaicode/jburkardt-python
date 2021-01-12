#! /usr/bin/env python
#
def i4_partition_count_values ( n_data ):

#*****************************************************************************80
#
## I4_PARTITION_COUNT_VALUES returns some values of the integer partition count.
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer
#    as the sum of nonzero positive integers.  The order of the summands
#    does not matter.  The number of partitions of N is symbolized
#    by P(N).  Thus, the number 5 has P(N) = 7, because it has the
#    following partitions:
#
#    5 = 5
#      = 4 + 1
#      = 3 + 2
#      = 3 + 1 + 1
#      = 2 + 2 + 1
#      = 2 + 1 + 1 + 1
#      = 1 + 1 + 1 + 1 + 1
#
#    In Mathematica, the function can be evaluated by
#
#      PartitionsP[n]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the integer.
#
#    Output, integer C, the number of partitions of the integer.
#
  import numpy as np

  n_max = 21

  c_vec = np.array ( ( \
      1, \
      1,   2,   3,   5,   7,  11,  15,  22,  30,  42, \
     56,  77, 101, 135, 176, 231, 297, 385, 490, 627 ) )

  n_vec = np.array ( ( \
     0,  \
     1,  2,  3,  4,  5,  6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def i4_partition_count_values_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_COUNT_VALUES_TEST tests I4_PARTITION_COUNT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_PARTITION_COUNT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_PARTITION_COUNT_VALUES returns values of ' )
  print ( '  the integer partition count function.' )
  print ( '' )
  print ( '     N         P(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_partition_count_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, fn ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_PARTITION_COUNT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_count_values_test ( )
  timestamp ( )
