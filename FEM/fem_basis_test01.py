#! /usr/bin/env python3
#


def fem_basis_1d(i, j, x):

    # *****************************************************************************80
    #
    # FEM_BASIS_1D evaluates an arbitrary 1D basis function.
    #
    #  Discussion:
    #
    #    Given the maximum degree D for the polynomial basis defined
    #    on a reference interval, we have D + 1 monomials
    #    of degree at most D.  In each barycentric coordinate, we define
    #    D+1 points, so that 0 <= I, J <= D and I+J = D, with
    #    (I,J) corresponding to
    #    * the basis point X(I,J) = ( I/D )
    #    * the basis monomial P(I,J)(X) = X^I.
    #
    #    For example, with D = 2, we have simply:
    #
    #      A---B---C
    #
    #    with
    #
    #       I J    X      P(I,J)(X)
    #
    #    A (0 2) ( 0.0 )  1
    #    B (1 1) ( 0.5 )  x
    #    C (2 0) ( 1.0 )  x^2
    #
    #    Now instead of the monomials P(I,J)(X), we want a set of
    #    polynomials L(I,J)(X) which span the same space, but have
    #    the Lagrange property, namely L(I,J) (X) is 1 if X is
    #    equal to X(I,J), and 0 if X is equal to any other
    #    of the basis points.
    #
    #    This is easily arranged.  Given an index (I,J), we compute
    #    1) I factors of the form (X-0)   * (X-1/D)   * ... * (X-(I-1)/D)
    #    2) J factors of the form ???
    #
    #    This results in the product of I+J linear factors, in other words,
    #    a polynomial of degree D.  This polynomial is 0 at all basis points
    #    except X(I,J).  If we divide this polynomial by its value at
    #    the basis point, we arrive at the desired Lagrange polynomial
    #    L(I,J)(X).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, the integer barycentric coordinates of the basis
    #    function, 0 <= I, J.  The polynomial degree D = I + J
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real LIJ, the value of the basis function at X.
    #
    d = i + j
    lij = 1.0
    cij = 1.0

    for p in range(0, i):
        lij = lij * (d * x - p)
        cij = cij * (i - p)

    for p in range(0, j):
        lij = lij * (d * x - (d - p))
        cij = cij * (i - (d - p))

    lij = lij / cij

    return lij


def fem_basis_2d(i, j, k, x, y):

    # *****************************************************************************80
    #
    # FEM_BASIS_2D evaluates an arbitrary triangular basis function.
    #
    #  Discussion:
    #
    #    Given the maximum degree D for the polynomial basis defined
    #    on a reference triangle, we have ( ( D + 1 ) * ( D + 2 ) ) / 2 monomials
    #    of degree at most D.  In each barycentric coordinate, we define
    #    D+1 planes, so that 0 <= I, J, K <= D and I+J+K = D, with
    #    (I,J,K) corresponding to
    #    * the basis point (X,Y)(I,J,K) = ( I/D, J/D )
    #    * the basis monomial P(I,J,K)(X,Y) = X^I Y^J.
    #
    #    For example, with D = 2, we have simply:
    #
    #    F
    #    |\
    #    C-E
    #    |\|\
    #    A-B-D
    #
    #    with
    #
    #       I J K    X    Y    P(I,J,K)(X,Y)
    #
    #    A (0 0 2) (0.0, 0.0)  1
    #    B (1 0 1) (0.5, 0.0)  x
    #    C (0 1 1) (0.0, 0.5)  y
    #    D (2 0 0) (1.0, 0.0)  x^2
    #    E (1 1 0) (0.5, 0.5)  x y
    #    F (0 2 0) (0.0, 1.0)  y^2
    #
    #    Now instead of the monomials P(I,J,K)(X,Y), we want a set of
    #    polynomials L(I,J,K)(X,Y) which span the same space, but have
    #    the Lagrange property, namely L(I,J,K) (X,Y) is 1 if (X,Y) is
    #    equal to (X,Y)(I,J,K), and 0 if (X,Y) is equal to any other
    #    of the basis points.
    #
    #    This is easily arranged.  Given an index (I,J,K), we compute
    #    1) I factors of the form (X-0)   * (X-1/D)   * ... * (X-(I-1)/D)
    #    2) J factors of the form (Y-0)   * (Y-1/D)   * ... * (Y-(J-1)/D)
    #    3) K factors of the form (X+Y-(D-0)/D) * (X+Y-(D-1)/D) * ... * (X+Y-(D-(K-1))/D).
    #
    #    This results in the product of I+J+K linear factors, in other words,
    #    a polynomial of degree D.  This polynomial is 0 at all basis points
    #    except (X,Y)(I,J,K).  If we divide this polynomial by its value at
    #    the basis point, we arrive at the desired Lagrange polynomial
    #    L(I,J,K)(X,Y).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, K, the integer barycentric coordinates of
    #    the basis function, 0 <= I, J, K.  The polynomial degree D = I + J + K.
    #
    #    Input, real X, Y, the evaluation point.
    #
    #    Output, real LIJK, the value of the basis function at (X,Y).
    #
    d = i + j + k
    lijk = 1.0
    cijk = 1.0

    for p in range(0, i):
        lijk = lijk * (d * x - p)
        cijk = cijk * (i - p)

    for p in range(0, j):
        lijk = lijk * (d * y - p)
        cijk = cijk * (j - p)

    for p in range(0, k):
        lijk = lijk * (d * (x + y) - (d - p))
        cijk = cijk * ((i + j) - (d - p))

    lijk = lijk / cijk

    return lijk


def fem_basis_3d(i, j, k, l, x, y, z):

    # *****************************************************************************80
    #
    # FEM_BASIS_3D evaluates an arbitrary tetrahedral basis function.
    #
    #  Discussion:
    #
    #    Given the maximum degree D for the polynomial basis defined
    #    on a reference tetrahedron, we have
    #    ( D + 1 ) * ( D + 2 ) * ( D + 3 ) / 6 monomials
    #    of degree at most D.  In each barycentric coordinate, we define
    #    D+1 planes, so that 0 <= I, J, K, L <= D and I+J+K+L = D, with
    #    (I,J,K,L) corresponding to
    #    * the basis point (X,Y,Z)(I,J,K,L) = ( I/D, J/D, K/D )
    #    * the basis monomial P(I,J,K,L)(X,Y,Z) = X^I Y^J Z^K.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, K, L, the integer barycentric
    #    coordinates of the basis function, 0 <= I, J, K, L.
    #    The polynomial degree D = I + J + K + L.
    #
    #    Input, real X, Y, Z, the evaluation point.
    #
    #    Output, real LIJKL, the value of the basis function at (X,Y,Z).
    #
    d = i + j + k + l
    lijkl = 1.0
    cijkl = 1.0

    for p in range(0, i):
        lijkl = lijkl * (d * x - p)
        cijkl = cijkl * (i - p)

    for p in range(0, j):
        lijkl = lijkl * (d * y - p)
        cijkl = cijkl * (j - p)

    for p in range(0, k):
        lijkl = lijkl * (d * z - p)
        cijkl = cijkl * (k - p)

    for p in range(0, l):
        lijkl = lijkl * (d * (x + y + z) - (d - p))
        cijkl = cijkl * ((i + j + k) - (d - p))

    lijkl = lijkl / cijkl

    return lijkl


def fem_basis_md(m, i, x):

    # *****************************************************************************80
    #
    # FEM_BASIS_MD evaluates an arbitrary M-dimensional basis function.
    #
    #  Discussion:
    #
    #    This routine evaluates the generalization of the formula used for
    #    the 1D, 2D and 3D cases.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer I(M+1), the integer barycentric
    #    coordinates of the basis function, 0 <= I(1:M+1).
    #    The polynomial degree D = sum(I(1:M+1)).
    #
    #    Input, real X(M), the evaluation point.
    #
    #    Output, real L, the value at X of the basis function designated by I.
    #
    import numpy as np
#
#  Augment the X vector.
#
    x2 = np.zeros(m + 1)
    for index in range(0, m):
        x2[index] = x[index]
    x2[m] = 1.0 - np.sum(x[0:m])
#
#  Determine the degree.
#
    d = np.sum(i[0:m + 1])

    l = 1.0

    for q in range(0, m + 1):
        for p in range(0, i[q]):
            l = l * (d * x2[q] - p) / float(i[q] - p)

    return l


def fem_basis_prism_triangle(i, j, xyz):

    # *****************************************************************************80
    #
    # FEM_BASIS_PRISM_TRIANGLE evaluates a triangular prism basis function.
    #
    #  Discussion:
    #
    #    The element is a 3D prism, formed from a triangular base in the
    #    XY plane that is extended vertically in the Z direction.
    #
    #    I(1:3) are the integer barycentric coordinates of a point in the
    #    triangle.  I(1) + I(2) + I(3) = DI, the degree of the triangular
    #    basis function BI.  X = I(1) / DI, Y = I(2) / DI.
    #    The triangle is assumed to be the unit reference
    #    triangle 0 <= X <= 1, 0 <= Y <= 1, 0 <= X + Y <= 1.
    #
    #    J(1:2) are the integer barycentric coordinates of a point in the
    #    line segment.  J(1) + J(2) = DJ, the degree of the linear basis
    #    function BJ.  Z = J(1) / DJ.
    #    The line is assumed to be the unit line 0 <= Z <= 1.
    #
    #    The degree of the basis function B = BI * BJ is D = DI + DJ.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I(3), the integer barycentric coordinates of
    #    the triangular basis function, 0 <= I(*).
    #    The polynomial degree DI = I(1) + I(2) + I(3).
    #
    #    Input, integer J(2), the integer barycentric coordinates of
    #    the linear basis function, 0 <= J(*).
    #    The polynomial degree DJ = J(1) + J(2).
    #
    #    Input, real XYZ(3), the evaluation point.
    #
    #    Output, real B, the value of the basis function at XYZ.
    #
    bi = fem_basis_2d(i[0], i[1], i[2], xyz[0], xyz[1])

    bj = fem_basis_1d(j[0], j[1], xyz[2])

    b = bi * bj

    return b


def fem_basis_test01():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST01 tests FEM_BASIS_1D
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('FEM_BASIS_TEST01 ')
    print('  FEM_BASIS_1D evaluates an arbitrary ')
    print('  basis function over an interval. ')

    i1 = 2
    j1 = 1
    d = i1 + j1
    x1 = float(i1) / float(d)
    print('')
    print('   I   J        X          L(I,J)(X) ')
    print('')
    print('  %2d  %2d  %10.4f  %14.6g ' % (i1, j1, x1, 1.0))
    print('')
    for i2 in range(0, d + 1):
        j2 = d - i2
        x2 = float(i2) / float(d)
        lij = fem_basis_1d(i1, j1, x2)
        print('  %2d  %2d  %10.4f  %14.6g ' % (i2, j2, x2, lij))


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
    # FEM_BASIS_TEST tests the FEM_BASIS library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FEM_BASIS_TEST: ')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the FEM_BASIS library. ')

    fem_basis_test01()

    print('')
    print('FEM_BASIS_TEST: ')
    print('  Normal end of execution. ')
    print('')

    timestamp()
