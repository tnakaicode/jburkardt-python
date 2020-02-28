#! /usr/bin/env python
#
def datenum_values ( n_data ):

#*****************************************************************************80
#
## DATENUM_VALUES returns the MATLAB DATENUM for various dates.
#
#  Discussion:
#
#    The CE or Common Era calendar is used, under the
#    hybrid Julian/Gregorian Calendar, with a transition from Julian
#    to Gregorian.  The day after 04 October 1582 was 15 October 1582.  
#
#    The year before 1 AD or CE is 1 BC or BCE.  In this data set,
#    years BC/BCE are indicated by a negative year value.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold, Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#    LC: CE12.R45.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer Y, M, D, the Common Era date.
#
#    Output, integer DATENUM, the MATLAB datenum value.
#
  import numpy as np

  n_max = 11

  d_vec = np.array ( ( \
     1, \
     1, \
     1, \
     1, \
    17, \
     9, \
    10, \
    12, \
     6, \
    25, \
     1 ))

  date_num_vec = np.array ( ( \
         1, \
       367, \
     36526, \
    365244, \
    708434, \
    710284, \
    713023, \
    718199, \
    723186, \
    729080, \
    730486 ))

  m_vec = np.array ( ( \
     1, \
     1, \
     1, \
     1, \
     8, \
     9, \
     3, \
     5, \
     1, \
     2, \
     1 ))

  y_vec = np.array ( ( \
        0, \
        1, \
      100, \
     1000, \
     1939, \
     1944, \
     1952, \
     1966, \
     1980, \
     1996, \
     2000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    y = 0
    m = 0
    d = 0
    date_num = 0
  else:
    y = y_vec[n_data]
    m = m_vec[n_data]
    d = d_vec[n_data]
    date_num = date_num_vec[n_data]
    n_data = n_data + 1

  return n_data, y, m, d, date_num

def datenum_values_test ( ):

#*****************************************************************************80
#
## DATENUM_VALUES_TEST tests DATENUM_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DATENUM_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DATENUM_VALUES stores values of' )
  print ( '  the MATLAB datenum for a given Y/M/D date' )
  print ( '' )
  print ( '       Y       M       D   DateNum' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, y, m, d, date_num = datenum_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %6d    %6d' % ( y, m, d, date_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DATENUM_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  datenum_values_test ( )
  timestamp ( )

