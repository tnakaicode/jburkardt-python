#! /usr/bin/env python3
#
def p00_data_num ( prob ):

#*****************************************************************************80
#
## P00_DATA_NUM returns the number of data points for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Output, integer DATA_NUM, the number of data points.
#
  from sys import exit

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
    print ( 'P00_DATA_NUM - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_DATA_NUM - Fatal error!' )

  return data_num

def p01_data_num ( ):

#*****************************************************************************80
#
## P01_DATA_NUM returns the number of data points for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 18

  return data_num

def p02_data_num ( ):

#*****************************************************************************80
#
## P02_DATA_NUM returns the number of data points for problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 18

  return data_num

def p03_data_num ( ):

#*****************************************************************************80
#
## P03_DATA_NUM returns the number of data points for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 11

  return data_num

def p04_data_num ( ):

#*****************************************************************************80
#
## P04_DATA_NUM returns the number of data points for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 8

  return data_num

def p05_data_num ( ):

#*****************************************************************************80
#
## P05_DATA_NUM returns the number of data points for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 9

  return data_num

def p06_data_num ( ):

#*****************************************************************************80
#
## P06_DATA_NUM returns the number of data points for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 49

  return data_num

def p07_data_num ( ):

#*****************************************************************************80
#
## P07_DATA_NUM returns the number of data points for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 4

  return data_num

def p08_data_num ( ):

#*****************************************************************************80
#
## P08_DATA_NUM returns the number of data points for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DATA_NUM, the number of data points.
#
  data_num = 12

  return data_num

def p00_data_num_test ( ):

#*****************************************************************************80
#
## P00_DATA_NUM_TEST tests P00_DATA_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P00_DATA_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_DATA_NUM returns the number of data points for any problem.' )
  print ( '' )
  print ( '  Problem   Data Num' )
  print ( '' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    data_num = p00_data_num ( prob )

    print ( '  %7d  %9d' % ( prob, data_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_DATA_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_data ( prob, dim_num, data_num ):

#*****************************************************************************80
#
## P00_DATA returns the data for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
#
  from sys import exit

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
    print ( 'P00_DATA - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_DATA - Fatal error!' )

  return p_data

def p01_data ( dim_num, data_num ):

#*****************************************************************************80
#
## P01_DATA returns the data for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P02_DATA returns the data for problem p02.
#
#  Discussion:
#
#    Two pairs of identical X values have now been slightly separated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P03_DATA returns the data for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P04_DATA returns the data for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P05_DATA returns the data for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P06_DATA returns the data for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P07_DATA returns the data for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P08_DATA returns the data for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension of the dependent
#    variables.
#
#    Input, integer DATA_NUM, the number of data points.
#
#    Output, real P_DATA(DIM_NUM,DATA_NUM), the data.
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
## P00_DATA_TEST tests P00_DATA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P00_DATA_TEST tests P00_DATA' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_DATA returns the actual (MxN) data for any problem.' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem %d' % ( prob ) )

    data_num = p00_data_num ( prob )
    print ( '  DATA_NUM = %d' % ( data_num ) )

    dim_num = p00_dim_num ( prob )
    print ( '  DIM_NUM  = %d' % ( dim_num ) )

    p = p00_data ( prob, dim_num, data_num )

    r8mat_transpose_print ( dim_num, data_num, p, '  Data array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_DATA_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_dim_num ( prob ):

#*****************************************************************************80
#
## P00_DIM_NUM returns the spatial dimension for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Output, integer DIM_NUM, the spatial dimension of the
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
    print ( 'P00_DIM_NUM - Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    exit ( 'P00_DIM_NUM - Fatal error!' )

  return dim_num

def p01_dim_num ( ):

#*****************************************************************************80
#
## P01_DIM_NUM returns the spatial dimension for problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p02_dim_num ( ):

#*****************************************************************************80
#
## P02_DIM_NUM returns the spatial dimension for problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p03_dim_num ( ):

#*****************************************************************************80
#
## P03_DIM_NUM returns the spatial dimension for problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p04_dim_num ( ):

#*****************************************************************************80
#
## P04_DIM_NUM returns the spatial dimension for problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p05_dim_num ( ):

#*****************************************************************************80
#
## P05_DIM_NUM returns the spatial dimension for problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p06_dim_num ( ):

#*****************************************************************************80
#
## P06_DIM_NUM returns the spatial dimension for problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p07_dim_num ( ):

#*****************************************************************************80
#
## P07_DIM_NUM returns the spatial dimension for problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p08_dim_num ( ):

#*****************************************************************************80
#
## P08_DIM_NUM returns the spatial dimension for problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer DIM_NUM, the spatial dimension of the
#    dependent variables.
#
  dim_num = 2

  return dim_num

def p00_dim_num_test ( ):

#*****************************************************************************80
#
## P00_DIM_NUM_TEST tests P00_DIM_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P00_DIM_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_DIM_NUM returns the spatial dimension for any problem.' )
  print ( '' )
  print ( '  Problem  Dimension' )
  print ( '' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    dim_num = p00_dim_num ( prob )

    print ( '  %7d  %9d' % ( prob, dim_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_DIM_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_prob_num ( ):

#*****************************************************************************80
#
## P00_PROB_NUM returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer VALUE, the number of problems.
#
  value = 8

  return value

def p00_prob_num_test ( ):

#*****************************************************************************80
#
## P00_PROB_NUM_TEST tests P00_PROB_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P00_PROB_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_PROB_NUM returns the number of test problems.' )

  num = p00_prob_num ( )

  print ( '' )
  print ( '  TEST_INTERP includes %d test problems.' % ( num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PROB_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## R8POLY_PRINT prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the nominal degree of the polynomial.
#
#    Input, real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## R8POLY_PRINT_TEST tests R8POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8POLY_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_PRINT prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_PRINT_TEST:' )
  print ( '  Normal end of execution.' )

  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
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
## R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm_affine ( n, v0, v1 ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE returns the affine norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The affine vector L2 norm is defined as:
#
#      R8VEC_NORM_AFFINE(V0,V1) 
#        = sqrt ( sum ( 1 <= I <= N ) ( V1(I) - V0(I) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the vector dimnension.
#
#    Input, real V0(N), the base vector.
#
#    Input, real V1(N), the vector.
#
#    Output, real VALUE, the affine L2 norm.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ): 
    value = value + ( v0[i] - v1[i] ) ** 2
  value =  np.sqrt ( value )

  return value

def r8vec_norm_affine_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE_TEST tests R8VEC_NORM_AFFINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_AFFINE computes the L2 norm of' )
  print ( '  the difference of two R8VECs.' )

  seed = 123456789;

  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  z = np.zeros ( n )
  for i in range ( 0, n ):
    z[i] = x[i] - y[i]

  print ( '' )
  print ( '  R8VEC_NORM_AFFINE(X,Y) = %g' % ( r8vec_norm_affine ( n, x, y ) ) )
  print ( '  R8VEC_NORM (X-Y):        %g' % ( r8vec_norm ( n, z ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L2 norm is desired.
#
#    Output, real VALUE, the L2 norm of A.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = np.sqrt ( value )

  return value

def r8vec_norm_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_TEST tests R8VEC_NORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM computes the L2 norm of an R8VEC.' )

  n = 10
  seed = 123456789
  a, seed = r8vec_uniform_01 ( n, seed )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm ( n, a )

  print ( '' )
  print ( '  L2 norm = %g' % ( a_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_AB - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_AB computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def vandermonde_coef_1d ( n, x, y ):

#*****************************************************************************80
#
## VANDERMONDE_COEF_1D computes coefficients of a 1D Vandermonde interpolant.
#
#  Discussion:
#
#    We assume the interpolant has the form
#
#      p(x) = c1 + c2 * x + c3 * x^2 + ... + cn * x^(n-1).
#
#    We have n data values (x(i),y(i)) which must be interpolated:
#
#      p(x(i)) = c1 + c2 * x(i) + c3 * x(i)^2 + ... + cn * x(i)^(n-1) = y(i)
#
#    This can be cast as an NxN linear system for the polynomial
#    coefficients:
#
#      [ 1 x1 x1^2 ... x1^(n-1) ] [  c1 ] = [  y1 ]
#      [ 1 x2 x2^2 ... x2^(n-1) ] [  c2 ] = [  y2 ]
#      [ ...................... ] [ ... ] = [ ... ]
#      [ 1 xn xn^2 ... xn^(n-1) ] [  cn ] = [  yn ]
#
#    and if the x values are distinct, the system is theoretically
#    invertible, so we can retrieve the coefficient vector c and
#    evaluate the interpolant.
#
#    The polynomial could be evaluated at the n-vector x by the command
#
#      pval = polyval ( c, x )
#
#    ...except that MATLAB assumes that c(1) multiplies x^(n-1).
#
#    so instead, you might use
#
#      pval = r8poly_value ( n - 1, c, n, x )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data points.
#
#    Input, real X(N,1), Y(N,1), the data values.
#
#    Output, real C(N,1), the coefficients of the interpolating
#    polynomial.  C(1) is the constant term, and C(N) multiplies X^(N-1).
#
  import numpy as np

  ad = vandermonde_matrix_1d ( n, x )

  c = np.linalg.solve ( ad, y )
 
  return c

def vandermonde_coef_1d_test ( ):

#*****************************************************************************80
#
## VANDERMONDE_COEF_1D_TEST tests VANDERMONDE_COEF_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 5
  xd = np.array ( [ 0.0, 1.0, 2.0, 3.0, 4.0 ] )
  yd = np.array ( [ 24.0, 0.0, 0.0, 0.0, 0.0 ] )

  print ( '' )
  print ( 'VANDERMONDE_COEF_1D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VANDERMONDE_COEF_1D sets the Vandermonde coefficients for 1D interpolation.' )

  r8vec2_print ( nd, xd, yd, '  Interpolation data:' )

  cd = vandermonde_coef_1d ( nd, xd, yd )

  r8vec_print ( nd, cd, '  Vandermonde interpolant coefficients:' )

  r8poly_print ( nd - 1, cd, '  Vandermonde interpolant polynomial:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VANDERMONDE_COEF_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def vandermonde_interp_1d_test ( ):

#*****************************************************************************80
#
## VANDERMONDE_INTERP_1D_TEST tests the VANDERMONDE_INTERP_1D library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'VANDERMONDE_INTERP_1D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the VANDERMONDE_INTERP_1D library.' )
#
#  Utility functions.
#
  p00_data_test ( )
  p00_data_num_test ( )
  p00_dim_num_test ( )
  p00_prob_num_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
  r8poly_print_test ( )
  r8vec_norm_test ( )
  r8vec_norm_affine_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )
  r8vec2_print_test ( )
#
#  Library functions.
#
  vandermonde_coef_1d_test ( )
  vandermonde_matrix_1d_test ( )
  vandermonde_value_1d_test ( )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    vandermonde_interp_1d_test01 ( prob )
#
#  Terminate.
#
  print ( '' )
  print ( 'VANDERMONDE_INTERP_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def vandermonde_interp_1d_test01 ( prob ):

#*****************************************************************************80
#
## VANDERMONDE_INTERP_1D_TEST01 tests VANDERMONDE_VALUE_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'VANDERMONDE_INTERP_1D_TEST01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Interpolate data from TEST_INTERP problem #%d.' % ( prob ) )

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
#  Get Vandermonde interpolant coefficients.
#
  cd = vandermonde_coef_1d ( nd, xd, yd )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = vandermonde_value_1d ( nd, cd, ni, xi )

  int_error = r8vec_norm_affine ( ni, yi, yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  xmin = np.min ( xd )
  xmax = np.max ( xd )
  ymin = np.min ( yd )
  ymax = np.max ( yd )

  ni = 501
  xi = np.linspace ( xmin, xmax, ni )
  yi = vandermonde_value_1d ( nd, cd, ni, xi )

  ld = 0.0
  for i in range ( 0, nd - 1 ):
    ld = ld + np.sqrt \
    ( \
        ( ( xd[i+1] - xd[i] ) / ( xmax - xmin ) ) ** 2 \
      + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2 \
    )

  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + np.sqrt \
    ( \
        ( ( xi[i+1] - xi[i] ) / ( xmax - xmin ) ) ** 2 \
      + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2 \
    )
  li = np.sqrt ( li )

  print ( '' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of Shepard interpolant          = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Piecewise Linear Interpolant'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_data.png'
  plt.savefig ( filename )
  plt.clf ( )

  print ( '' )
  print ( '  Created plot file "%s"' % ( filename ) )
#
#  #4: Plot the piecewise linear and Vandermonde interpolants.
#
  ni = 501
  xmin = np.min ( xd )
  xmax = np.max ( xd )
  xi = np.linspace ( xmin, xmax, ni )
  yi = vandermonde_value_1d ( nd, cd, ni, xi )

  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xi, yi, 'r-', linewidth = 4.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Vandermonde Interpolant for ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_vandermonde.png'
  plt.savefig ( filename )
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'VANDERMONDE_INTERP_1D_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def vandermonde_matrix_1d ( n, x ):

#*****************************************************************************80
#
## VANDERMONDE_MATRIX_1D computes a Vandermonde 1D interpolation matrix.
#
#  Discussion:
#
#    We assume the interpolant has the form
#
#      p(x) = c1 + c2 * x + c3 * x^2 + ... + cn * x^(n-1).
#
#    We have n data values (x(i),y(i)) which must be interpolated:
#
#      p(x(i)) = c1 + c2 * x(i) + c3 * x(i)^2 + ... + cn * x(i)^(n-1) = y(i)
#
#    This can be cast as an NxN linear system for the polynomial
#    coefficients:
#
#      [ 1 x1 x1^2 ... x1^(n-1) ] [  c1 ] = [  y1 ]
#      [ 1 x2 x2^2 ... x2^(n-1) ] [  c2 ] = [  y2 ]
#      [ ...................... ] [ ... ] = [ ... ]
#      [ 1 xn xn^2 ... xn^(n-1) ] [  cn ] = [  yn ]
#
#    and if the x values are distinct, the matrix A is theoretically
#    invertible (though in fact, generally badly conditioned).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data points.
#
#    Input, real X(N,1), the data values.
#
#    Output, real A(N,N), the Vandermonde matrix for X.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    a[i,0] = 1.0

  for j in range ( 1, n ):
    for i in range ( 0, n ):
      a[i,j] = a[i,j-1] * x[i]

  return a

def vandermonde_matrix_1d_test ( ):

#*****************************************************************************80
#
## VANDERMONDE_MATRIX_1D_TEST tests VANDERMONDE_MATRIX_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'VANDERMONDE_MATRIX_1D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VANDERMONDE_MATRIX_1D sets the Vandermonde matrix for 1D interpolation.' )

  nd = 4
  xd = np.array ( [ -1.0, 2.0, 3.0, 5.0 ] )

  ad = vandermonde_matrix_1d ( nd, xd )

  r8mat_print ( nd, nd, ad, '  Vandermonde matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VANDERMONDE_MATRIX_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def vandermonde_value_1d ( nd, cd, ni, xi ):

#*****************************************************************************80
#
## VANDERMONDE_VALUE_1D evaluates a Vandermonde interpolant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data values.
#
#    Input, real CD(ND,1), the polynomial coefficients.  
#    CD(I) is the coefficient of X^(I-1).
#
#    Input, integer NI, the number of interpolation points.
#
#    Input, real XI(NI,1), the interpolation points.
#
#    Output, real YI(NI,1), the interpolation values.
#
  import numpy as np

  yi = np.zeros ( ni )

  for j in range ( 0, ni ):
    yi[j] = cd[nd-1]
    for i in range ( nd - 2, -1, -1 ):
      yi[j] = yi[j] * xi[j] + cd[i]

  return yi

def vandermonde_value_1d_test ( ):

#*****************************************************************************80
#
## VANDERMONDE_VALUE_1D_TEST tests VANDERMONDE_VALUE_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'VANDERMONDE_VALUE_1D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VANDERMONDE_VALUE_1D evaluates a Vandermonde interpolant.' )

  nd = 5
  cd = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )
  r8poly_print ( nd - 1, cd, '  The Vandermonde interpolant:' )

  ni = 16
  x_lo = 0.0
  x_hi = 5.0
  xi = np.linspace ( x_lo, x_hi, ni )

  yi = vandermonde_value_1d ( nd, cd, ni, xi )

  r8vec2_print ( ni, xi, yi, '  Vandermonde interpolant values:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VANDERMONDE_VALUE_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  vandermonde_interp_1d_test ( )
  timestamp ( )

