import numpy as np


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
        data_num = int(2**prob / prob)
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
        p_data = np.random.rand(dim_num, data_num)
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


def phi1(r, r0):

    # *****************************************************************************80
    #
    # PHI1 evaluates the multiquadric radial basis function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
    #    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
    #    Third Edition,
    #    Cambridge University Press, 2007,
    #    ISBN13: 978-0-521-88068-8,
    #    LC: QA297.N866.
    #
    #  Parameters:
    #
    #    Input, real R(), the radial separation.
    #    0 < R.
    #
    #    Input, real R0, a scale factor.
    #
    #    Output, real V(), the value of the radial basis function.
    #
    v = np.sqrt(r ** 2 + r0 ** 2)
    return v


def phi2(r, r0):

    # *****************************************************************************80
    #
    # PHI2 evaluates the inverse multiquadric radial basis function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
    #    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
    #    Third Edition,
    #    Cambridge University Press, 2007,
    #    ISBN13: 978-0-521-88068-8,
    #    LC: QA297.N866.
    #
    #  Parameters:
    #
    #    Input, real R(), the radial separation.
    #    0 < R.
    #
    #    Input, real R0, a scale factor.
    #
    #    Output, real V(), the value of the radial basis function.
    #
    v = 1.0 / np.sqrt(r ** 2 + r0 ** 2)
    return v


def phi3(r, r0):

    # *****************************************************************************80
    #
    # PHI3 evaluates the thin-plate spline radial basis function.
    #
    #  Discussion:
    #
    #    Note that PHI3(R,R0) is negative if R < R0.  Thus, for this basis function,
    #    it may be desirable to choose a value of R0 smaller than any possible R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 June 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
    #    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
    #    Third Edition,
    #    Cambridge University Press, 2007,
    #    ISBN13: 978-0-521-88068-8,
    #    LC: QA297.N866.
    #
    #  Parameters:
    #
    #    Input, real R(), the radial separation.
    #    0 < R.
    #
    #    Input, real R0, a scale factor.
    #
    #    Output, real V(), the value of the radial basis function.
    #

    n = np.size(r)
    v = np.zeros(n)
    for i in range(0, n):
        if (r[i] != 0.0):
            v[i] = r[i] ** 2 * np.log(r[i] / r0)

    return v


def phi4(r, r0):

    # *****************************************************************************80
    #
    # PHI4 evaluates the gaussian radial basis function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
    #    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
    #    Third Edition,
    #    Cambridge University Press, 2007,
    #    ISBN13: 978-0-521-88068-8,
    #    LC: QA297.N866.
    #
    #  Parameters:
    #
    #    Input, real R(), the radial separation.
    #    0 < R.
    #
    #    Input, real R0, a scale factor.
    #
    #    Output, real V(), the value of the radial basis function.
    #
    v = np.exp(- 0.5 * r ** 2 / r0 ** 2)
    return v
