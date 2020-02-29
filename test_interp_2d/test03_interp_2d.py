#! /usr/bin/env python3
#


def file_name_sequence(file_name):

    # *****************************************************************************80
    #
    # FILE_NAME_SEQUENCE generates the next file name in a series.
    #
    #  Discussion:
    #
    #    It is assumed that the digits in the name, whether scattered or
    #    connected, represent a number that is to be increased by 1 on
    #    each call.  If this number is all 9's on input, the output number
    #    is all 0's.  Non-numeric letters of the name are unaffected..
    #
    #    If the name is empty, then the routine stops.
    #
    #    If the name contains no digits, the empty string is returned.
    #
    #  Example:
    #
    #      Input            Output
    #      -----            ------
    #      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
    #      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
    #      'a9to99.txt'     'a0to00.txt'  (wrap around)
    #      'cat.txt'        ' '           (no digits in input name.)
    #      ' '              STOP!         (error.)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILE_NAME, the string to be incremented.
    #
    #    Output, string FILE_NAME_NEXT, the incremented string.
    #
    #
    #  Because of Python's particular treatment of strings, (look up the
    #  word "immutable"!) we IMMEDIATELY copy a string into a list, treating
    #  the list like a normal data item, and then at the end, turning it back
    #  into a string.
    #
    file_name_list = list(file_name)

    flen = len(file_name_list)

    if (flen <= 0):
        print('')
        print('FILE_NAME_SEQUENCE - Fatal error!')
        print('  The input file name is empty.')
        exit('FILE_NAME_SEQUENCE - Fatal error!')

    change = 0

    for i in range(flen - 1, -1, -1):

        c = file_name_list[i]

        if ('0' <= c and c <= '8'):

            change = change + 1

            c = chr(ord(c) + 1)

            file_name_list[i] = c

            break

        elif (c == '9'):

            change = change + 1

            c = '0'

            file_name_list[i] = c

    if (change == 0):
        print('')
        print('FILE_NAME_SEQUENCE - Fatal error!')
        print('  The input file name contains no digits to increment.')
        exit('FILE_NAME_SEQUENCE - Fatal error!')

    file_name_next = "".join(file_name_list)

    return file_name_next


def g00_num():

    # *****************************************************************************80
    #
    # G00_NUM returns the number of grids available.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #   Output, integer GRID_NUM, the number of grids.
    #
    grid_num = 5

    return grid_num


def g00_size(gi):

    # *****************************************************************************80
    #
    # G00_SIZE returns the size for any grid.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GI, the index of the grid.
    #
    #    Output, integer GN, the grid size.
    #
    from sys import exit

    if (gi == 1):
        gn = g01_size()
    elif (gi == 2):
        gn = g02_size()
    elif (gi == 3):
        gn = g03_size()
    elif (gi == 4):
        gn = g04_size()
    elif (gi == 5):
        gn = g05_size()
    else:
        print('')
        print('G00_SIZE - Fatal error!')
        print('  Illegal grid index GI = %d' % (gi))
        exit('G00_SIZE - Fatal error!')

    return gn


def g00_title(gi):

    # *****************************************************************************80
    #
    # G00_TITLE returns the title for any grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GI, the index of the grid.
    #
    #    Output, string GT, the grid title.
    #
    from sys import exit

    if (gi == 1):
        gt = g01_title()
    elif (gi == 2):
        gt = g02_title()
    elif (gi == 3):
        gt = g03_title()
    elif (gi == 4):
        gt = g04_title()
    elif (gi == 5):
        gt = g05_title()
    else:
        print('')
        print('G00_TITLE - Fatal error!')
        print('  Illegal grid index GI = %d' % (gi))
        exit('G00_TITLE - Fatal error!')

    return gt


def g00_xy(gi, gn):

    # *****************************************************************************80
    #
    # G00_XY returns the grid points for any grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GI, the index of the grid.
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    from sys import exit

    if (gi == 1):
        gx, gy = g01_xy(gn)
    elif (gi == 2):
        gx, gy = g02_xy(gn)
    elif (gi == 3):
        gx, gy = g03_xy(gn)
    elif (gi == 4):
        gx, gy = g04_xy(gn)
    elif (gi == 5):
        gx, gy = g05_xy(gn)
    else:
        print('')
        print('G00_XY - Fatal error!')
        print('  Illegal grid index GI = %d' % (gi))
        exit('G00_XY - Fatal error!')

    return gx, gy


def g01_size():

    # *****************************************************************************80
    #
    # G01_SIZE returns the size for grid 1.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 100

    return gn


def g01_title():

    # *****************************************************************************80
    #
    # G01_TITLE returns the title for grid 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Franke\'s 100 node set'

    return gt


def g01_xy(gn):

    # *****************************************************************************80
    #
    # G01_XY returns the grid points for grid 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.0227035, 0.0539888, 0.0217008, 0.0175129, 0.0019029,
        -0.0509685, 0.0395408, -0.0487061, 0.0315828, -0.0418785,
        0.1324189, 0.1090271, 0.1254439, 0.0934540, 0.0767578,
        0.1451874, 0.0626494, 0.1452734, 0.0958668, 0.0695559,
        0.2645602, 0.2391645, 0.2088990, 0.2767329, 0.1714726,
        0.2266781, 0.1909212, 0.1867647, 0.2304634, 0.2426219,
        0.3663168, 0.3857662, 0.3832392, 0.3179087, 0.3466321,
        0.3776591, 0.3873159, 0.3812917, 0.3795364, 0.2803515,
        0.4149771, 0.4277679, 0.4200010, 0.4663631, 0.4855658,
        0.4092026, 0.4792578, 0.4812279, 0.3977761, 0.4027321,
        0.5848691, 0.5730076, 0.6063893, 0.5013894, 0.5741311,
        0.6106955, 0.5990105, 0.5380621, 0.6096967, 0.5026188,
        0.6616928, 0.6427836, 0.6396475, 0.6703963, 0.7001181,
        0.6333590, 0.6908947, 0.6895638, 0.6718889, 0.6837675,
        0.7736939, 0.7635332, 0.7410424, 0.8258981, 0.7306034,
        0.8086609, 0.8214531, 0.7290640, 0.8076643, 0.8170951,
        0.8424572, 0.8684053, 0.8366923, 0.9418461, 0.8478122,
        0.8599583, 0.9175700, 0.8596328, 0.9279871, 0.8512805,
        1.0449820, 0.9670631, 0.9857884, 0.9676313, 1.0129299,
        0.9657040, 1.0019855, 1.0359297, 1.0414677, 0.9471506])

    gy = np.array([
        -0.0310206, 0.1586742, 0.2576924, 0.3414014, 0.4943596,
        0.5782854, 0.6993418, 0.7470194, 0.9107649, 0.9962890,
        0.0501330, 0.0918555, 0.2592973, 0.3381592, 0.4171125,
        0.5615563, 0.6552235, 0.7524066, 0.9146523, 0.9632421,
        0.0292939, 0.0602303, 0.2668783, 0.3696044, 0.4801738,
        0.5940595, 0.6878797, 0.8185576, 0.9046507, 0.9805412,
        0.0396955, 0.0684484, 0.2389548, 0.3124129, 0.4902989,
        0.5199303, 0.6445227, 0.8203789, 0.8938079, 0.9711719,
        -0.0284618, 0.1560965, 0.2262471, 0.3175094, 0.3891417,
        0.5084949, 0.6324247, 0.7511007, 0.8489712, 0.9978728,
        -0.0271948, 0.1272430, 0.2709269, 0.3477728, 0.4259422,
        0.6084711, 0.6733781, 0.7235242, 0.9242411, 1.0308762,
        0.0255959, 0.0707835, 0.2008336, 0.3259843, 0.4890704,
        0.5096324, 0.6697880, 0.7759569, 0.9366096, 1.0064516,
        0.0285374, 0.1021403, 0.1936581, 0.3235775, 0.4714228,
        0.6091595, 0.6685053, 0.8022808, 0.8476790, 1.0512371,
        0.0380499, 0.0902048, 0.2083092, 0.3318491, 0.4335632,
        0.5910139, 0.6307383, 0.8144841, 0.9042310, 0.9696030,
        -0.0120900, 0.1334114, 0.2695844, 0.3795281, 0.4396054,
        0.5044425, 0.6941519, 0.7459923, 0.8682081, 0.9801409])

    return gx, gy


def g02_size():

    # *****************************************************************************80
    #
    # G02_SIZE returns the size for grid 2.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 33

    return gn


def g02_title():

    # *****************************************************************************80
    #
    # G02_TITLE returns the title for grid 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Franke\'s 33 node set'

    return gt


def g02_xy(gn):

    # *****************************************************************************80
    #
    # G02_XY returns the grid points for grid 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.05, 0.00, 0.00, 0.00, 0.10,
        0.10, 0.15, 0.20, 0.25, 0.30,
        0.35, 0.50, 0.50, 0.55, 0.60,
        0.60, 0.60, 0.65, 0.70, 0.70,
        0.70, 0.75, 0.75, 0.75, 0.80,
        0.80, 0.85, 0.90, 0.90, 0.95,
        1.00, 1.00, 1.00])

    gy = np.array([
        0.45, 0.50, 1.00, 0.00, 0.15,
        0.75, 0.30, 0.10, 0.20, 0.35,
        0.85, 0.00, 1.00, 0.95, 0.25,
        0.65, 0.85, 0.70, 0.20, 0.65,
        0.90, 0.10, 0.35, 0.85, 0.40,
        0.65, 0.25, 0.35, 0.80, 0.90,
        0.00, 0.50, 1.00])

    return gx, gy


def g03_size():

    # *****************************************************************************80
    #
    # G03_SIZE returns the size for grid 3.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 25

    return gn


def g03_title():

    # *****************************************************************************80
    #
    # G03_TITLE returns the title for grid 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Lawson\'s 25 node set'

    return gt


def g03_xy(gn):

    # *****************************************************************************80
    #
    # G03_XY returns the grid points for grid 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.13750, 0.91250, 0.71250, 0.22500, -0.05000,
        0.47500, 0.05000, 0.45000, 1.08750, 0.53750,
        -0.03750, 0.18750, 0.71250, 0.85000, 0.70000,
        0.27500, 0.45000, 0.81250, 0.45000, 1.00000,
        0.50000, 0.18750, 0.58750, 1.05000, 0.10000])

    gy = np.array([
        0.97500, 0.98750, 0.76250, 0.83750, 0.41250,
        0.63750, -0.05000, 1.03750, 0.55000, 0.80000,
        0.75000, 0.57500, 0.55000, 0.43750, 0.31250,
        0.42500, 0.28750, 0.18750, -0.03750, 0.26250,
        0.46250, 0.26250, 0.12500, -0.06125, 0.11250])

    return gx, gy


def g04_size():

    # *****************************************************************************80
    #
    # G04_SIZE returns the size for grid 4.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 100

    return gn


def g04_title():

    # *****************************************************************************80
    #
    # G04_TITLE returns the title for grid 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Random 100 node set'

    return gt


def g04_xy(gn):

    # *****************************************************************************80
    #
    # G04_XY returns the grid points for grid 4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.0096326, 0.0216348, 0.0298360, 0.0417447, 0.0470462,
        0.0562965, 0.0646857, 0.0740377, 0.0873907, 0.0934832,
        0.1032216, 0.1110176, 0.1181193, 0.1251704, 0.1327330,
        0.1439536, 0.1564861, 0.1651043, 0.1786039, 0.1886405,
        0.2016706, 0.2099886, 0.2147003, 0.2204141, 0.2343715,
        0.2409660, 0.2527740, 0.2570839, 0.2733365, 0.2853833,
        0.2901755, 0.2964854, 0.3019725, 0.3125695, 0.3307163,
        0.3378504, 0.3439061, 0.3529922, 0.3635507, 0.3766172,
        0.3822429, 0.3869838, 0.3973137, 0.4170708, 0.4255588,
        0.4299218, 0.4372839, 0.4705033, 0.4736655, 0.4879299,
        0.4940260, 0.5055324, 0.5162593, 0.5219219, 0.5348529,
        0.5483213, 0.5569571, 0.5638611, 0.5784908, 0.5863950,
        0.5929148, 0.5987839, 0.6117561, 0.6252296, 0.6331381,
        0.6399048, 0.6488972, 0.6558537, 0.6677405, 0.6814074,
        0.6887812, 0.6940896, 0.7061687, 0.7160957, 0.7317445,
        0.7370798, 0.7462030, 0.7566957, 0.7699998, 0.7879347,
        0.7944014, 0.8164468, 0.8192794, 0.8368405, 0.8500993,
        0.8588255, 0.8646496, 0.8792329, 0.8837536, 0.8900077,
        0.8969894, 0.9044917, 0.9083947, 0.9203972, 0.9347906,
        0.9434519, 0.9490328, 0.9569571, 0.9772067, 0.9983493])

    gy = np.array([
        0.3083158, 0.2450434, 0.8613847, 0.0977864, 0.3648355,
        0.7156339, 0.5311312, 0.9755672, 0.1781117, 0.5452797,
        0.1603881, 0.7837139, 0.9982015, 0.6910589, 0.1049580,
        0.8184662, 0.7086405, 0.4456593, 0.1178342, 0.3189021,
        0.9668446, 0.7571834, 0.2016598, 0.3232444, 0.4368583,
        0.8907869, 0.0647260, 0.5692618, 0.2947027, 0.4332426,
        0.3347464, 0.7436284, 0.1066265, 0.8845357, 0.5158730,
        0.9425637, 0.4799701, 0.1783069, 0.1146760, 0.8225797,
        0.2270688, 0.4073598, 0.8875080, 0.7631616, 0.9972804,
        0.4959884, 0.3410421, 0.2498120, 0.6409007, 0.1058690,
        0.5411969, 0.0089792, 0.8784268, 0.5515874, 0.4038952,
        0.1654023, 0.2965158, 0.3660356, 0.0366554, 0.9502420,
        0.2638101, 0.9277386, 0.5377694, 0.7374676, 0.4674627,
        0.9186109, 0.0416884, 0.1291029, 0.6763676, 0.8444238,
        0.3273328, 0.1893879, 0.0645923, 0.0180147, 0.8904992,
        0.4160648, 0.4688995, 0.2174508, 0.5734231, 0.8853319,
        0.8018436, 0.6388941, 0.8931002, 0.1000558, 0.2789506,
        0.9082948, 0.3259159, 0.8318747, 0.0508513, 0.9708450,
        0.5120548, 0.2859716, 0.9581641, 0.6183429, 0.3779934,
        0.4010423, 0.9478657, 0.7425486, 0.8883287, 0.5496750])

    return gx, gy


def g05_size():

    # *****************************************************************************80
    #
    # G05_SIZE returns the size for grid 5.
    #
    #  Discussion:
    #
    #    The "grid size" is simply the number of points in the grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer GN, the grid size.
    #
    gn = 81

    return gn


def g05_title():

    # *****************************************************************************80
    #
    # G05_TITLE returns the title for grid 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string GT, the grid title.
    #
    gt = 'Gridded 81 node set'

    return gt


def g05_xy(gn):

    # *****************************************************************************80
    #
    # G05_XY returns the grid points for grid 5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer GN, the grid size.
    #
    #    Output, real GX(GN), GY(GN), the grid coordinates.
    #
    import numpy as np

    gx = np.array([
        0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000,
        0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
        0.250, 0.250, 0.250, 0.250, 0.250, 0.250, 0.250, 0.250, 0.250,
        0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375,
        0.500, 0.500, 0.500, 0.500, 0.500, 0.500, 0.500, 0.500, 0.500,
        0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625,
        0.750, 0.750, 0.750, 0.750, 0.750, 0.750, 0.750, 0.750, 0.750,
        0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875,
        1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000])

    gy = np.array([
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000,
        0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000])

    return gx, gy


def test_interp_2d_test03():

    # *****************************************************************************80
    #
    # TEST_INTERP_2D_TEST03 plots each grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 July 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt

    print('')
    print('TEST_INTERP_2D_TEST03')
    print('  Plot each grid.')

    g_num = g00_num()
    filename = 'grid_00.png'

    for gi in range(1, g_num + 1):
        filename = file_name_sequence(filename)

        gt = g00_title(gi)
        gn = g00_size(gi)
        gx, gy = g00_xy(gi, gn)

        plt.plot(gx, gy, 'b.', markersize=10)
        plt.title(gt)
        plt.grid(True)
        plt.xlabel('<--- X --->')
        plt.ylabel('<--- Y --->')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.savefig(filename)
        plt.show(block=False)

        print('  Created file "%s".' % (filename))

    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
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

    t = time.time()
    print(time.ctime(t))

    return None


if (__name__ == '__main__'):
    timestamp()

    # *****************************************************************************80
    #
    # TEST_INTERP_2D_TEST tests the TEST_INTERP_2D library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('TEST_INTERP_2D_TEST')
    print('  MATLAB version')
    print('  Test the TEST_INTERP_2D library.')

    test_interp_2d_test03()

    print('')
    print('TEST_INTERP_2D_TEST')
    print('  Normal end of execution.')

    timestamp()
