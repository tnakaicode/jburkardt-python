#! /usr/bin/python3
#
def pbma_write ( file_name, comment, width, height, bits ):

#*****************************************************************************80
#
## PBMA_WRITE writes an ASCII PBM graphics file.
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
#    Input, string COMMENT, a comment, which may be empty ('');
#
#    Input, integer WIDTH, HEIGHT, the width and height of the graphics image.
#
#    Input, integer BITS[WIDTH,HEIGHT], bits values of 0 or 1.
#
  file_type = 'P1'

  file_handle = open ( file_name, 'wt' )
  file_handle.write ( "%s\n" % ( file_type ) ) 
  file_handle.write ( "#%s\n" % ( comment ) ) 
  file_handle.write ( "%d %d\n" % ( width, height ) ) 

  for i in range ( height ):
    for j in range ( width ):
      file_handle.write ( " %d" % ( bits[i,j] ) ) 
    file_handle.write ( "\n" )

  file_handle.close ( )

  return

def pbma_write_test ( ):

#*****************************************************************************80
#
## PBMA_WRITE_TEST tests PBMA_WRITE.
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

  print ( '' )
  print ( 'PBMA_WRITE_TEST:' )
  print ( '  PBMA_WRITE writes an ASCII PBM graphics file.' )

  file_name = 'pbma_io.pbm'

  comment = 'Example ASCII PBM graphics file.'

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

  pbma_write ( file_name, comment, width, height, bits )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PBMA_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  pbma_write_test ( )

