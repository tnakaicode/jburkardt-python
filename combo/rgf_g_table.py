#! /usr/bin/env python
#
def rgf_g_table ( m ):

#*****************************************************************************80
#
## RGF_G_TABLE tabulates the generalized restricted growth functions.
#
#  Example:
#
#    M = 6
#
#    D =  1    1    1    1    1    1    1
#         1    2    3    4    5    6    0
#         2    5   10   17   26    0    0
#         5   15   37   77    0    0    0
#        15   52  151    0    0    0    0
#        52  203    0    0    0    0    0
#       203    0    0    0    0    0    0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer M, indicates how many rows and columns are to
#    be computed.  M must be nonnegative.
#
#    Output, integer D(1:M+1,1:M+1), the first M+1 rows and
#    M+1 columns of the table of the number of generalized restricted growth
#    functions.  D(I+1,J+1) is the number of GRGF's of length I with restriction
#    parameter J.
#
  import numpy as np

  d = np.zeros ( [ m + 1, m + 1 ] )

  for j in range ( 0, m + 1 ):
    d[0,j] = 1

  for i in range ( 1, m + 1 ):
    for j in range ( 0, m + 1 ):
      if ( j <= m - i ):
        d[i,j] = j * d[i-1,j] + d[i-1,j+1]

  return d

def rgf_g_table_test ( ):

#*****************************************************************************80
#
## RGF_G_TABLE_TEST tests RGF_G_TABLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 6

  print ( '' )
  print ( 'RGF_G_TABLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_G_TABLE tabulates generalized restricted' )
  print ( '  growth functions.' )
  print ( '' )

  d = rgf_g_table ( m )

  for i in range ( 0, m + 1 ):
    for j in range ( 0, m - i + 1 ):
      print ( '%6d' % ( d[i,j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_G_TABLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_g_table_test ( )
  timestamp ( )
 
