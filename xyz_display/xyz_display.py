#! /usr/bin/env python3
#
def xyz_display_test ( ):

#*****************************************************************************80
#
## xyz_display_test() tests xyz_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'xyz_display_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test xyz_display()' )

  xyz_filename = 'helix_201.xyz'
  xyz_display ( xyz_filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'xyz_display_test():' )
  print ( '  Normal end of execution.' )

  return

def xyz_display ( xyz_filename ):

#*****************************************************************************80
#
## xyz_display() plots a set of points in 3D.
#
#  Discussion:
#
#    The data is stored in a text file with N rows and 3 columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Usage:
#
#    xyz_display ( 'filename.xyz' )
#
#  Input:
#
#    string xyz_filename: the name of the data file.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Read the data.
#
  xyz = np.loadtxt ( xyz_filename )
  point_num = xyz.shape[0]

  print ( '' )
  print ( '  Number of points POINT_NUM  = ', point_num )
  print ( '' )
  print ( '  First 5 nodes:' )
  print ( xyz[0:min(point_num,5),0:3] )

  plt.clf ( )
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.scatter ( xyz[:,0], xyz[:,1], xyz[:,2] )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->', fontsize = 16 )
  ax.set_ylabel ( '<-- Y -->', fontsize = 16 )
  ax.set_zlabel ( '<-- X -->', fontsize = 16 )
  ax.set_title ( xyz_filename )
  filename = 'xyz_display.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def s_escape_tex ( s1 ):

#*****************************************************************************80
#
## s_escape_tex() de-escapes TeX escape sequences.
#
#  Discussion:
#
#    In particular, every occurrence of the characters '\', '_',
#    '^', '{' and '}' will be replaced by '\\', '\_', '\^',
#    '\{' and '\}'.  A TeX interpreter, on seeing these character
#    strings, is then likely to return the original characters.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S1, the string to be de-escaped.
#
#  Output:
#
#    string S2, a copy of the string, modified to avoid TeX escapes.
#
  s1_length = len ( s1 )

  s1_pos = 0
  s2_pos = 0
  s2 = ''

  while ( s1_pos < s1_length ):

    if ( s1[s1_pos] == '\\' or \
         s1[s1_pos] == '_' or \
         s1[s1_pos] == '^' or \
         s1[s1_pos] == '{' or \
         s1[s1_pos] == '}' ):
      s2_pos = s2_pos + 1
      s2 = s2 + '\\'

    s2_pos = s2_pos + 1
    s2 = s2 + s1[s1_pos]

    s1_pos = s1_pos + 1

  return s2

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
  xyz_display_test ( )
  timestamp ( )

