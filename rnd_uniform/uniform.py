#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#

import numpy as np
from sys import exit


def r8po_fa(n, a):

    #
    # R8PO_FA factors a R8PO matrix.
    #
    #  Discussion:
    #
    #    The R8PO storage format is appropriate for a symmetric positive definite
    #    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
    #    upper triangular matrix, so it will be in R8GE storage format.)
    #
    #    Only the diagonal and upper triangle of the square array are used.
    #    This same storage scheme is used when the matrix is factored by
    #    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
    #    is set to zero.
    #
    #    The positive definite symmetric matrix A has a Cholesky factorization
    #    of the form:
    #
    #      A = R' * R
    #
    #    where R is an upper triangular matrix with positive elements on
    #    its diagonal.  This routine overwrites the matrix A with its
    #    factor R.
    #
    #    This function failed miserably when I wrote "r = a", because of a
    #    disastrously misconceived feature of Python, which does not copy
    #    one matrix to another, but makes them both point to the same object.
    #
    #  Reference:
    #
    #    Dongarra, Bunch, Moler, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the matrix in R8PO storage.
    #
    #    Output, real R(N,N), the Cholesky factor R in R8GE storage.
    #
    #    Output, integer INFO, error flag.
    #    0, normal return.
    #    K, error condition.  The principal minor of order K is not
    #    positive definite, and the factorization was not completed.
    #
    import numpy as np
    from sys import exit

    r = np.zeros([n, n])

    for i in range(0, n):
        for j in range(i, n):
            r[i, j] = a[i, j]

    for j in range(0, n):

        for k in range(0, j):
            t = 0.0
            for i in range(0, k):
                t = t + r[i, k] * r[i, j]
            r[k, j] = (r[k, j] - t) / r[k, k]

        t = 0.0
        for i in range(0, j):
            t = t + r[i, j] ** 2

        s = r[j, j] - t

        if (s <= 0.0):
            print('')
            print('R8PO_FA - Fatal error!')
            print('  Factorization fails on column %d.' % (j))
            exit('R8PO_FA - Fatal error!')

        r[j, j] = np.sqrt(s)
    #
    #  Since the Cholesky factor is stored in R8GE format, be sure to
    #  zero out the lower triangle.
    #
    for i in range(0, n):
        for j in range(0, i):
            r[i, j] = 0.0

    return r


def r8po_sl(n, r, b):

    # *****************************************************************************80
    #
    # R8PO_SL solves a R8PO system factored by R8PO_FA.
    #
    #  Discussion:
    #
    #    The R8PO storage format is appropriate for a symmetric positive definite
    #    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
    #    upper triangular matrix, so it will be in R8GE storage format.)
    #
    #    Only the diagonal and upper triangle of the square array are used.
    #    This same storage scheme is used when the matrix is factored by
    #    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
    #    is set to zero.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Bunch, Moler, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real R(N,N), the Cholesky factor, in R8GE storage,
    #    returned by R8PO_FA.
    #
    #    Input, real B(N), the right hand side.
    #
    #    Output, real X(N), the solution vector.
    #
    x = np.zeros(n)
    for i in range(0, n):
        x[i] = b[i]
    #
    #  Solve R' * y = b.
    #
    for k in range(0, n):
        t = 0.0
        for i in range(0, k):
            t = t + x[i] * r[i, k]
        x[k] = (x[k] - t) / r[k, k]
    #
    #  Solve R * x = y.
    #
    for k in range(n - 1, -1, -1):
        x[k] = x[k] / r[k, k]
        for i in range(0, k):
            x[i] = x[i] - r[i, k] * x[k]

    return x


def r8_normal_01(seed):

    # *****************************************************************************80
    #
    # R8_NORMAL_01 samples the standard normal probability distribution.
    #
    #  Discussion:
    #
    #    The standard normal probability distribution function (PDF) has
    #    mean 0 and standard deviation 1.
    #
    #    The Box-Muller method is used.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)
    x = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)
    return x, seed


def r8vec_normal_01(n, seed):

    #
    # R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
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
    x = np.zeros(n)
    for i in range(0, n):
        x[i], seed = r8_normal_01(seed)
    return x, seed


def r8_uniform_01(seed):

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


def r8mat_uniform_01(m, n, seed):

    #
    # R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
    #
    # Reference:
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

    i4_huge = 2147483647
    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8MAT_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8MAT_UNIFORM_01 - Fatal error!')

    r = np.zeros((m, n))
    for j in range(0, n):
        for i in range(0, m):
            k = (seed // 127773)
            seed = 16807 * (seed - k * 127773) - k * 2836
            seed = (seed % i4_huge)

            if (seed < 0):
                seed = seed + i4_huge

            r[i, j] = seed * 4.656612875E-10
    return r, seed


def r8vec_uniform_01(n, seed):

    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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


def uniform_in_sphere01_map(m, n, seed):

    #
    # UNIFORM_IN_SPHERE01_MAP maps uniform points in the unit M-dimensional sphere.
    #
    #  Discussion:
    #
    #    The sphere has center 0 and radius 1.
    #
    #    We first generate a point ON the sphere, and then distribute it
    #    IN the sphere.
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Random Variate Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998, pages 168.
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Wiley, 1986, page 232.
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the points.
    #
    exponent = 1.0 / float(m)
    x = np.zeros([m, n])
    for j in range(0, n):
        #
        #  Fill a vector with normally distributed values.
        #
        v, seed = r8vec_normal_01(m, seed)
        #
        #  Compute the length of the vector.
        #
        norm = np.linalg.norm(v)
        #
        #  Normalize the vector.
        #
        v[0:m] = v[0:m] / norm
        #
        #  Now compute a value to map the point ON the sphere INTO the sphere.
        #
        r, seed = r8_uniform_01(seed)

        x[0:m, j] = r ** exponent * v[0:m]

    return x, seed
