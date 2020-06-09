#! /usr/bin/env python3
#
import time


def cg_csc(n, a, b, x):

    # *****************************************************************************80
    #
    # CG_CSC uses the conjugate gradient method for a CSC matrix.
    #
    #  Discussion:
    #
    #    The linear system has the form A*x=b, where A is a positive-definite
    #    symmetric matrix, stored in Python's Compressed Sparse Column (CSC) format.
    #
    #    The method is designed to reach the solution to the linear system
    #      A * x = b
    #    after N computational steps.  However, roundoff may introduce
    #    unacceptably large errors for some problems.  In such a case,
    #    calling the routine a second time, using the current solution estimate
    #    as the new starting guess, should result in improved results.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Frank Beckman,
    #    The Solution of Linear Equations by the Conjugate Gradient Method,
    #    in Mathematical Methods for Digital Computers,
    #    edited by John Ralston, Herbert Wilf,
    #    Wiley, 1967,
    #    ISBN: 0471706892,
    #    LC: QA76.5.R3.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the matrix, in Python's CSC format.
    #
    #    Input, real B(N), the right hand side vector.
    #
    #    Input/output, real X(N).
    #    On input, an estimate for the solution, which may be 0.
    #    On output, the approximate solution vector.
    #
    import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
    ap = a.dot(x)

    r = b - ap
    p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
    for it in range(0, n):
        #
        #  Compute the matrix*vector product AP = A*P.
        #
        ap = a.dot(p)
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
        pap = np.dot(p, ap)
        pr = np.dot(p, r)

        if (pap == 0.0):
            return x

        alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
        x = x + alpha * p
        r = r - alpha * ap
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
        rap = np.dot(r, ap)

        beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
        p = r + beta * p

    return x


def cg_ge(n, a, b, x):

    # *****************************************************************************80
    #
    # CG_GE uses the conjugate gradient method for a general storage matrix.
    #
    #  Discussion:
    #
    #    The linear system has the form A*x=b, where A is a positive-definite
    #    symmetric matrix, stored as a full storage matrix.
    #
    #    The method is designed to reach the solution to the linear system
    #      A * x = b
    #    after N computational steps.  However, roundoff may introduce
    #    unacceptably large errors for some problems.  In such a case,
    #    calling the routine a second time, using the current solution estimate
    #    as the new starting guess, should result in improved results.
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
    #  Reference:
    #
    #    Frank Beckman,
    #    The Solution of Linear Equations by the Conjugate Gradient Method,
    #    in Mathematical Methods for Digital Computers,
    #    edited by John Ralston, Herbert Wilf,
    #    Wiley, 1967,
    #    ISBN: 0471706892,
    #    LC: QA76.5.R3.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the matrix.
    #
    #    Input, real B(N), the right hand side vector.
    #
    #    Input/output, real X(N).
    #    On input, an estimate for the solution, which may be 0.
    #    On output, the approximate solution vector.
    #
    import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
    ap = np.dot(a, x)

    r = b - ap
    p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
    for it in range(0, n):
        #
        #  Compute the matrix*vector product AP = A*P.
        #
        ap = np.dot(a, p)
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
        pap = np.dot(p, ap)
        pr = np.dot(p, r)

        if (pap == 0.0):
            return x

        alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
        x = x + alpha * p
        r = r - alpha * ap
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
        rap = np.dot(r, ap)

        beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
        p = r + beta * p

    return x


def cg_st(n, nz_num, row, col, a, b, x):

    # *****************************************************************************80
    #
    # CG_ST uses the conjugate gradient method for a sparse triplet storage matrix.
    #
    #  Discussion:
    #
    #    The linear system has the form A*x=b, where A is a positive-definite
    #    symmetric matrix, stored as a full storage matrix.
    #
    #    The method is designed to reach the solution to the linear system
    #      A * x = b
    #    after N computational steps.  However, roundoff may introduce
    #    unacceptably large errors for some problems.  In such a case,
    #    calling the routine a second time, using the current solution estimate
    #    as the new starting guess, should result in improved results.
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
    #  Reference:
    #
    #    Frank Beckman,
    #    The Solution of Linear Equations by the Conjugate Gradient Method,
    #    in Mathematical Methods for Digital Computers,
    #    edited by John Ralston, Herbert Wilf,
    #    Wiley, 1967,
    #    ISBN: 0471706892,
    #    LC: QA76.5.R3.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, integer NZ_NUM, the number of nonzeros.
    #
    #    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
    #    of the nonzero entries.
    #
    #    Input, real A(NZ_NUM), the nonzero entries.
    #
    #    Input, real B(N), the right hand side vector.
    #
    #    Input/output, real X(N).
    #    On input, an estimate for the solution, which may be 0.
    #    On output, the approximate solution vector.
    #
    import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
    ap = mv_st(n, n, nz_num, row, col, a, x)

    r = b - ap
    p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
    for it in range(0, n):
        #
        #  Compute the matrix*vector product AP = A*P.
        #
        ap = mv_st(n, n, nz_num, row, col, a, p)
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
        pap = np.dot(p, ap)
        pr = np.dot(p, r)

        if (pap == 0.0):
            return x

        alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
        x = x + alpha * p
        r = r - alpha * ap
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
        rap = np.dot(r, ap)

        beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
        p = r + beta * p

    return x


def mv_st(m, n, nz_num, row, col, a, x):

    # *****************************************************************************80
    #
    # MV_ST multiplies a sparse triple matrix times a vector.
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
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, integer NZ_NUM, the number of nonzero values.
    #
    #    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices.
    #
    #    Input, real A(NZ_NUM), the nonzero values in the M by N matrix.
    #
    #    Input, real X(N), the vector to be multiplied.
    #
    #    Output, real B(M), the product A*X.
    #
    import numpy as np

    b = np.zeros(m)

    for k in range(0, nz_num):
        b[row[k]] = b[row[k]] + a[k] * x[col[k]]

    return b


def nonzeros(m, n, a):

    # *****************************************************************************80
    #
    # NONZEROS counts the nonzeros in a matrix.
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
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Output, integer NNZ, the number of nonzero entries.
    #
    nnz = 0
    for j in range(0, n):
        for i in range(0, m):
            if (a[i, j] != 0.0):
                nnz = nnz + 1

    return nnz


def r8mat_uniform_01(m, n, seed):

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 April 2013
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
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.
    #
    #    Output, real R(M,N), an array of random values between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8MAT_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8MAT_UNIFORM_01 - Fatal error!')

    r = np.zeros([m, n])

    for j in range(0, n):
        for i in range(0, m):

            k = (seed // 127773)

            seed = 16807 * (seed - k * 127773) - k * 2836

            seed = (seed % i4_huge)

            if (seed < 0):
                seed = seed + i4_huge

            r[i, j] = seed * 4.656612875E-10

    return r, seed


def r8mat_uniform_01_test():

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_01_TEST tests R8MAT_UNIFORM_01.
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

    m = 5
    n = 4
    seed = 123456789

    print('')
    print('R8MAT_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_UNIFORM_01 computes a random R8MAT.')
    print('')
    print('  0 <= X <= 1')
    print('  Initial seed is %d' % (seed))

    v, seed = r8mat_uniform_01(m, n, seed)

#
#  Terminate.
#
    print('')
    print('R8MAT_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def r8_uniform_01(seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_01 returns a unit pseudorandom R8.
    #
    #  Discussion:
    #
    #    This routine implements the recursion
    #
    #      seed = 16807 * seed mod ( 2^31 - 1 )
    #      r8_uniform_01 = seed / ( 2^31 - 1 )
    #
    #    The integer arithmetic never requires more than 32 bits,
    #    including a sign bit.
    #
    #    If the initial seed is 12345, then the first three computations are
    #
    #      Input     Output      R8_UNIFORM_01
    #      SEED      SEED
    #
    #         12345   207482415  0.096616
    #     207482415  1790989824  0.833995
    #    1790989824  2035175616  0.947702
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 March 2013
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
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R, a random value between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_01 - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10

    return r, seed


def r8_uniform_01_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_01 produces a sequence of random values.')

    seed = 123456789

    print('')
    print('  Using random seed %d' % (seed))

    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')
    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))

    print('')
    print('  Verify that the sequence can be restarted.')
    print('  Set the seed back to its original value, and see that')
    print('  we generate the same sequence.')

    seed = 123456789
    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')

    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))
#
#  Terminate.
#
    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
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
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
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

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = np.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


def r8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
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

    print('')
    print('R8VEC_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_01 computes a random R8VEC.')
    print('')
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_01(n, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def st_to_ge(n_st, row, col, a_st):

    # *****************************************************************************80
    #
    # ST_TO_GE converts a sparse tripet (ST) matrix to general (GE) storage.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 June 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N_ST, the number of sparse triplet values.
    #
    #    Input, integer ROW(N_ST), COL(N_ST), the row and column indices.
    #
    #    Input, real A_ST(N_ST), the nonzero matrix values.
    #
    #    Output, real A_GE(M,N), the corresponding full storage matrix.
    #
    import numpy as np
#
#  Guess the number of rows and columns.
#
    m = max(row) + 1
    n = max(col) + 1
#
#  Set up the GE matrix.
#
    a_ge = np.zeros((m, n))
#
#  Copy the data as a vector.
#
    for k in range(0, n_st):
        a_ge[row[k], col[k]] = a_st[k]

    return a_ge


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


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
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

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


def wathen_bandwidth(nx, ny):

    # *****************************************************************************80
    #
    # WATHEN_BANDWIDTH returns the bandwidth of the WATHEN matrix.
    #
    #  Discussion:
    #
    #    The bandwidth measures the minimal number of contiguous diagonals,
    #    including the central diagonal, which contain all the nonzero elements
    #    of a matrix.
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
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, 1987, pages 449-457.
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, values which determine the size of A.
    #
    #    Output, integer L, D, U, the lower, diagonal, and upper bandwidths
    #    of the matrix,
    #
    l = 3 * nx + 4
    d = 1
    u = 3 * nx + 4

    return l, d, u


def wathen_csc(nx, ny, seed):

    # *****************************************************************************80
    #
    # WATHEN_CSC: Wathen matrix stored in Compressed Sparse Column (CSC) format.
    #
    #  Discussion:
    #
    #    When dealing with sparse matrices in MATLAB, it can be much more efficient
    #    to work first with a triple of I, J, and X vectors, and only once
    #    they are complete, convert to MATLAB's sparse format.
    #
    #    The Wathen matrix is a finite element matrix which is sparse.
    #
    #    The entries of the matrix depend in part on a physical quantity
    #    related to density.  That density is here assigned random values between
    #    0 and 100.
    #
    #    The matrix order N is determined by the input quantities NX and NY,
    #    which would usually be the number of elements in the X and Y directions.
    #
    #    The value of N is
    #
    #      N = 3*NX*NY + 2*NX + 2*NY + 1,
    #
    #    The matrix is the consistent mass matrix for a regular NX by NY grid
    #    of 8 node serendipity elements.
    #
    #    The local element numbering is
    #
    #      3--2--1
    #      |     |
    #      4     8
    #      |     |
    #      5--6--7
    #
    #    Here is an illustration for NX = 3, NY = 2:
    #
    #     23-24-25-26-27-28-29
    #      |     |     |     |
    #     19    20    21    22
    #      |     |     |     |
    #     12-13-14-15-16-17-18
    #      |     |     |     |
    #      8     9    10    11
    #      |     |     |     |
    #      1--2--3--4--5--6--7
    #
    #    For this example, the total number of nodes is, as expected,
    #
    #      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
    #
    #    The matrix is symmetric positive definite for any positive values of the
    #    density RHO(X,Y).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2014
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, Number 4, October 1987, pages 449-457.
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, values which determine the size of the matrix.
    #
    #    Input, integer SEED, the random number seed.
    #
    #    Output, real A(*,*), the compressed sparxe column version of the matrix.
    #
    #    Output, integer SEED, the random number seed.
    #
    import numpy as np
    from scipy.sparse import coo_matrix

    em = np.array(
        ((6.0, -6.0, 2.0, -8.0, 3.0, -8.0, 2.0, -6.0),
         (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0),
            (2.0, -6.0, 6.0, -6.0, 2.0, -8.0, 3.0, -8.0),
            (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0),
            (3.0, -8.0, 2.0, -6.0, 6.0, -6.0, 2.0, -8.0),
            (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0),
            (2.0, -8.0, 3.0, -8.0, 2.0, -6.0, 6.0, -6.0),
            (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0))
    )

    node = np.zeros(8, dtype=np.int32)

    st_num = 8 * 8 * nx * ny
    row = np.zeros(st_num, dtype=np.int32)
    col = np.zeros(st_num, dtype=np.int32)
    v = np.zeros(st_num)

    k = 0

    for j in range(0, ny):

        for i in range(0, nx):

            node[0] = (3 * (j + 1)) * nx + 2 * (j + 1) + 2 * (i + 1) + 1 - 1
            node[1] = node[0] - 1
            node[2] = node[0] - 2

            node[3] = (3 * (j + 1) - 1) * nx + 2 * (j + 1) + (i + 1) - 1 - 1
            node[7] = node[3] + 1

            node[4] = (3 * (j + 1) - 3) * nx + 2 * \
                (j + 1) + 2 * (i + 1) - 3 - 1
            node[5] = node[4] + 1
            node[6] = node[4] + 2

            rho, seed = r8_uniform_01(seed)
            rho = 100.0 * rho

            for krow in range(0, 8):
                for kcol in range(0, 8):
                    row[k] = node[krow]
                    col[k] = node[kcol]
                    v[k] = rho * em[krow, kcol]
                    k = k + 1
#
#  Convert triplet to a Python COO matrix.
#
    a = coo_matrix((v, (row, col)))
#
#  Convert COO matrix to CSC format.
#
    a = a.tocsc()

    return a, seed


def wathen_ge(nx, ny, n, seed):

    # *****************************************************************************80
    #
    # WATHEN_GE returns the Wathen matrix, using general (GE) storage.
    #
    #  Discussion:
    #
    #    The Wathen matrix is a finite element matrix which is sparse.
    #
    #    The entries of the matrix depend in part on a physical quantity
    #    related to density.  That density is here assigned random values between
    #    0 and 100.
    #
    #    The matrix order N is determined by the input quantities NX and NY,
    #    which would usually be the number of elements in the X and Y directions.
    #    The value of N is
    #
    #      N = 3*NX*NY + 2*NX + 2*NY + 1,
    #
    #    The matrix is the consistent mass matrix for a regular NX by NY grid
    #    of 8 node serendipity elements.
    #
    #    The local element numbering is
    #
    #      3--2--1
    #      |     |
    #      4     8
    #      |     |
    #      5--6--7
    #
    #    Here is an illustration for NX = 3, NY = 2:
    #
    #     23-24-25-26-27-28-29
    #      |     |     |     |
    #     19    20    21    22
    #      |     |     |     |
    #     12-13-14-15-16-17-18
    #      |     |     |     |
    #      8     9    10    11
    #      |     |     |     |
    #      1--2--3--4--5--6--7
    #
    #    For this example, the total number of nodes is, as expected,
    #
    #      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
    #
    #    The matrix is symmetric positive definite for any positive values of the
    #    density RHO(X,Y).
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
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, Number 4, October 1987, pages 449-457.
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, values which determine the size of the matrix.
    #
    #    Input, integer N, the number of variables.
    #
    #    Input/output, integer SEED, the random number seed.
    #
    #    Output, real A(N,N), the matrix.
    #
    import numpy as np

    a = np.zeros((n, n))

    em = np.array(
        ((6.0, -6.0, 2.0, -8.0, 3.0, -8.0, 2.0, -6.0),
         (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0),
            (2.0, -6.0, 6.0, -6.0, 2.0, -8.0, 3.0, -8.0),
            (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0),
            (3.0, -8.0, 2.0, -6.0, 6.0, -6.0, 2.0, -8.0),
            (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0),
            (2.0, -8.0, 3.0, -8.0, 2.0, -6.0, 6.0, -6.0),
            (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0))
    )

    node = np.zeros(8, dtype=np.int32)

    for j in range(0, ny):

        for i in range(0, nx):
            #
            #  For the element (I,J), determine the indices of the 8 nodes.
            #
            node[0] = (3 * (j + 1)) * nx + 2 * (j + 1) + 2 * (i + 1) + 1 - 1
            node[1] = node[0] - 1
            node[2] = node[0] - 2

            node[3] = (3 * (j + 1) - 1) * nx + 2 * (j + 1) + (i + 1) - 1 - 1
            node[7] = node[3] + 1

            node[4] = (3 * (j + 1) - 3) * nx + 2 * \
                (j + 1) + 2 * (i + 1) - 3 - 1
            node[5] = node[4] + 1
            node[6] = node[4] + 2

            rho, seed = r8_uniform_01(seed)
            rho = 100.0 * rho

            for krow in range(0, 8):
                for kcol in range(0, 8):
                    a[node[krow], node[kcol]] = a[node[krow], node[kcol]] \
                        + rho * em[krow, kcol]

    return a, seed


def wathen_order(nx, ny):

    # *****************************************************************************80
    #
    # WATHEN_ORDER returns the order of the WATHEN matrix.
    #
    #  Discussion:
    #
    #    N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
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
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, 1987, pages 449-457.
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, values which determine the size of A.
    #
    #    Output, integer N, the order of the matrix,
    #    as determined by NX and NY.
    #
    n = 3 * nx * ny + 2 * nx + 2 * ny + 1

    return n


def wathen_order_test():

    # *****************************************************************************80
    #
    # WATHEN_ORDER_TEST tests WATHEN_ORDER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, 1987, pages 449-457.
    #
    import platform

    print('')
    print('WATHEN_ORDER_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  WATHEN_ORDER returns N, the order of a Wathen finite element')
    print('  matrix given NX and NY, the number of rows and columns of')
    print('  nodes in the underlying grid.')
    print('')
    print('       NX / NY: 1       2       3       4       5       6')
    print('')

    for ny in range(1, 11):
        print('       %2d' % (ny), end='')
        for nx in range(1, 7):
            n = wathen_order(nx, ny)
            print('  %5d' % (n), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('WATHEN_ORDER_TEST:')
    print('  Normal end of execution.')
    return


def wathen_st(nx, ny, nz_num, seed):

    # *****************************************************************************80
    #
    # WATHEN_ST: Wathen matrix stored in sparse triplet format.
    #
    #  Discussion:
    #
    #    When dealing with sparse matrices in MATLAB, it can be much more efficient
    #    to work first with a triple of I, J, and X vectors, and only once
    #    they are complete, convert to MATLAB's sparse format.
    #
    #    The Wathen matrix is a finite element matrix which is sparse.
    #
    #    The entries of the matrix depend in part on a physical quantity
    #    related to density.  That density is here assigned random values between
    #    0 and 100.
    #
    #    The matrix order N is determined by the input quantities NX and NY,
    #    which would usually be the number of elements in the X and Y directions.
    #
    #    The value of N is
    #
    #      N = 3*NX*NY + 2*NX + 2*NY + 1,
    #
    #    The matrix is the consistent mass matrix for a regular NX by NY grid
    #    of 8 node serendipity elements.
    #
    #    The local element numbering is
    #
    #      3--2--1
    #      |     |
    #      4     8
    #      |     |
    #      5--6--7
    #
    #    Here is an illustration for NX = 3, NY = 2:
    #
    #     23-24-25-26-27-28-29
    #      |     |     |     |
    #     19    20    21    22
    #      |     |     |     |
    #     12-13-14-15-16-17-18
    #      |     |     |     |
    #      8     9    10    11
    #      |     |     |     |
    #      1--2--3--4--5--6--7
    #
    #    For this example, the total number of nodes is, as expected,
    #
    #      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
    #
    #    The matrix is symmetric positive definite for any positive values of the
    #    density RHO(X,Y).
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
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, Number 4, October 1987, pages 449-457.
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, values which determine the size of the matrix.
    #
    #    Input, integer NZ_NUM, the number of values used to describe the matrix.
    #
    #    Input/output, integer SEED, the random number seed.
    #
    #    Output, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
    #    of the nonzero entries.
    #
    #    Output, real A(NZ_NUM), the nonzero values.
    #
    import numpy as np

    em = np.array(
        ((6.0, -6.0, 2.0, -8.0, 3.0, -8.0, 2.0, -6.0),
         (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0),
            (2.0, -6.0, 6.0, -6.0, 2.0, -8.0, 3.0, -8.0),
            (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0),
            (3.0, -8.0, 2.0, -6.0, 6.0, -6.0, 2.0, -8.0),
            (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0),
            (2.0, -8.0, 3.0, -8.0, 2.0, -6.0, 6.0, -6.0),
            (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0))
    )

    node = np.zeros(8, dtype=np.int32)
    row = np.zeros(nz_num, dtype=np.int32)
    col = np.zeros(nz_num, dtype=np.int32)
    a = np.zeros(nz_num)

    k = 0

    for j in range(0, ny):

        for i in range(0, nx):

            node[0] = (3 * (j + 1)) * nx + 2 * (j + 1) + 2 * (i + 1) + 1 - 1
            node[1] = node[0] - 1
            node[2] = node[0] - 2

            node[3] = (3 * (j + 1) - 1) * nx + 2 * (j + 1) + (i + 1) - 1 - 1
            node[7] = node[3] + 1

            node[4] = (3 * (j + 1) - 3) * nx + 2 * \
                (j + 1) + 2 * (i + 1) - 3 - 1
            node[5] = node[4] + 1
            node[6] = node[4] + 2

            rho, seed = r8_uniform_01(seed)
            rho = 100.0 * rho

            for krow in range(0, 8):
                for kcol in range(0, 8):
                    row[k] = node[krow]
                    col[k] = node[kcol]
                    a[k] = rho * em[krow, kcol]
                    k = k + 1

    return row, col, a, seed


def wathen_st_size(nx, ny):

    # *****************************************************************************80
    #
    # WATHEN_ST_SIZE: Size of Wathen matrix stored in sparse triplet format.
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
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, Number 4, October 1987, pages 449-457.
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, values which determine the size of the matrix.
    #
    #    Output, integer NZ_NUM, the number of items of data used to describe
    #    the matrix.
    #
    nz_num = nx * ny * 64

    return nz_num


def wathen_st_size_test():

    # *****************************************************************************80
    #
    # WATHEN_ST_SIZE_TEST tests WATHEN_ST_SIZE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Nicholas Higham,
    #    Algorithm 694: A Collection of Test Matrices in MATLAB,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 3, September 1991, pages 289-305.
    #
    #    Andrew Wathen,
    #    Realistic eigenvalue bounds for the Galerkin mass matrix,
    #    IMA Journal of Numerical Analysis,
    #    Volume 7, 1987, pages 449-457.
    #
    import platform

    print('')
    print('WATHEN_ST_SIZE_TEST_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  WATHEN_ST_SIZE returns NZ_NUM, the number of nonzeros')
    print('  in a sparse triplet format for a Wathen finite element')
    print('  matrix, given NX and NY, the number of rows and columns of')
    print('  nodes in the underlying grid.')
    print('')
    print('       NX / NY: 1       2       3       4       5       6')
    print('')

    for ny in range(1, 11):
        print('       %2d' % (ny), end='')
        for nx in range(1, 7):
            n = wathen_st_size(nx, ny)
            print('  %5d' % (n), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('WATHEN_ST_SIZE_TEST:')
    print('  Normal end of execution.')
    return


def wathen_test01():

    # *****************************************************************************80
    #
    # WATHEN_TEST01 assembles, factor and solve using WATHEN_GE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    import scipy.linalg as la
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  Assemble, factor and solve a Wathen system')
    print('  defined by WATHEN_GE.')
    print('')

    nx = 4
    ny = 4
    print('  Elements in X direction NX = %d' % (nx))
    print('  Elements in Y direction NY = %d' % (ny))
    print('  Number of elements = %d' % (nx * ny))
#
#  Compute the number of unknowns.
#
    n = wathen_order(nx, ny)
    print('  Number of nodes N = %d' % (n))
#
#  Set up a random solution X1.
#
    seed = 123456789
    x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
#
#  Compute the corresponding right hand side B.
#
    b = np.dot(a, x1)
#
#  Solve the linear system.
#
    x2 = la.solve(a, b)
#
#  Compute the norm of the solution error.
#
    e = norm(x1 - x2)
    print('  Norm of solution error is %g' % (e))
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST01:')
    print('  Normal end of execution.')
    return


def wathen_test02():

    # *****************************************************************************80
    #
    # WATHEN_TEST02 assembles, factors and solves using WATHEN_CSC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    import scipy.sparse.linalg as ssl
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  Assemble, factor and solve a Wathen system')
    print('  defined by WATHEN_CSC.')
    print('')

    nx = 4
    ny = 4

    print('  Elements in X direction NX = %d' % (nx))
    print('  Elements in Y direction NY = %d' % (ny))
    print('  Number of elements = %d' % (nx * ny))
#
#  Compute the number of unknowns.
#
    n = wathen_order(nx, ny)
    print('  Number of nodes N = %d' % (n))
#
#  Set up a random solution X1.
#
    seed = 123456789
    x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
    seed = 123456789
    a, seed = wathen_csc(nx, ny, seed)
#
#  Compute the corresponding right hand side B.
#  Oddly enough, to compute A * x1 when A is sparse, you write A.dot(X1).
#
    b = a.dot(x1)
#
#  Solve the linear system.
#
    x2 = ssl.spsolve(a, b)
#
#  Compute the norm of the solution error.
#
    e = norm(x1 - x2)
    print('  Norm of solution error is %g' % (e))
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST02:')
    print('  Normal end of execution.')
    return


def wathen_test03():

    # *****************************************************************************80
    #
    # WATHEN_TEST03 times WATHEN_GE assembly and solution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    import scipy.linalg as la
    import time
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST03')
    print('  Python version: %s' % (platform.python_version()))
    print('  For various problem sizes,')
    print('  time the assembly and factorization of a Wathen system')
    print('  using the WATHEN_GE function.')
    print('')
    print('    NX  Elements   Nodes   Storage    Assembly      Factor      Error')
    print('')

    nx = 1
    ny = 1

    for test in range(0, 6):
        #
        #  Compute the number of unknowns.
        #
        n = wathen_order(nx, ny)
        storage_ge = n * n
#
#  Set up a random solution X1.
#
        seed = 123456789
        x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
        seed = 123456789
        t0 = time.time()
        a, seed = wathen_ge(nx, ny, n, seed)
        t1 = (time.time() - t0)
#
#  Compute the corresponding right hand side B.
#
        b = np.dot(a, x1)
#
#  Solve the system.
#
        t0 = time.time()
        x2 = la.solve(a, b)
        t2 = (time.time() - t0)
#
#  Compute the norm of the solution error.
#
        e = norm(x1 - x2)
#
#  Report.
#
        print('  %4d      %4d  %6d  %8d  %10.2e  %10.2e  %10.2e' %
              (nx, nx * ny, n, storage_ge, t1, t2, e))
#
#  Ready for next iteration.
#
        nx = nx * 2
        ny = ny * 2
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST03:')
    print('  Normal end of execution.')
    return


def wathen_test04():

    # *****************************************************************************80
    #
    # WATHEN_TEST04 times WATHEN_CSC assembly and solution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    import scipy.sparse.linalg as ssl
    import time
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST04')
    print('  Python version: %s' % (platform.python_version()))
    print('  For various problem sizes,')
    print('  time the assembly and factorization of a Wathen system')
    print('  using the WATHEN_CSC function.')
    print('')
    print('    NX  Elements   Nodes    Assembly      Factor      Error')
    print('')

    nx = 1
    ny = 1

    for test in range(0, 7):
        #
        #  Compute the number of unknowns.
        #
        n = wathen_order(nx, ny)
#
#  Set up a random solution X1.
#
        seed = 123456789
        x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
        seed = 123456789
        t0 = time.time()
        a, seed = wathen_csc(nx, ny, seed)
        t1 = (time.time() - t0)
#
#  Compute the corresponding right hand side B.
#
        b = a.dot(x1)
#
#  Solve the system.
#
        t0 = time.time()
        x2 = ssl.spsolve(a, b)
        t2 = (time.time() - t0)
#
#  Compute the norm of the solution error.
#
        e = norm(x1 - x2)
#
#  Report.
#
        print('  %4d      %4d  %6d  %10.2e  %10.2e  %10.2e' %
              (nx, nx * ny, n, t1, t2, e))
#
#  Ready for next iteration.
#
        nx = nx * 2
        ny = ny * 2
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST04:')
    print('  Normal end of execution.')
    return


def wathen_test05():

    # *****************************************************************************80
    #
    # WATHEN_TEST05 times WATHEN_GE and WATHEN_CSC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    import scipy.linalg as la
    import scipy.sparse.linalg as ssl
    import time
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST05')
    print('  Python version: %s' % (platform.python_version()))
    print('  For various problem sizes, ')
    print('  time the assembly and factorization of a Wathen system')
    print('  WATHEN_GE and WATHEN_CSC.')
    print('')
    print('                   NX  Elements   Nodes    Assembly      Factor      Error')

    nx = 1
    ny = 1

    for test in range(0, 6):
        #
        #  Compute the number of unknowns.
        #
        n = wathen_order(nx, ny)
#
#  Set up a random solution X1.
#
        seed = 123456789
        x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
        seed = 123456789
        t0 = time.time()
        [a, seed] = wathen_ge(nx, ny, n, seed)
        t1 = time.time() - t0
#
#  Compute the corresponding right hand side B.
#
        b = np.dot(a, x1)
#
#  Solve the system.
#
        t0 = time.time()
        x2 = la.solve(a, b)
        t2 = time.time() - t0
#
#  Compute the maximum solution error.
#
        e = norm(x1 - x2)
#
#  Report.
#
        print('')
        print('  WATHEN_GE      %4d      %4d  %6d  %10.2e  %10.2e  %10.2e'
              % (nx, nx * ny, n, t1, t2, e))
#
#  Compute the matrix.
#
        seed = 123456789
        t0 = time.time()
        a, seed = wathen_csc(nx, ny, seed)
        t1 = time.time() - t0
#
#  Solve the system.
#
        t0 = time.time()
        x2 = ssl.spsolve(a, b)
        t2 = time.time() - t0
#
#  Compute the maximum solution error.
#
        e = norm(x1 - x2)
#
#  Report.
#
        print('  WATHEN_CSC     %4d      %4d  %6d  %10.2e  %10.2e  %10.2e'
              % (nx, nx * ny, n, t1, t2, e))
#
#  Ready for next iteration.
#
        nx = nx * 2
        ny = ny * 2
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST05:')
    print('  Normal end of execution.')
    return


def wathen_test06():

    # *****************************************************************************80
    #
    # WATHEN_TEST06 assembles, factor and solves using WATHEN_GE + CG_GE.
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
    import numpy as np
    import platform
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST06')
    print('  Python version: %s' % (platform.python_version()))
    print('  Assemble, factor and solve a Wathen system')
    print('  defined by WATHEN_GE and CG_GE.')
    print('')

    nx = 2
    ny = 2
    print('  Elements in X direction NX = %d' % (nx))
    print('  Elements in Y direction NY = %d' % (ny))
    print('  Number of elements = %d' % (nx * ny))
#
#  Compute the number of unknowns.
#
    n = wathen_order(nx, ny)
    print('  Number of nodes N = %d' % (n))
#
#  Set up a random solution X1.
#
    seed = 123456789
    x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
#
#  Compute the corresponding right hand side B.
#
    b = np.dot(a, x1)
#
#  Solve the linear system.
#
    x2 = np.ones(n)
    x2 = cg_ge(n, a, b, x2)
#
#  Compute the maximum solution error.
#
    e = norm(x1 - x2)

    print('  Maximum solution error is %g' % (e))
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST06:')
    print('  Normal end of execution.')
    return


def wathen_test07():

    # *****************************************************************************80
    #
    # WATHEN_TEST06 assembles, factor and solves using WATHEN_CSC + CG_CSC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST07')
    print('  Python version: %s' % (platform.python_version()))
    print('  Assemble, factor and solve a Wathen system')
    print('  defined by WATHEN_CSC and CG_CSC.')
    print('')

    nx = 2
    ny = 2
    print('  Elements in X direction NX = %d' % (nx))
    print('  Elements in Y direction NY = %d' % (ny))
    print('  Number of elements = %d' % (nx * ny))
#
#  Compute the number of unknowns.
#
    n = wathen_order(nx, ny)
    print('  Number of nodes N = %d' % (n))
#
#  Set up a random solution X1.
#
    seed = 123456789
    x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
    seed = 123456789
    a, seed = wathen_csc(nx, ny, seed)
#
#  Compute the corresponding right hand side B.
#
    b = a.dot(x1)
#
#  Solve the linear system.
#
    x2 = np.ones(n)
    x2 = cg_csc(n, a, b, x2)
#
#  Compute the maximum solution error.
#
    e = norm(x1 - x2)
    print('  Maximum solution error is %g' % (e))
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST07:')
    print('  Normal end of execution.')
    return


def wathen_test08():

    # *****************************************************************************80
    #
    # WATHEN_TEST08 assemble, factor and solve using WATHEN_ST + CG_ST.
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
    import numpy as np
    import platform
    from numpy.linalg import norm

    print('')
    print('WATHEN_TEST08')
    print('  Python version: %s' % (platform.python_version()))
    print('  Assemble, factor and solve a Wathen system')
    print('  defined by WATHEN_ST and CG_ST.')
    print('')

    nx = 1
    ny = 1
    print('  Elements in X direction NX = %d' % (nx))
    print('  Elements in Y direction NY = %d' % (ny))
    print('  Number of elements = %d' % (nx * ny))
#
#  Compute the number of unknowns.
#
    n = wathen_order(nx, ny)
    print('  Number of nodes N = %d' % (n))
#
#  Compute the matrix size.
#
    nz_num = wathen_st_size(nx, ny)
    print('  Number of nonzeros = %d\n' % (nz_num))
#
#  Set up a random solution X1.
#
    seed = 123456789
    x1, seed = r8vec_uniform_01(n, seed)
#
#  Compute the matrix.
#
    seed = 123456789
    row, col, a, seed = wathen_st(nx, ny, nz_num, seed)
#
#  Compute the corresponding right hand side B.
#
    b = mv_st(n, n, nz_num, row, col, a, x1)
#
#  Solve the linear system.
#
    x2 = np.ones(n)
    x2 = cg_st(n, nz_num, row, col, a, b, x2)
#
#  Compute the solution error norm.
#
    e = norm(x1 - x2)
    print('  Maximum solution error is %g' % (e))
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST08:')
    print('  Normal end of execution.')
    return


def wathen_test09():

    # *****************************************************************************80
    #
    # WATHEN_TEST09 uses SPY to display the sparsity of the Wathen matrix.
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
    import platform
    from matplotlib.pyplot import figure
    from matplotlib.pyplot import show
    from matplotlib.pyplot import savefig

    print('')
    print('WATHEN_TEST09')
    print('  Python version: %s' % (platform.python_version()))
    print('  Display the sparsity of the Wathen matrix.')

    fig = figure()
    nx = 1
    ny = 1
    n = wathen_order(nx, ny)
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
    ax1 = fig.add_subplot(231)
    ax1.spy(a, markersize=4)

    nx = 2
    ny = 2
    n = wathen_order(nx, ny)
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
    ax2 = fig.add_subplot(232)
    ax2.spy(a, markersize=4)

    nx = 3
    ny = 3
    n = wathen_order(nx, ny)
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
    ax3 = fig.add_subplot(233)
    ax3.spy(a, markersize=4)

    nx = 4
    ny = 4
    n = wathen_order(nx, ny)
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
    ax4 = fig.add_subplot(234)
    ax4.spy(a, markersize=4)

    nx = 5
    ny = 5
    n = wathen_order(nx, ny)
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
    ax5 = fig.add_subplot(235)
    ax5.spy(a, markersize=4)

    nx = 6
    ny = 6
    n = wathen_order(nx, ny)
    seed = 123456789
    a, seed = wathen_ge(nx, ny, n, seed)
    ax6 = fig.add_subplot(236)
    ax6.spy(a, markersize=4)

    fig.suptitle('WATHEN Matrix Sparsity Pattern')

    show(block=False)

    filename = 'wathen_spy.png'
    fig.savefig(filename)
    print('')
    print('  Graphics file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST09:')
    print('  Normal end of execution.')
    return


def wathen_test():

    # *****************************************************************************80
    #
    # WATHEN_TEST tests the WATHEN library.
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
    import platform

    print('')
    print('WATHEN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WATHEN library.')
#
#  Direct Solve
#
    wathen_test01()
    wathen_test02()
#
#  Timings.
#
    wathen_test03()
    wathen_test04()
    wathen_test05()
#
#  CG Solve
#
    wathen_test06()
    wathen_test07()
    wathen_test08()
#
#  Use SPY to display the sparsity of the matrix.
#
    wathen_test09()

    wathen_order_test()
    wathen_st_size_test()
#
#  Terminate.
#
    print('')
    print('WATHEN_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    wathen_test()
    timestamp()
