#! /usr/bin/env python3
#
def ppm_example ( width, height ):

#*****************************************************************************80
#
## PPM_EXAMPLE sets up sample RGB data suitable for a PPM file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer WIDTH, HEIGHT, the number of columns and rows of data.
#    Reasonable values would be WIDTH = 200, HEIGHT = 600.
#
#    Output, integer RGB[WIDTH*HEIGHT,3], the RGB data.
#
  import numpy as np

  rgb = np.zeros ( [width * height, 3 ], dtype = np.int32 )

  k = 0

  for i in range ( 0, height ):

    y = float ( height - 1 - i ) / float ( height - 1 )

    for j in range ( 0, width ):

      x = float ( j ) / float ( width - 1 )

      f1 = 4.0 * ( x - 0.5 ) ** 2
      f2 = np.sin ( np.pi * x )
      f3 = x

      if ( y <= f1 ):
        rgb[k,0] = int ( 255.0 * f1 )
      else:
        rgb[k,0] = 50

      if ( y <= f2 ):
        rgb[k,1] = int ( 255.0 * f2 )
      else:
        rgb[k,1] = 150

      if ( y <= f3 ):
        rgb[k,2] = int ( 255.0 * f3 )
      else:
        rgb[k,2] = 250

      k = k + 1

  return rgb

def ppma_write ( file_name, width, height, rgb ):

#*****************************************************************************80
#
## PPMA_WRITE writes an ASCII PPM graphics file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILE_NAME, the name of the file.
#
#    Input, integer WIDTH, HEIGHT, the width and height of the graphics image.
#
#    Input, integer RGB[3,WIDTH*HEIGHT], a list of WIDTH*HEIGHT triples
#    of R, G, B values between 0 and 255.
#
  file_type = 'P3'

  file_handle = open ( file_name, 'wt' )
  file_handle.write ( "%s\n" % ( file_type ) ) 
  file_handle.write ( "%d %d\n" % ( width, height ) ) 
  file_handle.write ( "255\n" )

  for red, green, blue in rgb:
    file_handle.write ( "%d %d %d\n" % ( red, green, blue ) ) 

  file_handle.close ( )

  return

def ppma_write_test ( ):

#*****************************************************************************80
#
## PPMA_WRITE_TEST tests PPMA_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'PPMA_WRITE_TEST:' )
  print ( '  PPMA_WRITE writes an ASCII PPM graphics file.' )

  file_name = 'ppma_io.ppm'
#
#  Tiny example:
#
  width = 3
  height = 2

  rgb = \
  [ \
    [ 255,   0,   0 ], \
    [   0, 255,   0 ], \
    [   0,   0, 255 ], \
    [ 255, 255,   0 ], \
    [ 255, 255, 255 ], \
    [   0,   0,   0 ]  \
  ]
#
#  Large example.
#
  width = 200
  height = 600
  rgb = ppm_example ( width, height )

  ppma_write ( file_name, width, height, rgb )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PPMA_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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

if ( __name__ == '__main__' ):
  timestamp ( )
  ppma_write_test ( )
  timestamp ( )
