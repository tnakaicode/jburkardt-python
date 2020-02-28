#! /usr/bin/python3
#
def pgmb_write ( file_name, width, height, maxval, gray ):

#*****************************************************************************80
#
## PGMB_WRITE writes a binary PGM graphics file.
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
#    Input, string FILE_NAME, the name of the file.
#
#    Input, integer WIDTH, HEIGHT, the width and height of the graphics image.
#
#    Input, integer MAXVAL, the maximum allowed gray value.
#
#    Input, integer GRAY[WIDTH*HEIGHT], values between 0 and MAXVAL.
#
  import numpy as np
  import struct

  file_handle = open ( file_name, 'wb' )
#
#  Set up the header.
#
  pgm_header = f'P5 {width} {height} {maxval}\n'
  file_handle.write ( bytearray ( pgm_header, 'ascii' ) ) 
#
#  Convert 2D array to 1D vector.
#
  grayV = np.reshape ( gray, width * height )
#
#  Pack entries of vector into a string of bytes, replacing each integer
#  as an unsigned 1 byte character.
#
  grayB = struct.pack ( '%sB' % len(grayV), *grayV )
  file_handle.write ( grayB )
 
  file_handle.close ( )

  return

def pgmb_write_test ( ):

#*****************************************************************************80
#
## PGMB_WRITE_TEST tests PGMB_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PGMB_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PGMB_WRITE writes a binary PGM graphics file.' )

  file_name = 'pgmb_io.pgm'
  width = 24
  height = 7
  maxval = 255

  gray = np.array \
  ( [ \
    [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], \
    [ 0,  64,  64,  64,  64,   0,   0, 128, 128, 128, 128,   0,   0, 192, 192, 192, 192,   0,   0, 255, 255, 255, 255,   0], \
    [ 0,  64,   0,   0,   0,   0,   0, 128,   0,   0,   0,   0,   0, 192,   0,   0,   0,   0,   0, 255,   0,   0, 255,   0], \
    [ 0,  64,  64,  64,   0,   0,   0, 128, 128, 128,   0,   0,   0, 192, 192, 192,   0,   0,   0, 255, 255, 255, 255,   0], \
    [ 0,  64,   0,   0,   0,   0,   0, 128,   0,   0,   0,   0,   0, 192,   0,   0,   0,   0,   0, 255,   0,   0,   0,   0], \
    [ 0,  64,   0,   0,   0,   0,   0, 128, 128, 128, 128,   0,   0, 192, 192, 192, 192,   0,   0, 255,   0,   0,   0,   0], \
    [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]  \
  ] )

  pgmb_write ( file_name, width, height, maxval, gray )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PGMB_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  pgmb_write_test ( )
