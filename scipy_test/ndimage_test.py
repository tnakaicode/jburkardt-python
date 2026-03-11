#! /usr/bin/env python3
#
def ndimage_test ( ):

#*****************************************************************************80
#
## ndimage_test() tests some scipy.ndimage() functions for image analysis.
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
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy as sp
  import scipy.ndimage as nd

  print ( '' )
  print ( 'ndimage_test():' )
  print ( '  Apply ndimage() functions to manipulate an image.' )

  filename = 'face.png'
  face = plt.imread ( filename )
  print ( '  Reading original image from "' + filename + '"' )
  plt.imshow ( face )

  face_rotated = nd.rotate ( face, 45 )
  plt.imshow ( face_rotated )
  filename = 'ndimage_rotated.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  face_blurred = nd.gaussian_filter ( face, sigma = 3 )
  plt.imshow ( face_blurred )
  filename = 'ndimage_blurred.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

if ( __name__ == "__main__" ):
  ndimage_test ( )

