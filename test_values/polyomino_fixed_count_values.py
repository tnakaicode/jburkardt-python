#! /usr/bin/env python
#
def polyomino_fixed_count_values ( n_data ):

#*****************************************************************************80
#
## POLYOMINO_FIXED_COUNT_VALUES counts fixed polyominoes (allowing holes).
#
#  Discussion:
#
#    Polyominoes are connected planar shapes formed by adjoining unit squares.
#
#    The number of unit squares in a polyomino is its order.
#
#    If we do not ignore reflections and rotations when comparing polyominoes,
#    then we are considering the class of "fixed" polyominoes.  In that case,
#    for instance, there are 65 fixed polyominoes of order 5.
#
#    As the order increases, the number of polyominoes grows very rapidly.
#    The list offered here goes no further than order 28, but the later
#    numbers in the list are too large to represent as 32 byte integers. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Solomon Golomb,
#    Polyominoes: Puzzles, Patterns, Problems, and Packings,
#    Princeton University Press, 1996,
#    ISBN: 9780691024448
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer ORDER, the order of a polyomino.
#
#    Output, integer NUMBER, the number of fixed polyominos of this order.
#
  import numpy as np

  n_max = 29

  order_vec = np.array ( [ \
    0, \
    1,  2,  3,  4,  5, \
    6,  7,  8,  9, 10, \
   11, 12, 13, 14, 15, \
   16, 17, 18, 19, 20, \
   21, 22, 23, 24, 25, \
   26, 27, 28 ] )

  number_vec = np.array ( [  \
    1, \
    1, 2, 6, 19, 63,  \
    216, 760, 2725, 9910, 36446,  \
    135268, 505861, 1903890, 7204874, 27394666,  \
    104592937, 400795844, 1540820542, 5940738676, 22964779660,  \
    88983512783, 345532572678, 1344372335524, 5239988770268, 20457802016011,  \
    79992676367108, 313224032098244, 1228088671826973 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    order = 0
    number = 0
  else:
    order = order_vec[n_data]
    number = number_vec[n_data]
    n_data = n_data + 1

  return n_data, order, number

def polyomino_fixed_count_values_test ( ):

#*****************************************************************************80
#
## POLYOMINO_FIXED_COUNT_VALUES_TEST tests POLYOMINO_FIXED_COUNT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'POLYOMINO_FIXED_COUNT_VALUES_TEST:' )
  print ( '  POLYOMINO_FIXED_COUNT_VALUES returns counts of' )
  print ( '  the number of fixed polyominoes.' )
  print ( '' )
  print ( '     Order     Number' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, order, number = polyomino_fixed_count_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %d  %d' % (  order, number ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYOMINO_FIXED_COUNT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polyomino_fixed_count_values_test ( )
  timestamp ( )
