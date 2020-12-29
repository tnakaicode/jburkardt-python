import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# minimize
#     F = x[1]^2 + 4x[2]^2 -32x[2] + 64

# subject to:
#      x[1] + x[2] <= 7
#     -x[1] + 2x[2] <= 4
#      x[1] >= 0
#      x[2] >= 0
#      x[2] <= 4

# in matrix notation:
#     F = (1/2)*x.T*H*x + c*x + c0

# subject to:
#     Ax <= b

# where:
#     H = [[2, 0],
#          [0, 8]]

#     c = [0, -32]

#     c0 = 64

#     A = [[ 1, 1],
#          [-1, 2],
#          [-1, 0],
#          [0, -1],
#          [0,  1]]

#     b = [7,4,0,0,4]

# H = np.array([[2., 0.],
#               [0., 8.]])
#
# c = np.array([0, -32])
#
# c0 = 64
#
# A = np.array([[ 1., 1.],
#               [-1., 2.],
#               [-1., 0.],
#               [0., -1.],
#               [0.,  1.]])
#
# b = np.array([7., 4., 0., 0., 4.])
#
# x0 = np.random.randn(2)


def solve_qp(H, f, A, b):
    
    # https://stackoverflow.com/questions/17009774/quadratic-program-qp-solver-that-only-depends-on-numpy-scipy

    def loss(x, sign=1.):
        return sign * (0.5 * np.dot(x, np.dot(H, x)))

    def jac(x, sign=1.):
        return sign * (np.dot(x, H))

    cons = {'type': 'ineq',
            'fun': lambda x: b - np.dot(A.T, x),
            'jac': lambda x: -A}

    opt = {'disp': False}
    siz = f.shape[0]

    x0 = np.random.randn(siz)
    res_cons = optimize.minimize(
        loss, x0, jac=jac, constraints=cons, method='SLSQP', options=opt)
    res_uncons = optimize.minimize(
        loss, x0, jac=jac, method='SLSQP', options=opt)

    print('\nConstrained:')
    print(res_cons)

    print('\nUnconstrained:')
    print(res_uncons)

    x1, x2 = res_cons['x']
    f = res_cons['fun']

    x1_unc, x2_unc = res_uncons['x']
    f_unc = res_uncons['fun']

    # plotting
    #xgrid = np.mgrid[-2:4:0.1, 1.5:5.5:0.1]
    #xvec = xgrid.reshape(2, -1).T
    #F = np.vstack([loss(xi) for xi in xvec]).reshape(xgrid.shape[1:])
    #
    #ax = plt.axes(projection='3d')
    # ax.hold(True)
    # ax.plot_surface(xgrid[0], xgrid[1], F, rstride=1, cstride=1,
    #                cmap=plt.cm.jet, shade=True, alpha=0.9, linewidth=0)
    #ax.plot3D([x1], [x2], [f], 'og', mec='w', label='Constrained minimum')
    # ax.plot3D([x1_unc], [x2_unc], [f_unc], 'oy', mec='w',
    #          label='Unconstrained minimum')
    #ax.legend(fancybox=True, numpoints=1)
    # ax.set_xlabel('x1')
    # ax.set_ylabel('x2')
    # ax.set_zlabel('F')
    return res_cons
