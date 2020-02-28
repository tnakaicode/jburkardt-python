#! /usr/bin/env python3
#
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
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

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
  for y in range ( -10, 11 ):
    if ( y != 0 ):
      y2 = y_common_to_astronomical ( y )
      print ( '  %8d  %14d' % ( y, y2 ) )

  return
  
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

def weekday_test ( ):

#*****************************************************************************80
#
## WEEKDAY_TEST tests the WEEKDAY library.
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
  print ( 'WEEKDAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the WEEKDAY library.' )

  i4_modp_test ( )
  i4_wrap_test ( )
  jed_to_weekday_test ( )
  jed_weekday_values_test ( )
  weekday_to_name_common_test ( )
  weekday_values_test ( )
  y_common_to_astronomical_test ( )
  ymd_to_weekday_common_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEEKDAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  weekday_test ( )
  timestamp ( )
