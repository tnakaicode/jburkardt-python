#! /usr/bin/env python3
#
def char_to_num ( ch ):

#*****************************************************************************80
#
## char_to_num() converts a VIN character to a numeric value.
#
#  Discussion:
#
#    Assumes all characters are digits or capital letters.
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
#    character CH: the character to be converted.
#
#  Output:
#
#    integer VALUE: the corresponding value.
#
  n = ord ( ch )
#
#  Digits.
#
  if n <= ord('9'):
    value = n - ord('0')
#
#  A through I.
#
  elif n < ord('I'):
    value = n - ord('A') + 1
#
#  J through R
#
  elif n <= ord('R'):
    value = n - ord('J') + 1    
#
#  S through Z.
#
  else:
    value = n - ord('S') + 2

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
  assert ( len ( vin ) == 17 )

  w = [ 8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2 ]

  t = 0
  for i, c in enumerate ( vin ):
    t = t + char_to_num ( c ) * w[i]
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

def vin_test ( ):

#*****************************************************************************80
#
## vin_test() tests vin().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 September 2022
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
    "1M8GDM9AXKP042788" ]

  print ( '' )
  print ( 'vin_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  vin() verifies a Vehicle Identification Number (VIN).' )

  for vin in vin_data:
    print ( '"' + vin + '"', end = '' )
    print ( '  ', checksum ( vin ), end = '' )
    print ( '  ', validate ( vin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'vin_test():' )
  print ( '  Normal end of execution.' )

  return

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
  vin_test ( )
  timestamp ( )


