#! /usr/bin/env python3
#
def image_boundary_test ( ):

#*****************************************************************************80
#
## image_boundary_test() tests image_boundary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'image_boundary_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  image_boundary() finds edges in an image.' );
  print ( '' )

  image_file = 'cloud.png'
  boundary_file = 'cloud_boundary.png'
  image_boundary ( image_file, boundary_file )
  print ( '  Analyzed file "' + image_file + '"' )
  print ( '  Boundary file "' + boundary_file + '"' )
#
#  Terminate.
#
  print ( '' );
  print ( 'image_edge_test():' )
  print ( '  Normal end of execution.' )

  return

def image_boundary ( image_file, boundary_file ):

#*****************************************************************************80
#
## image_boundary() selects and displays the boundary edges in an image.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2024
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
#    image_file: the name of the file to be analyzed.
#
#    boundary_file: the name of the file to contain the highlighted boundary.
#
  from PIL import Image
  from PIL import ImageFilter

  image_data = Image.open ( image_file )
  boundary_data = image_data.filter ( ImageFilter.CONTOUR )
  boundary_data.save ( boundary_file )

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
  image_boundary_test ( )
  timestamp ( )
 
