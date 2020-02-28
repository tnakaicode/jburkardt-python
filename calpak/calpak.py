#! /usr/bin/env python3
#
def ch_cap ( c ):

#*****************************************************************************80
#
## CH_CAP capitalizes a single character.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character C, the character to capitalize.
#
#    Output, character C2, the capitalized character.
#
  i = ord ( c )

  if ( ord ( 'a' ) <= i and i <= ord ( 'z' ) ):
    i2 = i + ord ( 'A' ) - ord ( 'a' )
    c2 = chr ( i2 )
  else:
    c2 = c

  return c2

def ch_cap_test ( ):

#*****************************************************************************80
#
## CH_CAP_TEST tests CH_CAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CH_CAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_CAP uppercases a character.' )

  print ( '' )
  print ( '  C  CH_CAP(C)' )
  print ( '' )

  c = 'F'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = 'f'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = '1'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = 'b'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = '&'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_CAP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def datenum_to_jed ( dn ):

#*****************************************************************************80
#
## DATENUM_TO_JED converts a MATLAB DATENUM to a JED.
#
#  Discussion:
#
#    The MATLAB "datenum" function accepts a string defining
#    a date and returns a MATLAB date number:
#
#      dn = datenum ( 'Aug 17 1939' )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real DN, a MATLAB DATENUM.
#
#    Output, real JED, the Julian Ephemeris Date.
#
  jed = dn + epoch_to_jed_datenum ( )

  return jed

def datenum_to_jed_test ( ):

#*****************************************************************************80
#
## DATENUM_TO_JED_TEST tests DATENUM_TO_JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'DATENUM_TO_JED_TEST' )
  print ( '  DATENUM_TO_JED: Matlab DATENUM -> JED.' )
  print ( '' )
  print ( '  JED (in)    DATENUM             JED (out)' )
  print ( '' )

  jed_epoch = epoch_to_jed_datenum ( )

  i = 0

  while ( True ):

    i = i + 1
    jed1 = jed_test ( i )

    if ( jed1 < 0.0 ):
      break

    if ( jed_epoch <= jed1 ):

      date_num = jed_to_datenum ( jed1 )
      jed3 = datenum_to_jed ( date_num )

      print ( '  %11.2f  %12.2f  %11.2f'% ( jed1, date_num, jed3 ) )

  return

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
#    Output, integer DATENUM, the MATLAB DATENUM value.
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

def day_borrow_common ( y, m, d ):

#*****************************************************************************80
#
## DAY_BORROW_COMMON borrows days from months in a Common date.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, a year, month, and day
#    representing a date.  On input, D might be negative.  On output,
#    M should have decreased by one month, and D gone up by the
#    number of days in the month we "cashed in".  Y may be affected
#    if the input value of M was 1.
#
  while ( d <= 0 ):

    m = m - 1

    y, m = month_borrow_common ( y, m )

    days = month_length_common ( y, m )

    d = d + days

  return y, m, d

def day_carry_common ( y, m, d ):

#*****************************************************************************80
#
## DAY_CARRY_COMMON carries days to months in a Common date.
#
#  Discussion:
#
#    While ( number of days in M ) < D:
#      decrease the day D by the number of days in the month M;
#      increase M by 1;
#      if necessary, adjust Y.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, the YMD date.
#    On output, D is between 1 and the number of days in M.
#

#
#  If the date is in the transition month, deflate it,
#  so we can perform ordinary arithmetic.
#
  y, m, d = deflate_common ( y, m, d );

  days = month_length_common ( y, m )

  while ( days < d ):

    d = d - days
    m = m + 1
    days = month_length_common ( y, m )
#
#  Make sure the month isn't too big.
#
    y, m = month_carry_common ( y, m )
#
#  If the date is in the transition month, inflate it.
#
  y, m, d = inflate_common ( y, m, d )

  return y, m, d

def day_list_common ( y1, m1, d1, y2, m2, d2 ):

#*****************************************************************************80
#
## DAY_LIST_COMMON prints a list of days between two dates.
#
#  Discussion:
#
#    Given the dates of September 25, 2005 and October 2, 2005,
#    the routine should print out:
#
#    Sun, Sep 25 2005 -
#    Mon, Sep 26 2005 -
#    Tue, Sep 27 2005 -
#    Wed, Sep 28 2005 -
#    Thu, Sep 29 2005 -
#    Fri, Sep 30 2005 -
#    Sat, Oct 01 2005 -
#    Sun, Oct 02 2005 -
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y1, M1, D1, the first date.
#
#    Input, integer Y2, M2, D2, the second date.
#
  y = y1
  m = m1
  d = d1
  f = 0.0

  cmp = '<'

  while ( cmp != '>' ):

    w = ymdf_to_weekday_common ( y, m, d, f )

    w_name = weekday_to_name_common3 ( w )

    m_name = month_to_month_name_common3 ( m )

    print ( '%3s, %3s %02d %4d -' % ( w_name, m_name, d, y ) )

    y, m, d, f = ymdf_next_common ( y, m, d, f )

    cmp = ymdf_compare ( y, m, d, f, y2, m2, d2, f )

  return

def day_list_common_test ( ):

#*****************************************************************************80
#
## DAY_LIST_COMMON_TEST tests DAY_LIST_COMMON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
  d1 = 1
  d2 = 31
  m1 = 9
  m2 = 12
  y1 = 2012
  y2 = 2012

  print ( '' )
  print ( 'DAY_LIST_COMMON_TEST' )
  print ( '  DAY_LIST_COMMON prints a list of days between' )
  print ( '  two given YMD dates in the common calendar.' )
  print ( '' )
  s = ymd_to_s_common ( y1, m1, d1 )
  print ( '  Initial date: %s' % ( s ) )
  s = ymd_to_s_common ( y2, m2, d2 )
  print ( '  Final date:   %s' % ( s ) )
  print ( '\n' )

  day_list_common ( y1, m1, d1, y2, m2, d2 )

  return

def deflate_common ( y, m, d ):

#*****************************************************************************80
#
## DEFLATE_COMMON "deflates" dates in the Common Calendar transition month.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, the YMD date.
#
  if ( y == 1582 ):
    if ( m == 10 ):
      if ( 15 <= d ):
        d = d - 10

  return y, m, d

def easter_gregorian_ds ( y ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_DS computes the month and day of Easter for a Gregorian year.
#
#  Example:
#
#    Input:
#
#      Y = 2000
#
#    Output:
#
#      M = 4
#      D = 23
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Duffett-Smith,
#    Practical Astronomy With Your Calculator,
#    Third Edition,
#    Cambridge University Press, 1996,
#    ISBN: 0-521-35699-7,
#    LC: QB62.5.D83.
#
#  Parameters:
#
#    Input, integer Y, the year, which must be 1583 or greater.
#    (The formula is only valid for years after the Gregorian calendar
#    was adopted.)
#
#    Output, integer M, D, the month and day of Easter.
#
  if ( y <= 0 ):
    m = -1;
    d = -1;
    return m, d

  a = year_to_golden_number ( y )

  a = a - 1

  b = ( y // 100 )
  c = ( y % 100 )

  dd = ( b // 4 )
  e = ( b % 4 )

  f = ( ( b + 8 ) // 25 )
  g = ( ( b - f + 1 ) // 3 )
  h = ( ( 19 * a + b - dd - g + 15 ) % 30 )

  i = ( c // 4 )
  k = ( c % 4 )

  l = ( ( 32 + 2 * e + 2 * i - h - k ) % 7 )
  mm = ( ( a + 11 * h + 22 * l ) // 451 )

  m = ( ( h + l - 7 * mm + 114 ) // 31 )
  d = ( ( h + l - 7 * mm + 114 ) % 31 ) + 1

  return m, d

def easter_gregorian_ds_test ( ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_DS_TEST tests EASTER_GREGORIAN_DS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_test = 10
  d_test = np.array ( \
    [   30,   12,    4,   23,   15,   31,   20,   11,   27,   16 ] )
  m_test = np.array ( \
    [    3,    4,    4,    4,    4,    3,    4,    4,    3,    4 ] )
  y_test = np.array ( \
    [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_GREGORIAN_DS_TEST' )
  print ( '  For the Gregorian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_GREGORIAN_DS uses Duffett-Smith\'s algorithm.' )

  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT:  %s' % ( s ) )

    m, d = easter_gregorian_ds ( y )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  COMPUTED: %s' % ( s ) )

  return

def easter_gregorian_egr ( y ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_EGR computes the month and day of Easter for a Common year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Richards,
#    Algorithm O,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, page 375.
#
#  Parameters:
#
#    Input, integer Y, the year.
#
#    Output, integer M, D, the month and day of Easter.
#
  if ( y <= 0 ):
    m = -1
    d = -1
    return m, d

  p = y + ( y // 4 ) - ( y // 100 ) + ( y // 400 ) - 1
  n = 7 - ( p % 7 )
  h = ( y // 100 )
  q = h - ( h // 4 )
  g = 1 + ( y % 19 )
  e = ( ( 57 + 11 * g - q + ( ( h - ( ( h - 17 ) // 25 ) ) // 3 ) ) % 30 )
  u = ( ( 53 - e ) % 30 )
  vp = ( ( g - 1 + 11 * u ) // 319 )
  r = 22 + u - vp
  c = i4_wrap ( r + 3, 1, 7 )
  s = r + ( ( 7 + n - c ) % 7 )

  m = 3 + ( s // 32 )
  d = i4_wrap ( s, 1, 31 )

  return m, d

def easter_gregorian_egr_test ( ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_EGR_TEST tests EASTER_GREGORIAN_EGR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_test = 10
  d_test = np.array ( \
    [   30,   12,    4,   23,   15,   31,   20,   11,   27,   16 ] )
  m_test = np.array ( \
    [    3,    4,    4,    4,    4,    3,    4,    4,    3,    4 ] )
  y_test = np.array ( \
    [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_GREGORIAN_EGR_TEST' )
  print ( '  For the Gregorian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_GREGORIAN_EGR uses Richards\'s algorithm #1.' )

  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT:  %s' % ( s ) )

    m, d = easter_gregorian_egr ( y )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  COMPUTED: %s' % ( s ) )

  return

def easter_gregorian_egr2 ( y ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_EGR2 computes the month and day of Easter for a Common year.
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
#  Reference:
#
#    Edward Richards,
#    Algorithm P,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, page 376.
#
#  Parameters:
#
#    Input, integer Y, the year.
#
#    Output, integer M, D, the month and day of Easter.
#
  if ( y <= 0 ):
    m = -1
    d = -1
    return m, d

  a = ( y // 100 )
  b = a - ( a // 4 )
  c = ( y % 19 )
  d = ( ( 15 + 19 * c + b - ( ( a - ( ( a - 17 ) // 25 ) ) // 3 ) ) % 30 )
  e = d - ( ( c + 11 * d ) // 319 )
  s = 22 + e + ( ( 140004 - y - ( y // 4 ) + b - e ) % 7 )

  m = 3 + ( s // 32 )
  d = i4_wrap ( s, 1, 31 )

  return m, d

def easter_gregorian_egr2_test ( ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_EGR2_TEST tests EASTER_GREGORIAN_EGR2.
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
  import numpy as np

  n_test = 10
  d_test = np.array ( \
    [   30,   12,    4,   23,   15,   31,   20,   11,   27,   16 ] )
  m_test = np.array ( \
    [    3,    4,    4,    4,    4,    3,    4,    4,    3,    4 ] )
  y_test = np.array ( \
    [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_GREGORIAN_EGR2_TEST' )
  print ( '  For the Gregorian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_GREGORIAN_EGR2 uses Richards\'s algorithm #2.' )

  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT:  %s' % ( s ) )

    m, d = easter_gregorian_egr2 ( y )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  COMPUTED: %s' % ( s ) )

  return

def easter_gregorian_knuth ( y ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_KNUTH computes the month and day of Easter for a Gregorian year.
#
#  Discussion:
#
#    Knuth attributes the algorithm to Aloysius Lilius and Christopher Clavius
#    in the late 16th century.  The algorithm is for use with the Gregorian
#    calendar.
#
#  Example:
#
#    Input:
#
#      Y = 2000
#
#    Output:
#
#      M = 4
#      D = 23
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
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1: Fundamental Algorithms,
#    Addison Wesley, 1968, pages 155-156.
#
#    Donald Knuth,
#    The Calculation of Easter,
#    Communications of the ACM,
#    Volume 5, Number 4, April 1962, pages 209-210.
#
#    Thomas O'Beirne,
#    Puzzles and Paradoxes,
#    Oxford University Press, 1965, chapter 10.
#
#  Parameters:
#
#    Input, integer Y, the year, which must be 1583 or greater.
#    (The formula is only valid for years after the Gregorian calendar
#    was adopted.)
#
#    Output, integer M, D, the month and day of Easter.
#
  if ( y <= 0 ):
    m = -1
    d = -1
    return m, d
#
#  E1: Set the golden number of the year in the 19-year Metonic cycle.
#
  g = year_to_golden_number ( y )
#
#  E2: Set the century.
#
  c = ( y // 100 ) + 1
#
#  E3: Corrections.
#  X is the number of years divisible by 100 in which leap year was dropped.
#  Z is a special correction to synchronize Easter with the moon's orbit.
#
  x = ( 3 * c // 4 ) - 12
  z = ( ( 8 * c + 5 ) // 25 ) - 5
#
#  E4: Find Sunday.
#
  dd = ( 5 * y // 4 ) - x - 10
#
#  E5: Epact
#
  e = i4_modp ( 11 * g + 20 + z - x, 30 )

  if ( ( e == 25 and 11 < g ) or ( e == 24 ) ):
    e = e + 1
#
#  E6: Find the full moon.
#
  n = 44 - e
  if ( n < 21 ):
    n = n + 30
#
#  E7: Advance to Sunday.
#
  n = n + 7 - ( ( dd + n) % 7 )
#
#  E8: Get month.
#
  if ( 31 < n ):
    d = n - 31
    m = 4
  else:
    d = n
    m = 3

  return m, d

def easter_gregorian_knuth_test ( ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_KNUTH_TEST tests EASTER_GREGORIAN_KNUTH.
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
  import numpy as np

  n_test = 10
  d_test = np.array ( \
    [   30,   12,    4,   23,   15,   31,   20,   11,   27,   16 ] )
  m_test = np.array ( \
    [    3,    4,    4,    4,    4,    3,    4,    4,    3,    4 ] )
  y_test = np.array ( \
    [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_GREGORIAN_KNUTH_TEST' )
  print ( '  For the Gregorian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_GREGORIAN_KNUTH uses Knuth\'s algorithm.' )

  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT:  %s' % ( s ) )

    m, d = easter_gregorian_knuth ( y )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  COMPUTED: %s' % ( s ) )

  return

def easter_gregorian_stewart ( y ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_STEWART computes the month and day of Easter for a Gregorian year.
#
#  Example:
#
#    Y = 2001
#
#    A = 6
#    B = 20
#    C = 1
#    DD = 5
#    E = 0
#    G = 6
#    H = 18
#    MM = 0
#    J = 0
#    K = 1
#    L = 6
#    M = 4
#    D = 15
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
#  Reference:
#
#    Thomas O'Beirne,
#    Puzzles and Paradoxes,
#    Oxford University Press, 1965.
#
#    Ian Stewart,
#    Easter is a Quasicrystal,
#    Scientific American,
#    March 2001, pages 80-83.
#
#  Parameters:
#
#    Input, integer Y, the year.
#
#    Output, integer M, D, the month and day of Easter.
#
  a = ( y % 19 )
  b = ( y // 100 )
  c = ( y % 100 )
  dd = ( b // 4 )
  e = ( b % 4 )
  g = ( ( 8 * b + 13 ) // 25 )
  h = ( ( 19 * a + b - dd - g + 15 ) % 30 )
  mm = ( ( a + 11 * h ) // 319 )
  j = ( c // 4 )
  k = ( c % 4 )
  l = ( ( 2 * e + 2 * j - k - h + mm + 32 )% 7 )

  m = ( ( h - mm + l + 90 ) // 25 )
  d = ( ( h - mm + l + m + 19) % 32 )

  return m, d

def easter_gregorian_stewart_test ( ):

#*****************************************************************************80
#
## EASTER_GREGORIAN_STEWART_TEST tests EASTER_GREGORIAN_STEWART.
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
  import numpy as np

  n_test = 10
  d_test = np.array ( \
    [   30,   12,    4,   23,   15,   31,   20,   11,   27,   16 ] )
  m_test = np.array ( \
    [    3,    4,    4,    4,    4,    3,    4,    4,    3,    4 ] )
  y_test = np.array ( \
    [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_GREGORIAN_STEWART_TEST' )
  print ( '  For the Gregorian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_GREGORIAN_STEWART uses Stewart\'s algorithm.' )

  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT:  %s' % ( s ) )

    m, d = easter_gregorian_stewart ( y )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  COMPUTED: %s' % ( s ) )

  return

def easter_julian_egr ( y ):

#*****************************************************************************80
#
## EASTER_JULIAN_EGR computes the date of Easter in the Julian calendar.
#
#  Discussion:
#
#    This computation for the date of Easter uses the Dionysian
#    canon that applied to the Julian calendar.  The determination
#    of the date of Easter changed at the same time that the calendar
#    was modified to use the Gregorian system.
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
#  Reference:
#
#    Edward Richards,
#    Algorithm M,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, page 365.
#
#  Parameters:
#
#    Input, integer Y, the year.
#
#    Output, integer M, D, the month and day of the Julian
#    calendar on which Easter occurs.
#
  if ( y <= 0 ):
    m = -1
    d = -1
    return m, d

  p = y + ( y // 4 ) + 4
  n = 7 - ( p % 7 )

  e = year_to_epact_julian ( y )

  r = 22 + ( ( 53 - e ) % 30 )

  c = i4_wrap ( r + 3, 1, 7 )

  s = r + ( ( 7 + n - c ) % 7 )

  m = 3 + ( s // 32 )
#
#  Use wrapping so that 1 <= D <= 31.
#
  d = i4_wrap ( s, 1, 31 )

  return m, d

def easter_julian_egr_test ( ):

#*****************************************************************************80
#
## EASTER_JULIAN_EGR_TEST tests EASTER_JULIAN_EGR.
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
  import numpy as np

  n_test = 10
  d_test = np.array ( [ 27,    19,   11,  30,   15,    5,   27,   11,    1,   23 ] )
  m_test = np.array ( [ 4,     4,    4,    4,    4,    5,    4,    4,    5,    4 ] )
  y_test = np.array ( [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_JULIAN_EGR_TEST' )
  print ( '  For the Julian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_JULIAN_EGR uses Richards''s algorithm #1.' )
 
  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]
    f = 0.5

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT (Gregorian): %s' % ( s ) )

    jed = ymdf_to_jed_gregorian ( y, m, d, f )
    y, m, d, f = jed_to_ymdf_julian ( jed )

    s = ymd_to_s_julian ( y, m, d )
    print ( '  CORRECT (Julian):    %s' % ( s ) )

    m, d = easter_julian_egr ( y )
    s = ymd_to_s_julian ( y, m, d )
    print ( '  COMPUTED             %s' % ( s ) )

  return

def easter_julian_egr2 ( y ):

#*****************************************************************************80
#
## EASTER_JULIAN_EGR2 computes the date of Easter in the Julian calendar.
#
#  Discussion:
#
#    This computation for the date of Easter uses the Dionysian
#    canon that applied to the Julian calendar.  The determination
#    of the date of Easter changed at the same time that the calendar
#    was modified to use the Gregorian system.
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
#  Reference:
#
#    Edward Richards,
#    Algorithm N,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, page 365.
#
#  Parameters:
#
#    Input, integer Y, the year.
#
#    Output, integer M, D, the month and day of the Julian calendar
#    on which Easter occurs.
#
  if ( y <= 0 ):
    m = -1
    d = -1
    return m, d

  a = year_to_golden_number ( y )
  a = a - 1

  b = 22 + ( ( 225 - 11 * a ) % 30 )
  s = b + ( ( 56 + 6 * y - ( y // 4 ) - b ) % 7 )

  m = 3 + ( s // 32 )
#
#  Use wrapping to ensure that 1 <= D <= 31.
#
  d = i4_wrap ( s, 1, 31 )

  return m, d

def easter_julian_egr2_test ( ):

#*****************************************************************************80
#
## EASTER_JULIAN_EGR2_TEST tests EASTER_JULIAN_EGR2.
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
  import numpy as np

  n_test = 10
  d_test = np.array ( [ 27,    19,   11,  30,   15,    5,   27,   11,    1,   23 ] )
  m_test = np.array ( [ 4,     4,    4,    4,    4,    5,    4,    4,    5,    4 ] )
  y_test = np.array ( [ 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 ] )

  print ( '' )
  print ( 'EASTER_JULIAN_EGR2_TEST' )
  print ( '  For the Julian calendar,' )
  print ( '  for a given year, compute the day and month of Easter.' )
  print ( '  EASTER_JULIAN_EGR2 uses Richards''s algorithm #2.' )
 
  for i in range ( 0, n_test ):

    y = y_test[i]
    m = m_test[i]
    d = d_test[i]
    f = 0.5

    print ( '' )
    s = ymd_to_s_gregorian ( y, m, d )
    print ( '  CORRECT (Gregorian): %s' % ( s ) )

    jed = ymdf_to_jed_gregorian ( y, m, d, f )
    y, m, d, f = jed_to_ymdf_julian ( jed )

    s = ymd_to_s_julian ( y, m, d )
    print ( '  CORRECT (Julian):    %s' % ( s ) )

    m, d = easter_julian_egr2 ( y )
    s = ymd_to_s_julian ( y, m, d )
    print ( '  COMPUTED             %s' % ( s ) )

  return

def epoch_to_jed_akbar ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_AKBAR: epoch of the Akbar calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2289425.5

  return jed

def epoch_to_jed_alexandrian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ALEXANDRIAN: epoch of the Alexandrian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1713262.5

  return jed

def epoch_to_jed_armenian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ARMENIAN: epoch of the Armenian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1922867.5

  return jed

def epoch_to_jed_bahai ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_BAHAI: epoch of the Bahai calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2394646.5

  return jed

def epoch_to_jed_bessel ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_BESSEL: epoch of the Bessel calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2415020.31352

  return jed

def epoch_to_jed_chinese ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_CHINESE: epoch of the Chinese calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 758325.5

  return jed

def epoch_to_jed_common ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_COMMON: epoch of the Common calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1721423.5

  return jed

def epoch_to_jed_coptic ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_COPTIC: epoch of the Coptic calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1825029.5

  return jed

def epoch_to_jed_datenum ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_DATENUM: epoch of the MATLAB DATENUM calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1721058.5

  return jed

def epoch_to_jed_deccan ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_DECCAN: epoch of the Fasli Deccan calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1936747.5

  return jed

def epoch_to_jed_eg_civil ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_EG_CIVIL: epoch of the Egyptian Civil calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1448637.5

  return jed

def epoch_to_jed_eg_lunar ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_EG_LUNAR: epoch of the Egyptian Lunar calendar as a JED.
#
#  Discussion:
#
#    This is just a fake value, making the Egyptian Lunar calendar start
#    at the same data as the Egyptian Civil calendar.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1448637.5

  return jed

def epoch_to_jed_english ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ENGLISH: epoch of the English calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1721423.5

  return jed

def epoch_to_jed_ethiopian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ETHIOPIAN: epoch of the Ethiopian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1724220.5

  return jed

def epoch_to_jed_gps ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_GPS: epoch of the GPS calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2444244.5

  return jed

def epoch_to_jed_greek ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_GREEK: epoch of the Greek calendar as a JED.
#
#  Discussion:
#
#    The Greek Olympiad calendar began on 9 July 776 BC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1438178.5

  return jed

def epoch_to_jed_gregorian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_GREGORIAN: epoch of the Gregorian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1721425.5

  return jed

def epoch_to_jed_hebrew ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_HEBREW: epoch of the Hebrew calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 347998.5

  return jed

def epoch_to_jed_hindu_lunar ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_HINDU_LUNAR: epoch of the Hindu lunar calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1741959.5

  return jed

def epoch_to_jed_hindu_solar ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_HINDU_SOLAR: epoch of the Hindu solar calendar as a JED.
#
#  Discussion:
#
#    This is the beginning of the Kali Yuga era.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 588465.75

  return jed

def epoch_to_jed_islamic_a ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ISLAMIC_A: epoch of the Islamic A calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1948438.5

  return jed

def epoch_to_jed_islamic_b ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ISLAMIC_B: epoch of the Islamic B calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1948439.5

  return jed

def epoch_to_jed_jed ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_JED: epoch of the JED as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 0.0

  return jed

def epoch_to_jed_jelali ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_JELALI: epoch of the Jelali calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2114872.5

  return jed

def epoch_to_jed_julian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_JULIAN: epoch of the Julian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1721423.5

  return jed

def epoch_to_jed_khwarizmian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_KHWARIZMIAN: epoch of the Khwarizmian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1952067.5

  return jed

def epoch_to_jed_macedonian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_MACEDONIAN: epoch of the Macedonian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1607708.5

  return jed

def epoch_to_jed_mayan_long ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_MAYAN_LONG: epoch of the Mayan long count calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 584282.5

  return jed

def epoch_to_jed_mjd ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_MJD: epoch of the MJD calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2400000.5

  return jed

def epoch_to_jed_nyt ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_NYT: epoch of the NYT calendar as a JED.
#
#  Discussion:
#
#    The "epoch" of the NYT calendar is the mythical date when issue "0"
#    would have been printed, namely, a tad past midnight, 17 September 1851.
#
#    Volume #1, Issue #1 was printed on 18 September 1851.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2397382.5

  return jed

def epoch_to_jed_nyt_50000 ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_NYT_50000: epoch of the NYT_50000 calendar as a JED.
#
#  Discussion:
#
#    The "epoch" of the NYT_50000 calendar is the date when issue "50,000"
#    was printed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2449790.5

  return jed

def epoch_to_jed_persian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_PERSIAN: epoch of the Persian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1952062.5

  return jed

def epoch_to_jed_persian_solar ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_PERSIAN_SOLAR: epoch of the Persian solar calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1948320.5

  return jed

def epoch_to_jed_rd ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_RD: epoch of the RD calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1721425.5

  return jed

def epoch_to_jed_republican ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_REPUBLICAN: epoch of the Republican calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2375839.5

  return jed

def epoch_to_jed_roman ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ROMAN: epoch of the Roman calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#     10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1446389.5

  return jed

def epoch_to_jed_saka ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_SAKA: epoch of the Saka calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1749994.5

  return jed

def epoch_to_jed_soor_san ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_SOOR_SAN: epoch of the Fasli Soor San calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1940351.5

  return jed

def epoch_to_jed_syrian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_SYRIAN: epoch of the Syrian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1607738.5

  return jed

def epoch_to_jed_unix ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_UNIX: epoch of the UNIX calendar as a JED.
#
#  Discussion:
#
#    The UNIX Epoch is taken to be the first second of 1 January 1970.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2440587.50

  return jed

def epoch_to_jed_y2k ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_Y2K: epoch of the Y2K calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 2451544.5

  return jed

def epoch_to_jed_zoroastrian ( ):

#*****************************************************************************80
#
## EPOCH_TO_JED_ZOROASTRIAN: epoch of the Zoroastrian calendar as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the epoch.
#
  jed = 1862836.5

  return jed

def gps_to_jed ( c, w, s ):

#*****************************************************************************80
#
## GPS_TO_JED converts a GPS date to a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer C, integer W, real S,
#    the GPS cycle/week/second date.
#
#    Output, real JED, the corresponding Julian Ephemeris Date.
#
  jed_epoch = epoch_to_jed_gps ( )

  d = float ( 7 * ( 1024 * c + w ) ) + s / ( 24.0 * 60.0 * 60.0 )

  jed = jed_epoch + d

  return jed

def gps_to_jed_test ( ):

#*****************************************************************************80
#
## GPS_TO_JED_TEST tests GPS_TO_JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'GPS_TO_JED_TEST' )
  print ( '  GPS_TO_JED: GPS => JED' )
  print ( '' )
  print ( '   JED (in)       GPS (C/W/S)                   JED (out)' )
  print ( '' )

  jed_epoch = epoch_to_jed_gps ( )

  i = 0

  while ( True ):

    i = i + 1
    jed1 = jed_test ( i )

    if ( jed1 < 0.0 ):
      break

    if ( jed_epoch <= jed1 ):

      c2, w2, sec2 = jed_to_gps ( jed1 )

      jed3 = gps_to_jed ( c2, w2, sec2 )

      print ( '  %11.2f  %d/%d/%9.2f GPS  %11.2f' % ( jed1, c2, w2, sec2, jed3 ) )

  return

def hour_borrow_common ( y, m, d, h ):

#*****************************************************************************80
#
## HOUR_BORROW_COMMON "borrows" a day of hours.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, the year, month, day
#    and hour of the date.  The value of H is presumably negative, and
#    so hours will be "borrowed" to make H positive.
#
  while ( h <= 0 ):

    h = h + 24
    d = d - 1

    y, m, d = day_borrow_common ( y, m, d )

  return y, m, d, h

def hour_carry_common ( y, m, d, h ):

#*****************************************************************************80
#
## HOUR_CARRY_COMMON is given a YMDH date, and carries hours to days.
#
#  Algorithm:
#
#    While 24 < H:
#
#      decrease H by the number of hours in a day;
#      increase D by 1;
#      if necessary, adjust M and Y.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, the year, month, day
#    and hour of the date.  On input, H is presumably 24 or greater.
#
  while ( 24 < h ):

    h = h - 24
    d = d + 1

    y, m, d = day_carry_common ( y, m, d )

  return y, m, d, h 

def i4_modp ( i, j ):

#*****************************************************************************80
#
## I4_MODP returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = I4_MODP ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, I4_MODP(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  I4_MODP    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number to be divided.
#
#    Input, integer J, the number that divides I.
#
#    Output, integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  from sys import exit

  if ( j == 0 ):
    print ( '' )
    print ( 'I4_MODP - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    exit ( 'I4_MODP - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## I4_MODP_TEST tests I4_MODP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'I4_MODP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_MODP factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_MODP_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_normal_ab ( mu, sigma, seed ):

#*****************************************************************************80
#
## I4_NORMAL_AB returns a scaled pseudonormal I4.
#
#  Discussion:
#
#    The normal probability distribution function (PDF) is sampled,
#    with mean MU and standard deviation SIGMA.
#
#    The result is rounded to the nearest integer.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, the mean of the PDF.
#
#    Input, real SIGMA, the standard deviation of the PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer VALUE, a normally distributed
#    random value.
#
#    Output, integer SEED, an updated seed for the random
#    number generator.
#
  import numpy as np

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )
  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )
  value = int ( mu + sigma * value )

  return value, seed

def i4_normal_ab_test ( ):

#*****************************************************************************80
#
## I4_NORMAL_AB_TEST tests I4_NORMAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_NORMAL_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_NORMAL_AB computes integer pseudonormal values with' )
  print ( '  mean MU and standard deviation SIGMA.' )

  mu = 10.0
  sigma = 2.0
  seed = 123456789

  print ( '' )
  print ( '  MU = %g' % ( mu ) )
  print ( '  SIGMA = %g' % ( sigma ) )
  print ( '  SEED = %d' % ( seed ) )
  print ( '' )
  for i in range ( 0, 10 ):
    r, seed = i4_normal_ab ( mu, sigma, seed )
    print ( '  %2d  %12d' % ( i, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_NORMAL_AB_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## I4_WRAP forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer IVAL, an integer value.
#
#    Input, integer ILO, IHI, the desired bounds for the integer value.
#
#    Output, integer VALUE, a "wrapped" version of IVAL.
#
  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## I4_WRAP_TEST tests I4_WRAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'I4_WRAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_WRAP forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  I4_WRAP(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_WRAP_TEST' )
  print ( '  Normal end of execution.' )
  return

def inflate_common ( y, m, d ):

#*****************************************************************************80
#
## INFLATE_COMMON "inflates" dates in the Common Calendar transition month.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, the YMD date.
#
  if ( y == 1582 ):
    if ( m == 10 ):
      if ( 5 <= d ):
        d = d + 10

  return y, m, d

def jed_ce_values ( n_data ):

#*****************************************************************************80
#
## JED_CE_VALUES returns the Common Era dates for Julian Ephemeris Dates.
#
#  Discussion:
#
#    The JED (Julian Ephemeris Date) is a calendrical system which counts days,
#    starting from noon on 1 January 4713 BCE.
#
#    The CE or Common Era is the day, month and year under the
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
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold and Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real JED, the Julian Ephemeris Date.
#
#    Output, integer Y, M, D, the Common Era date.
#
#    Output, real F, the fractional part of the day.
#
  import numpy as np

  n_max = 51

  d_vec = np.array ( ( \
    1, \
    2, \
    26, \
    8, \
    6, \
    18, \
    8, \
    9, \
    1, \
    26, \
    26, \
    1, \
    1, \
    29, \
    31, \
    1, \
    3, \
    3, \
    29, \
    24, \
    24, \
    29, \
    3, \
    11, \
    12, \
    24, \
    19, \
    15, \
    16, \
    16, \
    21, \
    17, \
    9, \
    4, \
    15, \
    4, \
    13, \
    14, \
    18, \
    22, \
    21, \
    24, \
    17, \
    31, \
    1, \
    6, \
    25, \
    1, \
    9, \
    23, \
    1 ))

  f_vec = np.array ( ( \
    0.50, \
    0.50, \
    0.50, \
    0.00, \
    0.00, \
    0.25, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.50, \
    0.50, \
    0.00, \
    0.50, \
    0.50, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.81, \
    0.00, \
    0.00, \
    0.00, \
    0.00, \
    0.33, \
    0.00, \
    0.50 ))

  jed_vec = np.array ( ( \
           0.00, \
           1.00, \
      259261.00, \
      347998.50, \
      584282.50, \
      588465.75, \
      758325.50, \
     1438178.50, \
     1446389.50, \
     1448637.50, \
     1448637.50, \
     1607708.50, \
     1607738.50, \
     1713262.50, \
     1721422.50, \
     1721423.50, \
     1721425.50, \
     1721425.50, \
     1724220.50, \
     1741959.50, \
     1749994.50, \
     1825029.50, \
     1862836.50, \
     1922867.50, \
     1936747.50, \
     1940351.50, \
     1948320.50, \
     1948438.50, \
     1948439.50, \
     1952062.50, \
     1952067.50, \
     2114872.50, \
     2289425.50, \
     2299160.00, \
     2299161.00, \
     2333269.50, \
     2361221.00, \
     2361222.00, \
     2372547.50, \
     2375839.50, \
     2394646.50, \
     2394710.50, \
     2400000.50, \
     2415020.31, \
     2440587.50, \
     2444244.50, \
     2450138.50, \
     2451544.50, \
     2453073.83, \
     2456284.50, \
     2913943.00 ))

  m_vec = np.array ( ( \
     1, \
     1, \
     10, \
     10, \
     9, \
     2, \
     3, \
     7, \
     1, \
     2, \
     2, \
     9, \
     10, \
     8, \
     12, \
     1, \
     1, \
     1, \
     8, \
     3, \
     3, \
     8, \
     3, \
     7, \
     7, \
     5, \
     3, \
     7, \
     7, \
     6, \
     6, \
     3, \
     2, \
     10, \
     10, \
     3, \
     9, \
     9, \
     9, \
     9, \
     3, \
     5, \
     11, \
     12, \
     1, \
     1, \
     2, \
     1, \
     3, \
     12, \
     1 ))

  y_vec = np.array ( ( \
    -4713, \
    -4713, \
    -4004, \
    -3761, \
    -3114, \
    -3102, \
    -2637, \
     -776, \
     -753, \
     -747, \
     -747, \
     -312, \
     -312, \
      -23, \
       -1, \
        1, \
        1, \
        1, \
        8, \
       57, \
       79, \
      284, \
      388, \
      552, \
      590, \
      600, \
      622, \
      622, \
      622, \
      632, \
      632, \
     1078, \
     1556, \
     1582, \
     1582, \
     1676, \
     1752, \
     1752, \
     1783, \
     1792, \
     1844, \
     1844, \
     1858, \
     1899, \
     1970, \
     1980, \
     1996, \
     2000, \
     2004, \
     2012, \
     3266 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    jed = 0.0
    y = 0
    m = 0
    d = 0
    f = 0.0
  else:
    jed = jed_vec[n_data]
    y = y_vec[n_data]
    m = m_vec[n_data]
    d = d_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, jed, y, m, d, f

def jed_ce_values_test ( ):

#*****************************************************************************80
#
## JED_CE_VALUES_TEST demonstrates the use of JED_CE_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JED_CE_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JED_CE_VALUES stores of the YMDF CE calendar date for a given JED' )
  print ( '' )
  print ( '         JED         Y       M       D           F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, jed, y, m, d, f = jed_ce_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12.1f  %6d  %6d  %6d  %12.2g' % ( jed, y, m, d, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JED_CE_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def jed_is_legal ( jed ):

#*****************************************************************************80
#
## JED_IS_LEGAL checks a Julian Ephemeris Date.
#
#  Discussion:
#
#    The routine returns an error if JED < 0, although there is no
#    reason why such dates are invalid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, logical VALUE, is TRUE if JED is legal, and FALSE otherwise.
#
  if ( 0.0 <= jed ):
    value = True
  else:
    value = False

  return value

def jed_is_legal_test ( ):

#*****************************************************************************80
#
## JED_IS_LEGAL_TEST tests JED_IS_LEGAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JED_IS_LEGAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JED_IS_LEGAL returns TRUE if JED is a legal JED value' )
  print ( '' )
  print ( '         JED    JED_IS_LEGAL' )
  print ( '' )

  for jed in [ -100, -1, 0, 1, 1.5, 100, 50000 ]:
    legal = jed_is_legal ( jed )
    if ( legal ):
      print ( '  %12.1f  True' % ( jed ) )
    else:
      print ( '  %12.1f  False' % ( jed ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JED_IS_LEGAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def jed_mjd_values ( n_data ):

#*****************************************************************************80
#
## JED_MJD_VALUES returns the MJD for Julian Ephemeris Dates.
#
#  Discussion:
#
#    The JED (Julian Ephemeris Date) is a calendrical system which counts days,
#    starting from noon on 1 January 4713 BCE.
#
#    The MJD (Modified Julian Day) counts days starting from midnight, 
#    17 November 1858.  This essentially subtracts 2400000.5 days from the JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold and Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real JED, the Julian Ephemeris Date.
#
#    Output, real MJD, the Modified Julian Ephemeris Date.
#
  import numpy as np

  n_max = 33

  jed_vec = np.array ( ( \
     1507231.5E+00, \
     1660037.5E+00, \
     1746893.5E+00, \
     1770641.5E+00, \
     1892731.5E+00, \
     1931579.5E+00, \
     1974851.5E+00, \
     2091164.5E+00, \
     2121509.5E+00, \
     2155779.5E+00, \
     2174029.5E+00, \
     2191584.5E+00, \
     2195261.5E+00, \
     2229274.5E+00, \
     2245580.5E+00, \
     2266100.5E+00, \
     2288542.5E+00, \
     2290901.5E+00, \
     2323140.5E+00, \
     2334848.5E+00, \
     2348020.5E+00, \
     2366978.5E+00, \
     2385648.5E+00, \
     2392825.5E+00, \
     2416223.5E+00, \
     2425848.5E+00, \
     2430266.5E+00, \
     2430833.5E+00, \
     2431004.5E+00, \
     2448698.5E+00, \
     2450138.5E+00, \
     2465737.5E+00, \
     2486076.5E+00 ))

  mjd_vec = np.array ( ( \
     -892769.0E+00, \
     -739963.0E+00, \
     -653107.0E+00, \
     -629359.0E+00, \
     -507269.0E+00, \
     -468421.0E+00, \
     -425149.0E+00, \
     -308836.0E+00, \
     -278491.0E+00, \
     -244221.0E+00, \
     -225971.0E+00, \
     -208416.0E+00, \
     -204739.0E+00, \
     -170726.0E+00, \
     -154420.0E+00, \
     -133900.0E+00, \
     -111458.0E+00, \
     -109099.0E+00, \
      -76860.0E+00, \
      -65152.0E+00, \
      -51980.0E+00, \
      -33022.0E+00, \
      -14352.0E+00, \
       -7175.0E+00, \
       16223.0E+00, \
       25848.0E+00, \
       30266.0E+00, \
       30833.0E+00, \
       31004.0E+00, \
       48698.0E+00, \
       50138.0E+00, \
       65737.0E+00, \
       86076.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    jed = 0.0
    mjd = 0.0
  else:
    jed = jed_vec[n_data]
    mjd = mjd_vec[n_data]
    n_data = n_data + 1

  return n_data, jed, mjd

def jed_mjd_values_test ( ):

#*****************************************************************************80
#
## JED_MJD_VALUES_TEST demonstrates the use of JED_MJD_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JED_MJD_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JED_MJD_VALUES stores values of the Modified Julian Date.' )
  print ( '' )
  print ( '    JED         MJD(JED)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, jed, mjd = jed_mjd_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( jed, mjd ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JED_MJD_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def jed_rd_values ( n_data ):

#*****************************************************************************80
#
## JED_RD_VALUES returns the RD for Julian Ephemeris Dates.
#
#  Discussion:
#
#    The JED (Julian Ephemeris Date) is a calendrical system which counts days,
#    starting from noon on 1 January 4713 BCE.
#
#    The RD is the Reingold Dershowitz Date, which counts days from
#    midnight, 1 January year 1 in the Gregorian calendar.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold and Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real JED, the Julian Ephemeris Date.
#
#    Output, real RD, the Modified Julian Ephemeris Date.
#
  import numpy as np

  n_max = 33

  jed_vec = np.array ( ( \
     1507231.5E+00, \
     1660037.5E+00, \
     1746893.5E+00, \
     1770641.5E+00, \
     1892731.5E+00, \
     1931579.5E+00, \
     1974851.5E+00, \
     2091164.5E+00, \
     2121509.5E+00, \
     2155779.5E+00, \
     2174029.5E+00, \
     2191584.5E+00, \
     2195261.5E+00, \
     2229274.5E+00, \
     2245580.5E+00, \
     2266100.5E+00, \
     2288542.5E+00, \
     2290901.5E+00, \
     2323140.5E+00, \
     2334848.5E+00, \
     2348020.5E+00, \
     2366978.5E+00, \
     2385648.5E+00, \
     2392825.5E+00, \
     2416223.5E+00, \
     2425848.5E+00, \
     2430266.5E+00, \
     2430833.5E+00, \
     2431004.5E+00, \
     2448698.5E+00, \
     2450138.5E+00, \
     2465737.5E+00, \
     2486076.5E+00 ))

  rd_vec = np.array ( ( \
    -214193.0E+00, \
     -61387.0E+00, \
      25469.0E+00, \
      49217.0E+00, \
     171307.0E+00, \
     210155.0E+00, \
     253427.0E+00, \
     369740.0E+00, \
     400085.0E+00, \
     434355.0E+00, \
     452605.0E+00, \
     470160.0E+00, \
     473837.0E+00, \
     507850.0E+00, \
     524156.0E+00, \
     544676.0E+00, \
     567118.0E+00, \
     569477.0E+00, \
     601716.0E+00, \
     613424.0E+00, \
     626596.0E+00, \
     645554.0E+00, \
     664224.0E+00, \
     671401.0E+00, \
     694799.0E+00, \
     704424.0E+00, \
     708842.0E+00, \
     709409.0E+00, \
     709580.0E+00, \
     727274.0E+00, \
     728714.0E+00, \
     744313.0E+00, \
     764652.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    jed = 0.0
    rd = 0.0
  else:
    jed = jed_vec[n_data]
    rd = rd_vec[n_data]
    n_data = n_data + 1

  return n_data, jed, rd

def jed_rd_values_test ( ):

#*****************************************************************************80
#
## JED_RD_VALUES_TEST demonstrates the use of JED_RD_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JED_RD_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JED_RD_VALUES stores values of the Reingold Dershowitz Date.' )
  print ( '' )
  print ( '    JED         RD(JED)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, jed, rd = jed_rd_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( jed, rd ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JED_RD_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def jed_test ( i ):

#*****************************************************************************80
#
## JED_TEST returns some "interesting" JED's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Bonnie Blackburn, Leofranc Holford-Stevens,
#    The Oxford Companion to the Year,
#    Oxford, 1999.
#
#    Frank Parise, editor,
#    The Book of Calendars,
#    Facts on File, Inc, 1982,
#    CE11.K4 / 529.3.
#
#    Edward Reingold, Nachum Dershowitz,
#    Calendrical Calculations, the Millennium Edition,
#    Cambridge, 2002,
#    CE12.R45 / 529.3-dc21
#
#    Edward Richards,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999.
#
#  Parameters:
#
#    Input, integer I, the test date requested.
#
#    Output, real JED, the Julian Ephemeris Date.
#    If I is less than 1, or greater than the number of test dates
#    available, JED is returned as -1.0.
#
 
#
#  JED Epoch:
#  Beginning of current Scaliger cycle.
#  Monday, Noon, 1 January 4713 BCE/Julian
#
  if ( i == 1 ):

    jed = 0.0
#
#  The day after the JED Epoch.
#  Tuesday, Noon, 2 January 4713 BCE/Julian
#
  elif ( i == 2 ):

    jed = 1.0
#
#  Archbishop James Ussher's estimate of the date of Creation,
#  (Noon), 23 October 4004 BCE/Julian
#
  elif ( i == 3 ):

    jed = 259258.000
#
#  Hebrew Epoch.
#  7 October 3761 BCE/Julian
#
  elif ( i == 4 ):

    jed = 347998.5
#
#  Mayan Long Count Epoch.
#  6 September 3114 BCE/Julian
#  (Reingold and Dershowitz)
#
  elif ( i == 5 ):

    jed = 584282.5
#
#  Hindu Solar Epoch.
#  Beginning of the Kali Yuga age.
#  18 February 3102 BCE/Julian
#
  elif ( i == 6 ):

    jed = 588465.75
#
#  Chinese Epoch.
#  8 March 2637 BCE/Julian
#
  elif ( i == 7 ):

    jed = 758325.5
#
#  Greek Olympiad Epoch
#  9 July 776 BCE/Julian
#
  elif ( i == 8 ):

    jed = 1438178.5
#
#  Roman Epoch
#  Ab Urbe Condita
#  1 January 753 BCE/Julian
#
  elif ( i == 9 ):

    jed = 1446389.5
#
#  Egyptian Civil Calendar Epoch.
#  Ascension of Nabonassar to throne of Babylon.
#  26 February 747 BCE/Julian
#
  elif ( i == 10 ):

    jed = 1448637.5
#
#  Egyptian Lunar Calendar Epoch.
#  (Don't really know where to set this...)
#  Ascension of Nabonassar to throne of Babylon.
#  26 February 747 BCE/Julian
#
  elif ( i == 11 ):

    jed = 1448637.5
#
#  Macedonian Epoch
#  1 September 312 BCE/Julian
#
  elif ( i == 12 ):

    jed = 1607708.5
#
#  Syrian Epoch
#  1 October 312 BCE/Julian
#
  elif ( i == 13 ):

    jed = 1607738.5
#
#  Alexandrian Epoch
#  29 August 23 BCE/Julian
#
  elif ( i == 14 ):

    jed = 1713262.5
#
#  "1 January, 0 BC"?  DATENUM epoch.
#
  elif ( i == 15 ):

    jed = 1721058.5
#
#  Julian Epoch MINUS ONE DAY
#  Friday, 31 December 1 BCE/Julian
#
  elif ( i == 16 ):

    jed = 1721423.5
    jed = jed - 1.0
#
#  Julian Epoch
#  Saturday, 1 January 1 CE/Julian
#
  elif ( i == 17 ):

    jed = 1721423.5
#
#  Gregorian Epoch
#  Monday, 3 January 1 CE/Julian
#  Monday, 1 January 1 Gregorian
#
  elif ( i == 18 ):

    jed = 1721425.5
#
#  RD: Reingold and Dershowitz Epoch
#  Monday, 3 January 1 CE/Julian
#  Monday, 1 January 1 Gregorian
#
  elif ( i == 19 ):

    jed = 1721425.5
#
#  Ethiopian Epoch
#  29 August 8 CE/Julian
#  (Reingold and Dershowitz)
#
  elif ( i == 20 ):

    jed = 1724220.5
#
#  Hindu Lunar Epoch, the Vikrama
#  24 March 57 CE/Julian
#  (The actual day and month are not specified by RD)
#  (Reingold and Dershowitz)
#
  elif ( i == 21 ):

    jed = 1741959.5
#
#  Saka Epoch
#  4 March 79 CE/Julian
#
  elif ( i == 22 ):

    jed = 1749994.5
#
#  Coptic Epoch
#  29 August 284 CE/Julian
#
  elif ( i == 23 ):

    jed = 1825029.5
#
#  Zoroastrian Epoch.
#  3 March 388 CE/Julian
#
  elif ( i == 24 ):

    jed = 1862836.5
#
#  Armenian Epoch
#  11 July 552 CE/Julian
#
  elif ( i == 25 ):

    jed = 1922867.5
#
#  Fasli Deccan Epoch
#  12 July 590 CE/Julian
#
  elif ( i == 26 ):

    jed = 1936747.5
#
#  Fasli Soor San Epoch
#  24 May 600 CE/Julian
#
  elif ( i == 27 ):

    jed = 1940351.5
#
#  Persian Solar Epoch
#  19 March 622 CE/Julian
#
  elif ( i == 28 ):

    jed = 1948320.5
#
#  Islamic A Epoch
#  Thursday, 15 July 622 CE/Julian
#
  elif ( i == 29 ):

    jed = 1948438.5
#
#  Islamic B Epoch
#  Friday, 16 July 622 CE/Julian
#
  elif ( i == 30 ):

    jed = 1948439.5
#
#  Yazdegerd Epoch
#  16 June 632 CE
#
  elif ( i == 31 ):

    jed = 1952062.5
#
#  Khwarizmian Epoch
#  21 June 632 CE/Julian
#
  elif ( i == 32 ):

    jed = 1952067.5
#
#  Battle of Hastings.
#  Saturday, 14 October 1066 CE/Julian.
#           (20 October 1066 Gregorian.)
#
  elif ( i == 33 ):

    jed = 2110700.5
#
#  Jelali Epoch
#  17 March 1078 CE/Julian
#
  elif ( i == 34 ):

    jed = 2114872.5
#
#  Akbar Epoch
#  9 February 1556 CE/Julian
#  19 February 1556 Gregorian
#
  elif ( i == 35 ):

    jed = 2289425.5
#
#  Common Era calendar transition:
#  Noon of the last day of Julian calendar usage.
#  Thursday, 04 October 1582 CE/English/Julian
#  Thursday, 14 October 1582 Gregorian
#
  elif ( i == 36 ):

    jed = 2299160.5
    jed = jed - 0.5
#
#  Common Era calendar transition:
#  Noon of the first day of Gregorian calendar usage.
#  Friday, 05 October 1582 English/Julian
#  Friday, 15 October 1582 CE/Gregorian
#
  elif ( i == 37 ):

    jed = 2299160.5
    jed = jed + 0.5
#
#  A day chosen by Lewis Carroll to test his day-of-the-week algorithm,
#  Wednesday, 4 March 1676 CE/Gregorian
#  Wednesday, 23 February 1676 English/Julian
#
  elif ( i == 38 ):

    jed = 2333269.5
#
#  English calendar
#  noon of the last day of Julian calendar usage.
#  02 September 1752 English/Julian
#  13 September 1752 CE/Gregorian
#
  elif ( i == 39 ):

    jed = 2361221.5
    jed = jed - 0.5
#
#  English calendar,
#  noon of the first day of Gregorian calendar usage.
#  03 September 1752 Julian
#  14 September 1752 CE/English/Gregorian
#
  elif ( i == 40 ):

    jed = 2361221.5
    jed = jed + 0.5
#
#  A day chosen by Lewis Carroll to test his day-of-the-week algorithm,
#  Thursday, 18 September 1783 CE/Gregorian
#
  elif ( i == 41 ):

    jed = 2372547.5
#
#  French Republican Epoch
#  Saturday, 11 September 1792 Julian
#  Saturday, 22 September 1792 CE/Gregorian
#
  elif ( i == 42 ):

    jed = 2375839.5
#
#  Bahai Epoch.
#  9 March 1844 Julian
#  21 March 1844 CE/Gregorian
#
  elif ( i == 43 ):

    jed = 2394646.5
#
#  Clive James Lucas test date.
#
  elif ( i == 44 ):

    jed = 2394710.50
#
#  New York Times "epoch" date,
#  fictitious Volume 1, issue #0,
#  17 September 1851
#  (issue #1 was on 18 September 1851):
#
  elif ( i == 45 ):

    jed = 2397383.50
#
#  Modified Julian Date Epoch.
#  17 November 1858 CE/Gregorian
#
  elif ( i == 46 ):

    jed = 2400000.5
#
#  NYT issue 10,000
#  24 September 1883
#
  elif ( i == 47 ):

    jed_epoch_50000 = 2449790.5
    jed = jed_epoch_50000 - 40000.0 - 88.0
#
#  Bessel Year Count Epoch.
#  1 January 1900 CE/Gregorian
#
  elif ( i == 48 ):

    jed = 2415020.31352
#
#  NYT issue 30,000
#  14 March 1940
#
  elif ( i == 49 ):

    jed_epoch_50000 = 2449790.5
    jed = jed_epoch_50000 - 20000.0 - 88.0
#
#  NYT issue 40,000
#  ???
#
  elif ( i == 50 ):

    jed_epoch_50000 = 2449790.5
    jed = jed_epoch_50000 - 10000.0 - 88.0
#
#  UNIX epoch.
#  1 January 1970 CE/Gregorian.
#
  elif ( i == 51 ):

    jed = 2440587.50
#
#  NYT issue 44027
#  ???
#
  elif ( i == 52 ):

    jed_epoch_50000 = 2449790.5
    jed = jed_epoch_50000 - 5973
#
#  NYT issue 44028
#  ???
#
  elif ( i == 53 ):

    jed_epoch_50000 = 2449790.5
    jed = jed_epoch_50000 - 5972
#
#  GPS epoch.
#  6 January 1980 CE/Gregorian
#
  elif ( i == 54 ):

    jed = 2444244.5
#
#  NYT issue 50,000
#  14 March 1995
#
  elif ( i == 55 ):

    jed_epoch_50000 = 2449790.5
    jed = jed_epoch_50000
#
#  25 February 1996
#  A Reingold/Dershowitz test date.
#
  elif ( i == 56 ):

    jed = 2450138.5
#
#  Y2K day
#  1 January 2000 CE/Gregorian
#
  elif ( i == 57 ):

    jed = 2451544.5
#
#  Today
#
  elif ( i == 58 ):

    jed = now_to_jed ( )
#
#  End of Current Mayan Great Cycle
#  21 December 2012 CE/Gregorian
#
  elif ( i == 59 ):

    jed = 2456282.5
#
#  Scaliger cycle repeats.
#  1 January 3266 CE/Gregorian
#
  elif ( i == 60 ):

    jed = 2913943.0

  else:

    jed = -1.0


  return jed

def jed_to_datenum ( jed ):

#*****************************************************************************80
#
## JED_TO_DATENUM converts a JED to a MATLAB DATENUM.
#
#  Discussion:
#
#    The MATLAB "datenum" function accepts a string defining
#    a date and returns a datenumber:
#
#      dn = datenum ( 'Aug 17 1939' )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, real DN, a MATLAB DATENUM.
#
  dn = jed - epoch_to_jed_datenum ( )

  return dn

def jed_to_datenum_test ( ):

#*****************************************************************************80
#
## JED_TO_DATENUM_TEST tests JED_TO_DATENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'JED_TO_DATENUM_TEST' )
  print ( '  JED_TO_DATENUM: JED => Matlab DATENUM.' )
  print ( '' )
  print ( '  JED (in)    DATENUM             JED (out)' )
  print ( '' )

  jed_epoch = epoch_to_jed_datenum ( )

  i = 0

  while ( True ):

    i = i + 1
    jed1 = jed_test ( i )

    if ( jed1 < 0.0 ):
      break

    if ( jed_epoch <= jed1 ):

      date_num = jed_to_datenum ( jed1 )
      jed3 = datenum_to_jed ( date_num )

      print ( '  %11.2f  %12.2f  %11.2f'% ( jed1, date_num, jed3 ) )

  return

def jed_to_gps ( jed ):

#*****************************************************************************80
#
## JED_TO_GPS converts a JED to a GPS date.
#
#  Discussion:
#
#    The GPS time keeping is in terms of seconds, weeks, and cycles
#    of 1024 weeks.  The weeks and cycles begin numbering at 0.
#
#    The computation is only valid for dates after the GPS epoch,
#    that is, after 6 January 1980.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, integer C, W, real S, the
#    corresponding GPS cycles/weeks/seconds date.
#
  jed_epoch = epoch_to_jed_gps ( )

  d = jed - jed_epoch

  if ( d < 0.0 ):
    s = -1.0
    w = -1
    c = -1
    return c, w, s

  w = int ( d ) // 7
  d = d - ( 7 * w )

  c = w // 1024
  w = w - 1024 * c

  s = d * ( 24.0 * 60.0 * 60.0 )

  return c, w, s

def jed_to_gps_test ( ):

#*****************************************************************************80
#
## JED_TO_GPS_TEST tests JED_TO_GPS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'JED_TO_GPS_TEST' )
  print ( '  JED_TO_GPS: JED -> GPS.' )
  print ( '' )
  print ( '   JED (in)       GPS (C/W/S)                   JED (out)' )
  print ( '' )

  jed_epoch = epoch_to_jed_gps ( )

  i = 0

  while ( True ):

    i = i + 1
    jed1 = jed_test ( i )

    if ( jed1 < 0.0 ):
      break

    if ( jed_epoch <= jed1 ):

      c2, w2, sec2 = jed_to_gps ( jed1 )

      jed3 = gps_to_jed ( c2, w2, sec2 )

      print ( '  %11.2f  %d/%d/%.2f GPS  %11.2f' % ( jed1, c2, w2, sec2, jed3 ) )

  return

def jed_to_noon_next ( jed1 ):

#*****************************************************************************80
#
## JED_TO_NOON_NEXT converts a JED to the JED of the next noon.
#
#  Discussion:
#
#    This is primarily to make a fair test of the weekday routines,
#    which have trouble when the JED is at midnight.
#
#    Note that noon corresponds to an integral JED value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real JED1, the Julian Ephemeris Date.
#
#    Output, real JED2, the Julian Ephemeris Date
#    of the next noon.
#
  jed2 = round ( jed1 )
#
#  The integer part of JED1 is one of the two integers that
#  bracket JED1.  If it's the smaller one (which it should
#  be as long as JED1 is positive), make it the bigger one.
#
#  This correctly leaves undisturbed cases where JED1 is
#  already an integer, and where JED1 is negative (which
#  is not a case we expect to occur often).
#
  if ( jed2 < jed1 ):
    jed2 = jed2 + 1.0

  return jed2

def jed_to_noon_next_test ( ):

#*****************************************************************************80
#
## JED_TO_NOON_NEXT_TEST tests JED_TO_NOON_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'JED_TO_NOON_NEXT_TEST' )
  print ( '  JED_TO_NOON_NEXT: JED => JED of following noon time.' )
  print ( '' )
  print ( '      JED          JED(noon next)' )
  print ( '' )

  i = 0

  while ( True ):

    i = i + 1
    jed1 = jed_test ( i )

    if ( jed1 < 0 ):
      break

    y1, m1, d1, f1 = jed_to_ymdf_common ( jed1 )

    s1 = ymdf_to_s_common ( y1, m1, d1, f1 )

    jed2 = jed_to_noon_next ( jed1 )

    y2, m2, d2, f2 = jed_to_ymdf_common ( jed2 )

    s2 = ymdf_to_s_common ( y2, m2, d2, f2 )

    print ( '%11.2f  %s  %11.2f  %s' % ( jed1, s1, jed2, s2 ) )

  return

def jed_to_noon_nearest ( jed1 ):

#*****************************************************************************80
#
## JED_TO_NOON_NEAREST converts a JED to the JED of the nearest noon.
#
#  Discussion:
#
#    This is primarily to make a fair test of the weekday routines,
#    which have trouble when the JED is at midnight.
#
#    Note that noon corresponds to an integral JED value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real JED1, the Julian Ephemeris Date.
#
#    Output, real JED2, the Julian Ephemeris Date
#    of the nearest noon.
#
  jed2 = round ( jed1 )

  return jed2

def jed_to_noon_nearest_test ( ):

#*****************************************************************************80
#
## JED_TO_NOON_NEAREST_TEST tests JED_TO_NOON_NEAREST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'JED_TO_NOON_NEAREST_TEST' )
  print ( '  JED_TO_NOON_NEAREST: JED => JED of nearest noon.' )
  print ( '' )
  print ( '      JED          JED(noon nearest)' )
  print ( '' )

  i = 0

  while ( True ):

    i = i + 1
    jed1 = jed_test ( i )

    if ( jed1 < 0 ):
      break

    y1, m1, d1, f1 = jed_to_ymdf_common ( jed1 )

    s1 = ymdf_to_s_common ( y1, m1, d1, f1 )

    jed2 = jed_to_noon_nearest ( jed1 )

    y2, m2, d2, f2 = jed_to_ymdf_common ( jed2 )

    s2 = ymdf_to_s_common ( y2, m2, d2, f2 )

    print ( '%11.2f  %s  %11.2f  %s' % ( jed1, s1, jed2, s2 ) )

  return

def jed_to_weekday ( jed ):

#*****************************************************************************80
#
## JED_TO_WEEKDAY computes the day of the week from a JED.
#
#  Discussion:
#
#    BC 4713/01/01 => JED = 0.0 was noon on a Monday.
#
#    jedmod = mod ( 0.0, 7.0 ) = 0.0
#    j = mod ( nint ( 0 ), 7 ) = 0
#    f = ( 0.0 + 0.5 ) - real ( j ) = 0.5
#    w = i4_wrap ( 0 + 2, 1, 7 ) = 2 = MONDAY
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Richards,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999.
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, integer W, the day of the week of the date.
#    The days are numbered from Sunday through Saturday, 1 through 7.
#
#    Output, real F, the fractional part of the day.
#
  import numpy as np

  jedp = jed + 0.5
  jedpfrac = ( jedp % 1.0 )
  jedpwhole = int ( jedp - jedpfrac )

  f = jedpfrac
  w = i4_wrap ( jedpwhole + 2, 1, 7 )

  return w, f

def jed_to_weekday_test ( ):

#*****************************************************************************80
#
## JED_TO_WEEKDAY_TEST tests JED_TO_WEEKDAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JED_TO_WEEKDAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JED_TO_WEEKDAY determines the weekday corresponding to a JED.' )
  print ( '' )
  print ( '             JED  W     W' )
  print ( '                  True  Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, jed, w = jed_weekday_values ( n_data )

    if ( n_data == 0 ):
      break

    w2, f = jed_to_weekday ( jed )
    
    print ( '  %14f  %4d  %8d' % ( jed, w, w2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JED_TO_WEEKDAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def jed_to_ymdf_common ( jed ):

#*****************************************************************************80
#
## JED_TO_YMDF_COMMON converts a JED to a Common YMDF date.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    JED = 2299160.5, and Gregorian thereafter.
#
#    There is no year 0.  BC years are specified using a negative value.
#
#  Example:
#
#        JED            Y    M   D
#    -------    ------------------
#          0    BCE  4713  Jan   1
#    2440000    CE   1968  May  23
#    2446065    CE   1984  Dec  31
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, integer Y, M, D, real F, the YMDF date.
#
  jed_transition = transition_to_jed_common ( )

  if ( jed <= jed_transition ):
    y, m, d, f = jed_to_ymdf_julian ( jed )
  else:
    y, m, d, f = jed_to_ymdf_gregorian ( jed )

  return y, m, d, f

def jed_to_ymdf_julian ( jed ):

#*****************************************************************************80
#
## JED_TO_YMDF_JULIAN converts a JED to a Julian YMDF date.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Richards,
#    Algorithm F,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, pages 324-325.
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, integer Y, M, D, real F, the YMDF date.
#
  import numpy as np
#
#  Determine the computational date (Y'/M'/D').
#
  j = np.floor ( jed + 0.5 )
  f = ( jed + 0.5 ) - j

  j_prime = j + 1401

  y_prime = ( 4 * j_prime + 3 ) // 1461
  t_prime = ( ( ( 4 * j_prime + 3 ) % 1461 ) // 4 )
  m_prime = ( 5 * t_prime + 2 ) // 153
  d_prime = ( ( ( 5 * t_prime + 2 ) % 153 ) // 5 )
#
#  Convert the computational date to a calendar date.
#
  d = d_prime + 1
  m = ( ( m_prime + 2 ) % 12 ) + 1
  y = y_prime - 4716 + ( ( 14 - m ) // 12 )
#
#  Any year before 1 AD must be moved one year further back, since
#  this calendar does not include a year 0.
#
  y = y_astronomical_to_common ( y )

  return y, m, d, f

def jed_to_ymdf_gregorian ( jed ):

#*****************************************************************************80
#
## JED_TO_YMDF_GREGORIAN converts a JED to a Gregorian YMDF date.
#
#  Discussion:
#
#    This Gregorian calendar is extended backwards in time before
#    its actual adoption.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Richards,
#    Algorithm F,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, pages 324-325.
#
#  Parameters:
#
#    Input, real JED, the Julian Ephemeris Date.
#
#    Output, integer Y, M, D, real F, the YMDF date.
#
  import numpy as np
#
#  Determine the computational date (Y'/M'/D').
#
  j = np.floor ( jed + 0.5 )
  f = ( jed + 0.5 ) - j

  g = ( ( 4 * j + 274277 ) // 146097 )
  g = ( ( 3 * g ) // 4 ) - 38
  j_prime = j + 1401 + g

  y_prime = ( ( 4 * j_prime + 3 ) // 1461 )
  t_prime = ( ( ( 4 * j_prime + 3 ) % 1461 ) // 4 )
  m_prime = ( ( 5 * t_prime + 2 ) // 153 )
  d_prime = ( ( ( 5 * t_prime + 2 ) % 153 ) // 5 )
#
#  Convert the computational date to a calendar date.
#
  d = d_prime + 1
  m = ( ( m_prime + 2 ) % 12 ) + 1
  y = y_prime - 4716 +  ( ( 14 - m ) // 12 )
#
#  Any year before 1 AD must be moved one year further back, since
#  this calendar does not include a year 0.
#
  y = y_astronomical_to_common ( y )

  return y, m, d, f

def jed_weekday_values ( n_data ):

#*****************************************************************************80
#
## JED_WEEKDAY_VALUES returns the day of the week for Julian Ephemeris Dates.
#
#  Discussion:
#
#    The JED (Julian Ephemeris Date) is a calendrical system which counts days,
#    starting from noon on 1 January 4713 BCE.
#
#    Weekdays are numbered as follows:
#
#    1  Sunday
#    2  Monday
#    3  Tuesday
#    4  Wednesday
#    5  Thursday
#    6  Friday
#    7  Saturday
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold and Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real JED, the Julian Ephemeris Date.
#
#    Output, integer WEEKDAY, the day of the week.
#
  import numpy as np

  n_max = 33

  jed_vec = np.array ( (\
    1507231.5E+00, \
    1660037.5E+00, \
    1746893.5E+00, \
    1770641.5E+00, \
    1892731.5E+00, \
    1931579.5E+00, \
    1974851.5E+00, \
    2091164.5E+00, \
    2121509.5E+00, \
    2155779.5E+00, \
    2174029.5E+00, \
    2191584.5E+00, \
    2195261.5E+00, \
    2229274.5E+00, \
    2245580.5E+00, \
    2266100.5E+00, \
    2288542.5E+00, \
    2290901.5E+00, \
    2323140.5E+00, \
    2334848.5E+00, \
    2348020.5E+00, \
    2366978.5E+00, \
    2385648.5E+00, \
    2392825.5E+00, \
    2416223.5E+00, \
    2425848.5E+00, \
    2430266.5E+00, \
    2430833.5E+00, \
    2431004.5E+00, \
    2448698.5E+00, \
    2450138.5E+00, \
    2465737.5E+00, \
    2486076.5E+00 ))

  weekday_vec = np.array ( (\
    1, 4, 4, 1, 4, \
    2, 7, 1, 1, 6, \
    7, 6, 1, 1, 4, \
    7, 7, 7, 4, 1, \
    6, 1, 2, 4, 1, \
    1, 2, 2, 5, 3, \
    1, 4, 1 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    jed = 0.0
    weekday = 0
  else:
    jed = jed_vec[n_data]
    weekday = weekday_vec[n_data]
    n_data = n_data + 1

  return n_data, jed, weekday

def jed_weekday_values_test ( ):

#*****************************************************************************80
#
## JED_WEEKDAY_VALUES_TEST demonstrates the use of JED_WEEKDAY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JED_WEEKDAY_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JED_WEEKDAY_VALUES stores values of the Weekday for a given JED.' )
  print ( '' )
  print ( '    JED         WEEKDAY(JED)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, jed, weekday = jed_weekday_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %d' % ( jed, weekday ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JED_WEEKDAY_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def minute_borrow_common ( y, m, d, h, n ):

#*****************************************************************************80
#
## MINUTE_BORROW_COMMON "borrows" an hour of minutes in a Common date.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, N, the year,
#    month, day, hour and minute representing a date.  On input, N
#    might be negative.
#    On output, H should have decreased by one, and N gone up by 60.
#
  while ( n < 0 ):

    n = n + 60
    h = h - 1

    y, m, d, h = hour_borrow_common ( y, m, d, h )

  return y, m, d, h, n

def minute_carry_common ( y, m, d, h, n ):

#*****************************************************************************80
#
## MINUTE_CARRY_COMMON: given a Common YMDHMS date, carries minutes to hours.
#
#  Algorithm:
#
#    While 60 <= N:
#
#      decrease N by the number of minutes in an hour;
#      increase H by 1;
#      if necessary, adjust Y, M and D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, N, the date.
#    On output, N is between 0 and 59.
#
  while ( 60 <= n ):

    n = n - 60
    h = h + 1

    y, m, d, h = hour_carry_common ( y, m, d, h )

  return y, m, d, h, n

def month_borrow_common ( y, m ):

#*****************************************************************************80
#
## MONTH_BORROW_COMMON borrows a year of months on the Common calendar.
#
#  Discussion:
#
#    If the month index is legal, nothing is done.  If the month index
#    is too small, then one or more years are "cashed in" to bring the
#    month index up to a legal value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, the YM date.
#    On input, M might be negative.  On output, Y should have decreased by
#    one, and M gone up by the number of months in the year that we
#    "cashed in".  The routine knows there was no year 0.
#
  while ( m <= 0 ):

    months = year_length_months_common ( y )

    m = m + months
    y = y - 1

    if ( y == 0 ):
      y = - 1

  return y, m

def month_carry_common ( y, m ):

#*****************************************************************************80
#
## MONTH_CARRY_COMMON carries a year of months on the Common calendar.
#
#  Algorithm:
#
#    While 12 < M:
#
#      decrease M by 12;
#      increase Y by 1;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, the year and month.
#    On output, M is no greater than 12.
#
  while ( True ):

    months = year_length_months_common ( y )

    if ( m <= months ):
      break

    m = m - months
    y = y + 1

  return y, m

def month_length_common ( y, m ):

#*****************************************************************************80
#
## MONTH_LENGTH_COMMON returns the number of days in a Common month.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    day JED = 2299160, and Gregorian from day JED = 2299161 and after.
#
#    The routine knows that February has 28 days, except in leap years,
#    when it has 29.
#
#    In the Common calendar, October 1582 had only 21 days
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the year in which the month occurred.
#
#    Input, integer M, the number of the month.
#
#    Output, integer DAYS, the number of days
#    in the month.
#
  import numpy as np

  mdays = np.array ( [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] )
#
#  Check the input.
#
  y2, m2, ierror = ym_check_common ( y, m )

  if ( ierror != 0 ):
    days = 0
    return days
#
#  Take care of the special case.
#
  if ( y2 == 1582 ):
    if ( m2 == 10 ):
      days = 21
      return days
#
#  Get the number of days in the month.
#
  days = mdays[m2-1]
#
#  If necessary, add 1 day for February 29.
#
  if ( m2 == 2 and year_is_leap_common ( y2 ) ):
    days = days + 1

  return days

def month_to_month_name_common ( m ):

#*****************************************************************************80
#
## MONTH_TO_MONTH_NAME_COMMON returns the name of a Common month.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the month index.
#
#    Output, string MONTH_NAME, the month name.
#
  from sys import exit

  if ( m == 1 ):
    month_name = 'January'
  elif ( m == 2 ):
    month_name = 'February'
  elif ( m == 3 ):
    month_name = 'March'
  elif ( m == 4 ):
    month_name = 'April'
  elif ( m == 5 ):
    month_name = 'May'
  elif ( m == 6 ):
    month_name = 'June'
  elif ( m == 7 ):
    month_name = 'July'
  elif ( m == 8 ):
    month_name = 'August'
  elif ( m == 9 ):
    month_name = 'September'
  elif ( m == 10 ):
    month_name = 'October'
  elif ( m == 11 ):
    month_name = 'November'
  elif ( m == 12 ):
    month_name = 'December'
  else:
    print ( '' )
    print ( 'WEEKDAY_TO_NAME_COMMON - Fatal error!' )
    print ( '  Index M must be between 1 and 12.' )
    exit ( 'WEEKDAY_TO_NAME_COMMON - Fatal error!' )

  return month_name

def month_to_month_name_common_test ( ):

#*****************************************************************************80
#
## MONTH_TO_MONTH_NAME_COMMON_TEST tests MONTH_TO_MONTH_NAME_COMMON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'MONTH_TO_MONTH_NAME_COMMON_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MONTH_TO_MONTH_NAME_COMMON names the months.' )
  print ( '' )

  for m  in range ( 1, 13 ):
    month_name = month_to_month_name_common ( m )
    print ( '  %2d  %s' % ( m, month_name ) )

  return

def month_to_month_name_common3 ( m ):

#*****************************************************************************80
#
## MONTH_TO_MONTH_NAME_COMMON3 returns an abbreviation of a Common month.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the month index.
#
#    Output, string MONTH_NAME, the month name.
#
  from sys import exit

  if ( m == 1 ):
    month_name = 'Jan'
  elif ( m == 2 ):
    month_name = 'Feb'
  elif ( m == 3 ):
    month_name = 'Mar'
  elif ( m == 4 ):
    month_name = 'Apr'
  elif ( m == 5 ):
    month_name = 'May'
  elif ( m == 6 ):
    month_name = 'Jun'
  elif ( m == 7 ):
    month_name = 'Jul'
  elif ( m == 8 ):
    month_name = 'Aug'
  elif ( m == 9 ):
    month_name = 'Sep'
  elif ( m == 10 ):
    month_name = 'Oct'
  elif ( m == 11 ):
    month_name = 'Nov'
  elif ( m == 12 ):
    month_name = 'Dec'
  else:
    print ( '' )
    print ( 'WEEKDAY_TO_NAME_COMMON3 - Fatal error!' )
    print ( '  Index M must be between 1 and 12.' )
    exit ( 'WEEKDAY_TO_NAME_COMMON3 - Fatal error!' )

  return month_name

def month_to_month_name_common3_test ( ):

#*****************************************************************************80
#
## MONTH_TO_MONTH_NAME_COMMON3_TEST tests MONTH_TO_MONTH_NAME_COMMON3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'MONTH_TO_MONTH_NAME_COMMON3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MONTH_TO_MONTH_NAME_COMMON3 names the months.' )
  print ( '' )

  for m in range ( 1, 13 ):
    month_name = month_to_month_name_common3 ( m )
    print ( '  %2d  %s' % ( m, month_name ) )

  return

def now_to_jed ( ):

#*****************************************************************************80
#
## NOW_TO_JED expresses the current date as a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the JED for the current date.
#
  import time

  c = time.localtime ( );

  y = c[0];
  m = c[1];
  d = c[2];
  h = c[3];
  n = c[4];
  s = c[5];

  jed = ymdhms_to_jed_common ( y, m, d, h, n, s );

  return jed

def r8_mod ( x, y ):

#*****************************************************************************80
#
## R8_MOD returns the remainder of R8 division.
#
#  Formula:
#
#    If
#      REM = R8_MOD ( X, Y )
#      RMULT = ( X - REM ) / Y
#    then
#      X = Y * RMULT + REM
#    where REM has the same sign as X, and abs ( REM ) < Y.
#
#  Example:
#
#        X         Y     R8_MOD  R8_MOD Factorization
#
#      107        50       7      107 =  2 *  50 + 7
#      107       -50       7      107 = -2 * -50 + 7
#     -107        50      -7     -107 = -2 *  50 - 7
#     -107       -50      -7     -107 =  2 * -50 - 7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number to be divided.
#
#    Input, real Y, the number that divides X.
#
#    Output, real VALUE, the remainder when X is divided by Y.
#
  from sys import exit

  if ( y == 0.0 ):
    print ( '' )
    print ( 'R8_MOD - Fatal error!' )
    print ( '  R8_MOD ( X, Y ) called with Y = 0.' )
    exit ( 'R8_MOD - Fatal error!' )

  value = x - int ( x / y ) * y

  if ( x < 0.0 and 0.0 < value ):
    value = value - abs ( y )
  elif ( 0.0 < x and value < 0.0 ):
    value = value + abs ( y )

  return value

def r8_mod_test ( ):

#*****************************************************************************80
#
## R8_MOD_TEST tests R8_MOD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  test_num = 10

  print ( '' )
  print ( 'R8_MOD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_MOD returns the remainder after division.' )
  print ( '' )
  print ( '        X             Y             (X%Y)    R8_MOD(X,Y)' )
  print ( '' )

  x_lo = -10.0
  x_hi = +10.0

  seed = 123456789

  for test in range ( 0, test_num ):

    x, seed = r8_uniform_ab ( x_lo, x_hi, seed )
    y, seed = r8_uniform_ab ( x_lo, x_hi, seed )

    z1 = x % y
    z2 = r8_mod ( x, y )

    print ( '  %12f  %12f  %12f  %12f' % ( x, y, z1, z2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_MOD_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## R8_UNIFORM_AB returns a scaled pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, real A, B, the minimum and maximum values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real R, the randomly chosen value.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from sys import exit

  i4_huge = 2147483647

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_AB - Fatal error!' )

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_AB_TEST tests R8_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'R8_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_AB returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( a, b, seed )
    print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_AB_TEST' )
  print ( '  Normal end of execution' )
  return

def second_borrow_common ( y, m, d, h, n, s ):

#*****************************************************************************80
#
## SECOND_BORROW_COMMON "borrows" a minute of seconds in a common date.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, N, S, the YMDHMS date.
#
  while ( s < 0 ):

    s = s + 60
    n = n - 1

    y, m, d, h, n = minute_borrow_common ( y, m, d, h, n )

  return y, m, d, h, n, s

def second_carry_common ( y, m, d, h, n, s ):

#*****************************************************************************80
#
## SECOND_CARRY_COMMON: given a Common YMDHMS date, carries seconds to minutes.
#
#  Algorithm:
#
#    While 60 <= S:
#
#      decrease S by 60;
#      increase N by 1;
#      if necessary, adjust H, D, M and Y.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 Deember 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, N, S,
#    the year, month, day, hours, minutes, seconds,
#    On output, S is between 0 and 59.
#
  while ( 60 <= s ):

    s = s - 60
    n = n + 1

    y, m, d, h, n = minute_carry_common ( y, m, d, h, n )

  return y, m, d, h, n, s

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def transition_to_jed_common ( ):

#*****************************************************************************80
#
## TRANSITION_TO_JED_COMMON returns the Common calendar transition as a JED.
#
#  Discussion:
#
#    In the Common calendar, the last moment of the Julian calendar was
#      11:59 pm, 4 October 1582 Julian/CE,
#      11:59 pm, 14 October 1582 Gregorian.
#    The first minute of the Gregorian calendar ended at
#      12:01 am, 5 October 1582 Julian,
#      12:01 am, 15 October 1582 Gregorian/CE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real JED, the Julian Ephemeris Date of the date.
#
  jed = 2299160.5

  return jed

def weekday_to_name_common ( w ):

#*****************************************************************************80
#
## WEEKDAY_TO_NAME_COMMON returns the name of a Common weekday.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 1999
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer W, the weekday index.
#
#    Output, string S, the weekday name.
#
  from sys import exit
  
  if ( w == 1 ):
    s = 'Sunday'
  elif ( w == 2 ):
    s = 'Monday'
  elif ( w == 3 ):
    s = 'Tuesday'
  elif ( w == 4 ):
    s = 'Wednesday'
  elif ( w == 5 ):
    s = 'Thursday'
  elif ( w == 6 ):
    s = 'Friday'
  elif ( w == 7 ):
    s = 'Saturday'
  else:
    print ( '' )
    print ( 'WEEKDAY_TO_NAME_COMMON - Fatal error!' )
    print ( '  Index W must be between 1 and 7.' )
    exit ( 'WEEKDAY_TO_NAME_COMMON - Fatal error!' )

  return s

def weekday_to_name_common_test ( ):

#*****************************************************************************80
#
## WEEKDAY_TO_NAME_COMMON_TEST tests WEEKDAY_TO_NAME_COMMON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'WEEKDAY_TO_NAME_COMMON_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEEKDAY_TO_NAME_COMMON is given a weekday index between 1 and 7' )
  print ( '  and returns the corresponding name of the weekday.' )
  print ( '' )
  print ( '  Index    Name' )
  print ( '' )
  
  for w in range ( 1, 8 ):
    s = weekday_to_name_common ( w )
    print ( '  %5d  %s' % ( w, s ) )
    
  return

def weekday_to_name_common2 ( w ):

#*****************************************************************************80
#
## WEEKDAY_TO_NAME_COMMON2 returns the name of a Common weekday.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer W, the weekday index.
#
#    Output, string S, the weekday name.
#
  from sys import exit
  
  if ( w == 1 ):
    s = 'Su'
  elif ( w == 2 ):
    s = 'M '
  elif ( w == 3 ):
    s = 'Tu'
  elif ( w == 4 ):
    s = 'W '
  elif ( w == 5 ):
    s = 'Th'
  elif ( w == 6 ):
    s = 'F '
  elif ( w == 7 ):
    s = 'Sa'
  else:
    print ( '' )
    print ( 'WEEKDAY_TO_NAME_COMMON2 - Fatal error!' )
    print ( '  Index W must be between 1 and 7.' )
    exit ( 'WEEKDAY_TO_NAME_COMMON2 - Fatal error!' )

  return s

def weekday_to_name_common2_test ( ):

#*****************************************************************************80
#
## WEEKDAY_TO_NAME_COMMON2_TEST tests WEEKDAY_TO_NAME_COMMON2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'WEEKDAY_TO_NAME_COMMON2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEEKDAY_TO_NAME_COMMON2 is given a weekday index between 1 and 7' )
  print ( '  and returns the corresponding name of the weekday.' )
  print ( '' )
  print ( '  Index    Name' )
  print ( '' )
  
  for w in range ( 1, 8 ):
    s = weekday_to_name_common2 ( w )
    print ( '  %5d  %s' % ( w, s ) )
    
  return

def weekday_to_name_common3 ( w ):

#*****************************************************************************80
#
## WEEKDAY_TO_NAME_COMMON3 returns the name of a Common weekday.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 September 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer W, the weekday index.
#
#    Output, string S, the weekday name.
#
  from sys import exit
  
  if ( w == 1 ):
    s = 'Sun'
  elif ( w == 2 ):
    s = 'Mon'
  elif ( w == 3 ):
    s = 'Tue'
  elif ( w == 4 ):
    s = 'Wed'
  elif ( w == 5 ):
    s = 'Thu'
  elif ( w == 6 ):
    s = 'Fri'
  elif ( w == 7 ):
    s = 'Sat'
  else:
    print ( '' )
    print ( 'WEEKDAY_TO_NAME_COMMON3 - Fatal error!' )
    print ( '  Index W must be between 1 and 7.' )
    exit ( 'WEEKDAY_TO_NAME_COMMON3 - Fatal error!' )

  return s

def weekday_to_name_common3_test ( ):

#*****************************************************************************80
#
## WEEKDAY_TO_NAME_COMMON3_TEST tests WEEKDAY_TO_NAME_COMMON3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'WEEKDAY_TO_NAME_COMMON3_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEEKDAY_TO_NAME_COMMON3 is given a weekday index between 1 and 7' )
  print ( '  and returns the corresponding name of the weekday.' )
  print ( '' )
  print ( '  Index    Name' )
  print ( '' )
  
  for w in range ( 1, 8 ):
    s = weekday_to_name_common3 ( w )
    print ( '  %5d  %s' % ( w, s ) )
    
  return

def weekday_values ( n_data ):

#*****************************************************************************80
#
## WEEKDAY_VALUES returns the day of the week for various dates.
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
#    22 February 2015
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
#    and returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer Y, M, D, the Common Era date.
#
#    Output, integer W, the day of the week.  Sunday = 1.
#
  import numpy as np

  n_max = 34

  d_vec = np.array ( ( \
    30, \
     8, \
    26, \
     3, \
     7, \
    18, \
     7, \
    19, \
    14, \
    18, \
    16, \
     3, \
    26, \
    20, \
     4, \
    25, \
    31, \
     9, \
    24, \
    10, \
    30, \
    24, \
    19, \
     2, \
    27, \
    19, \
    25, \
    29, \
    19, \
     7, \
    17, \
    25, \
    10, \
    18 ))

  m_vec = np.array ( ( \
     7, \
    12, \
     9, \
    10, \
     1, \
     5, \
    11, \
     4, \
    10, \
     5, \
     3, \
     3, \
     3, \
     4, \
     6, \
     1, \
     3, \
     9, \
     2, \
     6, \
     6, \
     7, \
     6, \
     8, \
     3, \
     4, \
     8, \
     9, \
     4, \
    10, \
     3, \
     2, \
    11, \
     7 ))

  w_vec = np.array ( ( \
    1, \
    4, \
    4, \
    1, \
    4, \
    2, \
    7, \
    1, \
    7, \
    1, \
    6, \
    7, \
    6, \
    1, \
    1, \
    4, \
    7, \
    7, \
    7, \
    4, \
    1, \
    6, \
    1, \
    2, \
    4, \
    1, \
    1, \
    2, \
    2, \
    5, \
    3, \
    1, \
    4, \
    1 ))

  y_vec = np.array ( ( \
    - 587, \
    - 169, \
       70, \
      135, \
      470, \
      576, \
      694, \
     1013, \
     1066, \
     1096, \
     1190, \
     1240, \
     1288, \
     1298, \
     1391, \
     1436, \
     1492, \
     1553, \
     1560, \
     1648, \
     1680, \
     1716, \
     1768, \
     1819, \
     1839, \
     1903, \
     1929, \
     1941, \
     1943, \
     1943, \
     1992, \
     1996, \
     2038, \
     2094 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    y = 0
    m = 0
    d = 0
    w = 0
  else:
    y = y_vec[n_data]
    m = m_vec[n_data]
    d = d_vec[n_data]
    w = w_vec[n_data]
    n_data = n_data + 1

  return n_data, y, m, d, w

def weekday_values_test ( ):

#*****************************************************************************80
#
## WEEKDAY_VALUES_TEST demonstrates the use of WEEKDAY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEEKDAY_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEEKDAY_VALUES stores values of' )
  print ( '  the weekday for a given Y/M/D date' )
  print ( '' )
  print ( '         Y       M       D           W' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, y, m, d, w = weekday_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %6d  %6d' % ( y, m, d, w ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEEKDAY_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def y_astronomical_to_common ( y ):

#*****************************************************************************80
#
## Y_ASTRONOMICAL_TO_COMMON converts an Astronomical year to a Common year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the astronomical year.
#
#    Output, integer Y2, the Common year.
#
  if ( y <= 0 ):
    y2 = y - 1
  else:
    y2 = y

  return y2

def y_check_alexandrian ( y ):

#*****************************************************************************80
#
## y_check_alexandrian checks an Alexandrian year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_bahai ( y ):

#*****************************************************************************80
#
## y_check_bahai checks a Bahai year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_common ( y ):

#*****************************************************************************80
#
## Y_CHECK_COMMON checks a Common year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_eg_civil ( y ):

#*****************************************************************************80
#
## y_check_eg_civil checks an Egyptian Civil year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_english ( y ):

#*****************************************************************************80
#
## y_check_english checks an English year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_greek ( y ):

#*****************************************************************************80
#
## y_check_greek checks a Greek year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_gregorian ( y ):

#*****************************************************************************80
#
## y_check_gregorian checks a Gregorian year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_hebrew ( y ):

#*****************************************************************************80
#
## y_check_hebrew checks a Hebrew year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_islamic ( y ):

#*****************************************************************************80
#
## y_check_islamic checks an Islamic year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_julian ( y ):

#*****************************************************************************80
#
## y_check_julian checks a Julian year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_republican ( y ):

#*****************************************************************************80
#
## y_check_republican checks a Republican year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_check_roman ( y ):

#*****************************************************************************80
#
## y_check_roman checks a Roman year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year, which must not be 0.
#
#  Output:
#
#    integer IERROR, is 0 if Y is legal, and 1 otherwise.
#
  if ( y != 0 ):
    ierror = 0
  else:
    ierror = 1

  return ierror

def y_common_to_astronomical ( y ):

#*****************************************************************************80
#
## Y_COMMON_TO_ASTRONOMICAL converts a Common year to an Astronomical year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the Common year.
#
#    Output, integer Y2, the Astronomical year.
#
  from sys import exit
  
  if ( y < 0 ):
    y2 = y + 1
  elif ( y == 0 ):
    print ( '' )
    print ( 'Y_COMMON_TO_ASTRONOMICAL - Fatal error!' )
    print ( '  COMMON calendar does not have a year 0.' )
    exit ( 'Y_COMMON_TO_ASTRONOMICAL - Fatal error!' )
  else:
    y2 = y

  return y2

def y_common_to_astronomical_test ( ):

#*****************************************************************************80
#
## Y_COMMON_TO_ASTRONOMICAL_TEST tests Y_COMMON_TO_ASTRONOMICAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the Common year.
#
#    Output, integer Y2, the Astronomical year.
#
  import platform

  print ( '' )
  print ( 'Y_COMMON_TO_ASTRONOMICAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Y_COMMON_TO_ASTRONOMICAL converts a common year to an' )
  print ( '  "astronomical" year.' )
  print ( '' )
  print ( '  Y_COMMON  Y_ASTRONOMICAL' )
  print ( '' )

  for y in range ( -10, 11 ):
    if ( y != 0 ):
      y2 = y_common_to_astronomical ( y )
      print ( '  %8d  %14d' % ( y, y2 ) )

  return

def y_to_s_common ( y ):

#*****************************************************************************80
#
## Y_TO_S_COMMON writes a Common Y date into a string.
#
#  Format:
#
#    CE YYYY
#    BCE YYYY
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the Y date.
#
#    Output, string S, a representation of the date.
#
  if ( 0 <= y ):
    s1 = 'CE'
  else:
    s1 = 'BCE'
    
  if ( 0 <= y ):
    s2 = str ( y )
  else:
    s2 = str ( -y )

  s = s1 + ' ' + s2

  return s

def y_to_s_common_test ( ):

#*****************************************************************************80
#
## Y_TO_S_COMMON_TEST tests Y_TO_S_COMMON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'Y_TO_S_COMMON_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Y_TO_S_COMMON converts a year Y to a string S.' )
  print ( '' )
  print ( '      Y  "S"' )
  print ( '' )

  mu = 0.0
  sigma = 1000.0
  seed = 123456789

  for i in range ( 0, 10 ):
    y, seed = i4_normal_ab ( mu, sigma, seed )
    s = y_to_s_common ( y )
    print ( '  %6d  "%s"' % ( y, s ) )

  return

def year_is_leap_common ( y ):

#*****************************************************************************80
#
## YEAR_IS_LEAP_COMMON returns TRUE if the Common year was a leap year.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    day JED = 2299160, and Gregorian from day JED = 2299161 and after.
#
#  Algorithm:
#
#    If ( the year is less than 0 ) then
#
#      if the year+1 is divisible by 4 then
#        the year is a leap year.
#
#    else if ( the year is 0 ) then
#
#      the year is not a leap year ( in fact, it's illegal )
#
#    else if ( the year is no greater than 1582 ) then
#
#      if the year is divisible by 4 then
#        the year is a leap year.
#
#    else if (
#      the year is divisible by 4 and
#      ( the year is not divisible by 100
#      or
#      the year is divisible by 400 )
#      ) then
#        the year is a leap year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the year to be checked.
#
#    Output, logical VALUE, TRUE if the year was a leap year,
#    FALSE otherwise.
#
  from sys import exit

  if ( y == 0 ):
    print ( '' )
    print ( 'YEAR_IS_LEAP_COMMON - Fatal error!' )
    print ( '  Year 0 is illegal.' )
    exit ( 'YEAR_IS_LEAP_COMMON - Fatal error!' )
#
#  BC years have to have 1 added to them to make a proper leap year evaluation.
#
  y2 = y_common_to_astronomical ( y )

  if ( y2 <= 1582 ):

    if ( i4_modp ( y2, 4 ) == 0 ):
      value = True
    else:
      value = False

  else:

    if ( i4_modp ( y2, 400 ) == 0 ):
      value = True
    elif ( i4_modp ( y2, 100 ) == 0 ):
      value = False
    elif ( i4_modp ( y2, 4 ) == 0 ):
      value = True
    else:
      value = False

  return value

def year_is_leap_gregorian ( y ):

#*****************************************************************************80
#
## YEAR_IS_LEAP_GREGORIAN returns TRUE if the Gregorian year was a leap year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the year to be checked.
#
#    Output, bool YEAR_IS_LEAP_GREGORIAN, TRUE if the year was a leap year,
#    FALSE otherwise.
#
  from sys import exit

  if ( y <= 0 ):
    print ( '' )
    print ( 'YEAR_IS_LEAP_GREGORIAN - Fatal error!' )
    print ( '  This function will not accept nonpositive years.' )
    exit ( 'YEAR_IS_LEAP_GREGORIAN - Fatal error!' )

  if ( ( y % 400 ) == 0 ):
    value = True
  elif ( ( y % 100 ) == 0 ):
    value = False
  elif ( ( y % 4 ) == 0 ):
    value = True
  else:
    value = False

  return value

def year_is_leap_gregorian_test ( ):

#*****************************************************************************80
#
## YEAR_IS_LEAP_GREGORIAN_TEST tests YEAR_IS_LEAP_GREGORIAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'YEAR_IS_LEAP_GREGORIAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Report leap years in the Gregorian calendar.' )
  print ( '' )
  print ( '  Year  Leap?' )
  print ( '' )

  seed = 123456789
  for i in range ( 0, 20 ):
    y, seed = i4_uniform_ab ( 1, 2100, seed )
    is_leap = year_is_leap_gregorian ( y )
    print ( '  %4d  %s' % ( y, is_leap ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'YEAR_IS_LEAP_GREGORIAN_TEST' )
  print ( '  Normal end of execution.' )
  return

def year_length_days_common ( y ):

#*****************************************************************************80
#
## YEAR_LENGTH_DAYS_COMMON returns the number of days in a Common year.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    day JED = 2299160, and Gregorian from day JED = 2299161 and after.
#
#    If Y is 0, then the routine returns 0, reflecting the fact that
#    there was officially no year 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the year to be checked.
#
#    Output, integer VALUE, the number of
#    days in the year.
#
  if ( y == 0 ):
    value = 0
  elif ( y == 1582 ):
    value = 355
  elif ( year_is_leap_common ( y ) ):
    value = 366
  else:
    value = 365

  return value

def year_length_days_common_test ( ):

#*****************************************************************************80
#
## YEAR_LENGTH_DAYS_COMMON_TEST tests YEAR_LENGTH_DAYS_COMMON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'YEAR_LENGTH_DAYS_COMMON_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  For the Common calendar:' )
  print ( '  YEAR_LENGTH_DAYS_COMMON determines the length of a year.' )
  print ( '' )
  print ( '  Year  Length' )
  print ( '' )

  for y in range ( 1580, 1586 ):
    sy = y_to_s_common ( y )
    print ( '  %10s  %d' % ( sy, year_length_days_common ( y ) ) )

  for y in range ( 1750, 1755 ):
    sy = y_to_s_common ( y )
    print ( '  %10s  %d' % ( sy, year_length_days_common ( y ) ) )

  for y in range ( 1000, 2100, 100 ):
    sy = y_to_s_common ( y )
    print ( '  %10s  %d' % ( sy, year_length_days_common ( y ) ) )

  return

def year_length_months_common ( y ):

#*****************************************************************************80
#
## YEAR_LENGTH_MONTHS_COMMON returns the number of months in a Common year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the year to be checked.
#
#    Output, integer VALUE, the number of months in the year.
#
  value = 12

  return value

def year_to_epact_julian ( y ):

#*****************************************************************************80
#
## YEAR_TO_EPACT_JULIAN returns the epact of a Julian year.
#
#  Discussion:
#
#    The epact of a year is the age in days of the notional moon on
#    the first day of the year.  If the year begins with a new moon,
#    the epact is zero.  If the new moon occurred the day before,
#    the epact is 1.  There is a unique epact for every golden number.
#
#    Bear in mind that the notional moon is not the one in the sky,
#    but a theoretical one that satisfactorily approximates the behavior
#    of the real one, but which is tame enough to be described by a formula.
#
#  Example:
#
#    Year  Golden Number  Epact
#
#      1 BC     1           8
#      1 AD     2          19
#      2 AD     3           0
#      3 AD     4          11
#      4 AD     5          22
#      5 AD     6           3
#      6 AD     7          14
#      7 AD     8          25
#      8 AD     9           6
#      9 AD    10          17
#     10 AD    11          28
#     11 AD    12           9
#     12 AD    13          20
#     13 AD    14           1
#     14 AD    15          12
#     15 AD    16          23
#     16 AD    17           4
#     17 AD    18          15
#     18 AD    19          26
#     19 AD     1           8
#     20 AD     2          19
#   1066 AD     3           0
#   1900 AD     1           8
#   1919 AD     1           8
#   1938 AD     1           8
#   1957 AD     1           8
#   1976 AD     1           8
#   1995 AD     1           8
#   2014 AD     1           8
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
#  Reference:
#
#    Edward Richards,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999.
#
#  Parameters:
#
#    Input, integer Y, the year.  The year 0 is illegal input.
#
#    Output, integer E, the epact, between 0 and 28.
#
  from sys import exit

  if ( y == 0 ):
    print ( '' )
    print ( 'YEAR_TO_EPACT_JULIAN - Fatal error!' )
    print ( '  Illegal input Y = 0.' )
    exit ( 'YEAR_TO_EPACT_JULIAN - Fatal error!' )

  g = year_to_golden_number ( y )

  e = i4_wrap ( 11 * g - 3, 0, 29 )

  return e

def year_to_golden_number ( y ):

#*****************************************************************************80
#
## YEAR_TO_GOLDEN_NUMBER returns the golden number of a Common year.
#
#  Discussion:
#
#    Nineteen solar years are very close to 235 lunations.  Calendars
#    that try to keep track of both the sun and moon often make use of
#    this fact, ascribed to the Greek astronomer Meton.
#
#    While trying to determine a formula for Easter, Dionysus Exiguus
#    symbolized the place of each year in its Metonic cycle by a
#    "golden number" between 1 and 19.  The numbering began with the
#    year 1 BC, assigned the golden number of 1.  The following year,
#    1 AD, got the golden number of 2, and after that it gets easier.
#
#    The same golden year calculation is done for years in the Julian
#    or Gregorian calendar.
#
#  Example:
#
#    Year  Golden Number
#
#      1 BC     1
#      1 AD     2
#      2 AD     3
#     18 AD    19
#     19 AD     1
#     20 AD     2
#   1066 AD     3
#   1900 AD     1
#   1919 AD     1
#   1938 AD     1
#   1957 AD     1
#   1976 AD     1
#   1995 AD     1
#   2014 AD     1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, the year.
#
#    Output, integer G, the golden number, between 1 and 19.  This
#    records the position of the year in the 19 year Metonic cycle.
#
  from sys import exit

  if ( y == 0 ):
    print ( '' )
    print ( 'YEAR_TO_GOLDEN_NUMBER - Fatal error!' )
    print ( '  Illegal input Y = 0.' )
    exit ( 'YEAR_TO_GOLDEN_NUMBER - Fatal error!' )
#
#  We assume that BC years come in as negative numbers, and that
#  the year before 1 AD is 1 BC.  So add 1 to any negative value
#  so that the arithmetic works.
#
  y2 = y_common_to_astronomical ( y )

  g = i4_wrap ( y2 + 1, 1, 19 )

  return g

def year_to_golden_number_test ( ):

#*****************************************************************************80
#
## YEAR_TO_GOLDEN_NUMBER_TEST tests YEAR_TO_GOLDEN_NUMBER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'YEAR_TO_GOLDEN_NUMBER_TEST' )
  print ( '  YEAR_TO_GOLDEN_NUMBER determines the golden' )
  print ( '  number of a year.' )
  print ( '' )
  print ( '  Year  Golden Number' )
  print ( '' )

  for y in range ( -2, 21 ):
    if ( y != 0 ):
      s = y_to_s_common ( y )
      g = year_to_golden_number ( y )
      print ( '  %10s  %d' % ( s, g ) )

  return

def ym_check_common ( y, m ):

#*****************************************************************************80
#
## YM_CHECK_COMMON checks a Common YM date.
#
#  Discussion:
#
#    If the month is less than 1, then the month is incremented
#    by 12, and the year decremented by 1, repeatedly, until
#    the month is greater than or equal to 1.
#
#    If the month is greater than 12, then the month is decremented
#    by 12, and the year incremented by 1, repeatedly, until the
#    month is less than or equal to 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, the YM date.
#
#    Output, integer IERROR, is 0 if no error was found in the date
#    and 1 otherwise.
#

#
#  Check the year.
#
  ierror = y_check_common ( y )

  if ( ierror != 0 ):
    return y, m, ierror
#
#  Make sure the month isn't too small or too big.
#
  y, m = month_borrow_common ( y, m )

  y, m = month_carry_common ( y, m )

  return y, m, ierror

def ymd_check_common ( y, m, d ):

#*****************************************************************************80
#
## YMD_CHECK_COMMON checks a Common YMD date.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, the YMD date.
#
#    Output, integer IERROR, is 0 if no error was found in the date
#    and 1 otherwise.
#

#
#  Check the year.
#
  ierror = y_check_common ( y )

  if ( ierror != 0 ):
    return y, m, d, ierror
#
#  Make sure the month isn't too small or too big.
#
  y, m = month_borrow_common ( y, m )

  y, m = month_carry_common ( y, m )
#
#  Make sure the day isn't too small or too big.
#
  y, m, d = day_borrow_common ( y, m, d )

  y, m, d = day_carry_common ( y, m, d )

  return y, m, d, ierror

def ymd_to_s_common ( y, m, d ):

#*****************************************************************************80
#
## YMD_TO_S_COMMON writes a Common YMD date into a string.
#
#  Format:
#
#    CE YYYY/MM/DD
#    BCE YYYY/MM/DD
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, the YMD date.
#
#    Output, string S, a representation of the date.
#
  if ( 0 <= y ):
    s1 = 'CE'
  else:
    s1 = 'BCE'
    
  if ( 0 <= y ):
    s2 = str ( y )
  else:
    s2 = str ( -y )
    
  s3 = str ( m )
  
  s4 = str ( d )

  s = s1 + ' ' + s2 + '/' + s3 + '/' + s4

  return s

def ymd_to_s_gregorian ( y, m, d ):

#*****************************************************************************80
#
## YMD_TO_S_GREGORIAN writes a Gregorian YMD date into a string.
#
#  Format:
#
#    AD YYYY/MM/DD
#    BC YYYY/MM/DD
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, the YMD date.
#
#    Output, string S, a representation of the date.
#
  if ( 0 <= y ):
    s1 = 'AD'
  else:
    s1 = 'BC'
    
  if ( 0 <= y ):
    s2 = str ( y )
  else:
    s2 = str ( -y )
    
  s3 = str ( m )
  
  s4 = str ( d )

  s = s1 + ' ' + s2 + '/' + s3 + '/' + s4

  return s

def ymd_to_s_julian ( y, m, d ):

#*****************************************************************************80
#
## YMD_TO_S_JULIAN writes a Julian YMD date into a string.
#
#  Format:
#
#    AD YYYY/MM/DD
#    BC YYYY/MM/DD
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
#  Parameters:
#
#    Input, integer Y, M, D, the YMD date.
#
#    Output, string S, a representation of the date.
#
  if ( 0 <= y ):
    s1 = 'AD'
  else:
    s1 = 'BC'
    
  if ( 0 <= y ):
    s2 = str ( y )
  else:
    s2 = str ( -y )
    
  s3 = str ( m )
  
  s4 = str ( d )

  s = s1 + ' ' + s2 + '/' + s3 + '/' + s4

  return s

def ymd_to_weekday_common ( y, m, d ):

#*****************************************************************************80
#
## YMD_TO_WEEKDAY_COMMON returns the weekday of a Common YMD date.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    day JED = 2299160, and Gregorian from day JED = 2299161 and after.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 April 2010
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, the YMD date.
#
#    Output, integer W, is the week day number of the date, with
#    1 for Sunday, through 7 for Saturday.
#
  f = 0.5

  jed = ymdf_to_jed_common ( y, m, d, f )

  w, f2 = jed_to_weekday ( jed )

  return w

def ymd_to_weekday_common_test ( ):

#*****************************************************************************80
#
## YMD_TO_WEEKDAY_COMMON_TEST tests YMD_TO_WEEKDAY_COMMON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'YMD_TO_WEEKDAY_COMMON_TEST' )
  print ( '  YMD_TO_WEEKDAY_COMMON returns the day of the week' )
  print ( '  for Y/M/D dates in the Common calendar.' )
  print ( '' )
  print ( '  YMD                   Weekday    Weekday' )
  print ( '                        Tabulated  Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, y, m, d, w1 = weekday_values ( n_data )

    if ( n_data == 0 ):
      break
 
    s3 = ymd_to_s_common ( y, m, d )
    w2 = ymd_to_weekday_common ( y, m, d )
    s1 = weekday_to_name_common ( w1 )
    s2 = weekday_to_name_common ( w2 )

    print ( '  %20s  %9s  %9s' % ( s3, s1, s2 ) )

  return

def ymdf_compare ( y1, m1, d1, f1, y2, m2, d2, f2 ):

#*****************************************************************************80
#
## YMDF_COMPARE compares two YMDF dates.
#
#  Discussion:
#
#    The comparison should work for a pair of dates in any calendar.
#
#    No check is made that the dates are actually legitimate.  It is
#    assumed that the calling routine has already ensured that the
#    dates are properly "normalized".
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2001
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y1, M1, D1, real F1, the
#    first YMDF date.
#
#    Input, integer Y2, M2, D2, real F2, the
#    second YMDF date.
#
#    Output, character CMP:
#    '<' if date 1 precedes date 2
#    '=' if date 1 equals date 2
#    '>' if date 1 follows date 2
#
  cmp = '?'
#
#  Compare years...
#
  if ( y1 < y2 ):
    cmp = '<'
  elif ( y1 > y2 ):
    cmp = '>'
  else:
#
#  ...if necessary, compare months in equal years...
#
    if ( m1 < m2 ):
      cmp = '<'
    elif ( m1 > m2 ):
      cmp = '>'
    else:
#
#  ...if necessary, compare days in equal months...
#
      if ( d1 < d2 ):
        cmp = '<'
      elif ( d1 > d2 ):
        cmp = '>'
      else:
#
#  ...if necessary, compare fractional parts.
#
        if ( f1 < f2 ):
          cmp = '<'
        elif ( f1 > f2 ):
          cmp = '>'
        else:
          cmp = '='

  return cmp

def ymdf_next_common ( y1, m1, d1, f1 ):

#*****************************************************************************80
#
## YMDF_NEXT_COMMON returns the Common YMDF date of the next day.
#
#  Discussion:
#
#    The routine knows that in the Common calendar, the day after
#    4 October 1582 was 15 October 1582.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y1, M1, D1, real F1, the YMDF date.
#
#    Output, integer Y2, M2, D2, real F2, tomorrow's YMDF date.
#
  y2 = y1
  m2 = m1
  d2 = d1 + 1
  f2 = f1

  y2, m2, d2 = day_carry_common ( y2, m2, d2 )

  return y2, m2, d2, f2

def ymdf_to_jed_common ( y, m, d, f ):

#*****************************************************************************80
#
## YMDF_TO_JED_COMMON converts a Common YMDF date to a JED.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    day JED = 2299160, and Gregorian from day JED = 2299161 and after.
#
#    The Julian Ephemeris Date is essentially a count of the number
#    of days that have elapsed since noon, 1 January 4713 BC, at
#    Greenwich, England.  Strictly speaking, the Julian Ephemeris Date
#    is counted from noon, and thus day "0" began at noon on 1 January 4713 BC,
#    and ended at noon on 2 January 4713 BC.
#
#    The Julian Ephemeris Date was devised by Joseph Scaliger in 1583.
#
#    The Julian Ephemeris Date has been adopted by astronomers as
#    a convenient reference for dates.
#
#  Example:
#
#       Y   M     D         JED
#    --------------     -------
#    BC 4713 Jan  1           0
#    AD 1968 May 23     2440000
#    AD 1984 Dec 31     2446065
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 April 2010
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, real F, the YMDF date.
#
#    Output, real JED, the Julian Ephemeris Date.
#
  from sys import exit
#
#  Copy the month and year.
#
  y2 = 1582
  m2 = 10
  d2 = 4+1
  f2 = 0.0

  cmp = ymdf_compare ( y, m, d, f, y2, m2, d2, f2 )

  if ( cmp == '<' ):
    jed = ymdf_to_jed_julian ( y, m, d, f )
    return jed
#
#  Use the Gregorian calendar for dates strictly after 1752/9/13.
#
  y2 = 1582
  m2 = 10
  d2 = 15-1
  f2 = 0.0

  cmp = ymdf_compare ( y, m, d, f, y2, m2, d2, f2 )

  if ( cmp == '>' ):
    jed = ymdf_to_jed_gregorian ( y, m, d, f )
    return jed

  print ( '' )
  print ( 'YMDF_TO_JED_COMMON - Fatal error!' )
  print ( '  Illegal date!' )
  exit ( 'YMDF_TO_JED_COMMON - Fatal error!' )

  return jed

def ymdf_to_jed_gregorian ( y, m, d, f ):

#*****************************************************************************80
#
## YMDF_TO_JED_GREGORIAN converts a Gregorian YMDF date to a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 April 2010
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Richards,
#    Algorithm E,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, pages 323-324.
#
#  Parameters:
#
#    Input, integer Y, M, D, real F, the YMDF date.
#
#    Output, real JED, the corresponding JED.
#
  import numpy as np
#
#  Account for the missing year 0 by moving negative years up one.
#
  y2 = y_common_to_astronomical ( y )
#
#  Convert the calendar date to a computational date.
#
  y_prime = y2 + 4716 - int ( np.floor ( ( 14 - m ) / 12.0 ) )
  m_prime = ( ( m + 9 ) % 12 )
  d_prime = d - 1
#
#  Convert the computational date to a JED.
#
  j1 = np.floor ( ( 1461 * y_prime ) / 4.0 )

  j2 = np.floor ( ( 153 * m_prime + 2 ) / 5.0 )

  g = ( np.floor ( 3 * ( np.floor ( ( y_prime + 184 ) / 100.0 ) ) / 4.0 ) ) - 38

  jed = j1 + j2 + d_prime - 1401 - g - 0.5
  jed = jed + f

  return jed

def ymdf_to_jed_julian ( y, m, d, f ):

#*****************************************************************************80
#
## YMDF_TO_JED_JULIAN converts a Julian YMDF date to a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Richards,
#    Algorithm E,
#    Mapping Time, The Calendar and Its History,
#    Oxford, 1999, pages 323-324.
#
#  Parameters:
#
#    Input, integer Y, M, D, real F, the YMDF date.
#
#    Output, real JED, the Julian Ephemeris Date.
#
  import numpy as np
#
#  Account for the missing year 0 by moving negative years up one.
#
  y2 = y_common_to_astronomical ( y )
#
#  Convert the calendar date to a computational date.
#
  y_prime = y2 + 4716 - int ( np.floor ( ( 14 - m ) / 12.0 ) )
  m_prime = ( ( m + 9 ) % 12 )
  d_prime = d - 1
#
#  Convert the computational date to a JED.
#
  j1 = np.floor ( ( 1461 * y_prime ) / 4.0 )

  j2 = np.floor ( ( 153 * m_prime + 2 ) / 5.0 )

  jed = j1 + j2 + d_prime - 1401.0 - 0.5
  jed = jed + f

  return jed

def ymdf_to_s_common ( y, m, d, f ):

#*****************************************************************************80
#
## YMDF_TO_S_COMMON writes a Common YMDF date into a string.
#
#  Format:
#
#    CE YYYY/MM/DD.FF
#    BCE YYYY/MM/DD.FF
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, double F, the YMDF date.
#
#    Output, string S, a representation of the date.
#
  if ( 0 <= y ):
    s = 'CE %d/%d/%d%.2f' % ( y, m, d, f )
  else:
    s = 'BCE %d/%d/%d%.2f' % ( -y, m, d, f )
 
  return s

def ymdf_to_weekday_common ( y, m, d, f ):

#*****************************************************************************80
#
## YMD_TO_WEEKDAY_COMMON returns the weekday of a Common YMDF date.
#
#  Discussion:
#
#    The "common" calendar is meant to be the calendar which is Julian up to
#    day JED = 2299160, and Gregorian from day JED = 2299161 and after.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, F, the YMDF date.
#
#    Output, integer W, is the week day number of the date, with
#    1 for Sunday, through 7 for Saturday.
#
  jed = ymdf_to_jed_common ( y, m, d, f )

  w, f2 = jed_to_weekday ( jed )

  return w

def ymdhms_check_common ( y, m, d, h, n, s ):

#*****************************************************************************80
#
## YMDHMS_CHECK_COMMON checks a Common YMDHMS date.
#
#  Discussion:
#
#    The routine will correct certain simple errors in dates, such as
#      "11:03:42 31 September 1996"
#    which will become
#      "11:03:42 1 October 1996".
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer Y, M, D, H, N, S.
#    These items have the obvious meanings.
#    The routine may change any of these values to more reasonable values.
#
#    Output, integer IERROR, is 0 if no error was detected in the
#    date, and 1 otherwise.
#

#
#  Check that the second is between 0 and 59.
#  N may get bumped up or down.
#
  y, m, d, h, n, s = second_borrow_common ( y, m, d, h, n, s )

  y, m, d, h, n, s = second_carry_common ( y, m, d, h, n, s )
#
#  Check that the minute is between 0 and 59.
#  H may get bumped up or down.
#
  y, m, d, h, n = minute_borrow_common ( y, m, d, h, n )

  y, m, d, h, n = minute_carry_common ( y, m, d, h, n )
#
#  Check that the hour is between 0 and 23.
#  D may get bumped up or down.
#
  y, m, d, h = hour_borrow_common ( y, m, d, h )

  y, m, d, h = hour_carry_common ( y, m, d, h )
#
#  Now make adjustments to D, M, and Y.
#
  y, m, d, ierror = ymd_check_common ( y, m, d )

  return y, m, d, h, n, s, ierror

def ymdhms_to_jed_common ( y, m, d, h, n, s ):

#*****************************************************************************80
#
## YMDHMS_TO_JED_COMMON converts a Common YMDHMS date to a JED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y, M, D, H, N, S, the YMDHMS date.
#
#    Output, real JED, the Julian Ephemeris Date.
#
  y1, m1, d1, f1 = ymdhms_to_ymdf_common ( y, m, d, h, n, s )

  jed = ymdf_to_jed_common ( y1, m1, d1, f1 )

  return jed

def ymdhms_to_ymdf_common ( y1, m1, d1, h1, n1, s1 ):

#*****************************************************************************80
#
## YMDHMS_TO_YMDF_COMMON converts a YMDHMS date to a YMDF date.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer Y1, M1, D1, H1, N1, S1,
#    the year, month, day, hour, minute and second of the date.
#
#    Output, integer Y2, M2, D2, real F2, 
#    the YMDF date.
#
  from sys import exit
#
#  Check the date.
#
  y, m, d, h, n, s, ierror = ymdhms_check_common ( y1, m1, d1, h1, n1, s1 )

  if ( ierror != 0 ):
    print ( '' )
    print ( 'YMDHMS_TO_YMDF_COMMON - Fatal error!' )
    exit ( 1 )

  y2 = y1
  m2 = m1
  d2 = d1
#
#  Now compute the day fraction.
#
  f2 = ( ( h1 * 60 + n1 ) * 60 + s1 ) / ( 24 * 60 * 60 )

  return y2, m2, d2, f2

def calpak_test ( ):

#*****************************************************************************80
#
## CALPAK_TEST tests the CALPAK library.
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
  print ( 'CALPAK_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CALPAK library.' )

  ch_cap_test ( )
  datenum_to_jed_test ( )
  datenum_values_test ( )
  day_list_common_test ( )
  easter_gregorian_ds_test ( )
  easter_gregorian_egr_test ( )
  easter_gregorian_egr2_test ( )
  easter_gregorian_knuth_test ( )
  easter_gregorian_stewart_test ( )
  easter_julian_egr_test ( )
  easter_julian_egr2_test ( )
  gps_to_jed_test ( )
  i4_modp_test ( )
  i4_normal_ab_test ( )
  i4_uniform_ab_test ( )
  i4_wrap_test ( )
  jed_ce_values_test ( )
  jed_is_legal_test ( )
  jed_mjd_values_test ( )
  jed_rd_values_test ( )
  jed_to_datenum_test ( )
  jed_to_gps_test ( )
  jed_to_noon_nearest_test ( )
  jed_to_noon_next_test ( )
  jed_to_weekday_test ( )
  jed_weekday_values_test ( )
  month_to_month_name_common_test ( )
  month_to_month_name_common3_test ( )
  r8_mod_test ( )
  r8_uniform_01_test ( )
  weekday_to_name_common_test ( )
  weekday_to_name_common2_test ( )
  weekday_to_name_common3_test ( )
  weekday_values_test ( )
  y_common_to_astronomical_test ( )
  y_to_s_common_test ( )
  year_is_leap_gregorian_test ( )
  year_length_days_common_test ( )
  year_to_golden_number_test ( )
  ymd_to_weekday_common_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CALPAK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  calpak_test ( )
  timestamp ( )
