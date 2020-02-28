#! /usr/bin/env python
#
def pi_values ( n_data ):

#*****************************************************************************80
#
## PI_VALUES returns values of the Pi function.
#
#  Discussion:
#
#    Pi[n] is the number of primes less than or equal to n.
#
#    In Mathematica, the function can be evaluated by:
#
#      PrimePi[n]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    Output, integer N, the argument.
#
#    Output, integer P, the value of the function.
#
  import numpy as np

  n_max = 17

  n_vec = np.array ( ( \
            10, \
            20, \
            30, \
            40, \
            50, \
            60, \
            70, \
            80, \
            90, \
           100, \
          1000, \
         10000, \
        100000, \
       1000000, \
      10000000, \
     100000000, \
    1000000000 ))

  p_vec = np.array ( ( \
             4, \
             8, \
            10, \
            12, \
            15, \
            17, \
            19, \
            22, \
            24, \
            25, \
           168, \
          1229, \
          9592, \
         78498, \
        664579, \
       5761455, \
      50847534 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    p = 0
  else:
    n = n_vec[n_data]
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, n, p

def pi_values_test ( ):

#*****************************************************************************80
#
## PI_VALUES_TEST demonstrates the use of PI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'PI_VALUES_TEST:' )
  print ( '  PI_VALUES stores values of the PI function.' )
  print ( '' )
  print ( '             N    PI(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = pi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PI_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pi_values_test ( )
  timestamp ( )

