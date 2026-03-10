#! /usr/bin/env python3
#
def image_edge_test ( ):

#*****************************************************************************80
#
## image_edge_test() tests image_edge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'image_edge_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  image_edge() detects edges in an image.' );
  print ( '' )

# image_file = 'coins.ascii.pgm'
  image_file = 'coins.png'
  edge_file = 'coins.edge.png'
  image_edge ( image_file, edge_file )
  print ( '  Analyzed file "' + image_file + '"' )
  print ( '  Highlighted edges in "' + edge_file + '"' )
#
#  Terminate.
#
  print ( '' );
  print ( 'image_edge_test():' )
  print ( '  Normal end of execution.' )

  return

def image_edge ( image_file, edge_file ):

#*****************************************************************************80
#
## image_edge() selects the edges in an image.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2024
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
#    edge_file: the name of the file to contain the highlighted edges.
#
  from PIL import Image
  from PIL import ImageFilter

  image_data = Image.open ( image_file )
  edge_data = image_data.filter ( ImageFilter.FIND_EDGES )
  edge_data.save ( edge_file )

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
  image_edge_test ( )
  timestamp ( )
 
