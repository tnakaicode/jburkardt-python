#! /usr/bin/env python
#
def domino_tiling_num ( m, n ):

#*****************************************************************************80
#
## DOMINO_TILING_NUM counts tilings of an MxN rectangle by dominoes.
#
#  Discussion:
#
#    An 8x8 chessboard has 12,988,816 such tilings.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 June 2018
#
#  Author:
#
#    Original Python version by John D Cook.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Output, integer VALUE, the number of tilings.
#
  import numpy as np

  value = 1
  for k in range ( 1, m + 1 ):
    for l in range ( 1, n + 1 ):
      value = value * 2 * (        np.cos ( np.pi * k / ( m + 1 ) ) 
                            + 1j * np.cos ( np.pi * l / ( n + 1 ) ) )

  value = round ( np.sqrt ( abs ( value ) ) )

  return value
        
def domino_tiling_num_test ( ):

#*****************************************************************************80
#
## DOMINO_TILING_NUM_TEST tests DOMINO_TILING_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 June 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DOMINO_TILING_NUM_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DOMINO_TILING_NUM returns the number of tilings of an' )
  print ( '  MxN rectangle by dominoes.' )
  print ( '' )
  print ( '   M   N    Tilings' )
  for m in range ( 1, 9 ):
    print ( '' )
    for n in range ( 1, m + 1 ):
      value = domino_tiling_num ( m, n )
      print ( '  %d  %d  %d' % ( m, n, value ) )
  
  print ( '' )
  print ( 'DOMINO_TILING_NUM_TEST:' )
  print ( '  Normal end of execution.' )

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  domino_tiling_num_test ( )
  timestamp ( )
