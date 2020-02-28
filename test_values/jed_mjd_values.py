#! /usr/bin/env python
#
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

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jed_mjd_values_test ( )
  timestamp ( )

