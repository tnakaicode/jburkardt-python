#! /usr/bin/env python3
#
def dpofa(a, lda, n):
    
    # *****************************************************************************80
    #
    # DPOFA factors a real symmetric positive definite matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    FORTRAN77 version by Cleve Moler.
    #    Python version by John Burkardt.
    #
    #  Parameters:
    #
    #    Input, real A(LDA,N), the symmetric matrix to be factored.  Only the
    #    diagonal and upper triangle are accessed.
    #
    #    Input, integer LDA, the leading dimension of the array A.
    #    N <= LDA.
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Output, real A_FAC(LDA,N), an upper triangular matrix R such that
    #    A = R' * R.  If INFO is nonzero, the factorization was not completed.
    #
    #    Output, integer INFO, error flag.
    #    0, no error was detected.
    #    K, the leading minor of order K is not positive definite.
    #
    import numpy as np

    a_fac = a.copy()

    for i in range(1, n):
        for j in range(0, i):
            a_fac[i, j] = 0.0

    info = 0

    for j in range(0, n):
        s = 0.0
        for k in range(0, j):
            t = a_fac[k, j]
            for i in range(0, k):
                t = t - a_fac[i, k] * a_fac[i, j]
            t = t / a_fac[k, k]
            a_fac[k, j] = t
            s = s + t * t

        s = a_fac[j, j] - s
        if (s <= 0.0):
            info = j + 1
            return a_fac, info

        a_fac[j, j] = np.sqrt(s)

    return a_fac, info


def dpofa_test():

    # *****************************************************************************80
    #
    # DPOFA_TEST tests DPOFA.
    #
    #  Discussion:
    #
    #    DPOFA factors a positive definite symmetric matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 5
    lda = n

    print('')
    print('DPOFA_TEST')
    print('  DPOFA computes the LU factors of a positive definite symmetric matrix,')
#
#  Set the matrix A.
#
    a = np.zeros([n, n])

    for i in range(0, n):
        a[i, i] = 2.0
        if (0 < i):
            a[i, i - 1] = -1.0
        if (i < n - 1):
            a[i, i + 1] = -1.0

    print('')
    print('  Matrix A:')
    print('')
    for i in range(0, n):
        print('    ', end='')
        for j in range(0, n):
            print('%g' % (a[i, j]), end='')
        print('')
#
#  Factor the matrix.
#
    print('')
    print('  Call DPOFA to factor the matrix.')

    a_lu, info = dpofa(a, lda, n)

    if (info != 0):
        print('')
        print('  Error, DPOFA returns INFO = %d' % (info))
        return

    print('')
    print('  Upper triangular factor U:')
    print('')
    for i in range(0, n):
        print('    ', end='')
        for j in range(0, n):
            print('%8g' % (a_lu[i, j]), end='')
        print('')

    uut = np.dot(np.transpose(a_lu), a_lu)

    print('')
    print('  Product Ut * U:')
    print('')
    for i in range(0, n):
        print('    ', end='')
        for j in range(0, n):
            print('%8g' % (uut[i, j]), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('DPOFA_TEST')
    print('  Normal end of execution.')
    return


def dqrdc(a, lda, n, p, jpvt, job):

    # *****************************************************************************80
    #
    # DQRDC computes the QR factorization of a real rectangular matrix.
    #
    #  Discussion:
    #
    #    DQRDC uses Householder transformations.
    #
    #    Column pivoting based on the 2-norms of the reduced columns may be
    #    performed at the user's option.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2016
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Moler, Bunch, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, (Society for Industrial and Applied Mathematics),
    #    3600 University City Science Center,
    #    Philadelphia, PA, 19104-2688.
    #    ISBN 0-89871-172-X
    #
    #  Parameters:
    #
    #    Input, real A(LDA,P), the N by P matrix whose decomposition is to
    #    be computed.
    #
    #    Input, integer LDA, the leading dimension of the array A.  LDA must
    #    be at least N.
    #
    #    Input, integer N, the number of rows of the matrix A.
    #
    #    Input, integer P, the number of columns of the matrix A.
    #
    #    Input, integer JPVT(P), integers that control the selection of the pivot
    #    columns.  The K-th column A(*,K) of A is placed in one of three classes
    #    according to the value of JPVT(K).
    #      > 0, then A(K) is an initial column.
    #      = 0, then A(K) is a free column.
    #      < 0, then A(K) is a final column.
    #    Before the decomposition is computed, initial columns are moved to
    #    the beginning of the array A and final columns to the end.  Both
    #    initial and final columns are frozen in place during the computation
    #    and only free columns are moved.  At the K-th stage of the
    #    reduction, if A(*,K) is occupied by a free column it is interchanged
    #    with the free column of largest reduced norm.  JPVT is not referenced
    #    if JOB == 0.
    #
    #    Input, integer JOB, initiates column pivoting.
    #    0, no pivoting is done.
    #    nonzero, pivoting is done.
    #
    #    Output, real A(LDA,P), contains in its upper triangle the upper
    #    triangular matrix R of the QR factorization.  Below its diagonal
    #    A contains information from which the orthogonal part of the
    #    decomposition can be recovered.  Note that if pivoting has been
    #    requested, the decomposition is not that of the original matrix A
    #    but that of A with its columns permuted as described by JPVT.
    #
    #    Output, real QRAUX(P), contains further information required
    #    to recover the orthogonal part of the decomposition.
    #
    #    Output, integer JPVT(P), JPVT(K) contains the index of the column of the
    #    original matrix that has been interchanged into the K-th column, if
    #    pivoting was requested.
    #
    import numpy as np

    pl = 1
    pu = 0
    qraux = np.zeros(p)
    work = np.zeros(p)
#
#  If pivoting is requested, rearrange the columns.
#
    if (job != 0):

        for j in range(0, p):

            swapj = (0 < jpvt[j])

            if (jpvt[j] < 0):
                jpvt[j] = - (j + 1)
            else:
                jpvt[j] = (j + 1)

            if (swapj):

                if (j + 1 != pl):
                    for i in range(0, n):
                        t = a[i, pl - 1]
                        a[i, pl - 1] = a[i, j]
                        a[i, j] = t

                jpvt[j] = jpvt[pl - 1]
                jpvt[pl - 1] = j + 1
                pl = pl + 1

        pu = p

        for j in range(p - 1, -1, -1):

            if (jpvt[j] < 0):

                jpvt[j] = - jpvt[j]

                if (j + 1 != pu):

                    for i in range(0, n):
                        t = a[i, pu - 1]
                        a[i, pu - 1] = a[i, j]
                        a[i, j] = t

                    jp = jpvt[pu - 1]
                    jpvt[pu - 1] = jpvt[j]
                    jpvt[j] = jp

                pu = pu - 1
#
#  Compute the norms of the free columns.
#
    for j in range(pl - 1, pu):
        t = 0.0
        for i in range(0, n):
            t = t + a[i, j] ** 2
        qraux[j] = np.sqrt(t)
        work[j] = qraux[j]
#
#  Perform the Householder reduction of A.
#
    lup = min(n, p)

    for l in range(0, lup):
        #
        #  Bring the column of largest norm into the pivot position.
        #
        if (pl <= l + 1 and l + 1 < pu):

            maxnrm = 0.0
            maxj = l

            for j in range(l, pu):

                if (maxnrm < qraux[j]):
                    maxnrm = qraux[j]
                    maxj = j

            if (maxj != l):

                for i in range(0, n):
                    t = a[i, l]
                    a[i, l] = a[i, maxj]
                    a[i, maxj] = t

                qraux[maxj] = qraux[l]
                work[maxj] = work[l]

                jp = jpvt[maxj]
                jpvt[maxj] = jpvt[l]
                jpvt[l] = jp
#
#  Compute the Householder transformation for column L.
#
        qraux[l] = 0.0

        if (l + 1 != n):

            t = 0.0
            for i in range(l, n):
                t = t + a[i, l] ** 2
            nrmxl = np.sqrt(t)

            if (nrmxl != 0.0):

                if (a[l, l] < 0.0):
                    nrmxl = - abs(nrmxl)
                elif (0.0 < a[l, l]):
                    nrmxl = abs(nrmxl)

                for i in range(l, n):
                    a[i, l] = a[i, l] / nrmxl

                a[l, l] = 1.0 + a[l, l]
#
#  Apply the transformation to the remaining columns, updating the norms.
#
                for j in range(l + 1, p):

                    t = 0.0
                    for i in range(l, n):
                        t = t - a[i, l] * a[i, j]
                    t = t / a[l, l]

                    for i in range(l, n):
                        a[i, j] = a[i, j] + t * a[i, l]

                    if (pl <= j and j <= pu):

                        if (qraux[j] != 0.0):

                            tt = 1.0 - (abs(a[l, j]) / qraux[j]) ** 2
                            tt = max(tt, 0.0)
                            t = tt
                            tt = 1.0 + 0.05 * tt * (qraux[j] / work[j]) ** 2

                            if (tt != 1.0):
                                qraux[j] = qraux[j] * np.sqrt(t)
                            else:
                                t = 0.0
                                for i in range(l + 1, n):
                                    t = t + a[i, j] ** 2
                                qraux[j] = np.sqrt(t)
                                work[j] = qraux[j]
#
#  Save the transformation.
#
                qraux[l] = a[l, l]
                a[l, l] = - nrmxl

    return a, qraux, jpvt


def dqrdc_test():

    # *****************************************************************************80
    #
    # DQRDC_TEST tests DQRDC.
    #
    #  Discussion:
    #
    #    DQRDC computes the QR factorization.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 3
    p = 3
    lda = n

    print('')
    print('DQRDC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DQRDC computes the QR decomposition of a rectangular')
    print('  matrix, but does not return Q and R explicitly.')
    print('')
    print('  Show how Q and R can be recovered using DQRSL.')
#
#  Set the matrix A.
#
    a = np.array([
        [1.0, 1.0, 0.0],
        [1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0]
    ])

    print('')
    print('  The original matrix A:')
    print('')

    for i in range(0, n):
        for j in range(0, p):
            print('  %14.6g' % (a[i, j]), end='')
        print('')
#
#  Decompose the matrix.
#
    print('')
    print('  Decompose the matrix.')

    job = 0
    ipvt = np.zeros(p, dtype=np.int32)

    a, qraux, ipvt = dqrdc(a, lda, n, p, ipvt, job)
#
#  Print out what DQRDC has stored in A...
#
    print('')
    print('  The packed matrix A which describes Q and R:')
    print('')

    for i in range(0, n):
        for j in range(0, p):
            print('  %14.6g' % (a[i, j]), end='')
        print('')
#
#  ...and in QRAUX.
#
    print('')
    print('  The QRAUX vector, containing some additional')
    print('  information defining Q:')
    print('')

    for i in range(0, n):
        print('  %14.6g' % (qraux[i]))
    print('')
#
#  Print out the resulting R factor.
#
    r = np.zeros([n, p])

    print('')
    print('  The R factor:')
    print('')

    for i in range(0, n):
        for j in range(0, p):
            if (i <= j):
                r[i, j] = a[i, j]
            print('  %14.6g' % (r[i, j]), end='')
        print('')
#
#  Call DQRSL to extract the information about the Q matrix.
#  We do this, essentially, by asking DQRSL to tell us the
#  value of Q*Y, where Y is a column of the identity matrix.
#
    q = np.zeros([n, n])

    job = 10000

    for j in range(0, n):
        #
        #  Set the vector Y.
        #
        y = np.zeros(n)

        y[j] = 1.0
#
#  Ask DQRSL to tell us what Q*Y is.
#
        qy, qty, b, rsd, xb, info = dqrsl(a, lda, n, p, qraux, y, job)

        if (info != 0):
            print('  Error!  DQRSL returns INFO = %d' % (info))
            return
#
#  Copy QY into the appropriate column of Q.
#
        for i in range(0, n):
            q[i, j] = qy[i]
#
#  Now print out the Q matrix we have extracted.
#
    print('')
    print('  The Q factor:')
    print('')

    for i in range(0, n):
        for j in range(0, n):
            print('  %14.6g' % (q[i, j]), end='')
        print('')
#
#  Compute Q*R to verify that it equals A.
#
    b = np.dot(q, r)
#
#  Print the result.
#
    print('')
    print('  The product Q * R:')
    print('')

    for i in range(0, n):
        for j in range(0, p):
            print('  %14.6g' % (b[i, j]), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('DQRDC_TEST')
    print('  Normal end of execution.')
    return


def dqrsl(a, lda, n, k, qraux, y, job):

    # *****************************************************************************80
    #
    # DQRSL computes transformations, projections, and least squares solutions.
    #
    #  Discussion:
    #
    #    DQRSL requires the output of DQRDC.
    #
    #    For K <= min(N,P), let AK be the matrix
    #
    #      AK = ( A(JPVT(1)), A(JPVT(2)), ..., A(JPVT(K)) )
    #
    #    formed from columns JPVT(1), ..., JPVT(K) of the original
    #    N by P matrix A that was input to DQRDC.  If no pivoting was
    #    done, AK consists of the first K columns of A in their
    #    original order.  DQRDC produces a factored orthogonal matrix Q
    #    and an upper triangular matrix R such that
    #
    #      AK = Q * (R)
    #               (0)
    #
    #    This information is contained in coded form in the arrays
    #    A and QRAUX.
    #
    #    The parameters QY, QTY, B, RSD, and AB are not referenced
    #    if their computation is not requested and in this case
    #    can be replaced by dummy variables in the calling program.
    #    To save storage, the user may in some cases use the same
    #    array for different parameters in the calling sequence.  A
    #    frequently occuring example is when one wishes to compute
    #    any of B, RSD, or AB and does not need Y or QTY.  In this
    #    case one may identify Y, QTY, and one of B, RSD, or AB, while
    #    providing separate arrays for anything else that is to be
    #    computed.
    #
    #    Thus the calling sequence
    #
    #      call dqrsl ( a, lda, n, k, qraux, y, dum, y, b, y, dum, 110, info )
    #
    #    will result in the computation of B and RSD, with RSD
    #    overwriting Y.  More generally, each item in the following
    #    list contains groups of permissible identifications for
    #    a single calling sequence.
    #
    #      1. (Y,QTY,B) (RSD) (AB) (QY)
    #
    #      2. (Y,QTY,RSD) (B) (AB) (QY)
    #
    #      3. (Y,QTY,AB) (B) (RSD) (QY)
    #
    #      4. (Y,QY) (QTY,B) (RSD) (AB)
    #
    #      5. (Y,QY) (QTY,RSD) (B) (AB)
    #
    #      6. (Y,QY) (QTY,AB) (B) (RSD)
    #
    #    In any group the value returned in the array allocated to
    #    the group corresponds to the last member of the group.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2016
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Moler, Bunch, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, (Society for Industrial and Applied Mathematics),
    #    3600 University City Science Center,
    #    Philadelphia, PA, 19104-2688.
    #    ISBN 0-89871-172-X
    #
    #  Parameters:
    #
    #    Input, real A(LDA,P), contains the output of DQRDC.
    #
    #    Input, integer LDA, the leading dimension of the array A.
    #
    #    Input, integer N, the number of rows of the matrix AK.  It must
    #    have the same value as N in DQRDC.
    #
    #    Input, integer K, the number of columns of the matrix AK.  K
    #    must not be greater than min(N,P), where P is the same as in the
    #    calling sequence to DQRDC.
    #
    #    Input, real QRAUX(P), the auxiliary output from DQRDC.
    #
    #    Input, real Y(N), a vector to be manipulated by DQRSL.
    #
    #    Input, integer JOB, specifies what is to be computed.  JOB has
    #    the decimal expansion ABCDE, with the following meaning:
    #      if A /= 0, compute QY.
    #      if B /= 0, compute QTY.
    #      if C /= 0, compute QTY and B.
    #      if D /= 0, compute QTY and RSD.
    #      if E /= 0, compute QTY and AB.
    #    Note that a request to compute B, RSD, or AB automatically triggers
    #    the computation of QTY, for which an array must be provided in the
    #    calling sequence.
    #
    #    Output, real QY(N), contains Q * Y, if requested.
    #
    #    Output, real QTY(N), contains Q' * Y, if requested.
    #
    #    Output, real B(K), the solution of the least squares problem
    #      minimize norm2 ( Y - AK * B),
    #    if its computation has been requested.  Note that if pivoting was
    #    requested in DQRDC, the J-th component of B will be associated with
    #    column JPVT(J) of the original matrix A that was input into DQRDC.
    #
    #    Output, real RSD(N), the least squares residual Y - AK * B,
    #    if its computation has been requested.  RSD is also the orthogonal
    #    projection of Y onto the orthogonal complement of the column space
    #    of AK.
    #
    #    Output, real AB(N), the least squares approximation Ak * B,
    #    if its computation has been requested.  AB is also the orthogonal
    #    projection of Y onto the column space of A.
    #
    #    Output, integer INFO, is zero unless the computation of B has
    #    been requested and R is exactly singular.  In this case, INFO is the
    #    index of the first zero diagonal element of R, and B is left unaltered.
    #
    import numpy as np

    qy = np.zeros(n)
    qty = np.zeros(n)
    b = np.zeros(k)
    rsd = np.zeros(n)
    ab = np.zeros(n)
#
#  Set info flag.
#
    info = 0
#
#  Determine what is to be computed.
#
    cqy = int(job / 10000) != 0
    cqty = (job % 10000) != 0
    cb = int((job % 1000) / 100) != 0
    cr = int((job % 100) / 10) != 0
    cab = (job % 10) != 0

    ju = min(k, n - 1)
#
#  Special action when N = 1.
#
    if (ju == 0):

        qy[0] = y[0]
        qty[0] = y[0]
        ab[0] = y[0]

        if (a[0, 0] == 0.0):
            info = 1
        else:
            b[0] = y[0] / a[0]

        rsd[0] = 0.0

        return qy, qty, b, rsd, ab, info
#
#  Set up to compute QY or QTY.
#
    for i in range(0, n):
        qy[i] = y[i]
        qty[i] = y[i]
#
#  Compute QY.
#
    if (cqy):

        for j in range(ju - 1, -1, -1):

            if (qraux[j] != 0.0):
                ajj = a[j, j]
                a[j, j] = qraux[j]
                t = 0.0
                for i in range(j, n):
                    t = t - a[i, j] * qy[i]
                t = t / a[j, j]
                for i in range(j, n):
                    qy[i] = qy[i] + t * a[i, j]
                a[j, j] = ajj
#
#  Compute Q'*Y.
#
    if (cqty):

        for j in range(0, ju):
            if (qraux[j] != 0.0):
                ajj = a[j, j]
                a[j, j] = qraux[j]
                t = 0.0
                for i in range(j, n):
                    t = t - a[i, j] * qty[i]
                t = t / a[j, j]
                for i in range(j, n):
                    qty[i] = qty[i] + t * a[i, j]
                a[j, j] = ajj
#
#  Set up to compute B, RSD, or AB.
#
    for i in range(0, k):
        b[i] = qty[i]
        ab[i] = qty[i]

    for i in range(k, n):
        rsd[i] = qty[i]
#
#  Compute B.
#
    if (cb):

        for j in range(k - 1, -1, -1):

            if (a[j, j] == 0.0):
                info = j + 1
                break

            b[j] = b[j] / a[j, j]

            if (0 < j):
                t = - b[j]
                for i in range(0, j):
                    b[i] = b[i] + t * a[i, j]
#
#  Compute RSD or AB as required.
#
    if (cr or cab):

        for j in range(ju - 1, -1, -1):

            if (qraux[j] != 0.0):

                ajj = a[j, j]
                a[j, j] = qraux[j]

                if (cr):
                    t = 0.0
                    for i in range(j, n):
                        t = t - a[i, j] * rsd[i]
                    t = t / a[j, j]
                    for i in range(j, n):
                        rsd[i] = rsd[i] + t * a[i, j]

                if (cab):
                    t = 0.0
                    for i in range(j, n):
                        t = t - a[i, j] * ab[i]
                    t = t / a[j, j]
                    for i in range(j, n):
                        ab[i] = ab[i] + t * a[i, j]

                a[j, j] = ajj

    return qy, qty, b, rsd, ab, info


def dqrsl_test():

    # *****************************************************************************80
    #
    # DQRSL_TEST tests DQRSL.
    #
    #  Discussion:
    #
    #    DQRSL can solve a linear system that was factored by DQRDC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 5
    p = 3
    lda = n

    print('')
    print('DQRSL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DQRSL solves a rectangular linear system A*x=b in the')
    print('  least squares sense after A has been factored by DQRDC.')
#
#  Set the matrix A.
#
    a = np.array([
        [1.0, 1.0, 1.0],
        [1.0, 2.0, 4.0],
        [1.0, 3.0, 9.0],
        [1.0, 4.0, 16.0],
        [1.0, 5.0, 25.0]
    ])

    print('')
    print('  The matrix A:')
    print('')

    for i in range(0, n):
        for j in range(0, p):
            print('  %14.6g' % (a[i, j]), end='')
        print('')
#
#  Decompose the matrix.
#
    print('')
    print('  Decompose the matrix.')

    job = 0
    ipvt = np.zeros(n, dtype=np.int32)

    a, qraux, ipvt = dqrdc(a, lda, n, p, ipvt, job)
#
#  Call DQRSL to compute the least squares solution A*x=b.
#
    job = 110

    y = np.array([
        1.0,
        2.3,
        4.6,
        3.1,
        1.2
    ])

    b2 = np.array([
        -3.02,
        4.4914286,
        -0.72857143
    ])

    qy, qty, b, r, xb, info = dqrsl(a, lda, n, p, qraux, y, job)

    if (info != 0):
        print('')
        print('DQRSL_TEST - Warning!')
        print('  DQRSL returns INFO = %d' % (info))
        return

    print('')
    print('      X          X(expected):')
    print('')

    for i in range(0, p):
        print('  %14.6g  %14.6g' % (b[i], b2[i]))
#
#  Terminate.
#
    print('')
    print('DQRSL_TEST')
    print('  Normal end of execution.')
    return


def drotg(a, b):

    # *****************************************************************************80
    #
    # DROTG constructs a Givens plane rotation.
    #
    #  Discussion:
    #
    #    Given values A and B, this routine computes
    #
    #    SIGMA = sign ( A ) if abs ( A ) >  abs ( B )
    #          = sign ( B ) if abs ( A ) <= abs ( B )
    #
    #    R     = SIGMA * ( A * A + B * B )
    #
    #    C = A / R if R is not 0
    #      = 1     if R is 0
    #
    #    S = B / R if R is not 0,
    #        0     if R is 0.
    #
    #    The computed numbers then satisfy the equation
    #
    #    (  C  S ) ( A ) = ( R )
    #    ( -S  C ) ( B ) = ( 0 )
    #
    #    The routine also computes
    #
    #    Z = S     if abs ( A ) > abs ( B, end = '' )
    #      = 1 / C if abs ( A ) <= abs ( B ) and C is not 0,
    #      = 1     if C is 0.
    #
    #    The single value Z encodes C and S, and hence the rotation:
    #
    #    If Z = 1, set C = 0 and S = 1
    #    If abs ( Z ) < 1, set C = sqrt ( 1 - Z * Z ) and S = Z
    #    if abs ( Z ) > 1, set C = 1/ Z and S = sqrt ( 1 - C * C )
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
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
    #    Basic Linear Algebra Subprograms for Fortran Usage,
    #    Algorithm 539,
    #    ACM Transactions on Mathematical Software,
    #    Volume 5, Number 3, September 1979, pages 308-323.
    #
    #  Parameters:
    #
    #    Input, real A, B, the values A and B.
    #
    #    Output, real C, S, the cosine and sine of the Givens rotation.
    #
    #    Output, real R, Z, the values R and Z.
    #
    import numpy as np

    if (abs(b) < abs(a)):
        roe = a
    else:
        roe = b

    scale = abs(a) + abs(b)

    if (scale == 0.0):
        c = 1.0
        s = 0.0
        r = 0.0
    else:
        r = scale * np.sqrt((a / scale) ** 2 + (b / scale) ** 2)
        if (roe < 0.0):
            r = - r
        c = a / r
        s = b / r

    if (0.0 < abs(c) and abs(c) <= s):
        z = 1.0 / c
    else:
        z = s

    return c, s, r, z


def drotg_test():

    # *****************************************************************************80
    #
    # DROTG_TEST tests DROTG.
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
    import platform

    test_num = 5

    print('')
    print('DROTG_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DROTG generates a real Givens rotation')
    print('    (  C  S ) * ( A ) = ( R )')
    print('    ( -S  C )   ( B )   ( 0 )')
    print('')

    seed = 123456789

    for test in range(0, test_num):

        a, seed = r8_uniform_01(seed)
        b, seed = r8_uniform_01(seed)

        c, s, r, z = drotg(a, b)

        print('')
        print('  A =  %g  B =  %g' % (a, b))
        print('  C =  %g  S =  %g' % (c, s))
        print('  R =  %g  Z =  %g' % (r, z))
        print('   C*A+S*B = %g' % (c * a + s * b))
        print('  -S*A+C*B = %g' % (-s * a + c * b))
#
#  Terminate.
#
    print('')
    print('DROTG_TEST')
    print('  Normal end of execution.')
    return


def drot(n, x, incx, y, incy, c, s):

    # *****************************************************************************80
    #
    # DROT applies a plane rotation.
    #
    #  Discussion:
    #
    #    Note that the FORTRAN version of this function allowed users to pass in
    #    X and Y data that was noncontiguous, (such as rows of a FORTRAN matrix).
    #    The rotated data overwrote the input data, and so it might therefore
    #    also be noncontiguous.
    #
    #    This function does not assume that the output overwrites the input,
    #    and treats the output vectors as new items of length exactly N.
    #
    #    Note, moreover, that Python does NOT allow a matrix to be treated as a
    #    vector in quite the simple way that FORTRAN does.
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
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
    #    Basic Linear Algebra Subprograms for Fortran Usage,
    #    Algorithm 539,
    #    ACM Transactions on Mathematical Software,
    #    Volume 5, Number 3, September 1979, pages 308-323.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vectors.
    #
    #    Input, real X(INCX*N), one of the vectors to be rotated.
    #
    #    Input, integer INCX, the increment between successive entries of X.
    #
    #    Input, real Y(INCX*N), one of the vectors to be rotated.
    #
    #    Input, integer INCY, the increment between successive elements of Y.
    #
    #    Input, real C, S, parameters (presumably the cosine and
    #    sine of some angle) that define a plane rotation.
    #
    #    Output, real XR(N), the rotated vector.
    #
    #    Output, real YR(N), the rotated vector.
    #
    import numpy as np

    xr = np.zeros(n)
    yr = np.zeros(n)

    if (n <= 0):

        pass

    elif (incx == 1 and incy == 1):

        xr[0:n] = c * x[0:n] + s * y[0:n]
        yr[0:n] = c * y[0:n] - s * x[0:n]

    else:

        if (0 <= incx):
            ix = 0
        else:
            ix = (- n + 1) * incx

        if (0 <= incy):
            iy = 0
        else:
            iy = (- n + 1) * incy

        for i in range(0, n):
            xr[ix] = c * x[ix] + s * y[iy]
            yr[iy] = c * y[iy] - s * x[ix]
            ix = ix + incx
            iy = iy + incy

    return xr, yr


def drot_test():

    # *****************************************************************************80
    #
    # DROT_TEST tests DROT.
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
    import numpy as np
    import platform

    n = 6
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(0, n):
        x[i] = float(i + 1)
        y[i] = x[i] * x[i] - 12.0

    print('')
    print('DROT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DROT carries out a Givens rotation.')
    print('')
    print('  Vectors X and Y')
    print('')
    for i in range(0, n):
        print('  %6d  %14.6g  %14.6g' % (i, x[i], y[i]))

    c = 0.5
    s = np.sqrt(1.0 - c * c)
    xr, yr = drot(n, x, 1, y, 1, c, s)
    print('')
    print('  xr, yr = drot ( n, x, 1, y, 1, %g, %g )' % (c, s))
    print('')
    print('  Rotated vectors XR and YR')
    print('')
    for i in range(0, n):
        print('  %6d  %14.6g  %14.6g' % (i, xr[i], yr[i]))

    t = np.arctan2(y[0], x[0])
    c = np.cos(t)
    s = np.sin(t)
    xr, yr = drot(n, x, 1, y, 1, c, s)
    print('')
    print('  xr, yr = drot ( n, x, 1, y, 1, %g, %g )' % (c, s))
    print('')
    print('  Rotated vectors XR and YR')
    print('')
    for i in range(0, n):
        print('  %6d  %14.6g  %14.6g' % (i, xr[i], yr[i]))
#
#  Terminate.
#
    print('')
    print('DROT_TEST')
    print('  Normal end of execution.')
    return


def dsvdc(a, lda, m, n, ldu, ldv, job):

    # *****************************************************************************80
    #
    # DSVDC computes the singular value decomposition of a real rectangular matrix.
    #
    #  Discussion:
    #
    #    This routine reduces an M by N matrix A to diagonal form by orthogonal
    #    transformations U and V.  The diagonal elements S(I) are the singular
    #    values of A.  The columns of U are the corresponding left singular
    #    vectors, and the columns of V the right singular vectors.
    #
    #    The form of the singular value decomposition is then
    #
    #      A(MxN) = U(MxM) * S(MxN) * V(NxN)'
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2016
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Moler, Bunch and Stewart,
    #    LINPACK User's Guide,
    #    SIAM, (Society for Industrial and Applied Mathematics),
    #    3600 University City Science Center,
    #    Philadelphia, PA, 19104-2688.
    #    ISBN 0-89871-172-X
    #
    #  Parameters:
    #
    #    Input, real A(LDA,N), the M by N matrix whose singular
    #    value decomposition is to be computed.
    #
    #    Input, integer LDA, the leading dimension of the array A.
    #    LDA must be at least N.
    #
    #    Input, integer M, the number of rows of the matrix.
    #
    #    Input, integer N, the number of columns of the matrix A.
    #
    #    Input, integer LDU, the leading dimension of the array U.
    #    LDU must be at least M.
    #
    #    Input, integer LDV, the leading dimension of the array V.
    #    LDV must be at least N.
    #
    #    Input, integer JOB, controls the computation of the singular
    #    vectors.  It has the decimal expansion AB with the following meaning:
    #      A =  0, for not compute the left singular vectors.
    #      A =  1, return the M left singular vectors in U.
    #      A >= 2, return the first min(M,N) singular vectors in U.
    #      B =  0, for not compute the right singular vectors.
    #      B =  1, return the right singular vectors in V.
    #
    #    Output, real A(LDA,N), the matrix has been destroyed.  Depending on the
    #    user's requests, the matrix may contain other useful information.
    #
    #    Output, real S(MM), where MM = max(M+1,N).  The first
    #    min(M,N) entries of S contain the singular values of A arranged in
    #    descending order of magnitude.
    #
    #    Output, real E(MM), where MM = max(M+1,N), ordinarily contains zeros.
    #    However see the discussion of INFO for exceptions.
    #
    #    Output, real U(LDU,K).  If JOBA = 1 then K = M
    #    if 2 <= JOBA, then K = min(M,N).  U contains the M by M matrix of
    #    left singular vectors.  U is not referenced if JOBA = 0.  If M <= N
    #    or if JOBA = 2, then U may be identified with A in the subroutine call.
    #
    #    Output, real V(LDV,N), the N by N matrix of right singular
    #    vectors.  V is not referenced if JOB is 0.  If N <= M, then V may be
    #    identified with A in the subroutine call.
    #
    #    Output, integer INFO, status indicator.
    #    The singular values (and their corresponding singular vectors)
    #    S(INFO+1), S(INFO+2),...,S(MN) are correct.  Here MN = min ( M, N ).
    #    Thus if INFO is 0, all the singular values and their vectors are
    #    correct.  In any event, the matrix B = U' * A * V is the bidiagonal
    #    matrix with the elements of S on its diagonal and the elements of E on
    #    its superdiagonal.  Thus the singular values of A and B are the same.
    #
    import numpy as np

    maxit = 30
    mm = max(m + 1, n)

    s = np.zeros(mm)
    e = np.zeros(mm)
    joba = (job // 10)
    if (joba == 1):
        u = np.zeros([ldu, m])
    elif (1 <= joba):
        u = np.zeros([ldu, min(m, n)])
    v = np.zeros([ldv, n])
    work = np.zeros(m)

    info = 0
#
#  Determine what is to be computed.
#
    wantu = 0
    wantv = 0
    jobu = int((job % 100) / 10)

    if (1 < jobu):
        ncu = min(m, n)
    else:
        ncu = m

    if (jobu != 0):
        wantu = 1

    if ((job % 10) != 0):
        wantv = 1
#
#  Reduce A to bidiagonal form, storing the diagonal elements
#  in S and the super-diagonal elements in E.
#
    info = 0
    nct = min(m - 1, n)
    nrt = max(0, min(m, n - 2))
    lu = max(nct, nrt)

    for l in range(0, lu):
        #
        #  Compute the transformation for the L-th column and
        #  place the L-th diagonal in S(L).
        #
        if (l <= nct - 1):

            t = 0.0
            for i in range(l, m):
                t = t + a[i, l] ** 2
            t = np.sqrt(t)
            s[l] = t

            if (s[l] != 0.0):
                if (a[l, l] < 0.0):
                    s[l] = - s[l]
                for i in range(l, m):
                    a[i, l] = a[i, l] / s[l]
                a[l, l] = 1.0 + a[l, l]

            s[l] = - s[l]

        for j in range(l + 1, n):
            #
            #  Apply the transformation.
            #
            if (l <= nct - 1 and s[l] != 0.0):
                t = 0.0
                for i in range(l, m):
                    t = t - a[i, l] * a[i, j]
                t = t / a[l, l]
                for i in range(l, m):
                    a[i, j] = a[i, j] + t * a[i, l]
#
#  Place the L-th row of A into E for the
#  subsequent calculation of the row transformation.
#
            e[j] = a[l, j]
#
#  Place the transformation in U for subsequent back multiplication.
#
        if (wantu and l <= nct - 1):
            for i in range(l, m):
                u[i, l] = a[i, l]
#
#  Compute the L-th row transformation and place the
#  L-th superdiagonal in E(L).
#
        if (l <= nrt - 1):

            t = 0.0
            for i in range(l + 1, n):
                t = t + e[i] ** 2
            e[l] = np.sqrt(t)
            if (e[l] != 0.0):
                if (e[l + 1] < 0.0):
                    e[l] = - e[l]
                e[l + 1:n] = e[l + 1:n] / e[l]
                e[l + 1] = 1.0 + e[l + 1]
            e[l] = - e[l]
#
#  Apply the transformation.
#
            if (l + 1 <= m - 1 and e[l] != 0.0):

                work[l + 1:m] = 0.0

                for j in range(l + 1, n):
                    for i in range(l + 1, m):
                        work[i] = work[i] + e[j] * a[i, j]

                for j in range(l + 1, n):
                    for i in range(l + 1, m):
                        a[i, j] = a[i, j] - e[j] / e[l + 1] * work[i]
#
#  Place the transformation in V for subsequent back multiplication.
#
            if (wantv):
                v[l + 1:n, l] = e[l + 1:n]
#
#  Set up the final bidiagonal matrix of order MN.
#
    mn = min(m + 1, n)
    nctp1 = nct + 1
    nrtp1 = nrt + 1

    if (nct < n):
        s[nctp1 - 1] = a[nctp1 - 1, nctp1 - 1]

    if (m < mn):
        s[mn - 1] = 0.0

    if (nrtp1 < mn):
        e[nrtp1 - 1] = a[nrtp1 - 1, mn - 1]

    e[mn - 1] = 0.0
#
#  If required, generate U.
#
    if (wantu):

        for j in range(nctp1 - 1, ncu):
            for i in range(0, m):
                u[i, j] = 0.0

        for j in range(nctp1 - 1, ncu):
            u[j, j] = 1.0

        for l in range(nct - 1, -1, -1):

            if (s[l] != 0.0):

                for j in range(l + 1, ncu):
                    t = 0.0
                    for i in range(l, m):
                        t = t - u[i, l] * u[i, j]
                    t = t / u[l, l]
                    for i in range(l, m):
                        u[i, j] = u[i, j] + t * u[i, l]

                for i in range(0, l):
                    u[i, l] = 0.0
                for i in range(l, m):
                    u[i, l] = - u[i, l]
                u[l, l] = 1.0 + u[l, l]

            else:

                for i in range(0, m):
                    u[i, l] = 0.0
                u[l, l] = 1.0
#
#  If it is required, generate V.
#
    if (wantv):

        for l in range(n - 1, -1, -1):

            if (l <= nrt - 1 and e[l] != 0.0):

                for j in range(l + 1, n):
                    t = 0.0
                    for i in range(l + 1, n):
                        t = t - v[i, l] * v[i, j]
                    t = t / v[l + 1, l]
                    for i in range(l + 1, n):
                        v[i, j] = v[i, j] + t * v[i, l]

            for i in range(0, n):
                v[i, l] = 0.0
            v[l, l] = 1.0
#
#  Main iteration loop for the singular values.
#
    mm = mn
    iter = 0

    while (0 < mn):
        #
        #  If too many iterations have been performed, set flag and return.
        #
        if (maxit <= iter):
            print('')
            print('DSVDC - Warning!')
            print('  MAXIT = %d <= ITER = %d' % (maxit, iter))
            info = mn
            return a, s, e, u, v, info
#
#  This section of the program inspects for
#  negligible elements in the S and E arrays.
#
#  On completion the variables KASE and L are set as follows:
#
#  KASE = 1     if S(MN) and E(L-1) are negligible and L < MN
#  KASE = 2     if S(L) is negligible and L < MN
#  KASE = 3     if E(L-1) is negligible, L < MN, and
#               S(L), ..., S(MN) are not negligible (QR step).
#  KASE = 4     if E(MN-1) is negligible (convergence).
#
        for l in range(mn - 2, -2, -1):

            if (l == -1):
                break

            test = abs(s[l]) + abs(s[l + 1])
            ztest = test + abs(e[l])

            if (ztest == test):
                e[l] = 0.0
                break

        if (l == mn - 2):

            kase = 4

        else:

            for ls in range(mn - 1, l - 1, -1):

                if (ls == l):
                    break

                test = 0.0
                if (ls != mn - 1):
                    test = test + abs(e[ls])

                if (ls != l + 1):
                    test = test + abs(e[ls - 1])

                ztest = test + abs(s[ls])

                if (ztest == test):
                    s[ls] = 0.0
                    break

            if (ls == l):
                kase = 3
            elif (ls == mn - 1):
                kase = 1
            else:
                kase = 2
                l = ls

        l = l + 1
#
#  Deflate negligible S(MN).
#
        if (kase == 1):

            mm1 = mn - 1
            f = e[mn - 2]
            e[mn - 2] = 0.0

            for k in range(mm1 - 1, l - 1, -1):

                t1 = s[k]
                cs, sn, t1, f = drotg(t1, f)
                s[k] = t1

                if (k != l):
                    f = - sn * e[k - 1]
                    e[k - 1] = cs * e[k - 1]

                if (wantv):
                    v1, v2 = drot(n, v[0:n, k], 1, v[0:n, mn - 1], 1, cs, sn)
                    for i in range(0, n):
                        v[i, k] = v1[i]
                        v[i, mn - 1] = v2[i]
#
#  Split at negligible S(L).
#
        elif (kase == 2):

            f = e[l - 1]
            e[l - 1] = 0.0

            for k in range(l, mn):

                t1 = s[k]
                cs, sn, t1, f = drotg(t1, f)
                s[k] = t1
                f = - sn * e[k]
                e[k] = cs * e[k]
                if (wantu):
                    u1, u2 = drot(m, u[0:m, k], 1, u[0:m, l - 1], 1, cs, sn)
                    for i in range(0, m):
                        u[i, k] = u1[i]
                        u[i, l - 1] = u2[i]
#
#  Perform one QR step.
#
        elif (kase == 3):
            #
            #  Calculate the shift.
            #
            scale = max(abs(s[mn - 1]),
                        max(abs(s[mn - 2]),
                            max(abs(e[mn - 2]),
                                max(abs(s[l]),
                                    abs(e[l])))))

            sm = s[mn - 1] / scale
            smm1 = s[mn - 2] / scale
            emm1 = e[mn - 2] / scale
            sl = s[l] / scale
            el = e[l] / scale
            b = ((smm1 + sm) * (smm1 - sm) + emm1 * emm1) / 2.0
            c = sm * sm * emm1 * emm1
            shift = 0.0

            if (b != 0.0 or c != 0.0):
                shift = np.sqrt(b * b + c)
                if (b < 0.0):
                    shift = - shift
                shift = c / (b + shift)

            f = (sl + sm) * (sl - sm) - shift
            g = sl * el
#
#  Chase zeros.
#
            mm1 = mn - 1

            for k in range(l, mm1):

                cs, sn, f, g = drotg(f, g)

                if (k != l):
                    e[k - 1] = f

                f = cs * s[k] + sn * e[k]
                e[k] = cs * e[k] - sn * s[k]
                g = sn * s[k + 1]
                s[k + 1] = cs * s[k + 1]

                if (wantv):
                    v1, v2 = drot(n, v[0:n, k], 1, v[0:n, k + 1], 1, cs, sn)
                    for i in range(0, n):
                        v[i, k] = v1[i]
                        v[i, k + 1] = v2[i]

                cs, sn, f, g = drotg(f, g)
                s[k] = f
                f = cs * e[k] + sn * s[k + 1]
                s[k + 1] = - sn * e[k] + cs * s[k + 1]
                g = sn * e[k + 1]
                e[k + 1] = cs * e[k + 1]

                if (wantu and k < m):
                    u1, u2 = drot(m, u[0:m, k], 1, u[0:m, k + 1], 1, cs, sn)
                    for i in range(0, m):
                        u[i, k] = u1[i]
                        u[i, k + 1] = u2[i]

            e[mn - 2] = f

            iter = iter + 1
#
#  Convergence.
#
        elif (kase == 4):
            #
            #  Make the singular value nonnegative.
            #
            if (s[l] < 0.0):
                s[l] = - s[l]
                if (wantv):
                    for i in range(0, n):
                        v[i, l] = - v[i, l]
#
#  Order the singular values.
#
            while (True):

                if (l + 1 == mm):
                    break

                if (s[l + 1] <= s[l]):
                    break

                t = s[l]
                s[l] = s[l + 1]
                s[l + 1] = t

                if (wantv and l < n - 1):
                    for i in range(0, n):
                        t = v[i, l]
                        v[i, l] = v[i, l + 1]
                        v[i, l + 1] = t

                if (wantu and l < m - 1):
                    for i in range(0, m):
                        t = u[i, l]
                        u[i, l] = u[i, l + 1]
                        u[i, l + 1] = t

                l = l + 1

            iter = 0
            mn = mn - 1

    return a, s, e, u, v, info


def dsvdc_test():

    # *****************************************************************************80
    #
    # DSVDC_TEST tests DSVDC.
    #
    #  Discussion:
    #
    #    DSVDC computes the singular value decomposition:
    #
    #      A = U * S * V'
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    m = 6
    n = 4

    print('')
    print('DSVDC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DSVDC computes the singular value decomposition')
    print('  for an MxN matrix A in general storage.')
    print('    A = U * S * V\'')
    print('')
    print('  Matrix rows M =    %d' % (m))
    print('  Matrix columns N = %d' % (n))
#
#  Set A.
#
    seed = 123456789

    a, seed = r8mat_uniform_01(m, n, seed)

    r8mat_print(m, n, a, '  The matrix A:')
#
#  Decompose the matrix.
#
    print('')
    print('  Decompose the matrix.')

    job = 11
    lda = m
    ldu = m
    ldv = n

    a, s, e, u, v, info = dsvdc(a, lda, m, n, ldu, ldv, job)

    if (info != 0):
        print('')
        print('DSVDC_TEST - Warning:')
        print('  DSVDC returned nonzero INFO = %d' % (info))
#   return

    r8vec_print(min(m, n), s, '  Singular values S:')

    r8mat_print(m, m, u, '  Left Singular Vector Matrix U:')

    r8mat_print(n, n, v, '  Right Singular Vector Matrix V:')

    sigma = np.zeros([m, n])

    for i in range(0, min(m, n)):
        sigma[i, i] = s[i]

    usv = np.dot(u, np.dot(sigma, v.transpose()))

    r8mat_print(m, n, usv, '  The product U * S * V\' (should equal A):')
#
#  Terminate.
#
    print('')
    print('DSVDC_TEST')
    print('  Normal end of execution.')
    return


def linpack_d_test():

    # *****************************************************************************80
    #
    # LINPACK_D_TEST tests the LINPACK_D library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LINPACK_D_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the LINPACK_D library.')

    dpofa_test()
    dqrdc_test()
    dqrsl_test()
    dsvdc_test()
#
#  Terminate.
#
    print('')
    print('LINPACK_D_TEST')
    print('  Normal end of execution.')
    return


def r8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT prints an R8MAT.
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
    r8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_print_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_TEST tests R8MAT_PRINT.
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

    print('')
    print('R8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT prints an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print(m, n, v, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME prints out a portion of an R8MAT.
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

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def r8mat_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
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

    print('')
    print('R8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT_SOME prints some of an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


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

    r8mat_print(m, n, v, '  Random R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_UNIFORM_01_TEST:')
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


if (__name__ == '__main__'):
    timestamp()
    linpack_d_test()
    timestamp()
