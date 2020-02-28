#! /usr/bin/env python
#
def easter_gregorian_values ( n_data ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_VALUES: Easter dates in Gregorian calendar.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer D, M, Y, an Easter date.
#
  import numpy as np

  n_max = 10

  d_vec = np.array ( [ 30,   12,    4,   23,   15,   31,   20,   11,   27,   16 ] )
  m_vec = np.array ( [ 3,    4,    4,    4,    4,    3,    4,    4,    3,    4 ] )
  y_vec = np.array ( [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    d = 0
    m = 0
    y = 0
  else:
    d = d_vec[n_data]
    m = m_vec[n_data]
    y = y_vec[n_data]
    n_data = n_data + 1

  return n_data, d, m, y

def easter_gregorian_values_test ( ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_VALUES_TEST tests EASTER_GREGORIAN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EASTER_GREGORIAN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EASTER_GREGORIAN_VALUES stores values of' )
  print ( '  the date of Easter in the Gregorian calendar.' )
  print ( '' )
  print ( '   D   M     Y' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, d, m, y = easter_gregorian_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %2d  %2d  %4d' % ( d, m, y ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EASTER_GREGORIAN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  easter_gregorian_values_test ( )
  timestamp ( )

