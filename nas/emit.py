#! /usr/bin/env python3
#


def emit(nb, nvm, nw, dpds, force, gamma2, nwall, refpt, rmatrx,
         rmom, wall, z, zcr):

    # *****************************************************************************80
    #
    # EMIT creates new vortices according to certain boundary conditions.
    #
    #  Discussion:
    #
    #    This function was extracted from a vortex method program.
    #    It emits new vortices to satisfy the boundary condition.
    #    It also finishes computing pressure, forces, and other quantities.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np

    rhs = np.zeros([nw * nb], dtype=np.float64)

    period = 3.0
    sig2 = 3.0
    u0 = 4.0
    matdim = 500
    delt = 1.0
    chord = 5.0
    uupstr = 3.0 + 1j * 4.0
#
#  Store exp(z(i)) and exp(-z(i)) to reduce work in inner loop.
#
#  Note that the NV used here is a variable, whereas the NV in the
#  calling program is a constant.  They are separate quantities.
#
    nv = 1000
    pidp = np.pi / period

    expz = np.zeros(nvm, dtype=np.complex128)
    expmz = np.zeros(nvm, dtype=np.complex128)

    for i in range(1, nv + 1):
        expz[i - 1] = np.exp(z[i - 1] * pidp)
        expmz[i - 1] = 1.0 / expz[i - 1]

    i0 = 0
    cupst = (uupstr.real) ** 2 + (uupstr.imag) ** 2

    ps = np.zeros(nvm, dtype=np.float64)
    psi = np.zeros(nw, dtype=np.float64)

    for l in range(1, nb + 1):

        for k in range(1, nwall[l - 1] + 1):

            expwkl = np.exp(wall[k - 1, l - 1] * pidp)
            expmwk = 1.0 / expwkl

            sps = 0.0
            for i in range(1, nv + 1):
                dum3 = expz[i - 1] * expmwk - expwkl * expmz[i - 1]
                ps[i - 1] = gamma2[i - 1] * \
                    np.log((dum3.real) ** 2 + (dum3.imag) ** 2 + sig2)
                sps = sps + ps[i - 1]

            value = uupstr + 1j * u0
            value = wall[k - 1, l - 1] * value.conjugate()
            psi[k - 1] = value.imag - sps * 0.25 / np.pi
#
#  Compute the right-hand side.
#
        for k in range(1, nwall[l - 1] + 1):
            rhs[i0 + k - 1] = psi[k - 1] - psi[0]

        i0 = i0 + nwall[l - 1]
#
#  Solve the system.
#
    for i in range(1, matdim + 1):
        for j in range(i + 1, matdim + 1):
            rhs[j - 1] = rhs[j - 1] - rmatrx[j - 1, i - 1] * rhs[i - 1]

    for i in range(matdim, 0, -1):
        rhs[i - 1] = rmatrx[i - 1, i - 1] * rhs[i - 1]
        for j in range(1, i):
            rhs[j - 1] = rhs[j - 1] - rmatrx[j - 1, i - 1] * rhs[i - 1]
#
#  Create new vortices.
#
    nolld = nv
    i0 = 0

    cp = np.zeros([nw, nb], dtype=np.float64)

    for l in range(1, nb + 1):

        for k in range(1, nwall[l - 1] + 1):
            #
            #  Put the new vortex at the end of the array.
            #
            nv = nv + 1
            z[nv - 1] = zcr[k - 1, l - 1]
            gamma2[nv - 1] = rhs[i0 + k - 1]
#
#  Record the gain of linear and angular momentum.
#
            force[l - 1] = force[l - 1] + gamma2[nv - 1] * z[nv - 1]

            value = z[nv - 1] - refpt[l - 1]

            rmom[l - 1] = rmom[l - 1] + gamma2[nv - 1] * \
                (value.real ** 2 + value.imag ** 2)

            dpds[k - 1, l - 1] = dpds[k - 1, l - 1] - gamma2[nv - 1]
#
#  Filter and integrate pressure gradient to get pressure.
#
        cp[0, l - 1] = 0.0
        cpm = -1.0E+30

        for k in range(2, nwall[l - 1] + 1):
            cp[k - 1, l - 1] = cp[k - 2, l - 1] + (3.0 * (dpds[k - 1, l - 1] + dpds[k - 2, l - 1])
                                                   + dpds[k %
                                                          nwall[l - 1], l - 1]
                                                   + dpds[(k + nwall[l - 1] - 3) % nwall[l - 1], l - 1]) / (4.0 * delt * cupst)
            cpm = max(cpm, cp[k - 1, l - 1])
#
#  Normalize the pressure.
#
        for k in range(1, nwall[l - 1] + 1):
            cp[k - 1, l - 1] = cp[k - 1, l - 1] - cpm
#
#  Finish computing force and moment, as time rate of change of linear
#  and angular momentum.
#
        force[l - 1] = force[l - 1] * 2.0 * 1j / (delt * chord * cupst)

        rmom[l - 1] = rmom[l - 1] * 2.0 / (delt * chord ** 2 * cupst)

        i0 = i0 + nwall[l - 1]

    return rhs


def emit_test():

    # *****************************************************************************80
    #
    # EMIT_TEST tests EMIT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np
    from time import clock

    nb = 5
    nv = 1000
    nvm = 1500
    nw = 100

    it = 10
    ans = 6.0088546832072
#
#  Random initialization.
#
    f7 = 78125.0
    t30 = 1073741824.0
    t2 = f7 / t30

    dpds = np.zeros([nw, nb], dtype=np.float64)
    force = np.zeros(nb, dtype=np.complex128)
    nwall = np.zeros(nb, dtype=np.int32)
    refpt = np.zeros(nb, dtype=np.complex128)
    rmom = np.zeros(nb, dtype=np.float64)
    wall = np.zeros([nw, nb], dtype=np.complex128)
    zcr = np.zeros([nw, nb], dtype=np.complex128)

    for j in range(1, nb + 1):
        nwall[j - 1] = nw
        for i in range(1, nw + 1):
            t1 = ((f7 * t2) % 1.0)
            t2 = ((f7 * t1) % 1.0)
            wall[i - 1, j - 1] = t1 + 1j * t2
            t1 = ((f7 * t2) % 1.0)
            t2 = ((f7 * t1) % 1.0)
            zcr[i - 1, j - 1] = t1 + 1j * t2
            dpds[i - 1, j - 1] = 0.0

    rmatrx = np.zeros([nw * nb, nw * nb], dtype=np.float64)

    for j in range(1, nw * nb + 1):
        rmatrx[j - 1, j - 1] = 1.0
        for i in range(1, j):
            t2 = ((f7 * t2) % 1.0)
            rmatrx[i - 1, j - 1] = 0.001 * t2
            rmatrx[j - 1, i - 1] = 0.001 * t2

    gamma2 = np.zeros(nvm, dtype=np.float64)
    z = np.zeros(nvm, dtype=np.complex128)

    for i in range(1, nvm + 1):
        t1 = ((f7 * t2) % 1.0)
        t2 = ((f7 * t1) % 1.0)
        z[i - 1] = t1 + 1j * t2
        t2 = ((f7 * t2) % 1.0)
        gamma2[i - 1] = t2
#
#  Timing.
#
    tm = clock()

    for i in range(0, it):
        rhs = emit(nb, nvm, nw, dpds, force, gamma2, nwall, refpt, rmatrx,
                   rmom, wall, z, zcr)

    tm = clock() - tm
#
#  Results.
#
    er = abs((rhs[18] - ans) / ans)
    fp = it * (56 * nv + nb * nw * (97 + 44 * nv + 2 * nb * nw))
    rt = 1.0E-06 * fp / tm
#
#  Terminate.
#
    return er, fp, tm, rt


if (__name__ == '__main__'):
    import platform
    from timestamp import timestamp
    timestamp()
    er, fp, tm, rt = emit_test()
    print('')
    print('EMIT:')
    print('  Python version: %s' % (platform.python_version()))
    print('')
    print(' Program          Error         FP Ops     Seconds      MFLOPS')
    print('')
    print(' EMIT     %13.4e  %13.4e  %10.4e  %10.2e' % (er, fp, tm, rt))
    print('')
    print('EMIT:')
    print('  Normal end of execution.')
    timestamp()
