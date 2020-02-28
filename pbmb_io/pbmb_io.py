#! /usr/bin/python3
#
def pbmb_write ( file_name, width, height, bits ):

#*****************************************************************************80
#
## PBMB_WRITE writes a binary PBM graphics file.
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
#    Input, integer BITS[WIDTH*HEIGHT], values of 0 or 1.
#
  import numpy as np

  pbm_header = f'P4 {width} {height}\n'

  file_handle = open ( file_name, 'wb' )

  file_handle.write ( bytearray ( pbm_header, 'ascii' ) ) 

  np.packbits ( bits, axis = -1 ).tofile ( file_handle )

  file_handle.close ( )

  return

def pbmb_write_test ( ):

#*****************************************************************************80
#
## PBMB_WRITE_TEST tests PBMB_WRITE.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'PBMB_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PBMB_WRITE writes a binary PBM graphics file.' )

  file_name = 'pbmb_io.pbm'

  width = 24
  height = 7

  bits = np.array \
  ( [ \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0 ], \
    [ 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0 ], \
    [ 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]  \
  ] )

  pbmb_write ( file_name, width, height, bits )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PBMB_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  pbmb_write_test ( )
