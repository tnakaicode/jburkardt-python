#! /usr/bin/env python3
#
def image_rgb_to_gray_test ( ):

#*****************************************************************************80
#
## image_rgb_to_gray_test() tests image_rgb_to_gray().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'image_rgb_to_gray_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  image_rgb_to_gray() converts an RGB image to grayscale.' );
  print ( '' )

  rgb_file = 'conjunction.png'
  gray_file = 'conjunction_gray.png'
  image_rgb_to_gray ( rgb_file, gray_file )
  print ( '  Converted ' + rgb_file + ' to ' + gray_file )

  rgb_file = 'star_field.png'
  gray_file = 'star_field_gray.png'
  image_rgb_to_gray ( rgb_file, gray_file )
  print ( '  Converted ' + rgb_file + ' to ' + gray_file )
#
#  Terminate.
#
  print ( '' );
  print ( 'image_rgb_to_gray_test():' )
  print ( '  Normal end of execution.' )

  return

def image_rgb_to_gray ( rgb_file, gray_file ):

#*****************************************************************************80
#
## image_rgb_to_gray() writes a grayscale version of the image in an RGB file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#  Michael Driscoll,
#  Pillow: Image Processing with Python
#
#  Input:
#
#    rgb_file: the name of the RGB file to be converted.
#
#    gray_file: the name of the file for the gray scale version.
#
  from PIL import Image

  rgb_image = Image.open ( rgb_file )
  gray_image = rgb_image.convert ( "L" )
  gray_image.save ( gray_file )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  image_rgb_to_gray_test ( )
  timestamp ( )
 
