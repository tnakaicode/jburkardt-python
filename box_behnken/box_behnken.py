#! /usr/bin/env python3
#
def box_behnken_test ( ):

#*****************************************************************************80
#
## box_behnken_test() tests box_behnken().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'box_behnken_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test box_behnken().' )

  box_behnken_test01 ( )
  box_behnken_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'box_behnken_test():' )
  print ( '  Normal end of execution.' )

  return

def box_behnken_test01 ( ):

#*****************************************************************************80
#
## box_behnken_test01() tests box_behnken().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  dim_num = 3

  lohi = np.array ( [ \
    [  0.0, 10.0,  5.0 ], \
    [  1.0, 11.0, 15.0 ] ] )

  print ( '' )
  print ( 'box_behnken_test01():' )
  print ( '  box_behnken() computes a Box-Behnken dataset.' )

  print ( '' )
  print ( '  The ranges:' )
  pprint.pprint ( lohi )

  x_num = box_behnken_size ( dim_num )

  print ( '' )
  print ( '  For dimension DIM_NUM = ', dim_num )
  print ( ' the Box-Behnken design is of size ', x_num )

  x = box_behnken ( dim_num, x_num, lohi )

  print ( '' )
  print ( '  The Box-Behnken design:' )
  pprint.pprint ( x )

  return

def box_behnken_test02 ( ):

#*****************************************************************************80
#
## box_behnken_test02() writes a Box-Behnken dataset to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  dim_num = 4

  lohi = np.array ( [ \
    [ 0.0, 0.0, 0.0, 0.0 ], \
    [ 1.0, 1.0, 1.0, 1.0 ] ] )

  print ( '' )
  print ( 'box_behnken_test02()' )
  print ( '  Write a Box-Behnken dataset to a file.' )

  print ( '' )
  print ( '  The ranges:' )
  pprint.pprint ( lohi )

  x_num = box_behnken_size ( dim_num )

  print ( '' )
  print ( '  For dimension DIM_NUM = ', dim_num )
  print ( '  the Box-Behnken design is of size ', x_num )

  x = box_behnken ( dim_num, x_num, lohi )

  filename = 'box_behnken_04_33.txt'

  np.savetxt ( filename, x )

  print ( '' )
  print ( '  The data was written to "' + filename + '".' )

  return

def box_behnken ( dim_num, x_num, lohi ):

#*****************************************************************************80
#
## box_behnken() returns a Box-Behnken design for the given number of factors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Box, Donald Behnken,
#    Some new three level designs for the study of quantitative variables,
#    Technometrics,
#    Volume 2, pages 455-475, 1960.
#
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#
#    integer X_NUM, the number of elements of the design.
#    X_NUM should be equal to DIM_NUM * 2^(DIM_NUM-1) + 1.
#
#    real lohi[2,DIM_NUM], the minimum and maximum
#    value for each component.
#
#  Output:
#
#    real X[X_NUM,DIM_NUM], the elements of the design.
#
  import numpy as np
#
#  Allocate space.
#
  x = np.zeros ( [ x_num, dim_num ] )
#
#  The first point, J = 0, is the center.
#
  j = 0
  x[j,:] = ( lohi[0,:] + lohi[1,:] ) / 2.0
#
#  For subsequent elements, one entry is fixed at the middle of the range.
#  The others are set to either extreme.
#
  for i in range ( 0, dim_num ):

    j = j + 1

    x[j,:] = lohi[0,:]
    x[j,i] = ( lohi[0,i] + lohi[1,i] ) / 2.0
#
#  The next element is made by finding the last low value, making it
#  high, and all subsequent high values low.
#
    while ( True ):

      last_low = -1

      for i2 in range ( 0, dim_num ):
        if ( x[j,i2] == lohi[0,i2] ):
          last_low = i2

      if ( last_low == -1 ):
        break

      j = j + 1
      x[j,:] = x[j-1,:]
      x[j,last_low] = lohi[1,last_low]

      for i2 in range ( last_low + 1, dim_num ):
        if ( x[j,i2] == lohi[1,i2] ):
          x[j,i2] = lohi[0,i2]

  return x

def box_behnken_size ( dim_num ):

#*****************************************************************************80
#
## box_behnken_size() returns the size of a Box-Behnken design.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Box, Donald Behnken,
#    Some new three level designs for the study of quantitative variables,
#    Technometrics,
#    Volume 2, pages 455-475, 1960.
#
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#
#  Output:
#
#    integer X_NUM, the number of elements of the design.
#    X_NUM will be equal to DIM_NUM * 2^(DIM_NUM-1) + 1.
#
  if ( 1 <= dim_num ):
    x_num = 1 + dim_num * 2**( dim_num - 1 )
  else:
    x_num = -1

  return x_num

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
  box_behnken_test ( )
  timestamp ( )


