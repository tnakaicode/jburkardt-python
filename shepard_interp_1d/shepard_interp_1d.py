#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpi4py import MPI
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some
from r8lib.r8vec2_print import r8vec2_print

from r8lib.r8vec_norm_affine import r8vec_norm_affine

obj = plot2d()


def p00_data_num(prob):

    # *****************************************************************************80
    #
    # P00_DATA_NUM returns the number of data points for any problem.
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

    if (prob == 1):
        data_num = p01_data_num()
    elif (prob == 2):
        data_num = p02_data_num()
    elif (prob == 3):
        data_num = p03_data_num()
    elif (prob == 4):
        data_num = p04_data_num()
    elif (prob == 5):
        data_num = p05_data_num()
    elif (prob == 6):
        data_num = p06_data_num()
    elif (prob == 7):
        data_num = p07_data_num()
    elif (prob == 8):
        data_num = p08_data_num()
    else:
        print('')
        print('P00_DATA_NUM - Fatal error!')
        print('  Unexpected input value of PROB.')
        exit('P00_DATA_NUM - Fatal error!')

    return data_num


def p01_data_num():

    # *****************************************************************************80
    #
    # P01_DATA_NUM returns the number of data points for problem p01.
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


def p02_data_num():

    # *****************************************************************************80
    #
    # P02_DATA_NUM returns the number of data points for problem p02.
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


def p03_data_num():

    # *****************************************************************************80
    #
    # P03_DATA_NUM returns the number of data points for problem p03.
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


def p04_data_num():

    # *****************************************************************************80
    #
    # P04_DATA_NUM returns the number of data points for problem p04.
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


def p05_data_num():

    # *****************************************************************************80
    #
    # P05_DATA_NUM returns the number of data points for problem p05.
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


def p06_data_num():

    # *****************************************************************************80
    #
    # P06_DATA_NUM returns the number of data points for problem p06.
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


def p07_data_num():

    # *****************************************************************************80
    #
    # P07_DATA_NUM returns the number of data points for problem p07.
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


def p08_data_num():

    # *****************************************************************************80
    #
    # P08_DATA_NUM returns the number of data points for problem p08.
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


def p00_data_num_test():

    # *****************************************************************************80
    #
    # P00_DATA_NUM_TEST tests P00_DATA_NUM.
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

    print('')
    print('P00_DATA_NUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_DATA_NUM returns the number of data points for any problem.')
    print('')
    print('  Problem   Data Num')
    print('')

    prob_num = p00_prob_num()

    for prob in range(1, prob_num + 1):

        data_num = p00_data_num(prob)

        print('  %7d  %9d' % (prob, data_num))
#
#  Terminate.
#
    print('')
    print('P00_DATA_NUM_TEST:')
    print('  Normal end of execution.')
    return


def p00_data(prob, dim_num, data_num):

    # *****************************************************************************80
    #
    # P00_DATA returns the data for any problem.
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

    if (prob == 1):
        p_data = p01_data(dim_num, data_num)
    elif (prob == 2):
        p_data = p02_data(dim_num, data_num)
    elif (prob == 3):
        p_data = p03_data(dim_num, data_num)
    elif (prob == 4):
        p_data = p04_data(dim_num, data_num)
    elif (prob == 5):
        p_data = p05_data(dim_num, data_num)
    elif (prob == 6):
        p_data = p06_data(dim_num, data_num)
    elif (prob == 7):
        p_data = p07_data(dim_num, data_num)
    elif (prob == 8):
        p_data = p08_data(dim_num, data_num)
    else:
        print('')
        print('P00_DATA - Fatal error!')
        print('  Unexpected input value of PROB.')
        exit('P00_DATA - Fatal error!')

    return p_data


def p01_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P01_DATA returns the data for problem p01.
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

    p_data = np.array([
        [0.0, 4.0],
        [1.0, 5.0],
        [2.0, 6.0],
        [4.0, 6.0],
        [5.0, 5.0],
        [6.0, 3.0],
        [7.0, 1.0],
        [8.0, 1.0],
        [9.0, 1.0],
        [10.0, 3.0],
        [11.0, 4.0],
        [12.0, 4.0],
        [13.0, 3.0],
        [14.0, 3.0],
        [15.0, 4.0],
        [16.0, 4.0],
        [17.0, 3.0],
        [18.0, 0.0]])

    p_data = np.transpose(p_data)

    return p_data


def p02_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P02_DATA returns the data for problem p02.
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

    p_data = np.array([
        [0.00, 0.00],
        [1.34, 5.00],
        [5.00, 8.66],
        [10.00, 10.00],
        [10.60, 10.40],
        [10.70, 12.00],
        [10.705, 28.60],
        [10.80, 30.20],
        [11.40, 30.60],
        [19.60, 30.60],
        [20.20, 30.20],
        [20.295, 28.60],
        [20.30, 12.00],
        [20.40, 10.40],
        [21.00, 10.00],
        [26.00, 8.66],
        [29.66, 5.00],
        [31.00, 0.00]])

    p_data = np.transpose(p_data)

    return p_data


def p03_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P03_DATA returns the data for problem p03.
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

    p_data = np.array([
        [0.0, 0.0],
        [2.0, 10.0],
        [3.0, 10.0],
        [5.0, 10.0],
        [6.0, 10.0],
        [8.0, 10.0],
        [9.0, 10.5],
        [11.0, 15.0],
        [12.0, 50.0],
        [14.0, 60.0],
        [15.0, 85.0]])

    p_data = np.transpose(p_data)

    return p_data


def p04_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P04_DATA returns the data for problem p04.
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

    p_data = np.array([
        [0.00, 0.00],
        [0.05, 0.70],
        [0.10, 1.00],
        [0.20, 1.00],
        [0.80, 0.30],
        [0.85, 0.05],
        [0.90, 0.10],
        [1.00, 1.00]])

    p_data = np.transpose(p_data)

    return p_data


def p05_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P05_DATA returns the data for problem p05.
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

    p_data = np.array([
        [0.00, 0.00],
        [0.10, 0.90],
        [0.20, 0.95],
        [0.30, 0.90],
        [0.40, 0.10],
        [0.50, 0.05],
        [0.60, 0.05],
        [0.80, 0.20],
        [1.00, 1.00]])

    p_data = np.transpose(p_data)

    return p_data


def p06_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P06_DATA returns the data for problem p06.
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

    p_data = np.array([
        [595.0, 0.644],
        [605.0, 0.622],
        [615.0, 0.638],
        [625.0, 0.649],
        [635.0, 0.652],
        [645.0, 0.639],
        [655.0, 0.646],
        [665.0, 0.657],
        [675.0, 0.652],
        [685.0, 0.655],
        [695.0, 0.644],
        [705.0, 0.663],
        [715.0, 0.663],
        [725.0, 0.668],
        [735.0, 0.676],
        [745.0, 0.676],
        [755.0, 0.686],
        [765.0, 0.679],
        [775.0, 0.678],
        [785.0, 0.683],
        [795.0, 0.694],
        [805.0, 0.699],
        [815.0, 0.710],
        [825.0, 0.730],
        [835.0, 0.763],
        [845.0, 0.812],
        [855.0, 0.907],
        [865.0, 1.044],
        [875.0, 1.336],
        [885.0, 1.881],
        [895.0, 2.169],
        [905.0, 2.075],
        [915.0, 1.598],
        [925.0, 1.211],
        [935.0, 0.916],
        [945.0, 0.746],
        [955.0, 0.672],
        [965.0, 0.627],
        [975.0, 0.615],
        [985.0, 0.607],
        [995.0, 0.606],
        [1005.0, 0.609],
        [1015.0, 0.603],
        [1025.0, 0.601],
        [1035.0, 0.603],
        [1045.0, 0.601],
        [1055.0, 0.611],
        [1065.0, 0.601],
        [1075.0, 0.608]])

    p_data = np.transpose(p_data)

    return p_data


def p07_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P07_DATA returns the data for problem p07.
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

    p_data = np.array([
        [0.0, 1.0],
        [1.0, 2.0],
        [4.0, 2.0],
        [5.0, 1.0]])

    p_data = np.transpose(p_data)

    return p_data


def p08_data(dim_num, data_num):

    # *****************************************************************************80
    #
    # P08_DATA returns the data for problem p08.
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

    p_data = np.array([
        [-1.0, 1.00],
        [-0.8, 0.64],
        [-0.6, 0.36],
        [-0.4, 0.16],
        [-0.2, 0.04],
        [0.0, 0.00],
        [0.2, 0.04],
        [0.20001, 0.05],
        [0.4, 0.16],
        [0.6, 0.36],
        [0.8, 0.64],
        [1.0, 1.00]])

    p_data = np.transpose(p_data)

    return p_data


def p00_data_test():

    # *****************************************************************************80
    #
    # P00_DATA_TEST tests P00_DATA.
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

    print('')
    print('P00_DATA_TEST tests P00_DATA')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_DATA returns the actual (MxN) data for any problem.')

    prob_num = p00_prob_num()

    for prob in range(1, prob_num + 1):

        print('')
        print('  Problem %d' % (prob))

        data_num = p00_data_num(prob)
        print('  DATA_NUM = %d' % (data_num))

        dim_num = p00_dim_num(prob)
        print('  DIM_NUM  = %d' % (dim_num))

        p = p00_data(prob, dim_num, data_num)

        r8mat_transpose_print(dim_num, data_num, p, '  Data array:')
#
#  Terminate.
#
    print('')
    print('P00_DATA_TEST:')
    print('  Normal end of execution.')
    return


def p00_dim_num(prob):

    # *****************************************************************************80
    #
    # P00_DIM_NUM returns the spatial dimension for any problem.
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
    if (prob == 1):
        dim_num = p01_dim_num()
    elif (prob == 2):
        dim_num = p02_dim_num()
    elif (prob == 3):
        dim_num = p03_dim_num()
    elif (prob == 4):
        dim_num = p04_dim_num()
    elif (prob == 5):
        dim_num = p05_dim_num()
    elif (prob == 6):
        dim_num = p06_dim_num()
    elif (prob == 7):
        dim_num = p07_dim_num()
    elif (prob == 8):
        dim_num = p08_dim_num()
    else:
        print('')
        print('P00_DIM_NUM - Fatal error!')
        print('  Unexpected input value of PROB.')
        exit('P00_DIM_NUM - Fatal error!')

    return dim_num


def p01_dim_num():

    # *****************************************************************************80
    #
    # P01_DIM_NUM returns the spatial dimension for problem p01.
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


def p02_dim_num():

    # *****************************************************************************80
    #
    # P02_DIM_NUM returns the spatial dimension for problem p02.
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


def p03_dim_num():

    # *****************************************************************************80
    #
    # P03_DIM_NUM returns the spatial dimension for problem p03.
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


def p04_dim_num():

    # *****************************************************************************80
    #
    # P04_DIM_NUM returns the spatial dimension for problem p04.
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


def p05_dim_num():

    # *****************************************************************************80
    #
    # P05_DIM_NUM returns the spatial dimension for problem p05.
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


def p06_dim_num():

    # *****************************************************************************80
    #
    # P06_DIM_NUM returns the spatial dimension for problem p06.
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


def p07_dim_num():

    # *****************************************************************************80
    #
    # P07_DIM_NUM returns the spatial dimension for problem p07.
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


def p08_dim_num():

    # *****************************************************************************80
    #
    # P08_DIM_NUM returns the spatial dimension for problem p08.
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


def p00_dim_num_test():

    # *****************************************************************************80
    #
    # P00_DIM_NUM_TEST tests P00_DIM_NUM.
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

    print('')
    print('P00_DIM_NUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_DIM_NUM returns the spatial dimension for any problem.')
    print('')
    print('  Problem  Dimension')
    print('')

    prob_num = p00_prob_num()

    for prob in range(1, prob_num + 1):

        dim_num = p00_dim_num(prob)

        print('  %7d  %9d' % (prob, dim_num))
#
#  Terminate.
#
    print('')
    print('P00_DIM_NUM_TEST:')
    print('  Normal end of execution.')
    return


def p00_prob_num():

    # *****************************************************************************80
    #
    # P00_PROB_NUM returns the number of problems.
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


def p00_prob_num_test():

    # *****************************************************************************80
    #
    # P00_PROB_NUM_TEST tests P00_PROB_NUM.
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

    print('')
    print('P00_PROB_NUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_PROB_NUM returns the number of test problems.')

    num = p00_prob_num()
    print('')
    print('  TEST_INTERP includes %d test problems.' % (num))
#
#  Terminate.
#
    print('')
    print('P00_PROB_NUM_TEST:')
    print('  Normal end of execution.')
    return


def shepard_basis_1d(nd, xd, p, ni, xi):

    # *****************************************************************************80
    #
    # SHEPARD_BASIS_1D evaluates a 1D Shepard basis function.
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
    #  Reference:
    #
    #    Donald Shepard,
    #    A two-dimensional interpolation function for irregularly spaced data,
    #    ACM '68: Proceedings of the 1968 23rd ACM National Conference,
    #    ACM, pages 517-524, 1969.
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #
    #    Input, real XD(ND,1), the data points.
    #
    #    Input, integer K, the index of the desired basis function,
    #    1 <= K <= ND.
    #
    #    Input, real P, the power.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI,1), the interpolation points.
    #
    #    Output, real BK(NI,ND), the basis function at the interpolation points.
    #
    import numpy as np

    bk = np.zeros([ni, nd])

    w = np.zeros(nd)

    for i in range(0, ni):

        if (p == 0.0):

            for j in range(0, nd):
                w[j] = 1.0 / float(nd)

        else:

            z = -1
            for j in range(0, nd):
                w[j] = abs(xi[i] - xd[j])
                if (w[j] == 0.0):
                    z = j

            if (z != -1):
                for j in range(0, nd):
                    w[j] = 0.0
                w[z] = 1.0
            else:
                for j in range(0, nd):
                    w[j] = 1.0 / w[j] ** p
                s = np.sum(w)
                for j in range(0, nd):
                    w[j] = w[j] / s

        for j in range(0, nd):
            bk[i, j] = w[j]

    return bk


def shepard_basis_1d_test():

    # *****************************************************************************80
    #
    # SHEPARD_BASIS_1D_TEST tests SHEPARD_BASIS_1D.
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
    import numpy as np
    import platform

    nd = 4
    ni = 21

    p = 2.0

    xd = np.array([0.0, 2.0, 5.0, 10.0])

    print('')
    print('SHEPARD_BASIS_1D_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SHEPARD_BASIS_1D evaluates the Shepard 1D basis')
    print('  functions.')
    print('')
    print('  Using power P = %g' % (p))

    x_min = 0.0
    x_max = 10.0
    xi = np.linspace(x_min, x_max, ni)

    lb = shepard_basis_1d(nd, xd, p, ni, xi)

    r8mat_print(ni, nd, lb, '  The Shepard basis functions:')
#
#  Terminate.
#
    print('')
    print('SHEPARD_BASIS_1D_TEST:')
    print('  Normal end of execution.')
    return


def shepard_interp_1d_test():

    # *****************************************************************************80
    #
    # SHEPARD_INTERP_1D_TEST tests the SHEPARD_INTERP_1D library.
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

    print('')
    print('SHEPARD_INTERP_1D_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SHEPARD_INTERP_1D library.')

    p00_data_test()
    p00_data_num_test()
    p00_dim_num_test()
    p00_prob_num_test()

    shepard_basis_1d_test()
    shepard_value_1d_test()

    prob_num = p00_prob_num()
    for prob in range(1, prob_num + 1):
        for p in ([0.0, 1.0, 2.0, 4.0, 8.0]):
            shepard_interp_1d_test01(prob, p)

    print('')
    print('SHEPARD_INTERP_1D_TEST:')
    print('  Normal end of execution.')


def shepard_interp_1d_test01(prob, p):

    # *****************************************************************************80
    #
    # SHEPARD_INTERP_1D_TEST01 tests SHEPARD_VALUE_1D.
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
    #  Parameters:
    #
    #    Input, integer PROB, the problem index.
    #
    #    Input, real P, the exponent.
    #

    print('')
    print('SHEPARD_INTERP_1D_TEST01:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Interpolate data from TEST_INTERP problem #%d.' % (prob))
    print('  Use Shepard interpolation with P = %g' % (p))

    dim_num = p00_dim_num(prob)
    nd = p00_data_num(prob)
    print('  Number of data points = %d' % (nd))

    xy = p00_data(prob, dim_num, nd)
    xd = np.zeros(nd)
    yd = np.zeros(nd)
    for i in range(0, nd):
        xd[i] = xy[0, i]
        yd[i] = xy[1, i]

    #
    #  1:  Does interpolant match function at interpolation points?
    #
    ni = nd
    xi = xd
    yi = shepard_value_1d(nd, xd, yd, p, ni, xi)

    int_error = r8vec_norm_affine(ni, yi, yd) / float(ni)

    print('')
    print('  L2 interpolation error averaged per interpolant node = %g' %
          (int_error))

    #
    #  2: Compare estimated curve length to piecewise linear (minimal) curve length.
    #  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
    #  (YMAX-YMIN).
    #
    xmin = np.min(xd)
    xmax = np.max(xd)
    ymin = np.min(yd)
    ymax = np.max(yd)

    ni = 501
    xi = np.linspace(xmin, xmax, ni)
    yi = shepard_value_1d(nd, xd, yd, p, ni, xi)

    ld = 0.0
    for i in range(0, nd - 1):
        ld = ld + np.sqrt(
            ((xd[i + 1] - xd[i]) / (xmax - xmin)) ** 2
            + ((yd[i + 1] - yd[i]) / (ymax - ymin)) ** 2
        )

    li = 0.0
    for i in range(0, ni - 1):
        li = li + np.sqrt(
            ((xi[i + 1] - xi[i]) / (xmax - xmin)) ** 2
            + ((yi[i + 1] - yi[i]) / (ymax - ymin)) ** 2
        )
    li = np.sqrt(li)

    print('')
    print('  Normalized length of piecewise linear interpolant = %g' % (ld))
    print('  Normalized length of Shepard interpolant          = %g' % (li))

    #
    #  3: Plot the data.
    #

    name = "p{:03d}".format(prob)
    obj.new_2Dfig(aspect="auto")
    t = name + ' Piecewise Linear Interpolant'
    filename = name + '_data.png'
    obj.axs.plot(xd, yd, 'b-', linewidth=3.0)
    obj.axs.plot(xd, yd, 'k.', markersize=10)
    obj.axs.set_title(t)
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.SavePng(obj.tmpdir + filename)
    plt.clf()

    print('')
    print('  Created plot file "%s"' % (filename))

    #
    #  4: Plot the piecewise linear and Shepard interpolants.
    #
    ni = 501
    xmin = min(xd)
    xmax = max(xd)
    xi = np.linspace(xmin, xmax, ni)
    yi = shepard_value_1d(nd, xd, yd, p, ni, xi)

    obj.new_2Dfig(aspect="auto")
    t = name + ' Shepard Interpolant'
    filename = name + '_{:03d}_shepard.png'.format(int(p))
    obj.axs.plot(xd, yd, 'b-', linewidth=3.0)
    obj.axs.plot(xi, yi, 'r-', linewidth=4.0)
    obj.axs.plot(xd, yd, 'k.', markersize=10)
    obj.axs.set_title(t)
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.SavePng(obj.tmpdir + filename)
    plt.clf()

    print('  Created plot file "%s".' % (filename))
    print('')
    print('SHEPARD_INTERP_1D_TEST01:')
    print('  Normal end of execution.')


def shepard_value_1d(nd, xd, yd, p, ni, xi):

    # *****************************************************************************80
    #
    # SHEPARD_VALUE_1D evaluates a 1D Shepard interpolant.
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
    #  Reference:
    #
    #    Donald Shepard,
    #    A two-dimensional interpolation function for irregularly spaced data,
    #    ACM '68: Proceedings of the 1968 23rd ACM National Conference,
    #    ACM, pages 517-524, 1969.
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #
    #    Input, real XD(ND), the data points.
    #
    #    Input, real YD(ND), the data values.
    #
    #    Input, real P, the power.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI), the interpolation points.
    #
    #    Output, real YI(NI), the interpolated values.
    #

    yi = np.zeros(ni)
    w = np.zeros(nd)

    for i in range(0, ni):

        if (p == 0.0):

            for j in range(0, nd):
                w[j] = 1.0 / float(nd)

        else:

            z = -1
            for j in range(0, nd):
                w[j] = abs(xi[i] - xd[j])
                if (w[j] == 0.0):
                    z = j

            if (z != -1):
                for j in range(0, nd):
                    w[j] = 0.0
                w[z] = 1.0
            else:
                for j in range(0, nd):
                    w[j] = 1.0 / w[j] ** p
                s = np.sum(w)
                for j in range(0, nd):
                    w[j] = w[j] / s

        for j in range(0, nd):
            yi[i] = yi[i] + w[j] * yd[j]

    return yi


def shepard_value_1d_test():

    # *****************************************************************************80
    #
    # SHEPARD_VALUE_1D_TEST tests SHEPARD_VALUE_1D.
    #
    #  Discussion:
    #
    #    f(x) = x^3 - 12 x^2 + 39 x - 28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
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

    nd = 4
    ni = 21

    xd = np.array([0.0, 2.0, 5.0, 10.0])
    yd = np.array([-28.0, +10.0, -8.0, +162.0])

    print('')
    print('SHEPARD_VALUE_1D_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SHEPARD_VALUE_1D evaluates a Shepard 1D interpolant.')

    p = 2.0
    print('')
    print('  Using power P = %g' % (p))

    x_min = 0.0
    x_max = 10.0
    xi = np.linspace(x_min, x_max, ni)
    yi = shepard_value_1d(nd, xd, yd, p, ni, xi)
    r8vec2_print(ni, xi, yi, '  Table of interpolant values:')

    print('')
    print('SHEPARD_VALUE_1D_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    shepard_interp_1d_test()
    timestamp()
