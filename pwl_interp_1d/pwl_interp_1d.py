#! /usr/bin/env python3
#
def p00_data_num ( prob ):

#*****************************************************************************80
#
## p00_data_num() returns the number of data points for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  if ( prob == 1 ):
    data_num = p01_data_num ( )
  elif ( prob == 2 ):
    data_num = p02_data_num ( )
  elif ( prob == 3 ):
    data_num = p03_data_num ( )
  elif ( prob == 4 ):
    data_num = p04_data_num ( )
  elif ( prob == 5 ):
    data_num = p05_data_num ( )
  elif ( prob == 6 ):
    data_num = p06_data_num ( )
  elif ( prob == 7 ):
    data_num = p07_data_num ( )
  elif ( prob == 8 ):
    data_num = p08_data_num ( )
  else:
    print ( '' )
    print ( 'p00_data_num - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    raise Exception ( 'p00_data_num - Fatal error!' )

  return data_num

def p01_data_num ( ):

#*****************************************************************************80
#
## p01_data_num() returns the number of data points for problem p01.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 18

  return data_num

def p02_data_num ( ):

#*****************************************************************************80
#
## p02_data_num() returns the number of data points for problem p02.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 18

  return data_num

def p03_data_num ( ):

#*****************************************************************************80
#
## p03_data_num() returns the number of data points for problem p03.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 11

  return data_num

def p04_data_num ( ):

#*****************************************************************************80
#
## p04_data_num() returns the number of data points for problem p04.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 8

  return data_num

def p05_data_num ( ):

#*****************************************************************************80
#
## p05_data_num() returns the number of data points for problem p05.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 9

  return data_num

def p06_data_num ( ):

#*****************************************************************************80
#
## p06_data_num() returns the number of data points for problem p06.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 49

  return data_num

def p07_data_num ( ):

#*****************************************************************************80
#
## p07_data_num() returns the number of data points for problem p07.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 4

  return data_num

def p08_data_num ( ):

#*****************************************************************************80
#
## p08_data_num() returns the number of data points for problem p08.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DATA_num, the number of data points.
#
  data_num = 12

  return data_num

def p00_data_num_test ( ):

#*****************************************************************************80
#
## p00_data_num_test() tests p00_data_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p00_data_num_test' )
  print ( '  p00_data_num() returns the number of data points for any problem.' )
  print ( '' )
  print ( '  Problem   Data Num' )
  print ( '' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    data_num = p00_data_num ( prob )

    print ( '  %7d  %9d' % ( prob, data_num ) )

  return

def p00_data ( prob, dim_num, data_num ):

#*****************************************************************************80
#
## p00_data() returns the data for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  if ( prob == 1 ):
    p_data = p01_data ( dim_num, data_num )
  elif ( prob == 2 ):
    p_data = p02_data ( dim_num, data_num )
  elif ( prob == 3 ):
    p_data = p03_data ( dim_num, data_num )
  elif ( prob == 4 ):
    p_data = p04_data ( dim_num, data_num )
  elif ( prob == 5 ):
    p_data = p05_data ( dim_num, data_num )
  elif ( prob == 6 ):
    p_data = p06_data ( dim_num, data_num )
  elif ( prob == 7 ):
    p_data = p07_data ( dim_num, data_num )
  elif ( prob == 8 ):
    p_data = p08_data ( dim_num, data_num )
  else:
    print ( '' )
    print ( 'p00_data - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    raise Exception ( 'p00_data - Fatal error!' )

  return p_data

def p01_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p01_data() returns the data for problem p01.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
    [  0.0, 4.0 ], \
    [  1.0, 5.0 ], \
    [  2.0, 6.0 ], \
    [  4.0, 6.0 ], \
    [  5.0, 5.0 ], \
    [  6.0, 3.0 ], \
    [  7.0, 1.0 ], \
    [  8.0, 1.0 ], \
    [  9.0, 1.0 ], \
    [ 10.0, 3.0 ], \
    [ 11.0, 4.0 ], \
    [ 12.0, 4.0 ], \
    [ 13.0, 3.0 ], \
    [ 14.0, 3.0 ], \
    [ 15.0, 4.0 ], \
    [ 16.0, 4.0 ], \
    [ 17.0, 3.0 ], \
    [ 18.0, 0.0 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p02_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p02_data() returns the data for problem p02.
#
#  Discussion:
#
#    Two pairs of identical X values have now been slightly separated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [  0.00,   0.00 ], \
   [  1.34,   5.00 ], \
   [  5.00,   8.66 ], \
   [ 10.00,  10.00 ], \
   [ 10.60,  10.40 ], \
   [ 10.70,  12.00 ], \
   [ 10.705, 28.60 ], \
   [ 10.80,  30.20 ], \
   [ 11.40,  30.60 ], \
   [ 19.60,  30.60 ], \
   [ 20.20,  30.20 ], \
   [ 20.295, 28.60 ], \
   [ 20.30,  12.00 ], \
   [ 20.40,  10.40 ], \
   [ 21.00,  10.00 ], \
   [ 26.00,   8.66 ], \
   [ 29.66,   5.00 ], \
   [ 31.00,   0.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p03_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p03_data() returns the data for problem p03.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
    [  0.0,  0.0 ], \
    [  2.0, 10.0 ], \
    [  3.0, 10.0 ], \
    [  5.0, 10.0 ], \
    [  6.0, 10.0 ], \
    [  8.0, 10.0 ], \
    [  9.0, 10.5 ], \
    [ 11.0, 15.0 ], \
    [ 12.0, 50.0 ], \
    [ 14.0, 60.0 ], \
    [ 15.0, 85.0 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p04_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p04_data() returns the data for problem p04.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ 0.00,  0.00 ], \
   [ 0.05,  0.70 ], \
   [ 0.10,  1.00 ], \
   [ 0.20,  1.00 ], \
   [ 0.80,  0.30 ], \
   [ 0.85,  0.05 ], \
   [ 0.90,  0.10 ], \
   [ 1.00,  1.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p05_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p05_data() returns the data for problem p05.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
    [ 0.00, 0.00 ], \
    [ 0.10, 0.90 ], \
    [ 0.20, 0.95 ], \
    [ 0.30, 0.90 ], \
    [ 0.40, 0.10 ], \
    [ 0.50, 0.05 ], \
    [ 0.60, 0.05 ], \
    [ 0.80, 0.20 ], \
    [ 1.00, 1.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p06_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p06_data() returns the data for problem p06.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ 595.0, 0.644 ], \
   [ 605.0, 0.622 ], \
   [ 615.0, 0.638 ], \
   [ 625.0, 0.649 ], \
   [ 635.0, 0.652 ], \
   [ 645.0, 0.639 ], \
   [ 655.0, 0.646 ], \
   [ 665.0, 0.657 ], \
   [ 675.0, 0.652 ], \
   [ 685.0, 0.655 ], \
   [ 695.0, 0.644 ], \
   [ 705.0, 0.663 ], \
   [ 715.0, 0.663 ], \
   [ 725.0, 0.668 ], \
   [ 735.0, 0.676 ], \
   [ 745.0, 0.676 ], \
   [ 755.0, 0.686 ], \
   [ 765.0, 0.679 ], \
   [ 775.0, 0.678 ], \
   [ 785.0, 0.683 ], \
   [ 795.0, 0.694 ], \
   [ 805.0, 0.699 ], \
   [ 815.0, 0.710 ], \
   [ 825.0, 0.730 ], \
   [ 835.0, 0.763 ], \
   [ 845.0, 0.812 ], \
   [ 855.0, 0.907 ], \
   [ 865.0, 1.044 ], \
   [ 875.0, 1.336 ], \
   [ 885.0, 1.881 ], \
   [ 895.0, 2.169 ], \
   [ 905.0, 2.075 ], \
   [ 915.0, 1.598 ], \
   [ 925.0, 1.211 ], \
   [ 935.0, 0.916 ], \
   [ 945.0, 0.746 ], \
   [ 955.0, 0.672 ], \
   [ 965.0, 0.627 ], \
   [ 975.0, 0.615 ], \
   [ 985.0, 0.607 ], \
   [ 995.0, 0.606 ], \
   [1005.0, 0.609 ], \
   [1015.0, 0.603 ], \
   [1025.0, 0.601 ], \
   [1035.0, 0.603 ], \
   [1045.0, 0.601 ], \
   [1055.0, 0.611 ], \
   [1065.0, 0.601 ], \
   [1075.0, 0.608 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p07_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p07_data() returns the data for problem p07.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ 0.0, 1.0 ], \
   [ 1.0, 2.0 ], \
   [ 4.0, 2.0 ], \
   [ 5.0, 1.0 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p08_data ( dim_num, data_num ):

#*****************************************************************************80
#
## p08_data() returns the data for problem p08.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_num, the spatial dimension of the dependent
#    variables.
#
#    integer DATA_num, the number of data points.
#
#  Output:
#
#    real P_data(DIM_num,DATA_num), the data.
#
  import numpy as np

  p_data = np.array ( [ \
   [ -1.0, 1.00 ], \
   [ -0.8, 0.64 ], \
   [ -0.6, 0.36 ], \
   [ -0.4, 0.16 ], \
   [ -0.2, 0.04 ], \
   [  0.0, 0.00 ], \
   [  0.2, 0.04 ], \
   [  0.20001, 0.05 ], \
   [  0.4, 0.16 ], \
   [  0.6, 0.36 ], \
   [  0.8, 0.64 ], \
   [  1.0, 1.00 ] ] )

  p_data = np.transpose ( p_data )

  return p_data

def p00_data_test ( ):

#*****************************************************************************80
#
## p00_data_test() tests p00_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p00_data_test():' )
  print ( '  p00_data() returns the actual (MxN) data for any problem.' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem %d' % ( prob ) )

    data_num = p00_data_num ( prob )
    print ( '  DATA_num = %d' % ( data_num ) )

    dim_num = p00_dim_num ( prob )
    print ( '  DIM_num  = %d' % ( dim_num ) )

    p = p00_data ( prob, dim_num, data_num )

    r8mat_transpose_print ( dim_num, data_num, p, '  Data array:' )

  return

def p00_dim_num ( prob ):

#*****************************************************************************80
#
## p00_dim_num() returns the spatial dimension for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  if ( prob == 1 ):
    dim_num = p01_dim_num ( )
  elif ( prob == 2 ):
    dim_num = p02_dim_num ( )
  elif ( prob == 3 ):
    dim_num = p03_dim_num ( )
  elif ( prob == 4 ):
    dim_num = p04_dim_num ( )
  elif ( prob == 5 ):
    dim_num = p05_dim_num ( )
  elif ( prob == 6 ):
    dim_num = p06_dim_num ( )
  elif ( prob == 7 ):
    dim_num = p07_dim_num ( )
  elif ( prob == 8 ):
    dim_num = p08_dim_num ( )
  else:
    print ( '' )
    print ( 'p00_dim_num - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    raise Exception ( 'p00_dim_num - Fatal error!' )

  return dim_num

def p01_dim_num ( ):

#*****************************************************************************80
#
## p01_dim_num() returns the spatial dimension for problem p01.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p02_dim_num ( ):

#*****************************************************************************80
#
## p02_dim_num() returns the spatial dimension for problem p02.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p03_dim_num ( ):

#*****************************************************************************80
#
## p03_dim_num() returns the spatial dimension for problem p03.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p04_dim_num ( ):

#*****************************************************************************80
#
## p04_dim_num() returns the spatial dimension for problem p04.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p05_dim_num ( ):

#*****************************************************************************80
#
## p05_dim_num() returns the spatial dimension for problem p05.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p06_dim_num ( ):

#*****************************************************************************80
#
## p06_dim_num() returns the spatial dimension for problem p06.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p07_dim_num ( ):

#*****************************************************************************80
#
## p07_dim_num() returns the spatial dimension for problem p07.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p08_dim_num ( ):

#*****************************************************************************80
#
## p08_dim_num() returns the spatial dimension for problem p08.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer DIM_num, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p00_dim_num_test ( ):

#*****************************************************************************80
#
## p00_dim_num_test() tests p00_dim_num.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p00_dim_num_test' )
  print ( '  p00_dim_num() returns the spatial dimension for any problem.' )
  print ( '' )
  print ( '  Problem  Dimension' )
  print ( '' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    dim_num = p00_dim_num ( prob )

    print ( '  %7d  %9d' % ( prob, dim_num ) )

  return

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num() returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer VALUE, the number of problems.
#
  value = 8

  return value

def p00_prob_num_test ( ):

#*****************************************************************************80
#
## p00_prob_num_test() tests p00_prob_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p00_prob_num_test' )
  print ( '  p00_prob_num() returns the number of test problems.' )

  num = p00_prob_num ( )

  print ( '' )
  print ( '  test_interp includes %d test problems.' % ( num ) )

  return

def pwl_basis_1d ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## pwl_basis_1d() evaluates a 1D piecewise linear basis function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND), the data points.
#
#    integer NI, the number of interpolation points.
#
#    real XI(NI), the interpolation points.
#
#  Output:
#
#    real BK(NI,ND), the basis functions at the interpolation points.
#
  import numpy as np

  if ( nd == 1 ):
    bk = np.ones ( [ ni, nd ] )
    return bk

  bk = np.zeros ( [ ni, nd ] )

  for i in range ( 0, ni ):

    for j in range ( 0, nd ):

      if ( j == 0 and xi[i] <= xd[j] ):

        t = ( xi[i] - xd[j] ) / ( xd[j+1] - xd[j] )
        bk[i,j] = 1.0 - t

      elif ( j == nd - 1 and xd[j] <= xi[i] ):

        t = ( xi[i] - xd[j-1] ) / ( xd[j] - xd[j-1] )
        bk[i,j] = t

      elif ( xd[j-1] < xi[i] and xi[i] <= xd[j] ):

        t = ( xi[i] - xd[j-1] ) / ( xd[j] - xd[j-1] )
        bk[i,j] = t

      elif ( xd[j] <= xi[i] and xi[i] < xd[j+1] ):

        t = ( xi[i] - xd[j] ) / ( xd[j+1] - xd[j] )
        bk[i,j] = 1.0 - t

  return bk

def pwl_basis_1d_test ( ):

#*****************************************************************************80
#
## pwl_basis_1d_test() tests pwl_basis_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 4
  ni = 21

  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
 
  print ( '' )
  print ( 'pwl_basis_1d_test:' )
  print ( '  pwl_basis_1d evaluates the piecewise linear 1D basis' )
  print ( '  functions.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  lb = pwl_basis_1d ( nd, xd, ni, xi )

  r8mat_print ( ni, nd, lb, '  The PWL basis functions:' )

  return

def pwl_interp_1d_test ( ):

#*****************************************************************************80
#
## pwl_interp_1d_test() tests pwl_interp_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pwl_interp_1d_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pwl_interp_1d().' )
#
#  Utility functions.
#
  p00_data_test ( )
  p00_data_num_test ( )
  p00_dim_num_test ( )
  p00_prob_num_test ( )
#
#  Library functions.
#
  pwl_basis_1d_test ( )
  pwl_value_1d_test ( )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    for nd in ( [ 4, 8, 16, 32, 64 ] ):
      pwl_interp_1d_test01 ( prob, nd )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    for nd in ( [ 4, 8, 16, 32, 64 ] ):
      pwl_interp_1d_test02 ( prob, nd )
#
#  Terminate.
#
  print ( '' )
  print ( 'pwl_interp_1d_test():' )
  print ( '  Normal end of execution.' )
  return

def pwl_interp_1d_test01 ( prob, nd ):

#*****************************************************************************80
#
## pwl_interp_1d_test01() tests pwl_value_1d() with evenly spaced data
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'pwl_interp_1d_test01():' )
  print ( '  Interpolate data from test_interp() problem # %d.' % ( prob ) )
  print ( '  Use even spacing for data points.' )
  print ( '  Number of data points = %d' % ( nd ) )

  nd = p00_data_num ( prob )
  print ( '  Number of data points = %d' % ( nd ) )

  xy = p00_data ( prob, 2, nd )
  
  xd = np.zeros ( nd )
  yd = np.zeros ( nd )
  for i in range ( 0, nd ):
    xd[i] = xy[0,i]
    yd[i] = xy[1,i]
 
  if ( nd < 10 ):
    r8vec2_print ( nd, xd, yd, '  Data array:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = pwl_value_1d ( nd, xd, yd, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Plot the piecewise linear interpolant.
#
  ni = 501
  xmin = np.min ( xd )
  xmax = np.max ( xd )
  xi = np.linspace ( xmin, xmax, ni )
  yi = pwl_value_1d ( nd, xd, yd, ni, xi )

  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xi, yi, 'r-', linewidth = 4.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Lagrange/Even Polynomial Interpolant for ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_pwl_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def pwl_interp_1d_test02 ( prob, nd ):

#*****************************************************************************80
#
## pwl_interp_1d_test02() plots the basis functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'pwl_interp_1d_test02:' )
  print ( '  Plot the basis functions for test_interp problem # %d.' % ( prob ) )

  nd = p00_data_num ( prob )

  print ( '  Number of data points = %d' % ( nd ) )

  xy = p00_data ( prob, 2, nd )
  
  xd = np.zeros ( nd )
  for i in range ( 0, nd ):
    xd[i] = xy[0,i]

  r8vec_print ( nd, xd, '  X data locations:' )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 501
  xmin = np.min ( xd )
  xmax = np.max ( xd )
  xi = np.linspace ( xmin, xmax, ni )
  bk = pwl_basis_1d ( nd, xd, ni, xi )

  for k in range ( 0, nd ):
    plt.plot ( xi, bk[:,k], 'r-', linewidth = 4.0 )

  t = 'p0' + str ( prob ) + ' basis functions ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_pwl_basis_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def pwl_value_1d ( nd, xd, yd, ni, xi ):

#*****************************************************************************80
#
## pwl_value_1d() evaluates the piecewise linear interpolant.
#
#  Discussion:
#
#    The piecewise linear interpolant L(ND,XD,YD)(X) is the piecewise
#    linear function which interpolates the data (XD(I),YD(I)) for I = 1
#    to ND.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#    ND must be at least 1.
#
#    real XD(ND), the data points.
#
#    real YD(ND), the data values.
#
#    integer NI, the number of interpolation points.
#
#    real XI(NI), the interpolation points.
#
#  Output:
#
#    real YI(NI), the interpolated values.
#
  import numpy as np

  if ( nd == 1 ):
    yi = np.ones ( ni ) * yd[0]
    return yi

  yi = np.zeros ( ni )

  for i in range ( 0, ni ):
 
    if ( xi[i] <= xd[0] ):

      t = ( xi[i] - xd[0] ) / ( xd[1] - xd[0] )
      yi[i] = ( 1.0 - t ) * yd[0] + t * yd[1]

    elif ( xd[nd-2] <= xi[i] ):

      t = ( xi[i] - xd[nd-2] ) / ( xd[nd-1] - xd[nd-2] )
      yi[i] = ( 1.0 - t ) * yd[nd-2] + t * yd[nd-1]

    else:

      for k in range ( 1, nd ):
 
        if ( xd[k-1] <= xi[i] and xi[i] <= xd[k] ):

          t = ( xi[i] - xd[k-1] ) / ( xd[k] - xd[k-1] )
          yi[i] = ( 1.0 - t ) * yd[k-1] + t * yd[k]
  
  return yi

def pwl_value_1d_test ( ):

#*****************************************************************************80
#
## pwl_value_1d_test() tests pwl_value_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 4
  ni = 21
#
#  Values of f(x) = x^3 - 12 x^2 + 39 x -28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
#
  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
  yd = np.array ( [ -28.0, +10.0, -8.0, +162.0 ] )
 
  print ( '' )
  print ( 'pwl_value_1d_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pwl_value_1d evaluates a piecewise linear 1D interpolant.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  yi = pwl_value_1d ( nd, xd, yd, ni, xi )

  r8vec2_print ( ni, xi, yi, '  Table of interpolant values:' )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_transpose_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ' ),

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ) ),

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ) ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_transpose_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print_some prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  pwl_interp_1d_test ( )
  timestamp ( )

