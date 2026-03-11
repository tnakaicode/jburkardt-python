#! /usr/bin/env python3
#
def fft_el_nino_test ( ):

#*****************************************************************************80
#
## fft_el_nino_test() tests the scipy() FFT function on el Nino data.
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
  from scipy.fft import fftfreq
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fft_el_nino_test():' )
  print ( '  Use fft() to interpolate el nino pressure variation data. ' )

  data = np.loadtxt ( 'el_nino_data.txt' )

  t = data[:,0]
  y = data[:,1]
  n = len ( y )

  plt.clf ( )
  plt.plot ( t, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- pressure(t)  -->' )
  plt.title ( 'El nino pressure variation' )
  filename = 'fft_el_nino_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Compute fft.
#
  z = fft ( y ) 
  freq = fftfreq ( n, t )[:n//2]
  print ( freq )
  a = z.real * 2 / n
  print ( a )
  b = z.imag * 2 / n
  nh = n // 2
  y2 = 0.5 * z[0].real * np.ones ( n )
  for i in range ( 1, 40 ):
    y2 = y2 + a[i] * np.cos ( 2.0 * np.pi * freq[i] * t ) \
            + b[i] * np.sin ( 2.0 * np.pi * freq[i] * t )

  plt.clf ( )
  plt.plot ( t, y2, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- pressure(t)  -->' )
  plt.title ( 'El nino pressure variation' )
  filename = 'fft_el_nino_recovered.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

if ( __name__ == "__main__" ):
  fft_el_nino_test ( )

