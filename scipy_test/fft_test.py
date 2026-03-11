#! /usr/bin/env python3
#
def fft_test ( ):

#*****************************************************************************80
#
## fft_test() tests the scipy() fft() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  from scipy.fft import fft, ifft
  import numpy as np

  print ( '' )
  print ( 'fft_test():' )

  x = np.array ( [ 1.0, 2.0, 1.0, -1.0, 1.5 ] )
  print ( '' )
  print ( '  x:' )
  print ( x )

  y = fft ( x )

  print ( '' )
  print ( '  y = fft(x):' )
  print ( y )

  z = ifft ( y )

  print ( '' )
  print ( '  z = ifft(y):' )
  print ( z )

  return

if ( __name__ == "__main__" ):
  fft_test ( )

