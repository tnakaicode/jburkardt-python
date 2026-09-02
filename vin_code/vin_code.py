#! /usr/bin/env python3
#
def vin_code_test ( ):

#*****************************************************************************80
#
## vin_code_test() tests vin_code().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Vehicle Identification Number (VIN) Check Sum,
#    https://www.johndcook.com/blog/2019/09/12/vin-check-sum/
#    12 September 2019.
#
#    John D Cook,
#    Computing VIN Checksums,
#    https://www.johndcook.com/blog/2022/09/04/computing-vin-checksums/
#    04 September 2022.
#
  import numpy as np
  import platform

  vin_data = [ \
    "11111111111111111", \
    "5GZCZ43D13S812715", \
    "1M8GDM9AXKP042788", \
    "2M8GDM9AXKP042788", \
    "1M8GDM9AXKPO42788" ]

  print ( '' )
  print ( 'vin_code_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  vin_code() verifies a Vehicle Identification Number (VIN).' )

  for vin in vin_data:
    print ( '"' + vin + '"', end = '' )
    print ( '  ', checksum ( vin ), end = '' )
    print ( '  ', validate ( vin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'vin_code_test():' )
  print ( '  Normal end of execution.' )

  return

def vin_char_to_num ( ch ):

#*****************************************************************************80
#
## vin_char_to_num() converts a VIN character to a numeric value.
#
#  Discussion:
#
#    Assumes all characters are digits 0-9 or capital letters (A-Z) 
#    but excluding 'I', 'O' and 'Q'.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 May 2026
#
#  Input:
#
#    character CH: the character to be converted.
#    CH should be a character representing a digit '0' through '9',
#    or an upper case letter 'A' through 'Z', omitting 'I', 'O', and 'Q'.
#
#  Output:
#
#    integer VALUE: the corresponding value.
#
  from math import nan
#
#  Get the ASCII numeric code for the character.
#
  n = ord ( ch )
#
#  '0' through '9':
#  '0'  '1'  '2'  '3'  '4'  '5'  '6'  '7'  '8'  '9'
#   0    1    2    3    4    5    6    7    8    9
#
  if ( ord ( '0' ) <= n and n <= ord ( '9' ) ):
    value = n - ord ( '0' )
#
#  'A' through 'H' (skip 'I')
#  'A'  'B'  'C'  'D'  'E'  'F'  'G'  'H'  'I'
#   1    2    3    4    5    6    7    8    *
#
  elif ( ord ( 'A' ) <= n and n <= ord ( 'H' ) ):
    value = n - ord ('A') + 1
#
#  'J' through 'R' (skip 'O' and 'Q')
#  'J'  'K'  'L'  'M'  'N'  'O'  'P'  'Q'  'R'
#   1    2    3    4    5    *    7    *    9 
#
  elif ( ord ( 'J' ) <= n and n <= ord ( 'N' ) ):
    value = n - ord ('J') + 1  
  elif ( ord ( 'P' ) == n ):
    value = n - ord ('J') + 1 
  elif ( ord ( 'R' ) == n ):
    value = n - ord ('J') + 1   
#
#  'S' through 'Z', and start at 2!
#  'S'  'T'  'U'  'V'  'W'  'X'  'Y'  'Z'
#   2    3    4    5    6    7    8    9 
#
  elif ( ord ( 'S' ) <= n and n <= ord ( 'Z' ) ):
    value = n - ord ( 'S' ) + 2
#
#  Character is not legal.
#
  else:
    value = nan

  return value
        
def checksum ( vin ):

#*****************************************************************************80
#
## checksum() computes the checksum of a VIN.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 September 2022
#
#  Input:
#
#    string vin: a VIN.
#
#  Output:
#
#    character check: the VIN checksum.
#
  from math import isnan

  if ( len ( vin ) != 17 ):
    check = '*'
    return check

  w = [ 8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2 ]

  t = 0
  for i, c in enumerate ( vin ):
    t = t + vin_char_to_num ( c ) * w[i]
#
#  If any C was illegal, then t is a NaN, and the check should be '*'.
#
  if ( isnan ( t ) ):
    check = '*'
    return check

  t = ( t % 11 )

  if ( t == 10 ):
    check = 'X'
  else:
    check = str ( t )

  return check

def validate ( vin ):

#*****************************************************************************80
#
## validate() reports whether a VIN is valid.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 September 2022
#
#  Input:
#
#    string vin: a VIN.
#
#  Output:
#
#    logical result: True if the VIN is valid.
#
  result = ( checksum ( vin ) == vin[8] )

  return result

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  vin_code_test ( )
  timestamp ( )

