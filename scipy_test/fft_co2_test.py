#! /usr/bin/env python3
#
def fft_co2_test ( ):

#*****************************************************************************80
#
## fft_co2_test() tests the scipy() FFT function on CO2 data
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
  from scipy.fft import fft
  from scipy.fft import ifft
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fft_co2_test():' )
  print ( '  Use fft() and ifft() to analyze variation in CO2 levels. ' )

  data = np.loadtxt ( 'co2_data.txt' )

  y = data[:,1]
  n = len ( y )
  t = np.arange ( n )

  plt.clf ( )
  plt.plot ( t, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- CO2(t)  -->' )
  plt.title ( 'CO2 concentration' )
  filename = 'fft_co2_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  B = 300.81
  d = 14.18
  alpha = 0.0037
  y = y - B - d * np.exp ( alpha * t )

  plt.clf ( )
  plt.plot ( t, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- CO2(t)  -->' )
  plt.title ( 'CO2 concentration after trend removal' )
  filename = 'fft_co2_detrended.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  z = fft ( y )
  nh = n // 2 + 1
  omega = np.arange ( nh )
# power = np.sqrt ( z * np.conj ( z ) ) / np.sqrt ( nh )
  power = np.abs ( z ) / np.sqrt ( nh )

  plt.clf ( )
  plt.plot ( omega, power[0:nh], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- frequency -->' )
  plt.ylabel ( '<-- power  -->' )
  plt.title ( 'CO2 periodogram' )
  filename = 'fft_co2_periodogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

if ( __name__ == "__main__" ):
  fft_co2_test ( )

