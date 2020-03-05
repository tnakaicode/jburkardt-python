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

    return


def fem_basis_test02():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST02 tests FEM_BASIS_2D
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
    print('FEM_BASIS_TEST02 ')
    print('  FEM_BASIS_2D evaluates an arbitrary triangular ')
    print('  basis function. ')

    i1 = 1
    j1 = 0
    k1 = 2
    d = i1 + j1 + k1
    x1 = float(i1) / float(d)
    y1 = float(j1) / float(d)
    print('')
    print('   I   J   K        X           Y      L(I,J,K)(X,Y) ')
    print('')
    print('  %2d  %2d  %2d  %10.4f  %10.4f  %14.6g '
          % (i1, j1, k1, x1, y1, 1.0))
    print('')
    for j2 in range(0, d + 1):
        for i2 in range(0, d - j2 + 1):
            k2 = d - i2 - j2
            x2 = float(i2) / float(d)
            y2 = float(j2) / float(d)
            lijk = fem_basis_2d(i1, j1, k1, x2, y2)
            print('  %2d  %2d  %2d  %10.4f  %10.4f  %14.6g '
                  % (i2, j2, k2, x2, y2, lijk))

    return


def fem_basis_test03():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST03 tests FEM_BASIS_3D
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
    print('FEM_BASIS_TEST03 ')
    print('  FEM_BASIS_3D evaluates an arbitrary tetrahedral ')
    print('  basis function. ')

    i1 = 1
    j1 = 0
    k1 = 2
    l1 = 1
    d = i1 + j1 + k1 + l1
    x1 = float(i1) / float(d)
    y1 = float(j1) / float(d)
    z1 = float(k1) / float(d)
    print('')
    print('   I   J   K   L        X           Y           Z      L(I,J,K,L)(X,Y,Z) ')
    print('')
    print('  %2d  %2d  %2d  %2d  %10.4f  %10.4f  %10.4f  %14.6g '
          % (i1, j1, k1, l1, x1, y1, z1, 1.0))
    print('')
    for k2 in range(0, d + 1):
        for j2 in range(0, d - k2 + 1):
            for i2 in range(0, d - j2 - k2 + 1):
                l2 = d - i2 - j2 - k2
                x2 = float(i2) / float(d)
                y2 = float(j2) / float(d)
                z2 = float(k2) / float(d)
                lijkl = fem_basis_3d(i1, j1, k1, l1, x2, y2, z2)
                print('  %2d  %2d  %2d  %2d  %10.4f  %10.4f  %10.4f  %14.6g '
                      % (i2, j2, k2, l2, x2, y2, z2, lijkl))

    return


def fem_basis_test04():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST04 repeats TEST01 using FEM_BASIS_MD.
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
    import numpy as np

    print('')
    print('FEM_BASIS_TEST04 ')
    print('  FEM_BASIS_MD evaluates an arbitrary ')
    print('  basis function over an M-dimensional simplex. ')

    m = 1

    i1 = np.array([2, 1])
    d = np.sum(i1[0:m + 1])
    x1 = np.zeros(1)
    x1[0:m] = float(i1[0:m]) / float(d)
    print('')
    print('   I   J        X          L(I,J)(X) ')
    print('')
    print('  %2d  %2d  %10.4f  %14.6g' % (i1[0], i1[1], x1[0], 1.0))
    print('')
    i2 = np.zeros(m + 1)
    x2 = np.zeros(m)
    for p1 in range(0, d + 1):
        i2[0] = p1
        i2[m] = d - np.sum(i2[0:m])
        for index in range(0, m):
            x2[index] = float(i2[index]) / float(d)
        l = fem_basis_md(m, i1, x2)
        print('  %2d  %2d  %10.4f  %14.6g ' % (i2[0], i2[1], x2[0], l))

    return


def fem_basis_test05():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST05 repeats TEST02 using FEM_BASIS_MD.
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
    import numpy as np

    print('')
    print('FEM_BASIS_TEST05 ')
    print('  FEM_BASIS_MD evaluates an arbitrary ')
    print('  basis function over an M-dimensional simplex. ')

    m = 2

    i1 = np.array([1, 0, 2])
    d = np.sum(i1[0:m + 1])
    x1 = np.zeros(m)
    for index in range(0, m):
        x1[index] = float(i1[index]) / float(d)
    print('')
    print('   I   J   K        X           Y      L(I,J,K)(X,Y) ')
    print('')
    print('  %2d  %2d  %2d  %10.4f  %10.4f  %14.6g '
          % (i1[0], i1[1], i1[2], x1[0], x1[1], 1.0))
    print('')
    i2 = np.zeros(m + 1)
    x2 = np.zeros(m)
    for p2 in range(0, d + 1):
        i2[1] = p2
        for p1 in range(0, d - p2 + 1):
            i2[0] = p1
            i2[m] = d - np.sum(i2[0:m])
            for index in range(0, m):
                x2[index] = float(i2[index]) / float(d)
            l = fem_basis_md(m, i1, x2)
            print('  %2d  %2d  %2d  %10.4f  %10.4f  %14.6g '
                  % (i2[0], i2[1], i2[2], x2[0], x2[1], l))

    return


def fem_basis_test06():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST06 repeats TEST03 using FEM_BASIS_MD.
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
    import numpy as np

    print('')
    print('FEM_BASIS_TEST06 ')
    print('  FEM_BASIS_MD evaluates an arbitrary ')
    print('  basis function over an M-dimensional simplex. ')

    m = 3

    i1 = np.array([1, 0, 2, 1])
    d = np.sum(i1[0:m + 1])
    x1 = np.zeros(m)
    for index in range(0, m):
        x1[index] = float(i1[index]) / float(d)
    print('')
    print('   I   J   K   L        X           Y           Z      L(I,J,K,L)(X,Y,Z) ')
    print('')
    print('  %2d  %2d  %2d  %2d  %10.4f  %10.4f  %10.4f  %14.6g '
          % (i1[0], i1[1], i1[2], i1[3], x1[0], x1[1], x1[2], 1.0))
    print('')
    i2 = np.zeros(m + 1)
    x2 = np.zeros(m)
    for p3 in range(0, d + 1):
        i2[2] = p3
        for p2 in range(0, d - p3 + 1):
            i2[1] = p2
            for p1 in range(0, d - p2 - p3 + 1):
                i2[0] = p1
                i2[m] = d - np.sum(i2[0:m])
                for index in range(0, m):
                    x2[index] = float(i2[index]) / float(d)
                l = fem_basis_md(m, i1, x2)
                print('  %2d  %2d  %2d  %2d  %10.4f  %10.4f  %10.4f  %14.6g '
                      % (i2[0], i2[1], i2[2], i2[3], x2[0], x2[1], x2[2], l))

    return


def fem_basis_test07():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST07 tests FEM_BASIS_PRISM_TRIANGLE.
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
    import numpy as np

    print('')
    print('FEM_BASIS_TEST07 ')
    print('  FEM_BASIS_PRISM_TRIANGLE evaluates an arbitrary ')
    print('  basis function over a right triangular prism. ')
    print('')
    print('  Here, we generate basis functions which can be ')
    print('  up to degree 2 in X and Y, and up to degree 2 in Z. ')
    print('')
    print('  Choose a node N1, define the basis function associated ')
    print('  with that node, and then evaluate it at all other nodes. ')

    i1 = np.array([2, 0, 0], dtype=np.int32)
    di = np.sum(i1[0:3])
    xyz1 = np.zeros(3)
    xyz1[0] = float(i1[0]) / float(di)
    xyz1[1] = float(i1[1]) / float(di)

    j1 = np.array([1, 1], dtype=np.int32)
    dj = np.sum(j1[0:2])
    xyz1[2] = float(j1[0]) / float(dj)

    print('')
    print('  I1  I2  I3  J1  J2        X           Y           Z          B(X,Y,Z) ')
    print('')
    print('  %2d  %2d  %2d  %2d  %2d  %10f  %10f  %10f  %14g '
          % (i1[0], i1[1], i1[2], j1[0], j1[1], xyz1[0], xyz1[1], xyz1[2], 1.0))
    print('')

    xyz2 = np.zeros(3)

    i2 = np.zeros(3, dtype=np.int32)
    j2 = np.zeros(2, dtype=np.int32)
    for i_1 in range(0, di + 1):
        i2[0] = i_1
        xyz2[0] = float(i2[0]) / float(di)
        for i_2 in range(0, di - i2[0] + 1):
            i2[1] = i_2
            xyz2[1] = float(i2[1]) / float(di)
            i2[2] = di - i2[0] - i2[1]
            for j_1 in range(0, dj + 1):
                j2[0] = j_1
                j2[1] = dj - j2[0]
                xyz2[2] = float(j2[0]) / float(dj)

                b = fem_basis_prism_triangle(i1, j1, xyz2)

                print('  %2d  %2d  %2d  %2d  %2d  %10f  %10f  %10f  %14g '
                      % (i2[0], i2[1], i2[2], j2[0], j2[1], xyz2[0], xyz2[1], xyz2[2], b))

    return


def fem_basis_test08():

    # *****************************************************************************80
    #
    # FEM_BASIS_TEST08 tests FEM_BASIS_PRISM_TRIANGLE.
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
    import numpy as np

    print('')
    print('FEM_BASIS_TEST08 ')
    print('  FEM_BASIS_PRISM_TRIANGLE evaluates an arbitrary ')
    print('  basis function over a right triangular prism. ')
    print('')
    print('  Here, we generate basis functions which can be ')
    print('  up to degree 3 in X and Y, and up to degree 1 in Z. ')
    print('')
    print('  Choose a node N1, define the basis function associated ')
    print('  with that node, and then evaluate it at all other nodes. ')

    i1 = np.array([2, 0, 1], dtype=np.int32)
    di = np.sum(i1[0:3])
    xyz1 = np.zeros(3)
    xyz1[0] = float(i1[0]) / float(di)
    xyz1[1] = float(i1[1]) / float(di)

    j1 = np.array([1, 0], dtype=np.int32)
    dj = np.sum(j1[0:2])
    xyz1[2] = float(j1[0]) / float(dj)

    print('')
    print('  I1  I2  I3  J1  J2        X           Y           Z          B(X,Y,Z) ')
    print('')
    print('  %2d  %2d  %2d  %2d  %2d  %10f  %10f  %10f  %14g '
          % (i1[0], i1[1], i1[2], j1[0], j1[1], xyz1[0], xyz1[1], xyz1[2], 1.0))
    print('')

    xyz2 = np.zeros(3)

    i2 = np.zeros(3, dtype=np.int32)
    j2 = np.zeros(2, dtype=np.int32)
    for i_1 in range(0, di + 1):
        i2[0] = i_1
        xyz2[0] = float(i2[0]) / float(di)
        for i_2 in range(0, di - i2[0] + 1):
            i2[1] = i_2
            xyz2[1] = float(i2[1]) / float(di)
            i2[2] = di - i2[0] - i2[1]
            for j_1 in range(0, dj + 1):
                j2[0] = j_1
                j2[1] = dj - j2[0]
                xyz2[2] = float(j2[0]) / float(dj)

                b = fem_basis_prism_triangle(i1, j1, xyz2)

                print('  %2d  %2d  %2d  %2d  %2d  %10f  %10f  %10f  %14g '
                      % (i2[0], i2[1], i2[2], j2[0], j2[1], xyz2[0], xyz2[1], xyz2[2], b))

    return


def fem_basis_test():

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
    fem_basis_test02()
    fem_basis_test03()
#
#  Repeat the tests, now using FEM_BASIS_MD.
#
    fem_basis_test04()
    fem_basis_test05()
    fem_basis_test06()
#
#  Tests for triangular prism.
#
    fem_basis_test07()
    fem_basis_test08()
#
#  Terminate.
#
    print('')
    print('FEM_BASIS_TEST: ')
    print('  Normal end of execution. ')
    print('')
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
    fem_basis_test()
    timestamp()
